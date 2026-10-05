# References

A compact list of fundamental papers referenced in the notes.

## Expressivity and Depth
- Montúfar, Pascanu, Cho & Bengio (2014). *On the Number of Linear Regions of Deep Neural Networks*. NeurIPS. [arXiv:1402.1869](https://arxiv.org/abs/1402.1869) — [[Linear Regions of ReLU Network]]
- Telgarsky (2016). *Benefits of Depth in Neural Networks*. COLT. [arXiv:1602.04485](https://arxiv.org/abs/1602.04485) — [[Depth Separation]]
- Eldan & Shamir (2016). *The Power of Depth for Feedforward Neural Networks*. COLT. [arXiv:1512.03965](https://arxiv.org/abs/1512.03965) — [[Depth Separation]]
- Lu, Pu, Wang, Hu & Wang (2017). *The Expressive Power of Neural Networks: A View from the Width*. NeurIPS. [arXiv:1709.02540](https://arxiv.org/abs/1709.02540) — [[Universal Approximation Theorem]], [[Width Efficiency]]

## Activation Functions
- Glorot, Bordes & Bengio (2011). *Deep Sparse Rectifier Neural Networks*. AISTATS. [PMLR 15](https://proceedings.mlr.press/v15/glorot11a.html) — [[ReLU Function]], [[Softplus Function]]
- Hendrycks & Gimpel (2016). *Gaussian Error Linear Units (GELUs)*. [arXiv:1606.08415](https://arxiv.org/abs/1606.08415) — [[Gaussian Error Linear Unit]], [[Swish Function]]

## Loss Functions
- Lin, Goyal, Girshick, He & Dollár (2017). *Focal Loss for Dense Object Detection*. ICCV. [arXiv:1708.02002](https://arxiv.org/abs/1708.02002) — [[Focal Loss]]

## Optimization
- Duchi, Hazan & Singer (2011). *Adaptive Subgradient Methods for Online Learning and Stochastic Optimization*. JMLR. [JMLR 12](https://jmlr.org/papers/v12/duchi11a.html) — [[AdaGrad]]
- Kingma & Ba (2015). *Adam: A Method for Stochastic Optimization*. ICLR. [arXiv:1412.6980](https://arxiv.org/abs/1412.6980) — [[Adam]]
- Loshchilov & Hutter (2019). *Decoupled Weight Decay Regularization*. ICLR. [arXiv:1711.05101](https://arxiv.org/abs/1711.05101) — [[AdamW]]
- Wilson, Roelofs, Stern, Srebro & Recht (2017). *The Marginal Value of Adaptive Gradient Methods in Machine Learning*. NeurIPS. [arXiv:1705.08292](https://arxiv.org/abs/1705.08292) — [[Adam]], [[Stochastic Gradient Descent]]
- Goyal et al. (2017). *Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour*. [arXiv:1706.02677](https://arxiv.org/abs/1706.02677) — [[Learning Rate Warm-Up]], [[Batch Size]]

## Initialization and Normalization
- Glorot & Bengio (2010). *Understanding the Difficulty of Training Deep Feedforward Neural Networks*. AISTATS. [PMLR 9](https://proceedings.mlr.press/v9/glorot10a.html) — [[Xavier Initialization]]
- He, Zhang, Ren & Sun (2015). *Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification*. ICCV. [arXiv:1502.01852](https://arxiv.org/abs/1502.01852) — [[He Initialization]], [[Parametric ReLU]]
- Ioffe & Szegedy (2015). *Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift*. ICML. [arXiv:1502.03167](https://arxiv.org/abs/1502.03167) — [[Batch Normalization]]
- Ba, Kiros & Hinton (2016). *Layer Normalization*. [arXiv:1607.06450](https://arxiv.org/abs/1607.06450) — [[Layer Normalization]]
- Wu & He (2018). *Group Normalization*. ECCV. [arXiv:1803.08494](https://arxiv.org/abs/1803.08494) — [[Group Normalization]]
- Ulyanov, Vedaldi & Lempitsky (2016). *Instance Normalization: The Missing Ingredient for Fast Stylization*. [arXiv:1607.08022](https://arxiv.org/abs/1607.08022) — [[Instance Normalization]]
- Salimans & Kingma (2016). *Weight Normalization: A Simple Reparameterization to Accelerate Training of Deep Neural Networks*. NeurIPS. [arXiv:1602.07868](https://arxiv.org/abs/1602.07868) — [[Normalization Layer]]
- Santurkar, Tsipras, Ilyas & Madry (2018). *How Does Batch Normalization Help Optimization?* NeurIPS. [arXiv:1805.11604](https://arxiv.org/abs/1805.11604) — [[Batch Normalization]], [[Internal Covariate Shift]]
- Bjorck, Gomes, Selman & Weinberger (2018). *Understanding Batch Normalization*. NeurIPS. [arXiv:1806.02375](https://arxiv.org/abs/1806.02375) — [[Batch Normalization]]
- Yang, Pennington, Rao, Sohl-Dickstein & Schoenholz (2019). *A Mean Field Theory of Batch Normalization*. ICLR. [arXiv:1902.08129](https://arxiv.org/abs/1902.08129) — [[Batch Normalization]]
- Li & Arora (2019). *An Exponential Learning Rate Schedule for Deep Learning*. ICLR 2020. [arXiv:1910.07454](https://arxiv.org/abs/1910.07454) — [[Batch Normalization]]
- Hoffer, Hubara & Soudry (2017). *Train Longer, Generalize Better: Closing the Generalization Gap in Large Batch Training of Neural Networks*. NeurIPS. [arXiv:1705.08741](https://arxiv.org/abs/1705.08741) — [[Ghost Batch Normalization]]
- Luo, Wang, Shao & Peng (2019). *Towards Understanding Regularization in Batch Normalization*. ICLR. [arXiv:1809.00846](https://arxiv.org/abs/1809.00846) — [[Batch Normalization]]
- Teye, Azizpour & Smith (2018). *Bayesian Uncertainty Estimation for Batch Normalized Deep Networks*. ICML. [arXiv:1802.06455](https://arxiv.org/abs/1802.06455) — [[Batch Normalization]]
- Lubana, Dick & Tanaka (2021). *Beyond BatchNorm: Towards a Unified Understanding of Normalization in Deep Learning*. NeurIPS. [arXiv:2106.05956](https://arxiv.org/abs/2106.05956) — [[Normalization Layer]]

## Residual Networks
- He, Zhang, Ren & Sun (2016). *Deep Residual Learning for Image Recognition*. CVPR. [arXiv:1512.03385](https://arxiv.org/abs/1512.03385) — [[Residual Connection]]
- He, Zhang, Ren & Sun (2016). *Identity Mappings in Deep Residual Networks*. ECCV. [arXiv:1603.05027](https://arxiv.org/abs/1603.05027) — [[Residual Connection]]
- Balduzzi, Frean, Leary, Lewis, Ma & McWilliams (2017). *The Shattered Gradients Problem: If ResNets Are the Answer, Then What Is the Question?* ICML. [arXiv:1702.08591](https://arxiv.org/abs/1702.08591) — [[Shattered Gradients]]
- Veit, Wilber & Belongie (2016). *Residual Networks Behave Like Ensembles of Relatively Shallow Networks*. NeurIPS. [arXiv:1605.06431](https://arxiv.org/abs/1605.06431) — [[Residual Network as Ensemble]]
- Li, Xu, Taylor, Studer & Goldstein (2018). *Visualizing the Loss Landscape of Neural Nets*. NeurIPS. [arXiv:1712.09913](https://arxiv.org/abs/1712.09913) — [[Residual Connection]]
- Zagoruyko & Komodakis (2016). *Wide Residual Networks*. BMVC. [arXiv:1605.07146](https://arxiv.org/abs/1605.07146) — [[Residual Connection]]
- Orhan & Pitkow (2018). *Skip Connections Eliminate Singularities*. ICLR. [arXiv:1701.09175](https://arxiv.org/abs/1701.09175) — [[Residual Connection]]

## Generalization and Capacity
- Vapnik & Chervonenkis (1971). *On the Uniform Convergence of Relative Frequencies of Events to Their Probabilities*. Theory of Probability & Its Applications. [doi:10.1137/1116025](https://doi.org/10.1137/1116025) — [[VC Dimension]]
- Belkin, Hsu, Ma & Mandal (2019). *Reconciling Modern Machine-Learning Practice and the Classical Bias-Variance Trade-Off*. PNAS. [arXiv:1812.11118](https://arxiv.org/abs/1812.11118) — [[Double Descent]]
- Nakkiran, Kaplun, Bansal, Yang, Barak & Sutskever (2021). *Deep Double Descent: Where Bigger Models and More Data Hurt*. ICLR 2020 / J. Stat. Mech. [arXiv:1912.02292](https://arxiv.org/abs/1912.02292) — [[Double Descent]]
- Bubeck & Sellke (2021). *A Universal Law of Robustness via Isoperimetry*. NeurIPS. [arXiv:2105.12806](https://arxiv.org/abs/2105.12806) — [[Double Descent]]
- Moreno-Torres, Raeder, Alaiz-Rodríguez, Chawla & Herrera (2012). *A Unifying View on Dataset Shift in Classification*. Pattern Recognition. [doi:10.1016/j.patcog.2011.06.019](https://doi.org/10.1016/j.patcog.2011.06.019) — [[Dataset Shift]]

## Regularization
- Madry, Makelov, Schmidt, Tsipras & Vladu (2018). *Towards Deep Learning Models Resistant to Adversarial Attacks*. ICLR. [arXiv:1706.06083](https://arxiv.org/abs/1706.06083) — [[Adversarial Training]]

## Convolutional Networks
- Yu & Koltun (2016). *Multi-Scale Context Aggregation by Dilated Convolutions*. ICLR. [arXiv:1511.07122](https://arxiv.org/abs/1511.07122) — [[Dilated Convolution]]
- Chen, Papandreou, Kokkinos, Murphy & Yuille (2018). *DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs*. TPAMI. [arXiv:1606.00915](https://arxiv.org/abs/1606.00915) — [[Dilated Convolution]]
- Long, Shelhamer & Darrell (2015). *Fully Convolutional Networks for Semantic Segmentation*. CVPR. [arXiv:1411.4038](https://arxiv.org/abs/1411.4038) — [[Transposed Convolution]]
- Odena, Dumoulin & Olah (2016). *Deconvolution and Checkerboard Artifacts*. Distill. [doi:10.23915/distill.00003](https://doi.org/10.23915/distill.00003) — [[Transposed Convolution]]
- Lin, Chen & Yan (2014). *Network in Network*. ICLR. [arXiv:1312.4400](https://arxiv.org/abs/1312.4400) — [[1x1 Convolution]]
- Tompson, Goroshin, Jain, LeCun & Bregler (2015). *Efficient Object Localization Using Convolutional Networks*. CVPR. [arXiv:1411.4280](https://arxiv.org/abs/1411.4280) — [[Spatial Dropout]]
- DeVries & Taylor (2017). *Improved Regularization of Convolutional Neural Networks with Cutout*. [arXiv:1708.04552](https://arxiv.org/abs/1708.04552) — [[Cutout]]
- Erhan, Bengio, Courville & Vincent (2009). *Visualizing Higher-Layer Features of a Deep Network*. Univ. Montréal Tech. Report 1341. — [[Feature Visualization]]
- Zeiler & Fergus (2014). *Visualizing and Understanding Convolutional Networks*. ECCV. [arXiv:1311.2901](https://arxiv.org/abs/1311.2901) — [[Feature Visualization]]
- Mahendran & Vedaldi (2015). *Understanding Deep Image Representations by Inverting Them*. CVPR. [arXiv:1412.0035](https://arxiv.org/abs/1412.0035) — [[Feature Visualization]]
- Bau, Zhou, Khosla, Oliva & Torralba (2017). *Network Dissection: Quantifying Interpretability of Deep Visual Representations*. CVPR. [arXiv:1704.05796](https://arxiv.org/abs/1704.05796) — [[Network Dissection]]
- Qin, Yu, Liu & Wang (2018). *How Convolutional Neural Networks See the World — A Survey of Convolutional Neural Network Visualization Methods*. Mathematical Foundations of Computing. [arXiv:1804.11191](https://arxiv.org/abs/1804.11191) — [[Feature Visualization]]

## Hyperparameter Search
- Bergstra & Bengio (2012). *Random Search for Hyper-Parameter Optimization*. JMLR. [JMLR 13](https://jmlr.org/papers/v13/bergstra12a.html) — [[Hyperparameter Search]]
- Snoek, Larochelle & Adams (2012). *Practical Bayesian Optimization of Machine Learning Algorithms*. NeurIPS. [arXiv:1206.2944](https://arxiv.org/abs/1206.2944) — [[Bayesian Optimization]]
- Li, Jamieson, DeSalvo, Rostamizadeh & Talwalkar (2017). *Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization*. JMLR. [arXiv:1603.06560](https://arxiv.org/abs/1603.06560) — [[Hyperband]]

## Memory-Efficient Training
- Chen, Xu, Zhang & Guestrin (2016). *Training Deep Nets with Sublinear Memory Cost*. [arXiv:1604.06174](https://arxiv.org/abs/1604.06174) — [[Gradient Checkpointing]]
- Gomez, Ren, Urtasun & Grosse (2017). *The Reversible Residual Network: Backpropagation Without Storing Activations*. NeurIPS. [arXiv:1707.04585](https://arxiv.org/abs/1707.04585) — [[Gradient Checkpointing]]
- Huang et al. (2019). *GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism*. NeurIPS. [arXiv:1811.06965](https://arxiv.org/abs/1811.06965) — [[Micro-Batching]]

## Psychology of Happiness, Control, and Mortality
- Wegner, Schneider, Carter & White (1987). *Paradoxical Effects of Thought Suppression*. Journal of Personality and Social Psychology 53(1). [doi:10.1037/0022-3514.53.1.5](https://doi.org/10.1037/0022-3514.53.1.5) — [[Ironic Process Theory]]
- Wegner (1994). *Ironic Processes of Mental Control*. Psychological Review 101(1). [doi:10.1037/0033-295X.101.1.34](https://doi.org/10.1037/0033-295X.101.1.34) — [[Ironic Process Theory]]
- Wood, Perunovic & Lee (2009). *Positive Self-Statements: Power for Some, Peril for Others*. Psychological Science 20(7). — [[Ironic Process Theory]], [[Self-Talk]]
- Mauss, Tamir, Anderson & Savino (2011). *Can Seeking Happiness Make People Unhappy? Paradoxical Effects of Valuing Happiness*. Emotion 11(4). — [[Backwards Law]]
- Koo, Algoe, Wilson & Gilbert (2008). *It's a Wonderful Life: Mentally Subtracting Positive Events Improves People's Affective States*. Journal of Personality and Social Psychology 95(5). — [[Hedonic Adaptation]]
- David, Cotet, Matu, Mogoase & Stefan (2018). *50 Years of Rational-Emotive and Cognitive-Behavioral Therapy: A Systematic Review and Meta-Analysis*. Journal of Clinical Psychology 74(3). — [[Rational Emotive Behavior Therapy]]
- Zeidan et al. (2011). *Brain Mechanisms Supporting the Modulation of Pain by Mindfulness Meditation*. Journal of Neuroscience 31(14). [doi:10.1523/JNEUROSCI.5791-10.2011](https://doi.org/10.1523/JNEUROSCI.5791-10.2011) — [[Non-Attachment]]
- Ordóñez, Schweitzer, Galinsky & Bazerman (2009). *Goals Gone Wild: The Systematic Side Effects of Overprescribing Goal Setting*. Academy of Management Perspectives 23(1). — [[Goal-Setting Theory]]
- Sarasvathy (2001). *Causation and Effectuation: Toward a Theoretical Shift from Economic Inevitability to Entrepreneurial Contingency*. Academy of Management Review 26(2). — [[Effectuation]]
- Read, Song & Smit (2009). *A Meta-Analytic Review of Effectuation and Venture Performance*. Journal of Business Venturing 24(6). — [[Effectuation]]
- Carleton (2016). *Into the Unknown: A Review and Synthesis of Contemporary Models Involving Uncertainty*. Journal of Anxiety Disorders 39. — [[Intolerance of Uncertainty]]
- Denrell (2003). *Vicarious Learning, Undersampling of Failure, and the Myths of Management*. Organization Science 14(3). — [[Survivorship Bias]]
- Greenberg, Pyszczynski & Solomon (1986). *The Causes and Consequences of a Need for Self-Esteem: A Terror Management Theory*. In *Public Self and Private Self*. Springer. — [[Terror Management Theory]]
- Klein et al. (2022). *Many Labs 4: Failure to Replicate Mortality Salience Effect With and Without Original Author Involvement*. Collabra: Psychology 8(1). — [[Terror Management Theory]]
- Nagel (1970). *Death*. Noûs 4(1). [doi:10.2307/2214297](https://doi.org/10.2307/2214297) — [[Deprivation Account of Death]]
- Hume (1739). *A Treatise of Human Nature*, Book I, Part IV, Section 6. — [[Bundle Theory of Self]]
- Schneier (2003). *Beyond Fear: Thinking Sensibly About Security in an Uncertain World*. Copernicus. — [[Security Theater]]

## Self-Concept, Values, and Emotion Regulation
- Hayes, Wilson, Gifford, Follette & Strosahl (1996). *Experiential Avoidance and Behavioral Disorders: A Functional Dimensional Approach to Diagnosis and Treatment*. Journal of Consulting and Clinical Psychology 64(6). — [[Experiential Avoidance]]
- Ford, Lam, John & Mauss (2018). *The Psychological Health Benefits of Accepting Negative Emotions and Thoughts: Laboratory, Diary, and Longitudinal Evidence*. Journal of Personality and Social Psychology 115(6). — [[Experiential Avoidance]]
- Campbell, Bonacci, Shelton, Exline & Bushman (2004). *Psychological Entitlement: Interpersonal Consequences and Validation of a Self-Report Measure*. Journal of Personality Assessment 83(1). — [[Psychological Entitlement]]
- Festinger (1954). *A Theory of Social Comparison Processes*. Human Relations 7(2). — [[Social Comparison Theory]]
- Orben & Przybylski (2019). *The Association Between Adolescent Well-Being and Digital Technology Use*. Nature Human Behaviour 3. — [[Social Comparison Theory]]
- Crocker & Wolfe (2001). *Contingencies of Self-Worth*. Psychological Review 108(3). — [[Contingencies of Self-Worth]]
- Kasser & Ryan (1996). *Further Examining the American Dream: Differential Correlates of Intrinsic and Extrinsic Goals*. Personality and Social Psychology Bulletin 22(3). — [[Intrinsic and Extrinsic Aspirations]]
- Dittmar, Bond, Hurst & Kasser (2014). *The Relationship Between Materialism and Personal Well-Being: A Meta-Analysis*. Journal of Personality and Social Psychology 107(5). — [[Intrinsic and Extrinsic Aspirations]]
- Killingsworth, Kahneman & Mellers (2023). *Income and Emotional Well-Being: A Conflict Resolved*. PNAS 120(10). — [[Intrinsic and Extrinsic Aspirations]]
- Carstensen, Isaacowitz & Charles (1999). *Taking Time Seriously: A Theory of Socioemotional Selectivity*. American Psychologist 54(3). — [[Socioemotional Selectivity Theory]]
- Ono (1987). *Superstitious Behavior in Humans*. Journal of the Experimental Analysis of Behavior 47(3). — [[Superstitious Behavior]]
- Loftus & Pickrell (1995). *The Formation of False Memories*. Psychiatric Annals 25(12). — [[False Memory]]
- Swann (1983). *Self-Verification: Bringing Social Reality into Harmony with the Self*. In *Psychological Perspectives on the Self*, Vol. 2. — [[Self-Verification Theory]]
- Leary et al. (2017). *Cognitive and Interpersonal Features of Intellectual Humility*. Personality and Social Psychology Bulletin 43(6). — [[Intellectual Humility]]
- Milgram (1963). *Behavioral Study of Obedience*. Journal of Abnormal and Social Psychology 67(4). — [[Milgram Obedience Experiment]]
- Burger (2009). *Replicating Milgram: Would People Still Obey Today?* American Psychologist 64(1). — [[Milgram Obedience Experiment]]
- Scheibehenne, Greifeneder & Todd (2010). *Can There Ever Be Too Many Options? A Meta-Analytic Review of Choice Overload*. Journal of Consumer Research 37(3). — [[Paradox of Choice]]
