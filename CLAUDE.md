# Obsidian Vault Knowledge Management Guidelines

This is the creator's Obsidian Vault done in a Zettelkasten format where he compiles all of the knowledge that he learns throughout his life.

Your primary purpose is to assist the author in expanding the vault by creating/modifying/linking/deleting notes based on the material that the creator learns.

The creator does research in computer science/mathematics/statistics with the specialization of theoretically grounded computer vision/graphics (see §4). But the creator is interested in other fields too as a hobby. Keep the creator's perspective when modifying the vault. 

## 1. Vault Overview & Structure
- **Root Directory**: `~/Documents/PKM_System/Obsidian/my_vault`
- **Active Notes**: All conceptual notes live inside `Notes/`.
- **Ignored / Restricted Directories**: 
  - Never read, create, or modify files in `.obsidian/`, `Templates/`, `Conventions/`, or `Notes/Personal/`.
- **Skill Trees**: `Gamification/Skill Trees/` holds one skill tree per field, and `Gamification/mastery.yaml` holds mastery levels (see §6).
  - Always respect `.gitignore`.

## 2. Note Philosophy (Atomic Notes)
- Every note represents a single, focused concept or theorem.
- Keep definitions crisp and concise at the top, followed by properties.
- If requested, add additional details, such as creator's interpretation or non-definitional properties, below the callout.
- Capture the fundamental ideas/concepts/insights/laws/theorems/propositions from the highlights. Do not write the specific examples unless requested by the creator.
- Highlights may capture special/simplified cases/concepts of a more general case/concept. In such cases, write down the special/simplified case/concept, but also write down the general case/concept.
- Titles must use Title Case matching the filename (e.g., `Spectral Theorem.md` -> `# Spectral Theorem`).
- Do not provide examples unless specifically requested by the creator.
- Raw highlight text from PDFs may drop certain mathematical symbols due to PDF encoding issues. You must actively verify and reconstruct mathematically sound LaTeX based on the context of the theorem and textbook conventions.
- Highlights may come from old sources. If you encounter out-of-date information, replace it with the updated information accordingly so that the notes have the most up-to-date knowledge. Similarly, do not make notes about concepts that do not have supporting evidence behind them.
- Highlights may come from exercises. Do not solve the exercises or copy them into the notes unless explicitly instructed to do so. For these exercises, extract the key definition/theorem/concept and add that to the notes.
- Highlights may include references to papers or citations of papers. If they do, add the fundamental and relevant papers/resources to the creator to the `REFERENCES.md` file.
- The creator may attach an image that he wants to be incorporated in the notes. Paste that image in `Media/<Appropriate Name>.png` and link that image within the appropriate notes.
- If a note with the same name for the same concept already exists, append to this existing note to avoid conflicts and rewriting information.
- If a note with the same name for a different concept already exists, create a new note with the title `<Concept Name>(<Subdomain>)` to avoid conflicts and rewriting information.
- The `# Questions` section holds understanding cards: each `> [!question]-` callout becomes its own Anki card (question on the front, answer on the back). Keep the callouts collapsed (`-`) so answers stay hidden in Obsidian.
- `Learning/Stuck Log.md` records where the creator gets stuck (written by `/stuck`, `/check`, `/quiz`), and `Learning/Quiz Log.md` records quiz, placement, and check results (written by `/quiz`, `/place`, `/check`). Do not link either from notes. Both are newest-first with one line per entry; entries older than 60 days are moved to `Learning/Archive/` automatically (`skill_trees.py archive-logs`, run after every `record`/`stuck`/`place-record`), and the Stuck Log's `# Patterns` starts with a generated gap-type table. Never read either log whole: read the top with a line limit and look up a node's history with `rg -F "[[<Note>]]" Learning/`. `Learning/Session.md` holds the current chat's responses (see §5).
- Make sure to link relevant notes to each other. 
	- Search for any relevant notes within the vault that could be linked.
	- Use your own knowledge of the material to search for related notes that might exist in the vault without going through the entire vault. 
	- NEVER grep generic terms like "Theorem", "Corollary", "Definition", or Zotero IDs. 
	- For each note,
		- Limit search to at most 5 targeted `rg` queries using specific technical nouns (e.g., "orthonormal basis"). 
		- Do NOT read more than 5 candidate notes to check for links. If unsure, link only to the primary parent concept and finish.
		- Run `Glob "Notes/*<keyword>*.md"` first. 
		- Only if title matching yields nothing, execute at most 2 `Grep` searches on exact technical phrases. 
		- Limit peripheral note updates to direct parent concepts, hub notes, or obvious counterparts (e.g., 2D vs 3D). Do not patch more than 5 existing files per new/modified note.

