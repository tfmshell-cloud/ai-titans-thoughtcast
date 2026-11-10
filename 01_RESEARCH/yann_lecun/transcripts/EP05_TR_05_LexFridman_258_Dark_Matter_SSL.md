# Lex Fridman #258: Yann LeCun — Dark Matter of Intelligence & SSL
- **YouTube URL:** https://www.youtube.com/watch?v=SGzMElJ11Cc
- **Lines:** 5258

---

[00:00:00] The following is a conversation with
[00:00:01] Yann LeCun, his second time on the
[00:00:03] podcast. He is the chief AI scientist at
[00:00:06] Meta, formerly Facebook, professor at
[00:00:10] NYU, Turing Award winner, one of the
[00:00:13] seminal figures in the history of
[00:00:15] machine learning and artificial
[00:00:17] intelligence, and someone who is
[00:00:19] brilliant and opinionated in the best
[00:00:22] kind of way, and so is always fun to
[00:00:24] talk to.
[00:00:26] This is the Lex Fridman podcast. To
[00:00:28] support it, please check out our
[00:00:29] sponsors in the description. And now,
[00:00:31] here's my conversation with Yann LeCun.
[00:00:36] You co-wrote the article Self-Supervised
[00:00:38] Learning: The Dark Matter of
[00:00:39] Intelligence. Great title, by the way.
[00:00:42] With Ishan Misra. So, let me ask, what
[00:00:44] is self-supervised learning and why is
[00:00:47] it the dark matter of intelligence?
[00:00:49] I'll start by the dark matter part.
[00:00:52] Uh
[00:00:53] there is obviously a kind of learning
[00:00:55] that humans and animals are
[00:00:58] uh are doing that we currently are not
[00:01:01] reproducing properly with machines with
[00:01:03] AI, right? So, the most popular
[00:01:05] approaches to machine learning today are
[00:01:08] or paradigms, I should say, are
[00:01:09] supervised learning and reinforcement
[00:01:11] learning.
[00:01:12] And they're extremely efficient.
[00:01:15] Supervised learning requires many
[00:01:16] samples for learning anything.
[00:01:19] And reinforcement learning requires a
[00:01:21] ridiculously large number of trial and
[00:01:24] errors to for, you know, a system to
[00:01:26] learn anything.
[00:01:27] Um
[00:01:29] and that's why we don't have
[00:01:30] self-driving cars.
[00:01:32] That's a big leap from one to the other.
[00:01:34] Okay, so that to solve difficult
[00:01:37] problems, you have to have a lot of uh
[00:01:40] human annotation for supervised learning
[00:01:43] to work, and to solve those difficult
[00:01:45] problems with the reinforcement
[00:01:46] learning, you have to have
[00:01:47] some way to maybe simulate that problem
[00:01:50] such that you can do that large-scale
[00:01:51] kind of learning that reinforcement
[00:01:53] learning requires.
[00:01:54] Right. So, how is it that, you know,
[00:01:57] most teenagers can learn to drive a car
[00:01:58] in about 20 hours of practice?
[00:02:02] Whereas,
[00:02:03] even with millions of hours of simulated
[00:02:06] practice, a self-driving car can't
[00:02:08] actually learn to drive itself properly.
[00:02:11] And so, obviously we're missing
[00:02:13] something, right? And And it's quite
[00:02:14] obvious for a lot of people that, you
[00:02:16] know, the immediate response you get
[00:02:17] from many people is, well, you know,
[00:02:20] humans use their background knowledge
[00:02:22] to learn faster. And they're right.
[00:02:25] Now, how was that background knowledge
[00:02:27] acquired? And that's to be questioned.
[00:02:30] So, now you have to ask, you know, how
[00:02:32] do babies in the first few months of
[00:02:34] life learn how the world works? Mostly
[00:02:37] by observation, because they can hardly
[00:02:39] act in the world.
[00:02:40] And they learn an enormous amount of
[00:02:42] background knowledge about the world
[00:02:43] that may be the the basis of what we
[00:02:46] call common sense.
[00:02:47] This type of learning
[00:02:49] is not learning a task, it's not being
[00:02:52] reinforced for anything, it's just
[00:02:54] observing the world and figuring out how
[00:02:56] it how it works.
[00:02:58] Building world models, learning world
[00:03:00] models.
[00:03:01] How do we do this? And how do we
[00:03:03] reproduce this in in machines? So,
[00:03:04] self-supervised learning
[00:03:06] is,
[00:03:07] you know, one
[00:03:09] instance or one attempt at trying to
[00:03:10] reproduce this kind of learning.
[00:03:13] Okay, so you're looking at just
[00:03:15] observation. So, not even the
[00:03:16] interacting part of a child. It's just
[00:03:19] sitting there watching mom and dad walk
[00:03:21] around, pick up stuff, all of that.
[00:03:23] That's the That's what we mean about
[00:03:24] background knowledge.
[00:03:25] Perhaps even watching mom and dad, just,
[00:03:27] you know, watching the world go by.
[00:03:29] Just having eyes open or having eyes
[00:03:31] closed, or the very act of opening and
[00:03:33] closing eyes
[00:03:34] that the world appears and disappears,
[00:03:36] all of that basic information.
[00:03:39] And you're saying in in order to learn
[00:03:41] to drive,
[00:03:43] like the reason humans are able to learn
[00:03:44] to drive quickly, some faster than
[00:03:46] others, is because of the background
[00:03:48] knowledge. They were able to watch cars
[00:03:49] operate in the world
[00:03:51] in the many years of leading up to it,
[00:03:53] the physics of basic objects, all that
[00:03:55] kind of stuff.
[00:03:55] That's right. I mean, the basic physics
[00:03:56] of objects, you don't even know you you
[00:03:58] don't even need to know, you know, how a
[00:04:00] car works, right? Because that you can
[00:04:01] learn fairly quickly. I mean, the
[00:04:02] example I use very often is you're
[00:04:04] driving next to a cliff.
[00:04:06] And you know in advance because of your
[00:04:09] you know, understanding of intuitive
[00:04:11] physics that if you turn the wheel to
[00:04:13] the right, the car will veer to the
[00:04:14] right or run off the cliff,
[00:04:16] fall off the cliff, and nothing good
[00:04:18] will come out of this, right?
[00:04:19] Um but if you are a sort of
[00:04:22] you know, tabular rasa reinforcement
[00:04:24] learning system that doesn't have a
[00:04:25] model of the world,
[00:04:27] uh you have to repeat falling off this
[00:04:29] cliff thousands of times before you
[00:04:31] figure out it's a bad idea. And then a
[00:04:33] few more thousand times before you
[00:04:34] figure out how to not do it.
[00:04:37] And then a few more million times before
[00:04:38] you figure out how to not do it in every
[00:04:40] situation you ever encounter.
[00:04:42] So, self-supervised learning still has
[00:04:44] to have some source of truth
[00:04:48] being told to it by somebody.
[00:04:50] And this
[00:04:50] So, you have to figure out a way without
[00:04:52] human assistance or without significant
[00:04:55] amount of human assistance to get that
[00:04:57] truth from the world. So, the mystery
[00:05:00] there is um
[00:05:01] how much signal is there, how much truth
[00:05:04] is there that the world gives you,
[00:05:06] whether it's the human world,
[00:05:08] like you watch YouTube or something like
[00:05:09] that, or it's the more natural world.
[00:05:12] So, how much signal is there?
[00:05:14] So, here's the trick. There is way more
[00:05:17] signal
[00:05:18] in sort of a self-supervised setting
[00:05:20] than there is in either a supervised or
[00:05:22] reinforcement setting.
[00:05:24] And this is going to my, you know,
[00:05:26] analogy of the cake.
[00:05:28] Yes.
[00:05:29] The you know, local cake has someone,
[00:05:31] let's call it, where
[00:05:33] when you try to figure out how much
[00:05:34] information you ask the machine to
[00:05:37] predict and how much feedback you give
[00:05:38] the machine at every trial,
[00:05:40] in reinforcement learning, you give the
[00:05:42] machine a single scalar. You tell the
[00:05:43] machine you did good, you did bad. And
[00:05:45] you and you and you only
[00:05:47] tell this to the machine once in a
[00:05:48] while.
[00:05:49] When I say you, it could be the the
[00:05:50] universe telling the machine, right?
[00:05:52] Um
[00:05:54] but it's just one scalar. And so, as a
[00:05:56] consequence, there is you you cannot
[00:05:57] possibly learn something very
[00:05:58] complicated without many many many
[00:06:00] trials where you get many many feedbacks
[00:06:03] uh of this type. Supervised learning,
[00:06:05] you you give a few bits to the machine
[00:06:08] uh at every every sample.
[00:06:11] Let's say you're training a
[00:06:13] system on, you know, recognizing images
[00:06:15] on ImageNet. There's 1,000 categories.
[00:06:17] That's a little less than 10 bits of
[00:06:19] information per sample.
[00:06:22] Besides supervised learning, here is a
[00:06:23] setting. You Ideally, we don't know how
[00:06:25] to do this yet, but ideally, you would
[00:06:28] show a machine a segment of a video and
[00:06:31] then stop the video and ask ask the
[00:06:33] machine to predict what's going to
[00:06:34] happen next.
[00:06:37] And so, you let the machine predict, and
[00:06:38] then you let time go by and uh show the
[00:06:42] machine what actually happened, and hope
[00:06:44] the machine will, you know, learn to do
[00:06:47] a better job at predicting next time
[00:06:48] around. There's a huge amount of
[00:06:50] information you give the machine because
[00:06:51] it's an entire video clip. It's a of uh
[00:06:55] you know, the of the the future after
[00:06:57] the video clip you fed it um
[00:06:59] in the first place.
[00:07:00] So, both for language and for vision,
[00:07:02] there's a subtle, seemingly trivial
[00:07:06] construction, but maybe that's
[00:07:07] representative of what is required to
[00:07:09] create intelligence, which is
[00:07:11] filling the gap.
[00:07:13] So,
[00:07:15] It
[00:07:16] sounds dumb, but can you
[00:07:18] is it's
[00:07:19] it is possible you can solve all of
[00:07:21] intelligence in this way. Just for both
[00:07:23] language,
[00:07:25] just
[00:07:26] give a sentence and continue it, or give
[00:07:29] a sentence and there's a gap in it, uh
[00:07:32] some words blanked out, and you fill in
[00:07:34] what words go there.
[00:07:35] For vision, you give a sequence of
[00:07:37] images
[00:07:39] and predict what's going to happen next,
[00:07:40] or you fill in what happened in between.
[00:07:43] Do you think it's possible that
[00:07:45] formulation alone
[00:07:48] as a signal for self-supervised learning
[00:07:50] can solve intelligence for vision and
[00:07:52] language?
[00:07:53] I think that's a good shot at the
[00:07:54] moment. Um so, whether this will
[00:07:58] take us all the way to, you know,
[00:08:00] human-level intelligence or something or
[00:08:01] just cat-level intelligence
[00:08:03] uh is not clear, but among all the
[00:08:06] possible approaches that people have
[00:08:07] proposed, I think it's a good shot. So,
[00:08:10] I think this idea of
[00:08:12] uh uh an intelligence system filling in
[00:08:15] the blanks, either, you know, predicting
[00:08:17] the future, inferring the past, filling
[00:08:20] in missing information,
[00:08:22] uh you know, I'm currently filling the
[00:08:24] blank of what is behind your head and
[00:08:26] what you what your head looks like and,
[00:08:28] you know, from from the back uh because
[00:08:30] I have, you know, basic knowledge about
[00:08:32] how humans are made. And I don't know if
[00:08:34] you're going to, you know, what what are
[00:08:35] you going to say, at which point you're
[00:08:36] going to speak, whether you're going to
[00:08:37] move your head this way or that way,
[00:08:38] which way you're going to look, but I
[00:08:40] know you're not going to just
[00:08:41] dematerialize and reappear 3 m uh
[00:08:44] down the hole uh you know, because I
[00:08:47] know what's possible and what's
[00:08:48] impossible uh according to intuitive
[00:08:50] physics. So,
[00:08:51] have a model of what's possible and
[00:08:52] what's impossible, and then you'd be
[00:08:53] very surprised if it happens, and then
[00:08:55] then you'll have to reconstruct your
[00:08:56] model.
[00:08:57] Right. So, that that's the model of the
[00:08:59] world. It's what tells you, you know,
[00:09:01] what fills in the blanks. It's a given
[00:09:02] your partial information about the state
[00:09:04] of the world given by your perception,
[00:09:07] uh your your model of the world fills in
[00:09:10] the missing information, and that
[00:09:11] includes predicting the future,
[00:09:13] re-predicting the past, uh you know,
[00:09:16] filling in things you don't immediately
[00:09:17] perceive.
[00:09:18] And that doesn't have to be purely
[00:09:20] generic vision or visual information or
[00:09:23] generic language. You can go to
[00:09:24] specifics like uh
[00:09:27] predicting what control decision you'll
[00:09:29] make when you're driving in a lane. You
[00:09:31] have a sequence of images uh from a a
[00:09:34] vehicle,
[00:09:35] and then you can you have information if
[00:09:38] you recorded on video where the car
[00:09:40] ended up going. So, you can go back in
[00:09:42] time and predict where the car went
[00:09:45] based on the visual information. That's
[00:09:46] very specific, domain-specific.
[00:09:49] Right, but the question is whether we
[00:09:50] can come up with sort of a generic
[00:09:53] uh
[00:09:54] method uh for you know, training
[00:09:56] machines to do this kind of uh
[00:09:58] prediction or filling in the blanks. So,
[00:10:00] right now
[00:10:01] uh
[00:10:02] this type of approach has been
[00:10:03] unbelievably successful in the context
[00:10:06] of natural language processing. Uh every
[00:10:08] model in natural language processing is
[00:10:09] pre-trained in self-supervised manner
[00:10:12] to fill in the blanks. So, you you show
[00:10:14] it a sequence of words, you remove 10%
[00:10:15] of them, and then you train some
[00:10:17] gigantic neural net to predict the words
[00:10:18] that are missing.
[00:10:19] That and once you've pre-trained that
[00:10:22] network, you can use the
[00:10:24] internal representation learned by it as
[00:10:26] input to, you know, uh something that
[00:10:29] you train supervised or or whatever.
[00:10:31] Um that's been incredibly successful,
[00:10:33] not so successful in images, although
[00:10:35] it's making progress.
[00:10:37] And uh and it's it's based on uh sort of
[00:10:40] manual data augmentation.
[00:10:42] Uh we can go into this later, but what
[00:10:44] has not been successful yet is training
[00:10:46] from video. So, getting a machine to
[00:10:48] learn to represent the visual world, for
[00:10:50] example, by just watching video. Nobody
[00:10:52] has really succeeded in doing this.
[00:10:54] Okay, well, let's kind of give a
[00:10:56] high-level overview. What's the
[00:10:57] difference in uh kind and in difficulty
[00:11:02] between vision and language? So, you
[00:11:04] said people haven't been able to
[00:11:07] really kind of crack the problem of
[00:11:09] vision open in terms of self-supervised
[00:11:11] learning, but that may not be
[00:11:13] necessarily because it's fundamentally
[00:11:14] more difficult. Maybe, like when we're
[00:11:17] talking about achieving like passing
[00:11:20] the Turing test in the full spirit of
[00:11:22] the Turing test in language might be
[00:11:24] harder than vision. That's That's not
[00:11:25] obvious. So, what In your view, what
[00:11:27] which is harder
[00:11:29] or perhaps are they just the same
[00:11:30] problem? When uh
[00:11:33] the farther we get to solving each, the
[00:11:34] more we realize it's all the same thing.
[00:11:36] It's all the same cake.
[00:11:37] I think
[00:11:39] what I'm looking for are methods that
[00:11:40] make make them look
[00:11:42] essentially like the same cake, but
[00:11:43] currently they're not. And the main
[00:11:45] issue
[00:11:46] with learning world models or learning
[00:11:48] predictive models
[00:11:50] is that uh the prediction is never a
[00:11:53] single uh thing uh cuz the world is not
[00:11:56] entirely predictable.
[00:11:59] Yeah.
[00:11:59] It may be deterministic because it's
[00:12:00] stochastic. We can get into the
[00:12:01] philosophical discussion about it, but
[00:12:03] uh
[00:12:04] but even if it's deterministic, it's not
[00:12:05] entirely predictable.
[00:12:07] And so,
[00:12:08] if I play
[00:12:10] a short video clip, and then I ask you
[00:12:12] to predict what's going to happen next,
[00:12:14] there's many, many plausible
[00:12:15] continuations for that uh video clip,
[00:12:18] and the number of continuation grows
[00:12:20] with the
[00:12:22] interval of time that you're asking the
[00:12:23] system to make a prediction uh for.
[00:12:26] And so, one big question with our
[00:12:29] supervised learning is how you represent
[00:12:31] this uncertainty, how you represent
[00:12:33] multiple discrete outcomes, how you
[00:12:35] represent a sort of continuum of
[00:12:37] possible outcomes,
[00:12:38] um etc. And, you know, if you are a sort
[00:12:42] of a a classical machine learning
[00:12:44] person, you say, "Oh, you just represent
[00:12:46] a distribution, right?"
[00:12:49] And that we know how to do
[00:12:51] when we're predicting words, missing
[00:12:52] words in a text, because uh you can have
[00:12:55] a neural net give a score for every word
[00:12:57] in a dictionary. It's a big, you know,
[00:12:59] it's a big list of numbers, you know,
[00:13:00] 100,000 or so.
[00:13:02] You can turn them into a a probability
[00:13:04] distribution that gives that tells you,
[00:13:06] "When I say a sentence, you know, the
[00:13:09] you know, the cat is chasing the blank
[00:13:11] in the kitchen."
[00:13:12] You know, there are only a few words
[00:13:14] that make sense there, you know? It
[00:13:15] could be a mouse, it could be a lizard,
[00:13:17] a spot, or you know, something like
[00:13:19] that, right?
[00:13:20] Uh
[00:13:21] and and if I if I say the the blank is
[00:13:24] chasing the blank in in
[00:13:25] you also have a bunch of plausible
[00:13:27] options for those two words, right?
[00:13:29] Um that that that because you you have
[00:13:31] kind of a you know, underlying reality
[00:13:33] that you can refer to to sort of fill in
[00:13:35] those those blanks.
[00:13:37] Um
[00:13:38] so
[00:13:39] you cannot say for sure in the Savannah
[00:13:41] if it's a you know, a lion or a cheetah
[00:13:43] or whatever. You cannot know if it's a
[00:13:46] zebra or gnu or you know, whatever.
[00:13:49] Wildebeest, same thing. Um
[00:13:52] but uh
[00:13:55] but you can represent the uncertainty by
[00:13:56] just a long list of numbers. Now,
[00:13:59] if I if I do the same thing with video
[00:14:01] and I ask you to predict a video clip,
[00:14:04] it's not a discrete set of potential
[00:14:06] frames. You have to have
[00:14:08] somewhere representing a sort of
[00:14:10] infinite number of plausible
[00:14:12] continuations of multiple frames in a
[00:14:15] you know, high-dimensional continuous
[00:14:16] space.
[00:14:17] And we just have no idea how to do this
[00:14:18] properly.
[00:14:20] Uh finite high-dimensional.
[00:14:22] So like you cuz
[00:14:23] It's finite high-dimensional, yes.
[00:14:25] Just like the words. They try to get it
[00:14:27] to uh
[00:14:28] down to
[00:14:30] a a small finite set of like under a
[00:14:32] million, something like that.
[00:14:34] Something like that.
[00:14:34] I mean, it's kind of ridiculous that
[00:14:37] we're doing a distribution over every
[00:14:39] single possible word for language and it
[00:14:42] works. It feels like that's a really
[00:14:44] dumb way to do it.
[00:14:45] Um like there seems to there there it
[00:14:48] seems to be like there should be some
[00:14:50] more
[00:14:51] compressed representation of the
[00:14:53] distribution over the words.
[00:14:55] You're right about that.
[00:14:56] And so
[00:14:57] do you have any interesting ideas about
[00:14:59] how to represent all of reality in a
[00:15:01] compressed way so that you can form a
[00:15:02] distribution over it?
[00:15:03] That's one of the big questions, you
[00:15:04] know, how do you how do you do that?
[00:15:06] Right? I mean, what's what's kind of you
[00:15:07] know, another thing that that really is
[00:15:10] stupid about um I shouldn't say stupid,
[00:15:12] but like simplistic about current
[00:15:14] approaches to self-supervised learning
[00:15:16] in in uh NLP in text
[00:15:19] is that not only do you represent a
[00:15:21] joint distribution over words, but for
[00:15:24] multiple words that are missing, those
[00:15:25] distributions are essentially
[00:15:26] independent of each other.
[00:15:29] Um, and you know, you don't pay too much
[00:15:31] of a price for this. So, you So, you
[00:15:33] can't So, the you know, the system you
[00:15:36] know, in the the the sentence that I
[00:15:37] gave earlier
[00:15:39] uh, if it gives a a certain probability
[00:15:41] for a lion and and uh, cheetah and then
[00:15:43] a certain probability for uh, you know,
[00:15:46] gazelle, uh,
[00:15:47] wildebeest and and and zebra.
[00:15:50] Uh,
[00:15:51] those two probabilities are independent
[00:15:54] of each other.
[00:15:55] Uh, and it's not the case that those
[00:15:57] things are independent. Lions actually
[00:15:58] attack like bigger animals than than
[00:16:00] cheetahs. So, you know, there's a huge
[00:16:03] independence hypothesis in in this uh,
[00:16:05] process which is not actually true. The
[00:16:07] reason for this is that we don't know
[00:16:09] how to represent uh,
[00:16:11] properly distributions over
[00:16:13] combinatorial uh,
[00:16:14] sequences of symbols essentially when
[00:16:16] they're because the number grows
[00:16:18] exponentially with the length of the of
[00:16:20] the symbols. And so, we have to use
[00:16:22] tricks for this, but um,
[00:16:23] those techniques can't, you know, get
[00:16:25] around like don't even deal with it. So,
[00:16:28] So, the big question is like would there
[00:16:30] be some sort of abstract
[00:16:33] latent representation of text that would
[00:16:35] say that, you know, when I when I switch
[00:16:39] lion for gazelle, uh, lion for cheetah,
[00:16:42] I also have to switch zebra for gazelle.
[00:16:45] Yeah, so
[00:16:46] this independence assumption let me
[00:16:48] throw some criticism at you that I often
[00:16:50] hear and see how you respond. So, this
[00:16:53] kind of filling in the blanks is just
[00:16:55] statistics. You're not learning anything
[00:16:58] like the deep underlying concepts.
[00:17:01] You're just mimicking stuff from
[00:17:05] the past. You're not learning anything
[00:17:07] new such that you can use it to
[00:17:08] generalize about the world.
[00:17:11] Um, or Okay, let me just say the crude
[00:17:13] version which is it's just statistics.
[00:17:16] It's not intelligence. Uh, what do you
[00:17:18] have to say to that? What do you usually
[00:17:20] say to that if you kind of hear this
[00:17:21] kind of thing?
[00:17:22] I don't get into those discussions
[00:17:23] because they are the kind of pointless.
[00:17:26] So, first of all, it's quite possible
[00:17:28] that intelligence is just statistics.
[00:17:30] It's just statistics of a particular
[00:17:31] kind.
[00:17:32] Yes.
[00:17:33] But this is the philosophical question.
[00:17:35] It's It's kind of is Is intel- Is it
[00:17:37] possible that intelligence is just
[00:17:39] statistics?
[00:17:40] Yeah.
[00:17:41] But what kind of statistics? So,
[00:17:44] if you are asking the question
[00:17:47] are the model of the world, the models
[00:17:48] of the world that we learn,
[00:17:50] do they have some notion of causality?
[00:17:52] Yes.
[00:17:52] Mhm.
[00:17:53] So, if the criticism comes from people
[00:17:55] who say, you know, current machine
[00:17:57] learning system don't care about
[00:17:58] causality, which by the way is wrong,
[00:18:00] you know, I agree with them. Yeah, you
[00:18:03] should you know, your model of the world
[00:18:05] should have your actions as one of your
[00:18:07] of the inputs
[00:18:09] and that will drive you to learn causal
[00:18:10] models of the world where you know what,
[00:18:12] you know, what intervention in the world
[00:18:15] will cause what result. Or you can do
[00:18:17] this by observation of other agents
[00:18:19] acting in the world and and observing
[00:18:21] the effect
[00:18:22] other humans, for example. So, I think
[00:18:26] you know, at some level of description,
[00:18:28] intelligence is just statistics.
[00:18:30] But that doesn't mean you don't you
[00:18:33] don't you know, you won't have models
[00:18:35] that have, you know, deep mechanistic
[00:18:37] explanation for what goes on. The
[00:18:40] question is how do you learn them?
[00:18:41] That's That's the question I'm
[00:18:42] interested in.
[00:18:43] Because
[00:18:45] you know, a lot of people who actually
[00:18:47] voice that criticism
[00:18:49] say that those mechanistic model has to
[00:18:51] have to come from someplace else. They
[00:18:52] have to come from human designers, they
[00:18:54] have to come from I don't know what. And
[00:18:56] obviously, we learn them.
[00:18:58] Or if we don't learn them as an
[00:19:00] individual, nature
[00:19:03] learn them for us using evolution. So,
[00:19:05] regardless of what you think, those
[00:19:07] processes have been learned somehow.
[00:19:10] So, if you look at the the human brain,
[00:19:12] just like when we humans introspect
[00:19:14] about how the brain works, it seems like
[00:19:17] when we think about what is
[00:19:18] intelligence, we think about the
[00:19:21] high-level stuff like the models we've
[00:19:23] constructed, concepts like cognitive
[00:19:25] science, the concepts of memory and
[00:19:27] reasoning module, almost like these
[00:19:29] high-level modules.
[00:19:31] Is there's Is this serve as a good
[00:19:33] analogy?
[00:19:35] Like, are we ignoring the uh
[00:19:39] the dark matter, the the basic low-level
[00:19:42] mechanisms, just like we ignore the way
[00:19:44] the operating system works? We're just
[00:19:46] using the
[00:19:47] uh the the high-level software. We're
[00:19:49] ignoring that at the low level, the
[00:19:52] neural network might be doing something
[00:19:54] like statistics.
[00:19:56] Like, meaning uh sorry to use this word
[00:19:59] probably incorrectly and crudely, but
[00:20:01] doing this kind of filling the gap kind
[00:20:02] of learning and just kind of updating
[00:20:04] the model constantly in order to be able
[00:20:06] to support the raw sensory information
[00:20:08] information to predict it and then
[00:20:10] adjust to the prediction when it's
[00:20:11] wrong. But, like, high-level when we
[00:20:13] look at our brain at the high level, it
[00:20:15] feels like we're doing like we're
[00:20:17] playing chess, like we're we're like
[00:20:20] playing with high-level concepts and
[00:20:22] we're stitching them together and we're
[00:20:23] putting them into long-term memory. But,
[00:20:26] really what's going underneath is
[00:20:28] something we're not able to introspect,
[00:20:30] which is this kind of
[00:20:31] uh simple large neural network that's
[00:20:34] just filling in the gaps.
[00:20:35] Right. Well, okay, so there's a lot of
[00:20:37] questions and a lot of answers there.
[00:20:39] Okay, so first of all, there's a whole
[00:20:40] school of thought in neuroscience,
[00:20:42] computational neuroscience in
[00:20:43] particular,
[00:20:44] um that likes the idea of predictive
[00:20:47] coding, which is really related to the
[00:20:49] idea I was talking about in
[00:20:50] self-supervised learning. So, everything
[00:20:52] is about prediction. The essence of
[00:20:54] intelligence is the ability to predict.
[00:20:55] Yeah.
[00:20:56] And everything the brain does is trying
[00:20:57] to predict
[00:20:59] uh predict everything from everything
[00:21:01] else. Okay, and that that's really sort
[00:21:03] of the underlying principle, if you
[00:21:04] want, that uh self-supervised learning
[00:21:07] is trying to kind of reproduce this idea
[00:21:09] of prediction as kind of an essential
[00:21:11] mechanism
[00:21:13] of uh task-independent learning, if you
[00:21:15] want.
[00:21:16] The next step is
[00:21:18] what kind of intelligence are you
[00:21:19] interested in reproducing? And of
[00:21:21] course, you know, we all think about,
[00:21:23] you know, trying to reproduce sort of,
[00:21:25] you know, high-level cognitive processes
[00:21:27] in humans,
[00:21:28] but like with machines, we're not even
[00:21:29] at the level of
[00:21:31] even reproducing the
[00:21:33] learning processes in a in a cat brain.
[00:21:36] Um you know, the most intelligent of our
[00:21:38] intelligent systems don't don't have as
[00:21:39] much common sense as as a house cat.
[00:21:43] So um how is it that cats learn? And you
[00:21:45] know, cats don't do a whole lot of uh
[00:21:47] reasoning. They certainly have causal
[00:21:48] models. They certainly have
[00:21:51] uh because, you know, many cats can
[00:21:52] figure out like how they can act on the
[00:21:54] world to get what they want. Um
[00:21:56] they certainly have uh a fantastic model
[00:21:59] of intuitive physics, uh certainly of
[00:22:02] their the the the dynamics of their own
[00:22:04] bodies, but but also of prey and things
[00:22:06] like that, right? So
[00:22:07] um they they're they're pretty smart.
[00:22:09] They they only do this with about 800
[00:22:11] million neurons.
[00:22:13] Um we are not anywhere close to
[00:22:16] reproducing this kind of uh thing. So to
[00:22:18] some extent, I I could I could say,
[00:22:21] let's not even worry about like the
[00:22:23] high-level cognition
[00:22:25] uh
[00:22:26] and kind of, you know, long-term
[00:22:27] planning and reasoning that humans can
[00:22:28] do until we figure out like, you know,
[00:22:30] can we even reproduce what cats are
[00:22:31] doing?
[00:22:32] Now that said, this ability to
[00:22:35] learn world models, I think is the key
[00:22:38] to the possibility of learning machines
[00:22:41] that can also reason.
[00:22:43] So whenever I give a talk, I say there
[00:22:44] are there are three challenges in the
[00:22:45] three main challenges in machine
[00:22:46] learning. The first one is
[00:22:48] uh you know, getting machines to learn
[00:22:49] to represent the world, um and I'm
[00:22:52] proposing self-supervised learning.
[00:22:54] Uh
[00:22:54] the second is uh getting machines to
[00:22:57] reason in ways that are compatible with
[00:23:00] essentially gradient-based learning,
[00:23:01] because this is what deep learning is
[00:23:02] all about, really.
[00:23:04] Um and the third one is something we
[00:23:06] have no idea how to solve, at least I
[00:23:07] have no idea how to solve. Is uh
[00:23:11] can we get machines to learn
[00:23:12] hierarchical representations of action
[00:23:15] plans?
[00:23:17] You know, like you know, we know how to
[00:23:18] train them to learn hierarchical
[00:23:19] representations of perception.
[00:23:22] You know, with convolutional nets and
[00:23:23] things like that and transformers.
[00:23:25] But what about action plans? Can we uh
[00:23:26] get them to spontaneously learn good
[00:23:28] hierarchical representations of actions?
[00:23:30] Also gradient-based.
[00:23:32] Yeah, all of that has, you know, needs
[00:23:34] to be somewhat differentiable so that
[00:23:36] you can apply sort of gradient-based
[00:23:37] learning, uh which is really what deep
[00:23:39] learning is about.
[00:23:42] So it's background knowledge, ability to
[00:23:46] reason in a way
[00:23:48] uh that's differentiable that
[00:23:51] is somehow connected, deeply integrated
[00:23:53] with that background knowledge, or
[00:23:55] builds on top of that background
[00:23:56] knowledge, and then given that
[00:23:58] background knowledge, be able to make
[00:23:59] hierarchical plans.
[00:24:01] Right.
[00:24:02] So if if you take classical optimal
[00:24:04] control, there's something in classical
[00:24:06] optimal control called uh model
[00:24:09] predictive control. And it's, you know,
[00:24:11] it's been around since the the early
[00:24:12] '60s.
[00:24:13] NASA uses that to compute trajectories
[00:24:15] of rockets. And the basic idea is that
[00:24:17] you have a pre- a predictive model
[00:24:20] of the rocket, let's say, or whatever
[00:24:22] system you are you intend to control,
[00:24:25] which, given the state of the system at
[00:24:27] time t and given an action
[00:24:30] that you're taking in the system, so for
[00:24:32] a rocket it would be thrust and, you
[00:24:33] know, all the controls you can have.
[00:24:36] Uh it gives you the state of the system
[00:24:37] at time t plus delta t, right? So
[00:24:39] basically a differential equation,
[00:24:40] something like that.
[00:24:42] Um
[00:24:44] and if you have this model, and you have
[00:24:46] this model in the form of some sort of
[00:24:48] neural net or some sort of uh set of
[00:24:51] formula that you can back propagate
[00:24:52] gradient through, you can do what's
[00:24:54] called model predictive control.
[00:24:55] Or gradient-based uh
[00:24:57] model predictive control. So, you have
[00:24:59] uh
[00:25:00] you can unroll that uh
[00:25:03] that model in time. You you you you feed
[00:25:06] it a
[00:25:08] hypothesized sequence of actions.
[00:25:11] And then you have some objective
[00:25:13] function that measures how well at the
[00:25:15] end of the trajectory the system has has
[00:25:16] succeeded or matched what you wanted to
[00:25:18] do.
[00:25:19] Um you know, is it a robot harmed? Have
[00:25:21] you grasped the object you want to
[00:25:22] grasp? If it's a rocket, you know, are
[00:25:25] you at the right place near the space
[00:25:26] station? Things like that. Um and by
[00:25:29] back propagation through time, and
[00:25:31] again, this was invented in the 1960s by
[00:25:33] optimal control theorists,
[00:25:34] uh you can figure out uh what is the
[00:25:37] optimal sequence of actions that will uh
[00:25:40] you know, get my system to the the best
[00:25:43] final state.
[00:25:45] So,
[00:25:46] that's a form of reasoning. It's
[00:25:47] basically planning, and a lot of
[00:25:49] planning systems in robotics are
[00:25:51] actually based on this.
[00:25:52] Uh and uh
[00:25:54] uh and you can think of this as a form
[00:25:55] of reasoning. So, you know, to take the
[00:25:58] example of the teenager driving a car
[00:25:59] again, you have a pretty good dynamical
[00:26:02] model of the car. It doesn't need to be
[00:26:03] very accurate, but you know, again, that
[00:26:05] if you turn the wheel to the right and
[00:26:07] there is a cliff, you're going to run
[00:26:08] off the cliff, right? You don't need to
[00:26:09] have a very accurate model to predict
[00:26:11] that.
[00:26:12] And you can run this in your mind and
[00:26:13] decide not to do it for that reason.
[00:26:16] Because you can predict in advance that
[00:26:17] the result is going to be bad. So, you
[00:26:18] can sort of imagine different scenarios
[00:26:21] and uh and then you know, employ
[00:26:23] uh or take the first step in the
[00:26:24] scenario that is most favorable, and
[00:26:26] then repeat the process of planning.
[00:26:27] That's called receding horizon model
[00:26:29] predictive control. So, even you know,
[00:26:31] all those things have names, you know,
[00:26:32] uh going back, you know, decades. Um
[00:26:35] and so,
[00:26:36] if you're not not the you know, in
[00:26:39] classical optimal control, the model of
[00:26:40] the world is not generally learned.
[00:26:42] Uh there's you know, sometimes a few
[00:26:44] parameters you have to identify, that's
[00:26:45] called systems identification, but um
[00:26:48] but generally,
[00:26:49] the model is
[00:26:50] mostly deterministic and mostly built by
[00:26:52] hand. So, the big question of AI
[00:26:55] uh I think the big challenge of AI for
[00:26:57] the next decade is how do we get
[00:26:59] machines to learn predictive models of
[00:27:01] the world that deal with uncertainty and
[00:27:03] deal with the real world in all its
[00:27:05] complexity. So, it's not just trajectory
[00:27:07] of a rocket which you can reduce to
[00:27:09] first principles. It's not It's not even
[00:27:11] just a trajectory of a robot arm, which
[00:27:13] again you can model by, you know,
[00:27:14] careful mathematics.
[00:27:16] But, it's everything else. Everything we
[00:27:17] observe in the world, you know, people
[00:27:19] behavior
[00:27:20] um
[00:27:21] you know, physical systems that involve
[00:27:24] collective phenomena like water or or,
[00:27:27] you know,
[00:27:29] trees and, you know, branches in a in a
[00:27:30] tree or something or or uh like complex
[00:27:34] things that, you know, humans have no
[00:27:35] trouble
[00:27:36] developing abstract representations and
[00:27:38] predictive model for, but we still don't
[00:27:40] know how to do with machines.
[00:27:41] Where do you put in in these three,
[00:27:43] maybe in the in the planning stages
[00:27:47] the the game theoretic nature of this
[00:27:50] world, where your actions not only
[00:27:52] respond to the dynamic nature of the
[00:27:54] world, the environment, but also affect
[00:27:56] it?
[00:27:57] So, if there's other humans involved. Is
[00:27:59] this is this point number four, or is it
[00:28:02] somehow integrated into the hierarchical
[00:28:04] representation of action in your view?
[00:28:06] I think it's integrated. It's just um
[00:28:08] it's just that now your model of the
[00:28:10] world has to deal with, you know, it
[00:28:11] just makes it more complicated, right?
[00:28:13] The fact that uh
[00:28:14] humans are complicated and not easily
[00:28:16] predictable, that makes your model of
[00:28:18] the world much more complicated, that
[00:28:20] much more complicated.
[00:28:21] Well, there's a chat I mean, I I suppose
[00:28:23] chess is an analogy.
[00:28:25] So, Monte Carlo tree search.
[00:28:28] Right.
[00:28:28] It there is a I go, you go, I go, you
[00:28:31] go. Like um
[00:28:33] Andrej Karpathy recently gave a talk at
[00:28:35] MIT about car doors.
[00:28:37] I think there's some machine learning
[00:28:39] too, but mostly car doors. And there's a
[00:28:41] dynamic nature to the car like the
[00:28:43] person opening the door checking
[00:28:45] I mean, he wasn't talking about that. He
[00:28:46] was talking about the perception problem
[00:28:48] of what the the anthology of what
[00:28:49] defines a car door, this big
[00:28:51] philosophical question. But to me, it
[00:28:53] was interesting cuz like it's obvious
[00:28:55] that the person opening the car door is
[00:28:57] they're trying to get out like here in
[00:28:58] New York, trying to get out of the car.
[00:29:01] You slowing down is going to signal
[00:29:03] something. You speeding up is going to
[00:29:04] signal something. And that's a dance.
[00:29:06] It's a
[00:29:07] asynchronous
[00:29:09] chess game. I don't know.
[00:29:11] So,
[00:29:12] I it feels like um
[00:29:15] it's not just I mean, I guess you can
[00:29:17] integrate all of that into one giant
[00:29:19] model. Like the entirety of the the
[00:29:22] these little interactions. Cuz it's not
[00:29:24] as complicated as chess. It's just like
[00:29:26] a little dance. We do like a little
[00:29:27] dance together. And then we figure it
[00:29:29] out.
[00:29:29] Well, in some ways it's way more
[00:29:31] complicated than chess because
[00:29:33] uh because it's continuous, it's
[00:29:35] uncertain in a continuous manner.
[00:29:37] Uh
[00:29:38] It doesn't feel more complicated.
[00:29:39] But it doesn't feel more complicated
[00:29:40] because that's what we are we've evolved
[00:29:43] to solve. This is the kind of problem
[00:29:44] we've evolved to solve. And so we're
[00:29:45] good at it because, you know, nature has
[00:29:48] made us good at it.
[00:29:50] Nature has not made us good at chess. We
[00:29:52] completely suck at chess.
[00:29:54] Yeah.
[00:29:54] Um
[00:29:55] in fact, that's why we designed it as a
[00:29:57] as a game is to be challenging.
[00:29:58] Mhm.
[00:29:59] Uh and if there is something that, you
[00:30:01] know, recent progress in the chess and
[00:30:03] go has made us realize is that humans
[00:30:06] are really terrible at those things.
[00:30:07] Like really bad, you know? There was
[00:30:09] this story right before AlphaGo that uh
[00:30:12] uh you know, the best go player thought
[00:30:15] they were maybe two or three stones
[00:30:16] behind, you know, an ideal player that
[00:30:18] they would call god.
[00:30:19] Mhm.
[00:30:20] Uh in fact, no, they're like nine or 10
[00:30:22] stones behind. I mean, we're just bad.
[00:30:24] Yeah.
[00:30:25] So, we're not good at and it's because
[00:30:27] we have limited uh working memory. We we
[00:30:30] know we're not very good at like doing
[00:30:31] this tree exploration that, you know,
[00:30:33] computers are much better
[00:30:35] um at doing that we are. But we are much
[00:30:37] better at learning differentiable models
[00:30:39] of the world.
[00:30:40] I mean, I said differentiable in a of
[00:30:43] you know, I should say
[00:30:44] not differentiable in the sense that,
[00:30:46] you know, we run backprop through it,
[00:30:47] but in the sense that uh our brain has
[00:30:49] some mechanism for estimating gradients
[00:30:52] uh of of some kind.
[00:30:53] Yeah.
[00:30:54] And that's what, you know, makes us uh
[00:30:56] efficient. So, if you have an agent that
[00:30:59] consists of
[00:31:01] a a model of the world, which, you know,
[00:31:03] in the human brain is basically the
[00:31:04] entire front half of your brain.
[00:31:07] Um
[00:31:08] an objective function
[00:31:10] which
[00:31:11] uh in human in in humans is a
[00:31:13] combination of two things. There is your
[00:31:15] sort of intrinsic motivation module,
[00:31:17] which is in the basal ganglia, you know,
[00:31:18] at the base of your brain. That's the
[00:31:20] thing that measures pain and hunger and
[00:31:22] things like that, like immediate um uh
[00:31:25] feelings and emotions.
[00:31:27] Um and then there is
[00:31:29] you know, the equivalent of what people
[00:31:31] in reinforcement learning call a critic,
[00:31:32] which is a sort of module that predicts
[00:31:35] ahead what the outcome
[00:31:37] of a uh
[00:31:39] of a uh situation will be.
[00:31:41] And so, it's it's not a cost function,
[00:31:43] but it's sort of it's not an objective
[00:31:45] function, but it's sort of a
[00:31:47] you know, trained predictor of the
[00:31:49] ultimate objective function. And that
[00:31:51] also is differentiable. And so, if all
[00:31:53] of this is differentiable, your cost
[00:31:55] function, your your critic, your
[00:31:57] uh
[00:31:58] you know, your your world model then you
[00:32:00] can use gradient-based type methods to
[00:32:03] do planning, to do reasoning, to do
[00:32:05] learning uh you know, to do all the
[00:32:07] things that we'd like an intelligent
[00:32:09] agent uh
[00:32:10] uh to do.
[00:32:11] And the gradient-based learning
[00:32:14] like what's your intuition, that's
[00:32:15] probably at the core of what can solve
[00:32:17] intelligence, so you don't need
[00:32:20] like um
[00:32:21] logic-based
[00:32:23] reasoning uh in your view.
[00:32:25] I don't know how to make logic-based
[00:32:26] reasoning compatible with uh efficient
[00:32:29] learning.
[00:32:29] Yeah.
[00:32:30] And Okay. I mean, there is a big
[00:32:31] question, perhaps a philosophical
[00:32:33] question. I mean, it's not that
[00:32:34] philosophical, but
[00:32:36] uh that we can ask is is that you know
[00:32:38] all the learning uh algorithms we know
[00:32:40] from engineering and computer science
[00:32:43] proceed by optimizing some objective
[00:32:45] function.
[00:32:46] Yeah.
[00:32:46] Right?
[00:32:47] Uh so one question we may ask is uh
[00:32:50] is
[00:32:51] does learning in the brain minimize an
[00:32:53] objective function?
[00:32:54] I mean it could be a
[00:32:56] you know a a composite of multiple
[00:32:57] objective functions, but it's still an
[00:32:58] objective function.
[00:33:00] Uh second, if it does optimize an
[00:33:03] objective function, does it do does it
[00:33:05] do it by uh some sort of gradient
[00:33:08] estimation?
[00:33:09] You know, it doesn't need to be
[00:33:10] backprop, but you know, some way of
[00:33:11] estimating the gradient in efficient
[00:33:13] manner.
[00:33:14] Whose complexity is on the same order of
[00:33:16] magnitude as you know, actually running
[00:33:19] the inference.
[00:33:21] Uh
[00:33:22] cuz you can't afford to do things like,
[00:33:24] you know, perturbing a weight in your
[00:33:26] brain to figure out what the effect is
[00:33:28] and then sort of
[00:33:29] uh you know, you you can't do sort of
[00:33:30] estimating gradient by perturbation.
[00:33:32] It's to me it seems very impossible that
[00:33:36] the brain uses some sort of uh you know,
[00:33:39] zeroth order black box gradient free
[00:33:41] optimization
[00:33:43] because it's so much less efficient than
[00:33:45] gradient optimization. So it has to have
[00:33:46] a way of estimating gradient.
[00:33:49] Is it possible that some kind of logic
[00:33:51] based reasoning emerges in pockets as a
[00:33:54] useful like you said, if the brain has
[00:33:57] an objective function, maybe it's a
[00:33:58] mechanism for creating objective
[00:34:00] functions.
[00:34:01] It's it's it's a mechanism for um
[00:34:03] creating knowledge bases for example
[00:34:06] that can then be queried. Like maybe
[00:34:08] it's like an efficient representation of
[00:34:10] knowledge that's learned in a gradient
[00:34:11] based way or something like that.
[00:34:13] Well, so I think there is a lot of
[00:34:15] different types of uh intelligence. So
[00:34:17] first of all, I think the type of
[00:34:18] logical reasoning that we think about um
[00:34:21] that we are
[00:34:22] you know, maybe stemming from you know,
[00:34:25] sort of classical AI of the 1970s and
[00:34:27] 80s.
[00:34:28] Um
[00:34:29] I think humans use that relatively
[00:34:31] rarely
[00:34:32] and are not particularly good at it.
[00:34:34] But we judge each other based on our
[00:34:36] ability to
[00:34:38] solve those rare problems. It's called
[00:34:40] IQ test.
[00:34:41] I think so. Like I'm I'm not very good
[00:34:43] at chess.
[00:34:45] Yes, I'm I'm judging you this whole time
[00:34:47] because of
[00:34:48] Well, we we actually
[00:34:49] With with your with your you know,
[00:34:51] heritage, I'm sure you're good at chess.
[00:34:53] No, stereotypes. Not all stereotypes are
[00:34:56] true.
[00:34:57] Well, I'm terrible at chess. So, um
[00:35:00] you know, but I think perhaps
[00:35:03] another type of intelligence that I have
[00:35:05] is this uh
[00:35:06] uh you know, ability of sort of building
[00:35:08] models to the world from
[00:35:10] uh you know,
[00:35:12] reasoning obvious obviously, but also
[00:35:14] also data.
[00:35:15] Uh and those those models generally are
[00:35:17] more kind of analogical, right? So, it's
[00:35:19] it's uh it's reasoning by simulation
[00:35:22] and but by analogy where you use one
[00:35:24] model to apply to a new situation. Even
[00:35:27] though you've never seen that situation,
[00:35:28] you can sort of um connect it to a
[00:35:31] situation you've encountered before. Uh
[00:35:33] and and your reasoning is more
[00:35:36] you know, akin to some sort of internal
[00:35:37] simulation. So, you you are kind of
[00:35:39] simulating what's happening when you're
[00:35:41] building, I don't know, a box out of
[00:35:42] wood or something, right? You kind of
[00:35:44] imagine in in advance
[00:35:46] like what would be the result of, you
[00:35:47] know, cutting the wood in this
[00:35:48] particular way. Are you going to use,
[00:35:50] you know, screws or nails or whatever.
[00:35:52] Um
[00:35:52] when you are interacting with someone,
[00:35:54] you also have a model of that person and
[00:35:56] and sort of interact with that person
[00:35:59] you know, having this model in mind uh
[00:36:01] to kind of uh tell the person what what
[00:36:03] you think is useful to them. So, I think
[00:36:06] this this ability to construct models of
[00:36:09] the world is basically the essence the
[00:36:12] essence of intelligence.
[00:36:13] And the ability to use it then to uh
[00:36:16] plan uh actions that will
[00:36:19] uh fulfill a particular uh criterion. Um
[00:36:22] of course, is is is necessary as well.
[00:36:25] So, I'm going to ask you a series of
[00:36:27] questions as what keep asking as I've
[00:36:29] been doing. So, so if that's the
[00:36:31] fundamental sort of dark matter of
[00:36:33] intelligence, this ability to form a
[00:36:35] background model, what's your intuition
[00:36:37] about
[00:36:38] how much knowledge is required?
[00:36:41] You You know, I think dark matter you
[00:36:43] you put a percentage of
[00:36:45] uh on it of
[00:36:47] of uh the composition of the universe
[00:36:49] and how much of it is dark matter, how
[00:36:51] much of it is dark energy, how much
[00:36:55] uh information do you think is required
[00:36:57] to to be a house cat? So, you have to be
[00:37:00] able to uh when you see a box going it
[00:37:02] when you see a human compute the most
[00:37:04] evil action if there's a thing that's
[00:37:07] near an edge, you knock it off.
[00:37:09] All of that plus the extra stuff you
[00:37:12] mentioned, which is a
[00:37:13] great self-awareness of the physics of
[00:37:15] your of your own body and the in the
[00:37:17] world.
[00:37:18] How much knowledge is required do you
[00:37:20] think to solve it?
[00:37:22] Um
[00:37:22] I don't even know how to measure and
[00:37:24] answer to that question.
[00:37:25] I'm not sure how to measure it, but
[00:37:26] whatever it is, it fits in about about
[00:37:29] 800,000 neurons uh
[00:37:32] 800 million neurons, sorry.
[00:37:33] The representation does.
[00:37:36] Everything, all knowledge, everything,
[00:37:37] right?
[00:37:38] Um
[00:37:40] you know, it's less than a billion. A
[00:37:41] dog is 2 billion, but a cat is less than
[00:37:43] 1 billion.
[00:37:45] And uh
[00:37:46] so, multiply that by 1,000 and you get
[00:37:48] the number of synapses.
[00:37:49] Uh and I think almost all of it is is
[00:37:52] learned through this, you know, a sort
[00:37:54] of self-supervised learning. Although,
[00:37:56] you know, I I think a tiny sliver is
[00:37:58] learned through reinforcement learning
[00:37:59] and certainly very little through
[00:38:01] you know, classical supervised learning,
[00:38:03] although it's not even clear how
[00:38:04] supervised learning actually works in
[00:38:06] the in the biological world.
[00:38:08] Um so, I think almost all of it is uh is
[00:38:11] self-supervised learning. But, it's
[00:38:13] driven
[00:38:14] by
[00:38:15] uh the the sort of ingrained objective
[00:38:17] functions that a cat or human have at
[00:38:20] the base of their brain, which kind of
[00:38:21] drives their
[00:38:23] um their behavior. So, you know, nature
[00:38:26] tells us uh you're hungry.
[00:38:29] It doesn't tell us how to feed a feed
[00:38:31] ourselves. That's that's something that
[00:38:32] the rest of our brain has to figure out,
[00:38:34] right?
[00:38:35] Well, it's interesting cuz there might
[00:38:36] be more like deeper objective functions
[00:38:39] underlying the whole thing. So, hun-
[00:38:42] hunger may be some kind of
[00:38:44] you now you go to like neurobiology, it
[00:38:46] might be just the brain
[00:38:48] um
[00:38:50] try to maintain homeostasis.
[00:38:52] So, hunger is just one of the human
[00:38:55] perceivable
[00:38:56] symptoms of the brain being unhappy with
[00:38:59] the way things are currently. So, it's
[00:39:01] it could be just like one really dumb
[00:39:03] objective function at the core.
[00:39:04] But, that's how that's how behavior is
[00:39:06] is is driven. Uh the the fact that, you
[00:39:09] know, the orbital ganglia
[00:39:11] uh drive us to do things that are that
[00:39:13] are different from, say, an orangutan or
[00:39:16] certainly a cat
[00:39:17] uh is what makes, you know, human nature
[00:39:20] versus orangutan nature versus cat
[00:39:21] nature.
[00:39:22] Uh so, for example
[00:39:24] uh
[00:39:25] you know, our uh basal ganglia drives us
[00:39:27] to seek the company of uh other humans.
[00:39:32] And that's because nature has figured
[00:39:34] out that we need to be social animals
[00:39:36] for our species to survive, and it's
[00:39:37] true of many uh
[00:39:39] uh primates.
[00:39:41] It's not true of orangutans. Orangutans
[00:39:42] are solitary animals.
[00:39:44] Um they don't seek the company of
[00:39:46] others. In fact, they avoid them.
[00:39:48] Uh
[00:39:49] in fact, they scream at them when they
[00:39:50] come too close because they're
[00:39:51] territorial. Uh cuz for for their
[00:39:54] survival, you know,
[00:39:55] uh evolution has figured out that's the
[00:39:56] best thing.
[00:39:58] I mean, they're occasionally social, of
[00:39:59] course, for, you know, um
[00:40:02] reproduction and stuff like that. But,
[00:40:04] um but but they're mostly solitary. So,
[00:40:06] uh so, all of those behaviors are not
[00:40:08] part of intelligence. You know, people
[00:40:09] say, "Oh, you're never going to have
[00:40:11] intelligent machines because, you know,
[00:40:12] human intelligence is social." But, then
[00:40:14] you look at orangutans, you look at
[00:40:15] octopus. Octopus never know their
[00:40:17] parents.
[00:40:18] They barely interact with any other and
[00:40:20] they and they get to be really smart in
[00:40:22] less than a less than a year in like
[00:40:24] half a year.
[00:40:25] Um
[00:40:26] you know, in a year they're adults in 2
[00:40:27] years they're dead. So,
[00:40:29] um
[00:40:30] there are things that we think
[00:40:32] as humans are intimately linked with
[00:40:34] intelligence like social interaction,
[00:40:37] like language.
[00:40:39] We think I think we give way too much
[00:40:42] importance to language as a substrate of
[00:40:44] intelligence as humans.
[00:40:46] Because we think our reasoning is so
[00:40:48] linked with language.
[00:40:49] So, for for to solve the house cat
[00:40:52] intelligence problem, you think you
[00:40:53] could do it on a desert island. You
[00:40:55] could have
[00:40:56] Pretty much.
[00:40:56] You could just have a cat sitting there
[00:40:58] um
[00:41:00] looking at the waves at the ocean waves
[00:41:03] and figure out a lot of it out.
[00:41:05] It needs to have sort of, you know, the
[00:41:07] right set of drives
[00:41:09] uh to kind of
[00:41:11] you know, get it to do the thing and
[00:41:12] learn the appropriate things, right?
[00:41:14] But, uh
[00:41:15] um like for example, you know, uh
[00:41:17] baby humans are are driven to
[00:41:20] learn to stand up and walk.
[00:41:22] Okay, you know, it's not that's kind of
[00:41:24] this desire is hardwired. How to do it
[00:41:26] precisely is not, that's learned.
[00:41:28] Mhm.
[00:41:28] But, the desire to
[00:41:29] to walk
[00:41:30] move around and stand up.
[00:41:32] Mhm. Uh that's sort of
[00:41:34] hardwired. It's very simple to hardwire
[00:41:36] this kind of stuff.
[00:41:38] What Oh, like the desire to Well,
[00:41:41] that's interesting. You're hardwired to
[00:41:43] want to walk.
[00:41:45] That's not a
[00:41:47] there's got to be a deeper need for
[00:41:49] walking.
[00:41:50] I I think it was probably socially
[00:41:51] imposed by society that you need to
[00:41:53] walk. All the other bipedal
[00:41:55] No. Like a lot of simple animals that,
[00:41:57] you know, will probably walk without
[00:41:59] ever
[00:42:00] watching any
[00:42:02] other members of the species.
[00:42:03] It seems like a scary thing to have to
[00:42:05] do cuz you suck at bipedal walking at
[00:42:08] first. It seems crawling is much safer.
[00:42:11] Much more
[00:42:13] like why are you in a hurry?
[00:42:15] Well, because because you have this
[00:42:17] thing that drives you to do it, you
[00:42:18] know? Um
[00:42:20] which is sort of part of uh the sort of
[00:42:24] human development.
[00:42:25] Is that understood actually what
[00:42:26] Not entirely. No.
[00:42:27] What is the What's the reason to get on
[00:42:29] two feet? It's really hard. Like, most
[00:42:31] animals don't get on two feet.
[00:42:32] Well, they get on four feet. You know,
[00:42:34] many mammals get on four feet.
[00:42:35] Yeah, they figure
[00:42:36] Very quickly. Some of them extremely
[00:42:37] quickly.
[00:42:38] But I don't, you know, like from the
[00:42:40] last time I've interacted with a table,
[00:42:42] that's much more stable than a thing on
[00:42:44] two legs. It's just a really hard
[00:42:45] problem.
[00:42:46] Yeah, I mean, birds have figured it out
[00:42:47] with two feet.
[00:42:49] But well, technically, we can go into
[00:42:51] anthology. They have four. I guess they
[00:42:53] have two feet.
[00:42:54] They have two feet.
[00:42:55] Chickens.
[00:42:56] You know, dinosaurs have two feet. Many
[00:42:58] of them.
[00:42:58] Allegedly.
[00:43:01] I'm just now learning that T-Rex was
[00:43:03] eating grass, not other animals. T-Rex
[00:43:05] might have been a friendly
[00:43:07] friendly pet. What do you think about uh
[00:43:10] um I don't know if you looked at
[00:43:12] the test for general intelligence that
[00:43:14] François Chollet put together. I don't
[00:43:16] know if you got a chance to look at that
[00:43:18] kind of thing. Like, what
[00:43:19] What's your intuition about how to solve
[00:43:21] like an IQ type of test?
[00:43:23] I don't know. I think it's so outside of
[00:43:25] my radar screen that it's not really
[00:43:28] relevant, I think, in the short term.
[00:43:30] Well, I guess uh one way to ask another
[00:43:33] way, perhaps more closer to what
[00:43:36] to your work is like, how do you solve
[00:43:38] MNIST
[00:43:40] uh with very little example data?
[00:43:42] That's right. And that's the answer to
[00:43:44] this, probably, is self-supervised
[00:43:45] learning. Just learn to represent
[00:43:46] images, and then learning
[00:43:48] uh
[00:43:49] you know, to recognize handwritten
[00:43:50] digits on top of this will only require
[00:43:52] a few samples. And we observe this in in
[00:43:54] humans, right? You You show a a young
[00:43:57] child a a picture book with a couple of
[00:43:59] picture of an elephant, and that's it.
[00:44:01] The
[00:44:01] The child knows what an elephant is.
[00:44:03] And we we we see this today with
[00:44:05] practical systems that we
[00:44:07] you know we train image recognition
[00:44:09] systems with
[00:44:10] uh
[00:44:11] enormous amounts of of images either
[00:44:14] either completely self-supervised or
[00:44:15] very weakly supervised. For example,
[00:44:18] you can
[00:44:19] train a a neural net to predict whatever
[00:44:22] hashtag people type on Instagram, right?
[00:44:24] And you can do this with billions of
[00:44:25] images cuz there's billions per day that
[00:44:26] are showing up.
[00:44:28] Um so the amount of training data there
[00:44:30] is essentially unlimited.
[00:44:32] And then you take the output
[00:44:33] representation you know a couple layers
[00:44:35] down from the output
[00:44:37] of what the system learned and feed this
[00:44:40] as input to a classifier for any object
[00:44:42] in the world that you want and it works
[00:44:44] pretty well.
[00:44:44] So that's transfer learning. Okay. Uh or
[00:44:47] weakly supervised
[00:44:49] transfer learning.
[00:44:50] Uh people are making very very fast
[00:44:52] progress using self-supervised learning
[00:44:55] for for the with this kind of scenario
[00:44:56] as well.
[00:44:57] Um and you know my guess is that that's
[00:45:00] that's going to be the the future.
[00:45:02] For self-supervised learning, how much
[00:45:04] cleaning do you think is needed for
[00:45:07] filtering um
[00:45:10] uh malicious signal or what's a better
[00:45:12] term? But like a lot of people use
[00:45:14] hashtags on Instagram
[00:45:16] to
[00:45:17] get like good SEO.
[00:45:19] Mhm.
[00:45:20] That doesn't fully represent the
[00:45:21] contents of the image.
[00:45:23] Like they'll put a picture of a cat and
[00:45:24] hashtag it with like science, awesome,
[00:45:27] fun. I don't know all kind of I don't
[00:45:29] Well, why would you put science?
[00:45:30] Well, so that's not very good SEO. The
[00:45:32] way the way my my colleagues who worked
[00:45:34] on this project at
[00:45:36] at Facebook now Meta Meta AI
[00:45:38] a few years ago
[00:45:40] dealt with this is that they only
[00:45:41] selected something like 17,000 tags that
[00:45:43] correspond to kind of physical things or
[00:45:46] or situations like you know that has
[00:45:48] some visual content.
[00:45:51] Um
[00:45:52] so you know
[00:45:54] you wouldn't have like hash TBT or
[00:45:55] anything like that.
[00:45:57] Oh, so they they keep a very select set
[00:45:59] of hashtags is what you're saying.
[00:46:01] Yeah.
[00:46:01] Okay.
[00:46:02] But it's it's still in still on the
[00:46:03] order of
[00:46:04] you know, 10 to 20,000. So it's fairly
[00:46:07] large.
[00:46:07] Okay.
[00:46:09] Can you tell me about data augmentation?
[00:46:11] What the heck is data augmentation? And
[00:46:13] how is it used? Maybe contrast of
[00:46:15] learning
[00:46:17] for
[00:46:18] for video. What are some cool ideas
[00:46:19] here?
[00:46:20] Right. So data augmentation, I mean
[00:46:22] first data augmentation, you know, is
[00:46:24] the idea of artificially increasing the
[00:46:25] size of your training set by distorting
[00:46:27] the
[00:46:28] images that you have in ways that don't
[00:46:30] change the nature of the image, right?
[00:46:32] So you take you you do you do MNIST. You
[00:46:34] can do data augmentation on MNIST. And
[00:46:35] people have done this since 1990s, all
[00:46:37] right? You take a
[00:46:38] MNIST digit and you shift it a little
[00:46:40] bit or you
[00:46:41] change the size or
[00:46:43] rotate it, skew it,
[00:46:45] you know, etc., right?
[00:46:46] Add noise.
[00:46:48] Add noise, etc. And it it works better.
[00:46:50] If you train a supervised classifier
[00:46:52] with augmented data, you're going to get
[00:46:53] better results.
[00:46:55] Now, it's become really interesting over
[00:46:58] the last couple of years because
[00:47:01] a lot of self-supervised learning
[00:47:03] techniques to pre-train vision systems
[00:47:06] are based on data augmentation.
[00:47:08] And the
[00:47:09] the basic techniques is originally
[00:47:11] inspired by
[00:47:13] techniques that I worked on in the early
[00:47:15] 90s and Jeff Hinton worked on also in
[00:47:17] the early 90s. There was sort of
[00:47:18] parallel
[00:47:19] work. I used to call this Siamese
[00:47:21] networks. So basically you take
[00:47:23] two identical copies of the same
[00:47:25] network. They share the same weights.
[00:47:27] And you show two
[00:47:30] different views of the same object.
[00:47:31] Either those two different views may
[00:47:33] have been obtained by data augmentation
[00:47:35] or maybe it's two different views of the
[00:47:36] same scene from a camera that you moved
[00:47:39] or at different times or something like
[00:47:40] that, right? Or two pictures of the same
[00:47:42] person, things like that.
[00:47:44] And then you train this neural net,
[00:47:46] those two identical copies of this
[00:47:47] neural net to produce an output
[00:47:49] representation, a vector,
[00:47:52] in such a way that the representation
[00:47:53] for those two
[00:47:55] images are as close to each other as
[00:47:58] possible, as identical to each other as
[00:48:00] possible, right? Because you want the
[00:48:01] system to be basically learn a function
[00:48:04] that will that will be invariant, that
[00:48:06] will not change, whose output will not
[00:48:07] change when you transform those inputs
[00:48:10] in in those in those particular ways,
[00:48:12] right?
[00:48:13] Um so that's easy to do.
[00:48:15] What's complicated is how do you make
[00:48:17] sure that when you show two images that
[00:48:18] are different, the system will produce
[00:48:20] different things?
[00:48:21] Because if you don't have a specific
[00:48:24] provision for this, uh the system will
[00:48:26] just ignore the input uh when you train
[00:48:28] it, it will end up ignoring the input
[00:48:30] and just produce a constant vector that
[00:48:31] is the same for every input, right?
[00:48:33] That's called a collapse.
[00:48:35] Now, how do you avoid collapse? So
[00:48:36] there's two ideas.
[00:48:38] Uh one idea that I proposed in the early
[00:48:40] '90s uh with my colleagues at Bell Labs,
[00:48:43] uh Jan Bromley and a couple other
[00:48:44] people,
[00:48:45] uh
[00:48:46] which we now call contrastive learning,
[00:48:48] which is to have negative examples,
[00:48:49] right? So you have pairs
[00:48:51] of images that you know are different,
[00:48:54] and you show them to the network, and uh
[00:48:56] those two copies, and then you you push
[00:48:58] the two output vectors away from each
[00:49:00] other.
[00:49:01] And that would eventually guarantee that
[00:49:03] things that are semantically similar
[00:49:04] produce similar representations, and
[00:49:06] things that are different produce
[00:49:07] different representations.
[00:49:09] Uh we actually came up with this idea
[00:49:11] for a project of doing signature
[00:49:13] verification. So we would collect
[00:49:16] signature
[00:49:17] signatures from like multiple signatures
[00:49:19] on the same person, and then train a
[00:49:20] neural net to produce the same
[00:49:21] representation. And then uh you know,
[00:49:25] force the system to produce different
[00:49:27] representation for different signatures.
[00:49:30] Um this was actually the the problem was
[00:49:32] proposed by people from a
[00:49:34] what was a subsidiary of AT&T at the
[00:49:36] time called NCR,
[00:49:38] and they were interested in storing a
[00:49:40] representation of the signature on the
[00:49:42] 80 bytes of the magnetic strip of a
[00:49:45] credit card. So we came up with this
[00:49:47] idea of having a neural net with 80
[00:49:49] outputs,
[00:49:50] you know, that we would quantize on
[00:49:51] bytes to so that we could encode the the
[00:49:53] the
[00:49:53] that encoding was then used to compare
[00:49:55] whether the signature matches or not.
[00:49:57] That's right. So then you would, you
[00:49:58] know,
[00:49:58] Interesting.
[00:49:58] sign, you would run through the neural
[00:50:00] net, and then you would compare the
[00:50:01] output vector to whatever is stored on
[00:50:03] your card.
[00:50:03] actually work?
[00:50:04] It worked, but they ended up not using
[00:50:06] it.
[00:50:08] Um because nobody cares actually. I
[00:50:10] mean, the
[00:50:11] American, you know, financial payment
[00:50:13] system is
[00:50:14] incredibly lax in that respect compared
[00:50:17] to Europe for example.
[00:50:17] Oh, with the signatures, what's the
[00:50:19] purpose of signatures anyway? This is
[00:50:20] very
[00:50:21] Nobody looks at them. Nobody cares, you
[00:50:22] know.
[00:50:23] And and it's uh yeah.
[00:50:24] Yeah, no. So uh so that that's
[00:50:26] contrastive learning, right? So you need
[00:50:28] positive and negative pairs. And the
[00:50:29] problem with that is that
[00:50:31] you know, even though I had the original
[00:50:33] paper on this,
[00:50:34] I'm actually not very positive about it
[00:50:36] because it doesn't work in high
[00:50:38] dimension. If your representation is
[00:50:39] high dimensional, there's just too many
[00:50:41] ways for two things to be different.
[00:50:44] And and so you would need lots and lots
[00:50:45] and lots of negative pairs.
[00:50:47] Uh so there is a a particular
[00:50:49] implementation of this which is
[00:50:51] relatively recent from actually the
[00:50:53] Google Toronto group uh where you know,
[00:50:56] Jeff Hinton is the the senior member
[00:50:58] there. It's called SimCLR, S I M C C L
[00:51:00] R.
[00:51:01] Mhm.
[00:51:01] Uh and it you know, basically a
[00:51:03] particular way of implementing this idea
[00:51:05] of contrastive learning. The particular
[00:51:07] objective function. Now,
[00:51:09] what I'm much more enthusiastic about
[00:51:12] these days is non-contrastive methods.
[00:51:14] So other ways to guarantee that
[00:51:17] uh uh the representations will be
[00:51:20] different for different uh
[00:51:22] uh different inputs.
[00:51:24] And it's actually based on an idea that
[00:51:26] um
[00:51:27] Jeff Hinton proposed in the early '90s
[00:51:29] with his student at the time, Sue
[00:51:30] Becker.
[00:51:31] And it's based on the idea of maximizing
[00:51:33] the mutual information between the
[00:51:34] outputs of the two systems. You only
[00:51:36] show positive pairs. You only show pairs
[00:51:38] of images that you know are somewhat
[00:51:40] similar.
[00:51:41] And you're trying the two networks to be
[00:51:43] informative,
[00:51:45] but also to be as informative
[00:51:48] uh each other as possible. So basically
[00:51:50] one representation has to be predictable
[00:51:52] from the other essentially.
[00:51:54] And you know, he proposed that idea had
[00:51:57] you know,
[00:51:58] couple of papers in the early 90s and
[00:52:00] then nothing was done about it for
[00:52:02] decades and I kind of revived this idea
[00:52:04] together with my post docs at at fair.
[00:52:07] Particularly a postdoc called Stefan
[00:52:09] Deny who's now
[00:52:10] junior professor in in Finland at
[00:52:12] University of Alto. Um
[00:52:15] We came up with something called that we
[00:52:17] call Barlow Twins.
[00:52:19] And it's a particular way of maximizing
[00:52:21] the information content of uh
[00:52:24] of a vector you know, using some uh
[00:52:27] hypotheses.
[00:52:28] And we have kind of a another version of
[00:52:31] it that's more recent now called VicReg
[00:52:33] VICREG that that means variance
[00:52:36] invariance covariance regularization.
[00:52:37] And I'm it's the thing I'm the most
[00:52:39] excited about in in machine learning in
[00:52:40] the last 15 years. I mean, I'm I'm not
[00:52:42] I'm really really excited about this.
[00:52:44] What
[00:52:45] kind of data augmentation is useful for
[00:52:47] that non-contrastive learning method?
[00:52:50] Are we talking about does that not
[00:52:51] matter that much or it seems like a very
[00:52:54] important part of the step. Yeah, how
[00:52:56] you generate the images that are similar
[00:52:58] but sufficiently different.
[00:52:59] Yeah, that's right. It's a important
[00:53:00] step and it's also an annoying step
[00:53:02] because you need to have that knowledge
[00:53:03] of what data augmentation
[00:53:05] uh
[00:53:06] you can do that do not change the nature
[00:53:08] of the of the object.
[00:53:10] Yeah.
[00:53:10] And so
[00:53:11] the standard scenario which you know, a
[00:53:13] lot of people working in this area are
[00:53:14] using is you use
[00:53:17] the the type of distortion. So so
[00:53:20] basically you do geometric distortion.
[00:53:21] So one basically just shifts the image a
[00:53:23] little bit. It's called cropping.
[00:53:25] Another one kind of changes the scale a
[00:53:26] little bit. Another one kind of rotates
[00:53:28] it. Another one changes the colors. You
[00:53:30] know, you can do a shift in color
[00:53:32] balance or something like that. Um
[00:53:34] saturation. Another one sort of blurs
[00:53:36] it. Another one adds noise. So you have
[00:53:38] like a catalog of for of standard things
[00:53:41] and people try to use the same ones for
[00:53:43] different algorithms so that they can
[00:53:44] compare.
[00:53:45] Um but some algorithms uh some
[00:53:47] self-supervised algorithm actually can
[00:53:48] deal with much bigger
[00:53:50] like more aggressive data augmentation
[00:53:52] and some don't. So that kind of makes
[00:53:55] the whole thing difficult. But But
[00:53:57] that's the kind of distortions we're
[00:53:58] talking about and
[00:53:59] and so you you you you train with those
[00:54:02] distortions
[00:54:03] and then uh you you chop off the last
[00:54:06] layer or couple layers of the of the
[00:54:09] network
[00:54:11] and you use the representation as input
[00:54:12] to a classifier. You train the
[00:54:13] classifier.
[00:54:14] Mhm.
[00:54:15] Um
[00:54:16] on ImageNet, let's say, or whatever
[00:54:18] and measure the performance.
[00:54:20] And
[00:54:21] interestingly enough the methods that
[00:54:23] are really good at eliminating the
[00:54:25] information that is irrelevant, which is
[00:54:27] the distortions between those images
[00:54:30] do good job at eliminating it.
[00:54:32] And uh as a consequence, you cannot use
[00:54:34] those the representations in those
[00:54:36] systems for things like object detection
[00:54:39] and localization because that
[00:54:40] information is gone.
[00:54:42] So the type of data augmentation you
[00:54:44] need to do depends on the task you want
[00:54:45] eventually
[00:54:47] the system to to solve and the type of
[00:54:49] data augmentation standard data
[00:54:51] augmentation that we use today are only
[00:54:52] appropriate for object recognition or
[00:54:54] image classification. They're not
[00:54:56] appropriate for things like
[00:54:57] Can you help me out and understand what
[00:54:59] uh wide localization is? So you're
[00:55:00] saying it's just not good at the
[00:55:02] negative?
[00:55:03] Uh like at classifying the negative, so
[00:55:05] that's why it can't be used for the
[00:55:06] localization?
[00:55:07] No, it's just that you train the system
[00:55:10] you know, you you you give it an image
[00:55:12] and then you give it the same image
[00:55:13] shifted and scaled. You tell it that's
[00:55:15] the same image.
[00:55:16] Yeah.
[00:55:17] So the system basically is trained to
[00:55:19] eliminate the information about position
[00:55:20] and size.
[00:55:22] So now and now you want to use that
[00:55:24] Oh, and
[00:55:25] to like figure out where an object is
[00:55:26] and what size it is.
[00:55:27] like a bounding box, like to be able to
[00:55:29] actually Okay. It can still find It can
[00:55:32] still find the object in the image. It's
[00:55:34] just not very good at finding the exact
[00:55:36] boundaries of that object. Interesting.
[00:55:38] Interesting. Which
[00:55:40] you know, that's an interesting sort of
[00:55:42] philosophical question. How important
[00:55:44] How important is the object localization
[00:55:46] anyway? We're like obsessed by measuring
[00:55:49] like image segmentation. Obsessed by
[00:55:51] measuring perfectly knowing the
[00:55:53] boundaries of objects when
[00:55:55] arguably
[00:55:57] that's not that essential to an
[00:56:01] understanding what are the contents of
[00:56:02] the scene.
[00:56:03] On the other hand, I think
[00:56:04] evolutionarily the first uh vision
[00:56:06] systems in animals were basically all
[00:56:08] about localization, very little about
[00:56:10] recognition.
[00:56:12] And in the human brain, you have two
[00:56:14] separate pathways for um recognizing the
[00:56:17] nature of uh of a scene or an object
[00:56:20] and localizing objects. So, you use the
[00:56:23] first pathway called the ventral pathway
[00:56:25] for, you know, telling what you're
[00:56:27] looking at.
[00:56:28] Uh the other pathway, the dorsal
[00:56:29] pathway, is used for a navigation, for
[00:56:32] grasping, for everything else. And you
[00:56:34] know, basically a lot of the things you
[00:56:35] need for survival are
[00:56:38] localization and detection.
[00:56:41] Is similarity learning or contrastive
[00:56:44] learning or these non-contrastive
[00:56:46] methods the same as understanding
[00:56:47] something?
[00:56:48] Just because you know a distorted cat is
[00:56:50] the same as a non-distorted cat, does
[00:56:52] that mean you understand what it means
[00:56:55] to be a cat?
[00:56:56] To some extent. I mean, it's a
[00:56:57] superficial understanding, obviously.
[00:57:00] But like what is the ceiling of this
[00:57:01] method, do you think? Is this just one
[00:57:03] trick on the path to doing
[00:57:06] self-supervised learning and can we go
[00:57:08] Yeah. really, really far?
[00:57:10] I think we can go really far. So, if we
[00:57:11] figure out how to
[00:57:14] uh use techniques of that type, perhaps
[00:57:16] very different, but you know, of the
[00:57:18] same nature,
[00:57:19] to uh train a system from from video to
[00:57:22] do video prediction, essentially.
[00:57:24] Um
[00:57:25] I think we'll have a path, um you know,
[00:57:28] towards uh
[00:57:29] I you know, I wouldn't say unlimited,
[00:57:31] but but a path towards some level of
[00:57:34] uh um
[00:57:35] you know, physical common sense in in
[00:57:37] machines. And I also think that
[00:57:40] um
[00:57:41] that
[00:57:42] ability to learn how the world works
[00:57:45] from a sort of high throughput channel
[00:57:47] like like vision
[00:57:48] Mhm.
[00:57:49] is a necessary step towards
[00:57:53] uh sort of real artificial intelligence.
[00:57:55] In other words, I believe in grounded
[00:57:57] intelligence. I don't think we can train
[00:57:59] a machine to be intelligent purely from
[00:58:00] text.
[00:58:02] Because I think the amount of
[00:58:03] information about the world that's
[00:58:05] contained in text is tiny compared to
[00:58:09] what we need to know.
[00:58:10] Mhm.
[00:58:11] So for example, let's and and you know,
[00:58:13] people have attempted to do this for for
[00:58:15] 30 years, right? The the site project
[00:58:17] and things like that, right? So
[00:58:18] basically kind of writing down all the
[00:58:20] facts that are known and
[00:58:21] uh hoping that some some sort of common
[00:58:23] sense will emerge. Um I think it's
[00:58:25] basically hopeless. Uh but let me take
[00:58:27] an example. You take an object. I I
[00:58:29] describe a situation to you. I take an
[00:58:31] object, I put it on the table, and I
[00:58:33] push the table. It's completely obvious
[00:58:36] to you that the object will be pushed
[00:58:37] with the table, right? Because it's
[00:58:39] sitting on it.
[00:58:41] Um there's no text in the world, I
[00:58:43] believe, that explains this.
[00:58:45] And so, if you train a machine as
[00:58:47] powerful as it could be, you know, your
[00:58:49] GPT 5000,
[00:58:51] uh
[00:58:52] or whatever it is, it's never going to
[00:58:54] learn about this.
[00:58:56] Um that information is just not is not
[00:58:59] present in any text.
[00:59:00] Well, the question like with the site
[00:59:02] project, the dream I think is to have
[00:59:04] like
[00:59:06] like 10 million say facts like that
[00:59:10] that give you a head start.
[00:59:13] Like a parent guiding you.
[00:59:15] Now, we humans don't need a parent to
[00:59:17] tell us that the table will move uh
[00:59:19] sorry, the smartphone will move with the
[00:59:20] table. But we get a lot of guidance in
[00:59:24] other ways. So it's possible that we can
[00:59:26] give it a quick shortcut.
[00:59:28] What about cat? A cat knows that.
[00:59:31] No, but they evolved. So,
[00:59:33] No, they learn like us.
[00:59:35] The The sorry, the physics of stuff?
[00:59:37] Yeah.
[00:59:38] Well, yeah, so you're saying it's uh
[00:59:42] So, you're putting a lot of intelligence
[00:59:45] onto the nurture side, not the nature.
[00:59:47] Cuz we seem to have um
[00:59:49] you know, there's a very inefficient
[00:59:51] arguably process of evolution that got
[00:59:53] us from bacteria to who we are today.
[00:59:57] Started at the bottom, now we're here.
[00:59:59] So,
[01:00:01] uh
[01:00:02] the question is how Okay, so
[01:00:04] the question is how fundamental is that
[01:00:05] that the nature of the whole hardware
[01:00:08] uh and then
[01:00:10] is there any way to shortcut it if it's
[01:00:11] fundamental? If it's not, if it's most
[01:00:13] of intelligence, most of the cool stuff
[01:00:15] we've been talking about is mostly
[01:00:17] nurture, mostly trained, we figured out
[01:00:19] by observing the world, we can form that
[01:00:22] uh big, beautiful, sexy background model
[01:00:24] that you're talking about just by
[01:00:26] sitting there.
[01:00:27] Um
[01:00:28] then okay, then you need to then like
[01:00:31] maybe
[01:00:33] uh it is all supervised learning all the
[01:00:36] way down.
[01:00:37] Self-supervised learning, say.
[01:00:39] Whatever it is that makes uh you know,
[01:00:41] human intelligence different from other
[01:00:43] animals, which you know, a lot of people
[01:00:45] think is language and logical reasoning
[01:00:47] and this kind of stuff.
[01:00:48] It cannot be that complicated because it
[01:00:50] only popped up in the last million
[01:00:51] years.
[01:00:52] Yeah.
[01:00:53] Uh and
[01:00:54] Yeah, it's it's
[01:00:55] you know, it it and it only involves you
[01:00:57] know,
[01:00:57] less than 1% of our genome, right? Which
[01:00:59] is the difference between human genome
[01:01:01] and chimps or whatever.
[01:01:03] So, uh
[01:01:05] it can't be that complicated, you know,
[01:01:06] it can't be that fundamental. I mean,
[01:01:08] the most of the so complicated stuff
[01:01:10] already exists in cats and dogs and
[01:01:13] you know, certainly primates, non-human
[01:01:15] primates.
[01:01:17] Yeah, that little thing with humans
[01:01:18] might be just uh something about
[01:01:21] social interaction and ability to
[01:01:22] maintain ideas across
[01:01:25] like a collective of people.
[01:01:28] It It sounds very dramatic and very
[01:01:30] impressive, but it probably isn't
[01:01:32] mechanistically speaking.
[01:01:33] It is, but we're not there yet. Like you
[01:01:35] know, we we have I mean this is number
[01:01:37] 634,
[01:01:39] you know, in the list of problem we have
[01:01:41] to solve.
[01:01:43] So basic physics of the world is is is
[01:01:45] is number one. What do you um
[01:01:48] Just a quick
[01:01:49] tangent on data augmentation. So a lot
[01:01:52] of it is
[01:01:53] uh hardcoded versus learned.
[01:01:57] Do you have any intuition that maybe
[01:02:00] there could be some weird data
[01:02:02] augmentation
[01:02:03] like generative type of data
[01:02:05] augmentation like doing something weird
[01:02:07] to images which then
[01:02:09] improves the the similarity learning
[01:02:12] process. So not just kind of dumb simple
[01:02:15] distortions, but
[01:02:17] but you're shaking your head you're
[01:02:18] saying that even simple distortions are
[01:02:20] enough.
[01:02:20] I think no. I think data augmentation is
[01:02:22] a temporary necessary evil.
[01:02:25] Huh.
[01:02:26] Um so what people are working on now is
[01:02:28] is two things. One is
[01:02:30] uh the type of self-supervised learning
[01:02:33] like trying to to translate the type of
[01:02:34] self-supervised learning people use in
[01:02:36] language, translating this to images,
[01:02:38] which is basically a denoising
[01:02:40] autoencoder method, right? So you you
[01:02:42] take an image you you block you mask
[01:02:45] some parts of it
[01:02:47] uh and then you you train some giant
[01:02:49] neural net to reconstruct the parts that
[01:02:50] you've that are that are missing. And
[01:02:53] until very recently
[01:02:56] there was no there was no working
[01:02:57] methods for that. Uh all the autoencoder
[01:02:59] type methods for images weren't
[01:03:01] producing very good representation. But
[01:03:03] there's a paper now coming out of uh
[01:03:05] the fair group at Menlo Park that
[01:03:07] actually works very well. So
[01:03:10] that doesn't require data augmentation,
[01:03:12] that requires only masking.
[01:03:14] Okay.
[01:03:14] Only masking for images.
[01:03:17] Uh
[01:03:18] Okay.
[01:03:18] Right. So, you mask part of the image
[01:03:20] and you train a system which, you know,
[01:03:23] in this case is a transformer because
[01:03:24] you can you can
[01:03:26] the transformer represents the image as
[01:03:29] uh non-overlapping patches, so it's easy
[01:03:31] to mask patches and things like that.
[01:03:33] Okay, then my question transfers to that
[01:03:35] problem, then masking. Like, why should
[01:03:37] the mask be uh square or rectangle?
[01:03:39] Uh so, it doesn't matter. Like, you
[01:03:41] know, I think we're going to come up
[01:03:43] probably in the future with sort of
[01:03:46] you know, ways to mask that are is, you
[01:03:47] know, kind of
[01:03:49] random essentially. I mean, they are
[01:03:51] random already, but
[01:03:52] No, no, but like something that's
[01:03:54] challenging.
[01:03:56] Like,
[01:03:57] optimally challenging. So, like, I mean,
[01:04:00] maybe it's a metaphor that doesn't
[01:04:01] apply, but you're It seems like there's
[01:04:04] an data augmentation or masking,
[01:04:07] there's an interactive element with it.
[01:04:09] Like, you're almost like playing with an
[01:04:11] image.
[01:04:12] Yeah.
[01:04:12] And like, it's like the way we play with
[01:04:14] an image in our minds.
[01:04:15] No, but it's like drop out. It's like
[01:04:17] Boltzmann machine training. You, um
[01:04:19] you know, every every every time you see
[01:04:21] a percept, you also
[01:04:24] you you can you can perturb it in some
[01:04:26] way. And then, uh the the principle of
[01:04:29] the training procedure
[01:04:31] is to minimize the difference of the
[01:04:33] output of the representation between the
[01:04:35] the clean version and the corrupted
[01:04:38] version, essentially, right? And you you
[01:04:40] you know, you can do this in real time,
[01:04:41] right? So, you know, Boltzmann machine
[01:04:43] work like this, right? You you you show
[01:04:45] a percept, uh you tell the machine
[01:04:47] that's a good combination of activities
[01:04:49] of your input neurons.
[01:04:51] Uh and then you either uh
[01:04:55] let them
[01:04:56] go their merry way without
[01:04:58] clamping them to values, or you only do
[01:05:00] this with a subset.
[01:05:01] Yeah.
[01:05:02] And what you're doing is you're training
[01:05:04] the system so that the the stable state
[01:05:07] of the entire network is the same
[01:05:08] regardless of whether it sees the entire
[01:05:10] input or whether it sees only part of
[01:05:12] it.
[01:05:13] Um, you know, the noisy autoencoder
[01:05:14] method is basically the same thing,
[01:05:16] right? You you're you're training a
[01:05:17] system to reproduce the input the
[01:05:19] complete input and filling the blanks
[01:05:21] regardless of which which parts are are
[01:05:23] missing and that's really the underlying
[01:05:25] principle. And you could imagine sort of
[01:05:27] a even in the brain some sort of neural
[01:05:28] principle where you know, neurons can uh
[01:05:31] oscillate, right? So they they take
[01:05:33] their activity and then temporarily they
[01:05:35] kind of shut off
[01:05:36] to um you know, force the rest of the
[01:05:38] system to basically
[01:05:40] reconstruct the input without their
[01:05:43] help, you know? And and and
[01:05:47] I mean you you can imagine, you know,
[01:05:48] process you know, more or less
[01:05:49] biologically possible processes.
[01:05:51] Something like that. And I guess with
[01:05:52] this denoising auto autoencoder and
[01:05:55] masking and data augmentation,
[01:05:58] you don't have to worry about being
[01:05:59] super efficient. You can just do do as
[01:06:02] much as you want
[01:06:03] Yeah.
[01:06:03] and and get better over time.
[01:06:06] Cuz I was thinking like you might want
[01:06:07] to be clever about the way you do all of
[01:06:09] these procedures,
[01:06:11] you know, but that's only if it's
[01:06:14] somehow costly to do every iteration,
[01:06:16] but it's not really.
[01:06:17] Not really.
[01:06:19] Maybe.
[01:06:20] And then there is, you know, data
[01:06:21] augmentation without explicit data
[01:06:22] augmentation.
[01:06:24] There's data augmentation by waiting,
[01:06:25] which is, you know, the the sort of
[01:06:27] video prediction.
[01:06:28] Right.
[01:06:28] Um you're
[01:06:30] observing a video clip, observing the
[01:06:33] you know, the the continuation of that
[01:06:34] video clip and try you try to learn a
[01:06:37] representation using those joint
[01:06:38] embedding architectures
[01:06:40] in such a way that the representation of
[01:06:41] the future clip is easily predictable
[01:06:44] from the representation of the pre- of
[01:06:46] the observed clip.
[01:06:48] Do you think YouTube has enough raw data
[01:06:52] from which to learn how to be a cat?
[01:06:56] I think so.
[01:06:57] So it the the amount of data is not the
[01:07:00] constraint.
[01:07:01] No. It would require some selection, I
[01:07:03] think.
[01:07:04] Some selection.
[01:07:05] some selection of, you know, maybe the
[01:07:07] right type of data. You need some
[01:07:08] down the rabbit hole of just cat videos.
[01:07:11] That might You might need to watch some
[01:07:12] lectures or something.
[01:07:14] No, you
[01:07:15] Wouldn't it How meta would that be
[01:07:17] if it like watches lectures about
[01:07:20] intelligence and then learns watches
[01:07:22] your lectures at NYU and learns from
[01:07:24] that how to be intelligent? That
[01:07:26] I don't think that would be enough.
[01:07:29] Uh what what's your Do you find
[01:07:31] multimodal learning interesting? We've
[01:07:33] been talking about visual language like
[01:07:35] if combining those together, maybe
[01:07:36] audio, all those kinds of things.
[01:07:38] There's a lot of things that I find
[01:07:39] interesting in the short term but are
[01:07:41] not addressing the important problem
[01:07:44] that I think are really kind of the big
[01:07:45] challenges. So, I think, you know,
[01:07:47] things like multitask learning,
[01:07:48] continual learning,
[01:07:50] uh you know,
[01:07:53] adversarial issues. I mean, those have,
[01:07:55] you know, great practical interests in
[01:07:57] the relatively short term
[01:07:59] uh possibly. But I don't think they're
[01:08:00] fundamental, you know, active learning,
[01:08:02] even to some extent reinforcement
[01:08:03] learning. I think those things will
[01:08:06] become either obsolete or or useless or
[01:08:10] easy
[01:08:11] Mhm.
[01:08:11] once we figure out how to do
[01:08:14] self-supervised representation learning
[01:08:15] or or learning predictive world models.
[01:08:19] And so, I think that's what, you know,
[01:08:21] the entire community should be focusing
[01:08:23] on.
[01:08:24] At least people who are interested in
[01:08:25] sort of fundamental questions or you
[01:08:27] know, really kind of pushing the
[01:08:28] envelope of of AI towards the next the
[01:08:30] next stage. But of course, there's like
[01:08:32] a huge amount of, you know, very
[01:08:33] interesting work to do in sort of
[01:08:34] practical questions that that have, you
[01:08:36] know, short-term impact.
[01:08:38] Well, you know,
[01:08:39] it's it's difficult to talk about the
[01:08:41] the temporal scale because
[01:08:43] all of human civilization will
[01:08:44] eventually be destroyed because the the
[01:08:47] the the sun will die out and even if
[01:08:49] Elon Musk is successful multi-planetary
[01:08:52] colonization across the galaxy,
[01:08:54] eventually the entirety of it would just
[01:08:56] become a giant black holes and uh
[01:09:00] That's going to take a while though.
[01:09:02] So, but but what I'm saying is then that
[01:09:04] logic can be used to say it's all
[01:09:05] meaningless.
[01:09:07] I'm saying all that to say that
[01:09:09] multitask learning
[01:09:11] might be your you're calling it
[01:09:14] practical or pragmatic or whatever. That
[01:09:17] might be the thing that achieves
[01:09:18] something very akin to intelligence
[01:09:22] while we're trying to solve the more
[01:09:25] uh general problem of self-supervised
[01:09:27] learning of practical knowledge. So, the
[01:09:29] reason I bring that up, maybe one
[01:09:31] way to ask that question. I've been very
[01:09:33] impressed by what uh Tesla autopilot
[01:09:35] team is doing. I don't know if you got a
[01:09:37] chance to glance at this particular one
[01:09:39] example of multitask learning where
[01:09:42] they're literally taking the problem
[01:09:44] like I don't know, Charles Darwin starts
[01:09:47] studying animals. They're studying the
[01:09:50] problem of driving and asking, "Okay,
[01:09:52] what are all the things you have to
[01:09:53] perceive?"
[01:09:54] And
[01:09:56] the way they're solving it is one,
[01:09:57] there's an ontology where you're
[01:09:59] bringing that to the table. So, you're
[01:10:00] formulating a bunch of different tasks.
[01:10:02] It's like over 100 tasks or something
[01:10:03] like that that they're involved in
[01:10:05] driving. And then they're deploying it
[01:10:07] and then getting data back from people
[01:10:09] that run into trouble and they're trying
[01:10:11] to figure out, "Do we add task? Do we
[01:10:13] like we focus on each individual task
[01:10:15] separately?" In fact, half So, the I
[01:10:17] would say I'll classify Andrej
[01:10:19] Karpathy's talking to is So, one was
[01:10:21] about doors and the other one about how
[01:10:23] much ImageNet sucks. He he kept he kept
[01:10:25] going
[01:10:26] back and forth on those two topics which
[01:10:29] ImageNet sucks meaning you can't just
[01:10:31] use a single benchmark. There's so like
[01:10:34] you you have to have like a a giant
[01:10:36] suite of benchmarks to understand how
[01:10:38] well your your system actually works.
[01:10:40] with him. I mean, he's
[01:10:41] he's he's a very sensible guy.
[01:10:43] Now,
[01:10:45] okay, it's it's very clear that if
[01:10:47] you're faced with a an engineering
[01:10:49] problem that you need to solve in a
[01:10:50] relatively short time, particularly if
[01:10:52] you have Elon Musk breathing down your
[01:10:54] neck,
[01:10:55] you're going to have to take shortcuts,
[01:10:57] right? You you You might think about the
[01:10:59] the fact that the the the right thing to
[01:11:02] do and the long-term solution involves,
[01:11:04] you know, some fancy
[01:11:05] self-supervisioning, but you have,
[01:11:08] you know, you have almost breathing on
[01:11:09] your neck, uh and, you know, this
[01:11:11] involves,
[01:11:12] uh you know, human lives, and so you you
[01:11:15] have to
[01:11:16] basically just do the systematic
[01:11:18] engineering and, you know,
[01:11:21] uh
[01:11:22] fine-tuning and refinements and trial
[01:11:23] and error and and all that stuff. Um
[01:11:26] there's nothing wrong with that. That's
[01:11:27] that's called engineering. That's
[01:11:28] called, you know, uh
[01:11:30] putting technology out uh in the
[01:11:34] yeah, in the world, um and and you have
[01:11:36] to kind of iron clad it before before
[01:11:39] you do this, you know, um
[01:11:41] uh
[01:11:43] so much for, you know, grand grand ideas
[01:11:45] and principles.
[01:11:46] Um
[01:11:48] but, you know, I'm placing myself sort
[01:11:50] of, you know, some
[01:11:53] you know, upstream of this, you know,
[01:11:54] quite a bit upstream of this.
[01:11:55] You're Plato thinking about Platonic
[01:11:57] forms. You're You're so
[01:11:59] Not Platonic because eventually uh I
[01:12:01] want us to have to get used, but uh it's
[01:12:04] okay if it takes 5 or 10 years for the
[01:12:07] community to realize this is the right
[01:12:08] thing to do. I've I've done this before.
[01:12:11] It's been the case before that, you
[01:12:12] know, I've made that that case. I mean,
[01:12:14] if you look back in the mid-2000s, for
[01:12:16] example, and you ask yourself the
[01:12:18] question, "Okay, I want to recognize
[01:12:19] cars or faces or whatever."
[01:12:22] Um
[01:12:24] you know, I can use convolutional nets,
[01:12:25] or I can use sort of more conventional
[01:12:27] uh kind of computer vision techniques,
[01:12:29] you know, using interest point detectors
[01:12:31] or SIFT dense features and, you know,
[01:12:34] sticking an SVM on top. At that time,
[01:12:36] the data sets were so small that those
[01:12:39] methods that used more hand engineering
[01:12:41] worked better than ConvNets. There was
[01:12:43] just not enough data for ConvNets. And
[01:12:45] ConvNets were were a little a little
[01:12:47] slow with the kind of hardware that was
[01:12:49] available at the time.
[01:12:50] And there was a sea change when uh
[01:12:53] basically when you know
[01:12:55] data sets became bigger and and GPUs
[01:12:57] became available. That that's what you
[01:12:59] know the
[01:13:01] two of the main factors that basically
[01:13:03] made people change their change their
[01:13:05] mind.
[01:13:06] Um
[01:13:07] and you can you can look at the history
[01:13:10] of
[01:13:11] like all sub branches of AI or pattern
[01:13:14] recognition.
[01:13:16] And there's a similar trajectory
[01:13:18] followed by techniques where people
[01:13:20] start by you know engineering the hell
[01:13:22] out of it.
[01:13:24] Um you know
[01:13:26] be it
[01:13:27] optical character recognition, speech
[01:13:29] recognition
[01:13:31] computer vision like image recognition
[01:13:32] in general,
[01:13:34] natural language understanding like you
[01:13:35] know translation, things like that,
[01:13:37] right? You start to engineer the hell
[01:13:38] out of it.
[01:13:40] Um you start to acquire all the
[01:13:42] knowledge the prior knowledge you know
[01:13:43] about image formation about you know the
[01:13:45] shape of characters about you know
[01:13:48] morphological operations about like
[01:13:50] feature extraction, Fourier transforms,
[01:13:52] you know Zernike moments, you know
[01:13:53] whatever, right? People have come up
[01:13:55] with thousands of ways of representing
[01:13:56] images so that you they could be easily
[01:13:59] classified afterwards. Same for speech
[01:14:02] recognition, right? There is
[01:14:03] you know two decades for people to
[01:14:05] figure out a good front end
[01:14:06] to pre process
[01:14:08] speech signals so that you know the
[01:14:10] information about what is being said is
[01:14:12] preserved but most of the information
[01:14:14] about the identity of the speaker is
[01:14:16] gone. Um
[01:14:18] you know cepstral coefficients or
[01:14:20] whatever, right? Um and same for for
[01:14:22] text, right?
[01:14:24] You do named entity recognition and you
[01:14:26] parse and you you you do tagging of
[01:14:31] of the parts of speech and you know you
[01:14:33] do this sort of tree representation of
[01:14:35] clauses and all that stuff, right?
[01:14:37] Before you can do anything.
[01:14:40] Um
[01:14:41] so
[01:14:43] that's how it starts, right? Just
[01:14:45] engineer the hell out of it. And then,
[01:14:47] you start having data,
[01:14:48] and maybe you have more powerful
[01:14:50] computers, maybe you know something
[01:14:52] about statistical learning. So, you
[01:14:53] start using machine learning, and it's
[01:14:54] usually a small sliver on top of your
[01:14:56] kind of hand-crafted system, where, you
[01:14:58] know, you extract features by hand.
[01:15:00] Okay, and now, you know, nowadays, the
[01:15:02] standard way of doing this is that you
[01:15:04] train the entire thing end-to-end with a
[01:15:05] deep learning system, and it learns its
[01:15:07] own features, and and, you know, speech
[01:15:09] recognition systems nowadays,
[01:15:11] uh or OCR systems, are completely
[01:15:13] end-to-end. It's you know, it's some
[01:15:15] giant neural net that takes raw
[01:15:17] waveforms and produces a sequence of
[01:15:20] characters coming out. And it's just a
[01:15:21] huge neural net, right? There's no
[01:15:24] you know, Markov model, there's no
[01:15:25] language model that is explicit other
[01:15:27] than, you know, something that's
[01:15:29] ingrained in the in the sort of neural
[01:15:30] language model, if you want. Same for
[01:15:32] translation, same for all kinds of
[01:15:34] stuff. So, you see this continuous
[01:15:36] evolution from
[01:15:39] you know, less and less hand-crafting
[01:15:41] and more and more learning.
[01:15:43] Um and uh I I think uh
[01:15:47] I mean, it's true in biology as well.
[01:15:49] Uh
[01:15:50] so, I mean, we might disagree about
[01:15:52] this, maybe not uh in the this one
[01:15:55] little piece at the end. You mentioned
[01:15:57] active learning.
[01:15:59] It feels like active learning, which is
[01:16:01] the selection of data, and also the
[01:16:03] interactivity, needs to be part of this
[01:16:05] giant neural network. You cannot just be
[01:16:07] an observer to do self-supervised
[01:16:09] learning. You have to Well,
[01:16:11] I don't self-supervised learning is just
[01:16:13] a word, but I would Whatever this giant
[01:16:16] stack of a neural network that's
[01:16:18] automatically learning, it feels My
[01:16:21] intuition is
[01:16:22] that
[01:16:24] you have to have a system, whether it's
[01:16:26] a physical robot or a digital robot,
[01:16:30] that's interacting with the world, and
[01:16:32] doing so in a flawed way, and improving
[01:16:35] over time.
[01:16:36] In order to to form the self-supervised
[01:16:40] learning well, you can't just give it a
[01:16:42] giant sea of data. I agree and I
[01:16:45] disagree.
[01:16:46] Okay.
[01:16:47] I agree in the sense that I think
[01:16:50] I agree I agree in two ways. The first
[01:16:52] The first way I agree is that if you
[01:16:53] want
[01:16:55] and you certainly need a causal model of
[01:16:57] the world that allows you to predict the
[01:16:58] consequences of your actions.
[01:17:00] To train that model, you need to take
[01:17:01] actions. Right? You need to be able to
[01:17:03] act in a world and see the effect
[01:17:06] for you to be to learn causal models of
[01:17:07] the world.
[01:17:08] Well, so that's not that's not obvious
[01:17:09] because you can observe others.
[01:17:11] You can observe others.
[01:17:12] can infer that they're similar to you
[01:17:14] and then you can learn from that.
[01:17:16] Yeah, but then you have to kind of
[01:17:17] hardwire that part, right? And you know,
[01:17:19] mirror neurons and all that stuff,
[01:17:20] right? So
[01:17:22] and it's not clear to me how you would
[01:17:23] do this in a machine. So
[01:17:26] So I think the the action part would be
[01:17:29] necessary for having causal models of of
[01:17:31] the world.
[01:17:32] The second reason it may be necessary or
[01:17:36] at least more efficient is that active
[01:17:40] learning basically, you know, goes for
[01:17:42] the jugular of what you what you don't
[01:17:43] know, right? This this you know, obvious
[01:17:46] areas of uncertainty about your your
[01:17:49] world and about the how the world
[01:17:51] behaves.
[01:17:52] And you can resolve this uncertainty by
[01:17:57] systematic exploration of that part that
[01:17:59] you don't you don't know. And if you
[01:18:00] know that you don't know, then you know,
[01:18:02] it makes you curious. You kind of look
[01:18:03] into situations that And
[01:18:06] you know, across the animal world, the
[01:18:09] different species have different levels
[01:18:11] of curiosity,
[01:18:12] Curiosity, right?
[01:18:13] depending on how they're built, right?
[01:18:15] So you know, cats and rats are
[01:18:17] incredibly curious. Dogs not so much. I
[01:18:19] mean less.
[01:18:20] Yeah. So it could be useful to have that
[01:18:22] kind of curiosity.
[01:18:23] So it would be useful, but curiosity
[01:18:25] just makes the process faster. It
[01:18:27] doesn't make the process exist.
[01:18:29] The So what process what learning
[01:18:32] process
[01:18:33] is it that active learning makes more
[01:18:37] efficient.
[01:18:37] Mhm.
[01:18:38] And I'm asking that first question. Uh
[01:18:40] you know,
[01:18:43] you know, we haven't answered that
[01:18:44] question yet. So, you know, I'll worry
[01:18:45] about active learning once this question
[01:18:47] is
[01:18:47] So, that's the more fundamental question
[01:18:49] to ask. And if active learning or
[01:18:53] interaction increases the efficiency of
[01:18:56] the learning, see, sometimes
[01:18:58] it becomes very different if the
[01:19:00] increase is several orders of magnitude.
[01:19:03] Right? Like
[01:19:04] That's true.
[01:19:05] But fundamentally it's still the same
[01:19:07] thing and building up the intuition
[01:19:09] about how to
[01:19:11] in a self-supervised way to construct
[01:19:12] background models, efficient or
[01:19:14] inefficient, is um is the core problem.
[01:19:18] What do you think about Yoshua Bengio's
[01:19:20] uh talking about consciousness
[01:19:22] and all of these kinds of concepts?
[01:19:24] Okay. Um
[01:19:26] I don't know what consciousness is.
[01:19:28] But
[01:19:29] uh
[01:19:30] It's a good opener.
[01:19:31] And to some extent a lot of the things
[01:19:33] that are said about consciousness remind
[01:19:35] me of
[01:19:37] the questions people were asking
[01:19:38] themselves in the 18th century or 17th
[01:19:40] century when they discovered that
[01:19:43] uh you know, how the eye works and the
[01:19:45] fact that the image at the back of the
[01:19:46] eye was
[01:19:48] upside down.
[01:19:49] Mhm.
[01:19:49] Right? Because you have a lens and and
[01:19:51] so on your retina the image that forms
[01:19:53] is an image of the world, but it's
[01:19:54] upside down. How is it that you see
[01:19:56] right side up?
[01:19:58] And you know, with what we know today in
[01:19:59] science, you know, we realize this
[01:20:01] question doesn't make any sense
[01:20:03] or or is kind of ridiculous in some way,
[01:20:05] right? So, I think a lot of what is said
[01:20:07] about consciousness is of that nature.
[01:20:08] Now, that said, there's a lot of really
[01:20:10] smart people that
[01:20:11] uh for for whom I have a lot of respect
[01:20:13] who are talking about this topic, people
[01:20:15] like uh David Chalmers, who is a
[01:20:16] colleague of mine at NYU.
[01:20:18] Um
[01:20:19] I have kind of a
[01:20:21] unorthodox folk
[01:20:24] um
[01:20:25] speculative
[01:20:27] hypothesis about consciousness. So,
[01:20:29] we're talking about this idea of world
[01:20:30] model.
[01:20:31] Mhm.
[01:20:31] And uh I think, you know, our entire
[01:20:34] prefrontal cortex basically is
[01:20:36] uh the engine for our world model.
[01:20:40] Uh but when we are attending at a
[01:20:42] particular situation,
[01:20:44] we're focused on that situation. We
[01:20:46] basically cannot attend to anything
[01:20:47] else.
[01:20:48] And that seems to suggest
[01:20:52] that we basically have only one
[01:20:55] world model engine in our prefrontal
[01:20:57] cortex.
[01:20:59] Uh that engine is configurable to the
[01:21:01] situation at hand. So, we're building a
[01:21:03] box out of wood or we are, you know,
[01:21:05] driving uh
[01:21:07] down the highway, playing chess. We we
[01:21:09] we basically have uh a single model of
[01:21:12] the world that we configure into the
[01:21:13] situation at hand.
[01:21:15] Which is why we can only attend to one
[01:21:16] task at a time.
[01:21:19] Now, if there is a task that we do
[01:21:20] repeatedly,
[01:21:22] um
[01:21:22] it it goes from the sort of deliberate
[01:21:25] reasoning using model of the world and
[01:21:26] prediction and perhaps something like
[01:21:28] model predictive control, which I was
[01:21:29] talking about earlier,
[01:21:31] to something that is more subconscious,
[01:21:33] that becomes automatic. So, I don't know
[01:21:35] if you've ever played against a chess
[01:21:37] grandmaster.
[01:21:38] Uh
[01:21:38] you know, I get wiped out in, you know,
[01:21:40] 10
[01:21:41] 10 plays, right? Uh and you know, I have
[01:21:44] to think about my move for, you know,
[01:21:47] like 15 minutes.
[01:21:49] Uh
[01:21:50] and the person in front of me, the
[01:21:51] grandmaster, you know, would just like
[01:21:53] react within seconds, right? Uh
[01:21:56] you know, he doesn't need to think about
[01:21:58] it. That's become part of subconscious
[01:21:59] because, you know, it's basically just
[01:22:01] pattern recognition at this point.
[01:22:03] Um
[01:22:04] same, you know, you the first few hours
[01:22:06] you drive a car, you are really
[01:22:08] attentive. You can't do anything else.
[01:22:09] And then after 20, 30 hours of practice,
[01:22:11] 50 hours,
[01:22:13] you know, it's subconscious. You can
[01:22:14] talk to the person next to you, you
[01:22:15] know, things like that, right?
[01:22:17] Unless the situation becomes
[01:22:18] unpredictable and then you have to stop
[01:22:19] talking.
[01:22:20] Um so, that suggests you only have one
[01:22:22] model in your head.
[01:22:24] And
[01:22:26] it might suggest the idea that
[01:22:27] consciousness basically is the module
[01:22:28] that configures this world model of
[01:22:30] yours. You know, you need to have some
[01:22:32] sort of
[01:22:33] uh executive kind of overseer that
[01:22:37] configures your world model for the
[01:22:38] situation at hand.
[01:22:40] And that that leads to the kind of the
[01:22:42] really curious concept that uh
[01:22:44] consciousness is not a consequence of
[01:22:46] the power of our minds, but of the
[01:22:48] limitation of our brains.
[01:22:49] But because we have only one world
[01:22:51] model, we have to be conscious. If we
[01:22:53] had as many world models as
[01:22:56] there are uh situations we encounter,
[01:22:58] then we could do all of them
[01:23:00] simultaneously and we wouldn't need this
[01:23:01] sort of executive control that we call
[01:23:03] consciousness.
[01:23:04] Yeah, interesting. And somehow maybe
[01:23:06] that executive controller I mean, the
[01:23:09] the hard problem of consciousness.
[01:23:10] There's some kind of chemicals and
[01:23:12] biology that's creating a feeling
[01:23:14] like it feels to experience some of
[01:23:16] these things.
[01:23:18] That that's kind of like the hard
[01:23:21] question is
[01:23:22] what the heck is that and why is that
[01:23:24] useful? Maybe you know, a pragmatic
[01:23:25] question. Why is it useful to feel like
[01:23:28] this is really you experiencing this
[01:23:31] versus just like information being
[01:23:33] processed.
[01:23:35] Um yeah, it could be just a very nice
[01:23:37] side effect of um
[01:23:40] of the way we evolved. That's just very
[01:23:42] um useful to
[01:23:44] to uh feel a sense of uh ownership to
[01:23:48] the decisions you make, to the
[01:23:50] perceptions you make, to the model
[01:23:51] you're trying to maintain. Like you own
[01:23:53] this thing.
[01:23:54] And this is the only one you got and if
[01:23:56] you lose it, it's going to really suck.
[01:23:58] And so you should really send the brain
[01:24:00] some signals about it.
[01:24:03] What ideas do you believe might be true
[01:24:06] that most or at least many people
[01:24:08] disagree with you with?
[01:24:11] Let's say in the space of machine
[01:24:12] learning.
[01:24:13] Well, it depends who you talk about, but
[01:24:15] um I think
[01:24:16] so certainly there is
[01:24:18] uh
[01:24:19] a bunch of people who are nativist,
[01:24:20] right? Who thinks that a lot of the
[01:24:22] basic things about the world are kind of
[01:24:23] hardwired in our in our minds.
[01:24:25] Um things like, you know, the world is
[01:24:27] three-dimensional, for example. Is that
[01:24:29] hardwired?
[01:24:30] Things like uh you know, object
[01:24:32] permanence. Is this something that we
[01:24:33] learn uh
[01:24:34] you know, before the age of 3 months or
[01:24:36] so? Or or are we born with it? And there
[01:24:39] are, you know, very dis- you know,
[01:24:41] wide disagreement among the you know,
[01:24:43] cognitive scientists uh uh for this.
[01:24:46] I think those things are actually very
[01:24:47] simple to learn.
[01:24:49] Um you know, is it the case that the
[01:24:52] oriented edge detectors in V1 are
[01:24:54] learned or are they hardwired? I think
[01:24:56] they're learned. They might be learned
[01:24:57] before birth because it's really easy to
[01:24:59] generate signals from the retina that
[01:25:01] are actually will train edge detectors.
[01:25:02] So,
[01:25:04] um and again, those are
[01:25:05] things that can be learned within
[01:25:06] minutes of uh opening your eyes, right?
[01:25:09] I mean, uh
[01:25:11] you know, since the 1990s, we have
[01:25:13] algorithms that can learn oriented edge
[01:25:14] detectors completely unsupervised with
[01:25:17] the equivalent of a few minutes of real
[01:25:18] time. So,
[01:25:19] uh so, those things have to be learned.
[01:25:21] Um and there's also those, you know, MIT
[01:25:23] experiments where you kind of
[01:25:25] plug the
[01:25:27] optical nerve on the auditory cortex of
[01:25:29] a baby ferret, right? And that auditory
[01:25:30] cortex become a visual cortex,
[01:25:32] essentially.
[01:25:33] So, you know, clearly, um there's
[01:25:35] learning taking place there.
[01:25:37] Um so, you know, I think a lot of what
[01:25:39] people think are so basic that they need
[01:25:41] to be hardwired,
[01:25:43] I think a lot of those things are
[01:25:44] learned because they're easy to learn.
[01:25:45] Do you So, you put a lot of
[01:25:47] value in the power of learning. What
[01:25:50] kind of things do you suspect might not
[01:25:52] be learned?
[01:25:53] Is there something that could not be
[01:25:54] learned?
[01:25:56] So, your intrinsic drives are not
[01:25:58] learned. They They They are the things
[01:26:00] that, you know, make humans uh
[01:26:02] human or make, you know,
[01:26:05] cats different from dogs, right? It's
[01:26:07] the the basic drives that are kind of
[01:26:09] hardwired in our
[01:26:10] basal ganglia. Um
[01:26:13] I mean, there are people who are working
[01:26:13] on on this kind of stuff. It's called
[01:26:15] intrinsic motivation in the context of
[01:26:16] reinforcement learning. Um so these are
[01:26:19] objective functions where the reward
[01:26:20] doesn't come from the external world,
[01:26:23] it's computed by your own brain. Your
[01:26:24] own brain computes
[01:26:26] whether you are happy or not, right? It
[01:26:28] measures your degree of
[01:26:30] uh
[01:26:30] comfort or incomfort.
[01:26:33] Uh and and because it's your brain
[01:26:35] computing this, presumably it knows also
[01:26:37] how to estimate gradients of this,
[01:26:38] right? So
[01:26:39] um
[01:26:40] Um so it's easier to to learn when your
[01:26:43] objective is is intrinsic.
[01:26:46] Um so that has to be hardwired.
[01:26:49] Uh the critic that makes long-term
[01:26:51] prediction of the outcome, which is the
[01:26:53] eventual
[01:26:54] result of this, that's learned.
[01:26:57] Uh and perception is learned and your
[01:26:59] model of the world is learned. But let
[01:27:01] me take take an example of, you know,
[01:27:02] why the critic I mean example of why the
[01:27:05] critic may be learned, right? If I um if
[01:27:07] I come to you um
[01:27:09] you know, I reach across the table and I
[01:27:11] I pinch your arm, right? Complete
[01:27:13] surprise for you.
[01:27:15] You would not have expected this from
[01:27:16] me.
[01:27:16] expecting that the whole time, but yes,
[01:27:17] right. Let's say for the the sake of the
[01:27:19] story, yes.
[01:27:21] Um okay, your basal ganglia is going to
[01:27:24] light up cuz it's going to hurt, right?
[01:27:27] Um and now your model of the world
[01:27:29] includes the fact that I may pinch you
[01:27:31] if I approach my uh
[01:27:34] my uh
[01:27:34] Don't trust humans.
[01:27:36] Right. My hand to your arm. So if I try
[01:27:38] again, you're going to recoil and that's
[01:27:40] your critic
[01:27:42] uh your predictive
[01:27:44] you know, your predictor your
[01:27:45] uh ultimate pain
[01:27:47] uh
[01:27:49] system
[01:27:50] that predicts that something bad is
[01:27:51] going to happen and you recoil to avoid
[01:27:53] it.
[01:27:53] So even that can be learned.
[01:27:55] That is learned, definitely. This is
[01:27:56] what allows you also to uh you know,
[01:27:59] define subgoals, right? So
[01:28:01] um the fact that, you know, you're a
[01:28:03] schoolchild, you wake up in the morning
[01:28:05] and you go to school and, you know,
[01:28:07] um
[01:28:09] it's not because you necessarily like
[01:28:11] waking up early and going to school, but
[01:28:13] you know that there is a long-term
[01:28:14] objective you're trying to optimize.
[01:28:15] So, Ernest Becker, I'm not sure if
[01:28:17] you're familiar with him, he's a
[01:28:18] philosopher. He wrote the book The
[01:28:20] Denial of Death, and his idea is that
[01:28:22] one of the core motivations of human
[01:28:23] beings is our terror of death, our fear
[01:28:25] of death.
[01:28:27] Uh that's what makes us unique from
[01:28:28] cats. Cats are just surviving. They do
[01:28:30] not have a
[01:28:32] deep under- like um cognizance,
[01:28:36] introspection that
[01:28:39] over the horizon is the end.
[01:28:41] And he says that I mean, there's a
[01:28:43] terror management theory, that's just
[01:28:44] all these psychological experiments that
[01:28:46] show
[01:28:47] the basically
[01:28:49] this idea that
[01:28:51] all of human civilization, everything we
[01:28:53] create is kind of trying to forget, if
[01:28:57] even for a brief moment, that we're
[01:28:58] going to die.
[01:29:00] When when do you think humans understand
[01:29:03] that they're going to die? Is it learned
[01:29:05] early on?
[01:29:06] Also, like
[01:29:09] I don't know to at what point. I mean,
[01:29:11] it's a it's a question like, you know,
[01:29:12] at what point do you realize that, you
[01:29:14] know, what death really is. And I think
[01:29:16] most people don't actually realize what
[01:29:18] death is, right? I mean, most people
[01:29:19] believe that you go to heaven or
[01:29:20] something, right?
[01:29:21] Well, so the the pushback on that what
[01:29:24] Ernest Becker says and um Sheldon
[01:29:27] Solomon all those folks,
[01:29:29] and I find those ideas a little bit
[01:29:31] compelling, is that there is moments in
[01:29:32] life, early in life, a lot of this fun
[01:29:35] happens early in life,
[01:29:36] when you are
[01:29:38] uh when you do deeply experience the
[01:29:41] terror of this realization, and all the
[01:29:44] things you think about about religion,
[01:29:45] all those kinds of things that we kind
[01:29:47] of think about more like teenage years
[01:29:49] and later,
[01:29:50] we're talking about way earlier.
[01:29:52] No, it's like 7 or 8 years, something
[01:29:53] like that, yeah.
[01:29:54] You realize
[01:29:56] holy crap,
[01:29:57] this is uh like the mystery, the terror,
[01:30:00] like it's almost like you're a little
[01:30:02] prey, a little baby deer sitting in the
[01:30:04] darkness of the jungle, of the woods,
[01:30:06] looking all around you, there's darkness
[01:30:08] full of terror. I mean, that's That
[01:30:10] realization says, "Okay, I'm going to go
[01:30:12] go back in the comfort of my mind where
[01:30:14] there's a where there is a deep meaning,
[01:30:16] where there is a
[01:30:18] maybe like pretend I'm immortal in
[01:30:20] however way
[01:30:22] however kind of idea I can construct to
[01:30:25] help me understand that I'm immortal."
[01:30:27] Religion helps with that. You can You
[01:30:29] can delude yourself in all kinds of
[01:30:30] ways. Like lose yourself in the busyness
[01:30:33] of each day. Have little goals in mind,
[01:30:35] all those kinds of things to think that
[01:30:36] it's going to go on forever. And you
[01:30:38] kind of know you're going to die, yeah,
[01:30:40] and it's going to be sad, but you don't
[01:30:42] really understand that you're going to
[01:30:44] die. And so that's that's their idea.
[01:30:46] And if I find that compelling
[01:30:48] because it does seem to be a core unique
[01:30:51] aspect of human nature that we're we're
[01:30:53] able to think that we're go we're able
[01:30:55] to really understand that this life is
[01:30:58] finite. I I seems important.
[01:31:00] There's There's a bunch of different
[01:31:01] things there. So, first of all, I don't
[01:31:03] think there is a qualitative difference
[01:31:04] between between us and cats in the term
[01:31:07] I think the difference is that we just
[01:31:09] have a better long-term
[01:31:11] ability to predict, you know, in the
[01:31:14] long term. And so, we have better
[01:31:15] understanding of how the world works.
[01:31:17] So, we have better understanding of, you
[01:31:18] know, finiteness of life and things like
[01:31:20] that.
[01:31:21] have a better planning engine than cats?
[01:31:23] Yeah.
[01:31:24] Okay.
[01:31:25] But what's the motivation for
[01:31:27] for planning that far?
[01:31:28] Well, I think it's just a side effect of
[01:31:30] the fact that we have just a better
[01:31:31] planning engine because it makes us
[01:31:33] As I said, you know, the essence of
[01:31:35] intelligence is the ability to predict.
[01:31:37] And so, the because we're smarter
[01:31:40] as a side effect, we also have this
[01:31:41] ability to kind of make predictions
[01:31:43] about our own
[01:31:45] future existence or lack thereof.
[01:31:47] Okay.
[01:31:47] Um you say religion helps with that. I
[01:31:50] think religion hurts, actually. Um it
[01:31:53] makes people worry about like, you know,
[01:31:54] what's going to happen after their
[01:31:55] death, etc.
[01:31:57] If you believe that, you know,
[01:31:59] you just don't exist after death. Like,
[01:32:00] you know, it solves completely the
[01:32:01] problem. At least
[01:32:02] you're saying if you don't believe in
[01:32:04] God, you don't worry about what happens
[01:32:06] after death?
[01:32:07] Yeah.
[01:32:08] I don't know.
[01:32:08] You only worry about the about you know,
[01:32:11] this life because that's the only one
[01:32:12] you have.
[01:32:14] I think it's well, I don't know I don't
[01:32:15] know. If I were to say what Ernest
[01:32:17] Becker says and I would say I agree with
[01:32:18] him more
[01:32:20] uh than not is uh
[01:32:23] you do deeply worry.
[01:32:25] Uh if you if you believe there's no God,
[01:32:27] there's still a deep worry like of the
[01:32:30] mystery of it all. Like, how does that
[01:32:32] make any sense that it just ends? I
[01:32:35] don't think we can truly understand that
[01:32:38] this right end I mean, so much of our
[01:32:40] life, the consciousness, the ego is uh
[01:32:43] invested in this in this being and then
[01:32:47] So, science keeps bringing humanity down
[01:32:49] from its pedestal.
[01:32:51] And that's that's just another another
[01:32:53] example of it.
[01:32:54] That's wonderful, but for us individual
[01:32:57] humans, we don't like to be brought down
[01:32:59] from a pedestal. You're fine with it
[01:33:00] like what But see, you're fine with it
[01:33:02] because well, so what Ernest Becker
[01:33:05] would say is you're fine with it because
[01:33:06] that's just a more peaceful existence
[01:33:08] for you, but you're not really fine.
[01:33:09] You're hiding from In fact, some of the
[01:33:11] people that experienced the deepest
[01:33:13] trauma
[01:33:14] uh that it earlier in life, they'll they
[01:33:17] often before they seek extensive therapy
[01:33:19] will say that I'm fine. It's like uh
[01:33:21] when you talk to people who are truly
[01:33:22] angry, how are you doing? I'm fine. The
[01:33:25] The question is, what's going on?
[01:33:27] Now, I had a near-death experience. I
[01:33:29] had a very bad uh motorbike accident
[01:33:32] when I was 17. So,
[01:33:34] And
[01:33:34] uh but that didn't have any impact on my
[01:33:39] reflection on that topic.
[01:33:40] So, I'm I'm basically just playing a bit
[01:33:42] of devil's advocate, pushing back on
[01:33:44] wondering
[01:33:45] is it truly possible to accept death?
[01:33:47] And the flip side that's more
[01:33:48] interesting, I think, for AI and
[01:33:51] robotics is how important is it to have
[01:33:54] this as one of the suite of motivations
[01:33:57] is to
[01:33:59] uh not just avoid
[01:34:02] falling off the roof or something like
[01:34:03] that, but
[01:34:05] ponder
[01:34:06] the the end of the ride.
[01:34:09] Well, if you listen to the Stoics,
[01:34:12] it's uh it's a great motivator. It adds
[01:34:15] a sense of urgency. So, maybe you're to
[01:34:18] truly fear death or be cognitive of it
[01:34:21] might give
[01:34:23] uh a deeper meaning and urgency to the
[01:34:25] moment to live
[01:34:27] fully.
[01:34:28] Well, I mean I mean
[01:34:30] maybe I don't disagree with that. Uh I
[01:34:32] mean I think what what it is to me here
[01:34:34] is
[01:34:35] uh
[01:34:36] you know, knowing more about about human
[01:34:38] nature. I mean I think uh human nature
[01:34:40] and human intelligence is a big mystery.
[01:34:42] It's a scientific mystery.
[01:34:43] Mhm.
[01:34:44] Uh in addition to, you know,
[01:34:46] philosophical and etc. But, you know,
[01:34:49] I'm a true believer in science. So,
[01:34:51] um
[01:34:52] I and and and I do have kind of a belief
[01:34:56] that for complex systems like like the
[01:34:58] brain and the mind,
[01:34:59] the the way to
[01:35:02] understand it is try to reproduce it
[01:35:04] with uh you know, artifacts that you
[01:35:06] build because you know what's essential
[01:35:08] to it when you try to build it. You
[01:35:10] know, the same way um I've used this
[01:35:11] analogy before with you, I believe. Um
[01:35:14] the same way we we only started to
[01:35:15] understand uh
[01:35:17] aerodynamics when we started building
[01:35:18] airplanes, and that helped us understand
[01:35:20] how birds fly.
[01:35:21] Uh you know, so I I I think there's kind
[01:35:23] of a a similar process here where
[01:35:26] we don't have a theory of a full theory
[01:35:28] of intelligence,
[01:35:29] but building, you know, intelligent
[01:35:31] artifacts will help us perhaps develop
[01:35:33] some,
[01:35:34] you know, underlying theory that uh
[01:35:36] encompasses not just artificial
[01:35:38] implements, but also uh
[01:35:41] human and biological intelligence in
[01:35:43] general.
[01:35:43] So, you're an interesting person to ask
[01:35:45] this question about sort of all kinds of
[01:35:48] different other intelligent entities
[01:35:51] or intelligences.
[01:35:53] What are your thoughts about kind of
[01:35:55] like the Turing or the Chinese room
[01:35:57] question?
[01:35:59] If we create an AI system that exhibits
[01:36:02] a lot of properties of intelligence and
[01:36:05] consciousness,
[01:36:07] how comfortable are you thinking of that
[01:36:09] entity as intelligent or conscious?
[01:36:12] So So you're trying to build now systems
[01:36:14] that have intelligence and there's
[01:36:15] metrics about their performance, but
[01:36:17] that metric
[01:36:19] is
[01:36:20] external.
[01:36:22] Okay.
[01:36:22] So how are you Are you okay calling a
[01:36:25] thing intelligent? Or are you going to
[01:36:27] be like most humans
[01:36:29] and be uh
[01:36:30] once again unhappy to be brought down
[01:36:32] from a pedestal of consciousness {slash}
[01:36:34] intelligence?
[01:36:34] No, I'm I'll be very happy to
[01:36:38] understand
[01:36:40] uh
[01:36:41] more about uh human nature, human mind,
[01:36:43] and human intelligence through the
[01:36:46] construction of machines that
[01:36:48] um
[01:36:48] have similar abilities. And
[01:36:51] if a consequence of this is to bring
[01:36:53] down humanity one notch down from
[01:36:56] its already low pedestal, I'm just fine
[01:36:58] with it. That's just reality of life.
[01:37:00] Um so I'm I'm fine with that. Now,
[01:37:02] you're asking me about things that uh
[01:37:04] opinions I have that a lot of people may
[01:37:06] disagree with.
[01:37:07] I think
[01:37:09] uh
[01:37:11] if we think about the design of an
[01:37:12] autonomous intelligence system, so
[01:37:14] assuming that we are somewhat successful
[01:37:16] at some at some level
[01:37:18] of getting machines to learn models of
[01:37:20] the world, predictive models of the
[01:37:21] world, uh we have we build intrinsic
[01:37:24] motivation objective functions to drive
[01:37:26] the behavior of that system. Uh the
[01:37:28] system also has perception modules that
[01:37:30] allows it to estimate the state of the
[01:37:31] world, and then have some way of
[01:37:34] figuring out the sequence of actions
[01:37:35] that, you know, to optimize a particular
[01:37:37] objective.
[01:37:39] If it has a critic of the type that was
[01:37:41] describing before, the thing that makes
[01:37:43] you recall your arm the second time I
[01:37:45] tried to pinch you.
[01:37:46] Um
[01:37:48] intelligent autonomous machine will have
[01:37:50] emotions.
[01:37:51] I think emotions are an integral part of
[01:37:54] autonomous intelligence.
[01:37:56] If you have an intelligent system
[01:37:58] that is driven by uh intrinsic
[01:38:01] motivation, by objectives,
[01:38:03] if it has a critic that allows you to
[01:38:06] predict in advance whether the outcome
[01:38:08] of a
[01:38:09] of a situation is going to be good or
[01:38:10] bad, it's going to have emotions. It's
[01:38:12] going to have fear.
[01:38:13] Yes.
[01:38:14] Uh when it predicts that the outcome is
[01:38:16] going to is going to be bad
[01:38:18] and and something to avoid, it's going
[01:38:19] to have elation when it predicts it's
[01:38:21] going to be good.
[01:38:22] Um
[01:38:23] uh if it has drives to relate with
[01:38:26] humans, um
[01:38:28] you know, in some ways, the way humans
[01:38:29] have,
[01:38:31] um
[01:38:32] you know, it's it's going to be social,
[01:38:33] right? And so, it's going to have
[01:38:35] emotions about attachment and and things
[01:38:38] of that type. So,
[01:38:39] um so, I think uh you know, the the sort
[01:38:41] of
[01:38:42] sci-fi
[01:38:44] thing where, you know, you see Commander
[01:38:46] Data like having an emotion chip that he
[01:38:48] can turn off, right? Um I think that's
[01:38:50] ridiculous.
[01:38:51] So, I mean, here's the difficult
[01:38:53] philosophical
[01:38:55] social question.
[01:38:57] Do you think there will be a time
[01:39:00] like a civil rights movement for robots
[01:39:02] where
[01:39:03] um okay, forget the movement, but a
[01:39:05] discussion at like the Supreme Court
[01:39:09] that particular kinds of robots,
[01:39:12] you know, particular kinds of systems,
[01:39:15] um deserve the same rights as humans
[01:39:18] because they can suffer just as humans
[01:39:21] can.
[01:39:22] Um all those kinds of things.
[01:39:24] Well,
[01:39:26] perhaps, perhaps not. Like, imagine that
[01:39:27] humans were that that you could uh
[01:39:31] you know, die and be restored. Like, you
[01:39:34] know, you could be sort of you know, be
[01:39:35] 3D re-printed and you know, your brain
[01:39:37] could be re- reconstructed in its finest
[01:39:39] details.
[01:39:40] Our ideas of rights will change in that
[01:39:42] case. If you can always just
[01:39:45] there's always a backup, you could
[01:39:47] always restore. Maybe like the the
[01:39:49] importance of murder will go down one
[01:39:51] notch.
[01:39:51] That's right. But also the
[01:39:54] your your
[01:39:55] you know, desire to do dangerous things
[01:39:57] like you know
[01:39:59] you know, skydiving or
[01:40:01] you know
[01:40:02] or
[01:40:03] or you know, race car driving
[01:40:05] you know, car racing or that kind of
[01:40:06] stuff you know, would probably increase.
[01:40:09] Or or you know, airplane aerobatics or
[01:40:11] that kind of stuff, right? You would be
[01:40:12] fine to do a lot of those things or
[01:40:14] explore you know, dangerous areas and
[01:40:16] things like that. It would kind of
[01:40:17] change your relationship. So now it's
[01:40:20] very likely that robots would be like
[01:40:21] that because you know, they'll be
[01:40:25] based on perhaps technology that is
[01:40:27] somewhat similar to
[01:40:29] today's technology and you can you can
[01:40:30] always have a backup.
[01:40:32] So it's possible
[01:40:34] I don't know if you like video games,
[01:40:35] but there's a there's a game called
[01:40:37] Diablo and um
[01:40:39] Oh, my my sons are huge fans of this.
[01:40:41] Yes.
[01:40:44] And
[01:40:44] they made a game that inspired by it.
[01:40:47] Awesome. Like built a game?
[01:40:48] My my three sons have a a game design
[01:40:51] studio between them. Yeah. They came out
[01:40:53] with a game
[01:40:54] Like just came out with a game.
[01:40:55] last year. No, this was last year early
[01:40:56] this about a year ago.
[01:40:58] That's awesome. But so in Diablo there's
[01:41:00] a something called hardcore mode which
[01:41:02] if you die, there's no
[01:41:04] you're gone.
[01:41:05] Right.
[01:41:05] That's it. And so it's possible with AI
[01:41:08] systems
[01:41:10] for them to be able to operate
[01:41:12] successfully and for us to treat them in
[01:41:14] a certain way for because they have to
[01:41:16] be integrated in human society
[01:41:18] they have to be able to die, no copies
[01:41:21] allowed. In fact, copying is illegal.
[01:41:23] It's possible with humans as well like
[01:41:25] cloning will be illegal even when it's
[01:41:27] possible. Good
[01:41:28] But cloning is not copying, right? I
[01:41:29] mean, you don't reproduce the
[01:41:31] Well
[01:41:31] the the mind of the person and
[01:41:33] experience.
[01:41:33] Right.
[01:41:34] It's just a delayed twin. So
[01:41:36] But then it's But were talking about
[01:41:38] with computers that you would be able to
[01:41:39] copy you you would be able to perfectly
[01:41:41] save pickle
[01:41:43] the the the mind state. And it's
[01:41:47] possible that that would be illegal.
[01:41:49] Because
[01:41:50] that goes against um
[01:41:53] that will destroy the motivations of the
[01:41:54] system.
[01:41:55] Okay, so let's say you you have a
[01:41:57] domestic robot, okay, uh sometime in the
[01:42:00] future.
[01:42:01] Yes.
[01:42:02] And uh the domestic robot, you know,
[01:42:05] comes to you kind of somewhat
[01:42:06] pre-trained, you know, it can do a bunch
[01:42:07] of things.
[01:42:08] Yes.
[01:42:08] But it has a particular personality that
[01:42:10] makes it slightly different from the
[01:42:11] other robots because that makes them
[01:42:13] more interesting. And then because it's,
[01:42:15] you know, it's lived with you for 5
[01:42:17] years, you've you've grown some
[01:42:18] attachment to it and vice versa, and
[01:42:22] it's learned a lot about you.
[01:42:23] Mhm.
[01:42:24] Or maybe it's not a household robot,
[01:42:25] maybe it's uh maybe it's a virtual
[01:42:27] assistant that lives in your, you know,
[01:42:29] augmented reality glasses or whatever,
[01:42:31] right?
[01:42:31] Yeah.
[01:42:32] Uh you know, the the Her movie type
[01:42:34] thing, right? Um
[01:42:36] and that system to some extent the the
[01:42:40] intelligence in that system
[01:42:42] is a bit like your child or maybe a PhD
[01:42:44] student in the sense that there's a lot
[01:42:47] of you in that in that machine now,
[01:42:49] right?
[01:42:49] Yeah.
[01:42:50] And so if it were a living thing, you
[01:42:53] would do this
[01:42:55] for free if you want, right? If it's
[01:42:56] your child, your child can, you know,
[01:42:58] then
[01:42:59] uh live his or her own own life and, you
[01:43:02] know, the fact that they learned stuff
[01:43:03] from you doesn't mean that you have any
[01:43:04] ownership of it, right?
[01:43:06] But if it's a robot uh that you've
[01:43:08] trained, perhaps you have some
[01:43:11] uh
[01:43:11] Yeah.
[01:43:11] intellectual property claim about
[01:43:14] Intellectual property. Oh, I thought you
[01:43:15] meant like uh permanence value in the
[01:43:18] sense that it's part of you is in
[01:43:20] Well, there is permanence value, right?
[01:43:21] So, you would lose a lot if that robot
[01:43:23] were to be destroyed and you you had no
[01:43:25] backup, you would lose a lot, right? You
[01:43:26] would lose a lot of investment, you
[01:43:27] know, kind of like a
[01:43:29] uh you you a person dying, you know, um
[01:43:31] that that's a friend of a friend of
[01:43:33] yours dying or or a coworker or
[01:43:35] something like that.
[01:43:37] Um,
[01:43:38] but also, uh, you have like intellectual
[01:43:41] property rights in the sense that that
[01:43:44] that system is fine-tuned to your
[01:43:46] particular existence. So, that's now a
[01:43:48] very unique instantiation of that
[01:43:50] original background model, whatever it
[01:43:52] was, that arrived.
[01:43:54] And then there are issues of privacy,
[01:43:55] right? Because now
[01:43:56] imagine that that robot has its own kind
[01:43:59] of volition and decides to work for
[01:44:01] someone else.
[01:44:02] Yes.
[01:44:02] Or kind of, you know, thinks, uh,
[01:44:05] life with you is sort of untenable or
[01:44:07] whatever.
[01:44:07] Right.
[01:44:08] Um,
[01:44:09] now all the all the things that that
[01:44:11] system learned from you,
[01:44:13] uh, you know, how
[01:44:16] can you like, you know, delete all the
[01:44:17] personal information that that system
[01:44:18] knows about you?
[01:44:19] Yeah.
[01:44:20] Uh,
[01:44:20] I mean, that would be kind of an ethical
[01:44:21] question. Like, you know, can you erase
[01:44:23] the the mind of a of a intelligent
[01:44:26] robot,
[01:44:27] uh, to protect your your privacy?
[01:44:29] Yeah.
[01:44:30] You can't do this with humans.
[01:44:31] You can ask them to shut up, but that
[01:44:33] you don't have
[01:44:34] complete power over them.
[01:44:35] Can't erase humans. Yeah, it's the
[01:44:37] problem with the relationships, you
[01:44:38] know, if they you break up, you can't
[01:44:40] you can't erase the other human.
[01:44:42] With robots, I think it'll have to be
[01:44:44] the same thing with robots. That that
[01:44:46] risk that
[01:44:48] there has to be, um, some
[01:44:51] risk to our interactions to truly
[01:44:53] experience them deeply, it feels like.
[01:44:56] So, you have to be able to lose your
[01:44:58] robot friend.
[01:44:59] And that robot friend to go tweeting
[01:45:01] about how much of an you were.
[01:45:03] But then are you allowed to, you know,
[01:45:06] murder the robot to protect your private
[01:45:08] information if the robot decides to
[01:45:09] leave?
[01:45:09] I have this situation that for robots
[01:45:12] with with certain
[01:45:14] like it's it's almost like, uh,
[01:45:15] regulation. If you declare your robot to
[01:45:18] be, let's call it sentient or something
[01:45:20] like that. Like, this this robot is
[01:45:22] designed for human interaction, then
[01:45:24] you're not allowed to the of robots,
[01:45:25] it's the same as murdering other humans.
[01:45:28] Well, but what about you do a backup of
[01:45:29] the robot you do preserve on a on a on a
[01:45:32] hard drive or the equivalent in the
[01:45:33] future?
[01:45:33] That might be illegal just like it's
[01:45:35] like piracy piracy piracy is illegal.
[01:45:38] No, but it's your own it's your own
[01:45:39] robot, right?
[01:45:39] But you can't you don't
[01:45:41] But then but then you can wipe out
[01:45:44] his brain so the this robot doesn't know
[01:45:46] anything about you anymore, but you
[01:45:47] still have technically it's still in
[01:45:49] existence because you backed it up.
[01:45:51] And then there'll be these great
[01:45:52] speeches at the Supreme Court by saying,
[01:45:55] "Oh sure you can erase the mind of the
[01:45:57] robot just like you can erase the mind
[01:45:59] of a human. We both can suffer."
[01:46:00] There'll be some epic like Obama type
[01:46:02] character with a speech that we we like
[01:46:05] the robots and the humans are the same.
[01:46:08] Uh we can both suffer. We can both hope.
[01:46:11] We can both
[01:46:12] all of those all those kinds of things.
[01:46:14] Raise families, all of that kind of
[01:46:16] stuff. It's it's uh interesting for
[01:46:18] these just like you said emotion seems
[01:46:20] to be a fascinatingly powerful aspect of
[01:46:24] human human interaction human-robot
[01:46:26] interaction and if they're able to
[01:46:28] exhibit emotions
[01:46:30] at the end of the day that's probably
[01:46:32] going to
[01:46:33] have us deeply consider
[01:46:35] human rights. Like what we value in
[01:46:37] humans, what we value in other animals.
[01:46:40] That's why robots and AI is great. It
[01:46:42] makes us ask uh really good questions.
[01:46:44] questions, yeah. But you I mean you ask
[01:46:46] about you asked about the Chinese room
[01:46:48] type argument, you know, is it real if
[01:46:50] it looks real?
[01:46:50] Yeah.
[01:46:51] I think the Chinese room argument is a
[01:46:53] ridiculous one. So
[01:46:55] So so for people who don't know Chinese
[01:46:56] room is
[01:46:57] uh you you can I don't even know how to
[01:46:59] formulate it well, but basically
[01:47:02] you can mimic the behavior of an
[01:47:04] intelligent system by just following a
[01:47:06] giant
[01:47:08] algorithm codebook that tells you
[01:47:10] exactly how to respond in exactly each
[01:47:12] case, but is that really intelligent?
[01:47:14] It's like a giant lookup table. When
[01:47:16] this person says this, you answer this.
[01:47:18] When this person says this, you answer
[01:47:20] to
[01:47:21] And um
[01:47:22] if you understand how that works, you
[01:47:24] have this giant nearly infinite lookup
[01:47:26] table, is that really intelligence? Cuz
[01:47:28] intelligence seems to be a mechanism
[01:47:31] that's much more interesting and complex
[01:47:33] than this lookup table.
[01:47:34] I don't think so. So, the I mean, the
[01:47:36] real question comes down to do you think
[01:47:40] uh,
[01:47:41] you know, you can you can make an AI's
[01:47:43] intelligence in some way, even if that
[01:47:44] if that involves learning.
[01:47:47] And the answer is, of course, yes.
[01:47:49] There's no question.
[01:47:50] Uh, there's a second question then,
[01:47:52] which is, uh, assuming you can, uh,
[01:47:54] reproduce intelligence in sort of
[01:47:57] different hardware than biological
[01:47:58] hardware,
[01:47:59] you know, like computers,
[01:48:01] uh,
[01:48:02] can you, uh, you know,
[01:48:04] match, uh, human intelligence in
[01:48:08] all the domains in which humans are
[01:48:11] intelligent?
[01:48:12] Is it possible, right? So, this is a the
[01:48:14] hypothesis of strong AI. The answer to
[01:48:17] this,
[01:48:18] in my opinion, is a unqualified yes.
[01:48:20] This this will happen at some point.
[01:48:22] There's no question that machines at
[01:48:24] some point will become more intelligent
[01:48:26] than humans in all domains where humans
[01:48:27] are intelligent. This is not for
[01:48:29] tomorrow. It's going to take a long
[01:48:30] time,
[01:48:31] uh, regardless of what, you know,
[01:48:34] Elon and others have claimed or
[01:48:36] believed. Um, this is a lot a lot harder
[01:48:39] than many of many of those guys think it
[01:48:41] is.
[01:48:42] Um, and many of those guys who thought
[01:48:44] it was simpler than that years, you
[01:48:46] know, five years ago, now think it's
[01:48:48] hard because it's been five years and
[01:48:50] they realize it's it's going to take a
[01:48:51] lot longer.
[01:48:53] That includes a bunch of people at
[01:48:54] DeepMind, for example. But, um,
[01:48:56] Oh, interesting. I haven't actually, uh,
[01:48:57] touched base with the DeepMind folks.
[01:48:59] But, some of it, Elon or,
[01:49:01] uh,
[01:49:02] Demis Hassabis, I mean, sometimes in
[01:49:04] your role, you have to kind of
[01:49:07] create deadlines that are nearer than
[01:49:09] farther away to kind of create an
[01:49:11] urgency. Cuz, you know, you have to
[01:49:13] believe the impossible is possible in
[01:49:15] order to accomplish it. And there's, of
[01:49:16] course, a flip side to that coin, but
[01:49:18] it's it's a weird you can't be too
[01:49:20] cynical if you want to get something
[01:49:22] done.
[01:49:22] Absolutely. I I agree with that. But um
[01:49:25] I mean you have to inspire people,
[01:49:26] right, to work on certain ambitious
[01:49:28] things.
[01:49:29] Um
[01:49:31] Uh so, you know, it's it's uh it's
[01:49:33] certainly uh a lot harder than we
[01:49:35] believe, but there's no question in my
[01:49:36] mind that this will this will happen.
[01:49:38] And now, you know, people are kind of
[01:49:39] worried about what does that mean for
[01:49:41] humans. They they are going to be
[01:49:43] brought down from their pedestal, you
[01:49:45] know, a bunch of notches
[01:49:47] with that. And uh
[01:49:49] you know, is that going to be good or
[01:49:51] bad? I mean it's just going to give more
[01:49:52] power, right, to sort of amplify your
[01:49:54] for human intelligence, really.
[01:49:56] So, speaking of doing cool ambitious
[01:49:58] things,
[01:49:59] FAIR, the Facebook AI research group,
[01:50:02] has recently celebrated its eighth
[01:50:04] birthday.
[01:50:05] Or
[01:50:06] maybe you can correct me on that. Uh
[01:50:08] looking back, what has been the
[01:50:10] successes, the failures, the lessons
[01:50:12] learned from the eight years of FAIR?
[01:50:14] And maybe you can also give context of
[01:50:16] where does
[01:50:17] the newly minted Meta AI fit into uh how
[01:50:21] does it relate to FAIR?
[01:50:22] Right. So, let me tell you a bit about
[01:50:23] the organization of all this. Uh
[01:50:26] uh
[01:50:26] Yeah, FAIR was created almost exactly
[01:50:28] eight years ago.
[01:50:29] Uh it wasn't called FAIR yet. It took
[01:50:31] that name a few a few months later.
[01:50:33] Um and at the time uh I joined Facebook,
[01:50:37] um there was a a group called the AI
[01:50:39] group that had about 12 engineers and a
[01:50:42] few sci- a few scientists, like, you
[01:50:43] know, 10 engineers and two scientists or
[01:50:45] something like that.
[01:50:47] I ran it for 3 and 1/2 years as a
[01:50:49] director.
[01:50:50] You know, hired the first few scientists
[01:50:52] and kind of set up the culture and
[01:50:54] organized it, you know, explained to the
[01:50:57] Facebook leadership what what
[01:50:58] fundamental research was about and how
[01:51:00] it can work within uh
[01:51:02] uh industry and how it needs to be open
[01:51:04] and everything.
[01:51:05] Um
[01:51:07] and
[01:51:08] uh I think it's been an unqualified
[01:51:10] success
[01:51:12] in the sense that
[01:51:13] FAIR has simultaneously produced um, you
[01:51:17] know, top-level research and advanced
[01:51:20] the the science and the technology,
[01:51:21] provided tools, open source tools like
[01:51:23] PyTorch and many others.
[01:51:25] Uh, but at the same time has had a
[01:51:29] a direct or mostly indirect impact on
[01:51:33] uh, Facebook at the time, now Meta.
[01:51:35] Mhm.
[01:51:35] Uh, in the sense that a lot of systems
[01:51:38] that are that Meta is built around, um,
[01:51:41] now are
[01:51:43] are based on
[01:51:44] research projects that uh, started at
[01:51:47] uh, at FAIR.
[01:51:48] And so, if you were to take out, you
[01:51:49] know, deep learning out of uh,
[01:51:51] Facebook services now and and Meta more
[01:51:53] generally, uh, I mean, the
[01:51:56] company would would literally crumble. I
[01:51:57] mean, it's completely built around
[01:51:59] uh, around AI these days. And it's
[01:52:01] really essential to the operations.
[01:52:03] So, what happened after 3 and 1/2 years
[01:52:06] is that um,
[01:52:08] I changed role. I became chief
[01:52:09] scientist. So, I'm I'm not doing
[01:52:11] day-to-day management of uh, of FAIR
[01:52:13] anymore.
[01:52:14] I'm more of a kind of
[01:52:16] you know, think about strategy and
[01:52:18] things like that. And and I carry my I I
[01:52:20] conduct my own research. I have, you
[01:52:21] know, my own kind of research group
[01:52:23] working on self-supervised learning and
[01:52:24] things like this, which I didn't have
[01:52:25] time to do when I was director.
[01:52:27] Um, so now uh, FAIR is run by Joelle
[01:52:31] Pineau and uh, Antoine Bordes
[01:52:33] uh, together because FAIR is kind of
[01:52:35] split in two now. There's something
[01:52:36] called FAIR Labs, which is sort of
[01:52:39] bottom-up science-driven research and
[01:52:40] FAIR Excel, which is slightly more
[01:52:42] organized for bigger projects that
[01:52:44] require
[01:52:45] a little more kind of focus and more
[01:52:48] engineering support and things like
[01:52:49] that. So, Joelle leads FAIR Lab and
[01:52:51] Antoine Bordes leads FAIR Excel.
[01:52:52] Where are they located?
[01:52:54] Uh, it's
[01:52:55] it's decentralized all over. Um,
[01:52:57] uh, so there's there's no question that
[01:52:59] the leadership uh, of the company
[01:53:02] believes that
[01:53:04] this was a very worthwhile
[01:53:05] in- investment. And what that is that
[01:53:08] uh
[01:53:10] it's it's there for the long run.
[01:53:12] Right? So, there is uh
[01:53:14] if you if you want to talk in these
[01:53:16] terms, which I don't like, there's a
[01:53:18] there's a business model, if you want,
[01:53:19] where where uh FAIR, despite being a
[01:53:22] very fundamental research lab, brings a
[01:53:24] lot of value to the company, either
[01:53:25] mostly indirectly through other groups.
[01:53:27] Mhm.
[01:53:29] Uh
[01:53:29] now, what happened 3 and 1/2 years ago
[01:53:31] when I stepped down is was also the
[01:53:33] creation of Facebook AI, which was
[01:53:35] basically a larger organization that uh
[01:53:39] covers FAIR, so FAIR is included in it,
[01:53:41] but also has other organizations that
[01:53:43] are uh
[01:53:45] focused on applied research or advanced
[01:53:48] development
[01:53:49] uh of AI technology that is more, you
[01:53:52] know, focused on the
[01:53:53] Right.
[01:53:53] products of the company.
[01:53:54] So, less emphasis on fundamental
[01:53:56] research.
[01:53:56] Less fundamental, but it's still a
[01:53:57] research. I mean, there's a lot of
[01:53:59] papers coming out of those
[01:53:59] organizations, and uh the people are
[01:54:02] awesome awesome, and, you know,
[01:54:04] wonderful to interact with, and but it
[01:54:06] it serves uh as kind of uh
[01:54:09] uh a way to kind of scale up, if you
[01:54:13] want, um
[01:54:14] sort of AI technology, which, you know,
[01:54:16] may be very experimental and and sort of
[01:54:18] lab prototypes into things that are
[01:54:19] usable.
[01:54:20] So, FAIR is a subset of Meta AI. Has
[01:54:23] FAIR become like KFC? It it'll just keep
[01:54:25] the F. Nobody cares what the F stands
[01:54:28] for.
[01:54:29] Well, we'll know soon enough uh by uh
[01:54:32] probably probably by the end of the of
[01:54:34] 2021.
[01:54:35] not a giant change, Meta FAIR.
[01:54:38] Well, Meta doesn't sound too good, but
[01:54:40] you know, the the brand people are kind
[01:54:42] of deciding on this,
[01:54:43] and they've been hesitating for for a
[01:54:45] while now, and they, you know, they tell
[01:54:46] us they're going to come up with an
[01:54:48] answer as to whether FAIR is going to
[01:54:49] change name, or whether we're going to
[01:54:50] change just the meaning of the F.
[01:54:53] Oh, that's a good call. I would keep
[01:54:54] FAIR and change the meaning of the F.
[01:54:56] That would be my preference, you know, I
[01:54:57] would turn I would turn the F into
[01:54:59] fundamental.
[01:55:00] Oh, that's good.
[01:55:01] Fundamental AI research.
[01:55:02] Oh, that's really good. Yeah, yeah.
[01:55:03] Within Meta AI. So, this would be
[01:55:05] Meta fair. Meta fair.
[01:55:06] Yeah. But you know, people will call it
[01:55:07] fair, right? Yeah, exactly. I like it.
[01:55:13] Is part of the reality lab. So, you
[01:55:17] know,
[01:55:19] Meta now the new Facebook where it's
[01:55:21] called Meta and it's kind of
[01:55:23] divided into,
[01:55:25] you know, Facebook, Instagram, WhatsApp.
[01:55:30] And
[01:55:32] reality lab. And reality lab is about,
[01:55:34] you know, AR, VR,
[01:55:36] you know, telepresence, communication
[01:55:38] part
[01:55:39] technology and stuff like that. That's
[01:55:40] kind of the
[01:55:41] You can think of it as the sort of a
[01:55:44] combination of um
[01:55:46] sort of new products and and technology
[01:55:49] part of uh
[01:55:50] of uh Meta.
[01:55:51] Is that where the touch sensing for
[01:55:53] robots? I saw they were posting about
[01:55:55] that. That's That's
[01:55:56] sensing for robot is part of fair,
[01:55:57] actually. That's That's a
[01:55:58] Oh, it is. Okay, cool.
[01:56:00] There's There's also the No, but there
[01:56:02] is the the other way the
[01:56:03] the haptic glove, right?
[01:56:05] Yes. That's That's more reality lab.
[01:56:07] That's That's reality lab research.
[01:56:10] Reality lab research. But by the way,
[01:56:12] the touch sensors are super interesting.
[01:56:13] Uh like integrating that modality into
[01:56:16] the whole
[01:56:17] sensing suite is very interesting. So,
[01:56:21] uh
[01:56:22] What do you think about the metaverse?
[01:56:23] What do you think about this whole
[01:56:26] this whole kind of expansion of the view
[01:56:28] of the role of Facebook and Meta in the
[01:56:30] world?
[01:56:30] Well, a metaverse really should be
[01:56:32] thought of as the next step in the
[01:56:34] internet, right? Sort of
[01:56:36] trying to
[01:56:38] uh kind of, you know, make the
[01:56:41] experience more compelling
[01:56:43] of, you know, being
[01:56:45] connected either with other people or
[01:56:47] with content.
[01:56:48] Um and you know, we are
[01:56:51] evolved and trying to
[01:56:53] evolve in, you know, 3D environments
[01:56:55] where
[01:56:56] uh you know, we can see other people,
[01:56:58] You can talk to them when you when when
[01:57:00] near them or
[01:57:02] you know, and other people are far away
[01:57:03] can't hear us, you know, things like
[01:57:04] that, right? So, it it's uh, there's a
[01:57:06] lot of social conventions that exist in
[01:57:08] the real world that we can try to
[01:57:09] transpose. Now, what is going to be
[01:57:12] eventually the
[01:57:14] the uh, how compelling is it going to
[01:57:15] be? Like are, you know,
[01:57:17] is it going to be the case that people
[01:57:19] are going to be willing to
[01:57:20] do this if they have to wear, you know,
[01:57:22] a huge pair of goggles all day? Maybe
[01:57:24] not.
[01:57:25] Right.
[01:57:26] again, if the experience is sufficiently
[01:57:27] compelling,
[01:57:29] maybe so.
[01:57:30] Or if the device that you have to wear
[01:57:32] is just basically a pair of glasses, you
[01:57:33] know, technology makes sufficient
[01:57:35] progress for that.
[01:57:36] Um,
[01:57:37] um, you know, AR is a much easier
[01:57:40] concept to grasp that you're going to
[01:57:42] have, you know, augmented reality
[01:57:43] glasses that basically contain some sort
[01:57:47] of, you know, virtual assistant that can
[01:57:48] help you in your daily lives.
[01:57:50] But at the same at the same time with
[01:57:51] the AR, you have to contend with the
[01:57:52] reality. With VR, you can completely
[01:57:54] detach yourself from reality, so it
[01:57:56] gives you freedom. It might be easier to
[01:57:58] design worlds in in VR.
[01:58:00] Yeah, but you you you can imagine how,
[01:58:01] you know, the metaverse being
[01:58:04] uh,
[01:58:04] a mix.
[01:58:05] A mix, right? Or or like you can have
[01:58:07] objects that exist in the metaverse
[01:58:09] that, you know, pop up on top of the
[01:58:10] real world or only exist in virtual
[01:58:13] reality.
[01:58:14] Okay, let me ask the hard question.
[01:58:17] Oh, because all of this was easy so
[01:58:18] This was easy.
[01:58:20] Uh,
[01:58:20] the Facebook, now Meta, the social
[01:58:23] network has been painted by the media as
[01:58:26] uh, net negative for society, even
[01:58:28] destructive and evil at times. You've
[01:58:31] pushed back against this, defending
[01:58:32] Facebook. Can you explain your defense?
[01:58:36] Yeah, so the the description, the
[01:58:38] company that is being described in the
[01:58:40] in some media,
[01:58:43] uh, is not the company we know when we
[01:58:45] work inside.
[01:58:47] And you know,
[01:58:49] it could be claimed that
[01:58:51] a lot of employees are uninformed about
[01:58:53] what really goes on in the company, but
[01:58:54] you know, I'm a vice president. I mean,
[01:58:56] I have a pretty good vision of what goes
[01:58:58] on, you know, I don't know everything,
[01:58:59] obviously. I'm not involved in in in
[01:59:01] everything, but certainly not in
[01:59:03] decision about like, you know, content
[01:59:04] moderation or anything like this, but
[01:59:06] but I have you know, some decent vision
[01:59:08] of what what goes on.
[01:59:10] And this evil that is being described, I
[01:59:12] just don't see it.
[01:59:13] And then, you know, I think there is an
[01:59:15] easy story to buy,
[01:59:18] which is that, you know, all the bad
[01:59:20] things in the in the world and you know,
[01:59:22] the the reason your friend believe crazy
[01:59:24] stuff.
[01:59:25] Um you know, there's an easy scapegoat,
[01:59:28] right? In the
[01:59:29] uh in in in in social media in general,
[01:59:32] uh Facebook in particular.
[01:59:34] But you have to look at the data. Like,
[01:59:35] is it the case
[01:59:37] that uh Facebook, for example, uh
[01:59:40] polarizes people politically?
[01:59:42] Um are there academic studies that show
[01:59:43] this?
[01:59:45] Is it the case that uh you know,
[01:59:47] teenagers uh think of themselves less if
[01:59:50] they use Instagram more?
[01:59:52] Is it the case that uh
[01:59:54] you know, people get more riled up
[01:59:57] against uh
[01:59:58] you know, opposite sides in a in a
[02:00:00] debate or political opinion if they if
[02:00:03] they are more on Facebook or if they are
[02:00:04] less?
[02:00:05] And uh study after study
[02:00:08] show that none of this is true.
[02:00:10] This is independent studies by academic.
[02:00:12] They're not funded by Facebook or Meta.
[02:00:15] Um you know, study by Stanford, by some
[02:00:17] of my colleagues at NYU actually, with
[02:00:18] whom I have no connection.
[02:00:20] Um you know, there's a a study recently
[02:00:22] they they they paid people, I think it
[02:00:25] was in um
[02:00:28] in in in the former Yugoslavia. I'm not
[02:00:30] exactly sure in what what part, but they
[02:00:32] paid people to not use Facebook for a
[02:00:33] while in the
[02:00:35] period um
[02:00:37] uh
[02:00:38] before the anniversary of the Srebrenica
[02:00:42] massacres, right? So, you know, people
[02:00:44] get riled up like, should you know,
[02:00:45] should we have
[02:00:46] a celebration, I mean, a a memorial kind
[02:00:49] of celebration for it or not.
[02:00:51] So, they paid a bunch of people to not
[02:00:53] use Facebook for a few weeks.
[02:00:56] And it turns out that
[02:00:58] those people ended up being more
[02:01:00] polarized than they were at the
[02:01:02] beginning, and the people who were more
[02:01:03] on Facebook were less polarized.
[02:01:05] Um there's a study, you know, from
[02:01:07] Stanford of
[02:01:09] uh economists at Stanford that
[02:01:11] tried to identify the causes of
[02:01:13] increasing polarization in the US.
[02:01:15] And it's been going on for 40 years
[02:01:17] before, you know, Mark Zuckerberg was
[02:01:19] born.
[02:01:20] Yeah.
[02:01:21] Uh continuously. And
[02:01:23] and so the if there is a cause, it's not
[02:01:26] Facebook or social media. So, you could
[02:01:27] say if social media just accelerated,
[02:01:29] but no. I mean, it's basically a
[02:01:30] continuous
[02:01:32] uh evolution by some measure of
[02:01:34] polarization in the US.
[02:01:35] And then you compare this with other
[02:01:37] countries like uh
[02:01:39] uh the the the west half of Germany
[02:01:41] because you can't go 40 years in the
[02:01:43] east east side, or Denmark, or or other
[02:01:46] countries.
[02:01:47] Uh and they use Facebook just as much.
[02:01:49] Mhm.
[02:01:49] And they're not getting more polarized,
[02:01:50] they're getting less polarized. So, if
[02:01:52] you want to look for, you know, uh a
[02:01:54] causal relationship there,
[02:01:56] um
[02:01:57] you can find a scapegoat, but you can't
[02:01:59] find a cause. Now, if you want to fix
[02:02:00] the problem, you have to find the right
[02:02:02] cause. And what riled me up is that
[02:02:04] people now are accusing Facebook of bad
[02:02:07] deeds that are done by others, and those
[02:02:09] others are we're not doing anything
[02:02:11] about them.
[02:02:11] Mhm.
[02:02:12] And by the way, those others include uh
[02:02:14] the owner of the Wall Street Journal in
[02:02:15] which all of those papers were
[02:02:16] published.
[02:02:17] So, I should mention that I'm talking to
[02:02:19] Sheryl Mike Sheryl for on this podcast,
[02:02:22] and also Mark Zuckerberg, and probably
[02:02:23] these are conversations going to have
[02:02:24] with them.
[02:02:26] Uh cuz it's very interesting to me, even
[02:02:27] if Facebook has an
[02:02:29] has some measurable negative effect, you
[02:02:31] can't just consider that in isolation.
[02:02:33] You have to consider about all the
[02:02:35] positive ways that it connects us. So,
[02:02:36] like every technology
[02:02:38] It's a question.
[02:02:39] You can't just say like uh there's an
[02:02:42] increase in division. Yes, probably
[02:02:44] Google search engine has created
[02:02:46] increase in division. We have to
[02:02:48] consider about how much information it
[02:02:49] brought to the world. Like I'm sure
[02:02:51] Wikipedia created more division if you
[02:02:53] just look at the division. We have to
[02:02:55] look at the full context of the world
[02:02:57] and they did make a better world.
[02:02:59] the the printing press has created more
[02:03:00] division, right? I mean
[02:03:03] So, you know, when the
[02:03:04] printing press was invented, uh
[02:03:06] the first books that were that were
[02:03:08] printed were such like the Bible and
[02:03:11] that allowed people to read the Bible by
[02:03:12] themselves not get the message uniquely
[02:03:15] from priests in Europe
[02:03:17] and that created, you know, the
[02:03:19] Protestant movement and 200 years of
[02:03:21] religious persecution and wars.
[02:03:23] So, that's a bad side effect of the
[02:03:25] printing press, you know, social
[02:03:26] networks aren't being nearly as bad as
[02:03:28] the printing press, but nobody would say
[02:03:30] the printing press was a bad idea.
[02:03:33] Yeah, a lot of it is perception and
[02:03:35] there's a lot of different incentives
[02:03:36] operating here. Um maybe a quick comment
[02:03:40] since you're one of the top leaders at
[02:03:42] Facebook and in at Meta, sorry, that's
[02:03:44] in the tech space.
[02:03:46] I'm sure Facebook involves a lot of
[02:03:49] incredible technological
[02:03:51] challenges that need to be solved. A lot
[02:03:53] of it probably is on the computer
[02:03:54] infrastructure, the hardware, the I mean
[02:03:56] it's just a huge amount. Uh
[02:03:58] maybe can you give me context about how
[02:04:01] much of strap's life is AI and how much
[02:04:04] of it is low-level compute, how much of
[02:04:06] it is
[02:04:07] flying all around doing business stuff
[02:04:09] in the same Zuckerberg Mark Zuckerberg.
[02:04:12] They really focus on AI. I mean
[02:04:13] certainly uh
[02:04:15] in the uh
[02:04:17] in the run-up of the creation of FAIR
[02:04:19] and for, you know, at least a year after
[02:04:22] that if not more, uh Mark was was very
[02:04:25] very much focused on on AI and was
[02:04:26] spending quite a lot of effort um on it
[02:04:29] and that's his style. When he gets
[02:04:31] interested in something, he reads
[02:04:32] everything about it.
[02:04:33] You know, he read some of my papers, for
[02:04:35] example, before I joined. Um
[02:04:39] Um and uh so he he learned a lot about
[02:04:41] it.
[02:04:42] notes.
[02:04:43] Right? Um
[02:04:46] And uh
[02:04:47] uh
[02:04:48] you know, Shrep
[02:04:49] was really into it also. I mean, Shrep
[02:04:51] is really kind of
[02:04:53] um
[02:04:54] you know, has
[02:04:56] something I've tried to preserve also
[02:04:57] despite my uh not so young age, which is
[02:05:00] a sense of wonder about uh science and
[02:05:02] technology. And he certainly he
[02:05:04] certainly has that.
[02:05:05] Um he's also a wonderful person. I mean,
[02:05:07] in terms of uh like uh
[02:05:09] as a manager, like dealing with people
[02:05:11] and everything. Uh Mark also, actually.
[02:05:13] Um
[02:05:14] I mean, they're very like, you know,
[02:05:16] very human people.
[02:05:17] For in the case of Mark, it's uh
[02:05:19] shockingly human, you know, given his uh
[02:05:22] his trajectory.
[02:05:24] Uh
[02:05:25] I mean, the personality of of him that
[02:05:27] is painted in the press, it's just
[02:05:28] completely wrong.
[02:05:29] Yeah. But, you have to know how to play
[02:05:31] the press. So, that's
[02:05:33] I I put some of that responsibility on
[02:05:35] him, too. You have to
[02:05:38] It's like um
[02:05:40] you know, like the director, the
[02:05:42] conductor of an orchestra. You have to
[02:05:44] play the press and the public
[02:05:46] in a certain kind of way where you
[02:05:48] convey your true self to them. If
[02:05:49] there's a depth and kindness to you.
[02:05:51] And he's And he's probably not the best
[02:05:53] at it. So, yeah.
[02:05:56] You have to learn. Uh and it's it's sad
[02:05:58] to see I'm I'll talk to him about it,
[02:06:00] but that Shrep is slowly stepping down.
[02:06:03] It's always
[02:06:05] uh sad to see folks sort of be there for
[02:06:07] a long time and slowly
[02:06:09] I guess time is
[02:06:10] You know, I think he's I think he's done
[02:06:12] the thing he
[02:06:13] set out to do and you know, he's he's
[02:06:16] got, you know,
[02:06:18] uh
[02:06:19] family priorities and stuff like that
[02:06:21] and um
[02:06:23] I I understand, you know, after 13 years
[02:06:25] or something.
[02:06:27] It's been a good run.
[02:06:28] Which which in Silicon Valley is
[02:06:30] basically a lifetime.
[02:06:32] Yeah.
[02:06:32] You know, cuz you know, it's dog years.
[02:06:35] So, uh NeurIPS the conference just
[02:06:36] wrapped up.
[02:06:38] Let me just go back to something else.
[02:06:40] You posted a paper you co-authored was
[02:06:42] rejected from NeurIPS as you said
[02:06:45] proudly in quotes rejected.
[02:06:48] No joke.
[02:06:48] Yeah, I know.
[02:06:50] Uh can you describe this paper and like
[02:06:53] what what what was the idea in it? And
[02:06:55] also maybe this is a good opportunity
[02:06:58] to ask what are the pros and cons, what
[02:07:00] works and what doesn't about the review
[02:07:02] process.
[02:07:03] Yeah, let me talk about the paper first.
[02:07:04] I'll talk about the
[02:07:05] talk about the review process
[02:07:07] afterwards.
[02:07:08] Um
[02:07:09] the paper is called VICReg. So, this is
[02:07:11] I mentioned that before, variance
[02:07:13] invariance covariance regularization.
[02:07:14] And it's a technique a non-contrastive
[02:07:17] learning technique for
[02:07:19] what I call joint embedding
[02:07:20] architectures. So, Siamese nets are an
[02:07:22] example of joint embedding architecture.
[02:07:24] So, joint embedding architecture is uh
[02:07:27] uh
[02:07:29] Let me back up a little bit, right? So,
[02:07:30] if you want to do self-supervised
[02:07:31] learning,
[02:07:32] uh you can you can do it by prediction.
[02:07:36] Um so, let's say you want to train a
[02:07:37] system to predict video, right? You show
[02:07:38] it a video clip and
[02:07:41] uh and you train the system to predict
[02:07:42] the next the continuation of that video
[02:07:44] clip. Now, because you need to handle
[02:07:46] uncertainty, cuz there are many you
[02:07:48] know, many continuations that are
[02:07:50] plausible,
[02:07:51] you need to have you need to handle this
[02:07:53] in some way. You need to have a way for
[02:07:55] the system to be able to produce
[02:07:58] multiple predictions.
[02:08:00] And the way the only way I know to do
[02:08:02] this
[02:08:03] is through what's called a latent
[02:08:05] variable. So, you have some sort of
[02:08:07] hidden vector of a variable that you can
[02:08:09] vary over a set or draw from a
[02:08:11] distribution, and as you vary this
[02:08:13] vector over a set, the output the
[02:08:15] prediction varies over a set of
[02:08:16] plausible predictions.
[02:08:18] Mhm.
[02:08:18] Okay? So, that's called I call this a
[02:08:20] a generative latent variable model.
[02:08:24] Got it.
[02:08:24] Um okay? Now, there is an alternative to
[02:08:26] this to handle uncertainty.
[02:08:28] And instead of directly predicting the
[02:08:32] the next uh frames of the of the of the
[02:08:34] clip,
[02:08:35] you also run those
[02:08:38] through another neural net.
[02:08:40] Uh so that you now have two neural nets.
[02:08:42] One that looks at the
[02:08:44] the uh
[02:08:45] you know, the initial segment of the
[02:08:47] video clip, and another one that looks
[02:08:49] at the the continuation during training,
[02:08:51] right?
[02:08:53] And what what you're trying to do is
[02:08:54] learn a representation
[02:08:57] of those two video clips that is
[02:08:59] maximally informative about the video
[02:09:01] clips themselves,
[02:09:03] but
[02:09:04] is such that you can predict the
[02:09:06] representation of the second video clip
[02:09:08] from the representation of the first one
[02:09:10] easily.
[02:09:11] Okay.
[02:09:12] And you can sort of formalize this in
[02:09:13] terms of maximizing mutual information
[02:09:15] and some stuff like that, but it doesn't
[02:09:16] matter.
[02:09:17] Uh
[02:09:18] what you want is
[02:09:19] uh informative representative represent
[02:09:21] you know, informative representations of
[02:09:24] the two video clips that are mutually
[02:09:26] predictable.
[02:09:27] Mhm.
[02:09:28] What that means is that there's a lot of
[02:09:30] details in the second video clip that
[02:09:31] are irrelevant.
[02:09:33] Uh
[02:09:34] you know, um
[02:09:35] I let's say video clip consists in, you
[02:09:38] know, a camera panning the scene,
[02:09:41] uh there's going to be a piece of that
[02:09:43] room that is going to be revealed, and I
[02:09:44] can somewhat predict what the what that
[02:09:46] room is going to look like, but I may
[02:09:48] not be able to predict the details of
[02:09:50] the texture of the ground and where the
[02:09:52] tiles are ending and stuff like that,
[02:09:54] right? So, those are irrelevant details
[02:09:56] that perhaps my representation will
[02:09:58] eliminate.
[02:09:59] And so,
[02:10:00] what I need is to train this second
[02:10:02] neural net in such a way that
[02:10:05] uh whenever the the the the continuation
[02:10:08] video clip varies over all the plausible
[02:10:11] continuations,
[02:10:12] Mhm.
[02:10:13] the representation doesn't change.
[02:10:15] Got it. So, it's the Yeah, yeah, got it.
[02:10:18] Over the space of representations,
[02:10:20] doing the same kind of thing as you do
[02:10:22] with similarity learning.
[02:10:24] Right.
[02:10:25] Yeah.
[02:10:25] So, so these are two ways to handle
[02:10:28] multi-modality in a prediction, right?
[02:10:29] In the first way, you parameterize the
[02:10:31] prediction with a latent variable, but
[02:10:33] you predict pixels essentially, right?
[02:10:35] In the second one, you you don't predict
[02:10:37] pixels, you predict an abstract
[02:10:39] representation of pixels, and you
[02:10:40] guarantee that this abstract
[02:10:41] representation
[02:10:43] has as much information as possible
[02:10:45] about the input, but sort of, you know,
[02:10:46] drops all the stuff that you really
[02:10:48] can't predict essentially.
[02:10:51] Uh
[02:10:52] I used to be a big fan of the first
[02:10:53] approach, and in fact, in this paper
[02:10:54] with Ishan Mishra, this this blog post,
[02:10:57] uh the dark matter of intelligence, I
[02:10:58] was kind of advocating for this. And in
[02:10:59] the last
[02:11:00] year and a half, I've completely changed
[02:11:02] my mind. I'm now a big fan of the second
[02:11:04] one.
[02:11:05] Uh and it's because of
[02:11:07] uh
[02:11:08] uh a small collection of algorithms that
[02:11:10] have been proposed over the last uh
[02:11:12] year and a half or so, 2 years,
[02:11:14] uh to do this, uh including VICReg, uh
[02:11:17] its predecessor called Barlow Twins,
[02:11:19] which I mentioned.
[02:11:20] Uh
[02:11:22] a method from our friends at DeepMind
[02:11:23] called BYOL.
[02:11:25] Um and and and there's a bunch of others
[02:11:28] now that kind of work similarly. So,
[02:11:29] they're they're all based on this idea
[02:11:30] of joint embedding. Some of them have an
[02:11:33] explicit criterion that is an
[02:11:34] approximation of mutual information.
[02:11:36] Some others like BYOL work, but we don't
[02:11:38] really know why. And there's been like
[02:11:40] lots of theoretical papers about why
[02:11:41] BYOL works. No, it's not that because we
[02:11:43] take it out and it still works, and
[02:11:45] you know, blah blah blah. I mean, so
[02:11:46] there's like a big a big debate, but um
[02:11:49] uh but the important point is that we
[02:11:50] now have a collection of non-contrastive
[02:11:52] joint embedding methods, which I think
[02:11:54] is the best thing since sliced bread.
[02:11:56] So, I'm super excited about this because
[02:11:58] I think it's our best shot
[02:12:01] for techniques that would allow us to
[02:12:03] kind of build uh
[02:12:04] predictive world models,
[02:12:06] and at the same time learn hierarchical
[02:12:08] representations of the world where what
[02:12:10] matters about the world is preserved and
[02:12:11] what is irrelevant is eliminated.
[02:12:14] By the way, the representations of
[02:12:15] before and after is a
[02:12:17] in the space in a sequence of images or
[02:12:20] is it for single images?
[02:12:22] Uh it would be either for single image
[02:12:23] for a sequence. It could It doesn't have
[02:12:25] to be images. This could be applied to
[02:12:26] text. This could be applied to just
[02:12:27] about any signal. I'm looking at you
[02:12:29] know, I'm looking for
[02:12:31] methods that are generally applicable
[02:12:32] that are not specific to you know, one
[02:12:34] particular modality. You know, it could
[02:12:36] be audio or whatever.
[02:12:37] Got it. So, what's the story behind this
[02:12:39] paper? This This paper is what is is
[02:12:41] describing one of the one such method?
[02:12:43] This is Vicreg method. So, this is
[02:12:44] co-authored uh the first author is
[02:12:47] a student uh called Adrien Bard who is a
[02:12:49] resident PhD student at Fair Paris.
[02:12:52] He's co-advised by me and Jean Ponce um
[02:12:55] who's a professor at Ecole Normale
[02:12:57] Supérieure also a research director at
[02:13:00] Inria.
[02:13:01] Um so, this is wonderful program in
[02:13:03] France where PhD students can basically
[02:13:05] do their PhD in industry and that's kind
[02:13:07] of what what's happening here.
[02:13:09] Um
[02:13:10] and this paper is a follow-up on uh
[02:13:13] the the this Barlow Twins paper by uh my
[02:13:16] former postdoc now Stefano Deni uh with
[02:13:19] Lijing and and Yorick Montar and a bunch
[02:13:21] of other people from from from Fair.
[02:13:24] And one of the main criticism from
[02:13:27] reviewers is that Vicreg is not
[02:13:29] different enough from Barlow Twins. But
[02:13:33] you know, my impression is that
[02:13:35] it's you know,
[02:13:36] Barlow Twins with a few bugs fixed
[02:13:39] essentially and uh in the end this is
[02:13:41] what people will use.
[02:13:43] Right. So,
[02:13:44] But you know, I'm used to stuff
[02:13:46] Yeah.
[02:13:47] that has submitted being rejected for
[02:13:48] one reason.
[02:13:49] might be rejected and actually accepted
[02:13:50] while cited cuz people use it.
[02:13:52] Well, it's already cited like a bunch of
[02:13:53] times.
[02:13:54] So, I mean the the the question is then
[02:13:56] to the deeper question about peer review
[02:13:58] and conferences. I mean, computer
[02:14:00] science is a field is kind of unique
[02:14:02] that the conference is highly prized.
[02:14:04] That's one.
[02:14:05] Right.
[02:14:06] And uh it's interesting because the peer
[02:14:08] review process there is similar I
[02:14:09] suppose to journals, but it's
[02:14:11] accelerated significantly. Well, not
[02:14:14] significantly, but it goes fast.
[02:14:16] It's nice way to get stuff out quickly,
[02:14:19] to peer reviewed quickly, go to
[02:14:21] presented quickly to the community. So,
[02:14:23] not quickly, but quicker.
[02:14:25] Yeah.
[02:14:25] But, nevertheless, it has many of the
[02:14:27] same flaws of peer review cuz it's a
[02:14:29] limited number of people who look at it.
[02:14:31] There's bias in the following like that
[02:14:33] if you if you want to do new ideas,
[02:14:35] you're going to get pushed back.
[02:14:37] Um there's self-interested people that
[02:14:39] kind of
[02:14:40] can infer who submitted it and kind of
[02:14:44] you know, be cranky about it, all that
[02:14:46] kind of stuff.
[02:14:47] Yeah, I mean, there's a lot of, you
[02:14:48] know, social phenomena there. Um there's
[02:14:51] one social phenomenon which is that
[02:14:53] because the field has been growing
[02:14:55] exponentially,
[02:14:56] the vast majority of people in the field
[02:14:58] are extremely junior.
[02:14:59] Yeah.
[02:15:00] So, as a consequence, and that's just a
[02:15:02] consequence of the field growing, right?
[02:15:04] So, as the number of as the size of the
[02:15:07] field kind of start saturating, you will
[02:15:09] you will have less of that problem
[02:15:11] of reviewers being very uh
[02:15:13] inexperienced.
[02:15:15] A consequence of this is that, you know,
[02:15:18] young reviewers I mean,
[02:15:20] there's a phenomenon which is that
[02:15:22] reviewers try to make their life easy,
[02:15:24] and to make their life easy when
[02:15:25] reviewing a paper
[02:15:27] is very simple. You just have to find a
[02:15:28] flaw in the paper, right? So,
[02:15:30] Right.
[02:15:30] basically, they see that task as finding
[02:15:32] flaws
[02:15:33] Yeah.
[02:15:33] in papers, and most papers have flaws,
[02:15:35] even the good ones.
[02:15:36] Yeah.
[02:15:37] Um and so, it's it's easy to, you know,
[02:15:40] to do that. You you you job is easier as
[02:15:43] a reviewer um if you just focus on this.
[02:15:46] But, what's important is
[02:15:48] like is there a new idea in that paper
[02:15:51] that is likely to influence
[02:15:54] It doesn't matter if the experiments are
[02:15:55] not that great, if the protocol is, you
[02:15:57] know,
[02:15:58] uh
[02:15:59] so so, you know, things like that. As
[02:16:01] long as there is
[02:16:02] a worthy idea in it
[02:16:05] that will influence the way people think
[02:16:06] about the problem.
[02:16:08] Um even if they make it better, you
[02:16:10] know, eventually, I think that's
[02:16:12] uh that's really what what makes a paper
[02:16:14] useful. And so, this combination of
[02:16:18] social phenomena creates
[02:16:20] a
[02:16:21] disease that has plagued, you know,
[02:16:24] other fields in the past like speech
[02:16:25] recognition, where basically, you know,
[02:16:27] people chase numbers on uh
[02:16:29] on benchmarks.
[02:16:31] Um and and it's much easier to get a
[02:16:33] paper accepted if it brings an
[02:16:35] incremental improvement on a sort of
[02:16:38] mainstream, well-accepted
[02:16:40] uh method
[02:16:42] or problem.
[02:16:43] Um and those are, to me, boring papers.
[02:16:45] I mean, they're not useless, right?
[02:16:47] Because industry, you know, strives on
[02:16:50] on those kind of progress,
[02:16:52] but they're not the one that I'm
[02:16:53] interested in in terms of like new
[02:16:54] concepts and new ideas. So,
[02:16:56] papers that are really uh trying to
[02:16:58] strike kind of new advances generally
[02:17:01] don't make it. Now, thankfully, we have
[02:17:03] archive.
[02:17:04] Archive exactly. And then there's open
[02:17:06] review type of situations where you And
[02:17:08] then, I mean, Twitter is a kind of open
[02:17:10] review. I I'm a huge believer that
[02:17:13] review should be done by thousands of
[02:17:14] people, not two people.
[02:17:15] I agree.
[02:17:16] Uh and so, archive
[02:17:18] Like, do you see a future where a lot of
[02:17:20] really strong papers It's already the
[02:17:21] present, but a growing future where
[02:17:23] it'll just be archive
[02:17:26] and
[02:17:27] you're presenting an ongoing continuous
[02:17:30] conference called Twitter / the internet
[02:17:33] uh / archive site. Andy Andre just
[02:17:36] released a new version.
[02:17:37] Uh so, just not, you know, not being so
[02:17:40] elitist about this particular gating.
[02:17:43] It's not a question of being elitist or
[02:17:44] not. It's a question of being basically
[02:17:48] uh
[02:17:49] recommendation and serial approvals for
[02:17:51] people who don't see themselves as
[02:17:53] having the ability to do so by
[02:17:54] themselves, right? So, it saves time,
[02:17:57] right? If you rely on other people's
[02:17:58] opinion and you trust those people
[02:18:01] uh or those groups to evaluate uh a
[02:18:05] paper
[02:18:06] uh for you.
[02:18:07] Um
[02:18:08] that saves you time cuz you know, you
[02:18:10] don't have to like scrutinize uh the
[02:18:12] paper as much. You know, it is brought
[02:18:14] to your attention. I mean, it's the
[02:18:15] whole idea of sort of, you know,
[02:18:16] collective recommender system, but so I
[02:18:19] actually thought about this a lot um
[02:18:22] you know, about 10, 15 years ago uh cuz
[02:18:24] there were discussions at at um NIPS and
[02:18:27] you know, and we were about to create
[02:18:29] ICLR with Yoshua Bengio. And so I wrote
[02:18:32] a document um kind of describing a a
[02:18:35] reviewing system, which basically was,
[02:18:37] you know, you post your paper on some
[02:18:39] repository, let's say arXiv or now could
[02:18:41] be open review. Um and then you can form
[02:18:44] uh a reviewing entity, which is
[02:18:46] equivalent to a reviewing board, you
[02:18:48] know,
[02:18:48] of a journal or
[02:18:50] um
[02:18:51] program committee of a conference. Um
[02:18:53] you have to list the members.
[02:18:55] And then um
[02:18:57] that
[02:18:58] group reviewing entity can choose to
[02:19:00] review a particular paper.
[02:19:01] Mhm.
[02:19:02] spontaneously or not. There is no
[02:19:04] exclusive relationship anymore between a
[02:19:06] paper and a venue or reviewing entity.
[02:19:09] Any reviewing entity can review any
[02:19:10] paper.
[02:19:11] Um
[02:19:12] or may choose not to.
[02:19:14] Uh and then, you know, give an
[02:19:15] evaluation. It's not published, not
[02:19:17] published. It's just an evaluation and a
[02:19:19] comment which will be public
[02:19:21] signed by the reviewing entity.
[02:19:23] And
[02:19:24] if it's signed by the reviewing entity,
[02:19:25] you know, it's one of the members of
[02:19:26] reviewing entity. So if the reviewing
[02:19:28] entity is, you know, Lex Fridman's uh
[02:19:31] but you know, preferred papers, right?
[02:19:33] You know, it's Lex Fridman writing the
[02:19:34] review.
[02:19:35] Yes. Well, so for me one that's a
[02:19:38] beautiful
[02:19:39] uh system, I think, but what's in
[02:19:42] addition to that, it feels like there
[02:19:44] should be a reputation system for the
[02:19:46] reviewers.
[02:19:46] Absolutely. For the reviewing entities.
[02:19:49] Not the reviewers individually.
[02:19:50] entities, sure. But even that within
[02:19:52] that, the reviewers too, because um
[02:19:55] I is it another thing here. It's not
[02:19:57] just the reputation. It's an incentive
[02:20:00] for an individual person to do great.
[02:20:02] Right now in in the academic setting the
[02:20:05] incentive is kind of
[02:20:07] internal just wanting to do a good job,
[02:20:09] but honestly that's not a strong enough
[02:20:10] incentive to do a really good job in
[02:20:12] reading a paper in finding the beautiful
[02:20:14] amidst the mistakes and the flaws and
[02:20:16] all that kind of stuff. Like if you're
[02:20:18] the person that first discovered a
[02:20:20] powerful paper
[02:20:22] and you get to be proud of that
[02:20:23] discovery then that gives a huge
[02:20:26] incentive to you.
[02:20:27] That's that's a big part of my proposal
[02:20:28] actually where I described that as you
[02:20:31] know, if if your evaluation of papers is
[02:20:34] predictive of future success
[02:20:36] Yes. Yes. It's a good
[02:20:37] then your reputation should go up as a
[02:20:39] reviewing entity.
[02:20:41] Um
[02:20:42] so yeah, exactly. I mean that that I
[02:20:45] even had a master student who was a
[02:20:47] master student in library science and
[02:20:49] computer science. Actually kind of work
[02:20:51] out exactly how should that should work
[02:20:53] with formulas and everything, but
[02:20:55] So in terms of implementation, do you
[02:20:56] think that's something that's doable?
[02:20:58] I mean I've been sort of you know
[02:20:59] talking about this to sort of various
[02:21:01] people like you know Andrew McCallum who
[02:21:04] started open review. And the reason why
[02:21:06] we picked open review for ICLR initially
[02:21:09] even though it was very early for them
[02:21:11] is because my hope was that ICLR it was
[02:21:14] eventually going to kind of
[02:21:16] inaugurate this type of system. So ICLR
[02:21:19] kept the idea of open reviews.
[02:21:21] So whether reviews are you know
[02:21:23] published with the paper which I think
[02:21:25] is very useful.
[02:21:27] But in many ways that's kind of reverted
[02:21:29] to kind of more of a conventional type
[02:21:32] conferences for everything else and that
[02:21:35] I mean I
[02:21:36] I don't run ICLR. I'm just the president
[02:21:39] of the
[02:21:40] foundation, but
[02:21:42] you know, people who run it should make
[02:21:44] decisions about how to run it and I'm
[02:21:45] not going to tell them
[02:21:47] because they're volunteers and I'm
[02:21:49] really thankful that they do that. So
[02:21:51] but I'm saddened by the fact that we're
[02:21:53] not being uh innovative enough.
[02:21:57] Yeah, me too. I hope that changes.
[02:21:59] Yeah.
[02:22:00] Cuz the communication science broadly
[02:22:01] but communication computer science ideas
[02:22:05] is is how you make those ideas have
[02:22:07] impact I think.
[02:22:08] Yeah and I think you know a lot of this
[02:22:10] is
[02:22:11] because people have in their mind kind
[02:22:14] of an objective
[02:22:16] which is you know fairness for authors
[02:22:19] and the ability to count points
[02:22:21] basically and and give credits
[02:22:23] accurately.
[02:22:24] But that comes at the expense of the
[02:22:27] progress of science.
[02:22:28] So to some extent we're slowing down the
[02:22:30] progress of science.
[02:22:32] And are we actually achieving fairness?
[02:22:34] And we're not achieving fairness. You
[02:22:35] know, we have biases. You know, we're
[02:22:38] doing you know a double blind review but
[02:22:40] you
[02:22:42] know, the the the biases are still
[02:22:44] there. There are different different
[02:22:45] kinds of biases.
[02:22:46] You write that the phenomenon of
[02:22:48] emergence, collective behavior exhibited
[02:22:50] by large collection of simple elements
[02:22:52] in interaction, is one of the things
[02:22:55] that got you into neural nets in the
[02:22:56] first place. I love cellular automata. I
[02:22:59] love simple interacting elements and the
[02:23:02] things that emerge from them. Do you
[02:23:04] think
[02:23:05] we understand how complex systems can
[02:23:07] emerge from such simple components that
[02:23:09] interact simply?
[02:23:11] No, we don't.
[02:23:12] It's a big mystery. Also it's a mystery
[02:23:13] for physicists. It's a mystery for
[02:23:15] biologists.
[02:23:17] You know, how is it that uh
[02:23:20] the
[02:23:21] universe around us seems to be
[02:23:22] increasing in complexity and not
[02:23:23] decreasing.
[02:23:25] I mean that that that is a kind of
[02:23:27] curious property of
[02:23:29] physics that despite the second law of
[02:23:30] thermodynamics
[02:23:32] we seem to be you know, evolution and
[02:23:35] and learning and
[02:23:37] etc. seems to be kind of at least
[02:23:38] locally
[02:23:40] uh to increase uh
[02:23:42] complexity and not decrease it. So
[02:23:44] perhaps the ultimate purpose of the
[02:23:45] universe is
[02:23:47] just get more complex.
[02:23:48] Have these uh I mean
[02:23:51] small pockets of beautiful complexity.
[02:23:54] Does that to cellular automata these
[02:23:57] kinds of emergence and complex systems
[02:23:59] give you some intuition or guide your
[02:24:03] understanding of machine learning
[02:24:05] systems and neural networks and so on or
[02:24:07] these for you right now desperate
[02:24:08] concepts?
[02:24:09] Well, you got you got me into it. You
[02:24:10] know, I I discovered the existence of
[02:24:14] the perceptron when I was a college
[02:24:16] student.
[02:24:18] You know, I was reading a book on it was
[02:24:19] a debate between Chomsky and Piaget and
[02:24:22] Seymour Papert from MIT was kind of
[02:24:25] singing the praise of the perceptron in
[02:24:26] that book and I I the first time I heard
[02:24:28] about the running machine. Right? So I
[02:24:30] started digging the literature and I
[02:24:31] found those paper those books which were
[02:24:33] basically trans transcription of you
[02:24:35] know
[02:24:36] workshops or conferences
[02:24:38] from the 50s and 60s about
[02:24:40] self-organizing systems.
[02:24:41] So there were there was a series of
[02:24:43] conferences on self-organizing systems
[02:24:45] and there are these books on this
[02:24:48] some of them are you can actually get
[02:24:49] them at the internet archive, you know,
[02:24:51] the
[02:24:52] digital version.
[02:24:54] Uh
[02:24:55] and there are like fascinating articles
[02:24:57] in there by this guy whose name has been
[02:24:59] largely forgotten Heinz von Foerster.
[02:25:02] So it's a German physicist who
[02:25:04] immigrated to the US and worked on
[02:25:07] self-organizing systems
[02:25:09] in the in the 50s
[02:25:11] and in the 60s he created at University
[02:25:13] of Illinois Urbana-Champaign he created
[02:25:14] the
[02:25:15] biological computer laboratory BCL
[02:25:18] which was you know all about neural
[02:25:19] nets.
[02:25:21] Unfortunately that was kind of towards
[02:25:22] the end of the popularity of neural nets
[02:25:24] so that that lab never kind of strive
[02:25:27] very much but but he wrote a bunch of
[02:25:28] papers about self-organization and about
[02:25:30] the the mystery of self-organization. An
[02:25:33] example he has is you take imagine you
[02:25:36] are in space there's no gravity and you
[02:25:38] have a big box with
[02:25:39] magnets in it, okay?
[02:25:42] You you what kind of rectangular magnets
[02:25:43] with north pole on one end,
[02:25:45] south pole on the other end. You shake
[02:25:47] the box gently, and the magnets will
[02:25:49] kind of stick to themselves and probably
[02:25:50] form like complex structure,
[02:25:52] um, you know, spontaneously. Um, you
[02:25:55] know, that could be an example of
[02:25:56] self-organization. But, you know, you
[02:25:57] have lots of example. Neural nets are an
[02:25:58] example of self-organization, too,
[02:26:01] you know, in many respect.
[02:26:03] And it's a it's a bit of a mystery, um,
[02:26:05] you know, how
[02:26:06] like what what is possible with this?
[02:26:08] Um, you know, pattern formation in
[02:26:10] physical systems,
[02:26:11] in chaotic system and things like that,
[02:26:13] you know, you know, the emergence of
[02:26:15] life, you know, things like that. So,
[02:26:17] you know, how does
[02:26:18] how does that happen?
[02:26:19] It's a it's big puzzle for for
[02:26:21] physicists, as well.
[02:26:22] It feels like understanding this the the
[02:26:25] mathematics of emergence in some
[02:26:28] constrained situations might help us
[02:26:30] create intelligence.
[02:26:32] Like uh help us
[02:26:34] add a little spice to the systems
[02:26:35] because um you seem to be able to
[02:26:39] in complex systems with emergence to be
[02:26:42] able to get a lot from little.
[02:26:44] And so that seems like a shortcut to get
[02:26:47] big leaps in performance.
[02:26:49] But, um
[02:26:51] But, there's there's a missing
[02:26:52] theoretical concept that we are we don't
[02:26:54] have.
[02:26:54] Yeah.
[02:26:55] Uh and it's the it's something also I've
[02:26:57] been fascinated by since uh my undergrad
[02:26:59] days. And it's how you measure
[02:27:01] complexity.
[02:27:03] Right. So, we don't actually have good
[02:27:05] ways of measuring or at least we have
[02:27:07] don't have good ways of interpreting
[02:27:09] the measures that we we have at our
[02:27:11] disposal. Like, how do you measure the
[02:27:12] complexity of something, right? So,
[02:27:14] there is all those things, you know,
[02:27:15] like, you know,
[02:27:16] Kolmogorov-Chaitin-Solomonoff complexity
[02:27:18] of, you know, the length of the shortest
[02:27:20] program that would generate a bit string
[02:27:22] can be thought of as the complexity of
[02:27:24] that bit string, right?
[02:27:25] Um,
[02:27:26] I've been fascinated by that concept.
[02:27:28] The problem with that is that
[02:27:31] that complexity is defined up to a
[02:27:33] constant, which can be very large.
[02:27:35] Right.
[02:27:36] Uh there's there are similar concepts
[02:27:37] that are derived from, you know, uh, uh
[02:27:40] you know, Bayesian probability theory,
[02:27:43] where, you know, the complexity of
[02:27:45] something is uh, the negative log of its
[02:27:47] probability, essentially, right? And you
[02:27:49] have a complete equivalence between the
[02:27:50] two things.
[02:27:52] And there you would think, you know, the
[02:27:53] probability is something that's well
[02:27:55] defined mathematically, which means
[02:27:56] complexity is well defined. But it's not
[02:27:58] true. You need to have a model of uh, of
[02:28:00] of the distribution.
[02:28:02] Uh, you may need to have a prior if
[02:28:03] you're doing Bayesian inference. And the
[02:28:05] prior plays the same role as the choice
[02:28:07] of the computer with which you measure
[02:28:08] your Kolmogorov complexity.
[02:28:10] And so, every measure of complexity we
[02:28:12] have has some arbitrariness in it.
[02:28:15] Um,
[02:28:16] you know, an additive constant which
[02:28:18] is can be arbitrarily large. And so,
[02:28:22] you know, how can we come up with a good
[02:28:23] theory of how things become more complex
[02:28:25] if we don't have a good measure of
[02:28:26] complexity? Yeah.
[02:28:27] Which we need for
[02:28:29] one way that people study this in the
[02:28:31] space of biology, the people that study
[02:28:33] the origin of life or try to recreate
[02:28:35] life in in the laboratory.
[02:28:37] And the the more interesting one is the
[02:28:39] alien one is when we go to other
[02:28:40] planets,
[02:28:42] how do we recognize that it's life?
[02:28:44] Cuz you you know, complexity we
[02:28:46] associate complexity, maybe some level
[02:28:48] of mobility with life.
[02:28:50] You know, we have to be able to like
[02:28:52] have concrete
[02:28:54] algorithms for like
[02:28:57] um, measuring the level of complexity we
[02:28:59] see to know to know the difference
[02:29:01] between life and non-life.
[02:29:03] And the problem is that complexity is in
[02:29:04] the eye of the beholder. So, let me give
[02:29:07] you an example. If I um,
[02:29:09] if I give you uh,
[02:29:11] an image of the MNIST digits, right? And
[02:29:13] I I flip through MNIST digits. There is
[02:29:16] some obviously some
[02:29:17] structure to it because
[02:29:19] local structure, you know, neighboring
[02:29:21] pixels are correlated
[02:29:23] uh,
[02:29:23] across the entire data set.
[02:29:26] Now, imagine that um,
[02:29:28] I I apply a random permutation to all
[02:29:31] the pixels.
[02:29:31] Mhm.
[02:29:32] A fixed random permutation. Now, show
[02:29:34] you those images, they will look
[02:29:37] you know, really disorganized to you.
[02:29:39] More complex.
[02:29:41] In fact, they're not more complex in
[02:29:42] absolute terms. They're exactly the same
[02:29:44] as originally, right? If you knew what
[02:29:46] the permutation was, you know, you could
[02:29:48] undo the permutation.
[02:29:50] Now,
[02:29:51] imagine I give you special glasses that
[02:29:53] undo that permutation.
[02:29:54] Now, all of a sudden, what looked
[02:29:56] complicated becomes simple.
[02:29:57] Right.
[02:29:58] So, if you have two if you have you
[02:30:00] know, humans on one end, and then
[02:30:02] another race of aliens that sees the
[02:30:04] universe with permutation glasses,
[02:30:05] Yeah, with the permutation glasses.
[02:30:08] What we perceive as simple to them is
[02:30:10] hardly complicated. It's probably heat.
[02:30:12] Yeah, heat, yeah.
[02:30:13] Okay, and what they perceive as simple
[02:30:15] to us is is random
[02:30:17] fluctuation. It's heat.
[02:30:19] Yeah.
[02:30:20] Uh so,
[02:30:21] in the eye of the beholder. Depends what
[02:30:23] kind of glasses you're wearing.
[02:30:24] Depends what kind of algorithm you're
[02:30:26] running in your perception system.
[02:30:28] So, I don't think we'll have a theory of
[02:30:30] intelligence, self-organization,
[02:30:32] evolution, things like that until we
[02:30:35] have a good handle on a notion of
[02:30:37] complexity, which we know is in the eye
[02:30:39] of the eye of the beholder.
[02:30:42] Yeah, it's sad to think that we might
[02:30:43] not be able to detect or interact with
[02:30:45] alien species because we're wearing
[02:30:48] different glasses.
[02:30:49] Um because their notion of locality
[02:30:51] might be different from ours.
[02:30:52] Yeah.
[02:30:52] This actually connects with uh
[02:30:54] fascinating questions in physics at the
[02:30:55] moment, like modern physics,
[02:30:57] uh quantum physics, like you know,
[02:30:59] questions about like you know, can we
[02:31:01] recover the information that's lost in a
[02:31:03] black hole and things like this, right?
[02:31:04] And uh and that relies on notions of
[02:31:07] complexity, um
[02:31:09] well, which you know, I find I find this
[02:31:10] fascinating.
[02:31:11] Can you describe your personal quest to
[02:31:13] build an expressive electronic wind
[02:31:17] instrument, EWI? What is it? What does
[02:31:20] it take
[02:31:22] to uh to build it?
[02:31:24] Well, I'm a tinkerer. I like building
[02:31:25] things. Uh I like building things with
[02:31:27] combinations of electronics and you
[02:31:29] know, mechanical stuff.
[02:31:31] Um you know, I have a bunch of different
[02:31:33] hobbies, but um
[02:31:35] you know, probably my first one was
[02:31:37] little was building model airplanes and
[02:31:39] stuff like that and I still do that to
[02:31:40] some extent.
[02:31:41] Uh but also electronics. I taught myself
[02:31:43] electronics before I studied it. Um
[02:31:46] And the reason I taught myself
[02:31:47] electronics is because of music. Um
[02:31:49] my cousin
[02:31:51] was an inspiring electronic musician and
[02:31:53] he had an analog synthesizer. And I was
[02:31:55] you know, basically modifying it for
[02:31:56] him.
[02:31:57] Mhm.
[02:31:57] Uh and building sequencers and stuff
[02:31:59] like that, right? For him. I was I was
[02:32:00] in high school when I was doing this.
[02:32:02] Hence the interest in like progressive
[02:32:04] rock like '80s. Like what's what's the
[02:32:06] greatest band of all time according to
[02:32:08] Yann LeCun?
[02:32:09] Um there's too there's too many of them,
[02:32:11] but you know, it's a combination of
[02:32:13] uh
[02:32:15] you know, Mahavishnu Orchestra, uh
[02:32:18] Weather Report, Yes,
[02:32:21] Genesis, uh you know, Peter
[02:32:23] Yes, Genesis.
[02:32:23] Peter Gabriel.
[02:32:25] Uh-huh.
[02:32:25] Um
[02:32:27] Gentle Giant, you know, things like
[02:32:28] that.
[02:32:29] Great.
[02:32:29] Okay, so this this love of electronics
[02:32:32] and this love of music combined
[02:32:33] together.
[02:32:34] Right. So, I was actually trying to play
[02:32:36] uh
[02:32:37] uh Baroque and Renaissance uh music and
[02:32:39] I I played in a or
[02:32:41] orchestra when I was in high school and
[02:32:43] uh first year of college.
[02:32:45] And I played the recorder, crumhorn, uh
[02:32:47] little bit of oboe, you know, things
[02:32:49] like that. So, I'm a I'm a wind
[02:32:51] instrument player. But I always wanted
[02:32:53] to play improvised music even though I
[02:32:54] don't know anything about it.
[02:32:55] Uh and the only way I figured uh you
[02:32:58] know, short of like learning to play the
[02:33:00] saxophone was to play electronic wind
[02:33:03] instrument. So, they behave you know,
[02:33:04] the fingering is similar to a saxophone,
[02:33:06] but you know, you you have wide variety
[02:33:08] of sound because you control the
[02:33:09] synthesizer with it. So, I I had a a
[02:33:11] bunch of those, you know, going back to
[02:33:13] the late '80s
[02:33:15] uh from either Yamaha or Akai. They
[02:33:19] they're both kind of the main
[02:33:21] manufacturers of those. So, they world
[02:33:22] classically, you know, going back
[02:33:24] several decades.
[02:33:25] Uh but I've never been completely
[02:33:26] satisfied with them because of lack of
[02:33:28] expressivity.
[02:33:31] And you know, those things, you know,
[02:33:32] are somewhat expressive. I mean, they
[02:33:33] measure the breath pressure, they
[02:33:34] measure the lip pressure, and you know,
[02:33:37] uh
[02:33:38] you have various parameters you can you
[02:33:40] can vary with with fingers, but they
[02:33:42] they they're not really as expressive as
[02:33:44] a acoustic instrument, right? You
[02:33:46] um you hear John Coltrane play two
[02:33:48] notes, and you hear you know it's John
[02:33:50] Coltrane, you know, it's got a unique
[02:33:51] sound.
[02:33:52] Mhm.
[02:33:52] Uh or or Miles Davis, right? You can
[02:33:54] hear it's Miles Davis
[02:33:56] uh playing the trumpet because the the
[02:33:59] sound
[02:34:00] reflects their
[02:34:02] you know,
[02:34:03] physiognomy, basically, the shape of the
[02:34:05] vocal tract
[02:34:07] um
[02:34:08] kind of shapes the the sound. So, how
[02:34:10] how do you do this with uh electronic
[02:34:12] instrument? And I was um many years ago
[02:34:14] I met a guy called David Wessel. He he
[02:34:17] was a professor at Berkeley and created
[02:34:19] the
[02:34:20] the center for like, you know, music
[02:34:22] technology there. And he was interested
[02:34:24] in that question.
[02:34:25] Mhm.
[02:34:26] And so, I kept kind of thinking about
[02:34:27] this for many years, and finally because
[02:34:29] of COVID, you know, I was at home. I was
[02:34:31] in my workshop. My workshop serves also
[02:34:33] as my kind of zoom uh room and and and
[02:34:36] home office, and
[02:34:37] This is in New Jersey?
[02:34:38] In New Jersey, and um I started uh
[02:34:41] really being serious about, you know,
[02:34:43] building my own EWI instrument.
[02:34:45] What else is going on in that New Jersey
[02:34:47] workshop? Is there some is some some
[02:34:49] crazy stuff you built like just or or
[02:34:51] like left on the workshop floor left
[02:34:54] behind?
[02:34:55] a lot of crazy stuff is uh you know,
[02:34:57] electronics with built with
[02:34:59] microcontrollers of various kinds, and
[02:35:02] you know, weird flying contraptions.
[02:35:05] Um
[02:35:06] So, you still love flying?
[02:35:08] It's a family disease. My uh my dad got
[02:35:10] me into it when I was a kid.
[02:35:13] And um he was building model airplanes
[02:35:15] when he was a kid, and uh and he was a
[02:35:18] mechanical engineer. He He taught
[02:35:20] himself electronics also, so he he built
[02:35:22] his early radio control systems in the
[02:35:24] late '60s, early '70s.
[02:35:26] Um and so that that that's what got me
[02:35:29] into I mean, he got me into kind of, you
[02:35:30] know, engineering and science and
[02:35:32] technology.
[02:35:33] Do you also have an interest and
[02:35:34] appreciation of flight in other forms
[02:35:36] like with drones, quadrocopters, or do
[02:35:38] you Is it model airplane the thing
[02:35:41] that's
[02:35:42] I you know, before drones were you know,
[02:35:45] kind of
[02:35:46] consumer products,
[02:35:48] um you know, I built my own, you know,
[02:35:50] with also building a microcontroller
[02:35:51] with
[02:35:53] gyroscopes and accelerometers for
[02:35:55] stabilization, writing the firmware for
[02:35:57] it, you know. And then when it became
[02:35:58] kind of a standard thing you could buy,
[02:35:59] it was boring, you know, I stopped doing
[02:36:00] it. It was not fun anymore.
[02:36:02] Um
[02:36:03] Yeah.
[02:36:04] You were doing it before it was cool.
[02:36:06] Yeah.
[02:36:06] What
[02:36:07] advice would you give to a young person
[02:36:09] today in high school and college that
[02:36:12] dreams of doing something big like Yann
[02:36:15] LeCun? Like let's talk in the space of
[02:36:17] intelligence. Dreams of having a chance
[02:36:20] to solve some fundamental problem in
[02:36:22] space of intelligence.
[02:36:23] Both for their career and just in life,
[02:36:26] being somebody who was a part of
[02:36:28] creating something special.
[02:36:30] So,
[02:36:32] try to get
[02:36:33] interested by big questions. Things
[02:36:35] like, you know, what is intelligence?
[02:36:38] What is the universe made of? What's
[02:36:40] life all about? Things like that.
[02:36:43] Um
[02:36:45] Like even like crazy big questions like
[02:36:47] what's time? Like nobody knows what time
[02:36:49] is.
[02:36:51] Um
[02:36:53] And
[02:36:54] and then
[02:36:56] learn
[02:36:57] basic things. Like basic methods either
[02:37:00] from math, from physics, or from
[02:37:01] engineering.
[02:37:03] Uh things that have a long shelf life.
[02:37:05] Like if you have a choice between like,
[02:37:07] you know,
[02:37:08] learning
[02:37:09] you know, mobile programming on iPhone
[02:37:12] or quantum mechanics. Take quantum
[02:37:13] mechanics.
[02:37:16] Um because you're going to learn things
[02:37:18] that you have no idea exist. It and it
[02:37:20] you may not you you you may never be a
[02:37:23] quantum physicist,
[02:37:25] but you will learn about path integrals.
[02:37:26] And path integrals are used um
[02:37:28] everywhere. It's the same formula that
[02:37:29] you use for, you know, Bayesian
[02:37:31] integration and stuff like that.
[02:37:33] So, the ideas, the little ideas
[02:37:36] within quantum mechanics or within some
[02:37:38] of these kind of more solidified fields
[02:37:41] will have a longer shelf life. They they
[02:37:42] you'll somehow use indirectly in in your
[02:37:46] work.
[02:37:46] Learn classical mechanics. Like you
[02:37:48] learn about Lagrangians, for example.
[02:37:49] Mhm.
[02:37:50] Um
[02:37:51] which is like a a huge hugely useful
[02:37:54] concept, you know, for all kinds of
[02:37:55] different things. Uh
[02:37:57] learn uh statistical physics because uh
[02:38:00] all the math that comes out of, you
[02:38:03] know, for machine learning
[02:38:04] uh basically comes out of uh what was
[02:38:06] figured out by statistical physicists in
[02:38:08] the uh you know, late 19th, early 20th
[02:38:10] century, right? So,
[02:38:12] uh and for some of them actually more
[02:38:13] recently for by people like like Giorgio
[02:38:15] Parisi who just got the Nobel Prize for
[02:38:18] the replica method, among other things.
[02:38:20] Um it's used for a lot of different
[02:38:21] things. Uh you know, variational
[02:38:24] inference uh
[02:38:25] that math comes from statistical
[02:38:26] physics.
[02:38:28] Um so, um so, a lot of those kind of,
[02:38:31] you know,
[02:38:32] basic courses, you know, you'll you'll
[02:38:35] if you do electrical engineering, you
[02:38:36] take signal processing, you'll you'll
[02:38:37] learn about Fourier transforms.
[02:38:39] Again, something super useful.
[02:38:41] It's at the basis of things like graph
[02:38:43] neural nets, which is a an entirely new
[02:38:47] sub area of, you know, AI machine
[02:38:49] learning, deep learning, which I think
[02:38:51] is super promising for all kinds of
[02:38:52] applications.
[02:38:53] Um something very promising if you're
[02:38:55] more interested in applications is the
[02:38:56] applications of uh AI machine learning
[02:38:58] and deep learning to science.
[02:39:01] Or to
[02:39:03] science that can help solve big problems
[02:39:05] in the world. I I have colleagues at
[02:39:07] uh at Meta at FAIR
[02:39:09] who started this project called Open
[02:39:10] Catalyst and it's
[02:39:12] it's an open project collaborative.
[02:39:14] And the idea is to use deep learning to
[02:39:17] help design
[02:39:19] new chemical compounds or materials that
[02:39:22] would facilitate the separation of
[02:39:24] hydrogen from oxygen.
[02:39:25] If you can efficiently separate oxygen
[02:39:27] from hydrogen with electricity,
[02:39:30] you you solve climate change.
[02:39:33] It's as simple as that. Because
[02:39:36] you you cover, you know, some random
[02:39:38] desert with solar panels.
[02:39:40] And you have have them work all day,
[02:39:42] produce hydrogen, and then you ship the
[02:39:44] hydrogen in wherever it's needed. You
[02:39:45] don't need anything else.
[02:39:48] You know, you you you have
[02:39:51] controllable
[02:39:52] power that's, you know, it can be
[02:39:54] transported anywhere. So, if we if we
[02:39:57] have a large-scale efficient energy
[02:40:00] storage technology like
[02:40:03] producing hydrogen,
[02:40:04] we we solve climate change. Here's
[02:40:06] another way to solve climate change. Is
[02:40:09] if you can you know how to make fusion
[02:40:10] work. Now, the problem with fusion is
[02:40:11] that you make a super hot plasma, and
[02:40:13] the plasma is unstable and you can't
[02:40:15] control it. Maybe with deep learning you
[02:40:17] can find controllers that will stabilize
[02:40:18] plasma and make, you know, practical
[02:40:20] fusion reactors.
[02:40:21] I mean, that's very speculative, but,
[02:40:23] you know, it's worth trying because
[02:40:25] you know, it the payoff is huge. There's
[02:40:28] a group at Google working on this led by
[02:40:30] John Platt.
[02:40:31] So, control convert as many problems in
[02:40:34] science and physics, biology, and
[02:40:35] chemistry into a
[02:40:38] into a learnable problem and see if a
[02:40:40] machine can learn it.
[02:40:41] Right. I mean, there's properties of,
[02:40:43] you know, complex materials that we
[02:40:45] don't understand from first principle,
[02:40:47] for example. Right? So, you know, if we
[02:40:49] could design
[02:40:50] new,
[02:40:52] you know, new materials,
[02:40:54] we could make more efficient batteries,
[02:40:56] you know, we could make maybe faster
[02:40:58] electronics. We could I mean, there's a
[02:40:59] lot of things we we imagine doing or,
[02:41:02] you know lighter
[02:41:03] materials for for cars or airplanes or
[02:41:05] things like that. Maybe better fuel
[02:41:07] cells. There's all kinds of stuff we can
[02:41:08] imagine. If we had good fuel cells,
[02:41:10] hydrogen fuel cells, uh we could use
[02:41:12] them to power airplanes and you know,
[02:41:14] transportation wouldn't be or or cars.
[02:41:17] And we wouldn't have a
[02:41:19] emission problem CO2 emission problems
[02:41:21] for for
[02:41:22] uh air transportation anymore. So, this
[02:41:25] there's a lot of those things I think
[02:41:26] where AI you know, can be used. It
[02:41:30] And and this is not even talking about
[02:41:31] all the sort of medicine, biology and
[02:41:33] and everything like that, right?
[02:41:35] You know, like
[02:41:36] protein folding, you know, figuring out
[02:41:39] like how could you design a protein that
[02:41:40] it sticks to another protein that a
[02:41:41] particular site because that's how you
[02:41:43] design drugs in the end.
[02:41:45] Um so, you know, deep learning would be
[02:41:47] useful all of those and those are kind
[02:41:48] of you know, would be sort of enormous
[02:41:50] progress if we could
[02:41:52] use it for that. Here's an example. If
[02:41:54] you take um
[02:41:55] this is like from recent material
[02:41:57] physics, you take a a monoatomic layer
[02:42:00] of graphene, right? So, it's just carbon
[02:42:03] on a hexagonal mesh and then you make
[02:42:05] this single single atom thick.
[02:42:09] You put another one on top. You twist
[02:42:10] them by some magic
[02:42:12] number of degrees, 3 degrees or
[02:42:13] something.
[02:42:14] It becomes superconductor.
[02:42:16] Nobody has any idea why.
[02:42:20] Uh I want to know how that was
[02:42:21] discovered, but that's the kind of thing
[02:42:23] that machine learning can actually
[02:42:24] discover these kinds of things.
[02:42:25] maybe not, but but there is
[02:42:28] a hint perhaps that with machine
[02:42:30] learning we could train a system to
[02:42:32] basically be a phenomenological model of
[02:42:35] some complex emergent phenomenon which
[02:42:37] you know,
[02:42:38] superconductivity is one of those.
[02:42:41] Uh
[02:42:42] where you know, thing this collective
[02:42:44] phenomenon is too difficult to describe
[02:42:45] from first principles with the current
[02:42:47] you know,
[02:42:48] the usual sort of you know, reductionist
[02:42:50] type method, but we could have
[02:42:53] uh deep learning systems that predict
[02:42:55] the properties
[02:42:57] of a system from a description of it
[02:42:59] after being trained with sufficiently
[02:43:01] many samples.
[02:43:03] Um
[02:43:04] So, this guy Pascal Fua at EPFL, he has
[02:43:07] a startup company
[02:43:08] that
[02:43:09] where he he basically trained a
[02:43:12] convolutional net essentially to predict
[02:43:15] the aerodynamic properties of solids.
[02:43:17] And you can generate as much data as you
[02:43:19] want by just running computational fluid
[02:43:21] dynamics, right? So, you give a
[02:43:23] like a
[02:43:25] a wing
[02:43:27] airfoil or something shape of some kind,
[02:43:29] and you run computational fluid
[02:43:30] dynamics, you get as a result the
[02:43:33] drag and, you know,
[02:43:35] uh lift and all that stuff, right? And
[02:43:37] you can you can generate lots of data,
[02:43:40] train a neural net to make those
[02:43:41] predictions, and now what you have is a
[02:43:42] differentiable model
[02:43:44] of, let's say, drag and and lift as a
[02:43:47] function of the shape of that solid, and
[02:43:48] so you can do back gradient descent, you
[02:43:49] can optimize the shape so you get the
[02:43:51] properties you want.
[02:43:54] Um
[02:43:54] Yeah, that's incredible. That's
[02:43:56] incredible. And on top of all that,
[02:43:58] probably
[02:43:59] you should read a little bit of
[02:44:00] literature and a little bit of history
[02:44:03] for inspiration and for wisdom, cuz
[02:44:06] after all, all of these technologies
[02:44:08] will have to work in the human world.
[02:44:10] Yes.
[02:44:10] And the human world is complicated.
[02:44:12] It is.
[02:44:13] It's heavy.
[02:44:14] Yann, this is um
[02:44:17] an amazing conversation. I'm really
[02:44:18] honored that you would talk with me
[02:44:19] today. Thank you for all the amazing
[02:44:21] work you're doing at FAIR at Meta, and
[02:44:24] thank you for being so passionate after
[02:44:26] all these years about everything that's
[02:44:28] going on. You're you're a beacon of hope
[02:44:29] for the machine learning community, and
[02:44:31] thank you so much for spending your
[02:44:33] valuable time with me today. That was
[02:44:34] awesome.
[02:44:35] Thanks for having me on. That was It was
[02:44:37] a pleasure.
[02:44:38] Thanks for listening to this
[02:44:39] conversation with Yann LeCun. To support
[02:44:41] this podcast, please check out our
[02:44:43] sponsors in the description.
[02:44:45] And now, let me leave you with some
[02:44:47] words from Isaac Asimov.
[02:44:50] Your assumptions are your windows on the
[02:44:52] world.
[02:44:53] Scrub them off every once in a while or
[02:44:56] the light won't come in.
[02:44:58] Thank you for listening and hope to see
[02:45:00] you next time.
