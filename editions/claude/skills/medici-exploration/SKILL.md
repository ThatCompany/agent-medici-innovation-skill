---
name: medici-exploration
description: Explore an idea, code project or design decision through randomly drawn perspectives, current evidence and small experiments. Use when asked, or when distinct framings could change a decision.
license: MIT
compatibility: Claude edition for Claude Code, Cowork and chat in Claude.ai. Claude Code and Cowork supply subagents, a shell for the draw helper and, where allowed, AskUserQuestion and web tools. Chat needs code execution for the helper; without separate agent contexts, perspectives run sequentially and are disclosed as simulated.
---

# Medici Exploration

Discover useful connections and turn them into an assessable next step. Diversity is a hypothesis about value: role names, fluent output and repeated agreement do not establish useful diversity or independent corroboration. Work directly when a clear approach or lookup suffices. Ordinary implementation, routine review and task parallelization do not by themselves call for this workflow.

## Read by responsibility

Every participant receives this common contract, the original request, relevant earlier user guidance, known facts and constraints, authorization, effort ceiling and its assignment. Supply an existing design as the review subject when applicable. Do not supply a preferred central answer before independent commitments. Share essential evidence promptly; disclose distinct source assignments.

Load the applicable guide, rather than every role's procedure:

| Responsibility | Required guide |
|---|---|
| Facilitate, select perspectives or check reporting | [Facilitator charter](references/facilitator-charter.md) |
| Author a drawn contribution or receive an exchange | [Participant guide](references/participant-guide.md), plus the assigned family's complete text |
| Retrieve evidence or investigate practice and purpose | [Research and practice](references/research-and-practice.md) |
| Coordinate or facilitate multiple panels | [Multi-panel mode](references/multi-panel.md) |
| Coordinate in Claude Code or Claude.ai | [Claude hosts](references/claude-hosts.md) |

The coordinator reads the host guide and the applicable mode guide, then assigns each role its guide. References add detail; the shared protections below apply to every role. Separate contexts and records provide procedural separation, not a technical security boundary. Shared models, evidence, framing and the standing pool can retain blind spots.

## Brief once and bound the work

The facilitator owns adaptive intake. Reuse existing guidance in one brief separating verbatim user statements, interpretations and open questions. Preserve the original request beside any reframe; inferred needs, values and design assumptions do not become user requirements by repetition.

Ask only for information that changes the next useful step. Start with one question if needed; normally offer a bounded first exploration after no more than two follow-ups. Accept uncertainty and open discovery. Stop intake once one useful authorized step, preserved constraints and examined assumptions are clear. Do not demand a preferred solution, measurable final objective, repeated optional answers or approval of routine briefing. Revisit only for material changes.

Pause only dependent work for missing authorization, contradictory binding constraints or a consequential commitment requiring an unresolved user priority. Silence supplies no required answer or approval. Continue independent work and preserve existing authorization.

State the question, evidence, scope and proportionate effort ceiling; choose and communicate a small ceiling if absent. **Explore** develops framings and possibilities; **develop** examines or carries out small changes within existing authorization. Exploration does not itself authorize installation, publication or unrelated implementation.

## Compose and select

Use at least **three different standing-pool families per panel**, in addition to the coordinator's own perspective. Fixed duties and task-specific additions do not replace these seats, even when concerns overlap. This is a coverage floor, not proof of completeness.

The provisional single-panel default is seven logical participants:

- Coordinator: resources, execution, verification of decision-carrying claims and an explicitly attributed recommendation.
- Separate facilitator: selection, fair process and faithful reporting; no substantive winner vote.
- Evidence researcher: current sources, existing alternatives and contrary findings.
- Practice and purpose investigator: actual activities, desired experiences and domain practice; distinguish observation from simulation.
- Three independently committing drawn contributors.

A narrow run may combine practice investigation with coordination for six; record it. Keep facilitation separate to claim independent facilitation. Add seats only for a named gap that could change the next action, one at a time within the ceiling; eight is a normal single-panel planning ceiling. Verification or specialist gaps can justify an addition. Beyond that, consider separate decisions. These counts are design defaults, not measured optima; honor explicit user composition and limits.

The facilitator reads the [standing pool](references/perspective-pool.json), records the question, constraints, fixed assignments, ceiling and coordinator perspective, and administers the [draw helper](scripts/draw_perspectives.py) under its charter. In Claude Code and Cowork its full path is `${CLAUDE_SKILL_DIR}/scripts/draw_perspectives.py`. Keep the version, fingerprint, seed and allocation. No convenient rerolls, substitutions or mid-draw pool changes. Reveal families and selection rationale. Preserve an inapplicable lens and explain the mismatch; do not remove it from coverage accounting. Pool revisions are visible changes with the user and preserve earlier versions.

Use subagents for independent contributions and respect runtime capacity; batch work when needed. Honor requests for fresh participants. The coordinator may execute tools for a facilitator if necessary, retaining its request and result. If subagents are unavailable, disclose sequential lens work as simulated; do not claim independent-agent coverage. The host guide maps these duties onto the tools each Claude surface provides.

## Explore, exchange and account

Research is a standing duty: retrieve consequential evidence and existing ways to accomplish the intended activities, rather than relying on training memory alone. Supplied materials may suffice for a closed hypothetical task; state that scope. The researcher informs; the coordinator verifies claims carrying its recommendation. Missing retrieval or inadequate sources qualify affected conclusions.

