# Verification playbooks

## perf-issue

1. Capture a baseline on the symptom's real surface. Record version, fixture, workload, warmup, repetitions and metric. Trace the hot path and change one mechanism at a time.
2. Repeat the identical measurement after the change. Report distribution or range, correctness checks, and confounders instead of asserting a speedup from a single lucky sample.

## hillclimb

1. Specify a realistic target metric, correctness constraints, and budget. Establish a harness that distinguishes failing and acceptable behavior. Freeze the workload and metric.
2. Log each hypothesis, diff, before/after measurement, correctness result and keep/revert decision in a scratch ledger. Keep only observed improvements without a correctness or complexity regression. On plateau change the mechanism, not the metric.
3. Stop when the predicate is met, evidence says further work is not worthwhile, or budget expires. Preserve the ledger and a reproducible best result.

## runtime-forensics

1. Capture the live symptom on an authorized process: profile, logs, memory sample or browser trace. Observe production read-only; use instrumentation and experiments on an isolated replica unless separately authorized.
2. Reduce to a hot stack, retainer, state transition or failing request. Link the strongest evidence to a source symbol. Record an alternative explanation and a discriminating probe. Do not modify code unless requested.

## trace-forensics

1. Identify format, timeframe, and symbols. Summarize a large capture off-context, preserving the raw artifact; query structured spans/samples rather than dumping them into chat.
2. Rank hot or failing frames, follow callers/retainers, and attribute to source with timestamps or sample counts. Compare paired traces where available; otherwise distinguish observation from hypothesis. Return diagnosis before any change.

## visual-parity

1. Capture trusted before/target images under matching viewport, fonts, device scale, data and animation time. Define tolerances before looking at the diff; no moving the baseline to turn a failure green.
2. Migrate one component or flow at a time. Capture the same states, inspect diffs and exercise behavior using a real browser. If visuals cannot be inspected, report the numerical evidence without inventing a visual verdict.

## eval

1. Define the question and rubric before collecting candidates. Use identical prompts and comparable budgets with isolated or read-only environments; tell the user if model diversity is unavailable.
2. Remove model and candidate identities from judge inputs; keep the intended rubric hidden from candidates. Run deterministic checks first when possible, then a fresh bounded judge. Inspect each result and reconcile discrepancies. Report sample size and limitations.

## Shared verification record

For each material claim name the surface, observed input and expected/actual result, Git revision or diff, and artifact path. For UI see coding-mode's review-evidence reference. For formal verification use only a concrete invariant and a project-supported checker; record the properties and bounds checked, and verify integrated behavior separately.
