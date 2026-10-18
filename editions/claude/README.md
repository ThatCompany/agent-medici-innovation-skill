# Agent Medici Innovation for Claude

Claude edition of the `medici-exploration` skill, version 0.1.0. It explores an idea, code project or design decision through independently facilitated, randomly drawn perspectives, current evidence and small experiments.

## Claude Code plugin

From GitHub, on Claude Code 2.1.275 or later:

```text
/plugin install agent-medici-innovation --marketplace ThatCompany/agent-medici-innovation-skill
```

On earlier releases:

```text
/plugin marketplace add ThatCompany/agent-medici-innovation-skill
/plugin install agent-medici-innovation@medici-innovation
```

From this extracted folder instead, run `/plugin marketplace add ./agent-medici-innovation` from its parent directory, then the same install command. To try it for one session without installing, start `claude --plugin-dir ./agent-medici-innovation`.

Invoke it as `/agent-medici-innovation:medici-exploration`, or ask Claude to use the Medici exploration method.

## Claude.ai and Claude Desktop

Use the standalone skill ZIP, `medici-exploration-claude-v0.1.0.zip`, from the release page. Turn on **Code execution and file creation** in Settings > Capabilities, then upload the ZIP under Customize > Skills. Claude.ai chat usually cannot start separate agents, so the skill runs its perspectives one after another and says they are simulated.

The same ZIP also works as a standalone Claude Code skill: extract its `medici-exploration` folder into `~/.claude/skills/` or a project's `.claude/skills/`, then invoke `/medici-exploration`.

## Requirements and limits

The draw helper needs Python 3 or Node.js 18.3 or later; both use only their standard libraries. Retrieval needs web tools to be allowed. Beyond structural checks, it has had one bounded forward-use run in Claude Code and none yet in Claude.ai; see `docs/validation-claude.md` in the repository.

MIT licensed. This is an independent project and does not imply endorsement by Anthropic.
