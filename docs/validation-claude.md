# Validation of the Claude edition

Version: **0.1.0 preview**, prepared on 2026-10-18 from the Codex 0.1.0 edition. Recorded fingerprints and tool versions are in `tests/claude-recorded-results.json`.

## What changed from Codex

Every shared reference file, the archived pool, the current pool and the Python draw helper are byte-identical to the Codex edition; `python scripts/check_package.py --edition claude` enforces this. Three files differ:

- `SKILL.md` has a description of 192 characters (Claude.ai's help pages state a 200-character limit), `license` and `compatibility` fields, a row pointing coordinators to the host guide, and a Claude Code question tool in place of the Codex one.
- `references/claude-hosts.md` maps each duty onto Claude Code, Claude.ai chat and API hosts, with fallbacks.
- `scripts/draw_perspectives.mjs` is a Node.js fallback for hosts without Python.

## Structural validation

- Anthropic's skill-creator `quick_validate.py`, unmodified, returned **"Skill is valid!"** for the source folder and for the folder extracted from the release ZIP.
- Claude Code 2.1.299 `claude plugin validate --strict` passed for the plugin manifest, the repository marketplace and the local marketplace inside the plugin ZIP, both in the source tree and after extraction.
- `claude plugin details`, with the plugin loaded from disk, lists one skill, `medici-exploration`. It estimates about 60 tokens always on and about 3,200 tokens each time the skill is invoked.
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

## Limits

Claude.ai upload and use were not exercised; the upload path, the 200-character limit and the frontmatter key list come from Anthropic's documentation. No run in Claude.ai chat, Claude Desktop or the API took place. No real users took part. Creative outcomes and latency were not measured, and token use was only partly counted. As with the Codex edition, separate contexts provide procedural separation, not technical isolation, and a demonstration is not evidence that a panel beats a capable single agent.
