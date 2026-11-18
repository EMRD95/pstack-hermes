# Specialist modes

Invoke through `/pstack <mode>: <task>`. These are Hermes implementations of the capability, not separate Cursor commands. When a specialist names an existing Hermes skill, load it if available and applicable. Otherwise follow the procedure directly and report missing tools.

| Mode | Hermes procedure |
|---|---|
| poteto-mode | Use the main pstack work contract and select a playbook. |
| poteto-help | Show the playbook index and examples relevant to the request. |
| setup-pstack | Check available tools, configured delegation and repository verify commands; recommend a per-project setup. Do not change configuration unless requested. |
| architect | Sketch the simplest caller first, then types, ownership, invalid states, recovery, and interface tests. Compare one credible alternative if the decision matters. |
| arena | Same brief, isolated roles, different approaches; evaluate blindly when feasible with a predeclared rubric; choose evidence over vote count. Use eval for measured comparisons. |
| automate-me | With consent examine scoped task history, find repeated decisions and suggest one opt-in skill or executable check. Do not install routines by inference. |
| benchmark-checklist | Identify fixture, dimensions, metrics, environment, baseline, repetitions and confounders. Require before/after on matching workload and verify correctness. |
| blast-radius | Trace callers, storage and external effects; list consumers, failure propagation and rollback boundaries. Read-only unless asked. |
| bro | Give a candid, plain-language answer from code/evidence, with the strongest counterargument and no gratuitous edits. |
| correct | Capture the actual correction and whether it generalizes; favor a test or interface constraint. Use reflect for process improvements. Do not silently change global behavior. |
| create-formal-verification-skill | Identify concrete invariants and a fitting, available model checker. Build small positive and negative fixtures and document the model's bounds; do not install an external checker without permission. |
| create-verification-skill | Map the real feature, build a reusable driver around existing browser/CLI APIs and test success plus a controlled failure. |
| figure-it-out | Define the outcome and permissions, split into independently verifiable slices, use multi-phase-plan then execute only authorized slices. Stop at blocked gates. |
| how | Trace symbols and runtime data through investigation. |
| in-your-own-words | Restate what changes in plain language and identify two points of uncertainty or misunderstanding; validate against source. |
| interrogate | Fresh read-only review of exact diff. Inspect design, failures, boundaries, missing tests and actual acceptance; give severity and exact evidence. |
| ketchup | Read-only change briefing: establish baseline and summarize what changed, why, review hotspots, and evidence gaps. |
| ketchup-video | Create a review walkthrough with real screenshots/trace; record video only if a capable driver exists. No simulated visual evidence. |
| maintain-formal-verification-skill | Update the invariant or model with a stated semantic reason; check counterexample and passing scenarios; do not loosen bounds merely to pass. |
| maintain-verification-skill | Reproduce verifier failures; separate product regression, fixture drift and driver breakage. Keep the acceptance predicate unless intent changed. |
| make-bot-ui | Use existing components, stable accessibility semantics and an isolated browser fixture; document a feature map and exercise success/failure. No Grok Bot APIs assumed. |
| no-comments | Review additions for comments that restate code or justify workarounds. Prefer clearer structure or executable checks. Preserve rationale, licenses and safety notes when useful. |
| recall | Search only relevant memory/history, then verify facts against current source and separate stale leads. |
| reflect | Compare expected outcome with observed result. Save one durable process lesson or add a check when authorized; skip log-like memories. |
| sharpen | Identify ambiguous technical and product claims, then turn each into a falsifiable question or acceptance check. |
| show-me-your-work | Maintain a private decision trail: state, alternative, action, evidence, verdict and next check; use the evidence template. |
| statechart | Model actions and visible states, transitions with guard/effect, failure and recovery. Read back observed states; Mermaid is optional, not proof. |
| swarm | Split independent responsibilities, assign disjoint files or isolated worktrees, brief acceptance, collect evidence and integrate in parent. No implicit writes by reviewers. |
| tdd | Follow test-driven-development: red for correct reason, minimal green, refactor, then rerun. |
| teach | Explain with motivating examples and a small check for understanding; use actual code behavior rather than invention. |
| technical-writing | Write for the reader's actions and constraints. State requirements, result, verification and known gaps. Remove unsupported claims. |
| typescript-best-practices | Identify actual TS settings. Model closed states and validate boundary data; avoid assertions masking real mismatches; confirm compiler and relevant tests. |
| unslop | Remove stock phrases, unsupported certainty and repeated prose; retain qualifications and evidence. |
| why | Find history/decision evidence, name inferred rationale separately, and use a small reproduction if appropriate. |
