# UC Berkeley EECS Colloquium: Ilya Sutskever — OpenAI
- **YouTube URL:** https://www.youtube.com/watch?v=RvEwFvl-TrY
- **Lines:** 1665

---

[00:00:00] So, about half and half. So,
[00:00:03] we do this every week. We try to get a
[00:00:06] fantastic speaker every week just like
[00:00:07] this week. And so, why don't you just
[00:00:10] make it a regular habit to
[00:00:12] set aside Wednesday afternoon and come
[00:00:14] and learn something? It's not always in
[00:00:17] the same field. You'll learn about
[00:00:18] different fields so that when you
[00:00:19] graduate, you're actually
[00:00:22] a person of all seasons. And you can you
[00:00:25] can
[00:00:26] face up to any kind of a challenge. And
[00:00:28] so, it's a it's an entire education even
[00:00:30] for the professors. It's an education to
[00:00:32] attend colloquium every week. Always
[00:00:35] learn something new. So,
[00:00:37] to introduce the speaker, let me ask
[00:00:39] Peter Abeel
[00:00:42] Everyone, it's a great pleasure to
[00:00:44] introduce Ilya Sutskever. Ilya did his
[00:00:47] PhD at the University of Toronto working
[00:00:49] with Jeff Hinton. Um
[00:00:51] then from there went on to do a post doc
[00:00:53] at Stanford, then founded a company, got
[00:00:57] acquired by Google.
[00:00:59] Uh from there
[00:01:00] uh founded OpenAI, the AI Institute in
[00:01:04] San Francisco largely funded by Elon
[00:01:07] Musk. And along the way Ilya's written a
[00:01:09] lot of the papers that a lot of us are
[00:01:11] building up on these days. For example,
[00:01:14] Ilya's paper on uh
[00:01:15] ImageNet from 20 2012, the first big
[00:01:19] deep learning results for image
[00:01:20] recognition,
[00:01:21] sparked the whole activity in in the
[00:01:23] field.
[00:01:24] After that, papers on more specifics on
[00:01:26] how to do this, dropout. Um also paper
[00:01:30] on sequence-to-sequence that showed that
[00:01:32] actually deep learning works for
[00:01:34] discrete objects like language and
[00:01:36] namely established new state-of-the-art
[00:01:38] machine translation.
[00:01:39] Some of the learn-to-execute papers for
[00:01:41] neural Turing machines.
[00:01:43] And more recently a lot of meta learning
[00:01:45] and reinforcement learning work. Uh one
[00:01:47] of the I think most notable things is
[00:01:49] that even though Ilya is still super
[00:01:51] young, turns out that
[00:01:53] just in 2017 his papers were cited
[00:01:55] 20,000 times just in one year. Uh please
[00:01:58] join me in WELCOMING ILYA.
[00:02:05] THANKS FOR THE INTRODUCTION, PETER.
[00:02:08] OKAY, SO thanks for thanks for stopping
[00:02:10] by my talk. I will
[00:02:13] give you an overview of some of the work
[00:02:14] that we've done at OpenAI over the past
[00:02:22] about some of the work we've done at
[00:02:24] OpenAI over the past year and this is
[00:02:27] like a
[00:02:29] an arrow subset that focus The talk will
[00:02:31] be
[00:02:33] a subset of that work focusing on meta
[00:02:35] learning and self-play, which are two
[00:02:37] topics I like very much.
[00:02:41] But I've been told that this is a more
[00:02:43] slightly broader, a little bit more of a
[00:02:45] general interest talk. So, I wanted to
[00:02:47] begin the presentation by talking a
[00:02:50] little bit about why deep learning
[00:02:52] actually works.
[00:02:57] And
[00:02:58] I think it's not a self-evident question
[00:03:01] why deep learning works. It's not
[00:03:03] self-evident that it should work.
[00:03:06] And I want to give
[00:03:08] some
[00:03:10] a perspective which I think is not
[00:03:11] entirely obvious on that.
[00:03:14] So, one thing that you can actually
[00:03:16] prove mathematically
[00:03:17] that the best possible way
[00:03:20] of generalizing that's completely
[00:03:22] unprovable
[00:03:24] is to find the best short program that
[00:03:26] explains your data and then use that to
[00:03:29] make predictions.
[00:03:31] And you can prove that it's impossible
[00:03:32] to do better than that.
[00:03:33] So, if you think about machine learning,
[00:03:36] you need to think about concept classes.
[00:03:37] What are you looking for given the data?
[00:03:40] And if you're looking for the best short
[00:03:41] program, it's impossible to generalize
[00:03:43] better than that.
[00:03:45] And it can be proved and the proof is
[00:03:46] not even that complicated.
[00:03:50] And like the intuition of it basically
[00:03:53] is that any regularity any regularity
[00:03:56] that can possibly exist is expressible
[00:03:58] as a short program. If you have some
[00:04:00] piece of data which cannot be compressed
[00:04:02] with a slightly shorter program, then
[00:04:04] that piece of data is totally random.
[00:04:07] So,
[00:04:08] you can take my word on it that it
[00:04:10] therefore follows
[00:04:12] that short programs are the best
[00:04:13] possible way to generalize if only we
[00:04:15] could use them.
[00:04:17] Problem is
[00:04:18] it is impossible to find the best short
[00:04:20] program that describes the data.
[00:04:22] At least given today's knowledge,
[00:04:25] the computational problem of finding the
[00:04:27] best short program is intractable in
[00:04:29] practice, undecidable in theory.
[00:04:32] So, no short programs for us.
[00:04:35] But
[00:04:36] what about small circuits? Small
[00:04:38] circuits are the next best thing
[00:04:41] after short programs cuz
[00:04:43] a short a small circuit can also
[00:04:46] performs
[00:04:47] non-obvious computation. If you have a
[00:04:49] really deep
[00:04:50] really wide circuit, maybe you know,
[00:04:52] many many thousand layers and many
[00:04:54] millions of neurons wide, you can run
[00:04:56] lots of different algorithms on the
[00:04:58] inside.
[00:04:59] So, it comes close. It comes close to
[00:05:01] short programs.
[00:05:03] And extremely fortunately,
[00:05:05] the problem of finding
[00:05:08] the best small circuit given the data is
[00:05:10] solvable with backprop.
[00:05:14] And so,
[00:05:16] basically, what it boils down to is that
[00:05:19] we can find the best small circuit that
[00:05:20] explains the data.
[00:05:22] And small circuits are kind of like
[00:05:23] programs but not really. They're a
[00:05:25] little bit worse. It's like finding the
[00:05:27] best
[00:05:29] parallel program that runs for 100 or
[00:05:32] less, 50 steps that solves your problem.
[00:05:35] And that's where the generalization
[00:05:36] comes from.
[00:05:38] Now,
[00:05:40] we don't know why don't know exactly why
[00:05:43] backpropagation is successful at finding
[00:05:45] the best short circuit
[00:05:48] given given your data.
[00:05:51] It's a mystery and it's a very fortunate
[00:05:53] mystery. It powers all the progress that
[00:05:54] we've made in
[00:05:55] all the progress that's been made in
[00:05:58] artificial intelligence over the past 6
[00:05:59] years.
[00:06:01] So, I think
[00:06:03] there is an element of luck here. We are
[00:06:04] lucky that it works.
[00:06:07] One thing which I One useful analogy
[00:06:09] that I like
[00:06:11] to make when thinking about
[00:06:12] generalization
[00:06:14] is that
[00:06:15] models
[00:06:17] learning models that in some ways have
[00:06:19] greater computational power
[00:06:21] generalize better.
[00:06:23] So, you could make this you could make
[00:06:25] the case that the deeper your neural
[00:06:27] network is,
[00:06:28] the closer it comes to the
[00:06:31] ultimate best short program and so the
[00:06:32] better it will generalize.
[00:06:37] So, that's that's tries to touch on the
[00:06:39] question of where does generalization
[00:06:41] come from?
[00:06:43] I think the full answer is going to be
[00:06:46] unknown for quite some time because it
[00:06:47] also has to do with the specific data
[00:06:49] that we happen to want to solve.
[00:06:52] It is very nice indeed that the problems
[00:06:54] we want to solve happen to be solvable
[00:06:56] with these classes of models.
[00:07:00] One other statement I want to make is
[00:07:02] that
[00:07:05] I think that the backpropagation
[00:07:06] algorithm is going to stay with us until
[00:07:08] the very end because the problem that it
[00:07:10] solved is so fundamental, which is given
[00:07:13] data, find the best small circuit that
[00:07:16] fits to it.
[00:07:18] It seems unlikely that this problem that
[00:07:20] we will not want to to solve this
[00:07:21] problem in the future.
[00:07:23] And so, for this reason I feel like
[00:07:26] backprop is really important.
[00:07:30] Now, I want to spend a little bit of
[00:07:32] time talking about reinforcement
[00:07:34] learning.
[00:07:36] And so,
[00:07:37] reinforcement learning is a framework
[00:07:40] for describing the behavior of agents.
[00:07:43] You've got an agent which takes actions,
[00:07:45] interacts with an environment,
[00:07:47] and receives rewards when it succeeds.
[00:07:52] And it's pretty clear that it's a very
[00:07:54] general framework.
[00:07:56] But the thing that makes reinforcement
[00:07:57] learning interesting is that there exist
[00:08:00] useful algorithms in reinforcement
[00:08:02] learning. So, in other words, the
[00:08:03] algorithms
[00:08:05] of reinforcement learning make the
[00:08:06] framework interesting.
[00:08:08] Even though these algorithms have still
[00:08:09] a lot of room for improvement, they can
[00:08:11] already succeed in lots of non-obvious
[00:08:13] tasks.
[00:08:16] And so, therefore it's worth pushing on
[00:08:17] these algorithms. If you make a really
[00:08:19] good reinforcement learning algorithms,
[00:08:20] perhaps we'll build very clever agents.
[00:08:23] And so,
[00:08:25] the way the way the reinforcement
[00:08:27] learning problem is formulated
[00:08:29] is
[00:08:32] as follows. You have some
[00:08:35] policy class where policy is just some
[00:08:37] function which takes inputs and produces
[00:08:40] actions.
[00:08:41] And for any given policy, you can run it
[00:08:43] and you can figure out its performance,
[00:08:46] its cost.
[00:08:48] And your goal is just to find the best
[00:08:50] policy that minimizes cost, maximizes
[00:08:53] reward rewards.
[00:08:55] Now, one way in which this framework
[00:08:56] formulation is different from reality is
[00:08:59] that in reality
[00:09:00] the agents generate the rewards to
[00:09:02] themselves.
[00:09:05] And the only true cost function
[00:09:08] that exists is survival.
[00:09:15] So,
[00:09:16] the
[00:09:17] if you want to build good reinforcement
[00:09:20] any reinforcement learning algorithm at
[00:09:21] all, you need to represent the policy
[00:09:22] somehow.
[00:09:24] So, how are you going to represent
[00:09:25] anything? The answer is always through
[00:09:27] using a neural network.
[00:09:29] The neural network is going to take the
[00:09:31] actions and produce take the
[00:09:32] observations and produce actions.
[00:09:34] And then for a given setting of the
[00:09:36] parameters, you could
[00:09:39] figure out how you could calculate how
[00:09:41] good they are.
[00:09:42] And then you could calculate you could
[00:09:43] you could figure out how to compute
[00:09:45] the way to change these parameters to
[00:09:47] improve the model.
[00:09:49] So, if you make if you change the
[00:09:50] parameters of the model many times and
[00:09:52] make many small improvements,
[00:09:54] then you may make a big improvement.
[00:09:56] And very often in practice, the
[00:09:58] improvement ends up being
[00:10:00] big enough to solve the problem.
[00:10:03] So, I want to talk a little bit about
[00:10:05] how reinforcement learning algorithms
[00:10:06] work.
[00:10:09] The modern ones, the model-free ones,
[00:10:11] the one that everyone the ones that
[00:10:12] everyone uses today.
[00:10:14] And
[00:10:16] you take a policy and you add a little
[00:10:18] bit of randomness to your actions
[00:10:19] somehow.
[00:10:21] So, you deviate from your usual
[00:10:23] behavior.
[00:10:25] And then you simply check
[00:10:27] if the resulting cost was better than
[00:10:30] expected.
[00:10:32] And if it is,
[00:10:34] you make it more likely. By the way, I
[00:10:36] want for the for for um
[00:10:38] I'm actually curious. How many people
[00:10:40] are familiar with the basics? Please
[00:10:43] raise your hand.
[00:10:44] Okay, so the audience here is informed,
[00:10:46] so I can skip through the introductory
[00:10:48] parts.
[00:10:49] Don't don't skip too much.
[00:10:53] All right.
[00:10:55] I'll skip only a little bit.
[00:10:59] But the point is, you do something
[00:11:01] randomly and you see if it's better than
[00:11:03] usual. And if it is, do more of that.
[00:11:06] And do a lot of and repeat this many
[00:11:08] times.
[00:11:11] So,
[00:11:12] in reinforcement learning, there are two
[00:11:13] classes of algorithms.
[00:11:16] One of them is called policy gradients,
[00:11:18] which is basically what I just
[00:11:20] described.
[00:11:21] And there is a beautiful formula above
[00:11:24] which says that if you just take
[00:11:27] of your cost function and do a little
[00:11:29] bit of math, you get something which is
[00:11:31] exactly as described where you just take
[00:11:33] random take some random actions with a
[00:11:36] little bit of randomness.
[00:11:37] And if the result is better than
[00:11:38] expected, then increase the probability
[00:11:40] of taking these actions in the future.
[00:11:43] Then there is also the Q-learning
[00:11:44] algorithm, which is a little bit less
[00:11:46] stable,
[00:11:47] a little bit more sample efficient.
[00:11:49] Won't explain too detail in too much
[00:11:51] detail how it how it works,
[00:11:53] but it has the property that it is
[00:11:54] off-policy.
[00:11:56] Which means
[00:11:58] that it can learn not just from its own
[00:12:01] actions. And I want to explain what it
[00:12:03] means.
[00:12:04] On-policy means that you can only learn
[00:12:07] you can only
[00:12:10] learn at all if you're the one who's
[00:12:12] taking the actions.
[00:12:14] While off-policy means that you can
[00:12:16] learn from anyone's other anyone's
[00:12:18] actions. It doesn't just have to be your
[00:12:20] own. So, it's a bit more It seems like a
[00:12:22] more useful thing. Although, it's
[00:12:23] interesting that the algorithm which is
[00:12:25] more stable
[00:12:28] the the stable algorithms tend to be
[00:12:29] policy gradient-based, the on-policy
[00:12:31] ones.
[00:12:32] The ones that are the Q-learning
[00:12:34] Q-learning, which is off-policy, is also
[00:12:35] less stable, at least as of today.
[00:12:38] Things change quickly.
[00:12:41] Now, I'll spend a little bit of time
[00:12:43] illustrating how Q-learning works,
[00:12:45] even though I think it may be familiar
[00:12:48] this may be familiar with many to many
[00:12:49] people.
[00:12:50] And basically, you have this Q-function,
[00:12:51] which tries to estimate for a given
[00:12:53] state and a given action how good or bad
[00:12:56] the future is going to be.
[00:12:59] And
[00:13:00] you have this trajectory of states
[00:13:02] because you your agent is taking many
[00:13:03] actions in the world. It's
[00:13:05] relentlessly pursuing a goal.
[00:13:09] Well, the Q-function is a
[00:13:11] recur recur recursive property where the
[00:13:14] Q-function of SA
[00:13:15] is basically just the Q-function of
[00:13:18] S'A' plus the reward you got earlier.
[00:13:21] So, you got this recursivity and you can
[00:13:23] use this recursivity to estimate the
[00:13:24] Q-function. That gives you the
[00:13:26] Q-learning algorithm and I won't explain
[00:13:29] why it's off-policy. All you need is to
[00:13:32] um for for the purposes of this
[00:13:34] presentation, just take my word for it.
[00:13:38] And now,
[00:13:39] what's the potential here? Why is this
[00:13:40] exciting?
[00:13:41] So, yes, the reinforcement learning
[00:13:43] algorithms that we have right now, they
[00:13:44] are very sample inefficient.
[00:13:46] They are really bad at exploration yet,
[00:13:48] although progress is being made.
[00:13:52] But you can kind of see that if you had
[00:13:54] a really
[00:13:55] great reinforcement learning algorithm
[00:13:57] that would be just really data efficient
[00:14:01] and explore really well and make really
[00:14:03] good use of
[00:14:05] lots of sources of information,
[00:14:07] then we'd be in good shape in terms of
[00:14:10] the go in terms of building intelligent
[00:14:12] agents.
[00:14:14] But we still have work to do.
[00:14:16] We're still a little bit data
[00:14:17] inefficient.
[00:14:20] So, now I want to talk a little bit
[00:14:21] about meta-learning, which it will be
[00:14:23] um
[00:14:24] an important part of this talk.
[00:14:27] And I want to explain what it is.
[00:14:29] So, so there is the abstract the the
[00:14:32] dream of meta-learning, the abstract
[00:14:33] idea that meta-learning is the idea that
[00:14:35] you can learn to learn.
[00:14:37] Kind of in the same way in which
[00:14:40] biological evolution has learned the
[00:14:43] learning algorithm of the brain.
[00:14:47] And spiritually, the way you'd approach
[00:14:49] this problem
[00:14:51] is by training a system
[00:14:53] not on one task, but on many tasks.
[00:14:57] And if you do that, then suddenly you've
[00:14:59] trained your system to solve new tasks
[00:15:02] really quickly.
[00:15:05] So, that'd be a nice thing if you could
[00:15:06] do that.
[00:15:07] It'd be great if we could learn to
[00:15:08] learn. We won't need to design the
[00:15:09] algorithms ourselves.
[00:15:11] Use the learning algorithm that we have
[00:15:13] right now to do the rest of the thinking
[00:15:15] for us.
[00:15:17] We're not quite there yet, but
[00:15:19] meta-learning has had
[00:15:22] a fair bit of success. And I just want
[00:15:24] to show um explain the dominant the
[00:15:29] most common way of doing meta-learning.
[00:15:32] The most common way of doing
[00:15:33] meta-learning is the most attractive one
[00:15:35] where you basically say that you you
[00:15:37] want to reduce the problem of
[00:15:38] meta-learning
[00:15:40] to traditional deep learning.
[00:15:42] Where you basically
[00:15:43] take your
[00:15:45] familiar supervised learning framework
[00:15:48] and you replace each data point with a
[00:15:51] task from your training set of tasks.
[00:15:54] And so, what you do is that all all
[00:15:55] these algorithms have the same kind of
[00:15:57] high-level shape where
[00:15:59] you have a model which receives
[00:16:01] information about the task plus any task
[00:16:05] instance and it needs to make the
[00:16:06] prediction.
[00:16:09] And it's pretty easy to see that if you
[00:16:10] do that, then you will train a model
[00:16:11] which can receive a new description of a
[00:16:13] task
[00:16:15] and make good predictions there.
[00:16:19] And there have been some very um
[00:16:21] some pretty successful compa- compelling
[00:16:24] success stories and I'll mention some of
[00:16:26] them. A lot of a lot of meta-learning
[00:16:27] work was done
[00:16:28] in Berkeley as well, but I'll mention
[00:16:31] some of the visual ones, the early ones
[00:16:33] that I think are notable
[00:16:35] because you see this task right here,
[00:16:38] it's I took this figure from paper by
[00:16:41] Brendan Lake et al.
[00:16:43] And this
[00:16:44] but I think the data set
[00:16:46] came earlier, so this isn't the right
[00:16:48] citation.
[00:16:50] But
[00:16:54] one of the criticisms of
[00:16:56] one of the ways in which neural networks
[00:16:58] are criticized is that
[00:17:02] they can't learn quickly, which is kind
[00:17:04] of true.
[00:17:07] And
[00:17:09] a team in Josh Tenenbaum's lab had
[00:17:11] developed this
[00:17:13] data set, which has a very large number
[00:17:15] of different
[00:17:17] characters and a very small number of
[00:17:19] examples for each character.
[00:17:21] Specifically as a challenge for neural
[00:17:22] networks.
[00:17:24] And it turns out that the simple
[00:17:26] meta-learning approach where you just
[00:17:27] say
[00:17:29] that I want to train a neural network
[00:17:30] that can learn to recognize any
[00:17:32] character really quickly, that approach
[00:17:34] works super well. And it's been able to
[00:17:36] get
[00:17:37] superhuman performance and as far as I
[00:17:40] know, the best performance is achieved
[00:17:41] by Misha et al. and I believe it's the
[00:17:43] work done with Peter.
[00:17:46] And they it's basically superhuman.
[00:17:49] And it's just a neural net. So,
[00:17:52] meta-learning sometimes work really
[00:17:53] well.
[00:17:55] There is also a very different take on
[00:17:57] meta-learning, which is a lot more
[00:18:00] which is a lot closer to the approach of
[00:18:02] instead of learning the parameters of a
[00:18:03] big model,
[00:18:05] let's learn something compact and small,
[00:18:07] like the architecture
[00:18:09] or even the algorithm, which is what
[00:18:10] evolution did. And here you just say,
[00:18:13] why don't you search in architecture
[00:18:15] space and find the best architecture?
[00:18:17] This is also a form of meta-learning.
[00:18:19] It also generalizes really well because
[00:18:20] this work
[00:18:22] if you do if you learn an architecture
[00:18:24] on a small image data set, it will work
[00:18:26] really well on a large image data set as
[00:18:27] well.
[00:18:29] And the reason it generalizes well is
[00:18:30] because the amount of information in
[00:18:34] an architecture is small.
[00:18:36] And this is work from a Google by
[00:18:38] Zoph and Le.
[00:18:41] So, meta-learning works.
[00:18:43] Sometimes there are signs of life. The
[00:18:46] promise is very strong. It's just so
[00:18:47] compelling. Yeah, you just
[00:18:49] just set everything right and then your
[00:18:51] existing learning algorithm will learn
[00:18:53] the learning algorithm of the future.
[00:18:55] That would be nice.
[00:18:58] So, now I want to
[00:19:00] dive into
[00:19:03] a detailed description of uh
[00:19:08] one algorithm that we've done. It's
[00:19:10] called hindsight experience replay.
[00:19:12] And it's been a large collaboration with
[00:19:14] many people,
[00:19:15] driven um primarily by Andrychowicz et
[00:19:17] al.
[00:19:18] And this is not exactly meta-learning.
[00:19:20] This is almost meta-learning.
[00:19:23] And
[00:19:27] basically,
[00:19:28] what happened there is that
[00:19:36] the way to think about what this
[00:19:37] algorithm does is that you try to solve
[00:19:39] a
[00:19:42] a hard problem
[00:19:45] by making it harder.
[00:19:47] And as a result, it becomes easier.
[00:19:49] And so, you frame one problem into the
[00:19:52] into the context of many problems.
[00:19:55] You have very many problems
[00:19:57] that you're going to solve
[00:19:57] simultaneously, and that makes it easy.
[00:20:01] And the problem here is basically a
[00:20:02] combination of exploration, where in
[00:20:06] reinforcement learning,
[00:20:07] we need to take the right action.
[00:20:09] If you don't take the right action, you
[00:20:10] don't learn. If you don't get rewards,
[00:20:12] how can you improve?
[00:20:14] All your effort that doesn't lead to
[00:20:15] rewards will be wasted.
[00:20:17] It'd be nice if we didn't have that.
[00:20:20] And so,
[00:20:22] if our rewards are sparse,
[00:20:25] if you try to achieve our goal and to
[00:20:26] fail,
[00:20:28] the model doesn't learn. So, how do we
[00:20:29] fix that?
[00:20:30] So, it's a really simple idea. It's
[00:20:32] super intuitive. You basically say
[00:20:34] you have the starting point,
[00:20:37] you try to reach the state A, but you
[00:20:39] reach the state B instead.
[00:20:42] And
[00:20:46] so, what can we learn something from
[00:20:48] this?
[00:20:50] Well, we we have a data we have a
[00:20:51] trajectory of how to reach the state B.
[00:20:54] So, maybe we can use this
[00:20:56] flawed attempt at reaching A as an
[00:20:58] opportunity to learn the state B.
[00:21:01] And so, this is very
[00:21:05] correct directionally.
[00:21:09] Means that you don't waste experience,
[00:21:11] and you but you need an off-policy
[00:21:12] algorithm in order to learn it, and
[00:21:14] that's why I've emphasized off-policy
[00:21:15] stuff earlier.
[00:21:16] Because your policy tries to reach A,
[00:21:20] but you're going to use this data to
[00:21:21] teach a different policy which reaches
[00:21:22] B.
[00:21:23] So, you have this big parameterized
[00:21:27] function,
[00:21:31] and you just simply tell it
[00:21:33] which state you reach. Like, it's it's
[00:21:35] too super It's super super
[00:21:36] straightforward.
[00:21:38] And it's intuitive, and it works really
[00:21:39] well, too.
[00:21:43] Hindsight experience replay. So, I'm
[00:21:44] going to show you the video.
[00:21:46] It's a
[00:21:48] It's pretty cool.
[00:21:53] And so, in this case, the reward is very
[00:21:54] sparse and binary,
[00:21:56] and
[00:22:00] so, so I should I should just say
[00:22:02] because the reward is sparse and binary,
[00:22:03] this makes it very hard for traditional
[00:22:06] reinforcement learning algorithms.
[00:22:08] Because you never get to see the reward.
[00:22:10] If you were to shape your reward,
[00:22:12] perhaps you could solve these problems a
[00:22:14] little bit better. Although, we still
[00:22:15] found it um
[00:22:17] you know, when the people that that were
[00:22:18] working on this tried it, they still
[00:22:20] found it difficult.
[00:22:23] But, this algorithm just works
[00:22:26] on these cool tasks. And it just The
[00:22:28] videos look cool.
[00:22:31] So, let's keep watching.
[00:22:34] You get these very nice
[00:22:35] confident-looking movements
[00:22:37] from the hindsight experience replay
[00:22:38] algorithm.
[00:22:41] And it just makes sense. Like, anytime
[00:22:43] something happens, we want to learn from
[00:22:44] it. And so, we want this to be the basis
[00:22:46] of all future algorithms.
[00:22:54] Now, again, this is in the absolutely
[00:22:57] sparse binary reward setting,
[00:22:59] which means that the standard
[00:23:01] reinforcement learning algorithms are
[00:23:02] very disadvantaged.
[00:23:04] But, even if you try to shape a reward,
[00:23:06] what's one thing that you discover is
[00:23:07] that shaping rewards is sometimes easy,
[00:23:10] but sometimes quite challenging.
[00:23:13] And here is the same thing working on
[00:23:16] uh
[00:23:17] real physical blocks.
[00:23:22] Okay. So, this is the
[00:23:26] This This basically sums sums up the
[00:23:28] hindsight experience replay results. Can
[00:23:30] you tell us what acronym is represented
[00:23:32] by HER? Hindsight experience replay.
[00:23:36] And
[00:23:37] like, what you can see is like the If
[00:23:38] you want to One of the limitations of
[00:23:40] all these results
[00:23:42] is that they
[00:23:44] the state is very low dimensional.
[00:23:48] And if you have a general environment
[00:23:49] with very high dimensional inputs and
[00:23:51] very long histories,
[00:23:52] you got the question of how do you
[00:23:54] represent your goals?
[00:23:56] And so, what it means is that
[00:23:57] representation learning is going to be
[00:23:58] very important.
[00:24:01] And unsupervised learning is probably
[00:24:04] doesn't work yet, but I think it's
[00:24:06] pretty close.
[00:24:08] And we should keep thinking about how to
[00:24:10] really fuse unsupervised learning with
[00:24:12] reinforcement learning. I think this is
[00:24:14] a
[00:24:14] fruitful area for the future.
[00:24:17] Now, I want to talk about a different
[00:24:19] project on using on on doing transfer
[00:24:23] from sim to real with meta learning, and
[00:24:25] this work is by Peng et al.
[00:24:28] And multiple people who did this work
[00:24:30] are from Berkeley. Unfortunately, I
[00:24:31] don't
[00:24:33] have the full list here.
[00:24:35] So,
[00:24:38] it would be nice if you could train our
[00:24:39] robots in simulation and then deploy
[00:24:42] them
[00:24:43] on physical robots.
[00:24:44] Simulation is easy to work with.
[00:24:48] But, it's also very clear that you can't
[00:24:50] simulate most things.
[00:24:52] So, then
[00:24:54] can anything be done here?
[00:24:57] And I just want to explain one very
[00:24:59] simple idea of how you could do that.
[00:25:02] And the answer is basically
[00:25:04] you
[00:25:05] train a policy that doesn't just solve
[00:25:08] the task in one simulated setting,
[00:25:10] but it solves the task in a family of
[00:25:12] simulated settings. So, what does it
[00:25:14] mean? You say, "Okay, I'm going to
[00:25:16] randomize the friction coefficients and
[00:25:18] gravity and
[00:25:20] pretty much anything you can think of,
[00:25:22] the length of your robotic limbs and
[00:25:24] their masses and their frictions and
[00:25:26] sizes."
[00:25:28] And your policy isn't told what you've
[00:25:30] done. You just need to figure it It
[00:25:32] needs to figure it out by interacting
[00:25:34] with the environment.
[00:25:37] Well, if you do that, then you'll
[00:25:39] develop a robust policy that's pretty
[00:25:41] good at figuring out what's going on, at
[00:25:43] least in these simulations.
[00:25:45] And if this is done, then
[00:25:49] the resulting system will be much more
[00:25:50] likely
[00:25:55] to
[00:25:56] generalize its knowledge from the
[00:25:57] simulation to the real world. And this
[00:26:00] is an instance of meta learning because
[00:26:01] in effect, you're learning
[00:26:04] a policy
[00:26:05] which is very quick
[00:26:08] at identifying the
[00:26:10] precise physics you're using. So, I
[00:26:11] would say this is a little bit I mean,
[00:26:12] calling it meta learning is a bit of a
[00:26:13] stretch. It's more of a kind of a robust
[00:26:16] adaptive dynamic thing.
[00:26:20] But, it also has a meta learning feel to
[00:26:22] it.
[00:26:24] I want to show this video of the
[00:26:25] baseline.
[00:26:29] So, this is what happens when you don't
[00:26:35] This is what happens when you don't do
[00:26:37] this robustification of the policy.
[00:26:40] So, you try to get the hockey puck into
[00:26:42] the red
[00:26:44] uh dot, and it just fails really
[00:26:47] dramatically.
[00:26:49] And um
[00:26:55] doesn't look very good. And if you add
[00:26:57] these robustifications,
[00:26:59] then the result is a lot better.
[00:27:02] Then it's like, you know, even when it
[00:27:03] pushes it around and it overshoots, it's
[00:27:05] just no problem.
[00:27:17] So, it looks pretty good.
[00:27:20] So, I think
[00:27:22] this toy example illustrates that the
[00:27:24] approach of
[00:27:26] training a policy in simulation
[00:27:29] and then making sure that the policy
[00:27:31] doesn't solve just one instance of the
[00:27:32] simulation, but many different instances
[00:27:34] of it,
[00:27:35] and figures out which one it is,
[00:27:44] then
[00:27:46] it could succeed in generalizing to the
[00:27:48] real to the real physical robot.
[00:27:51] So, that's encouraging.
[00:27:53] Now, I want to talk about another
[00:27:55] project by Franc et al.
[00:28:01] And
[00:28:03] it's about doing hierarchical
[00:28:04] reinforcement learning.
[00:28:07] So, hierarchical reinforcement learning
[00:28:08] is one of those ideas that would be nice
[00:28:11] if we could
[00:28:14] get it to work.
[00:28:16] Because one of the problems with
[00:28:17] reinforce with reinforcement learning as
[00:28:19] it's currently done today
[00:28:21] is that you have very long horizons,
[00:28:25] which you have trouble dealing with. And
[00:28:27] you have trouble dealing with that.
[00:28:29] Exploration is not very directed, so
[00:28:32] it's not as fast as you would like.
[00:28:35] And the credit assignment is challenging
[00:28:36] as well.
[00:28:41] And so, we can do a very simple meta
[00:28:43] learning approach, where
[00:28:47] you basically say
[00:28:49] that you want to learn low-level actions
[00:28:52] which make learning fast. So, you have a
[00:28:54] distribution over tasks,
[00:28:56] and
[00:29:02] you have a distribution over tasks,
[00:29:04] and you want to
[00:29:06] find a set of low-level policies such
[00:29:10] that
[00:29:11] if you use them inside a reinforcement
[00:29:13] learning algorithm,
[00:29:15] you learn as quickly as possible.
[00:29:18] And so, if you do that,
[00:29:20] you can learn pretty sensible locomotion
[00:29:23] strategies that go in a persistent
[00:29:24] direction.
[00:29:35] And so,
[00:29:39] here it is. You got three policies.
[00:29:41] They're high-level, and the
[00:29:44] the system has been learned to find to
[00:29:46] find the policies that will solve
[00:29:48] problems like this. And there is a
[00:29:50] specific distribution over this kind of
[00:29:52] problems that solve this quickly as
[00:29:53] possible.
[00:29:55] So,
[00:29:56] that's pretty nice.
[00:29:59] Now,
[00:30:01] one thing I want to mention here
[00:30:03] is
[00:30:05] the one important limitation of high
[00:30:07] capacity meta learning.
[00:30:09] So, there are two kinds of there are two
[00:30:11] ways to do meta learning. One is by
[00:30:14] learning a big neural network that can
[00:30:17] quickly solve problems in your
[00:30:19] distribution of tasks.
[00:30:22] And
[00:30:24] the other one is by learning an
[00:30:26] architecture or an algorithm. So, you
[00:30:28] learn a small object.
[00:30:30] So, if you learn an architecture, if you
[00:30:31] learn an algorithm in a meta learning
[00:30:33] setting, it will likely generalize to
[00:30:36] many other tasks.
[00:30:38] But this is not the case, or at least it
[00:30:40] is much less the case for high capacity
[00:30:42] meta learning.
[00:30:43] Where if you just wanted, for example,
[00:30:44] train a very large recurrent neural
[00:30:46] network,
[00:30:50] you want to learn a very large recurrent
[00:30:51] neural network that
[00:30:53] solves
[00:30:56] many tasks. It will be very committed to
[00:31:00] the distribution of tasks that you've
[00:31:02] trained it on.
[00:31:04] And if you give it a task that's
[00:31:04] meaningfully outside of the
[00:31:05] distribution, it will not succeed.
[00:31:08] So, as a kind of a slightly
[00:31:12] the kind of example I have in mind is,
[00:31:14] well, let's say you take your system and
[00:31:15] you train it to do math, you know, a
[00:31:16] little bit of math, and you teach it a
[00:31:18] little bit of programming, and you teach
[00:31:19] it how to read, could it do chemistry?
[00:31:23] Well, not according to this paradigm, at
[00:31:24] least not obviously.
[00:31:26] Because it really needs to have the task
[00:31:28] to come from the same distribution of
[00:31:30] the training and at and and in test
[00:31:32] time.
[00:31:34] So, I think for this to work, we will
[00:31:36] need to improve our the generalization
[00:31:37] of our algorithms further.
[00:31:41] And now I want to finish by talking
[00:31:42] about self-play.
[00:31:47] I think self-play is a really cool
[00:31:48] topic.
[00:31:50] It's been around for a long time.
[00:31:53] And
[00:31:58] I think it's really interesting and
[00:32:00] intriguing and mysterious.
[00:32:03] And I want to start by talking about the
[00:32:06] uh very
[00:32:09] earliest work on self-play that I know
[00:32:11] of.
[00:32:12] And that's TD-Gammon. It was done back
[00:32:14] in 1992.
[00:32:17] It was by Tesauro.
[00:32:20] Single author work.
[00:32:22] And in this work, they've used
[00:32:24] Q-learning with self-play
[00:32:27] to train a neural network that beats the
[00:32:29] world champion in backgammon.
[00:32:31] So, I think this may sound familiar in
[00:32:33] 2017 and 2018. But that's in 1992.
[00:32:37] That's back when your CPUs were of like,
[00:32:39] I don't know, 33 MHz or something.
[00:32:42] And if you look at this plot, you see it
[00:32:44] shows the performance as a function of
[00:32:45] time with different numbers of hidden
[00:32:48] units. You see, okay, you have 10 hidden
[00:32:49] units,
[00:32:50] which that's the red that's the red the
[00:32:52] red curve, and 20 hidden units is the
[00:32:55] green curve, all the way to the purple
[00:32:56] curve.
[00:32:58] And yeah, it's basically nothing changed
[00:33:00] in 25 years, just the number of zeros in
[00:33:02] the number of hidden units.
[00:33:06] And in fact, they've even discovered
[00:33:08] unconventional strategies
[00:33:10] that surprised experts in backgammon.
[00:33:14] So, that's just amazing.
[00:33:17] That this that this work was done so
[00:33:18] long ago and it had so it was looking
[00:33:20] forward into the future so much.
[00:33:23] And this approach basically remained
[00:33:25] dormant. People were trying it out a
[00:33:26] little bit, but it really was revived by
[00:33:28] the Atari results of DeepMind.
[00:33:34] And
[00:33:39] you know, they've also had very
[00:33:41] compelling self-play results in AlphaGo
[00:33:43] Zero, where they could train a very
[00:33:45] strong Go player from no knowledge at
[00:33:48] all to beating all humans.
[00:33:50] Same is true about our Dota 2 results.
[00:33:53] It again started from zero and just did
[00:33:56] lots and lots of self-play.
[00:33:58] And I want to talk a little bit about
[00:34:00] why I think self-play is really
[00:34:01] exciting.
[00:34:03] Cuz you get things like this.
[00:34:05] Like you can
[00:34:08] self-play
[00:34:10] makes it possible to create very simple
[00:34:13] environments
[00:34:14] that support potentially unbounded
[00:34:17] complexity,
[00:34:19] unbounded
[00:34:21] sophistication in your agents, unbounded
[00:34:26] scheming and social skills.
[00:34:28] And
[00:34:31] seems relevant towards building for
[00:34:33] building intelligent agents.
[00:34:36] And there is work on artificial life
[00:34:39] by
[00:34:40] Karl Sims from '94.
[00:34:42] And you can see that already there it
[00:34:44] looks very very familiar. You see these
[00:34:46] little evolved creatures whose
[00:34:48] morphologies are evolved as well. And
[00:34:49] here they are competing for the
[00:34:51] possession of a little green cube.
[00:34:55] And again, this was done in 1994 on tiny
[00:34:58] computers.
[00:35:00] And just like many and just like other
[00:35:02] uh
[00:35:04] promising ideas that we may that we are
[00:35:05] familiar with,
[00:35:07] didn't have enough compute to really
[00:35:08] push them forward.
[00:35:11] But I think that this is the kind of
[00:35:13] thing that we could get with large-scale
[00:35:15] self-play.
[00:35:17] And I want to show some work that we've
[00:35:18] done just trying to revive this concept
[00:35:20] a little bit.
[00:35:21] And I'm going to show this video. This
[00:35:22] was work by Bansal et al.
[00:35:25] Was a productive summer internship.
[00:35:28] There is a bit of music here. Let me
[00:35:29] turn it off.
[00:35:31] Actually, maybe I can keep it on.
[00:35:38] No, I can't. I can't.
[00:35:41] But the point is, what's the point?
[00:35:44] You got this super simple environment,
[00:35:46] which in this case is just the sumo
[00:35:48] ring.
[00:35:50] And you just tell the agents, you get a
[00:35:52] plus one when the other agents get gets
[00:35:54] outside the ring.
[00:35:56] And the reason I find this so
[00:35:59] well, I personally like it because these
[00:36:00] things look alive. Like they have these
[00:36:03] breaths of
[00:36:05] complicated behaviors
[00:36:07] that they learn just in order to stay in
[00:36:10] the game.
[00:36:12] And so, you can kind of see that if you
[00:36:14] let your imagination run wild,
[00:36:17] then
[00:36:18] yeah, so this this self-play is not
[00:36:20] symmetric.
[00:36:22] And also the human these humanoids are a
[00:36:24] bit unnatural because they they
[00:36:28] they don't feel pain and they don't get
[00:36:30] tired and they don't have any, you know,
[00:36:32] a whole lot of energy constraints.
[00:36:40] Oh, it blocked it.
[00:36:42] That was good.
[00:36:44] So, that's pretty good, too.
[00:36:45] So, here the goal you can guess what the
[00:36:47] goal is.
[00:36:50] That that was a
[00:36:51] That was a nice dodge.
[00:36:59] And now this is So, this is example. So,
[00:37:01] one of the things that would be nice
[00:37:05] is that if you could take these
[00:37:06] self-play environments,
[00:37:08] train our agents to do some kind of
[00:37:12] tasks from the self-play,
[00:37:14] and then take the agent outside and get
[00:37:17] it to do something useful for us. I
[00:37:18] think if that were possible, that would
[00:37:19] be amazing. And here there is like a
[00:37:21] tiniest the tiniest of tests where we
[00:37:23] take the sumo wrestling agent and we
[00:37:26] just apply we put it we put it isolated
[00:37:28] and alone inside the ring. It doesn't
[00:37:30] have a friend. And you just apply big
[00:37:32] forces on it and see if it can balance
[00:37:34] itself. And of course, it can balance
[00:37:36] itself because it's been trained
[00:37:40] because it's been trained against an
[00:37:41] opponent that tried to push it. So, it's
[00:37:43] really good at resisting forces in
[00:37:45] general.
[00:37:46] And so, kind of the the mental image
[00:37:49] here is that imagine you take a ninja
[00:37:51] and then you ask it to to learn to
[00:37:53] become a chef.
[00:37:55] Because the ninja is already so
[00:37:56] dexterous, it should have a really
[00:37:58] fairly easy time to be a very good good
[00:38:00] cook.
[00:38:01] That's the kind of high-level idea here.
[00:38:03] It hasn't happened yet.
[00:38:05] But one thing I'd like to ask yeah, and
[00:38:07] so
[00:38:09] And so, I think one of the key questions
[00:38:10] in this line of work is
[00:38:13] how can you set up
[00:38:16] a type of self-play environment which,
[00:38:19] once you succeed,
[00:38:22] it can solve useful tasks for us which
[00:38:24] are different just from the environment
[00:38:25] itself. And that's the big difference
[00:38:27] between games. In games, the goal is to
[00:38:29] actually win the environment.
[00:38:31] But that's not what we want. We want it
[00:38:32] to
[00:38:33] just be generally good at being clever
[00:38:36] and then solve solve our problems, you
[00:38:37] know, do my homework type
[00:38:39] agent.
[00:38:41] I want to um
[00:38:43] Yeah, I want to show one
[00:38:46] one slide which I think is interesting.
[00:38:48] So,
[00:38:49] one of the one of the reasons, like if
[00:38:51] you like I would like to ask you to let
[00:38:53] your imaginations run wild and imagine
[00:38:55] that
[00:38:57] neural nets
[00:38:59] the hardware designers of neural nets
[00:39:00] have built enormous giant computers and
[00:39:03] this self-play has been scaled up
[00:39:05] massively. One thing that's
[00:39:07] notable
[00:39:09] that we know about biological evolution
[00:39:13] is that social species tend to be
[00:39:16] tend to have larger brains. They tend to
[00:39:18] be smarter.
[00:39:20] We know that this is true for any It is
[00:39:22] very often the case that whenever you
[00:39:24] have two species which are related, but
[00:39:26] one is social and one isn't, then the
[00:39:29] social one tends to be smarter.
[00:39:31] We know that human biological evolution
[00:39:33] really accelerated over the past few
[00:39:35] million years.
[00:39:37] Probably because
[00:39:39] at that point,
[00:39:42] well, this is a bit speculative.
[00:39:45] But the theory here, my theory at least,
[00:39:47] is that
[00:39:49] humans became sufficiently competent
[00:39:51] with respect to their environment. So,
[00:39:53] you're not They stopped being afraid of
[00:39:55] the lion.
[00:39:56] And the biggest concern became now the
[00:39:57] human. What the other humans think of
[00:39:59] you.
[00:40:00] What are they gossiping about you? Where
[00:40:02] you stand in the pecking order.
[00:40:05] And so, I think this kind of
[00:40:08] environment
[00:40:10] created an incentive for the larger
[00:40:12] brains. And I was able, you know,
[00:40:15] as is often the case in science, it's
[00:40:17] very easy to find some scientific
[00:40:19] support for your hypothesis, which we
[00:40:21] did.
[00:40:22] So, there exists a paper in science
[00:40:29] which supports the claim that
[00:40:32] social environments
[00:40:35] stimulated the development of larger,
[00:40:38] more clever brains. And the specific
[00:40:39] evidence they present is the convergent
[00:40:42] evolution in smart social apes
[00:40:45] and smart birds
[00:40:47] like crows.
[00:40:50] Who apparently they have similar
[00:40:51] cognitive functions even though they
[00:40:52] have very different brain structures.
[00:40:54] Now, I'm only 75% confident in this
[00:40:57] claim, but I'm pretty sure that birds
[00:40:59] don't have the same kind of cortex as we
[00:41:01] do.
[00:41:03] Because the evolutionary split occurred
[00:41:05] a long time back in the past.
[00:41:08] So,
[00:41:14] I think it's interesting. I think it's I
[00:41:15] I I like I like I think this is
[00:41:17] intriguing at the very least. But yeah,
[00:41:19] you could create a society of agents and
[00:41:22] just keep scaling it up, and perhaps
[00:41:24] you're going to get
[00:41:26] agents that are going to be smart.
[00:41:29] Now, I want to finish one
[00:41:31] with one observation about
[00:41:33] environments that are trained to be
[00:41:35] self-play.
[00:41:36] And this is And this is um a plot from
[00:41:39] our from the the strength of our Dota
[00:41:41] bot as a function of time.
[00:41:44] Going from April all the way to August.
[00:41:48] And basically, you just fix the bugs and
[00:41:50] you scale up your self-play environment.
[00:41:52] And you scale up
[00:41:54] the amount of compute, and you get a
[00:41:55] very rapid increase in the strength of
[00:41:58] the system.
[00:42:00] And it makes sense. In self-play
[00:42:02] environments,
[00:42:04] the compute is the data.
[00:42:06] So, you can generate more of it.
[00:42:09] So, I guess I want to finish with the
[00:42:10] provocative question, which is
[00:42:13] if you have a self- a sufficiently
[00:42:16] open-ended self-play environment,
[00:42:18] will you get extremely rapid increase in
[00:42:22] the cognitive ability of your agents
[00:42:25] all the way to superhuman?
[00:42:27] And on this note,
[00:42:29] I will finish the presentation. Thank
[00:42:31] you so much for your attention.
[00:42:39] Yeah, before Before Before I Before I
[00:42:40] start the question answering session, I
[00:42:43] want to say that one One important thing
[00:42:45] I want to say is that many of these
[00:42:46] works were done in collaboration with
[00:42:48] many people from Berkeley and especially
[00:42:49] Peter Abbeel.
[00:42:50] And I want to I want to highlight that.
[00:42:53] Okay, great. I wonder if you can show
[00:42:56] the last slide cuz you It seemed like it
[00:42:57] was a very important conclusion, but you
[00:42:59] went over it very quickly. Yeah, so this
[00:43:02] is a very This is a It's It's a
[00:43:06] It is a bit speculative.
[00:43:10] And it really is a question of
[00:43:13] The specific statement here is that
[00:43:15] if you believe
[00:43:18] that you're going to get truly smart
[00:43:20] human-level agents as a result of some
[00:43:22] kind of massive scale self-play,
[00:43:25] will
[00:43:27] you also experience the same kind of
[00:43:30] rapid increase in the capability of the
[00:43:32] agent
[00:43:33] that you see that that we saw in our
[00:43:37] experience with Dota, and in general,
[00:43:40] because you can convert compute into
[00:43:41] data. So, you put more compute, this
[00:43:44] thing gets better.
[00:43:49] Yeah.
[00:43:50] So, I mean, that's that's sort of a a
[00:43:51] general remark. I obviously you do you
[00:43:54] compute more, you get you get better
[00:43:55] results, but I didn't quite grasp the um
[00:43:59] uh the difference between these two
[00:44:01] panels.
[00:44:02] Well,
[00:44:03] so
[00:44:09] So, it's really a question of uh
[00:44:17] So, it's So, it really boils down to
[00:44:18] this.
[00:44:19] It's a question of where do the the What
[00:44:22] are the limits to progress in the fields
[00:44:25] and in capabilities are?
[00:44:26] Uh do the limits come from
[00:44:29] Like in other words,
[00:44:32] given the right algorithms, which
[00:44:34] currently don't yet exist,
[00:44:36] once you have them,
[00:44:38] how will the increase in the in the
[00:44:41] actual capability of the system look
[00:44:42] like?
[00:44:43] I think there is a definitely a
[00:44:45] possibility that it will be like on the
[00:44:46] right side. That once you have,
[00:44:49] you know, you figure out your
[00:44:50] hierarchical reinforcement learning, you
[00:44:51] figured out concept learning,
[00:44:54] all your your supervised learning is in
[00:44:55] good shape,
[00:44:57] and then
[00:44:58] the massive neural net
[00:45:00] much bigger than a human brain, this
[00:45:02] will
[00:45:03] much bigger than a human brain,
[00:45:04] this will happen.
[00:45:06] Like how how could How will the plot
[00:45:09] look like over time?
[00:45:12] So, you're you're projecting that we've
[00:45:14] only seen the very beginning. Okay, so
[00:45:16] let's throw it up to questions, and I
[00:45:18] see you already have your hand up.
[00:45:22] Thank you for that. Um you mentioned
[00:45:24] hierarchy, and I'm wondering if you have
[00:45:26] an example of hierarchical self-play
[00:45:29] that would
[00:45:30] uh you know, increase the slope of this
[00:45:32] curve. Yeah, so we don't have hierarchy
[00:45:35] We have not tried hierarchical
[00:45:36] self-play.
[00:45:39] This is more a statement from our
[00:45:40] experience with our Dota bot, where you
[00:45:43] start at basically losing to everyone,
[00:45:45] and then
[00:45:46] your true skill metric, which is like an
[00:45:48] Elo rating, just
[00:45:50] increased pretty much linearly all the
[00:45:51] way to the best humans.
[00:45:54] So, that's And I think this is a
[00:45:57] gen- It seems like it could be a general
[00:46:00] property of self-play systems.
[00:46:04] And which game was this? Dota. Dota.
[00:46:07] Yeah.
[00:46:09] Okay. More questions?
[00:46:13] Hey Ilya. Hey. Very nice talk. Thank
[00:46:14] you. I had a question on environments.
[00:46:17] Do you have any thoughts on
[00:46:19] going beyond like sumo wrestling
[00:46:21] environments? Like what What are good
[00:46:23] environments to to study?
[00:46:26] Well, these are
[00:46:28] question of what makes
[00:46:31] a good environment.
[00:46:34] So,
[00:46:38] I think there are two ways of getting
[00:46:39] good environments.
[00:46:41] One of them is from
[00:46:44] trying to solve problems that we care
[00:46:45] about, and they naturally generate
[00:46:47] environments.
[00:46:50] I think another one is
[00:46:52] to think of open-ended environments
[00:46:55] where
[00:46:56] you can build lot So, one of this one of
[00:46:58] the slightly unsatisfying
[00:47:00] features of most of the environments
[00:47:02] that we have today
[00:47:04] is that they're a little bit not
[00:47:05] open-ended.
[00:47:06] You got a very kind of narrow domain,
[00:47:08] and you want to perform a task in this
[00:47:09] narrow domain.
[00:47:11] But one But some environments which are
[00:47:12] very interesting to think about are one
[00:47:14] where there is no limit to the depth of
[00:47:16] these environments. And some of these
[00:47:18] examples include programming,
[00:47:21] math, even Minecraft. In Minecraft, you
[00:47:23] could build structures of greater and
[00:47:25] greater complexity. And you know, at
[00:47:26] first people build little homes in
[00:47:28] Minecraft.
[00:47:29] Then they build big castles, and now
[00:47:31] people You can find people who are
[00:47:32] building entire cities and even
[00:47:34] computers inside Minecraft. Now,
[00:47:36] obviously, Minecraft has its obvious
[00:47:37] challenge, which is
[00:47:39] problem, which is what do we want the
[00:47:41] agents to do there?
[00:47:43] So, it needs to be addressed, but
[00:47:45] kind of uh
[00:47:47] directionally,
[00:47:49] these would be nice environments to
[00:47:50] think about more.
[00:47:54] Okay.
[00:47:55] Um
[00:47:56] someone up here.
[00:48:04] Uh this is This is sort of similar to
[00:48:06] that last question.
[00:48:08] But I was wondering uh what the effect
[00:48:10] if if you know of complicated uh
[00:48:13] non-agent objects and non-agent entities
[00:48:17] in the environment is on how well
[00:48:19] self-play works. For instance, in the
[00:48:21] sumo environment, the reason that the
[00:48:24] self-play agents can become very complex
[00:48:26] and use very complex strategies is
[00:48:28] because that's necessary in order to
[00:48:30] compete against this other agent, which
[00:48:32] is also using very complex strategies.
[00:48:34] If instead you were uh
[00:48:37] working maybe not against another agent,
[00:48:39] but against a very simple agent that
[00:48:40] doesn't train, but through some very
[00:48:43] complicated system, you had to operate a
[00:48:45] lot of machines in this environment or
[00:48:47] something like that, how does that
[00:48:49] affect the the effectiveness of this?
[00:48:52] Yeah, I mean, I think I think it depends
[00:48:53] a little bit on the specifics. Like for
[00:48:55] sure that, you know, if you have a
[00:48:56] complicated environment or complicated
[00:48:58] problem that's produced somehow,
[00:49:01] then you will also need to develop a
[00:49:03] pretty competent agent.
[00:49:05] I think the thing that's interesting
[00:49:06] about the self-play approach is that
[00:49:09] you generate the challenge yourself. So,
[00:49:11] the question of where does the challenge
[00:49:14] come from
[00:49:15] is
[00:49:16] answered for you. There's a mic problem.
[00:49:18] Oh, there's a mic problem. Maybe a mic
[00:49:20] problem or Uh-oh. I don't know. Doesn't
[00:49:22] seem to be muted. Let me check again.
[00:49:25] Anyway, let's let's continue.
[00:49:27] Any more questions?
[00:49:30] Okay.
[00:49:31] Uh so, uh oh, we have quite a few.
[00:49:39] Um back a bit to the hindsight
[00:49:41] experience policy, you talked about you
[00:49:43] give the example of, you know, you
[00:49:45] trying to reach the red spot A and you
[00:49:47] instead reach some spot B and you're
[00:49:50] going to use that to train. I guess I
[00:49:51] was wondering if you could elaborate on
[00:49:52] that a little bit more. I mean, I'm not
[00:49:54] very familiar with DDPG, so perhaps
[00:49:56] that's critical to understanding this,
[00:49:57] but I guess what I'm wondering is how do
[00:49:59] you turn every experience into, you
[00:50:01] know, hitting the ball this way
[00:50:02] translates into this motion without
[00:50:05] doing it in a reward-based way. Yeah, so
[00:50:07] basically you just say you're you you
[00:50:09] have a policy, which is parameterized by
[00:50:13] a goal state.
[00:50:15] So then you say in effect you have a
[00:50:17] family of policies, one per for every
[00:50:19] possible goal.
[00:50:21] And then you say, "Okay, I'm going to
[00:50:22] run a poll I'm going to run the policy
[00:50:24] that tries to reach state A."
[00:50:26] And it reached state B instead.
[00:50:28] So I'm going to say, "Well, this is
[00:50:29] great for training data for the policy
[00:50:31] which reaches state B."
[00:50:33] So that's how you do it.
[00:50:35] In effect. Like if you want more
[00:50:36] details, we could talk about it offline.
[00:50:42] Uh
[00:50:46] Okay.
[00:50:47] So um two questions. One One is a very
[00:50:49] simple question about about HER again.
[00:50:52] So if a task is
[00:50:54] difficult, for example, you know,
[00:50:56] hitting a fastball in baseball, right?
[00:50:58] So even the best humans
[00:51:00] can do it
[00:51:01] like 38% of the time or something like
[00:51:03] that,
[00:51:04] right? Um
[00:51:06] so the danger is that if you miss,
[00:51:08] you're going to say, "Oh, I was trying
[00:51:09] to miss. So so now I take this as a
[00:51:12] training example of how to miss."
[00:51:14] Right? Which is not All right, you're
[00:51:15] actually doing the optimal action,
[00:51:17] right? But your perceptual apparatus
[00:51:19] contractable fast enough.
[00:51:21] So with that's the best you can do. So
[00:51:22] it seems like you would you would run
[00:51:24] into trouble on tasks like that. I mean,
[00:51:27] okay.
[00:51:28] Sh- Should I should should answer the
[00:51:29] first question before you ask the
[00:51:30] second?
[00:51:31] let's do that. So
[00:51:32] the method is still not absolutely
[00:51:34] perfect,
[00:51:36] but on the question of what happens when
[00:51:38] you miss
[00:51:40] and you're trying to actually succeed,
[00:51:42] then yeah, you will have a lot of data
[00:51:43] on how to not reach the state.
[00:51:46] Like so you're trying to reach a certain
[00:51:47] desired state which is hard to reach.
[00:51:49] You try to do that, you reach a
[00:51:50] different state. So you say, "Okay,
[00:51:51] well, I'm going to I will train my
[00:51:53] system
[00:51:55] to reach this state."
[00:51:57] But next time I'm going to say I still
[00:51:59] want to
[00:52:00] It What it means is that for that
[00:52:01] specific problem, the approach of
[00:52:04] this approach will be less beneficial
[00:52:07] than for approach when approach for the
[00:52:08] tasks a little bit more continuous,
[00:52:10] where you can have a more of a hill
[00:52:11] climbing effect where you gradually,
[00:52:13] like let's say
[00:52:14] in a programming
[00:52:15] in the in the setting of context of
[00:52:17] programming, you learn to program
[00:52:19] simple programs. You learn to write
[00:52:20] different subroutines and you gradually
[00:52:22] increase your competence, the set of
[00:52:24] states you know how to reach.
[00:52:26] So I agree that when there is a very
[00:52:27] narrow state which is very hard to
[00:52:28] reach, then it will not help. But
[00:52:31] whenever there is a kind of a continuity
[00:52:33] to the states, then this approach will
[00:52:35] help.
[00:52:37] Okay. So the sec- the second question is
[00:52:40] about self-play. So
[00:52:42] when I when I saw your title, what I
[00:52:43] thought you were going to say was
[00:52:45] was this So if you if you think about um
[00:52:49] AlphaGo, right? If we tried to train
[00:52:51] AlphaGo by playing it against
[00:52:54] the existing world champion,
[00:52:57] since it would never win a single game
[00:53:00] for the first 50 million game games,
[00:53:01] right? It would learn nothing at all.
[00:53:03] Yeah.
[00:53:04] Um but because we play it against
[00:53:06] itself, it always has a 50% chance of
[00:53:08] winning. So you're always going to get a
[00:53:09] gradient signal, no matter how poorly
[00:53:12] you play.
[00:53:13] Yeah, that's very important. Now, the
[00:53:16] the So the the question is, you know, is
[00:53:18] there some magic trick there that you
[00:53:20] can then apply
[00:53:22] to tasks that are intrinsically
[00:53:24] difficult
[00:53:26] to get
[00:53:27] uh to get any reward signal on, right?
[00:53:29] So if you take Spider Solitaire, for
[00:53:31] example, if you watch an ordinary human
[00:53:34] play Spider Solitaire, they lose the
[00:53:36] first 100 games
[00:53:37] and then they give up. They say, "This
[00:53:39] is impossible, you know, I I hate this
[00:53:40] game."
[00:53:41] Right? There's no reward signal there
[00:53:43] because you're just not good enough to
[00:53:44] ever win.
[00:53:46] Um and so is there a way you can convert
[00:53:49] Spider Solitaire into a two-player game
[00:53:51] and somehow
[00:53:52] guarantee that you always get a a
[00:53:54] gradient signal
[00:53:55] for that game? So that's a very good
[00:53:57] question. That's a very good What What
[00:53:58] What you said is a very good point. I
[00:53:59] just want to Before Before I am
[00:54:01] elaborate on your question, I just want
[00:54:03] to also
[00:54:05] talk about the fact that
[00:54:07] one of the key things of self-play is
[00:54:09] that you always have an equal evenly
[00:54:10] matched opponent.
[00:54:12] And what it means that you also have
[00:54:15] potentially an indefinite incentive for
[00:54:17] improvement.
[00:54:19] Like even if you are really really
[00:54:20] competent, if you have a super competent
[00:54:22] agent, the opponent will be just as
[00:54:24] competent and so
[00:54:25] if done right,
[00:54:27] the system will be incentivized to
[00:54:28] improve.
[00:54:30] And so
[00:54:33] I think yeah, I I think it's it's an
[00:54:35] important thing to emphasize and that's
[00:54:36] also by the way why the exploration
[00:54:38] problem is much easier
[00:54:41] because you explore the strategy space
[00:54:43] together with your opponent. And it's
[00:54:45] actually important not to have just one
[00:54:46] opponent, but to have a whole little
[00:54:47] family of them for stability.
[00:54:50] But that's that that's that's basically
[00:54:52] crucial. Now, on your second question of
[00:54:54] what to do when you just can't get the
[00:54:55] reward,
[00:54:56] so very often
[00:54:58] if the problem is hard enough, I think
[00:55:01] there isn't much you can do without
[00:55:02] having some kind of deep domain, you
[00:55:04] know, side information about the task.
[00:55:06] But one approach that is popular and has
[00:55:08] been pursued by multiple uh groups is to
[00:55:11] use like asymmetric self-play for
[00:55:14] exploration.
[00:55:16] You've got a predictor which tries to
[00:55:17] predict what's going to happen.
[00:55:20] And you've got a policy which tries to
[00:55:23] take action which surprise the
[00:55:24] predictor.
[00:55:26] So the predictor is going to say, "Okay,
[00:55:27] well, if you're going to I I basically
[00:55:29] have opinions about
[00:55:32] what will be the consequence of the
[00:55:33] different actions."
[00:55:35] And the actor tries to find regions of
[00:55:38] space which surprise the predictor. So
[00:55:40] you have this kind of a self-play. It's
[00:55:42] not exactly self-play, it's more of a
[00:55:43] kind of a competitive adversarial
[00:55:44] scenario where the agent is incentivized
[00:55:47] to
[00:55:48] cover the entire space. It doesn't
[00:55:50] answer the question of how to solve a
[00:55:52] hard task like so like Spider Solitaire
[00:55:55] because if the if you actually need to
[00:55:56] be super good,
[00:55:57] I think
[00:56:01] I think that's tough.
[00:56:03] But at least you can see how this can
[00:56:04] give you a general guide of how to move
[00:56:07] forward in general.
[00:56:09] I had a question back here. Uh
[00:56:11] Same question?
[00:56:12] I'll say here.
[00:56:16] Um
[00:56:17] What do you think is exciting in terms
[00:56:20] of
[00:56:21] new architectures such as, you know,
[00:56:24] they've been building
[00:56:26] They've been adding like memory
[00:56:27] structures to neural nets, like the DNC
[00:56:29] paper. Yeah. So what do you see the role
[00:56:31] of new architectures playing in actually
[00:56:35] uh achieving what we want for
[00:56:36] generalization, meta learning?
[00:56:39] Yeah, so I think I think this is a very
[00:56:40] good question, the question of
[00:56:41] architectures.
[00:56:42] And I'd say that it's very rare to find
[00:56:44] a really a genuinely good new
[00:56:46] architecture. And truly truly genuine
[00:56:50] innovation in architecture space is
[00:56:51] uncommon.
[00:56:53] I'd say the biggest innovation in
[00:56:55] architecture space over the past
[00:56:57] many years has been soft attention.
[00:57:01] So soft attention is legitimately a
[00:57:03] major advance in architectures.
[00:57:06] But
[00:57:07] it's also very hard to innovate in
[00:57:08] architecture space
[00:57:10] because
[00:57:12] the basic architecture is so good.
[00:57:15] I think that better generalization will
[00:57:16] be achieved not
[00:57:18] and this is my opinion, it's not backed
[00:57:20] by data yet.
[00:57:22] I think a better generalization will not
[00:57:23] be achieved by means of just improving
[00:57:25] the architecture,
[00:57:27] but by means of changing
[00:57:29] the learning algorithm and possibly even
[00:57:32] the paradigm of the way we think about
[00:57:34] our models. So I think things like uh
[00:57:36] minimum description length and
[00:57:38] compression will be a lot more popular.
[00:57:42] But it's not I think these are
[00:57:44] non-obvious questions. But basically, I
[00:57:46] think architecture is important
[00:57:48] whenever you can actually find good new
[00:57:50] good new architectures.
[00:57:52] For the hard problems, uh how about
[00:57:53] curriculum learning? So to learn to hit
[00:57:55] a fastball, start with a slow ball.
[00:57:58] Yeah, for sure. Curriculum learning is
[00:58:00] a very important idea.
[00:58:02] It's how human It's It's how humans
[00:58:05] learn.
[00:58:07] And it's very I guess a pleasant
[00:58:08] surprise that
[00:58:10] our neural networks also benefit from
[00:58:12] curriculums.
[00:58:13] One nice thing about self-play
[00:58:16] is that the curriculum is built in. It's
[00:58:18] like intrinsic.
[00:58:20] What you lose in self-play is the
[00:58:23] ability to direct the self-play to a
[00:58:25] specified point.
[00:58:27] So I I have a question. Uh you showed us
[00:58:30] the nice videos, the wrestlers and uh
[00:58:33] and the robots and so forth. And uh I
[00:58:36] assume I assume it's similar to deep
[00:58:38] learning in the sense that there's a
[00:58:40] framework of linear algebra underlying
[00:58:43] the whole thing.
[00:58:44] So is there anything there other than
[00:58:45] the linear algebra?
[00:58:47] I mean, you just have neural net I mean,
[00:58:48] so it's not it's it's even it's just you
[00:58:50] just take two agents and you apply
[00:58:52] reinforcement learning algorithms.
[00:58:54] And a reinforcement learning algorithm
[00:58:55] is a neural net with a slightly
[00:58:57] different way of dating the parameters.
[00:58:58] So it's all it's all matrix
[00:58:59] multiplication all the way down.
[00:59:01] Just want to multiply big matrices as
[00:59:03] fast as possible.
[00:59:05] Right.
[00:59:06] Okay. Uh we have one more.
[00:59:12] So you mentioned something about uh
[00:59:13] transfer learning uh and the importance
[00:59:15] of that. Um what do you think about
[00:59:18] concept extraction and uh transferring
[00:59:21] that and if that's something that you
[00:59:23] think is possible or people are doing
[00:59:25] right now?
[00:59:26] So I think it really depends on what you
[00:59:28] mean by contact concept extraction
[00:59:30] exactly.
[00:59:31] I think it's definitely the case that
[00:59:33] our transfer learning abilities are
[00:59:35] still rudimentary.
[00:59:37] And we don't yet have methods that can
[00:59:39] extract like
[00:59:41] seriously high-level concepts from one
[00:59:43] domain
[00:59:44] and then apply it in another domain.
[00:59:46] I mean, there are ideas on how to do it,
[00:59:48] to approach that, but nothing that's
[00:59:49] really convincing on a task that
[00:59:51] matters.
[00:59:52] Not yet.
[00:59:56] Well, we really have a lot of questions,
[00:59:58] and the reason is that you gave very
[01:00:00] short, succinct answers, for which we
[01:00:02] are very grateful. Thank you very much.
[01:00:04] Let's
[01:00:05] give him a great hand.
[01:00:07] THANK YOU.
[01:00:20] THANK YOU. YEAH, THANKS FOR COMING.
