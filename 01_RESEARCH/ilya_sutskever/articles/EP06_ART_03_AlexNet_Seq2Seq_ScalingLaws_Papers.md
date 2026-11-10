# EP06_ART_03: Landmark Papers — AlexNet (NIPS 2012), Seq2Seq (arXiv:1409.3215), Scaling Laws (arXiv:2001.08361)

## 1. ImageNet Classification with Deep CNNs (Krizhevsky, Sutskever, Hinton — NIPS 2012)
ImageNet Classification with Deep Convolutional Neural Networks 

 NeurIPS Proceedings 

 Search 

ImageNet Classification with Deep Convolutional Neural Networks 

Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton 

 Advances in Neural Information Processing Systems 25 (NIPS 2012) 

 Bibtex Metadata Paper Supplemental 

Abstract 

We trained a large, deep convolutional neural network to classify the 1.3 million high-resolution images in the LSVRC-2010 ImageNet training set into the 1000 different classes. On the test data, we achieved top-1 and top-5 error rates of 39.7\% and 18.9\% which is considerably better than the previous state-of-the-art results. The neural network, which has 60 million parameters and 500,000 neurons, consists of five convolutional layers, some of which are followed by max-pooling layers, and two globally connected layers with a final 1000-way softmax. To make training faster, we used non-saturating neurons and a very efficient GPU implementation of convolutional nets. To reduce overfitting in the globally connected layers we employed a new regularization method that proved to be very effective. 

Name Change Policy 
 × 

Requests for name changes in the electronic proceedings will be accepted with no questions asked. However name changes may cause bibliographic tracking issues. Authors are asked to consider this carefully and discuss it with their co-authors prior to requesting a name change in the electronic proceedings. 

Use the "Report an Issue" link to request a name change. 

 Report an Issue    |    Name Change Policy 

Do not remove: This comment is monitored to verify that the site is working properly

## 2. Sequence to Sequence Learning with Neural Networks (Sutskever, Vinyals, Le — arXiv:1409.3215)
[1409.3215] Sequence to Sequence Learning with Neural Networks 

 Skip to main content 

 Search 

 Submit 
 Donate 

 Log in 

 Search arXiv 

 Press Enter to search · Advanced search 

-->

Computer Science > Computation and Language 

 arXiv:1409.3215 (cs)

 [Submitted on 10 Sep 2014 ( v1 ), last revised 14 Dec 2014 (this version, v3)] 

 Title: Sequence to Sequence Learning with Neural Networks 

 Authors: Ilya Sutskever , Oriol Vinyals , Quoc V. Le 
View a PDF of the paper titled Sequence to Sequence Learning with Neural Networks, by Ilya Sutskever and Oriol Vinyals and Quoc V. Le 
 View PDF 
 HTML (experimental) 

 Abstract: Deep Neural Networks (DNNs) are powerful models that have achieved excellent performance on difficult learning tasks. Although DNNs work well whenever large labeled training sets are available, they cannot be used to map sequences to sequences. In this paper, we present a general end-to-end approach to sequence learning that makes minimal assumptions on the sequence structure. Our method uses a multilayered Long Short-Term Memory (LSTM) to map the input sequence to a vector of a fixed dimensionality, and then another deep LSTM to decode the target sequence from the vector. Our main result is that on an English to French translation task from the WMT'14 dataset, the translations produced by the LSTM achieve a BLEU score of 34.8 on the entire test set, where the LSTM's BLEU score was penalized on out-of-vocabulary words. Additionally, the LSTM did not have difficulty on long sentences. For comparison, a phrase-based SMT system achieves a BLEU score of 33.3 on the same dataset. When we used the LSTM to rerank the 1000 hypotheses produced by the aforementioned SMT system, its BLEU score increases to 36.5, which is close to the previous best result on this task. The LSTM also learned sensible phrase and sentence representations that are sensitive to word order and are relatively invariant to the active and the passive voice. Finally, we found that reversing the order of the words in all source sentences (but not target sentences) improved the LSTM's performance markedly, because doing so introduced many short term dependencies between the source and the target sentence which made the optimization problem easier.

 Comments: 
 9 pages 

 Subjects: 

 Computation and Language (cs.CL) ; Machine Learning (cs.LG) 

 Cite as: 
 arXiv:1409.3215 [cs.CL] 

 (or 
 arXiv:1409.3215v3 [cs.CL] for this version)

 https://doi.org/10.48550/arXiv.1409.3215 

 Focus to learn more 

 arXiv-issued DOI via DataCite 

