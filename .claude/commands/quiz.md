Quiz me with ONE question on a skill-tree node, pitched at the node's next mastery level, and set in a context that matters to my research or curiosities. The skill-tree rules (levels, gating, rust) are in CLAUDE.md §6; `Scripts/skill_trees.py` enforces them, so always use it rather than working levels out yourself.

**Sources.** Prefer questions grounded in real use: a step in a research paper (strongly preferred), a result from a textbook or lecture notes I'm *not* reading, or a known application. Never use exercises from textbooks I'm reading (any book cited in a vault note footnote or listed in the research profile), since I may already have solved them. Make up a question yourself only when no relevant real-world setting fits.

## If there's a pending question
If `Learning/Quiz Log.md` has a question under `# Pending` and my input looks like an answer to it, skip to **Grading**. If my input is a new request instead, grade the pending one as Incorrect (skipped) with `record` as in Grading step 3, log it, and continue.

## Choosing the question
1. **Pick the node.** Run `python3 Scripts/skill_trees.py next`, adding `--tree "<Tree>"` if my input names a field, or `--node "<Note Title>"` if it names a concept. It returns the node, the level to ask at, and why it was chosen:
   - *frontier (progressive order)*: the earliest unlocked node in the tree that is below L3, so I build up concepts in order.
   - *rust check*: a mastered node whose rust interval has passed; ask at its current level. A clean pass doubles its interval.
   - *review*: a random mastered node (L3+), asked at the next level.
   - *placement check*: a node whose level was set by `/place`; ask at its current level to confirm it. Recording the answer clears the check.
   Never pick a node yourself, and never ask about a node the script says is locked. If my input says "easier", ask at the node's current level instead (practice only: it confirms the level but gives no progress). If the script reports no converted trees, or that the named concept isn't in a tree, tell me and stop.
