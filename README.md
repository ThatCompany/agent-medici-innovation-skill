# Agent Medici Innovation Skill

Explore an idea or design decision through diverse perspectives, current evidence, independent facilitation, and small experiments. The method draws on the Medici Effect's cross-disciplinary connections and the activity-based reframing and prototyping discussed in *The Art of Innovation*.

## Choose an edition

| Edition | Status | Download |
|---|---|---|
| **Codex** | v0.1.0; structurally validated and screened on three synthetic saved scenarios | [Codex skill ZIP](https://github.com/ThatCompany/agent-medici-innovation-skill/releases/download/v0.1.0/medici-exploration-codex-v0.1.0.zip) |
| **Claude** | v0.1.0 preview; passes Anthropic's skill validator and Claude Code's strict plugin validator; one forward-use run in Claude Code; Claude.ai upload not yet tried | [Claude skill ZIP](https://github.com/ThatCompany/agent-medici-innovation-skill/releases/download/claude-v0.1.0/medici-exploration-claude-v0.1.0.zip) (Claude.ai, Claude Desktop or Claude Code) · [Claude Code plugin ZIP](https://github.com/ThatCompany/agent-medici-innovation-skill/releases/download/claude-v0.1.0/agent-medici-innovation-claude-code-v0.1.0.zip) |

[All releases and checksums](https://github.com/ThatCompany/agent-medici-innovation-skill/releases) · [Codex source](editions/codex/skills/medici-exploration/SKILL.md) · [Claude source](editions/claude/skills/medici-exploration/SKILL.md) · [Validation details](docs/validation.md) · [Claude validation](docs/validation-claude.md)

Each edition was checked only in its own hosts. The shared method is portable, but a host must supply independent agents, retrieval, code execution and suitable question controls. A skill does not create those capabilities. Both editions include explicit fallbacks and must disclose when independent-agent coverage is unavailable.

An [OpenAI plugin ZIP](https://github.com/ThatCompany/agent-medici-innovation-skill/releases/download/v0.1.0/agent-medici-innovation-openai-v0.1.0.zip) packages the same skill for plugin import or distribution. ChatGPT execution has not been validated. This repository release is separate from approval or publication in the OpenAI Plugins Directory.

## Use the Codex edition

1. Download the **Codex skill ZIP** above and extract its `medici-exploration` folder.
2. Put that folder in your user skill directory, `~/.agents/skills/`, or a repository's `.agents/skills/` directory.
3. In Codex, invoke `$medici-exploration`. Newly installed skills are detected automatically; restart Codex if it does not appear.

Example requests:

```text
Use $medici-exploration to explore this idea: [idea].

Use $medici-exploration in multi-panel mode, with fresh participants,
to explore [question]. Keep [constraints] fixed.
```

See [OpenAI's skill installation and discovery documentation](https://learn.chatgpt.com/docs/build-skills?product=breeze) for current supported locations. The draw helper needs Python 3 and uses only the standard library. PyYAML is needed for development checks, not normal skill use.

## Use the Claude edition

**Claude Code plugin.** On Claude Code 2.1.275 or later, install from this repository in one step:

```text
/plugin install agent-medici-innovation --marketplace ThatCompany/agent-medici-innovation-skill
```

On earlier releases, run `/plugin marketplace add ThatCompany/agent-medici-innovation-skill`, then `/plugin install agent-medici-innovation@medici-innovation`. Invoke it as `/agent-medici-innovation:medici-exploration`, or ask Claude to use the Medici exploration method. The plugin ZIP holds the same plugin with a local marketplace for offline installation; its README explains the steps.

**Claude.ai and Claude Desktop.** Turn on **Code execution and file creation** in Settings > Capabilities. Then upload the **Claude skill ZIP** under Customize > Skills. Chat usually cannot start separate agents, so the skill runs its perspectives one after another and labels them as simulated.

**Standalone Claude Code skill.** Extract the `medici-exploration` folder from the Claude skill ZIP into `~/.claude/skills/` or a project's `.claude/skills/`, then invoke `/medici-exploration`.

In Claude Code the skill uses subagents for each role, `AskUserQuestion` for submitted questions, and WebSearch/WebFetch where they are allowed. Its draw helper runs with Python 3 or, as a fallback, Node.js 18.3 or later; both give the same selection for a given seed. [The Claude host guide](editions/claude/skills/medici-exploration/references/claude-hosts.md) lists every mapping and fallback.

## What the method preserves

- A standing pool of 15 perspective families, with at least three drawn families per panel and a recorded draw that cannot be conveniently rerolled.
- Separate facilitation, independent initial contributions, current evidence and actual user guidance distinguished from simulation.
- A provisional seven-participant single panel or eleven-participant two-panel setup; logical roles can run in capacity-limited batches.
- Activity-based reframing, concrete specimens and one starting targeted exchange, followed by bounded closure.
- Attributable dissent, complete authored notes, every submitted user question, and a next-action checkpoint with a free-text route.

These are procedural protections, not proof of neutrality, complete diversity, or superiority over a capable single agent. [Validation scope and remaining gaps](docs/validation.md) describe what has actually been checked.

## Develop and package

Use an existing Python 3 environment. An isolated development environment keeps validation dependencies local:

```text
python -m venv .venv
# Activate .venv using your platform's standard command.
python -m pip install -r requirements-dev.txt
python scripts/check_package.py
python scripts/package_release.py --edition codex --version 0.1.0
python scripts/check_package.py --edition claude
python scripts/package_release.py --edition claude --version 0.1.0
```

The packaging script creates a standalone skill ZIP, an optional plugin ZIP, and checksums under `dist/`. Each run replaces `dist/SHA256SUMS.txt` with that edition's checksums. The Claude check also needs Node.js, to confirm that both draw helpers agree. For the Claude edition, also run `claude plugin validate editions/claude/.claude-plugin/plugin.json --strict` and `claude plugin validate . --strict`. Build artifacts are attached to GitHub Releases rather than committed. No GitHub Actions workflow is included; run checks locally.

## Editions and contributions

The Claude edition sits alongside the Codex edition so visitors can choose either; neither download replaces the other. Its shared reference files and pool are byte-identical to the Codex edition. Only `SKILL.md`, the Claude host guide and the Node draw helper differ. [CONTRIBUTING.md](CONTRIBUTING.md) explains the layout and evidence expected for another edition.

## License

[MIT](LICENSE). This is an independent project and does not imply endorsement by OpenAI, Anthropic, or the authors of the books that inspired the method.
