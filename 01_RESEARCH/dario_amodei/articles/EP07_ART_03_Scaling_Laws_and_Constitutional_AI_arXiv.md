# EP07_ART_03: Landmark Scientific Papers — Scaling Laws, Constitutional AI & Mechanistic Interpretability
- **Archives:** arXiv.org (Open Access) & Transformer Circuits Thread

---

## arXiv:2001.08361 — Scaling Laws for Neural Language Models
- **Reference:** Scaling Laws for Neural Language Models (Kaplan, McCandlish, Amodei et al., 2020)
- **URL:** https://arxiv.org/abs/2001.08361
- **Authors:** Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, Dario Amodei

### Abstract
# Computer Science > Machine Learning # Title: Scaling Laws for Neural Language Models > Abstract: We study empirical scaling laws for language model performance on the cross-entropy loss. The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude. Other architectural details such as network width or depth have minimal effects within a wide range. Simple equations govern the dependence of overfitting on model/dataset size and the dependence of training speed on model size. These relationships allow us to determine the optimal allocation of a fixed compute budget. Larger models are significantly more sample-efficient, such that optimally compute-efficient training involves training very large models on a relatively modest amount of data and stopping significantly before convergence. ## Submission history ## Access Paper: - View PDF - HTML (experimental) - TeX Source ### Additional Features - Audio Summary ### Current browse context: ### References & Citations - SciX - Google Scholar - Semantic Scholar ### 15 blog links ### DBLP - CS Bibliography ## BibTeX formatted citation ### Bookmark # Bibliographic and Citation Tools # Code, Data and Media Associated with this Article # Demos # Recommenders and Search Tools - Author - Venue - Institution - Topic # arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .

## arXiv:2212.08073 — Constitutional AI: Harmlessness from AI Feedback
- **Reference:** Constitutional AI: Harmlessness from AI Feedback (Bai, Amodei et al., 2022)
- **URL:** https://arxiv.org/abs/2212.08073
- **Authors:** Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, Carol Chen, Catherine Olsson, Christopher Olah, Danny Hernandez, Dawn Drain, Deep Ganguli, Dustin Li, Eli Tran-Johnson, Ethan Perez, Jamie Kerr, Jared Mueller, Jeffrey Ladish, Joshua Landau, Kamal Ndousse, Kamile Lukosuite, Liane Lovitt, Michael Sellitto, Nelson Elhage, Nicholas Schiefer, Noemi Mercado, Nova DasSarma, Robert Lasenby, Robin Larson, Sam Ringer, Scott Johnston, Shauna Kravec, Sheer El Showk, Stanislav Fort, Tamera Lanham, Timothy Telleen-Lawton, Tom Conerly, Tom Henighan, Tristan Hume, Samuel R. Bowman, Zac Hatfield-Dodds, Ben Mann, Dario Amodei, Nicholas Joseph, Sam McCandlish, Tom Brown, Jared Kaplan

### Abstract
# Computer Science > Computation and Language # Title: Constitutional AI: Harmlessness from AI Feedback > Abstract: As AI systems become more capable, we would like to enlist their help to supervise other AIs. We experiment with methods for training a harmless AI assistant through self-improvement, without any human labels identifying harmful outputs. The only human oversight is provided through a list of rules or principles, and so we refer to the method as 'Constitutional AI'. The process involves both a supervised learning and a reinforcement learning phase. In the supervised phase we sample from an initial model, then generate self-critiques and revisions, and then finetune the original model on revised responses. In the RL phase, we sample from the finetuned model, use a model to evaluate which of the two samples is better, and then train a preference model from this dataset of AI preferences. We then train with RL using the preference model as the reward signal, i.e. we use 'RL from AI Feedback' (RLAIF). As a result we are able to train a harmless but non-evasive AI assistant that engages with harmful queries by explaining its objections to them. Both the SL and RL methods can leverage chain-of-thought style reasoning to improve the human-judged performance and transparency of AI decision making. These methods make it possible to control AI behavior more precisely and with far fewer human labels. ## Submission history ## Access Paper: - View PDF - HTML (experimental) - TeX Source ### Additional Features - Audio Summary ### Current browse context: ### References & Citations - SciX - Google Scholar - Semantic Scholar ### 2 blog links ## BibTeX formatted citation ### Bookmark # Bibliographic and Citation Tools # Code, Data and Media Associated with this Article # Demos # Recommenders and Search Tools - Author - Venue - Institution - Topic # arXivLabs: experimental projects with community collaborators arXiv

## arXiv:2209.00626 — The Alignment Problem from a Deep Learning Perspective
- **Reference:** Red Teaming Language Models to Reduce Harms (Ganguli, Amodei et al., 2022)
- **URL:** https://arxiv.org/abs/2209.00626
- **Authors:** Richard Ngo, Lawrence Chan, Sören Mindermann

