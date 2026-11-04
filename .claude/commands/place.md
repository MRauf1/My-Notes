Run the skill-tree placement test: a short adaptive test that sets my starting mastery levels (rules in CLAUDE.md §6). `Scripts/skill_trees.py` chooses every question target and applies every result, so never pick nodes or set levels yourself.

## Loop
1. **Get the target.** Run `python3 Scripts/skill_trees.py place-next "<Tree>"` if my input names a tree; otherwise run `place-next` with no tree, which continues bottom-up with the first unfinished tree (`place-order` shows the order). If it prints `done`, go to **Finish**.
2. **Ground it.** Read the node's note and at most 3 of its prerequisites' notes, so the question uses my notation and conventions (e.g. O'Neill signs in differential geometry).
3. **Write ONE question** that tests exactly the target level for this node:
   - **L2 Apply:** apply the result directly, check whether its hypotheses hold in a concrete situation, or answer true/false with a one-line justification.
   - **L3 Prove:** a short proof, a counterexample, or why a hypothesis is needed.

   Aim for 2–5 minutes of my time. Make it self-contained, with no web or paper sourcing (that's for `/quiz`), and never use an exercise from a book I'm reading. Solve it yourself first and make sure it's well-posed and tests the node rather than a neighbouring concept.
4. **Ask** in this format: `**Placement** · [[<Node>]] (<Tree>) · L<k> <Rank> · question <n>/<budget> of this stage`, then the question. Stop and wait.
5. **Grade per concept** (CLAUDE.md §6, *Per-part credit*), pass or fail for each node. The target node passes if every part that uses its concept is right; errors confined to parts testing other concepts don't count against it. Hinted or "I don't know" answers on the node's parts are a fail. I answer with proof sketches: grade the validity of the ideas, not the presentation (CLAUDE.md §5, *Grading sketches*). Don't give hints during placement; tell me "I don't know" is fine and saves time.
6. **Record:** `python3 Scripts/skill_trees.py place-record "<Node>" --level <k> --result pass|fail`. If a correct part isolated another tree node (its concept appears in no wrong part), also run `place-record "<Other>" --level <level that part tested, 2 or 3> --result pass --bonus` (up to 15 per question; never a bonus fail). Then give one line of feedback: correct or not, plus the key idea if I missed it. Give the full model answer only if I ask.
7. **Log** a line under `# History` in `Learning/Quiz Log.md` (newest first): `- **YYYY-MM-DD** | [[Node]] (<Tree>) | L<k> | placement pass/fail | Q: <one-line summary> | Result: <script output>`.
8. **Continue immediately** with step 1 for the next question in the same turn, until the tree is `done` or I say "stop" or "pause". The state is saved after every answer, so I can resume later with `/place`.

## Finish
When a tree is done:
- Show `place-status "<Tree>"` and that tree's stats line (the `**Mastered:**` line at the top of its file in `Gamification/Skill Trees/`).
- Summarize in 2–3 sentences where my L2 and L3 boundaries fell, naming notable strong and weak areas.
- Then offer to continue with the next tree from `place-order`.

Placed levels are provisional: `/quiz` re-checks each placed node once at its placed level, so an occasional lucky or unlucky placement answer corrects itself. Remind me of this the first time.

My input:
$ARGUMENTS
