Run a **recall round**: a quick closed-book batch of L1 Recall questions that opens the skill trees for reach quizzes (CLAUDE.md §6, *Recall rounds*). Each node's L1 is "state the definition or theorem precisely, with all hypotheses", from memory.

1. **Pick the nodes.** Run `python3 Scripts/skill_trees.py recall-next --count <N>` (default 10; add `--tree "<Tree>"` if my input names a field, or use the count I give). It lists unlocked L0 nodes, research spine first, prerequisites before dependents. Never pick nodes yourself.
2. **Ask.** Read each node's note (only the callout at the top) so the expected statement uses my notation. Write the list under `# Pending` in `Learning/Quiz Log.md` as `recall round: <titles>`. Then show me the numbered list: for each node, one line naming the concept and what to state (e.g. "State the Spectral Theorem for real symmetric matrices, with hypotheses."), without giving away the statement. Remind me it's **closed-book**: answer all of them before opening any notes. Stop and wait.
3. **Grade** each statement separately as **Correct** (precise, every hypothesis present; wording may differ, and an equivalent formulation counts), **Partial** (right idea, a hypothesis missing or a condition wrong), or **Incorrect** (wrong or blank). Give the correct statement for every one that wasn't Correct, quoting my flawed phrase and saying exactly what was missing. Keep feedback short: one or two lines per node.
4. **Record** each node: `python3 Scripts/skill_trees.py record "<Note Title>" --level 1 --result correct|partial|incorrect`. An L1 level-up can cascade through banked L2/L3 credit from earlier quizzes; report those level-ups (and any `audit flagged` lines).
5. **Log.** Clear `# Pending` and prepend one `# History` entry (Read only the top ~25 lines of the log to Edit it): `- **YYYY-MM-DD** | recall round (<N> nodes) | L1 | <correct>/<N> correct | Hints: 0 | Q: <titles with result, e.g. [[Eigenvalue]] ✓, [[Eigenvector]] ✗ (missing v ≠ 0)> | Source: own | Result: <script lines joined with ; >`. For a statement that was wrong because of a real gap (not a slip), prepend an entry to `Learning/Stuck Log.md` with source "recall: <node>".
6. End with one line: how many nodes reached L1, any cascades, and which reach anchors that opened (run `next` only if I ask for a quiz).

Follow the session-file rule in CLAUDE.md §5 for the questions and grading.

My input:
$ARGUMENTS
