Turn the following commands into Anki command cards:
1. Group the commands by tool/language and pick the target file `Commands/<topic>.yaml` (kebab-case stem, e.g. `git.yaml`, `pacman.yaml`, `python-builtins.yaml`, `numpy.yaml`). Reuse an existing file if one fits; follow the schema in the docstring of `Scripts/commands_to_anki.py`.
2. Get the documentation for each command. Use any documentation pasted below first. Otherwise prefer the installed version's docs (`man`, `<cmd> --help`, `git help`, `python -c "help(x)"`, `pydoc`), then fall back to the official online docs. Never write from memory alone when a source is available, and record the most specific page as `source`.
3. Write one entry per command. The card is shown command → meaning, so:
   - `command`: exactly as it would be typed or called (include the flags/arguments being learned).
   - `meaning`: one crisp sentence saying what it does.
   - `details`: only the key flags, variants, signature, or gotchas (Markdown, a few lines at most).
   - `example`: only if requested.
   - If the command already exists in the file, update that entry instead of adding a duplicate.
4. Run `python3 Scripts/commands_to_anki.py`, fix any reported errors, and report the files touched and the card count. The user imports `Scripts/output/Commands.apkg`.

Commands:
$ARGUMENTS
