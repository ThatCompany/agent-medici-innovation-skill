# Agent Medici Innovation Skill

Explore an idea or design decision through diverse perspectives, current evidence, independent facilitation, and small experiments. The method draws on the Medici Effect's cross-disciplinary connections and the activity-based reframing and prototyping discussed in *The Art of Innovation*.

## Choose an edition

| Edition | Status | Download |
|---|---|---|
| **Codex** | v0.1.0; structurally validated and screened on three synthetic saved scenarios | [Codex skill ZIP](https://github.com/ThatCompany/agent-medici-innovation-skill/releases/download/v0.1.0/medici-exploration-codex-v0.1.0.zip) |
| **Claude** | Planned; awaiting separate evaluation and adaptation | No Claude download yet |

[All releases and checksums](https://github.com/ThatCompany/agent-medici-innovation-skill/releases) · [Codex source](editions/codex/skills/medici-exploration/SKILL.md) · [Validation details](docs/validation.md)

The current edition was tested in Codex. Its shared method is largely portable, but other hosts must supply independent agents, retrieval, code execution and suitable question controls. A skill does not create those capabilities. The package includes explicit fallbacks and must disclose when independent-agent coverage is unavailable.

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
```

The packaging script creates a standalone skill ZIP, an optional plugin ZIP, and checksums under `dist/`. Build artifacts are attached to GitHub Releases rather than committed. No GitHub Actions workflow is included; run checks locally.

## Claude edition and contributions

The Claude edition will be added after its separate evaluation. Keep it alongside the Codex edition so visitors can choose either; do not overwrite the Codex download. [CONTRIBUTING.md](CONTRIBUTING.md) explains the layout and evidence expected for another edition.

## License

[MIT](LICENSE). This is an independent project and does not imply endorsement by OpenAI, Anthropic, or the authors of the books that inspired the method.
