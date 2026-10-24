--!strict
--[[
	PlayerData: versioned save schema with defaults, reconcile, migration and size guard.

	Roblox data store guidance this implements (create.roblox.com/docs/cloud-services/data-stores/best-practices):
	  - one key per player (e.g. "User_" .. userId) holding one table, under the 4 MB per-key limit
	  - buffer in memory, save periodically / on leave / on shutdown (the saving loop lives elsewhere)
	  - prefer UpdateAsync when a write depends on the current value
	This module is pure: it turns whatever came out of GetAsync/UpdateAsync into a valid current-version
	table, and back. That is the part that silently corrupts saves when it is wrong, so it is tested.
]]

local PlayerData = {}

PlayerData.VERSION = 3

export type Data = {
	version: number,
	coins: number,
	level: number,
	inventory: { [string]: number },
	settings: { music: number, sfx: number },
	stats: { playSeconds: number, sessions: number },
	claimedRewards: { [string]: boolean },
}

local function defaults(): Data
	return {
		version = PlayerData.VERSION,
		coins = 0,
		level = 1,
		inventory = {},
		settings = { music = 0.6, sfx = 0.8 },
		stats = { playSeconds = 0, sessions = 0 },
		claimedRewards = {},
	}
end
PlayerData.defaults = defaults

-- Migrations: each step upgrades from version N to N+1. Never edit an old step after release;
-- add a new one. Saves without a version are treated as version 1.
local migrations: { [number]: (any) -> any } = {
	[1] = function(d)
		-- v1 stored `gold`; v2 renamed it to `coins`
		d.coins = d.coins or d.gold
		d.gold = nil
		d.version = 2
		return d
	end,
	[2] = function(d)
		-- v2 had a flat `musicVolume`; v3 groups settings and adds stats
		d.settings = d.settings or { music = d.musicVolume }
		d.musicVolume = nil
		d.version = 3
		return d
	end,
}

-- Fill missing keys from defaults, recursively; drop values whose type does not match the default.
local function reconcile(value: any, template: any): any
	if type(template) ~= "table" then
		if type(value) == type(template) and not (type(value) == "number" and value ~= value) then
			return value
		end
		return template
	end
	if type(value) ~= "table" then
		return table.clone(template)
	end
	local out = {}
	local isMap = next(template) == nil -- empty template table = free-form map (inventory, claimed)
	if isMap then
		for k, v in value do
			if type(k) == "string" and (type(v) == "number" or type(v) == "boolean") and v == v then
				out[k] = v
			end
		end
		return out
	end
	for k, t in template do
		out[k] = reconcile(value[k], t)
	end
	return out
end

-- Turn anything loaded from the store (nil for new players, old versions, damaged tables) into Data.
function PlayerData.fromSave(raw: unknown): (Data, { string })
	local notes = {}
	if raw == nil then
		table.insert(notes, "new player")
		return defaults(), notes
	end
	if type(raw) ~= "table" then
		table.insert(notes, "save was not a table; reset to defaults")
		return defaults(), notes
	end
	local d = table.clone(raw :: any)
	local v = if type(d.version) == "number" then d.version else 1
	if v > PlayerData.VERSION then
		-- Saved by a NEWER server version (rolling update). Do not downgrade-overwrite it.
		error("save version " .. v .. " is newer than this server (" .. PlayerData.VERSION .. "); refuse to load")
	end
	while v < PlayerData.VERSION do
		d = migrations[v](d)
		table.insert(notes, "migrated v" .. v .. " -> v" .. d.version)
		v = d.version
	end
	return reconcile(d, defaults()) :: Data, notes
end

-- Approximate serialized size, to catch runaway growth long before the 4 MB per-key limit.
function PlayerData.estimateBytes(value: any): number
	local t = type(value)
	if t == "string" then
		return #value + 2
	elseif t == "number" then
		return 12
	elseif t == "boolean" then
		return 5
	elseif t == "table" then
		local n = 2
		for k, v in value do
			n += PlayerData.estimateBytes(k) + PlayerData.estimateBytes(v) + 2
		end
		return n
	end
	return 4
end

PlayerData.LIMIT_BYTES = 4 * 1024 * 1024
PlayerData.WARN_BYTES = 256 * 1024 -- house rule: investigate long before the hard limit

function PlayerData.toSave(d: Data): (Data, string?)
	local bytes = PlayerData.estimateBytes(d)
	if bytes > PlayerData.LIMIT_BYTES then
		error("player data exceeds the 4 MB data store key limit (" .. bytes .. " bytes estimated)")
	end
	return d, if bytes > PlayerData.WARN_BYTES then "player data is large: " .. bytes .. " bytes" else nil
end

function PlayerData.key(userId: number): string
	return "User_" .. tostring(userId) -- static pattern, never display names (they change)
end

return PlayerData