### Abstract
# Computer Science > Artificial Intelligence # Title: The Alignment Problem from a Deep Learning Perspective > Abstract: In coming years or decades, artificial general intelligence (AGI) may surpass human capabilities across many critical domains. We argue that, without substantial effort to prevent it, AGIs could learn to pursue goals that are in conflict (i.e. misaligned) with human interests. If trained like today's most capable models, AGIs could learn to act deceptively to receive higher reward, learn misaligned internally-represented goals which generalize beyond their fine-tuning distributions, and pursue those goals using power-seeking strategies. We review emerging evidence for these properties. In this revised paper, we include more direct empirical evidence published as of early 2025. AGIs with these properties would be difficult to align and may appear aligned even when they are not. Finally, we briefly outline how the deployment of misaligned AGIs might irreversibly undermine human control over the world, and we review research directions aimed at preventing this outcome. ## Submission history ## Access Paper: - View PDF - HTML (experimental) - TeX Source ### Additional Features - Audio Summary ### Current browse context: ### References & Citations - SciX - Google Scholar - Semantic Scholar ### 3 blog links ## BibTeX formatted citation ### Bookmark # Bibliographic and Citation Tools # Code, Data and Media Associated with this Article # Demos # Recommenders and Search Tools - Author - Venue - Institution - Topic # arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with

## arXiv:2204.05862 — Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback
- **Reference:** Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback (Bai et al., 2022)
- **URL:** https://arxiv.org/abs/2204.05862
- **Authors:** Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, Nicholas Joseph, Saurav Kadavath, Jackson Kernion, Tom Conerly, Sheer El-Showk, Nelson Elhage, Zac Hatfield-Dodds, Danny Hernandez, Tristan Hume, Scott Johnston, Shauna Kravec, Liane Lovitt, Neel Nanda, Catherine Olsson, Dario Amodei, Tom Brown, Jack Clark, Sam McCandlish, Chris Olah, Ben Mann, Jared Kaplan

### Abstract
# Computer Science > Computation and Language # Title: Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback > Abstract: We apply preference modeling and reinforcement learning from human feedback (RLHF) to finetune language models to act as helpful and harmless assistants. We find this alignment training improves performance on almost all NLP evaluations, and is fully compatible with training for specialized skills such as python coding and summarization. We explore an iterated online mode of training, where preference models and RL policies are updated on a weekly cadence with fresh human feedback data, efficiently improving our datasets and models. Finally, we investigate the robustness of RLHF training, and identify a roughly linear relation between the RL reward and the square root of the KL divergence between the policy and its initialization. Alongside our main results, we perform peripheral analyses on calibration, competing objectives, and the use of OOD detection, compare our models with human writers, and provide samples from our models using prompts appearing in recent related work. ## Submission history ## Access Paper: - View PDF - HTML (experimental) - TeX Source ### Additional Features - Audio Summary ### Current browse context: ### References & Citations - SciX - Google Scholar - Semantic Scholar ### 1 blog link ## BibTeX formatted citation ### Bookmark # Bibliographic and Citation Tools # Code, Data and Media Associated with this Article # Demos # Recommenders and Search Tools - Author - Venue - Institution - Topic # arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is c


---
## Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet (May 2024)
- **URL:** https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html


# Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet



# Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet



### Authors



### Affiliations



### Published


Eight months ago, we demonstrated that sparse autoencoders could recover monosemantic features from a small one-layer transformer. At the time, a major concern was that this method might not scale feasibly to state-of-the-art transformers and, as a result, be unable to practically contribute to AI safety. Since then, scaling sparse autoencoders has been a major priority of the Anthropic interpretability team, and we're pleased to report extracting high-quality features from Claude 3 Sonnet , For clarity, this is the 3.0 version of Claude 3 Sonnet, released March 4, 2024. It is the exact model in production as of the writing of this paper. It is the finetuned model, not the base pretrained model (although our method also works on the base model). Anthropic's medium-sized production model.

We find a diversity of highly abstract features. They both respond to and behaviorally cause abstract behaviors. Examples of features we find include features for famous people, features for countries and cities, and features tracking type signatures in code. Many features are multilingual (responding to the same concept across languages) and multimodal (responding to the same concept in both text and images), as well as encompassing both abstract and concrete instantiations of the same idea (such as code with security vulnerabilities, and abstract discussion of security vulnerabilities).

Some of the features we find are of particular interest because they may be safety-relevant – that is, they are plausibly connected to a range of ways in which modern AI systems may cause harm. In particular, we find features related to security vulnerabilities and backdoors in code ; bias (including both overt slurs, and more subtle biases); lying, deception, and power-seeking (including treacherous turns); sycophancy ; and dangerous / criminal content (e.g., producing bioweapons). However, we caution not to read too much into the mere existence of such features: there's a difference (for example) between knowing about lies, being capable of lying, and actually lying in the real world. This research is also very preliminary. Further work will be needed to understand the implications of these potentially safety-relevant features.


### Key Results


- Sparse autoencoders produce interpretable features for large models.

- Scaling laws can be used to guide the training of sparse autoencoders.

- The resulting features are highly abstract: multilingual, multimodal, and generalizing between concrete and abstract references.

- There appears to be a systematic relationship between the frequency of concepts and the dictionary size needed to resolve features for them.

- Features can be used to steer large models ( see e.g. Influence on Behavior ). This extends prior work on steering models using other methods (see Related Work ).

- We observe features related to a broad range of safety concerns, including deception , sycophancy , bias , and dangerous content .


## Scaling Dictionary Learning to Claude 3 Sonnet


