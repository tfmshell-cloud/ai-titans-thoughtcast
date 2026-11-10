# Landmark Scientific Papers: Google Brain Cat Neuron, Inverted Helicopters & Baidu Deep Speech

## OpenAlex Citation Telemetry

### Google Brain 16,000-Core Cat Neuron (ICML 2012)

- **TensorFlow: A system for large-scale machine learning** (2016, arXiv (Cornell University)) — **Citations: 16614** (`https://doi.org/10.48550/arxiv.1605.08695`)
- **Momentum Contrast for Unsupervised Visual Representation Learning** (2020, IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings - IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings) — **Citations: 14187** (`https://doi.org/10.1109/cvpr42600.2020.00975`)
- **Intriguing properties of neural networks** (2013, arXiv (Cornell University)) — **Citations: 14009** (`https://doi.org/10.48550/arxiv.1312.6199`)

### Stanford Autonomous Inverted Helicopter RL (Abbeel & Ng)

- **End-to-End Driving Via Conditional Imitation Learning** (2018, Proceedings - IEEE International Conference on Robotics and Automation/Proceedings) — **Citations: 1231** (`https://doi.org/10.1109/icra.2018.8460487`)
- **Challenges of real-world reinforcement learning: definitions, benchmarks and analysis** (2021, Machine Learning) — **Citations: 910** (`https://doi.org/10.1007/s10994-021-05961-4`)
- **Recent Advances in Robot Learning from Demonstration** (2019, Annual Review of Control Robotics and Autonomous Systems) — **Citations: 838** (`https://doi.org/10.1146/annurev-control-100819-063206`)

### Baidu SVAIL Deep Speech (2014–2015)

- **Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification** (2015, IEEE/CVF International Conference on Computer Vision (ICCV)) — **Citations: 20943** (`https://doi.org/10.1109/iccv.2015.123`)
- **Towards Evaluating the Robustness of Neural Networks** (2017, IEEE Symposium on Security and Privacy (S&P)) — **Citations: 9348** (`https://doi.org/10.1109/sp.2017.49`)
- **Gaussian Error Linear Units (GELUs)** (2016, arXiv (Cornell University)) — **Citations: 8787** (`https://doi.org/10.48550/arxiv.1606.08415`)

## arXiv Abstracts & Metadata

### Deep Speech 2: End-to-End Speech Recognition in English and Mandarin (`http://arxiv.org/abs/1512.02595v1`, published `2015-12-08`)

**Authors:** Dario Amodei, Rishita Anubhai, Eric Battenberg, Carl Case, Jared Casper, Bryan Catanzaro, Jingdong Chen, Mike Chrzanowski, Adam Coates, Greg Diamos, Erich Elsen, Jesse Engel, Linxi Fan, Christopher Fougner, Tony Han, Awni Hannun, Billy Jun, Patrick LeGresley, Libby Lin, Sharan Narang, Andrew Ng, Sherjil Ozair, Ryan Prenger, Jonathan Raiman, Sanjeev Satheesh, David Seetapun, Shubho Sengupta, Yi Wang, Zhiqian Wang, Chong Wang, Bo Xiao, Dani Yogatama, Jun Zhan, Zhenyao Zhu

We show that an end-to-end deep learning approach can be used to recognize either English or Mandarin Chinese speech--two vastly different languages. Because it replaces entire pipelines of hand-engineered components with neural networks, end-to-end learning allows us to handle a diverse variety of speech including noisy environments, accents and different languages. Key to our approach is our application of HPC techniques, resulting in a 7x speedup over our previous system. Because of this efficiency, experiments that previously took weeks now run in days. This enables us to iterate more quickly to identify superior architectures and algorithms. As a result, in several cases, our system is competitive with the transcription of human workers when benchmarked on standard datasets. Finally, using a technique called Batch Dispatch with GPUs in the data center, we show that our system can be inexpensively deployed in an online setting, delivering low latency when serving users at scale.

### Deep Speech: Scaling up end-to-end speech recognition (`http://arxiv.org/abs/1412.5567v2`, published `2014-12-17`)

**Authors:** Awni Hannun, Carl Case, Jared Casper, Bryan Catanzaro, Greg Diamos, Erich Elsen, Ryan Prenger, Sanjeev Satheesh, Shubho Sengupta, Adam Coates, Andrew Y. Ng

We present a state-of-the-art speech recognition system developed using end-to-end deep learning. Our architecture is significantly simpler than traditional speech systems, which rely on laboriously engineered processing pipelines; these traditional systems also tend to perform poorly when used in noisy environments. In contrast, our system does not need hand-designed components to model background noise, reverberation, or speaker variation, but instead directly learns a function that is robust to such effects. We do not need a phoneme dictionary, nor even the concept of a "phoneme." Key to our approach is a well-optimized RNN training system that uses multiple GPUs, as well as a set of novel data synthesis techniques that allow us to efficiently obtain a large amount of varied data for training. Our system, called Deep Speech, outperforms previously published results on the widely studied Switchboard Hub5'00, achieving 16.0% error on the full test set. Deep Speech also handles challenging noisy environments better than widely used, state-of-the-art commercial speech systems.

### The Synchrosqueezing algorithm for time-varying spectral analysis: robustness properties and new paleoclimate applications (`http://arxiv.org/abs/1105.0010v3`, published `2011-04-29`)

**Authors:** Gaurav Thakur, Eugene Brevdo, Neven S. Fučkar, Hau-Tieng Wu

We analyze the stability properties of the Synchrosqueezing transform, a time-frequency signal analysis method that can identify and extract oscillatory components with time-varying frequency and amplitude. We show that Synchrosqueezing is robust to bounded perturbations of the signal and to Gaussian white noise. These results justify its applicability to noisy or nonuniformly sampled data that is ubiquitous in engineering and the natural sciences. We also describe a practical implementation of Synchrosqueezing and provide guidance on tuning its main parameters. As a case study in the geosciences, we examine characteristics of a key paleoclimate change in the last 2.5 million years, where Synchrosqueezing provides significantly improved insights.

### Building high-level features using large scale unsupervised learning (`http://arxiv.org/abs/1112.6209v5`, published `2011-12-29`)

**Authors:** Quoc V. Le, Marc'Aurelio Ranzato, Rajat Monga, Matthieu Devin, Kai Chen, Greg S. Corrado, Jeff Dean, Andrew Y. Ng

We consider the problem of building high-level, class-specific feature detectors from only unlabeled data. For example, is it possible to learn a face detector using only unlabeled images? To answer this, we train a 9-layered locally connected sparse autoencoder with pooling and local contrast normalization on a large dataset of images (the model has 1 billion connections, the dataset has 10 million 200x200 pixel images downloaded from the Internet). We train this network using model parallelism and asynchronous SGD on a cluster with 1,000 machines (16,000 cores) for three days. Contrary to what appears to be a widely-held intuition, our experimental results reveal that it is possible to train a face detector without having to label images as containing a face or not. Control experiments show that this feature detector is robust not only to translation but also to scaling and out-of-plane rotation. We also find that the same network is sensitive to other high-level concepts such as cat faces and human bodies. Starting with these learned features, we trained our network to obtain 15.8% accuracy in recognizing 20,000 object categories from ImageNet, a leap of 70% relative improvement over the previous state-of-the-art.
