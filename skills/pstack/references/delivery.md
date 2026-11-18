# Delivery playbooks

## opening-a-pr

1. Confirm remote, branch, base, authorized actions and whether a PR already exists. Inspect staged and unstaged changes; exclude unrelated files and credentials. For dependent work use the actual parent branch and make ancestry explicit.
2. Describe why, changes, evidence, risks, and recovery in the body. Record the verified head. Link real screenshots or traces only after checking for secrets. Follow github-pr-workflow; don't push or create the PR unless requested. Read back the exact PR/head if written.

## babysit

1. Read exact PR head, mergeability, required checks and review threads. Compare checks to the current head and distinguish failing, pending, infrastructure and not configured. Do not infer approval from a green check.
2. Triage each review comment or failure with evidence. Apply changes, reply, rerun, or resolve only when expressly in scope. Recheck the new head afterward. No polling loop, merge or automatic rebuttal merely because status was requested.

## shipping

1. Confirm the user's explicit merge grant for the exact PRs. Resolve dependencies and identify the bottom contiguous reviewed, green sequence. Do not treat authorization for one PR as authorization for the stack.
2. Confirm each head's verification and reviews, base, protection, and deploy triggers. Revalidate changed heads against the updated base. Respect repository settings and never bypass required checks.
3. Merge bottom-up within the authorized set using normal forge operations and verify landed commits before advancing. Stop on mismatch or new failure. Do not conflate merge, deploy dispatch and production verification.
