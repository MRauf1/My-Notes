---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Curiosity-Driven Exploration[^1]
> Designing [[Reinforcement Learning|reinforcement-learning]] agents that are *intrinsically* motivated, rewarded for novelty or surprise rather than (or in addition to) extrinsic task reward, so that they explore for its own sake, as curious humans and animals do.

# Types
Humans' [[Intrinsic Motivation|intrinsic motivation]] involves three drives:[^2]
- *Novelty* - rather than acting randomly (as epsilon-greedy agents do), we are reliably drawn to new things; agents can be rewarded simply for seeing something new.[^3]
- *Surprise* - we stay interested in things that defy our expectations and have something to teach us; resolving uncertainty and gaining information drive children's exploration. Pathak's agent pairs a predictor, rewarded for accurate predictions of action outcomes, with a policy rewarded when the predictor is wrong, turning prediction error into reward.[^4]
- *Mastery*.

# Properties
- Curiosity breeds competence: surprise-driven agents solved much larger mazes, and novelty-driven agents with no access to game score reached state-of-the-art scores on several Atari games. Death needs no explicit penalty, since restarting at the familiar beginning is simply boring.[^5]
- Two curious agents playing a zero-sum game against each other cooperate to prolong rallies indefinitely, since both seek to escape the well-trodden start.[^6]
- Failure modes: an agent that cannot cross an obstacle (e.g. a jump requiring 15 precise frames) may stall at a dead end; once everything is predictable, it loiters doing nothing. Random events are always somewhat surprising, so gambling addiction may be intrinsic reward overtaking extrinsic reward.[^7]
- Novel and surprising stimuli trigger dopamine even absent reward ([[Reward Prediction Error Hypothesis]]).[^8]
- Since every reward is evaluated within the brain, "all rewards are internal" (Singh, Lewis, Barto).[^9]
- **Toward general AI**: purpose-built systems relying on dense external labels or rewards are arguably not truly intelligent; life does not come pre-labelled with feedback, and humans must learn to judge by their own lights. Removing reward altogether, letting agents set their own objectives or be measured by behaviour, raises safety questions; a knowledge-seeking agent would be "the ultimate scientist" but might commandeer resources ([[Instrumental Convergence Thesis]]).[^10]
- Challenges the [[Reward Hypothesis]].

[^1]: [Christian, 2021, p. 181](zotero://open-pdf/library/items/P27SWKW4?page=181&annotation=HMHHC5RP); [Christian, 2021, p. 187](zotero://open-pdf/library/items/P27SWKW4?page=187&annotation=82YQZX2K)
[^2]: [Christian, 2021, p. 190](zotero://open-pdf/library/items/P27SWKW4?page=190&annotation=LB6K9HCB)
[^3]: [Christian, 2021, p. 190](zotero://open-pdf/library/items/P27SWKW4?page=190&annotation=8356I4BD); [Christian, 2021, p. 194](zotero://open-pdf/library/items/P27SWKW4?page=194&annotation=FIK88T2U)
[^4]: [Christian, 2021, p. 196](zotero://open-pdf/library/items/P27SWKW4?page=196&annotation=K8E6PH6D); [Christian, 2021, p. 196](zotero://open-pdf/library/items/P27SWKW4?page=196&annotation=LZQLYMEQ); [Christian, 2021, p. 197](zotero://open-pdf/library/items/P27SWKW4?page=197&annotation=XFURCR3K); [Christian, 2021, p. 199](zotero://open-pdf/library/items/P27SWKW4?page=199&annotation=ASXYIGZQ); [Christian, 2021, p. 199](zotero://open-pdf/library/items/P27SWKW4?page=199&annotation=P7JXWAPT); [Christian, 2021, p. 200](zotero://open-pdf/library/items/P27SWKW4?page=200&annotation=MYXQKND9)
[^5]: [Christian, 2021, p. 200](zotero://open-pdf/library/items/P27SWKW4?page=200&annotation=ZA2VVNRW); [Christian, 2021, p. 201](zotero://open-pdf/library/items/P27SWKW4?page=201&annotation=J2NN9TE8); [Christian, 2021, p. 202](zotero://open-pdf/library/items/P27SWKW4?page=202&annotation=XXZCG5UQ); [Christian, 2021, p. 202](zotero://open-pdf/library/items/P27SWKW4?page=202&annotation=K87A7I82)
[^6]: [Christian, 2021, p. 203](zotero://open-pdf/library/items/P27SWKW4?page=203&annotation=XX2Y9ZD8)
[^7]: [Christian, 2021, p. 204](zotero://open-pdf/library/items/P27SWKW4?page=204&annotation=BNQSXX7H); [Christian, 2021, p. 204](zotero://open-pdf/library/items/P27SWKW4?page=204&annotation=5FFZJVC4); [Christian, 2021, p. 204](zotero://open-pdf/library/items/P27SWKW4?page=204&annotation=ISZYDB56); [Christian, 2021, p. 208](zotero://open-pdf/library/items/P27SWKW4?page=208&annotation=66JCXBWC)
[^8]: [Christian, 2021, p. 208](zotero://open-pdf/library/items/P27SWKW4?page=208&annotation=J4XDE9NG)
[^9]: [Christian, 2021, p. 203](zotero://open-pdf/library/items/P27SWKW4?page=203&annotation=KCSHBE94)
[^10]: [Christian, 2021, p. 209](zotero://open-pdf/library/items/P27SWKW4?page=209&annotation=NPF54894); [Christian, 2021, p. 209](zotero://open-pdf/library/items/P27SWKW4?page=209&annotation=LI3MGQHF); [Christian, 2021, p. 209](zotero://open-pdf/library/items/P27SWKW4?page=209&annotation=D4NNATUV); [Christian, 2021, p. 209](zotero://open-pdf/library/items/P27SWKW4?page=209&annotation=2THZDPDF); [Christian, 2021, p. 210](zotero://open-pdf/library/items/P27SWKW4?page=210&annotation=PWZIIUXW); [Christian, 2021, p. 210](zotero://open-pdf/library/items/P27SWKW4?page=210&annotation=JNVQBGEW); [Christian, 2021, p. 210](zotero://open-pdf/library/items/P27SWKW4?page=210&annotation=U55GQASY); [Christian, 2021, p. 211](zotero://open-pdf/library/items/P27SWKW4?page=211&annotation=WYHCIJSW)
