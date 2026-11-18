Grade my solution to a textbook exercise, or my proof of a theorem from the section I'm studying, like `/check` does, then credit it to the skill trees with **placement rules** (CLAUDE.md §6, *Exercise credit*). Use `/exercises` for work done while progressing through a textbook. `/check` is for problems I come across outside that, and it keeps its own credit rules.

**Pick the mode from my input:**
- **Mode A (grade and credit):** the input contains an exercise or theorem statement together with my solution. Follow steps 1–6.
- **Mode B (plan):** the input is only a book and section/chapter (e.g. "Hogg 1.4"), or it is empty. Follow **Mode B** below. When it's empty, use the section from the most recent `/note` or `/exercises` in this chat. If there is none, use the latest `exercise` Source in the Quiz Log, and say which section you picked. Ask only if none of these exists.

## Mode A: grade and credit

1. **Get the inputs.** You need the source (book, section, exercise or theorem number), the exact statement, and my solution (text, LaTeX, or an image path). If the statement is missing, ask for it and stop. If the book or section is unclear, ask once. Several exercises in one message are graded and recorded one at a time, in the order given. Read the vault notes for the concepts involved (within CLAUDE.md §2's limits) to see which definitions, conventions, and results I have available.
2. **Grade it** exactly as `/check` steps 2–6 do (`.claude/commands/check.md`). Read line by line, then report issues labeled Error, Gap, Imprecision, or Style, with level-2 hints for errors and gaps. Give a verdict (*Correct*, *Correct with gaps*, or *Incorrect*), plus an optional perspective. I write proof sketches, so grade the ideas, not the presentation. For a theorem from the text, grade my proof against the statement. The book's proof is a valid reference, but other routes count too.
3. **Choose nodes, levels, and results.** List every node (at most 15) whose concept the solution genuinely uses in a non-routine step (CLAUDE.md §6, *Downward credit*, counterfactual test), with exact note titles. Skip notation, routine algebra, and definitions merely mentioned. For a theorem I proved, the theorem's own node is always included at L3.
   - **L2**: a computation or direct application (evaluate, solve, check hypotheses, apply the result).
   - **L3**: a short proof, a counterexample, or a decision that needs one. This is the cap for nodes from the section being studied.
   - **L4 / L5**: only for a prerequisite from an *earlier* section or another tree. L4 needs the node already at L3, and the solution must combine it with other results in a genuinely multi-step argument. L5 needs the node already at L4, and the solution must connect it across topics, generalize it, or use it in research. The script raises that node to L4/L5 and its ancestors to L3.

   Each node gets **pass** if every step that uses it is right, and **fail** otherwise. A Gap or Error in a step using the node counts as a fail, and so do 2+ `/stuck` hints on that step. Errors confined to steps about other concepts don't count against it (per-part credit). Before recording, check in one batch that each candidate note exists, which tree it lives in, and its current level in `Gamification/mastery.yaml`. When a concept has no note, don't create one: credit the nodes that exist and list the missing concepts in the report.
4. **Record.** First, look at the ancestors a pass would raise. Run `python3 Scripts/skill_trees.py tree-for` as needed, or do a dry read of the tree edges. Exclude an ancestor only if the edge is wrong (offer to fix it), if the note is a genuinely different concept (e.g. the 1-form [[Differential]] vs. $dy=f'(x)\,dx$), or if I've said I don't understand it yet (e.g. [[Differential Form]]). A more general form of the same concept is fine to raise. Then record all nodes in **one** call:
   `python3 Scripts/skill_trees.py exercise-record --node "<Node>" <K> pass|fail [--node ...] [--exclude "<Ancestor>" ...]`
   - **Pass:** raises the node and every ancestor (in every tree) to $K$, and marks each raised node *provisional*. The next `/quiz` on a provisional node is a placement check at its level, and a fail there drops one level.
   - **Fail:** changes nothing.
   - Levels are never lowered, and nodes already at $K$ or above are untouched.

   Skip credit entirely if I say I worked from a solution.
5. **Log.** Prepend one `# History` entry per exercise to `Learning/Quiz Log.md`, directly under the format comment. Read only the top of the file to Edit it.
   `- **YYYY-MM-DD** | [[Node]], ... (<Tree>) | L<K> | exercise <verdict> | Q: <problem, one line> | Source: <book> §<section>, Ex./Thm <n> | Result: <script output, including the raised line>`
   For each Error or Gap that reflects a real misunderstanding, prepend a Stuck Log entry (source "exercise: <book § Ex. n>") and run `python3 Scripts/skill_trees.py archive-logs`. Exercise credit never lowers a level, so there is no recalibration. A genuine concept error goes through `/stuck` if I want it applied.
6. **Report.** Append a `## Exercise: <book> <§> Ex. <n>` section to `Learning/Session.md` with three parts: the referee report and verdict, the nodes with pass/fail, and what the script raised. Then offer (don't do without a yes) a re-do card for any Error. The chat reply is 1–3 sentences: the verdict, the headline raises, and any missing notes.

## Mode B: plan the minimal exercise set for a section

Don't grade or credit anything in this mode. Only the recommendation is produced.

1. **Find the PDF.** Get the Zotero key from the footnotes of notes that cite the book: `rg -o "\[<Book title>\]\(zotero://open-pdf/library/items/[A-Z0-9]+" Notes`. The PDF is in `~/Documents/PKM_System/Zotero/storage/<KEY>/`. Footnote `page=` values are PDF page numbers. Find the section's page range from its heading and the next section's heading. Extract the text with `pdftotext -layout -f <a> -l <b>` into the scratchpad, and read the whole section: the definitions, the theorems with their proofs, and the exercise set.
2. **Direct nodes.** These are the notes whose footnotes cite pages in the section (`rg -l "<KEY>?page=(a|...|b)\b" Notes`), plus any notes `/note` created from the section in this chat. Read their current levels and `provisional` flags from `Gamification/mastery.yaml`, and their ancestors from the tree edges (a short Python script over the `skilltree` blocks).
3. **Candidates.**
   - **What counts:** every exercise in the section's set, and every theorem, proposition, or lemma the section proves. Proving a theorem yourself is a candidate at L3 for its node.
   - **What to drop:** anything already done. That means items graded in this chat, and items with a Quiz Log `exercise` entry for this source (`rg -F "Source: <book> §<section>" Learning/`).
   - **What each candidate would credit:** the direct nodes it would pass, at L2 (application or computation) or L3 (proof, counterexample, or a decision needing one), judged as Mode A step 3 would grade the expected solution. Skip exercises that need software (e.g. "write R code") unless they also contain a pen-and-paper part, and count only that part.
4. **Targets.** A direct node's target is the highest level any candidate reaches for it, capped at L3. A node already at its target (provisional or not) needs nothing.
5. **Minimal cover.** A pass at $K$ also raises every ancestor to $K$, so the cheapest cover takes the **deepest** node of each chain at its target level. Choose the smallest set of candidates that brings every direct node to its target, counting the ancestor raises. Solve it exactly when it's small (it usually is); otherwise use greedy max-coverage and say so. Among equal-size sets, prefer:
   - proofs of the section's own theorems,
   - then exercises that also exercise more nodes,
   - then shorter ones.
6. **Report** in a `## Exercise plan: <book> §<section>` section of `Learning/Session.md`:
   - **The set:** a table with one row per chosen item: the exercise or theorem number, a one-line description, the level, and the nodes it settles, both directly and through ancestors.
   - **Unreachable:** direct nodes no candidate reaches, with their current level. Suggest `/place` at the end of the book, or `/quiz`.
   - **Optional extras:**
     - exercises that would also raise an earlier-section prerequisite to L4 (if it's already at L3) or to L5 (if it's already at L4), kept separate from the minimal set;
     - one or two interesting exercises the cover doesn't need, if any stand out.

   The chat reply is 1–2 sentences: how many items, and how many nodes they settle.

Input:
$ARGUMENTS
