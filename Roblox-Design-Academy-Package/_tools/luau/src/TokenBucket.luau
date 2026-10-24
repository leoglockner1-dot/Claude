--!strict
--[[
	TokenBucket: per-player rate limiter for anything a client can trigger on the server
	(remotes, Touched, ProximityPrompt, ClickDetector).

	Based on the token-bucket example in Roblox "Securing the client-server boundary > Rate limiting".
	Differences from the docs version (deliberate, for testability and hygiene):
	  - the clock is injected (`now`), so tests can control time; in Roblox pass `time` or `os.clock`
	  - `forget(userId)` for Players.PlayerRemoving (the docs call this out to avoid leaks)
	  - `cost` lets expensive actions spend more than one token
]]

export type TokenBucket = {
	capacity: number,
	refillPerSecond: number,
	now: () -> number,
	buckets: { [number]: { tokens: number, last: number } },
	allow: (self: TokenBucket, userId: number, cost: number?) -> boolean,
	forget: (self: TokenBucket, userId: number) -> (),
}

local TokenBucket = {}
TokenBucket.__index = TokenBucket

-- capacity = burst size; windowSeconds = time to refill a full bucket.
-- new(5, 10): bursts of 5, then one action every 2 s on average.
function TokenBucket.new(capacity: number, windowSeconds: number, now: (() -> number)?): TokenBucket
	assert(capacity >= 1, "capacity must be >= 1")
	assert(windowSeconds > 0, "windowSeconds must be > 0")
	local self = {
		capacity = capacity,
		refillPerSecond = capacity / windowSeconds,
		now = now or os.clock,
		buckets = {},
	}
	return (setmetatable(self, TokenBucket) :: any) :: TokenBucket
end

function TokenBucket.allow(self: TokenBucket, userId: number, cost: number?): boolean
	local c = cost or 1
	local t = self.now()
	local b = self.buckets[userId]
	if not b then
		b = { tokens = self.capacity, last = t }
		self.buckets[userId] = b
	else
		local elapsed = t - b.last
		if elapsed > 0 then
			b.tokens = math.min(self.capacity, b.tokens + elapsed * self.refillPerSecond)
			b.last = t
		end
	end
	if b.tokens >= c then
		b.tokens -= c
		return true
	end
	return false
end

function TokenBucket.forget(self: TokenBucket, userId: number)
	self.buckets[userId] = nil
end

return TokenBucket
