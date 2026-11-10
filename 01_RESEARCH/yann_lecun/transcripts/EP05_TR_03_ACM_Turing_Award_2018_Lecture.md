# Geoffrey Hinton & Yann LeCun — 2018 ACM A.M. Turing Award Lecture
- **YouTube URL:** https://www.youtube.com/watch?v=VsnQf7exv5I
- **Lines:** 2904

---

[00:00:03] - Good evening.
[00:00:06] That worked.
[00:00:08] I'm Vivek Sarkar from Georgia Tech.
[00:00:10] And it gives me great pleasure on behalf
[00:00:13] of all the organizers to welcome you
[00:00:16] here in Phoenix for FCRC 2019.
[00:00:19] And to also welcome everyone
[00:00:19] connected on live stream.
[00:00:24] As we all know, and at this point,
[00:00:27] all our deans, provosts,
[00:00:30] high tech managers know,
[00:00:33] our conference is where
[00:00:33] you find the cutting edge
[00:00:35] of computer science research.
[00:00:38] FCRC was created in 1993 with the idea
[00:00:42] of having a federated event
[00:00:42] every three to four years
[00:00:45] at which major conferences
[00:00:45] can be co-located.
[00:00:49] This year we have a record
[00:00:49] number of 2700 participants
[00:00:55] in 30 major conferences
[00:00:57] and many related workshops and tutorials.
[00:01:01] That was about 20% more than
[00:01:01] what we had planned for.
[00:01:05] Actually on that note,
[00:01:06] if your cell phone rings this evening,
[00:01:08] that's 2700 people who will remember you
[00:01:11] for the rest of your career,
[00:01:13] including everyone on live stream.
[00:01:17] Let me take a moment to read out the names
[00:01:19] of all the conferences to
[00:01:19] remind you who all are here.
[00:01:23] So we have COLT, e-Energy, EC
[00:01:27] HPDC, ICS, ISCA, ISMM,
[00:01:32] IWQoS, LCTES, PLDI,
[00:01:36] SIGMETRICS, SPAA, and STOC.
[00:01:40] These conferences cover
[00:01:40] as you know a wide range
[00:01:44] of foundation areas of
[00:01:44] computer science research
[00:01:47] including computer architecture,
[00:01:50] economics and computation,
[00:01:52] embedded systems,
[00:01:53] high performance of super computing,
[00:01:55] machine learning theory,
[00:01:57] measurement and modeling,
[00:01:59] compilers and programming languages,
[00:02:03] memory management,
[00:02:04] panel algorithms,
[00:02:05] quality of service,
[00:02:07] smart energy systems,
[00:02:08] theory of computing,
[00:02:09] and many related topics.
[00:02:12] I'm specially pleased from
[00:02:12] an attendance perspective
[00:02:15] that we also have a record number
[00:02:17] of over 1100 students attending this year.
[00:02:21] I'd like to encourage everyone,
[00:02:23] especially the students to take advantage
[00:02:25] of the unique opportunity offered by FCRC
[00:02:28] to attend sessions and conferences outside
[00:02:31] your research area as
[00:02:31] well so you can be exposed
[00:02:34] to emerging ideas in other
[00:02:34] fields of computer science.
[00:02:38] Just check out the Hoover
[00:02:38] app or the online schedule
[00:02:40] to see what's going on in
[00:02:40] the core located events.
[00:02:45] Now, a major highlight of FCRC,
[00:02:47] the opportunity for you
[00:02:47] to hear plenary talks
[00:02:50] by imminent leaders from different
[00:02:50] areas of computer science
[00:02:54] starting of course with today
[00:02:54] evening's Turing lecture
[00:02:58] by Goeff Hinton and Yann LeCun.
[00:03:01] All plenary talks will
[00:03:01] be held in this beautiful
[00:03:03] symphony hall space.
[00:03:05] During next week, the talks are scheduled
[00:03:08] at 11:20 in the morning each day
[00:03:10] with no conflicting events.
[00:03:12] So be sure to attend.
[00:03:13] You have no excuse for missing them.
[00:03:16] As a reminder, the
[00:03:16] plenary speakers next week
[00:03:18] are Jim Smith,
[00:03:20] Cynthia Dwork,
[00:03:21] Shriram Krishnamurthi,
[00:03:23] Jeannette Wing,
[00:03:24] and Erik Lindahl,
[00:03:25] and they will all be
[00:03:25] introduced by Mary Hall,
[00:03:28] the plenary speaker chair for FCRC.
[00:03:32] Though I'll have the opportunity to give
[00:03:35] more comprehensive round of thanks
[00:03:36] to everyone at the end of
[00:03:36] the conference on Friday,
[00:03:39] I'd like to definitely express
[00:03:39] my deepest appreciation
[00:03:43] to the sponsors of all conferences,
[00:03:45] and specially the sponsors
[00:03:45] listed here for FCRC as a whole.
[00:03:50] This is a unique once in four years event.
[00:03:53] And that's just not possible without
[00:03:55] the companies listed here stepping up
[00:03:58] to support FCRC.
[00:03:59] So thanks to all of them.
[00:04:02] Also, the entire ACM team
[00:04:02] has been working hard
[00:04:04] to make sure that this
[00:04:04] entire week is a success.
[00:04:08] And I'd like to specially
[00:04:08] thank Donna Kappel,
[00:04:10] for her tireless leadership
[00:04:10] of the conference
[00:04:13] administration team.
[00:04:15] Donna's been involved with organizing FCRC
[00:04:18] since it's first instance in 1993.
[00:04:22] And is absolutely vital
[00:04:22] to the success of FCRC.
[00:04:25] So thank you Donna.
[00:04:27] Yeah.
[00:04:28] (audience clapping)
[00:04:33] And finally thanks to all of you
[00:04:35] for coming to Phoenix for FCRC
[00:04:37] and for filling this room.
[00:04:39] I hope you have a great conference
[00:04:41] and enjoy the numerous interactions
[00:04:43] with all your CS research colleagues.
[00:04:46] And with that I would like
[00:04:46] to invite Cherri Pancake
[00:04:49] president of ACM to the stage
[00:04:52] to introduce the Turing lecture.
[00:04:56] Thank you.
[00:04:58] (audience clapping)
[00:05:03] - Thank you.
[00:05:03] I'm delighted to be here at FCRC.
[00:05:06] As Vivek mentioned I have
[00:05:06] the honor of being president
[00:05:10] of ACM, the world's largest society
[00:05:13] for computing professionals.
[00:05:15] Did you know that ACM has
[00:05:15] almost 100,000 members
[00:05:18] around the globe?
[00:05:20] We serve the computing community
[00:05:23] in 190 countries with our
[00:05:23] conferences like these,
[00:05:28] our publications,
[00:05:29] webinars, and learning resources.
[00:05:32] ACM is also very active
[00:05:32] in computing education
[00:05:36] and curriculum guidelines
[00:05:36] around the world.
[00:05:40] It's particularly great to be here at FCRC
[00:05:43] because of the reasons
[00:05:43] that Vivek mentioned.
[00:05:46] What a unique opportunity it is.
[00:05:49] We all know that computing has become
[00:05:51] much more interdisciplinary
[00:05:51] but it's not often
[00:05:55] that we have the chance
[00:05:55] to meet and interact
[00:05:58] with leading researchers from other areas
[00:06:01] outside our own.
[00:06:03] I really encourage you to take
[00:06:03] advantage of that this week.
[00:06:08] As all of us know, AI is the
[00:06:08] most rapidly growing area
[00:06:13] in all the sciences.
[00:06:14] And certainly a hot topic
[00:06:14] in society at large.
[00:06:19] The incredible advances
[00:06:19] that we've been seeing
[00:06:22] in AI would not have been possible without
[00:06:26] some of the foundations
[00:06:26] that were established
[00:06:30] by people like those
[00:06:30] we're honoring tonight.
[00:06:34] For example, when we think about impact.
[00:06:39] Think about the research
[00:06:39] that went into development
[00:06:42] of GPUs originally in the gaming industry.
[00:06:46] Who would have imagined at that point
[00:06:48] that later they would be
[00:06:48] assembled into large arrays
[00:06:52] and used as a platform
[00:06:52] for vast neural networks
[00:06:56] that in turn have driven,
[00:06:58] just leapfrogged advances
[00:06:58] in fields like robotics
[00:07:03] and computer vision?
[00:07:06] The kinds of advances that
[00:07:06] we're recognizing tonight
[00:07:09] are those generally in
[00:07:09] the area of deep learning.
[00:07:14] Billions of people around the world
[00:07:16] benefit from the machine
[00:07:16] learning advantages.
[00:07:20] Anybody with a smart phone has access
[00:07:23] to just amazing advances in things
[00:07:26] like computer vision
[00:07:26] and speech recognition
[00:07:29] that we never even dreamed
[00:07:29] of just a few years ago.
[00:07:34] Even more importantly perhaps,
[00:07:36] machine learning has
[00:07:36] been giving scientists
[00:07:39] new tools that are allowing them
[00:07:41] to make advances in fields from medicine
[00:07:44] to astronomy and material science.
[00:07:49] FCRC only happens every four years.
[00:07:52] So when we talked about this session
[00:07:54] we wanted to do something
[00:07:54] special for the welcome session.
[00:07:58] I think you'll agree with me
[00:07:59] that hearing from this year's laureates
[00:08:03] of the Turing prize is the way
[00:08:05] to make it really special.
[00:08:07] The 2018 ACM A.M. Turing award
[00:08:12] was presented just last week
[00:08:14] in San Francisco to three
[00:08:14] pioneers of deep learning.
[00:08:19] Yoshua Bengio,
[00:08:20] Geoffrey Hinton,
[00:08:22] and Yann LeCun.
[00:08:24] The three of them
[00:08:24] collectively and independently
[00:08:28] worked over a 30 year period
[00:08:31] to develop first of all
[00:08:31] the conceptual foundations
[00:08:34] for deep neural networks,
[00:08:37] and then performed experimentation
[00:08:40] that ended up identifying
[00:08:41] a lot of very interesting phenomena.
[00:08:43] But they didn't stop there.
[00:08:45] They went on to develop
[00:08:45] engineering advances
[00:08:49] that demonstrated conclusively
[00:08:52] that deep neural nets
[00:08:52] could actually be applied
[00:08:57] in practice and in an economic way.
[00:09:01] This in turn allowed other people
[00:09:04] to develop these amazing concepts
[00:09:09] that we are now, and
[00:09:09] advances that we are now
[00:09:11] benefiting from in so
[00:09:11] many different areas.
[00:09:16] Computer vision,
[00:09:17] speech recognition,
[00:09:18] natural language processing,
[00:09:20] robotics, so many different other areas.
[00:09:24] So it is with great pleasure
[00:09:26] that I am able to introduce
[00:09:26] tonight's speakers.
[00:09:29] The first is Geoff Hinton,
[00:09:32] who will be giving his
[00:09:32] Turing lecture on the topic
[00:09:36] the Digital Learning Revolution.
[00:09:38] He will be followed by Yann LeCun
[00:09:40] who very fittingly has called his
[00:09:43] talk the Deep Learning
[00:09:43] Revolution, the Sequel.
[00:09:47] So Geoffrey I'd like to welcome you.
[00:09:50] (audience clapping)
[00:10:05] - I'd first like to thank
[00:10:05] all the people at ACM
[00:10:08] who devote their time to making
[00:10:10] all of this run smoothly.
[00:10:14] So there have been two paradigms for AI.
[00:10:19] Since the 1950s, there's been
[00:10:19] the logic inspired approach,
[00:10:24] where the essence of intelligence is seen
[00:10:26] as symbolic expressions operated
[00:10:29] on by symbolic rules.
[00:10:31] And the main problem has been reasoning.
[00:10:34] How do we get a computer to
[00:10:34] do reasoning like people do?
[00:10:40] And there's been the
[00:10:40] biologically inspired approach.
[00:10:42] Which is very different.
[00:10:45] It sees the essence of intelligence
[00:10:47] as learning the connection
[00:10:47] strengths in the neural network
[00:10:50] and the main things to focus on
[00:10:52] at least to begin with are
[00:10:52] learning and perception.
[00:10:55] So they're very different paradigms
[00:10:57] with very different initial goals.
[00:11:01] They have very different views
[00:11:02] of the internal representations
[00:11:02] that should be used.
[00:11:05] So the symbolic paradigm thinks that
[00:11:09] you should use symbolic expressions
[00:11:11] and you can give these to the computer
[00:11:13] if you invent a good
[00:11:13] language to express them in.
[00:11:16] And you can of course get new expressions
[00:11:18] within the computer by applying rules.
[00:11:20] The biological paradigm thinks
[00:11:22] the internal representations
[00:11:24] are nothing at all like language.
[00:11:26] They're just big vectors
[00:11:26] of neural activity.
[00:11:28] And these big vectors
[00:11:28] have cause and effects
[00:11:30] on other big vectors.
[00:11:33] And these vectors are
[00:11:33] gonna be learned from data.
[00:11:35] So all the structure in these vectors
[00:11:37] is gonna be learned from data.
[00:11:39] I'm obviously giving sort of caricatures
[00:11:41] of the two positions
[00:11:42] to emphasize how different they are.
[00:11:46] They lead to two very different ways
[00:11:47] of trying to get a computer
[00:11:47] to do what you want.
[00:11:50] So one method which I slightly naughtily
[00:11:55] call intelligent design
[00:11:56] is what you would call programming,
[00:11:59] it's you figure out how
[00:11:59] to solve the problem.
[00:12:01] And then you tell the
[00:12:01] computer exactly what to do.
[00:12:05] The other method is you
[00:12:05] just show the computer
[00:12:07] a lot of examples of
[00:12:07] inputs and the outputs
[00:12:11] that you produce and you let
[00:12:11] the computer figure it out.
[00:12:13] Of course, you have to
[00:12:13] program the computer there to.
[00:12:15] But it's programmed once
[00:12:17] with some general purpose
[00:12:17] learning algorithm.
[00:12:20] That again is a simplification.
[00:12:23] So an example of a kind of thing
[00:12:25] that people spent 50 years trying to do
[00:12:27] with symbolic AI
[00:12:28] is take an image and
[00:12:28] describe what's in the image.
[00:12:32] So think about taking
[00:12:32] the millions of pixels
[00:12:37] in the image on the
[00:12:37] left and converting them
[00:12:41] to a string of words.
[00:12:42] It's not obvious how
[00:12:42] you'd write that program.
[00:12:45] People tried for a long time
[00:12:46] and they couldn't write that program.
[00:12:49] People doing neural nets
[00:12:49] also tried for a long time
[00:12:52] and in the end,
[00:12:53] they managed to get a system
[00:12:53] that worked quite well,
[00:12:55] which was based on the
[00:12:55] pure learning approach.
[00:13:00] So the central question for neural nets
[00:13:03] was always we know the big neural nets
[00:13:06] with lots of layers and
[00:13:06] non-linear processing elements
[00:13:09] can compute complicated things.
[00:13:11] At least we believe they can.
[00:13:13] But the question is,
[00:13:14] can they learn to do it?
[00:13:16] So can you learn a task
[00:13:16] like object recognition
[00:13:19] or machine translation
[00:13:20] by taking a big net and
[00:13:20] starting from random weights
[00:13:24] and somehow training it
[00:13:25] so it changes the weights,
[00:13:27] so it changes what it computes?
[00:13:32] There's an obvious learning
[00:13:32] algorithm for such systems
[00:13:34] which was proposed by
[00:13:34] Turing and by Selfridge
[00:13:37] and by many other people,
[00:13:38] variations of it.
[00:13:40] And the idea is you start
[00:13:40] with random weights.
[00:13:43] So this is how Turing believed
[00:13:43] human intelligence works.
[00:13:45] You start with random weights
[00:13:47] and rewards and punishments cause you
[00:13:49] to change the connection strengths
[00:13:51] so you eventually learn stuff.
[00:13:53] Um, this is extremely inefficient.
[00:13:56] It will work.
[00:13:57] But it's extremely inefficient.
[00:14:00] In the 1960s,
[00:14:03] Rosenblatt introduced a fairly simple
[00:14:05] and efficient learning procedure.
[00:14:07] Much more efficient than
[00:14:07] random trial and error
[00:14:09] that could figure out
[00:14:09] how to learn the weights
[00:14:12] on features in which you extract features
[00:14:16] from the image and then you combine
[00:14:20] the features using weights
[00:14:20] to make a decision.
[00:14:23] And he managed to show you
[00:14:23] can do some things like that.
[00:14:26] Some moderately impressive things.
[00:14:28] But in perceptrons you
[00:14:28] don't learn the features.
[00:14:32] That again is a simplification.
[00:14:33] Rosenblatt had all sorts of ideas about
[00:14:35] how you would learn features.
[00:14:36] But he didn't invent backpropagation.
[00:14:39] In 1969, Minsky and Papert showed that
[00:14:41] the kinds of perceptrons that Rosenblatt
[00:14:44] had got to work were very limited
[00:14:46] in what they could do.
[00:14:47] There were some fairly simple things
[00:14:48] they were unable to do.
[00:14:50] And Minsky and Papert strongly implied
[00:14:53] that making them deeper wouldn't help.
[00:14:55] And better learning
[00:14:55] algorithms wouldn't help.
[00:14:57] There was a basic limitation
[00:14:58] of this way of doing things.
[00:15:00] And that led to the
[00:15:00] first neural net winter.
[00:15:05] In the 1970s and the 1980s,
[00:15:08] many different groups invented
[00:15:09] the backpropagation algorithm.
[00:15:11] Variations of it.
[00:15:12] And backpropagation
[00:15:12] allows a neural network
[00:15:16] to learn the feature detectors
[00:15:18] and to have multiple layers
[00:15:18] of learned feature detectors.
[00:15:21] That created a lot of excitement.
[00:15:25] It allowed neural networks for example
[00:15:28] to convert words into vectors
[00:15:32] that represented the
[00:15:32] meanings of the words,
[00:15:34] and they could do that just by trying
[00:15:36] to predict the next word.
[00:15:38] And it looked as if it might be able
[00:15:40] to solve tough problems
[00:15:40] like speech recognition
[00:15:43] and shape recognition.
[00:15:45] And indeed it did solve,
[00:15:47] it did do moderately well
[00:15:47] at speech recognition.
[00:15:49] And for some forms of shape recognition
[00:15:51] it did very well.
[00:15:52] Like Yalican's networks
[00:15:52] that read handwriting.
[00:15:58] But, what I'm gonna do now is explain
[00:16:02] very briefly how neural networks work.
[00:16:04] I know most of you will know this.
[00:16:06] But I just want to go
[00:16:06] over it just in case.
[00:16:09] So we make a gross
[00:16:09] idealization of a neuron.
[00:16:12] And the aim of this idealization
[00:16:15] is to get something that can learn
[00:16:17] so that we can study how you
[00:16:17] put all these things together
[00:16:20] to learn something complicated
[00:16:21] in big networks of these things.
[00:16:23] So it has some incoming weights
[00:16:24] that you can vary.
[00:16:26] Well the learning algorithm will vary.
[00:16:28] And it gives an output
[00:16:28] that's just equal to its input,
[00:16:31] provided the input's
[00:16:31] over a certain amount.
[00:16:33] So that's a rectified linear neuron.
[00:16:35] Which we actually didn't
[00:16:35] start using 'til later
[00:16:37] but these are the kinds of
[00:16:37] neurons that work very well.
[00:16:42] And then you hook them up into a network
[00:16:44] and you have weights
[00:16:44] on the incoming weights
[00:16:48] for each of these neurons.
[00:16:49] And as you change those incoming weights,
[00:16:51] you're changing what feature that neuron
[00:16:53] will respond to.
[00:16:54] So by learning these weights,
[00:16:55] you're learning the features.
[00:16:57] You put in a few hidden layers,
[00:16:59] and then you'd like to train it
[00:17:00] so that the output
[00:17:00] neurons do what you like.
[00:17:03] So for example, we might show it images
[00:17:04] of dogs and cats.
[00:17:06] And we might like the left neuron
[00:17:07] to turn on for a dog
[00:17:07] and the right for a cat.
[00:17:10] And the question is how
[00:17:10] are we gonna train it?
[00:17:14] So there's two kinds of
[00:17:14] learning algorithms mainly.
[00:17:18] Oh there's actually three,
[00:17:19] but the third one doesn't work very well.
[00:17:20] That's called reinforcement learning.
[00:17:22] (audience laughing)
[00:17:25] There's a wonderful reductor
[00:17:27] at absurd of reinforcement
[00:17:27] learning called Deep Mind.
[00:17:30] (audience laughing)
[00:17:32] So, that was a joke.
[00:17:34] (audience laughing)
[00:17:35] There's supervised training
[00:17:36] where you show the network
[00:17:37] what the output ought to be.
[00:17:39] And you adjust the
[00:17:39] weights until it produces
[00:17:42] the output you want.
[00:17:44] And for that you need to know
[00:17:44] what the output ought to be.
[00:17:45] And there's unsupervised learning
[00:17:47] where you take some data
[00:17:49] and you try and represent
[00:17:49] that data in the hidden layers
[00:17:53] in such a way that you
[00:17:53] can reconstruct the data
[00:17:55] or perhaps reconstruct parts of the data.
[00:17:57] If I blank out small parts of the data,
[00:17:59] can I reconstruct them
[00:17:59] now from the hidden notes?
[00:18:02] That's the way unsupervised
[00:18:02] learning typically works
[00:18:05] in neural nets.
[00:18:08] So here's a really inefficient
[00:18:08] way to do supervised learning
[00:18:11] by using a mutational
[00:18:11] reinforcement kinda method.
[00:18:14] What you would do is you
[00:18:14] take your neural net,
[00:18:17] you give it some, a
[00:18:17] typical set of examples,
[00:18:20] you'd see how well it did.
[00:18:21] You then take one weight
[00:18:23] and you change that weight slightly,
[00:18:25] and you'd see if the neural
[00:18:25] net does better or worse.
[00:18:28] If it does better, you keep that change.
[00:18:30] If it does worse you throw it away.
[00:18:33] Perhaps you change in
[00:18:33] the opposite direction
[00:18:35] and that's already a
[00:18:35] factor of two improvement.
[00:18:38] But this is an incredibly
[00:18:38] slow learning algorithm.
[00:18:40] It will work.
[00:18:42] But what it achieves can be
[00:18:42] achieved many, many times
[00:18:45] faster by backpropagation.
[00:18:47] So you could think of backpropagation
[00:18:48] as just an efficient version
[00:18:50] of this algorithm.
[00:18:52] So in backpropagation,
[00:18:54] instead of changing a weight
[00:18:57] and measuring what effect that has
[00:18:59] on the performance of the network,
[00:19:01] what you do is you use the fact
[00:19:02] that all of the weights of the network
[00:19:04] are inside the computer.
[00:19:06] You use that fact to
[00:19:06] compute what the effect
[00:19:08] of a weight change would
[00:19:08] be on the performance.
[00:19:10] And you do that for all of
[00:19:10] the weights in parallel.
[00:19:13] So if you have a million weights,
[00:19:15] you can compute for
[00:19:15] all of them in parallel
[00:19:17] what the effect of a small
[00:19:17] change in that weight
[00:19:19] would be on the performance.
[00:19:21] And then you can update
[00:19:21] them all in parallel.
[00:19:23] That has it's own problems,
[00:19:24] but it'll go a million times faster
[00:19:26] than the previous algorithm.
[00:19:29] Many people in the press describe that
[00:19:31] as an exponential speed up.
[00:19:33] Actually it's a linear speed up.
[00:19:35] The term exponential is used
[00:19:35] quadratically too often.
[00:19:38] (audience laughing)
[00:19:42] So we get to backpropagation
[00:19:45] where you do a forward
[00:19:45] pass through the net,
[00:19:49] you look to see what the outputs are,
[00:19:51] and then using the difference between
[00:19:53] what you got and what you wanted,
[00:19:54] you do a backwards pass
[00:19:56] which has much the same flavor
[00:19:57] as a forward pass.
[00:19:58] It's just high school calculus
[00:20:00] or maybe first university year calculus.
[00:20:03] And you can now compute in parallel
[00:20:07] which direction you should
[00:20:07] change each weight in.
[00:20:10] And then very surprisingly you don't have
[00:20:11] to do that for the whole training set.
[00:20:13] You just take a small batch of examples
[00:20:15] and on that batch of examples you compute
[00:20:17] how to change the connection strengths.
[00:20:19] And you might have got it wrong
[00:20:20] because of the quirks of
[00:20:20] that batch of examples.
[00:20:23] But you change them anyway.
[00:20:24] And then you take another
[00:20:24] batch of examples.
[00:20:26] This is called stochastic
[00:20:26] gradient descent.
[00:20:28] And I guess the major discovery of
[00:20:31] the neural net community is
[00:20:33] that stochastic gradient descent,
[00:20:35] even though it has no real right to work,
[00:20:38] actually works really well.
[00:20:40] But it works really well at scale.
[00:20:42] If you give it lots of data and big nets,
[00:20:44] it really shows its colors.
[00:20:50] However,
[00:20:54] in the 1980s we were very, very pleased
[00:20:56] by backpropagation.
[00:20:57] It seemed to have solved the problem.
[00:20:59] We were convinced it was
[00:20:59] gonna solve everything.
[00:21:02] And it did actually do quite well
[00:21:05] at speech recognition and some forms
[00:21:07] of auditory recognition.
[00:21:08] But it was basically a disappointment.
[00:21:10] It didn't work nearly
[00:21:10] as well as we thought.
[00:21:12] And the real issue was why.
[00:21:14] And at the time people
[00:21:14] had all sorts of analyses
[00:21:16] of why it didn't work.
[00:21:18] Most of which were wrong.
[00:21:19] So they said it's getting trapped
[00:21:21] in local optima.
[00:21:22] We now know that wasn't the problem.
[00:21:26] When other learning
[00:21:26] algorithms worked better
[00:21:29] than backpropagation on
[00:21:29] modest sized data sets,
[00:21:32] most people in the
[00:21:32] machine learning community
[00:21:35] adopted the view that what
[00:21:35] you guys are trying to do
[00:21:39] is learn these deep multi-layer networks
[00:21:42] from random weights just using
[00:21:44] stochastic gradient descent,
[00:21:46] and this is crazy.
[00:21:48] It's never gonna work.
[00:21:49] You're just asking for too much.
[00:21:52] There's no way you're gonna get systems
[00:21:53] like this to work unless you put in
[00:21:55] quite a lot of hand engineering.
[00:21:57] You somehow wire in some prior knowledge.
[00:22:00] So linguists for example
[00:22:02] have been indoctrinated to believe
[00:22:03] that a lot of language is innate
[00:22:05] and you'd never learn language
[00:22:05] without prior knowledge.
[00:22:08] In fact they have mathematical theorems
[00:22:10] that proved you couldn't learn language
[00:22:11] without prior knowledge.
[00:22:14] My response to that is
[00:22:14] beware of mathematicians
[00:22:17] bearing theorems.
[00:22:23] So I just want to give you
[00:22:23] some really silly theories.
[00:22:27] I'm a Monty Python fan.
[00:22:28] So here's some really silly theories.
[00:22:31] The continents used to be connected
[00:22:32] and then drifted apart.
[00:22:34] And you can imagine how silly geologists
[00:22:36] thought that theory was.
[00:22:38] Great big neural nets that start with
[00:22:40] random weights and no prior knowledge
[00:22:41] can learn to do machine translation.
[00:22:43] That seemed like a very, very silly theory
[00:22:45] to many people.
[00:22:48] Just to add one more.
[00:22:49] If you take a natural remedy
[00:22:50] and you keep diluting it,
[00:22:51] the more you dilute it,
[00:22:52] the more potent it gets.
[00:22:54] (audience laughing)
[00:22:55] And some people believe that too.
[00:23:02] So the quote at the top was taken actually
[00:23:04] from the continental drift literature.
[00:23:07] Wegener, who suggested it in 1912,
[00:23:10] was kinda laughed out of town.
[00:23:12] Even though he actually
[00:23:12] had very arguments.
[00:23:14] He didn't have a good mechanism.
[00:23:16] And the geological community said
[00:23:19] we've gotta keep this
[00:23:19] stuff out of the textbooks
[00:23:21] and out of the journals.
[00:23:22] It's just gonna confuse people.
[00:23:25] We had our own little experience of that
[00:23:27] in the second neural net winter.
[00:23:30] So NIPS, of all conferences,
[00:23:34] declined to take a paper of mine.
[00:23:38] You don't forget those things.
[00:23:40] (audience laughing)
[00:23:45] And like many other disappointed authors,
[00:23:48] I had a word with a friend
[00:23:48] on the program committee.
[00:23:51] And my friend on the
[00:23:51] program committee told me,
[00:23:53] "Well, you see they couldn't accept this
[00:23:54] because they had two
[00:23:54] papers on deep learning
[00:23:57] and they had to decide
[00:23:57] which one to accept."
[00:23:59] And they had actually
[00:23:59] accepted the other one.
[00:24:01] So they couldn't reasonably
[00:24:01] be expected to have
[00:24:02] two papers on the same thing
[00:24:02] in the same conference.
[00:24:06] I suggest you go to NIPS now
[00:24:07] and see where they're at.
[00:24:09] (audience laughing)
[00:24:11] Yoshua Bengio submitted a paper to ICML
[00:24:14] in about 2009.
[00:24:15] I'm not certain of the
[00:24:15] year, but it's around then.
[00:24:18] And one of the reviewers said
[00:24:18] that neural network papers
[00:24:22] had no place in a machine
[00:24:22] learning conference.
[00:24:25] So I suggest you to to ICML.
[00:24:28] CVPR, which is the leading
[00:24:28] computer vision conference,
[00:24:31] that was the most
[00:24:31] outrageous of all I think.
[00:24:34] Yann and his coworkers submitted a paper
[00:24:37] doing some antique segmentation
[00:24:39] that beat the state of the art.
[00:24:41] It beat what the main line
[00:24:41] computer vision people could do.
[00:24:45] And it got rejected.
[00:24:47] And one of the reviewers said,
[00:24:49] "This paper tells us nothing
[00:24:49] about computer vision
[00:24:53] "because everything's learned."
[00:24:55] So the reviewer,
[00:24:57] like the field of computer
[00:24:57] vision at the time,
[00:24:59] was stuck in the frame of mind that
[00:25:01] the way you do computer vision is
[00:25:03] you think about the nature
[00:25:03] of the task of vision,
[00:25:06] you preferably write down some equations,
[00:25:08] you think about how to do the computations
[00:25:10] that are required to do vision,
[00:25:12] then you get some implementation of it,
[00:25:13] and then you see whether it works.
[00:25:17] The idea that you just learn everything
[00:25:20] was outside the realm of things
[00:25:22] that were worth considering.
[00:25:24] And so the reviewer
[00:25:24] basically missed the point
[00:25:28] which was that everything was learned.
[00:25:31] He completely failed to see
[00:25:31] how that completely changed
[00:25:34] computer vision.
[00:25:35] Now I shouldn't be too hard on those guys.
[00:25:37] 'Cause a little later on,
[00:25:37] they were very reasonable.
[00:25:40] With a bit more evidence,
[00:25:40] they suddenly flipped.
[00:25:44] So between 2005 and 2009,
[00:25:48] researchers, some of them in Canada,
[00:25:51] we make Yann an honorary Canadian
[00:25:53] 'cause he's French.
[00:25:54] (audience laughing)
[00:25:55] Made several technical advances
[00:25:58] that allowed backpropagation
[00:25:58] to work better
[00:26:00] in feed forward nets.
[00:26:03] They involved using
[00:26:03] unsupervised pre-training
[00:26:05] to initialize the weights
[00:26:06] before you turn on backpropagation.
[00:26:08] Things like dropping out units at random
[00:26:10] to make the whole thing much more robust.
[00:26:13] And introducing rectified linear units
[00:26:15] which turned out to be easier to train.
[00:26:19] For us the details of those advances
[00:26:21] are our bread and butter.
[00:26:22] We are very interested in those.
[00:26:23] But the main message is that
[00:26:26] with a few technical advances,
[00:26:28] backpropagation works amazingly well.
[00:26:30] And the main reason is 'cause we now have
[00:26:32] lots of labeled data
[00:26:34] and a lot of convenient compute power.
[00:26:37] Inconvenient compute power isn't much use.
[00:26:41] But things like GPUs
[00:26:41] and more recently, TPUs,
[00:26:44] allow you to apply a lot of computation
[00:26:47] and they've made the huge difference.
[00:26:49] So really the deciding factor I think
[00:26:51] was the increase in compute power.
[00:26:54] So I think a lot of the
[00:26:54] credit for deep learning
[00:26:57] really goes to the people who collected
[00:26:59] the big databases like Fay Fay Lee.
[00:27:02] And the people who made
[00:27:02] the computers go fast
[00:27:05] like David Patterson and others.
[00:27:08] Lots of others.
[00:27:11] So the killer app from my point of view
[00:27:13] is in 2009 when in my lab
[00:27:16] we've got a bunch of GPUs,
[00:27:18] and two graduate students.
[00:27:21] Made them learn to do
[00:27:27] acoustic modeling.
[00:27:28] Acoustic modeling means you take something
[00:27:30] like a spectrogram
[00:27:31] and you try and figure out
[00:27:32] for the middle frame of the spectrogram,
[00:27:34] which piece of which phone in the speaker
[00:27:36] is trying to express?
[00:27:38] And in this little database we used,
[00:27:40] relatively little,
[00:27:42] there are 183 labels for which piece
[00:27:44] of which phone it might be.
[00:27:47] And so you pre-train
[00:27:47] a net with many layers
[00:27:50] of 2000 hidden units,
[00:27:53] you can't pre-train the last leg
[00:27:54] 'cause you don't know the labels yet.
[00:27:56] And you're training it just to be able
[00:27:57] to reproduce what's in the layer below.
[00:28:00] And then you turn on
[00:28:00] learning in all the layers,
[00:28:03] and it does slightly better
[00:28:03] than the state of the art,
[00:28:05] which had taken 30 years to develop.
[00:28:09] When people in speech saw that,
[00:28:11] the smart people,
[00:28:11] they realized that with
[00:28:11] more development this stuff
[00:28:13] was gonna be amazing.
[00:28:16] And my graduate students went off
[00:28:20] to various groups like
[00:28:20] MSR and IBM & Google.
[00:28:23] In particular Navdeep
[00:28:23] Jaitly went to Google
[00:28:27] and ported the system
[00:28:32] for acoustic modeling
[00:28:33] that was developed in Toronto,
[00:28:35] fairly literally,
[00:28:37] and it came out in the Android in 2012.
[00:28:41] There was a lot of good engineering
[00:28:42] to make it run in real time.
[00:28:45] And it gave a big decrease in error rates.
[00:28:47] And at more or less the same time
[00:28:48] all the other groups started changing
[00:28:50] the way they did speech recognition.
[00:28:52] And now, all the good speech recognizers
[00:28:54] use neural nets.
[00:28:55] They're not like the neural
[00:28:55] nets we introduced initially,
[00:28:58] neural nets have gradually
[00:28:58] eroded more and more
[00:29:01] parts of the system.
[00:29:03] Sort of putting a neural
[00:29:03] net in your system
[00:29:05] is a bit like getting gangrene.
[00:29:06] It'll gradually eat the whole system.
[00:29:11] Then in 2012,
[00:29:14] two other of my graduate students applied
[00:29:17] neural nets of the kind
[00:29:17] developed over many years
[00:29:19] by Yann LeCun to object recognition
[00:29:22] on a big database that
[00:29:24] Fay Fay Lee had put together
[00:29:25] with a 1000 different classes of object.
[00:29:27] And it was finally a big enough database
[00:29:29] of real images so you could show
[00:29:31] what neural nets could do.
[00:29:32] And they could do a lot.
[00:29:34] So if you looked at the results
[00:29:37] all the computer vision systems,
[00:29:39] the standard ones,
[00:29:40] had asymptoted at about 25% error.
[00:29:44] Our system developed by
[00:29:44] two graduate students
[00:29:48] got 16% error.
[00:29:49] And then further work on
[00:29:49] neural nets like that,
[00:29:52] by 2015 it was down to 5%.
[00:29:54] And now it's down to
[00:29:54] considerably below that.
[00:29:58] So then what happened was exactly
[00:30:00] what ought to happen in science.
[00:30:03] Leaders of the computer vision community
[00:30:05] looked at this result and they said,
[00:30:07] "Oh, they really do work.
[00:30:09] "We were wrong.
[00:30:09] "Okay we're gonna switch."
[00:30:11] And within a year they all switched.
[00:30:13] And so science finally
[00:30:13] worked like it was meant to.
[00:30:18] The last thing I want to talk about
[00:30:19] is a radically new way to
[00:30:19] do machine translation.
[00:30:22] Which was introduced in
[00:30:22] 2014 by people at Google
[00:30:26] and also in Montreal by
[00:30:26] people in Yoshua Bengio's lab.
[00:30:30] And the idea in 2014 was for each language
[00:30:32] we're gonna have a neural network.
[00:30:34] It'll be a recurring network
[00:30:35] that is gonna encode the string of words
[00:30:39] in that language.
[00:30:40] Which it receives one at a time
[00:30:41] into a big vector.
[00:30:43] I call that big vector a thought vector.
[00:30:45] The idea is that big
[00:30:45] vector captures the meaning
[00:30:48] of that string of words.
[00:30:50] Then you take that big vector
[00:30:51] and you give it to a decoder network.
[00:30:53] And the decoder network
[00:30:53] turns the big vector
[00:30:56] into a string of words
[00:30:56] in another language.
[00:30:58] And it sorta worked.
[00:31:00] And with a bit of development
[00:31:00] it worked very well.
[00:31:06] Since 2014, one of the
[00:31:06] major pieces of development
[00:31:09] has been that when you're decoding
[00:31:13] the meaning of a sentence,
[00:31:14] what you do is you look back
[00:31:15] at the sentence you were encoding,
[00:31:17] and that's called soft attention.
[00:31:18] So each time you produce a new word
[00:31:20] you're deciding where
[00:31:20] to look in the sentence
[00:31:23] that you're translating.
[00:31:25] That helps a lot.
[00:31:27] You also now pre-train
[00:31:27] the word embeddings.
[00:31:30] And that helps a lot.
[00:31:32] And the way the pre-training works is
[00:31:34] you take a bunch of words and you try
[00:31:38] and reproduce these words in a deep net
[00:31:41] but you've left out some of the words.
[00:31:43] So from these words you have to reproduce
[00:31:45] the same words,
[00:31:46] but you have to fill in
[00:31:46] the blanks essentially.
[00:31:49] They use things called transformers where
[00:31:53] in this deep net,
[00:31:54] as each word goes through the net,
[00:31:57] it's looking at kind of nearby words
[00:32:00] to disambiguate what it might mean.
[00:32:02] So if you have a word like "may,"
[00:32:04] when it goes in you'll
[00:32:04] get an initial vector
[00:32:06] that sorts of ambiguous between
[00:32:06] the modal and the month,
[00:32:09] but if it sees "the 13th" next to it,
[00:32:12] it knows pretty well it's the month.
[00:32:15] And so in the next area
[00:32:15] it can disambiguate that
[00:32:17] and the meaning of that
[00:32:17] May will be the month.
[00:32:21] And those transformer
[00:32:21] nets now work really well
[00:32:23] for getting word embeddings.
[00:32:25] They also it turns out learn
[00:32:25] a whole lot of grammar.
[00:32:28] So all the stuff that linguists thought
[00:32:29] had to be put in innately,
[00:32:31] these neural nets are
[00:32:31] now getting in there.
[00:32:33] They're getting lots of
[00:32:33] syntactical understanding.
[00:32:35] But it's all being learned from data.
[00:32:38] If you look in the early layers
[00:32:39] of transformer nets,
[00:32:40] they know what parts of speech things are.
[00:32:43] If you look in later parts of the nets,
[00:32:44] they know how to disambiguate
[00:32:44] pronoun references.
[00:32:48] Basically, they're learning grammar
[00:32:51] the way a little kid learns grammar.
[00:32:53] Just from looking at sentences.
[00:32:59] So I think that the machine translation
[00:33:01] was really the final nail in the coffin
[00:33:03] of symbolic AI.
[00:33:06] 'Cause machine translation
[00:33:06] is the ideal task
[00:33:08] for symbolic AI.
[00:33:10] It symbols in and it symbols out.
[00:33:13] But it turns out if
[00:33:13] you want to do it well,
[00:33:15] inside what you need is big vectors.
[00:33:22] Okay, I have said everything
[00:33:26] I wanted to say about the
[00:33:26] history up to 2014 or so
[00:33:31] of neural nets.
[00:33:33] I've emphasized the ideology.
[00:33:35] That there were these two camps.
[00:33:37] And that the good guys one.
[00:33:42] It's not over yet
[00:33:43] because of course what we
[00:33:43] need is for neural nets now
[00:33:48] to begin to be able to explain reasoning.
[00:33:51] We can't do that yet.
[00:33:52] We're working on it.
[00:33:54] But reasoning is the last
[00:33:54] thing that people do,
[00:33:56] not the first thing.
[00:33:57] And reasoning is built on
[00:33:57] top of all this other stuff.
[00:34:00] And my view's always been,
[00:34:01] you're never gonna understand reasoning
[00:34:03] until you understand all this other stuff.
[00:34:05] And now we are beginning to
[00:34:05] understand all this other stuff.
[00:34:07] And we're more or less ready
[00:34:08] to begin to understand reasoning.
[00:34:10] But reasoning just with
[00:34:10] sort of bare symbols
[00:34:13] by using rules that
[00:34:13] expresses other symbols.
[00:34:16] That seemed to me just hopeless.
[00:34:18] You're missing all the content.
[00:34:20] There's no meaning there.
[00:34:23] Okay, I want to talk
[00:34:25] a little bit about the
[00:34:25] future of computer vision.
[00:34:28] So convolutional neural nets
[00:34:28] have been very effective.
[00:34:31] And what convolutional neural
[00:34:31] nets do is they wire in
[00:34:34] the idea that if a feature's
[00:34:34] useful in one place,
[00:34:37] it's also gonna be
[00:34:37] useful in another place.
[00:34:39] And that allows us to combine evidence
[00:34:42] from different locations to
[00:34:42] learn a shared feature detector.
[00:34:46] That is to learn replicative
[00:34:46] feature detectors
[00:34:48] that are the same in all these places.
[00:34:50] And that's a huge win.
[00:34:52] It makes it much more data efficient.
[00:34:54] And those things Yann
[00:34:54] got working in the 1990s.
[00:34:57] They were one of the few things
[00:34:59] that worked really well in the 1990s.
[00:35:01] And they work even better now.
[00:35:03] But I don't think they're the way
[00:35:04] people do vision.
[00:35:06] I mean I think one aspect of it,
[00:35:07] that there's replicated apparatus.
[00:35:09] That's clearly true of the brain.
[00:35:13] But they don't recognize objects
[00:35:14] the same way as we do.
[00:35:17] And that leads to adversary examples.
[00:35:19] So if I give you a big database,
[00:35:20] a convolutional neural
[00:35:20] net will do very well.
[00:35:22] It may do better than a person.
[00:35:24] But it doesn't recognize things
[00:35:25] the same way as a person does.
[00:35:27] And so I can change things in a way
[00:35:29] that will cause the
[00:35:29] convolutional neural net
[00:35:31] to change its mind.
[00:35:33] And a person can't even
[00:35:33] see the changes I've made.
[00:35:36] They're using things much
[00:35:36] more like texture and color.
[00:35:39] They're not using the
[00:35:39] geometrical relationships
[00:35:42] between objects and their paths.
[00:35:46] I'm convinced that people,
[00:35:48] the main way in which
[00:35:48] people recognize objects,
[00:35:50] they obviously use texture and color,
[00:35:52] but they're very well aware of
[00:35:52] the geometrical relationships
[00:35:55] between an object and its parts.
[00:35:57] And that geometrical
[00:35:57] relationship is completely
[00:35:59] independent of viewpoint.
[00:36:03] And that gives you something
[00:36:03] that is very robust.
[00:36:05] That you should be able to
[00:36:05] train from much less data.
[00:36:08] And I actually can't resist
[00:36:08] doing a little demonstration
[00:36:11] to convince you that when
[00:36:11] you understand objects,
[00:36:15] it's not just when
[00:36:15] you're being a scientist
[00:36:17] that you use coordinate frames.
[00:36:19] It's even when you're just
[00:36:19] naively thinking about objects,
[00:36:23] you impose coordinate frames on them.
[00:36:25] And so I'm gonna do a
[00:36:25] little demonstration.
[00:36:28] And you have to participate
[00:36:28] in this demonstration,
[00:36:31] otherwise it's no fun.
[00:36:33] Okay, so I want you to imagine
[00:36:33] sitting on the table top
[00:36:35] in front of you there's a cube.
[00:36:37] So here's the top, here's the bottom.
[00:36:39] Here's the cube.
[00:36:40] It's a wire frame cube like this.
[00:36:42] Matte black wires.
[00:36:45] And what I'm gonna do with this cube
[00:36:46] is from your point of view,
[00:36:48] there's a front bottom
[00:36:48] right hand corner here
[00:36:50] and this top back left hand corner here.
[00:36:54] Okay.
[00:36:55] And I'm gonna rotate the cube
[00:36:57] so that the top back left hand corner
[00:37:00] is vertically above the front
[00:37:00] bottom right hand corner.
[00:37:04] So here we are.
[00:37:05] And so now I want you to
[00:37:05] hold your fingertip in space,
[00:37:08] probably your left finger tip,
[00:37:10] where the top vertex of the cube is, okay?
[00:37:13] And now, nobody's doing it, come on.
[00:37:16] (audience laughing)
[00:37:18] Now, with your other finger tip
[00:37:19] I just want you to point
[00:37:19] to where the other corners
[00:37:21] of the cube are.
[00:37:22] The ones that aren't resting on the table.
[00:37:23] So there's one on the table.
[00:37:24] One vertically above it here.
[00:37:26] Where are the other corners?
[00:37:28] And you have to do it,
[00:37:29] you have to point them out.
[00:37:32] Okay, now I can't see what you're doing,
[00:37:35] but I know that a large number of you
[00:37:38] will have pointed out four other corners
[00:37:40] 'cause I've done this before.
[00:37:42] And now I want you to imagine a cube
[00:37:43] in the normal orientation and ask
[00:37:45] how many corners does it have?
[00:37:49] It's got eight corners, right?
[00:37:50] So there's six of these guys.
[00:37:52] And what most people do is they say
[00:37:53] here, here, here, and here.
[00:37:55] What's the problem?
[00:37:56] Well the problem is that's not a cube.
[00:37:58] What you've done is you've preserved
[00:38:00] the four fold rotational
[00:38:00] symmetry that a cube has.
[00:38:04] And pointed out a
[00:38:04] completely different shape.
[00:38:06] It's a completely different shape
[00:38:07] that has the same number of faces
[00:38:09] as a cube has corners.
[00:38:10] And the same number of
[00:38:10] corners as a cube has faces.
[00:38:12] It's the jewel of a cube.
[00:38:14] If you substitute corners for faces.
[00:38:16] 'Cause you really like symmetry so much
[00:38:17] that you had to really mangle things
[00:38:19] to preserve the symmetries.
[00:38:22] Actually, a cube has three
[00:38:22] edges coming down like that.
[00:38:26] And three just coming up like that.
[00:38:28] And my six fingertips are
[00:38:28] where the corners are.
[00:38:31] And people just can't see that.
[00:38:33] Unless they're crystallographers
[00:38:33] or very clever.
[00:38:37] So the main point of this demo
[00:38:39] is I forced you by doing this rotation
[00:38:42] to use an axis for the cube.
[00:38:44] The main axis that defined
[00:38:44] the orientation of the cube
[00:38:47] was not one of the axes
[00:38:47] of the coordinate frame
[00:38:50] you usually use for a cube.
[00:38:52] And by forcing you to use an
[00:38:52] unfamiliar coordinate frame,
[00:38:55] I destroyed all your knowledge
[00:38:56] about where the parts of a cube are.
[00:38:58] You understand things
[00:38:58] relative to coordinate frames.
[00:39:02] And if I get you to impose a
[00:39:02] different coordinate frame,
[00:39:05] it's just a different object
[00:39:05] as far as you're concerned.
[00:39:07] Now convolutional nets don't do that.
[00:39:10] And because they don't do that,
[00:39:11] I don't think they're the
[00:39:11] way people perceive shapes.
[00:39:16] We've recently managed to
[00:39:16] make neural nets do that
[00:39:19] by doing some self supervised training.
[00:39:22] And there's an archive reference there
[00:39:25] which if you're very quick you could get
[00:39:28] or you could, I'll send
[00:39:28] out a tweet about it later.
[00:39:35] And the last thing I want to say
[00:39:37] is not about shape
[00:39:37] recognition in particular,
[00:39:39] but about the future of neural networks.
[00:39:41] There's something very
[00:39:41] funny and very unbiological
[00:39:43] we've been doing for the last 50 years.
[00:39:46] Which is we've only been
[00:39:46] using two time scales.
[00:39:49] That is you have neural activities,
[00:39:51] and they change rapidly.
[00:39:53] And you have weights
[00:39:53] and they change slowly.
[00:39:55] And that's it.
[00:39:57] But we know that in
[00:39:57] biology synapses change
[00:40:00] at all sorts of time scales.
[00:40:03] And the question is what happens
[00:40:05] if you now introduce more time scales.
[00:40:08] In particular, let's just
[00:40:08] introduce one more time scale
[00:40:11] and let's say that in addition
[00:40:12] to these weights changing slowly,
[00:40:15] and that's what's going
[00:40:15] on in long term learning.
[00:40:17] The weights have a component.
[00:40:20] The very same weights,
[00:40:21] the very same synapses.
[00:40:22] But there's an extra component
[00:40:23] that can change more rapidly
[00:40:25] and decays quite rapidly.
[00:40:28] So if you ask where's your memory
[00:40:30] of the fact that a minute ago
[00:40:32] I put my finger on this corner here,
[00:40:34] is that in a bunch of neurons
[00:40:35] that are sitting there
[00:40:38] sort of being active,
[00:40:39] so that you can remember that?
[00:40:40] That seems unlikely.
[00:40:41] It's much more likely your memory for this
[00:40:44] is in fast modifications to the weights
[00:40:46] of the neural network that allow you
[00:40:48] to reconstruct this very rapidly.
[00:40:50] And that will decay with time.
[00:40:53] So you've got a memory
[00:40:53] that's in the weights,
[00:40:55] that's a short term memory.
[00:40:57] As soon as you do that,
[00:40:57] all sorts of good things happen.
[00:41:01] You can use that to get a
[00:41:01] better optimization method.
[00:41:05] And you can use that to do something
[00:41:07] that may very well be
[00:41:07] relevant to reasoning.
[00:41:11] You can use it to allow neural networks
[00:41:13] to do true recursion.
[00:41:14] Not very deep, but true recursion.
[00:41:16] And what I mean by true recursion
[00:41:17] is when you do the recursive call
[00:41:21] like a relative clause in a sentence,
[00:41:24] the neural net can use
[00:41:24] all the same neurons
[00:41:27] and all the same weights
[00:41:28] that it was using for the whole sentence
[00:41:30] to process the relative clause.
[00:41:33] And of course to do that,
[00:41:34] somehow it has to
[00:41:34] remember what was going on
[00:41:37] when it decided to process
[00:41:37] the relative clause.
[00:41:40] It has to store that somewhere.
[00:41:42] And I don't think it
[00:41:42] stores it on the neurons,
[00:41:43] I think it stores it in temporary changes
[00:41:46] to synapse strengths.
[00:41:47] And when it's finished
[00:41:47] processing the relative clause,
[00:41:49] it packages it up and says,
[00:41:50] basically it says now what was I doing
[00:41:52] when I started doing this processing?
[00:41:54] And it can get the information back
[00:41:56] from this associative
[00:41:56] memory and the fast weights.
[00:42:00] I wanted to finish with that
[00:42:01] because the very first talk I gave in 1973
[00:42:05] was about exactly that.
[00:42:06] I had a system that worked on a computer
[00:42:08] that had 64K of memory.
[00:42:11] I haven't got round to publishing it yet.
[00:42:13] But I think it's becoming
[00:42:13] fashionable again,
[00:42:14] so I soon will.
[00:42:17] And that's the end of my talk.
[00:42:20] And I'm out of time.
[00:42:21] (audience clapping)
[00:42:32] And now I'd like to introduce Yann LeCun
[00:42:35] who's not only a colleague,
[00:42:36] but a very good friend.
[00:42:39] (audience clapping)
[00:42:46] - Okay, I'll talk about the sequel.
[00:42:51] But I'll start also with
[00:42:51] a little bit of history
[00:42:53] and sort of go through some of the things
[00:42:55] that Geoff just mentioned.
[00:42:58] So Geoff talked about
[00:43:01] supervised learning.
[00:43:02] And supervised learning
[00:43:02] works amazingly well
[00:43:04] if you have lots of data.
[00:43:06] We all knew this so we
[00:43:06] can do speech recognition,
[00:43:08] we can do image recognition,
[00:43:11] we can do face recognition,
[00:43:13] we can generate captions for images.
[00:43:15] We can do translation.
[00:43:16] That works really well.
[00:43:18] And if you give your neural
[00:43:18] net a particular structure
[00:43:20] in something like a convolutional net,
[00:43:23] as Geoff mentioned in
[00:43:23] the late 80s, early 90s,
[00:43:26] we could train systems
[00:43:26] to recognize handwriting
[00:43:29] that was quite successful.
[00:43:31] By the end of the 90s,
[00:43:31] a system of this type
[00:43:33] that I built at Bell Labs,
[00:43:35] was reading something like 10 to 20%
[00:43:37] of all the checks in the U.S.
[00:43:38] So a big success,
[00:43:40] even a commercial success.
[00:43:41] But by the time the entire community
[00:43:45] had basically abandoned neural nets,
[00:43:46] partly because of the
[00:43:46] lack of large datasets
[00:43:49] for which they could work.
[00:43:50] Partly because the type
[00:43:50] of software at the time
[00:43:52] that you had to write
[00:43:52] was fairly complicated
[00:43:54] and it was a big investment to do this.
[00:43:58] Partly also because computers
[00:43:58] were not fast enough for
[00:44:02] all kinds of other applications.
[00:44:04] But convolutional nets really are
[00:44:06] inspired by biology.
[00:44:08] They're not copying biology,
[00:44:09] but there is a lot of
[00:44:09] inspiration from biology,
[00:44:12] from the architecture of the visual cortex
[00:44:15] and ideas that come naturally
[00:44:17] when used to the signal processing
[00:44:18] the idea that filtering is a good way
[00:44:22] to kinda process signals.
[00:44:24] Whether they are audio
[00:44:24] signals or image signals.
[00:44:27] And the convolution is
[00:44:27] the way to do filtering
[00:44:29] is very natural.
[00:44:30] And the fact that you
[00:44:30] find this in the brain
[00:44:31] is really not that surprising.
[00:44:33] And those ideas of course were proposed
[00:44:36] by Hubel and Wiesel in
[00:44:36] sort of classic work
[00:44:38] in neuroscience back
[00:44:38] in the 60s as well as,
[00:44:42] and sort of picked up by Fukushima,
[00:44:44] who's a Japanese researcher who tried
[00:44:46] to build computer models
[00:44:49] of the Hubel & Wiesel model if you want.
[00:44:52] And I found that inspiring
[00:44:54] and sort of tried to reproduce this
[00:44:56] using neural nets that could be trained
[00:44:58] with backpropagation.
[00:44:59] That's basically what
[00:44:59] a convolutional net is.
[00:45:03] And so the idea of a
[00:45:03] convolutional net is that
[00:45:05] the world, the perceptual world
[00:45:08] is compositional.
[00:45:10] That the visual world,
[00:45:13] objects are formed by parts,
[00:45:15] and parts are formed by motifs,
[00:45:18] and motifs are formed by textures
[00:45:23] or elementary combinations of edges
[00:45:26] and edges are formed by pixels,
[00:45:29] arrangements of pixels.
[00:45:30] And so if you have a system
[00:45:31] that sort of hierarchically can detect
[00:45:35] unusually useful combinations
[00:45:35] of pixels into edges,
[00:45:38] and edges into motifs,
[00:45:40] and motifs into parts of objects,
[00:45:41] then you will have a recognition system.
[00:45:43] This idea of hierarchy
[00:45:43] actually goes back a long time.
[00:45:46] And so that's the really the principal
[00:45:48] of convolutional nets.
[00:45:50] And it turns out that
[00:45:50] hierarchical representations
[00:45:53] are good not just for vision,
[00:45:55] but also for speech,
[00:45:56] for text, and for all kinds
[00:45:56] of other natural signals
[00:45:59] that are comprehensible because
[00:46:01] they are compositional.
[00:46:03] I think there is this saying.
[00:46:05] It's attributed to Einstein I believe.
[00:46:09] What is most
[00:46:12] mysterious about the world is that
[00:46:14] it is understandable.
[00:46:16] And it's probably because
[00:46:16] of the compositional nature
[00:46:20] of natural signals.
[00:46:22] So in the early 90s, we're able
[00:46:25] to do things like build
[00:46:25] recognition systems like this one.
[00:46:28] This is the younger
[00:46:28] version of myself here.
[00:46:30] I'm at Bell Labs.
[00:46:31] This is by the way my
[00:46:31] phone number at Bell Labs
[00:46:33] in Holmdel, no longer operating.
[00:46:35] I'm hitting a key here and
[00:46:35] the system captures an image
[00:46:39] with a video camera.
[00:46:40] This runs on the PC with
[00:46:40] a special DSP card in it.
[00:46:43] And it could run those convolutional nets
[00:46:45] at several hundred characters per second
[00:46:47] at the time which was amazing.
[00:46:49] We could run 20 mega flops.
[00:46:50] You know that was just incredible.
[00:46:52] So that worked pretty well.
[00:46:55] And pretty soon we realized we could use
[00:46:57] this on actual images as well
[00:46:58] to do things like detecting faces.
[00:47:02] Eventually detecting pedestrians.
[00:47:03] That took a few years.
[00:47:06] But as Geoff mentioned there
[00:47:06] was sort of a neural net winter
[00:47:09] between the mid 90s and the
[00:47:09] sort of late 2000 if you want
[00:47:13] where almost nobody
[00:47:13] was working neural nets
[00:47:16] except a few crazy people like us.
[00:47:19] So that didn't stop us.
[00:47:21] And so working on face detection,
[00:47:24] pedestrian detection.
[00:47:25] Even working on using machine learning
[00:47:28] and convolutional net for robotics
[00:47:31] where we would use a convolutional net
[00:47:34] to label an entire
[00:47:34] image in such a way that
[00:47:38] every pixel in an image would be labeled
[00:47:40] as to whether it's
[00:47:40] traversable or not traversable
[00:47:43] by a robot.
[00:47:44] And the nice thing about this is that you
[00:47:46] can collect data automatically.
[00:47:48] You don't need to manually label it
[00:47:49] because using stereo
[00:47:49] vision you can figure out
[00:47:52] if a pixel sticks out of the ground or not
[00:47:56] using 3D reconstruction.
[00:47:57] But unfortunately that
[00:47:57] only works at short range.
[00:47:59] So if you want a system that can plan
[00:48:01] long range trajectories,
[00:48:03] then you can train a convolutional net
[00:48:04] to make the predictions for traversability
[00:48:07] using those labels and then let the robot
[00:48:10] drive itself around.
[00:48:11] So it's got this particular robot here
[00:48:13] has a combination of different features
[00:48:16] that it uses extracted
[00:48:16] by the convolutional net
[00:48:21] and also a rapid stereo vision system
[00:48:24] that allows it to avoid obstacles
[00:48:28] such as pesky graduate students.
[00:48:30] (audience laughing)
[00:48:33] Cassel Manet and Ryan Hedse
[00:48:33] by the way who are pretty sure
[00:48:37] the robot is not gonna run them over
[00:48:38] because they actually wrote the code.
[00:48:41] (audience laughing)
[00:48:44] Okay, and then a couple years later
[00:48:46] we used a very similar system
[00:48:48] to do some antique segmentation.
[00:48:50] This is actually the work that Geoff
[00:48:52] was talking about that was rejected
[00:48:53] from CVPR 2011.
[00:48:55] So this is the system
[00:48:55] that could in real time
[00:48:58] using a FGA implementation segment.
[00:49:02] Basically give a category
[00:49:02] for every pixel in an image
[00:49:06] at about 30 frames per second
[00:49:08] at sort of decent resolution.
[00:49:09] It was far from perfect,
[00:49:10] but it could sort of label with sort of
[00:49:13] reasonable accuracy,
[00:49:14] detect pedestrians,
[00:49:14] detect the roads and the trees, et cetera.
[00:49:20] But the results basically
[00:49:20] were not immediately believed
[00:49:23] by the computer vision community.
[00:49:26] Now to measure the progress
[00:49:28] that has happened since then
[00:49:30] in the last 10 years essentially,
[00:49:33] this is an example of a result
[00:49:34] of a really recent system
[00:49:34] that was put together
[00:49:36] by a team at Facebook that they call
[00:49:39] the panoptic feature pyramid network.
[00:49:41] So it's basically a
[00:49:41] large convolutional net
[00:49:43] that has sort of a path
[00:49:43] that extracts features.
[00:49:47] Multi-layer pass that extracts features
[00:49:49] and then another pass that sort
[00:49:49] of generates an output image.
[00:49:51] And the output image basically identifies
[00:49:54] and generates a mask for every instance
[00:49:57] of every object in the image
[00:49:58] and tells you what category they are.
[00:50:00] So here the name of the
[00:50:00] category's on the display,
[00:50:01] but it can recognize something
[00:50:01] like a few 100 categories.
[00:50:04] People, vehicles of various kinds,
[00:50:07] and not just object categories.
[00:50:09] But also sort of background,
[00:50:12] sort of textures or regions.
[00:50:14] Thinks like grass and sand,
[00:50:17] trees and things like that.
[00:50:19] So you would imagine a system like this
[00:50:20] would be very useful for
[00:50:20] things like self driving cars
[00:50:23] if you have the complete segmentation,
[00:50:25] identification of all pixels in an image,
[00:50:27] it would make it easier to build
[00:50:29] self driving cars.
[00:50:30] Not just self driving cars,
[00:50:31] but also medical image analysis systems.
[00:50:33] So this is a relatively
[00:50:33] similar architecture.
[00:50:36] People call this U-net
[00:50:36] sometimes because of the obvious
[00:50:39] U shape of this convolutional net.
[00:50:42] Again, it has an encoded
[00:50:42] part that sort of extracts
[00:50:45] features and then a sort of the part
[00:50:48] that constructs the output image
[00:50:49] where the parts of the
[00:50:49] medical images are segmented.
[00:50:54] This is the kind of result
[00:50:54] that it's producing.
[00:50:56] This is some work by some
[00:50:56] of my colleagues at NYU.
[00:50:59] I was not involved in this work.
[00:51:01] A different sub group of colleagues
[00:51:03] with some common
[00:51:03] co-authors as Wartle so on
[00:51:06] detecting breast cancer from imaging
[00:51:09] from x-rays from mammograms.
[00:51:12] In fact, one of the most
[00:51:12] sort of hottest topics
[00:51:16] in radiology these days
[00:51:16] is using deep learning
[00:51:20] for medical vision analysis.
[00:51:22] It's probably going to effect,
[00:51:25] if not revolutionize, radiology
[00:51:27] in the next few years.
[00:51:28] It already has to some extent.
[00:51:32] Some more work along those directions.
[00:51:33] This is actually a collaboration between
[00:51:35] the NYU medical school
[00:51:35] and physical care research
[00:51:38] in accelerating the
[00:51:38] data collection for MRI.
[00:51:41] So when you go through an MRI
[00:51:43] you have to sit in the
[00:51:43] machine for about an hour,
[00:51:45] or 20 minutes, depending on the kind
[00:51:46] of exam you're going through.
[00:51:48] And this technique here using
[00:51:53] those kinds of reconstruction
[00:51:53] convolutional net
[00:51:56] allows to basically reduce
[00:51:56] the data collection time
[00:52:00] and get images that are
[00:52:00] essentially of the same quality.
[00:52:04] So they will not put
[00:52:04] radiology out of jobs.
[00:52:11] But it will make the job
[00:52:11] more interesting probably.
[00:52:14] Geoff was mentioning work on translation
[00:52:17] with neural nets.
[00:52:18] This is I think a very surprising
[00:52:22] and interesting development of the fact
[00:52:24] that you can use neural
[00:52:24] nets to do translation.
[00:52:26] And there is a lot of innovation
[00:52:29] in the kind of architectures
[00:52:29] that are used for this.
[00:52:31] So Geoff talked about
[00:52:31] the attention mechanism,
[00:52:33] the transformer architecture.
[00:52:35] This is a new one called
[00:52:35] dynamic convolutions
[00:52:37] which kinda recycles a bit of those ideas.
[00:52:40] And things work really well there.
[00:52:42] Those networks are very large.
[00:52:43] They have a few hundred
[00:52:43] million parameters in them.
[00:52:46] And so, some of the challenges there is
[00:52:50] actually running them on GPUs.
[00:52:53] Having enough memory to run them.
[00:52:54] We're basically limited by
[00:52:57] GPU memory there.
[00:52:58] So those ideas of image segmentation
[00:53:00] have been used by people working
[00:53:02] on self driving cars.
[00:53:03] Particularly people at MobilEye going,
[00:53:07] which is now Intel going
[00:53:07] back several years.
[00:53:10] The first convolutional nets I think
[00:53:12] that were deployed for self driving cars
[00:53:14] or for driving assistance were
[00:53:14] in the 2015 Tesla S model.
[00:53:19] NVIDIA has devoted a large sort of efforts
[00:53:22] also to self driving cars.
[00:53:24] And so there's a lot of
[00:53:24] interesting things going on there.
[00:53:26] But progress is,
[00:53:30] I wouldn't say slow,
[00:53:32] but to completely autonomous
[00:53:32] driving is a hard problem.
[00:53:35] It's not as easy as
[00:53:35] people thought initially.
[00:53:38] Okay, so Geoff kinda brushed away
[00:53:42] reinforcement learning.
[00:53:43] But reinforcement learning is something
[00:53:44] that a lot of people are
[00:53:44] really excited about.
[00:53:46] Particularly people at Deep Mind.
[00:53:48] But there is a problem
[00:53:48] with the current crop
[00:53:50] of reinforcement learning.
[00:53:51] Which is that it's
[00:53:51] extremely data inefficient.
[00:53:53] If you want to train a
[00:53:53] system to do anything
[00:53:55] using reinforcement learning,
[00:53:57] it will have to do lots and
[00:53:57] lots of trial and errors.
[00:54:00] So for example, to get a
[00:54:00] machine to play Atari games,
[00:54:03] classic Atari games,
[00:54:04] to the level that any human can reach
[00:54:07] in about 15 minutes of training,
[00:54:09] the machine will have
[00:54:09] to play the equivalent
[00:54:12] of 80 hours of real time play.
[00:54:16] To play Go at superhuman level,
[00:54:20] it will have to play something
[00:54:20] like 20 million games.
[00:54:24] To play StarCraft.
[00:54:25] This is a recent Deep Mind work,
[00:54:29] it's a blog post, not a paper,
[00:54:30] the AlphaStar system took the equivalent
[00:54:34] of 200 years of real time play
[00:54:36] to reach human level,
[00:54:39] on a single map for kind
[00:54:39] of a single type of player.
[00:54:43] By the way, all those systems use ConvNets
[00:54:45] and various other things.
[00:54:46] But that's an interesting thing.
[00:54:49] So the problem with reinforcement learning
[00:54:51] is that those models have to try something
[00:54:54] to know if it's gonna work.
[00:54:56] And it's really not practical
[00:54:56] to use in the real world
[00:54:58] if you want to train a
[00:54:58] robot to grasp those things
[00:55:01] or you want to train
[00:55:01] a car to drive itself.
[00:55:04] So to figure out,
[00:55:08] to train a system to drive a car
[00:55:10] so it doesn't run off cliffs,
[00:55:12] it will actually have to try to,
[00:55:15] it will actually have to run off a cliffs
[00:55:17] multiple times before it figures out
[00:55:18] how not to do that.
[00:55:21] First of all, to figure
[00:55:21] out it's a bad idea,
[00:55:23] and second, to figure
[00:55:23] out how not to do it.
[00:55:26] Because it doesn't have
[00:55:26] a model of the world.
[00:55:27] It doesn't, it can't
[00:55:27] imagine what's gonna happen
[00:55:29] before it happens.
[00:55:30] It has to try things to correct itself.
[00:55:32] That's why it's so inefficient.
[00:55:35] So that begs the question,
[00:55:37] how is it that humans
[00:55:37] and animals can learn
[00:55:39] so efficiently, so quickly?
[00:55:40] We can learn to drive a car.
[00:55:42] Most of us can learn to drive a car
[00:55:43] in about 20 hours of training
[00:55:44] with hardly any accident.
[00:55:46] How does that happen?
[00:55:48] We don't run off cliffs because
[00:55:50] we have a pretty good
[00:55:50] intuitive physics model
[00:55:52] that tells us if I'm
[00:55:52] driving next to a cliff,
[00:55:55] and I'm turning the wheel to the right,
[00:55:57] the car is gonna run off the cliff,
[00:55:58] it's gonna fall and nothing good
[00:56:00] is gonna come out of this.
[00:56:02] So we have this internal model.
[00:56:04] And the question is how do
[00:56:04] we learn this internal model?
[00:56:06] And the next question is
[00:56:06] how do we get machines
[00:56:09] to learn internal models like that?
[00:56:11] Basically just by observation.
[00:56:14] So there is a gentlemen
[00:56:18] called Emmanual Dupoux in Paris.
[00:56:19] He's a developmental psychologist.
[00:56:22] He works actually on how
[00:56:22] children learn language
[00:56:25] and speech and things like that.
[00:56:26] But also other concepts.
[00:56:27] And he made this chart about the time,
[00:56:31] the age in months at which
[00:56:31] babies learn basic concepts.
[00:56:34] Like things like
[00:56:34] distinguishing animate objects
[00:56:37] from inanimate objects.
[00:56:38] That happens really quickly
[00:56:38] around three months old.
[00:56:41] The fact that some objects are stable,
[00:56:44] some of them will fall,
[00:56:46] and you can sort of measure whether babies
[00:56:48] are surprised by the
[00:56:48] behavior of some objects.
[00:56:52] And then it takes about nine months
[00:56:54] for babies to figure out that objects
[00:56:56] that are not supported will fall.
[00:56:58] Basically gravity.
[00:57:00] So if you show a six month old baby
[00:57:05] the scenario on the top left
[00:57:08] where there's a little car and a platform
[00:57:10] and you push the little
[00:57:10] car off the platform,
[00:57:11] and the car doesn't fall,
[00:57:13] it's a trick.
[00:57:14] Babies at six months old
[00:57:14] don't even pay attention.
[00:57:16] That's just another thing that the world
[00:57:19] throws at them that they
[00:57:19] have to learn, it's fine.
[00:57:23] A nine month old baby will go
[00:57:24] like the little girl at the bottom left.
[00:57:28] Be very, very surprised.
[00:57:29] In the meantime they've
[00:57:29] learned the concept of gravity.
[00:57:33] And nobody has really
[00:57:33] told them what gravity is.
[00:57:35] They've just kind of observed the world
[00:57:37] and they figured out that objects
[00:57:38] that are not supported just fall.
[00:57:39] And so when that doesn't happen,
[00:57:40] they get surprised.
[00:57:43] How does that happen?
[00:57:45] It's not just humans.
[00:57:46] Animals have those models too.
[00:57:47] You know cats, dogs, rats, orangutans.
[00:57:52] So here's a video.
[00:57:53] The orangutan here is
[00:57:53] being shown a magic trick.
[00:57:55] Put an object in a cup.
[00:57:58] Remove the object, but
[00:57:58] he doesn't see that.
[00:58:00] Then show the cup.
[00:58:03] It's empty.
[00:58:05] He rolls on the floor laughing.
[00:58:06] (audience laughing)
[00:58:08] So his model of the world was violated.
[00:58:12] He has a pretty good model of the world.
[00:58:13] Object permanence.
[00:58:14] That's a very basic concept.
[00:58:15] Objects are not supposed
[00:58:15] to disappear like that.
[00:58:19] And when your model of the
[00:58:19] world is being violated,
[00:58:23] you pay attention because
[00:58:23] you're gonna learn something
[00:58:25] about the world you didn't know.
[00:58:28] If it reevaluates a very
[00:58:28] basic thing about the world,
[00:58:31] it's funny.
[00:58:33] But it also, it might be dangerous.
[00:58:36] It's something that can kill you
[00:58:37] 'cause you just didn't
[00:58:37] predict what just happened.
[00:58:41] Okay, so what's the salvation?
[00:58:42] Really, how do we get
[00:58:42] machines to learn this
[00:58:44] kind of stuff?
[00:58:46] You know, learn all the huge
[00:58:46] amount of background knowledge
[00:58:48] we learn about the world by just observing
[00:58:50] in the first few months of life.
[00:58:52] And animals do this too.
[00:58:54] So for example, if I ask you,
[00:58:58] if I train myself to predict
[00:58:59] what the world is gonna look like
[00:59:01] when I move my head slightly to the left,
[00:59:04] because of parallel motion,
[00:59:07] objects that are nearby
[00:59:09] and objects that are faraway
[00:59:10] won't move the same way relative
[00:59:13] to my viewpoint.
[00:59:17] And so the best way to
[00:59:17] predict how the world
[00:59:21] is gonna look when I move my head,
[00:59:23] is to basically represent internally
[00:59:26] the notion of depth.
[00:59:29] And consequently, sort of conversely,
[00:59:32] if I train a system to predict
[00:59:34] what the world is gonna look like
[00:59:36] when it moves its camera,
[00:59:37] maybe it's gonna learn the
[00:59:37] notion of depth automatically.
[00:59:40] And once you have depth, you have objects,
[00:59:42] because you have objects
[00:59:42] in front of others.
[00:59:43] You have occlusion edges.
[00:59:45] Once you have objects,
[00:59:45] you have things you can influence.
[00:59:48] And things that can move
[00:59:48] independently of others
[00:59:50] and things like that.
[00:59:51] So concepts can kind of build
[00:59:51] on top of each other like this
[00:59:54] through prediction.
[00:59:57] So that's the idea of
[00:59:57] self supervised learning.
[00:59:59] It's prediction and reconstruction.
[01:00:01] I give the machine a piece of data.
[01:00:05] Let's say a video clip.
[01:00:06] I mask a piece of that video clip
[01:00:08] and I ask the system to
[01:00:08] predict the missing part
[01:00:11] from the part that it can observe.
[01:00:14] Okay so that would be video prediction.
[01:00:15] Just predict the future.
[01:00:18] But the more general form
[01:00:18] of self supervised learning
[01:00:20] is I don't specify in advance which part
[01:00:22] I'm gonna mask or not,
[01:00:23] I'm just gonna tell the system
[01:00:23] I'm gonna mask a piece of it,
[01:00:26] and whatever is masked,
[01:00:27] I'm asking you to reconstruct it.
[01:00:31] And in fact, I may not
[01:00:31] even mask it at all.
[01:00:34] I'm just gonna virtually mask it
[01:00:36] and just ask the system
[01:00:36] to reconstruct the input
[01:00:39] under certain constraints.
[01:00:41] So the advantage of this
[01:00:41] self supervised learning
[01:00:42] is that it's not task dependent.
[01:00:44] You get the machine to
[01:00:44] learn about the world
[01:00:45] without training it for a particular task.
[01:00:48] And so it can learn just by observation
[01:00:49] without having to interact with the world,
[01:00:51] which is a bit more efficient.
[01:00:52] But more importantly,
[01:00:53] you're asking the system
[01:00:53] to predict a lot of stuff.
[01:00:56] Not just a value function like
[01:00:56] in reinforcement learning,
[01:01:00] where basically the only thing you
[01:01:01] give the machine to predict
[01:01:02] is a scale or value once in a while.
[01:01:06] Not supervised learning
[01:01:08] where you ask the system
[01:01:08] to predict a label,
[01:01:10] which is a few bits.
[01:01:12] In the case of self supervised learning
[01:01:13] you're asking the machine
[01:01:13] to predict a lot of stuff.
[01:01:18] And so that led me to this
[01:01:18] slightly obnoxious analogy,
[01:01:21] at least for people who work
[01:01:21] on reinforcement learning,
[01:01:23] which is the idea that if intelligence
[01:01:25] or learning is a cake,
[01:01:28] the bulk of the cake, the genoise
[01:01:30] as we say in French is really
[01:01:30] self supervised learning.
[01:01:33] Most of what we learn,
[01:01:34] most of the knowledge we
[01:01:34] accumulate about the world
[01:01:36] is learned through self
[01:01:36] supervised learning.
[01:01:39] This little bit of icing on the cake,
[01:01:41] which is supervised learning.
[01:01:42] We're being showed a picture book
[01:01:43] and we're being told the name of objects,
[01:01:46] and with just a few examples,
[01:01:47] we can know what the objects are.
[01:01:50] We're taught the meaning of some words
[01:01:53] and babies can learn,
[01:01:56] young children can learn
[01:01:56] many, many words per day.
[01:02:01] New words.
[01:02:02] And then the cherry on the
[01:02:02] cake is reinforcement learning.
[01:02:04] It's a very small amount of information
[01:02:06] you're asking the machine to predict.
[01:02:07] And so there's no way
[01:02:07] that the machine can learn
[01:02:10] purely from that form of learning.
[01:02:12] It has to be a combination of
[01:02:16] probably all three forms of learning,
[01:02:17] but principally self supervised learning.
[01:02:20] This idea is not new.
[01:02:22] A lot of people have argued
[01:02:22] for the idea of prediction
[01:02:24] for learning.
[01:02:26] The idea of learning models,
[01:02:28] predictive models.
[01:02:30] And one such person is Geoff
[01:02:34] as a matter of fact.
[01:02:35] This is a quote from him,
[01:02:37] which this is from a few years ago,
[01:02:39] but he's been saying
[01:02:39] this for about 40 years.
[01:02:42] At least for longer than I've known him.
[01:02:46] And it goes like this.
[01:02:47] "The brain has about
[01:02:47] 10 to the 14th synapses
[01:02:49] "and we only live about
[01:02:49] 10 to the nine seconds.
[01:02:52] "So we have a lot more
[01:02:52] parameters than data.
[01:02:54] "This motivates the idea that we must
[01:02:56] "do a lot of unsupervised learning
[01:02:57] "or self supervised learning
[01:02:57] since the perceptual
[01:02:59] "input including proprioception
[01:02:59] is the only place
[01:03:02] "where we can get 10 to the 15 dimensions
[01:03:04] "of constraint per second."
[01:03:06] If you're asked to predict everything
[01:03:08] that comes into your senses,
[01:03:12] every fraction of a second,
[01:03:14] that's a lot of information
[01:03:14] you have to learn.
[01:03:15] And that might be enough to constrain
[01:03:18] all the synapses we have in
[01:03:18] our brain to learn things
[01:03:20] that are meaningful.
[01:03:23] So the sequel of deep
[01:03:23] learning in my opinion
[01:03:27] is self supervised learning.
[01:03:28] And in fact, historically
[01:03:28] as Geoff mentioned,
[01:03:31] the sort of deep learning conspiracy
[01:03:34] that Yoshua, Geoff and I
[01:03:34] started in the early 2000s
[01:03:39] was focused on unsupervised learning,
[01:03:41] unsupervised speech training.
[01:03:43] And it was partly successful.
[01:03:44] But we kind of put it
[01:03:47] on the back burner for a while.
[01:03:49] And it's coming back to the fore now.
[01:03:51] It's gonna create a new revolution.
[01:03:52] At least that's my prediction.
[01:03:54] And the next, the revolution
[01:03:54] will not be supervised.
[01:03:58] So I have to thank Alyosha
[01:03:58] Efros for this slogan.
[01:04:02] He invented it.
[01:04:04] Of course he got inspired
[01:04:04] by Gil Scott Heron,
[01:04:06] the revolution will not be televised.
[01:04:09] You can even get a t-shirt with it now.
[01:04:14] So what is self supervised
[01:04:14] learning really?
[01:04:16] Self supervised learning
[01:04:16] is filling in the blanks.
[01:04:19] And it works really well for
[01:04:19] natural language processing.
[01:04:22] So in natural language processing,
[01:04:24] a method that has become
[01:04:24] standard over the last year,
[01:04:27] in models like Burt and others is
[01:04:29] you take a long sequence
[01:04:29] of words extracted
[01:04:33] from a corpus of text,
[01:04:35] you blank out some
[01:04:35] proportion of the words.
[01:04:40] And you train a very large neural net
[01:04:42] based on those transformer architectures
[01:04:43] or various other architectures
[01:04:45] to predict the missing words.
[01:04:47] And in fact, it cannot exactly
[01:04:47] predict the missing words,
[01:04:49] so you're asking it to
[01:04:49] predict the distribution
[01:04:51] over the entire vocabulary
[01:04:51] for the probability
[01:04:54] that each word may occur
[01:04:54] at those locations.
[01:05:00] So that's called,
[01:05:01] that's a special case of what we call
[01:05:02] a masked auto encoder.
[01:05:04] Give it an input, ask it to reconstruct
[01:05:06] this part of input that is not present.
[01:05:09] People have been trained
[01:05:09] to do this in the context
[01:05:11] of image recognition as well.
[01:05:12] There's various attempts at doing this.
[01:05:14] So this is work from Pathak, et al
[01:05:17] from a few years ago where you blank
[01:05:19] out some pieces of an image
[01:05:20] and then you ask the
[01:05:20] system to fill them in.
[01:05:23] And it's only partially successful.
[01:05:24] Not nearly as successful
[01:05:26] as in the context of
[01:05:26] natural language processing.
[01:05:28] So natural language processing,
[01:05:30] there's been a revolution
[01:05:30] over the last year
[01:05:32] of using those pre-training systems
[01:05:34] for natural language,
[01:05:36] understanding translation,
[01:05:37] all kinds of stuff.
[01:05:38] And the performance is amazing.
[01:05:39] They're very, very big models.
[01:05:41] But the performance
[01:05:41] really works really well.
[01:05:42] And there were sort of
[01:05:42] early indications of this
[01:05:45] in work that Yoshua Bengio
[01:05:45] did a long time ago in the 90s
[01:05:51] and Milan Colevent, and
[01:05:51] Weston did around 2010
[01:05:58] using neural nets for an LP.
[01:06:00] And then more recent work,
[01:06:01] Word2vec, FastText, et cetera
[01:06:02] I would choose this
[01:06:02] idea of predicting words
[01:06:04] from the context basically.
[01:06:06] But really sort of, this whole
[01:06:06] idea is completely taken off.
[01:06:10] So why does it work for
[01:06:10] natural language processing
[01:06:13] and why does it not work so well
[01:06:16] in the context of images and vision?
[01:06:19] I think it's because of the sort of,
[01:06:22] how we represent uncertainty
[01:06:24] or how we do not represent uncertainty.
[01:06:27] So let's say we want
[01:06:27] to do video prediction.
[01:06:29] We have short video clips
[01:06:32] with a few frames.
[01:06:33] In this case here, a little girl
[01:06:34] approaching a birthday cake.
[01:06:36] And then we asked the machine to predict
[01:06:38] the next few frames in the video.
[01:06:40] If you train a large neural net to predict
[01:06:43] the next few frames
[01:06:44] using least squared error,
[01:06:46] what you get are blurry predictions.
[01:06:50] Why?
[01:06:51] Because the system cannot exactly predict
[01:06:53] what's gonna happen and so it,
[01:06:55] the best it can do is predict the average
[01:06:57] of all the possible futures.
[01:06:59] To be more concrete,
[01:07:00] let's say all the videos consist
[01:07:01] of someone putting a pen on the table
[01:07:03] and letting it go
[01:07:04] and every time you repeat the experiment,
[01:07:05] the pen falls in a different direction.
[01:07:07] And you can't really
[01:07:07] predict in which direction
[01:07:09] it's gonna fall.
[01:07:10] Then if you predict the average
[01:07:12] of all the outcomes,
[01:07:12] it would be a transparent pen
[01:07:16] superimposed on itself in
[01:07:16] all possible orientations.
[01:07:19] That's not a good prediction.
[01:07:22] So if you want the system to be able
[01:07:25] to represent multiple predictions,
[01:07:28] it has to have what's
[01:07:28] called a latent variable.
[01:07:30] So you have a function
[01:07:30] implemented by neural net.
[01:07:33] It takes the past let's say
[01:07:33] a few frames from a video,
[01:07:36] and it wants to predict
[01:07:36] the next few frames.
[01:07:38] It has to have an extra variable,
[01:07:40] here it's called Z,
[01:07:41] so that when you vary this variable,
[01:07:43] the output varies over a particular set
[01:07:44] of possible predictions.
[01:07:47] Okay, that's called a
[01:07:47] latent variable model.
[01:07:49] The problem with training those things
[01:07:50] is that there's basically
[01:07:50] only two ways of training them
[01:07:53] that we know about.
[01:07:54] Or two kind of families of ways
[01:07:58] to train those systems.
[01:07:59] One is a very cool idea
[01:08:02] from Ian Goodfellow and his collaborators
[01:08:04] at University of Montreal a few years ago
[01:08:05] called adversarial training.
[01:08:06] Or generative adversarial networks.
[01:08:09] And the idea of GANs,
[01:08:13] generative adversarial networks,
[01:08:13] is to train the second neural net
[01:08:15] to tell the first neural net whether
[01:08:16] it's prediction is on this manifold
[01:08:18] or set of plausible futures or not.
[01:08:21] And you train those two
[01:08:21] networks simultaneously.
[01:08:26] There's another technique that consist in
[01:08:28] sort of inferring what the ideal value
[01:08:30] of the latent variable would be
[01:08:31] to make a good prediction.
[01:08:33] But if you do this,
[01:08:34] you have the danger
[01:08:34] that the latent variable
[01:08:36] would capture all the information there is
[01:08:38] to capture about the prediction,
[01:08:41] and no information will actually be used
[01:08:43] from the past to make that prediction.
[01:08:46] So you have to regularize
[01:08:46] this latent variable.
[01:08:48] Okay, so those ideas of things like
[01:08:53] adversarial training work really well.
[01:08:55] So what you see here at the bottom
[01:08:56] is a video prediction for a short clip
[01:08:59] where the system has been trained
[01:09:00] with this adversarial training.
[01:09:02] And there are various ways
[01:09:02] of doing those predictions.
[01:09:05] Not just in pixel space,
[01:09:06] but also in the space of objects
[01:09:08] that have been already segmented.
[01:09:11] Those adversarial generative
[01:09:11] adversarial networks
[01:09:13] can generate images
[01:09:15] that are used for kind of assistance
[01:09:18] to sort of artistic production.
[01:09:19] So these are non-existing faces.
[01:09:22] You have a system here
[01:09:22] that has been trained
[01:09:23] to produce an image that looks like
[01:09:26] a celebrity and after
[01:09:26] the system is trained,
[01:09:29] you feed it a few 100 random numbers,
[01:09:31] and out comes a face that doesn't exist.
[01:09:35] And they look pretty good.
[01:09:36] This is work by NVIDIA
[01:09:37] from this year actually it
[01:09:37] was presented this year.
[01:09:41] You can use this to produce all kinds
[01:09:43] of different things.
[01:09:44] Like you know,
[01:09:47] clothing for example.
[01:09:48] Training on a collection of
[01:09:52] clothes from a famous designer.
[01:09:55] So I think we need sort of new ways
[01:09:57] of sort of formulating this problem
[01:10:00] of unsupervised learning
[01:10:01] so that our systems can
[01:10:01] deal with this uncertainty
[01:10:05] in the prediction in the context
[01:10:06] of continuous high dimensional spaces.
[01:10:09] We don't have the problem in the context
[01:10:13] of natural language processing,
[01:10:16] because it's easy to represent
[01:10:16] a distribution of our words,
[01:10:19] it's just a discrete distribution.
[01:10:20] It's a long vector of numbers
[01:10:22] between zero and one that's sum to one.
[01:10:24] But it's very hard in continuous
[01:10:24] high dimensional spaces.
[01:10:28] And so we need new techniques for this.
[01:10:29] And one technique I'm proposing
[01:10:30] is something called energy
[01:10:30] based self supervised learning.
[01:10:33] Which is imagine that your world
[01:10:36] is two dimensional.
[01:10:37] You only have two input variables,
[01:10:38] two sensors,
[01:10:39] and your entire world,
[01:10:42] your entire training set
[01:10:42] is composed of those dots
[01:10:44] here in this two dimensional space.
[01:10:46] What you'd like is to train
[01:10:49] a contrast function,
[01:10:50] let's call it an energy
[01:10:51] that gives low energy to points
[01:10:53] that are on the manifold of data.
[01:10:56] And higher energy outside.
[01:10:58] There is basically a lot
[01:10:58] of research to do there
[01:11:01] to find the best method to do this.
[01:11:04] My favorite one is what I call
[01:11:05] regularized latent variable models.
[01:11:06] And we had some success about 10 years ago
[01:11:09] in using techniques of this type
[01:11:10] for learning features
[01:11:10] in a convolutional net,
[01:11:12] completely unsupervised.
[01:11:14] What you see on the left here
[01:11:15] is animation of a system that learns
[01:11:19] basically oriented filters
[01:11:19] by just being trained
[01:11:21] with natural image patches to reconstruct
[01:11:23] those under sparsity constraints.
[01:11:26] And what you see on the right is
[01:11:28] filters of the convolutional net
[01:11:29] that are learned in the same,
[01:11:32] with the same algorithm
[01:11:33] with different numbers of filters.
[01:11:35] Those things kinda work.
[01:11:37] They don't beat supervised learning
[01:11:38] if you have tons of data.
[01:11:40] But the hope is that they will reduce
[01:11:42] the amount of necessary label data.
[01:11:45] So I'm gonna end with an example
[01:11:48] of how to combine all
[01:11:48] those to get a machine
[01:11:50] to learn something
[01:11:53] useful like a task, a motor task.
[01:11:57] So here what I'm talking about is
[01:11:59] can we train a machine to learn to drive
[01:12:02] by just observing other people driving?
[01:12:06] And by training a model
[01:12:08] of what goes on in the world?
[01:12:11] So you are in your car.
[01:12:14] You can see all the cars around you.
[01:12:15] And if you can predict
[01:12:15] what the cars around you
[01:12:17] are gonna do ahead of time,
[01:12:20] then you can drive defensively basically.
[01:12:22] You can decide to stay away from this car
[01:12:24] because you see it swerving.
[01:12:26] You can decide to kinda slow down
[01:12:29] because the car in front of you
[01:12:30] is likely to slow down 'cause
[01:12:32] there's another car in front of it
[01:12:33] that is slowing down.
[01:12:34] So you have all those predictive models
[01:12:36] that basically keep you safe
[01:12:38] and you sort of learn to
[01:12:38] integrate them over time.
[01:12:40] You don't even have to think about it.
[01:12:42] It's just in your sort
[01:12:42] of reflexes of driving.
[01:12:45] You can talk at the same time.
[01:12:47] And your work.
[01:12:52] But the way to train a system like this
[01:12:53] is you first have to
[01:12:53] train a forward model.
[01:12:55] So forward model would be
[01:12:57] here is the state of the world at time T,
[01:12:59] give me a prediction about
[01:12:59] the state of the world
[01:13:01] at time T plus one.
[01:13:03] And the problem with this of course
[01:13:04] is the world is not deterministic.
[01:13:07] There's a lot of things that could happen.
[01:13:08] So it's the same problem
[01:13:08] that I was talking about
[01:13:10] with a pen,
[01:13:11] many things can happen.
[01:13:14] But if you had such a forward model,
[01:13:16] you could run the forward
[01:13:16] model multiple time steps.
[01:13:21] And then if you had an objective function
[01:13:23] like how far you are from the other cars,
[01:13:26] whether you are in lane,
[01:13:27] things like this,
[01:13:28] you could backpropagate
[01:13:28] gradient with this entire system
[01:13:31] to train a neural net
[01:13:31] to predict the correct
[01:13:34] course of action that would
[01:13:34] be safe over the long run.
[01:13:39] And this can be done
[01:13:39] completely in your head.
[01:13:41] If you have a forward model in your head,
[01:13:42] you don't have to actually drive
[01:13:44] to train yourself to drive,
[01:13:45] you can just imagine all of those things.
[01:13:51] So that's a specific example.
[01:13:52] So put a camera looking down at a highway.
[01:13:56] It follows every car and it
[01:13:56] extracts a little rectangle
[01:13:59] around every car that follows every car
[01:14:01] that you see at the bottom.
[01:14:02] And what you're doing
[01:14:02] now is you're training
[01:14:05] a convolutional net to take a few frames
[01:14:08] centered on a particular car
[01:14:10] and predict the next state of the world.
[01:14:13] And if you do this,
[01:14:17] you get, oops, sorry.
[01:14:25] You get the second column.
[01:14:27] So the column on the left is what happens
[01:14:29] in the real world.
[01:14:30] The second column is what happens if you
[01:14:32] just train a convolutional
[01:14:32] net with Z squared
[01:14:34] to predict what's gonna happen.
[01:14:35] It can only predict the
[01:14:35] average of all the possible
[01:14:37] futures, and so you
[01:14:37] get blurry predictions.
[01:14:40] If you now transform the model so that it
[01:14:41] has a latent variable that allows it to
[01:14:43] take into account the uncertainty about
[01:14:45] the world.
[01:14:46] And I'm not going to explain
[01:14:46] exactly how that works.
[01:14:48] Then you get the prediction
[01:14:48] that you just saw
[01:14:52] on the right
[01:14:53] where for every drawing
[01:14:53] of this latent variable
[01:14:57] you get different predictions,
[01:14:58] but they are crisp.
[01:15:00] Okay, so now what you can do is
[01:15:02] you can to do this training
[01:15:04] I was telling you about earlier,
[01:15:06] you sample the certain variables
[01:15:07] so you get possible scenarios
[01:15:09] about what's gonna happen in your future.
[01:15:11] Then through backpropagation
[01:15:11] you train your policy network
[01:15:14] to get your system to drive.
[01:15:16] And if you do this, it doesn't work.
[01:15:18] It doesn't work because the
[01:15:18] system goes into regions
[01:15:21] of the state space where the forward model
[01:15:23] is very inaccurate and very uncertain.
[01:15:26] So what we have to do is add another term
[01:15:28] in the objective function
[01:15:30] that prevents the system from going into
[01:15:31] parts of the space where it doesn't,
[01:15:33] where it's predictions are bad.
[01:15:35] Okay, so it's like an inverse curiosity
[01:15:38] constraint if you want.
[01:15:40] And if you do this, it works.
[01:15:41] So these are examples of,
[01:15:44] the blue car is driving itself.
[01:15:45] The little white dot indicates
[01:15:46] whether it accelerates, whether it brakes,
[01:15:47] or whether it turns.
[01:15:48] And it kinda keeps itself safe
[01:15:50] away from the other cars.
[01:15:51] The other cars can't see it.
[01:15:53] The blue car is invisible here.
[01:15:55] Let me show you another example here.
[01:15:58] So here the yellow car is the actual car
[01:16:00] in the video.
[01:16:01] The blue car is what the agent here
[01:16:03] that's been trained is doing.
[01:16:05] And it's being squeezed between two cars
[01:16:06] so it has to escape because
[01:16:06] the other cars don't see it.
[01:16:10] So it has to squeeze out.
[01:16:13] But it works.
[01:16:14] It works reasonably well.
[01:16:15] And basically that system has never
[01:16:19] interacted with the real world.
[01:16:20] It's just watched other people drive.
[01:16:24] And then ensues that for training
[01:16:26] its actions plans.
[01:16:28] Basically it's policy.
[01:16:30] Okay, now I'm gonna go a little
[01:16:32] philosophical if you want.
[01:16:36] There is, throughout history
[01:16:36] of technology and science,
[01:16:39] there's been this phenomenon.
[01:16:40] It's not universal,
[01:16:41] but it's pretty frequent
[01:16:43] where people invent an artifact
[01:16:45] and then derive science
[01:16:45] out of this artifact
[01:16:47] to explain how this artifact works
[01:16:50] or to kind of figure out its limitations.
[01:16:53] So a good example is the
[01:16:53] invention of the telescope
[01:16:56] in the 1600s.
[01:16:57] Optics was not developed
[01:16:57] until at least 50 years later.
[01:17:02] But people had a good intuition
[01:17:03] of how to build telescopes before that.
[01:17:06] The steam engine was
[01:17:06] invented in late 1600,
[01:17:08] early 1700s,
[01:17:10] and thermodynamics was, came
[01:17:10] out more than 100 years later.
[01:17:14] Basically designed to explain
[01:17:16] the limitations of thermal engines.
[01:17:19] And thermodynamics now is the foundation
[01:17:21] of one of the most fundamental
[01:17:23] integral for construction of all science.
[01:17:26] So it was purposely defined to explain
[01:17:29] a particular artifact.
[01:17:31] That's very interesting.
[01:17:33] Same thing with electromagnetism
[01:17:35] and electrodynamics.
[01:17:36] With the invention of
[01:17:36] sailboats and airplanes,
[01:17:38] and aerodynamics.
[01:17:42] Invention of compounds and chemistry
[01:17:44] to explain, et cetera, right?
[01:17:46] Computer science came after
[01:17:48] the invention of computers, right?
[01:17:51] Information theory came
[01:17:51] after the invention
[01:17:53] of first digital communication
[01:17:56] through radio and teletype
[01:17:56] and things like that.
[01:17:59] So it's quite possible that now we have
[01:18:03] in the next few decades,
[01:18:04] we'll have empirical systems
[01:18:06] that are built by trial and error,
[01:18:09] perhaps by systematic optimization
[01:18:11] on powerful machines.
[01:18:13] Perhaps by intuitions.
[01:18:14] By empirical work.
[01:18:17] Perhaps with a little bit of theory.
[01:18:19] Perhaps a lot of theory hopefully.
[01:18:22] And the question is whether this will lead
[01:18:24] to a whole theory of intelligence.
[01:18:28] The fact that we can build an artifact
[01:18:30] that is intelligent might
[01:18:30] lead to a general theory
[01:18:33] of information processing
[01:18:33] and intelligence.
[01:18:37] And that's kind of a big hope.
[01:18:40] I'm not sure this is gonna be realized
[01:18:42] over the next few decades,
[01:18:43] but that's a good program.
[01:18:46] A word of caution
[01:18:48] about biological inspiration.
[01:18:49] So neural nets are biologically inspired.
[01:18:51] Convolutional nets are
[01:18:51] biologically inspired.
[01:18:52] But they're just inspired,
[01:18:53] they're not copied.
[01:18:55] Let me give you a story of a gentlemen
[01:18:57] called Clement Ader.
[01:18:59] Is there any French
[01:18:59] people in the room here?
[01:19:01] Okay, can you raise your
[01:19:01] hand, French people?
[01:19:04] No French people.
[01:19:05] Yeah, okay a couple.
[01:19:06] Have you heard of Clement Ader?
[01:19:09] Never heard of Clement Ader.
[01:19:11] Yeah, you have, okay.
[01:19:12] Is there anyone who is not French
[01:19:14] who have heard of Clement Ader?
[01:19:17] Okay, one person, two persons.
[01:19:20] Basically nobody.
[01:19:21] You guys have no idea who he is.
[01:19:22] Okay.
[01:19:23] So this guy built in the late 1800
[01:19:27] a bat shaped airplane, steam powered.
[01:19:30] He was a steam engine designer.
[01:19:32] And his airplane actually took off
[01:19:35] on its own power 13 years
[01:19:35] before the Wright brothers.
[01:19:39] Flew for about 50 meters at
[01:19:39] about 50 centimeters altitude
[01:19:42] and then kinda crashed, landed.
[01:19:45] It was basically uncontrollable.
[01:19:48] So basically the guy just copied bats
[01:19:50] and just assumed that because
[01:19:51] it has the shape of a bat,
[01:19:52] it would just fly.
[01:19:55] That seemed a little bit naive.
[01:19:56] It was not naive at all
[01:19:57] but it was, it kinda stuck
[01:19:59] a little bit too close to biology
[01:20:00] and got sort of hypnotized
[01:20:00] by it a little bit.
[01:20:03] And didn't do things like build a model
[01:20:06] or a glider or a kite
[01:20:09] or you know, a wind tunnel
[01:20:11] like the Wright brothers did.
[01:20:14] So he stuck a little too close to biology.
[01:20:16] On the other hand,
[01:20:17] he had a big legacy which is that
[01:20:20] his second airplane
[01:20:20] was called the L'Avion.
[01:20:22] And that's actually the word in French,
[01:20:24] Spanish, and Portuguese for airplane.
[01:20:27] So he had some legacy.
[01:20:30] But he was kind of a secretive guy.
[01:20:31] This was before the open source days.
[01:20:33] And so, this is why
[01:20:33] you never heard of him.
[01:20:37] Thank you very much.
[01:20:39] (audience clapping)
[01:20:47] - Thank you.
[01:20:49] Thank you Geoff.
[01:20:51] Thank you Yann.
[01:20:52] We have, can we get the
[01:20:52] house lights on please?
[01:20:55] We have two microphones up
[01:20:56] and we have time for
[01:20:56] a couple of questions.
[01:20:59] House lights on please.
[01:21:02] I know they came on earlier.
[01:21:04] (audience laughing)
[01:21:06] Yes, so well first,
[01:21:06] let's give Yann and Geoff
[01:21:10] a round of applause
[01:21:10] for an amazing, amazing talk.
[01:21:12] (audience clapping)
[01:21:21] A little piece of trivia while someone
[01:21:23] comes up to the microphone.
[01:21:25] Alan Turing's birthday
[01:21:25] was June 23rd, 1912.
[01:21:29] So today is the 107th birth anniversary.
[01:21:33] And so it's very appropriate that we
[01:21:34] had this memorable Turing lecture today.
[01:21:37] Okay, question.
[01:21:42] Yeah.
[01:21:43] - [Woman] Hi thank you both.
[01:21:45] I'm really interested in the work
[01:21:46] on understanding reasoning.
[01:21:48] Can you give us a little taste of what
[01:21:50] you're thinking there?
[01:21:52] The reasoning of how neural nets reason.
[01:21:55] - Okay, so
[01:21:58] neural nets are pretty
[01:21:58] good at things you do
[01:22:00] in parallel in a hundred milliseconds.
[01:22:04] So far they're not so good
[01:22:05] at things you do over longer time periods.
[01:22:07] And in particular, one thing
[01:22:10] that people criticize neural nets for
[01:22:12] is they can't do recursion.
[01:22:14] So when we understand a sentence,
[01:22:17] we can off into a relative clause,
[01:22:19] and understand the relative clause.
[01:22:20] And we devote all our effort
[01:22:22] to understanding that relative clause
[01:22:24] and then come back again.
[01:22:25] And that kind of thing
[01:22:27] we're just beginning to be able to do
[01:22:28] with neural nets.
[01:22:30] So people at Facebook
[01:22:30] have done lots of that.
[01:22:32] People at Google are doing it.
[01:22:34] But in order to do things like that,
[01:22:37] you need some kind of memory.
[01:22:38] The typical thing to use in a neural net
[01:22:40] is you just have another bank of neurons,
[01:22:43] which are copies of
[01:22:43] neurons you already have.
[01:22:45] But that's not biologically plausible.
[01:22:48] So I always want something
[01:22:48] that's biologically plausible.
[01:22:51] And in the brain
[01:22:53] it seemed much more
[01:22:53] likely that this memory
[01:22:56] is not copies of neural activities,
[01:22:58] it's an associative memory
[01:22:59] that can recreate neural activities.
[01:23:02] But it's one that's just
[01:23:02] used for temporary things.
[01:23:06] - There's actually quite
[01:23:06] a lot of work on this
[01:23:07] on sort of trying to sort of fill the gap
[01:23:10] of neural nets not being able
[01:23:12] to do long chains of reasoning.
[01:23:14] So there's one question that
[01:23:17] Geoff has been sort of advocating for
[01:23:18] for a long time is the fact that
[01:23:21] if you have sort of classical
[01:23:21] logic based reasoning,
[01:23:25] it's discrete,
[01:23:26] therefore incompatible with
[01:23:26] gradient based learning.
[01:23:29] And so, how can you do
[01:23:29] reasoning with vectors
[01:23:32] by replacing symbols by vectors
[01:23:34] and replacing logic by
[01:23:34] continuous functions.
[01:23:37] Basically prime continuous functions.
[01:23:40] And then if you want
[01:23:40] long chains of reasoning,
[01:23:42] you need to have a working memory.
[01:23:43] So Geoff was kinda mentioning one idea
[01:23:45] using fast weights,
[01:23:46] there's a lot of people working
[01:23:47] on what's called memory networks.
[01:23:48] So you have basically what amounts
[01:23:51] to a recurrent net which can access
[01:23:52] the separate neural net
[01:23:52] which is also differentiable
[01:23:54] but it's built,
[01:23:55] the particular architecture of that
[01:23:57] turns it into an associative
[01:23:57] memory basically.
[01:24:00] And those kind of work in simple cases.
[01:24:02] They haven't really been scaled up
[01:24:03] to big problems.
[01:24:05] But there is very interesting work
[01:24:07] on basically neural nets that
[01:24:10] do not directly compute an answer.
[01:24:13] But they produce a neural net
[01:24:16] which is designed to answer the question
[01:24:18] that's being asked.
[01:24:19] So visual question answering
[01:24:21] is a typical example of this.
[01:24:22] You show a complex image to a system,
[01:24:24] and you ask it
[01:24:26] "Is there a Chinese
[01:24:26] theater that is larger than
[01:24:30] "the two cubes in this picture?"
[01:24:32] And what the neural
[01:24:32] net does is it produces
[01:24:35] another neural net which
[01:24:35] has the right module
[01:24:36] to answer that question.
[01:24:38] You can train this whole
[01:24:38] thing with backprop
[01:24:40] and it's kind of amazing
[01:24:40] that it works at all.
[01:24:42] But it works.
[01:24:44] - [Vivek] Uh, one more question.
[01:24:47] Oh sorry, yeah go ahead.
[01:24:50] - [Efram] Efram from
[01:24:50] Northeastern University.
[01:24:51] So I know many people
[01:24:51] question about neural network
[01:24:55] saying that we know neural network work.
[01:24:58] But we don't know how they works.
[01:25:00] So I wonder what's your
[01:25:00] comments on this question.
[01:25:04] - It's not really true.
[01:25:05] I mean we have some
[01:25:05] understanding of course.
[01:25:07] I mean, first of all, we have access
[01:25:08] to everything inside the machine, right?
[01:25:11] Obviously those things
[01:25:11] have hundreds of millions
[01:25:13] of parameters, hundreds of
[01:25:13] thousands of variables inside.
[01:25:16] It's gonna be complicated.
[01:25:17] It has to be complicated because
[01:25:19] we want them to solve
[01:25:19] complicated problems.
[01:25:21] So thinking that you're gonna have
[01:25:23] a complete understanding of exactly
[01:25:25] every detail is hopeless.
[01:25:27] On the other hand,
[01:25:29] I think there is quite a lot
[01:25:29] of theoretical understanding of
[01:25:31] for example, why
[01:25:31] optimization seems to work
[01:25:34] in large networks.
[01:25:36] Why the system doesn't seem to be trapped
[01:25:39] in the local mini mart for example.
[01:25:42] Or the kind of representations
[01:25:42] that are learned.
[01:25:44] - I have something to say about that too.
[01:25:45] Which is most of the things people do
[01:25:50] we don't know how they work.
[01:25:51] We have no idea how they do it.
[01:25:54] And so if you replace people
[01:25:55] by neural networks, you're no worse off
[01:25:56] than you were with people.
[01:25:58] But you're probably better off
[01:26:00] because you can direct for bias
[01:26:01] better with a neural network
[01:26:02] than you can with a person.
[01:26:04] But the other thing is there may be
[01:26:05] some tasks where you need to use
[01:26:07] hundreds of thousands of
[01:26:07] weak regularities in the data
[01:26:11] to make a prediction.
[01:26:13] And there's no simple rules.
[01:26:15] There's just lots of weak regularities.
[01:26:17] And what big neural nets do is they
[01:26:19] use them all and they say you know,
[01:26:20] 300,000 regularities say yes,
[01:26:23] and 150,000 regularities say no,
[01:26:25] so it's probably yes.
[01:26:27] And if you ask me, but how did it do it?
[01:26:30] If you're expecting to get some lines
[01:26:31] of computer code that would compute that,
[01:26:34] you're not gonna get it.
[01:26:35] This neural network has
[01:26:35] a billion weights in it
[01:26:37] and the way it did it
[01:26:37] was those billion weights
[01:26:39] have these values.
[01:26:40] And that may be the best you can get.
[01:26:42] So for that kind of decision,
[01:26:44] you're just gonna have
[01:26:44] to live with the fact
[01:26:45] that people have intuitions
[01:26:45] and their intuitions
[01:26:47] tell 'em what to do.
[01:26:48] And neural nets have intuitions too.
[01:26:50] And they work by having,
[01:26:51] the same way they do with people,
[01:26:53] by having large numbers of weights
[01:26:54] that conspire together to say this
[01:26:56] is more likely than that.
[01:27:00] - [Vivek] Thanks, I
[01:27:00] know you've been waiting
[01:27:01] so why don't you go ahead
[01:27:02] and then we'll take one more from there.
[01:27:04] - [Man] Sorry, just a quick question.
[01:27:06] On other AI aspects like
[01:27:06] evolution computation and stuff,
[01:27:10] do you have some opinion
[01:27:12] whether they will?
[01:27:14] - Sorry I didn't hear what you said.
[01:27:15] - [Man] In other AI fields like
[01:27:17] evolutionary computation for example,
[01:27:20] do you have any opinion on those?
[01:27:21] Because you sort of mentioned
[01:27:23] they're only symbolic in Europe.
[01:27:24] - Did you say evolution?
[01:27:25] - [Man] Like genetic programming,
[01:27:26] those kind of things.
[01:27:27] - Ah yes.
[01:27:29] I think it's great for
[01:27:29] setting hyperparameters.
[01:27:31] That is if you're in a
[01:27:31] high dimensional space,
[01:27:33] and you want to improve,
[01:27:35] if you can get a gradient
[01:27:35] you're gonna do much better
[01:27:37] than someone who can't get a gradient.
[01:27:40] And the brain is a device
[01:27:40] for getting gradients.
[01:27:43] Evolution can't get gradients 'cause
[01:27:45] a lot of what determines the relationship
[01:27:48] between the genotype and the phenotype
[01:27:50] is outside your control.
[01:27:51] It's the environment.
[01:27:53] So evolution has to use techniques
[01:27:54] like mutation, random changes,
[01:27:57] and recombinations.
[01:27:59] But we're not limited to that.
[01:28:00] We can produce a device
[01:28:00] that can get gradients.
[01:28:03] Now obviously if you can get gradients,
[01:28:05] you can also use evolution
[01:28:05] to make that device better.
[01:28:09] And if you look at what
[01:28:09] happens in neural nets now,
[01:28:12] you train a neural net using gradients.
[01:28:15] But now you fiddle with
[01:28:15] the hyperparameters
[01:28:17] using something much more like
[01:28:17] an evolutionary technique.
[01:28:20] So.
[01:28:21] - [Vivek] I think we have
[01:28:21] time for one more question
[01:28:24] from that side.
[01:28:26] - [Man] Thank you so Yann talk about using
[01:28:30] CNs or other types of
[01:28:30] neural nets in perception
[01:28:33] for autonomous vehicles
[01:28:36] and doesn't sound very positive.
[01:28:38] So could you make some
[01:28:38] more comments on that?
[01:28:41] - Well there's been a lot of
[01:28:44] declaration probably kinda
[01:28:44] more marketing oriented
[01:28:47] than science oriented
[01:28:48] that fully autonomous driving
[01:28:48] is just around the corner.
[01:28:53] And it's just a lot harder
[01:28:55] than most people imagine.
[01:28:58] A lot of people in the business of course
[01:28:59] knew it was hard and it's
[01:28:59] not just around the corner.
[01:29:02] I think there's a similar story in
[01:29:05] a lot of areas of AI,
[01:29:07] and AI as a whole
[01:29:08] where a lot of people had
[01:29:08] very optimistic expectations
[01:29:13] about when human level AI
[01:29:13] will be attained for example.
[01:29:17] In my opinion, it's not
[01:29:17] just around the corner.
[01:29:19] There are certainly things like
[01:29:23] how to do self supervised running properly
[01:29:24] that need to be figured
[01:29:24] out before that happens.
[01:29:27] But it's not the only obstacles.
[01:29:29] It's just the first mountain that we see.
[01:29:32] And there might be a whole
[01:29:32] bunch of mountains behind
[01:29:33] that we haven't figured out.
[01:29:35] So I think it's a little bit the same
[01:29:37] for autonomous driving.
[01:29:39] Autonomous driving, it's easy to get
[01:29:41] early impressive results
[01:29:41] where a car appears
[01:29:44] to drive itself pretty well
[01:29:44] for about half an hour.
[01:29:47] But to get the same level
[01:29:47] of reliability as humans,
[01:29:50] which is one fatal accident per 100 miles,
[01:29:53] per 100 million miles, I'm sorry.
[01:29:55] (audience laughing)
[01:30:01] You know what's 10 to the
[01:30:01] sixth between friends.
[01:30:04] (audience laughing)
[01:30:06] That it's really hard
[01:30:06] to get to that level.
[01:30:09] And if you try to sort of
[01:30:09] extrapolate how much data you need
[01:30:12] to get to that level by sort of seeing
[01:30:14] how the performance improves
[01:30:16] as you increase the amount of data,
[01:30:17] it's basically impractical.
[01:30:18] So we have to find new ways
[01:30:18] of training those systems.
[01:30:21] And I think self supervised learning
[01:30:22] is part of the answer.
[01:30:24] We'll see, okay.
[01:30:26] It's a hard problem.
[01:30:28] You can over engineer it.
[01:30:30] You can add sensors that make
[01:30:31] the processing easier.
[01:30:32] You can do detailed maps.
[01:30:35] You can do all kinds of stuff
[01:30:36] to kinda make it practical
[01:30:36] in some conditions.
[01:30:39] But fully sort of level five
[01:30:39] autonomous driving is hard.
[01:30:44] - [Man] Thank you very much.
[01:30:45] - [Vivek] Okay, with
[01:30:45] that I know many of you
[01:30:47] have other conference events to go to.
[01:30:49] Now we're done with the last question.
[01:30:50] So I would really like
[01:30:50] to thank Yann and Geoff
[01:30:54] once again for a most
[01:30:54] memorable Turing lecture.
[01:30:57] (audience clapping)
[01:30:57] Thank you.
[01:31:06] And enjoy the rest of the conference
[01:31:08] including the events that
[01:31:08] you have this evening.
[01:31:11] Thank you.