Our general approach to understanding Claude 3 Sonnet is based on the linear representation hypothesis ( see e.g. ) and the superposition hypothesis ( see e.g. ). For an introduction to these ideas, we refer readers to the Background and Motivation section of Toy Models . At a high level, the linear representation hypothesis suggests that neural networks represent meaningful concepts – referred to as features – as directions in their activation spaces. The superposition hypothesis accepts the idea of linear representations and further hypothesizes that neural networks use the existence of almost-orthogonal directions in high-dimensional spaces to represent more features than there are dimensions.

If one believes these hypotheses, the natural approach is to use a standard method called dictionary learning . Recently, several papers have suggested that this can be quite effective for transformer language models . In particular, a specific approximation of dictionary learning called a sparse autoencoder appears to be very effective .

To date, these efforts have been on relatively small language models by the standards of modern foundation models. Our previous paper , which focused on a one-layer model, was a particularly extreme example of this. As a result, an important question has been left hanging: will these methods work for large models? Or is there some reason, whether pragmatic questions of engineering or more fundamental differences in how large models operate, that would mean these efforts can't generalize?

This context motivates our project of scaling sparse autoencoders to Claude 3 Sonnet, Anthropic's medium-scale production model. The rest of this section will review our general sparse autoencoder setup, the specifics of the three sparse autoencoders we'll analyze in this paper, and how we used scaling laws to make informed decisions about the design of our sparse autoencoders. From there, we'll dive into analyzing the features our sparse autoencoders learn – and the interesting properties of Claude 3 Sonnet they reveal.


### Sparse Autoencoders


Our high-level goal in this work is to decompose the activations of a model (Claude 3 Sonnet) into more interpretable pieces. We do so by training a sparse autoencoder (SAE) on the model activations, as in our prior work and that of several other groups ( e.g. ; see Related Work ). SAEs are an instance of a family of “sparse dictionary learning” algorithms that seek to decompose data into a weighted sum of sparsely active components.

Our SAE consists of two layers. The first layer (“encoder”) maps the activity to a higher-dimensional layer via a learned linear transformation followed by a ReLU nonlinearity. We refer to the units of this high-dimensional layer as “features.” The second layer (“decoder”) attempts to reconstruct the model activations via a linear transformation of the feature activations. The model is trained to minimize a combination of (1) reconstruction error and (2) an L1 regularization penalty on the feature activations, which incentivizes sparsity.

Once the SAE is trained, it provides us with an approximate decomposition of the model’s activations into a linear combination of “feature directions” (SAE decoder weights) with coefficients equal to the feature activations. The sparsity penalty ensures that, for many given inputs to the model, a very small fraction of features will have nonzero activations. Thus, for any given token in any given context, the model activations are “explained” by a small set of active features (out of a large pool of possible features). For more motivation and explanation of SAEs, see the Problem Setup section of Towards Monosemanticity .

Here’s a brief overview of our methodology which we described in greater detail in Update on how we train SAEs from our April 2024 Update.

As a preprocessing step we apply a scalar normalization to the model activations so their average squared L2 norm is the residual stream dimension, D . We denote the normalized activations as \mathbf{x} \in \mathbb{R}^D , and attempt to decompose this vector using F features as follows:

\hat{\mathbf{x}} = \mathbf{b}^{dec} + \sum_{i=1}^F f_i(\mathbf{x}) \mathbf{W}^{dec}_{\cdot,i}

where W^{dec} \in \mathbb{R}^{D \times F} are the learned SAE decoder weights, \mathbf{b}^{dec} \in \mathbb{R}^D are learned biases, and f_i denotes the activity of feature i . Feature activations are given by the output of the encoder:

f_i(x) = \text{ReLU}\left(\mathbf{W}^{enc}_{i, \cdot} \cdot \mathbf{x} +b^{enc}_i \right)

where W^{enc} \in \mathbb{R}^{F \times D} are the learned SAE encoder weights, and \mathbf{b}^{enc} \in \mathbb{R}^F are learned biases.

The loss function \mathcal{L} is the combination of an L2 penalty on the reconstruction loss and an L1 penalty on feature activations.

\mathcal{L} = \mathbb{E}_\mathbf{x} \left[ \|\mathbf{x}-\hat{\mathbf{x}}\|_2^2 + \lambda\sum_i f_i(\mathbf{x}) \cdot \|\mathbf{W}^{dec}_{\cdot,i}\|_2 \right]

Including the factor of \|\mathbf{W}^{dec}_{\cdot,i}\|_2 in the L1 penalty term allows us to interpret the unit-normalized decoder vectors \frac{\mathbf{W}^{dec}_{\cdot,i}}{\|\mathbf{W}^{dec}_{\cdot,i}\|_2} as “feature vectors” or “feature directions,” and the product f_i(\mathbf{x}) \cdot \|\mathbf{W}^{dec}_{\cdot,i}\|_2 as the feature activations This also prevents the SAE from “cheating” the L1 penalty by making f_i(\mathbf{x}) small and \mathbf{W}^{dec}_{\cdot,i} large in a way that leaves the reconstructed activations unchanged. . Henceforth we will use “feature activation” to refer to this quantity.


### Our SAE experiments


Claude 3 Sonnet is a proprietary model for both safety and competitive reasons. Some of the decisions in this publication reflect this, such as not reporting the size of the model, leaving units off certain plots, and using a simplified tokenizer. For more information on how Anthropic thinks about safety considerations in publishing research results, we refer readers to our Core Views on AI Safety .

