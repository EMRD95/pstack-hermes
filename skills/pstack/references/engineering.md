# Engineering playbooks

## investigation

1. State the exact question, scope and what would settle it. Trace entry point to data, state, effects and outputs. For “why,” locate the original decision in Git history and separate evidence from inference.
2. Check claims with a read-only reproduction or existing test when useful. No changing code. Hand off a short map of files/symbols, behavior, and uncertainties; provide tradeoffs if asked to recommend.

## bug-fix

1. Reproduce on the matching surface before editing. Trace candidate causes and choose the probe that distinguishes them fastest. Pin the root cause with evidence. If blocked, label the exact missing fixture or permission, not a guess.
2. Add the cheapest regression detector that would fail for the reported cause. Observe red; design the boundary first if a caller contract changes. Implement the smallest rooted fix. Delegate only with a narrow file scope and the reproduction.
3. Observe green and repeat the original reproduction on the same surface. Check neighboring behavior and changed invariants. A pass from a different surface is only partial evidence. Move to opening-a-pr only if requested.

## feature

1. Trace the existing flow and choose one useful vertical slice. Name the domain types, caller interface, ownership and invalid states. Prototype contested decisions and turn important constraints into tests or validation.
2. Record four considerations: what can be deleted, what behavior is measurable, what can be delegated without write overlap, and what feedback should become an enforceable rule. Mark irrelevant ones with reasons.
3. Build the slice using a failing acceptance or regression check where practical. Integrate before expanding. For UI map the feature, permissions, user transitions and failure path.
4. Verify the real path plus edge cases and review exact diff. Prepare delivery evidence; open a PR only if requested.

## refactoring

1. Capture existing behavior in a characterization test, recorded outputs, or equivalence harness. State a concrete structural gain, e.g. one source of truth or fewer invalid states.
2. Remove obsolete branches/wrappers first. Move in verifiable steps. For replaced internal interfaces identify every caller before removal and avoid parallel legacy paths unless there is a real compatibility constraint.
3. Compare pre/post outputs on the relevant artifact. If the refactor did not reduce incidental complexity, do not present it as a win. Preserve unrelated work.

## prototype

1. Decide what the experiment must resolve and define competing choices and measures. If the choice is already made, use feature.
2. Build the cheapest comparable variants away from production source. Use identical workloads and label variants so differences are attributable.
3. Exercise each in the real surface, record evidence and recommend one. Report what remains unproven. Do not promote experiment code by default.

## multi-phase-plan

1. Trace current contracts and resolve empirical uncertainties with a small read-only or scratch experiment where in scope. If trivial, give the direct sequence rather than inventing phases.
2. Write ordered slices with ownership, dependencies, file boundaries, rollback and a checkable exit criterion per slice. Separate independent branches from actual stack dependencies. Include unit, runtime and performance evidence where relevant, with concrete scenarios or an N/A reason.
3. Hand off the plan when planning only. With explicit build authority execute one slice at a time and update the decision trail as evidence changes.

## authoring-a-skill

1. Distinguish a user-local skill from a distributable skill. Check existing skills before adding another. Use skill_manage for local changes and hermes-agent-skill-authoring for repository standards.
2. Add trigger, actionable checklist, references, failure modes, and executable tests for helpers. Preserve upstream attribution and license when adapting source. Test broken and valid examples.
3. Verify the installed skill resolves and that its entry routes to a real artifact. Do not change Hermes core or publish unless asked.
