# MIT AGI (Lex Fridman): Ilya Sutskever — OpenAI Meta-Learning & Self-Play
- **YouTube URL:** https://www.youtube.com/watch?v=9EN_HoEk3KY
- **Lines:** 1370

---

[00:00:00] welcome back to 6 SZ row 99 artificial
[00:00:02] general intelligence today we have Ilya
[00:00:05] sutskever co-founder and research
[00:00:11] director of open AI he started in the
[00:00:14] amel group in Toronto Geoffrey Hinton
[00:00:16] then at Stanford with an jiaying
[00:00:18] co-founded DNN research for three years
[00:00:21] as a research scientist at Google brain
[00:00:22] and finally co-founded open AI citations
[00:00:27] aren't everything
[00:00:28] but they do indicate impact and his work
[00:00:31] recent work in the past five years has
[00:00:35] been cited over forty six thousand times
[00:00:38] he has been the key creative intellect
[00:00:42] and driver behind some of the biggest
[00:00:44] breakthrough ideas in deep learning and
[00:00:46] artificial intelligence ever
[00:00:48] so please welcome Ilya alright thanks
[00:00:59] for the introduction Lex
[00:01:01] alright thanks for coming to my talk I
[00:01:04] will tell you about some work we've done
[00:01:06] over the past year on on meta learning
[00:01:09] and software open AI and before I dive
[00:01:12] into some of the more technical details
[00:01:15] of the work I want to spend a little bit
[00:01:18] of time talking about deep learning and
[00:01:22] why it works at all in the first place
[00:01:25] which I think it's actually not a
[00:01:27] self-evident saying that they should
[00:01:29] work one fact it's actually a fact it's
[00:01:35] a mathematical theory that you can prove
[00:01:37] is that if you could find the shortest
[00:01:42] program the does very very well on your
[00:01:46] data then you will achieve the best
[00:01:48] generalization possible with a little
[00:01:51] bit of modification you can turn it into
[00:01:52] a precise theorem
[00:01:54] and on a very intuitive level it's easy
[00:01:58] to see what it should be the case if you
[00:02:01] have some data and you're able to find a
[00:02:04] shorter program which generates this
[00:02:06] data then you've essentially extracted
[00:02:09] all the all conceivable regularity from
[00:02:11] this data into your program and then you
[00:02:14] can use these objects to make the best
[00:02:15] predictions possible like if if you have
[00:02:19] data which is so complex but there is no
[00:02:22] way to express it as a shorter program
[00:02:25] then it means that your data is totally
[00:02:27] random there is no way to extract any
[00:02:29] regularity from it whatsoever now there
[00:02:32] is little known mathematical theory
[00:02:34] behind this and the proofs of these
[00:02:36] statements actually not even that hard
[00:02:38] but the one minor slight disappointment
[00:02:41] is that it's actually not possible at
[00:02:44] least given today's tools and
[00:02:45] understanding to find the best short
[00:02:48] program that explains or generates or
[00:02:52] solves your problem given your data this
[00:02:55] problem is computationally intractable
[00:02:58] the space of all programs is a very
[00:03:02] nasty space small changes to your
[00:03:04] program result in massive changes in the
[00:03:06] behavior of the program as it should be
[00:03:08] it makes sense you have a loop you
[00:03:11] change the inside of the loop of course
[00:03:13] you get something totally different so
[00:03:15] the space of programs is so hard at
[00:03:17] least given what we know today search
[00:03:19] there seems to be completely off the
[00:03:21] table well if we give up on shorts on
[00:03:27] short programs what about small circuits
[00:03:31] well it turns out that we are lucky it
[00:03:34] turns out that when it comes to small
[00:03:36] circuits you can just find the best
[00:03:38] small circuits circuits that solves the
[00:03:40] problem using back propagation and this
[00:03:43] is the miraculous fact on which the rest
[00:03:47] of AI stands it is the fact but then you
[00:03:51] have a circuit and you impose
[00:03:52] constraints on your circuits on your
[00:03:54] circuit using data you can find the way
[00:03:58] to satisfy these constraints these
[00:04:00] constraints using that problem by
[00:04:02] iteratively making small changes
[00:04:05] to the base of your neural network until
[00:04:08] its predictions satisfy the data what
[00:04:13] this means is that the computational
[00:04:15] problem that so the back propagation is
[00:04:17] extremely profound it is circuit search
[00:04:20] now we know that you can solve it solve
[00:04:22] it always but you can solve it sometimes
[00:04:25] and you can solve it at those times
[00:04:29] where we have a practical data set it is
[00:04:32] easy to design artificial data sets for
[00:04:34] which you cannot find the best neural
[00:04:35] network but in practice that seems to be
[00:04:38] not a problem you can think of training
[00:04:41] a neural network as solving a neural
[00:04:43] equation in many cases where you have a
[00:04:47] large number of equation terms like this
[00:04:50] f of X I theta equals y I so you got
[00:04:53] your parameters and they represent all
[00:04:54] your degrees of freedom and you use
[00:04:58] gradient descent to push the information
[00:05:01] from these equations into the parameters
[00:05:02] satisfy them all and you can see that
[00:05:06] the neural network let's say one with 50
[00:05:09] layers is basically a parallel computer
[00:05:13] that is given 50 time steps to run and
[00:05:17] you can do quite a lot with a 15 with 50
[00:05:19] time steps of a very very powerful
[00:05:21] massively parallel computer so for
[00:05:24] example I do I think it is not widely
[00:05:27] known that you can learn to sort sort n
[00:05:33] n bit numbers using a modestly sized
[00:05:37] neural network with just two hidden
[00:05:38] layers which is not bad it's not
[00:05:42] self-evident especially since we've been
[00:05:45] taught that sorting requires log n
[00:05:48] parallel steps with the neural network
[00:05:50] you can sort successful using only two
[00:05:53] parallel steps so there's some things
[00:05:55] like an arm is going on now these are
[00:05:58] parallel steps of threshold threshold
[00:06:00] neurons so they're doing a little bit
[00:06:02] more work let's answer to the mystery
[00:06:04] but if you've got 50 such layers you can
[00:06:05] do quite a bit of logic quite a bit of
[00:06:07] reasoning all inside the neural network
[00:06:09] and that's why it works
[00:06:11] given the data we are able to find the
[00:06:15] best neural network and because the
[00:06:17] neural network is deep because it can
[00:06:19] run computation inside of its act inside
[00:06:21] of its layers the best neural network is
[00:06:24] worth finding because that's really what
[00:06:26] you need you need something you need the
[00:06:29] model class which is worth optimizing
[00:06:32] but it also needs to be optimizable and
[00:06:35] deep neural networks satisfy both of
[00:06:37] these constraints and this is why
[00:06:39] everything works this is the basis on
[00:06:41] which everything else resides now I want
[00:06:45] to talk a little bit about reinforcement
[00:06:46] learning so reinforcement learning is a
[00:06:49] framework it's a framework of evaluating
[00:06:53] agents in their ability to achieve goals
[00:06:56] and complicated stochastic environments
[00:06:58] you've got an agent which is plugged
[00:07:00] into an environment as shown in the
[00:07:02] figure right here and for any given
[00:07:06] agent you can simply run it many times
[00:07:08] and compute its average reward now the
[00:07:13] thing that's interesting about the
[00:07:14] reinforcement learning framework is that
[00:07:16] there exist interesting useful
[00:07:20] reinforcement learning algorithms the
[00:07:22] framework existed for a long time it
[00:07:25] became interesting once we realized that
[00:07:27] good algorithms exist now these are
[00:07:29] there are perfect algorithms but they
[00:07:31] are good enough to do interesting things
[00:07:32] and all you want the mathematical
[00:07:37] problem is one where you need to
[00:07:39] maximize the expected reward now one
[00:07:44] important way in which the reinforcement
[00:07:46] learning framework is not quite complete
[00:07:48] is that it assumes that the reward is
[00:07:50] given by the environment you see this
[00:07:52] picture the agent sends an action while
[00:07:56] the reward sends it an observation in a
[00:07:58] both the observation and the reward
[00:08:00] backwards that's what the environment
[00:08:01] communicates back
[00:08:03] the way in which this is not the case in
[00:08:06] the real world is that we figure out
[00:08:11] what the reward is from the observation
[00:08:13] we reward ourselves we are not told
[00:08:16] environment doesn't say hey here's some
[00:08:18] negative reward it's our interpretation
[00:08:20] over census that lets us determine what
[00:08:23] the reward is and there is only one real
[00:08:26] true reward in life and this is
[00:08:28] existence or nonexistence and everything
[00:08:31] else is a corollary of that so well what
[00:08:35] should our agent be you already know the
[00:08:37] answer should be a neural network
[00:08:39] because whenever you want to do
[00:08:41] something dense it's going to be a
[00:08:42] neural network and you want the agent to
[00:08:44] map observations to actions so you let
[00:08:47] it be parametrized with a neural net and
[00:08:49] you apply learning algorithm so I want
[00:08:51] to explain to you how reinforcement
[00:08:53] learning works this is model free
[00:08:55] reinforcement learning the reinforcement
[00:08:56] learning has actually been used in
[00:08:58] practice everywhere but it's also deeply
[00:09:02] it's very robust it's very simple it's
[00:09:05] also not very efficient so the way it
[00:09:08] works is the following this is literally
[00:09:09] the one sentence description of what
[00:09:11] happens in short try something new add
[00:09:17] randomness directions and compare the
[00:09:21] result to your expectation if the result
[00:09:25] surprises you if you find that the
[00:09:28] results exceeded your expectation then
[00:09:31] change your parameters to take those
[00:09:33] actions in the future that's it this is
[00:09:36] the fool idea of reinforcement learning
[00:09:38] try it out see if you like it and if you
[00:09:41] do do more of that in the future and
[00:09:44] that's it that's literally it this is
[00:09:47] the core idea now it turns out it's not
[00:09:49] difficult to formalize mathematically
[00:09:51] but this is really what's going on
[00:09:52] if in a neural network in a regular
[00:09:54] neural network like this you might say
[00:09:57] okay what's the goal
[00:09:59] you run the neural network you get an
[00:10:01] answer you compare it to the desired
[00:10:03] answer and whatever difference you have
[00:10:05] between those two you send it back
[00:10:08] to change the neural network that's
[00:10:10] supervised line in reinforcement
[00:10:12] learning you run in your own network you
[00:10:14] add a bit of randomness to your action
[00:10:16] and then if you like the result your
[00:10:19] randomness turns into the desired target
[00:10:21] in effect so that's it trivial now math
[00:10:29] exists without explaining what these
[00:10:34] equations mean the point is not really
[00:10:36] to derive them but just to show that
[00:10:37] they exist there are two classes of
[00:10:40] reinforcement learning algorithms one of
[00:10:42] them is the policy gradient where
[00:10:45] basically what you do is that you take
[00:10:46] this expression right there the sum of
[00:10:49] expected we work the sum of rewards and
[00:10:51] it just crunched through the derivatives
[00:10:53] you expand the terms iran you do some
[00:10:56] algebra and you get a derivative and
[00:11:00] miraculously the derivative has exactly
[00:11:03] the form that i told you which is try
[00:11:07] some actions and if you like them
[00:11:09] increase the log probability of the
[00:11:11] actions that we truly follows from the
[00:11:13] math it's very nice when the intuitive
[00:11:15] explanation has a one-to-one
[00:11:17] correspondence to what you get in the
[00:11:19] equation even though you have to take my
[00:11:21] word for it if you are not familiar with
[00:11:22] it that's that equation at the top now
[00:11:26] there is a different class of
[00:11:27] reinforcement learning algorithms which
[00:11:28] is a little bit more difficult to
[00:11:29] explain it's called the Q learning based
[00:11:31] algorithms they are a bit less stable a
[00:11:34] bit more sample efficient and it has the
[00:11:39] property that it can learn not only from
[00:11:43] the data generated by the actor but from
[00:11:46] any other data as well so it has it has
[00:11:48] some rope but it has different
[00:11:50] robustness profile which would be a
[00:11:52] little bit important but it's only going
[00:11:53] to be a technicality so yeah this is the
[00:11:57] own policy of policy distinction but
[00:11:59] it's a little bit technical so if you
[00:12:00] find this hard to understand don't worry
[00:12:03] about it if you already know this then
[00:12:05] you already know it so now what's the
[00:12:08] potential for enforcement learning
[00:12:10] wasn't it promised what is it actually
[00:12:12] why should we be excited about it
[00:12:15] now there are two reasons the
[00:12:17] reinforcement learning algorithms of
[00:12:18] today already useful and interesting and
[00:12:22] especially if you have a really good
[00:12:24] simulation of your world you could train
[00:12:26] agents to do lots of interesting things
[00:12:30] but what's really exciting is if you can
[00:12:33] build a super amazing sample efficient
[00:12:35] out of reinforcement learning algorithm
[00:12:37] we just give it a tiny amount of data
[00:12:38] and the algorithm just crunches through
[00:12:41] it and extracts every bit of entropy out
[00:12:42] of it in order to learn in the fastest
[00:12:45] way possible now today our algorithms
[00:12:48] are not particularly efficient they are
[00:12:50] data inefficient but as our field keeps
[00:12:54] making progress this will change next I
[00:12:58] want to dive into the topic of meta
[00:12:59] learning the goal of meta learning so
[00:13:04] meta learning is a beautiful idea that
[00:13:07] doesn't really work but it kind of works
[00:13:09] and it's really promising too it's
[00:13:11] another promising idea so what's the
[00:13:14] dream we have some learning algorithms
[00:13:18] perhaps you could use those learning
[00:13:20] algorithms in order to learn to learn
[00:13:22] I'd be nice if we could learn to learn
[00:13:25] so how would you do that you will take a
[00:13:29] system which you train it not on one
[00:13:34] task but on many tasks and you ask you
[00:13:36] that it learns to solve these tasks
[00:13:38] quickly and that may actually be enough
[00:13:41] so here's how it looks like here's how
[00:13:43] most traditional metal earning look
[00:13:46] works like it looks like you have a
[00:13:48] model which is a big neural network what
[00:13:51] what you do is that you treat every
[00:13:54] instead of training cases you have
[00:13:57] training tasks and instead of test cases
[00:13:59] you have test tasks so your input may be
[00:14:02] instead of just your current test case
[00:14:05] it would be all the information about
[00:14:07] the new T above the test tasks plus the
[00:14:09] test case and you'll try to output the
[00:14:12] prediction reaction for that test case
[00:14:14] so basically you say yeah I'm going to
[00:14:17] give you your ten examples as part of
[00:14:19] your input to your model figure out how
[00:14:21] to make the best use of them it's a
[00:14:24] really
[00:14:25] straightforward idea u-turn the neural
[00:14:28] network into the learning algorithm by
[00:14:30] turning a training task into a training
[00:14:33] case so training to ask a constraining
[00:14:36] case this is meta learning just one
[00:14:39] sentence and so they've been several
[00:14:44] success stories which I I think are very
[00:14:46] interesting one of the success stories
[00:14:49] of meta learning is learning to
[00:14:51] recognize characters quickly so they've
[00:14:53] been a dataset
[00:14:56] produced by MIT by lake corral and this
[00:15:02] is a data set we have a large number of
[00:15:03] different handwritten characters and
[00:15:05] people have been able to train extremely
[00:15:08] strong meta learning system for this
[00:15:10] desk another successful another very
[00:15:13] successful example of meta learning is
[00:15:14] in that of neural architecture search by
[00:15:17] is openly from google where they found
[00:15:21] neural architecture that solved one
[00:15:24] problem well small problem and then you
[00:15:26] could generalize and then if you
[00:15:27] successfully solve large problems as
[00:15:28] well so this is the kind of the the
[00:15:32] small number of bits meta learning is
[00:15:34] that when you learn the architecture or
[00:15:36] maybe even learn a program small program
[00:15:37] or learning algorithm which you apply to
[00:15:39] new tasks so this is the other way of
[00:15:42] doing meta learning so anyway but the
[00:15:44] point is what's happening what's really
[00:15:46] happening in meta learning in most cases
[00:15:48] is that you turn a training task into a
[00:15:51] training case and pretend this is
[00:15:54] totally normal
[00:15:54] normal deep learning that's it this is
[00:15:57] the entirety of meta learning everything
[00:15:59] else suggests minor details next I wanna
[00:16:04] dive in so now that I've finished the
[00:16:06] introduction section I want to start
[00:16:08] discussing different work by different
[00:16:11] people from opening I and I want to
[00:16:13] start by talking about hindsight
[00:16:14] experience replay it's been a large
[00:16:17] effort by and recurvature all to develop
[00:16:20] a learning algorithm for reinforcement
[00:16:22] learning
[00:16:23] that doesn't solve just one task but it
[00:16:28] solves many tasks and it learns to make
[00:16:31] use of its experience in a much more
[00:16:33] efficient way and I want to discuss one
[00:16:36] problem in reinforcement learning it's
[00:16:38] actually I guess a set of problems which
[00:16:41] all related to each other at one really
[00:16:47] important thing you need to learn to do
[00:16:48] is to explore you're in that you start
[00:16:51] out in an environment you don't know
[00:16:54] what to do what do you do so one very
[00:16:56] important thing that has to happen is
[00:16:58] that you must get rewards from time to
[00:17:00] time if you try something and you don't
[00:17:03] get rewards then how can you learn so
[00:17:09] said that's the kind of the crux of the
[00:17:10] problem how do you learn and relatedly
[00:17:13] is there any way to meaningfully benefit
[00:17:17] from your ex from the experience from
[00:17:20] your attempts to from from your failures
[00:17:22] if you try to achieve a goal and you
[00:17:24] fail can you still learn from it you
[00:17:26] tell you instead of asking your
[00:17:28] algorithm to achieve a single goal you
[00:17:31] want to learn a policy that can achieve
[00:17:32] a very large family of goals for example
[00:17:34] instead of reaching one state you want
[00:17:37] to learn a policy that reaches every
[00:17:38] state of your system and what's the
[00:17:41] implication anytime you do something you
[00:17:44] achieve some state so let's suppose you
[00:17:47] say I want to achieve state a I try my
[00:17:51] best and I end up achieving state B I
[00:17:55] can either conclude well that was
[00:17:57] disappointing I haven't learned almost
[00:17:58] anything I'm still have no idea how to
[00:18:01] cheat how to achieve state aid but
[00:18:04] alternatively I can say well wait a
[00:18:05] second I've just reached a perfectly
[00:18:07] good state which is B can I learn how to
[00:18:10] achieve state B from my attempt to
[00:18:12] achieve state a an answer is yes you can
[00:18:15] and it just works and I just want to
[00:18:18] point out this is the one case there is
[00:18:20] a small subtlety here which may be
[00:18:23] interesting to those of you who are very
[00:18:26] familiar with on Part B the distinction
[00:18:28] between on policy and off policy when
[00:18:31] you try to achieve a you are on you're
[00:18:33] doing on policy learning for
[00:18:35] reaching the state a but you're doing
[00:18:38] off policy learning for it in the state
[00:18:40] be because you would take different
[00:18:41] actions if you would actually try to
[00:18:43] reach they'd be so that's why it's very
[00:18:45] important that the algorithm you use
[00:18:46] here can support of policy learning but
[00:18:49] that's a minor technicality at the crux
[00:18:52] the crux of the idea is you make the
[00:18:55] problem easier by ostensibly making it
[00:18:58] harder by training a system which can
[00:19:01] which aspires to reach to learn to reach
[00:19:04] every state to learn to achieve every
[00:19:06] goal to learn to master its environment
[00:19:09] in general you build a system which
[00:19:12] always learn something it learns from
[00:19:15] success as well as from failure because
[00:19:17] if it tries to do one thing one thing
[00:19:19] and it does something else
[00:19:20] it now has training data for how to
[00:19:22] achieve that something else I want to
[00:19:24] show you a video of how this thing works
[00:19:26] in practice so one challenge in
[00:19:30] reinforcement learning systems is the
[00:19:32] need to shape the reward so what does it
[00:19:34] mean
[00:19:35] it means that at the beginning of the
[00:19:37] system at the start of learning then the
[00:19:39] system doesn't know much it will
[00:19:42] probably not achieve your goal and so
[00:19:44] it's important that you design your
[00:19:45] reward function to give it gradual
[00:19:46] increments to make it smooth and
[00:19:48] continuous so that even when the system
[00:19:49] is not very good it achieves the goal
[00:19:51] now if you give your state your system a
[00:19:54] very sparse reward where the reward is
[00:19:56] achieved only when you reach a final
[00:19:57] state then it becomes very hard for
[00:20:01] normal reinforcement learning algorithms
[00:20:03] to solve a problem because naturally you
[00:20:05] never get the reward so you never learn
[00:20:07] no reward means no learning but here
[00:20:10] because you learn from failure as well
[00:20:13] as from success
[00:20:14] this is this problem simply doesn't
[00:20:16] occur and so this is this is nice I
[00:20:19] think you know let's let's look at the
[00:20:21] videos a little bit more like it's nice
[00:20:23] how this is it confidently and
[00:20:25] energetically moves the little green
[00:20:27] buck to its target and here's another
[00:20:29] one
[00:20:37] you
[00:20:50] okay so we can skip the it works on
[00:20:52] spawn on the face if you do it on
[00:20:53] physical robot as well but we can skip
[00:20:54] it so I think the point is that the
[00:20:58] hindsight experience replay algorithm is
[00:21:01] directionally correct because you want
[00:21:05] to make use of all your data and not
[00:21:07] only a small fraction of it now one huge
[00:21:10] question is where do you get the high
[00:21:13] level states where do the high level
[00:21:16] states come from because in the work of
[00:21:20] showing you so far
[00:21:21] the system is asked to achieve low level
[00:21:24] States so I think one thing it will
[00:21:26] become very important for this kind
[00:21:28] approaches is representation learning
[00:21:30] and unsupervised learning figure out
[00:21:33] what are the rights what are the right
[00:21:34] states what's the state space of goals
[00:21:37] that's worth achieving now I want to go
[00:21:43] through some real meta learning results
[00:21:46] and I'll show you a very simple way of
[00:21:49] doing seem to reel from simulation to
[00:21:53] the physical robot with meta learning
[00:21:55] and this is where my pain growl was an a
[00:21:58] and encouraged a really nice intern
[00:22:00] project in 2017 so I think we can agree
[00:22:06] that in the domain of robotics it would
[00:22:09] be nice if you could train your policy
[00:22:12] in simulation and then somehow this
[00:22:14] knowledge would carry over to the
[00:22:17] physical robot now we can build we can
[00:22:23] build simulators that are okay but they
[00:22:26] can never perfectly match the real world
[00:22:29] unless you want to have an insanely slow
[00:22:31] simulator and the reason for that is
[00:22:33] that it turns out that simulating freaky
[00:22:37] simulating contacts is super hard and I
[00:22:40] heard somewhere correct me if I'm wrong
[00:22:42] that simulating friction is np-complete
[00:22:44] I'm not sure but it's like stuff like
[00:22:48] that so your simulation is just not
[00:22:51] going to match reality there will be
[00:22:54] some resemblance but that's it
[00:22:55] how can we
[00:22:57] address this problem and I want to show
[00:22:59] you one simple idea so let's say one
[00:23:05] thing once one thing that would be nice
[00:23:07] is that if you could learn a policy
[00:23:10] learn a policy that would quickly adapt
[00:23:12] itself to the real world well if you
[00:23:17] want to learn a policy that can quickly
[00:23:19] adapt we need to make sure it has
[00:23:21] opportunities to adapt during training
[00:23:23] time so what do we do instead of solving
[00:23:27] a problem in just one simulator we add a
[00:23:30] huge amount of variability to the
[00:23:32] simulator we say we will randomize the
[00:23:35] friction so we will randomize the masses
[00:23:37] the length of the different objects and
[00:23:40] their I guess M dimensions so you try to
[00:23:44] randomize physics they simulate in lots
[00:23:48] of different ways and then importantly
[00:23:50] you don't tell the policy how you
[00:23:52] randomized it so what is it going to do
[00:23:55] then you take your policy and you put it
[00:23:57] in an environment then says well this is
[00:23:59] really really tough I don't know what
[00:24:01] the masses are and I don't know what the
[00:24:02] frictions are I need to try things out
[00:24:04] and figure out what the friction is as I
[00:24:07] get it responses from the environment so
[00:24:10] you're building you you learn a certain
[00:24:12] degree of adaptability into the policy
[00:24:15] and it actually works
[00:24:17] let's want to show you this is what
[00:24:19] happens when you just strain a policy in
[00:24:21] simulation and deploy it on the physical
[00:24:24] robot and here the goal is to bring the
[00:24:26] hockey puck towards the red dot and you
[00:24:30] will see that it will struggle and the
[00:24:38] reason it struggles is because of the
[00:24:39] systematic differences between the
[00:24:41] simulator and the real physical robot so
[00:24:47] I can even the basic movement is
[00:24:49] difficult for the policy because the
[00:24:51] assumptions are violated so much so if
[00:24:54] you do the training as I discussed we
[00:24:55] train a recurrent neural network policy
[00:24:57] which learns to quickly infer properties
[00:25:00] of the simulator in order to accomplish
[00:25:03] the task you can then give it the real
[00:25:05] thing
[00:25:06] the real physics and it will do much
[00:25:08] better so now this is not a perfect
[00:25:11] technique but it's definitely very
[00:25:12] promising it's promising whenever you
[00:25:14] are able to sufficiently randomize the
[00:25:16] simulator so it's definitely very nice
[00:25:20] to see the closed-loop nature of the
[00:25:22] policy you consider it would push the
[00:25:24] hockey puck and would correct it
[00:25:26] very very gently to bring it to the goal
[00:25:28] yeah so that that was cool so that was
[00:25:35] very that was a cool application of meta
[00:25:37] learning I want to discuss one more
[00:25:40] application of meta learning which is
[00:25:42] learning a hierarchy of actions and this
[00:25:47] was work done by France at all actually
[00:25:49] kept in France the ancient who did it
[00:25:52] was in high school I mean he wrote this
[00:25:54] paper so one thing that would be nice is
[00:26:04] if reinforcement learning was
[00:26:07] hierarchical if instead of simply taking
[00:26:10] micro actions you've had some kind of
[00:26:12] little subroutines that you could deploy
[00:26:15] maybe the term subroutine is a little
[00:26:17] bit too crude but if you had some idea
[00:26:20] of which action primitives are worth
[00:26:23] starting with now no one has been able
[00:26:26] to to get actually like real value add
[00:26:31] from curricula reinforcement learning
[00:26:33] yet so far all the really cool results
[00:26:35] all the really convincing is also
[00:26:36] reinforcement learning do not use it
[00:26:39] that's because we haven't quite figured
[00:26:42] out what's the right way for
[00:26:44] reinforcement learning for her ocular
[00:26:45] reinforcement learning
[00:26:47] I just want to show you one very simple
[00:26:49] approach where you use meta-learning to
[00:26:55] learn to learn a hierarchy of actions so
[00:26:57] here's what you do you have in this
[00:27:01] specific work you have a certain yeah
[00:27:05] let's say you have a certain number of
[00:27:07] low-level primitives let's say you have
[00:27:09] two ten of them and you have a
[00:27:11] distribution of tasks and your goal is
[00:27:15] to learn low level primitives such that
[00:27:20] when they are used inside a very brief
[00:27:24] run of some reinforcement learning
[00:27:25] algorithm you will make as much progress
[00:27:27] as possible so the idea is you want to
[00:27:31] get the greatest amount of progress you
[00:27:33] want to learn policies that result in
[00:27:35] the great story you want to learn
[00:27:38] primitives that result in the greatest
[00:27:41] amount of progress is possible when used
[00:27:43] inside learning so this is a meta
[00:27:45] learning setter because any distribution
[00:27:46] of tasks and here we've had if we've had
[00:27:50] a little maze here the distribution of a
[00:27:53] mazes and in this case the little bug
[00:27:54] learned three policies which move it in
[00:27:58] its fixed direction and as a result of
[00:28:01] having this hierarchy you're able to
[00:28:02] solve problems really fast but only when
[00:28:04] the hierarchy is correct
[00:28:05] so horican reinforcement learning is
[00:28:07] still working progress and this was an
[00:28:09] and this work is an interesting proof
[00:28:12] point of how Haruko reinforcement could
[00:28:19] be like how heretical reinforcement
[00:28:21] learning could be like if it worked now
[00:28:26] I want to just spend one slide
[00:28:29] addressing the limitations of high
[00:28:32] capacity method learning the specific
[00:28:35] limitation is that the training test
[00:28:41] distribution has to be equal to the test
[00:28:44] test distribution and I think this is a
[00:28:47] real limitation because in reality you
[00:28:50] the new test that you want to learn do
[00:28:52] in some ways being fundamentally
[00:28:54] different from anything you've seen so
[00:28:57] far so for example if you go to school
[00:28:59] you learn lots of useful things but then
[00:29:02] they go to work only a fraction of this
[00:29:05] of the things that you've learned
[00:29:07] carries over you need to learn if you
[00:29:10] need quite a few more things from
[00:29:11] scratch so metal owning would struggle
[00:29:15] with that because it really assumes that
[00:29:17] the Train the training data is that the
[00:29:19] distribution over the training task has
[00:29:21] to be equal to the distribution of the
[00:29:22] test tasks that's the limitation I think
[00:29:25] that as we develop better algorithms for
[00:29:28] being robust when the test tasks outside
[00:29:34] of the distribution of the training
[00:29:35] tasks the metal on would work much
[00:29:38] better now I want to talk about self
[00:29:42] play the links of play is a very cool
[00:29:45] topic that's starting to get attention
[00:29:49] only now and I want to start by
[00:29:52] reviewing very old work called TD gammon
[00:29:56] it's back from all the way from 1992 so
[00:30:00] it's 26 years old now it was done by
[00:30:02] Jerry to cero so this work is really
[00:30:06] incredible because it has so much
[00:30:13] relevance today what they did basically
[00:30:16] they said okay let's take two neural
[00:30:20] networks and let them let them play
[00:30:24] against each other let them play
[00:30:26] backgammon against each other and let
[00:30:28] them in tray let them be trained
[00:30:29] particularly so it's a super-modern
[00:30:32] approach and you would think this was a
[00:30:36] paper from 2017 except that then you
[00:30:39] look at this plot it shows that you only
[00:30:41] have ten hidden units twenty hidden
[00:30:42] units forty and eighty for the different
[00:30:44] M colors where you notice that the
[00:30:47] largest neural network works best so in
[00:30:50] some ways not much has changed and this
[00:30:52] is the evidence
[00:30:54] and in fact they were able to beat the
[00:30:57] world champion in backgammon and they
[00:30:58] were able to discover new strategies
[00:31:00] that the best human a backgammon players
[00:31:02] weren't ever not noticed and they've
[00:31:06] determined that the strategy discovered
[00:31:07] by TD gammon actually better
[00:31:09] so that's pure self play with cue
[00:31:11] learning which is which remained dormant
[00:31:16] until the DQ and work with Atari mid
[00:31:19] mind so now other examples of self play
[00:31:27] include alphago zero which was able to
[00:31:30] learn to beat the world champion and go
[00:31:32] without using any external data
[00:31:34] whatsoever another result of this vein
[00:31:37] is by open AI which is our dota 2 BOTS
[00:31:40] which was able to build the world
[00:31:42] champion on the 1v1 version of the game
[00:31:46] and so I want to spend a little bit of
[00:31:49] time talking about the allure of self
[00:31:52] play and why I think it's exciting so
[00:31:58] one important problem that's a that
[00:32:02] that's that we must face as we try to
[00:32:05] build truly intelligent systems is what
[00:32:09] is the task what are we actually
[00:32:11] teaching the systems to do and one very
[00:32:15] attractive attribute of self play is
[00:32:17] that the agents create the environment
[00:32:24] by virtue of the agent acting in the
[00:32:26] environment the environment becomes
[00:32:30] difficult for the other agents and you
[00:32:32] can see here an example of an iguana
[00:32:34] interacting with snakes that try to eat
[00:32:36] it
[00:32:37] unsuccessfully this time so we can see
[00:32:40] what will happen in a moment the iguana
[00:32:43] strains best and so the fact you have
[00:32:46] this arms race between the snakes and
[00:32:49] the iguana
[00:32:50] motivates their development potentially
[00:32:54] without bound and this is what happens
[00:32:56] in effect in but in biological evolution
[00:32:59] now interesting work in this direction
[00:33:02] was done in 1994 but Carl says there is
[00:33:06] a really cool video on YouTube by Carl
[00:33:09] seems you should check it out which
[00:33:11] really kind of shows all the work that
[00:33:12] he's done and here you have a little
[00:33:15] competition between agents where you
[00:33:17] evolved both the behavior and their
[00:33:19] morphology when you when the agents is
[00:33:22] trying to gain possession of a green
[00:33:24] cube and so you can see that the agents
[00:33:29] create the challenge for each other and
[00:33:30] that's why they need to develop so one
[00:33:36] thing that we did and this is work by
[00:33:38] advance a little from open ai is we said
[00:33:43] okay well can we demonstrate some
[00:33:46] unusual results in self play that would
[00:33:48] really convince us that there is
[00:33:50] something there so what we did here is
[00:33:53] that we created a small a small ring and
[00:33:56] you have these two humanoid figures and
[00:33:58] their goal is just to push each other
[00:34:00] outside the ring and they don't know
[00:34:03] anything about wrestling they don't know
[00:34:05] anything about standing your balance in
[00:34:07] each other they don't know anything
[00:34:08] about centers of gravity all they know
[00:34:10] is that if you don't do a good job then
[00:34:13] your competition is going to do a better
[00:34:14] job now one of the really attractive
[00:34:17] things about self play is that you
[00:34:22] always have an opponent that's roughly
[00:34:25] as good as you are in order to learn you
[00:34:29] need to sometimes win and sometimes lose
[00:34:32] but you can't always win sometimes you
[00:34:35] must fail sometimes you must succeed so
[00:34:39] let's see what will happen here yeah so
[00:34:43] it was able to do so the green humanoid
[00:34:44] was able to block the ball in a Cell in
[00:34:48] a well balanced self play environment
[00:34:53] petition is always level no matter how
[00:34:55] good you are or how bad you are you have
[00:34:58] a competition that makes it exact
[00:35:00] exactly of exactly the right challenge
[00:35:02] for you on one thing here so this video
[00:35:04] shows transfer learning it takes a
[00:35:06] little wrestling humanoid and you take
[00:35:09] its friend away and you start applying a
[00:35:12] big large random forces on it and you
[00:35:14] see if it can maintain its balance and
[00:35:16] the answer turns out to be but yes it
[00:35:19] can because it's been trained against an
[00:35:22] opponent it pushes it and so that's why
[00:35:25] even if it doesn't understand where the
[00:35:27] fresh force is being applied on it it's
[00:35:29] still able to balance itself so this is
[00:35:31] one potentially attractive feature of
[00:35:35] subway environments that you could learn
[00:35:36] a certain broad set of skills although
[00:35:40] it's real hard to control the square the
[00:35:42] skills will be and so the biggest open
[00:35:44] question with this research is how do
[00:35:46] you learn agents in a software
[00:35:49] environment such that they do whatever
[00:35:53] they do but then they are able to solve
[00:35:55] a battery of tasks that is useful for us
[00:35:58] that is explicitly specified externally
[00:36:00] yeah I also want to want to highlight
[00:36:06] one attribute of self play environments
[00:36:09] that we've observed in our dota BOTS and
[00:36:12] that is that we've seen a very rapid
[00:36:13] increase in the competence of the bots
[00:36:15] so over the period over the course of
[00:36:17] maybe five months we've seen the bots go
[00:36:19] from playing totally randomly all the
[00:36:24] way to the world champion and the reason
[00:36:28] for that is that once you have a self
[00:36:30] play environment if we put compute into
[00:36:33] it you turn it into data self play
[00:36:36] allows you to turn compute into data and
[00:36:40] I think you will see a lot more of that
[00:36:41] as being an extremely important thing to
[00:36:44] be able to turn compute into essentially
[00:36:46] data generalization simply because the
[00:36:50] speed of neural net processors will
[00:36:51] increase very dramatically over the next
[00:36:53] few years so neural net cycles will be
[00:36:55] cheap and it will be important to make
[00:36:57] use of this new of newly-found
[00:37:00] overabundance of cycles
[00:37:02] I also want to talk a little bit about
[00:37:04] the endgame of the self approach so one
[00:37:08] thing that we know about the human brain
[00:37:11] is that it has increased in sized fairly
[00:37:14] rapidly over the past two million years
[00:37:17] my theory the reason I think it happened
[00:37:21] is because our ancestors got to a point
[00:37:25] where the thing that's most important
[00:37:27] for your survival is your standing in
[00:37:30] the tribe and less the tiger and the
[00:37:33] lion once the most important thing is
[00:37:36] how you deal with those other things
[00:37:39] which have a large brain then it really
[00:37:40] helps to have a slightly larger brain
[00:37:42] and I think that's what happened and
[00:37:44] there exists at least one paper from
[00:37:47] science which supports this point of
[00:37:48] view so apparently there has been
[00:37:51] convergent evolution between social apps
[00:37:54] and social Birds even though in terms of
[00:37:57] various behaviors even though the
[00:38:02] divergence in evolutionary timescale
[00:38:04] between humans and birds has occurred a
[00:38:07] very long time ago and humans and humans
[00:38:09] apes and humans apes and birds have very
[00:38:12] different brain structure so I think
[00:38:17] what should happen if we succeed if we
[00:38:19] successfully follow the path of this
[00:38:22] approach is that you should create a
[00:38:23] society of agents which will have
[00:38:25] language and theory of mind negotiation
[00:38:29] social skills trade economy politics
[00:38:33] justice system all these things should
[00:38:35] happen inside the multi-agent
[00:38:37] environment and it will also be some
[00:38:39] alignment issue of how do you make sure
[00:38:41] that the agents we learn behave in a way
[00:38:43] that we want now I want to make a
[00:38:46] speculative digression here which is I
[00:38:51] want to make the following observation
[00:38:56] if you believe that this kind of society
[00:39:01] of agents is a plausible place where
[00:39:05] truly where the fuller fully general
[00:39:10] intelligence will emerge and if you
[00:39:12] accept that our experience with the dota
[00:39:16] BOTS we've seen a very rapid increase in
[00:39:17] competence will carry over once all the
[00:39:20] details are right if you assume both of
[00:39:22] these conditions then it should follow
[00:39:26] that we should see a very rapid increase
[00:39:27] in the competence of our agents as they
[00:39:30] live in the Society of agents so now
[00:39:34] that we've talked about a potentially
[00:39:38] interesting way of increasing the
[00:39:41] competence and teachings of an agent's
[00:39:43] social skills and language and a lot of
[00:39:46] things that actually exist in humans as
[00:39:48] well we want to talk a little bit about
[00:39:50] how you convey goals to agents and the
[00:39:57] question of the main goal to eight calls
[00:39:58] to agents is just a technical problem
[00:40:00] but it will be important because it is a
[00:40:05] lot more likely than not that the agents
[00:40:09] of evil train will eventually be
[00:40:12] dramatically smarter than us and this is
[00:40:14] work by the opening eye safety team by
[00:40:17] Paul Christiana at all and others so I'm
[00:40:22] just going to show you this video which
[00:40:23] basically explains how the whole thing
[00:40:25] works you there is some behavior looking
[00:40:29] for and you the human gets to see pairs
[00:40:33] of behaviors and you simply click on the
[00:40:36] one that looks better and after a very
[00:40:41] modest number of clicks you can get this
[00:40:45] little simulated leg to do back flips
[00:40:49] and there
[00:40:57] go picking out the back flips and in
[00:41:00] this to get this specific behavior it
[00:41:02] took about 500 clicks by human
[00:41:06] annotators the way it works is that you
[00:41:09] take all the so this is a very data
[00:41:11] efficient reinforcement learning
[00:41:13] algorithm but it is efficient in terms
[00:41:15] of rewards and not in terms of the
[00:41:18] environment interactions so what you do
[00:41:20] here is that you take all the clicks so
[00:41:22] you've got your here is one B here which
[00:41:26] is better than other you fit a reward
[00:41:29] function a numerical reward function to
[00:41:32] those clicks so you want to fit a reward
[00:41:34] function which satisfies those clicks
[00:41:35] clicks and you optimize this reward
[00:41:37] function with reinforcement learning and
[00:41:38] it actually works so this requires 500
[00:41:42] bits of information you've also been
[00:41:45] able to train lots of Atari games using
[00:41:48] several thousand bits of information so
[00:41:49] in all these cases you had human and
[00:41:51] human annotators or human judges just
[00:41:54] like in the previous slide looking at
[00:41:57] the pairs of trajectories and clicking
[00:42:00] on the one that they thought was better
[00:42:02] and here's an example of an unusual goal
[00:42:07] where this is a car racing game but the
[00:42:10] goal was to ask the the agent to train
[00:42:14] the white car drive right behind the
[00:42:17] orange car so it's a different goal and
[00:42:19] it was very straightforward to
[00:42:21] communicate this goal using this
[00:42:23] approach so then to finish off alignment
[00:42:30] is a technical problem it has to be
[00:42:31] solved but of course the determination
[00:42:35] of the correct goals we want array
[00:42:36] assistance the systems to have will be a
[00:42:38] very challenging political problem and
[00:42:41] on this note I want to thank you so much
[00:42:44] for your attention and I just want to
[00:42:47] say that will be a happy hour at
[00:42:48] Cambridge Brewing Company at 8:45 if you
[00:42:50] want to chat more about AI and other
[00:42:52] topics please come by I think that
[00:42:55] deserves an applause
[00:43:03] so back propagation is a or neural
[00:43:07] networks of bio-inspired but back
[00:43:09] propagation doesn't look as though it's
[00:43:10] what's going on in the brain because
[00:43:12] signals in the brain go one direction
[00:43:14] down the axons whereas back propagation
[00:43:16] requires the errors to be propagated
[00:43:18] back up the the wires so can you just
[00:43:23] talk a little bit about that whole
[00:43:24] situation where it looks as the brain is
[00:43:27] doing something a bit different than our
[00:43:28] highly successful algorithms our
[00:43:31] algorithm is going to be improved once
[00:43:33] we figure out what the brain is doing or
[00:43:35] is the brain really sending signals back
[00:43:37] even though it's got no obvious way of
[00:43:39] doing that what's what's happening in
[00:43:41] that area so that's a great question so
[00:43:44] first of all I'll say that the true
[00:43:45] answer is that the honest answer is that
[00:43:48] I don't know but I have opinions and so
[00:43:52] I'll say two things
[00:43:54] but first of all given that look if you
[00:43:59] agree if we agree like so rather it is a
[00:44:01] true fact the back propagation solves
[00:44:04] the problem of circuit search this
[00:44:08] problem feels like an extremely
[00:44:09] fundamental problem and for this reason
[00:44:12] I think that it's unlikely to go away
[00:44:14] now you also write that the brain
[00:44:16] doesn't obviously do back propagation
[00:44:19] although they've been multiple proposals
[00:44:20] of how it could be how it could be doing
[00:44:22] them for example there's been a work by
[00:44:27] Tim little crap and others where they've
[00:44:29] shown that if you use that it's possible
[00:44:31] to learn a different set of connections
[00:44:33] but can be used for the backward pass
[00:44:36] and that can result in successful
[00:44:37] learning now the reason this hasn't been
[00:44:40] like really pushed to the limit by
[00:44:42] practitioners is because they say well I
[00:44:44] got TF to the gradients I'm just not
[00:44:46] going to worry about it but you are
[00:44:48] right this is an important issue and you
[00:44:51] know one of two things is going to
[00:44:52] happen so my personal opinion is that
[00:44:55] back propagation is just going to stay
[00:44:56] with us till the very end and will
[00:44:58] actually build fully human level and
[00:45:00] beyond systems before we understand how
[00:45:02] the brain does what it does so that's
[00:45:07] what I believe but of course it is a
[00:45:09] difference that has to be acknowledged
[00:45:12] okay thank you do you think it was a
[00:45:14] fair matchup for the dota bot and that
[00:45:18] person given the constraints of the
[00:45:21] system so I'd say that like the biggest
[00:45:23] advantage computers have in games like
[00:45:26] this like one of the big advantages is
[00:45:28] that they obviously have a better
[00:45:30] reaction time although in DotA in
[00:45:33] particular the number of clicks per
[00:45:35] second over the top players is fairly
[00:45:38] small which is different from Starcraft
[00:45:40] so in Starcraft stuff up is a very
[00:45:42] compact mechanically heavy game because
[00:45:45] of a large number of units and so the
[00:45:47] top players that is click all the time
[00:45:49] in DotA every player controls just one
[00:45:52] hero and so that greatly reduces the
[00:45:55] total number of actions they need to
[00:45:56] make now still precision matters I think
[00:45:58] that will discover that but what I think
[00:46:02] it'll really happen is if you'll
[00:46:03] discover that computers have the
[00:46:05] advantage in any domain or rather every
[00:46:11] domain not yet so do you think that the
[00:46:16] emergent behaviors from the agent were
[00:46:18] actually kind of directed because the
[00:46:21] constraints already kinda in place like
[00:46:22] so it was kind of forced discover those
[00:46:23] or do you think that like that was
[00:46:26] actually something quite novel that like
[00:46:28] wow it actually discovered these on its
[00:46:30] own like you didn't actually am biased
[00:46:32] towards constraining it so it's
[00:46:33] definitely discover new strategies and I
[00:46:35] can share an anecdote where our tester
[00:46:38] we have a probe which would test the
[00:46:40] bots and he played against for a long
[00:46:44] time and the bots would do all kinds of
[00:46:46] things against the player the human
[00:46:48] player which were effective then at some
[00:46:50] point that Pro decided to play against
[00:46:53] the better plot Pro and he decided to
[00:46:55] imitate one of the things that the bot
[00:46:56] was doing and this image but by
[00:47:00] imitating if he was able to defeat a
[00:47:02] better pro so I think I think the
[00:47:04] strategy discovers are real and so like
[00:47:06] it means that like this very real
[00:47:08] transformative Tran you know I would say
[00:47:11] I think what that means is that he
[00:47:15] because the strategies discovered by the
[00:47:17] bot of the humans it means that we like
[00:47:19] a fundamental game plays deeply related
[00:47:22] for a long time now I've heard that the
[00:47:25] objective of reinforcement learning is
[00:47:27] to determine a policy that chooses an
[00:47:30] action to maximize the expected reward
[00:47:33] which is what you said earlier would you
[00:47:36] ever want to look at the standard
[00:47:38] deviation of possible rewards does that
[00:47:41] even make sense yeah I mean I think for
[00:47:44] sure I think it's a really application
[00:47:45] dependent one of the reasons to maximize
[00:47:49] the expected reward it's because it's
[00:47:52] easier to design algorithms for it
[00:47:53] so you write down this equation the
[00:47:58] formula you do a little bit of
[00:47:59] derivation you get something which
[00:48:02] amounts to a nice-looking algorithm now
[00:48:03] I think there exist like really there
[00:48:08] exist applications where you'd never
[00:48:10] want to make mistakes and you want to
[00:48:11] work on the standard deviation as well
[00:48:13] but in practice it seems that the just
[00:48:16] looking at the expected reward covers a
[00:48:18] large fraction of the B the situation as
[00:48:23] you'd like to apply this door Thanks
[00:48:28] we talked last week about motivations
[00:48:32] and that has a lot to do with the
[00:48:35] reinforcement and some of the ideas is
[00:48:39] that the our motivations are actually
[00:48:42] connection with others and cooperation
[00:48:45] and I'm wondering if they're thrown off
[00:48:48] and I understand it's very popular to
[00:48:50] have the computers play these
[00:48:52] competitive games but is there any use
[00:48:56] in like having an agent self play
[00:49:00] collaboratively collaborative games Yeah
[00:49:03] right that's an extremely good question
[00:49:05] I don't think one place from which we
[00:49:09] can get some inspiration is from the
[00:49:11] evolution of cooperation
[00:49:12] like I think cooperation like we
[00:49:17] cooperate ultimately because it's much
[00:49:21] better for you the person to be
[00:49:22] cooperative than not and so I think what
[00:49:27] should happen
[00:49:28] if you have a sufficiently open-ended
[00:49:31] game then cooperation will be the
[00:49:34] winning strategy and so I think we will
[00:49:37] get cooperation whether we like it or
[00:49:39] not Hey
[00:49:44] you mentioned the complexity of this
[00:49:47] simulation of friction I was wondering
[00:49:50] if you feel that there exists open
[00:49:52] complexity theoretic problems relevant
[00:49:55] to relevant to AI or whether it's just a
[00:49:57] matter of finding good approximations
[00:49:59] that humans of the types of problems
[00:50:02] that humans tend to solve yeah so
[00:50:04] complexity theory well like at a very
[00:50:09] basic level we know that whatever
[00:50:11] algorithm we gonna run is going to run
[00:50:14] fairly efficiently on some hardware so
[00:50:17] that puts a pretty strict upper bound
[00:50:20] and the true complexity of the problems
[00:50:22] we're solving but by definition we are
[00:50:25] solving problems which aren't too hard
[00:50:26] in a complexity theoretic sense now it
[00:50:30] is also the case that many of the
[00:50:32] problems so while the overall thing that
[00:50:35] we do is not hard from a complexity
[00:50:37] theory makes sense and indeed humans
[00:50:39] cannot solve np-complete problems in
[00:50:41] general it is true that many of the like
[00:50:45] optimization problems that we pose to
[00:50:47] our algorithms are intractable in the
[00:50:49] general case starting from a neural net
[00:50:51] optimization itself it is easy to create
[00:50:54] a family of data sets for a neural
[00:50:56] network with a very small number of
[00:50:57] neurons such that find a global optimum
[00:50:59] is np-complete and so how do we avoid it
[00:51:03] well we just try gradient descent anyway
[00:51:06] and somehow it works but without
[00:51:09] question like we cannot we do not solve
[00:51:14] problems which are truly intractable so
[00:51:17] I mean I hope this answer the question
[00:51:20] hello
[00:51:21] it seems like an important sub-problem
[00:51:24] on the path towards AGI will be
[00:51:26] understanding language and the state of
[00:51:29] generative language modeling right now
[00:51:31] is pretty abysmal what do you think are
[00:51:33] the most productive research
[00:51:35] trajectories towards generative language
[00:51:37] models so
[00:51:39] I'll first say that you are completely
[00:51:41] correct that the situation with language
[00:51:42] is still far from great although
[00:51:44] progress has been made even without any
[00:51:47] particular innovations beyond models
[00:51:51] that exist today simply scaling up
[00:51:53] models that exist today on larger
[00:51:55] datasets is going to go surprisingly far
[00:51:58] not even large datasets but larger and
[00:52:00] deeper models for example if you trained
[00:52:02] a language model be the thousand layers
[00:52:04] and it's the same layer I think it's
[00:52:07] gonna be a pretty amazing language model
[00:52:10] like we don't have the cycles for it yet
[00:52:12] but to think it will change very soon
[00:52:14] now I also agree with you that there are
[00:52:17] some fundamental things missing in a
[00:52:21] current understanding of deep learning
[00:52:23] which prevent us from really solving the
[00:52:27] problem that we want so I think one of
[00:52:28] these problems one of the things that's
[00:52:30] missing is that or that seems like
[00:52:31] patently wrong is the fact that we train
[00:52:37] a model then you stop training the model
[00:52:40] and you freeze it even though it's the
[00:52:43] training process where the magic really
[00:52:45] happens but the magic is that if you
[00:52:48] think about it like the training process
[00:52:51] is the true general part of the whole of
[00:52:54] the whole of the whole story because you
[00:52:56] tends to flow code doesn't care which
[00:52:57] data set to optimize it just says
[00:52:59] whatever just give me the data set I
[00:53:00] don't care which one solve I'll sew them
[00:53:02] all
[00:53:02] so like the ability to do that feels
[00:53:06] really special and I think we are not
[00:53:08] using it at test time like it's hard to
[00:53:12] speculate about like things which you
[00:53:14] don't know the answer but all I'll say
[00:53:15] is that simply train bigger deeper
[00:53:18] language models you'll go surprisingly
[00:53:20] far scaling up but also doing things
[00:53:23] like training a test them and inference
[00:53:24] the test time I think would be another
[00:53:26] important boosts the performance hi
[00:53:30] thank you for the talk so it seems like
[00:53:33] right now another interesting approach
[00:53:34] to solving reinforcement learning
[00:53:36] problems could be to go for the
[00:53:37] evolutionary roots using evolutionary
[00:53:40] strategies and although they have they
[00:53:42] their cave Hut's I wanted to know if I'd
[00:53:44] open a I particularly you're working on
[00:53:46] something related and what are what is
[00:53:48] your general opinion on them
[00:53:50] so like at present I believe that
[00:53:54] something evolutionary strategies is not
[00:53:55] great for reinforcement learning I think
[00:53:58] that normal reinforcement learning
[00:53:59] algorithms especially with big policies
[00:54:02] are better but I think if you want to
[00:54:04] evolve a small compact object like like
[00:54:08] a piece of code for example I think that
[00:54:10] would be a place where this would be
[00:54:12] seriously was considering but this all
[00:54:15] you know evolving a beautiful piece of
[00:54:19] code is a cool idea hasn't been done yet
[00:54:21] so still a lot of work to be done before
[00:54:23] we get there hi thank you so much for
[00:54:26] coming my question is you mentioned what
[00:54:29] is the right go is a political problem
[00:54:31] so I'm wondering if you can elaborate a
[00:54:33] bit on that and also what do you think
[00:54:35] would be their approach for us to maybe
[00:54:37] get there well I can't I can't really
[00:54:41] comment too much because all the
[00:54:42] thoughts that you know we have we now
[00:54:46] have a few people who are thinking about
[00:54:48] this full-time at opening I I don't have
[00:54:52] enough of a super strong opinion to say
[00:54:55] anything too definitive all I can say at
[00:54:58] the very high level is given the size
[00:55:00] like if you go into the future whenever
[00:55:02] soon or late you know whenever it's
[00:55:05] going to happen when you build a
[00:55:06] computer which can do anything better
[00:55:09] than a human it will happen because the
[00:55:11] brain is physical the impact on society
[00:55:14] is going to be completely massive and
[00:55:16] overwhelming it's it's very difficult to
[00:55:20] imagine even if you try really hard and
[00:55:23] I think what it means is that people who
[00:55:25] care a lot and that's what I was
[00:55:28] alluding to the fact that this will be
[00:55:30] something that many people who care
[00:55:32] about strongly and like as the impact
[00:55:36] increases gradually with self-driving
[00:55:38] cars more automation I think we will see
[00:55:40] a lot more people care do we need to
[00:55:43] have a very accurate model of the
[00:55:45] physical world and then simulate that in
[00:55:48] order to have these agents that can
[00:55:51] eventually come out into the real world
[00:55:53] and do something approaching you know
[00:55:56] human level intelligence tasks that's a
[00:55:59] very good question so I think if that
[00:56:02] were the case
[00:56:03] be in trouble and I am very certain that
[00:56:09] it could be avoided so specifically the
[00:56:11] real answer has to be that look you
[00:56:14] learn the problem so we learn to
[00:56:17] negotiate you learn to persist you not a
[00:56:18] lots of different useful life lessons in
[00:56:20] the simulation and yes you learn some
[00:56:22] physics too but then you go outside to
[00:56:24] the real world
[00:56:24] and you have to start over to some
[00:56:26] extent because many of you are deeply
[00:56:28] held assumptions will be false in one of
[00:56:31] the goals so what was that's one reasons
[00:56:33] I care so much about never stopping
[00:56:36] training you've accumulated your
[00:56:38] knowledge now we go into an environment
[00:56:40] for some of your assumptions of valid
[00:56:41] you continue training you try to connect
[00:56:43] the new data to your old data and this
[00:56:45] is an important requirement from our
[00:56:46] algorithms which is already met to some
[00:56:48] extent but it will have to be met a lot
[00:56:49] more so that you can take the partial
[00:56:52] knowledge if you've acquired then go in
[00:56:55] a new situation learn some more
[00:56:57] literally the example of you go to
[00:56:59] school ballon useful things then you go
[00:57:01] to work it's not a perfect it's not you
[00:57:04] know you pour your four years of CS and
[00:57:06] undergrad is not going to fully prepare
[00:57:08] you for whatever it is you need to know
[00:57:09] it work
[00:57:10] it will help somewhat you'll be able to
[00:57:12] get off the ground but it will be lots
[00:57:13] of new things you need to learn so
[00:57:14] that's that's the spirit of it I think
[00:57:16] of a toes of the school one of the
[00:57:19] things you mentioned pretty early on in
[00:57:20] your talk is that one of the limitations
[00:57:22] of this sort of style of reinforcement
[00:57:24] learning is there's no self-organization
[00:57:26] so you have to tell it when it did a
[00:57:28] good thing or did a bad thing and that's
[00:57:30] actually a problem in neuroscience is
[00:57:31] when you're trying to teach a rat to you
[00:57:32] know navigate maze you have to
[00:57:34] artificially tell it what to do so where
[00:57:36] do you see moving forward when we
[00:57:38] already have this problem with teaching
[00:57:39] you know not necessarily learning but
[00:57:41] also teaching so where do you see the
[00:57:42] research moving forward in that respect
[00:57:44] how do you sort of introduce this notion
[00:57:46] of self-organization so I think without
[00:57:48] question one really important thing you
[00:57:50] need to do is to be able to infer the
[00:57:54] goals and strategies of other agents by
[00:57:56] observing them that's a fundamental
[00:57:59] skill we need to be able to learn to to
[00:58:01] embed into the agent so if for example
[00:58:03] you have two agents one of them is doing
[00:58:05] something and the other agent says well
[00:58:07] that's really cool I want to be able to
[00:58:08] do that too and
[00:58:09] you go and do that and so I'd say that
[00:58:11] this is a very important component in
[00:58:12] terms of second every word oh you see
[00:58:16] what they do you infer the reward and
[00:58:19] now we have a knob which says you see
[00:58:21] what they're doing now go and try to do
[00:58:22] the same thing
[00:58:23] let's say this this is as far as I know
[00:58:26] as far as I know this is was one of the
[00:58:27] important ways in which humans are quite
[00:58:31] different from other animals in way
[00:58:34] which in the like scale and scope in
[00:58:40] which we copy the behavior of other
[00:58:41] humans might ask a quick follow-up work
[00:58:45] go for it so that's kind of obvious how
[00:58:47] that works in the scope of competition
[00:58:48] but what about just sort of arbitrary
[00:58:50] tasks like I'm in a math class for
[00:58:52] someone and I see someone doing a
[00:58:53] problem a particular way and I go that's
[00:58:55] a good strategy maybe I should try that
[00:58:56] out how does that work in a sort of non
[00:58:58] competitive environment so I think that
[00:59:00] this will be I think that's going to be
[00:59:03] a little bit separate from the
[00:59:05] competitive environment but it will have
[00:59:07] to be somehow either way you know
[00:59:11] probably baked in maybe volved into the
[00:59:14] system where like if you have other
[00:59:17] agents doing things they're generating
[00:59:20] data which you observe and the only way
[00:59:22] to truly make sense of the data that you
[00:59:24] see is to infer the goal of the agent
[00:59:26] the strategy their belief state that's
[00:59:29] important also for communicating them if
[00:59:32] you want to successfully communicate
[00:59:33] with someone you have to keep track both
[00:59:35] of their goal and of their belief state
[00:59:36] instead of knowledge so I think you will
[00:59:38] find that there are many I guess
[00:59:40] connections between understanding what
[00:59:44] other agents are doing inferring their
[00:59:45] goals imitating them and community
[00:59:47] successfully communicating them all
[00:59:49] right let's give in the happy hour a big
[00:59:51] hand
[00:59:52] [Applause]
[00:59:55] you
[00:59:55] [Applause]
[01:00:05] you
