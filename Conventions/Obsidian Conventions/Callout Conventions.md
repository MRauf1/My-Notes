# Callout Conventions

- General callout conventions
	- For LaTeX math inside callouts (i.e., definitions, theorems, proofs, examples, etc...), always use display mode (i.e., double $) with *align* block. The double $ and the *align* block boundaries (i.e., begin align and end align) are each on their own line. As for the math itself, the first two math portions separated by a logical relation are on the same line, while every next one will be on a new line. The spacing is set on the logical relation with & symbol. For an example, see the [[Addition Property of Equality]] note. For spacing parts of math on the same line (e.g., logical quantifiers), use quad.
- *Definition* callout
	- This callout is always unfolded. 
	- Definition callouts are numbered in sequential order according to the order that they appear in within the note.
- *Examples* callout
	- Divided into parent *Examples* (collection of related examples) callouts and child *Example* (one example) callouts.
	- Both the parent and child callouts are always foldable and always start off as folded.
	- Parent callouts are numbered in sequential order according to the order that they appear in within the note.
	- Parent callouts each have their name within parenthesis after their number which describes what kind of examples they contain.
	- Parent callout contains $\geq$ 1 child *Example* callouts.
	- Child callouts are numbered with their parent's number, a dot, and their own number in sequential order according to the order that they appear in within their parent callout (e.g. 2nd child of 3rd parent will have the number 3.2).
	- Child callouts each have their name within parenthesis after their number which describes what kind of an example they contain.

TODO:
- Link to a note with these conventions