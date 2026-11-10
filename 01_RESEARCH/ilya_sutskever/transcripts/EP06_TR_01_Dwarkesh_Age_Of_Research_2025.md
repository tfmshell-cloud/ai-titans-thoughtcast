# Dwarkesh Patel: Ilya Sutskever — Moving From Age of Scaling to Age of Research
- **YouTube URL:** https://www.youtube.com/watch?v=aR20FWCCjAs
- **Lines:** 2537

---

[00:00:00] You know what's crazy that all of this
[00:00:02] is real?
[00:00:04] >> Yeah. Meaning what?
[00:00:05] >> Don't you think so?
[00:00:06] >> Meaning what?
[00:00:06] >> Like all this AI stuff and all this
[00:00:08] area. Yeah. That it's happen like
[00:00:11] >> isn't it straight out of science
[00:00:13] fiction?
[00:00:13] >> Yeah. Another thing that's crazy is like
[00:00:16] how normal the slow takeoff feels. The
[00:00:19] idea that we'd be investing 1% of GDP in
[00:00:22] AI, like I feel like it would have felt
[00:00:24] like a bigger deal, you know, where
[00:00:26] right now it just feels like
[00:00:27] >> you get used to things pretty fast.
[00:00:28] Turns out Yeah. But also it's kind of
[00:00:30] like it's abstract like what does it
[00:00:32] mean? What it means that you see it in
[00:00:35] the news.
[00:00:35] >> Yeah.
[00:00:36] >> That such and such company announced
[00:00:37] such and such dollar amount,
[00:00:39] >> right?
[00:00:40] >> That's that's all you see,
[00:00:41] >> right?
[00:00:42] >> It's not really felt in any other way so
[00:00:45] far.
[00:00:45] >> Yeah. Should we actually begin here? I
[00:00:46] think this is an interesting discussion.
[00:00:48] >> Sure.
[00:00:48] >> I think your point about well from the
[00:00:51] average person's point of view, nothing
[00:00:53] is that different will continue being
[00:00:55] true even into the singularity.
[00:00:57] >> No, I don't think so. Okay. Interesting.
[00:01:00] >> So the thing which I was referring to
[00:01:02] not feeling different
[00:01:05] is okay. So such and such company
[00:01:07] announced some difficult to comprehend
[00:01:10] dollar amount of investment
[00:01:12] >> right
[00:01:12] >> I don't think anyone knows what to do
[00:01:14] with that.
[00:01:15] >> Yeah.
[00:01:15] >> But I think that the impact of AI is
[00:01:19] going to be felt.
[00:01:21] >> AI is going to be diffused through the
[00:01:23] economy. There are very strong economic
[00:01:25] forces for this and I think the impact
[00:01:28] is going to be felt very strongly.
[00:01:30] >> When do you expect that impact? I think
[00:01:32] the models seem smarter than their
[00:01:35] economic impact would imply.
[00:01:38] >> Yeah, this is
[00:01:41] one of the very confusing things about
[00:01:42] the models right now. How to reconcile
[00:01:47] the fact that they are doing so well on
[00:01:51] evals.
[00:01:52] >> Mhm. And you look at the evals and you
[00:01:54] go, those are pretty hard evals,
[00:01:56] >> right?
[00:01:57] >> They're doing so well,
[00:01:59] >> but the economic impact seems to be
[00:02:02] dramatically behind. And it's almost
[00:02:05] like
[00:02:07] it's it's very difficult to make sense
[00:02:09] of how can the model on the one hand do
[00:02:12] these amazing things and then on the
[00:02:14] other hand like repeat itself twice in
[00:02:17] some situation in a kind of a an example
[00:02:21] would be let's say you use VIP coding to
[00:02:23] do something and you go to some place
[00:02:25] and then you get a bug and then you tell
[00:02:27] the model can you please fix the bug?
[00:02:29] >> Yeah. And the model says, "Oh my god,
[00:02:32] you're so right. I have a bug. Let me go
[00:02:33] fix that." And it introduces a second
[00:02:35] bug.
[00:02:35] >> Yeah.
[00:02:36] >> And then you tell it you have you have
[00:02:38] this new second bug and it tells you,
[00:02:40] "Oh my god, how could I've done it?
[00:02:41] You're so right again."
[00:02:42] >> And brings back the first bug. And you
[00:02:44] can alternate between those.
[00:02:45] >> Yeah.
[00:02:46] >> And it's like, how is that possible?
[00:02:48] >> Yeah.
[00:02:48] >> It's like I'm not sure. But it does
[00:02:52] suggest that the
[00:02:54] something strange is going on. I have
[00:02:57] two possible explanations. So here this
[00:02:59] is the more kind of a whimsical
[00:03:02] explanation is that maybe a real
[00:03:03] training makes the models a little bit
[00:03:05] too single-minded and narrowly focused a
[00:03:08] little bit too
[00:03:11] I don't know unaware
[00:03:14] even though it also makes them aware in
[00:03:15] some other ways
[00:03:17] and because of this they can't do basic
[00:03:20] things but there is another explanation
[00:03:22] which is
[00:03:24] back when people were doing pre-training
[00:03:27] the question of what data to train on
[00:03:31] was answered because the that answer was
[00:03:34] everything.
[00:03:35] >> Yeah.
[00:03:36] >> When you do pre-training, you need all
[00:03:38] the data.
[00:03:41] So you don't have to think is it going
[00:03:43] to be this data or that data.
[00:03:44] >> Yeah.
[00:03:44] >> But when people do RL training, they do
[00:03:47] need to think. They say okay, we want to
[00:03:49] have this kind of RL training for this
[00:03:51] thing and that kind of RL training for
[00:03:53] that thing. And from what I hear, all
[00:03:56] the companies have teams that just
[00:03:58] produce new RL environments and just add
[00:04:01] it to the training mix. And then the
[00:04:02] question is, well, what are those? There
[00:04:04] are so many degrees of freedom. There is
[00:04:06] such a huge variety of environments you
[00:04:08] could produce. And one of the
[00:04:12] one thing you could do, and I think
[00:04:14] that's something that is done
[00:04:15] inadvertently,
[00:04:17] is that people take inspiration from the
[00:04:20] evals. you say, "Hey, I would love our
[00:04:24] model to do really well when we release
[00:04:25] it. I want the EVOS to look great."
[00:04:28] What would be RL training that could
[00:04:31] help on this task, right? I think that
[00:04:34] is something that happens and I think it
[00:04:36] could explain a lot of what's going on.
[00:04:39] If you combine this with generalization
[00:04:41] of the models actually being inadequate,
[00:04:44] that has the potential to explain a lot
[00:04:46] of what we are seeing. this disconnect
[00:04:48] between eval performance and actual real
[00:04:52] real world performance which is
[00:04:54] something that we don't today exactly
[00:04:57] even understand what what we mean by
[00:04:59] that I I like this idea that the real
[00:05:02] reward hacking is a human researchers
[00:05:05] who are too focused on the evals um I
[00:05:09] think there's two ways to understand or
[00:05:11] to try to think about what what you have
[00:05:13] just pointed out one is look if it's the
[00:05:17] case that simply by becoming superhuman
[00:05:20] at a coding competition, a model will
[00:05:22] not automatically become more tasteful
[00:05:26] and exercise better judgment about how
[00:05:28] to improve your codebase. Well, then you
[00:05:30] should expand the suite of environments
[00:05:32] such that you're not just testing it on
[00:05:34] having the best performance in coding
[00:05:36] competition. It should also be able to
[00:05:37] make the best kind of application for X
[00:05:40] thing or Y thing or Z thing. And another
[00:05:42] maybe this is what you're hinting at is
[00:05:44] to say why should it be the case in the
[00:05:47] first place that becoming super human at
[00:05:50] coding competitions doesn't make you a
[00:05:52] more tasteful programmer more generally.
[00:05:54] Maybe the thing to do is not to keep
[00:05:57] stacking up the amount of environments
[00:05:58] and the diversity of environments to
[00:06:00] figure out approach with let you learn
[00:06:02] from one environment and improve your
[00:06:05] performance on something else. So I have
[00:06:09] I have an analog a human analogy which
[00:06:11] might be helpful. So even the case let's
[00:06:14] take the case of competitive programming
[00:06:15] since you mentioned that and suppose you
[00:06:17] have two students
[00:06:19] one of them work decided they want to be
[00:06:22] the best competitive programmer. So they
[00:06:24] will practice 10,000 hours for that
[00:06:28] domain. They will solve all the
[00:06:30] problems, memorize all the proof
[00:06:31] techniques and be very very you know
[00:06:35] be very skilled at quickly and correctly
[00:06:38] implementing all the algorithms and by
[00:06:40] doing by doing so they became the best
[00:06:42] one of the best student number two
[00:06:45] thought oh competitive programming is
[00:06:47] cool maybe they practiced for 100 hours
[00:06:50] >> much much less and they also did really
[00:06:52] well which one do you think is going to
[00:06:53] do better in their career later on
[00:06:56] >> the second
[00:06:56] >> right and I think that's basically
[00:06:58] what's going on. The models are much
[00:07:00] more like the first student but even
[00:07:01] more because then we say okay so the
[00:07:04] model should be good at competitive
[00:07:05] programming so let's get every single
[00:07:07] competitive programming problem ever and
[00:07:10] then let's do some data augmentation so
[00:07:11] we have even more competitive
[00:07:13] programming problems
[00:07:14] >> yes
[00:07:14] >> and we train on that and so now you got
[00:07:16] this great competitive programmer and
[00:07:18] with this analogy I think it's more
[00:07:20] intuitive I think it's more intuitive
[00:07:22] with this analogy that yeah okay so if
[00:07:24] it's so well trained okay it's like all
[00:07:26] the different algorithms and all the
[00:07:28] proof techniques are like right at it at
[00:07:30] its fingertips
[00:07:32] and it's more intuitive that with this
[00:07:34] level of preparation it not would not
[00:07:36] necessarily generalize to other things.
[00:07:39] >> But then what is the um analogy for what
[00:07:42] the second student is doing before they
[00:07:45] do the 100 hours of fine-tuning.
[00:07:48] >> I think it's like
[00:07:50] they have it. I think it's the it
[00:07:53] factor.
[00:07:53] >> Yeah.
[00:07:54] >> Right. And like I know like when I was
[00:07:55] in undergrad, I remember there was there
[00:07:57] was a student like this that studied
[00:07:59] with me. So I I know it exists.
[00:08:01] >> Yeah. I think it's interesting to
[00:08:02] distinguish it from whatever
[00:08:04] pre-training does. So one way to
[00:08:06] understand what you just said about we
[00:08:09] don't have to choose the data in
[00:08:10] pre-training is to say actually it's not
[00:08:13] dissimilar to the 10,000 hours of
[00:08:14] practice. It's just that you get that
[00:08:15] 10,000 hours of practice for free
[00:08:18] because it's already somewhere in the
[00:08:21] pre-training distribution. But it's like
[00:08:22] maybe you're suggesting actually there's
[00:08:24] actually not that much generalization
[00:08:26] for pre-training. There's just so much
[00:08:27] data in pre-training but it's like it's
[00:08:29] not necessarily generalizing better than
[00:08:30] RL.
[00:08:31] >> Like the main the main strength of
[00:08:32] pre-training is that there is a so much
[00:08:34] of it.
[00:08:35] >> Yeah.
[00:08:36] >> And b you don't have to think hard about
[00:08:39] what data to put into pre-training.
[00:08:42] >> And it's a very kind of natural data and
[00:08:45] it does include in it a lot of what
[00:08:48] people do.
[00:08:48] >> Yeah.
[00:08:50] people's thoughts and a lot of the
[00:08:53] features of you know it's like the whole
[00:08:55] world as projected by people onto text.
[00:08:59] >> Yeah.
[00:09:00] >> And pre-training tries to capture that
[00:09:01] using a huge amount of data.
[00:09:04] It's it's very the pre-training is very
[00:09:07] difficult to reason about because it's
[00:09:09] so hard to understand the manner in
[00:09:13] which the model relies on pre-training
[00:09:16] data. And whenever the model makes a
[00:09:18] mistake, could it be because something
[00:09:21] by chance is not as supported by the
[00:09:23] pre-training data? You know, and pre
[00:09:25] support by pre-training is maybe a loose
[00:09:28] term.
[00:09:30] I I don't know if I can add anything
[00:09:32] more useful on this, but
[00:09:36] I don't think there is a human analog to
[00:09:37] pre-training. Um, here's analogies that
[00:09:40] people have proposed for what the human
[00:09:42] analogy to pre-training is, and I'm
[00:09:43] curious to get your thoughts on why
[00:09:45] they're potentially wrong. One is to
[00:09:49] think about the first 18 or 15 or 13
[00:09:52] years of a person's life when they
[00:09:54] aren't necessarily economically
[00:09:55] productive, but they are doing something
[00:09:58] that is making them understand the world
[00:10:02] better and so forth. And the other is to
[00:10:04] think about evolution as doing some kind
[00:10:07] of search for three billion years which
[00:10:09] then results in a human lifetime
[00:10:12] instance. And then I'm curious if you
[00:10:15] think either of these are actually
[00:10:16] analogous to pre-training or how how
[00:10:18] would you think about at least what
[00:10:19] lifetime human learning is like if not
[00:10:21] pre-training. I think there are some
[00:10:24] similarities between both of these two
[00:10:26] pre-training and pre-training tries to
[00:10:28] play the role of both of these
[00:10:30] >> but I think there are some big
[00:10:32] differences as well.
[00:10:34] The amount of pre-training data is
[00:10:37] very very staggering.
[00:10:39] >> Yes.
[00:10:41] >> And somehow a a human being after even
[00:10:44] 15 years with a tiny fraction of that
[00:10:47] pre-training data they know much less.
[00:10:49] >> Yeah. But whatever they do know they
[00:10:50] know much more deeply somehow and the
[00:10:53] mistakes like like already at that age
[00:10:56] you would not make mistakes that are
[00:10:58] make.
[00:10:59] >> Yeah. There is another thing you might
[00:11:00] say could it be something like evolution
[00:11:02] and the answer is maybe but in this case
[00:11:05] I think evolution might actually have an
[00:11:06] edge like there is this I remember
[00:11:10] reading about this case where some you
[00:11:14] know that one thing that neuroscientists
[00:11:16] do or rather one way in which
[00:11:18] neuroscientists can learn about the
[00:11:20] brain is by studying people with brain
[00:11:23] damage to different parts of the brain
[00:11:25] >> and and so and some people have the most
[00:11:28] strange symptoms you could imagine. It's
[00:11:29] actually really really interesting. And
[00:11:32] there was one case that comes to mind
[00:11:33] that's relevant.
[00:11:35] I read about this person who had some
[00:11:38] kind of brain damage that took out I
[00:11:41] think a stroke or an accident that took
[00:11:44] out his emotional
[00:11:47] processing. So he stopped feeling any
[00:11:49] emotion
[00:11:51] and as a result of that you know he
[00:11:55] still remained very articulate and he
[00:11:56] could solve little puzzles and on tests
[00:11:59] he seemed to be just fine but he felt no
[00:12:02] emotion he didn't feel sad he didn't
[00:12:03] feel angry he didn't feel animated and
[00:12:06] he became somehow extremely bad at
[00:12:09] making any decisions at all it would
[00:12:11] take him hours to decide on which socks
[00:12:13] to wear and he would make very bad
[00:12:16] financial decisions
[00:12:18] And that's very
[00:12:22] but does what what does it say about
[00:12:26] the role of our built-in emotions
[00:12:30] in making us like a viable agent
[00:12:32] essentially
[00:12:33] >> and I guess to connect to your question
[00:12:35] about pre-training
[00:12:36] >> it's like maybe pre- like maybe if you
[00:12:39] are good enough at like getting
[00:12:41] everything out of pre-training you can
[00:12:42] get you could get that as well but
[00:12:45] that's the kind of thing which seems is
[00:12:50] well it may or may not be possible to
[00:12:53] get that from pre-training. What is
[00:12:58] that clearly not just directly emotion?
[00:13:00] And it seems like some
[00:13:04] almost value function like thing which
[00:13:05] is giving telling you which decision to
[00:13:07] be like what the end reward for any
[00:13:10] decision should be and you think that
[00:13:12] doesn't sort of implicitly come from
[00:13:15] >> I think it could I'm just saying it's
[00:13:16] not one it's not 100% obvious.
[00:13:19] >> Yeah. But what is that like what how do
[00:13:22] you think about emotions and what is the
[00:13:24] ML analogy for emotions?
[00:13:26] >> It should be some kind of a value
[00:13:27] function thing.
[00:13:28] >> Yeah. But I don't think there is a great
[00:13:30] ML analogy because right now value
[00:13:32] functions don't play a very prominent
[00:13:34] role in uh the things people do.
[00:13:36] >> It might be worth defining for the
[00:13:37] audience what a value function is if if
[00:13:39] you want to do that.
[00:13:40] >> I mean certainly I I'll be very happy to
[00:13:42] do that. Right. So
[00:13:49] so when people do reinforcement learning
[00:13:50] the way reinforcement learning is done
[00:13:52] right now how do they do how do people
[00:13:54] train those agents? So you have your
[00:13:56] neural net and you give it a problem and
[00:13:59] then you tell the model go solve it and
[00:14:01] the model takes maybe thousands hundreds
[00:14:03] of thousands of actions
[00:14:06] or thoughts or something and then it
[00:14:08] produces a solution. The solution is
[00:14:09] created and then the score
[00:14:12] is used to provide a training signal for
[00:14:15] every single action
[00:14:18] in your trajectory.
[00:14:19] >> Mhm. So that means that if you are doing
[00:14:22] something that goes for a long time, if
[00:14:24] you're training a task that takes a long
[00:14:27] time to solve, you will do no learning
[00:14:30] at all until you solve the until you
[00:14:31] came up with a proposed solution. That's
[00:14:33] how reinforcement learning is done
[00:14:34] naively. That's how O1 R1 ostensibly are
[00:14:38] done.
[00:14:40] The value function says something like
[00:14:43] okay look maybe I could sometimes not
[00:14:46] always could tell you if you're doing
[00:14:49] well or badly. The notion of a value
[00:14:51] function is more useful in some domains
[00:14:53] than others. So for example when you
[00:14:54] play chess
[00:14:56] and you lose a piece you know I messed
[00:14:58] up. You don't need to play the whole
[00:15:01] game to know that what I just did was
[00:15:03] bad and therefore whatever um whatever
[00:15:06] preceded it was also bad. So the value
[00:15:09] function lets you short circuit the
[00:15:13] weight until the very end. Like let's
[00:15:15] suppose that you started to pursue some
[00:15:17] kind of um okay let's suppose that you
[00:15:19] are doing some kind of a math thing or a
[00:15:21] programming thing and you're trying to
[00:15:23] explore a particular solution direction
[00:15:26] and after let's say after a thousand uh
[00:15:29] steps of thinking you concluded that
[00:15:31] this direction is unpromising.
[00:15:34] As soon as you conclude this, you could
[00:15:36] already get a reward signal a thousand
[00:15:40] time steps previously when you decided
[00:15:42] to pursue down this path. You say, "Oh,
[00:15:44] next time I shouldn't pursue this path
[00:15:46] in a similar situation long before you
[00:15:49] actually came up with a proposed
[00:15:50] solution." M this was in the deepcar one
[00:15:53] paper is that the
[00:15:56] space of trajectories is so wide that
[00:16:00] maybe it's hard to learn a mapping from
[00:16:03] an intermediate trajectory and value and
[00:16:06] also given that you know in coding for
[00:16:08] example you'll have the wrong idea then
[00:16:10] you'll go back then you'll change
[00:16:12] something
[00:16:12] >> this sounds like such lack of faith in
[00:16:14] deep learning
[00:16:15] >> like I mean sure it might be difficult
[00:16:18] but
[00:16:19] >> nothing deep learning can't Yeah.
[00:16:22] >> So my expectation is that
[00:16:26] like value functions should be useful
[00:16:28] and
[00:16:30] and I fully I fully expect that they
[00:16:32] will be used in the future if not
[00:16:33] already. What was I alluding to with the
[00:16:36] person whose emotional center got
[00:16:39] >> um damaged is more that
[00:16:45] maybe what it suggests is that the value
[00:16:47] function of humans is modulated by
[00:16:50] emotions in some important way that's
[00:16:52] hardcoded by evolution
[00:16:55] and maybe that is important for people
[00:16:57] to be effective in the world.
[00:17:00] >> That that's the thing I was actually
[00:17:01] planning on asking you. There's
[00:17:02] something really interesting about
[00:17:03] emotions as a value function, which is
[00:17:05] that it's impressive that they have this
[00:17:08] much utility while still being rather
[00:17:12] um simple to understand.
[00:17:15] So I have two responses. I do agree that
[00:17:20] compared to
[00:17:23] the kind of things that we learn and the
[00:17:25] things we are talking about, the kind of
[00:17:26] ads we talking about, emotions are
[00:17:28] relatively simple.
[00:17:31] They might even be so simple that maybe
[00:17:33] you could map them out in a human
[00:17:34] understandable way. I think it would be
[00:17:36] cool to do.
[00:17:39] In terms of utility though, I think
[00:17:41] there is a thing where you know there is
[00:17:43] this complexity robustness trade-off
[00:17:48] where complex things can be very useful
[00:17:52] but simple things are very useful in a
[00:17:56] very broad range of situations. And so I
[00:17:59] think what what one way to interpret
[00:18:01] what we are seeing is that we've got
[00:18:02] these emotions that essentially evolved
[00:18:05] mostly mostly from our mammal ancestors
[00:18:09] and then fine-tuned a little bit while
[00:18:10] we were homminids just a bit. We do have
[00:18:13] like a decent amount of social emotions
[00:18:15] though which mammals may lack
[00:18:19] but they're not very sophisticated
[00:18:21] and because they're not sophisticated
[00:18:23] they serve us so well in this very
[00:18:25] different world compared to the one that
[00:18:26] we've been living in. Actually they they
[00:18:29] also make mistakes. For example, our
[00:18:31] emotions well I don't know does hunger
[00:18:33] count as an emotion
[00:18:35] debate. It's debatable but I think for
[00:18:37] example our intuitive feeling of hunger
[00:18:42] is not succeeding in guiding us
[00:18:46] correctly in this world with an
[00:18:48] abundance of food.
[00:18:49] >> Yeah. People have been talking about
[00:18:51] scaling data, scaling parameters,
[00:18:54] scaling compute.
[00:18:56] Is there a more general way to think
[00:18:57] about scaling? What are the other
[00:18:58] scaling axes?
[00:19:00] So
[00:19:03] the thing so so here here is a
[00:19:05] perspective here's a perspective I think
[00:19:07] might be might be true.
[00:19:10] So
[00:19:12] the way ML used to work is that people
[00:19:15] would just think of it with stuff and
[00:19:17] try to
[00:19:20] and try to get interesting results.
[00:19:22] That's what's been going on in the past.
[00:19:26] Then
[00:19:28] the scaling insight arrived, right?
[00:19:31] Scaling laws, GPT3.
[00:19:34] And suddenly everyone realized we should
[00:19:36] scale.
[00:19:39] And it's just this, this is an example
[00:19:41] of how language affects thought.
[00:19:45] Scaling is what just one word, but it's
[00:19:48] such a powerful word because it informs
[00:19:50] people what to do. They say, "Okay,
[00:19:51] let's let's try to scale things." And so
[00:19:54] you say okay so what are we scaling and
[00:19:57] pre-training was a thing to scale it was
[00:19:59] a particular scaling recipe.
[00:20:01] >> Yes
[00:20:02] >> the big breakthrough of pre-training is
[00:20:04] the realization that this recipe is
[00:20:06] good. So you say hey if you mix some
[00:20:10] compute with some data into a neural net
[00:20:14] of a certain size you will get results
[00:20:17] and you will know that it will be better
[00:20:19] if you just scale the recipe up. And
[00:20:22] this is also great. Companies love this
[00:20:24] because it gives you a very uh lowrisk
[00:20:28] way of investing.
[00:20:30] >> Yeah.
[00:20:30] >> Your resources.
[00:20:31] >> Yeah.
[00:20:32] >> Right. It's much harder to invest your
[00:20:34] resources in research. Compare that. You
[00:20:37] know, if you research, you need to have
[00:20:38] like go forth researchers and research
[00:20:40] and come up with something versus get
[00:20:43] more data, get more compute. You know,
[00:20:45] you'll get something from pre-training.
[00:20:48] And indeed, you know, it looks like I
[00:20:51] based on various um
[00:20:54] um things people say on some people say
[00:20:56] on Twitter, maybe it appears that Gemini
[00:20:58] have found a way to get more out of
[00:21:00] pre-training. At some point though,
[00:21:02] pre-training will run out of data. The
[00:21:03] data is very clearly finite. And so
[00:21:05] then, okay, what do you do next? Either
[00:21:07] you do some kind of a souped-up
[00:21:09] pre-training, different recipe from the
[00:21:11] one you've done before, or you're doing
[00:21:13] a RL or maybe something else. But now
[00:21:16] that compute is big, computer is now
[00:21:18] very big. In some sense, we are back to
[00:21:20] the age of research. So maybe here's
[00:21:23] another way to put it. Up until 2020,
[00:21:25] from 201 from 2012 to 2020, it was the
[00:21:29] age of research. Now from 2020 to 2025,
[00:21:33] it was the age of scaling or maybe plus
[00:21:35] minus. Let's add arrow bars to those
[00:21:37] years because people say this is
[00:21:38] amazing. You got to scale more. Keep
[00:21:40] scaling. The one word scaling. But now
[00:21:43] the scale is so big. Like is is it is
[00:21:46] the belief really that oh it's so big
[00:21:49] but if you had 100x more everything
[00:21:51] would be so different. Like it would be
[00:21:53] different for sure but like is the
[00:21:56] belief that if you just 100x the scale
[00:21:59] everything would be transformed.
[00:22:02] I don't think that's true. So it's back
[00:22:04] to the age of research again just with
[00:22:05] big computers.
[00:22:06] >> That's a very interesting way to put it.
[00:22:10] But let me ask you the question you just
[00:22:11] posed then. What are we scaling and what
[00:22:14] what is what would it mean to have a
[00:22:16] recipe? Because I guess I'm not aware of
[00:22:19] a very clean
[00:22:22] relationship that almost looks like a
[00:22:23] law of physics which existed in
[00:22:24] pre-training that was a power law
[00:22:26] between data or computer parameters and
[00:22:29] loss. What is the kind of relationship
[00:22:33] we should be seeking and how how should
[00:22:35] we think about what this new recipe
[00:22:37] might look like? So, we've we've already
[00:22:41] witnessed a transition from
[00:22:45] one type of scaling to a different type
[00:22:46] of scaling, from pre-training to RL.
[00:22:51] Now, people are scaling RL. Now, based
[00:22:53] on what people say on Twitter, they
[00:22:57] spend more compute on RL than on
[00:22:58] pre-training at this point because RL
[00:23:01] can actually consume quite a bit of
[00:23:02] compute. You know, you do very very long
[00:23:05] rollouts.
[00:23:06] >> Yes. So it takes a lot of compute to
[00:23:08] produce those rollouts and then you get
[00:23:10] relatively small amount of learning per
[00:23:12] roll out. So you really can spend you
[00:23:13] really can spend a lot of compute and I
[00:23:16] could imagine like I wouldn't at this at
[00:23:19] this st it's it's more like I wouldn't
[00:23:22] even call it a scale um scaling I would
[00:23:24] say hey like what are you doing and is
[00:23:27] the thing you are doing the the the the
[00:23:29] most productive thing you could be
[00:23:31] doing? Yeah.
[00:23:31] >> Can you find a most more productive way
[00:23:34] of using your compute? We've discussed
[00:23:36] the value function business earlier and
[00:23:39] maybe once people get good at value
[00:23:41] functions they will be using their their
[00:23:44] um resources more productively
[00:23:47] and if you find a whole other way of
[00:23:50] training models you could say is this
[00:23:53] scaling or is it just using your
[00:23:55] resources I think it becomes a little
[00:23:57] bit ambiguous in a sense that when
[00:23:59] people were in the age of research back
[00:24:01] then it was like people say hey let's
[00:24:02] try this and this and this let's try
[00:24:03] that and that and that oh look something
[00:24:05] interesting is happening and I think
[00:24:08] there will be a return to that.
[00:24:10] >> So if we're back in the era of research,
[00:24:12] stepping back, what is the part of the
[00:24:13] recipe that we need to think most about?
[00:24:17] When you say value function, people are
[00:24:18] already trying the current recipe, but
[00:24:21] then having LLM as a judge and so forth,
[00:24:23] you could say that's a value function,
[00:24:24] but it sounds like you have something
[00:24:25] much more fundamental in mind. Do we
[00:24:27] need do we need to go back to
[00:24:29] should we even rethink pre-training at
[00:24:32] all and not just add more steps to the
[00:24:34] end of that process?
[00:24:35] >> Yeah. So the the the the discussion
[00:24:39] about value function I think it was
[00:24:40] interesting. I want to like emphasize
[00:24:43] that I think the value function is
[00:24:45] something like
[00:24:46] it's going to make RL more efficient
[00:24:50] and I think that makes a difference but
[00:24:52] I think that anything you can do with a
[00:24:55] value function you can do without just
[00:24:56] more slowly.
[00:24:57] >> Mhm.
[00:25:00] >> The thing which I think is the most
[00:25:01] fundamental is that these models somehow
[00:25:03] just generalize dramatically worse than
[00:25:06] people.
[00:25:06] >> Yes.
[00:25:07] >> And it's super obvious.
[00:25:10] That's that seems like a very
[00:25:11] fundamental thing.
[00:25:12] >> Okay, so this is the crux of
[00:25:14] generalization and there's two
[00:25:18] sub questions.
[00:25:20] There's one which is about sample
[00:25:22] efficiency which is why should it take
[00:25:23] so much more data for these models to
[00:25:24] learn than humans. There's a second
[00:25:26] about even separate from the amount of
[00:25:29] data it takes, there's a question of why
[00:25:31] is it so hard to teach the thing we want
[00:25:34] to a model than to a human which is to
[00:25:36] say for to a human that we don't
[00:25:39] necessarily need a verifiable reward to
[00:25:41] be able to
[00:25:43] you're probably mentoring a bunch of
[00:25:44] researchers right now and you're you
[00:25:46] know talking with them you're showing
[00:25:48] them your code and you're showing them
[00:25:49] how you think and from that they're
[00:25:51] picking up your way of thinking and how
[00:25:53] they should do research. You don't have
[00:25:55] to set like a verifiable reward for them
[00:25:57] that's like okay this is the next part
[00:25:58] of the curriculum and now this is the
[00:25:59] next part of your curriculum and oh it
[00:26:01] was this training was unstable and we
[00:26:02] gota there's not this shleppy bespoke
[00:26:04] process. So perhaps these two issues are
[00:26:07] actually related in some way but I'd be
[00:26:09] curious to
[00:26:12] explore this this second thing which
[00:26:13] feels more like continual learning and
[00:26:14] this first thing which feels just like
[00:26:17] um sample efficiency.
[00:26:19] >> Yeah. So you know you could actually
[00:26:20] wonder one one possible explanation for
[00:26:25] the human sample efficiency that needs
[00:26:27] to be considered is evolution
[00:26:30] and evolution has given us a small
[00:26:33] amount of the mo the most useful
[00:26:36] information possible
[00:26:38] and for things like vision
[00:26:41] hearing and locomotion
[00:26:44] I think there's a pretty strong case
[00:26:45] that evolution actually has given us a
[00:26:48] lot. Mhm.
[00:26:49] >> So for example, human dexterity far
[00:26:53] exceeds I mean robots can become
[00:26:56] dexterous too if you subject them to
[00:26:57] like a huge amount of training in
[00:26:59] simulation. But to train a robot in the
[00:27:02] real world to quickly like pick up a new
[00:27:04] skill like a person does seems very out
[00:27:06] of reach. And here you could say, oh
[00:27:08] yeah, like locomotion all our ancestors
[00:27:12] needed great locomotion squirrels like
[00:27:15] so locomotion maybe like we've got like
[00:27:18] some unbelievable prior. You could make
[00:27:20] the same case for vision. You know, I I
[00:27:22] believe Yan Lakhan made the point, oh,
[00:27:24] like um children learn to drive after 16
[00:27:27] hour after like 10 hours of practice,
[00:27:29] which is true, but our vision is so
[00:27:32] good. At least for me, when I remember
[00:27:35] myself being 5 years old, my I was I was
[00:27:38] very excited about cars back then, and
[00:27:41] I'm pretty sure my car recognition was
[00:27:43] more than adequate for self-driving
[00:27:45] already. As a 5-year-old, you don't get
[00:27:47] to see that much data as a 5-year-old.
[00:27:49] You spend most of your time in your
[00:27:50] parents house, so you have very low data
[00:27:52] diversity. But you could say maybe
[00:27:53] that's evolution, too. But then language
[00:27:56] and math and coding, probably not.
[00:28:00] >> It still seems better than models. I
[00:28:02] mean, obviously models are better than
[00:28:04] the average human at language and math
[00:28:05] and coding, but are they better at the
[00:28:07] average human at learning?
[00:28:09] >> Oh, yeah. Oh, yeah. Absolutely. What I
[00:28:11] meant to say is that language math and
[00:28:14] coding and especially math and coding
[00:28:17] suggests that whatever it is that makes
[00:28:19] people
[00:28:21] good at learning
[00:28:22] is probably not so much a complicated
[00:28:25] prior but something more some
[00:28:27] fundamental thing.
[00:28:29] >> Wait, I'm not sure understood. Why
[00:28:30] should that be the case? So consider a
[00:28:33] skill
[00:28:34] that people exhibit some kind of great
[00:28:36] reliability or you know um
[00:28:41] >> if the skill is one that was very useful
[00:28:44] to our ancestors for many millions of
[00:28:46] years, hundreds of millions of years,
[00:28:48] you could say you could argue that maybe
[00:28:52] humans are good at it because of
[00:28:55] evolution because we have a prior
[00:28:58] >> an evolutionary prior that's encoded in
[00:29:01] some very nonobvious way.
[00:29:03] >> Yeah.
[00:29:04] >> That somehow makes us so good at it.
[00:29:06] >> Yeah.
[00:29:07] >> But if people exhibit great ability,
[00:29:11] reliability, robustness, ability to
[00:29:14] learn in a domain that really did not
[00:29:17] exist until recently,
[00:29:19] then this is more an indication that
[00:29:23] people might have [snorts]
[00:29:26] just better machine learning period.
[00:29:28] >> Mhm. But then how should we think about
[00:29:30] what that is? Is it a matter of
[00:29:34] Yeah. What is the ML analogy for what?
[00:29:38] There's a couple interesting things
[00:29:39] about it. It takes fewer samples. It's
[00:29:41] more unsupervised. You don't have to set
[00:29:42] a ver like a child learning to drive a
[00:29:44] car. Children are not learning to drive
[00:29:46] a car. A teenager learning how to drive
[00:29:48] a car is like not exactly getting
[00:29:53] some pre-built verifiable reward.
[00:29:56] it comes from their interaction with the
[00:29:59] machine and the with the environment. Um
[00:30:02] and yet it takes much fewer samples. It
[00:30:04] seems more unsupervised. It seems more
[00:30:06] robust. Much more robust. The robustness
[00:30:09] of people is really staggering.
[00:30:12] >> Yeah. So like Okay. And do you have a
[00:30:14] unified way of thinking about why are
[00:30:16] all these things happening at once? What
[00:30:18] is the ML analogy that would that could
[00:30:21] be could realize something like this?
[00:30:24] So, so, so, um, this is where, you know,
[00:30:26] one of the things that you've been
[00:30:27] asking about is how can, you know, the
[00:30:30] teenage driver kind of self-correct and
[00:30:33] learn from their experience without an
[00:30:36] external teacher.
[00:30:37] >> And the answer is well, they have their
[00:30:39] value function,
[00:30:41] >> right? They have a general sense which
[00:30:43] is also by the way extremely robust in
[00:30:46] people like
[00:30:48] whatever it is the human value function
[00:30:50] whatever the human value function is
[00:30:52] with a few exceptions around addiction
[00:30:56] it's actually very very robust
[00:30:59] and so for something like a teenager
[00:31:00] that's learning to drive they start to
[00:31:03] drive and they already have a sense of
[00:31:06] how they're driving immediately how
[00:31:09] badly they're unconfident and then they
[00:31:11] See? Okay. And they and then of course
[00:31:13] the the learning speed of any teenager
[00:31:15] is so fast after 10 hours you're good to
[00:31:16] go.
[00:31:17] >> Yeah. It seems like humans has some
[00:31:18] solution, but I'm curious about like
[00:31:20] well how are they doing it and like why
[00:31:22] is it so hard to like how do we need to
[00:31:24] reconceptualize the way we're training
[00:31:25] models to make something like this
[00:31:26] possible?
[00:31:27] >> You know that is a great question to ask
[00:31:31] and it's a question I have a lot of
[00:31:34] opinions about.
[00:31:37] But unfortunately
[00:31:39] we live in a world where not not all
[00:31:41] machine learning ideas are discussed
[00:31:43] freely and this is this is one of them.
[00:31:44] So there's probably a way to do it.
[00:31:49] I think it can be done. The fact that
[00:31:51] people are like that I think it's a
[00:31:54] proof that it can be done. There may be
[00:31:56] another blocker though which is there is
[00:31:59] a possibility
[00:32:02] that the human neurons actually do more
[00:32:05] compute than we think. And if that is
[00:32:08] true and if that plays an important role
[00:32:10] then things might be more difficult. But
[00:32:14] regardless I do think it points to the
[00:32:16] existence of some
[00:32:19] machine learning principle
[00:32:21] that I have opinions on. But
[00:32:23] unfortunately, circumstances make it
[00:32:26] hard to to discuss in detail. Even
[00:32:28] though
[00:32:28] >> nobody nobody listens to this podcast,
[00:32:29] Ilia.
[00:32:31] >> Yeah.
[00:32:32] >> So, I have to say that prepping for Ilia
[00:32:34] was pretty tough because neither I nor
[00:32:37] anybody else had any idea what he's
[00:32:39] working on and what SSI is trying to do.
[00:32:41] I had no basis to come up with my
[00:32:43] questions and the only thing I could go
[00:32:45] off honestly was trying to think from
[00:32:48] first principles about what are the
[00:32:49] bottlenecks to hi because clearly Ilia
[00:32:52] is working on them in some way. Part of
[00:32:54] this question involved thinking about RL
[00:32:56] scaling because everybody's asking how
[00:32:58] well RL will generalize and how we can
[00:33:00] make it generalize better. As part of
[00:33:02] this I was reading this paper that came
[00:33:03] out recently on RL scaling and it showed
[00:33:05] that actually the learning curve on RL
[00:33:08] looks like a sigmoid. I found this very
[00:33:10] curious. Why should it be a sigmoid
[00:33:11] where it learns very little for a long
[00:33:14] time and then it quickly learns a lot
[00:33:16] and then it asmmptotes. This is very
[00:33:18] different from the power law you see in
[00:33:19] pre-training where the model learns a
[00:33:21] bunch at the very beginning and then
[00:33:23] less and less over time. And it actually
[00:33:25] reminded me of a note that I had written
[00:33:27] down after I had a conversation with a
[00:33:28] researcher friend where he pointed out
[00:33:30] that the number of samples that you need
[00:33:32] to take in order to find a correct
[00:33:35] answer scales exponentially with how
[00:33:37] different your current probability
[00:33:38] distribution is from the target
[00:33:40] probability distribution. And I was
[00:33:42] thinking about how these two ideas are
[00:33:43] related. I had this vague idea that they
[00:33:45] should be connected, but I really didn't
[00:33:46] know how. I don't have a math
[00:33:48] background, so I couldn't really
[00:33:49] formalize it. But I wondered if Gemini 3
[00:33:52] could help me out here. And so I took a
[00:33:53] picture of my notebook and I took the
[00:33:55] paper and I put them both in the context
[00:33:57] of Gemini 3 and I asked it to find the
[00:33:59] connection. And it thought a bunch and
[00:34:02] then it [music] realized that the
[00:34:03] correct way to model the information you
[00:34:06] gain from a single yes or no outcome in
[00:34:08] RL is as the entropy of a random binary
[00:34:11] variable. It made a graph which showed
[00:34:14] how the bits you gain for a sample in RL
[00:34:17] versus supervised learning scale as a
[00:34:19] pass rate increases. And as soon as I
[00:34:21] saw the graph that Gemini 3 made,
[00:34:23] immediately a ton of things started
[00:34:24] making sense to me. Then I wanted to see
[00:34:26] if there was any empirical basis to this
[00:34:28] theory. So I asked Gemini to code my
[00:34:30] experiment to show whether [music] the
[00:34:33] improvement in loss scales in this way
[00:34:35] with pass rate. I just took the code
[00:34:37] that Gemini outputed. I copy pasted it
[00:34:39] into a Google Collab notebook and I was
[00:34:41] able to run this toy ML experiment and
[00:34:44] visualize its results without a single
[00:34:46] bug. It's interesting because the
[00:34:47] results look similar but not identical
[00:34:50] to what we should have expected. And so
[00:34:51] I downloaded this chart and I put it
[00:34:53] into Gemini and I asked it what is going
[00:34:55] on here. I came up with a hypothesis
[00:34:56] that I think is actually correct which
[00:34:58] is that we're capping how much
[00:34:59] supervised learning can improve in the
[00:35:02] beginning by having a fixed learning
[00:35:04] rate and in fact we should decrease the
[00:35:05] learning rate over time. It actually
[00:35:06] gives us an intuitive understanding for
[00:35:08] why in practice we have learning rate
[00:35:11] schedulers that decrease the learning
[00:35:13] rate over time. I did this entire flow
[00:35:15] from coming up with this vague initial
[00:35:17] question to building a theoretical
[00:35:20] understanding to running some toy ML
[00:35:22] experiments all with Gemini 3. This
[00:35:24] feels like the first model where it can
[00:35:26] actually come up with new connections
[00:35:28] that I wouldn't have anticipated. It's
[00:35:30] actually now become the default place I
[00:35:31] go to when I want to brainstorm new ways
[00:35:34] to think about a problem. If you want to
[00:35:36] read more about RL scaling, you can
[00:35:37] check out the blog post that I wrote
[00:35:38] with a little help from Gemini 3. And if
[00:35:41] you want to check out Gemini 3 yourself,
[00:35:42] go [music] to gemini.google.
[00:35:45] I am curious if you say we are back in
[00:35:47] an era of research.
[00:35:49] You were there from 2012 to 2020
[00:35:53] and do do you have Yeah. What what is
[00:35:56] now the vibe going to be if we go back
[00:35:58] to the era of research? For example,
[00:36:02] even after Alexet, the amount of compute
[00:36:05] that was used to run experiments kept
[00:36:07] increasing and the size of frontier
[00:36:09] systems kept increasing.
[00:36:12] And do you think now that this era of
[00:36:15] research will still require tremendous
[00:36:17] amounts of compute? Um, do you think it
[00:36:20] will require going back into the
[00:36:22] archives and reading old papers? What is
[00:36:26] maybe what was the vibe of like you were
[00:36:28] at Google and um OpenAI and Stanford
[00:36:31] these places when there was like a more
[00:36:33] of a vibe of research. What what kind of
[00:36:35] thing should we be expecting in the
[00:36:37] community?
[00:36:38] >> So one consequence of um the age of
[00:36:42] scaling is that there was this
[00:36:47] um scaling sucked out all the air in the
[00:36:49] room.
[00:36:49] >> Yeah.
[00:36:51] And so
[00:36:53] because scaling sucked out all the air
[00:36:54] in the room,
[00:36:57] everyone started to do the same thing.
[00:36:59] We got to the point where
[00:37:02] uh we are in a world where there are
[00:37:05] more companies than ideas by quite a
[00:37:07] bit.
[00:37:08] >> Actually on that you know there is this
[00:37:11] Silicon Valley saying that says that
[00:37:14] ideas are cheap, execution is everything
[00:37:18] and people say that a lot.
[00:37:19] >> Yeah. And there is truth to that. But
[00:37:21] then I saw I saw someone say on Twitter
[00:37:24] um something like if ideas are are so
[00:37:28] cheap, how come no one's having any
[00:37:29] ideas?
[00:37:30] >> And I think it's true too. I think like
[00:37:34] if you think about um research progress
[00:37:37] in terms of bottlenecks,
[00:37:40] there are several bottlenecks. If you go
[00:37:42] back to the if if you and um one of them
[00:37:44] is ideas and one of them is your ability
[00:37:47] to bring them to life.
[00:37:48] >> Yeah. which might be compute but also
[00:37:50] engineering.
[00:37:52] So if you go back to the '9s let's say
[00:37:54] you had people who had had pretty good
[00:37:55] ideas and if they had much larger
[00:37:58] computers maybe they could demonstrate
[00:37:59] that their ideas were viable but they
[00:38:01] could not. So they could only have very
[00:38:04] very small demonstration that did not
[00:38:05] convince anyone.
[00:38:06] >> Yeah.
[00:38:07] >> So the bottleneck was compute. Then in
[00:38:10] the age of scaling computers increased a
[00:38:13] lot and of course there is a question of
[00:38:16] how much comput is needed but compute is
[00:38:19] large so compute is large enough such
[00:38:24] that
[00:38:25] it's like not obvious that you need that
[00:38:28] much more compute to prove some idea
[00:38:32] like I'll give you an analogy. Alexet
[00:38:35] was built on two GPUs. That was the
[00:38:38] total amount of compute used for it. The
[00:38:40] transformer
[00:38:43] was built on 8 to 64 GPUs. No single
[00:38:46] transformer paper experiment used more
[00:38:48] than 64 GPUs of 2017 which would be like
[00:38:52] what two GPUs of today. So the ResNet
[00:38:57] right many like even even the the um you
[00:39:00] could argue that the like 01
[00:39:04] reasoning was not the most comput heavy
[00:39:06] thing in the world. So there definitely
[00:39:10] for for research
[00:39:13] you need like definitely some amount of
[00:39:15] compute but it's far from obvious that
[00:39:18] you need the absolutely largest amount
[00:39:20] of compute ever for research. H
[00:39:22] >> you might argue and I think it is true
[00:39:24] that if you want to build the absolutely
[00:39:26] best system, if you want to build the
[00:39:29] absolutely best system, then it helps to
[00:39:32] have much more compute and especially if
[00:39:34] everyone is within the same paradigm,
[00:39:37] then compute becomes one of the big
[00:39:39] differentiators.
[00:39:42] >> Yeah, I guess while it was possible to
[00:39:44] develop these ideas, I'm asking you for
[00:39:47] the history because you were actually
[00:39:48] there. I'm not sure what actually
[00:39:49] happened, but it sounds like it was
[00:39:50] possible to develop these ideas using
[00:39:53] minimal amounts of compute, but it
[00:39:55] wasn't the transformer didn't
[00:39:56] immediately become famous. It became the
[00:39:58] thing everybody started doing and then
[00:40:00] started experimenting on top of and
[00:40:01] building on top of because it was
[00:40:03] validated at higher and higher levels of
[00:40:05] compute.
[00:40:06] >> Correct. And if you at SSI have 50
[00:40:09] different ideas, how will you know which
[00:40:12] one is the next transformer and which
[00:40:14] one is you know brittle without having
[00:40:19] the kinds of compute that other frontier
[00:40:21] labs have. So I can I can comment on
[00:40:23] that which is
[00:40:26] the short comment is that you know you
[00:40:28] mentioned SSI specifically for us
[00:40:33] the amount of compute that SSI has for
[00:40:36] research is really not that small and I
[00:40:41] want to explain why like a simple math
[00:40:43] can explain why the amount of compute
[00:40:45] that we have is actually a lot more
[00:40:46] comparable for research than one might
[00:40:49] think. And I'll explain. So
[00:40:55] SSI has raised $3 billion which is like
[00:41:00] not small by it's like a lot by any
[00:41:03] absolute sense but you could say but
[00:41:05] look at the other companies raising
[00:41:06] >> much more
[00:41:08] but a lot of what their a lot of their
[00:41:10] compute goes for inference
[00:41:13] like these big numbers these big loans
[00:41:16] it's earmarked for inference. That's
[00:41:18] number one. Number two, you need if you
[00:41:22] want to have a product on which you do
[00:41:24] inference, you need to have a big staff
[00:41:26] of engineers of salespeople. A lot of
[00:41:29] the research needs to be dedicated for
[00:41:31] producing all kinds of product related
[00:41:34] features. So then when you look at
[00:41:36] what's actually left for research, the
[00:41:38] difference becomes a lot smaller.
[00:41:42] Now the other thing is is that if you
[00:41:44] are doing something different do you
[00:41:47] really need the absolute maximal scale
[00:41:49] to prove it? I don't think it's true at
[00:41:52] all. I think that in our case we have
[00:41:57] sufficient compute to prove to convince
[00:41:59] ourselves and anyone else that what
[00:42:01] we're doing is correct.
[00:42:02] There's been public estimates that you
[00:42:04] know companies like OpenAI spend on the
[00:42:06] order of56
[00:42:07] billion dollars a year even just so far
[00:42:10] on experiments.
[00:42:12] >> This is separate from the amount of
[00:42:13] money they're spending on inference and
[00:42:15] so forth. So seems like they're spending
[00:42:17] more a year running exper like research
[00:42:20] experiments than you guys have in total
[00:42:22] funding.
[00:42:22] >> I think it's a question of what you do
[00:42:24] with it. It's a question of what you do
[00:42:26] with it. like they have a like the more
[00:42:29] I think in in in their case in the case
[00:42:31] of others I think there's a lot more
[00:42:32] demand on the training compute there's a
[00:42:35] lot more different work streams there is
[00:42:38] there are different modalities there is
[00:42:40] just more stuff and so it becomes
[00:42:42] fragmented
[00:42:44] >> how will SSI make money
[00:42:46] >> you know
[00:42:48] my answer to this question is something
[00:42:50] like
[00:42:52] we just f right now we just focus on the
[00:42:54] research and then the answer to that
[00:42:56] will reveal itself. I think there will
[00:42:59] be lots of possible answers.
[00:43:01] >> Is SSI's plan still to straightshot
[00:43:03] super intelligence?
[00:43:05] >> Maybe.
[00:43:06] I think that there is merit to it.
[00:43:09] >> I think there's a lot of merit because I
[00:43:11] think that it's very nice to not be
[00:43:13] affected by the day-to-day market
[00:43:15] competition.
[00:43:17] But I think there are two reasons that
[00:43:22] may cause us to change the plan. one is
[00:43:25] pragmatic if timelines turn out to be
[00:43:28] long
[00:43:29] which they might and second I think
[00:43:32] there is a lot of value in the best and
[00:43:38] most powerful AI being out there
[00:43:41] impacting the world
[00:43:43] >> I think this is a meaningfully valuable
[00:43:45] thing
[00:43:46] >> but then so why is your default plan to
[00:43:48] straight shot super intelligence because
[00:43:50] it sounds like you know openai anthropic
[00:43:52] all these other companies their explicit
[00:43:54] thinking is look we have weaker and
[00:43:55] weaker intelligences that the public can
[00:43:58] get used to and prepare for and why is
[00:44:01] it potentially better to build a super
[00:44:04] intelligence directly
[00:44:06] >> so I'll make the case for and against
[00:44:08] >> the case for is that you are so one of
[00:44:11] the challenges
[00:44:14] that people face when they're in the
[00:44:15] market is that they have to participate
[00:44:18] in the rat race and the rat race is
[00:44:21] quite difficult in that it exposes you
[00:44:23] to to to difficult trade-offs which you
[00:44:25] need to make
[00:44:27] and there is it is it is nice to say
[00:44:30] we'll insulate ourselves from all this
[00:44:32] and just focus on the research and come
[00:44:35] out only when we are ready and not
[00:44:36] before but the counterpoint is valid too
[00:44:40] and those those are opposing forces the
[00:44:43] counterpoint is hey it is useful for the
[00:44:47] world to see powerful AI it is useful
[00:44:51] for the world to see powerful AI because
[00:44:53] that's the only way you and communicate
[00:44:54] it.
[00:44:55] >> Well, I guess not even just that you can
[00:44:56] communicate the idea, but
[00:44:58] >> communicate the AI, not the idea.
[00:45:01] Communicate the AI.
[00:45:02] >> What do you mean communicate the AI?
[00:45:04] >> So, okay. So, let's suppose you read an
[00:45:05] essay about AI
[00:45:07] >> and the essay says AI is going to be
[00:45:09] this and AI is going to be that and it's
[00:45:10] going to be this
[00:45:12] >> and you read it and you say, okay, this
[00:45:14] is an interesting essay
[00:45:15] >> right
[00:45:15] >> now. Suppose you see an AI doing this
[00:45:18] and AI doing that.
[00:45:20] >> It is incomparable. Like basically I
[00:45:23] think I think that there is a big
[00:45:26] benefit from AI being in the public and
[00:45:30] that would be a reason for us to not be
[00:45:34] quite straight shot.
[00:45:35] >> Yeah. Well, I guess it's not even that
[00:45:37] which I but I do think that is an
[00:45:39] important part of it. The other big
[00:45:41] thing is I can't think of another
[00:45:43] discipline in human engineering and
[00:45:45] research where
[00:45:47] the end artifact was made safer
[00:45:51] mostly through just thinking about how
[00:45:53] to make it safe as opposed to why are
[00:45:56] airplane crashes per mile so much lower
[00:45:58] today than they were decades ago? Why is
[00:46:00] it so much harder to find a bug in Linux
[00:46:02] than it would have been decades ago? And
[00:46:05] I think it's mostly because these
[00:46:06] systems were deployed to the world. you
[00:46:08] noticed failures, those failures were
[00:46:11] corrected and the systems became more
[00:46:12] robust. Now, I'm not sure why AGI and
[00:46:16] superhuman intelligence would be any
[00:46:17] different, especially given, and I hope
[00:46:19] we can talk, we're going to get to this.
[00:46:23] It seems like the harms of super
[00:46:25] intelligence are not just about like
[00:46:27] having some malevolent uh paper clipper
[00:46:29] out there, but it just like this is a
[00:46:31] really powerful thing and we don't even
[00:46:32] know how to conceptualize how people
[00:46:34] interact with it, what people will do
[00:46:35] with it and having gradual access to it
[00:46:38] seems like a um better way to maybe
[00:46:41] spread out the impact of it and to help
[00:46:44] people prepare for it. Well, I think I
[00:46:46] think on this point even in the straight
[00:46:49] shot scenario, you would still do a
[00:46:52] gradual release of it is how I would
[00:46:55] imagine it.
[00:46:57] The the gra gradualism would be an
[00:47:00] inherent inherent component of any plan.
[00:47:03] It's just a question of what is the
[00:47:04] first thing that you get out of the
[00:47:05] door. That's number one. Number two, I
[00:47:07] also think you know I believe you have
[00:47:11] advocated for continual learning more
[00:47:12] than other people
[00:47:14] >> and I actually think that this is an
[00:47:16] important and correct thing and here is
[00:47:19] why
[00:47:21] so one of the things so I'll give you
[00:47:24] another example of how thinking how
[00:47:27] language affects thinking and in this
[00:47:30] case it will be two words two words that
[00:47:33] have shaped everyone's thinking I
[00:47:35] maintain
[00:47:37] F first word AGI
[00:47:40] second word pre-training let me explain.
[00:47:44] So the word the term AGI,
[00:47:47] why does this term exist? It's a very
[00:47:50] particular term. Why does it exist?
[00:47:52] There's a reason.
[00:47:54] The reason that the term AGI exists is
[00:47:58] in my opinion not so much because it's
[00:48:00] like a very important essential
[00:48:02] descriptor of of of some end state of
[00:48:05] intelligence but
[00:48:09] because it is a reaction to a different
[00:48:13] term that existed and the term is narrow
[00:48:16] AI. If you go back to ancient history of
[00:48:20] gameplay AI, of checkers AI, chess AI,
[00:48:23] computer games AI, everyone would say,
[00:48:25] look at this narrow intelligence. Sure,
[00:48:28] the chess AI can beat Casper off, but it
[00:48:29] can't do anything else. It is so narrow,
[00:48:32] artificial narrow intelligence. So in
[00:48:35] response, as a reaction to this, some
[00:48:38] people said, well, this is not good. It
[00:48:41] is so narrow. What we need is general
[00:48:44] AI.
[00:48:46] general AI, an AI that can just do all
[00:48:48] the things.
[00:48:50] The second and and that term just got a
[00:48:54] lot of traction.
[00:48:55] >> Yeah.
[00:48:57] >> The second thing that got a lot of
[00:48:58] traction is pre-training.
[00:49:01] Specifically, the recipe of
[00:49:02] pre-training. I think the current the
[00:49:04] way people do RL now is maybe um un is
[00:49:09] undoing the conceptual imprint of
[00:49:11] pre-training. But pre-training had the
[00:49:14] property. you do more pre-training and
[00:49:16] the model gets better at everything more
[00:49:19] or less uniformly. Yeah,
[00:49:21] >> general AI pre-training gives AGI
[00:49:27] but
[00:49:29] the thing that happened with AGI and
[00:49:32] pre-training is that in some sense they
[00:49:34] overshock the target
[00:49:36] because by the kind if you think about
[00:49:38] the term AGI you will realize and
[00:49:41] especially in the context of
[00:49:42] pre-training you will realize that a
[00:49:44] human being is not an AGI
[00:49:48] because a human being Yes, there is
[00:49:50] definitely a foundation of skills.
[00:49:53] A human being,
[00:49:56] a human being lacks a huge amount of
[00:49:59] knowledge. Instead, we rely on continual
[00:50:02] learning. We rely on continual learning.
[00:50:05] And so then when you think about okay,
[00:50:06] so let's suppose that we achieve success
[00:50:08] and we produce a safe super some kind of
[00:50:10] safe super intelligence. The question is
[00:50:13] but how do you define it? Where on the
[00:50:15] curve of continual learning is it going
[00:50:17] to be? I produce like um a super
[00:50:20] intelligent 15 year old that's very
[00:50:21] eager to go and you say okay I'm going
[00:50:23] to they don't know very much at all the
[00:50:25] great student very eager you go and be a
[00:50:28] programmer you go and be a doctor
[00:50:31] go and learn so you could imagine that
[00:50:34] the deployment itself will involve some
[00:50:35] kind of a learning trial and error
[00:50:37] period
[00:50:38] >> it's a process as opposed to you drop
[00:50:42] the finished thing
[00:50:43] >> okay I I I I see so you're you're
[00:50:45] suggesting
[00:50:47] that the thing you're pointing out with
[00:50:49] super intelligence
[00:50:51] is not some finished
[00:50:55] mind which knows how to do every single
[00:50:57] job in the economy cuz the way say the
[00:51:00] original I think openi charter or
[00:51:02] whatever defines AGI is like it can do
[00:51:04] every single job that a every single
[00:51:06] thing a human can do. You're proposing
[00:51:08] instead a mind which can learn to do any
[00:51:12] single every single job.
[00:51:13] >> Yes.
[00:51:14] >> And that is super intelligence. And then
[00:51:16] but once you have the learning
[00:51:17] algorithm,
[00:51:19] it gets deployed into the world the same
[00:51:21] way a human laborer might join an
[00:51:23] organization.
[00:51:25] >> And it seems like one of these two
[00:51:27] things might happen. Maybe neither of
[00:51:28] these happens. One, this super efficient
[00:51:33] learning algorithm
[00:51:35] becomes superhuman becomes as good as
[00:51:38] you and potentially even better at the
[00:51:41] task of ML research. And as a result the
[00:51:45] algorithm itself becomes more and more
[00:51:47] superhuman. The other is even if that
[00:51:49] doesn't happen if you have a single
[00:51:51] model I mean this this is explicitly
[00:51:53] your vision. If you have a single model
[00:51:54] or instances of a model which are
[00:51:57] deployed through the economy doing
[00:51:59] different jobs learning how to do those
[00:52:00] jobs continually learning on the job
[00:52:03] picking up all the skills that any human
[00:52:05] could pick up but actually picking them
[00:52:06] all up at the same time and then
[00:52:07] amalgamating the learnings.
[00:52:10] you basically have a model which
[00:52:11] functionally becomes super intelligent
[00:52:14] even without any sort of recursive
[00:52:16] self-improvement in software right
[00:52:19] because you now have one model that can
[00:52:20] do every single job in the economy and
[00:52:22] humans can't merge our minds in the same
[00:52:24] way and so do you expect some sort of
[00:52:26] like intelligence explosion from broad
[00:52:27] deployment
[00:52:28] >> I think that it is likely that we will
[00:52:33] have rapid economic growth
[00:52:37] I think the broad deployment And
[00:52:40] like there are two arguments you could
[00:52:43] make which are conflicting.
[00:52:46] One is that look if indeed you get once
[00:52:49] indeed you get to a point where you have
[00:52:53] an AI that can learn to do
[00:52:57] things quickly
[00:52:59] and you have many of them then they will
[00:53:02] then there will be a strong force to
[00:53:05] deploy them in the economy. Unless there
[00:53:07] will be some kind of a regulation that
[00:53:09] stops it, which by the way there might
[00:53:12] be. But I think the idea of very rapid
[00:53:17] economic growth for some time, I think
[00:53:19] it's very possible from broad
[00:53:20] deployment. The other question is how
[00:53:22] rapid it's going to be.
[00:53:25] So I think this is hard to know because
[00:53:27] on the one hand you have this very
[00:53:29] efficient worker. on the other hand
[00:53:31] there is the world is just really big
[00:53:33] and there's a lot of stuff
[00:53:36] and that stuff moves at a different
[00:53:38] speed but then on the other hand now the
[00:53:40] AI could you know so I think very rapid
[00:53:43] economic growth is possible and we will
[00:53:44] see like all kinds of things like
[00:53:47] different countries with different rules
[00:53:49] and the ones which have the friendlier
[00:53:50] rules the economic growth will be faster
[00:53:53] hard to predict
[00:53:54] >> some people in our audience like to read
[00:53:56] the transcripts instead of listening to
[00:53:57] the episode and so we put a ton of
[00:53:59] effort into making the transcripts read
[00:54:02] like they are standalone essays. The
[00:54:04] problem is that if you just transcribe a
[00:54:06] conversation verbatim using a speech to
[00:54:08] text model, it'll be full of all kinds
[00:54:11] of fits and starts and confusing
[00:54:13] phrasing. We mentioned this problem to
[00:54:14] Labelbox and they asked if they could
[00:54:16] take a stab. Working with them on this
[00:54:18] is probably the reason that I'm most
[00:54:19] excited to recommend Labelbox to people.
[00:54:22] It wasn't just, oh, hey, tell us what
[00:54:23] kind of data you need and we'll go get
[00:54:25] it. They walked us through the entire
[00:54:26] process from helping us identify what
[00:54:28] kind of data we needed in the first
[00:54:30] place to assembling a team of expert
[00:54:33] aligners to generate it. Even after we
[00:54:35] got all the data back, Labelbox stayed
[00:54:37] involved. They helped us choose the
[00:54:39] right base model and set up auto QA on
[00:54:42] the model's output so that we could
[00:54:43] tweak and refine it. And now we have a
[00:54:45] new transcriber tool that we can use for
[00:54:47] all our episodes moving forward. This is
[00:54:49] just one example of how Labelbox meets
[00:54:52] their customers at the ideas level and
[00:54:54] partners with them through their entire
[00:54:56] journey. If you want to learn more or if
[00:54:58] you want to try out the transcriber tool
[00:55:00] yourself, go to labelbox.com/barcash.
[00:55:07] It seems to me that this is a very
[00:55:09] precarious situation to be in where
[00:55:13] looking the limit we know that this
[00:55:14] should be possible because if you have
[00:55:16] something that is as good as a human at
[00:55:18] learning but which can merge its brains
[00:55:22] merge there are different instances in a
[00:55:24] way that humans can't merge already.
[00:55:26] This seems like a thing that should
[00:55:27] physically be possible. Humans are
[00:55:28] possible, digital computers are
[00:55:30] possible. You just need both of those
[00:55:31] combined to produce this thing. And it
[00:55:33] also seems like this kind of thing is
[00:55:36] extremely um powerful
[00:55:40] and economic growth is one way to put
[00:55:43] it. Um I mean Dyson spear is a lot of
[00:55:44] economic growth but another way to put
[00:55:46] it is just like you will have
[00:55:48] potentially a very short period of time
[00:55:50] because a human on the job can you know
[00:55:52] you you're hiring people at SSI in six
[00:55:53] months they're like net productive
[00:55:54] probably right um a human like learns
[00:55:57] really fast and so this thing is
[00:55:58] becoming smarter and smarter very fast
[00:56:00] what is how do you think about making
[00:56:02] that go well and why is SSI positioned
[00:56:04] to do that well or what is SSI's plan
[00:56:06] there basically is what I'm trying to
[00:56:07] ask
[00:56:08] >> yeah
[00:56:10] so one of the one of the ways in which
[00:56:14] my thinking has been changing is that
[00:56:19] I now place more importance on AI
[00:56:24] being
[00:56:26] deployed
[00:56:27] incrementally and in advance. One very
[00:56:31] difficult thing about AI is that we are
[00:56:34] talking about systems that don't yet
[00:56:38] exist
[00:56:40] and it's hard to imagine them.
[00:56:43] I think that one of the things that's
[00:56:45] happening is that in practice it's very
[00:56:49] hard to feel the AGI.
[00:56:52] It's very hard to feel the AGI.
[00:56:54] We can talk about it, but it's like it's
[00:56:58] like talking about like the long f like
[00:57:00] imagine like having a conversation about
[00:57:02] like how is it like to be old when
[00:57:04] you're like old and and frail and you
[00:57:08] can have a conversation. You can try to
[00:57:09] imagine it, but it's just hard and you
[00:57:12] come back to reality. Well, that's not
[00:57:14] the case. And I think that a lot of the
[00:57:18] issues around
[00:57:21] AGI and its future power stem from the
[00:57:26] fact that it's very difficult to imagine
[00:57:30] future AI is going to be diff different.
[00:57:34] It's going to be powerful. Indeed, the
[00:57:36] whole problem, what is the problem of AI
[00:57:38] and AGI? The whole problem is the power.
[00:57:43] The whole problem is the power.
[00:57:46] When the power is really big, what's
[00:57:48] going to happen?
[00:57:50] And one of the one of the ways in which
[00:57:52] I've changed my mind over the past year
[00:57:54] and so that that change of mind may back
[00:57:59] may I'll say I I'll I'll hedge a little
[00:58:01] bit may back propagate into into the
[00:58:03] plans of our of our company is that
[00:58:08] so if it's hard to imagine
[00:58:12] what do you do you got to be showing the
[00:58:13] thing you got to be showing the thing
[00:58:16] and I maintain that I think I think most
[00:58:18] people who work Con AI also can't
[00:58:21] imagine it because it's too different
[00:58:24] from what people see on a day-to-day
[00:58:26] basis.
[00:58:28] I do maintain here is something which I
[00:58:31] predict will happen. That's a
[00:58:33] prediction.
[00:58:34] I maintain
[00:58:36] that as AI becomes more powerful
[00:58:40] then people will change their behaviors
[00:58:45] and we will see all kinds of
[00:58:47] unprecedented things which are not
[00:58:49] happening right now and I'll give some
[00:58:52] examples. I do like I I think I think
[00:58:55] for better or worse the the frontier
[00:58:58] companies will play a very important
[00:58:59] role in what happens as will the
[00:59:01] government and the kind of things that I
[00:59:04] think we'll see which you see the
[00:59:06] beginnings of
[00:59:08] companies that are fierce competitors
[00:59:11] starting collaborate to to collaborate
[00:59:14] on AI safety you may have seen open AI
[00:59:17] and anthropic event doing a first small
[00:59:20] step but that did not exist That's
[00:59:23] actually something which I predicted in
[00:59:24] one of my talks about three years ago
[00:59:27] that such a thing will happen. I also
[00:59:29] maintain that as AI continues to become
[00:59:31] more powerful, more visibly powerful,
[00:59:36] there will also be a desire from
[00:59:38] governments and the public to do
[00:59:40] something
[00:59:42] and I think that this is a very
[00:59:43] important force
[00:59:46] of showing the AI. That's number one.
[00:59:49] Number two, okay, so then the AI is
[00:59:51] being built. what needs to what needs to
[00:59:53] be done.
[00:59:55] So one thing that I maintain that will
[00:59:57] happen is that right now people who are
[01:00:00] working on AI I maintain that the AI
[01:00:03] doesn't feel powerful because of its
[01:00:04] mistakes.
[01:00:06] I do think that at some point the AI
[01:00:08] will start to feel powerful actually and
[01:00:10] I think when that happens we will see a
[01:00:12] big change in the way
[01:00:15] all AI companies approach safety.
[01:00:19] they'll become much more paranoid. I
[01:00:22] think I I say this as a predict as a as
[01:00:24] a as a prediction that we will see
[01:00:25] happen. We'll see if I'm right, but I
[01:00:28] think this is something that will happen
[01:00:29] because they will see the AI becoming
[01:00:31] more powerful. Everything that's
[01:00:33] happening right now, I maintain is
[01:00:35] because people look at today's AI and
[01:00:38] it's hard to imagine the future AI.
[01:00:42] And there is a third thing which needs
[01:00:44] to happen. And I think this is this this
[01:00:46] and I'm talking about it in in broader
[01:00:48] terms not just from the perspective of
[01:00:51] SSI
[01:00:52] because you ask me about our company but
[01:00:54] the question is okay so then what should
[01:00:56] what should the companies aspire to
[01:00:57] build
[01:00:58] >> what should they aspire to build and
[01:01:00] there has been one big idea that
[01:01:02] actually every that um everyone has been
[01:01:04] locked in locked into which is the the
[01:01:07] self-improving AI
[01:01:09] and why why did it happen because there
[01:01:11] is fewer ideas than companies
[01:01:14] But I maintain that there is something
[01:01:16] that's better to build and I think that
[01:01:19] everyone will actually want that. It's
[01:01:21] like the AI that's robustly aligned to
[01:01:26] care about sentient life specifically.
[01:01:29] I think in particular it will be there's
[01:01:32] a case to be made that it will be easier
[01:01:34] to build an AI that cares about sentient
[01:01:37] life than an AI that cares about human
[01:01:39] life alone because the AI itself will be
[01:01:42] sentient.
[01:01:44] And if you think about things like
[01:01:45] mirror neurons and human empathy for
[01:01:48] animals which is you know you might
[01:01:49] argue it's not big enough but it exists.
[01:01:53] I think it's an emerging property from
[01:01:54] the fact that we model others with the
[01:01:58] same circuit that we used to model
[01:02:00] ourselves because that's the most
[01:02:01] efficient thing to do.
[01:02:03] >> So even if you got an AI to care about
[01:02:06] sentient beings and it's not actually
[01:02:08] clear to me that that's what you should
[01:02:09] try to do if you solved alignment. It
[01:02:12] would still be the case that most
[01:02:14] sentient beings will be AIS. There will
[01:02:16] be trillions eventually quadrillions of
[01:02:18] AIs. Humans will be a very small
[01:02:20] fraction of sentient beings.
[01:02:23] So, it's not clear to me if the goal is
[01:02:26] some kind of human control over
[01:02:29] this future civilization
[01:02:32] that this is the best criterion.
[01:02:35] >> It's true. I I think that
[01:02:38] it's possible it's not the best
[01:02:40] criterion. I'll say two things. I think
[01:02:43] that thing number one
[01:02:47] I think that if there so
[01:02:50] I think that care for sentient life I
[01:02:52] think there is merit to it. I think it
[01:02:54] should be considered. I think that it
[01:02:56] will be helpful if there was some kind
[01:02:59] of a
[01:03:00] short list of ideas that then the
[01:03:05] companies when they are in this
[01:03:07] situation could use. That's number two.
[01:03:10] Number three, I think it would be really
[01:03:12] materially helpful if the power of the
[01:03:16] most powerful super intelligence was
[01:03:18] somehow capped
[01:03:20] because it would address a lot of these
[01:03:21] concerns.
[01:03:23] The question of how to do it, I'm not
[01:03:26] sure, but I think that would be
[01:03:27] materially helpful when you're talking
[01:03:29] about really really powerful systems.
[01:03:32] >> Yeah. Um, before we continue the element
[01:03:34] discussion, I I want to double click on
[01:03:36] that. How much room is there at the top?
[01:03:38] How do you think about super
[01:03:39] intelligence? Do you think I mean using
[01:03:42] this learning efficiency idea maybe is
[01:03:44] just extremely fast at learning new
[01:03:47] skills or new knowledge and does it just
[01:03:49] have a bigger pool of strategies? Is
[01:03:51] there a single cohesive it in the center
[01:03:54] that's more powerful or bigger? And if
[01:03:57] so,
[01:03:59] do you do you imagine that this will be
[01:04:01] sort of godlike in comparison to the
[01:04:02] rest of human civilization? or does it
[01:04:04] just feel like another agent or another
[01:04:06] cluster of agents?
[01:04:08] >> So this is an area where different
[01:04:10] people have different intuitions.
[01:04:11] >> I think it will be very powerful for
[01:04:13] sure. I think that what I think is most
[01:04:17] likely to happen
[01:04:19] is that there will be multiple
[01:04:22] such AIS being created roughly at the
[01:04:26] same time.
[01:04:27] I think that
[01:04:29] if the cluster is big enough, like if
[01:04:33] the cluster is literally continent
[01:04:35] sized, that thing could be really
[01:04:37] powerful indeed, right? If you literally
[01:04:39] have a continentsized cluster, like
[01:04:42] those those AIs can be very powerful.
[01:04:44] And I like all I can tell you is that if
[01:04:49] you're talking about extremely powerful
[01:04:51] AIs, like truly dramatically powerful,
[01:04:53] then yeah, it would be nice if they
[01:04:55] could be restrained in some ways or if
[01:04:59] there was some kind of an agreement or
[01:05:01] something
[01:05:03] because I think that if you are saying
[01:05:05] hey like if if you really like what what
[01:05:08] is the the concern of super
[01:05:10] intelligence? What is one way to explain
[01:05:12] the concern? If you imagine a system
[01:05:14] that is sufficiently powerful, like
[01:05:17] really sufficiently powerful, and you
[01:05:20] could say, okay, you need to do
[01:05:22] something sensible like care for
[01:05:23] sentient life, let's say, in a very
[01:05:25] single-minded way, we might not like the
[01:05:28] results. That's really what it is. And
[01:05:30] so maybe, by the way, the answer is that
[01:05:32] you do not build a single you do not
[01:05:34] build an RL agent in the usual sense.
[01:05:36] And actually, I'll point I'll point
[01:05:38] several things out. I think human beings
[01:05:40] are a semi agent. You know, we pursue a
[01:05:44] reward and then the emotions or whatever
[01:05:47] make us tire out of the reward. We
[01:05:48] pursue a different reward.
[01:05:50] The market is like kind it's like a very
[01:05:53] shortsighted
[01:05:55] kind of agent. Evolution is the same.
[01:05:57] Evolution is very intelligent in some
[01:05:59] ways but very dumb in other ways. The
[01:06:01] government has been designed to be a
[01:06:04] never- ending fight between three parts
[01:06:06] which has an effect. So I think things
[01:06:09] like this
[01:06:11] another thing that makes this discussion
[01:06:13] difficult is that we are talking about
[01:06:15] systems that don't exist that we don't
[01:06:17] know how to build
[01:06:19] right that's the other thing and that's
[01:06:21] actually my belief I think what people
[01:06:22] are doing right now will go some
[01:06:24] distance and then peter out it will
[01:06:26] continue to improve but it will also not
[01:06:28] be it so the it we don't know how to
[01:06:32] build and I think that a lot h a lot
[01:06:35] hinges on
[01:06:37] understanding and in reliable
[01:06:38] generalization
[01:06:41] and I'll say another thing which is like
[01:06:45] you know one of the things that you
[01:06:46] could say is that cause alignment to be
[01:06:48] difficult is that human val that it's
[01:06:51] it's um
[01:06:53] your ability to learn human values is
[01:06:54] fragile then your ability to optimize
[01:06:57] them is fragile will you actually learn
[01:06:58] to optimize them and then can't you say
[01:07:01] are these not all instances of
[01:07:02] unreliable generalization
[01:07:06] why is it that human beings appear to
[01:07:08] generalize so much better. What if
[01:07:10] generalization was much better? What
[01:07:11] would happen in this case? What would be
[01:07:13] the effect? But those we can't we can't
[01:07:15] like those questions are right now still
[01:07:17] unanswerable.
[01:07:18] >> Um how [clears throat] does one think
[01:07:20] about what AI going well looks like
[01:07:24] because I think you've scoped out how AI
[01:07:26] might evolve. We'll have these sort of
[01:07:28] continual learning agents. AI will be
[01:07:30] very powerful. Maybe there will be many
[01:07:32] different AIs. How do you think about
[01:07:34] lots of continent computes size
[01:07:37] intelligences going around? How
[01:07:40] dangerous is that? How do we make that
[01:07:43] less dangerous? And how do we do that in
[01:07:46] a way that
[01:07:48] protects a equilibrium where there might
[01:07:51] be misaligned AIs out there and bad
[01:07:54] actors out there? So, one reason why I
[01:07:57] liked the AI that cares for sentient
[01:07:59] life,
[01:08:00] >> you know, and we can debate on whether
[01:08:01] it's good or bad, but
[01:08:04] if the first N of these dramatic systems
[01:08:10] actually do care for, you know,
[01:08:14] love humanity or something, you know,
[01:08:16] care for sentient life. Obviously, this
[01:08:18] also needs to be achieved. This needs to
[01:08:20] be achieved.
[01:08:22] So if this is achieved by the first n of
[01:08:24] those systems
[01:08:27] then then I can see it go well at least
[01:08:31] for quite some time and then there is
[01:08:33] the question of what happens in the long
[01:08:34] run what happens in the long run how do
[01:08:36] you achieve a long run equilibrium
[01:08:39] >> and I think that there there is an
[01:08:43] answer as well and I don't like this
[01:08:45] answer
[01:08:47] but it needs to be considered
[01:08:51] In the long run, you might say, okay, so
[01:08:53] if you have a world where powerful AI
[01:08:55] exist. In the short term, you could say,
[01:08:58] okay, you have universal high income.
[01:09:01] You have universal high income and we
[01:09:03] all doing well. But we know that what do
[01:09:07] the Buddhists say? Change is the only
[01:09:08] constant. And so things change and there
[01:09:11] is some kind of government political
[01:09:13] structure thing and it changes because
[01:09:15] these things have a shelf life. you know
[01:09:18] some new new government thing comes up
[01:09:20] and it functions and then after some
[01:09:22] time it stops functioning
[01:09:25] that's something that you see happening
[01:09:26] all the time and so I think that for the
[01:09:28] long run equilibrium
[01:09:32] one approach you could say okay so maybe
[01:09:35] every person will have an AI that will
[01:09:37] do their bidding and that's good and if
[01:09:40] that could be maintained indefinitely
[01:09:42] that's true but the downside with that
[01:09:44] is okay so then the AI goes and like
[01:09:48] earns earn earn you know earns money for
[01:09:50] for the person and you know advocates
[01:09:52] for their needs in like the political
[01:09:54] sphere and maybe then writes a little
[01:09:56] report saying okay here's what I've done
[01:09:58] here's the situation and the person says
[01:10:00] great keep it up but the person is no
[01:10:03] longer a participant
[01:10:05] and then you can say that's a precarious
[01:10:07] place to be in but so I'm going to
[01:10:10] preface by saying
[01:10:13] I don't like this solution but it is a
[01:10:16] solution
[01:10:18] And the solution is if people become
[01:10:20] part AI with some kind of neural link++
[01:10:23] because what will happen as a result is
[01:10:25] that now the AI understands something
[01:10:27] and we understand it too like
[01:10:31] because now the understanding is
[01:10:32] transmitted wholesale. So now if the AI
[01:10:34] is in some situation now it's like you
[01:10:38] are involved in the situation yourself
[01:10:40] fully
[01:10:41] and I think this is the answer to the
[01:10:43] equilibrium. I wonder if uh the fact
[01:10:46] that emotions which were
[01:10:49] developed
[01:10:51] millions or in many cases billions of
[01:10:53] years ago in a totally different
[01:10:54] environment are still guiding our
[01:10:57] actions so strongly is an example of
[01:11:01] alignment success to maybe spell out
[01:11:04] what I mean the brain stem has these
[01:11:10] I don't know if it's more accurate to
[01:11:11] call it a value function or reward
[01:11:12] function but the brain stem has a
[01:11:14] directive where it's saying mate with
[01:11:16] somebody who's more successful. The
[01:11:17] cortex is the part that understands what
[01:11:19] does success mean in the modern context
[01:11:22] but the brain stem is able to align the
[01:11:24] cortex and say however you recognize
[01:11:27] success to be and I I'm not smart enough
[01:11:28] to understand what that is. You're still
[01:11:30] going to pursue this directive.
[01:11:31] >> I think I think there is
[01:11:34] so I think there's a more general point.
[01:11:36] I think it's actually really mysterious
[01:11:39] how the brain encodes high level
[01:11:43] desires. Sorry, how evolution encodes
[01:11:45] high level desires.
[01:11:46] >> Like it's pretty easy to understand how
[01:11:49] evolution would would endow us with the
[01:11:51] desire for food that smells good cuz
[01:11:54] smell is a chemical
[01:11:56] and so just pursue that chemical. It's
[01:11:58] very easy to imagine such a me evolution
[01:12:00] doing such a thing. But evolution also
[01:12:04] has has endowed us with all these social
[01:12:07] desires like we we really care about
[01:12:10] being seen positively by society. We
[01:12:12] care about being in a good standing. We
[01:12:15] like all these social intuitions that we
[01:12:18] have. I feel strongly that they are
[01:12:21] baked in and I don't know how evolution
[01:12:25] did it because it's a high level
[01:12:27] concept. It's represented in the brain.
[01:12:29] like what people think like let's say
[01:12:31] you are like you care about
[01:12:35] some social thing.
[01:12:37] It's not like a low-level signal like
[01:12:40] smell. It's not something that for which
[01:12:42] there's a sensor like the brain needs to
[01:12:44] do a lot of processing to piece together
[01:12:46] lots of bits of information to
[01:12:49] understand what's going on socially and
[01:12:51] somehow evolution said that's what you
[01:12:53] should care about.
[01:12:54] >> Yes.
[01:12:54] >> How did it do it? And it did it quickly
[01:12:56] too.
[01:12:57] >> Yeah. because I think all these
[01:12:58] sophisticated social things that um we
[01:13:01] care about I think they evolved pretty
[01:13:03] recently. So evolution had an easy time
[01:13:06] hardcoding this high level desire and
[01:13:09] >> I maintain or you know at least I'll say
[01:13:12] I'm unaware of good hypothesis for how
[01:13:15] it's done. I I had some ideas I was
[01:13:18] kicking around but none of them none of
[01:13:21] them uh are satisfying.
[01:13:23] >> Yeah. And what's especially impressive
[01:13:25] is if it was a desire that you learned
[01:13:27] in your lifetime, it kind of makes sense
[01:13:29] because your brain is intelligent. It
[01:13:31] makes sense why we be able to learn
[01:13:33] intelligent desires. But your point is
[01:13:35] that the desire is maybe this is not
[01:13:38] your point, but one way to understand it
[01:13:39] is the desire is built into the genome
[01:13:42] and the genome is not intelligent,
[01:13:44] right? But it's able to you're somehow
[01:13:45] able to describe this feature that
[01:13:47] requires like it's not even clear how
[01:13:49] you define that feature and you can get
[01:13:50] it into the you can build it into the
[01:13:53] genes. Yeah, essentially, or maybe I'll
[01:13:54] put it differently. If you think about
[01:13:56] the tools that are available to the
[01:13:58] genome,
[01:14:00] it says, okay, here's a recipe for
[01:14:02] building a brain. And you could say,
[01:14:04] here is a recipe for connecting the
[01:14:05] dopamine neurons to like the smell
[01:14:07] sensor.
[01:14:08] >> Yeah.
[01:14:09] >> And if the smell is a certain kind of,
[01:14:10] you know, good smell, you want to eat
[01:14:12] that. I could imagine the genome doing
[01:14:14] that. I'm I'm claiming that it is harder
[01:14:17] to imagine. It's harder to imagine the
[01:14:20] genome saying you should care about some
[01:14:23] complicated computation that your entire
[01:14:26] brain that like a big chunk of your
[01:14:27] brain does. That's all I'm claiming. I I
[01:14:30] can tell you like a speculation. I was
[01:14:32] wondering how it could be done. And let
[01:14:34] me offer a speculation and I'll explain
[01:14:35] why the speculation is probably false.
[01:14:37] So the speculation is okay. So the brain
[01:14:43] it's like the brain has those regions.
[01:14:46] You know the brain regions. We have our
[01:14:48] cortex, right?
[01:14:49] >> Yeah.
[01:14:49] >> It has all those brain regions and the
[01:14:52] cortex is uniform. But the brain regions
[01:14:54] and and and the neurons in the cortex,
[01:14:56] they kind of speak to their neighbors
[01:14:58] mostly. And that's explains why you get
[01:15:00] brain regions because if you want to do
[01:15:02] some kind of speech processing, all the
[01:15:04] neurons that do speech need to talk to
[01:15:05] each other and they can and because
[01:15:07] neurons can only speak to their nearby
[01:15:08] neighbors for the most part, it has to
[01:15:10] be a region. All the regions are mostly
[01:15:12] located in the same place from person to
[01:15:14] person. So maybe evolution hardcoded
[01:15:16] literally a location on the brain.
[01:15:21] So it says, "Oh, like when when like you
[01:15:23] know the GPS of the brain, GPS
[01:15:26] coordinates, such and such, when that
[01:15:27] fires, that's what you should care
[01:15:28] about." Like maybe that's what evolution
[01:15:30] did cuz that would be within the toolkit
[01:15:31] of evolution. Yeah. Although there are
[01:15:34] examples where for example people who
[01:15:37] are born blind have that area of their
[01:15:38] cortex adopted by
[01:15:42] another sense and I have no idea but I'd
[01:15:46] be surprised if the desires or the
[01:15:50] reward functions which require visual
[01:15:53] signal no longer worked. You know people
[01:15:56] who have their different areas of their
[01:15:57] cortex co-opted. For example, if you no
[01:16:00] longer have vision,
[01:16:03] can you still feel the sense that I want
[01:16:05] people around me to like me and so
[01:16:06] forth, which usually there's also visual
[01:16:09] cues for.
[01:16:09] >> So, I actually fully agree with that. I
[01:16:11] I think there's an even stronger counter
[01:16:12] argument to this theory,
[01:16:14] >> which is like if you think about people,
[01:16:16] so there are people who get half of
[01:16:19] their brain removed in childhood.
[01:16:22] >> Yeah. and they still have all their
[01:16:24] brain regions, but they all somehow move
[01:16:26] to just one hemisphere, which suggests
[01:16:28] that the brain regions the the location
[01:16:31] is not fixed. And so that theory is not
[01:16:33] true. It would have been cool if it was
[01:16:34] true, but it's not. And so I think
[01:16:37] that's a mystery, but it's an
[01:16:38] interesting mystery. Like the fact is
[01:16:39] somehow
[01:16:41] >> evolution was able to endow us to care
[01:16:44] about social stuff very very reliably.
[01:16:46] And even people who have like all kinds
[01:16:48] of strange mental conditions and
[01:16:50] deficiencies and emotional problems tend
[01:16:52] to care about this. Also, AI tools like
[01:16:55] defakes, voice clones, and agents have
[01:16:58] dramatically increased the
[01:17:00] sophistication [music]
[01:17:01] of fraud and abuse. So, it's more
[01:17:03] important than ever to actually
[01:17:05] understand the identity and intent
[01:17:07] [music] of whoever or whatever is using
[01:17:10] your platform. That's exactly what
[01:17:12] Sardine helps you do. Sardine brings
[01:17:14] together thousands of device behavior
[01:17:16] and identity signals to help you assess
[01:17:19] risk. Everything from how a user types
[01:17:21] or moves their mouse or holds their
[01:17:23] device to whether they're hiding their
[01:17:25] true location behind a [music] VPN to
[01:17:28] whether they're injecting a fake camera
[01:17:30] feed during KYC selfie checks. Sardine
[01:17:33] combines these signals with insights
[01:17:35] from their network of almost 4 billion
[01:17:37] devices. things like a user's history of
[01:17:39] fraud or their associations with other
[01:17:42] high-risisk accounts so you can spot bad
[01:17:44] actors before they do damage. This would
[01:17:47] literally be impossible if you only use
[01:17:50] data from your own [music] application.
[01:17:52] Sardine doesn't stop at detection. They
[01:17:54] offer a suite of agents to streamline
[01:17:56] onboarding checks and automate
[01:17:57] investigations. [music] So, as
[01:17:59] fraudsters use AI to scale their
[01:18:01] attacks, you can use AI to scale your
[01:18:03] defenses. Go to sardine.ai/warcash.
[01:18:06] AI/Swarcash
[01:18:08] to learn more and download their guide
[01:18:10] on AI fraud detection.
[01:18:13] What is SSI planning on doing
[01:18:15] differently? So presumably your plan is
[01:18:17] to be one of the frontier companies when
[01:18:19] this time arrives
[01:18:22] and then what is
[01:18:24] presumably you started SSI because
[01:18:26] you're like I I think I have a way of
[01:18:28] approaching how to do this safely in a
[01:18:30] way that the other companies don't. What
[01:18:32] what is that difference? So the way I
[01:18:34] would describe it as
[01:18:37] there are some ideas that I think are
[01:18:39] promising and I want to investigate them
[01:18:42] and see if they are indeed promising or
[01:18:44] not. It's really that simple. It's an
[01:18:46] attempt. I think that if the ideas turn
[01:18:48] out to be correct, these ideas that we
[01:18:50] discussed around understanding
[01:18:54] generalization,
[01:18:56] >> if these ideas turn out to be correct,
[01:19:00] then I think we will have something
[01:19:02] worthy. Will it turn out to be correct?
[01:19:04] We are doing research. We are squarely
[01:19:07] age of research company. We are making
[01:19:09] progress. We've actually made quite good
[01:19:11] progress over the past year. But we need
[01:19:13] to keep making more progress,
[01:19:14] >> more research.
[01:19:16] >> And that's how I see it. I see it as an
[01:19:18] attempt to be
[01:19:22] an attempt to be a voice and a
[01:19:25] participant.
[01:19:26] Um people have asked uh your co-founder
[01:19:31] and previous CEO left to go to Meta
[01:19:34] recently and people have asked well if
[01:19:37] there was a lot of breakthroughs being
[01:19:39] made that seems like a thing that should
[01:19:40] have been unlikely. I wonder how you
[01:19:42] respond.
[01:19:43] >> Yeah. So I in for for this I will simply
[01:19:46] remind a few facts that may have been
[01:19:50] forgotten and I think this these facts
[01:19:52] which provide the context I think they
[01:19:53] explain the situation. So the context
[01:19:56] was that we were fundraising at a 32
[01:19:59] billion valuation
[01:20:01] and then Meta um came in and offered to
[01:20:06] to acquire us and I said no
[01:20:10] but my former co-founder
[01:20:14] like in some sense said yes and as a
[01:20:17] result he also was able to enjoy from a
[01:20:19] lot of near-term liquidity and he was
[01:20:22] the only person from SSI to join Meta.
[01:20:25] It sounds like SSI's plan is to be a
[01:20:27] company that is at the frontier when you
[01:20:29] get to this
[01:20:31] very important period in human history
[01:20:33] where you have superhuman intelligence
[01:20:35] and you have these ideas about how to
[01:20:36] make superhuman intelligence go well but
[01:20:39] other companies will be trying their own
[01:20:41] ideas. What distinguishes SSI's approach
[01:20:45] to making super intelligence go well?
[01:20:48] The
[01:20:48] >> the main thing that distinguishes SSI is
[01:20:52] its technical approach.
[01:20:54] So we have a different technical
[01:20:55] approach that I think is worthy
[01:20:59] and we are pursuing it.
[01:21:01] I maintain that in the end there will be
[01:21:03] a convergence of strategies. So I think
[01:21:06] there will be a convergence of
[01:21:07] strategies where
[01:21:10] at some point as AI becomes more
[01:21:13] powerful
[01:21:14] it's going to become more or less
[01:21:16] clearer to everyone what the strategy
[01:21:18] should be. And it should be something
[01:21:20] like, yeah, you need to find some way to
[01:21:23] talk to each other. And you want your
[01:21:25] first
[01:21:27] actual like real super intelligent AI to
[01:21:29] be aligned and somehow be,
[01:21:35] you know, care for sentient life, care
[01:21:38] for people, democratic, one of those,
[01:21:40] some combination of thereof. And I think
[01:21:44] this is the condition
[01:21:47] that everyone should strive for and
[01:21:50] that's what SSI is striving for and I
[01:21:53] think that with time if not already all
[01:21:57] the other companies will realizing that
[01:21:58] they're striving towards the same thing
[01:22:00] and we'll see. I think that the world
[01:22:01] will truly change as AI becomes more
[01:22:03] powerful.
[01:22:03] >> Yeah.
[01:22:04] >> And I think a lot of these forecasts
[01:22:06] will like I think things will be really
[01:22:09] different and people will be acting
[01:22:10] really differently. What speaking of
[01:22:12] forecast what are your forecasts to this
[01:22:15] system you're describing which can learn
[01:22:17] as well as a human and
[01:22:21] subsequently as a result become
[01:22:22] superhuman.
[01:22:23] >> I think like uh 5 to 20
[01:22:26] >> 5 to 20 years.
[01:22:27] >> Mhm.
[01:22:28] >> So I just want to unroll your
[01:22:32] how you might see the world coming. It's
[01:22:33] like we have a couple more years where
[01:22:35] these other companies are continuing the
[01:22:37] current approach and it stalls out and
[01:22:40] stalls out here meaning they earn no
[01:22:41] more than low hundreds of billions in
[01:22:44] revenue or how do you think about what
[01:22:45] stalling out means?
[01:22:46] >> Yeah,
[01:22:48] I think the re I think it could I think
[01:22:50] it could stall out and
[01:22:53] I think stalling out will look like
[01:22:56] it will all look very similar.
[01:22:58] >> Yeah.
[01:22:59] >> Among all the different companies
[01:23:00] something like this. I'm not sure
[01:23:02] because I think I think I think even
[01:23:03] with I think even I think even with
[01:23:05] stolen out I think these companies could
[01:23:07] make a stupendous stupendous revenue
[01:23:10] maybe not profits because they will be
[01:23:12] it will be they will need to work hard
[01:23:14] to differentiate each other from
[01:23:15] themselves but revenue definitely
[01:23:18] >> but there's something in your model
[01:23:20] implies that
[01:23:22] the when the correct solution does
[01:23:24] emerge there will be convergence between
[01:23:26] all the companies and I'm curious why
[01:23:28] you think that's the case
[01:23:29] >> well I was talking more about converg
[01:23:31] convergence on their larger strategies.
[01:23:33] >> I think eventual convergence on the
[01:23:34] technical approach is probably going to
[01:23:36] happen as well but I I was alluding to
[01:23:39] convergence to the larger strategies.
[01:23:40] What what what exactly is the thing that
[01:23:42] should be done?
[01:23:43] >> I I just want to better understand how
[01:23:45] you see the future on rolling. So
[01:23:46] currently we have these different
[01:23:47] companies and you expect their approach
[01:23:49] to continue generating revenue. Yes.
[01:23:51] >> But not get to this humanlike learner.
[01:23:52] >> Yes.
[01:23:54] >> So now we have these different forks of
[01:23:55] companies. We have you we have thinking
[01:23:57] machines. There's a bunch of other labs.
[01:23:59] >> Yes. and maybe one of them figures out
[01:24:01] the correct approach
[01:24:03] >> but then the release of their product
[01:24:04] makes it clear to other people how to do
[01:24:06] this thing.
[01:24:07] >> I think it won't be clear how to do it
[01:24:10] thing but it will be clear that
[01:24:11] something different is possible
[01:24:12] >> right
[01:24:12] >> and that is information and I think
[01:24:15] people will will then be trying to
[01:24:17] figure out how how that's how that
[01:24:19] works. I do think though that one of the
[01:24:23] things that's that I think you know not
[01:24:26] addressed here not discussed is that
[01:24:30] with each increase in the AI's
[01:24:33] capabilities I think there will be some
[01:24:34] kind of changes but I don't know exactly
[01:24:37] which ones in how things are being done.
[01:24:41] So like I think it's going to be
[01:24:43] important yet I can't spell out what
[01:24:46] that is exactly.
[01:24:47] >> And how how are the
[01:24:50] by default you would expect the company
[01:24:52] that has the model company that has that
[01:24:53] model to be getting all these gains
[01:24:55] because they have the model that is
[01:24:57] learning how to do all has the skills
[01:24:59] and knowledge that it's building up in
[01:25:01] the world. What is the reason to think
[01:25:03] that the benefits of that would be
[01:25:04] widely distributed and not just end up
[01:25:06] at whatever model company gets this
[01:25:08] continuous learning loop going first?
[01:25:11] >> Like I think that empirically what
[01:25:13] happen so here here is what I think is
[01:25:15] going to happen. Number one, I think
[01:25:18] empirically when
[01:25:22] let's let's look at let's look at how
[01:25:25] things have gone so far with um the AIs
[01:25:28] of the past. So one company produced an
[01:25:30] advance and the other company scrambled
[01:25:33] and produced some competi some some
[01:25:36] similar things after some amount of time
[01:25:39] and they started to compete in the
[01:25:41] market and push their push the prices
[01:25:45] down
[01:25:45] >> and so I think from the market
[01:25:47] perspective I think something similar
[01:25:49] will happen there as well even if
[01:25:51] someone okay so okay so okay so okay so
[01:25:51] okay so okay so okay so okay so okay so
[01:25:51] okay so okay we talking about the good
[01:25:53] world by the way where
[01:25:56] what's the good world. What's the good
[01:25:58] world?
[01:26:01] Where we have these powerful humanlike
[01:26:04] learners that are also like and by the
[01:26:08] way maybe there there's another thing we
[01:26:09] haven't discussed on the on the the spec
[01:26:12] of the super intelligent AI that I think
[01:26:15] is worth considering is that you make it
[01:26:18] narrow
[01:26:19] can be useful and narrow at the same
[01:26:21] time. So you can have lots of narrow
[01:26:22] super intelligent AIs. But suppose you
[01:26:25] have many of them
[01:26:28] and you have some and you have some
[01:26:29] company that's producing a lot of um
[01:26:32] profits from it and then you have
[01:26:35] another company that comes in and starts
[01:26:37] to compete and the way the competition
[01:26:39] is going to work is through
[01:26:40] specialization.
[01:26:42] I think what's going to happen is that
[01:26:45] the way
[01:26:47] competition like competition loves
[01:26:50] specialization and you see it in the
[01:26:52] market, you see it in evolution as well.
[01:26:54] So you're going to have lots of
[01:26:55] different niches and you're going to
[01:26:56] have lots of different companies who are
[01:26:58] occupying different niches in
[01:27:02] in this kind of world where you might
[01:27:03] say yeah like one AI company is really
[01:27:06] quite a bit better at some area of
[01:27:09] really complicated economic activity and
[01:27:11] a different company is better at another
[01:27:12] area and the third company is really
[01:27:14] good at litigation and that's
[01:27:16] contradicted by what humanlike learning
[01:27:17] implies is that like it can learn
[01:27:19] >> it can but but you have accumulated
[01:27:22] learning you have a big investment. You
[01:27:25] spent a lot of compute to become really
[01:27:27] really really good really phenomenal at
[01:27:30] this thing and someone else spent a huge
[01:27:32] amount of comput and a huge amount of
[01:27:34] experience to get really really good at
[01:27:35] some other thing
[01:27:35] >> right
[01:27:36] >> you apply a lot of human learning to get
[01:27:37] there but now like you you are at this
[01:27:41] high point where someone else would say
[01:27:43] look like I don't want to start learning
[01:27:45] what you've learned to go
[01:27:46] >> I guess that would require many
[01:27:47] different companies to begin at the
[01:27:49] human like continual learning agent at
[01:27:51] the same time so that they can start
[01:27:54] their different research in different
[01:27:56] branches. But if one company,
[01:28:01] you know, gets that agent first or gets
[01:28:02] that learner first,
[01:28:05] it does then seem like well, you know,
[01:28:07] they could like if you just think about
[01:28:09] every single job in the economy,
[01:28:12] you just have uh instance learning each
[01:28:15] one seems tractable for a company.
[01:28:17] >> Yeah, that's that's that's a valid
[01:28:19] argument. My my strong intuition is that
[01:28:21] it's not how it's going to go.
[01:28:24] My strong intuition is that yeah like
[01:28:25] the argument says it will go this way.
[01:28:28] >> Yeah.
[01:28:28] >> But my strong intuition is that it will
[01:28:29] not go this way that this is the you
[01:28:33] know in in theory there is no difference
[01:28:35] between theory and practice. In practice
[01:28:37] there is and I think that's going to be
[01:28:38] one of those
[01:28:39] >> a lot of people's models of recursive
[01:28:41] self-improvement literally explicitly
[01:28:43] state we will have a million Ilias in a
[01:28:46] server that are coming in with different
[01:28:48] ideas and this will lead to a super
[01:28:49] intelligence emerging very fast. Do you
[01:28:51] have some intuition about how
[01:28:52] parallelizable the thing you are doing
[01:28:55] is? How how what are the gains from
[01:28:59] making copies of Ilia?
[01:29:00] >> I don't know. I think
[01:29:04] I think there'll definitely be there'll
[01:29:06] be diminishing returns because you want
[01:29:08] you want people who think differently
[01:29:10] rather than the same. I think that if
[01:29:12] they were literal copies of me, I'm not
[01:29:14] sure how much more incremental value
[01:29:16] you'd get. I think that
[01:29:20] but people who think differently that's
[01:29:22] what you want.
[01:29:23] >> Why is it that it's been if you look at
[01:29:25] different models even released by
[01:29:27] totally different companies trained on
[01:29:29] potentially non-over overlapping data
[01:29:31] sets it's actually crazy how similar
[01:29:34] LLMs are to each other.
[01:29:35] >> Maybe the data sets are not as non-over
[01:29:37] overlapping as it seems. But there's
[01:29:41] there's some sense there's like even if
[01:29:42] an individual human might be less
[01:29:44] productive than the future AI. Maybe
[01:29:45] there's something to the fact that human
[01:29:46] teams have more diversity than teams of
[01:29:48] AIs might have. But how do we elicit
[01:29:50] meaningful diversity among AI? So I
[01:29:53] think just raising the temperature just
[01:29:55] results in gibberish. I think you want
[01:29:57] something more like
[01:29:58] >> different scientists have different
[01:29:59] different prejudices or different ideas.
[01:30:01] [clears throat] How do you get that kind
[01:30:02] of diversity among AI agents? So the
[01:30:05] reason there has been no diversity I
[01:30:07] believe is because of pre-training.
[01:30:10] All the pre-trained models are the same
[01:30:13] pretty much because the pre-train on the
[01:30:15] same data. Now RL and postraining is
[01:30:19] where some differentiation starts to
[01:30:20] emerge because different people come up
[01:30:23] with different RL training.
[01:30:24] >> Yeah. And then I've heard you hint in
[01:30:27] the past about selfplay as a way to
[01:30:31] either get data or match agents to other
[01:30:33] agents of equivalent intelligence to
[01:30:36] kick off learning. How should we think
[01:30:38] about why there's no public
[01:30:43] um proposals of this kind of thing and
[01:30:45] working with LLM?
[01:30:46] >> I would say there are two things to say.
[01:30:49] I would say that the reason why I
[01:30:51] thought selfplayful is interesting
[01:30:53] is because it offered a way to create
[01:30:56] models using compute only without data,
[01:31:00] right? And if you think that data is the
[01:31:01] ultimate bottleneck, then using compute
[01:31:04] only is very interesting. So that's what
[01:31:07] makes it interesting. Now the
[01:31:10] the thing is
[01:31:13] that selfplay at least the way it was
[01:31:16] done in the past when you have agents
[01:31:18] which are somehow compete with each
[01:31:20] other it's only good for developing a
[01:31:22] certain set of skills it is too narrow.
[01:31:25] It's only good for like negotiation
[01:31:28] uh conflict
[01:31:30] certain social skills
[01:31:33] strategizing that kind of stuff. And so
[01:31:35] if you care about those skills then
[01:31:37] selfplay will be useful. Now actually I
[01:31:39] think that selfplay
[01:31:41] did
[01:31:43] find a home but just in a different form
[01:31:46] in a different form. So things like
[01:31:49] debate prove a verifier. You have some
[01:31:53] kind of an LLM as a judge which is also
[01:31:56] incentivized to find mistakes in your
[01:31:57] work. You could say this is not exactly
[01:31:59] selfplay but this is you know a related
[01:32:01] adversarial setup that people are doing.
[01:32:03] believe
[01:32:04] >> and really selfplay is an example of um
[01:32:06] is a special case of more general like
[01:32:09] um competition between between agents,
[01:32:12] >> right? The response the natural response
[01:32:14] to competition is to try to be
[01:32:15] different. And so if you were to put
[01:32:17] multiple agents and you tell them, you
[01:32:19] know, you all need to work on some
[01:32:21] problem and you're an agent and you're
[01:32:24] inspecting what everyone else is
[01:32:25] working, you're going to say, well, if
[01:32:27] they already taken this approach, it's
[01:32:30] not clear I should pursue it. they
[01:32:31] should pursue something differentiated
[01:32:33] and so I think that something like this
[01:32:35] could also create an incentive for um a
[01:32:37] diversity of approaches.
[01:32:39] >> Yeah. Um final question,
[01:32:43] what is research taste? You're obviously
[01:32:47] the person in the world who is
[01:32:50] considered to have the best taste in
[01:32:53] doing research in AI. you were uh the
[01:32:57] co-author on many of the biggest the
[01:33:00] biggest things that have happened in the
[01:33:02] history of deep learning from Alex net
[01:33:03] to GBT3 to so on what is it that how do
[01:33:06] you characterize how
[01:33:09] you come up with these ideas
[01:33:11] >> I can answer so I can comment on this
[01:33:13] for myself
[01:33:14] >> I think different people do it
[01:33:15] differently
[01:33:18] >> but one thing that um guides me
[01:33:21] personally
[01:33:22] is
[01:33:24] an aesthetic
[01:33:26] of how AI should be
[01:33:28] >> by thinking about how people are but
[01:33:31] thinking correctly
[01:33:33] >> like it's very easy to think about how
[01:33:34] people are incorrectly but what does it
[01:33:37] mean to think about people correctly
[01:33:39] >> so I'll give you some examples
[01:33:41] the idea of the artificial neuron is
[01:33:45] directly inspired by the brain and it's
[01:33:47] a great idea why because you say sure
[01:33:49] the brain has all these different organs
[01:33:51] has the faults but the faults probably
[01:33:53] don't matter M
[01:33:54] >> why do we think that the neurons matter?
[01:33:56] Because there's many of them. It kind of
[01:33:58] feels right. So you want the neuron.
[01:34:00] >> Yeah.
[01:34:01] >> You want some kind of local learning
[01:34:02] rule that will change the connections.
[01:34:04] You want some local learning rule rule
[01:34:06] that will change the connections between
[01:34:07] the neurons,
[01:34:09] >> right? It feels plausible that the brain
[01:34:11] does it. The idea of the distributed
[01:34:13] representation,
[01:34:15] the idea that the brain,
[01:34:18] you know, the brain responds to
[01:34:19] experience or neural network should
[01:34:20] learn from experience, not response. The
[01:34:21] brain learns from experience.
[01:34:24] the neural network of experience and you
[01:34:27] kind of ask yourself is some is
[01:34:28] something fundamental or not fundamental
[01:34:30] how things should be
[01:34:32] >> and I think that's been guiding me a
[01:34:34] fair bit kind of thinking from multiple
[01:34:37] angles and looking for almost beauty
[01:34:39] beauty simplicity ugliness there's no
[01:34:42] room for ugliness it's just beauty
[01:34:44] simplicity elegance correct inspiration
[01:34:47] from the brain and all of those things
[01:34:49] need to be present at the same time and
[01:34:51] the more they are present the more
[01:34:53] confident you can be in a top- down
[01:34:54] belief. And then the top down belief is
[01:34:57] the thing that sustains you when the
[01:34:59] experiments contradict you. Because if
[01:35:02] you just trust the data all the time,
[01:35:04] well, sometimes you can be doing a
[01:35:05] correct thing, but there's a bug.
[01:35:07] >> But you don't know that there is a bug.
[01:35:08] How can you tell that there is a bug?
[01:35:11] >> How do you know if you should keep
[01:35:12] debugging or you conclude it's the wrong
[01:35:13] direction? Well, it's the top down.
[01:35:15] Well, how should you can say the things
[01:35:17] have to be this way? Something like this
[01:35:19] has to work. Therefore, we got to keep
[01:35:22] going. That's the top down. And it's
[01:35:24] based on this like multifaceted beauty
[01:35:27] and inspiration by the brain.
[01:35:29] >> All right, we'll leave it there.
[01:35:31] >> Thank you so much.
[01:35:34] >> All right. Appreciate it.
[01:35:35] >> That was great.
[01:35:36] >> Yeah, I enjoyed it.
[01:35:37] >> Yes, me too.
[01:35:39] >> Hey everybody, I hope you enjoyed that
[01:35:40] episode. If you did, the most helpful
[01:35:42] thing you can do is just share it with
[01:35:44] other people who you think might enjoy
[01:35:46] it. It's also helpful if you leave a
[01:35:48] rating or a comment on whatever platform
[01:35:51] you're listening on. If you're
[01:35:52] interested in sponsoring the podcast,
[01:35:54] you can reach out at
[01:35:56] dwarcash.com/advertise.
[01:36:00] Otherwise, I'll see you on the next one.
