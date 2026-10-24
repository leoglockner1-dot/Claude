--!strict
--[[
	Signal + Janitor: decoupled module events and leak-free cleanup.

	Signal: lets modules talk without requiring each other (Currency changed -> HUD updates). Listeners
	connected or disconnected while the signal is firing take effect from the next fire - the snapshot
	avoids the classic "skipped listener" bug when one handler disconnects another.
	Janitor: collects connections/functions so a player's or round's resources are released together
	(PlayerRemoving, round end). Leaked connections are a top cause of slow server memory growth.
	In Roblox, prefer BindableEvent only when you need cross-script communication; a Luau signal is cheaper.
]]

export type Connection = { connected: boolean, disconnect: (self: Connection) -> () }
export type Signal<T...> = {
	_handlers: { { fn: (T...) -> (), conn: Connection } },
	connect: (self: Signal<T...>, fn: (T...) -> ()) -> Connection,
	fire: (self: Signal<T...>, T...) -> (),
	count: (self: Signal<T...>) -> number,
}

local Signal = {}

function Signal.new<T...>(): Signal<T...>
	local self = { _handlers = {} } :: any
	function self.connect(s: any, fn)
		local conn: any = { connected = true }
		function conn.disconnect(c: any)
			if not c.connected then
				return
			end
			c.connected = false
			for i, h in s._handlers do
				if h.conn == c then
					table.remove(s._handlers, i)
					break
				end
			end
		end
		table.insert(s._handlers, { fn = fn, conn = conn })
		return conn
	end
	function self.fire(s: any, ...)
		local snapshot = table.clone(s._handlers)
		for _, h in snapshot do
			if h.conn.connected then
				h.fn(...)
			end
		end
	end
	function self.count(s: any)
		return #s._handlers
	end
	return self
end

export type Janitor = { _items: { any }, add: (self: Janitor, item: any) -> any, clean: (self: Janitor) -> number }

function Signal.janitor(): Janitor
	local j = { _items = {} } :: any
	function j.add(self: any, item)
		table.insert(self._items, item)
		return item
	end
	function j.clean(self: any): number
		local n = 0
		for i = #self._items, 1, -1 do -- reverse order: undo in the opposite order of setup
			local item: any = self._items[i]
			local obj: any = item -- separate local: type refinement on `item` below must not narrow this one
			if type(item) == "function" then
				(item :: () -> ())()
			elseif type(item) == "table" then
				-- Luau signal connection, RBXScriptConnection, or Instance-like object
				local fn: ((any) -> ())? = obj.disconnect or obj.Disconnect or obj.Destroy
				if fn ~= nil then
					fn(obj)
				end
			end
			self._items[i] = nil
			n += 1
		end
		return n
	end
	return j
end

return Signal