In this work, we focused on applying SAEs to residual stream activations halfway through the model (i.e. at the “middle layer”). We made this choice for several reasons. First, the residual stream is smaller than the MLP layer, making SAE training and inference computationally cheaper. Second, focusing on the residual stream in theory helps us mitigate an issue we call “cross-layer superposition” (see Limitations for more discussion). We chose to focus on the middle layer of the model because we reasoned that it is likely to contain interesting, abstract features (see e.g., ).

We trained three SAEs of varying sizes: 1,048,576 (~1M), 4,194,304 (~4M), and 33,554,432 (~34M) features. The number of training steps for the 34M feature run was selected using a scaling laws analysis to minimize the training loss given a fixed compute budget (see below). We used an L1 coefficient of 5 Our L1 coefficient is only relevant in the context of how we normalize activations. See Update on how we train SAEs for full details. . We performed a sweep over a narrow range of learning rates (suggested by the scaling laws analysis) and chose the value that gave the lowest loss.

For all three SAEs, the average number of features active (i.e. with nonzero activations) on a given token was fewer than 300, and the SAE reconstruction explained at least 65% of the variance of the model activations. At the end of training, we defined “dead” features as those which were not active over a sample of 10^{7} tokens. The proportion of dead features was roughly 2% for the 1M SAE, 35% for the 4M SAE, and 65% for the 34M SAE. We expect that improvements to the training procedure may be able to reduce the number of dead features in future experiments.


### Scaling Laws


Training SAEs on larger models is computationally intensive. It is important to understand (1) the extent to which additional compute improves dictionary learning results, and (2) how that compute should be allocated to obtain the highest-quality dictionary possible for a given computational budget.

Though we lack a gold-standard method of assessing the quality of a dictionary learning run, we have found that the loss function we use during training – a weighted combination of reconstruction mean-squared error (MSE) and an L1 penalty on feature activations – is a useful proxy, conditioned on a reasonable choice of the L1 coefficient. That is, we have found that dictionaries with low loss values (using an L1 coefficient of 5) tend to produce interpretable features and to improve other metrics of interest (the L0 norm, and the number of dead or otherwise degenerate features). Of course, this is an imperfect metric, and we have little confidence that it is optimal. It may well be the case that other L1 coefficients (or other objective functions altogether) would be better proxies to optimize.

With this proxy, we can treat dictionary learning as a standard machine learning problem, to which we can apply the “scaling laws” framework for hyperparameter optimization ( see e.g. ). In an SAE, compute usage primarily depends on two key hyperparameters: the number of features being learned, and the number of steps used to train the autoencoder (which maps linearly to the amount of data used, as we train the SAE for only one epoch). The compute cost scales with the product of these parameters if the input dimension and other hyperparameters are held constant.

We conducted a thorough sweep over these parameters, fixing the values of other hyperparameters (learning rate, batch size, optimization protocol, etc.). We were also interested in tracking the compute-optimal values of the loss function and parameters of interest; that is, the lowest loss that can be achieved using a given compute budget, and the number of training steps and features that achieve this minimum.

We make the following observations:

Over the ranges we tested, given the compute-optimal choice of training steps and number of features, loss decreases approximately according to a power law with respect to compute.

As the compute budget increases, the optimal allocations of FLOPS to training steps and number of features both scale approximately as power laws. In general, the optimal number of features appears to scale somewhat more quickly than the optimal number of training steps at the compute budgets we tested, though this trend may change at higher compute budgets.

These analyses used a fixed learning rate. For different compute budgets, we subsequently swept over learning rates at different optimal parameter settings according to the plots above. The inferred optimal learning rates decreased approximately as a power law as a function of compute budget, and we extrapolated this trend to choose learning rates for the larger runs.


## Assessing Feature Interpretability


In the previous section, we described how we trained sparse autoencoders on Claude 3 Sonnet. And as predicted by scaling laws, we achieved lower losses by training large SAEs. But the loss is only a proxy for what we actually care about: interpretable features that explain model behavior.

The goal of this section is to investigate whether these features are actually interpretable and explain model behavior. We'll first look at a handful of relatively straightforward features and provide evidence that they're interpretable. Then we'll look at two much more complex features, and demonstrate that they track very abstract concepts. We'll close with an experiment using automated interpretability to evaluate a larger number of features and compare them to neurons.


### Four Examples of Interpretable Features


In this subsection, we'll look at a few features and argue that they are genuinely interpretable. Our goal is just to demonstrate that interpretable features exist, leaving strong claims (such as most features being interpretable) to a later section. We will provide evidence that our interpretations are good descriptions of what the features represent and how they function in the network, using an analysis similar to that in Towards Monosemanticity .

The features we study in this section respond to:

- The Golden Gate Bridge 34M/31164353 : Descriptions of or references to the Golden Gate Bridge.

- Brain sciences 34M/9493533 : discussions of neuroscience and related academic research on brains or minds.

- Monuments and popular tourist attractions 1M/887839

- Transit infrastructure 1M/3

Here and elsewhere in the paper, for each feature, we show representative examples from the top 20 text inputs in our SAE dataset, as ranked by how strongly they activate that feature (see the appendix for details ). A larger, randomly sampled set of activations can be found by clicking on the feature ID. The highlight colors indicate activation strength at each token (white: no activation, orange : strongest activation).

