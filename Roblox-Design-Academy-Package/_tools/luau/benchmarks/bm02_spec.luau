--!strict
-- BM-02 spec. Runs the same tests against the buggy and the fixed module.
-- One test per planted defect (D1..D5), each on fresh states so one defect cannot mask another,
-- plus controls that both versions must pass. From _tools/luau:  luau benchmarks/bm02_spec.luau
-- (v1 of this spec reused one state across sub-cases; the mutation defect D5 then masked D3. See BM-02.)
local T = require("../tests/TestKit")
local H = 3600

local function suite(label: string, M: any)
	local function claimedAt(t: number)
		local _, _, s = M.claim(M.new(), t)
		return s
	end
	T.describe("BM-02 DailyReward (" .. label .. ")", function()
		T.it("control: refuses a claim inside the cooldown", function()
			T.falsy((M.claim(claimedAt(0), 19 * H)))
		end)
		T.it("control: refuses a clock earlier than the last claim", function()
			T.falsy((M.claim(claimedAt(100 * H), 50 * H)))
		end)
		T.it("control: streak continues just inside the window", function()
			local _, _, s = M.claim(claimedAt(0), 48 * H - 1)
			T.eq(s.streak, 2)
		end)
		T.it("D1a: refuses NaN time", function()
			T.falsy((M.claim(claimedAt(100 * H), 0 / 0)))
		end)
		T.it("D1b: refuses infinite time", function()
			T.falsy((M.claim(claimedAt(100 * H), math.huge)))
		end)
		T.it("D2: streak resets at exactly STREAK_WINDOW", function()
			local _, _, s = M.claim(claimedAt(0), 48 * H)
			T.eq(s.streak, 1)
		end)
		T.it("D3: first claim pays BASE (reward uses the new streak)", function()
			local ok, reward = M.claim(M.new(), 1000)
			T.truthy(ok); T.eq(reward, 50)
		end)
		T.it("D4: reward is capped at MAX_STREAK", function()
			local s = M.new()
			local reward = 0
			for day = 0, 9 do
				local _, r, ns = M.claim(s, day * 24 * H)
				s = ns; reward = r
			end
			T.eq(s.streak, 10); T.eq(reward, 50 * 7)
		end)
		T.it("D5: does not modify the state it is given", function()
			local s0 = M.new()
			M.claim(s0, 0)
			T.eq(s0.streak, 0); T.eq(s0.lastClaim, nil)
		end)
	end)
end

suite("buggy", require("./DailyReward_buggy"))
suite("fixed", require("./DailyReward_fixed"))
T.finish()
