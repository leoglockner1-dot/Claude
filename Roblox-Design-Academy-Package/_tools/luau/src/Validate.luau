--!strict
--[[
	Validate: server-side checks for values that arrive from clients (RemoteEvent/RemoteFunction args).

	Follows Roblox "Securing the client-server boundary" (create.roblox.com/docs/scripting/security/client-server-boundary):
	  - type and structure validation (exact shape, bounded size, no surprise tables)
	  - value validation (range, integer, finite: NaN and +/-inf are type "number" but break comparisons)
	Every checker returns (ok: boolean, err: string?) so handlers can early-return.

	In Roblox, also check typeof(x) == "Instance" plus :IsA()/:IsDescendantOf() for instance arguments.
	This module stays engine-free so it runs in the standalone Luau CLI tests.
]]

local Validate = {}


export type NumberOpts = { min: number?, max: number?, integer: boolean? }
export type StrOpts = { maxLen: number?, minLen: number?, pattern: string? }

function Validate.number(v: unknown, opts: NumberOpts?): (boolean, string?)
	if type(v) ~= "number" then
		return false, "expected number"
	end
	-- math.isfinite exists in Roblox's Luau; this form also works in the standalone CLI.
	if v ~= v or v == math.huge or v == -math.huge then
		return false, "number must be finite"
	end
	local o: NumberOpts = opts or {}
	local min, max = o.min, o.max
	if o.integer and v % 1 ~= 0 then
		return false, "expected integer"
	end
	if min and v < min then
		return false, "below minimum " .. min
	end
	if max and v > max then
		return false, "above maximum " .. max
	end
	return true, nil
end

function Validate.str(v: unknown, opts: StrOpts?): (boolean, string?)
	if type(v) ~= "string" then
		return false, "expected string"
	end
	local o: StrOpts = opts or {}
	local maxLen = o.maxLen or 200 -- default cap: unbounded strings are a server-cost attack
	if #v > maxLen then
		return false, "string too long"
	end
	local minLen = o.minLen
	if minLen and #v < minLen then
		return false, "string too short"
	end
	if utf8.len(v) == nil then
		return false, "invalid utf8"
	end
	local pattern = o.pattern
	if pattern and not string.match(v, pattern) then
		return false, "string format rejected"
	end
	return true, nil
end

function Validate.oneOf<T>(v: unknown, allowed: { T }): (boolean, string?)
	for _, a in allowed do
		if v == a then
			return true, nil
		end
	end
	return false, "value not allowed"
end

function Validate.bool(v: unknown): (boolean, string?)
	if type(v) ~= "boolean" then
		return false, "expected boolean"
	end
	return true, nil
end

export type Checker = (unknown) -> (boolean, string?)

-- shape: exact table structure. Rejects non-tables, metatables, missing keys and EXTRA keys,
-- so a client cannot smuggle fields ("Price = 0") into a payload the server later trusts.
function Validate.shape(v: unknown, schema: { [string]: Checker }, maxKeys: number?): (boolean, string?)
	if type(v) ~= "table" then
		return false, "expected table"
	end
	if getmetatable(v :: any) ~= nil then
		return false, "table must not have a metatable"
	end
	local count = 0
	for k in v :: any do
		count += 1
		if count > (maxKeys or 32) then
			return false, "too many keys"
		end
		if type(k) ~= "string" or schema[k] == nil then
			return false, "unexpected key " .. tostring(k)
		end
	end
	for key, check in schema do
		local ok, err = check((v :: any)[key])
		if not ok then
			return false, key .. ": " .. (err or "invalid")
		end
	end
	return true, nil
end

-- array: list of bounded length where every element passes `each`.
function Validate.array(v: unknown, each: Checker, maxLen: number): (boolean, string?)
	if type(v) ~= "table" or getmetatable(v :: any) ~= nil then
		return false, "expected array"
	end
	local n = 0
	for k in v :: any do
		n += 1
		if type(k) ~= "number" or k % 1 ~= 0 or k < 1 then
			return false, "array has non-index key"
		end
		if n > maxLen then
			return false, "array too long"
		end
	end
	if n ~= #(v :: any) then
		return false, "array has holes"
	end
	for i = 1, n do
		local ok, err = each((v :: any)[i])
		if not ok then
			return false, "[" .. i .. "] " .. (err or "invalid")
		end
	end
	return true, nil
end

-- Helpers that turn option tables into Checkers, for use inside shape/array schemas.
function Validate.Number(opts: NumberOpts?): Checker
	return function(v)
		return Validate.number(v, opts)
	end
end

function Validate.Str(opts: StrOpts?): Checker
	return function(v)
		return Validate.str(v, opts)
	end
end

function Validate.OneOf(allowed: { any }): Checker
	return function(v)
		return Validate.oneOf(v, allowed)
	end
end

function Validate.Optional(check: Checker): Checker
	return function(v)
		if v == nil then
			return true, nil
		end
		return check(v)
	end
end

return Validate
