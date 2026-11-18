# Upstream and compatibility

Adapted from [Lauren Tan's pstack](https://github.com/cursor/plugins/tree/35a90942a7f02e1ebbc2443643179815f2147954/pstack), at commit `35a90942a7f02e1ebbc2443643179815f2147954`. See the original [talk transcript](https://ai.engineer/talks/O_zcc6Xl12g-all-code-is-slop-except-mine.md). The upstream MIT notice is in `references/LICENSE.txt`.

The port translates every entry in the pinned snapshot's mode playbook directory, plus its named specialist skills and design principles. It does not execute or install upstream scripts, agents, extensions, assets, or automation definitions. Adaptations are local to this Hermes profile. Recheck the upstream inventory before upgrading a pin: run `python3 scripts/check-port.py --upstream <checkout>` from the skill directory. Run without `--upstream` for the installed pack's structural checks.

| Upstream mechanism | Hermes equivalent or gap |
|---|---|
| poteto-mode and playbook checklists | `/pstack` entry with explicit routes, per-task todo list for substantial work, same-task follow-ups. |
| Poteto agent and comment reviewer | Scoped `delegate_task` briefs and fresh read-only review, with locally configured models. No external model pins or enforced independent family. |
| Cursor projects, `/loop`, workflow automation | Bounded interactive runs; use the existing Hermes unattended workflow only when explicitly requested. No release-triggered Benny automation or auto-merge installed. |
| Cursor Team Kit `control-ui`, `control-cli` and `deslop` | Hermes browser/terminal and exact-diff review; app-specific GUI drivers only when available. No drop-in Team Kit compatibility. |
| Graphite/Origin stacks | Explicit parent/base dependencies using Git/GitHub. No automatic stack rewrites. |
| Runtime and formal verification | Reuse installed browsers, project drivers, test runners and model checkers. No bundled TLA+, Lean or Bombadil. |
| Model setup and presets | Reuse active Hermes profile. `/pstack setup-pstack` audits tooling without changing config. |

This is workflow coverage, not parity with every upstream side effect, helper binary or platform. Use `/pstack help` to see available modes; only `/pstack` is registered by this skill.