While these examples suggest interpretations for each feature, more work needs to be done to establish that our interpretations truly capture the behavior and function of the corresponding features. Concretely, for each feature, we attempt to establish the following claims:

- When the feature is active, the relevant concept is reliably present in the context ( specificity ).

- Intervening on the feature’s activation produces relevant downstream behavior ( influence on behavior ).


### Specificity


It is difficult to rigorously measure the extent to which a concept is present in a text input. In our prior work, we focused on features that unambiguously corresponded to sets of tokens (e.g., Arabic script or DNA sequences) and computed the likelihood of that set of tokens relative to the rest of the vocabulary, conditioned on the feature’s activation. This technique does not generalize to more abstract features. Instead, to demonstrate specificity in this work we more heavily leverage automated interpretability methods (similar to ). We use the same automated interpretability pipeline as in our previous work in the features vs. neurons section below, but we additionally find that current-generation models can now more accurately rate text samples according to how well they match a proposed feature interpretation.

We constructed the following rubric for scoring how a feature’s description relates to the text on which it fires. We then asked Claude 3 Opus to rate feature activations at many tokens on that rubric.

- 0 – The feature is completely irrelevant throughout the context (relative to the base distribution of the internet).

- 1 – The feature is related to the context, but not near the highlighted text or only vaguely related.

- 2 – The feature is only loosely related to the highlighted text or related to the context near the highlighted text.

- 3 – The feature cleanly identifies the activating text.

By scoring examples of activating text, we provide a measure of specificity for each feature. We also manually checked a number of examples to ensure they were generally handled correctly. The features in this section are selected to have straightforward interpretations, to make automated interpretability analysis more reliable. They are not intended to be a representative example of all features in our SAEs. Later, we provide an analysis of the interpretability of randomly sampled features. We also conduct in-depth explorations throughout the paper of many more features which have interesting interpretations which are more abstract or nuanced, and thus more difficult to quantitatively assess.

Below we show distributions of feature activations (excluding zero activations) for the four features mentioned above, along with example text and image inputs that induce low and high activations. Note that these features also activate on relevant images, despite our only performing dictionary learning on a text-based dataset!

First, we study a Golden Gate Bridge feature 34M/31164353 . Its greatest activations are essentially all references to the bridge, and weaker activations also include related tourist attractions, similar bridges, and other monuments. Next, a brain sciences feature 34M/9493533 activates on discussions of neuroscience books and courses, as well as cognitive science, psychology, and related philosophy. In the 1M training run, we also find a feature that strongly activates for various kinds of transit infrastructure 1M/3 including trains, ferries, tunnels, bridges, and even wormholes! A final feature 1M/887839 responds to popular tourist attractions including the Eiffel Tower, the Tower of Pisa, the Golden Gate Bridge, and the Sistine Chapel.

To quantify specificity, we used Claude 3 Opus to automatically score examples that activate these features according to the rubric above, with roughly 1000 activations of the feature drawn from the dataset used to train the dictionary learning model. We plot the frequency of each rubric score as a function of the feature’s activation level. We see that inputs that induce strong feature activations are all judged to be highly consistent with the proposed interpretation.

As in Towards Monosemanticity , we see that these features become less specific as the activation strength weakens. This could be due to the model using activation strengths to represent confidence in a concept being present. Or it may be that the feature activates most strongly for central examples of the feature, but weakly for related ideas – for example, the Golden Gate Bridge feature 34M/31164353 appears to weakly activate for other San Francisco landmarks. It could also reflect imperfection in our dictionary learning procedure. For example, it may be that the architecture of the autoencoder is not able to extract and discriminate among features as cleanly as we might want. And of course interference from features that are not exactly orthogonal could also be a culprit, making it more difficult for Sonnet itself to activate features on precisely the right examples. It is also plausible that our feature interpretations slightly misrepresent the feature's actual function, and that this inaccuracy manifests more clearly at lower activations. Nonetheless, we often find that lower activations tend to maintain some specificity to our interpretations, including related concepts or generalizations of the core feature. As an illustrative example, weak activations of the transit infrastructure feature 1M/3 include procedural mechanics instructions describing which through-holes to use for particular parts.

Moreover, we expect that very weak activations of features are not especially meaningful, and thus we are not too concerned with low specificity scores for these activation ranges. For instance, we have observed that techniques such as rounding feature activations below a threshold to zero can improve specificity at the low-activation end of the spectrum without substantially increasing the reconstruction error of the SAE, and there are a variety of techniques in the literature that potentially address the same issue .

Regardless, the activations that have the most impact on the model’s behavior are the largest ones, so it is encouraging to see high specificity among the strong activations.

Note that we have had more difficulty in quantifying feature sensitivity – that is, how reliably a feature activates for text that matches our proposed interpretation – in a scalable, rigorous way. This is due to the difficulty of generating text related to a concept in an unbiased fashion. Moreover, many features may represent something more specific than we are able to glean with our visualizations, in which case they would not respond reliably to text selected based on our proposed interpretation, and this problem gets harder the more abstract the features are. As a basic check, however, we observe that the Golden Gate Bridge feature still fires strongly on the first sentence of the Wikipedia article for the Golden Gate Bridge in various languages (after removing any English parentheticals). In fact, the Golden Gate Bridge feature is the top feature by average activation for every example below.

