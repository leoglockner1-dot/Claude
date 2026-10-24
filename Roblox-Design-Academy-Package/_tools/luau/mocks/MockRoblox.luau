--!strict
--[[
	MockRoblox: just enough fake engine to drive ShopServer in the CLI.
	It imitates the *contract* (a RemoteFunction handler receives the calling player first, then
	arbitrary client data), not engine behaviour like replication, yielding or latency.
	Passing these tests means the logic is right; it does not replace a Studio playtest.
]]

local MockRoblox = {}

export type Env = {
	handlers: { [string]: (any, unknown) -> (boolean, any) },
	removing: { (any) -> () },
	positions: { [number]: { x: number, y: number, z: number } },
	saved: { [string]: any },
	clockValue: number,
	deps: any,
	addPlayer: (self: Env, userId: number, pos: { x: number, y: number, z: number }) -> any,
	removePlayer: (self: Env, player: any) -> (),
	invoke: (self: Env, player: any, name: string, payload: unknown) -> (boolean, any),
}

function MockRoblox.new(): Env
	local env: any = { handlers = {}, removing = {}, positions = {}, saved = {}, clockValue = 0 }
	env.deps = {
		setInvokeHandler = function(name, fn)
			env.handlers[name] = fn
		end,
		onPlayerRemoving = function(fn)
			table.insert(env.removing, fn)
		end,
		characterPosition = function(p)
			return env.positions[p.UserId]
		end,
		shopPosition = { x = 0, y = 0, z = 0 },
		clock = function()
			return env.clockValue
		end,
		save = function(key, data)
			env.saved[key] = data
		end,
	}
	function env.addPlayer(self, userId, pos)
		self.positions[userId] = pos
		return { UserId = userId }
	end
	function env.removePlayer(self, player)
		for _, fn in self.removing do
			fn(player)
		end
		self.positions[player.UserId] = nil
	end
	function env.invoke(self, player, name, payload)
		-- Like OnServerInvoke: errors inside the handler would propagate to the client; pcall to report.
		local ok, a, b = pcall(self.handlers[name], player, payload)
		if not ok then
			return false, "server error: " .. tostring(a)
		end
		return a, b
	end
	return env
end

return MockRoblox
