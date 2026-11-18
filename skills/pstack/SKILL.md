---
name: pstack
description: Use when asked for pstack. Run its coding playbooks.
version: 0.1.0
author: Lauren Tan (poteto), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Coding, Verification, Workflows]
    related_skills: [coding-mode, test-driven-development, requesting-code-review]
---

# pstack for Hermes

Local port of Lauren Tan's pstack workflow. Upstream provenance, credit and compatibility: `references/upstream.md`. Keep `/coding-mode` as the lightweight alternative.

## When to Use

Invoke `/pstack <task>` to select a playbook, `/pstack help` to list playbooks and specialist modes, or `/pstack <playbook-or-specialist>: <task>` to select explicitly. Examples: `/pstack bug-fix: typing stutters on long runs`, `/pstack interrogate: review this diff`, `/pstack statechart: map service retirement`.

## Operator contract

- Opening a mode never grants new permissions. Read only for investigations, reviews, plans, and status unless the user explicitly asks for changes. No commit, push, PR write, merge, deploy, cron, or global configuration change merely because a playbook mentions one. In particular, a request to verify or babysit is not permission to merge.
- Keep the playbook active on follow-ups about the same task in this conversation. A new task routes anew. A user stop or reversal takes priority; stop scoped workers promptly and use Pause safely without starting new work.
- Use the current Hermes session and configured delegation. No Cursor binaries, hidden credentials, nested autopilot, changes to model config, or unattended loops by default. Use `delegate_task` for bounded independent work, not for polling or self-approval. Assign disjoint write scopes and inspect the results yourself. A second model is optional and never claimed without evidence.

## Workflow

1. Establish repo, base/dirty state, exact goal, observable acceptance and authority. Read the relevant repo instructions, CI, and call sites. Never reset someone else's edits to establish a baseline.
2. Select the closest playbook from `references/playbook-index.md`, then load only its file. Explicit specialist requests use `references/specialists.md`. For large changes, put the selected steps in `todo_list` if available; mark steps not applicable with reasons. Document scope, data shape, smallest change, and independent work before delegating.
3. Encode recurring constraints in the API, types or deterministic checks before adding more prose. Start with the user-facing outcome, trace root causes, prefer a small testable slice, and remove dead alternatives rather than adding a second path. Load `references/principles.md` when choosing between designs or deciding the evidence needed.
4. Verify on the same surface as the request. For UI use `browser_exec` or app-specific drivers, map feature, action, expected result and failure path; record screenshots or traces where useful. A statechart describes the intended behavior; compare it with real behavior rather than calling the diagram a proof. For CLI use `terminal` and record the command, exit status, and observed result. If the optional `coding-mode` skill is installed, its verification helper can create a private receipt. Run checks after the last relevant edit. A green test that cannot detect the reported failure is not acceptance.
5. Before publishing or presenting substantial changes as ready, get a fresh bounded review when available. Fix real blockers, rerun affected checks, and report what was measured, observed, or remains unverified. For authorized GitHub operations use `github-pr-workflow`, obey branch protection, and read back the resulting ref/PR. For long-running work leave verifiable checkpoints and a stop condition, not a promise to continue invisibly.
