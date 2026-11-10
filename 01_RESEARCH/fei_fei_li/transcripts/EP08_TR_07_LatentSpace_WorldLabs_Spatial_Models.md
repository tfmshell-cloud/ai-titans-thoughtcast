# Latent Space: After LLMs — Spatial Intelligence & World Models (Fei-Fei Li & Justin Johnson)
- **YouTube URL:** https://www.youtube.com/watch?v=60iW8FZ7MJU
- **Lines:** 1805

---

[00:00:01] I think the whole history of deep
[00:00:01] learning is in some sense the the
[00:00:02] history of scaling up compute.
[00:00:03] >> When I graduated from grad school, I
[00:00:06] really thought the rest of [music] my
[00:00:07] entire career would be towards solving
[00:00:10] that single problem which is
[00:00:14] a lot of AI as a field as a discipline
[00:00:17] is inspired by human intelligence. We
[00:00:20] [music] thought we were the first people
[00:00:22] doing it. It turned out that was also
[00:00:24] simultaneously doing it.
[00:00:26] >> So marble like basically one way of
[00:00:28] looking at it, it's the system. It's a
[00:00:29] generative model of 3D worlds, right? So
[00:00:31] you can input [music] things like text
[00:00:33] or image or multiple images and it will
[00:00:34] generate for you a 3D world that kind of
[00:00:36] matches [music] those inputs. So while
[00:00:38] Marble is simultaneously a world model
[00:00:40] that is building towards this vision of
[00:00:42] spatial intelligence, it was also very
[00:00:44] intentionally [music] designed to be a
[00:00:46] thing that people could find useful
[00:00:48] today. Um, and we're see starting to see
[00:00:50] emerging use cases [music]
[00:00:51] um, in gaming, in VFX, um, in in film
[00:00:54] where I think there's a lot of really
[00:00:56] interesting stuff that Marvel [music]
[00:00:57] can do today as a product and then also
[00:00:59] set a foundation for the for the for the
[00:01:01] grand world models that we want to build
[00:01:03] going into the future.
[00:01:13] Hey everyone, welcome to the Len Space
[00:01:13] podcast. This is Allesio, founder of
[00:01:15] Colonel Labs, and I'm joined by Swix,
[00:01:17] editor of Blade in Space,
[00:01:18] >> and we are so excited to be in the
[00:01:20] studio with Fifi and Justin of uh World
[00:01:22] Labs. Welcome.
[00:01:24] >> We're excited, too.
[00:01:25] >> I nearly said Marble. [laughter]
[00:01:27] >> Yeah, thanks for having us. I think
[00:01:29] there's a lot of interest in world
[00:01:30] models and you've done you've done a
[00:01:32] little bit of publicity around spatial
[00:01:33] intelligence and all that. Um, I guess
[00:01:35] maybe one of the part of story that is a
[00:01:37] rare opportunity for you to tell is how
[00:01:39] you two came together uh to start
[00:01:41] building world apps. That's very easy
[00:01:44] because Justin [laughter] was my former
[00:01:45] student. Yeah. So Justin came to my I
[00:01:48] you know in my [clears throat] the other
[00:01:50] hat I wear is a professor of computer
[00:01:53] science at Stanford. Justin joined my
[00:01:55] lab when which year?
[00:01:57] >> Uh 2012 actually the the semester that I
[00:01:59] the quarter that I joined your lab was
[00:02:00] the same quarter that that uh Alex net
[00:02:02] came out.
[00:02:03] >> Yeah. Yeah. So Justin is my first
[00:02:05] >> Were you involved in the whole
[00:02:06] announcement uh drama I guess? No, no,
[00:02:08] not at all. But I was sort of watching
[00:02:10] all the imageet excitement around
[00:02:12] Alexnet at that that quarter.
[00:02:14] So he was my one of my very best
[00:02:17] students and uh and then he went on to
[00:02:20] have a very successful early career as a
[00:02:24] professor in Michigan University of
[00:02:26] Michigan and Arbor in Meta and then when
[00:02:29] we um I think around you know more than
[00:02:33] two years ago for sure I think both
[00:02:36] independently both of us have been
[00:02:38] looking at the development of the large
[00:02:40] models and thinking about what's beyond
[00:02:43] language models and and this idea of
[00:02:46] building world models, spatial
[00:02:47] intelligence uh really was natural for
[00:02:50] us. So we started talking and decided
[00:02:54] that we should just put all the eggs in
[00:02:57] one basket and focus on solving this
[00:03:00] problem and started world labs together.
[00:03:02] >> Yeah, pretty much. I mean like I after
[00:03:04] that seeing that kind of imageet era
[00:03:07] during my PhD um I had the sense that
[00:03:09] the next sort of decade of computer
[00:03:10] vision was going to be about getting
[00:03:11] getting AI out of the out of the data
[00:03:13] center and out into the world. Um so a
[00:03:16] lot of my interests post PhD kind of
[00:03:17] shifted in uh into 3D vision a little
[00:03:20] bit more into computer graphics uh more
[00:03:22] into generative modeling. Um and I was
[00:03:24] uh I thought I was kind of drifting away
[00:03:25] from my adviser post PhD but then when
[00:03:27] we reunited a couple years later it
[00:03:29] turned out she was thinking of very
[00:03:30] similar things. So if you think about
[00:03:32] AlexNet, the core pieces of it were
[00:03:34] obviously imageet, it was the move to
[00:03:36] GPUs and neural networks. How do you
[00:03:38] think about the AlexNet equivalent model
[00:03:41] for world models? In a way, it's an idea
[00:03:42] that has been out there, right? There's
[00:03:44] been, you know, Young Lagoon is maybe
[00:03:46] like the most the biggest proponent most
[00:03:47] prominent of it. What have you seen in
[00:03:49] the last two years that you were like,
[00:03:51] hey, now is the time to do this. And
[00:03:53] what are maybe the things um
[00:03:54] fundamentally that you want to build as
[00:03:56] far as data and kind of like maybe
[00:03:58] different types of uh algorithms or
[00:04:00] approaches to compute uh to make world
[00:04:02] models really come to life?
[00:04:04] >> Yeah, I I think one is just there is a
[00:04:06] lot more data in compute generally
[00:04:08] available. Um I think the whole history
[00:04:10] of deep learning is in some sense the
[00:04:11] the history of scaling up compute. Um
[00:04:13] and if you think about you know Alexet
[00:04:15] required this jump from CPUs to GPUs but
[00:04:17] even from Alexet to today we're getting
[00:04:19] about a thousand times more performance
[00:04:21] per card. um than we had in Alexet days
[00:04:24] and now it's common to train to train
[00:04:25] models not just on one GPU but on
[00:04:27] hundreds or thousands or tens of
[00:04:28] thousands or even more. So the amount of
[00:04:30] compute that we can marshall today on on
[00:04:32] a single model is is you know about a
[00:04:34] millionfold more than we could have even
[00:04:35] at the start of my PhD. So I think
[00:04:37] language was one of the really really
[00:04:40] interesting things that started to work
[00:04:41] quite well the last couple of years. But
[00:04:43] as we think about moving towards visual
[00:04:44] data and spatial data and world data,
[00:04:46] you just need to process a lot more. And
[00:04:48] I think that's going to be um a good way
[00:04:50] to soak up this uh this new compute
[00:04:52] that's coming online more and more.
[00:04:53] >> Does the model of having a public
[00:04:56] challenge still work or should it be
[00:04:58] centralized with inside of a lab?
[00:05:00] >> I think open science still uh is
[00:05:03] important. you know AI obviously
[00:05:05] compared to um the image that Alex that
[00:05:09] time has really evolved right [laughter]
[00:05:12] that was such a niche computer science
[00:05:15] discipline now it's just like
[00:05:17] civilizational
[00:05:18] um technology but I'll give you an
[00:05:21] example right uh recently my Stanford uh
[00:05:24] lab just announced a open uh data set
[00:05:28] and benchmark called uh behavior which
[00:05:30] is for benchmarking robotic learning in
[00:05:33] uh simulated environments and that is a
[00:05:37] very clear effort in still keeping up
[00:05:41] this open science model of doing things
[00:05:44] especially as in academia but I think
[00:05:47] it's important to recognize the
[00:05:49] ecosystem is uh is a mixture right I I
[00:05:52] think uh uh a lot of the the very
[00:05:55] focused work in industry some of them
[00:05:59] are more seeing the daylight in the form
[00:06:02] of a
[00:06:03] rather than an open challenge per se.
[00:06:05] >> Yeah. And and that's just a matter of
[00:06:07] the like funding in the business model
[00:06:09] like you have to see some ROI from it. I
[00:06:12] think it's just a matter of the
[00:06:16] diversity of the ecosystem right even
[00:06:18] during the so so-cal Alex image net time
[00:06:22] I mean there were closed models there
[00:06:24] were proprietary models there were open
[00:06:26] models you know um you know if or you
[00:06:29] think about iOS versus Android right
[00:06:32] there are different business model I I
[00:06:34] wouldn't say it's just a matter of
[00:06:36] funding per se it's just how the the
[00:06:38] market is there are different plays
[00:06:40] >> yeah but do Do you feel like you could
[00:06:42] redo imageet today with the commercial
[00:06:45] pressure that some of these labs has? I
[00:06:47] mean to me that's like the biggest
[00:06:48] question, right? It's like what can you
[00:06:50] open versus what do should you keep
[00:06:53] inside? Like you know if I put myself in
[00:06:55] your shoes, right? It's like you raise a
[00:06:57] lot of money, you're building all of
[00:06:58] this. If you had the best data set for
[00:07:00] this, what incentives do you really have
[00:07:02] to publish it? And it feels like the
[00:07:04] people at the labs are getting more and
[00:07:05] more pulled in the PhD programs are
[00:07:09] getting pulled earlier and earlier into
[00:07:10] these labs. So I'm curious if you think
[00:07:12] there's like an issue right now with
[00:07:14] like how much money has taken, how much
[00:07:16] pressure it puts on like the more
[00:07:17] academia open research space or if you
[00:07:20] feel like that's not really a a concern.
[00:07:22] >> I do have concerns about less about the
[00:07:26] pressure. It's more about the resourcing
[00:07:30] and the imbalanced resourcing of
[00:07:32] academia. This is a little bit of a
[00:07:34] different conversation from World Labs.
[00:07:36] You know, I have been the past few years
[00:07:39] advocating for uh uh resourcing the
[00:07:42] healthy ecosystem. you know, as the uh
[00:07:46] founding director, co-director of
[00:07:48] Stanford's uh Institute for Human Center
[00:07:51] AI, Stanford High, I've been, you know,
[00:07:53] working with policy uh makers about uh
[00:07:57] resourcing public sector and academic uh
[00:07:59] AI work, right? We work with the first
[00:08:02] Trump administration on uh this bill
[00:08:05] called national AI research uh resource
[00:08:08] NAR bill which is uh scoping out a
[00:08:13] national AI compute cloud as well as
[00:08:17] data repository and I also think that
[00:08:20] open-source open data sets continue to
[00:08:23] be important part of the ecosystem. Like
[00:08:26] I said, right now in my Stanford lab, we
[00:08:30] are doing the open data set, open
[00:08:32] benchmark on robotic learning called
[00:08:35] behavior and many of my colleagues are
[00:08:37] still doing that. I think that's part of
[00:08:40] the ecosystem. I think what the industry
[00:08:42] is doing, some startups are doing are
[00:08:45] running fast with models creating
[00:08:47] products is also a good thing. For
[00:08:50] example, when Justin was a PhD student
[00:08:54] with me, none of the computer vision
[00:08:56] programs work that well, right? We could
[00:08:59] write beautiful papers. Justin has
[00:09:01] >> I mean like actually even even before
[00:09:03] grad school like I wanted to do computer
[00:09:04] vision and I reached out to a team at
[00:09:06] Google and like wanted to I potentially
[00:09:08] go and try to do computer vision like
[00:09:09] out of out of undergrad and they told me
[00:09:11] like what what are you talking about
[00:09:12] like you can't do that like go do a PhD
[00:09:14] first and come back.
[00:09:14] >> What was the motivation that that got
[00:09:16] you? Oh, I had done some computer vision
[00:09:19] research in during my undergrad with uh
[00:09:21] with actually Fay's PhD adviser.
[00:09:23] >> There's [laughter] a lineage.
[00:09:24] >> There's a lineage here. So, I had I had
[00:09:26] done some computer vision even as an
[00:09:28] undergrad and I thought it was really
[00:09:29] cool and I wanted to keep doing it. Um
[00:09:30] so then I I was sort of faced with this
[00:09:32] sort of industry academia choice even
[00:09:34] coming out of undergrad that I think a
[00:09:35] lot of people in the research community
[00:09:36] are facing now. Um but but to your
[00:09:39] question I I think like the role of of
[00:09:41] academia especially in AI has shifted
[00:09:43] quite a lot in the last decade. Um and
[00:09:45] it's not a bad thing. Um it's it's a
[00:09:47] sense of it's it's because the
[00:09:48] technology has has grown and emerged,
[00:09:50] right? Like 5 or 10 years ago, you
[00:09:52] really could train state-of-the-art
[00:09:53] models in the lab um even with with just
[00:09:55] a couple GPUs, but you know, because
[00:09:58] that technology was so successful and
[00:09:59] scaled up so much, then you you can't
[00:10:01] train state-of-the-art models with a
[00:10:03] couple GPUs anymore. And that's not a
[00:10:04] bad thing. It's a good thing. It means
[00:10:06] the technology actually worked. Um but
[00:10:07] that means the the expectations around
[00:10:09] what we should be doing as academics
[00:10:11] shifts a little bit. And it shouldn't be
[00:10:12] about trying to train the biggest model
[00:10:14] and scaling up the biggest thing. It
[00:10:16] should be about trying wacky ideas and
[00:10:18] new ideas and crazy ideas. Um, most of
[00:10:20] which won't work. And I think there's a
[00:10:22] lot to be done there. If anything, I'm
[00:10:24] worried that too many people in academia
[00:10:26] are hyperfocused on this notion of
[00:10:28] trying to pretend like we can train the
[00:10:30] biggest models or or treating it as
[00:10:32] almost a vocational training program to
[00:10:34] then graduate and go to a big lab and
[00:10:35] then be able to play with all the GPUs.
[00:10:37] I think there's just so much crazy stuff
[00:10:39] you can do around like new algorithms,
[00:10:41] new architectures, like new systems that
[00:10:43] you know there's a lot you can do as as
[00:10:45] one person
[00:10:46] >> and also just um academia has a role to
[00:10:49] play in understanding the theoretical
[00:10:51] underpinning of these large models. We
[00:10:53] still know so little about this or
[00:10:56] extend to the interdisciplinary,
[00:10:59] you know, Justin calls wacky ideas.
[00:11:01] There's a lot of uh basic science ideas.
[00:11:03] There's a lot of blue sky problems. So I
[00:11:07] agree. I don't think the problem is open
[00:11:10] versus closed, productization versus uh
[00:11:13] open sourcing. I think the problem right
[00:11:15] now is that academia by itself is
[00:11:18] severely underresourced. So that uh you
[00:11:21] know the the researchers and the uh
[00:11:24] students do not have enough resources to
[00:11:27] try these uh these uh ideas.
[00:11:30] >> Yeah. Just for people to nerd snipe uh
[00:11:32] what's a wacky idea that comes to mind
[00:11:34] when you talk about wacky ideas? Oh,
[00:11:35] like I had I had this idea that I kept
[00:11:37] pitching to my students uh at at
[00:11:39] Michigan, which is that I really like
[00:11:41] hardware and I really like like new
[00:11:42] kinds of hardware coming online. Um, and
[00:11:44] in some sense the the emergence of the
[00:11:46] neural networks that you we use today
[00:11:47] and transformers are really based around
[00:11:49] matrix multiplication because matrix
[00:11:50] multiplication fits really well with
[00:11:52] GPUs. But if we think about how GPUs are
[00:11:55] going to scale, how how hardware is
[00:11:56] likely to scale in the future. I don't
[00:11:58] think the current system that we have
[00:12:00] like the GPU like hardware design is
[00:12:02] going to scale infinitely and that we
[00:12:04] start to see that even now that like the
[00:12:06] unit of compute is not not the single
[00:12:07] device anymore. It's this whole cluster
[00:12:09] of devices. So if you imagine
[00:12:10] >> node
[00:12:11] >> yeah it's a whole node or a whole
[00:12:12] cluster but the way we talk about neural
[00:12:14] networks is still as if they are a
[00:12:16] monolithic thing that could be coded
[00:12:18] like in one GPU in pietorch um but then
[00:12:20] in practice they could distribute over
[00:12:21] thousands of devices. So are there like
[00:12:23] dra just as you know transformers are
[00:12:25] based around matmal and mattal is sort
[00:12:27] of the primitive that works really well
[00:12:28] on on GPUs as you imagine hardware
[00:12:30] scaling out are there other primitives
[00:12:31] that make more sense for large scale
[00:12:33] distributed systems that we could build
[00:12:34] our neural networks on um and I think
[00:12:36] it's possible that there could be
[00:12:37] drastically different architectures that
[00:12:39] fit with the next generation or like the
[00:12:41] the the hardware that's going to come 10
[00:12:42] or 20 years down the line and we could
[00:12:44] start imagining that today it's really
[00:12:46] hard to make those kinds of bets because
[00:12:48] there's also the concept of the hardware
[00:12:49] lottery where let's just say you know
[00:12:52] Nvidia has on and we should just, you
[00:12:54] know, scale that out in infinitely and
[00:12:55] write software to patch up any any gaps
[00:12:58] we have in the in the mix, right? I
[00:13:00] mean, yes, yes and no. Like, if you look
[00:13:01] at if you look at the numbers, like even
[00:13:02] going from Hopper to Blackwell, like the
[00:13:05] performance per watt is about the same.
[00:13:06] Yes. Um, they mostly make the the number
[00:13:08] of transistors go up and they make the
[00:13:09] chip size go up and they make the the
[00:13:11] power usage go up. But even from Hopper
[00:13:13] to Blackwell, we're kind of already
[00:13:14] seeing like a a scaling limit in terms
[00:13:16] of what is the what is the performance
[00:13:17] per watt that we can get. So, um, I
[00:13:20] think I think there are there is room to
[00:13:21] to do something new and I don't know
[00:13:22] exactly what it is and I don't think you
[00:13:24] can get it done like in a three-month
[00:13:25] cycle as a startup, but I think that's
[00:13:27] the kind of idea that if you sit down
[00:13:28] and sit with for a couple years, like
[00:13:30] maybe you could come up come up with
[00:13:31] some breakthroughs and I think that's
[00:13:32] the kind of longrange stuff that is is a
[00:13:34] perfect match for academia. Coming back
[00:13:36] to the little bit of of background in
[00:13:38] history, we have this sort of research
[00:13:40] note on the scene storytelling work that
[00:13:42] you did or new newer image captioning uh
[00:13:44] that you did with Andre and I just
[00:13:47] wanted to hear you guys tell that story
[00:13:48] about you know you you were like sort of
[00:13:50] embarking on that for your PhD and and
[00:13:52] Fe you like having that reaction that
[00:13:54] you had.
[00:13:55] >> Yeah. So I think that line of work
[00:13:57] started between me and Andre and then
[00:14:00] Justin joined right. So um Andre started
[00:14:03] his PhD. He and I were looking at what
[00:14:07] is beyond imageet object recognition and
[00:14:10] at that time we you know the
[00:14:13] convolutional neuronet network was uh
[00:14:16] has proven some power in uh imageet
[00:14:19] tasks. So so convenet is a great way to
[00:14:22] represent images. In the meantime, I
[00:14:25] think in the language that the space a
[00:14:27] early sequential model is called LSTM
[00:14:30] was also being experimented. So Andre
[00:14:34] and I were just talking about this has
[00:14:38] been a longterm dream of mine. I thought
[00:14:40] it would take a 100 years to to solve
[00:14:42] which is telling the story of images.
[00:14:45] When I graduated from grad school, I
[00:14:47] really thought the rest of my entire
[00:14:49] career would be towards solving that
[00:14:52] single problem which is given a picture
[00:14:55] or given a scene, tell the story in
[00:14:58] natural language. But things evolve so
[00:15:00] fast. Uh when Andre and I uh when Andre
[00:15:03] started, we're like maybe combining the
[00:15:06] representation of convolutional neuronet
[00:15:07] network as well as the the the language
[00:15:10] sequential model of LSTM, we we might be
[00:15:14] able to learn uh through training to
[00:15:17] match uh um caption with images. So
[00:15:21] that's when we started that line of work
[00:15:24] and I I don't it was 2014 or 2015. It
[00:15:27] was a CVPR 2015 was the captioning
[00:15:30] paper. So it was uh our first paper that
[00:15:34] uh uh Andre got it to work that was you
[00:15:38] know given an image the image is
[00:15:40] represented with convet the language
[00:15:43] model is the LSTM model and then we
[00:15:46] combine it and it's able to generate one
[00:15:49] sentence and that was one of the first
[00:15:52] time it was pretty I I think I wrote it
[00:15:54] in my book uh we thought we were the
[00:15:57] first people doing it turned out that
[00:15:59] Google at that time was also
[00:16:00] simultaneously doing it and uh a
[00:16:03] reporter it was John Marov from uh uh
[00:16:06] New York Times was breaking the Google
[00:16:08] story but he by accident heard about us
[00:16:11] and then he realized that we really
[00:16:13] independently got there together at the
[00:16:16] same time. So he wrote the story of both
[00:16:18] the Google research as well as Andre and
[00:16:20] my research but after that I think
[00:16:23] Justin was already in the lab at that
[00:16:26] time.
[00:16:26] >> Yeah. Yeah. I remember the group read
[00:16:28] the the group meeting where Andre was
[00:16:29] presenting some of those results and
[00:16:30] explaining this new thing called LSTMs
[00:16:32] and RNN's that I had never heard of
[00:16:34] before and I thought like wow this is
[00:16:35] really amazing stuff I want to I want to
[00:16:36] work on that. So then he had the paper
[00:16:38] at 20 CVPR 2015 on the first image
[00:16:41] captioning results. Then after that we
[00:16:43] started working together and we did a we
[00:16:45] first we did a paper actually just on
[00:16:47] language modeling um back in uh 2015 I
[00:16:51] clear 2015. Yeah. Yeah. I I should have
[00:16:53] stuck with language modeling that turned
[00:16:54] out [laughter] to be pretty lucrative in
[00:16:56] retrospective. But we did this language
[00:16:57] modeling paper together um me and Andre
[00:16:59] uh in uh 2015 where it was like really
[00:17:02] cool. We trained these little r these
[00:17:03] little RNN language models that could
[00:17:04] you know spit out a couple sentences at
[00:17:06] a time and poke at them and try to
[00:17:08] understand what the neurons inside the
[00:17:09] neural network inside the things were
[00:17:11] doing.
[00:17:11] >> You guys were doing analysis on the
[00:17:13] different like memory and
[00:17:15] >> Yeah. Yeah. It was it was really it was
[00:17:16] really cool. And even at that time we
[00:17:17] had these results where you could like
[00:17:19] look inside the LSTM and say like oh
[00:17:21] this thing is reading code. So one of
[00:17:22] the like one of the data sets that we
[00:17:24] that we trained on for this one was the
[00:17:25] the um the Linux source code right
[00:17:28] because the whole the whole the whole
[00:17:29] thing is you know open source and you
[00:17:30] could just download this. So we train an
[00:17:32] RNN on this on this data set and then as
[00:17:34] the network is trying to predict the
[00:17:36] tokens there then you know try to
[00:17:38] correlate the kinds of predictions that
[00:17:40] it's making with the kind of internal
[00:17:41] structures uh in the RNN and there we
[00:17:44] were able to find some correlations
[00:17:45] between oh like this unit in this layer
[00:17:47] of the LSTM fires when there's an open
[00:17:49] PN and then like turns off when there's
[00:17:50] a closed PN um and try to do some
[00:17:52] empirical stuff like that to to figure
[00:17:54] it out. So that was pretty cool and that
[00:17:56] was just like d that was sort of like
[00:17:57] cutting out the CNN from this language
[00:17:59] modeling part and just looking at the
[00:18:00] language models in isolation.
[00:18:02] >> But then we wanted to extend the the
[00:18:04] image captioning work. Yeah. I remember
[00:18:07] at that time we even have a sense of
[00:18:09] space because we feel like captioning
[00:18:11] does not capture different parts of the
[00:18:13] image. Right. So I was talking to Justin
[00:18:16] and Andrea about can you go what we what
[00:18:20] we end up calling dense captioning which
[00:18:22] is you know uh describe the scene in
[00:18:25] greater details especially different
[00:18:27] parts of the scene. So that's
[00:18:28] >> yeah and so then then we built this
[00:18:30] system then it was um me and Andre and
[00:18:32] and Fe on a paper the following year
[00:18:34] CVPR 2016 where we built this system
[00:18:36] that did dense captioning. So you input
[00:18:38] a single image and then it would draw
[00:18:39] boxes around all the interesting stuff
[00:18:41] in the image and then write a short
[00:18:42] snippet about each of them. It's like,
[00:18:43] oh, it's a green B water bottle on the
[00:18:45] table. It's a person wearing a black
[00:18:46] shirt. And this was a really complicated
[00:18:48] neural network because um that was built
[00:18:50] on a lot of um advancements that had
[00:18:52] been made in object detection around
[00:18:53] that time, which was a major topic in
[00:18:55] computer vision for for a long time. And
[00:18:57] then it was actually like one joint
[00:18:58] neural network that was both uh you know
[00:19:00] learning to look at individual images
[00:19:02] because they actually had like then
[00:19:03] three different representations inside
[00:19:05] this network. One was the representation
[00:19:07] of the whole image to kind of get the
[00:19:08] gestalt of what's going on. Then it
[00:19:10] would propose individual regions that it
[00:19:11] wants to focus on and then look at you
[00:19:13] know represent each region independently
[00:19:15] and then once you look at the region
[00:19:16] then you need to spit out tax for each
[00:19:17] region. So that was a pretty complicated
[00:19:19] neural network architecture. Um this was
[00:19:21] all pre pytorch
[00:19:22] >> right
[00:19:22] >> and does it do it in one pass?
[00:19:23] >> Yeah. Yeah. So it was a single forward
[00:19:24] pass that did all of that.
[00:19:25] >> Not only it was doing it in one pass.
[00:19:27] You also optimize inference. You're
[00:19:30] doing it on a webcam. I remember. Yeah.
[00:19:32] >> Yeah. So, I had built this like crazy
[00:19:34] real-time demo um where I had the
[00:19:37] network running like on a server at
[00:19:39] Stanford and then a web front end that
[00:19:41] would stream from a webcam and then like
[00:19:42] send the image back to the server. The
[00:19:44] server would run the model and stream
[00:19:45] the predictions back. So, I was just
[00:19:47] like walking around the lab with this
[00:19:48] laptop that would just like show people
[00:19:50] this uh this like this network in real
[00:19:53] time.
[00:19:53] >> Identification and labeling as well.
[00:19:55] Yeah, it was it was uh it was pretty
[00:19:58] impressive cuz most of our graduate
[00:20:00] students would be satisfied if they can
[00:20:02] publish the paper, right? They they
[00:20:04] package the the the research, put it in
[00:20:06] a paper, but Justin went a step further.
[00:20:09] He's like, I want to do this real time
[00:20:11] web demo.
[00:20:12] >> Well, actually, I don't I don't know if
[00:20:13] I told you this story, but then um we
[00:20:15] had a there was a conference that year
[00:20:16] in Santiago uh at ICCV. It was ICCV 15.
[00:20:20] Um and then like I had a paper at that
[00:20:22] conference for something different, but
[00:20:23] I had my my laptop. I was like walking
[00:20:25] around the conference with my laptop
[00:20:26] showing everybody this like real-time
[00:20:28] captioning demo and the model was
[00:20:29] running on a server in California. So,
[00:20:31] it was like actually able to stream like
[00:20:32] all the way from California down to
[00:20:34] Santiago. Well, latency is it [laughter]
[00:20:36] was terrible. It was like
[00:20:38] it was like 1 FPS, but the fact that it
[00:20:40] worked at all was pretty was pretty
[00:20:41] amazing.
[00:20:42] >> I was going to briefly quip that, you
[00:20:44] know, maybe vision and language modeling
[00:20:45] are not that different. you know, DeSQL
[00:20:47] CR recently uh tried the crazy thing of
[00:20:50] let's language let's model text from
[00:20:52] pixels and and just like train on that
[00:20:55] and it might be the future. I don't
[00:20:57] know. I don't know if you guys have any
[00:20:58] takes on whether language is actually
[00:21:00] necessary at all.
[00:21:02] >> I just wrote a whole manifesto on space
[00:21:04] intelligence. [laughter]
[00:21:05] >> This is my segue into this. Yes,
[00:21:08] >> I think they are different. Um I do
[00:21:11] think the architecture uh of uh these
[00:21:14] generative models will share a lot of uh
[00:21:17] sharable components but uh I think the
[00:21:20] deeply 3D 4D spatial world has a level
[00:21:27] of structure that is fundamentally
[00:21:29] different from a purely generative uh
[00:21:32] signal that is one-dimensional.
[00:21:34] >> Yeah, I think there's something to be
[00:21:36] said for pixel maximalism, right? Like
[00:21:38] there's this notion that language is
[00:21:40] this different thing, but you we see
[00:21:42] language with our eyes and our eyes are
[00:21:44] just like, you know, basically pixels,
[00:21:46] right? Like we've got sort of biological
[00:21:47] pixels in the back of our eyes that are
[00:21:49] processing these things. And you know,
[00:21:50] we see text and we think of it as this
[00:21:52] discrete thing, but that really only
[00:21:53] exists in our minds. Like the physical
[00:21:55] manifestation of text and language in
[00:21:57] our world are, you know, physical
[00:21:59] objects that are printed on things in
[00:22:01] the world and we see it with our eyes.
[00:22:02] Well, you can also think it's sound, but
[00:22:04] even sound even sound you can translate
[00:22:06] into sound. Yeah, you can corog
[00:22:10] signal,
[00:22:11] >> right? And then like you actually lose
[00:22:12] something if you translate to this like
[00:22:13] purely tokenized representations that we
[00:22:15] use in LLMs, right? Like you lose the
[00:22:17] font, you lose you lose the line breaks,
[00:22:19] you lose sort of the 2D arrangement on
[00:22:21] the page. Um, and and for a lot of
[00:22:23] cases, for a lot of things, maybe that
[00:22:24] doesn't matter. Um, but for some things
[00:22:25] it does. Um, and I I think pixels are
[00:22:28] this sort of, you know, more more
[00:22:29] lossless representation of what's going
[00:22:31] on in the world and in in some ways a
[00:22:33] more general general representation that
[00:22:35] more matches what what we what we humans
[00:22:37] see as we as we navigate the world. So,
[00:22:39] so like there's an efficiency argument
[00:22:41] to be made like maybe it's not super
[00:22:42] efficient to like you know render your
[00:22:44] text to an image and then feed that to a
[00:22:45] vision model.
[00:22:46] >> That's exactly what Deep Seek did,
[00:22:47] right? It was like kind of worked.
[00:22:49] [laughter]
[00:22:51] I think this ties into the whole world
[00:22:53] model like one of the my favorite papers
[00:22:55] that I saw this year was about inductive
[00:22:57] bias to pro for world model. So it was a
[00:22:59] Harvard paper where they fed a lot of
[00:23:01] like orbital uh patterns into an LLM and
[00:23:04] then they asked the LLM to predict the
[00:23:06] orbit of a planet around the sun and the
[00:23:09] model generated looked good but then if
[00:23:11] you asked it to draw the force vectors
[00:23:14] >> it would be all wacky you know it
[00:23:16] wouldn't actually follow it. So how do
[00:23:18] you think about what's embedded into the
[00:23:21] data that you get? And we can talk about
[00:23:22] maybe tokenizing for 3D world models
[00:23:25] like what are like the dimensions of
[00:23:27] information. There's the visual but like
[00:23:30] how much of like the underlying hidden
[00:23:33] forces so to speak you need to extract
[00:23:35] out of this data and like what are some
[00:23:36] of the challenges there? Yeah, I think
[00:23:38] there's different ways you could
[00:23:39] approach that problem. Um, one is like
[00:23:41] you could try to be explicit about it
[00:23:43] and say like, "Oh, I want to, you know,
[00:23:45] measure all the forces and feed those as
[00:23:46] training data to your model, right? Then
[00:23:48] you could like sort of run a traditional
[00:23:50] physics simulation and, you know, then
[00:23:52] know all the forces in the scene and
[00:23:54] then use those as as training data to
[00:23:55] train a model that's now going to
[00:23:56] hopefully predict those. Or you could
[00:23:58] hope that something emerges more
[00:23:59] latently, right? that you kind of train
[00:24:01] on something end to end and then on on a
[00:24:03] more general problem and then hope that
[00:24:05] somewhere some something in the
[00:24:07] internals of the model must learn to
[00:24:09] model something like physics in order to
[00:24:11] make the proper predictions. And those
[00:24:12] are kind of the two big paradigms that
[00:24:14] we have more generally.
[00:24:15] >> But there's no indication that those
[00:24:18] latent uh modeling will get you to a
[00:24:21] causal law of uh of space and dynamics.
[00:24:25] Right? That's where today's deep
[00:24:27] learning and uh human intelligence
[00:24:30] actually start to bifrocate because
[00:24:32] fundamentally the deep learning is still
[00:24:34] fitting patterns.
[00:24:35] >> There you sort of get philosophical and
[00:24:37] you say that like we're trying to fit
[00:24:38] patterns too but maybe we're trying to
[00:24:39] fit you know a more broad array of
[00:24:41] patterns like over a with with a longer
[00:24:43] time horizon a different reward
[00:24:44] function. Um but but like basically the
[00:24:47] paper you mentioned is sort of you know
[00:24:48] that problem that it learns to fit the
[00:24:50] specific patterns of orbits but then it
[00:24:52] doesn't actually generalize in the way
[00:24:53] that you'd like. doesn't have a sort of
[00:24:54] causal model of gravity,
[00:24:55] >> right? Because even in marble, you know,
[00:24:57] I was trying it and it generates this
[00:24:58] beautiful sceneries and there's like
[00:25:00] arches in them.
[00:25:02] >> But does the model actually understand
[00:25:04] how you know the arch is actually, you
[00:25:06] know, drawing on the center kind of like
[00:25:09] stone and like you know the actual
[00:25:11] physical structure of it. And the other
[00:25:13] question is like does it matter that it
[00:25:15] does understand it as long as it always
[00:25:17] renders something that would fit the
[00:25:19] physical model that we imagine? If you
[00:25:22] use the word understand the way you
[00:25:25] understand, I'm pretty sure the model
[00:25:27] doesn't understand [laughter] it. The
[00:25:29] model is learning from the data,
[00:25:31] learning from the pattern. Um, yeah.
[00:25:34] Does it matter? Especially for the use
[00:25:36] cases for it. It's a good question,
[00:25:39] right? Like for now, I don't think it
[00:25:41] matters because it renders out what you
[00:25:44] need assuming it's perfect.
[00:25:46] >> Yeah. I mean, it depends on the use
[00:25:47] case. It's like if the use case is I
[00:25:49] want to generate sort of a backdrop for
[00:25:51] for virtual film or production or
[00:25:53] something like that all you need is
[00:25:54] something that looks plausible and in
[00:25:56] that case probably it doesn't matter.
[00:25:57] But if you're going to use this to like
[00:25:59] you know if you're an architect and
[00:26:00] you're going to use this to design a
[00:26:01] building that you're then going to go
[00:26:02] build in the real world then yeah it
[00:26:04] does matter that you model the forces
[00:26:05] correctly because you don't want the
[00:26:06] thing to break once you actually
[00:26:07] actually build it. But even there right
[00:26:09] like even if your model has the
[00:26:11] semantics in it let's say I still don't
[00:26:14] think the understanding of the signal or
[00:26:19] the or the the output on the model part
[00:26:23] and the understanding on the human part
[00:26:25] is a different word but this gets again
[00:26:28] philosophical
[00:26:29] >> yeah I mean there there's this trick
[00:26:30] with understanding right like these
[00:26:31] models are a very different kind of
[00:26:33] intelligence than human intelligence um
[00:26:34] and human intelligence is interesting
[00:26:36] because you You know, I think that I
[00:26:39] understand things because I can
[00:26:40] introspect my own thought process to
[00:26:41] some extent. And then I believe that my
[00:26:44] thought process probably works similar
[00:26:45] to other people's so that when I observe
[00:26:48] someone else's behavior, then I infer
[00:26:50] that their internal mental state is
[00:26:51] probably similar to my own internal
[00:26:53] mental state that I've observed. And
[00:26:54] therefore, I know that I understand
[00:26:56] things. So there I assume that you
[00:26:57] understand something. But these models
[00:26:59] are sort of like this this alien form of
[00:27:01] intelligence where they can do really
[00:27:03] interesting things. They can exhibit
[00:27:04] really interesting behavior. But
[00:27:06] whatever kind of internal the equivalent
[00:27:08] of internal cognition or internal
[00:27:09] self-reflection that they have if it
[00:27:11] exists at all is totally different from
[00:27:12] what we do. So
[00:27:14] >> it doesn't have the self-awareness.
[00:27:15] >> Right? But what that means is that when
[00:27:17] when we observe seemingly interesting or
[00:27:19] intelligent behavior out of these
[00:27:21] systems, we can't necessarily infer
[00:27:23] other things about them because their
[00:27:25] their model of the world and the way
[00:27:26] they think is so different from us.
[00:27:28] >> So would you need two different models
[00:27:29] to do the visual one and the
[00:27:31] architectural generation? you think
[00:27:33] eventually like there's not anything
[00:27:35] fundamental about the approach that
[00:27:36] you've taken on the model building. It's
[00:27:39] more about scaling the model and the
[00:27:41] capabilities of it or like is there
[00:27:43] something about being very visual that
[00:27:46] prohibits you from actually learning the
[00:27:49] physics behind it so to speak so that
[00:27:51] you could trust it to generate a cat
[00:27:53] design that then is actually going to
[00:27:56] work in the real world. I think this is
[00:27:58] a matter of scaling data and and and
[00:28:01] bettering model. I don't think there's
[00:28:03] anything fundamental that separates
[00:28:05] these two.
[00:28:06] >> Yeah, I would like it to be one model,
[00:28:07] but I think like the big problem in deep
[00:28:09] learning in some sense is how do you get
[00:28:11] emergent capabilities beyond your
[00:28:13] training data? Are you going to get
[00:28:14] something that understands the forces
[00:28:16] while it wasn't trained to predict the
[00:28:18] forces, but it's going to learn them
[00:28:19] implicitly internally? Um, and I think a
[00:28:21] lot of what we've seen in other large
[00:28:22] models is that a lot of this emergent
[00:28:24] behavior does happen at scale. Um, and
[00:28:26] will that transfer to other modalities
[00:28:27] and other use cases and other tasks? Um,
[00:28:29] I hope so, but that'll that'll be a
[00:28:31] process that we need to play out over
[00:28:32] time and see.
[00:28:33] >> Is there a temptation to rely on um
[00:28:35] physics engines um that already exist
[00:28:38] out there that are, you know, basically
[00:28:40] the gaming industry has saved you a lot
[00:28:42] of this work or do we have to reinvent
[00:28:44] things for some fundamental mismatch? I
[00:28:46] think that's sort of like climbing the
[00:28:48] ladder of technology, right? Like in
[00:28:50] some sense, the reason that you want to
[00:28:51] build these things at all is because
[00:28:53] maybe traditional physics engines don't
[00:28:54] work in some situations. If a physics
[00:28:56] engine was perfect, we would have sort
[00:28:58] of no need to build models because the
[00:28:59] problem would have already been solved.
[00:29:01] So in some sense, the reason why we want
[00:29:02] to do these is because classical physics
[00:29:04] engines don't solve problems in the
[00:29:06] generality that we want. Um but that
[00:29:08] doesn't mean we need to throw them away
[00:29:09] and start everything from scratch,
[00:29:10] right? We can use traditional physics
[00:29:12] engines to generate data that we then
[00:29:14] train our models on. And then you're
[00:29:15] sort of distilling the physics engine
[00:29:17] into the weights of the neural network
[00:29:18] that you're training. I think that's a
[00:29:20] lot of what if you compare the work of
[00:29:22] other labs, people are speculating that,
[00:29:25] you know, Sora had a little bit of that.
[00:29:27] Genie3 had a bit of that. Um, and Genie
[00:29:31] is like explicitly like a video game.
[00:29:33] Like you have controls to to walk around
[00:29:34] in. And I I I always think like it's
[00:29:37] really funny how the things that we
[00:29:38] invent for fun actually does eventually
[00:29:40] make it into serious work.
[00:29:43] >> Yeah. The whole AI revolution started by
[00:29:46] graphics chips. Yeah. Partially
[00:29:48] [laughter]
[00:29:50] >> misusing the GPU for uh for generating a
[00:29:53] lot of triangles into generating a lot
[00:29:54] of everything else basically.
[00:29:56] >> Yeah.
[00:29:56] >> We touched on marble a little bit. I
[00:29:58] think you guys chose marble as like kind
[00:29:59] of your like your sort of a little bit
[00:30:01] coming out of stealth moment if you can
[00:30:02] call it that.
[00:30:03] >> Yeah. Uh maybe we can get a concise
[00:30:05] explanation from you on what people
[00:30:07] should take away because everyone here
[00:30:09] can try marble but I don't think they
[00:30:11] might be able to link it to the
[00:30:13] differences between what your vision is
[00:30:15] versus other I guess generative worlds
[00:30:18] they may have seen from other labs.
[00:30:20] >> So Marbo is a glimpse into our model
[00:30:22] right we are a model spatial
[00:30:24] intelligence model company. We believe
[00:30:26] spatial intelligence is the next
[00:30:28] frontier. And in order to make spatial
[00:30:30] spatially intelligent models, the model
[00:30:32] has to be very powerful in terms of its
[00:30:35] ability to you know understand, reason,
[00:30:38] generate in very multimodal uh fashion
[00:30:42] of worlds as well as allow the level of
[00:30:45] interactivity that we eventually hope to
[00:30:47] be as you know complex as how humans can
[00:30:51] interact with the world. So that's the
[00:30:53] grand vision of spatial intelligence as
[00:30:55] well as the the kind of world models we
[00:30:58] we uh see. Marble is the first glimpse
[00:31:02] into that. It's the it's the the first
[00:31:04] part of that journey. It's the first
[00:31:06] in-class model in the world that
[00:31:09] generates uh 3D worlds in this level of
[00:31:12] fidelity that is in the hands of the the
[00:31:14] public. It's the starting point, right?
[00:31:17] Uh we actually wrote this tech blog.
[00:31:19] Justin spent a lot of time writing that
[00:31:22] tech blog. I don't know if you had time
[00:31:24] to browse it. I mean Justin really broke
[00:31:26] it down into what are the inputs uh we
[00:31:29] can multimodal inputs of uh marble what
[00:31:32] are the kind of uh editability which is
[00:31:36] you know allows user to be interactive
[00:31:38] with the model and what are the kind of
[00:31:40] outputs we can have.
[00:31:42] >> Yeah. Uh so so marble like basically one
[00:31:44] way of looking at it it's the system
[00:31:45] it's a generative model of 3D worlds
[00:31:47] right so you can input things like text
[00:31:49] or image or multiple images and it will
[00:31:51] generate for you a 3D world that kind of
[00:31:53] matches those inputs and it's also
[00:31:55] interactive in the sense that um you can
[00:31:57] interactively edit scenes like I could
[00:32:00] generate this scene and then say I don't
[00:32:01] like the water bottle make it blue
[00:32:02] instead like take out the table like
[00:32:04] change these microphones around and then
[00:32:06] you can generate new worlds based on
[00:32:07] these interactive edits and export in a
[00:32:09] variety of formats and with marble we
[00:32:11] were actually trying to do sort of two
[00:32:13] things simultaneously and I think we we
[00:32:14] managed to pull off the balance pretty
[00:32:16] well. Um one is actually build a model
[00:32:18] that goes towards the grand vision of
[00:32:20] spatial intelligence and models need to
[00:32:22] be able to understand lots of different
[00:32:23] kinds of inputs need to be able to model
[00:32:25] worlds in a lot of situations need to be
[00:32:27] able to model counterfactuals of how
[00:32:28] they could change over time. So we
[00:32:30] wanted to start to build models that
[00:32:32] have these capabilities and marble
[00:32:33] marble today does already have hints of
[00:32:35] all of these. But at the same time we
[00:32:37] we're we're a company. We're a business.
[00:32:38] We were really trying not to have this
[00:32:40] be a science project but also build a
[00:32:42] product that would be useful to people
[00:32:44] in the real world today. So while Marble
[00:32:47] is simultaneously a world model that is
[00:32:49] building towards this vision of spatial
[00:32:51] intelligence, it was also very
[00:32:52] intentionally designed to be a thing
[00:32:54] that people could find useful today. Um
[00:32:57] and we're see starting to see emerging
[00:32:59] use cases. um for in gaming, in VFX, um
[00:33:01] in in film where I think there's a lot
[00:33:03] of really interesting stuff that Marvel
[00:33:05] can do today as a product and then also
[00:33:07] set a foundation for the grand world
[00:33:09] models that we want to build going into
[00:33:11] the future.
[00:33:11] >> Yeah. I noticed one tool that was very
[00:33:13] interesting because you can record your
[00:33:14] scene inside.
[00:33:15] >> Yes.
[00:33:16] >> Yes. It's very important the ability to
[00:33:19] record means a very precise control of
[00:33:23] camera placement. In order to have
[00:33:26] precise camera placement, it means you
[00:33:28] have to have a sense of 3D space.
[00:33:31] Otherwise, you don't know how to orient
[00:33:32] your camera, right? And how to move your
[00:33:34] camera. So, that is a natural
[00:33:37] consequence of this kind of model and
[00:33:39] and this is why this is just one of the
[00:33:42] examples.
[00:33:43] >> Yeah. I I find when I play with video
[00:33:45] generative models, I'm having to learn
[00:33:47] the the language of being a director
[00:33:50] because I have to move them like pan uh
[00:33:52] you know like
[00:33:54] you cannot say pan 63 degrees to the
[00:33:57] north, right? You just don't have that
[00:33:59] control. Whereas in marble you have
[00:34:02] precise control in terms of placing your
[00:34:05] camera. Yeah, I think that's one of the
[00:34:07] first things people need to understand
[00:34:09] is like it's not you're not generating
[00:34:11] frame by frame which is like what a lot
[00:34:12] of the other models are.
[00:34:14] >> Yeah.
[00:34:14] >> What are you know people understand that
[00:34:16] LLM generates one token. What are like
[00:34:19] the atomic units? There's kind of like
[00:34:20] you know the meshes, there's like the
[00:34:22] splats, the voxels, there's a lot of
[00:34:23] pieces in a 3D world. What should be the
[00:34:26] mental model that people have of like
[00:34:28] your generations?
[00:34:29] >> Yeah, I I think there's like what exists
[00:34:31] today and what could exist in the
[00:34:32] future. Um, so what exists today is the
[00:34:34] model natively outputs splats. Um, so
[00:34:36] gausian splats are these like, you know,
[00:34:38] each one is a tiny tiny particle that's
[00:34:39] semi-transparent, has a position
[00:34:41] orientation in in 3D space. Um, and the
[00:34:43] scene is built up from a large number of
[00:34:45] these gausian splats. Um, and gausian
[00:34:47] splats are really cool because you can
[00:34:48] render them in real time really
[00:34:49] efficiently. So you can render on your
[00:34:51] iPhone, render render everything. Um,
[00:34:52] and that's that's how we get that sort
[00:34:54] of precise camera control because the
[00:34:56] splats can be rendered real time on just
[00:34:57] on pretty much any client side device
[00:34:59] that we want. So for a lot of the scenes
[00:35:01] that we're generating today, uh that
[00:35:03] kind of atomic unit is that individual
[00:35:04] splat, but I don't think that's
[00:35:06] fundamental. I I could imagine other
[00:35:07] approaches in the future that would be
[00:35:09] interesting. So there like there are
[00:35:11] other approaches that even we've worked
[00:35:13] on at World Labs um like our recent RTFM
[00:35:15] model that does generate frames one at a
[00:35:17] time. Um and there the atomic unit is
[00:35:19] generating frames one at a time as the
[00:35:21] user interacts with the system. Um or
[00:35:23] you could imagine other architectures in
[00:35:25] the future where the atomic unit is a
[00:35:26] token where that token now represents
[00:35:28] you know some chunk of the 3D world and
[00:35:30] I think there's a lot of different
[00:35:31] architectures that we can experiment
[00:35:32] with here over time. I do want to press
[00:35:34] on double click on this a little bit. My
[00:35:37] version of what Allesia was going to say
[00:35:38] was like what is the fundamental data
[00:35:39] structure of a world model because
[00:35:41] exactly like you said like it's it's
[00:35:43] either Gaussian splat or it's like the
[00:35:44] frame or what have you. uh you also in
[00:35:46] in the the sort of previous statements
[00:35:48] focus a lot on the physics and the
[00:35:50] forces which is something over time
[00:35:53] which is loosely I don't see that in
[00:35:55] marble I presume it's not there yet
[00:35:58] maybe if there was like a marble 2 you
[00:35:59] would have movement or is there a
[00:36:02] modification to go splats that makes
[00:36:04] sense or would it be something
[00:36:06] completely different yeah I think
[00:36:07] there's a couple modifications that make
[00:36:09] sense and there's actually a lot of
[00:36:10] interesting ways to integrate things
[00:36:11] here which is another nice place of
[00:36:13] working in this space then there's
[00:36:15] actually been a lot of research work on
[00:36:16] this. Like when you talk about wacky
[00:36:17] ideas, like there's actually been a lot
[00:36:18] of really interesting academic work on
[00:36:20] different ways to imbue physics.
[00:36:21] >> You can also do wacky ideas in industry.
[00:36:24] >> Yeah. [laughter]
[00:36:25] >> Right. But but it's then it's like
[00:36:26] gausian splats are themselves little
[00:36:28] particles. There's been a lot of um
[00:36:29] approaches where you basically attach
[00:36:31] physical properties to those splats and
[00:36:33] say that each one has a mass or like
[00:36:34] maybe you treat each one as being
[00:36:35] coupled with some kind of um virtual
[00:36:37] spring to nearby neighbors and now you
[00:36:39] can start to do sort of physics
[00:36:40] simulation on top of splats. So one kind
[00:36:42] of avenue for adding uh adding physics
[00:36:45] or dynamics or interaction to these
[00:36:46] things would be to you know predict
[00:36:48] physical properties associated with each
[00:36:50] of your splat particles um and then
[00:36:52] simulate those downstream either using
[00:36:54] classical physics or something learned
[00:36:56] or you know the kind of the beauty of
[00:36:58] working in 3D is things compose and you
[00:37:00] can inject logic in different places. So
[00:37:02] one way is sort of like we're generating
[00:37:04] a 3D scene. We're going to predict 3D
[00:37:05] properties of everything in the scene.
[00:37:07] Then we use a classical physics engine
[00:37:08] to to simulate the interaction. Or you
[00:37:11] could do something where like as a
[00:37:12] result of a user action, the model is
[00:37:14] now going to regenerate the entire scene
[00:37:16] um in in splats or some other
[00:37:18] representation. Um and that could
[00:37:20] potentially be a lot more general
[00:37:21] because then you're not bound to
[00:37:22] whatever sort of um you know physical
[00:37:24] properties you know how to model
[00:37:25] already. But that's also a lot more
[00:37:27] computationally demanding because then
[00:37:28] you need to regenerate the whole scene
[00:37:30] in response to to user actions. But I
[00:37:32] think this is a this was a really
[00:37:33] interesting area for for future work and
[00:37:35] for uh adding on to to into potential
[00:37:39] marble too as you say.
[00:37:40] >> Yeah. And there's opportunity for
[00:37:42] dynamics, right?
[00:37:43] >> What's the state of like splats density
[00:37:46] I guess? Like do we can we render enough
[00:37:49] to have very high resolution when we
[00:37:51] zoom in? Are we limited by like the
[00:37:52] amount that you can generate? the amount
[00:37:54] that we can render like how are these
[00:37:56] gonna get super high fidelity so to
[00:37:58] speak?
[00:37:59] >> You have some limitations but depending
[00:38:00] on your target use case. So like one of
[00:38:03] the one of the big constraints that we
[00:38:04] have on our scenes is we wanted things
[00:38:06] to render cleanly on mobile. Um and we
[00:38:08] wanted things to render cleanly in VR
[00:38:10] headsets. So those are those devices
[00:38:11] have a lot less compute than you're used
[00:38:13] than you have in a lot of other
[00:38:14] situations. Um, and like if you want to
[00:38:16] get a splat file to render at high
[00:38:18] resolution, high like 30 to 60 fps on
[00:38:21] like an iPhone from 4 years ago, then
[00:38:23] you are a bit limited in like the number
[00:38:25] of splats that you can handle. Um, but
[00:38:27] if you're allowed to like work on a
[00:38:28] recent like even this year's iPhone or
[00:38:31] like a recent MacBook or even if you
[00:38:32] have a local GPU or if you don't need if
[00:38:35] you don't need that 60 fps 1080p like
[00:38:38] then you can relax the constraints and
[00:38:39] and get away with more splats and that
[00:38:41] lets you get higher resolution in your
[00:38:42] scenes. One uh use case I was expecting
[00:38:45] but didn't hear from you was embodied
[00:38:47] use cases. Are you you're just focusing
[00:38:50] on virtual for now?
[00:38:51] >> If you go to World Labs home homepage,
[00:38:54] there is a particular page called Marble
[00:38:56] Labs.
[00:38:57] >> There we showcase different use cases
[00:39:00] and we actually organize them in more
[00:39:03] visual effect use cases or gaming use
[00:39:06] cases as well as simulation use cases.
[00:39:09] And in that we actually show this is a
[00:39:12] technology that can help a lot in
[00:39:14] robotic training. Right? This uh goes
[00:39:16] back to what I was talking about earlier
[00:39:18] in uh speaking of data starvation. Uh
[00:39:22] robotic training really lack data. You
[00:39:24] know highfidelity real world data is
[00:39:26] absolutely very critical. But uh it's
[00:39:29] you're just not going to get a ton of
[00:39:31] that. Of course the other extreme is
[00:39:34] just purely internet video data. then
[00:39:36] you lack a lot of the the
[00:39:38] controllability that you want to train
[00:39:40] your your embodied agents with. So
[00:39:43] simulation and synthetic data is
[00:39:45] actually a very important middle ground
[00:39:47] for that. I've been working in this
[00:39:50] space for many years and one of the
[00:39:52] biggest pain point is where do you get
[00:39:54] this synthetic simulated data? you have
[00:39:57] to curate assets and and and and build
[00:40:00] these uh compose these complex
[00:40:02] situations and in robotics you want a
[00:40:05] lot of different states. You want the
[00:40:07] embodied uh agent to to uh interact in
[00:40:10] the synthetic environment. Marble
[00:40:13] actually is a really potential for uh
[00:40:16] helping to generate these synthetic uh
[00:40:18] simulated worlds for embodied uh agent
[00:40:21] training.
[00:40:22] >> Obviously that's yeah that's on the it's
[00:40:24] on the homepage. It'll be there. I just
[00:40:26] I was like trying to make the link to as
[00:40:28] you said like you also have to build
[00:40:30] like a business model the market for
[00:40:32] robotics obviously is very huge maybe
[00:40:34] you don't need that or maybe we need to
[00:40:36] build up and solve the virtual worlds
[00:40:38] first before we go to embody it and
[00:40:40] obviously stepping stone
[00:40:42] >> that is to be decided I I do think that
[00:40:45] uh
[00:40:46] >> because everyone else is going straight
[00:40:47] there [laughter] right
[00:40:49] >> not everyone else but there is a there
[00:40:52] is an excitement I would say but you
[00:40:55] know I think the world is big enough to
[00:40:57] to have different uh approaches.
[00:41:00] >> Yeah. Approaches.
[00:41:00] >> Yeah.
[00:41:01] >> Yeah. I mean, and we always view this as
[00:41:02] a pretty horizontal technology that
[00:41:03] should be able to touch a lot of
[00:41:04] different industries over time. And, you
[00:41:06] know, Marble is a little bit more
[00:41:07] focused on creative industries for now,
[00:41:09] but I think that the technology that
[00:41:11] powers it should be applicable to a lot
[00:41:12] of different things over time. And
[00:41:14] robotics is one that, you know, is maybe
[00:41:16] going to happen sooner than later.
[00:41:17] >> Also, design, right, is very adjacent to
[00:41:20] creative.
[00:41:21] >> Oh, yeah. Definitely. Like, I I I think
[00:41:22] it's like the architecture stuff.
[00:41:24] >> Yes. Okay. Yeah. I mean, I I I was
[00:41:25] joking online. I posted this uh this
[00:41:27] video on Slack of like, oh, who wants to
[00:41:29] use marble to to plan your next kitchen
[00:41:30] remodel? It actually works great for
[00:41:32] this already. Just like take two images
[00:41:34] of your kitchen, like reconstruct it in
[00:41:35] marble, and then use the editing
[00:41:36] features to see what would that space
[00:41:38] look like if you change the countertops
[00:41:39] or change the floors or change the
[00:41:41] cabinets. And this is something that's,
[00:41:42] you know, we didn't necessarily build
[00:41:44] anything specific for this use case, but
[00:41:46] because it's a it's a powerful
[00:41:48] horizontal technology, you kind of get
[00:41:49] these emergent use cases that that just
[00:41:51] fall out of the model. We have early
[00:41:52] beta users using a um um API key that uh
[00:41:57] is already building for interior design
[00:42:00] uh use case.
[00:42:02] >> I just did my garage. I should have
[00:42:04] known about [laughter] this. I got to
[00:42:06] >> next time you remodel, we can be of
[00:42:09] help.
[00:42:09] >> Well, kitchen is next, I'm sure.
[00:42:11] >> Yeah.
[00:42:11] >> Yeah. I'm curious about the whole
[00:42:13] spatial intelligence space. I think we
[00:42:15] should dig more into that one. How do
[00:42:17] you define it and like what are like the
[00:42:20] gaps between traditional intelligence
[00:42:23] that people might think about a LLMS
[00:42:25] when you know Dario says we have a data
[00:42:27] center full of Einstein that's like
[00:42:29] traditional intelligence it's not
[00:42:31] spatial intelligence what is required to
[00:42:34] be spatially intelligent
[00:42:36] >> first of all I don't understand that
[00:42:38] sentence a data center full of Einsteins
[00:42:41] that
[00:42:43] [laughter]
[00:42:43] >> I I just don't understand that it's not
[00:42:45] a
[00:42:46] >> it's an analogy it's analogy.
[00:42:47] >> Well, so a lot of AI as a field, as a
[00:42:52] discipline is inspired by human
[00:42:54] intelligence, right? Because we are the
[00:42:56] most intelligent animal we know in the
[00:42:58] universe for now. And if you look at
[00:43:01] human intelligence, it's very
[00:43:04] multi-intelligent,
[00:43:05] right? There is a psychologist, I think
[00:43:07] his name is Howard Gardner in the 1960s
[00:43:10] actually literally called multiple
[00:43:13] intelligence to describe human
[00:43:15] intelligence. And there is linguistic
[00:43:17] intelligence, there's spatial
[00:43:18] intelligence, there is logical
[00:43:20] intelligence and and and emotional
[00:43:23] intelligence. So for me when I think
[00:43:26] about spatial intelligence, I see it as
[00:43:29] complimentary to language intelligence.
[00:43:32] So I I personally would not say it's
[00:43:34] spatial versus traditional because I
[00:43:36] don't know tradition means what does it
[00:43:39] mean? I do think spatial is
[00:43:41] complimentary to linguistic and uh and
[00:43:46] uh how do we define spatial intelligence
[00:43:48] is it's the capability that uh allows
[00:43:51] you to reason,
[00:43:53] understand, move and interact in space.
[00:43:58] And I use this example of the deduction
[00:44:02] of DNA structure, right? And and of
[00:44:04] course I'm simplifying this uh story,
[00:44:07] but a lot of that had to do with the
[00:44:10] spatial reasoning of the molecules and
[00:44:13] the chemical bonds in a 3D space to to
[00:44:17] eventually conjecture a double helix and
[00:44:20] that ability that humans or uh Francis
[00:44:24] Cricken Watson had had done. It is very
[00:44:29] very hard to reduce that process into
[00:44:32] pure language. And that's that's a
[00:44:34] pinnacle of a civilizational moment. But
[00:44:37] every day, right, I'm here trying to
[00:44:39] grasp a a mug. This whole process of
[00:44:43] seeing the mug, seeing the context where
[00:44:46] it is, seeing my own hand, opening of my
[00:44:49] hand that geometrically would match the
[00:44:51] mug and touching the right affordance
[00:44:54] point. All this is deeply deeply spatial
[00:44:57] there. It's very hard. I'm trying to use
[00:45:00] language to narrate it. But on the other
[00:45:03] hand, that narrated language itself
[00:45:06] cannot get you to to pick up a a mug.
[00:45:09] >> Yeah. Bandwidth constraint.
[00:45:10] >> Yes.
[00:45:10] >> I did some math recently on like if you
[00:45:12] just spoke uh all day every day for 24
[00:45:15] hours a day, uh how many tokens do you
[00:45:17] generate? at the average speaking rate
[00:45:18] of like 150 words per minute, it roughly
[00:45:21] rounds rounds out to about 215,000
[00:45:23] tokens per day and like your your your
[00:45:27] world that you live in is so much higher
[00:45:29] bandwidth than that. [laughter]
[00:45:31] >> Well, I think that is true. But if I
[00:45:34] think about Sir Isaac Newton, right,
[00:45:36] it's like you have things like gravity
[00:45:38] at the time that have not been
[00:45:39] formalized in language that people
[00:45:42] inherently spatially understand that
[00:45:43] things fall, right? But then it's
[00:45:46] helpful to formalize that in some way or
[00:45:48] like you know all these different rules
[00:45:50] that we use language to like really
[00:45:53] capture something that empirically and
[00:45:55] spatially you can also understand but
[00:45:57] it's easier to like describe in a way.
[00:45:59] So I'm curious like the interplay of
[00:46:01] like spatial and like linguistic
[00:46:03] intelligence which is like okay you need
[00:46:05] to understand some rules are easier to
[00:46:07] write in language for then the spatial
[00:46:10] intelligence to understand but you
[00:46:12] cannot you know you cannot write put
[00:46:14] your hand like this and put it down this
[00:46:16] amount. So I'm always curious about how
[00:46:18] you leverage each other together.
[00:46:20] >> I mean if if anything like the example
[00:46:22] of of Newton like Newton only thinks to
[00:46:24] write down those laws because he's had a
[00:46:25] lot of embodied experience in the world
[00:46:27] watching baseball.
[00:46:28] >> Exactly. And actually it's useful to
[00:46:29] distinguish between the theory building
[00:46:30] that you're mentioning versus like the
[00:46:32] embodied like the daily experience of
[00:46:34] being embedded in the threedimensional
[00:46:35] world. Right. So so to me spatial
[00:46:38] intelligence is sort of encapsulating
[00:46:40] that embodied experience of being there
[00:46:42] in 3D space moving through it seeing it
[00:46:44] actioning it. And as Fay said you can
[00:46:46] narrate those things but it's a very
[00:46:48] lossy channel. It's a just like the
[00:46:49] notion of you know being in the world
[00:46:52] and doing things in it is a very
[00:46:53] different modality from trying to
[00:46:55] describe it. But because we as humans
[00:46:58] are animals who have evolved interacting
[00:47:00] in space all the time, like we don't
[00:47:01] even think that that's that's a hard
[00:47:03] thing, right? And then we sort of
[00:47:04] naturally leap to language and then
[00:47:06] theory building as mechanisms to
[00:47:08] abstract above that sort of native
[00:47:10] spatial understanding. And in some
[00:47:12] sense, LLM have just like jumped all the
[00:47:13] way to those highest forms of abstracted
[00:47:15] reasoning, which is very interesting and
[00:47:17] very useful. But spatial intelligence is
[00:47:19] almost like opening up that black box
[00:47:21] again and saying maybe we've lost
[00:47:22] something by going straight to that
[00:47:23] fully abstracted form of of language and
[00:47:25] reasoning and communication.
[00:47:27] >> You know, it's funny as a vision
[00:47:28] scientist, right? I always find that
[00:47:30] vision is underappreciated
[00:47:33] because it's effortless for humans. You
[00:47:36] open your eyes as a baby, you start to
[00:47:39] see your work. We're somehow born with
[00:47:40] it,
[00:47:40] >> right? We're almost born with it. But
[00:47:43] you have to put effort in learning
[00:47:45] language including learning how to
[00:47:47] write, how to do grammar, how to express
[00:47:50] and that makes it feel hard. Whereas
[00:47:53] something that nature spend way more
[00:47:56] time actually optimizing which is
[00:47:58] perception and spatial intelligence is
[00:48:01] underappreciated by humans.
[00:48:03] >> Is there proof that we are born with it?
[00:48:05] You said you said almost born. So it
[00:48:06] sounds like we actually do learn after
[00:48:09] we're born. When we are born, our visual
[00:48:11] acuity is less and our perceptual
[00:48:15] ability does increase. But we are most
[00:48:19] humans are born with the ability to see
[00:48:22] and most humans are born with the
[00:48:24] ability to link perception with motor um
[00:48:28] movements, right? I mean the motor
[00:48:30] movement itself is takes a while to uh
[00:48:33] refine, but uh and then animals are
[00:48:36] incredible, right? Like I was just in
[00:48:38] Africa earlier this summer. These little
[00:48:40] animals, they're born and within minutes
[00:48:42] they have to get going and otherwise the
[00:48:44] you know the the the lions will get
[00:48:46] them. And in nature, you know, it took
[00:48:49] 540 million years to uh optimize
[00:48:53] perception and spatial intelligence and
[00:48:55] language. The most generous estimation
[00:48:58] of uh language development is probably
[00:49:01] half a million years.
[00:49:02] >> Wow.
[00:49:03] >> Yeah, [laughter]
[00:49:03] >> that's longer than I would have got to
[00:49:05] say. Well, I'm being very generous.
[00:49:07] Yeah.
[00:49:08] >> Yeah. No, I I was uh you know, sort of
[00:49:10] going through your book and I was sort
[00:49:11] of realizing that that one of the
[00:49:13] interesting links to something that we
[00:49:15] covered on the podcast is language model
[00:49:18] benchmarks and how wow grand uh actually
[00:49:21] put in all these like sort of physical
[00:49:22] impossibilities that require spatial
[00:49:23] intelligence, right? Like A is on top of
[00:49:25] B, therefore A cannot fall through B
[00:49:27] >> is
[00:49:28] >> obvious to us, but to a language model
[00:49:30] it could happen. I don't know, maybe
[00:49:32] it's like a part of the, you know, the
[00:49:34] next token prediction.
[00:49:35] >> And that's sort of what I mean about
[00:49:36] like unwrapping this abstraction, right?
[00:49:38] Like if your whole model of the world is
[00:49:39] just like saying sequences of words
[00:49:41] after each other, it's really kind of
[00:49:43] hard to like why why not?
[00:49:45] >> It's actually unfair,
[00:49:46] >> right? But then the reason it's obvious
[00:49:47] to us is because we are internally
[00:49:49] mapping it back to some threedimensional
[00:49:50] representation of the world that we're
[00:49:52] familiar with. This the question is I
[00:49:53] guess like how hard is it, you know, how
[00:49:55] long is it going to take us to distill
[00:49:58] from? Like I I use the word distill. I
[00:50:00] don't know if you agree with that to
[00:50:01] distill from your world models into a
[00:50:03] language model cuz we do want our models
[00:50:05] to have spatial intelligence right like
[00:50:07] and do we have to throw language model
[00:50:09] out completely in order to to do that or
[00:50:11] >> no
[00:50:12] >> no right I don't think so right
[00:50:13] >> I think they're multimodal I mean even
[00:50:15] our model marble today takes language as
[00:50:17] a input
[00:50:18] >> right
[00:50:18] >> right so it's deeply multi multimodel
[00:50:21] and I think in many use cases these
[00:50:24] models will work together maybe one day
[00:50:26] we'll have a universal model
[00:50:28] >> I mean even even if you do like there
[00:50:29] there's sort of a pragmatic thing where
[00:50:31] people use language and people want to
[00:50:33] interact with systems using language.
[00:50:35] Even pragmatically, it's useful to build
[00:50:37] systems and build products and build
[00:50:38] models that let people talk to them. So,
[00:50:40] I don't see that going away. I think
[00:50:42] there's a sort of intellectual curiosity
[00:50:44] of of saying how like intellectually how
[00:50:46] much could you build a model that that
[00:50:48] only uses vision or only uses spatial
[00:50:50] intelligence. I don't know that that
[00:50:52] would be practically useful, but I think
[00:50:53] it'd be an interesting intellectual or
[00:50:54] academic exercise to see how far you
[00:50:56] could push that. I think I mean not to
[00:50:58] bring it back to physics but I'm curious
[00:51:00] like if you had a highly precise world
[00:51:03] model and you didn't give it any notion
[00:51:06] of like our current understanding of the
[00:51:08] standard model of physics how much of it
[00:51:10] it would be able to come up with and
[00:51:12] like recreate from scratch and what
[00:51:14] level of like language understanding it
[00:51:17] would need because we have so many
[00:51:18] notations that like we kind of use that
[00:51:19] like we create it but like maybe we'll
[00:51:21] come up with a very different model of
[00:51:23] it and still be accurate and I wonder
[00:51:25] how much we're kind of limited But I you
[00:51:28] know how people say human always need to
[00:51:29] be like humans because the world is
[00:51:31] built for humans and in a way it's like
[00:51:33] the way we build language constraints
[00:51:36] some of the outputs that we can get from
[00:51:38] these other modalities as well. So I'm
[00:51:40] super excited to follow your work.
[00:51:42] >> Yeah. I mean like there's another I mean
[00:51:43] you actually don't even need to be doing
[00:51:44] AI to answer that question. You could
[00:51:46] discover aliens and see what kind of
[00:51:47] physics they have, right? And they might
[00:51:49] have a
[00:51:49] >> let's face it we are so far the smartest
[00:51:53] animal in the universe,
[00:51:54] >> right? So, so what do you so I mean but
[00:51:55] that is a really interesting question
[00:51:56] right like is our knowledge of the
[00:51:58] universe and our understanding of
[00:51:59] physics is it constrained in some way by
[00:52:01] our own cognition or by the path
[00:52:03] dependence of our own technological
[00:52:04] evolution and one way to sort of and
[00:52:07] like do an experiment like you almost
[00:52:08] want to do an experiment and say like if
[00:52:10] we were to rerun human civilization
[00:52:11] again would we come up with the same
[00:52:13] physics in the same order and I don't
[00:52:14] think that's a very practical practical
[00:52:16] experiment to run
[00:52:17] >> you know one experiment I wonder if
[00:52:18] people could run is that we have plenty
[00:52:21] of astrophysical
[00:52:23] data now on the planet uh or or
[00:52:26] celestial body uh movements just feed
[00:52:29] the data into a model and see if
[00:52:31] Newtonian law uh emerges.
[00:52:34] >> My my guess is it probably probably
[00:52:36] won't.
[00:52:37] >> That's my guess. It's not the
[00:52:39] abstraction level of Newtonian law is at
[00:52:42] a different level from what these
[00:52:44] language uh LLM represents.
[00:52:47] >> Yeah. So I wouldn't be surprised that
[00:52:50] given enough celestial movement data, an
[00:52:53] LLM would actually predict pretty
[00:52:55] accurate movement trajectories. Let's
[00:52:58] say I invent a planet uh surrounding a a
[00:53:02] a star and giving enough data my my
[00:53:05] model would tell you, you know, on day
[00:53:08] one where it is, day two where it is. I
[00:53:10] wouldn't be surprised. But F equals MA
[00:53:14] or or you know action equals reaction.
[00:53:18] That's just a whole different
[00:53:19] abstraction level. That's beyond just
[00:53:22] the today's LLM.
[00:53:23] >> Okay. What what model would you need to
[00:53:26] not have it be a geocentric model?
[00:53:28] Because if I'm training just on visual
[00:53:30] data, it makes sense that you think the
[00:53:32] sun rotates around the earth, right? But
[00:53:34] obviously that's not the case. So how
[00:53:38] would it learn that? Like I'm curious
[00:53:40] about all these like you know forces
[00:53:41] that we talk about it's like sometimes
[00:53:43] maybe you don't need them because as
[00:53:45] long as it looks right it's right but
[00:53:47] like as you make the jump to like trying
[00:53:49] to use these models to do more highle
[00:53:51] tasks how much can we rely on them I
[00:53:54] think you can need kind of a different
[00:53:56] learning paradigm right so like you know
[00:53:58] there's a bit of conflation here
[00:53:59] happening where saying is it LLMs and
[00:54:02] language and symbols versus you know
[00:54:05] human theory building and human human
[00:54:06] physics and they're very different
[00:54:08] because an LLM Like the human objective
[00:54:10] function is to understand the world and
[00:54:12] thrive in your life. And the way that
[00:54:14] you do that is by you know sometimes you
[00:54:16] observe data and then you think about it
[00:54:18] and then you try to do something in the
[00:54:19] world and it doesn't match your
[00:54:21] expectations and then you want to go and
[00:54:22] update sort of your your your your
[00:54:24] understanding of the world online. And
[00:54:26] people do this all the time constantly
[00:54:28] like whether it's you know I think my
[00:54:30] keys are downstairs so I go downstairs
[00:54:31] and I look for them and I don't see them
[00:54:33] and oh no they're actually up in my
[00:54:34] bedroom. So we're we're like because
[00:54:36] we're constantly interacting with the
[00:54:38] world, we're constantly having to build
[00:54:40] theories about what's happening in the
[00:54:41] world around us and then falsify or add
[00:54:44] evidence to those theories. And I think
[00:54:46] that that kind of process writ large and
[00:54:48] scaled up is what gives us F= MA and
[00:54:50] Newtonian physics. And I think that's a
[00:54:52] little orthogonal to you know the
[00:54:53] modality of model that we're training
[00:54:55] whether it's language or or or
[00:54:56] spatially. The way I put it is almost
[00:54:58] like this is almost more efficient
[00:55:00] learning because you have a hypothesis
[00:55:02] of here are the different possible
[00:55:04] worlds that are granted by my available
[00:55:06] data and you then you do experiments to
[00:55:08] eliminate the worlds that are not
[00:55:10] possible and you resolve to the one
[00:55:11] that's right. To me, that's also how I
[00:55:14] also have theory of mind, which is like
[00:55:16] I'm I have a few the thesis of what
[00:55:18] you're thinking, what you're thinking.
[00:55:20] Um, and I try to create actions to
[00:55:23] resolve that or or check my intuition as
[00:55:25] to what you're thinking. You know that
[00:55:27] and and obviously LLMs don't do any of
[00:55:29] these.
[00:55:31] >> A theory of mind possibly also will
[00:55:34] break into even emotional intelligence,
[00:55:36] which today's AI is really not touching
[00:55:39] at all. Right. and when and we really
[00:55:41] really need it. Uh you know people are
[00:55:43] starting to depend on these things uh
[00:55:45] probably too much and uh and that's
[00:55:47] that's a whole topic of of other debate.
[00:55:49] I do have to ask because a lot of people
[00:55:51] have like sent this to us. How much do
[00:55:53] we have to get rid of? Uh you know is uh
[00:55:55] is sequence to sequence modeling out the
[00:55:57] window? Is attention out the window?
[00:55:59] Like how much are we requesting
[00:56:01] everything?
[00:56:02] >> I think uh I think you stick with stuff
[00:56:03] that works right [clears throat] I I
[00:56:05] think attention is still there. I think
[00:56:08] there's a lot like you don't need to fix
[00:56:10] things that aren't broken. Um, and like
[00:56:12] it's it's there's a lot of hard problems
[00:56:14] in the world to solve, but let's focus
[00:56:15] on one at a time. Um, I I think it is
[00:56:17] pretty interesting to think about new
[00:56:18] architectures or new paradigms or or
[00:56:20] drastically different learning ways to
[00:56:22] learn. Um, but you don't need to throw
[00:56:24] away everything just because you're
[00:56:25] working on new modalities.
[00:56:27] >> I think sequence to sequence is actually
[00:56:30] um in world models. I think we are going
[00:56:34] to see algorithm or architecture beyond
[00:56:37] sequence to sequence.
[00:56:38] >> Oh, but but here actually I think
[00:56:39] there's there's a little bit of um you
[00:56:40] know technological confusion and and
[00:56:42] transformers already solved that for us,
[00:56:44] right? Like transformers are actually
[00:56:45] not a model of sequences. A transformer
[00:56:47] is natively a model of sets. Um and
[00:56:49] that's very powerful but because um a
[00:56:51] lot of the transformers grew out of
[00:56:53] earlier architectures based around
[00:56:54] recurrent neural networks and RNN's
[00:56:56] definitely do have like a built-in
[00:56:58] architectural like they do modeled
[00:57:00] one-dimensional sequences. Okay.
[00:57:01] >> But transformers are just object models
[00:57:03] of sets and they can model a lot of
[00:57:05] those sets could be you know 1D
[00:57:07] sequences they could be other things as
[00:57:08] well.
[00:57:08] >> So you literally mean set theory like
[00:57:10] >> Yeah. Yeah. So whatever.
[00:57:12] >> Yeah. Yeah. So a transformer is actually
[00:57:14] not a model of a sequence of tokens. A
[00:57:16] transformer is actually a model of a set
[00:57:18] of tokens, right? The only thing that
[00:57:19] gives that that injects the order into
[00:57:22] in the trans in the standard transformer
[00:57:23] architecture. The only thing that
[00:57:24] differentiates the order of the things
[00:57:26] is the positional embedding that you
[00:57:27] give the tokens, right? So if you if you
[00:57:29] choose to give it a sort of 1D
[00:57:30] positional embedding that's the only
[00:57:32] like mechanism that the model has to
[00:57:34] know that it's a 1D sequence but all the
[00:57:36] all like operators that happen inside a
[00:57:38] transformer block are either token wise
[00:57:40] right so they either you have an FFN you
[00:57:42] have QKV projections like you have per
[00:57:44] token normalization all of those happen
[00:57:46] independently per token and then you
[00:57:47] have interactions between tokens through
[00:57:49] the attention mechanism but that's also
[00:57:51] sort of um it's it's permutation
[00:57:52] equariant so if I permute my tokens then
[00:57:55] the tension operator gets a permuted
[00:57:57] output in exactly the same
[00:57:58] [clears throat] way. So, it's actually
[00:57:59] natively an architecture of sets of
[00:58:01] tokens.
[00:58:02] >> Literally a transform.
[00:58:03] >> Yeah. [laughter]
[00:58:04] >> In in a math term,
[00:58:05] >> I know we're out of time, but uh we just
[00:58:08] want to give you the floor for some call
[00:58:09] to action either on people that would
[00:58:11] enjoy working at World Labs, what kind
[00:58:13] of people should apply, what research
[00:58:15] people should be doing outside of World
[00:58:17] War Labs that would be helpful to you or
[00:58:19] anything else on your mind. I do think
[00:58:21] it's very exciting time to um to be
[00:58:24] looking beyond just language models and
[00:58:27] think about the the boundless
[00:58:29] possibilities of uh spatial
[00:58:31] intelligence. So we are actually hungry
[00:58:33] for talent ranging from very deep
[00:58:36] researchers right thinking about the
[00:58:38] problems like Justin just described you
[00:58:41] know training large models of world
[00:58:43] models uh we are hungry for engineers
[00:58:47] good engineers building systems you know
[00:58:49] from training optimization to inference
[00:58:52] to uh product and we're also hungry for
[00:58:56] good business uh you know um product uh
[00:59:00] thinkers and go to market and you know
[00:59:02] business talents. So, so we are hungry
[00:59:05] for for talent. We especially now that
[00:59:07] we have uh uh exposed the model uh to
[00:59:10] the world through marble, I think we
[00:59:12] have a great opportunity to work with
[00:59:15] even a bigger pool of talent to solve
[00:59:18] both the the model problem as well as uh
[00:59:21] deliver the best product to uh to the
[00:59:23] world.
[00:59:25] >> Yeah, I think I'm also excited for
[00:59:26] people to try Marble and do a lot of
[00:59:27] cool stuff with it. I think it has a lot
[00:59:29] of really cool capabilities, a lot of
[00:59:30] really cool features that fit together
[00:59:32] really nicely.
[00:59:32] >> In the car coming here, Justin and I
[00:59:35] were saying people have not totally
[00:59:36] discovered the Okay, it's only 24 hours
[00:59:39] [laughter]
[00:59:40] have not totally discovered some of the
[00:59:42] advanced mode of editing, right? Like
[00:59:44] turn on the advanced mode. You can, like
[00:59:47] Justin said, change this color of the
[00:59:49] bottle, you know, change your floor and
[00:59:51] change the trees and
[00:59:53] >> Well, I I actually tried to get there,
[00:59:54] but when it says create, it just makes
[00:59:56] me create a completely different world.
[00:59:58] >> You need to click on the advanced
[00:59:59] [laughter] mode. It's a good UI.
[01:00:01] >> We can improve on our UI UI. Remember to
[01:00:05] click.
[01:00:05] >> Yeah, we need to we need to hire people.
[01:00:06] We work on the product. [laughter]
[01:00:08] >> Uh, but one thing we got that was clear
[01:00:10] from you guys are looking for is also
[01:00:11] intellectual fearlessness. which is
[01:00:14] something that I think you guys hold as
[01:00:15] principle.
[01:00:16] >> Yeah, I mean we are literally the first
[01:00:19] people who are trying this both on the
[01:00:21] model side as well as as on the product
[01:00:24] side.
[01:00:24] >> Thank you so much for joining us. This
[01:00:26] was fun. Yeah, thanks for having us.
[01:00:28] >> Yeah.
