---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Linked List
> A pointer-based [[Data Structure]] made up of nodes containing the list's items, linked together into a sequence via references.[^1]

Compared to array-based implementations of the list interface, a linked list loses the ability to access an arbitrary element in $O(1)$ time — instead, it must be found by walking the list one node at a time. Its main advantage is dynamism: given a reference to any node, that node can be deleted, or a new node inserted adjacent to it, in $O(1)$ time, regardless of where it lies in the list.[^1]

# Types
- [[Singly Linked List]]
- [[Doubly Linked List]]
- [[Space Efficient Linked List]]

# Space Usage
Depends on the variant; see [[Singly Linked List]], [[Doubly Linked List]], and [[Space Efficient Linked List]] for exact formulas.

# Properties
- [[Linear Data Structure]]

[^1]: [Morin, p. 61](zotero://select/library/items/HYS8NDAB)
