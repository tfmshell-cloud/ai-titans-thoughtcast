# Yann LeCun: Turing Award Lecture Sequel — The Deep Learning Revolution
- **YouTube URL:** https://www.youtube.com/watch?v=psl1wY2V-L0
- **Lines:** 1142

---

[00:00:00] okay i'll talk about the sequel
[00:00:04] but i'll start also with a little bit of
[00:00:06] history and sort of
[00:00:08] go through some of the things that uh
[00:00:10] jeff just mentioned
[00:00:11] so jeff talked about about supervised
[00:00:14] running and supervisioning works
[00:00:16] amazingly well if you have lots of data
[00:00:19] we all know this so we can do speech
[00:00:21] recognition we can do
[00:00:23] image recognition we can do face
[00:00:25] recognition we can do
[00:00:26] we can generate captions for images we
[00:00:28] can do translation
[00:00:30] that works really well and if you give
[00:00:32] your neural net a particular structure
[00:00:34] something like a convolutional net
[00:00:36] uh as jeff mentioned in the late 80s
[00:00:38] early 90s we could
[00:00:41] train systems to recognize handwriting
[00:00:43] that was quite successful
[00:00:44] uh by the end of the 90s the system of
[00:00:46] this type that i built at bell labs
[00:00:48] i was reading something like 10 to 20 of
[00:00:51] all the checks in the us so
[00:00:52] a big success even a commercial success
[00:00:55] but that but by that time the entire
[00:00:57] community
[00:00:58] had basically abandoned neural nets
[00:01:00] partly because of the lack of large data
[00:01:02] sets
[00:01:02] for which they could work partly because
[00:01:04] the type of software at the time that
[00:01:06] you had to write was fairly complicated
[00:01:08] and
[00:01:08] it it was a big investment to um to do
[00:01:11] this
[00:01:12] partly also because computers were not
[00:01:13] fast enough for
[00:01:15] all kinds of other applications but
[00:01:17] convolutional nets really
[00:01:18] are inspired by uh biology they're not
[00:01:22] copying biology but there is a lot of
[00:01:23] inspiration from
[00:01:24] from biology from the architecture of
[00:01:26] the visual cortex
[00:01:28] and ideas that come naturally when you
[00:01:30] study signal processing the
[00:01:32] idea that filtering is is a good
[00:01:35] way to kind of process signals whether
[00:01:38] they're audio signals or image
[00:01:39] image signals and the convolutions is a
[00:01:41] way to do filtering is very natural
[00:01:43] and the fact that you find this in the
[00:01:44] brain is really not that surprising
[00:01:47] and those ideas of course were proposed
[00:01:49] by hublin weasel in sort of classic work
[00:01:52] in neuroscience back in the 60s
[00:01:54] as well as uh and sort of picked up by
[00:01:57] fukushima who's a japanese
[00:01:59] researcher who tried to build computer
[00:02:01] models of
[00:02:03] uh the the hublin result model if you
[00:02:05] want
[00:02:06] and i found that inspiring and and sort
[00:02:08] of tried to reproduce this using
[00:02:10] uh neural nets that could be trained
[00:02:12] with back propagation that's basically
[00:02:13] what the convolutional net uh
[00:02:15] is and so the idea accomplished on that
[00:02:18] is that
[00:02:18] uh the the world the perceptual world is
[00:02:22] compositional that the
[00:02:25] the visual world objects are formed by
[00:02:28] parts
[00:02:29] and parts are formed by motifs and
[00:02:31] motifs
[00:02:32] of one by uh
[00:02:36] textures or elementary combinations of
[00:02:39] edges
[00:02:40] and edges are formed by by pixels
[00:02:42] arrangements of pixels and so if you
[00:02:44] have a system that sort of
[00:02:45] hierarchically
[00:02:46] can detect uh unusually
[00:02:50] useful combinations of pixels into edges
[00:02:52] and edges into
[00:02:53] motifs and motifs into parts of objects
[00:02:55] then you will have
[00:02:56] a recognition system this idea of
[00:02:57] hierarchy actually goes back a long time
[00:03:00] and so that's uh that's really the
[00:03:02] principle of computational nets and it
[00:03:03] turns out
[00:03:04] that hierarchical representations are
[00:03:06] good not just for
[00:03:08] for vision but also for speech for text
[00:03:10] and for all kinds of other natural
[00:03:12] signals
[00:03:13] that are comprehensible because they are
[00:03:15] compositional
[00:03:17] i think there is this saying uh it's
[00:03:18] attributed to einstein i believe the
[00:03:22] what is most uh
[00:03:26] mysterious about the world is that it is
[00:03:28] understandable
[00:03:29] and it's probably because of the
[00:03:30] compositional nature
[00:03:32] of uh of the natural of natural signals
[00:03:35] so uh in the early 90s we were able to
[00:03:38] do things like build recognition systems
[00:03:40] like this one this is a younger version
[00:03:41] of myself here
[00:03:43] i'm at bell labs this is by the way my
[00:03:45] phone number at bell labs in hondal
[00:03:47] no longer operating i'm hitting a key
[00:03:50] here and
[00:03:50] the system captures an image with a
[00:03:52] video camera this runs on the pc with a
[00:03:55] special dsp card in it
[00:03:56] and it could run those commercial nets
[00:03:58] at you know several hundred characters
[00:04:00] per second at the time which was
[00:04:02] amazing we could run 20 megaflops you
[00:04:04] know that was just incredible so
[00:04:06] that worked really well and uh pretty
[00:04:09] soon we realized we could use this for
[00:04:10] natural images as well to do things like
[00:04:12] detecting
[00:04:13] uh faces eventually detecting
[00:04:16] pedestrians that took uh
[00:04:18] a few years but as uh jeff mentioned
[00:04:21] there was sort of a neural net winter
[00:04:23] between the mid 90s and the
[00:04:25] uh sort of late 2000s if you want where
[00:04:28] almost nobody was working on their own
[00:04:29] ads except a few crazy people like us
[00:04:33] so that didn't stop us and so
[00:04:36] working on face detection pedestrian
[00:04:38] detection even working on
[00:04:40] using machine learning and convolutional
[00:04:42] net for
[00:04:44] robotics where we we would use a
[00:04:47] convolutional net to
[00:04:48] label an entire image in such a way that
[00:04:51] every pixel in an image would be labeled
[00:04:54] as to whether it's traversable or not
[00:04:56] reversible by a robot
[00:04:57] and the nice thing about this is that
[00:04:59] you can you can collect data
[00:05:00] automatically
[00:05:01] you don't need to manually label it
[00:05:03] because using stereo vision you can
[00:05:05] figure out if
[00:05:06] a pixel sticks out of the ground or not
[00:05:09] using 3d reconstruction
[00:05:11] but unfortunately that only works at
[00:05:12] short range so if you want a system that
[00:05:14] can plan long range
[00:05:15] trajectories then you can train a
[00:05:17] convolutional net to
[00:05:18] make the predictions for traversability
[00:05:20] using those labels and then
[00:05:22] let the robot drive itself around so
[00:05:25] it's got
[00:05:25] this particular robot here as a
[00:05:27] combination of different
[00:05:29] features that it uses
[00:05:33] extracted by the conventional net and
[00:05:36] also a
[00:05:37] rapid stereo vision system that allows
[00:05:38] it to
[00:05:40] avoid obstacles such as pesky graduate
[00:05:43] students
[00:05:46] uh piazza mania and raya hatsel by the
[00:05:48] way who
[00:05:49] are pretty sure the robot is not going
[00:05:51] to run them over because they actually
[00:05:53] wrote the code
[00:05:58] okay and then a couple years later we
[00:06:01] used a very similar system to do
[00:06:02] semantic segmentation this is actually
[00:06:04] the work
[00:06:05] that jeff was talking about that was
[00:06:06] rejected from cvpr2011
[00:06:09] so this is the system that could in real
[00:06:11] time using a
[00:06:12] fpga implementation uh segment you know
[00:06:15] basically give
[00:06:16] a category for every pixel in an image
[00:06:20] at about 30 frames per second that sort
[00:06:22] of decent resolution
[00:06:23] it was far from perfect but it could
[00:06:25] sort of label with sort of reasonable
[00:06:26] accuracy detect pedestrians detect the
[00:06:29] roads and the trees and etc um
[00:06:34] but the results basically were not
[00:06:36] immediately believed by the
[00:06:38] computer vision community now to measure
[00:06:40] the progress
[00:06:41] that has happened uh since then in the
[00:06:44] last 10 years essentially
[00:06:46] this is an example of a result of a
[00:06:48] really recent system that was put
[00:06:49] together by a team at facebook
[00:06:52] that they called the panoptic feature
[00:06:54] pyramid network so it's basically a
[00:06:55] large convolutional net that has
[00:06:57] sort of a path that extracts features
[00:07:00] multi-layer extract features and then
[00:07:02] another path that sort of generates an
[00:07:04] output image
[00:07:04] and the output image basically
[00:07:06] identifies and
[00:07:08] generates a mask for every instance of
[00:07:11] every object in the image and tells you
[00:07:12] what category they are
[00:07:13] so here the name of the categories on
[00:07:15] the display but it can recognize
[00:07:16] something like a few hundred categories
[00:07:18] people vehicles of various kinds and not
[00:07:21] just object categories but also sort of
[00:07:23] background
[00:07:24] uh sort of textures or regions
[00:07:28] things like you know grass and sand and
[00:07:31] uh
[00:07:31] trees and things like that so you would
[00:07:33] imagine a system like this would be very
[00:07:34] useful for
[00:07:35] things like self-driving cars if you
[00:07:37] have the complete segmentation
[00:07:38] identification of all the pixels in an
[00:07:40] image uh it would make it easier to
[00:07:42] build star-driven cars not just not just
[00:07:44] driving cars but also
[00:07:46] medical image analysis system so this is
[00:07:48] a relatively similar architecture
[00:07:50] people call this u-net sometimes because
[00:07:52] of the obvious u-shaped of this
[00:07:54] of this commercial net again it has
[00:07:57] an encoder part that sort of extracts
[00:07:59] features and then a sort of
[00:08:01] a part that constructs the output image
[00:08:03] where the the parts of the
[00:08:05] medical images are segmented this is the
[00:08:08] kind of result that it's producing
[00:08:09] uh this is some work by some of my
[00:08:11] colleagues at nyu i was not involved in
[00:08:13] this work
[00:08:14] uh this a different subgroup of
[00:08:16] colleagues with some
[00:08:17] common co-authors has worked also on uh
[00:08:20] detecting breast cancer from from
[00:08:21] imaging
[00:08:22] from from x-rays from mammograms uh in
[00:08:25] fact one of the
[00:08:27] most sort of hardest topics in uh
[00:08:30] in in radiology these days is using deep
[00:08:33] learning for
[00:08:34] uh medical image analysis it's a it's
[00:08:37] probably going to
[00:08:38] affect if not revolutionize radiology in
[00:08:41] the next few years it's already it
[00:08:42] already has to some extent
[00:08:45] some more work along those directions
[00:08:47] this is actually a collaboration between
[00:08:49] the nyu medical school and physical care
[00:08:50] research
[00:08:51] in accelerating the data collection for
[00:08:54] mri so
[00:08:55] when you go to an mri you have to sit in
[00:08:57] the machine for about an hour
[00:08:58] or 20 minutes depending on the kind of
[00:09:00] exam you're going through and
[00:09:03] this technique here using
[00:09:06] those kind of reconstruction condition
[00:09:09] that
[00:09:09] allows to basically reduce the data
[00:09:12] collection time
[00:09:13] and get images that are essentially of
[00:09:15] the same quality
[00:09:17] so they will
[00:09:21] not put radiology out of jobs
[00:09:24] but it will make the job more
[00:09:26] interesting probably
[00:09:27] um jeff was mentioning work on
[00:09:30] translation with neural nets this is
[00:09:33] i think a very surprising and
[00:09:35] interesting development of the fact that
[00:09:37] you can use neural nets to do
[00:09:38] translation
[00:09:40] and there is a lot of innovation in the
[00:09:42] kind of architectures that are used for
[00:09:44] this so
[00:09:45] jeff talked about the attention
[00:09:46] mechanism the transformer architecture
[00:09:48] this is a new one called enemy
[00:09:50] convolutions which kind of recycles a
[00:09:52] bit of those ideas
[00:09:53] and and things work really well there
[00:09:55] those networks are very large they have
[00:09:57] a few hundred million parameters in them
[00:10:00] and so
[00:10:01] the the some of the challenges there is
[00:10:03] actually running them
[00:10:05] on on gpus having enough memory to run
[00:10:08] them
[00:10:08] we're basically limited by uh gpu memory
[00:10:11] there
[00:10:12] so those ideas of image segmentation
[00:10:14] have been used by people working on
[00:10:15] self-driving cars particularly
[00:10:18] people at mobile life going which is not
[00:10:21] intel going back several years those the
[00:10:24] first convolutional nets i think that
[00:10:26] were deployed for self-driving cars or
[00:10:27] for driving assistance were in the
[00:10:30] 2015 tesla s model
[00:10:33] nvidia has devoted a large set of
[00:10:35] efforts also to sell driving cars
[00:10:37] and so there's a lot of interesting
[00:10:39] things going on there but progress
[00:10:42] is uh i wouldn't say slow
[00:10:45] but completely autonomous driving is a
[00:10:48] hard problem
[00:10:48] it's not as easy as people thought
[00:10:50] initially
[00:10:51] okay so um jeff uh kind of brushed away
[00:10:55] reinforcement learning but reinforcement
[00:10:57] learning is something that a lot of
[00:10:58] people are really excited about
[00:10:59] particularly people at deepmind
[00:11:02] but there is a problem with the current
[00:11:03] crop of reinforcement learning which is
[00:11:05] that it's extremely data inefficient
[00:11:07] if you want to train a system to do
[00:11:08] anything using reinforcement learning
[00:11:10] it will have to do lots and lots of
[00:11:12] trial and errors so for example
[00:11:14] to get a machine to play atari games
[00:11:16] classic atari games to
[00:11:18] the level that any human can reach in
[00:11:20] about 15 minutes of
[00:11:22] training the machine will have to play
[00:11:25] the equivalent of 80 hours
[00:11:26] of real-time play
[00:11:30] to play uh go at a
[00:11:33] superhuman level they will have to to
[00:11:35] play something like 20 million games
[00:11:37] to play starcraft this is a recent
[00:11:39] deepmind work
[00:11:42] it's a blog post noted paper the alpha
[00:11:44] star system
[00:11:46] took the equivalent of 200 years of
[00:11:48] real-time play
[00:11:49] to reach a human level on a single map
[00:11:53] for kind of a single type of player
[00:11:57] by the way all those systems use comb
[00:11:58] nets and various other things but
[00:12:00] uh that's an interesting thing so the
[00:12:03] problem with refreshment running is that
[00:12:05] those those models have to try something
[00:12:07] to to know if it's
[00:12:09] to work and it's really not practical to
[00:12:11] use in the real world if you want to
[00:12:12] train a robot to
[00:12:13] grasp things or you want to train a car
[00:12:16] to drive itself
[00:12:18] so you know to figure out um
[00:12:21] to train a system to drive a car so it
[00:12:24] doesn't run off cliffs
[00:12:25] it will actually have to dry to you know
[00:12:28] it will actually have to run off the
[00:12:30] cliffs multiple times before it figures
[00:12:31] out how not to do that
[00:12:35] first of all to figure out it's a bad
[00:12:36] idea and second to figure out how not to
[00:12:38] do it
[00:12:39] because it doesn't have a model of the
[00:12:41] world it doesn't it can't imagine what's
[00:12:42] going to happen
[00:12:43] before it happens it has to try things
[00:12:45] to correct itself that's why it's so
[00:12:47] inefficient so that begs the question
[00:12:50] how is it that humans
[00:12:51] and animals can learn so efficiently so
[00:12:53] quickly we can learn to drive a car most
[00:12:55] of us can learn to drive a car in about
[00:12:57] 20 hours of training
[00:12:58] with hardly any accident how does that
[00:13:00] happen
[00:13:01] we don't run off cliffs because we have
[00:13:03] a pretty good intuitive physics model
[00:13:05] that tells us
[00:13:06] if i turn if i'm driving next to a cliff
[00:13:08] and i'm turning the wheel to the right
[00:13:10] the car is going to run off the cliff
[00:13:11] it's going to fall and nothing good is
[00:13:13] going to come out of this
[00:13:14] okay so we have this internal model
[00:13:18] and the question is how do we learn this
[00:13:19] internal model and then and the next
[00:13:21] question is how do we get machines to
[00:13:22] learn internal models like that
[00:13:24] basically just by observation
[00:13:28] so there is a a gentleman called
[00:13:31] emmanuel dupu in paris is a
[00:13:33] developmental psychologist he works
[00:13:36] actually on
[00:13:37] how children learn language and speech
[00:13:39] and things like that but
[00:13:40] also other concepts and he made this
[00:13:41] chart about the time
[00:13:44] the the age and months at which babies
[00:13:46] learn basic concepts like things like
[00:13:49] distinguishing animate objects from
[00:13:51] inanimate objects that happens really
[00:13:52] quickly around three months old
[00:13:54] now the fact that some objects are are
[00:13:57] stable some of them will fall
[00:14:00] and you can sort of measure whether
[00:14:01] babies are surprised by the behavior of
[00:14:03] some objects
[00:14:05] and then it takes about nine months for
[00:14:07] babies to figure out that objects
[00:14:09] that are not supported will fall
[00:14:11] basically gravity
[00:14:13] so if you show a six month be
[00:14:18] a six month old baby the the the
[00:14:20] scenario on the top left where
[00:14:22] there's a little car on a platform and
[00:14:23] you push the little car off the platform
[00:14:25] and the car doesn't fall
[00:14:26] it's a trick baby six months old don't
[00:14:29] even pay attention that's just another
[00:14:31] thing that the world
[00:14:32] throws at them that they you know they
[00:14:34] have to learn
[00:14:35] it's fine a nine-month-old baby will go
[00:14:38] like the little girl at the bottom left
[00:14:42] be very very surprised in the meantime
[00:14:45] they've learned the concept of gravity
[00:14:47] and nobody has really told them what
[00:14:48] gravity is they've just kind of observed
[00:14:50] the world and
[00:14:50] they figured out objects that are not
[00:14:52] supported just fall and so when that
[00:14:54] doesn't happen they get surprised
[00:14:56] how does that happen it's not just
[00:14:59] humans animals have those models too
[00:15:01] you know cats dogs rats
[00:15:04] or wrong tongues so here is a baby
[00:15:06] orangutong here is being shown a magic
[00:15:08] trick
[00:15:09] put an object in a cup um remove the
[00:15:12] object but he doesn't see that
[00:15:14] then show the cut it's empty
[00:15:18] it was on the floor laughing
[00:15:22] so his model of the world was violated
[00:15:25] right he has a pretty good model of the
[00:15:26] world object permanence that's a very
[00:15:28] basic concept
[00:15:29] objects are not supposed to disappear
[00:15:30] like that um
[00:15:32] and when your model of the world is
[00:15:34] being violated
[00:15:36] you pay attention because you're going
[00:15:38] to learn something about the world you
[00:15:39] didn't know
[00:15:41] if it really violates a very basic thing
[00:15:43] about the world
[00:15:44] it's funny but it's also it might be
[00:15:48] dangerous
[00:15:49] right it's something that can kill you
[00:15:50] because you just didn't predict what
[00:15:53] what just happened okay so what's the
[00:15:55] salvation really
[00:15:56] you know how do we get machines to learn
[00:15:57] this this kind of stuff
[00:16:00] you know learn all the huge amount of
[00:16:01] background knowledge we learn about the
[00:16:02] world by just
[00:16:03] observing in the first few months of
[00:16:05] life and animals do this too
[00:16:08] so for example if i ask you um
[00:16:11] if i train myself to predict what the
[00:16:13] world is going to look like when i move
[00:16:15] my head slightly to the left
[00:16:18] because of parallax motion
[00:16:21] objects that are nearby and objects that
[00:16:23] are far away won't move
[00:16:25] uh the same way relative to you know
[00:16:28] my my viewpoint and so
[00:16:32] the best way to predict how the world is
[00:16:35] going to look
[00:16:36] when i move my head is to basically
[00:16:38] represent internally the notion of depth
[00:16:42] and consequently sort of conversely
[00:16:45] if i train a system to predict what the
[00:16:47] world what the world is going to look
[00:16:48] like
[00:16:49] when it moves its camera maybe it's
[00:16:51] going to learn the notion of depth
[00:16:53] automatically
[00:16:54] and once you have depth you have objects
[00:16:55] because you have objects in front of
[00:16:56] others you have occlusion edges
[00:16:58] once you have objects you have you know
[00:17:00] things you can influence and things that
[00:17:02] can move independently of others and
[00:17:03] things like that so
[00:17:04] concepts can kind of build on top of
[00:17:06] each other each other like this through
[00:17:09] prediction so that's the idea of cell
[00:17:12] supervision
[00:17:12] it's prediction and reconstruction i
[00:17:15] give the
[00:17:16] machine a piece of data that's a video
[00:17:18] clip
[00:17:19] i mask a piece of that video clip and i
[00:17:22] ask the system to predict
[00:17:23] the missing part from the part that it
[00:17:26] can observe
[00:17:27] okay so that would be video prediction
[00:17:29] just predict the future
[00:17:31] but the more general form of cell
[00:17:33] supervised running is i don't specify in
[00:17:35] advance which part i'm going to mask or
[00:17:36] not
[00:17:37] i'm just going to tell the system i'm
[00:17:38] going to mask a piece of it and whatever
[00:17:40] is masked you i'm
[00:17:41] asking you to reconstruct it
[00:17:45] and in fact i may not even mask it at
[00:17:47] all i'm just going to
[00:17:49] virtually mask it and just ask the
[00:17:50] system to reconstruct the input
[00:17:52] under certain constraints so the
[00:17:54] advantage of this cell supervision is
[00:17:56] that it's not task dependent you get the
[00:17:58] machine to learn about the world without
[00:17:59] training it for a particular task
[00:18:01] and so you can learn just by observation
[00:18:03] without having to interact with the
[00:18:04] world which is much more efficient
[00:18:06] but more importantly you're asking the
[00:18:07] system to predict a lot of stuff
[00:18:10] not just a value function like in
[00:18:13] reinforcement learning
[00:18:14] where basically the only thing you give
[00:18:15] the machine to predict is a scalar value
[00:18:17] once in a while
[00:18:18] not reinforcement not uh supervised
[00:18:21] learning where you ask the system to
[00:18:22] predict a label
[00:18:24] which is a few bits in the case of cell
[00:18:26] supervisor you're asking the machine to
[00:18:28] predict a lot of stuff
[00:18:31] and so that led me to this slightly
[00:18:33] obnoxious analogy at least for people
[00:18:35] who work on reinforcement learning
[00:18:37] which is the idea that if intelligence
[00:18:39] or learning
[00:18:40] is a is a cake the bulk of the cake the
[00:18:43] gene wise as we say in french
[00:18:44] uh israeli self-supervisioning most of
[00:18:47] what we learn most of the knowledge we
[00:18:48] accumulate about the world is learned
[00:18:50] through self-supervised learning
[00:18:52] um there's a little bit of icing on the
[00:18:54] cake which is supervised running we're
[00:18:56] you know being showed a picture book and
[00:18:57] we're being told the name of objects
[00:18:59] and with just a few examples we can know
[00:19:01] what the objects are
[00:19:04] we're we're taught the meaning of some
[00:19:06] words and
[00:19:07] you know babies can learn young
[00:19:10] young children can learn many many words
[00:19:13] per day
[00:19:14] new words and then the cherry on the
[00:19:16] cake is refreshing accounting it's
[00:19:18] it's a very small amount of information
[00:19:19] you're asking the machine to predict and
[00:19:21] so there's no way
[00:19:22] that the machine can learn purely from
[00:19:24] from that form of learning it has to be
[00:19:26] a combination
[00:19:27] of uh probably all three forms of
[00:19:30] learning but but
[00:19:31] principally self-supervised running this
[00:19:34] idea
[00:19:34] is not new a lot of people have argued
[00:19:36] for the idea of prediction
[00:19:38] for for learning the idea of learning
[00:19:41] models
[00:19:42] predictive models and one
[00:19:45] one such person is is jeff as a matter
[00:19:48] of fact this is a quote from
[00:19:49] from him which you know this is from a
[00:19:52] few years ago but he's been saying this
[00:19:54] for about 40 years
[00:19:55] at least for longer than i've known him
[00:20:00] and and it goes like this the brain has
[00:20:01] about 10 to 14 synapses and we only live
[00:20:03] about
[00:20:04] 10 to the 9 seconds so we have a lot
[00:20:07] more parameters than data this motivates
[00:20:08] the idea that we must do a lot of
[00:20:10] unsupervised learning or
[00:20:11] self-supervisioning
[00:20:12] since the perceptual input including
[00:20:13] proprioception is the only place where
[00:20:16] we can get 10 to the 50 dimensions of
[00:20:17] constraints per second
[00:20:19] if you're asked to predict everything
[00:20:21] that comes into your sense
[00:20:23] your your senses uh you know every
[00:20:26] fraction of a second that's a lot of
[00:20:28] information you have to learn
[00:20:29] and that might be enough to constrain
[00:20:32] all the synapses we have in our brain to
[00:20:33] learn things that are meaningful
[00:20:36] so the sequel of deep learning
[00:20:40] in my opinion is self-supervisioning and
[00:20:42] in fact historically as jeff mentioned
[00:20:44] the the the sort of deep learning
[00:20:47] conspiracy
[00:20:48] that that joshua jeff and i started
[00:20:51] in the early 2000s was focused on
[00:20:54] unsupervised running and super speed
[00:20:55] training and it was partly successful
[00:20:58] but we kind of put it
[00:21:01] on the back burner for a while and it's
[00:21:02] coming back to the four now
[00:21:04] it's going to create a new revolution at
[00:21:06] least that's my prediction
[00:21:08] and the next the revolution will not be
[00:21:10] supervised
[00:21:12] so i have to thank uh alyosha efros for
[00:21:15] this slogan he
[00:21:16] invented it uh of course he got inspired
[00:21:18] by
[00:21:19] jill scott heron you know the revolution
[00:21:21] will not be televised
[00:21:22] you can even get a t-shirt with it now
[00:21:24] um
[00:21:28] so what is self-supervised running
[00:21:29] really surprising is filling in the
[00:21:31] blanks
[00:21:32] and it works really well for natural
[00:21:34] language processing so natural language
[00:21:36] processing
[00:21:37] a method has become standard over the
[00:21:39] last year uh in models like bert and
[00:21:42] and others is you take a long uh
[00:21:45] sequence of words extracted from a
[00:21:47] corpus of of text
[00:21:49] you blank out uh some proportion of the
[00:21:52] words
[00:21:53] and you train a very large neural net
[00:21:55] based on those transformer architectures
[00:21:57] or various other architectures
[00:21:58] to predict the missing words and in fact
[00:22:01] it cannot exactly predict the missing
[00:22:02] word so you're
[00:22:03] asking it to predict a distribution over
[00:22:05] the entire vocabulary
[00:22:06] for the probability that every you know
[00:22:08] each word
[00:22:09] may occur at those locations
[00:22:13] so that's called that's a special case
[00:22:14] of what we call a masked auto encoder
[00:22:17] okay give it an input ask it to
[00:22:18] reconstruct with this part of input that
[00:22:20] are not that is not present
[00:22:22] people have been trying to do this in
[00:22:24] the context of image recognition
[00:22:25] as well there's these various attempts
[00:22:27] at doing this so this is word from uh
[00:22:30] pathetic at all from a few years ago
[00:22:31] where you blank out some pieces of an
[00:22:33] image
[00:22:34] and then you ask the system to fill it
[00:22:35] to fill them in and it's only partially
[00:22:37] successful not nearly as successful as
[00:22:40] in the context of natural language
[00:22:41] processing so natural language
[00:22:43] processing
[00:22:43] has been a revolution over the last year
[00:22:45] of using those pre-training systems
[00:22:48] for natural language understanding
[00:22:50] translation all kinds of stuff and
[00:22:51] the performance is amazing it they're
[00:22:53] very very big models but the performance
[00:22:55] really works really well
[00:22:56] and there were sort of early indications
[00:22:58] of this uh in
[00:22:59] work that uh joshua ventura did a long
[00:23:03] time ago in the 90s
[00:23:04] and uh roland colliber and jason weston
[00:23:07] did in the
[00:23:08] uh around 2010 uh
[00:23:11] in uh using neural nets for nlp and then
[00:23:14] more recent work work to vag fast decks
[00:23:15] etc which use this idea of predicting
[00:23:17] words from their context basically
[00:23:19] but really is sort of the this whole
[00:23:22] idea is completely taken off
[00:23:23] so why does it work for natural language
[00:23:26] processing
[00:23:27] and why does it not work so well for for
[00:23:29] in the context of images
[00:23:30] and vision i think it's because of
[00:23:34] the sort of how we represent uncertainty
[00:23:38] or how we do not represent uncertainty
[00:23:40] so let's say we want to do video
[00:23:42] prediction we
[00:23:44] we have short video clips with a few
[00:23:46] frames in this case here a little girl
[00:23:48] approaching a birthday cake
[00:23:50] and then we asked the machine to predict
[00:23:51] the next few frames in the video
[00:23:54] if you train a large neural net to
[00:23:56] predict the next few frames
[00:23:58] using least squared error you know
[00:23:59] squared error
[00:24:01] what you get are blurry predictions why
[00:24:04] because the system cannot exactly
[00:24:06] predict what's going to happen
[00:24:08] and so it the best thing you can do is
[00:24:09] predict the average of all the possible
[00:24:11] futures
[00:24:12] to be more concrete let's say all the
[00:24:14] videos consist of someone putting a pen
[00:24:16] on the table and letting it go and every
[00:24:18] time you repeat the experiment the pen
[00:24:19] falls in a different direction and you
[00:24:21] can't really predict which direction
[00:24:22] it's going to fall
[00:24:24] then if you predict the average of all
[00:24:25] the outcomes it would be a transparent
[00:24:27] pen
[00:24:29] you know superimposed on itself in all
[00:24:31] possible
[00:24:32] orientations that's not a good
[00:24:34] prediction
[00:24:36] so if you want a system to be able to
[00:24:39] represent multiple predictions it has to
[00:24:42] have what's called a little variable so
[00:24:44] you have a function
[00:24:45] implemented by neural net it takes the
[00:24:47] past let's say a few frames from a video
[00:24:49] and it wants to predict the next few
[00:24:50] frames it has to have an extra variable
[00:24:53] here it's called z
[00:24:54] so that when you vary this variable the
[00:24:56] output varies over a particular set of
[00:24:58] plausible
[00:24:59] predictions okay that's called electron
[00:25:01] variable model
[00:25:02] the problem with training those things
[00:25:04] is that there's basically only two ways
[00:25:05] of training them
[00:25:06] that we know about or two kind of uh
[00:25:09] families of
[00:25:10] uh of ways to train those systems one is
[00:25:13] a very cool idea from ian goodfellow and
[00:25:17] his collaborators in your
[00:25:18] montreal a few years ago called
[00:25:19] adversarial training or generative
[00:25:21] adversarial networks
[00:25:22] and the idea of
[00:25:24] [Music]
[00:25:26] gans during antiversal networks is to
[00:25:27] train the second neural net to tell the
[00:25:29] first neural net whether its prediction
[00:25:30] is on this
[00:25:31] manifold or or set of plausible futures
[00:25:34] or not
[00:25:34] and you train those two networks
[00:25:35] simultaneously
[00:25:39] there's another technique that consists
[00:25:41] in sort of inferring what the ideal
[00:25:43] value of the latent variable would be to
[00:25:45] make a good prediction
[00:25:47] but if you do this you have the danger
[00:25:49] that the latent variable will capture
[00:25:50] all the information there is to
[00:25:52] to capture about about the prediction
[00:25:54] and no information will actually be used
[00:25:56] from the past to make that prediction
[00:25:59] so you have to regularize this related
[00:26:01] variable okay so
[00:26:04] those ideas of things like adversarial
[00:26:07] training work really well so what you
[00:26:09] see here at the bottom
[00:26:10] is a video prediction for a small short
[00:26:12] clip where the system has been trained
[00:26:13] with this adversarial training
[00:26:15] uh and there are you know various ways
[00:26:17] of doing those uh predictions not just
[00:26:19] in pixel space but also in the space of
[00:26:21] objects that have been already segmented
[00:26:24] those adversarial genetic virtual
[00:26:26] networks can generate
[00:26:28] images that are used for kind of
[00:26:31] assistance to sort of artistic
[00:26:32] production
[00:26:33] so these are non-existing faces you have
[00:26:35] a system here that's been trained to
[00:26:37] produce an image that looks like a
[00:26:39] celebrity
[00:26:40] and after the system is trained you feed
[00:26:43] it
[00:26:43] a few hundred random numbers and that
[00:26:45] comes a face that doesn't exist
[00:26:48] and they look pretty good this is worked
[00:26:50] by nvidia from
[00:26:52] this year actually it was presented this
[00:26:54] year you can use this to produce all
[00:26:56] kinds of different things like you know
[00:27:00] clothing for example training on a
[00:27:03] collection of
[00:27:06] clothes from a famous designer um so
[00:27:09] i think we need sort of new ways of uh
[00:27:11] representing
[00:27:12] of of sort of formulating this problem
[00:27:14] with unsupervised running so that our
[00:27:15] systems can deal with this
[00:27:17] uh uncertainty in the prediction in the
[00:27:19] context of
[00:27:20] continuous high-dimensional spaces we
[00:27:22] don't have the problem in the context of
[00:27:26] adversarial of natural language
[00:27:28] processing
[00:27:29] because it's easy to represent the
[00:27:31] distribution of a words
[00:27:33] it's just a discrete distribution it's a
[00:27:34] long vector of numbers between zero and
[00:27:36] one that's sum to one
[00:27:38] but it's very hard in continuous high
[00:27:40] dimensional spaces
[00:27:41] and so we need new techniques for this
[00:27:43] and one technique i'm proposing is
[00:27:44] something called energy-based
[00:27:45] self-supervise running which is imagine
[00:27:48] that
[00:27:49] your world is two-dimensional you only
[00:27:50] have two input variables two sensors
[00:27:53] and your entire uh world your entire
[00:27:56] training set is composed of those dots
[00:27:58] here in this two-dimensional space
[00:28:00] what you'd like is to train a contrast
[00:28:03] function let's call it an energy
[00:28:04] that gives low energy to points that are
[00:28:06] on the manifold
[00:28:08] of data and higher energy outside
[00:28:11] and there is basically a lot of research
[00:28:13] to do there to find the best method to
[00:28:15] do this
[00:28:17] my favorite one is what i call
[00:28:18] regularization viable models and we had
[00:28:20] some success about 10 years ago
[00:28:22] in using techniques of this type for
[00:28:24] learning features in accomplishment
[00:28:26] completely unsupervised
[00:28:28] what you see on the left here is uh
[00:28:30] animation of a system that learns
[00:28:32] uh basically oriented filters by just
[00:28:34] being trained with natural image patches
[00:28:36] to reconstruct those under sparsity
[00:28:38] constraints uh
[00:28:39] and what you see on the right is uh
[00:28:41] filters of a convolutional net that are
[00:28:43] learned
[00:28:44] in the same with the same algorithm with
[00:28:46] different numbers of filters
[00:28:48] those things kind of work they don't
[00:28:50] beat
[00:28:51] supervisor only if you have tons of data
[00:28:53] but the hope is that
[00:28:54] they will reduce the amount of necessary
[00:28:57] label data
[00:28:59] so i'm going to end with an example of
[00:29:02] how to combine
[00:29:02] combine all this to get a machine to
[00:29:04] learn something
[00:29:07] useful like a like a task a motor task
[00:29:10] so here what i'm what i'm talking about
[00:29:12] is can we train a machine to
[00:29:15] learn to drive by just observing uh
[00:29:19] other people driving and by training a
[00:29:20] model of
[00:29:22] what goes on in the world so
[00:29:26] you are in your car you can see all the
[00:29:28] cars around you and if you can predict
[00:29:30] what the cars around you are going to do
[00:29:32] ahead of time then you can drive
[00:29:34] defensively basically you can
[00:29:36] you can decide to stay away from this
[00:29:38] car because you see it swerving
[00:29:40] you can decide to uh you know kind of
[00:29:42] slow down because the car in front of
[00:29:43] you is likely to uh to slow down because
[00:29:45] there's another car in front of it that
[00:29:47] is slowing down so you have all those
[00:29:49] predictive models that
[00:29:50] basically keep you safe and you've sort
[00:29:52] of learned to integrate them over time
[00:29:54] you don't even have to think about it
[00:29:55] it's just in your in your sort of
[00:29:57] reflexes of driving
[00:29:59] you can talk at the same time and and
[00:30:01] your your work
[00:30:05] but the way to train a system like this
[00:30:07] is you first have to train a forward
[00:30:08] model so forward model would be
[00:30:10] here is the state of the world at time t
[00:30:12] give me the a prediction about the set
[00:30:14] of the world at time t plus one
[00:30:17] and the problem with this of course is
[00:30:18] the world is not deterministic
[00:30:20] there's a lot of things that could
[00:30:21] happen so it's the same problem i was
[00:30:23] talking about with a pen
[00:30:24] many things can happen so
[00:30:27] but if you had such a forward model you
[00:30:30] could run the forward model multiple
[00:30:31] time steps and then
[00:30:35] if you had an objective function like
[00:30:38] how far you are from the other cars
[00:30:39] whether you are in lane things like this
[00:30:41] you could back propagate gradient
[00:30:43] through this entire system
[00:30:45] to train a neural net to predict the
[00:30:46] correct course of action
[00:30:48] they would uh they would be safe over
[00:30:52] the long run
[00:30:53] and this can be done completely in your
[00:30:54] head if you have a forward model in your
[00:30:56] head you don't have to actually drive
[00:30:57] to train yourself to drive you can just
[00:30:59] imagine
[00:31:00] all of those things
[00:31:04] so that's a specific example so you put
[00:31:07] a camera
[00:31:08] looking down on the highway it follows
[00:31:10] every car and it extracts a little
[00:31:12] rectangle around every car that follows
[00:31:14] every car that you see at the bottom
[00:31:16] and uh and what you're doing now is
[00:31:18] you're training a commercial net to
[00:31:20] take a few frames centered or on a
[00:31:23] particular car
[00:31:24] and predict the next state of the world
[00:31:26] and if you do this
[00:31:30] you get uh oops sorry
[00:31:39] you get the second column so the the
[00:31:41] column on the left is what happens in
[00:31:43] the real world the second column is what
[00:31:44] happens if you
[00:31:46] just train a commercial net with least
[00:31:47] square to predict what's going to happen
[00:31:49] it can only predict the average of all
[00:31:50] the possible features and so you get
[00:31:51] blurry predictions
[00:31:53] if you now transform the model so it has
[00:31:55] a latent variable that allows it to
[00:31:57] take into account the uncertainty about
[00:31:59] the world and i'm not going to explain
[00:32:00] exactly how that works
[00:32:02] then you get the the prediction that you
[00:32:03] just saw
[00:32:05] on the on the right where for every
[00:32:09] drawing of this latent variable you get
[00:32:11] different predictions but they're crisp
[00:32:14] okay so now what you can do is um you
[00:32:16] can to do this training i was telling
[00:32:18] you about earlier
[00:32:19] you sample this related variable so you
[00:32:21] get different possible scenarios about
[00:32:23] what's going to happen in your future
[00:32:24] then through back propagation you train
[00:32:26] your policy network
[00:32:28] to get your system to drive if you do
[00:32:30] this it doesn't work
[00:32:32] it doesn't work because the system goes
[00:32:33] into regions of
[00:32:35] the state space where your the forward
[00:32:37] model is very inaccurate and very
[00:32:38] uncertain
[00:32:39] so we have to do is add another term in
[00:32:42] the objective function
[00:32:43] that prevents the system from going into
[00:32:45] parts of the space where it doesn't
[00:32:46] where its predictions are bad
[00:32:48] okay so it's like an inverse curiosity
[00:32:52] constraint if you want and if you do
[00:32:54] this it works so
[00:32:55] these are examples of the blue car is
[00:32:58] driving itself the little white dot
[00:32:59] indicates whether it accelerates whether
[00:33:00] it breaks or whether it turns
[00:33:02] and it kind of keeps itself safe away
[00:33:04] from the other cars the other cars can't
[00:33:05] see it
[00:33:06] the blue car is invisible here let me
[00:33:09] show you another example here
[00:33:12] so here the yellow car is the actual car
[00:33:14] in the video the blue car is what the
[00:33:15] agent here that's been trained is
[00:33:17] uh is doing and it's being squeezed
[00:33:19] between two cars so it has to escape
[00:33:21] because the other cars don't see it
[00:33:23] so to squeeze out
[00:33:27] but it works it works reasonably well
[00:33:29] and
[00:33:30] basically that system has never
[00:33:32] interacted with the real world it's just
[00:33:34] watched other people drive
[00:33:38] and then it's used that for for training
[00:33:40] its action plans basically it's policy
[00:33:43] okay now i'm going to go a little uh
[00:33:47] philosophical if you want there is
[00:33:50] throughout history of technology and
[00:33:52] science there's been this phenomenon
[00:33:54] it's not universal but it's pretty
[00:33:56] frequent where people invent an artifact
[00:33:58] and then derive a science out of this
[00:34:00] artifact to explain
[00:34:02] how this artifact works or to kind of
[00:34:06] figure out its limitations so a good
[00:34:07] example is the invention of the
[00:34:08] telescope
[00:34:10] in the 1600s optics was not developed
[00:34:12] until at least 50 years later
[00:34:15] but people had a good intuition of how
[00:34:17] to build telescopes before that
[00:34:19] steam engine was invented in the late
[00:34:21] 1600s early 1700s
[00:34:24] and thermodynamics was you know came up
[00:34:26] more than 100 years later
[00:34:27] basically designed to explain the
[00:34:30] limitations
[00:34:31] of thermal engines and thermodynamics
[00:34:34] now is the foundation of
[00:34:35] one of the most fundamental intellectual
[00:34:37] construction of all science
[00:34:39] so it was purposely defined to
[00:34:42] explain a particular artifact that's
[00:34:44] very interesting
[00:34:47] same thing with electromagnetism
[00:34:48] electrodynamics with uh
[00:34:50] you know the invention of sailboats and
[00:34:52] airplanes and aerodynamics
[00:34:53] uh uh you know invention of compounds
[00:34:57] and
[00:34:57] chemistry to explain et cetera right
[00:35:00] computers
[00:35:00] and computer science came after the
[00:35:02] inventory of computers right
[00:35:04] information theory came after the
[00:35:06] invention of first digital communication
[00:35:09] through radio and data type and things
[00:35:11] like that
[00:35:12] so it's quite possible that now we have
[00:35:16] you know in the next few decades we'll
[00:35:18] have
[00:35:19] empirical systems that are built by
[00:35:22] trial and error perhaps by
[00:35:23] systematic optimization on powerful
[00:35:25] machines perhaps by intuitions
[00:35:28] by empirical work perhaps with a little
[00:35:31] bit of theory
[00:35:33] perhaps a lot of theory hopefully and
[00:35:36] the question is whether this will lead
[00:35:38] to
[00:35:38] a whole theory of intelligence
[00:35:42] the fact that we can build an artifact
[00:35:44] that is intelligent
[00:35:45] might lead to a general theory of
[00:35:48] information processing and intelligence
[00:35:50] um and that's kind of a big hope
[00:35:54] i'm not sure this is going to be
[00:35:55] realized over the next few decades but
[00:35:57] that's a good program a word of caution
[00:36:01] about biological inspiration so neural
[00:36:03] nets are biologically inspired cognition
[00:36:04] nets are biologically inspired but
[00:36:06] they're just inspired they're not copied
[00:36:08] let me give you a story of a gentleman
[00:36:11] called clement idea
[00:36:12] uh is there any french people in the
[00:36:13] room here okay
[00:36:15] can you raise your hand french people no
[00:36:17] french people yeah okay a couple
[00:36:19] have you heard of climate idea
[00:36:23] never heard of cleveland right there
[00:36:24] yeah you have okay
[00:36:26] is there anyone who is not french who
[00:36:27] have heard of clemon idea
[00:36:30] okay one person two person
[00:36:33] basically nobody you guys have no idea
[00:36:35] who he is right okay
[00:36:36] so this guy built in the late 1800s
[00:36:41] a bat-shaped airplane steam-powered
[00:36:44] he was a steam engine designer and his
[00:36:47] airplane actually took off
[00:36:48] on his own power 13 years before the
[00:36:51] wright brothers
[00:36:52] flew for about 50 meters at about 50
[00:36:54] centimeters altitude
[00:36:56] and then kind of crashed landed
[00:36:59] um it was basically uncontrollable so
[00:37:02] basically the guy just copied bats and
[00:37:03] just assumed that because it has the
[00:37:05] shape of a bat it would just fly
[00:37:07] right that seemed a little bit naive it
[00:37:09] was not naive at all but it was it kind
[00:37:11] of
[00:37:12] you know stuck a little bit too close to
[00:37:13] biology and and got sort of hypnotized
[00:37:15] by it a little bit
[00:37:17] and didn't do things like you know build
[00:37:19] a model or a glider
[00:37:21] or a kite or you know a wind tunnel like
[00:37:25] the
[00:37:25] like the red brothers did so he stuck a
[00:37:28] little too close to biology
[00:37:30] on the other hand he had a big legacy
[00:37:32] which is that
[00:37:33] his second airplane was called the avion
[00:37:35] and that's actually the word in french
[00:37:38] spanish and portuguese for airplane so
[00:37:41] he had some legacy
[00:37:42] um but he was kind of a secretive guy he
[00:37:45] you know this was before the open source
[00:37:46] days
[00:37:47] and so this is why you never heard of
[00:37:49] him
[00:37:51] thank you very much
