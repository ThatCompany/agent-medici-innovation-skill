# Agent Medici Innovation for Claude

Claude edition of the `medici-exploration` skill, version 0.1.1. It explores an idea, code project or design decision through independently facilitated, randomly drawn perspectives, current evidence and small experiments.

## Install

Pick where you use Claude. Adding the plugin once on claude.ai or in the desktop app covers chat, Cowork and Claude Code.

### Claude.ai, the desktop app and Cowork

1. Open **Customize > Plugins**.
2. Select **Add > Add marketplace** and enter `ThatCompany/agent-medici-innovation-skill`.
3. Find **agent-medici-innovation** in the list and add it.
4. For chat, turn on **Code execution and file creation** in Settings > Capabilities.

The plugin is saved to your account. It then works in chat on the web, desktop and mobile apps, in Cowork tasks, and in Claude Code when you sign in with the same account. To use it, ask Claude to use the Medici exploration method, or type `/` and choose it. To get a newer version, select **Check for updates** on the marketplace, or turn on **Sync automatically**.

If you can't add a marketplace from GitHub, use **Add > Upload plugin** with `agent-medici-innovation-claude-plugin-v0.1.1.zip`. To add only the skill, open **Customize > Skills**, select **+ > Create skill > Upload a skill**, and choose `medici-exploration-claude-v0.1.1.zip`.

On Team and Enterprise plans, a missing **Add** option means an Owner has turned off member-added plugins. An Owner can add the plugin for everyone in **Organization settings > Plugins & skills**: select **Add > Upload a plugin**, then set its **Default access**.

### Claude Code

This covers the terminal, the IDE extensions and the desktop app's Code tab. If you already added the plugin on claude.ai, Claude Code 2.1.273 or later loads it at the next session start, signed in with the same account; run `/reload-plugins` to load it right away.

Otherwise, on Claude Code 2.1.275 or later:

```text
/plugin install agent-medici-innovation --marketplace ThatCompany/agent-medici-innovation-skill
```

On earlier releases:

```text
/plugin marketplace add ThatCompany/agent-medici-innovation-skill
/plugin install agent-medici-innovation@medici-innovation
```

Invoke it as `/agent-medici-innovation:medici-exploration`, or ask Claude to use the Medici exploration method.

From this extracted folder instead, run `/plugin marketplace add ./agent-medici-innovation` from its parent directory, then the second install command above. To try it for one session without installing, start `claude --plugin-dir ./agent-medici-innovation`. To install only the skill, extract the `medici-exploration` folder from the skill ZIP into `~/.claude/skills/` or a project's `.claude/skills/`, then invoke `/medici-exploration`.

### Claude API and Agent SDK

Upload the skill folder with the [Skills API](https://platform.claude.com/docs/en/build-with-claude/skills-guide) and use it with the code execution tool, or pass this plugin folder to the Agent SDK's `plugins` option.

## Requirements and limits

The draw helper needs Python 3 or Node.js 18.3 or later; both use only their standard libraries. Retrieval needs web tools to be allowed. Beyond structural checks, it has had one bounded forward-use run in Claude Code and none yet in Cowork or chat; see `docs/validation-claude.md` in the repository.

MIT licensed. This is an independent project and does not imply endorsement by Anthropic.