We leave further investigation of this issue to future work.


### Influence on Behavior


Next, to demonstrate whether our interpretations of features accurately describe their influence on model behavior, we experiment with feature steering , where we “clamp” specific features of interest to artificially high or low values during the forward pass (see Methodological Details for implementation details). This builds on a long history of modifying feature activations to test causal theories, as well as work on other approaches to model steering, discussed in Related Work. We conduct these experiments with prompts in the “Human:”/“Assistant:” format that Sonnet is typically used with. We find that feature steering is remarkably effective at modifying model outputs in specific, interpretable ways. It can be used to modify the model’s demeanor, preferences, stated goals, and biases; to induce it to make specific errors; and to circumvent model safeguards (see also Safety-Relevant Features ). We find this compelling evidence that our interpretations of features line up with how they are used by the model.

For instance, we see that clamping the Golden Gate Bridge feature 34M/31164353 to 10× its maximum activation value induces thematically-related model behavior. In this example, the model starts to self-identify as the Golden Gate Bridge! Similarly, clamping the Transit infrastructure feature 1M/3 to 5× its maximum activation value causes the model to mention a bridge when it otherwise would not. In each case, the downstream influence of the feature appears consistent with our interpretation of the feature, even though these interpretations were made based only on the contexts in which the feature activates and we are intervening in contexts in which the feature is inactive.


### Sophisticated Features


So far we have presented features in Claude 3 Sonnet that fire on relatively simple concepts. These features are in some ways similar to those found in Towards Monosemanticity which, because they were trained on the activations of a 1-layer Transformer, reflected a very shallow knowledge of the world. For example, we found features that correspond to predicting a range of common nouns conditioned on a fairly general context (e.g. biology nouns following “the” in the context of biology).

Sonnet, in contrast, is a much larger and more sophisticated model, so we expect that it contains features demonstrating depth and clarity of understanding. To study this, we looked for features that activate in programming contexts, because these contexts admit precise statements about e.g. correctness of code or the types of variables.


### Code error feature


We begin by considering a simple Python function for adding two arguments, but with a bug. One feature 1M/1013764 fires almost continuously upon encountering a variable incorrectly named “rihgt” (highlighted below):

This is certainly suspicious, but it could be a Python-specific feature, so we checked and found that 1M/1013764 also fires on similar bugs in C and Scheme:

To check whether or not this is a more general typo feature, we tested 1M/1013764 on examples of typos in English prose, and found that it does not fire in those.

So it is not a general “typo detector”: it has some specificity to code contexts.

But is 1M/1013764 just a “typos in code” feature? We also tested it on a number of other examples and found that it also fires on erroneous expressions (e.g., divide by zero) and on invalid input in function calls:

The two examples shown above are representative of a broader pattern. Looking through the dataset examples where this feature activates, we found instances of it activating for:

- Array overflow

- Asserting provably false claims (e.g. 1==2)

- Calling a function with string instead of int

- Divide by zero

- Adding a string to int

- Writing to a null ptr

- Exiting with nonzero error code

Some top dataset examples can be found below:

Thus, we concluded that 1M/1013764 represents a broad variety of errors in code. Note that we have not established that it exhaustively represents all forms of errors in code; indeed, we suspect that there are many features representing different kinds of errors.

But does it also control model behavior? We claim that it does, but will need to do different experiments to show this. The above experiments only support that the feature activates in response to bugs, and don't show a corresponding effect. As a result, we'll now turn to using feature steering (see methods and related work ) to demonstrate 1M/1013764 behavioral effects.

As a first experiment, we input a prompt with bug-free code and clamped the feature to a large positive activation. We see that the model proceeds to hallucinate an error message: The hallucinated error message includes the name of a real person, which we have redacted.

We can also intervene to clamp this feature to a large negative activation. Doing this for code that does contain a bug causes the model to predict what the code would have produced if the bug was not there!

Surprisingly, if we add an extra “ >>> ” to the end of the prompt (indicating that a new line of code is being written) and clamp the feature to a large negative activation, the model rewrites the code without the bug!

The last example is somewhat delicate – the “code rewriting” behavior is sensitive to the details of the prompt – but the fact that it occurs at all points to a deep connection between this feature and the model’s understanding of bugs in code.


### Features representing functions


We also discovered features that track specific function definitions and references to them in code. A particularly interesting example is an addition feature 1M/697189 , which activates on names of functions that add numbers. For example, this feature fires on “bar” when it is defined to perform addition, but not when it is defined to perform multiplication. Moreover, it fires at the end of any function definition that implements addition.

Remarkably, this feature even correctly handles function composition, activating in response to functions that call other functions that perform addition. In the following example, on the left, we redefine “bar” to call “foo”, therefore inheriting its addition operation and causing the feature to fire. On the right, “bar” instead calls the multiply operation from “goo”, and the feature does not fire.

We also verified that this feature is in fact involved in the model’s computation of addition-related functions. For instance, this feature is among the top ten features with strongest attributions (explained in Features as Computational Intermediates ) when the model is asked to execute a block of code involving an addition function.

Thus this feature appears to represent the function of addition being performed by the model, reminiscent of Todd et al. 's function vectors . To further test this hypothesis, we experimented with clamping the feature to be active on code that does not involve addition. When we do so, we find that the model is “tricked” into believing that it has been asked to execute an addition.


