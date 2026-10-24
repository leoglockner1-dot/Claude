--!strict
-- BM-02 worked answer. Each fix is tagged with the defect it removes (see BM-02 note).
local DailyReward = {}

DailyReward.COOLDOWN = 20 * 3600
DailyReward.STREAK_WINDOW = 48 * 3600
DailyReward.BASE = 50
DailyReward.MAX_STREAK = 7

export type State = { lastClaim: number?, streak: number }

function DailyReward.new(): State
	return { lastClaim = nil, streak = 0 }
end

local function validTime(t: number): boolean
	return t == t and t ~= math.huge and t ~= -math.huge -- D1: NaN/inf refused (NaN fails every comparison)
end

function DailyReward.claim(state: State, now: number): (boolean, number, State)
	if not validTime(now) then
		return false, 0, state
	end
	local last = state.lastClaim
	if last ~= nil then
		local elapsed = now - last
		if elapsed < 0 then
			return false, 0, state -- not a planted defect: the cooldown check already refuses this; kept explicit for clarity
		end
		if elapsed < DailyReward.COOLDOWN then
			return false, 0, state
		end
	end
	-- D2: "less than STREAK_WINDOW" continues, so exactly STREAK_WINDOW resets (>= not >)
	local continues = last ~= nil and (now - last) < DailyReward.STREAK_WINDOW
	local streak = if continues then state.streak + 1 else 1
	-- D3: reward uses the new streak (was the old one, so the first claim paid 0)
	-- D4: capped at MAX_STREAK
	local reward = DailyReward.BASE * math.min(streak, DailyReward.MAX_STREAK)
	-- D5: return a new table instead of mutating the caller's state
	return true, reward, { lastClaim = now, streak = streak }
end

return DailyReward
