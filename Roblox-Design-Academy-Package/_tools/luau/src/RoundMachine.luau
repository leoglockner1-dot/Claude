--!strict
--[[
	RoundMachine: the lobby -> intermission -> playing -> results loop most round-based games need.

	Driven by step(dt) so it is deterministic and testable; in Roblox call it from a server
	RunService.Heartbeat connection (or a task.wait loop). It never touches Instances: subscribe to
	onEnter to update UI, teleport players, spawn the map, etc.

	Design rules it encodes (see 13-Onboarding-and-Multiplayer/Multiplayer/Low-Population-Design):
	  - a round needs minPlayers; if players drop below it mid-round, the round ends (no zombie rounds)
	  - every state has a time limit, so a stuck condition can never freeze the server loop
]]

export type State = "Waiting" | "Intermission" | "Playing" | "Results"

export type Config = {
	minPlayers: number,
	intermission: number,
	roundLength: number,
	results: number,
}

export type Machine = {
	state: State,
	timeLeft: number,
	players: number,
	round: number,
	config: Config,
	winner: string?,
	listeners: { (State, Machine) -> () },
}

local RoundMachine = {}

local function enter(m: Machine, s: State)
	m.state = s
	if s == "Intermission" then
		m.timeLeft = m.config.intermission
	elseif s == "Playing" then
		m.timeLeft = m.config.roundLength
		m.round += 1
		m.winner = nil
	elseif s == "Results" then
		m.timeLeft = m.config.results
	else
		m.timeLeft = math.huge
	end
	for _, fn in m.listeners do
		fn(s, m)
	end
end

function RoundMachine.new(config: Config): Machine
	return { state = "Waiting", timeLeft = math.huge, players = 0, round = 0, config = config, winner = nil, listeners = {} }
end

function RoundMachine.onEnter(m: Machine, fn: (State, Machine) -> ())
	table.insert(m.listeners, fn)
end

function RoundMachine.setPlayers(m: Machine, n: number)
	m.players = n
	if m.state == "Waiting" and n >= m.config.minPlayers then
		enter(m, "Intermission")
	elseif (m.state == "Intermission" or m.state == "Playing") and n < m.config.minPlayers then
		m.winner = nil
		enter(m, if m.state == "Playing" then "Results" else "Waiting")
	end
end

-- Call when the win condition is met (last player standing, goal reached...).
function RoundMachine.finish(m: Machine, winner: string?)
	if m.state == "Playing" then
		enter(m, "Results")
		m.winner = winner
	end
end

function RoundMachine.step(m: Machine, dt: number)
	if m.timeLeft == math.huge then
		return
	end
	m.timeLeft -= dt
	if m.timeLeft > 0 then
		return
	end
	if m.state == "Intermission" then
		enter(m, "Playing")
	elseif m.state == "Playing" then
		enter(m, "Results") -- time ran out: no winner unless the game decides one in onEnter
	elseif m.state == "Results" then
		enter(m, if m.players >= m.config.minPlayers then "Intermission" else "Waiting")
	end
end

return RoundMachine