### Features vs. Neurons


A natural question to ask about SAEs is whether the feature directions they uncover are more interpretable than, or even distinct from, the neurons of the model. We fit our SAEs on residual stream activity, which to first approximation has no privileged basis ( but see ) – thus the directions in the residual stream are not especially meaningful. However, residual stream activity receives inputs from all preceding MLP layers. Thus, a priori, it could be the case that SAEs identify feature directions in the residual stream whose activity reflects the activity of individual neurons in preceding layers. If that were the case, fitting an SAE would not be particularly useful, as we could have identified the same features by simply inspecting MLP neurons.

To address this question, for a random subset of the features in our 1M SAE, we measured the Pearson correlation between its activations and those of every neuron in all preceding layers. Similar to our findings in Towards Monosemanticity , we find that for the vast majority of features, there is no strongly correlated neuron – for 82% of our features, the most-correlated neuron has a correlation of 0.3 or smaller. Manually inspecting visualizations for the best-matching neuron for a random set of features, we found almost no resemblance in semantic content between the feature and the corresponding neuron. We additionally confirmed that feature activations are not strongly correlated with activations of any residual stream basis direction.

Even if dictionary learning features are not highly correlated with any individual neurons, it could still be the case that the neurons are interpretable. However, upon manual inspection of a random sample of 50 neurons and features each, the neurons appear significantly less interpretable than the features, typically activating in multiple unrelated contexts.

To quantify this difference, we first compared the interpretability of 100 randomly chosen features versus that of 100 randomly chosen neurons. We did this with the same automated interpretability approach outlined in Towards Monosemanticity , but using Claude 3 Opus to provide explanations of features and predict their held out activations. We find that activations of a random selection of SAE features are significantly more interpretable on average than a random selection of MLP neurons.

We additionally evaluated the specificity of random neurons and SAE features using the automated specificity rubric above. We find that the activations of a random selection of SAE features are significantly more specific than those of the neurons in the previous layer.


## Feature Survey


The features we find in Sonnet are rich and diverse. These range from features corresponding to famous people, to regions of the world (countries, cities, neighborhoods, and even famous buildings!), to features tracking type signatures in computer programs, and much more besides. Our goal in this section is to provide some sense of this breadth.

One challenge is that we have millions of features. Scaling feature exploration is an important open problem (see Limitations, Challenges, and Open Problems ), which we do not solve in this paper. Nevertheless, we have made some progress in characterizing the space of features, aided by automated interpretability . We will first focus on the local structure of features, which are often organized in geometrically-related clusters that share a semantic relationship. We then turn to understanding more global properties of features, such as how comprehensively they cover a given topic or category. Finally, we examine some categories of features we uncovered through manual inspection.


### Exploring Feature Neighborhoods


Here we walk through the local neighborhoods of several features of interest across the 1M, 4M and 34M SAEs, with closeness measured by the cosine similarity of the feature vectors. We find that this consistently surfaces features that share a related meaning or context — the interactive feature UMAP has additional neighborhoods to explore.


### Golden Gate Bridge feature


Focusing on a small neighborhood around the Golden Gate Bridge feature 34M/31164353 , we find that there are features corresponding to particular locations in San Francisco such as Alcatraz and the Presidio. More distantly, we also see features with decreasing degrees of relatedness, such as features related to Lake Tahoe, Yosemite National Park, and Solano County (which is near San Francisco). At greater distances, we also see features related in more abstract ways, like features corresponding to tourist attractions in other regions (e.g. “Médoc wine region, France”; “Isle of Skye, Scotland”). Overall, it appears that distance in decoder space maps roughly onto relatedness in concept space, often in interesting and unexpected ways.

We also find evidence of feature splitting , a phenomenon in which features in smaller SAEs “split” into multiple features in a larger SAE, which are geometrically close and semantically related to the original feature, but represent more specific concepts. For instance, a “San Francisco” feature in the 1M SAE splits into two features in the 4M SAE and eleven fine-grained features in the 34M SAE.

In addition to feature splitting, we also see examples in which larger SAEs contain features that represent concepts not captured by features in smaller SAEs. For instance, there is a group of earthquake features from the 4M and 34M SAEs that has no analog in this neighborhood in the 1M SAE, nor do any of the nearest 1M SAE features seem related.


### Immunology feature


The next feature neighborhood on our tour is centered around an Immunology feature 1M/533737 .

We see several distinct clusters within this neighborhood. Towards the top of the figure, we see a cluster focused on immunocompromised people, immunosuppression, diseases causing impaired immune function, and so on. As we move down and to the left, this transitions to a cluster of features focused on specific diseases (colds, flu, respiratory illness generally), then into immune response-related features, and then into features representing organ systems with immune involvement. In contrast, as we move down and to the right from the immunocompromised cluster, we see more features corresponding to microscopic aspects of the immune system (e.g. immunoglobulins), then immunology techniques (e.g. vaccines), and so on.

Towards the bottom, quite separated from the rest, we see a cluster of features related to immunity in non-medical contexts (e.g. legal/social).

These results are consistent with the trend identified above, in which nearby features in dictionary vector space touch on similar concepts.


### Inner Conflict feature


