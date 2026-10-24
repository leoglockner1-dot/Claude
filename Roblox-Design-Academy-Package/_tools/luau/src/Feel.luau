--!strict
--[[
	Feel: small math helpers for game feel - easing curves, a critically damped spring, and
	number formatting for HUDs. Pure functions; safe on client or server.

	Easing formulas are the standard Penner-style curves (t in 0..1). Roblox's TweenService uses
	the same names (Enum.EasingStyle Quad, Cubic, Back, Bounce, Elastic, Sine, Exponential...), but its
	exact constants were not verified here; use TweenService for Instance properties and these only
	where you animate values yourself (springs, custom cameras, number count-ups).
]]

local Feel = {}

local ease: { [string]: (number) -> number } = {
	linear = function(t: number): number
		return t
	end,
	quadOut = function(t: number): number
		return 1 - (1 - t) * (1 - t)
	end,
	cubicOut = function(t: number): number
		return 1 - (1 - t) ^ 3
	end,
	cubicInOut = function(t: number): number
		return if t < 0.5 then 4 * t ^ 3 else 1 - (-2 * t + 2) ^ 3 / 2
	end,
	backOut = function(t: number): number -- overshoots ~10% then settles: "pop" for buttons/rewards
		local c1 = 1.70158
		local c3 = c1 + 1
		return 1 + c3 * (t - 1) ^ 3 + c1 * (t - 1) ^ 2
	end,
	elasticOut = function(t: number): number
		if t == 0 or t == 1 then
			return t
		end
		return 2 ^ (-10 * t) * math.sin((t * 10 - 0.75) * (2 * math.pi) / 3) + 1
	end,
}
Feel.ease = ease

-- Critically damped spring (no overshoot, fastest settle). `omega` ~ responsiveness (rad/s):
-- 10-20 snappy UI, 4-8 soft camera. Stable for any dt (closed-form step).
function Feel.springStep(x: number, v: number, target: number, omega: number, dt: number): (number, number)
	local exp = math.exp(-omega * dt)
	local delta = x - target
	local temp = (v + omega * delta) * dt
	local newX = target + (delta + temp) * exp
	local newV = (v - omega * temp) * exp
	return newX, newV
end

-- 1234 -> "1.23K", 9_870_000 -> "9.87M". Three significant digits keep HUD width stable.
local suffixes = { "", "K", "M", "B", "T", "Qa", "Qi" }
function Feel.abbreviate(n: number): string
	if n ~= n then
		return "NaN"
	end
	local sign = if n < 0 then "-" else ""
	n = math.abs(n)
	if n < 1000 then
		return sign .. tostring(math.floor(n))
	end
	local i = 1
	while n >= 1000 and i < #suffixes do
		n /= 1000
		i += 1
	end
	-- Truncate (never round up: "1.00M" for 999,999 would lie), but add a tiny epsilon first:
	-- 9,870,000 / 1e6 is 9.869999... in binary floating point and would truncate to "9.86M".
	local e = 1e-9
	local s = if n >= 100 then string.format("%d", math.floor(n + e))
		elseif n >= 10 then string.format("%.1f", math.floor(n * 10 + e) / 10)
		else string.format("%.2f", math.floor(n * 100 + e) / 100)
	return sign .. s .. suffixes[i]
end

-- 1234567 -> "1,234,567" (for shop prices where exact values matter)
function Feel.commas(n: number): string
	local s = tostring(math.floor(math.abs(n)))
	local out = s:reverse():gsub("(%d%d%d)", "%1,"):reverse()
	if out:sub(1, 1) == "," then
		out = out:sub(2)
	end
	return (if n < 0 then "-" else "") .. out
end

-- 75 -> "1:15"
function Feel.clock(seconds: number): string
	local s = math.max(0, math.floor(seconds))
	return string.format("%d:%02d", s // 60, s % 60)
end

return Feel
