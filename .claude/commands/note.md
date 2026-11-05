Process the following raw highlighted reading material into atomic Zettelkasten notes:
1. Identify the core atomic concepts/theorems.
   - **Tags:** use the domain and subdomain tags I give as the default. If a concept clearly belongs to a different subdomain, use that one instead and tell me which and why. Base this on what the concept *is*, not where I read it: e.g. a Fourier-series theorem met in a vision book is still analysis. Prefer existing subdomain tags (listed in `Gamification/tree_tags.yaml`, plus non-technical ones used in the vault). Keep my tag as a secondary tag when the concept really spans both fields. Domain and subdomain tags decide the Anki deck and the skill tree.
2. Extract the citation and attach it to the generated notes.
3. Check note titles in `Notes/` to resolve internal [[Wikilinks]]. When reading a candidate note to decide links or patches, read only its first ~20 lines (tags and definition callout), never the whole file. Never print a skill tree's source block; look nodes up with `rg` instead.
4. Write the new notes and patch reciprocal links in relevant existing notes.
5. For notes on substantive theorems, propositions, or lemmas (not plain definitions or minor facts), add a `# Questions` section with the three card kinds defined in CLAUDE.md §5:
   - 1-4 *Understanding* cards.
   - At most 2 *Application* cards, only when the connection to a project in `Learning/Research Profile.md` is genuine. Read the profile before writing them.
   - At most 1 *Connection* card, only when the same idea appears precisely in another subfield, preferably one with a vault note (link it). Give the dictionary and where it breaks.
   - **Whole-document input** (an entire paper, chapter, or lecture note rather than my highlights): at most 2 cards per note in total, and no cards for corollaries or minor results.
   Only include questions you can answer with certainty, and verify every counterexample and cited paper. Skip a question rather than guess. If the note already has a `# Questions` section, add to it without duplicating existing questions.
6. **Add each new note to the skill trees** (rules in CLAUDE.md §6). Every note in a technical domain (`mathematics`, `statistics`, `computer_science`, `physics`) gets a node. Skip notes in other domains unless their subdomain tag has a tree in `Gamification/tree_tags.yaml`.
   - **Planned nodes first.** Before naming a new note, check whether a planned node already stands for the concept: `rg -i '<keyword>' "Gamification/Skill Trees/"`. If one does, title the note exactly as the node's label when that fits the vault's naming conventions; the node then becomes Discovered automatically and needs no `add`. If the note needs a different title, run `python3 Scripts/skill_trees.py rename "<Planned Title>" "<Note Title>"` instead of adding a duplicate node, then add any missing prerequisite edges with `edge`.
   - **Tree = subdomain tag.** Run `python3 Scripts/skill_trees.py tree-for "<Note Title>"`; it prints the tree of the note's first subdomain tag. If it prints `NO TREE`, create the tree: add `<Tree Name>: <tag>` to `Gamification/tree_tags.yaml` (Title Case of the tag, as the existing entries do), then pass `--create` to the first `add`, and tell me.
   - Prerequisites are the notes this one directly builds on: the linked concepts needed to *state* or *prove* it (usually links in the definition callout). Links in Types (subtypes depend on this note, not the reverse) and loosely related Properties links are not prerequisites. List only direct prerequisites: skip A when A → B → this note already holds.
   - Run `python3 Scripts/skill_trees.py add "<Tree>" "<Note Title>" --prereq "<Prerequisite>" ... --group "<Group>"`, using the note's place in the source (chapter or topic) as the group. New nodes start at L0 Discovered. If the script says a prerequisite isn't in any tree, add that prerequisite first (to its own field's tree, with only the prerequisites it already has in the trees), then retry.
   - For existing notes you patched with a link to the new note, if the new note is a prerequisite of that existing note and both are in trees, add the edge: `python3 Scripts/skill_trees.py edge "<New Note>" "<Existing Note>"`.
   - Finish with `python3 Scripts/skill_trees.py check` and fix anything it reports.

Raw Input:
$ARGUMENTS
