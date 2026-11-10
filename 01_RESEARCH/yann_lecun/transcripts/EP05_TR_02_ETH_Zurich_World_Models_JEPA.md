# Yann LeCun: World Models — Enabling the next AI revolution (ETH Zurich)
- **YouTube URL:** https://www.youtube.com/watch?v=72Xj8k5WQX4
- **Lines:** 1781

---

[00:00:00] Yeah, I'll talk about world models. Uh
[00:00:03] possibly the enabler for the next AR
[00:00:07] revolution.
[00:00:09] So,
[00:00:11] there's a lot of machine learning people
[00:00:12] I think in the room, perhaps.
[00:00:14] Uh I have bad news for you. Machine
[00:00:16] learning sucks.
[00:00:20] Uh you know, basically if when we
[00:00:22] compare the learning abilities of
[00:00:25] uh machines with humans and animals, uh
[00:00:27] clearly there is a big gap.
[00:00:29] Um
[00:00:31] you know, people and animals can learn
[00:00:33] new tasks uh extremely quickly
[00:00:36] and with very few trials, very few
[00:00:38] samples. Uh people have common sense,
[00:00:41] animals too, physical common sense.
[00:00:44] There's a lot of tasks that we can
[00:00:45] accomplish zero shot even if we've never
[00:00:47] faced them before.
[00:00:48] Um and
[00:00:50] how how do we do this with machines? How
[00:00:53] And you know, we have very powerful AI
[00:00:55] techniques that everybody is using, but
[00:00:58] they don't really handle
[00:01:00] the real world. They don't handle
[00:01:02] continuous, high-dimensional, noisy
[00:01:05] data.
[00:01:06] Language is easy by comparison. And so,
[00:01:10] uh
[00:01:11] the real world is messy. Language is
[00:01:13] simple. That
[00:01:15] And and you know, this connects with
[00:01:16] what you know, Vladlen said earlier and
[00:01:19] uh
[00:01:19] Jitendra as well,
[00:01:21] uh the Moravec paradox that you know,
[00:01:23] things that are simple are difficult for
[00:01:26] computers and things that are
[00:01:28] complicated for humans turn out to not
[00:01:30] be that difficult for computers. Uh like
[00:01:33] playing chess, computing integrals
[00:01:34] symbolically, and you know, solving
[00:01:36] equations, proving math theorems, etc.
[00:01:39] Uh so,
[00:01:41] you know, how is it that a 10-year-old
[00:01:43] can
[00:01:44] uh basically do what you would like a
[00:01:47] domestic robot to do and do most of
[00:01:49] those tasks without actually being
[00:01:51] trained to do them the first time you
[00:01:52] ask them, they can do it.
[00:01:54] They may not want to do it, but they
[00:01:56] can. Uh
[00:01:58] How come, you know, any teenager can
[00:02:00] learn to drive a car in a few hours of
[00:02:02] practice, yet
[00:02:04] the self-driving car companies have
[00:02:06] literally millions of hours of training
[00:02:08] data,
[00:02:09] and despite that, they can't use those
[00:02:11] millions of hours of training data to
[00:02:13] get a machine to
[00:02:14] just imitating uh humans to uh to drive
[00:02:17] at the at the same level of uh
[00:02:19] reliability. Otherwise, we'll have
[00:02:22] level five self-driving cars, and we
[00:02:24] don't we don't have them.
[00:02:25] At best,
[00:02:27] in the consumer car business, we have
[00:02:28] level two or three,
[00:02:30] and uh the the robo-taxis are
[00:02:32] engineered,
[00:02:34] you know, very heavily engineered with
[00:02:36] various uh sensors and other things. So,
[00:02:40] you know, we keep
[00:02:41] bumping into this Moravec paradox, and
[00:02:43] we really have to go beyond this if you
[00:02:45] believe that a
[00:02:46] intelligence requires grounding. Of
[00:02:49] course, some philosophers, and certainly
[00:02:50] some language people, don't believe
[00:02:52] that's necessary, but I think it is. Uh
[00:02:55] So, like uh Vladlen, we're in
[00:02:56] Switzerland outside Jean Piaget. He was
[00:02:58] a big influence on me.
[00:03:00] Uh
[00:03:01] He had a debate with uh Noam Chomsky uh
[00:03:04] in France in the late 1970s, where um
[00:03:09] you know, they were debating whether
[00:03:10] language was innate or learned,
[00:03:12] and uh the trans- you know, there was
[00:03:15] transcriptions of that debate with, you
[00:03:17] know, people participating in it, and
[00:03:19] one of them was Jean uh was uh
[00:03:22] um
[00:03:24] uh was uh
[00:03:28] a a guy who had worked with Jean Piaget,
[00:03:30] who was a professor at MIT,
[00:03:33] and was talking about the perceptron,
[00:03:36] uh
[00:03:37] kind of saying, you know, there's those
[00:03:38] simple
[00:03:39] machine learning models that are you
[00:03:41] know, capable of uh learning
[00:03:42] surprisingly complex uh tasks, and uh
[00:03:47] uh
[00:03:47] you know, that may be kind of evidence
[00:03:49] for for fact that learning is possible,
[00:03:51] contrary to what Chomsky was saying.
[00:03:53] Um
[00:03:55] This guy was Seymour Papert. He was
[00:03:56] professor at MIT, and 10 years before
[00:03:58] that, he had written a book that
[00:03:59] basically killed the entire field of
[00:04:02] neural net, including the this basically
[00:04:04] pointing out the limitation of the
[00:04:06] perceptron. But here he was, 10 years
[00:04:08] later,
[00:04:09] arguing for the fact that those things
[00:04:11] were actually interesting to study. But
[00:04:13] anyway, so Jean Piaget says,
[00:04:15] "Intelligence is not what you know, it's
[00:04:17] what you do when you don't know."
[00:04:19] In fact, he never actually said this.
[00:04:20] This is apocryphal.
[00:04:22] Uh
[00:04:23] but there are other psychologists who
[00:04:24] basically kind of distilled
[00:04:27] his thinking into this sentence, which
[00:04:29] he never said. Um
[00:04:31] So he's kind of quoted as as saying
[00:04:32] that. Uh
[00:04:33] so intelligence is not an accumulation
[00:04:36] of declarative knowledge. LLMs are an
[00:04:38] accumulation of declarative knowledge,
[00:04:39] not just, but the main reason they're
[00:04:42] useful is because they can accumulate a
[00:04:43] lot of declarative knowledge.
[00:04:45] Uh intelligence is not a collection of
[00:04:48] skills.
[00:04:49] Uh
[00:04:51] You can probably build a machine to
[00:04:53] accomplish sort of any task if you spend
[00:04:55] enough resources on it, including things
[00:04:57] like self-driving.
[00:04:59] But that's not really what intelligence
[00:05:01] is. Intelligence is the ability to learn
[00:05:02] to drive in about 20 hours.
[00:05:05] Or to learn, you know, learn any new
[00:05:08] task with very little training, or
[00:05:10] accomplish new tasks in a zero-shot.
[00:05:13] Uh that's really what intelligence is,
[00:05:14] and that's really what Jean Piaget
[00:05:16] means. What that means is that we're not
[00:05:18] going to have any simple measures uh
[00:05:21] of intelligence because
[00:05:23] uh because again, any particular task,
[00:05:25] you can always, you know, if you spend
[00:05:27] enough effort and and time, you can
[00:05:29] always kind of crack it.
[00:05:31] So it's more, you know, how adaptive you
[00:05:33] are.
[00:05:34] Um
[00:05:36] And, you know, this this connects to
[00:05:37] something that Bled and said, like the
[00:05:39] notion of AGI is complete nonsense.
[00:05:42] Uh human intelligence is specialized.
[00:05:45] The characterization of human
[00:05:46] intelligence is that it's very quickly
[00:05:48] adaptive and we can learn new task. We
[00:05:51] all all of us know different sets of
[00:05:55] uh
[00:05:56] knowledge and have different skills.
[00:05:59] Uh and so
[00:06:01] it's because we've been exposed to, you
[00:06:04] know, different environments and we
[00:06:06] we've had to solve different problems.
[00:06:08] Uh we're adaptive. That's really what
[00:06:10] intelligence is. Okay, so how do you uh
[00:06:13] how do humans learn and animals for that
[00:06:16] uh there's a lot of uh
[00:06:19] learning that takes place in the early
[00:06:21] months of life mostly by observation. Uh
[00:06:23] so, you know,
[00:06:25] two-month-old baby, you know, can just
[00:06:26] take a rate so can develop a dynamical
[00:06:29] model of its own limbs but basically
[00:06:31] cannot affect the world. You know, it
[00:06:33] can't move an object or anything. Uh
[00:06:37] but it does
[00:06:38] it, you know, can learn a lot of things
[00:06:41] about the world. One thing a baby can
[00:06:43] learn really quickly is that the world
[00:06:45] is three-dimensional.
[00:06:47] Why? Because
[00:06:49] the fact that an object has a distance
[00:06:52] every
[00:06:53] every uh
[00:06:55] point in the world has a distance from
[00:06:57] us is the best way to explain how our
[00:07:00] view of the world changes when we move
[00:07:01] our head.
[00:07:03] And of course babies don't move
[00:07:05] necessarily their head but they are
[00:07:06] being moved so they this this see
[00:07:09] parallax and sort of they derive from
[00:07:10] this the fact that the world is
[00:07:13] three-dimensional. We can do this with
[00:07:15] learning machines today. They learn that
[00:07:17] that the world is three-dimensional only
[00:07:19] by being exposed passively to
[00:07:21] uh
[00:07:22] videos. Uh
[00:07:24] so that's that's uh an interesting uh
[00:07:27] thing.
[00:07:29] And I'm going to silence my phone
[00:07:31] because
[00:07:33] it's actually
[00:07:38] Okay.
[00:07:40] So um
[00:07:43] So, basic concepts like object
[00:07:45] permanence is this is learned really
[00:07:47] quickly. Uh
[00:07:48] notions of stability, rigidity, and
[00:07:50] things like that. But then, uh what we
[00:07:52] would consider intuitive physics, uh
[00:07:54] things like uh inertia,
[00:07:57] gravity,
[00:07:59] that actually takes 9 months for uh
[00:08:01] human infants.
[00:08:03] Shorter for most animals.
[00:08:05] And
[00:08:07] if you put a 8-month-old on a high chair
[00:08:10] and you put a bunch of toys,
[00:08:12] uh 8 or 9 months old,
[00:08:16] the child will most likely
[00:08:17] systematically take all the
[00:08:20] toys and throw them on the floor and
[00:08:22] watch the result. They're doing the
[00:08:23] experiment that gravity actually applies
[00:08:25] to everything.
[00:08:27] Uh
[00:08:30] So, that takes a long time. How does
[00:08:31] that happen? What type of learning is
[00:08:32] taking place there? They're doing the
[00:08:34] experiment, but they can learn about
[00:08:35] gravity just by observation as well.
[00:08:38] Uh so, if you if you show the the
[00:08:39] scenario here at the bottom, where a car
[00:08:42] is on a platform, you push it off the
[00:08:43] platform, it appears to float in the
[00:08:45] air,
[00:08:46] uh a 6-month-old will barely pay
[00:08:47] attention, hasn't learned about gravity
[00:08:49] yet. Uh a 10-month-old will go very
[00:08:52] surprised, like the little girl.
[00:08:54] Uh and that that's actually how
[00:08:56] psychologists measure
[00:08:57] uh
[00:08:58] whether a baby has learned a particular
[00:09:01] concept about the world, uh which is a
[00:09:03] the violation of expectation. Um we
[00:09:06] actually we can actually use those
[00:09:07] techniques to test whether
[00:09:09] machine learning system has have
[00:09:11] acquired some, you know, some notion of
[00:09:13] common sense. Uh so, there there's uh a
[00:09:15] lot that can be said about this. Uh
[00:09:18] Uh Jitendra and I uh collaborated on on
[00:09:20] a a paper here, mostly written by
[00:09:22] Emmanuel Dupoux, actually. And Jitendra
[00:09:24] I very little uh
[00:09:26] contributions to it on on on this this
[00:09:29] whole kind of
[00:09:31] set of questions.
[00:09:33] Okay, well, what is really what is
[00:09:35] intelligence is if it's not an
[00:09:36] accumulation of
[00:09:38] uh of skills and not an accumulation
[00:09:39] accumulation of declarative knowledge is
[00:09:42] the ability to accomplish new tasks as I
[00:09:44] said, solve new problems with with
[00:09:46] without prior training. Uh
[00:09:48] and again AGI has no makes no sense as a
[00:09:51] as a as a phrase.
[00:09:53] Uh human intelligence is specialized and
[00:09:56] the the question is is not do you know
[00:09:58] how to do everything? Is it Can you
[00:10:01] learn quickly how to do anything?
[00:10:03] Or a wide spectrum of of things. Uh
[00:10:06] there's a a little kind of somewhat
[00:10:08] philosophical paper here at the bottom
[00:10:10] uh
[00:10:12] written by some of my young colleagues.
[00:10:15] So, um here is a simple calculation.
[00:10:18] There's still a lot of people
[00:10:19] particularly on the west coast of the US
[00:10:21] uh who believes that
[00:10:23] uh we're going to reach
[00:10:25] what they call AGI, okay?
[00:10:27] Uh
[00:10:29] by by scaling up LLMs
[00:10:32] uh maybe training them on synthetic
[00:10:34] data, maybe you know, using a few tricks
[00:10:36] and post training and reinforcement
[00:10:38] learning.
[00:10:39] And I think that's impossible.
[00:10:41] Uh I'm a believer in sort of grounded uh
[00:10:45] intelligence if you want, but but you
[00:10:46] can do the simple calculation.
[00:10:48] Uh an LLM you know, typical LLM of today
[00:10:52] is trained on something like uh
[00:10:55] 20 trillion words but that corresponds
[00:10:57] to about 30 trillion tokens.
[00:10:59] And each token is 3 bytes, something
[00:11:02] like that.
[00:11:03] Um
[00:11:04] So, the data volume is about 10 to the
[00:11:06] 14 bytes. This would take about 400,000
[00:11:08] years for any human to read.
[00:11:11] Uh
[00:11:11] then compare this with what a a
[00:11:13] 4-year-old has seen during his or her
[00:11:16] life. That's about 16 hours of wake
[00:11:18] time.
[00:11:20] And uh which by the way the small amount
[00:11:22] of video is about 30 minutes of YouTube
[00:11:24] uploads.
[00:11:25] And uh we have 2 million optic nerve
[00:11:28] fibers carrying about 1 byte per second
[00:11:30] each. So, the data volume uh that for
[00:11:33] your world I see through vision and
[00:11:35] probably through touch as well is about
[00:11:37] 10 to the 14 bytes.
[00:11:39] So,
[00:11:40] for your world through vision, same
[00:11:42] amount of data as 400,000 years through
[00:11:45] text.
[00:11:47] With all the human produced text
[00:11:49] available on the publicly on the
[00:11:51] internet.
[00:11:52] Uh,
[00:11:53] we're not going to get to
[00:11:55] anything like human-like intelligence by
[00:11:57] just training on text. It's just not
[00:11:58] going to happen.
[00:12:00] Um,
[00:12:04] so
[00:12:06] of course you're going to say, well,
[00:12:08] video is much more redundant than than
[00:12:10] text.
[00:12:11] But in fact, that's a feature not a bug.
[00:12:13] If you want to train a system,
[00:12:15] particularly using self-supervised
[00:12:16] learning, you need redundancy in the in
[00:12:18] the data.
[00:12:20] If you don't have redundancy, you can't
[00:12:21] learn anything.
[00:12:23] So, redundancy is a good thing. You
[00:12:25] don't want too much of it though.
[00:12:27] Okay, so then there is another question
[00:12:28] about what are the right properties of
[00:12:30] intelligent systems. And
[00:12:33] in my opinion, an important property
[00:12:36] of an intelligent system is
[00:12:38] the mode of inference.
[00:12:40] Does it compute its output by
[00:12:42] propagating through a fixed number of
[00:12:43] layers of some neural net?
[00:12:47] Or consider the alternative. The
[00:12:49] alternative is computing the output of a
[00:12:51] system by searching for an output that
[00:12:54] is
[00:12:55] most compatible, if you want, with the
[00:12:57] input. Okay? So, you observe a situation
[00:13:01] that runs through some perception module
[00:13:03] that produce some sort of
[00:13:05] representation of the current state of
[00:13:07] the world as you observe it.
[00:13:08] Uh, you can directly produce an action.
[00:13:11] Okay? That's a reactive
[00:13:13] uh, system, if you want. Or you could
[00:13:17] imagine an action
[00:13:19] and then have an intelligent system, the
[00:13:22] intelligent system, figure out is this a
[00:13:24] good action for this observation? Is
[00:13:26] this something that,
[00:13:28] you know, will accomplish the task I
[00:13:29] want? So, the objective here
[00:13:32] characterizes whether the task the
[00:13:34] system wants to accomplish has been
[00:13:35] accomplished or not. Think of it as a
[00:13:37] cost function. It's not used for
[00:13:39] learning, it's used for inference.
[00:13:41] Think of it as, you know, negative log
[00:13:43] likelihood in a probabilistic inference
[00:13:45] model.
[00:13:46] Or,
[00:13:47] as I prefer to think of it, an energy
[00:13:49] function.
[00:13:50] So, basically there, the inference
[00:13:53] is a process by which you search for an
[00:13:56] output that minimizes some energy
[00:13:58] function at inference time.
[00:14:00] Okay? That's intrinsically more powerful
[00:14:01] computationally
[00:14:03] than just propagation through a fixed
[00:14:05] number of layers.
[00:14:11] And then contrast, uh, so the model on
[00:14:13] the
[00:14:15] on the left, uh, is sort of LLM-like,
[00:14:19] right? Take a window of of inputs,
[00:14:21] run this through a fixed number of
[00:14:23] layers of some big neural net with a few
[00:14:25] hundred billion parameters, produce one
[00:14:27] token.
[00:14:28] Okay, then shift that token on the in
[00:14:30] the input and then produce the second
[00:14:31] token, etc., etc.
[00:14:34] That's auto-regressive prediction, and
[00:14:36] every token involves the computation of,
[00:14:38] you know, a fixed amount of computation
[00:14:40] running through a fixed number of layers
[00:14:41] of some neural net.
[00:14:43] Uh, this is not a good model. It's not a
[00:14:45] good model of reasoning. The way you
[00:14:47] coerce an LLM to do reasoning is that
[00:14:49] you trick it into generating more
[00:14:51] tokens.
[00:14:53] But, that's not the way
[00:14:55] we reason. We reason internally, we
[00:14:57] don't reason in token space,
[00:14:59] in language even.
[00:15:01] Um,
[00:15:02] okay, compare this with the model on the
[00:15:04] on the right, uh, which is a slight
[00:15:06] specialization of the the previous one.
[00:15:09] Uh, you perceive, uh,
[00:15:11] the world or your environment, you get
[00:15:13] some idea of the state the current state
[00:15:15] of the of the world, and then you
[00:15:17] imagine a sequence of actions, a
[00:15:19] proposal for an action,
[00:15:21] you feed it to
[00:15:23] an internal world model for the system,
[00:15:25] and the world model predicts the
[00:15:26] outcome, and then feeds feeds this
[00:15:28] outcome to a an objective that measures
[00:15:31] to what extent a task has been
[00:15:33] accomplished or not.
[00:15:34] Okay, then by optimization, you search
[00:15:36] for an action sequence that optimizes
[00:15:37] this this uh objective, minimizes this
[00:15:40] energy.
[00:15:41] At inference time, I haven't talked
[00:15:42] about learning yet, okay?
[00:15:46] In my opinion, that's a much more
[00:15:47] powerful model.
[00:15:49] Um
[00:15:51] But you need a world model. Now, if you
[00:15:52] do have
[00:15:53] So so I've I've sort of uh
[00:15:56] settled on this kind of uh
[00:15:58] I idea or architecture
[00:16:00] uh about 5 years ago. I wrote a long
[00:16:02] paper about it uh that I put online in
[00:16:05] 2022 uh with some general architecture,
[00:16:09] etc. If you want to take pictures, here
[00:16:11] are QR codes, you can get to it. Um
[00:16:14] And uh
[00:16:17] it's you know
[00:16:18] relatively easy to read, but kind of
[00:16:20] long.
[00:16:22] And
[00:16:24] and it's really based on this idea that
[00:16:26] uh
[00:16:27] reasoning and planning are essential,
[00:16:30] and they basically proceed by energy
[00:16:33] minimization rather than forward
[00:16:34] propagation.
[00:16:36] And that
[00:16:37] for this to work, you need some world
[00:16:38] model, okay? So, same process that I
[00:16:41] described before, there is a few a few
[00:16:42] additional tricks.
[00:16:44] You observe the environment, perception
[00:16:46] module produce an uh
[00:16:47] representation of the initial state of
[00:16:49] the world, but only a representation of
[00:16:51] what you currently perceive. So, you may
[00:16:53] have to combine this
[00:16:55] with the content of
[00:16:56] the memory to uh get a
[00:17:00] complete complete idea of the the state
[00:17:02] of the world, uh what you know about it
[00:17:03] at least. Then you feed this to your
[00:17:05] world model together with a proposal for
[00:17:07] an action sequence, and and your world
[00:17:09] model predicts the outcome of that uh
[00:17:12] action sequence. You feed this to an
[00:17:14] objective, an energy function that
[00:17:16] measures to what extent a a particular
[00:17:18] task has been accomplished. So, this
[00:17:21] function outputs zero if the task is
[00:17:23] accomplished and some,
[00:17:25] you know, positive number
[00:17:28] if the task is not not accomplished and
[00:17:30] perhaps measures some distance to the
[00:17:32] task being accomplished. So,
[00:17:34] intuitively, you can have another set of
[00:17:35] objectives that are guardrails that
[00:17:38] would ensure that whatever
[00:17:40] state sequences the the system is going
[00:17:43] to take the world through is not going
[00:17:44] to kill anyone or hurt anyone or, you
[00:17:47] know, have any kind of
[00:17:49] deleterious effect. And so,
[00:17:52] a system constructed this way can be
[00:17:53] made intrinsically safe because it has
[00:17:56] to
[00:17:57] obey and,
[00:17:59] you know, optimize the guardrail
[00:18:01] objective with every output it produces.
[00:18:04] This is not the case for an LLM. An LLM,
[00:18:07] the only way an LLM can be made, uh,
[00:18:10] you know, safe or non-toxic or whatever
[00:18:11] you want to call it, is by fine-tuning
[00:18:13] it. And there is always a way to break
[00:18:16] the conditioning, if you want, to
[00:18:18] jailbreak the the system.
[00:18:20] Here, you can't jailbreak a system like
[00:18:23] this. It It can do nothing but optimize
[00:18:26] the guardrail objectives and and the
[00:18:28] task objective.
[00:18:30] Of course, if you have a world model,
[00:18:33] certainly a lot of robotics system
[00:18:35] optimal control people in the room,
[00:18:37] you can apply this world model multiple
[00:18:39] time steps and, you know, each action an
[00:18:41] action sequence can be decomposed into a
[00:18:42] sequence. The guardrails can be applied
[00:18:45] to all the the steps in the sequence.
[00:18:48] Okay, that's the way you would use a
[00:18:49] world model. And the way you plan by
[00:18:51] optimization there is akin to model
[00:18:53] predictive control, MPC, very classical
[00:18:56] stuff in optimal control going back to
[00:18:57] the 1960s.
[00:18:59] Ultimately, what you want though is
[00:19:01] something that can do hierarchical
[00:19:02] planning.
[00:19:03] All of us do hierarchical planning.
[00:19:05] Animals do hierarchical planning. What
[00:19:07] is hierarchical planning? Let's say that
[00:19:10] Uh, I'm sitting in my office at NYU
[00:19:13] and I want to be in Paris tomorrow.
[00:19:16] There's no way I can plan my entire trip
[00:19:18] to Paris in terms of
[00:19:21] kind of muscle actions 10 ms by 10 ms.
[00:19:25] Uh, which are the elementary actions
[00:19:27] that humans can can do.
[00:19:29] Uh,
[00:19:30] I can't do that because first of all,
[00:19:32] it's too long. But second of all, I
[00:19:33] don't have the information.
[00:19:36] I don't know if when I'm going down on
[00:19:38] the street how long I'm going to have to
[00:19:40] wait before a taxi stops. Right? So,
[00:19:42] there's no way I can plan the entire
[00:19:43] thing.
[00:19:44] I have to do hierarchical planning. So,
[00:19:46] what I have to do is at a high level, I
[00:19:48] have to say, "Well,
[00:19:49] I don't know how long it's going to take
[00:19:51] me to go to the airport, but you know,
[00:19:52] maybe maybe roughly an hour and an hour
[00:19:54] and a half. So,
[00:19:55] uh,
[00:19:56] I need to get to the airport and catch a
[00:19:57] plane. Okay, that's a two-step
[00:19:59] high-level plan. I don't need to know
[00:20:01] many details
[00:20:02] uh, to make that plan.
[00:20:04] And now I have a sub-goal, which is
[00:20:05] being at the airport.
[00:20:07] I mean, New York, so going to the
[00:20:09] airport involves going down on the
[00:20:10] street and catching hailing a taxi
[00:20:13] and go to the airport.
[00:20:15] Uh,
[00:20:15] now I need to go down on the street.
[00:20:18] I'm in a NYU building, that involves
[00:20:20] uh, walking to the elevator, pushing the
[00:20:22] button, getting down, and walking out
[00:20:24] the door.
[00:20:25] Uh,
[00:20:26] now I have a sub-goal of getting to the
[00:20:27] elevator, right? Etcetera. So, you you
[00:20:29] can sort of go down this entire
[00:20:30] hierarchy and at some point you get to a
[00:20:32] point where the action you need to take
[00:20:34] is very simple. It's something that you
[00:20:35] are familiar with. You may not have to
[00:20:38] use your full mental power to kind of
[00:20:40] plan the action. You can probably stand
[00:20:42] up from your chair without having to
[00:20:43] think about it. That could be just
[00:20:44] policy. Uh,
[00:20:46] but essentially,
[00:20:47] uh,
[00:20:48] ultimately, we want systems to do
[00:20:50] hierarchical planning.
[00:20:52] How do we solve that? This is an
[00:20:54] unsolved problem.
[00:20:55] If you're a roboticist or an AI for
[00:20:57] robotics kind of person or agentic AI
[00:20:59] kind of person,
[00:21:01] if you're studying a PhD on this topic,
[00:21:03] this is a great topic. It's completely
[00:21:04] open. Nobody knows how to do this.
[00:21:07] Nobody he proved that they know how to
[00:21:08] do this.
[00:21:10] Um
[00:21:11] Okay, so now the big question is how how
[00:21:14] are we going to train those
[00:21:16] those world models?
[00:21:18] Um okay, hierarchical or not? Let's say
[00:21:21] non-hierarchical to start. So first of
[00:21:23] all, we have to figure out what
[00:21:24] architecture to give them.
[00:21:26] And a natural instinct in these days
[00:21:30] days and age is to train a generative
[00:21:32] model.
[00:21:33] And in fact, I've been working on sort
[00:21:36] of trying to
[00:21:37] train world model like things for about
[00:21:39] 15 years, mostly failing for the first
[00:21:41] 10.
[00:21:44] Because I was trying to train generative
[00:21:46] models. Okay, what's a generative model?
[00:21:48] So
[00:21:49] uh
[00:21:50] self-supervised learning has been
[00:21:51] incredibly
[00:21:53] successful, astonishingly successful in
[00:21:55] the context of language, right? You take
[00:21:57] a
[00:21:58] a string of words,
[00:22:00] you remove some of the words,
[00:22:02] um you correct the the input,
[00:22:05] and then you run the corrupted input
[00:22:07] through some big neural net, and you
[00:22:09] train it to recover the missing parts.
[00:22:11] Okay?
[00:22:12] That works amazingly well for text.
[00:22:15] So there are original models like BERT
[00:22:16] that that used to do this. An LLM is a
[00:22:18] special case of this where the only word
[00:22:20] you remove is the last one. So that the
[00:22:22] entire system is trying to just produce
[00:22:24] the next word in a in a sequence. Okay?
[00:22:26] But it works amazingly well if you and
[00:22:28] it it scales if you do it right.
[00:22:31] It doesn't work if you apply it to
[00:22:32] video. So if you take a a video
[00:22:34] and then you show the initial segment of
[00:22:36] the video to the system, and you ask it
[00:22:38] to predict what's going to happen next
[00:22:39] at a pixel level,
[00:22:41] it doesn't really work. Like the
[00:22:42] representations you get out of the
[00:22:43] system for your video are not
[00:22:45] particularly good.
[00:22:47] Um
[00:22:49] And the reason is
[00:22:52] you simply cannot predict everything
[00:22:53] that takes place in a video. There's an
[00:22:55] infinite number of plausible things.
[00:22:57] In text, it's easy because there is only
[00:22:59] a finite number of words, and so you can
[00:23:01] get the system to produce
[00:23:03] a probability distribution over all
[00:23:05] possible words or tokens in your
[00:23:06] dictionary.
[00:23:07] But,
[00:23:08] you can't do this with video, right?
[00:23:10] There's just a
[00:23:11] incredibly large number of
[00:23:13] possible video frames.
[00:23:15] Uh let me take an example. Uh if I take
[00:23:17] a video of this room, right? I start
[00:23:18] here, and I kind of slowly rotate the
[00:23:20] camera, I stop here,
[00:23:22] and I ask the system to continue the
[00:23:23] video. You know, it's probably going to
[00:23:25] predict, you know, we are in some sort
[00:23:26] of empty
[00:23:28] classroom, uh auditorium, and you know,
[00:23:31] the room has a finite size, there might
[00:23:33] be windows on this side, and things like
[00:23:34] that. There's absolutely no way the
[00:23:36] system can predict what all of you look
[00:23:38] like.
[00:23:39] Or which, you know, chairs are
[00:23:41] unoccupied.
[00:23:42] Um it's just impossible. You just don't
[00:23:44] have the information. So, when you train
[00:23:46] a system to make this kind of
[00:23:47] prediction, you kill it.
[00:23:50] Now, of course, you're going to tell me,
[00:23:51] "Oh, but we can train system to produce
[00:23:53] cute videos, right? Video generation."
[00:23:56] Yes,
[00:23:57] but
[00:23:59] this prediction usually is done in
[00:24:01] representation space, not in pixel
[00:24:03] space. It's only a second stage that
[00:24:05] actually turns
[00:24:06] the predictions into high-resolution
[00:24:09] uh
[00:24:10] high-frame-rate uh uh videos.
[00:24:13] And
[00:24:14] the system only needs to produce one
[00:24:16] cute-looking video. It doesn't need to
[00:24:18] actually
[00:24:20] represent all plausible videos.
[00:24:23] Uh
[00:24:24] so, which is a much simpler problem.
[00:24:26] Okay, and as I said, I've been kind of
[00:24:28] attempting to work on this for the
[00:24:30] better part of the last 15 years. So,
[00:24:31] this is
[00:24:32] a 10-year
[00:24:33] 10-year-old paper
[00:24:35] where we tried to train some uh neural
[00:24:37] net to predict, you know, short video
[00:24:38] clips, you know, two frames from from
[00:24:40] four frames of context. You get blurry
[00:24:42] predictions. Why? Because the system
[00:24:44] predicts the average of everything that
[00:24:46] can happen. Of course, you can correct
[00:24:47] that with latent variable models, like
[00:24:49] diffusion models, uh
[00:24:51] but we which we didn't know at the time.
[00:24:53] We tried to use GANs and stuff like
[00:24:54] that. Wasn't too successful.
[00:24:57] Uh but, you know, perhaps using latent
[00:24:59] variable models would uh would help, uh,
[00:25:01] diffusion models in particular.
[00:25:04] Um, which of course produce cute videos.
[00:25:06] Do they actually understand the world?
[00:25:09] The evidence is no.
[00:25:11] Um, so here's my solution. My solution
[00:25:13] is a architecture I called uh joint
[00:25:15] embedding, or more precisely joint
[00:25:18] embedding predictive architecture, JEPA,
[00:25:21] which is shown uh on the right.
[00:25:23] Okay, on the left you have generative
[00:25:25] architecture. You observe X, maybe you
[00:25:27] observe A, an action that is taking
[00:25:28] place,
[00:25:29] and you observe the result Y, and the
[00:25:31] system is trying to
[00:25:33] reconstruct Y in its most minute
[00:25:35] details.
[00:25:36] Uh, with uh JEPA,
[00:25:39] you observe X and Y and A, but you
[00:25:42] encode both X and Y, and the prediction
[00:25:44] takes place in that representation
[00:25:45] space.
[00:25:47] Okay?
[00:25:48] Major difference.
[00:25:50] What the system can do is essentially
[00:25:52] eliminate from the input
[00:25:56] uh,
[00:25:56] by constructing a representation of Y,
[00:25:58] it can eliminate all the information
[00:26:00] about about Y that is simply not
[00:26:03] predictable.
[00:26:05] Right?
[00:26:06] And that makes the prediction more
[00:26:08] abstract, with fewer details,
[00:26:10] but more accurate in a way.
[00:26:13] Um,
[00:26:15] so
[00:26:17] you know, how do you train a generative
[00:26:18] model? It's easy to train a generative
[00:26:20] model because the cost is just a
[00:26:21] reconstruction cost.
[00:26:23] It's just going to, you know, you're
[00:26:24] just training it to reconstruct. You can
[00:26:26] train it as an auto encoder, but then
[00:26:28] you need to restrict the information
[00:26:29] content in the code, or as denoising
[00:26:31] auto encoder, which is what a lot of uh,
[00:26:34] techniques have attempted to do like
[00:26:35] masked auto encoders and things like
[00:26:37] that. So that means uh taking a an
[00:26:39] input, corrupting it in some ways, and
[00:26:42] then training an auto encoder to recover
[00:26:44] the initial one. Uh,
[00:26:46] and by the way, uh
[00:26:47] diffusion models are a bit of a special
[00:26:49] case of this of this
[00:26:51] sort of
[00:26:52] general thing of denoising.
[00:26:54] Um
[00:26:55] So,
[00:26:56] the values is when you train systems of
[00:26:59] this type to learn representations of
[00:27:01] images,
[00:27:03] you don't get good representations.
[00:27:05] If you use the representation of images
[00:27:06] obtained this way, you feed it to a
[00:27:08] downstream uh task that you train
[00:27:11] supervise, okay, you train a head
[00:27:13] supervise.
[00:27:15] The results you get are
[00:27:16] not great.
[00:27:19] To get good results, you have to use
[00:27:20] joint-embedding architectures. All the
[00:27:22] best systems that use self-supervised
[00:27:24] learning to train an image or video
[00:27:26] representation systems system,
[00:27:29] all use joint-embedding. None of them
[00:27:31] uses reconstruction.
[00:27:33] Okay? All the best ones.
[00:27:35] And
[00:27:36] uh
[00:27:39] either you Let's say you apply this to
[00:27:40] images, uh either you have two views of
[00:27:43] the same scene,
[00:27:45] and you train a neural net to produce
[00:27:47] representations, and you tell the
[00:27:48] system, "I want those two
[00:27:49] representations to be identical."
[00:27:52] Um
[00:27:53] or you you use this uh corruption
[00:27:56] technique. You take a an input, you
[00:27:58] corrupt it,
[00:27:59] uh or transform it in some ways, and
[00:28:01] then uh you know, train the this Jepa
[00:28:04] architecture to predict the
[00:28:05] representation of the original image
[00:28:07] from the representation of the
[00:28:09] uh corrupted uh version. Okay, there's a
[00:28:12] big issue with this,
[00:28:15] which is that the system can collapse.
[00:28:18] Now, the generative models can actually
[00:28:19] collapse to some extent. Like, if you
[00:28:21] try to train an autoencoder without
[00:28:23] a restricted a restricted you know,
[00:28:25] restriction on the information content
[00:28:26] of the code,
[00:28:27] your autoencoder is just going to learn
[00:28:29] the identity function, and that's a
[00:28:30] collapse.
[00:28:31] It's not going to learn anything useful.
[00:28:34] Um
[00:28:35] Similarly,
[00:28:37] a system like this can can collapse, and
[00:28:40] how can it collapse? It can
[00:28:42] essentially completely ignore
[00:28:45] the inputs,
[00:28:47] produce constant representations and
[00:28:49] other prediction problem is trivial. So,
[00:28:51] if you're just trying a system of this
[00:28:53] type to minimize
[00:28:54] the prediction error, it's going to
[00:28:56] collapse. It's not going to do anything
[00:28:58] useful for you. So, the whole trick of
[00:29:00] how you do self-supervised learning for
[00:29:02] joint embedding uh system is how you
[00:29:05] prevent collapse.
[00:29:09] And there is uh my favorite concept for
[00:29:13] this. I'll talk about other ways to do
[00:29:15] this but my favorite concept to prevent
[00:29:17] collapse
[00:29:18] is uh
[00:29:20] is information maximization. Okay? So,
[00:29:22] you basically come up with some
[00:29:25] objective function that measures the
[00:29:28] some sort of information content
[00:29:30] of the representation that comes out of
[00:29:32] your encoders.
[00:29:34] And you try to maximize that information
[00:29:36] content. Okay? So, your cost function is
[00:29:37] minus the information or whatever.
[00:29:40] Uh so, there's a bunch of uh
[00:29:42] uh techniques uh for this uh
[00:29:46] you know, since like the last 6 or 7
[00:29:48] years with names like MNCR, NCR squared,
[00:29:52] WMSE, Seegrid, VICReg, and Barlow Twins.
[00:29:56] Uh the Barlow Twins, VICReg, Seegrid uh
[00:30:00] come from uh
[00:30:02] people working with me.
[00:30:03] Uh the other ones from other groups.
[00:30:05] MNCR comes from uh uh Berkeley and NCR
[00:30:09] squared from uh
[00:30:11] a colleague at NYU Neuroscience. It was
[00:30:13] Sam Chelleli.
[00:30:14] Uh so,
[00:30:18] but this idea of JPAC is getting
[00:30:20] popularity.
[00:30:21] Uh there's about 1,700 papers
[00:30:23] that mention joint embedding predictive
[00:30:25] architecture
[00:30:26] spelled out uh on Google Scholar. Okay,
[00:30:29] so how
[00:30:30] There's an issue with this type of
[00:30:32] method, which is how do you measure
[00:30:33] information content?
[00:30:36] We need to have a cost function that is
[00:30:37] a differentiable measure of information
[00:30:39] content, so we can back propagate
[00:30:41] gradient and maximize it.
[00:30:43] And the bad news is, first of all, we
[00:30:46] don't actually have objective measures
[00:30:47] of information content because all the
[00:30:50] proper definitions
[00:30:52] are based on knowing the distribution
[00:30:55] of the the vectors or whatever that you
[00:30:57] want to measure the information content
[00:30:59] of.
[00:31:00] And we don't know the distribution. We
[00:31:01] only have samples coming out of an
[00:31:02] encoder.
[00:31:04] So, how you
[00:31:05] how do you compute information content
[00:31:06] from a finite number of samples?
[00:31:08] Okay, that's the first problem. Second
[00:31:10] problem is to maximize something you
[00:31:12] would need a lower bound
[00:31:14] on information content so that when you
[00:31:16] maximize, you push the actual
[00:31:17] information content up.
[00:31:21] Problem is, every empirical measure that
[00:31:23] we we have are all upper bounds.
[00:31:26] So, what do we do?
[00:31:27] We come up with a good upper bound and
[00:31:29] we cross our fingers.
[00:31:34] And we show some theorems and whatever.
[00:31:35] Okay. Uh
[00:31:37] so, this technique uh
[00:31:40] and and many others and on like the way
[00:31:42] to properly explain how you how
[00:31:45] you know, how you can train
[00:31:46] self-supervised learning systems and and
[00:31:48] every learning system really is a
[00:31:50] framework I call energy-based models
[00:31:52] that I've been advocating for 20 years
[00:31:54] or so. Uh
[00:31:56] it's basically
[00:31:58] the basic idea is like this. If you want
[00:32:00] to capture the dependency between two
[00:32:01] variables,
[00:32:02] X and Y, there is no real functional
[00:32:05] relationship between X and Y. So, you
[00:32:07] cannot there's no single Y for a given
[00:32:09] X. Right? It's just a dependency, but
[00:32:11] it's not a function.
[00:32:12] Like it's a relation or some kind of
[00:32:14] mapping, but not a function.
[00:32:16] Uh so, indicated by the diagram on the
[00:32:18] right here, you have a bunch of data
[00:32:20] points, so those are the the black uh
[00:32:22] uh uh
[00:32:23] dots.
[00:32:24] Um and so, they indicate some sort of
[00:32:26] dependency between X and Y. How do you
[00:32:29] capture this dependency
[00:32:31] given that you cannot run a function
[00:32:32] that that computes Y from X?
[00:32:35] So, one way to do this is to
[00:32:37] uh uh
[00:32:39] learn or build a contrast function
[00:32:42] energy function
[00:32:43] that tells you
[00:32:46] a point in this XY space is near the
[00:32:50] the the training data or not. Okay? So,
[00:32:53] we think of it as some some sort of
[00:32:54] landscape uh
[00:32:56] where the the black dots are in the
[00:32:59] valley.
[00:33:00] Okay? In Switzerland, it would be a
[00:33:01] lake.
[00:33:03] Uh and then, you know, you get like
[00:33:06] you know, level curves, right? As as you
[00:33:09] move out, you know, outside of those
[00:33:11] regions, the altitude goes up. Okay? The
[00:33:13] energy goes up, right?
[00:33:15] Now, if I give you a value for X, you
[00:33:17] can infer you can give me a bunch of
[00:33:19] values for Y that are compatible with X.
[00:33:21] They are values of Y that minimize the
[00:33:22] energy, right? So, it's the kind of
[00:33:23] inference I was talking about earlier,
[00:33:25] inference by optimization, not by
[00:33:27] forward propagation.
[00:33:29] Uh
[00:33:30] but you can also possibly do it the
[00:33:32] other way around. If I give you a Y, you
[00:33:34] can infer X uh from Y. And you can give
[00:33:36] me multiple answers. So, in situations
[00:33:39] like like video prediction, where there
[00:33:41] is a basically an infinite number of
[00:33:42] possible answers,
[00:33:44] the proper way to train the system of
[00:33:45] this type is to think of it in terms of
[00:33:47] energy-based models.
[00:33:49] Uh and by the way, probabilistic uh
[00:33:52] models are special case.
[00:33:54] Where where your energy has particular
[00:33:56] form and the way you train it has
[00:33:57] particular loss function.
[00:33:59] Um so, it's a slightly more general
[00:34:01] framework, if you want, than
[00:34:02] probabilistic
[00:34:03] uh inference
[00:34:05] and learning.
[00:34:06] >> [clears throat]
[00:34:07] >> Okay, so what you to train an
[00:34:09] energy-based model,
[00:34:11] you have to prevent collapse. The
[00:34:12] collapse problem I was telling you about
[00:34:13] before will be manifested by the energy
[00:34:16] function being flat everywhere. You
[00:34:18] train the system to minimize the energy
[00:34:20] for a bunch of training samples, and
[00:34:22] what the system gives you an energy
[00:34:23] function that is zero everywhere. That's
[00:34:25] what a autoencoder that learns the
[00:34:26] identity function, that's what it it
[00:34:28] does to you. A jetpack that ignores the
[00:34:30] input and produces constant
[00:34:32] representation at zero prediction error
[00:34:34] for everything. So, it's a collapse. To
[00:34:37] prevent collapse, you need to do one of
[00:34:39] two things. One is contrastive methods.
[00:34:41] You You generate points outside the
[00:34:44] region of data, and you push the energy
[00:34:46] up.
[00:34:47] Okay? You come up with some cost
[00:34:48] function that makes sure the energy of
[00:34:50] the data points come down, and and the
[00:34:52] energy of other points is is higher.
[00:34:55] And there's a whole bunch of them.
[00:34:57] And there is another set of method which
[00:34:58] I I've come to prefer, uh regularized
[00:35:01] method, which work by minimizing the
[00:35:03] volume of space that can take low
[00:35:04] energy. Okay? So, if you push down the
[00:35:06] energy of certain regions, the rest has
[00:35:08] to go up because there is only a small
[00:35:10] amount of a small volume of energy to go
[00:35:12] around.
[00:35:14] Of low energy.
[00:35:16] Um
[00:35:18] So, in practice,
[00:35:20] how how how do you sort of reduce this
[00:35:22] to practice? Okay? Those one of those
[00:35:24] two methods.
[00:35:25] Okay. So, um
[00:35:27] let's go back to this idea of
[00:35:28] information maximization. Uh so, I want
[00:35:31] to train this uh this uh jet bar uh some
[00:35:34] measure of information.
[00:35:36] Uh
[00:35:38] let's say I run a batch of samples
[00:35:39] through uh through one of the encoders.
[00:35:42] I get a matrix where each row is the
[00:35:45] representation for one sample. Each
[00:35:47] column is the value of one variable
[00:35:51] in the representation for all samples.
[00:35:53] Okay?
[00:35:55] There's two ways to make that matrix
[00:35:56] informative.
[00:35:58] One way is to make sure all the rows are
[00:36:00] different.
[00:36:02] And other way is to make sure all the
[00:36:03] columns are different.
[00:36:06] You want to make sure the columns are
[00:36:07] different because if all the columns are
[00:36:09] the same, that means every variable in
[00:36:11] the representation carries the same
[00:36:12] information.
[00:36:13] And of course, that's not very
[00:36:14] informative. So, you want to, you know,
[00:36:17] each
[00:36:18] variable in the representation to be
[00:36:20] maximally disentangled from the other
[00:36:21] ones to give you an independent
[00:36:23] information from the other
[00:36:25] variables.
[00:36:26] Okay?
[00:36:27] Um so, that would be an example of
[00:36:31] what we can call dimension contrastive
[00:36:33] methods, which is a form of
[00:36:36] regularized method. And then at the
[00:36:39] bottom
[00:36:41] the the type of criterion that makes the
[00:36:44] the rows all different, those are
[00:36:45] contrastive methods or sample
[00:36:46] contrastive methods.
[00:36:48] Okay, sample contrastive methods are
[00:36:49] very popular for certain applications.
[00:36:52] A lot of the perceptual pipelines in
[00:36:54] lens are trained with a technique called
[00:36:57] clip, which basically is contrastive
[00:36:58] method that does joint embedding between
[00:37:00] images and text.
[00:37:04] But I prefer the other one.
[00:37:06] So this idea that you need to find an
[00:37:10] abstract representation of an input to
[00:37:13] be able to make prediction
[00:37:15] is actually very natural.
[00:37:16] We do this all the time as humans.
[00:37:18] We do this all the time as scientists
[00:37:21] and engineers.
[00:37:22] Animals do it too.
[00:37:24] Let me explain why. In principle, I
[00:37:26] could explain
[00:37:28] or simulate everything that takes place
[00:37:29] in this room at the moment
[00:37:31] at the level of quantum field theory or
[00:37:34] particle physics, right? Could simulate
[00:37:36] the trajectory of every particle in this
[00:37:38] room.
[00:37:39] And that would go down to actually
[00:37:40] simulating all of our brain processes
[00:37:42] and everything. So in principle,
[00:37:45] running the simulation I could figure
[00:37:46] out if you know any of you actually
[00:37:48] understands the word I'm saying or not.
[00:37:50] Okay? Or if you are sleeping right now.
[00:37:54] Or if you are actually bored, right?
[00:37:57] Okay, but of course that's completely
[00:37:59] impractical.
[00:38:00] And then you know what we do in science
[00:38:03] is that we invent abstractions to allow
[00:38:05] us to make predictions and those
[00:38:06] abstractions ignore a lot of details
[00:38:09] about the state the underlying state of
[00:38:11] the system. So we invent those
[00:38:14] abstractions you know from quantum field
[00:38:15] to particles, atoms, molecules,
[00:38:17] proteins, organelles, cells, organisms,
[00:38:19] individuals, societies, ecosystem.
[00:38:22] Every level in this hierarchy is a
[00:38:23] particular level of abstraction with
[00:38:25] which we describe uh the world.
[00:38:29] Which
[00:38:30] allows us to make
[00:38:33] longer range predictions, if you want,
[00:38:36] than the levels below
[00:38:38] by ignoring a lot of details about the
[00:38:40] level below.
[00:38:41] Which is why
[00:38:43] the the way to understand what goes on
[00:38:46] in this room at the moment is is more at
[00:38:48] the level of psychology than at the
[00:38:50] level of particle physics,
[00:38:51] right?
[00:38:53] Now, of course, physicists always make
[00:38:54] fun of everyone saying like, you know,
[00:38:56] you just apply physics, right? Even
[00:38:58] psychology is applied physics to some
[00:39:00] extent. Uh
[00:39:01] but in fact, you know, there is uh
[00:39:04] you know, specific knowledge about
[00:39:05] chemistry that
[00:39:07] does not derive directly from physics,
[00:39:10] right? So so this abstraction actually
[00:39:12] kind of contains
[00:39:14] uh
[00:39:14] new knowledge or information or
[00:39:16] structure, if you want, that was not
[00:39:18] apparent at the level below.
[00:39:21] So this idea of Jetpack really kind of
[00:39:22] constructs on this concept that you need
[00:39:24] to find an abstraction to be able to
[00:39:26] make predictions.
[00:39:27] Uh let's say you you want to do um
[00:39:30] uh
[00:39:32] you want to design an airplane.
[00:39:34] You need to design the air flow for the
[00:39:35] airplane. You do computational fluid
[00:39:37] dynamics, right? You simulate the flow
[00:39:38] of air around
[00:39:40] around the wing.
[00:39:42] Uh you you model the state of the air in
[00:39:44] every little cube around around the wing
[00:39:46] by basically
[00:39:49] the velocity and the density and things
[00:39:51] like that.
[00:39:52] And and then you solve Navier-Stokes
[00:39:55] partial differential equations. And that
[00:39:57] simulates the flow of air.
[00:39:59] But in fact, it's ignoring a huge amount
[00:40:00] of details in the underlying mechanism.
[00:40:03] The underlying mechanism is molecules of
[00:40:05] air bumping into each other and bumping
[00:40:07] on the plane.
[00:40:08] But you never simulate
[00:40:11] fluids at that level. It's just
[00:40:13] too complicated. And also it would
[00:40:14] diverge from reality really quickly
[00:40:17] because it has too many details.
[00:40:19] So, you have to ignore details to be
[00:40:20] able to make accurate long-term
[00:40:22] predictions.
[00:40:24] Um and so, we do this in science all the
[00:40:26] time. And so, world models should not be
[00:40:28] simulators.
[00:40:30] Right? They should work in abstract
[00:40:31] space. They should not be digital twins,
[00:40:33] you know, that's a
[00:40:35] buzzword.
[00:40:36] They should definitely not be generative
[00:40:38] models, as I just explained.
[00:40:40] Uh and they should not be video
[00:40:41] generation. So, a lot of people are
[00:40:43] working on video generation and they
[00:40:45] call this world models.
[00:40:47] They They're not world models. They're
[00:40:49] video generation systems.
[00:40:51] Uh so, one one big message from my talk
[00:40:54] is that if if you want to use world
[00:40:57] models,
[00:40:58] do not work on video generation. This is
[00:41:00] a different problem, okay? If you want
[00:41:02] to produce cute videos, work on video
[00:41:04] generation.
[00:41:06] But if you want to like control robots
[00:41:07] or industrial processes or understand
[00:41:09] the world,
[00:41:11] do not work on generation.
[00:41:15] Um
[00:41:17] you want world models to control complex
[00:41:19] systems
[00:41:20] where you cannot
[00:41:22] model the dynamics of the system by
[00:41:24] writing a bunch of equations. Okay, if
[00:41:25] you have a humanoid robot or a you know,
[00:41:27] any kind of robot, you can just write
[00:41:29] down the dynamical equations
[00:41:31] and then simulate the dynamics of the
[00:41:32] robot and you can get your humanoid
[00:41:34] robot to do somersaults and
[00:41:36] and kung fu and whatever, right? That's
[00:41:38] simple.
[00:41:40] Uh as soon as the robot starts to
[00:41:41] interact with the real world, that's a
[00:41:43] lot more complicated.
[00:41:45] Um
[00:41:47] and and that is actually more difficult
[00:41:49] to reduce to a
[00:41:51] simple equations.
[00:41:52] But then, you know, think about a
[00:41:54] complex system, like I said, a turbojet
[00:41:56] or
[00:41:57] uh I don't know, a chemical plant or
[00:41:59] a patient
[00:42:00] uh or a robot, but a robot that
[00:42:02] interacts with the real world in complex
[00:42:04] ways.
[00:42:05] You cannot reduce this to a small number
[00:42:07] of equations. What you have to do is
[00:42:08] basically learn a energy
[00:42:11] model
[00:42:12] of the whole system,
[00:42:14] the system you control and its
[00:42:15] interaction with the environment, uh
[00:42:18] so that you can make predictions and you
[00:42:19] can plan a sequence of actions to arrive
[00:42:21] at a particular uh outcome.
[00:42:26] So that's one model. I mean, the concept
[00:42:28] is very old. It goes back to the 1960s.
[00:42:30] Uh it's the root of optimal control.
[00:42:32] Um
[00:42:33] and uh
[00:42:34] okay, so now I come down to a particular
[00:42:37] technique that I'm very fond of, which I
[00:42:39] think um
[00:42:41] we're going to
[00:42:43] expand over the next uh few months and
[00:42:45] years
[00:42:46] to do this information maximization uh
[00:42:48] that I was telling you about earlier.
[00:42:50] And it's called Sigreg. That means
[00:42:53] sketch isotropic Gaussian
[00:42:54] regularization.
[00:42:56] Okay, the trick here is the following.
[00:42:58] You you run a batch of samples through
[00:43:00] your encoders, and what you get is a
[00:43:02] bunch of points
[00:43:03] in the vector space
[00:43:05] of dimension whatever the dimension of
[00:43:07] your representation space is.
[00:43:09] We're going to try to make the
[00:43:10] distribution of those points as a tropic
[00:43:13] Gaussian with the same
[00:43:15] uh
[00:43:16] variance in all dimensions. Why? Because
[00:43:20] an isotropic Gaussian is a distribution
[00:43:22] where all the variables are independent.
[00:43:25] Okay? So they're maximally informative
[00:43:28] individually.
[00:43:30] Uh and it's also the distribution that
[00:43:32] has maximum entropy for a given
[00:43:33] variance, but we don't really care about
[00:43:35] that.
[00:43:36] Um
[00:43:37] what's interesting is that it makes the
[00:43:38] variable independent of each other.
[00:43:40] Okay, so how do we do this? Now, of
[00:43:41] course,
[00:43:42] we don't have the distribution. We just
[00:43:44] have a bunch of points
[00:43:45] uh in that space. And it may be a
[00:43:47] high-dimensional space like 2,000
[00:43:49] dimensions. And we may have, you know, a
[00:43:51] few hundred or a few thousand points.
[00:43:52] Like how do how can we make sure this is
[00:43:55] uh this is a Gaussian. So here's the
[00:43:56] trick.
[00:43:58] Uh the trick is you project
[00:44:00] the
[00:44:01] individual points
[00:44:04] along a single direction.
[00:44:06] And what you get is a marginal
[00:44:08] distribution. Okay? Now, of course, you
[00:44:09] still have discrete points. You don't
[00:44:11] have
[00:44:12] a distribute you don't have continuous
[00:44:14] uh density. You have discrete points.
[00:44:16] Okay, so one trick you can do is compute
[00:44:18] the cumulative distribution that those
[00:44:20] points give you, right?
[00:44:21] So,
[00:44:22] it's a staircase,
[00:44:24] right?
[00:44:26] Because you have discrete points
[00:44:27] in one dimension.
[00:44:29] And then what you can you can you can do
[00:44:31] is you can ask, "What is the distance
[00:44:33] between the staircase, the cumulative
[00:44:35] empirical cumulative distribution of my
[00:44:36] points,
[00:44:37] and the cumulative distribution of,
[00:44:39] let's say, a Gaussian?"
[00:44:41] You can do that, because you know what
[00:44:43] the Gaussian looks like. And for every
[00:44:45] point, you can tell
[00:44:47] on the staircase, you can tell if it's
[00:44:49] to the left or to the right of the ideal
[00:44:51] Gaussian. And so, that gives you a
[00:44:52] gradient. Like, do I move the point this
[00:44:54] way or that way?
[00:44:56] In that projection.
[00:44:58] Okay? It gives you a gradient. Now, for
[00:45:00] every training sample
[00:45:02] uh in your
[00:45:04] in your batch.
[00:45:06] Okay. Now, if you
[00:45:08] make the distribution you know, by
[00:45:10] gradient descent by optimizing this cost
[00:45:11] function, it's going to make the
[00:45:12] distribution Gaussian along the marginal
[00:45:16] uh of that distribution along this
[00:45:17] projection.
[00:45:19] But now, there's a theorem that says, if
[00:45:20] you do this
[00:45:22] along lots and lots and lots of
[00:45:24] directions, in the limit,
[00:45:26] your joint distribution is actually
[00:45:28] a isotropic Gaussian.
[00:45:31] Okay? So,
[00:45:32] what we need to do now is do many many
[00:45:34] projections. For all of those
[00:45:36] projections, compute those gradients. Uh
[00:45:39] you know, move the points or back
[00:45:40] propagate through the network, change
[00:45:41] the weights so that the points move so
[00:45:43] that the overall distribution gets more
[00:45:45] Gaussian.
[00:45:46] And
[00:45:48] uh if you apply this to a distribution
[00:45:50] like the one on the top left here, like
[00:45:52] an X,
[00:45:53] these are actually two dimen- two
[00:45:54] dimensions among 1,024.
[00:45:57] And then you do a gradient descent. You
[00:45:59] just move the points here. You don't
[00:46:00] train the neural net. You uh So, the
[00:46:02] technique I'm advocating for is on the
[00:46:03] left. You get something that's sort of
[00:46:06] Gaussian-ish.
[00:46:09] Uh
[00:46:10] and this this really works in in
[00:46:12] practice. We actually applied it to
[00:46:15] um
[00:46:16] uh
[00:46:17] training world models that are action
[00:46:18] conditioned and and we've used them for
[00:46:20] for planning and it works decently. It's
[00:46:23] a very the the
[00:46:24] the source code is available. It's very
[00:46:26] simple. You can train it on one GPU.
[00:46:28] Um and uh what we need to do with this
[00:46:31] technique is scale it up basically.
[00:46:34] There's a few other things that we need
[00:46:35] to do, but that's the the main one.
[00:46:38] Uh and so in simple cases you can train
[00:46:40] this world model and you can use it to
[00:46:42] plan simple actions in like in a push T
[00:46:45] or like simple robotic situation in
[00:46:47] simulated environments.
[00:46:49] Um so that needs to be scaled up, but
[00:46:50] it's it's sort of a a good work. There
[00:46:52] is a a theoretical paper that uh
[00:46:55] we put out just a few days ago
[00:46:58] where if you make the hypothesis that
[00:47:00] the underlying distribution
[00:47:02] of your data is actually an isotropic
[00:47:04] Gaussian,
[00:47:07] if you assume that the observations you
[00:47:08] get from the world are some sort of
[00:47:10] complicated non-linear transformation
[00:47:13] of those points, like in this case like
[00:47:15] some sort of spiral
[00:47:17] uh
[00:47:18] transformation,
[00:47:20] you apply you train a neural net with
[00:47:22] Sigreg on it, it will recover the
[00:47:24] original
[00:47:26] Gaussian in the representation space.
[00:47:28] Okay?
[00:47:29] So
[00:47:30] it's not a proof that it works in every
[00:47:32] case, but it's a
[00:47:33] proof that if your original
[00:47:36] explanatory variables are
[00:47:38] Gaussian,
[00:47:40] the system will recover those variables
[00:47:42] up to a rotation.
[00:47:47] Okay. So we we can use those techniques
[00:47:50] to
[00:47:52] in in the context of self-supervised
[00:47:53] learning to train an image recognition
[00:47:54] system uh
[00:47:56] and there is another set of technique
[00:47:58] which I should mention because they work
[00:48:00] really well and they are the ones that
[00:48:02] have been scaled up so far. C-reg is
[00:48:05] conceptually my favorite method but it's
[00:48:07] very recent and we haven't scaled it up.
[00:48:09] Whereas
[00:48:10] those other methods that are based on
[00:48:11] distillation we scaled them up and we
[00:48:13] got really good results both for images
[00:48:15] and video
[00:48:16] with techniques like I-jeppa and
[00:48:18] V-jeppa. So what's the basic idea of
[00:48:20] those distillation methods? You you
[00:48:22] still have those two encoders so this is
[00:48:24] a jeppa architecture
[00:48:25] you take a an input you transform it or
[00:48:28] corrupt it or mask it or something and
[00:48:30] then you train the system
[00:48:33] you know to predict in representation
[00:48:34] space but you don't propagate gradient
[00:48:36] through the encoder on the right.
[00:48:39] Okay, those are two encoders with
[00:48:41] identical
[00:48:42] architectures and they kind of share the
[00:48:44] weights but the funny thing is that the
[00:48:47] encoder on the right
[00:48:49] use
[00:48:50] a exponential moving average
[00:48:53] over time of the weights of the encoder
[00:48:55] on the left. The encoder on the left
[00:48:57] gets gradient and gets updated all the
[00:48:59] time.
[00:49:00] The encoder on the right gets updated
[00:49:02] slower essentially and share the
[00:49:04] weights.
[00:49:05] This is derived from
[00:49:07] some intuitive ideas
[00:49:09] some people at Google DeepMind who are
[00:49:11] using techniques like this to stabilize
[00:49:13] the variance in reinforcement learning
[00:49:15] and they realized you could apply this
[00:49:17] to self-supervised learning from images.
[00:49:19] They call this BYOL
[00:49:21] bootstrap your own latent and there is
[00:49:24] like a whole bunch of methods coming
[00:49:26] from Meta in particular
[00:49:28] SimSiam, MoCo etc. that use this
[00:49:30] exponential moving average idea and
[00:49:33] particular method called I-jeppa which I
[00:49:36] I show here
[00:49:37] it produced really really good results
[00:49:40] and what we were able to do with I-jeppa
[00:49:41] is compare the results of I-jeppa with a
[00:49:44] generative approach called MAE masked
[00:49:47] autoencoder.
[00:49:49] And
[00:49:49] it it's not only better but it is much
[00:49:52] faster to train.
[00:49:54] Um
[00:49:55] Another uh and another technique is is
[00:49:58] called DINO. Many of you
[00:50:00] I'm sure have heard of it. I know some
[00:50:02] of you have used it because there were
[00:50:03] projects in the robot demos that
[00:50:05] actually used DINO. Uh
[00:50:07] So, this is done by some of my former
[00:50:09] colleagues at Meta in Paris and it's
[00:50:12] completely self-supervised. It's a joint
[00:50:13] embedding architecture. It's using
[00:50:16] distillation, but with various tricks,
[00:50:18] which I'm not going to explain. Uh
[00:50:20] there's a lot of engineering that goes
[00:50:21] behind it. And those systems basically
[00:50:24] at this time produce the best generic
[00:50:26] representations of images. If you have
[00:50:27] any type of vision task that you want to
[00:50:30] to do, that's probably the best the best
[00:50:33] uh
[00:50:33] the best technique to I mean the best
[00:50:35] encoder for images. Okay, but what we've
[00:50:38] done is
[00:50:39] among other things use DINO as an
[00:50:40] encoder and then train a world model and
[00:50:42] do planning. Let me show you just a cute
[00:50:44] video on this.
[00:50:45] If if I can.
[00:50:48] Okay, so you have a initial state here
[00:50:50] of a kind of simulated environment that
[00:50:52] has pretty complex dynamics. And you
[00:50:54] have goals at the top and at the bottom
[00:50:56] what you see is the sequence of actions
[00:50:58] of a planner that uses this trained
[00:51:00] world model to get the world to a
[00:51:03] configuration as close as possible to
[00:51:05] the original one in less less than 25
[00:51:07] steps.
[00:51:09] Um and this uh
[00:51:12] has been applied to a number of
[00:51:13] different uh
[00:51:14] uh scenarios uh like double pendulum and
[00:51:19] and and push the in whatever.
[00:51:22] Um
[00:51:24] Now, I did that works really well. So,
[00:51:26] we uh
[00:51:27] we sent more recently applied it to
[00:51:29] video. So, there you take a video, you
[00:51:31] mask a big chunk of it, and you train
[00:51:33] the JAPA to again produce good
[00:51:35] representations so that you can predict
[00:51:37] the representation of full video from
[00:51:39] the representation of partially masked
[00:51:40] one. Once the system is trained, you use
[00:51:42] the encoder as a way to extract features
[00:51:44] from the video and you train a head on
[00:51:47] top of it to
[00:51:49] uh accomplish some task and it works
[00:51:51] like really well. It's state of the art
[00:51:53] for a lot of
[00:51:55] traditional vision task particularly
[00:51:57] from video like action recognition,
[00:51:58] action prediction and stuff like that.
[00:52:00] The one interesting thing that I want to
[00:52:02] mention
[00:52:03] instead of boring you with the table of
[00:52:04] results is
[00:52:06] is that those systems
[00:52:08] V-Jeppa in particular has has learned
[00:52:10] some level of common sense. So one thing
[00:52:11] we can do V-Jeppa because we train it to
[00:52:13] predict what's going to happen next in
[00:52:15] the video. We can try to predict her to
[00:52:16] do that.
[00:52:17] We can measure its internal prediction
[00:52:19] error. We can show it a video and
[00:52:21] monitor the internal prediction error at
[00:52:22] every every time step.
[00:52:24] The system takes a window of 16 frames.
[00:52:28] So we we just slide those those frames
[00:52:30] right on the on the video and measure
[00:52:32] the prediction error
[00:52:33] with for the next 50 16 frames.
[00:52:38] And the cool thing is that if you show
[00:52:39] it a video where something impossible
[00:52:42] occurs, something unphysical
[00:52:44] the prediction error shoots to the roof.
[00:52:46] So it's like the little girl in the one
[00:52:48] of the early slides like you know looks
[00:52:50] at the scene of the car not falling.
[00:52:53] Same thing. You have a video of a
[00:52:56] a ball being thrown and the ball
[00:52:58] disappears.
[00:53:01] Prediction error will shoot through the
[00:53:02] roof.
[00:53:05] So that's interesting because it's the
[00:53:06] first time
[00:53:08] at least from my point of view that I've
[00:53:10] seen
[00:53:11] completely self-supervised system
[00:53:13] acquire some level of common sense.
[00:53:16] It'll tell you what's possible, what's
[00:53:18] not possible.
[00:53:19] Um
[00:53:20] Let me skip this. It's cute but
[00:53:22] it's
[00:53:23] it just says V-Jeppa can be used for
[00:53:25] planning and you know
[00:53:27] this
[00:53:28] new versions of this that do a better
[00:53:30] job at planning and everything. But here
[00:53:31] is an interesting thing.
[00:53:33] Remember I told you
[00:53:34] the way babies learn that the world is
[00:53:36] three-dimensional is because it's the
[00:53:38] best way to explain how your view of the
[00:53:40] the changes when you move your head.
[00:53:41] Okay, so we took the representation
[00:53:43] learned by uh uh
[00:53:45] some version of VJ pack or VJ pack 2.1.
[00:53:47] And then we trained a head on top of it
[00:53:49] to predict depth from a single image.
[00:53:52] And it does a really good job.
[00:53:54] Um it's it's
[00:53:56] produces really good results. In fact,
[00:53:57] better than you know, V3.
[00:53:59] Uh and
[00:54:02] uh what that shows is that this system,
[00:54:04] by just being trained
[00:54:06] to predict to miss, you know, fill in
[00:54:08] the blanks in videos at a representation
[00:54:11] level,
[00:54:12] basically understands that the world is
[00:54:13] three-dimensional.
[00:54:15] I mean, understands with double quotes.
[00:54:17] Understands the notion of object. If you
[00:54:19] use the representation
[00:54:21] as input to a segmentation system, it it
[00:54:23] works decently well.
[00:54:25] Uh and for, you know, various other
[00:54:26] things. Okay, let me conclude.
[00:54:29] So,
[00:54:33] it's funny, huh?
[00:54:36] So, abandon generative models.
[00:54:41] I mean, if you work on LLM, of course.
[00:54:43] But you should not work on LLM.
[00:54:46] Uh at least if you're in academia, you
[00:54:47] should absolutely not work in LLM. There
[00:54:49] is nothing you can bring to the table.
[00:54:51] Uh so, abandon generative model in favor
[00:54:53] of joint embedding architectures. If you
[00:54:55] are interested in, you know,
[00:54:57] uh
[00:54:58] intelligence, abandon probabilistic
[00:55:00] models in favor of those energy-based
[00:55:02] models. I didn't have time to really
[00:55:04] kind of explain why.
[00:55:06] Uh
[00:55:07] I
[00:55:08] you know, I made an argument in favor of
[00:55:10] of those
[00:55:12] regularized methods or information
[00:55:14] maximization
[00:55:16] through
[00:55:17] through variables instead of samples.
[00:55:19] So, abandon contrastive methods,
[00:55:21] which again have a lot of
[00:55:23] practical applications.
[00:55:25] I've I've been saying for ever to
[00:55:29] abandon reinforcement learning. I don't
[00:55:30] really mean abandon. I mean, minimize
[00:55:32] its use because it's so so horribly
[00:55:35] inefficient in terms of sample
[00:55:36] efficiency. And I know there are people
[00:55:38] here who work on this, but
[00:55:40] uh
[00:55:41] but like, you know, RL is like
[00:55:43] what you do when you're desperate and
[00:55:45] there is nothing else you can do.
[00:55:47] Okay.
[00:55:48] Well, you like you have to do most of
[00:55:50] the learning,
[00:55:51] you know, in by observation.
[00:55:53] Uh you know, learning world models, blah
[00:55:55] blah blah. And once you have good
[00:55:56] representations, you know, you can use
[00:55:58] RL on top of it because you already have
[00:55:59] the good representations.
[00:56:01] Uh you you won't require too many
[00:56:03] samples. Sometimes you can't you can't
[00:56:05] avoid it.
[00:56:06] Uh and certainly, if you're interested
[00:56:08] in making real progress in AI,
[00:56:10] in sort of grounded, you know, AI for
[00:56:12] the real world, if you want,
[00:56:14] physical AI,
[00:56:16] don't work on LLMs. Don't work on
[00:56:17] generative models, either. So, as you
[00:56:19] can probably guess, this does not make
[00:56:22] me very popular in Silicon Valley.
[00:56:25] Yes.
[00:56:27] Um and so, I left Meta, as many of you
[00:56:31] probably know, at uh the end of last
[00:56:32] year and formed a new company called Ami
[00:56:34] Labs.
[00:56:35] And the purpose of uh Ami Labs is sort
[00:56:38] of AI for the real world, like, you
[00:56:40] know, physical AI.
[00:56:41] Uh robotics is a use case, but it's not
[00:56:43] just that. It's control of uh industrial
[00:56:46] processes. Like, anything that is
[00:56:48] high-dimensional, continuous, and noisy,
[00:56:51] for which LLMs are completely helpless.
[00:56:53] Um this is the kind of problems we're
[00:56:56] working on.
[00:56:58] And that's it. Thank you very much.
[00:57:01] >> [applause]
[00:57:12] >> Okay, so
[00:57:15] I know there's many questions. Maybe
[00:57:17] we'll take, you know, one or two, but
[00:57:19] then we have to to wrap up. So, and
[00:57:22] please quick questions and quick
[00:57:23] answers.
[00:57:24] >> Thanks for the talk. Uh I wanted to ask
[00:57:26] about the guardrails that you mentioned
[00:57:28] on the uh one of the earlier slides
[00:57:30] where you also talked about MPC.
[00:57:32] Engineers love MPC cuz they can put in
[00:57:34] their constraints, describe them in
[00:57:36] state space, like 3D space. But from
[00:57:38] what I understand, in your uh system,
[00:57:41] everything works in representation
[00:57:43] space.
[00:57:44] How do I even get a constraint like
[00:57:46] don't bump into the wall into this
[00:57:48] representation space? Do you envision
[00:57:50] the system learning the constraints by
[00:57:53] itself, or can engineers really put them
[00:57:55] in?
[00:57:56] >> No, you would have to learn uh a very
[00:57:58] small head on top of your
[00:58:00] representation that maps
[00:58:02] uh that to your
[00:58:05] you know, the constraint that you're
[00:58:06] interested in.
[00:58:07] Uh so, that part has to be trained, but
[00:58:09] you can train it with a very small
[00:58:10] number of samples because it's a tiny
[00:58:12] basically it's just a projection.
[00:58:14] >> But you need a different encoder for
[00:58:16] each kind of uh constraint that you
[00:58:18] might want to put in, no?
[00:58:19] >> Well, you need a a different projector
[00:58:21] for for each constraint, right. So, if
[00:58:23] if your task is to like open a door,
[00:58:26] I'm not talking about constraint, I'm
[00:58:27] talking about like a task objective. Uh
[00:58:29] you need some cost function to tell you
[00:58:30] like is the door open or not, right?
[00:58:33] And uh so, that might have to be trained
[00:58:35] when you're
[00:58:36] uh trained to
[00:58:37] accomplish the task, but basically that
[00:58:39] requires two samples.
[00:58:40] All right.
[00:58:41] >> Okay, I think we'll have to leave it
[00:58:42] here. Thank you, Jan, very much.
[00:58:44] >> All right. Thank you.
[00:58:46] >> [applause]