Submission history From: Ilya Sutskever [ view email ] 
 [v1] 
 Wed, 10 Sep 2014 19:55:35 UTC (37 KB)

 [v2] 
 Wed, 29 Oct 2014 12:13:17 UTC (66 KB)

 [v3] 
 Sun, 14 Dec 2014 20:59:51 UTC (66 KB)

 Full-text links: 

Access Paper: 

View a PDF of the paper titled Sequence to Sequence Learning with Neural Networks, by Ilya Sutskever and Oriol Vinyals and Quoc V. Le 
 View PDF 
 HTML (experimental) 
 TeX Source

 view license 

Additional Features 

 Audio Summary 

Current browse context: 

cs.CL 

 < prev 

   |   
 next > 

 new 
 | 
 recent 
 | 2014-09 

 Change to browse by:

 cs 

 cs.LG 

References & Citations 

 SciX 
 Google Scholar 

 Semantic Scholar 

 18 blog links ( what is this? )

 DBLP - CS Bibliography 

 listing | bibtex 

 Ilya Sutskever 
 Oriol Vinyals 
 Quoc V. Le 

 export BibTeX citation 
 Loading... 

BibTeX formatted citation 
 × 

 loading... 

 Data provided by: 

Bookmark 

 Bibliographic Tools 

Bibliographic and Citation Tools 

 Bibliographic Explorer Toggle 

 Bibliographic Explorer ( What is the Explorer? ) 

 Connected Papers Toggle 

 Connected Papers ( What is Connected Papers? ) 

 Litmaps Toggle 

 Litmaps ( What is Litmaps? ) 

 scite.ai Toggle 

 scite Smart Citations ( What are Smart Citations? ) 

 Code, Data, Media 

Code, Data and Media Associated with this Article 

 alphaXiv Toggle 

 alphaXiv ( What is alphaXiv? ) 

 Links to Code Toggle 

 CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) 

 DagsHub Toggle 

 DagsHub ( What is DagsHub? ) 

 GotitPub Toggle 

 Gotit.pub ( What is GotitPub? ) 

 Huggingface Toggle 

 Hugging Face ( What is Huggingface? ) 

 ScienceCast Toggle 

 ScienceCast ( What is ScienceCast? ) 

 Demos 

Demos 

 Replicate Toggle 

 Replicate ( What is Replicate? ) 

 Spaces Toggle 

 Hugging Face Spaces ( What is Spaces? ) 

 Spaces Toggle 

 TXYZ.AI ( What is TXYZ.AI? ) 

 Related Papers 

Recommenders and Search Tools 

 Link to Influence Flower 

 Influence Flower ( What are Influence Flowers? ) 

 Core recommender toggle 

 CORE Recommender ( What is CORE? ) 

 Author 

 Venue 

 Institution 

 Topic 

 About arXivLabs

arXivLabs: experimental projects with community collaborators 

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. 

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. 

Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs . 

 Which authors of this paper are endorsers? |
 Disable MathJax ( What is MathJax? )

 We gratefully acknowledge support from our major funders ,
 member institutions , ,
 and all contributors.

 About · 
 Help · 
 Contact · 
 Subscribe · 
 Copyright · 
 Privacy · 
 Accessibility · 
 Operational Status (opens in new tab)

## 3. Scaling Laws for Neural Language Models (Kaplan, McCandlish, Henighan, Brown, Chess, Child, Gray, Radford, Wu, Amodei — & OpenAI Scaling Lineage — arXiv:2001.08361)
[2001.08361] Scaling Laws for Neural Language Models 

 Skip to main content 

 Search 

 Submit 
 Donate 

 Log in 

 Search arXiv 

 Press Enter to search · Advanced search 

-->

Computer Science > Machine Learning 

 arXiv:2001.08361 (cs)

 [Submitted on 23 Jan 2020] 

 Title: Scaling Laws for Neural Language Models 

 Authors: Jared Kaplan , Sam McCandlish , Tom Henighan , Tom B. Brown , Benjamin Chess , Rewon Child , Scott Gray , Alec Radford , Jeffrey Wu , Dario Amodei 
