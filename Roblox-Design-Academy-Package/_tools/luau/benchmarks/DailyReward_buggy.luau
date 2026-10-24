--!strict
-- BM-02 starting file: a daily-reward module with planted defects. Do not fix this file; copy it.
-- Rules (the spec in bm02_spec.luau is the source of truth):
--   * A claim is allowed when at least COOLDOWN seconds have passed since the last claim (or never claimed).
--   * The streak continues if the claim happens less than STREAK_WINDOW seconds after the last claim,
--     otherwise it resets to 1. The first claim ever is streak 1.
--   * Reward = BASE * min(streak, MAX_STREAK).
--   * `now` is the server's clock. Invalid times (NaN, infinite, earlier than the last claim) are refused.
--   * claim() never modifies the state it is given; it returns a new state.
local DailyReward = {}

DailyReward.COOLDOWN = 20 * 3600
DailyReward.STREAK_WINDOW = 48 * 3600
DailyReward.BASE = 50
DailyReward.MAX_STREAK = 7

export type State = { lastClaim: number?, streak: number }

function DailyReward.new(): State
	return { lastClaim = nil, streak = 0 }
end

function DailyReward.claim(state: State, now: number): (boolean, number, State)
	local last = state.lastClaim
	if last ~= nil and now - last < DailyReward.COOLDOWN then
		return false, 0, state
	end
	if last == nil or now - last > DailyReward.STREAK_WINDOW then
		state.streak = 0
	end
	local reward = DailyReward.BASE * state.streak
	state.streak += 1
	state.lastClaim = now
	return true, reward, state
end

return DailyReward