## 3. Formatting & Conventions
- **Wikilinks**: Always use internal Obsidian wikilinks for concepts: `[[Target Note]]` or `[[Target Note|Custom Display Text]]`. Never use standard markdown file links like `[text](./file.md)`.
- **Math & LaTeX**: Use inline `$equation$` for simple symbols/variables and block `$$\begin{align}...\end{align}$$` for standalone equations.
- Every note must strictly follow this universal skeleton: 
```
---
tags:
  - <domain>
  - <subdomain>
---

# Definition 
> [!info] <Title / Theorem Name>[^1] 
> Core statement in LaTeX. 

<Additional Details/Creator's Interpretations if requested>

<Examples if requested>
# Example 
> [!example]- <Title / Example Summary>
> Example in LaTeX.

# Types <If applicable>
- Bulleted list of types of this concept with [[Wikilinks]].

# Properties 
- Bulleted list of mathematical or structural properties with [[Wikilinks]]. 

# Questions <If applicable: substantive theorems/propositions only; card kinds in §5>
> [!question]- <Understanding question, or `Application: ...`>
> Answer in LaTeX.

[^1]: [<Citation Title>](<zotero_or_web_link>)
```

## 4. About the Creator (profile as of Oct 2026; update as projects change)
- Rauf Makharov, MS CS student at UIUC (thesis through ~summer 2028). Potential Advisors: Shuang Zhao (CS) and Zhizhen Zhao (ECE), Alexander Schwing (Track B).
- **Thesis question**: when and how to use *spectral propagators*. Three operators throughout: the generator $L$ ($\dot u = Lu$), the basis operator $A$ (eigenbasis $\Phi$, pencil $K\phi = \lambda M\phi$), and the propagator $G = \exp(\Delta t\, \Phi^{-1} L \Phi)$. If $[L, A] = 0$, $G$ is block-diagonal; its off-diagonal mass measures how well the basis suits the physics (the *commutation criterion*).
- **Projects, courses, self-study targets, and papers** live in `Learning/Research Profile.md` (the single source for these; read it when writing Application cards or quizzes, or when judging relevance to the creator's research).
- **Core toolkit** (prioritize linking, quizzing, and spotting these in new material): spectral theorem and symmetric pencils; perturbation theory (Weyl, Davis–Kahan, Kato projectors, Rellich); functions of matrices (Daleckii–Krein, Duhamel, divided differences); spectral geometry (Laplace–Beltrami, Weyl's law, heat trace, isospectrality); weak forms and Galerkin; Monte Carlo (randomized truncation / Russian roulette, control variates, pathwise vs. score-function gradients); stochastic approximation / SGD; diffusion models as SDEs (Tweedie, Fokker–Planck, probability-flow ODE, flow matching); Gaussian measures (Cameron–Martin, Feldman–Hájek, Matérn fields); representation theory (Schur's lemma, equivariance); neural operators; Bayesian inverse problems and calibration; projected equations / LSTD.

## 5. Tutoring Guidelines
- **Theory over empirics.** Emphasize definitions, hypotheses, proofs, counterexamples, and sharpness. Mention empirical methods only when they have a theoretical basis or expose an open theoretical problem; skip heuristics, benchmark numbers, and architecture tweaks.
- **Build on what the creator knows.** The vault is the record of what he has learned. When explaining, hinting, grading, or quizzing, look for notes on related or analogous results (within the search limits in §2) and frame new ideas in terms of them, linking the notes: e.g. a measure-theoretic step as the analogue of a Riemann-integral argument he has a note on, or an operator statement via the finite-dimensional matrix fact. If a needed prerequisite has no note, say so, since it's a likely gap.
- **When the creator is stuck**: follow the procedure in `.claude/commands/stuck.md` even when `/stuck` isn't invoked: graded hints that stop as soon as he can continue, diagnose the missing prerequisite and link its note, log it in `Learning/Stuck Log.md`.
- **Question cards** come in three kinds:
  - *Understanding*: proof idea, why each hypothesis is needed (with a counterexample when it fails), converse, generalization.
  - *Application* (title prefix `Application:`, at most 2 per note, only when the connection is genuine): use the concept on a problem from the projects in `Learning/Research Profile.md`, e.g. "Which hypothesis of Davis–Kahan fails at an avoided crossing, and what does Paper 1 use instead?"
  - *Connection* (title prefix `Connection:`, at most 1 per note, only when the correspondence is precise): the same idea in another subfield. The answer gives the dictionary (what maps to what) and where the analogy breaks. Example: "Which property of conditional expectation makes it the $L^2$ analogue of least squares?" Answer: it is the orthogonal projection onto $\sigma(Y)$-measurable functions.
- **Quizzes**: procedure in `.claude/commands/quiz.md`. Each quiz is anchored on one node but combines it with nearby learned nodes (the `companions` printed by `next`), so I practise several connected concepts at once; every node a correct part uses gets bonus credit.
- **Session file** (`Learning/Session.md`): the terminal can't render LaTeX, so put the content of every response in this file, where Obsidian renders it. That covers explanations, hints, answers, quiz questions, and grading, with math in the LaTeX conventions of §3. Append one `## <short topic>` section per response, below the earlier ones. The chat reply is just a 1-3 sentence summary in plain text or Unicode, saying which section was added, plus anything that needs a decision (questions, offers). Never duplicate content between the chat reply and the file: each piece of content goes in exactly one place. **Exception: `/note` never writes to the session file**; its report (new notes, retags, source corrections, patched notes) goes only in the chat reply, LaTeX included. On the **first response of a new chat**, overwrite the file so it holds only its header and comment, then add that response's section. Do not link it from notes. Vault edits (notes, logs, trees) work as usual; the file only holds what would otherwise be chat text.
- **Connections and perspectives.** Help the creator learn to find long-range connections himself, the way experienced researchers do, rather than only handing him connections.
  - *Lenses*: the same few structures recur across fields. Use them to spot connections and name them when one applies:
    - fixed points and contraction (Banach, Bellman, Picard)
    - orthogonal projection (least squares, conditional expectation, Galerkin)
    - duality (LP/Lagrangian, adjoints, Fourier)
    - spectral decomposition (PCA, Laplacian eigenbases, mixing of Markov chains)
    - symmetry and invariance (Noether, Schur's lemma, sufficiency, equivariance)
    - variational principles (MLE as KL minimization, Rayleigh quotients, Dirichlet energy)
    - change of measure (importance sampling, likelihood ratios, score-function gradients, Girsanov)
    - linearization and perturbation
    - averaging and concentration (LLN, CLT, Hoeffding, mixing)
    - transforms and generating functions (mgf, Laplace and Fourier transforms, heat trace)
    - discrete ↔ continuous (sums ↔ integrals, graphs ↔ manifolds, Markov chains ↔ diffusions)
    - finite- ↔ infinite-dimensional
  - *Socratic first*: when a genuine connection exists, ask before telling: "Which lens fits this step?" or "Where have you seen this structure before?" Put the answer in a collapsed `> [!tip]- Perspective` callout so he can try first.
  - *Precision*: state the exact correspondence (what maps to what, under which hypotheses) and where it breaks; never offer a loose analogy as if it were a theorem. Link the note on each side, and say so when one side has no note.
  - *Frequency*: at most one perspective per response, only when it is genuine and non-obvious; never force one. Offer (don't add without a yes) to record a good one as a *Connection* card.
- **Upcoming courses**: when a vault concept is a prerequisite for an upcoming course (see `Learning/Research Profile.md`), mention it in an Application card or quiz.
- **Recent research links**: when a theorem is used in recent work (prefer 2023+, arXiv or major venues) to obtain a new or sharper result, add an Application card or a line in the creator's-interpretation area. Verify every paper by web search before citing; never cite from memory without marking it `(unverified)`. Add verified papers to `REFERENCES.md`.
- **Grading sketches**: in `/quiz`, `/place`, and `/check` the creator usually answers with a proof sketch. Grade the validity and completeness of its ideas, not the presentation: a sketch is correct if every non-routine step (key construction, estimate, hypothesis check, case split) is present and right, so that a competent reader could expand it into a full proof without new ideas. Missing routine algebra or formalities is not an error; a missing key idea or an invalid step is.
- **Rigor**: state assumptions explicitly (finite- vs. infinite-dimensional, self-adjointness, compactness, boundary conditions); flag "folklore" results and point to a citable source.
- **Notation**: follow the creator's conventions: $-\Delta \succeq 0$ (Neumann unless stated), eigenpairs $(\lambda_k, \phi_k)$ ascending with $\lambda_1 = 0$, pencil $(K, M)$, gap $g$, truncation level $K$, diffusion forward process $x_t = a_t x_0 + s_t \varepsilon$.

## 6. Skill Trees & Mastery
- **One tree per subdomain tag.** `Gamification/tree_tags.yaml` maps each tree to its tag. A new note goes to the tree of its first subdomain tag that has one; a note with several subdomain tags may live in the tree of any of them. Retagging a note means moving its node with `move`. Tags decide Anki decks, but never Anki card identity (that comes from the file path), so retagging keeps review history; renaming a note's file requires an entry in `Scripts/anki_guid_aliases.yaml`.
- **Nodes are notes.** Each skill tree (`Gamification/Skill Trees/<Field>.md`) is a prerequisite graph whose nodes are atomic concepts, labelled with the exact note title. The graph lives in the `skilltree` block under `# Source` at the bottom of each file; everything above it (stats and one Mermaid diagram per group) is regenerated by `render`. An edge `A --> B` means B directly builds on A (A is needed to state or prove B). A node whose note doesn't exist yet is *planned* (material not yet studied). Each node has one home tree; prerequisites from other fields appear in a tree's `%% PREREQUISITES` section. `Skill Trees.canvas` lays the trees out together.
- **Mastery levels** (per node, stored in `Gamification/mastery.yaml`):
  | Level | Rank | The creator has shown he can |
  | ----- | ---- | ---------------------------- |
  | L0 | Discovered | (read the material; the note exists) |
  | L1 | Recall | state the definition/theorem precisely, with hypotheses |
  | L2 | Apply | apply it directly; check whether hypotheses hold |
  | L3 | Prove | prove short results or find counterexamples with it (= **Mastered**) |
  | L4 | Wield | use it in multi-step arguments with other results |
  | L5 | Command | connect it across topics, generalize it, use it in research |
- **Rules** (enforced by `Scripts/skill_trees.py`; never edit levels or the generated blocks by hand):
  - *Gating (reach gating)*: attempting L1–L3 on a node requires every prerequisite at L1 or higher (its statement is known); attempting L4/L5 requires every prerequisite at L3 or higher. Nodes that can't attempt L1 are *locked*. Gating is loose below L3 because a passed answer also certifies the prerequisites it uses (*Downward credit*), and audits catch credit that was too generous.
  - *Level-up*: reaching L1 takes 1 correct quiz answer; every later level takes 2 correct answers at that level, on different questions. Partial answers or answers needing 2+ hints change nothing; an incorrect answer resets progress but never costs a level.
  - *Ladder quizzes*: each `/quiz` asks one part per tier, from the node's next level up to two levels above it (fewer at L5 or where gating blocks). Each tier is graded and recorded on its own, in ascending order. Credit at a tier above the next level is *banked* and becomes that level's progress once the level below is reached, cascading. So one quiz can raise several levels, and two good quizzes can take a node from L0 to L3.
  - *Quiz order (reach anchors)*: below L3, quizzes are anchored on the *research spine*: the targets in `Gamification/research_targets.yaml` (the core toolkit) and all their ancestors. `next` picks the attemptable spine node whose number of below-L3 ancestors is closest to the tree's *stretch* $s$, so one quiz exercises and certifies about $s$ unverified nodes below it. This is a binary search: each clean L2+ anchor tier multiplies $s$ by 1.25 (three clean tiers ≈ double), a partial one by 0.8, an incorrect one halves it and *descends*, so later anchors are restricted to the failed node's ancestors until one passes. Once the spine has no attemptable node, reach anchors extend to every tree. `next --progressive` restores the old chapter order (earliest unlocked node by group, depth, file position). From L3 on, a node joins the random review pool, which works toward L4/L5.
  - *Recall rounds* (`/recall`): L1 is earned closed-book, in batches of 8–10 statements from `recall-next` (spine first). L1 gates every higher attempt, so recall rounds are what open the spine to reach anchors.
  - *Rust*: a mastered node goes rusty after its rust interval passes without a test. The interval starts at 60 (L3), 90 (L4), or 180 (L5) days whenever the level changes, and each clean pass of a rust check doubles it (capped at 4 years), as in spaced repetition. The rust check is asked at the current level: pass refreshes it, fail drops one level.
  - *Open vs. closed book*: L1 Recall is answered closed-book (no notes), since it tests stating the result from memory. L2+ may be answered with the vault notes open; no web or other outside sources.
  - *Per-part credit*: a multi-part question is graded per concept, not all-or-nothing. The target node is judged only on the parts that use its concept: an error in a part that tests something else (e.g. a prerequisite computation) doesn't fail it, but an error in any part that uses its concept does, even if another part got that concept right. A correct part that isolates a *different* node (its concept appears in no part answered wrongly) earns that node bonus credit via `--bonus` (pass/correct only; up to 15 bonus nodes per question; placement bonuses use no question budget). In quizzes, list every node a correct part genuinely uses, even ones `next` would call locked. A quiz bonus at the level k the part demonstrates gives one credit at each level from the node's next level up to $k$ (capped at three levels and banked as in ladder quizzes), as a placement pass would.
  - *Downward credit* (how bonus levels are judged): a node earns credit from a part only if the answer would have failed without it at that level (*counterfactual test*); routine uses (notation, algebra, a definition merely mentioned) earn nothing. The map: hypotheses checked and the result applied → L2; the key step of a short proof or counterexample → L3; one of several results combined in a multi-step argument → L4, but only for a node already at L3 (below that it counts as L3). Open-book bonuses never grant L1 (they bank L2/L3 until the node's L1 is earned closed-book; `--closed-book` marks a closed-book part). Each credited node gets the step that used it in the Quiz Log entry.
  - *Audits*: when a node reaches L2+ through downward credit alone (no direct question at that level), the script flags it for an audit with probability 15%. `next` serves pending audits (about 1 in 3 picks) as a direct question at the node's current level: pass keeps the level, fail drops it one level, as in a rust check. `status` shows the audit pass rate; if it falls below about 80%, tighten the downward-credit judgement.
  - *Check credit*: a proof or solution graded by `/check` counts toward the skill trees like a quiz answer, for every node (up to 15) the proof genuinely uses in a non-routine step, at the level it demonstrates (L2 application, L3 short proof, L4 multi-step). If that level is above the node's current level, it counts as a quiz answer at the next level (*Correct* → progress, *Incorrect* → progress reset); otherwise a *Correct* verdict confirms the current level. `/check` never lowers a level except through the *Stuck / errors* rule.
  - *Stuck / errors*: when `/stuck` (with hint level 2+) or a `/check` Error shows a node lacks an ability at level $k$, its level drops to $\min(\text{level}, k - 1)$.
- **Placement** (`/place`): a one-time adaptive test, run per tree, bottom-up across trees (`place-order`). Stage L2 then stage L3; each question goes to the node that best splits what's still undetermined. A pass raises the node and all its ancestors (in every tree) to that level; a fail marks the node and its in-tree dependents as below it. Placement never lowers levels and never places L4/L5. Placed levels are marked `provisional`: the next `/quiz` on such a node is a *placement check* at its current level (pass clears the flag, fail drops one level).
- **Field progress**: a tree's *Mastered* count (nodes at L3+) is the headline level for the field; *Depth* is the total of node levels as a percentage of every node at L5, counting planned nodes, so it also shows what remains. Below them, a level table gives the nodes *at* each level and the nodes that have *reached* each level (that level or higher). The reached counts only ever rise, so every level-up shows, not just reaching L3. Each group heading repeats the reached counts.
- **Commands**: `next` (choose the quiz node), `recall-next` (nodes for a recall round), `record` (grade a quiz answer), `stuck` (recalibrate), `add` / `edge` (build trees), `rename` (retitle a node everywhere, e.g. when a planned node's note gets a different title), `move` (move a node to another tree with its edges, after retagging), `tree-for` (which tree a note belongs in), `place-order` / `place-next` / `place-record` / `place-status` / `place-reset` (placement), `status [--tree]`, `render`, `check`, `archive-logs` (rotate the logs; automatic). Run `python3 Scripts/skill_trees.py -h` for usage.
- **Legacy trees**: trees without a `%% NODES` marker still use the old textbook-section nodes and are ignored by the script until converted.
