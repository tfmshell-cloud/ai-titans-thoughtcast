# No Priors Ep. 39: OpenAI Co-Founder & Chief Scientist Ilya Sutskever
- **YouTube URL:** https://www.youtube.com/watch?v=Ft0gTO2K85A
- **Lines:** 1271

---

[00:00:06] OpenAI, a company that we all know now,
[00:00:08] but only a year ago was 100 people, is
[00:00:11] changing the world. Their research is
[00:00:12] leading the charge to AGI.
[00:00:15] Since ChatGPT captured consumer
[00:00:17] attention last November, they show no
[00:00:19] signs of slowing down.
[00:00:20] This week, Elon and I sit down with Ilya
[00:00:22] Sutskever, co-founder and chief
[00:00:24] scientist at OpenAI, to discuss the
[00:00:27] state of AI research, where we'll hit
[00:00:29] limits, the future of AGI, and what's
[00:00:32] going to take to reach super alignment.
[00:00:34] Ilya, welcome to No Priors.
[00:00:36] Thank you. It's good to be here.
[00:00:37] Let's start with the beginning.
[00:00:38] Pre-AlexNet, nothing in deep learning
[00:00:40] was really working. And then, given that
[00:00:42] environment, you guys took a
[00:00:44] um a very unique bet. What motivated you
[00:00:46] to go in this direction?
[00:00:48] Indeed. In those dark ages, AI was not
[00:00:53] an area where people had
[00:00:56] hope, and people were not accustomed to
[00:00:59] any kind of success at all. And because
[00:01:02] there wasn't there hasn't been any
[00:01:03] success, there was a lot of debate, and
[00:01:06] there were different schools of thoughts
[00:01:07] that had different arguments about
[00:01:10] how machine learning and AI should be.
[00:01:13] And you had people who were
[00:01:15] into knowledge representation from a
[00:01:17] good old-fashioned AI. You had people
[00:01:19] who were Bayesians, and they liked
[00:01:21] Bayesian non-parametric methods. You had
[00:01:23] people who liked graphical models, and
[00:01:25] you had the people who liked neural
[00:01:26] networks. Those people were marginalized
[00:01:29] because neural networks did not had the
[00:01:32] property that you can't prove math
[00:01:34] theorems about them.
[00:01:36] If you can't prove theorems about
[00:01:37] something, it means that your research
[00:01:39] isn't good. That's how it has been. But
[00:01:41] the reason why I gravitated to neural
[00:01:43] networks from the beginning is because
[00:01:44] it felt like those are small little
[00:01:46] brains. And who cares if you can't prove
[00:01:49] any theorems about them, because we are
[00:01:50] training small little brains, and maybe
[00:01:52] they'll become maybe they'll do
[00:01:53] something one day.
[00:01:55] And the reason that we were able to do
[00:01:58] AlexNet when we did is because a
[00:02:00] combination of two factors, three
[00:02:03] factors.
[00:02:04] The first factor is that this was
[00:02:06] shortly after GPUs started to be used in
[00:02:09] machine learning.
[00:02:10] People kind of had an intuition that
[00:02:12] that's a good thing to do, but
[00:02:14] it wasn't like today where people
[00:02:15] exactly knew what they needed GPUs for.
[00:02:17] It was like, "Oh, let's like play with
[00:02:18] those cool fast computers and see what
[00:02:20] we can do with them." It was an
[00:02:21] especially good fit for neural networks,
[00:02:23] so that was a very that definitely
[00:02:25] helped us.
[00:02:27] I was very fortunate in that I was able
[00:02:29] to realize that
[00:02:31] the reason neural networks of the time
[00:02:34] weren't good is because they were too
[00:02:36] small. So, like if you try to solve a
[00:02:39] vision task with a neural network which
[00:02:41] has like
[00:02:42] a thousand neurons, what can it do? It
[00:02:45] can't do anything. It doesn't matter how
[00:02:47] good your learning is and everything
[00:02:48] else.
[00:02:49] But if you have a much larger neural
[00:02:50] network, you'll do something
[00:02:51] unprecedented.
[00:02:52] What What gave you that intuition to
[00:02:54] think that that was the case?
[00:02:55] Because I think at the time it was
[00:02:57] reasonably
[00:02:58] um contrarian to think that despite to
[00:03:00] your point, you know, a lot of the the
[00:03:01] human brain in some sense works that way
[00:03:03] or different, you know, biological
[00:03:04] neural circuits. But I'm just curious
[00:03:05] like what gave you that intuition early
[00:03:07] on to think that this was a good
[00:03:08] direction.
[00:03:09] [sighs and gasps]
[00:03:09] I think yeah, looking at the brain and
[00:03:11] specifically the if you if like
[00:03:14] all those things
[00:03:16] follow very easily if you allow yourself
[00:03:20] if you allow yourself to accept the
[00:03:23] idea. Right now, this idea
[00:03:25] Yeah, is reasonably well accepted.
[00:03:27] Back then, people still talked about it,
[00:03:29] but they haven't really accepted it or
[00:03:31] internalized the idea that maybe an
[00:03:34] artificial neuron in some sense is not
[00:03:37] that different from a biological neuron.
[00:03:39] So, now whatever you imagine animals do
[00:03:41] with their brains, you could perhaps
[00:03:43] assemble some artificial neural network
[00:03:46] of similar size. Maybe if you train it
[00:03:48] to
[00:03:48] it will do something similar.
[00:03:50] So, there
[00:03:52] So, that leads to the
[00:03:54] So, that leads you to start to imagine,
[00:03:56] okay? Like you almost imagine the
[00:03:57] computation being done by the neural
[00:03:59] network. You can almost think like if
[00:04:00] you have a high-resolution image and you
[00:04:02] have like
[00:04:04] one neuron for like a large group of
[00:04:06] pixels, what can the neuron do? It's
[00:04:08] just It's just not much it can do. If
[00:04:09] you But if you have a lot of neurons,
[00:04:11] then they can actually do something and
[00:04:12] compute something.
[00:04:13] So, I think it was like our like it was
[00:04:15] This was It was considerations like this
[00:04:17] plus a technical realization. The
[00:04:20] technical realization is
[00:04:22] that
[00:04:24] if you have a large training set that
[00:04:27] specifies the behavior of the neural
[00:04:29] network
[00:04:31] and the training set is large enough
[00:04:33] such that it can constrain the large
[00:04:35] neural networks efficiently.
[00:04:37] And furthermore, if you have the
[00:04:39] algorithm to find that neural network
[00:04:40] because what we do is that we turn the
[00:04:43] training set
[00:04:45] into a neural network which satisfies
[00:04:47] the training set. Neural network
[00:04:49] training can almost be seen as solving a
[00:04:53] neural equation.
[00:04:56] Solving a neural equation where every
[00:04:58] data point is an equation
[00:05:00] and every parameter is a variable.
[00:05:04] And so
[00:05:06] it was multiple things. The realization
[00:05:08] that a bigger neural network could do
[00:05:10] something unprecedented. The realization
[00:05:13] that if you have a large data set
[00:05:16] together with the compute
[00:05:18] to solve the neural equation. That's
[00:05:20] what
[00:05:21] gradient descent comes in, but it's not
[00:05:23] gradient descent. Gradient descent was
[00:05:24] around for a long time. It was certain
[00:05:27] technical insights about how to make it
[00:05:29] work because back then the prevailing
[00:05:31] belief was well, you can't train those
[00:05:32] neural nets anything. It's all hopeless.
[00:05:34] So, it wasn't just about the size. It
[00:05:35] was about Even if someone did think,
[00:05:38] "Gosh, it would be cool to train a big
[00:05:39] neural net." They didn't have the
[00:05:41] technical
[00:05:43] ability to turn this idea into reality.
[00:05:46] You needed not only to to code the
[00:05:47] neural net, you need to do a bunch of
[00:05:49] things right.
[00:05:50] And only then it will work.
[00:05:52] And then another fortunate thing is that
[00:05:54] the person whom I work with, Alex
[00:05:56] Krizhevsky,
[00:05:57] he
[00:05:58] just discovered that he really loves
[00:06:00] GPUs, and he was perhaps one of the the
[00:06:02] the first person who really mastered
[00:06:06] writing really like really performing
[00:06:08] code for for the GPUs. And that's why we
[00:06:10] were able to squeeze a lot of
[00:06:11] performance out of two GPUs and do
[00:06:13] something and produce something
[00:06:14] unprecedented. So, to sum up,
[00:06:16] it was multiple things.
[00:06:19] The idea that a big neural network, in
[00:06:21] this case a a vision neural network, a
[00:06:23] convolutional neural network with many
[00:06:24] layers,
[00:06:26] one that's much much bigger than
[00:06:27] anything that's ever been done before
[00:06:29] could do something very unprecedented
[00:06:31] because the brain can see, and the brain
[00:06:33] is a large neural network. And we can
[00:06:35] see quickly, so our neurons don't have a
[00:06:36] lot of time. Then the compute needed,
[00:06:39] the technical know-how, that in fact we
[00:06:42] can train such neural networks, and it
[00:06:44] was not at all widely distributed. Most
[00:06:46] people in machine learning would not
[00:06:48] have been able to train such a neural
[00:06:50] network even if they wanted to.
[00:06:52] Did you guys have any um like particular
[00:06:55] goal from a size perspective, or was it
[00:06:58] just as as uh you know, and as as
[00:07:00] biologically inspired or where that
[00:07:02] number comes from or just as large as we
[00:07:03] can go?
[00:07:04] Definitely as large as we can go. Cuz
[00:07:06] keep in mind, I mean, we had a certain
[00:07:08] amount of compute which we could
[00:07:10] usefully consume,
[00:07:11] and then what can it do?
[00:07:13] Maybe if we think about just like uh the
[00:07:16] origin of OpenAI and uh the goals of the
[00:07:20] organization, like what was the original
[00:07:22] goal and how's that evolved over time?
[00:07:24] The goal did not evolve over time.
[00:07:26] The tactic evolved over time.
[00:07:30] So, the goal of OpenAI from the very
[00:07:33] beginning
[00:07:34] has been to make sure
[00:07:36] that artificial general intelligence,
[00:07:39] by which we mean autonomous systems,
[00:07:42] AI that can actually do most of the jobs
[00:07:46] and activities and tasks that people do
[00:07:49] benefits all of humanity.
[00:07:51] That was the goal from the beginning.
[00:07:53] The initial thinking has been that maybe
[00:07:57] the best way to do it is by just open
[00:07:59] sourcing a lot of technology.
[00:08:02] We later and we also attempted to do it
[00:08:05] as a non-profit. Seemed very sensible.
[00:08:07] This is the goal.
[00:08:09] Non-profit is the way to do it.
[00:08:11] What changed? Some point at OpenAI
[00:08:15] we realized and we were
[00:08:17] perhaps among among the the earlier the
[00:08:19] earliest to realize that
[00:08:21] to make progress in AI for real, you
[00:08:23] need a lot of compute.
[00:08:25] Now, what does a lot mean? The appetite
[00:08:27] for computer is truly endless as
[00:08:30] as now as it is now clearly seen, but we
[00:08:32] realized we will need a lot.
[00:08:34] And
[00:08:36] a non-profit was wouldn't wouldn't be
[00:08:38] the way to to to get there.
[00:08:40] Wouldn't be able to build a large
[00:08:41] cluster with a non-profit. That's why we
[00:08:43] became we converted into this unusual
[00:08:46] structure
[00:08:47] called cap profit.
[00:08:49] And to my knowledge, we are the only cap
[00:08:51] profit company in the world.
[00:08:53] But the idea is that investors put in
[00:08:56] some money, but even if the company does
[00:08:58] incredibly well, they don't get more
[00:09:00] than some multiplier on top of their
[00:09:02] original investment.
[00:09:04] And the reason to do this, the reason
[00:09:06] why that makes sense
[00:09:09] you know, there are arguments One could
[00:09:10] make arguments against it as well.
[00:09:12] But the argument for it is that
[00:09:15] if you believe
[00:09:17] that the technology that we are
[00:09:18] building, AGI
[00:09:21] could potentially
[00:09:23] be so capable as to do every single task
[00:09:27] that people do
[00:09:29] does it mean that it might unemploy
[00:09:31] everyone?
[00:09:33] Well, I don't know, but it's not
[00:09:34] impossible. And if that's the case, it
[00:09:36] makes sense. It will make a lot of sense
[00:09:38] if the company that built such a
[00:09:39] technology would not be able to make
[00:09:42] infinite would not be incentivized
[00:09:45] rather to make infinite profits. I don't
[00:09:46] know if it will literally play out this
[00:09:48] way because of competition in AI. So
[00:09:51] there will be multiple companies and I
[00:09:53] think that will
[00:09:55] have some unforeseen implications on the
[00:09:57] argument which I'm making, but that was
[00:09:58] the thinking.
[00:09:59] I remember visiting the offices back
[00:10:01] when you were I think housed at YC or
[00:10:03] something or you know cohabitated some
[00:10:04] space there and at the time there was
[00:10:07] a suite of different efforts. There was
[00:10:09] robotic arms
[00:10:10] that were being manipulated and then
[00:10:12] there was
[00:10:13] you know some video game related work
[00:10:14] which was really cutting edge.
[00:10:16] How did you think about how the research
[00:10:18] agenda evolved and what really drove it
[00:10:20] down this path of transformer based
[00:10:22] models and other forms of of learning?
[00:10:24] So our thinking
[00:10:27] has been evolving
[00:10:28] over the years from when we started
[00:10:30] OpenAI.
[00:10:31] In the first year we indeed did some of
[00:10:33] the more conventional machine learning
[00:10:35] work. By conventional machine learning
[00:10:37] work I mean because the world has
[00:10:38] changed so much a lot of things which
[00:10:40] were
[00:10:42] known to everyone in 2016 or 2017 are
[00:10:44] completely and utterly forgotten. It's
[00:10:46] like this the Stone Age almost. So in
[00:10:48] that in that Stone Age the world the
[00:10:51] world of machine learning looked very
[00:10:52] different.
[00:10:53] It was
[00:10:55] dramatically more academic.
[00:10:58] The goals, values, and objectives were
[00:11:01] much more academic. They were about
[00:11:03] discovering small bits of knowledge and
[00:11:05] sharing them with the other researchers
[00:11:07] and getting scientific recognition as a
[00:11:08] result. And it's a very valid goal and
[00:11:11] it's very understandable. I've been
[00:11:12] doing AI for 20 years now. More than
[00:11:14] half of my time that I spent in AI was
[00:11:16] in that framework. And so what do you
[00:11:18] do?
[00:11:19] You write papers. You share your small
[00:11:21] discoveries. Two realizations. The first
[00:11:23] realization is
[00:11:25] just at a high level it doesn't seem
[00:11:26] like it's the way to go to
[00:11:29] for a dramatic impact. And why is that?
[00:11:32] Because if you imagine
[00:11:34] how an AGI should look like,
[00:11:36] it has to be some kind of a big
[00:11:39] engineering project that's using a lot
[00:11:41] of compute.
[00:11:42] Right? Even if you don't know how to
[00:11:44] build it, what that should look like,
[00:11:45] you know that this is the ideal you want
[00:11:46] to strive towards. So, you want to
[00:11:48] somehow move towards larger projects as
[00:11:50] opposed to small projects. So, while we
[00:11:52] attempted
[00:11:54] a first large project
[00:11:56] where we trained a neural network to
[00:11:58] play a real-time strategy game as well
[00:12:00] as as well as the best humans. It's the
[00:12:03] Dota 2 project and it was
[00:12:05] it was driven by two people, uh
[00:12:08] Jakub Pachocki and Greg Brockman. They
[00:12:10] they really drove this project and make
[00:12:12] it made it a success. And this was our
[00:12:13] first attempt at a large project.
[00:12:17] But it wasn't quite the right formula
[00:12:19] for us because that the neural networks
[00:12:21] were a little bit too small. It was just
[00:12:23] a narrow domain, just a game. I mean,
[00:12:25] it's cool to play a game. And we kept
[00:12:26] looking. And at some point we realized
[00:12:28] that, "Hey, if you train a large neural
[00:12:30] network,
[00:12:32] a very, very large transformer
[00:12:34] to predict text better and better,
[00:12:36] something very surprising will happen."
[00:12:38] This realization also arrived a little
[00:12:39] bit gradually. We
[00:12:41] were exploring generative models. We
[00:12:44] were exploring ideas around next word
[00:12:46] prediction.
[00:12:48] Those are ideas also related to
[00:12:49] compression. We were exploring them.
[00:12:52] Then transformer came out. We got really
[00:12:53] excited. We were like, "This is This is
[00:12:55] the greatest thing. We're going to do
[00:12:56] transformers now. It's clearly superior
[00:12:58] than anything else before it." We
[00:13:00] started doing transformers. We did
[00:13:01] GPT-1. GPT-1 started to show very
[00:13:04] interesting signs of life.
[00:13:06] And that led us to doing GPT-2 and then
[00:13:08] ultimately GPT-3. GPT-3 really opened
[00:13:11] everyone else's eyes as well to, "Hey,
[00:13:13] this thing has a lot of traction." There
[00:13:15] is one specific formula right now that
[00:13:18] everyone is doing. And this formula is
[00:13:20] train a larger and larger transformer on
[00:13:23] more and more data.
[00:13:24] I mean, for me the big wake-up moment to
[00:13:26] your point was
[00:13:27] to GPT-3 transition where you saw such a
[00:13:29] big step function in capabilities and
[00:13:32] then obviously with four open AI's
[00:13:34] published some really interesting
[00:13:36] uh
[00:13:37] research around some of the different
[00:13:39] domains of knowledge or domains of
[00:13:41] expertise or chain of thought or other
[00:13:42] things that the models can suddenly do
[00:13:44] in an emergent form.
[00:13:45] What was the most surprising thing for
[00:13:47] you in terms of emergent behavior in
[00:13:48] these models over time?
[00:13:50] You know, it's very hard to answer that
[00:13:51] question. It's very hard to answer
[00:13:53] because I'm too close and I've seen it
[00:13:55] progress every step of the way.
[00:13:58] So,
[00:13:59] as much as I'd like, I find it very hard
[00:14:00] to answer that question. I think if I
[00:14:03] had to pick one,
[00:14:06] I think maybe the the most surprising
[00:14:07] thing for me is the whole thing works at
[00:14:10] all, you know?
[00:14:12] It's hard it's I'm not sure I I know how
[00:14:15] to convey this what what I have in mind
[00:14:17] here because if you see a lot of neural
[00:14:20] networks do amazing things, well,
[00:14:22] obviously neural networks is the thing
[00:14:24] that works.
[00:14:25] But I have
[00:14:27] witnessed personally
[00:14:28] what it's like to be in a world for many
[00:14:30] years
[00:14:32] where the neural networks don't work at
[00:14:33] all.
[00:14:34] And then to contrast that to where we
[00:14:36] are today,
[00:14:38] just the fact that they work and they do
[00:14:39] these amazing things, I think maybe the
[00:14:42] most surprising thing the most
[00:14:43] surprising if I had to pick one, it
[00:14:45] would be the fact that when I speak to
[00:14:47] it, I feel understood.
[00:14:49] Gathers there's a really good
[00:14:51] saying from I'm trying to remember maybe
[00:14:52] it's Arthur Clark or one of the sci-fi
[00:14:54] authors which is
[00:14:55] effectively it says advanced technology
[00:14:58] is sometimes indistinguishable from
[00:14:59] magic.
[00:15:01] Yeah, I'm I'm fully in this camp.
[00:15:03] Yeah. Yeah, it definitely feels like
[00:15:04] there's some magical moments with with
[00:15:06] some of these models now.
[00:15:07] Is there a way that you guys decide
[00:15:10] internally given all of the different
[00:15:13] capabilities you could pursue how to
[00:15:16] continually choose the set of big
[00:15:18] projects? You've sort of described that
[00:15:20] centralization and committing to certain
[00:15:23] research directions at scale is really
[00:15:26] important to OpenAI's success. Given the
[00:15:28] breadth of opportunity now, like what's
[00:15:29] the process for deciding what's worth
[00:15:31] working on?
[00:15:33] I mean, I think there is some
[00:15:34] combination of bottom-up and top-down
[00:15:36] where we have some top-down ideas that
[00:15:39] we believe should work, but we're not
[00:15:41] 100% sure.
[00:15:43] So, we still we need to have good
[00:15:45] top-down ideas, and there's a lot of
[00:15:47] bottom-up exploration that's guided by
[00:15:48] those top-down ideas as well.
[00:15:50] And their combination is what informs us
[00:15:53] as to what to do next.
[00:15:55] And if you think about those bottom I
[00:15:58] mean, either direction, top-down or
[00:15:59] bottom-up ideas, like clearly we have
[00:16:02] this dominant continue to scale
[00:16:04] transformers direction.
[00:16:07] Do you explore additional like
[00:16:09] architectural directions, or is that
[00:16:10] just not relevant?
[00:16:11] It's certainly possible that various
[00:16:13] improvements can be found.
[00:16:16] I think I think improvements can be
[00:16:18] found in all kinds of places, both small
[00:16:20] improvements and large improvements.
[00:16:22] I think the way to think about it is
[00:16:23] that while the current thing that's
[00:16:26] being done
[00:16:28] keeps getting better
[00:16:30] as you keep on increasing the amount of
[00:16:32] compute and data that you put into it.
[00:16:35] So, we have that property. The bigger
[00:16:36] you make it, the better it gets.
[00:16:39] It is also the property that different
[00:16:41] things
[00:16:42] get better by different amounts
[00:16:46] as you keep on improving as you keep on
[00:16:47] scaling them up. So, not only do we
[00:16:49] want, of course, scale up what we're
[00:16:51] doing, we also want to scale keep
[00:16:52] scaling up the best thing possible.
[00:16:55] What is uh
[00:16:56] a I mean, you you probably don't need to
[00:16:58] predict because you can see internally.
[00:17:00] What do you think is improving most from
[00:17:03] a capability perspective in the current
[00:17:05] generation of scale?
[00:17:06] The best way for me to answer this
[00:17:08] question
[00:17:09] would be to point out the
[00:17:14] to point to the models that are publicly
[00:17:17] available. And you can see how they
[00:17:19] compare from this year to last year.
[00:17:22] And the difference is quite significant.
[00:17:24] I'm not talking about the difference
[00:17:25] between not only the difference between
[00:17:28] let's say you can look at the difference
[00:17:29] between GPT-3 and GPT-3.5 and then
[00:17:32] ChatGPT, ChatGPT-4, ChatGPT-4 with
[00:17:35] vision.
[00:17:36] And you can just see for yourself. It's
[00:17:37] easy to forget where things used to be,
[00:17:39] but certainly the big way in which
[00:17:42] things are changing is that these models
[00:17:44] become more and more reliable.
[00:17:47] Before they were very they were only
[00:17:49] very partly there. Right now they are
[00:17:52] mostly there, but there are still gaps.
[00:17:54] And in the future perhaps these models
[00:17:56] will be there even more. You could trust
[00:17:59] their answers. They'll be more reliable.
[00:18:01] They'll be able to do more tasks in
[00:18:03] general across the board.
[00:18:05] And then another thing that they will do
[00:18:07] is that they'll have deeper insight. As
[00:18:09] we train them,
[00:18:10] they gain more and more insight into the
[00:18:12] true nature of the human world.
[00:18:16] And their insight will continue to
[00:18:17] deepen.
[00:18:18] I I was just going to ask about how that
[00:18:20] relates to a sort of model scale over
[00:18:22] time because a lot of people are
[00:18:25] really stricken by the capabilities of
[00:18:27] the very large-scale models and the
[00:18:29] emergent behavior in terms of
[00:18:30] understanding of the world.
[00:18:32] And then in parallel as people
[00:18:33] incorporate some of these things into
[00:18:35] products, which is a very different type
[00:18:36] of path,
[00:18:37] they often start worrying about
[00:18:38] inference cost going up with the scale
[00:18:40] of the model and therefore they're
[00:18:41] looking for smaller models that are
[00:18:42] fine-tuned. But then of course you may
[00:18:44] lose some of the capabilities around
[00:18:46] some of the insights and ability to to
[00:18:48] reason.
[00:18:49] And so I was curious in your thinking in
[00:18:51] terms of how all this evolves over the
[00:18:52] coming years.
[00:18:53] I would actually point out that the main
[00:18:55] thing that's lost when you switch to the
[00:18:56] smaller models is reliability. I would
[00:18:59] argue that at this point it is
[00:19:01] reliability
[00:19:02] that's the biggest bottleneck
[00:19:05] to these models being truly useful.
[00:19:07] How are you defining reliability?
[00:19:09] So it's like when you ask the question
[00:19:11] that's not much harder
[00:19:13] than other questions that the model
[00:19:15] succeeds at.
[00:19:17] Then you'll have very high degree of
[00:19:19] confidence that it will continue to
[00:19:20] succeed. So, I'll give you an example.
[00:19:22] Let's suppose that I want to learn about
[00:19:24] some historical thing.
[00:19:26] And I can ask, well, what tell me what
[00:19:28] is the prevailing opinion about this and
[00:19:30] about that, and I can keep asking
[00:19:31] questions.
[00:19:32] And let's suppose it answered 20 of my
[00:19:34] questions correctly.
[00:19:36] I really don't want the 21st question to
[00:19:38] have a gross gross mistake.
[00:19:41] That's what I mean by by reliability. Or
[00:19:43] like let's suppose I upload some
[00:19:44] documents, some financial documents.
[00:19:46] Suppose they say something, I want you
[00:19:47] to do some analysis and to make some
[00:19:49] conclusion, and I want to take action on
[00:19:50] this based on this conclusion.
[00:19:53] And it's like it's not a super hard
[00:19:54] task.
[00:19:55] And the the model these models clearly
[00:19:57] succeed on this task most of the time.
[00:19:59] But because they don't succeed all the
[00:20:00] time, and if it's a consequential
[00:20:01] decision, I actually can't trust the
[00:20:03] model any of those times, and I have to
[00:20:05] verify the answer somehow.
[00:20:07] So, that's how I define reliability.
[00:20:08] It's very similar to the self-driving
[00:20:10] situation, right? If you have a
[00:20:11] self-driving car, and it's like
[00:20:14] does things mostly well, that's not good
[00:20:16] enough. Situation is not as extreme as
[00:20:18] with a self-driving car, but that's what
[00:20:19] I mean by reliability.
[00:20:21] My perception of reliability is that it
[00:20:23] um
[00:20:24] to your point, it it goes up with model
[00:20:25] scale, but also it goes up in if you
[00:20:28] fine-tune for specific use cases or
[00:20:30] instances or data sets. And so, there is
[00:20:32] that trade-off in terms of size versus
[00:20:35] uh
[00:20:36] you know, specialized fine-tuning versus
[00:20:38] reliability.
[00:20:39] So, certainly people who care about some
[00:20:42] specific application have every
[00:20:44] incentive to get the smallest model
[00:20:46] working
[00:20:47] well enough.
[00:20:49] I think that's true. It's undeniable. I
[00:20:51] think anyone who cares about a specific
[00:20:53] application will want the smallest model
[00:20:55] for it. That's self-evident.
[00:20:57] I do think though that as models
[00:20:58] continue to get larger and better, then
[00:21:01] they will unlock new and unprecedentedly
[00:21:04] valuable applications. So, yeah, the the
[00:21:07] small models will have their niche for
[00:21:08] the less interesting applications, which
[00:21:10] are still very useful. And then the
[00:21:11] bigger models will be delivering on
[00:21:15] applications with Okay, let's let's pick
[00:21:17] an example.
[00:21:18] Consider the task of producing good
[00:21:21] legal advice. It's really valuable if
[00:21:23] you can really trust the answer. Maybe
[00:21:25] you need a much bigger model for it, but
[00:21:26] it justifies the cost.
[00:21:27] There's been a lot of investment this
[00:21:29] year
[00:21:30] uh at the
[00:21:31] 7B in particular, but 7B, 13B, 34B
[00:21:35] sizes. Do you Do you think continued
[00:21:38] research at those scales is wasted?
[00:21:41] No, of course not.
[00:21:43] I mean, I think that in the kind of
[00:21:47] mid- like medium-term
[00:21:50] medium-term by a time scale anyway,
[00:21:52] there will be
[00:21:53] an ecosystem. There will be
[00:21:56] different uses for different model
[00:21:57] sizes. There will be plenty of people
[00:22:00] who are very excited for whom a the best
[00:22:02] 7B model is good enough. They'll be very
[00:22:05] happy with it. And then there'll be very
[00:22:08] plenty of very, very exciting and
[00:22:10] amazing applications for which it won't
[00:22:11] be enough.
[00:22:13] I think that's all. I mean, I think the
[00:22:15] big models will will be better than the
[00:22:17] small models.
[00:22:19] But not all applications will justify
[00:22:21] the cost of a small of a large model.
[00:22:23] What do you think the role of open
[00:22:25] source is in this ecosystem?
[00:22:27] Well, open source is complicated. I'll
[00:22:29] describe to you my mental picture.
[00:22:32] I think that in the near term, open
[00:22:34] source is just helping companies produce
[00:22:36] useful
[00:22:39] Like, let's see.
[00:22:41] Why would one want to have an open
[00:22:42] source but use an open source model
[00:22:44] instead of a closed source model that's
[00:22:46] hosted by some other company?
[00:22:48] I mean, I think it's very valid to want
[00:22:50] to
[00:22:52] be the final decider on
[00:22:56] the exact way in which you want your
[00:22:58] model to be used. And for you to make
[00:23:00] the decision of exactly how you want the
[00:23:03] model to be used and which use case you
[00:23:05] wish to support.
[00:23:06] And I think there's going to be a lot of
[00:23:07] demand for open source models and I
[00:23:09] think there will be quite a few
[00:23:10] companies that will use them. And I'd
[00:23:12] imagine that will be the case in the
[00:23:13] near term. I would say in the long run,
[00:23:17] I think the situation with open source
[00:23:19] models will become more complicated and
[00:23:20] I'm not sure what the right answer is
[00:23:22] there. Right now it's a little bit
[00:23:24] difficult to imagine so we need to put
[00:23:25] our
[00:23:27] future hat
[00:23:29] maybe futurist hat. It's not too hard to
[00:23:31] get into sci-fi into a sci-fi mode when
[00:23:33] you remember that we are talking to
[00:23:34] computers and they understand us. But so
[00:23:36] far these computers these models
[00:23:38] actually not very competent. They can't
[00:23:40] do tasks at all.
[00:23:43] I do think that there will come a day
[00:23:46] where
[00:23:47] the level of capability of models will
[00:23:50] be very high. Like in the end of the day
[00:23:51] intelligence is power.
[00:23:54] Right? Right now these models their main
[00:23:56] impact I would say at least popular
[00:23:58] impact is primarily around entertainment
[00:24:00] and like simple questions.
[00:24:03] So you talk to a model about this is so
[00:24:05] cool. You produce some images. You had a
[00:24:07] conversation maybe you had some
[00:24:08] questions you got answered.
[00:24:10] But it's very different from completing
[00:24:12] some large and complicated task like
[00:24:16] What about if you had a model which
[00:24:17] could autonomously start
[00:24:20] and
[00:24:21] build a large tech company.
[00:24:23] I think if these models were open source
[00:24:26] they would have a difficult to predict
[00:24:28] consequence. Like we are quite far from
[00:24:30] these models right now and by quite far
[00:24:31] I mean by by a time scale but still
[00:24:33] that.
[00:24:35] This is not what we're talking about but
[00:24:36] the day will come when you have models
[00:24:38] which can do science autonomously.
[00:24:41] Like build deliver on
[00:24:43] big science projects.
[00:24:45] And it becomes more complicated as to
[00:24:48] whether
[00:24:50] it is desirable that models of such
[00:24:51] power should be open sourced.
[00:24:54] I think the argument there is a lot less
[00:24:57] clear cut a lot less straightforward
[00:24:58] compared to the current level models,
[00:25:00] which are very useful and
[00:25:03] I think it's fantastic that the current
[00:25:04] level models have been built. So, like
[00:25:06] that is maybe maybe I answered a
[00:25:08] slightly bigger question, rather than
[00:25:10] what is the role of open-source models,
[00:25:11] if like what's the deal with open
[00:25:12] source. And the deal is
[00:25:15] up to a certain capability, it's great,
[00:25:17] but not difficult to imagine models
[00:25:19] sufficiently powerful
[00:25:21] which will be built, where it becomes a
[00:25:23] lot less obvious as to the
[00:25:25] benefits of their open source.
[00:25:27] Is there a signal for you that we've
[00:25:29] reached that level, or that we're
[00:25:31] approaching it? Like, what's the
[00:25:33] what's the boundary?
[00:25:34] So, I think figuring out this boundary
[00:25:37] very well
[00:25:38] is an urgent research pro- research
[00:25:40] project. I think one of the things that
[00:25:42] help is that
[00:25:46] the closed-source models are
[00:25:49] more capable than open-source models, so
[00:25:50] the closed-source models could be
[00:25:52] studied and so on.
[00:25:54] And so, you'd have some experience with
[00:25:55] the generation of closed-source model,
[00:25:57] and then then you know, like, oh, this
[00:25:59] model's capability is fine, there's no
[00:26:00] big deal there, and then in a in like
[00:26:02] couple years, the open-source models
[00:26:04] catch up. And maybe a day will come when
[00:26:06] we're going to say, well, like, these
[00:26:07] closed-source models, they're getting
[00:26:09] a little too a little too drastic, and
[00:26:11] then some other approach is needed.
[00:26:13] If we have our
[00:26:15] you know, future hat on, maybe let's
[00:26:17] like think about like a several year
[00:26:19] timeline. Um what are the limits you
[00:26:22] see, if any, in the in the near term in
[00:26:25] scaling? Is it like data, token
[00:26:28] scarcity, cost of compute, architectural
[00:26:31] issues?
[00:26:32] So, the most near-term limit to scaling
[00:26:35] is obviously data. This is well known,
[00:26:38] and some research is required to address
[00:26:41] it. Without going into the details, I'll
[00:26:43] just say that the data limit can be
[00:26:46] overcome,
[00:26:47] [clears throat]
[00:26:48] and progress will continue.
[00:26:50] One question I've heard people debate a
[00:26:52] little bit
[00:26:54] is the degree to which the transformer
[00:26:55] based models can be applied to sort of
[00:26:56] the full set of
[00:26:58] areas that you'd need for AGI.
[00:27:00] And if you look at the human brain for
[00:27:01] example, you do have reasonably
[00:27:03] specialized systems. They're all neural
[00:27:05] networks, but they have specialized
[00:27:06] systems for the visual cortex versus
[00:27:08] you know, um, areas of higher thought,
[00:27:11] areas for empathy, or other sort of
[00:27:13] aspects of everything from personality
[00:27:14] to processing.
[00:27:16] Do you think that the transformer
[00:27:17] architectures are the main thing that
[00:27:19] will just keep going and get us there,
[00:27:21] or do you think we'll need other
[00:27:21] architectures over time?
[00:27:23] So, I have two
[00:27:25] I understand precisely what you're
[00:27:26] saying, and I have two
[00:27:28] answers to this question. The first is
[00:27:31] that, in my opinion, the best way to
[00:27:33] think about the question of architecture
[00:27:35] is not in terms of a binary, is it
[00:27:38] enough,
[00:27:39] but how much
[00:27:42] effort, how much what will be the cost
[00:27:44] of using this particular architecture.
[00:27:47] Like at this point, I don't think anyone
[00:27:50] doubts that the transformer architecture
[00:27:52] can do amazing things, but maybe
[00:27:53] something else, maybe some modification
[00:27:55] could
[00:27:57] have some computer efficiency benefits.
[00:28:00] So, you will so better to think about it
[00:28:01] in terms of computer efficiency rather
[00:28:03] than in terms of
[00:28:04] can it get there at all. I think at this
[00:28:06] point, the answer is obviously yes.
[00:28:09] To the question about, well, what about
[00:28:11] the human brain and with its brain
[00:28:13] regions, I actually think
[00:28:15] that the situation there is
[00:28:19] subtle in the effective for the
[00:28:20] following reasons. So,
[00:28:22] what I believe you alluded to is the
[00:28:23] fact that the human brain has known
[00:28:25] regions. It has like it has a speech
[00:28:28] perception region, it has a speech
[00:28:29] production region, it has an image
[00:28:31] region, it has a face region, it has
[00:28:32] like all these regions.
[00:28:34] And it looks like it's specialized.
[00:28:36] But, you know what's interesting?
[00:28:38] Sometimes, there are cases where very
[00:28:41] young children have severe cases of
[00:28:43] epilepsy at the young age.
[00:28:45] And the only way they figured out how to
[00:28:47] treat
[00:28:48] such children is by removing half of the
[00:28:51] brain.
[00:28:53] Because it happened in such a young age,
[00:28:55] these
[00:28:56] children grow up to be pretty functional
[00:28:58] adults.
[00:28:59] And they have all the same brain
[00:29:01] regions, but they are somehow compressed
[00:29:02] onto one hemisphere.
[00:29:05] So, maybe some
[00:29:07] you know, information processing
[00:29:08] efficiency is lost. It's a very
[00:29:10] traumatic thing to experience, but
[00:29:12] somehow all these brain regions
[00:29:13] rearrange themselves. There is another
[00:29:14] experiment where that which was done
[00:29:17] maybe 30 or 40 years ago on ferrets. So,
[00:29:20] the ferret is a small animal.
[00:29:21] It's a pretty mean experiment. They took
[00:29:23] the optic nerve of the ferret, which
[00:29:25] comes from its eye,
[00:29:28] and attached it to its auditory cortex.
[00:29:31] So, now the inputs from the eye
[00:29:33] starts to map to the speech processing
[00:29:35] area of the brain. And then they
[00:29:36] recorded different neurons after it had
[00:29:39] a few days of learning to see, and they
[00:29:41] found neurons in the auditory cortex,
[00:29:43] which were very similar to the visual
[00:29:45] cortex. Or vice versa. It was either
[00:29:47] they mapped their eye to the ear to the
[00:29:49] auditory cortex or the ear to the visual
[00:29:51] cortex, but
[00:29:53] something like this has happened. These
[00:29:54] are fairly well-known ideas in AI that
[00:29:57] the cortex of humans and animals are
[00:29:59] extremely uniform.
[00:30:01] And so, that further supports the AI
[00:30:02] like you just need one unit big uniform
[00:30:04] architecture. That's all you need.
[00:30:06] Yeah, in general it seems like every
[00:30:07] biological system is reasonably lazy in
[00:30:09] terms of taking one system and then
[00:30:10] reproducing it and then reusing it in
[00:30:12] different ways, and that's true of
[00:30:13] everything from DNA encoding you know,
[00:30:15] there's 20 amino acids and protein
[00:30:16] sequences and so, everything is made out
[00:30:18] of the same 20 amino acids on through to
[00:30:20] uh to your point, sort of how you think
[00:30:22] about tissue architectures. So, it's
[00:30:24] remarkable that that carries over into
[00:30:25] the digital world as well, depending on
[00:30:27] the architecture you use.
[00:30:28] I mean, the way I see it is that this is
[00:30:30] an indication from a technological point
[00:30:33] of view, we are very much on the right
[00:30:34] track. Because you have all these
[00:30:36] interesting analogies between human
[00:30:38] intelligence and biological intelligence
[00:30:40] and artificial intelligence. We've got
[00:30:42] artificial neurons, biological neurons,
[00:30:44] unified
[00:30:45] brain architecture for biological
[00:30:47] intelligence, unified
[00:30:49] neural network architecture for
[00:30:50] artificial intelligence.
[00:30:51] At what point do you think we should
[00:30:52] start thinking about these systems as
[00:30:54] digital life?
[00:30:55] I can answer that question. I think that
[00:30:58] will happen when those systems become
[00:31:00] reliable
[00:31:02] in such a way as to be very autonomous.
[00:31:04] Right now, those systems are clearly not
[00:31:06] autonomous.
[00:31:07] They're inching there, but they're not.
[00:31:10] And that makes them a lot less useful,
[00:31:11] too, because you can't ask it, "Hey,
[00:31:13] like do my homework or do my taxes." Or
[00:31:15] you see what I mean? So, the usefulness
[00:31:17] is greatly limited.
[00:31:18] As the usefulness increases, they will
[00:31:20] indeed become more like artificial life,
[00:31:23] which is also makes it more
[00:31:25] I would argue
[00:31:26] um
[00:31:27] trepidations, right? Like if you imagine
[00:31:29] actual artificial life with brains that
[00:31:32] are smarter than humans, go, "Gosh,
[00:31:34] that's like
[00:31:36] that seems pretty monumental."
[00:31:37] Why is your uh definition based on
[00:31:39] autonomy? Cuz, you know,
[00:31:41] if you often look at the definition of
[00:31:43] biological life, it has to do with
[00:31:44] reproductive capability.
[00:31:46] Plus, I guess some form of autonomy,
[00:31:48] right? Like a virus isn't really
[00:31:49] necessarily considered alive much of the
[00:31:51] time, right? But a bacteria is.
[00:31:53] And you could imagine situations where
[00:31:55] you have um symbiotic relationships
[00:31:57] rather things where something can't
[00:31:58] really quite function autonomously, but
[00:32:00] it's still considered a life form. So,
[00:32:02] I'm a little bit curious about autonomy
[00:32:03] being the definition versus some of
[00:32:04] these other aspects.
[00:32:06] Well, I mean, definitions are chosen for
[00:32:08] our convenience, and it's a matter of
[00:32:10] debate.
[00:32:11] In my opinion, technology already has
[00:32:14] the reproduction, the reproductive
[00:32:15] function, right? And if you look at, for
[00:32:17] example, I don't know if you've seen
[00:32:18] those images of the evolution of cell
[00:32:21] phones and then smartphones over the
[00:32:22] past 25 years. You got this like what
[00:32:24] almost looks like an evolutionary tree
[00:32:25] or the evolution of cars over the past
[00:32:27] century. So, technology is already
[00:32:29] reproducing using the minds of people
[00:32:31] who copy ideas from previous generation
[00:32:33] of technology.
[00:32:34] So, I claim that the reproduction is
[00:32:36] already there. The autonomy piece, I
[00:32:39] claim, is not.
[00:32:40] And indeed, I also agree that there is
[00:32:42] no autonomous reproduction. But that
[00:32:43] would be like, can you imagine if you
[00:32:46] have like autonomous reproducing AIs? I
[00:32:48] actually think that that is a pretty
[00:32:50] dramatic and I would say quite a scary
[00:32:54] thing if you have an autonomously
[00:32:55] reproducing AI.
[00:32:56] If it's also very capable.
[00:32:58] Should we talk about uh super alignment?
[00:33:00] Yeah.
[00:33:01] Very much so.
[00:33:02] Can you um just sort of define it? And
[00:33:05] then, you know, we were talking about
[00:33:06] what the boundary is for we when we when
[00:33:09] you feel we need to begin to worry about
[00:33:12] uh these capabilities being in in open
[00:33:14] source. Like, what is super alignment
[00:33:16] and like why invest in it now?
[00:33:19] The answer to your question
[00:33:20] really
[00:33:22] depends to where you think AI is headed.
[00:33:26] If you just try to imagine looking to
[00:33:28] the future,
[00:33:29] which is of course a very difficult
[00:33:31] thing to do, but let's make let's let's
[00:33:33] try to do it anyway.
[00:33:35] Where do we think things will be in 5
[00:33:37] years or in 10 years?
[00:33:39] I mean, progress has been really
[00:33:40] stunning over the past few years. Maybe
[00:33:43] it will be a little bit slower,
[00:33:45] but still, if you if you extrapolate
[00:33:46] this kind of progress, you'll be in a
[00:33:48] very, very different place
[00:33:51] in 5 years, let alone 10 years.
[00:33:54] It doesn't seem implausible.
[00:33:56] It doesn't seem at all implausible that
[00:33:58] we will have computers,
[00:34:01] data centers that are much smarter than
[00:34:04] people. And by smarter, I don't mean
[00:34:06] just have more memory or have more
[00:34:07] knowledge, but also have mean have
[00:34:10] deeper insight into
[00:34:12] the same subjects that we people are
[00:34:14] studying and looking into. It means
[00:34:17] learn even faster than people.
[00:34:21] Like, what could such AIs do?
[00:34:23] I don't know. Certainly, if such an AI
[00:34:26] were the basis of some artificial life,
[00:34:28] it would be
[00:34:29] Well, how do you even think about it? If
[00:34:31] you have some very powerful data center
[00:34:33] that's also alive
[00:34:35] in a sense.
[00:34:36] That's what you're talking about. And
[00:34:38] when I imagine this world, I
[00:34:39] my reaction is gosh, this is very
[00:34:41] unpredictable what's going to happen.
[00:34:43] Very unpredictable.
[00:34:44] But the bare minimum but there is a bare
[00:34:46] minimum which we can articulate.
[00:34:49] That
[00:34:51] if such
[00:34:52] super if such very very intelligent
[00:34:54] super intelligent data centers are built
[00:34:57] being built at all,
[00:34:58] we want those data centers to hold warm
[00:35:01] and positive feelings towards people,
[00:35:04] towards humanity.
[00:35:06] Because those this is going to be
[00:35:08] non-human life
[00:35:10] in a sense. Potentially, it could be
[00:35:12] potentially be that.
[00:35:14] And so I would want that any instance of
[00:35:17] such
[00:35:19] superintelligence to have warm feelings
[00:35:21] towards humanity. And so this is what we
[00:35:22] are doing with
[00:35:24] the super alignment project. We are
[00:35:25] saying, "Hey, if you just allow yourself
[00:35:28] if you just accept the
[00:35:30] progress that we've seen, maybe it will
[00:35:32] be slower but it will continue.
[00:35:35] If you allow yourself that,
[00:35:39] then can you start can start doing
[00:35:40] productive work today
[00:35:43] to build the science so that we will
[00:35:46] be able to handle
[00:35:49] the problem of controlling such future
[00:35:52] superintelligence, of imprinting onto
[00:35:55] them a strong desire to be nice and
[00:35:59] kind to people. Because those data
[00:36:01] centers, right? They'll be
[00:36:03] they'll be really quite powerful.
[00:36:05] You know, they'll probably be many of
[00:36:06] them. They will be the world will be
[00:36:08] very complicated but somehow
[00:36:11] to the extent that they are autonomous,
[00:36:13] to the extent that they are agents, to
[00:36:15] the extent they are beings, I want them
[00:36:17] to be
[00:36:19] to be prosocial, prohuman social.
[00:36:22] That's the goal.
[00:36:23] What do you think is the likelihood
[00:36:25] of that goal? I mean, some of it it
[00:36:28] feels like
[00:36:29] a outcome you can hopefully affect,
[00:36:32] right? But,
[00:36:34] uh are we are we likely to have
[00:36:35] prosocial AIs that we are friends with
[00:36:38] individually or
[00:36:40] you know, as a species?
[00:36:41] Well,
[00:36:43] I mean, friends bees, I think that's
[00:36:45] that part is not necessary.
[00:36:47] The the the the friendship piece, I
[00:36:49] think it's optional, but I do think that
[00:36:50] we want to have a very prosocial AI.
[00:36:53] I think it's I think it's possible. I
[00:36:55] don't think it's guaranteed, but I think
[00:36:56] it's possible. I think it's going to be
[00:36:58] possible, and the possibility of that
[00:37:00] will increase in so far as more and more
[00:37:03] people allow themselves to look into the
[00:37:06] future, into the 5-to-10-year future.
[00:37:09] And just ask yourself, what
[00:37:13] what do you expect AI to be able to do
[00:37:15] then? How capable do you expect it to be
[00:37:17] then?
[00:37:19] And I think that with each passing year,
[00:37:22] if indeed AI continues to improve, and
[00:37:26] as people get to experience Excuse me,
[00:37:29] but right now we are talking, making
[00:37:30] arguments.
[00:37:31] But if you actually get to experience,
[00:37:33] "Oh gosh, the AI from last year, which
[00:37:35] was really helpful,
[00:37:37] this year it's like puts the previous
[00:37:39] one to shame."
[00:37:40] And you go, "Okay."
[00:37:42] And then 1 year later, and 1 year it's
[00:37:43] starting to do science. The AI software
[00:37:46] engineer is starting to get really quite
[00:37:47] good. Let's say.
[00:37:50] I think that will create a lot more
[00:37:51] desire in people
[00:37:54] for
[00:37:56] what you just described, for the future
[00:37:59] superintelligence to indeed be very
[00:38:00] prosocial.
[00:38:02] You know, I think there's going to be a
[00:38:02] lot of disagreements, going to be lots
[00:38:04] of political questions, but I think that
[00:38:06] as people see AI actually getting
[00:38:09] better, as people experience it,
[00:38:12] the desire for
[00:38:14] the prosocial
[00:38:15] superintelligence,
[00:38:17] the humanity-loving superintelligence,
[00:38:19] you know, as much as this is as as much
[00:38:21] as it can be done, will increase. And on
[00:38:23] the scientific problem,
[00:38:25] you know, I think right now it's still
[00:38:27] being an area where not that many people
[00:38:28] were working on.
[00:38:30] Our AIs are getting powerful enough
[00:38:32] where you can really start studying it
[00:38:34] productively. We'll have some very
[00:38:35] exciting research to to share soon.
[00:38:40] But I would say that's the
[00:38:41] big picture situation here. Just really
[00:38:43] it really boils down to
[00:38:45] look at what you've experienced with AI
[00:38:47] up until now. Ask yourself,
[00:38:50] like is it slowing down?
[00:38:52] Will it slow down next year? Look, we
[00:38:54] will see and we'll experience it again
[00:38:56] and again.
[00:38:57] And I think it will keep keep and what
[00:38:58] needs to be done will keep becoming
[00:38:59] clear.
[00:39:00] Do you think we're just on an
[00:39:01] accelerated path because I think
[00:39:03] fundamentally if you look at certain
[00:39:04] technology waves,
[00:39:06] they tend to inflect and then accelerate
[00:39:08] versus decelerate.
[00:39:10] And so it really feels like we're in an
[00:39:11] acceleration phase right now versus the
[00:39:13] deceleration phase.
[00:39:15] Yeah. I mean, we are right now it is
[00:39:17] indeed the case that we are in an
[00:39:19] acceleration phase. You know, it's hard
[00:39:21] to say.
[00:39:23] You know, multiple forces will come into
[00:39:26] play. Some forces are accelerating
[00:39:28] forces and some forces are decelerating.
[00:39:30] So for example, the cost and scale are a
[00:39:33] decelerating force.
[00:39:35] But the fact that our data is finite is
[00:39:38] a decelerating force to some degree to
[00:39:40] some degree at least. I don't want to
[00:39:41] overstate.
[00:39:41] kind of a within an asymptote, right?
[00:39:43] Like at some point you hit a one it's
[00:39:45] the standard S curve, right? Or
[00:39:47] sigmoidal.
[00:39:47] Well, we we with the data in particular,
[00:39:50] I just think it won't be it just won't
[00:39:51] be an issue because we'll figure out
[00:39:53] some something else.
[00:39:54] [sighs]
[00:39:55] But then you might argue that the size
[00:39:57] of the engineering project is an
[00:39:58] accelerating force, just the complexity
[00:40:00] of management. On the other hand, the
[00:40:02] amount of investment is an accelerating
[00:40:04] force. The amount of interest from
[00:40:05] people, from engineers, scientists is an
[00:40:07] accelerating force.
[00:40:09] And I think there is one other
[00:40:09] accelerating force.
[00:40:11] And that is the fact that biological
[00:40:14] evolution has been able to figure it out
[00:40:16] and the fact that up until now
[00:40:19] progress in AI has had up until this
[00:40:22] point this weird property that it's kind
[00:40:25] of been
[00:40:27] you know, it's been very hard to execute
[00:40:28] on, but in some sense it's also been
[00:40:31] more straightforward than one would have
[00:40:33] expected perhaps.
[00:40:36] Like in some sense
[00:40:38] I don't know much physics, but my
[00:40:40] understanding is that if you want to
[00:40:42] make progress in quantum physics or
[00:40:44] something, you need to be really
[00:40:46] intelligent and
[00:40:48] spend many years
[00:40:50] in grad school studying how these things
[00:40:52] work. Whereas with AI, you have people
[00:40:54] come in, get up to speed quickly, start
[00:40:56] making contributions quickly. It has the
[00:40:57] flavor is somehow different. Somehow
[00:40:59] that it's very
[00:41:01] there is some kind of there's a lot of
[00:41:02] give
[00:41:04] to this particular area of research. And
[00:41:05] I think this is also an accelerating
[00:41:06] force. How will it all play out remains
[00:41:09] to be seen. Like it may be that somehow
[00:41:12] the scale required of engineering
[00:41:13] complexity will start to make it so that
[00:41:15] the rate of progress will start to slow
[00:41:17] down. It will still continue, but maybe
[00:41:19] not as quick as we had before. Or maybe
[00:41:21] the forces which are coming together to
[00:41:23] push it will be such that it will be as
[00:41:25] fast for maybe a few more years before
[00:41:27] it will start to slow down. If at all,
[00:41:30] that's that would be my articulation
[00:41:32] here.
[00:41:33] Ilya, this has been a great
[00:41:34] conversation. [music]
[00:41:35] Uh thanks for joining us.
[00:41:36] Thank you so much for the conversation.
[00:41:37] I really enjoyed it.
[00:41:39] Find us on Twitter at No Priors Pod.
[00:41:42] [music]
[00:41:42] Subscribe to our YouTube channel if you
[00:41:43] want to see our faces. Follow the show
[00:41:45] on Apple Podcasts, Spotify, or wherever
[00:41:48] you listen. That way you get a new
[00:41:49] episode [music] every week. And sign up
[00:41:51] for emails or find transcripts for every
[00:41:53] episode at no-priors.com.
