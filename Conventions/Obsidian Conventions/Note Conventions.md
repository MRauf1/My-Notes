# Note Conventions

- The main headers are of size `h1`, and sub-headers are of progressively smaller sizes (i.e. `h2`, then `h3`, and so on).
- All links must always have a custom text (i.e. of the form `Link Title|link text`) even if it is redundant (e.g. `Integer|integer`). This is done for future-proofing so that if I were to change the title of a note, I don't have to go through each backlink to fix the text.

TODO:
- Add a hotkey or something to make this (links with custom text) faster to write and reduce redundancy.
- Reintroduce this?
Add the necessary aliases to every note. Aliases give rise to unlinked mentions, which can help to discover connections that may have been missed or forgotten. For aliases, include every form the note/topic may appear in (e.g., for nouns, include both singular and plural form, for verbs, include the different tenses, for math operations, include their symbols).
- This vs linking only the first? Need to decide
Link every occurrence of a topic inside a note. This is done for future-proofing so that if I were to change the contents of the note (e.g. dividing a note into two separate notes), I wouldn't need to go through the note and update the links. **TODO: this could result in way too many links, which could be very distracting. See how the current scheme goes and make adjustments if necessary.** **TODO: Currently only linking non-LaTeX content. Decide on whether to link LaTeX content too and proceed accordingly.**
- Should the LaTeX math convention be only for callouts? What about outside of callouts?