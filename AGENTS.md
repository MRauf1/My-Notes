# Obsidian Vault Knowledge Management Guidelines

This is the creator's Obsidian Vault done in a Zettelkasten format where he compiles all of the knowledge that he learns throughout his life.

Your primary purpose is to assist the author in expanding the vault by creating/modifying/linking/deleting notes based on the material that the creator learns.

The creator does research in computer science/mathematics/statistics with the specialization of theoretically grounded computer vision/graphics. But the creator is interested in other fields too as a hobby. Keep the creator's perspective when modifying the vault. 

## 1. Vault Overview & Structure
- **Root Directory**: `~/Documents/PKM_System/Obsidian/my_vault`
- **Active Notes**: All conceptual notes live inside `Notes/`.
- **Ignored / Restricted Directories**: 
  - Never read, create, or modify files in `.obsidian/`, `Templates/`, `Conventions/`, `Notes/Personal/`, or `Notes/Gamification/`.
  - Always respect `.gitignore`.

## 2. Note Philosophy (Atomic Notes)
- Every note represents a single, focused concept or theorem.
- Keep definitions crisp and concise at the top, followed by properties.
- If requested, add additional details, such as creator's interpretation or non-definitional properties, below the callout.
- Titles must use Title Case matching the filename (e.g., `Spectral Theorem.md` -> `# Spectral Theorem`).
- Do not provide examples unless specifically requested by the creator.
- Raw highlight text from PDFs may drop certain mathematical symbols due to PDF encoding issues. You must actively verify and reconstruct mathematically sound LaTeX based on the context of the theorem and textbook conventions.
- The creator may attach an image that he wants to be incorporated in the notes. Paste that image in `Media/<Appropriate Name>.png` and link that image within the appropriate notes.
- If a note with the same name for a different concept already exists, create a new note with the title `<Concept Name>(<Subdomain>)` to avoid conflicts and rewriting information.
- Make sure to link relevant notes to each other. 
	- Search for any relevant notes within the vault that could be linked.
	- Use your own knowledge of the material to search for related notes that might exist in the vault without going through the entire vault. 
	- NEVER grep generic terms like "Theorem", "Corollary", "Definition", or Zotero IDs. 
	- For each note,
		- Limit search to at most 5 targeted `rg` queries using specific technical nouns (e.g., "orthonormal basis"). 
		- Do NOT read more than 5 candidate notes to check for links. If unsure, link only to the primary parent concept and finish.
		- Run `Glob "Notes/*<keyword>*.md"` first. 
		- Only if title matching yields nothing, execute at most 2 `Grep` searches on exact technical phrases. 
		- Limit peripheral note updates to direct parent concepts, hub notes, or obvious counterparts (e.g., 2D vs 3D). Do not patch more than 3 existing files per run.

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

# Properties 
- Bulleted list of mathematical or structural properties with [[Wikilinks]]. 

[^1]: [<Citation Title>](<zotero_or_web_link>)
```