2. **Read state.** Read the node's note and its prerequisites' notes (at most 5 notes) so the question uses my notation and conventions (e.g. O'Neill signs in differential geometry) and assumes only the node and its prerequisites, plus anything else at L2 or higher. Read the recent entries in `Learning/Stuck Log.md` and the last ~10 History entries in `Learning/Quiz Log.md`; if the node was involved in a past stuck point, aim the question at that missing idea in a new setting.
3. **Match the level.** The question must test exactly the ability of the target level, for this node:
   - **L1 Recall:** state the definition or theorem precisely, with all hypotheses.
   - **L2 Apply:** apply it directly; check whether its hypotheses hold in a given situation; true/false with a short justification.
   - **L3 Prove:** a short proof or counterexample using it; show why a hypothesis is needed.
   - **L4 Wield:** a multi-step proof combining it with other results, or constructing a non-obvious object or counterexample.
   - **L5 Command:** connect it across topics, generalize it, or use it on a research problem.
   L1 questions can be asked directly, and are **closed-book**: remind me not to open my notes for them. L2+ questions are open-book (vault notes allowed). For L2+, mix *understanding* and *application* questions (CLAUDE.md §5) and vary the format: prove, disprove, find a counterexample, true/false and why, compute, "what goes wrong if...", "state the converse and decide it".
4. **Find a relevant setting (L2+).** Read `Learning/Research Profile.md` (projects, courses, papers) and use the core toolkit in CLAUDE.md §4. Look for where the concept is used in my projects, the core toolkit, an upcoming course, or my curiosities, searching both my references and the internet:
   - Papers I'm reading or building on (profile), and papers/resources in `REFERENCES.md`: `rg` it for the concept's specific technical terms and for the note title (entries end with `[[Note]]` links), and look at the relevant section.
   - A paper found with WebSearch (prefer 2023+, arXiv or major venues such as SIGGRAPH, CVPR, ICCV, NeurIPS, ICML, ICLR, or applied math journals) related to my projects, where the concept appears in a derivation, proof, or assumption. Fetch the paper to confirm it exists and says what you attribute to it; never cite from memory. Good material: "why does this lemma in the paper hold?", "which hypothesis of <theorem> does this step need, and is it satisfied?", "the paper says X follows from Y: prove it", "does this assumption actually hold for real data/images/meshes?".
   - Textbooks or lecture notes I'm not reading (also found by search).
   Spend at most ~3 web searches on this. If nothing fits within that budget, write your own question, still framed around my research area where that's natural.
   Turn the source into a **self-contained** question: give enough of the setup (notation, assumptions) that I can answer without reading the paper, and adapt it to the target level instead of copying it verbatim.
5. **Verify before asking.** Solve the question completely in private. Make sure it is true or false as intended, well-posed, solvable with what I know, and tests the target level. Don't trust a source's claim just because it's published: check the step yourself, and if the paper's argument has a gap, that can itself be a good question ("find the missing hypothesis"). If anything is shaky, change the question. Never ask something you haven't solved.
6. **Record the source.** If the question comes from a paper or resource not yet in `REFERENCES.md`, add it now (even if I end up skipping the question), only after you've confirmed it exists. Put it in the most appropriate `##` section, or create a new section in the same style if none fits. Match the existing entry format:
   `- Authors (Year). *Title*. Venue. [arXiv:XXXX.XXXXX](url) — [[Related Note]]`
   If it's already there, add the related `[[Note]]` link to its entry if missing. Self-generated questions add nothing.
7. **Ask.** Write the node, the level asked, the question, and its source under `# Pending` in the log (no solution). Then show me:
   `**Node:** [[<Note>]] (<Tree>) · **Level:** L<k> <Rank> · **Progress:** <progress line from the script> · **Format:** <e.g. short proof>` followed by the question, then one line `**Context:** <why this matters, e.g. "used in <paper> to justify <step>">` with a link to the source (omit the line for self-generated questions). Stop and wait.

## During the question
- If I ask for a hint, give one at a time (locate → idea → next step, as in `/stuck`) and count it. Two or more hints means the answer can't count toward a level-up.
- If I say "skip" or "I don't know", treat it as Incorrect but explain the solution.

## Grading
1. Re-solve the question carefully, then grade my answer as **Correct** (valid and complete in its ideas for the target level; I answer with proof sketches, so judge the reasoning, not the presentation, per CLAUDE.md §5 *Grading sketches*), **Partial** (right idea but a gap or error), or **Incorrect**. Grade per concept (CLAUDE.md §6, *Per-part credit*): judge the node only on the parts that use its concept, and note any correct part that isolates a different node for bonus credit.
2. Feedback: say what was right, quote any flawed line and say exactly why it's flawed (as in `/check`), then give a concise model answer that builds on results from my notes (linked) where possible. If I got it wrong, connect the missing idea to something I already know. If my answer is correct but takes a different route, say so and briefly mention the other route only if it teaches something. For paper-based questions, add one sentence on how the result is used in the paper.
3. **Record it:** `python3 Scripts/skill_trees.py record "<Note Title>" --level <k asked> --result correct|partial|incorrect --hints <n>`. For each bonus node, also run `record "<Other>" --level <level that part tested> --result correct --bonus` (up to 15; the script ignores it unless that level is the node's current or next level). This updates `Gamification/mastery.yaml` and recolours the trees. Then clear `# Pending` and prepend a `# History` entry to `Learning/Quiz Log.md` with the script's result line.
4. If I got it wrong because of a real gap (not a slip), prepend an entry to `Learning/Stuck Log.md` with source "quiz: <node>", and offer (don't do without a yes) to add the question to the node's `# Questions` section as a card. If the gap is in a *prerequisite* (not the node itself), also recalibrate that prerequisite as in `/stuck` step 8.
5. End with one line on progression, celebrating level-ups (e.g. "**Level up!** [[Fatou's Lemma]] is now L3 Prove (Mastered), which unlocks [[Dominated Convergence Theorem]]"); otherwise state the progress toward the next level. Use `status --tree "<Tree>"` to see what a level-up unlocked.

My input:
$ARGUMENTS
