# Validation of the Claude edition

Version: **0.1.1 preview**, prepared on 2026-10-18 from the Codex 0.1.0 edition. Release 0.1.0 is unchanged; the 0.1.1 changes are listed below. Recorded fingerprints and tool versions are in `tests/claude-recorded-results.json`.

## What changed from Codex

Every shared reference file, the archived pool, the current pool and the Python draw helper are byte-identical to the Codex edition; `python scripts/check_package.py --edition claude` enforces this. Three files differ:

- `SKILL.md` has a description of 192 characters, `license` and `compatibility` fields, a row pointing coordinators to the host guide, the helper's `${CLAUDE_SKILL_DIR}` path, and a Claude Code question tool in place of the Codex one. Anthropic's sources disagree on the description limit: one Help Center page says 200 characters, the skill-authoring docs say 1,024. The description stays under 200 to satisfy both.
- `references/claude-hosts.md` maps each duty onto Claude Code and Cowork, chat, and API hosts, with fallbacks.
- `scripts/draw_perspectives.mjs` is a Node.js fallback for hosts without Python.

## Changes in 0.1.1

- The host guide names Cowork, which runs the same agent loop as Claude Code, and gives the chat sandbox path for the draw helper.
- `SKILL.md` gives the helper's full path as `${CLAUDE_SKILL_DIR}/scripts/draw_perspectives.py`. Anthropic documents that Claude Code and Cowork fill this in when the skill loads; the forward-use run had found helper paths awkward to resolve.
- The plugin archive is now `agent-medici-innovation-claude-plugin-v0.1.1.zip`, because it also installs in Claude.ai and Cowork through **Customize > Plugins > Add > Upload plugin**. It holds exactly one `.claude-plugin/plugin.json`, which that upload requires.
- Every structural check below was rerun on 0.1.1, from source and after extraction. The shared method files and both draw helpers are unchanged, so the helper equivalence results still apply. No new forward-use run took place.

## Structural validation

- Anthropic's skill-creator `quick_validate.py`, unmodified, returned **"Skill is valid!"** for the source folder and for the folder extracted from the release ZIP.
- Claude Code 2.1.299 `claude plugin validate --strict` passed for the plugin manifest, the repository marketplace and the local marketplace inside the plugin ZIP, both in the source tree and after extraction.
- `claude plugin details`, with the plugin loaded from disk, lists one skill, `medici-exploration`. It estimates about 60 tokens always on and about 3,300 tokens each time the skill is invoked.
- A headless Claude Code session started with `--plugin-dir` listed the skill as `agent-medici-innovation:medici-exploration`. That session could not go further because the bundled command-line client was not signed in.
- The Node and Python helpers produced byte-identical receipts for 301 replays: random seeds, every count from 3 to 15, non-ASCII perspective text and the archived v0.1 pool. Their exit codes also matched on eight invalid inputs. Both reproduce the recorded replay in `tests/draw-replay.json` from the source tree and from each extracted ZIP.
- Both archives passed the packager's byte-for-byte content check.

## Forward-use run in Claude Code

One bounded run took place on 2026-10-18 in Claude Code 2.1.299 on Windows 11. The headless client could not sign in, so a general-purpose subagent acted as coordinator and followed the skill from its files. The Skill tool's own loading step was therefore not part of this run; discovery was checked separately above. The request was a fictional closed hypothetical: a five-person team's weekly planning meeting runs over time, the meeting stays weekly with everyone attending, and the ceiling was small, with one exchange and a single panel. No user was reachable. `AskUserQuestion` is removed from subagents, so the run also exercised the text fallback for questions.

Observed:

