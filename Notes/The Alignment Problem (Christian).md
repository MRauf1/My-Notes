---
tags: [literature_review]
---

# Review[^1]

Always take note of biases the dataset for they will become biases in the trained model as well.

Since models learn from our biases, we could use these models - like the word embeddings - to study the biases that are present in us.

When models are used, they also change us and our world too, so we should be cautious about what models we deploy and what they are capable of.

The book feels like one of those self-help books I've read before, but applied to AI. It is similar in a way to the book [[Why Machines Learn]]. There is a lot of specific examples being described in some other fields of how similar methods are used and what came about because of them to guide the thinking for the alignment problem in AI. There is also quite a bit of history of AI described that I'm already familiar with. But as an AI practitioner, a lot of this information feels not very relevant and applicable to me. This is more of a casual and entertaining read rather than something more grounded and philosophical, such as [[Superintelligence (Bostrom)]]. This book feels like a pop science book. Also, by the title, I thought this book would be about aligning AI before it reaches AGI, but halfway through, there's been no talk of the sort.

Even if sensitive attributes like race are absent from the model, as long as the attributes correlated with it are present, it's really no different than using that sensitive attribute directly. Thus, bias doesn't have to come directly; it can be indirect. This concept is known as "redundant encodings". In some cases, the sensitive attribute being absent may make things worse by making it even harder to detect the present bias. Thus, blindness cannot get rid of bias.

Fairness is a subjective concept and true fairness (at least one of the definitions) is theoretically impossible for most cases when the groups differ from each other. This is true regardless if the model is statistical or human. Thus, there are always tradeoffs to be made when it comes to bias and fairness. You can't satisfy every single criteria for fairness and bias, so you have to choose what's important for your model. The only theoretically possible way to provide fairness is if the model is a perfect predictor with 0 error. This follows from the Impossibility Theorem that states that you cannot simultaneously satisfy calibration, false positive parity, and false negative parity unless the base rates are equal or the model is a perfect predictor with 0 error. But even then, there are philosophical arguments stating that even a perfect predictor need not be completely fair as fairness has many definitions, some of which may not be satisfied even by a perfect predictor.

A lot of the models learn on human data. But human data itself is biased, so these biases get fed to the model, and when we use the model's biased predictions, this creates a closed feedback loop that keeps feeding itself.

You should be very cautious and reluctant of using models for tasks outside of their design. You should also be careful with how you use the model's predictions to determine your own future actions and decisions. A statistical/ML model is not always the right tool to solve a problem, such as when you're trying to design interventions and mechanisms to change the world.

Interpretability of ML models is crucial especially in certain domains, such as medicine or other fields where safety is vital. Tweaking interpretable models is also typically easier than tweaking black boxes. A pattern in ML is that the most accurate models are the least interpretable, while the most interpretable models are the least accurate.

Be careful of your model's outputs based on how your dataset is and what the reality looks like. For example, the author mentions a case where the model said that having asthma means less risk of pneumonia, but that is only because people with asthma received much better care compared to the healthy person and this was reflected in the training data making the final model to make incorrect assumptions.

In some cases, multitask learning can improve the performance of the singular task metric you were using before as the additional outputs as labels can be thought of as providing additional signal. They are also more transparent. In particular, when you are given inputs that don't add towards the model's performance, try using them as outputs instead to make the network more robust and transparent.

Dopamine works like temporal difference does in reinforcement learning. Thus, a spike on the dopamine system is a fluctuation in the organism's expectation.

Since rewards can be sparse in RL, a good technique to use that comes from Skinner's psychology is shaping, where the complex behavior is instilled through successive approximation of it (like through simpler behaviors that lead to the complex behavior). In this spirit, not just for reinforcement learning, but all of machine learning, if the model is having trouble training on a complex task, train it on a simpler one and then fine-tune it on the harder task, similar to how children learn simple things first, but grow to learn more complex things as they grow into adults. Remember divide and conquer.

An idea from physics to RL is the law of conservation of energy. Using this for designing the reward functions, you design a conservative field so that if the model goes back to its starting point, the net reward is 0, which can help with some of the RL reward hacking. Treat incentives like potential energy. More generally, we should reward states of the world rather than the actions of the agent as the states represent progress towards the goal more accurately.

Evolution has led us to not have reproductive success as the reward, but our predictors of reward as the reward. In other words, we optimize our behavior to maximize the things we find rewarding, while evolution itself is shaping what we find rewarding in the first place.

The 3 intrinsic motivators of humans that can be applied to AI:
1) Novelty
	1) Experiencing new events can be a reward on its own
2) Surprise
	1) With a component that predicts the reward of action, when the predictor gets it wrong, that prediction error can be made a reward itself
3) Mastery

These intrinsic motivators could be used to advocate for the agent to explore the world on its own even without explicit extrinsic rewards for completing a task that the researcher wants the model to complete. So much so, that even without an extrinsic reward, the agent can accomplish a lot purely with intrinsic motivation.

Philosophically, all the rewards are the result of one's brain and their evaluation of good and bad, not the environment. In that sense, all rewards are internal.

Inverse reinforcement learning - instilling human values in machines by having the machines observe us and infer our values and desires from that. Instead of asking "given a reward signal, what behavior will optimize it", you ask "given the observed behavior, what reward signal, if any, is being optimized". This is an ill-posed problem in that there is no one, unique answer.

Inverse Reward Design - pulling back further from IRL, and the machine is asking, "What do I think you want, based on what you told me to do?" There is inherent uncertainty in the instruction itself that humans devise because they cannot come up with a perfect solution, and this uncertainty is reflected when they construct the agent. Thus, the agent tries to make sense of what the humans want based on the instruction that imperfectly represents what the humans want. Kind of like telling the agent to understand just how difficult it is for humans to design a reward function that actually captures what they want.

[^1]: [The Alignment Problem: Machine Learning and Human Values](zotero://open-pdf/library/items/P27SWKW4?page=1)