The last neighborhood we investigate in detail is centered around an Inner Conflict feature 1M/284095 . While this neighborhood does not cleanly separate out into clusters, we still find that different subregions are associated with different themes. For instance, there is a subregion corresponding to balancing tradeoffs, which sits near a subregion corresponding to opposing principles and legal conflict. These are relatively distant from a subregion focused more on emotional struggle, reluctance, and guilt.

We highly recommend exploring the neighborhoods of other features using our interactive interface to get a sense both for how proximity in decoder space corresponds to similarity of concepts and for the breadth of concepts represented.


### Feature Completeness


We were curious about the breadth and completeness with which our features cover the space of concepts. For instance, does the model have a feature corresponding to every major world city? To study questions like this, we used Claude to search for features which fired on members of particular families of concepts/terms. Specifically:

- We pass a prompt with the relevant concept (e.g. “The physicist Richard Feynman”) to the model and see which features activate on the final token.

- We then take the top five features by activation magnitude and run them through our automated interpretability pipeline, asking Sonnet to provide explanations of what those features fire on.

- We then look at each of the top 5 explanations and a human rater judges whether the concept, or some subset of the concept, is specifically indicated by the model-generated explanation as the most important part of the feature As an example of how we draw these boundaries, mentions of mid-20th century physicists such as Richard Feynman would not count, but mentions of mid-20th century physicists, especially Richard Feynman would (just barely) count, though most cases are much more clear-cut. .

We find increasing coverage of concepts as we increase the number of features, though even in the 34M SAE we see evidence that the set of features we uncovered is an incomplete description of the model’s internal representations. For instance, we confirmed that Claude 3 Sonnet can list all of the London boroughs when asked, and in fact can name tens of individual streets in many of the areas. However, we could only find features corresponding to about 60% of the boroughs in the 34M SAE. This suggests that the model contains many more features than we have found, which may be able to be extracted with even larger SAEs.

We also took a more detailed look at what determines whether a feature corresponding to a concept is present in our SAEs. If one looks at the frequency of the elements in a proxy of the SAE training data, we find that representation in our dictionaries is closely tied with the frequency of the concept in the training data. For instance, chemical elements which are mentioned often in the training data almost always have corresponding features in our dictionary, while those which are mentioned rarely or not at all do not. Since the SAEs were trained on a data mixture very similar to Sonnet’s pre-training data, it’s unclear to what extent feature learning is dependent on frequency in the model’s training data rather than on the SAE’s training data. Frequency in training data is measured by a search for <space>[Name]<space> , which causes some false positives in cases like the element “lead”.

We quantified this relationship for four different categories of concepts – elements, cities, animals and foods (fruits and vegetables) – using 100–200 concepts in each category. We focused on concepts that could be unambiguously expressed by a single word (i.e. that word has few other common meanings) and with a wide distribution of frequencies in text data. We found a consistent tendency for the larger SAEs to have features for concepts that are rarer in the training data, with the rough “threshold” frequency required for a feature to be present being similar across categories.

Notably, for each of the three runs, the frequency in the training data at which the dictionary becomes more than 50% likely to include a concept is consistently slightly lower than the inverse of the number of alive features (the 34M model having only about 12M alive features). We can show this more clearly by rescaling the x -axis for each line by the number of alive features, finding that the lines end up approximately overlapping, following a common curve that resembles a sigmoid in log-frequency space. Speculatively, this may be connected to Zipf’s law, a common phenomenon in which the frequency of the n th most common object in a population, relative to the most common, is roughly 1/n . Zipf’s law would predict that, for example, the millionth feature would represent a concept 10× rarer than the hundred thousandth feature.

This finding gives us some handle on the SAE scale at which we should expect a concept-specific feature to appear – if a concept is present in the training data only once in a billion tokens, then we should expect to need a dictionary with on the order of a billion alive features in order to find a feature which uniquely represents that specific concept. Importantly, not having a feature dedicated to a particular concept does not mean that the reconstructed activations do not contain information about that concept, as the model can use multiple related features compositionally to reference a specific concept. For example, if there were features for “large non-capital city” and “in New York state”, those together would suffice to specify New York City.

This also informs how much data we should expect to need in order to train larger dictionaries – if we assume that the SAE needs to see data corresponding to a feature a certain fixed number of times during training in order to learn it, then the amount of SAE training data needed to learn N features would be proportional to N .


### Feature Categories


Through manual inspection, we identified a number of other interesting categories of features. Here we describe several of these, in the spirit of providing a flavor of what we see in our dictionaries rather than attempting to be complete or prescriptive.


### Person Features


To start, we find many features corresponding to famous individuals, which are active on descriptions of those people as well as relevant historical context.


### Country Features


Next, we see features which only activate strongly on references to specific countries. From the top activating examples, we can see that many of these features fire not just on the country name itself, but also when the country is being described.


### Basic Code Features


We also see a number of features that represent different syntax elements or other low-level concepts in code, which give the impression of syntax highlighting when visualized together (here for simplicity we binarize activation information, only distinguishing between zero vs. nonzero activations):

These features were chosen primarily to fire on the Python examples. We have found that there is some transfer from Python code features to related languages like Java, but not more distant ones (e.g. Haskell), suggesting at least some level of language specificity. We hypothesize that more abstract features are more likely to span many languages, but so far have only found one concrete example of this (see the Code error feature ).


### List Position Features


Finally, we see fe