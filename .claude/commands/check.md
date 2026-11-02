Grade my proof or solution strictly, like a careful referee. Point out problems; do not rewrite the proof.

1. **Get the inputs.** You need the exact statement being proved and my proof (text, LaTeX, or an image path). If the statement is missing, ask for it and stop. Read the vault notes for the concepts involved (within CLAUDE.md §2's limits) to check which definitions and conventions I'm working with and which results I have available.
2. **Read line by line.** For every step ask: is it true, and does it follow from what came before plus the hypotheses? Track which hypotheses are used. An unused hypothesis means either it's unnecessary or the proof has a hole; say which.
3. **Report issues** in order of appearance, each quoting the exact line it refers to, labeled:
   - **Error:** a false claim or invalid inference. Give a counterexample to the step when possible.
   - **Gap:** true but non-trivial and unjustified. Name what's needed to fill it.
   - **Imprecision:** quantifier order, undefined objects, dependence of constants (e.g. $N$ depending on $\varepsilon$), notation.
   - **Style:** only if it hurts readability. Keep it to at most 2.
   For errors and gaps, give a level-2 hint toward the fix (the idea, not the repair), pointing to a result I already have a note on when one does the job (`[[Note]]`). If I reproved something the vault already has, mention that I could cite it. Give the full repair only if I ask.
4. **Verdict:** one of *Correct*, *Correct with gaps*, or *Incorrect*, plus one sentence on the overall strategy (is it the right approach even if execution failed?).
5. **Calibrate.** Don't invent issues to look thorough. If the proof is correct, say so plainly. If you're unsure whether a step is valid, say so and explain why, rather than ruling either way.
6. **Log, recalibrate, and offer.** For each Error or Gap that reflects a real misunderstanding (not a typo), prepend an entry to `Learning/Stuck Log.md` under `# Entries` with source "check: <problem>". For each **Error** that comes from misunderstanding a specific concept, recalibrate that node as in `/stuck` step 8. Then offer (don't do without a yes) a re-do card in the `# Questions` section of the most relevant note.

Statement and my proof:
$ARGUMENTS
