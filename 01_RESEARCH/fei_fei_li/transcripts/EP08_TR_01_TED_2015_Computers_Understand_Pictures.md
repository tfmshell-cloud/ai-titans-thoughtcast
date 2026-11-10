# TED 2015: How We're Teaching Computers to Understand Pictures — Fei-Fei Li
- **YouTube URL:** https://www.youtube.com/watch?v=40riCqvRoMs
- **Lines:** 376

---

[00:00:17] Let me show you something.
[00:00:17] Okay.
[00:00:19] That's a cat sitting in a bed.
[00:00:22] The boy's petting the elephant.
[00:00:26] Those are people that going on a
[00:00:30] That's a big airplane.
[00:00:33] This is a 3-year-old child describing
[00:00:36] what she sees in a series of photos.
[00:00:39] She might still have a lot to learn
[00:00:41] about this world, but she's already an
[00:00:43] expert at one very important task, to
[00:00:47] make sense of what she sees.
[00:00:50] Our society is more technologically
[00:00:52] advanced than ever. We send people to
[00:00:55] the moon. We make phones that talk to us
[00:00:58] or customize radio stations that can
[00:01:00] play only music we like.
[00:01:03] Yet, our most advanced machines and
[00:01:06] computers still struggle at this task.
[00:01:09] So, I'm here today to give you a
[00:01:11] progress report on the latest advances
[00:01:15] in our research in computer vision, one
[00:01:17] of the most frontier and potentially
[00:01:20] revolutionary technology in computer
[00:01:23] science.
[00:01:24] Yes, we have prototype cars that can
[00:01:27] drive by themselves.
[00:01:29] But without smart vision, they cannot
[00:01:32] really tell the difference between a
[00:01:33] crumpled paper bag on the road, which
[00:01:35] can be run over, and a rock that size,
[00:01:39] which should be avoided.
[00:01:41] We have made fabulous megapixel cameras,
[00:01:44] but we have not delivered sight to the
[00:01:47] blind.
[00:01:48] Drones can fly over massive land, but
[00:01:51] not enough vision technology can help us
[00:01:54] to track the changes of the rainforests.
[00:01:57] Security cameras are everywhere,
[00:02:00] but they do not us when a child is
[00:02:03] drowning in a swimming pool.
[00:02:06] Photos and videos
[00:02:08] are becoming an integral part of global
[00:02:10] life. They're being generated at a pace
[00:02:13] that's far beyond any human or teams of
[00:02:16] human could hope to view. And you and I
[00:02:19] are contributing to that at this TED.
[00:02:22] Yet, our most advanced software are
[00:02:25] still struggling at understanding and
[00:02:28] managing this enormous content.
[00:02:31] So, in other words, collectively, as a
[00:02:34] society,
[00:02:36] we're very much blind because our
[00:02:38] smartest machines are still blind.
[00:02:43] Why is this so hard, you might ask?
[00:02:46] Cameras can take pictures like this one
[00:02:48] by converting lights into a
[00:02:50] two-dimensional array of numbers known
[00:02:53] as pixels.
[00:02:54] But these are just lifeless numbers.
[00:02:57] They do not carry meaning in themselves.
[00:03:00] Just like to hear is not the same as to
[00:03:03] listen. To take pictures is not the same
[00:03:06] as to see.
[00:03:08] And by seeing, we really mean
[00:03:11] understanding.
[00:03:13] In fact, it took Mother Nature 540
[00:03:17] million years of hard work to do this
[00:03:20] task. And much of that effort went into
[00:03:23] developing the visual processing
[00:03:26] apparatus of our brains, not the eyes
[00:03:29] themselves.
[00:03:30] So, vision begins with the eyes,
[00:03:34] but it truly takes place in the brain.
[00:03:38] So, for 15 years now, starting from my
[00:03:41] PhD at Caltech and then leading
[00:03:44] Stanford's Vision Lab, I've been working
[00:03:46] with my mentors, collaborators, and
[00:03:49] students to teach computers to see.
[00:03:54] Our research field is called computer
[00:03:56] vision and machine learning. It's part
[00:03:58] of the general field of artificial
[00:04:00] intelligence.
[00:04:03] So, ultimately, we want to teach the
[00:04:05] machines to see just like we do, naming
[00:04:08] objects, identifying people, inferring
[00:04:11] 3D geometry of things, understanding
[00:04:14] relations, emotions, actions, and
[00:04:17] intentions.
[00:04:19] You and I, weave together entire stories
[00:04:22] of people, places, and things the moment
[00:04:26] we lay our gaze on them.
[00:04:29] The first step towards this goal is to
[00:04:32] teach a computer to see objects, the
[00:04:34] building block of the visual world.
[00:04:37] In its simplest terms, imagine this
[00:04:41] teaching process as showing the computer
[00:04:43] some training images of a particular
[00:04:46] object, let's say cats, and design a
[00:04:49] model that learn from these training
[00:04:52] images.
[00:04:53] How hard can this be?
[00:04:55] After all, a cat is just a collection of
[00:04:58] shapes and colors. And this is what we
[00:05:00] did in the early days of object
[00:05:02] modeling. We tell the computer algorithm
[00:05:05] in a mathematical language that a cat
[00:05:07] has a round face, a chubby body, two
[00:05:10] pointy ears, and a long tail. And that
[00:05:12] looked all fine.
[00:05:14] But what about this cat?
[00:05:17] It's all curled up. Now, you have to add
[00:05:20] another shape and viewpoint to the
[00:05:22] object model.
[00:05:24] But what if cats are hidden?
[00:05:27] What about these silly cats?
[00:05:34] Now, you get my point. Even something as
[00:05:34] simple as a household pet can present an
[00:05:37] infinite number of variations to the
[00:05:39] object model. And that's just one
[00:05:42] object.
[00:05:44] So, about eight years ago,
[00:05:47] a very simple and profound observation
[00:05:50] changed my thinking.
[00:05:53] No one tells a child how to see,
[00:05:55] especially in the early years. They
[00:05:58] learn this through real-world
[00:06:00] experiences and examples.
[00:06:03] If you consider a child's eyes as a pair
[00:06:06] of biological cameras, they take one
[00:06:09] picture about every 200 ms, the average
[00:06:13] time an eye movement is made.
[00:06:15] So, by age three, a child would have
[00:06:18] seen hundreds of millions of pictures of
[00:06:21] the real world.
[00:06:23] That's a lot of training examples.
[00:06:26] So, instead of focusing on solely on
[00:06:29] better and better algorithms, my insight
[00:06:33] was to give the algorithms the kind of
[00:06:36] training data that a child was given
[00:06:39] through experiences in both quantity and
[00:06:42] quality.
[00:06:44] Once we know this, we knew we needed to
[00:06:48] collect a data set that has far more
[00:06:50] images than we have ever had before,
[00:06:53] perhaps thousands of times more.
[00:06:56] And together with Professor Kaylee at
[00:06:59] Princeton University, we launched the
[00:07:01] ImageNet project in 2007.
[00:07:06] Luckily, we didn't have to mount a
[00:07:07] camera on our head and wait for many
[00:07:10] years. We went to the internet, the
[00:07:12] biggest treasure trove of pictures that
[00:07:15] humans have ever created. We downloaded
[00:07:18] nearly a billion images and used the
[00:07:20] crowdsourcing technology like Amazon
[00:07:24] Mechanical Turk platform to help us to
[00:07:26] label these images.
[00:07:28] At its peak, ImageNet was one of the
[00:07:31] biggest employers of the Amazon
[00:07:34] Mechanical Turk workers.
[00:07:36] Together, almost 50,000 workers
[00:07:40] from 167
[00:07:42] countries around the world helped us to
[00:07:44] clean, sort, and label nearly a billion
[00:07:49] candidate images.
[00:07:52] That was how much effort it took to
[00:07:55] capture even a fraction of the imageries
[00:07:58] a child's mind takes in in the early
[00:08:01] developmental years.
[00:08:03] In hindsight, this idea of using big
[00:08:07] data to train computer algorithms may
[00:08:10] seem obvious now,
[00:08:12] but back in 2007, it was not so obvious.
[00:08:16] We were fairly alone on this journey for
[00:08:18] quite a while.
[00:08:20] Some very friendly colleagues advised me
[00:08:22] to do something more useful for my
[00:08:24] tenure.
[00:08:25] And we were constantly struggling for
[00:08:28] research funding. Once, I even joked to
[00:08:30] my graduate students that I would just
[00:08:32] reopen my dry cleaner shop to fund
[00:08:35] ImageNet. After all, that's how I funded
[00:08:38] through my college years.
[00:08:40] So, we carried on. In 2009,
[00:08:44] ImageNet project delivered a database of
[00:08:48] 15 million images across 22,000
[00:08:52] classes of objects and things,
[00:08:55] organized by everyday English words. In
[00:08:58] both quantity and quality, this was a
[00:09:02] non-precedented scale.
[00:09:05] As an example, in the case of cats, we
[00:09:08] have more than 62,000 cats of all kinds
[00:09:12] of looks and poses,
[00:09:15] and across all species of domestic and
[00:09:18] wild cats.
[00:09:20] We were thrilled to have put together
[00:09:22] ImageNet, and we wanted the whole
[00:09:25] research world to benefit from it. So,
[00:09:27] in a TED fashion, we opened up the
[00:09:29] entire data set to the worldwide
[00:09:32] research community for free.
[00:09:43] Now that we have the data to nourish our
[00:09:43] computer brain,
[00:09:45] we're ready to come back to the
[00:09:47] algorithms themselves.
[00:09:49] As it turned out, the wealth of
[00:09:52] information provided by ImageNet was a
[00:09:54] perfect match to a particular class of
[00:09:57] machine learning algorithms called
[00:10:00] convolutional neural network pioneered
[00:10:03] by Kunihiko Fukushima, Jeff Hinton, and
[00:10:06] Yann LeCun back in 1970s and 80s.
[00:10:10] Just like the brain is consisted of
[00:10:13] billions of highly connected neurons,
[00:10:16] a basic operating unit in a neural
[00:10:19] network is a neuron-like node. It takes
[00:10:23] input from other nodes and sends output
[00:10:26] to others.
[00:10:27] Moreover, these hundreds of thousands or
[00:10:31] even millions of nodes are organized in
[00:10:34] hierarchical layers, also similar to the
[00:10:37] brain.
[00:10:38] In a typical neural network we used to
[00:10:40] train our object recognition model, it
[00:10:43] has 24 million nodes, 140 million
[00:10:48] parameters, and 15 billion connections.
[00:10:52] That's an enormous model.
[00:10:55] Powered by the massive data from
[00:10:57] ImageNet and the modern CPUs and GPUs to
[00:11:01] train such a humongous model, the
[00:11:04] convolutional neural network blossomed
[00:11:07] in a way that no one expected.
[00:11:10] It became the winning architecture to
[00:11:13] generate exciting new results in object
[00:11:16] recognition.
[00:11:18] This is a computer telling us this
[00:11:21] picture contains a cat and where the cat
[00:11:23] is. Of course, there are more things
[00:11:25] than cats. So, here's a computer
[00:11:28] algorithm telling us the picture
[00:11:29] contains a boy and a teddy bear.
[00:11:32] A dog, a person, and a small kite in the
[00:11:35] background.
[00:11:36] Or a picture of very busy things, like a
[00:11:40] man, a skateboard, railings, and lamp
[00:11:43] posts, and so on.
[00:11:45] Sometimes, when the computer is not so
[00:11:47] confident about what it sees,
[00:11:51] we have taught it to be smart enough to
[00:11:54] give us a safe answer instead of
[00:11:56] committing too much, just like we would
[00:11:58] do.
[00:12:00] But other times, our computer algorithm
[00:12:02] is remarkable at telling us what exactly
[00:12:05] the objects are, like the make, model,
[00:12:08] year of the cars.
[00:12:10] We apply this algorithm to millions of
[00:12:14] Google Street View images across
[00:12:16] hundreds of American cities, and we have
[00:12:19] learned something really interesting.
[00:12:22] First, it confirmed our common wisdom
[00:12:25] that car prices correlate very well with
[00:12:29] household incomes.
[00:12:30] But surprisingly,
[00:12:32] car prices also correlate well with
[00:12:35] crime rates in cities.
[00:12:38] Or voting patterns by zip codes.
[00:12:46] So, wait a minute. Is that it? Has
[00:12:46] computer already matched or even
[00:12:48] surpassed human capabilities?
[00:12:51] Not so fast.
[00:12:53] So far, we have just taught the computer
[00:12:56] to see objects. This is like a small
[00:12:59] child learning to utter a few nouns.
[00:13:02] It's an incredible accomplishment, but
[00:13:05] it's only the first step.
[00:13:08] Soon, another developmental milestone
[00:13:11] will hit, and children begin to
[00:13:13] communicate in sentences.
[00:13:15] So, instead of saying this is a cat in
[00:13:18] the picture, you already heard the
[00:13:20] little girl telling us this is a cat
[00:13:22] lying on a bed.
[00:13:25] So, to teach a computer to see a picture
[00:13:28] and generate sentences, the marriage
[00:13:31] between big data and machine learning
[00:13:33] algorithm has to take another step. Now,
[00:13:37] the computer has to learn from both
[00:13:39] pictures as well as natural language
[00:13:42] sentences generated by humans.
[00:13:47] Just like the brain integrates vision
[00:13:49] and language, we developed a model that
[00:13:53] connects parts of visual things, like
[00:13:56] visual snippets, with words and phrases
[00:14:00] in sentences.
[00:14:02] About 4 months ago, we finally tied all
[00:14:06] this together and produced one of the
[00:14:08] first computer vision models that is
[00:14:11] capable of generating a human-like
[00:14:14] sentence when it sees a picture for the
[00:14:16] first time.
[00:14:19] Now, I'm ready to show you what the
[00:14:21] computer says when it sees the picture
[00:14:25] that the little girl saw at the
[00:14:27] beginning of this talk.
[00:14:38] A large airplane sitting on top of an
[00:14:38] airport runway.
[00:14:40] Of course, we're still working hard to
[00:14:43] improve our algorithms, and it still has
[00:14:46] a lot to learn.
[00:14:54] And the computer still makes mistakes.
[00:14:54] A cat lying on a bed in a blanket.
[00:14:57] So, of course, when it sees too many
[00:14:59] cats, it thinks everything might look
[00:15:01] like a cat.
[00:15:09] A young boy is holding a baseball bat.
[00:15:09] Or if it hasn't seen a toothbrush, it
[00:15:11] confuses a baseball bat.
[00:15:15] A man riding a horse down the street
[00:15:17] next to a building.
[00:15:20] We haven't taught art 101 to the
[00:15:22] computers.
[00:15:25] A zebra standing in a field of grass.
[00:15:28] And it hasn't learned to appreciate the
[00:15:30] stunning beauty of nature like you and I
[00:15:32] do.
[00:15:34] So, it has been a long journey.
[00:15:37] To get from age 0 to 3 was hard. The
[00:15:41] real challenge is to go from 3 to 13 and
[00:15:45] far beyond. Let me remind you with this
[00:15:48] picture of the boy and the cake again.
[00:15:51] So far, we have taught the computer to
[00:15:54] see objects or even tell us a simple
[00:15:57] story when seeing a picture. A person
[00:16:00] sitting at a table with a cake.
[00:16:03] But there's so much more to this picture
[00:16:05] than just a person and a cake. What the
[00:16:08] computer doesn't see is that this is a
[00:16:11] special Italian cake that's only served
[00:16:14] during Easter time.
[00:16:15] The boy is wearing his favorite t-shirt
[00:16:19] given to him as a gift by his father
[00:16:21] after trip to Sydney.
[00:16:23] And you and I can all tell how happy he
[00:16:26] is and what's exactly on his mind at
[00:16:28] that moment.
[00:16:30] This is my son, Leo.
[00:16:34] On my quest for visual intelligence, I
[00:16:36] think of Leo constantly and the future
[00:16:39] world he will live in.
[00:16:41] When machines can see, doctors and
[00:16:45] nurses will have extra pairs of tireless
[00:16:48] eyes to help them to diagnose and take
[00:16:51] care of patients. Cars will run smarter
[00:16:55] and safer on the road.
[00:16:57] Robots, not just humans, will help us to
[00:17:00] brave the disaster zones to save the
[00:17:03] trapped and wounded.
[00:17:05] We will discover new species, better
[00:17:08] materials, and explore unseen frontiers
[00:17:11] with the help of the machines.
[00:17:14] Little by little, we're giving sights to
[00:17:17] the machines. First, we teach them to
[00:17:20] see. Then, they help us to see better.
[00:17:24] For the first time, human eyes won't be
[00:17:27] the only ones pondering and exploring
[00:17:30] our world. We will not only use the
[00:17:33] machines of their intelligence, we will
[00:17:35] also collaborate with them in ways that
[00:17:38] we cannot even imagine.
[00:17:41] This is my quest to give computer visual
[00:17:45] intelligence
[00:17:46] and to create a better future for Leo
[00:17:49] and for the world. Thank you.
