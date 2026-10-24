--!strict
--[[
	Retry: call a yielding API (DataStore, MessagingService, HttpService) with capped exponential
	backoff and jitter, as Roblox's data store best practices recommend:
	  "Wrap requests in pcall() and retry transient failures with exponential backoff. Add random
	   jitter ... Cap the delay and number of attempts, and don't retry errors caused by invalid requests."

	wait and rng are injected (task.wait / math.random in Roblox) so tests run instantly.
	Remember the docs' caveat: a failed write may still have succeeded on the backend, and retries
	for one key must stay ordered - this helper does not reorder, but it cannot fix a caller that
	issues overlapping saves for the same key.
]]

export type Options = {
	attempts: number?, -- total tries, default 5
	baseDelay: number?, -- seconds, default 1
	maxDelay: number?, -- seconds, default 16
	jitter: number?, -- 0..1 fraction of the delay, default 0.3
	isRetryable: ((err: any) -> boolean)?,
	wait: ((seconds: number) -> ())?,
	rng: (() -> number)?,
}

local Retry = {}

function Retry.delays(o: Options): { number }
	local out = {}
	local base, cap = o.baseDelay or 1, o.maxDelay or 16
	for i = 1, (o.attempts or 5) - 1 do
		table.insert(out, math.min(cap, base * 2 ^ (i - 1)))
	end
	return out
end

function Retry.call(fn: () -> ...any, o: Options?): (boolean, ...any)
	local opts: Options = o or {}
	local attempts = opts.attempts or 5
	local wait = opts.wait or function(_s: number) end
	local rng = opts.rng or math.random
	local jitter = opts.jitter or 0.3
	local delays = Retry.delays(opts)
	local lastErr: any = nil
	for i = 1, attempts do
		local result = table.pack(pcall(fn))
		if result[1] then
			return true, table.unpack(result, 2, result.n)
		end
		lastErr = result[2]
		if opts.isRetryable and not opts.isRetryable(lastErr) then
			return false, lastErr
		end
		if i < attempts then
			local d = delays[i]
			wait(d * (1 - jitter + 2 * jitter * rng()))
		end
	end
	return false, lastErr
end

return Retry