- The Python helper drew use-context, economics-resources and power-governance from pool v0.2. The coordinator checked the pool fingerprint and passed the receipt on unedited.
- Six seats ran: a separate facilitator, an evidence researcher and three contributors, each its own subagent, with practice investigation combined with coordination and recorded. The contributors started concurrently. None received the coordinator's preference, peers' proposals or the solution landscape before committing.
- One routed exchange used `SendMessage`; the receiving contributor transformed one step and combined it with another contributor's route. The facilitator kept an eight-item objection ledger with dispositions and checked the synthesis once; all seven of its correction groups were applied.
- All three authored notes appeared verbatim with attribution, including one that disagreed with the recommendation. Five submitted questions and the closing next-action choice appeared as numbered text choices ending in Other, all marked optional and pending. No answers were invented.
- The delivery disclosed the absence of retrieval and question controls, the six-seat composition, procedural-only separation and each process departure.

Departures, all recorded in the delivery: contributors started before the facilitator saw the receipt, to fit an eight-call cap. Only one contributor confronted the researcher's landscape. Contributors were not offered the synthesis to append corrections, and the researcher worked from the packet before intake had checked it. The run also hit tool friction: `SendMessage` had to be loaded as a deferred tool, replies arrived asynchronously, one report arrived twice, and one contributor said it had messaged an agent the coordinator never started.

These findings changed `references/claude-hosts.md` before release. It now tells roles to report only to the coordinator, explains how to continue a role and treat duplicate reports, asks for the facilitator's packet check before dispatch, and says which facilitator turns to merge under a small ceiling. It also gives the Windows interpreter order with an absolute helper path, and covers the researcher's scope in a closed hypothetical. The revised guide has not been re-run. The coordinator and facilitator alone used about 263,000 tokens; the other subagents were not totaled.

## Account install test

On 2026-10-18 the plugin was installed on a Max account through claude.ai in Chrome, following the README:

- **Customize > Plugins > Add** offered Add marketplace, Upload plugin, Create a plugin and Create with Claude. **Add marketplace** then asked for a source: Browse Anthropic sources, or **Add from repository**. The repository field accepted `ThatCompany/agent-medici-innovation-skill`; it also lists repositories from a connected GitHub account. The dialog warns that Anthropic does not verify marketplace plugins, and **Sync automatically** was on by default.
- After **Sync**, the list showed **Agent medici innovation**, "by agent-medici-innovation-skill". **Add** installed it as version 0.1.1 with one skill and 13 files, marked "Synced from a repository · read-only".
- In a new chat, typing `/medici` listed **medici-exploration** with its description, labeled "Agent medici innovation plugin". Nothing was sent, so the skill did not run.
- The desktop app downloaded the plugin to its local plugin store within minutes. It was listed there as `agent-medici-innovation`, from the `agent-medici-innovation-skill` marketplace, next to the account's other plugins. All 10 skill files matched the v0.1.1 fingerprints. The copy already carried a README change merged after the install, so **Sync automatically** picked it up.
- Cowork itself was not opened. It loads account plugins from that store when a task starts, through the same Claude Code loader that loads the account's other plugins in desktop sessions. The downloaded copy passed `claude plugin validate --strict` and loaded as one skill. It has no component Cowork refuses or ignores (no `bin/`, hooks, agents, commands, MCP or LSP servers) and is 84 KB in 13 files. Its Python draw helper reproduced the recorded replay and made a fresh draw in a Linux Python 3.12 container with no network. Loading in Cowork is therefore inferred, not observed.
- The Claude Code terminal sync into `~/.claude/plugins/synced/` had not run yet; it runs when a terminal session starts.

## Limits

Installing through the desktop app, Upload plugin or organization settings was not exercised; those paths, the description limits and the frontmatter key list come from Anthropic's documentation, checked on 2026-10-18. The skill has not run in chat, Cowork or the API, and `${CLAUDE_SKILL_DIR}` substitution was not observed directly. No real users took part. Creative outcomes and latency were not measured, and token use was only partly counted. As with the Codex edition, separate contexts provide procedural separation, not technical isolation, and a demonstration is not evidence that a panel beats a capable single agent.