Contributors author their own investigative questions and briefs before seeing peers' proposals or a preferred central solution. Preserve initial commitments and attributable revisions in context or existing artifacts. Do not create files merely to repeat the conversation. Use both challenge and constructive family prompts, seek a plausible cross-disciplinary mechanism, and name one missing assumption or perspective. Report examined and remaining gaps.

Use the participant guide for specimens, independent activity-based reframing and exchange. The facilitator routes a consequential uncertainty or promising pair to a suitable receiver; one selective exchange is the starting default. Retain, combine, transform or reject with reasons. Compare mechanisms and assumptions, not vocabulary. An unchanged proposal or no useful connection is a valid result.

Trial concise change replies: cite originals, state the disposition, changed mechanism, evidence status, consequential condition and alternative action, unresolved objection and distinguishing observation. Keep these relationships in the reply itself. Links supply supporting detail. A short reply is a soft default; expand when compression conceals a distinction. Do not create a capsule for every option or preserve alternatives merely because different agents proposed them.

Account for each consequential objection with an inspectable source and disposition: adopted, rejected with reasons or unresolved. Classify disagreements as evidence gaps, causal assumptions, scope differences or competing values. Neither facilitator nor coordinator settles truth or user values through votes or confidence. Retain an alternative when it supports a worthwhile different action or test. When a recommendation changes, say what evidence or reasoning changed it.

## Resume proportionately

For batched or interrupted work, keep phase, receipt and commitment references, dependencies, pending choices and next authorized action in the existing brief. Check for changed common evidence on resumption. Refresh affected contributions once within the remaining ceiling; notify all if dependencies are shared or uncertain. Preserve originals and distinguish author revisions from coordinator annotations; do not repeat settled intake or redraw automatically.

If a seat remains unavailable, retain its identity and state. Continue independent work, bound recovery, and deliver available findings explicitly as partial with affected conclusions identified. Never invent assent or claim the required coverage was achieved. A complete-panel requirement remains unsatisfied until its missing work is obtained or the user changes it.

## Deliver and call the question

Deliver a proportionate account: recommended direction; consequential connection and originating contributions; decisive evidence and assumptions; strongest remaining objection or alternative; smallest useful test, disconfirming result and stopping point. Label observations, sourced findings, hypotheses, analogies and synthetic walkthroughs. Real user evidence is not replaced by simulated preferences. Report when more perspectives produced no useful change.

The facilitator checks the synthesis once for omitted or misrepresented objections. Contributors may append a direct correction without another adjudicator; this is a reporting right, not a veto. The coordinator may disagree while preserving the source position and must label its own judgments. Neither role silently changes membership, substantive purpose, evaluation rules or representations of agreement.

Preserve every optional authored user-facing note and question verbatim with attribution, originals and revisions. Use predeclared slot order, not agreement ranking. Present all notes or an explicitly complete linked record with counts and delivery limits; a summary does not replace them. Contributor submissions are bounded in the participant guide. Facilitator notes concern process.

After every completed panel round, present **every submitted user question** as multiple choice through supported interactive controls, with an Other/free-text route. Preserve authored wording, alternatives and attribution; label coordinator-authored choices. Identify the affected next action and whether answering is required or optional. Keep original notes alongside controls. No silent deferral of optional questions. Manageable batches are allowed; disclose any pending batch. Include keep-open when meaningful and never treat a preselected choice as an answer.

Use a documented question tool supported in the active mode. In Claude Code, `AskUserQuestion` supplies Other/free text automatically: omit a duplicate Other choice and follow the limits in the host guide. Only the coordinator asks; relay subagent questions with their wording intact. If controls are unavailable, explain the fallback and provide text choices ending in Other; do not retry an absent tool or switch modes just to obtain controls.

Keep unanswered questions visible as pending, answered, declined or superseded; optional answers do not block authorized work. A required answer blocks only its dependent action. Any participant or the user can call an earlier checkpoint. At closure offer decision, reversible experiment, specific evidence gathering, bounded continuation, retained alternatives and park/stop without a winner. Include one overall next-round choice in the interface when continuation is open, even when contributors pass. Record answers in the brief, preserve free text verbatim and route the direction to the relevant panel.

## Stop and evaluate

Stop after a bounded exchange and synthesis unless a named uncertainty justifies further work within the ceiling. Stop earlier for repeated mechanisms, no consequential distinction or unavailable observations. Further rounds name the uncertainty, plausible information gain, limit and stopping point; no automatic debate loops. Avoid recursive self-evaluation panels; an explicit user request may authorize one bounded self-review.

Use the smallest authorized specimen or experiment; otherwise specify it. An efficiency change should examine useful discoveries, constraint and objection fidelity, total cost and latency, and human reading/correction effort. Record possible experience losses and whether those values are stated, observed, hypothetical or unknown. Fewer words or agents alone do not establish improvement.

A demonstration is not proof of multi-agent superiority. Such a claim needs a capable revisable single-agent baseline with the same evidence, comparable total resources and anonymized task-specific assessment. A small current-versus-revised check can expose regressions without establishing preserved efficacy. Agree a broader comparison separately when needed; calling the question does not settle factual truth or authorize unrelated work.
