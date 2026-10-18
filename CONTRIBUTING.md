# Contributing editions and improvements

The current implementation is under `editions/codex/skills/medici-exploration/`. Keep platform-specific editions in separate directories. A Claude edition should use `editions/claude/skills/medici-exploration/` and describe the host and capabilities actually tested. Do not add a downloadable placeholder before a working edition exists.

Preserve the common method where possible: original user purpose, three drawn families per panel, independent facilitation and commitments, retrieval, meaningful dissent, complete authored notes/questions, existing authorization and bounded stopping. Document intentional differences rather than implying both editions behave identically.

When adapting, check how the host creates independent contexts, schedules capacity, retrieves sources, runs the draw helper, preserves artifacts and captures questions. If a capability is absent, disclose the limitation; do not describe simulated lenses as independent agents. Test ordinary discovery, explicit invocation, incomplete input, requests that should bypass the method, and failure/recovery behavior.

## Evaluation materials

- `tests/cases.json`: three fully fictional saved explorations and their output contract.
- `tests/criteria.json`: preregistered behavioral criteria and comparison limits.
- `tests/recorded-codex-output.json`: recorded output from the consolidated Codex edition.
- `tests/recorded-results.json`: structural validation, comparison findings and bundle fingerprints.
- `tests/draw-replay.json`: recorded selection for a deterministic packaging smoke check.

These saved-record scenarios exercise evidence correction, incomplete coverage and central comparison. They do not validate fresh panel assembly, live retrieval, resistance to coordinator steering, or actual interface delivery. A new edition needs its own forward-use checks. Record consequential failures and corrections, not just agreement or a word-count reduction.

For a release, run the local package check and the official skill-creator validator when available. The bundled check is a project sanity check, not the official validator. Keep runtime/tooling dependencies out of distributed skill ZIPs.

## Pool and version discipline

Pool fingerprints cover exact bytes. Git attributes preserve the edition files without line-ending conversion. Retain earlier pool versions and receipts; make pool changes visible rather than modifying a live draw. Changing the pool also requires updating replay expectations deliberately.

Use edition-specific archive names. When Claude is ready, add its release asset and installation instructions, update the README's status/download row, and retain existing Codex assets. A plugin manifest is optional for an edition; the packaging script always supports a standalone skill archive.
