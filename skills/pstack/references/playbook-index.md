# Playbook index

Pick one primary route. Explicit route names win. A request to diagnose without changing code is read-only. Choose the most specific evidence surface: use trace-forensics when given a capture, runtime-forensics for a live symptom without a capture, perf-issue for a requested measured fix, hillclimb for iterative improvement against a budget. Names below are exact section anchors, not additional slash commands.

| Route | Load | Use for |
|---|---|---|
| investigation | `engineering.md` | Explain or trace behavior, no edit |
| bug-fix | `engineering.md` | Reproduce and fix a failure |
| feature | `engineering.md` | Deliver new behavior |
| refactoring | `engineering.md` | Improve structure without behavior changes |
| prototype | `engineering.md` | Resolve a decision with a disposable experiment |
| multi-phase-plan | `engineering.md` | Plan ordered independent or dependent slices |
| authoring-a-skill | `engineering.md` | Build and test a reusable Hermes skill |
| perf-issue | `verification.md` | Fix a measurable regression |
| hillclimb | `verification.md` | Optimize against a frozen metric |
| runtime-forensics | `verification.md` | Diagnose a running app |
| trace-forensics | `verification.md` | Analyze existing trace or dump |
| visual-parity | `verification.md` | Preserve or match rendered behavior |
| eval | `verification.md` | Compare variants with a blinded rubric |
| opening-a-pr | `delivery.md` | Prepare or open an authorized PR |
| babysit | `delivery.md` | Inspect CI or review state |
| shipping | `delivery.md` | Land explicitly approved verified PRs |
| autonomous-run | `operations.md` | Bounded execution with checkpoints |
| autopilot-full | `operations.md` | Coordinate a queue up to its authorized gates |
| autopilot-stack | `operations.md` | Verify dependent PRs and hand them off |
| pause-safely | `operations.md` | Stop new work and preserve state |
| session-pickup | `operations.md` | Resume a known task from evidence |
| worktree-cleanup | `operations.md` | Audit worktrees and remove only approved paths |

Playbook files are in `references/`. Read only the selected section (plus the declared shared contract) at runtime. If no playbook fits a large task, start with multi-phase-plan and choose a route for each slice. If the user authorized implementation, proceed with the first slice; if they requested only a plan, stop at the plan.
