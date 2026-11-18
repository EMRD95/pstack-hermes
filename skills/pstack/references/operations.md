# Operations playbooks

## autonomous-run

1. Set testable completion, allowed effects, workspace, time/attempt budget and way to stop before starting. A run in the current turn is not permission to schedule. Use unattended-work-loop for explicitly requested persistence; never silently use a wider credential or bypass approvals.
2. Each iteration takes one evidence-backed step, tests it and records change, outcome and next step. Respect budget and stop on authority or safety boundary, repeated blocker, or success. No automatic escalation or goal expansion.

## autopilot-full

1. Confirm the exact queue, repos, budgets, authorized effects and stop conditions. Split independent items from dependencies; assign one owner per item and distinct branches/worktrees. Controller owns integration and any publication actions.
2. Verify each landed candidate with project checks, matching runtime evidence where applicable, and a separate review. On base/head change recheck affected evidence. No observer can approve its own change or loosen a gate to clear the queue.
3. Stop at merge-ready absent an explicit grant for each publish/merge/deploy step. A stop signal cancels scoped workers and prevents new writes. Report verified outcomes, remaining owner/branch and blockers.

## autopilot-stack

1. Use the same ownership and checkpoints as autopilot-full, but build only true dependency stacks. Each child branches from its actual parent and verifies against that base.
2. Stop at verified heads and hand off dependency order, base/head, checks and open work. No auto-merge. If parents change, revalidate descendants before calling them ready.

## pause-safely

1. Stop new work and cancel scoped workers. Resolve only an in-flight atomic step that cannot be left safely, and do not continue beyond that boundary.
2. Preserve dirty state without committing, stashing, deleting, publishing or undoing work unless authorized. Record goal, branch, changed paths, checks, pending effects, and a single safe resume action in a private checkpoint if needed.

## session-pickup

1. Confirm the latest user intent still authorizes the task. Reconstruct branch/head/base, dirty files, pending workers and tracked remote effects from git, scoped session_search, and recorded checkpoints.
2. Verify material inherited claims at their real target. Do not repeat completed writes; resolve uncertainty before retrying. Continue at the earliest unmet criterion in the matching route.

## worktree-cleanup

1. List worktrees, dirty/untracked files, branch ancestry and active sessions/processes that might use them. Treat merged or old as a clue, not a grant. Preserve user edits and ignored valuable data.
2. Offer exact removable paths and why they are safe. Remove only explicitly approved clean inactive worktrees through Git without force by default; don't delete branches or unrelated cache. Verify worktree list and report skips.