View a PDF of the paper titled Scaling Laws for Neural Language Models, by Jared Kaplan and 9 other authors 
 View PDF 
 HTML (experimental) 

 Abstract: We study empirical scaling laws for language model performance on the cross-entropy loss. The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude. Other architectural details such as network width or depth have minimal effects within a wide range. Simple equations govern the dependence of overfitting on model/dataset size and the dependence of training speed on model size. These relationships allow us to determine the optimal allocation of a fixed compute budget. Larger models are significantly more sample-efficient, such that optimally compute-efficient training involves training very large models on a relatively modest amount of data and stopping significantly before convergence.

 Comments: 
 19 pages, 15 figures 

 Subjects: 

 Machine Learning (cs.LG) ; Machine Learning (stat.ML) 

 Cite as: 
 arXiv:2001.08361 [cs.LG] 

 (or 
 arXiv:2001.08361v1 [cs.LG] for this version)

 https://doi.org/10.48550/arXiv.2001.08361 

 Focus to learn more 

 arXiv-issued DOI via DataCite 

Submission history From: Samuel McCandlish [ view email ] 
 [v1] 
 Thu, 23 Jan 2020 03:59:20 UTC (1,520 KB)

 Full-text links: 

Access Paper: 

View a PDF of the paper titled Scaling Laws for Neural Language Models, by Jared Kaplan and 9 other authors 
 View PDF 
 HTML (experimental) 
 TeX Source

 view license 

Additional Features 

 Audio Summary 

Current browse context: 

cs.LG 

 < prev 

   |   
 next > 

 new 
 | 
 recent 
 | 2020-01 

 Change to browse by:

 cs 

 stat 

 stat.ML 

References & Citations 

 SciX 
 Google Scholar 

 Semantic Scholar 

 15 blog links ( what is this? )

 DBLP - CS Bibliography 

 listing | bibtex 

 Jared Kaplan 
 Sam McCandlish 
 Tom B. Brown 
 Rewon Child 
 Scott Gray 
… 

 export BibTeX citation 
 Loading... 

BibTeX formatted citation 
 × 

 loading... 

 Data provided by: 

Bookmark 

 Bibliographic Tools 

Bibliographic and Citation Tools 

 Bibliographic Explorer Toggle 

 Bibliographic Explorer ( What is the Explorer? ) 

 Connected Papers Toggle 

 Connected Papers ( What is Connected Papers? ) 

 Litmaps Toggle 

 Litmaps ( What is Litmaps? ) 

 scite.ai Toggle 

 scite Smart Citations ( What are Smart Citations? ) 

 Code, Data, Media 

Code, Data and Media Associated with this Article 

 alphaXiv Toggle 

 alphaXiv ( What is alphaXiv? ) 

 Links to Code Toggle 

 CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) 

 DagsHub Toggle 

 DagsHub ( What is DagsHub? ) 

 GotitPub Toggle 

 Gotit.pub ( What is GotitPub? ) 

 Huggingface Toggle 

 Hugging Face ( What is Huggingface? ) 

 ScienceCast Toggle 

 ScienceCast ( What is ScienceCast? ) 

 Demos 

Demos 

 Replicate Toggle 

 Replicate ( What is Replicate? ) 

 Spaces Toggle 

 Hugging Face Spaces ( What is Spaces? ) 

 Spaces Toggle 

 TXYZ.AI ( What is TXYZ.AI? ) 

 Related Papers 

Recommenders and Search Tools 

 Link to Influence Flower 

 Influence Flower ( What are Influence Flowers? ) 

 Core recommender toggle 

 CORE Recommender ( What is CORE? ) 

 IArxiv recommender toggle 

 IArxiv Recommender 
 ( What is IArxiv? ) 

 Author 

 Venue 

 Institution 

 Topic 

 About arXivLabs

arXivLabs: experimental projects with community collaborators 

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. 

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. 

Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs . 

 Which authors of this paper are endorsers? |
 Disable MathJax ( What is MathJax? )

 We gratefully acknowledge support from our major funders ,
 member institutions , ,
 and all contributors.

 About · 
 Help · 
 Contact · 
 Subscribe · 
 Copyright · 
 Privacy · 
 Accessibility · 
 Operational Status (opens in new tab)
