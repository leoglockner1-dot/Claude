--!strict
-- Minimal test harness for running academy modules in the standalone Luau CLI.
-- Usage: local T = require("./TestKit"); T.describe("Thing", function() T.it("works", function() T.eq(1, 1) end) end); T.finish()

local TestKit = {}

local passed, failed = 0, 0
local failures: { string } = {}
local prefix = ""

function TestKit.describe(name: string, body: () -> ())
	local old = prefix
	prefix = if old == "" then name else old .. " > " .. name
	body()
	prefix = old
end

function TestKit.it(name: string, body: () -> ())
	local ok, err = pcall(body)
	if ok then
		passed += 1
	else
		failed += 1
		table.insert(failures, prefix .. " > " .. name .. "\n    " .. tostring(err))
	end
end

local function show(v: any): string
	if type(v) == "string" then
		return string.format("%q", v)
	end
	return tostring(v)
end

function TestKit.eq(actual: any, expected: any, msg: string?)
	if actual ~= expected then
		error((msg or "values differ") .. ": expected " .. show(expected) .. ", got " .. show(actual), 2)
	end
end

function TestKit.near(actual: number, expected: number, tol: number, msg: string?)
	if math.abs(actual - expected) > tol then
		error((msg or "not within tolerance") .. ": expected " .. expected .. " +/- " .. tol .. ", got " .. actual, 2)
	end
end

function TestKit.truthy(v: any, msg: string?)
	if not v then
		error(msg or ("expected truthy, got " .. show(v)), 2)
	end
end

function TestKit.falsy(v: any, msg: string?)
	if v then
		error(msg or ("expected falsy, got " .. show(v)), 2)
	end
end

function TestKit.throws(fn: () -> (), pattern: string?)
	local ok, err = pcall(fn)
	if ok then
		error("expected an error", 2)
	end
	if pattern and not string.find(tostring(err), pattern) then
		error("error " .. show(tostring(err)) .. " does not match " .. show(pattern), 2)
	end
end

function TestKit.finish(): (number, number)
	for _, f in failures do
		print("FAIL " .. f)
	end
	print(string.format("%d passed, %d failed", passed, failed))
	return passed, failed
end

function TestKit.counts(): (number, number)
	return passed, failed
end

return TestKit
