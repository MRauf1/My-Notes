---
tags: literature_review
---

# Review[^1]

Neural circuits have specialized components, but even these specialized components constantly intercommunicate between each other and between different regions and parts of the brain.

20% of neurons are inhibitory and suppress signals. Can this be somehow incorporated to modern models? Would modern models benefit from such neurons? Would these types of neurons perhaps enhance efficiency of the models? Can you think of dropout as a technique that implements this inhibition?

The neural circuits for vision are structured in progressive layers, which I suppose is where the inspiration for CNNs comes from as they also start with low level features, such as edges, and such, and progressively, the later layers recognize higher level features, such as specific animals and such.

How does our brain have capacity to have unlimited long-term memories considering it itself is not infinite? And if we have this unlimited capacity, why is our memory seemingly limited in what we actually remember?

Different types of memories are stored and processed in different parts of the brain, presenting the principle of redundancy from computer architecture to preserve information when some part may break. Could this kind of separation of types of memory into different modules within neural networks improve the memory of models too?

Memories are "stored" within the synapses of the neurons, and in the same way, the "memories" learned from the data are stored within the weights of neural networks.

Information between neurons is transferred not just through electrical signals, but also through the chemical messengers called neurotransmitters. Could such a messenger be created for neural networks as well to communicate between the different components? One could create some kind of a latent representation behaving as a sort of neurotransmitter, which then gets passed to the other modules of the neural network. In particular, when something is very rewarding, we are more likely to remember it thanks to the neurotransmitter dopamine. Thus, one could a create a class of different "neurotransmitters" for neural networks, each serving an analogous function to the brain's neurotransmitters. One could, for example, have a dopamine-like "neurotransmitter", which enforces memory preservation within the neural network.

The brain has multiple layers of filtering, first through perception, then through comparing the information to past memories that might be similar. Perhaps similar kind of filtering could be added to neural networks to be able to process significantly more information with the same amount of compute. This would be especially beneficial in real-time tasks, such as for embodied AI and robots and such. Perhaps the input goes through a filtering neural network first, and the lower dimensional outputs go to the actual processing neural network. In a way, that is how FasterRCNN works too. The brain also handles the vast amount of information through encoding them into simple representations and using associations with past memories.

For agents, just like how humans have executive function, perhaps one way would be to create an executive function module that takes in all of the processed inputs by the other modules, and then uses them to plan and execute decisions.

Just like how humans mentalize, that is, try to think about what other people are thinking, that kind of simulation and imagination would be helpful for AI too.

Could neurogenesis be useful for neural networks? In other words, giving the neural networks to create new "neurons"/weights/modules within themselves and slowly build up and train those, allowing for the neural network to be more dynamic in its own capacity and capabilities. Just like how embryo's brain develops, one could have a specialized module for creating new "neurons", which are then transferred to their long term locations in the neural network, such as attaching as additional layers in one of the modules.

Perhaps create a "myelinated" vs "unmyelinated" neurons in the neural network. The former has faster signals, while the latter preserves the plasticity of the brain. Similarly, perhaps one could differentiate neurons/weights in the neural network and make them more plastic or have them be more focused on outputting their signal instead. In other words, creating a specialization of neurons in the neural network.

Would a state like sleep be beneficial for neural networks to consolidate all of their knowledge and memory in the past day? It would go against a lot of people wanting neural networks to be able to function and work 24/7 though, but sleep might result in better performance.

Just like there are neurotransmitters for fast, but local changes and hormones for slow, but global changes, neural networks could have their own specialized messengers as well to change activities within the modules within the neural network.

[^1]: [Brain Facts](zotero://open-pdf/library/items/LH25JA7R?page=1)