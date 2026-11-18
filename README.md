# pstack for Hermes

An unofficial Hermes Agent port of [Lauren Tan's pstack](https://github.com/cursor/plugins/tree/35a90942a7f02e1ebbc2443643179815f2147954/pstack). It routes coding tasks to 22 playbooks and maps 34 specialist modes and 24 engineering principles onto Hermes' existing tools. It is not the Cursor plugin, and it does not install background automation or authorize GitHub writes.

## Install

Clone this repository with an account that has access. Review `skills/pstack/` before installing it. Copy that directory into the active Hermes profile's `skills` directory. The commands below use the default profile and refuse to overwrite that destination:

```sh
git clone git@github.com:EMRD95/pstack-hermes.git
cd pstack-hermes
skills="${HERMES_HOME:-$HOME/.hermes}/skills"
mkdir -p "$skills"
mkdir "$skills/pstack" && cp -R skills/pstack/. "$skills/pstack/"
```

If you already have a `pstack` skill under a category such as `skills/software-development/pstack`, back it up and move it outside the profile's `skills` directory before installing. Keep just one copy. Start a new Hermes chat if the slash command is not visible.

```text
/pstack help
/pstack bug-fix: reproduce the typing stutter and verify the fix
/pstack interrogate: review this diff without editing it
```

The skill can also be preloaded with `hermes chat --skills pstack`. This port does not require Cursor, additional Python packages, or a special model configuration. Some playbooks depend on tools that your task actually needs, such as a browser for UI evidence or a project-specific checker for formal verification.

## Verify and contribute

```sh
python3 -B skills/pstack/scripts/check-port.py
python3 -B -m unittest discover -s tests -v
```

For upstream parity, add `--upstream <cursor-plugins-checkout>` at the revision recorded in [upstream.md](skills/pstack/references/upstream.md). That check verifies inventory and attribution, not the quality of every agent run. For changes to the playbooks, describe the observed behavior and include a reproducible check with the diff. Keep runtime settings, transcripts and private evidence outside the repository.

Original pstack by [Lauren Tan](https://github.com/poteto), MIT licensed. See [LICENSE](LICENSE) and [upstream.md](skills/pstack/references/upstream.md).
