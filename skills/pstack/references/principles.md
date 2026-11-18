# Principles

Apply only the principles that change a concrete decision. Name that decision at handoff when it helps. Prefer an executable constraint over prose when the rule can be expressed exactly.

| Upstream principle | Hermes application |
|---|---|
| attack-the-premise | When fixes for the same supposed cause fail, test the assumed mechanism directly before adding another patch. |
| boundary-discipline | Define ownership and validate at trust boundaries; do not mix storage, policy, runtime and UI responsibilities. |
| build-the-lever | Invest in a cheap repeatable test/driver only when it makes a real decision repeatable or measurable. |
| encode-lessons-in-structure | Turn recurring defects into hard-to-misuse APIs, validation, types, lint or regression checks. |
| exhaust-the-design-space | Compare plausible alternatives before locking in high-cost design; use small comparable prototypes. |
| experience-first | Define success from user-visible behavior, not passing types or code counts. |
| explain-the-number | Label every measured outcome with method, workload, units and limitations. |
| fix-root-causes | Explain causal evidence and remove the mechanism rather than hiding its symptom. |
| foundational-thinking | Design data shape, invariants and ownership before detailed control flow. |
| guard-the-context-window | Read the smallest relevant slice; aggregate bulky traces outside conversation. |
| laziness-protocol | Prefer fewer moving parts and the smallest change that actually solves the problem. |
| make-operations-idempotent | Isolate retryable operations and make ambiguous external writes require reconciliation. |
| migrate-callers-then-delete-legacy-apis | Inventory consumers, migrate them, and delete obsolete paths when compatibility permits. |
| minimize-reader-load | Collapse unnecessary indirection; make important state explicit and local. |
| model-the-domain | Name states and invariants in the user's domain; prevent illegal combinations where possible. |
| never-block-on-the-human | Resolve evidence questions yourself; still stop at permission, safety, or an actual product decision. |
| outcome-oriented-execution | Work to explicit acceptance instead of equating activity with progress. |
| prove-it-works | Run the actual feature on the matching surface and retain evidence of what happened. |
| redesign-from-first-principles | Revisit the incumbent structure when constraints change rather than layering on exceptions. |
| separate-before-serializing-shared-state | Isolate independent write scopes and define the one owner of unavoidable shared state. |
| sequence-verifiable-units | Keep each slice independently checkable; make dependencies explicit. |
| subtract-before-you-add | Remove obsolete code or paths before reaching for a new layer. |
| test-behavior-not-implementation | Assert the contract and failure mode instead of internal call choreography. |
| type-system-discipline | Use closed types and real boundary checks instead of casts or permissive fallbacks. |
