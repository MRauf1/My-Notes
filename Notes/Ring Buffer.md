---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Ring Buffer[^1]
> A simple, usually fixed-size storage mechanism that treats a block of contiguous memory as circular, using two index counters to track the current beginning and end of the queue.

# Properties
- Since array indexing is not itself circular, the index counters must wrap around to zero once they move past the end of the underlying array.
- Data is enqueued at the front and dequeued from the tail, so the buffer's current contents appear to travel around the underlying array like a train circling a track.
- The same circular-indexing technique underlies a resizable [[Queue (ArrayList)]]; a ring buffer is the fixed-size case, which never reallocates.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=181&annotation=YEGS9IR3)
