# Dwarkesh Patel: AI Lab Leaders Debate Recursive Self-Improvement (Dario Amodei)
- **YouTube URL:** https://www.youtube.com/watch?v=PrSf7IOYu-I
- **Lines:** 3129

---

[00:00:02] Today I'm chatting with three of my AI
[00:00:02] researcher friends from whom I learn a
[00:00:04] lot every time we talk and who also
[00:00:06] happen to be at somewhat openish uh labs
[00:00:09] and companies so you guys can actually
[00:00:11] um say things on the record. I'm joined
[00:00:13] by Baron Militch who is the CTO of Zyra
[00:00:14] which is developing open source models.
[00:00:16] John Schulman who is the chief scientist
[00:00:18] at thinking machines previously the
[00:00:20] co-founder of OpenAI led the RLF work
[00:00:22] that led to CHPT and Charlie O'Neal who
[00:00:26] is head of model training at base 10.
[00:00:29] The first question I have, if we're in
[00:00:31] 2036, it's been 10 years, and we don't
[00:00:33] have like crazy billions of crazy super
[00:00:35] intelligences that are running around
[00:00:37] that like radically transform the world,
[00:00:39] what is the most likely reason that that
[00:00:42] doesn't end up being the case other than
[00:00:44] sort of exogenous political shocks or
[00:00:46] like there's a war or they ban AI or
[00:00:48] something, but what is the most likely
[00:00:50] technical reason that we don't like 2036
[00:00:53] isn't like a crazy alien super
[00:00:54] intelligence world? I mean like my
[00:00:57] reason would just be like it's got to be
[00:00:58] the sort of like there's been a classic
[00:01:01] thing almost like Marvik's paradox right
[00:01:03] where like we see like you know we think
[00:01:05] of the AI being like if it can do this
[00:01:06] it's going to be amazing right like if
[00:01:07] it can solve these hard math problems if
[00:01:09] it can win a chess blah blah and then it
[00:01:10] solves these things and then it's like
[00:01:12] not that impactful obviously it's
[00:01:13] somewhat impactful but like not
[00:01:15] everything it's like if somehow that
[00:01:16] continues and like there's never like
[00:01:18] the true like spark of generalization
[00:01:20] that occurs I think that could lead to
[00:01:22] like the AI just being like extremely
[00:01:24] good at kind of everything that people
[00:01:25] like put into a benchmark, put into an
[00:01:27] environment, but like there are still
[00:01:28] some persistent like sim to real which
[00:01:30] is somehow blocking everything. I think
[00:01:32] this is kind of unlikely. I think we do
[00:01:34] actually see this kind of generalization
[00:01:35] even from RL in practice already. But
[00:01:37] like if it is just like ridiculously
[00:01:39] hard to like generalize metalarning plus
[00:01:41] like we don't solve continuous learning,
[00:01:42] it is just like super hard and
[00:01:43] impossible. Yeah,
[00:01:44] >> like this would be my like default
[00:01:46] scenario in that case.
[00:01:47] >> Yeah, I agree with that. Humans uh have
[00:01:50] a lot of advantages over models now and
[00:01:53] uh each time a new model comes out,
[00:01:56] it'll sort of uh it'll catch up in some
[00:01:59] of these areas. Um but uh like you end
[00:02:02] up getting bottlenecked by the places
[00:02:04] where the model is weaker and where it
[00:02:06] has uh worse judgment or um the models
[00:02:09] can't check themselves well enough.
[00:02:11] Yeah. So so there's this uh cycle that
[00:02:13] keeps repeating where people think uh
[00:02:15] where a new model comes out and people
[00:02:16] are blown away and they're like this is
[00:02:18] it. This is the this is AGI. but then uh
[00:02:21] they use it a bit and and then it starts
[00:02:22] to feel dumb after a month or so. So
[00:02:25] that cycle just might keep going and
[00:02:27] it's hard to predict how many times it's
[00:02:29] it's going to repeat. And uh like right
[00:02:31] now you don't get explosive growth um in
[00:02:34] capabilities because uh you still get
[00:02:37] bottlenecked enough when you're trying
[00:02:38] to do research and engineering that even
[00:02:40] if the model can write way more code
[00:02:42] than a person, it doesn't make you like
[00:02:44] a 100 times more productive. Uh but
[00:02:47] yeah, so maybe maybe they're just more
[00:02:49] of these cycles than we would than we
[00:02:51] would expect.
[00:02:52] >> For me, it's like a question of how far
[00:02:54] off like this global optimum of a
[00:02:57] learner you could have on a chip is like
[00:02:59] the transformer plus like RL basically
[00:03:02] like the current recipe. So like I think
[00:03:05] people imagine that even like once you
[00:03:07] have a a an agent which is better than
[00:03:10] all humans at AI research even if it's
[00:03:12] like.1% better than all humans then the
[00:03:15] fact that you can run like you know
[00:03:16] hundreds of thousands if not millions of
[00:03:17] these in parallel um you can run them
[00:03:19] much faster like chip's going to speed
[00:03:21] up that's going to outweigh every other
[00:03:22] like bottleneck and like you're
[00:03:24] eventually just going to like hit this
[00:03:25] like very fast takeoff with recursive
[00:03:26] self-improvement. I could imagine that
[00:03:28] if we continue along the trajectory that
[00:03:30] we're currently on with that paradigm
[00:03:32] where you know it's basically just like
[00:03:34] self attention RL scaling up RL
[00:03:36] environments the I guess like if you
[00:03:39] think about what happened with Mo's law
[00:03:41] right like we had this very like nice
[00:03:42] straight line and that held for a really
[00:03:44] really long time but there were so many
[00:03:46] like discrete like discontinuities and
[00:03:49] innovations that had to happen to keep
[00:03:50] that scaling law going and the same
[00:03:52] thing has kind of happened with LM like
[00:03:54] we had this pre-training like scaling
[00:03:55] law and then that was kind of like you
[00:03:57] know hitting the diminishing returns and
[00:03:59] then we came up with like RL and solved
[00:04:00] that and then we got this new like you
[00:04:02] know diminishing returns curve to hit
[00:04:04] that made it keep looking like a
[00:04:05] straight line going up and so like if it
[00:04:08] requires another one of those
[00:04:09] discontinuities to solve like I'm not
[00:04:11] sure that like the current method of
[00:04:13] like training LM with these RL
[00:04:15] environments even like RSI targeted RL
[00:04:17] environments would be able to discover
[00:04:19] that discontinuity and if not like we're
[00:04:22] probably going to hit this like asmtoic
[00:04:24] like curve where like
[00:04:25] >> sorry but do do you think discontinuity
[00:04:27] will be harder than anything that's come
[00:04:29] since 2012.
[00:04:31] >> If if we had the answer to that that
[00:04:32] that we'd kind of have the ability to
[00:04:34] implement it, but like maybe there's the
[00:04:36] distinguish we should distinguish
[00:04:38] between a discontinuity which adds to
[00:04:39] the current paradigm. Again, it's like
[00:04:40] cumulative like there's some thing
[00:04:42] beyond the RL that we have to discover
[00:04:43] and maybe they're capable of like you
[00:04:45] know connecting the dots in that
[00:04:47] straight line
[00:04:48] >> or like like again how far off the the
[00:04:50] global optimum are we? Do we have to go
[00:04:52] back and throw out like you know
[00:04:53] gradient descent and like neural nets in
[00:04:56] general? And I don't think like if you
[00:04:58] continue to scale up the current
[00:04:59] paradigm an LLM no matter how many LM
[00:05:01] you're running are capable of
[00:05:02] necessarily discovering that if it's too
[00:05:04] far away.
[00:05:05] >> Yeah. The only hope really is if deep
[00:05:08] learning just can't get us to an AI
[00:05:12] which is at least uh can dominate human
[00:05:16] research and human development including
[00:05:18] the human ability to come up with new
[00:05:19] paradigms and so forth or like I don't
[00:05:21] know maybe humans would also never have
[00:05:23] discovered the the next learning
[00:05:25] architecture but um to the extent humans
[00:05:27] could have discovered it eventually but
[00:05:29] it just seems like I don't know if if
[00:05:32] you just look at the progress that's
[00:05:33] happens in 2012 till now and you just
[00:05:36] continued that on. I mean, I know it's
[00:05:38] been powered by huge amounts of comput
[00:05:39] scaling and so forth, but um uh it would
[00:05:42] be weird if like it just didn't get to
[00:05:45] the point where it could like dominate
[00:05:46] humans, at least in R&D, especially over
[00:05:50] the next few years, there's going to be
[00:05:52] Ryan Greenbl was on the podcast recently
[00:05:54] and he made this point that you could
[00:05:55] imagine as AI get more and more capable
[00:05:57] and are capable of making progress on
[00:06:01] simulations which incentivize getting
[00:06:03] better at not only AI R&D, but generally
[00:06:05] at science. So this is a thing that all
[00:06:07] the labs are targeting, many startups
[00:06:08] are targeting or the another intuition
[00:06:10] pump is if you look at the ELO score of
[00:06:12] chess bots since the 80s, there's just
[00:06:14] like a very linear increase in ELO over
[00:06:17] time, but there's this huge
[00:06:18] discontinuity as they cross the human
[00:06:20] range of human experts always win
[00:06:23] against AIS to like human experts never
[00:06:25] win against AIS as this linear increase
[00:06:27] in happen. You could think I agree with
[00:06:29] your point that the so far AI
[00:06:31] capabilities have not been that big of a
[00:06:33] deal in terms of their end economic
[00:06:35] impact in the world. But that is because
[00:06:37] like they're slowly rising in ELO
[00:06:38] relative to humans.
[00:06:39] >> Yeah.
[00:06:40] >> Yeah. I mean I agree it would be very I
[00:06:41] mean the only way for this to not happen
[00:06:43] is if like as you say somehow asmto like
[00:06:46] just before basically cuz we're already
[00:06:47] pretty close in my opinion to like where
[00:06:49] we'll start crossing like the human elo
[00:06:50] score and so we'll need to asent before
[00:06:52] that and like that's the only way you
[00:06:54] know in the scenario you pose where like
[00:06:55] somehow we're sitting here in 2035 and
[00:06:57] like everything is normal for this to
[00:06:58] happen. I think I mean the only other
[00:07:00] way is like there's like some dramatic
[00:07:01] like regulation on AI. It's like this is
[00:07:03] kind of what I see as like the most
[00:07:04] likely way for this scenario to happen
[00:07:05] actually rather than the technical
[00:07:07] thing. Yeah, I I think there's different
[00:07:09] kinds of research. There's like research
[00:07:11] where it's like the auto research style
[00:07:12] where the objective is already specified
[00:07:14] very cleanly and you're optimizing that
[00:07:16] objective. And I think everyone is
[00:07:17] picturing like
[00:07:18] >> if we continue along this path of like,
[00:07:20] you know, making pre-training loss go
[00:07:21] down, making our environments, making
[00:07:23] water go up, that's going to lead to
[00:07:24] like improvement. But like, you know,
[00:07:26] maybe what Ryan is talking about is like
[00:07:27] this much more open-ended type of
[00:07:28] science which is required for like
[00:07:30] paradigm shifts where we can't specify
[00:07:32] the objective and the AIS are definitely
[00:07:33] not able to specify that objective
[00:07:35] either. like we have to be really really
[00:07:36] careful about how we specify objectives
[00:07:38] for any of these things.
[00:07:39] >> And maybe your point is that like the
[00:07:40] nature of the breakthroughs that have
[00:07:41] happened since 2012 is that we have
[00:07:44] found like in 2012 people weren't saying
[00:07:46] or I'm assuming I don't know you guys
[00:07:48] were there or at least John you were
[00:07:50] there but I was
[00:07:51] >> I was in primary school. [laughter]
[00:07:53] Um, actually, John, I'm curious for your
[00:07:55] like sort of uh wi wisdom of the ages of
[00:07:58] or wisdom of like being in the trenches
[00:08:00] way back when, but presumably a big
[00:08:02] breakthrough was realizing that next
[00:08:04] token prediction is the like you
[00:08:05] wouldn't have thought that nano nano GPT
[00:08:08] speedrun is the thing to be optimizing
[00:08:10] for in 2014. Um, but now that we have
[00:08:13] come to this new paradigm, that's you
[00:08:15] wouldn't think to do a speedrun on that
[00:08:16] and have you guys get really good at
[00:08:17] that. But maybe there's like a next
[00:08:20] inner loop to optimize that the AIS
[00:08:23] wouldn't anticipate. And there's an
[00:08:24] outer loop of like revenue or something
[00:08:25] that eventually should be strong. But
[00:08:28] it's a very slow outer loop.
[00:08:29] >> Yeah. In fact, I remember in the early
[00:08:32] OpenAI days uh having the int intuition
[00:08:35] that um actually just uh do like
[00:08:39] minimizing log loss wasn't going to get
[00:08:40] you to intelligence uh because uh
[00:08:44] >> like the important bits are accounting
[00:08:46] to for such a small fraction of the loss
[00:08:48] uh that like it was going to be
[00:08:50] overwhelmed by noise. So just training a
[00:08:53] a language model uh on next token
[00:08:56] prediction just wasn't going to learn
[00:08:58] the interesting things you wanted to
[00:08:59] learn. And uh we needed to craft better
[00:09:02] objectives that would put more emphasis
[00:09:04] on the important things. And uh like you
[00:09:07] can make all sorts of arguments for this
[00:09:08] and you could say um oh humans probably
[00:09:11] don't learn how to like uh we don't
[00:09:14] learn how to model everything in our
[00:09:16] environment. uh we can't uh most like
[00:09:19] people can't uh create a photorealistic
[00:09:22] uh reproduction of uh some kind of scene
[00:09:24] they've looked at. Uh so
[00:09:27] um there must be we must need a better
[00:09:30] objective. But then it turned out that
[00:09:31] it it just worked anyway.
[00:09:32] >> And as you were pointing out the inner
[00:09:34] loop even in current AI research of like
[00:09:37] post-training benchmarks or whatever
[00:09:39] doesn't necessarily translate into what
[00:09:40] users like.
[00:09:41] >> Oh yeah. I mean the whole field relies a
[00:09:44] lot on generalization and it's very hard
[00:09:45] to uh predict when when you're going to
[00:09:48] get generalization or when you're going
[00:09:50] to get some kind of out of distribution
[00:09:51] generalization. So we know that if you
[00:09:53] train on the task you care about you're
[00:09:54] going to do better.
[00:09:55] >> Yeah.
[00:09:56] >> Uh but like the most important advances
[00:09:58] are often uh the opp are are um types of
[00:10:03] generalization that we have no right to
[00:10:05] expect. So for example from uh just
[00:10:08] pre-training on this um very naive um
[00:10:12] next token prediction objective um to
[00:10:15] like various tasks of interest uh where
[00:10:18] uh some very uh that require
[00:10:20] understanding of the input in some deep
[00:10:23] way or learning some skill from
[00:10:25] pre-training that's like very uh rare
[00:10:27] and like not very like heavily
[00:10:31] represented. Um and then like also
[00:10:33] generalization from these verifiable
[00:10:35] tasks to um less verifiable ones. This
[00:10:38] is also a type of generalization that
[00:10:40] >> there's no reason a priori to expect it.
[00:10:43] >> Yeah. Yeah. So this is an interesting
[00:10:45] question because one intuition pump that
[00:10:47] you could have for why you would see um
[00:10:50] some sort of singularity
[00:10:52] very rapidly without even scaling up the
[00:10:54] inputs to AI progress that are not just
[00:10:56] AI labor is that before every single
[00:10:58] experiment you run that's you know like
[00:11:00] a seven figure experiment you spend an
[00:11:02] equivalent amount of compute on AI labor
[00:11:05] and so you just have automated versions
[00:11:07] of you guys spending a century uh
[00:11:10] thinking about like what is the optimal
[00:11:12] experiment to run um doing like small
[00:11:14] scale ablations developing literally
[00:11:17] like in a century's worth of theory. So
[00:11:20] going back even before like deep
[00:11:21] learning it in before you decide what
[00:11:24] experiment to run doing extremely
[00:11:25] optimal like setting up of the
[00:11:26] experiment. Then you do a century of
[00:11:28] thinking after the experiment is over
[00:11:29] where you're like analyzing what
[00:11:31] happened and what the next experiment to
[00:11:32] run is.
[00:11:33] >> Yeah. Well, I think if if you think hard
[00:11:35] enough, you probably could have um
[00:11:37] expected some of these things
[00:11:38] beforehand. Like uh like there is
[00:11:40] probably some very clever way to do a
[00:11:42] small scale experiment that'll let you
[00:11:44] build the theory that then will
[00:11:46] generalize to the large scale
[00:11:47] experiments. So I would expect that like
[00:11:49] we're nowhere near the ceiling of how
[00:11:51] well you can do research. And like I
[00:11:54] would imagine a future where um where AI
[00:11:57] is like um is doing a lot of uh like
[00:12:01] analysis and theory building um like
[00:12:05] spending a comparable amount of compute
[00:12:06] to the amount that you're spending on
[00:12:08] the experiments themselves uh doing
[00:12:10] various kinds of analysis and building a
[00:12:13] theory around what we've seen so far.
[00:12:15] >> I think there's like really concrete
[00:12:16] examples of this when the objective is
[00:12:18] well specified. So again like all
[00:12:20] thinking can do is like update your
[00:12:22] posterior based on like you know the
[00:12:23] bits that you've gotten since you formed
[00:12:25] your prior like you can't gain any new
[00:12:27] bits from like just thinking
[00:12:28] >> but when the objective is well specified
[00:12:30] and there is like this data sitting
[00:12:31] around like I imagine there will be this
[00:12:33] big speed up in the current paradigm
[00:12:34] we're in and like good example of this
[00:12:36] is like you know if you got an AI to
[00:12:37] think about like the cap plan scaling
[00:12:39] walls like an AI at this point would
[00:12:42] have noticed that like you know oh like
[00:12:44] they've just taken these intermediate
[00:12:45] checkpoints and didn't account for like
[00:12:46] the analing and so like this is wrong
[00:12:48] and that would have caught that like
[00:12:49] years earlier. We would have made like
[00:12:51] you know progress like like would have
[00:12:53] cut off a year or two of progress just
[00:12:54] from that like observation from an AI.
[00:12:56] Um and like again once the objective is
[00:12:58] well specified which is like lower
[00:13:00] pre-training loss or or whatever like
[00:13:02] there's many many good examples where if
[00:13:03] you just thought about it a bit more you
[00:13:05] would have been able to like cut down a
[00:13:06] significant on things that you've done.
[00:13:09] So like mu and like how learning rate
[00:13:10] scales with like model size and like
[00:13:12] realizing that model width is important
[00:13:14] in that as well. Um, like I feel like
[00:13:16] you can you can really back out a lot of
[00:13:18] these things and cut off like a lot of
[00:13:19] low hanging fruit. So I would imagine
[00:13:21] like a 10 times speed up if our thing is
[00:13:23] just like maximize the objective we're
[00:13:24] currently on.
[00:13:25] >> But I don't see that how that
[00:13:26] generalizes at all to you know come up
[00:13:28] with the right objective in the first
[00:13:29] place. Like just thinking doesn't
[00:13:31] necessarily buy you the right objective
[00:13:32] in the first place. I mean, yeah, I
[00:13:34] think this is really the key question to
[00:13:35] like any kind of like very rapid RSIs
[00:13:38] like from current AI is like how well
[00:13:40] can AI generalize to like learning their
[00:13:42] own objectives because to have any kind
[00:13:43] of like self-propelling automated loop,
[00:13:45] you need the AI to like propose
[00:13:46] objectives, optimize them, figure that
[00:13:48] out, propose a new objective and like
[00:13:49] have this like not go off the rails at
[00:13:51] like any point for like a long long
[00:13:52] time. Coming back to MVX products, there
[00:13:54] might be like a case of MX products
[00:13:56] where like we think this kind of like
[00:13:58] autonomy and sort of like being like
[00:14:00] self- encapsulated so we can, you know,
[00:14:01] think of what we should do ourselves and
[00:14:02] then go do it and like have this loop is
[00:14:04] like super easy because we always do
[00:14:05] this and like obviously evolution needs
[00:14:07] to create creatures that can like
[00:14:08] survive on by themselves like long
[00:14:09] periods of time and like this just might
[00:14:11] be something that for some reason is
[00:14:12] like really hard for the AI in the same
[00:14:14] way that like locomotion stuff is really
[00:14:16] hard. Like math is super easy despite
[00:14:17] being super hard for us.
[00:14:18] >> I don't know. Doesn't the time horizon
[00:14:20] increasing suggest that that's
[00:14:21] >> you would Yeah, exactly. I mean this is
[00:14:22] another possibility which like but I
[00:14:24] agree like there's no obviously evidence
[00:14:25] for this like in fact
[00:14:27] >> the fact that you know agent is now like
[00:14:29] super persistent and it's quite easy to
[00:14:30] do this is kind of evidence against this
[00:14:32] >> but like this would be you know
[00:14:34] potentially like one of the reasons why
[00:14:35] like we just don't get this like
[00:14:36] immediate takeoff is like if this is
[00:14:38] hard
[00:14:39] >> if if you look back from 2012 till now
[00:14:42] or maybe from when you started doing
[00:14:45] your research till now what part of
[00:14:48] of all the innovations that have
[00:14:51] happened since that time, including
[00:14:54] purely engineering ones, including
[00:14:55] purely conceptual ones. What seems like
[00:14:58] the thing that is the thing that would
[00:15:00] be the last things humans would have to
[00:15:02] do before AI is totally automate AI R&D?
[00:15:05] >> Probably just like iteratively asking
[00:15:06] the right questions like if you can get
[00:15:08] the AI to like do any experiment, but
[00:15:10] like you need to decide what experiments
[00:15:11] to do. And like right now, I think AI
[00:15:13] are not very good at this compared
[00:15:15] compared to coding the experiments at
[00:15:16] all.
[00:15:16] >> Yeah. Yeah, like whenever we talk about
[00:15:18] research, they proposed like a bunch of
[00:15:19] like miscellaneous things which are like
[00:15:20] very very tiny steps
[00:15:22] >> or even going from like you know deep
[00:15:23] mind's approach of like we're going to
[00:15:24] solve intelligence by learning to play
[00:15:26] games at a superhuman level. that's
[00:15:28] going to be the approach to like one
[00:15:30] random researcher like Radford being
[00:15:32] >> like I'm going to try and just predict
[00:15:33] the next token off a very wide swath of
[00:15:36] data like
[00:15:38] >> and then even once Radford had
[00:15:39] discovered that right like it took a
[00:15:40] while before people decided to scale it
[00:15:42] up because we had to come up with the
[00:15:43] idea of scaling walls and the fact that
[00:15:44] like you could very reliably predict
[00:15:46] these things.
[00:15:46] >> Yeah. Yeah. I would say that the last um
[00:15:50] job for humans uh or the the the role
[00:15:53] for humans that'll last the longest is
[00:15:55] like defining the objective. uh and like
[00:15:59] deciding what we actually want. Um so
[00:16:02] like in that vein uh something like uh
[00:16:07] deciding what um how like the AI the
[00:16:09] assistant should behave or what what it
[00:16:11] means to be helpful or what what's like
[00:16:13] the objective when we're doing our all
[00:16:15] from human feedback
[00:16:16] >> is one such thing and then like then
[00:16:19] later like defining like constitutions
[00:16:21] and model specs
[00:16:23] >> is another one and I think uh even if
[00:16:26] the AIs can do all the technical work uh
[00:16:28] we'll have to still do a lot of that and
[00:16:29] decide what we actually want.
[00:16:31] >> Yeah, alignment is the final job.
[00:16:33] >> Yeah, alignment is sort of the answer,
[00:16:35] but it's also um alignment itself can be
[00:16:37] kind of decomposed into um into like uh
[00:16:41] specification of the objective or
[00:16:43] figuring out what the right objective
[00:16:44] should be. And then uh like actually uh
[00:16:48] like achieving or optimizing the
[00:16:50] objective you've defined and uh I think
[00:16:52] the first one is not going to go any
[00:16:55] away anytime soon. And like if I think
[00:16:58] about like a post-training team and uh
[00:17:01] why you need a lot of people um to be on
[00:17:04] the team, it's it's it's just because
[00:17:06] there are a lot of different uh like
[00:17:07] areas where you have to figure out like
[00:17:10] how the model should behave and uh like
[00:17:13] there's no way of um like there's no way
[00:17:16] of uh it would be very hard to automate
[00:17:18] the whole thing just because someone has
[00:17:20] to think about how how should the model
[00:17:22] behave in this area. Jane Street started
[00:17:25] using antithesis to test our software in
[00:17:27] early 2025 and they were so impressed by
[00:17:29] the product that they decided to invest
[00:17:31] in the company. I recently caught up
[00:17:33] with Ron Minsky who co-leads Jane
[00:17:35] Street's tech group to ask about [music]
[00:17:36] how antithesis actually plugs in. The
[00:17:39] thing that I think is most impressive
[00:17:40] about antithesis is we started using it
[00:17:42] in a team that was building high
[00:17:44] assurance software and being really
[00:17:46] careful and nonetheless it was able to
[00:17:48] shake out bugs that were otherwise going
[00:17:50] to be really hard to find. And that's
[00:17:52] important both because it helps make
[00:17:54] those systems more reliable, but also
[00:17:56] because it helps the teams that build it
[00:17:58] to just move faster.
[00:17:59] >> This matters more and more as code
[00:18:01] production is increasingly automated.
[00:18:02] [music]
[00:18:02] >> I think in general as we've been using
[00:18:04] agents more and more, the key problem
[00:18:06] that you run into is the verification
[00:18:08] bottleneck. Just the the time it takes
[00:18:10] from people to look at code and figure
[00:18:12] out is that actually something you want
[00:18:13] to accept in your production software.
[00:18:16] And tools that make testing better are
[00:18:18] just incredibly helpful there. you just
[00:18:20] ease the verification bottleneck and
[00:18:21] make it possible for you to get more
[00:18:23] stuff done and move faster because you
[00:18:25] can have more confidence [music] that
[00:18:26] the code generated by the agent is
[00:18:28] actually not introducing new problems.
[00:18:30] To see how antithesis fits into your
[00:18:32] development process, go to
[00:18:34] antithesis.com/bash.
[00:18:42] What is the story for why there there
[00:18:42] isn't huge consolidation in model
[00:18:44] providers? There's just so many things
[00:18:45] that point to centralization here. Is
[00:18:48] there is it yeah if you if we step back
[00:18:50] over the course of years is there
[00:18:52] something that is gonna prevent that?
[00:18:54] >> Yeah I think um distillation is the main
[00:18:56] thing that uh fights against the
[00:18:58] centralizing force uh because basically
[00:19:00] anything that can be learned uh through
[00:19:02] RL can be distilled very easily because
[00:19:05] uh um like it's a small number of bits
[00:19:09] uh it's something that you can learn
[00:19:10] from a small amount of data. So if you
[00:19:12] can coll if you can get uh trajectories
[00:19:14] from the model that uh show a behavior
[00:19:17] you can easily distill it. So I think um
[00:19:20] I think distillation is one of the uh
[00:19:23] things that fight central
[00:19:25] centralization.
[00:19:26] uh there's also um I mean there is a
[00:19:30] possibility that there'll be company
[00:19:32] specific u models that it'll it'll be
[00:19:34] possible to learn from deployment um and
[00:19:37] uh h have a company continually
[00:19:39] improving its its own model
[00:19:41] >> uh and um such a system could be
[00:19:44] provided by the uh current oligopoly of
[00:19:46] model providers or some other uh
[00:19:49] currently smaller company uh but I think
[00:19:51] that'll that'll change the game a bit
[00:19:53] >> yeah and I also want to point out that
[00:19:55] like continual learning and So it
[00:19:56] doesn't stop distillation, right? Like
[00:19:58] even if your model is improving every
[00:19:59] day, like you people could be distilling
[00:20:00] it every day. So it's like the loops
[00:20:02] could just operate at the same pace,
[00:20:03] >> right? That makes sense. Okay, so
[00:20:05] copying model behavior
[00:20:09] um you I I guess you need to know
[00:20:11] yourself what the right distribution to
[00:20:13] prompt is in order to get like the
[00:20:15] relevant model behavior.
[00:20:16] >> Oh yeah, for um just distilling uh with
[00:20:19] supervised learning um the prompt
[00:20:21] distribution is extremely important. So
[00:20:23] it's uh very non trivial to distill a
[00:20:26] model even if you have full access to it
[00:20:27] and have the cot the chain of thought
[00:20:30] and everything. Uh yeah it's it's
[00:20:32] non-trivial to distill all of the all of
[00:20:35] the useful capabilities from it. Um
[00:20:37] because you need to prompt the model
[00:20:39] with something and you need to prompt it
[00:20:41] with uh like realistic prompts. Uh you
[00:20:45] you need to have a really wide
[00:20:47] distribution of realistic prompts. So
[00:20:50] yeah, one thing that's been coming out
[00:20:51] recently is um some of the some of the
[00:20:55] Chinese companies are probably using
[00:20:57] these uh router services which are
[00:20:59] designed to allow people in China to use
[00:21:01] uh the US frontier models which would
[00:21:03] otherwise be blocked in China. Uh but
[00:21:05] there are all these uh router or proxy
[00:21:07] services that allow people in China to
[00:21:09] use these models mostly for coding and
[00:21:12] uh and these router services are
[00:21:14] collecting and selling some of the data.
[00:21:16] So I think this is uh like a very useful
[00:21:19] data set for uh distillation because it
[00:21:23] gives you the perfect prompt
[00:21:24] distribution.
[00:21:25] >> Yeah, I think this is one of those
[00:21:26] things where AI help a lot here. Like if
[00:21:28] you actually look at like you know the
[00:21:29] frontier pipelines of say like the
[00:21:31] Chinese models that they actually put in
[00:21:32] their papers, it's a lot of like humans
[00:21:34] or like they get seed prompts from
[00:21:36] somewhere which is some combination of
[00:21:37] humans this kind of data and then they
[00:21:38] like synthesize a vast coverage from
[00:21:40] those seed prompts using their existing
[00:21:42] models or like the other frontier
[00:21:43] models. And so it's like you can
[00:21:44] automate like an awful lot of this like
[00:21:46] prompt distribution gathering and like
[00:21:47] environment creation. It's just like
[00:21:49] humans need to provide like increasingly
[00:21:50] few amounts of bits. It's like the
[00:21:52] models get better,
[00:21:52] >> right? But it seems it still seems
[00:21:54] you're bottlenecked by um like having a
[00:21:58] service which has users or users are
[00:22:00] going through. So like
[00:22:01] >> not necessarily I mean like yeah that's
[00:22:02] obviously very helpful but like
[00:22:03] theoretically you can just think about
[00:22:05] like what users want or like
[00:22:07] >> like the whole point is that we don't
[00:22:09] the user says make me an application
[00:22:11] like this. Oh that didn't I actually
[00:22:12] want you to make this new feature but
[00:22:14] actually let's step back and do this
[00:22:16] other thing and capturing that whole
[00:22:17] trace is the or to the extent you could
[00:22:20] have done that anyways then you just
[00:22:21] have like RSI any
[00:22:24] >> yeah I mean like ultimately like if you
[00:22:25] have this like fully automated loop that
[00:22:27] is basically RSI right like the AI is
[00:22:28] deciding the data it's deciding the
[00:22:30] training that that is the loop but yeah
[00:22:31] I mean like it depends how much human
[00:22:33] information you need like at some point
[00:22:34] if you're just like I want traces that
[00:22:36] look like this you prompt that to the
[00:22:37] model the model will be able to like
[00:22:38] come up with like a pretty good
[00:22:39] approximation
[00:22:40] >> but what if you want to do like make me
[00:22:41] a really good politician in the like
[00:22:43] anticipate denovo like how how would
[00:22:46] discussion in like the Senate halls go
[00:22:48] or something. I just feel like there's
[00:22:49] going to be a lot of things.
[00:22:50] >> Ironically, this is actually I think
[00:22:51] easier for the distillers than the
[00:22:53] frontier labs, right? Because the
[00:22:54] distillers just like I want a good
[00:22:56] politician, they go to the like frontier
[00:22:57] model. The frontier model already knows
[00:22:58] how to be a good politician. So it just
[00:22:59] like generates those traces. Whereas
[00:23:01] like if you actually want to build the
[00:23:02] first model that does this, you have to
[00:23:04] like actually somehow like get data on
[00:23:05] like what politicians do every day and
[00:23:07] like build that. So it's actually much
[00:23:09] easier to like say like I want something
[00:23:10] like this and then like get like the AI
[00:23:12] to produce like a billion variations to
[00:23:13] actually create the thing to begin with.
[00:23:15] >> I think you can actually make a really
[00:23:17] concrete prediction based off like this
[00:23:19] observation that the Chinese labs have
[00:23:21] this router data. Like I think the thing
[00:23:23] that that just stated this originally
[00:23:24] was I was saying isn't it weird how set
[00:23:27] 5 and opus 5 are like like almost
[00:23:30] objectively worse models than like GLM
[00:23:32] 5.3 Kim K3 even though they've had
[00:23:35] access to like not only distillation but
[00:23:37] logic distillation from like mythos and
[00:23:39] so the counter here was that like okay
[00:23:40] the prompt distribution really really
[00:23:41] matters um like you need to see what
[00:23:44] users are doing so you can distill like
[00:23:45] kind of these behaviors and things in I
[00:23:47] think the prediction from this is that
[00:23:49] the frontier labs don't necessarily have
[00:23:51] much of an advantage if at all in Ral
[00:23:54] environments now because yes like user
[00:23:56] distribution matters for like general
[00:23:58] like behavior and and so on but like the
[00:24:00] best measure of a capability is the very
[00:24:02] very hard RL environments you've made at
[00:24:04] the frontier and so if you have access
[00:24:06] to those RL environments as anthropic
[00:24:08] and you have access to logic
[00:24:09] distillation and you've still made a
[00:24:11] worse model then maybe like
[00:24:13] >> then real world deployment matters more
[00:24:14] than the environment that's really
[00:24:16] interesting so but they they had to
[00:24:18] incentivize those capabilities in the
[00:24:20] first face in um in Fable or the
[00:24:23] Frontier model.
[00:24:24] >> And so it's weird that they can't
[00:24:25] incentivize them again
[00:24:27] >> uh or with a smaller model or something.
[00:24:30] >> Maybe like maybe we're just in this
[00:24:31] weird like uncanny valley where you know
[00:24:34] like
[00:24:34] >> actually trying to copy that frontier
[00:24:36] model too much like the the student
[00:24:37] teacher gap or whatever it is is just
[00:24:39] like too large. And like I think people
[00:24:41] people made this point with Opus is it's
[00:24:42] like the difference between Opus 4.6 six
[00:24:44] and Opus 5 is that Opus 5 really feels
[00:24:47] like it's got this like AI as a judge
[00:24:49] checking every possible thing it's done
[00:24:50] and it's like that's why it uses so many
[00:24:52] tokens. It like tries to think about all
[00:24:53] these things but it doesn't necessarily
[00:24:55] have the big model smell of fable to
[00:24:57] know when to like stop doing that or
[00:24:58] like when's the good path to go down or
[00:25:00] whatever.
[00:25:00] >> The reach exceeds the grass.
[00:25:02] >> Yeah.
[00:25:02] >> Yeah. I would offer a slightly different
[00:25:04] uh hypothesis. So I would say there are
[00:25:07] a couple of different axes for uh the
[00:25:10] environments you can create and uh like
[00:25:12] one of them is difficulty and the other
[00:25:14] is uh realism.
[00:25:15] >> It's sort of easy to create or it's
[00:25:17] comparatively easy to create a lot of
[00:25:19] difficult environments uh like um
[00:25:23] >> that are just um like involve uh like
[00:25:26] doing a much more complicated task or
[00:25:28] doing something that requires a lot more
[00:25:30] cleverness. And uh you could you could
[00:25:32] say this is like the benchmaxing
[00:25:34] distribution because a lot of the most
[00:25:35] prominent benchmarks just involve doing
[00:25:37] some very hard puzzle-like task uh
[00:25:40] that's easy to verify. And then there's
[00:25:42] sort of uh like the realism axis where
[00:25:44] you want the model to be good in the
[00:25:46] realistic coding agent setting where
[00:25:48] there's like multiple back and forth. is
[00:25:49] the human and there's like multiple
[00:25:51] objectives and uh like I'd say um like
[00:25:56] the people like the labs who are
[00:25:59] crafting the model behavior for the
[00:26:01] first time need to push in both
[00:26:02] directions and to get good model
[00:26:04] behavior you need to really push on the
[00:26:06] realism axis and have like rubrics or
[00:26:09] some kind of human feedback that's
[00:26:11] informing uh the reward function you use
[00:26:13] there. Um but uh I think when if you try
[00:26:17] to do distillation naively, you end up
[00:26:19] just sort of matching the teacher on the
[00:26:21] benchmaxing distribution. And um uh but
[00:26:24] if you don't have enough of the
[00:26:26] environments that really exercise the
[00:26:28] capabilities in these um like trickier
[00:26:31] realistic settings, then you're not
[00:26:32] going to you're not going to get those
[00:26:34] into your student model. And I think
[00:26:36] maybe one thing that's happening is the
[00:26:38] big models uh generalize better from the
[00:26:41] uh like the tricky narrow tasks uh to
[00:26:44] these sort of uh more realistic tasks.
[00:26:47] Um so if you have a really good um like
[00:26:51] realistic uh prompt distribution for
[00:26:53] distillation, you can match uh the big
[00:26:55] model really well. But if you only have
[00:26:57] this uh like uh this distribution of
[00:27:01] easily verifiable tasks, then you can
[00:27:03] match the big model on all the
[00:27:04] benchmarks. um but uh you do worse on um
[00:27:07] this broader distribution. So you might
[00:27:10] uh that might even explain um something
[00:27:13] about the uh smaller anthropic models uh
[00:27:16] like Sonnet 5, though it's hard to
[00:27:18] predict exactly what uh what they're
[00:27:20] doing to post-train those models. It
[00:27:22] could also be that they're always
[00:27:23] changing their post-raining uh stack and
[00:27:26] they just um made they just got a few
[00:27:28] things wrong in some of these models. So
[00:27:30] they uh like I I don't know they they
[00:27:33] turned up like some um something too
[00:27:37] high and created some quirks that people
[00:27:38] really don't like. So it's like really
[00:27:40] easy to screw up post training in some
[00:27:42] way that's uh doesn't show up in
[00:27:44] benchmarks. I mean just one other sort
[00:27:46] of very basic point is just like the AI
[00:27:48] like the frontier AI labs buy all their
[00:27:50] data from big data companies and like
[00:27:51] the Chinese can also just buy the same
[00:27:52] data from data companies and they are
[00:27:54] like they are exactly there's a lot of
[00:27:55] people like you know being annoyed about
[00:27:57] this but like if they have exactly the
[00:27:59] same data and like they can buy that
[00:28:00] they can also distill it's like it's it
[00:28:03] means it's quite easy to like keep up
[00:28:05] really.
[00:28:05] >> Yeah. Yeah. Yeah. Okay. The the other
[00:28:07] question I had is
[00:28:09] how the first models that are capable of
[00:28:12] automating AI R&D will actually be
[00:28:14] trained because there's a toy version
[00:28:16] which is this thing that Ryan was
[00:28:19] talking about which is you just have
[00:28:20] GPT8 try to build GPT3 size models that
[00:28:24] are really good at like inner loop type
[00:28:26] challenges of beating video games that
[00:28:28] require continual learning or um just
[00:28:31] get getting to a certain loss with like
[00:28:33] the least amount of compute etc. But
[00:28:35] John, I think you had an interesting
[00:28:36] point that maybe that's not the way it
[00:28:37] actually will happen in practice. So I'd
[00:28:40] be curious about yeah, by the point
[00:28:41] which you have that are actually capable
[00:28:43] of automating R&D, how are they probably
[00:28:44] trained?
[00:28:45] >> Yeah, I think we'll probably do some
[00:28:47] combination of learning from human
[00:28:48] feedback to absorb uh like the
[00:28:50] researchers taste uh and uh just like
[00:28:53] creating a lot of practice environments
[00:28:56] uh which involve like doing multi-step
[00:28:58] research projects. So I think uh yeah
[00:29:03] people will in practice do some
[00:29:04] combination of those two things and uh
[00:29:07] just um each iteration like patch
[00:29:09] whatever seems to be most broken in the
[00:29:12] last iteration. So uh like researchers
[00:29:15] will be using uh the AIS uh a lot and um
[00:29:19] and we'll notice that they have some
[00:29:21] consistent weaknesses and then uh those
[00:29:23] things will either be patched by like
[00:29:25] collecting human feedback or uh like
[00:29:27] creating environments.
[00:29:28] >> Yeah. Makes sense.
[00:29:29] >> Maybe maybe useful way to think about
[00:29:31] this is like how much of the lineage we
[00:29:33] roll back and then let self play from
[00:29:34] there. Like I think in the limit like
[00:29:37] you're picturing like you know just
[00:29:38] giving them like a GPU and maybe neural
[00:29:41] nets or something and saying like okay
[00:29:43] figure out how to train a model to like
[00:29:45] do these particular tasks. Like the way
[00:29:48] it currently works is like we go up to
[00:29:49] the very like edge of the of the lineage
[00:29:51] and say okay like here are the bugs like
[00:29:53] you know Anthropic has found in their
[00:29:54] training stack in the last few months.
[00:29:55] tenants into environments like you need
[00:29:57] to train and get better on the frontier
[00:29:59] and so you obviously lock in all the
[00:30:00] previous history of the lineage but you
[00:30:02] could imagine a world in which you roll
[00:30:03] back to like you know before GRPO or
[00:30:06] something and then you have environments
[00:30:07] which like trying to get it to discover
[00:30:09] like the best will form to like oral
[00:30:11] models on and then maybe roll further
[00:30:13] and further back but I think we will be
[00:30:15] still so computer bottlenecked that like
[00:30:17] people will just keep like staying at
[00:30:18] the frontier and like diffing
[00:30:20] essentially the bugs and whatever
[00:30:21] improvements they found since the last
[00:30:22] model version turning those into
[00:30:23] training environments
[00:30:24] >> which is also really good for having
[00:30:25] non-stale like new data between model
[00:30:29] generations. is just again this is
[00:30:30] basically continual learning within the
[00:30:32] AI lab of distilling the last 3 months
[00:30:35] of AI research progress through
[00:30:37] environments and like RLHF's type stuff
[00:30:40] back into the model itself
[00:30:41] >> and and it is distilling right and
[00:30:43] that's maybe why some of us feel like
[00:30:44] it's asic is like you're always like
[00:30:47] just trying to get the last 3 months of
[00:30:49] progress and that that progress is being
[00:30:51] contributed to bys of course but it also
[00:30:53] still has humans in the loop and it
[00:30:54] feels like you know you're just
[00:30:55] constantly inching closer and closer to
[00:30:57] what the human researchers are like
[00:30:58] finding capable apable of doing.
[00:31:00] >> Yeah.
[00:31:00] >> I mean, the one thing I will say though
[00:31:01] is like obviously if you're just
[00:31:02] distilling on like trajectories, you can
[00:31:04] never go above it, but environments can
[00:31:05] go quite a far way above what a humans
[00:31:07] can do. Like it's very easy to design
[00:31:08] environment that like no human can
[00:31:09] solve, but the AI can obviously still
[00:31:11] try and solve it.
[00:31:12] >> And so that would be the path to like go
[00:31:13] ahead of just like what the human AI
[00:31:15] research.
[00:31:15] >> Do you have like an example of like
[00:31:17] >> in terms of RSI or like like you know
[00:31:20] doing it even faster than a human speedr
[00:31:22] runner?
[00:31:22] >> Yeah. I mean, I feel like in AI research
[00:31:24] especially, it's very easy to define
[00:31:25] like goals which like, you know, you
[00:31:27] could say like the loss needs to be like
[00:31:28] 1.3 or something and like no human can
[00:31:30] get there, you know, now, but like
[00:31:32] that's a very extremely measurable
[00:31:34] verifiable task and the if the AI gets
[00:31:35] there then then great,
[00:31:37] >> right? I don't know. Building like a 100
[00:31:39] million parameter model that beats
[00:31:40] Minecraft, that's maybe too easy, but
[00:31:42] like be like a much more complicated
[00:31:44] game or something.
[00:31:45] >> Isn't it crazy that 100 million
[00:31:47] parameter models to beat Minecraft?
[00:31:48] We're calling that too easy. Like
[00:31:49] imagine you said that [laughter] like
[00:31:50] five years ago. I would say a lot of
[00:31:53] research is not exactly like that though
[00:31:56] where it's like hill climbing on a well-
[00:31:57] definfined goal. It's sort of more like
[00:31:59] uh here's an intuition we have about uh
[00:32:02] some way model should be better and then
[00:32:04] we also have uh some idea for an
[00:32:06] algorithm that seems to go a little bit
[00:32:09] in this direction. So let's come up with
[00:32:12] a task that is uh sort of designed to
[00:32:15] show signs of life on this approach and
[00:32:18] uh like see if we get some uh get those
[00:32:21] signs of life and then if we do we can
[00:32:22] make successively more realistic
[00:32:24] versions of the task, right? It's like a
[00:32:26] lot more guided by intuition and then
[00:32:29] the the out the the inner loop is to
[00:32:31] elicit the uh or make test for that
[00:32:35] intuition rather than like the the the
[00:32:37] test itself leading to the insight,
[00:32:40] >> right? Like you're not directly
[00:32:41] optimizing uh for the eventual objective
[00:32:44] you care about or the practical
[00:32:46] >> like production objective. It's it's
[00:32:49] sort of uh you're um you're relaxing
[00:32:52] your objective a little bit. You're
[00:32:54] saying, "Yeah, let's relax on the
[00:32:55] realism axis a little bit and find uh
[00:32:58] some methods that actually work and then
[00:33:00] like then try to get back to realism
[00:33:02] later after the method matures a little
[00:33:04] bit."
[00:33:04] >> Yeah.
[00:33:04] >> And then there's also like more uh
[00:33:08] there's research that's more oriented
[00:33:09] towards explaining things and like uh
[00:33:12] developing a theory or a sort of Yeah.
[00:33:15] often we don't have like mathematical
[00:33:17] theories in machine learning that are
[00:33:19] that um predictive but we have like a
[00:33:21] lot of um like more informal theories
[00:33:25] for what's going on.
[00:33:26] >> Yeah. I mean like presumably the models
[00:33:28] will be trained on like some combination
[00:33:29] of all of these tasks and like some will
[00:33:30] be very easily verifiable some will be
[00:33:32] like l judge or like just ask the human
[00:33:34] like does this look reasonable and then
[00:33:36] you will the hope would be that like
[00:33:39] these would all generalize to like these
[00:33:40] much sort of hard sort of more vague
[00:33:42] fuzzy kind of tasks and like it probably
[00:33:43] will to some extent whether it
[00:33:44] generalized enough that like we could
[00:33:46] the loop can become like self-sealing
[00:33:48] without humans being in the loop at all
[00:33:49] it's like unclear.
[00:33:50] >> Yeah. Yeah. Yeah. Wait, maybe taking a
[00:33:52] step back. Here's what I here's what it
[00:33:54] seems to me that the plan uh for AI
[00:33:58] research going forward is and you tell
[00:33:59] me if you think it's going to work or if
[00:34:01] you agree with this characterization.
[00:34:03] So the bet is that we will scale up RLVR
[00:34:07] training across millions of diverse
[00:34:10] environments across hundreds of
[00:34:11] different kinds of domains. And what
[00:34:14] will emerge at the other end is an agent
[00:34:16] which has like learned these basic skill
[00:34:18] or less than basic skills around being
[00:34:21] persistent um being able to triage
[00:34:24] information in context uh eventually
[00:34:27] having like end to- end optimization of
[00:34:28] working with other agents and things
[00:34:29] like that. And such an agent will be
[00:34:32] very sample efficient within the
[00:34:34] context. You know, you've done research
[00:34:35] on how you actually scale up in context
[00:34:37] learning to make it like arbitrarily
[00:34:38] long, but you keep scaling it up. And so
[00:34:41] what comes out the other end will
[00:34:42] something will be something that it
[00:34:43] basically functions like a drop in
[00:34:45] remote worker over the course of a week
[00:34:47] or a month. First of all, do you agree
[00:34:49] that that is a bet the labs are making?
[00:34:50] And second, is it is that enough like
[00:34:53] basically learning how to learn within
[00:34:55] these simulacura within a data center uh
[00:34:58] and then getting deployed into the real
[00:35:00] world? but not actually like learning
[00:35:01] from real world deployment, only
[00:35:02] learning these meta skills from the the
[00:35:05] simulated environments in the data
[00:35:06] center.
[00:35:07] >> Yeah, I I think it's now hard to
[00:35:10] separate out like how much of the lab's
[00:35:12] effort is going towards like direct RSI
[00:35:14] versus like making generally intelligent
[00:35:16] models they can continue to deploy to
[00:35:18] collect revenue to fund the next big
[00:35:19] training run. I think for the um latter
[00:35:23] like yes that's probably just the bet
[00:35:24] they're making like and it's very clear
[00:35:27] like the pattern of like where these
[00:35:28] environments are going over the last few
[00:35:30] years. I mean like anthropics lineage of
[00:35:32] of environments is like a very clear
[00:35:33] example of this like you know first like
[00:35:35] we just focus on coding and like we're
[00:35:37] going to get really really good at that
[00:35:38] and then the task horizon that we've got
[00:35:41] from coding which is probably the lowest
[00:35:42] hanging fruit in terms of like data
[00:35:44] available on the internet to create
[00:35:45] environments like their own internal
[00:35:47] stuff that they can turn into
[00:35:48] environments. then we're going to
[00:35:49] generalize. We're going to go after
[00:35:50] finance next and like literally like
[00:35:52] just so much Excel data and and all that
[00:35:54] sort of stuff in the in the training and
[00:35:56] then you know it's powerpoints. It's
[00:35:58] like this long tale of like the working
[00:35:59] economy and like that seemed to work
[00:36:01] really well and like a lot of the other
[00:36:02] labs and thing even the open source labs
[00:36:04] have now realized that that was the
[00:36:05] correct
[00:36:05] >> that but what is the implication from
[00:36:07] that when I had Dario on the podcast the
[00:36:09] thing I asked him was if you truly
[00:36:10] expect models which will be humanlike in
[00:36:12] their ability to learn on the job why
[00:36:15] would you try to bake in all these uh
[00:36:18] skills of like working with PowerPoint
[00:36:20] or something wouldn't you just expect
[00:36:21] the model to be able to pick that up on
[00:36:23] while it's deployed and so yeah there's
[00:36:25] multiple different explanations one is
[00:36:26] just that this
[00:36:27] we expect models to get there soon, but
[00:36:29] they're not there yet. So, why not
[00:36:31] amortize these skills um into the model
[00:36:34] training. Another is that we're not
[00:36:37] concentrated on making it really good at
[00:36:39] widely deployed work. We just want it
[00:36:41] really good at RSI. Um, and this is just
[00:36:44] like a way for us to like get revenue so
[00:36:46] that we can pour it back into a model
[00:36:47] that is actually like really good at
[00:36:48] doing um RSI development and then like
[00:36:51] once the singularity happens the thing
[00:36:52] that comes out the other end will be
[00:36:54] really good at all the things which seem
[00:36:55] like bottlenecks to the current
[00:36:57] generation of models. Yeah, John I don't
[00:36:58] know if you have takes on like what um
[00:37:00] how how once you construe why there is
[00:37:02] so much task specific knowledge in these
[00:37:05] models if the if the path is like this
[00:37:06] kind of generalization. Yeah, I mean if
[00:37:09] the models were good enough at learning
[00:37:10] in context, then in theory you wouldn't
[00:37:12] be a you wouldn't need to train them on
[00:37:14] finance. Uh they would just be able to
[00:37:16] figure out uh read all the um all the
[00:37:19] books on the fly and uh figure out how
[00:37:21] to
[00:37:22] >> how to do everything in the appropriate
[00:37:24] jurisdiction.
[00:37:25] >> Um yeah, and you could argue that um you
[00:37:28] need to do um a lot of this domain
[00:37:30] specific training um just to make the uh
[00:37:32] to make them more efficient. Uh so even
[00:37:35] if they they were smart enough to figure
[00:37:37] this out on the fly, you still might
[00:37:38] want to do a bunch of RL and bake the uh
[00:37:42] bake all these intuitions into the
[00:37:44] weights. Uh so the model would be more
[00:37:46] efficient at runtime.
[00:37:47] >> Yeah.
[00:37:48] >> Yeah. I'd say in practice it does seem
[00:37:50] like um model providers are um going
[00:37:53] domain by domain and trying to
[00:37:54] strengthen the models in the highest
[00:37:56] value domain. And I I'd say that that's
[00:37:58] one of the answers to why the models
[00:38:00] have gotten so much better. It's just
[00:38:02] because um the model providers have
[00:38:04] covered a lot of the highv value domains
[00:38:06] and the most [clears throat] common
[00:38:09] types of skills.
[00:38:10] >> I mean I think another thing is just
[00:38:11] that like it's not that expensive to do
[00:38:13] both at the same time, right? Because
[00:38:14] like the models are massive. they can
[00:38:15] easily afford in terms of their
[00:38:16] parameters to like learn everything and
[00:38:18] like there is likely some transfer in
[00:38:19] sort of even just even if like finance
[00:38:21] is not specifically like the information
[00:38:23] is important for like RSI just the
[00:38:24] general like metal learning of like how
[00:38:26] to figure out what's important how to
[00:38:27] have taste how to like do long horizon
[00:38:29] work is potentially generalizable and
[00:38:31] like there's not that much RSI like data
[00:38:33] in the world as well like it's kind of
[00:38:34] hard to generate and like that requires
[00:38:36] a lot of effort so like if you can of
[00:38:37] amatize in this other data get some
[00:38:39] transfer from it you already have masses
[00:38:41] of comput masses of parameter space so
[00:38:42] like why not do that as well as like
[00:38:44] obviously the direct like commercial
[00:38:45] incentive of like selling a model.
[00:38:47] >> Yeah, it makes sense.
[00:38:48] >> Oh yeah, I'll add that. Um I mean
[00:38:50] there's one question about whether um
[00:38:52] this uh current paradigm uh of doing
[00:38:55] like sim to real uh will be the dominant
[00:38:58] one forever. So basically you you look
[00:39:00] at what the real world tasks uh are like
[00:39:02] and then you try to create a bunch of
[00:39:04] environments that can be simulated uh
[00:39:06] like in the data center and uh you can
[00:39:09] do RL on them and I think um obviously
[00:39:12] this has been very successful successful
[00:39:14] but it has a lot of weaknesses uh
[00:39:16] because a lot of things are just kind of
[00:39:18] hard to simulate um especially if they
[00:39:20] involve like interact interacting with a
[00:39:23] bunch of humans in real time. Yeah. So
[00:39:25] there's some question about uh like sim
[00:39:27] like whether sim to real will be the
[00:39:29] dominant framework forever.
[00:39:31] >> I think sim to real has to be the
[00:39:32] dominant framework while like sample
[00:39:33] efficiency is kind of low cuz like right
[00:39:35] now you need like you know thousands and
[00:39:37] thousands of interactions with the
[00:39:38] humans and no human is going to sit
[00:39:39] there and like deal with this basically
[00:39:40] be in the loop of RL training
[00:39:42] >> and so like we kind of have to simulate
[00:39:44] that now to like get the samples you
[00:39:45] need but like obviously if sample
[00:39:46] affinity improves a lot you'd expect
[00:39:48] learning from deployment to like become
[00:39:50] like a much bigger part of it. Though
[00:39:51] there are also other things you could do
[00:39:53] like you can learn um off policy so you
[00:39:56] can take all the traces and even without
[00:39:58] reimulating everything you can
[00:39:59] potentially learn something from them.
[00:40:01] >> Jane Street just launched a new
[00:40:03] competition and it's their most
[00:40:04] ambitious one yet. Design a protocol
[00:40:07] emulator ASIC. Basically if you have a
[00:40:09] chip that you want to test you can
[00:40:10] connect it to this ASIC and then this
[00:40:12] ASIC will simulate realistic traffic.
[00:40:14] That way you can see how the chip
[00:40:16] responds without having to plug it into
[00:40:17] a live system. Jane Street is looking
[00:40:19] for flexible generalpurpose designs, not
[00:40:22] single protocol emulators. When I was
[00:40:24] chatting with them, they suggested that
[00:40:25] I start off by trying to implement what
[00:40:27] are apparently three very common
[00:40:29] protocols, UART, SPI, and I squared C.
[00:40:32] Jere also mentioned that they hoped that
[00:40:34] more ambitious designs will also tackle
[00:40:37] low-speed USB and Ethernet and any other
[00:40:39] protocols that flex your chip specific
[00:40:42] architecture. Importantly, your design
[00:40:44] should be reprogrammable rather than
[00:40:46] smashing a bunch of specific protocols
[00:40:48] onto a chip. If a new protocol comes out
[00:40:51] after your ASIC is taped out, your chip
[00:40:53] still needs to be able to handle it. How
[00:40:55] exactly it does it is up to you, but
[00:40:57] there is one hard constraint. Your
[00:40:59] design must target an open-source 130 nm
[00:41:03] process node. That's because Jane Street
[00:41:04] will pay to tape out the most novel
[00:41:06] submissions and send the physical copies
[00:41:08] to the winners. The competition is open
[00:41:10] till January 18th, 2027 and working in
[00:41:13] Teams is highly encouraged. Go to
[00:41:16] janestreet.com/scash
[00:41:19] to download the template code and get
[00:41:20] started.
[00:41:22] I want to ask more about this cuz it
[00:41:24] it's sort of weird that you have 50% of
[00:41:28] compute that's spent on inference that
[00:41:29] is not directly helping the model become
[00:41:32] better. Like one of the key advantages
[00:41:33] you'd expect eventually digital minds to
[00:41:35] have is unlike a human who gets to have
[00:41:38] 50 years of like real world experience,
[00:41:40] a model will get to through all its
[00:41:43] instances will get to experience I don't
[00:41:45] know millions of years of deployment
[00:41:48] across all kinds of economically
[00:41:49] relevant work in the economy and right
[00:41:52] now that data is just not in a
[00:41:53] meaningful sense helping the model get
[00:41:55] better. Like it just seems so obvious
[00:41:57] that eventually models should be able to
[00:41:59] learn from this data and once they do
[00:42:00] you would have something that almost
[00:42:02] feels like a widely deployed
[00:42:03] intelligence explosion because the model
[00:42:05] is assimilating so much information um
[00:42:07] across all these deployed instances but
[00:42:09] when do you expect this kind of hive
[00:42:10] mind kind of crazy to be start
[00:42:12] happening.
[00:42:13] >> I think broadly like at a very basic
[00:42:15] level this is already happening right
[00:42:16] like just in the next generation of
[00:42:17] models. So like right now you can
[00:42:19] obviously take your deployment data and
[00:42:20] put this in the pre-train or the mid
[00:42:22] train of like future models especially
[00:42:23] if you do like some kind of filtering or
[00:42:25] some kind of like judgment or annotation
[00:42:26] or like recent you know synthesization
[00:42:28] of that.
[00:42:28] >> How much do you think that explains the
[00:42:30] generation over generation improvement?
[00:42:31] >> I think it explains like quite a bit. I
[00:42:33] mean especially like I mean this is you
[00:42:34] know I don't know whether the labs do
[00:42:36] this because you know theoretically they
[00:42:37] claim not to train on people's data but
[00:42:39] like the Chinese 100% do and like they
[00:42:41] definitely get this advantage both like
[00:42:42] obviously deploying this is basically
[00:42:44] what distillation is like they take out
[00:42:45] the models they get some of their like
[00:42:47] deployment data they get some fraction
[00:42:48] of that by like pinging the model and
[00:42:50] then they train their next generation
[00:42:51] models on it and they can suddenly do it
[00:42:52] on their own models as well like there's
[00:42:54] no reason not to whatsoever.
[00:42:55] >> I completely agree with this. I think if
[00:42:56] you zoom out far enough, this is like
[00:42:58] definitely happening. Like you're
[00:42:59] picturing this like and we're all
[00:43:01] picturing this. This is like what
[00:43:02] continual learning like the holy grail
[00:43:03] is is like
[00:43:04] >> this very very organic like live loop of
[00:43:07] like an individual model like getting an
[00:43:08] experience and like live updating on the
[00:43:10] spot and learning from that. And like a
[00:43:12] lot of things break when you like zoom
[00:43:13] into that level of granularity. But like
[00:43:15] yeah the big labs are doing this like
[00:43:16] the closed the closed models are doing
[00:43:18] this. There's also early signs of life
[00:43:19] of like people using open source models
[00:43:21] doing this at a much faster cadence. So
[00:43:24] like a good example is probably like
[00:43:25] composer um like you have some sort of
[00:43:28] model and you are able to or like you
[00:43:31] know Harvey's doing the same thing with
[00:43:32] like legal legal agents like
[00:43:35] >> it is getting very specific environments
[00:43:37] from the data that you have for that
[00:43:39] particular task and things that like you
[00:43:40] know users are complaining about and
[00:43:42] like all the feedback that you're
[00:43:43] somehow extracting from like your
[00:43:45] specific deployments and a lot of these
[00:43:47] companies have the advantage over the
[00:43:48] big labs and that they can use this data
[00:43:50] really really well and then they will
[00:43:52] create environments they like you know
[00:43:53] do a big post train of Kimmy K3 um they
[00:43:56] will go deploy it they might do some
[00:43:57] online learning as well like composer
[00:43:59] did online basically like reinforce for
[00:44:01] a long time um so yeah like there's
[00:44:04] still a human in the loop there's still
[00:44:05] a human saying okay these are the
[00:44:06] signals we care about here's how we're
[00:44:07] going to create environments from the
[00:44:08] data that we have and it's like still a
[00:44:10] longer cadence than maybe the one that
[00:44:12] you're thinking of but like it really is
[00:44:13] happening and like eventually that loop
[00:44:15] will become like faster and faster
[00:44:16] >> I mean the composer thing is interesting
[00:44:17] because this is where the model like in
[00:44:20] cursor people like press tab or they
[00:44:22] don't press tab tab on the next
[00:44:24] completion that the model suggests and
[00:44:26] based on that every single day composer
[00:44:28] gets better at like predicting the next.
[00:44:29] >> So that was that was the old tab model
[00:44:31] like they actually did the same thing
[00:44:32] for the actual not just like the tab
[00:44:34] model but the actual like generative
[00:44:35] model. Oh, it's interesting.
[00:44:36] >> And they it was it's hard because when
[00:44:38] you do online reinforcement learning,
[00:44:40] you don't have groups, right? You just
[00:44:41] have one user saying one thing and then
[00:44:42] you get one roll out. And so like you
[00:44:44] have a big variance reduction problem
[00:44:46] >> and like curs's kind of fuzzy answer to
[00:44:48] this was like oh you know we have very
[00:44:49] good heristics which are able to
[00:44:51] estimate like
[00:44:52] >> like what the what how much better than
[00:44:54] average like this response was or how
[00:44:55] much worse than average this response
[00:44:56] was. And then they would do like this
[00:44:58] big, you know, like reinforce update and
[00:45:01] then their solution to like whether it
[00:45:02] got worse or not was like if it improved
[00:45:04] on cursor bench, they would deploy the
[00:45:05] new model like every five hours and if
[00:45:07] it didn't, they would like throw that
[00:45:08] version out.
[00:45:08] >> Interesting.
[00:45:09] >> Yeah. I think your biggest problem is
[00:45:10] actually just not knowing what the
[00:45:12] reward function should be from natural
[00:45:13] data. And if you use some kind of
[00:45:16] superficial signal like did they accept
[00:45:18] the the code the the edit um you might
[00:45:22] that might get reward hacked in some
[00:45:24] way. But is it this seems like a bigger
[00:45:26] issue with the sim to real thing where
[00:45:28] the longer and longer horizon tasks get,
[00:45:31] the harder they are to simulate within a
[00:45:33] data center, right? It seems to me
[00:45:35] already potentially at least even in
[00:45:37] coding, we're getting to over the point
[00:45:38] where um there there's like not some
[00:45:42] year-long coding task that doesn't
[00:45:44] eventually require you to like talk to a
[00:45:46] client or interact with the company or
[00:45:48] interact with users. And if you think
[00:45:50] about the gamut of things we would want
[00:45:52] AI to be capable at, you want eventually
[00:45:54] super intelligence should be able to
[00:45:55] like run a business or like start a new
[00:45:57] business and make it profitable or like
[00:45:59] have a profitable day trading in the
[00:46:00] markets or win a court case. And these
[00:46:02] are all things which are very hard to
[00:46:04] simulate in a data center like inherent
[00:46:06] part of the learning there is
[00:46:07] interacting with the real world. Then so
[00:46:09] maybe maybe yeah they better learn how
[00:46:10] to get better at these things from like
[00:46:12] the transfer between sim to real but
[00:46:14] alternatively maybe you do need weight
[00:46:16] updates from these kinds of interactions
[00:46:19] in order to get better at them and then
[00:46:21] if that is the case if transfer isn't
[00:46:23] strong enough and you need do need
[00:46:24] weight updates then the fact that the
[00:46:25] models are quite sample inefficient is
[00:46:28] like maybe a deeper problem and the
[00:46:30] reason I'm curious about this I feel
[00:46:32] like by default I I don't see how you
[00:46:35] don't get some kind of crazy recursive
[00:46:36] self-improvement within the next 10
[00:46:38] years. But the one reason why that might
[00:46:40] not happen is in terms of like weight
[00:46:43] updates, the sample efficiency of weight
[00:46:45] updates, they just seem way far behind
[00:46:47] humans, right? Like plausibly
[00:46:48] millionfold behind humans in terms of
[00:46:50] how much data a human sees from birth to
[00:46:52] adulthood versus how much a model sees
[00:46:54] from, you know, like cold start to like
[00:46:56] finishing training. And so yeah, this is
[00:47:00] all to say first of all, is there is
[00:47:02] there going to be a good transfer
[00:47:03] between simulations and extremely long
[00:47:04] horizon really complicated real
[00:47:06] that we want the AI to do in the real
[00:47:07] world? And if not, does that really mean
[00:47:09] that like the the lack of sample
[00:47:10] efficiency in these models comes to bite
[00:47:12] us?
[00:47:13] >> I think maybe the way I'd break down
[00:47:16] like the two types of tasks in which
[00:47:17] models get good and models will like
[00:47:19] still continue to struggle is whether
[00:47:20] the task is like cumulative or like you
[00:47:23] kind of have to you have this like
[00:47:24] non-stationary distribution you have to
[00:47:26] keep learning and like relitigating a
[00:47:27] bunch of stuff. So like maybe an example
[00:47:29] of a cumulative task might be RSI like
[00:47:32] it's theoretically possible to maybe
[00:47:34] like have a less than a million token
[00:47:35] like you know Python file which like
[00:47:37] from scratch trains a model that is
[00:47:39] capable of recursive self-improvement
[00:47:41] and like every discovery that you make
[00:47:43] is kind of a line in the sand that you
[00:47:44] hold like if it's true that you know for
[00:47:46] RSI we don't need to discover a new
[00:47:48] attention variant or whatever like once
[00:47:49] you've discovered attention and then
[00:47:50] once you've discovered you know mixture
[00:47:52] of experts and once you discover GPO you
[00:47:53] just add that to the training stack and
[00:47:55] like that's that's there and like a good
[00:47:57] example of this is like you 5.6 all
[00:48:00] training 5.6 ter whichever one openai
[00:48:02] told it to train like it didn't have to
[00:48:04] go back and discover attention like it
[00:48:06] basically probably would have called a
[00:48:07] bunch of like scripts which is like
[00:48:08] pre-training.sh and post training.sh and
[00:48:11] just did that. So like that's an example
[00:48:12] of like a cumulative task. I think the
[00:48:14] real world and the reason like people
[00:48:16] are thinking so much about like continue
[00:48:17] learning is it's it's not really a
[00:48:19] cumulative task. Like imagine like in a
[00:48:21] law firm you have an agent acting as a
[00:48:23] legal associate. Like that's a very
[00:48:25] non-stationary distribution. you have to
[00:48:27] be able to fit in your context like all
[00:48:29] the relationships between all the
[00:48:30] important people at that company which
[00:48:31] are also changing all the time. Yeah.
[00:48:33] >> Um you have like all these like implicit
[00:48:35] like ways about how things are done,
[00:48:36] where to find information etc. And like
[00:48:38] that's not as as clean of an example of
[00:48:41] a cumulative task as like RSI is. So I
[00:48:44] think that there will be this breakdown
[00:48:45] between tasks but you know like if the
[00:48:46] labs realize that and they they do
[00:48:48] believe that RSI is cumulative in the
[00:48:49] sense that like we don't need to go back
[00:48:51] and discover some brand new like
[00:48:52] architecture or whatever
[00:48:53] >> then maybe more and more effort and
[00:48:55] comput gets focused on that versus the
[00:48:56] >> it's so unfortunate that RSI happen to
[00:48:58] be easier than parallegal. [laughter]
[00:49:01] >> Yeah.
[00:49:02] >> Um yeah I don't know if you guys have
[00:49:03] thoughts on this. Yeah, I would say
[00:49:05] there's uh like models um are today's
[00:49:08] models are um weaker than humans in a
[00:49:11] lot of different ways and uh some of
[00:49:13] them might have to do with um sample
[00:49:15] efficiency in a certain regime. Uh where
[00:49:18] I mean in in some regimes models are
[00:49:20] very sample efficient like learning in
[00:49:22] context. Uh but then there might be some
[00:49:24] like medium length regime where they're
[00:49:26] less sample efficient because humans can
[00:49:28] uh do uh some kind of weight update um
[00:49:32] more efficiently than models. So so I
[00:49:35] think like being less sample efficient
[00:49:37] in certain regimes might be one of the
[00:49:40] sources of weakness. But then I think
[00:49:41] there are other sources of weaknesses
[00:49:42] that are completely different than that.
[00:49:45] for example, uh having lower diversity
[00:49:48] of thought than humans or um yeah being
[00:49:52] bad at certain kinds of long horizon
[00:49:53] judgments. Uh I mean I think a lot of um
[00:49:56] what people call taste is uh is
[00:49:59] something about um behavior that um
[00:50:03] works in the long run and that people
[00:50:05] have realized works in the long run. uh
[00:50:08] not everything but like some some aspect
[00:50:11] of taste like especially for something
[00:50:13] like software engineering like I think a
[00:50:15] lot of taste is like what are the
[00:50:17] systems that are going to be
[00:50:18] maintainable and
[00:50:20] >> uh work well yeah in the long run of
[00:50:22] this project. So uh yeah I think the
[00:50:25] weaknesses of humans which limit um RSI
[00:50:30] along with other things uh are um yeah
[00:50:33] there's a variety of them and some of
[00:50:35] them are related to sample efficiency
[00:50:36] and some of them aren't. Maybe an
[00:50:38] interesting thought experiment is like
[00:50:39] if you were able to give a model like a
[00:50:42] context window of I don't know a
[00:50:43] trillion tokens or whatever you would
[00:50:45] have needed to fit in like your
[00:50:46] experience prior to like let's say RHF
[00:50:49] and like it's got all that experience in
[00:50:51] the context window and has the same
[00:50:53] sample efficiency and in context
[00:50:55] learning ability as it does at a million
[00:50:56] tokens like do you think taste is then
[00:50:59] solved like would it be able to like
[00:51:00] make the same judgments that you did or
[00:51:02] is there like something fundamentally
[00:51:03] missing apart from just a longer context
[00:51:05] window with the same sample efficiency?
[00:51:07] Yeah, I mean it would have to be trained
[00:51:08] to learn from that context. So, uh I'm
[00:51:12] not sure um yeah, either it would have
[00:51:15] to be um trained to learn uh the right
[00:51:18] update um to make from that context or
[00:51:21] >> you have to just like dump it all in
[00:51:23] like your whole like life like research
[00:51:25] experience.
[00:51:25] >> I mean like you still need the data to
[00:51:27] train it long context, right? Like even
[00:51:28] if you could theoretically get like a
[00:51:29] trillion context, you would need a
[00:51:31] trillion lengths of data to train it.
[00:51:32] Like right now you have like context.
[00:51:35] I'm just asking if you had that
[00:51:37] >> in theory. I think yes. I mean, this
[00:51:38] really just comes down to the question
[00:51:40] of like how metalarnable is taste from
[00:51:42] like shorter horizon episodes and like I
[00:51:44] feel like there's no obvious reason it's
[00:51:46] super long cuz like humans somehow
[00:51:47] develop taste with not having many long
[00:51:49] episodes like we don't live to be like
[00:51:51] 10,000. We have like you know we develop
[00:51:53] pretty quickly, right? And so like you
[00:51:55] know if you think about like even like
[00:51:56] in a PhD the difference between like a
[00:51:57] first year PhD student and like a final
[00:51:59] like postto or something that's like
[00:52:01] five years maybe and they've only done
[00:52:02] like maybe like 10 fifth 30 research
[00:52:04] projects in total but somehow they
[00:52:06] develop taste quite quickly from like a
[00:52:08] relatively short succession of like
[00:52:09] small things and so like theoretically
[00:52:11] it's you know possible to develop it
[00:52:13] like that. The AI obviously will have
[00:52:14] vastly more experience in which to
[00:52:16] develop taste to like metal learn it and
[00:52:18] there's like how well does that
[00:52:19] generalize to like really long horizon
[00:52:20] things is I think the question which I
[00:52:22] think is really unsolved at this point
[00:52:23] like we don't know going back to this
[00:52:26] question
[00:52:27] eventually there should be a regime
[00:52:28] where EIS are learning a ton from each
[00:52:31] individual instance of deployment that
[00:52:32] they have well currently you could say
[00:52:34] there's a meta fuzzy process by which
[00:52:37] models do improve from deployment but I
[00:52:39] feel like it's a very weak uh very weak
[00:52:42] uh feedback loop Do you see this around
[00:52:44] the horizon where there's this like hive
[00:52:45] mind kind of learning that's very rapid
[00:52:48] and um and if if so how exactly does it
[00:52:50] happen?
[00:52:52] >> Actually I would say that around uh will
[00:52:55] we get a hive mind uh that learns from
[00:52:57] all of its deployment experience? I mean
[00:52:59] a big part of that is actually about
[00:53:01] incentives uh rather than um being a
[00:53:04] technical question. So like companies
[00:53:06] aren't going to want to um have the
[00:53:08] model provider learn from all of their
[00:53:11] deployment because that that might just
[00:53:13] reduce the uh advantage of their
[00:53:15] business.
[00:53:16] >> I think that maybe the economics of this
[00:53:19] will pressure not necessarily weight
[00:53:21] updates to one big like common shared
[00:53:23] model but like kind of like modules that
[00:53:25] get subbed in. like a very obvious
[00:53:27] example. This is a Laura, but it might
[00:53:28] be something else like you know there's
[00:53:30] been a lot of work to try and fit like
[00:53:32] an arbitrary context length into a fixed
[00:53:34] size like this is all the linear tension
[00:53:35] stuff and all that sort of stuff and
[00:53:36] like cartridges which are essentially KB
[00:53:39] cases trained to be very very compressed
[00:53:41] KB cases to fit in a lot of information.
[00:53:43] That's another example of like you know
[00:53:45] something that like companies may be
[00:53:47] willing to sign up for if that's get
[00:53:48] subbed into the model and it's not like
[00:53:50] actually changing the base underlying
[00:53:51] model itself. So like there's many
[00:53:53] different versions of like learning from
[00:53:54] from your data in real time and like the
[00:53:57] latter ones are not really helping the
[00:53:58] big labs cuz they are just these
[00:53:59] modules. But I think the like the like
[00:54:02] the the economic pressure will force
[00:54:04] like the labs to go down that path first
[00:54:06] before they can embark on this like you
[00:54:08] know
[00:54:09] >> so which economic pressure though cuz I
[00:54:11] feel like even if you have like a bunch
[00:54:12] of cartridges or laws or whatnot you can
[00:54:14] still just like take all these traces
[00:54:15] and just like distill this dub this to
[00:54:17] the pre-training of like your next
[00:54:18] generation of bombers.
[00:54:19] >> Yeah. So it it may be a more indirect
[00:54:21] form of learning that the big labs are
[00:54:22] getting and it's that's obviously still
[00:54:23] really valuable to them, but I can't
[00:54:25] imagine a world in which we start off
[00:54:26] with like you know we're going to just
[00:54:28] like directly train this one big model
[00:54:30] on like all the exact data. I think it
[00:54:31] will definitely like go through stages
[00:54:33] cuz cuz I mean this is assuming there's
[00:54:34] like one discontinuous event whereas
[00:54:36] like suddenly we fix like weight updates
[00:54:37] continuously and like in practice I
[00:54:39] think it's much more likely to be like
[00:54:40] the cartridges and stuff allow you
[00:54:42] specialize in deployments then you
[00:54:43] generate traces you put that in your
[00:54:44] model like 3 months later you come out
[00:54:46] with a model which is better at this
[00:54:47] stuff you specialize it again and you
[00:54:48] like consolidate it again and then
[00:54:50] eventually we'll just like make this
[00:54:51] loop faster and faster so instead of
[00:54:53] like every 3 months we release a model
[00:54:54] now it's like every week and then every
[00:54:55] like day and then every hour in which
[00:54:57] point we basically have obviously solved
[00:54:58] it. Yeah, and I think this is a good
[00:55:00] point as well because um you asked like
[00:55:02] kind of how far off the current paradigm
[00:55:04] we are from being able to do this. I
[00:55:05] think like we've we've done a bit of
[00:55:06] research to this and people have done a
[00:55:08] lot of research like at a really large
[00:55:10] scale like when you wash out enough
[00:55:11] noise and you have large enough patches
[00:55:13] like this outer loop process of like
[00:55:15] putting data into mid training and
[00:55:16] creating our environments like it does
[00:55:17] work in like some sort of continual
[00:55:19] learning regime. But the problem is like
[00:55:20] when you zoom in close enough at like a
[00:55:22] micro level it's like I've got one model
[00:55:24] and I'm trying to update it again for
[00:55:25] like a law firm or something. Um, and
[00:55:27] I'm trying to do that very continuously
[00:55:29] like with a relatively small amount of
[00:55:30] data. Um, like all the methods kind of
[00:55:33] break down a bit. So like if I SFT the
[00:55:36] model on just like you know successful
[00:55:37] traces um off policy on policy like
[00:55:41] eventually in the very iterative regime
[00:55:43] like when you're doing like you know
[00:55:44] hundreds of these micro updates you see
[00:55:47] both catastrophic forgetting you see
[00:55:49] forgetting of like previous information
[00:55:50] I've learned on top of the base model
[00:55:51] that was much earlier on and I see
[00:55:53] degradation of general like use general
[00:55:56] capabilities um you know on policy
[00:55:58] distillation seems to like push this
[00:56:00] horizon out a little bit but it still
[00:56:02] eventually succumbs to the same
[00:56:04] Um and RL is not very good at like it it
[00:56:07] is good at like getting capabilities in
[00:56:09] but it's not as good as getting like
[00:56:10] knowledge in and like just this very
[00:56:12] explicit knowledge of like oh okay like
[00:56:13] this person does this at this law firm
[00:56:15] and like this is a very specific process
[00:56:16] we find and you have to pour in a lot of
[00:56:18] compute to create the right environments
[00:56:19] to get the the knowledge in
[00:56:21] >> do you think that the fundamental issue
[00:56:22] here why you get worse at any of these
[00:56:24] other skills or there's forgetting and
[00:56:26] stuff do you think it's fundamentally an
[00:56:27] issue of capacity or it's an issue of
[00:56:29] techniques
[00:56:30] >> uh a little bit of both I think like SFT
[00:56:32] and even like distillate like on policy
[00:56:34] distillation can be like way too
[00:56:36] destructive. Um like the reason RL is so
[00:56:39] nice is because like yeah it it changes
[00:56:42] a very very small amount about the model
[00:56:44] and there's like a lot of evidence for
[00:56:45] why this is the case and so like it kind
[00:56:47] of just like tweaks it in this very very
[00:56:49] very small like loss value to like get
[00:56:51] it into the right point. Um, but that
[00:56:53] also then limits what you can do with
[00:56:54] RL, like how much you can actually
[00:56:56] change the model.
[00:56:56] >> Or sorry, are you're saying like the
[00:56:58] reason this isn't a winner or take all
[00:56:59] potentially is that is just like very
[00:57:01] hard to distill that much information
[00:57:02] into the base model
[00:57:03] >> without ruining something in an
[00:57:05] interface. Like it's easy to distill it
[00:57:07] into like a different base model. Like
[00:57:08] this is where I think it's mostly
[00:57:09] technique. It's not like it's definitely
[00:57:11] not like just like there isn't capacity.
[00:57:13] Like if you had some model, you know,
[00:57:15] with all this data and you take like
[00:57:16] literally the same size model and
[00:57:17] pre-train it from scratch with like all
[00:57:18] of this stuff in mid training, it will
[00:57:19] be better. And I think that's a lot of
[00:57:20] what's happening today.
[00:57:21] >> Yeah. And so it's very much like
[00:57:22] there's, you know, a bottleneck that
[00:57:24] stops us from just keeping training the
[00:57:25] same model forever versus just like
[00:57:27] getting all the data from the old model
[00:57:28] and like training a new model from
[00:57:29] scratch. And this is exactly saying like
[00:57:31] some combination like plasticity and
[00:57:33] like catastrophically forgetting in that
[00:57:34] like you know if you just naively train
[00:57:37] on like non-stationary data because
[00:57:38] you're adding new data as you go
[00:57:39] basically this is messing with the data
[00:57:41] distribution. So like the old stuff is
[00:57:42] just forgotten and we don't really have
[00:57:44] good methods to like stop that from
[00:57:45] happening.
[00:57:45] >> And so maybe at the in the limit you're
[00:57:47] like just bottleneck by retraining the
[00:57:48] model from scratch with all this new
[00:57:50] information.
[00:57:50] >> Yes. which of course is like very
[00:57:52] expensive like training a model from
[00:57:53] scratch is is expensive
[00:57:54] >> but you're going to do that anyways and
[00:57:55] >> I mean not necessarily I mean like maybe
[00:57:57] eventually if you have continual
[00:57:58] learning you never train a new model you
[00:57:59] just like just have a model and it keeps
[00:58:01] learning and like expanding right
[00:58:02] >> but but there's there might be like some
[00:58:03] deep technical reason why that's very
[00:58:05] difficult because of these like
[00:58:06] >> I mean that's the question I think we
[00:58:08] have pushed back like how much from
[00:58:10] scratch we need to do like it is
[00:58:12] definitely possible now to take like the
[00:58:13] pre-trained base and like do very good
[00:58:15] mid training on top of that like kind of
[00:58:17] continuously plus some RL from like
[00:58:20] different checkpoints that are later on
[00:58:21] in the training and like that's looking
[00:58:22] more like a learning but certainly not
[00:58:24] the case of like you know take the most
[00:58:25] recent model apply a couple of very
[00:58:27] small updates and like iteratively like
[00:58:29] never lose it.
[00:58:29] >> So but isn't this like I'm a bit
[00:58:31] confused cuz isn't this literally what
[00:58:32] happens during training where during
[00:58:34] post training or something you just have
[00:58:35] like you have a model that's already
[00:58:36] gone through so much training and then
[00:58:38] you like distill some fork that's been
[00:58:41] further RL or something. Isn't Isn't
[00:58:43] that literally what happens? And like
[00:58:44] >> it's it's still at a large enough scale
[00:58:46] I think that you're washing out a lot of
[00:58:47] like the noise and like you're not just
[00:58:49] focused on one distribution which as
[00:58:50] Baron said is like you know that is now
[00:58:52] a very if you're just like focusing on
[00:58:54] one task right like that's I mean in the
[00:58:57] eventual regime you'd be doing I don't
[00:58:59] know there's billions of deployed
[00:59:00] instances you're like doing you're
[00:59:03] learning from all of them at once and so
[00:59:05] hopefully there's some washing out of
[00:59:07] noise and stuff from that right
[00:59:09] >> maybe that scale. Yeah.
[00:59:10] >> Yeah. I mean I think like definitely is
[00:59:12] as I was saying like you can do
[00:59:13] continual mid training for like a long
[00:59:15] time and you can like roll back to a
[00:59:16] checkpoint give a new mid training data
[00:59:18] >> but at the same time like you can't do
[00:59:19] this like indefinitely like if you just
[00:59:20] keep continue mid training the same base
[00:59:22] forever it just like get it does it's
[00:59:24] sort of asmmpto like you can't just
[00:59:26] learn new stuff in that base and this is
[00:59:28] why people end up training new bases
[00:59:29] like otherwise you would just keep m
[00:59:30] training the same base forever whenever
[00:59:32] I finish recording an interview I
[00:59:34] immediately brain dump all my thoughts
[00:59:35] into slack things like what was most
[00:59:37] interesting and what should get cut this
[00:59:39] ensures that my editors have all the
[00:59:40] context they need to start editing the
[00:59:42] episode. But it's not like these brain
[00:59:44] dumps have any clear timestamps and my
[00:59:46] unedited recordings are many hours long.
[00:59:48] It can take a ton of editor time to even
[00:59:51] find the exact moments that I was
[00:59:53] referencing. So, we decided to try
[00:59:54] adding a Grockbot producer to our chat.
[00:59:58] Now, whenever one of my editors post a
[00:59:59] rough cut of the episode, Grockbot opens
[01:00:02] a transcript on its own computer and
[01:00:03] starts working, usually before I've even
[01:00:05] seen the message. It takes the notes
[01:00:07] that I dropped into Slack and it
[01:00:08] highlights the relevant snippets in the
[01:00:09] transcript. It also uses a big case file
[01:00:11] that I've compiled with all my
[01:00:13] preferences so it can suggest potential
[01:00:15] edits. And when it's done, it sends me
[01:00:17] its top clip candidates so that I can
[01:00:18] review everything from my phone. This
[01:00:20] has worked really well. Being able to
[01:00:22] send informal messages like I'm texting
[01:00:24] my editor and then having the transcript
[01:00:26] immediately reflect my preferences has
[01:00:28] just been so helpful. Try Grockbot
[01:00:30] yourself at x.ai/bot.
[01:00:33] Okay, let's talk a bit about data now.
[01:00:36] So, I'm generally interested in this
[01:00:38] question of how much of AI progress is
[01:00:39] just explained by data progress. Um,
[01:00:42] doesn't mean it will be necessarily hard
[01:00:43] to automate, but that's a separate
[01:00:45] question. So, is there some data
[01:00:48] distribution which if you trained
[01:00:50] current architectures on would result in
[01:00:54] a super intelligence that totally
[01:00:56] dominates human experts across every
[01:00:57] single field.
[01:00:58] >> Are we talking about like pre-training
[01:01:00] plus post- training data like
[01:01:01] environments as well?
[01:01:03] Like I think the existence of this is
[01:01:04] obvious. It's just like whether we can
[01:01:06] create the right environments.
[01:01:08] >> Yeah.
[01:01:08] >> In the trivial case, we could just train
[01:01:09] it to output the Python file which like
[01:01:11] trains the actual super intelligence
[01:01:12] like just have that memorizing the
[01:01:13] weights.
[01:01:14] >> Like yes, there's probably like a ladder
[01:01:16] of oral environments that is possible to
[01:01:19] construct such that you would get a AI
[01:01:22] researcher which is at least as good as
[01:01:24] a human researcher. But the effort to
[01:01:27] climb each successive rung grows like
[01:01:30] kind of exponentially. Um, and that's
[01:01:33] going to be the two things that you have
[01:01:34] to trade off against as to whether like
[01:01:36] like how fast we're going to hit like
[01:01:38] that final run where it's where it's
[01:01:39] better. Um, I think that's fairly clear
[01:01:41] and I think there's like, you know,
[01:01:42] we're still relatively early in like our
[01:01:45] environment creation. Like there's a lot
[01:01:46] of asymmetries that we exploit in order
[01:01:48] to create good environments. So, one of
[01:01:50] those asymmetries which we've talked
[01:01:51] about before is like it's there's
[01:01:54] environments where it's easier to go
[01:01:55] backwards and forwards. And like what I
[01:01:57] mean by that is like it's very easy to
[01:01:59] define this like complex data generating
[01:02:00] process. And this is like this kind of
[01:02:02] latent variable you keep hidden from the
[01:02:03] model. Um you can generate like
[01:02:05] arbitrarily complex like environments
[01:02:07] and the model has to do a lot of like
[01:02:08] irreducible like token spend and
[01:02:10] irreducible work to figure out what that
[01:02:12] data generating process was. Um there's
[01:02:14] asymmetries in terms of like you know
[01:02:16] you can inject information from the real
[01:02:17] world. So like anthropic finds a bug um
[01:02:20] through like you know tens of thousands
[01:02:21] of human and LMR hours combined and like
[01:02:23] turn that into a very very neat
[01:02:25] environment which a single LM could
[01:02:26] theoretically find within like you know
[01:02:28] a few million tokens. So like there's
[01:02:30] all these asymmetries which we're
[01:02:31] cherrypicking and like we're counting on
[01:02:33] like kind of this task horizon
[01:02:34] generalization. Um but I think yeah
[01:02:37] again there's just going to hit
[01:02:38] diminishing returns at some point like
[01:02:39] at some point diminishing returns and
[01:02:41] how hard it is to create those
[01:02:42] environments in the first place like
[01:02:43] coming up with them because you can't
[01:02:45] necessarily just like have these really
[01:02:47] like these processes where it's easier
[01:02:49] to go backwards than forwards like you
[01:02:50] actually have to sit down and construct
[01:02:52] like something that looks like with
[01:02:54] humans like you know a long enough time
[01:02:55] horizon like it's going to be a really
[01:02:57] complex task to create. Um, and then
[01:02:59] there's also going to be like the
[01:03:00] compute and time bottlenecks for the
[01:03:01] agent to actually do those tasks. Um, so
[01:03:04] like I think you're just going to start
[01:03:05] seeing this like curve to flatten out.
[01:03:07] >> I saw something about how someone
[01:03:08] fine-tuned the talkie model uh which is
[01:03:11] only trained on data up to 1930 on this
[01:03:14] uh like modern coding agent data and um
[01:03:18] and it did better than claude 3 opus on
[01:03:21] on Sweepbench. Um so so this model that
[01:03:24] has uh like no knowledge of code
[01:03:26] whatsoever can be fine-tuned on a
[01:03:28] moderate amount of data and uh like
[01:03:31] behave better as as a coding agent than
[01:03:33] this much larger pre-trained model is
[01:03:35] pretty crazy. And it kind of shows you
[01:03:37] that like once you have an example of uh
[01:03:40] like the right expert behavior, it's
[01:03:42] actually surprisingly easy to like copy
[01:03:44] that into a like relatively weak model.
[01:03:48] >> Yeah. But a counter example to like that
[01:03:50] kind of is the there was a paper
[01:03:52] recently where they trained it up to
[01:03:53] like fifth grade maths.
[01:03:54] >> Um and like also like primary school
[01:03:56] like English and stuff. So it was like a
[01:03:58] decent language model and they tried to
[01:04:00] RL it to do like you know late high
[01:04:02] school and college maths and the gap was
[01:04:03] just too large. Like they couldn't get
[01:04:05] it to climb at all. Like but if you did
[01:04:07] like successive runs of like you know
[01:04:08] your seven maths and then year eight
[01:04:09] maths and so on like you could obviously
[01:04:12] climb to to year 12. So like again it's
[01:04:14] just like what is the distance between
[01:04:15] the rungs on those ladders and how hard
[01:04:17] is it to create?
[01:04:18] >> Yeah. And this just comes back to like
[01:04:19] the RL signal problem. Like RL is not
[01:04:21] very good at like exploring right now.
[01:04:22] And so if you if the model can't like
[01:04:24] get in like you know 128 rollouts it's
[01:04:26] very unlikely to get signal to like
[01:04:28] progress. And this is why like in RL we
[01:04:29] need like curricular whereas like in
[01:04:31] pre-training we don't because like it's
[01:04:32] that's not a problem for pre-training at
[01:04:34] all.
[01:04:34] >> Yeah. And and again, pre-training data
[01:04:36] is different to post-training data.
[01:04:39] >> And I imagine as we continue on, like
[01:04:41] yeah, humans will be involved less and
[01:04:43] less, but that doesn't change the fact
[01:04:44] that you're bottlenecked on like how
[01:04:46] much signal you can extract from the the
[01:04:48] real world. So like there's a lot of
[01:04:50] signal in the world and that's true like
[01:04:51] you know there's people doing like
[01:04:53] spreadsheet tasks, there's people doing
[01:04:54] like legal tasks and all this sort of
[01:04:56] stuff, but you know the capability
[01:04:58] frontier of where the models are at now.
[01:05:00] like how many bits in the world are
[01:05:02] actually like really relevant to like
[01:05:04] improving the the model's capabilities
[01:05:06] like you know how many new maths
[01:05:07] problems are being solved that like
[01:05:08] couldn't that are just beyond the reach
[01:05:10] or grasp of the current models like how
[01:05:12] many new coding problems are being
[01:05:13] created or or solved that are beyond the
[01:05:14] reach of the current models and like I
[01:05:16] think that's why the diminishing returns
[01:05:17] kicks in cuz like even the world as a
[01:05:19] whole is not giving you the bits that
[01:05:21] are useful for tipping you into the next
[01:05:22] like basin of of capability.
[01:05:25] >> Yeah, I I totally agree with this. So
[01:05:26] it's like really a question of like
[01:05:27] where the signal is coming from and so
[01:05:29] like the signal doesn't you know in
[01:05:31] pre-training the signal is like already
[01:05:32] in common core right like for the tasks
[01:05:34] that you care about in pre-training the
[01:05:36] problem is it's not just like getting
[01:05:37] signal at all it's like filtering out
[01:05:39] all the noise that exists and that's
[01:05:40] quite an automatable process but like as
[01:05:42] the models get better as we enter mid-
[01:05:44] training and post- training the signal
[01:05:45] just like doesn't exist anywhere in the
[01:05:47] original data we have like no amount of
[01:05:48] filtering will like get this you know
[01:05:50] there's no like hidden proof of like the
[01:05:52] millennium prize problem sitting in
[01:05:53] common core we can just like filter
[01:05:54] until we see it And so like at that
[01:05:56] point you have to get bits some other
[01:05:58] way either from humans like directly
[01:05:59] like asking them to like write out their
[01:06:01] reasoning or like by like creating
[01:06:03] environment where like humans decide
[01:06:04] like what environment should be created
[01:06:05] what the objectives of these
[01:06:06] environments are or like you know some
[01:06:08] kind of like training on like the human
[01:06:10] data that exists in deployment like you
[01:06:12] have to get the bits from somewhere.
[01:06:13] >> Yeah. Yeah. There's a question of how
[01:06:15] much of the progress in pre-raining is
[01:06:16] being driven by data. Y
[01:06:18] >> I I did this investigation with um Jerry
[01:06:20] Han who's a student at Princeton where
[01:06:22] we basically trained all the recipes
[01:06:26] from 2019 till now pairwise with all the
[01:06:30] data sets from 2019 to now. So you train
[01:06:31] like GPT2 on the newest data set like
[01:06:34] ultra fine web and you train deli which
[01:06:37] is the newest training recipe or the
[01:06:38] open source training recipe on like the
[01:06:40] pile or some old data set and you do
[01:06:42] like the whole grid and you see the
[01:06:46] getting to some level of capabilities.
[01:06:49] How much less compute does it take
[01:06:50] across this grid? And you see that the
[01:06:54] the data seems to explain like 9x of a
[01:06:57] compute efficiency gain. Uh but the the
[01:06:59] architecture improvements explains like
[01:07:00] a 3x computer efficiency gain at a very
[01:07:02] small scale. Um and so to the extent
[01:07:05] that that is true at large scale that
[01:07:07] most of the pre-training computer
[01:07:08] efficiency gains are coming from better
[01:07:10] data how much can that continue like can
[01:07:13] you keep just filtering data more and
[01:07:15] more and building more and more
[01:07:16] synthetic data until yeah do you have a
[01:07:19] sense of how much this kind of
[01:07:20] pre-training progress can continue? I
[01:07:22] think my my prior is that like again the
[01:07:26] low hanging fruit is like somewhat
[01:07:27] exhausted with like we got the internet
[01:07:29] as this big block and like there's it's
[01:07:32] not like the internet is necessarily
[01:07:34] like growing at the same like rate. All
[01:07:36] the useful stuff on the internet is
[01:07:37] growing at the same rate. So like we've
[01:07:39] probably got like a bunch of like.1%
[01:07:40] loss drops to go but like not definitely
[01:07:42] not as many as have currently occurred.
[01:07:44] >> But like that's also really interesting
[01:07:46] that like you know you find this like
[01:07:47] what cumulative like 27 times
[01:07:49] improvement across both. I think like it
[01:07:52] was epoch or someone who estimated like
[01:07:54] three times a year since 2019 which
[01:07:56] would imply something like you know 3 to
[01:07:58] the 7 like over 2,000
[01:08:00] >> like times improvement. So like where's
[01:08:02] that missing you know 100 times or
[01:08:04] whatever coming from like that probably
[01:08:05] gives you a good signal of like how much
[01:08:06] is this is like post training. I think
[01:08:09] the explanation has to be that a lot of
[01:08:11] the comput efficiency gains are scale
[01:08:13] dependent and we're studying at
[01:08:15] extremely small scale
[01:08:16] >> and that raises the question of do the
[01:08:19] data comput efficiency gains or the
[01:08:22] algorithmic comput efficiency gains have
[01:08:24] more scale dependence I don't know if
[01:08:26] you guys are prior on that we just
[01:08:27] didn't have enough computer to
[01:08:28] investigate that question
[01:08:29] >> I mean like just naively right like the
[01:08:31] theoretically the scale dependence of
[01:08:33] the architecture is like fairly wellnown
[01:08:36] >> and like you can fit a straight line to
[01:08:38] Whereas like I would have no idea how to
[01:08:40] do that for like combining pre-training
[01:08:42] plus post- training data and
[01:08:43] mid-training data.
[01:08:44] >> Funny enough, I feel like data is
[01:08:46] actually more like more important with
[01:08:47] scale. Like I feel like architectures
[01:08:49] are kind of like a one time like you
[01:08:50] know an architect I think like combining
[01:08:52] like saying just like an x% efficiency
[01:08:54] gain is kind of misleading because like
[01:08:56] what an architecture does is like let
[01:08:57] you reach like a qualitatively new
[01:08:59] regime which you couldn't reach with the
[01:09:00] old architecture and then within that
[01:09:01] regime obviously the data is like the
[01:09:03] primary thing determining it but like
[01:09:05] you know if we say didn't have like even
[01:09:06] like GQA we're doing like full attention
[01:09:08] all day we wouldn't be able to do like a
[01:09:09] million it would be like ridiculous
[01:09:10] expenses to do a million context and
[01:09:12] then like because of that we couldn't we
[01:09:14] could never use the data which is like
[01:09:15] actually at a million context and so we
[01:09:17] couldn't get these capabilities even
[01:09:18] though like if you just do a naive like
[01:09:20] how much does this do at like 2k context
[01:09:22] where the architecture isn't unlocking
[01:09:23] anything then like the data you know
[01:09:25] that will look much more important than
[01:09:26] in some sense it is right it's unclear
[01:09:28] to me that these things are like really
[01:09:29] just like multiplicative gains in this
[01:09:31] way
[01:09:32] >> I see so but then what is the take away
[01:09:34] for the scale dependence of data
[01:09:36] >> so I mean on scale dependence I think
[01:09:38] like a lot of the like mid-training and
[01:09:41] post- training data we have now is like
[01:09:42] actually gets better with scale cuz like
[01:09:44] a lot of it like the very long context
[01:09:46] horizon environment really requires like
[01:09:48] big models to be able to like make use
[01:09:49] of them.
[01:09:49] >> Yeah.
[01:09:50] >> And like this is not, you know, if you
[01:09:51] try and train like your 100 million
[01:09:52] parameter model on like three bench
[01:09:54] traces. It's not going to get anywhere.
[01:09:55] Like it's not going to show you the same
[01:09:57] kind of improvement that you would get
[01:09:58] if you train like an actual sensible
[01:10:00] size model on it.
[01:10:00] >> Yeah.
[01:10:01] >> Yeah. And like it's hard as well now
[01:10:02] because so many of the architecture
[01:10:03] changes like you look at like Kimmy for
[01:10:05] instance like or DeepSeek, they're doing
[01:10:08] these architectural modifications with
[01:10:10] not just like dropping the pre-training
[01:10:11] loss in mind but like for instance how
[01:10:13] the models are going to be used in the
[01:10:14] real world. like the inference
[01:10:16] efficiency like having some form of
[01:10:17] compressed attention in the deepse
[01:10:18] models is not necessarily geared around
[01:10:21] you know this is fundamentally like a
[01:10:22] improvement it's just like okay we're
[01:10:24] considering how the models are going to
[01:10:25] be used
[01:10:26] >> right right what one question I'm
[01:10:27] curious about to understand the future
[01:10:28] is how parameter scaling will go as
[01:10:31] we're getting into more of a RL heavy
[01:10:33] regime like I don't know I don't know
[01:10:35] how fast historically yeah you can look
[01:10:37] at sort of opensource architectures and
[01:10:39] see how fast parameters have been
[01:10:41] scaling and maybe it's like roughly 2x
[01:10:43] every for frontier open source models
[01:10:46] and to the extent that like even
[01:10:47] frontier closed source models have like
[01:10:49] 100b or 200b active parameters. Do you
[01:10:52] think that like keeps 2xing year over
[01:10:53] year or now that we're in an RL regime
[01:10:55] where you also want to conserve compute
[01:10:57] on um rollouts that and also maybe there
[01:11:00] is like a threshold effect where you
[01:11:01] have enough capacity and at the point
[01:11:03] does increasing parameters arbitrarily
[01:11:05] doesn't matter as much. Do you guys have
[01:11:06] a sense of in 2030 how many active
[01:11:08] parameters will a frontier model have?
[01:11:10] Yeah, I think for the next few years
[01:11:12] we're going to be like like because
[01:11:14] we're so focused on doing longer and
[01:11:16] longer horizon rollouts for RL where
[01:11:18] like inference efficiency ma matters a
[01:11:20] lot. Um it feels like the the malls
[01:11:23] aren't necessarily saturated on their
[01:11:24] ability to do that where the bottleneck
[01:11:25] is still the environments and so we
[01:11:27] might see like a little bit of plateau
[01:11:29] like I I I have a feeling that you know
[01:11:30] like mythos and and the GPG models are
[01:11:33] much smaller than like you know the 10
[01:11:35] trillion parameter range that that
[01:11:36] people are talking about. um even just
[01:11:38] naively comparing them to open source
[01:11:40] models, you can probably back out that
[01:11:41] conclusion.
[01:11:42] >> Um so yeah, probably for the next few
[01:11:44] years I wouldn't imagine a huge growth
[01:11:46] in the number of parameters, but again
[01:11:48] like there's so many different different
[01:11:49] things to trade-off here. Like you
[01:11:51] decide the size of your model based on
[01:11:53] like how much pre-training data you have
[01:11:55] and then like the difficulty of the RL
[01:11:57] environments that you've got to train
[01:11:58] on. And you ideally want to like get to
[01:12:00] the optimal point where you know you can
[01:12:02] get like a decent pass at one or
[01:12:04] something on like the the hardest
[01:12:05] environments you have and like it
[01:12:07] wouldn't make sense to like make a big
[01:12:08] bigger model pass there because then
[01:12:09] you're just paying like much more
[01:12:10] inference flop than you need to. Um so
[01:12:13] there's there's a lot of input to this
[01:12:14] like depends on how quickly you know
[01:12:15] like Mccor and then inhouse these these
[01:12:17] guys can scale up the complexity of the
[01:12:19] oral environments they're training on.
[01:12:20] >> I would expect the models to keep
[01:12:22] getting bigger just because people are
[01:12:23] scaling up compute and the GPUs are
[01:12:25] getting bigger. But I would say exactly
[01:12:28] how much they get bigger depends a bit
[01:12:30] on the scaling laws in non-obvious ways.
[01:12:33] So one thing is that I think um like
[01:12:35] data efficiency is going to be a bigger
[01:12:37] driver than compute efficiency of uh
[01:12:40] like the exact architectures people use
[01:12:42] uh now that we're getting to the uh
[01:12:45] regime where we're sort of running low
[01:12:47] on um like high quality pre-training
[01:12:49] data. So that might affect how sparse
[01:12:51] you want to make the model. And then I
[01:12:53] also think we don't uh understand
[01:12:56] sparsity that well
[01:12:57] >> and it's like parameters are a different
[01:12:59] resource than active parameters but it's
[01:13:02] uh and um like sparsity uh has um
[01:13:07] definitely increased a bit but it's not
[01:13:08] clear that it's going to keep increasing
[01:13:10] without bound. There might be some kind
[01:13:12] of sweet spot.
[01:13:13] >> There's an argument that sparity should
[01:13:15] u make data efficiency worse because you
[01:13:18] might have to learn the same thing on
[01:13:19] multiple experts.
[01:13:21] uh though that's debatable. So I think
[01:13:24] we don't um I don't think we we have a
[01:13:27] good enough theory of scaling laws that
[01:13:29] we we really understand why sparity is
[01:13:32] helping and to what ex how much it'll
[01:13:34] help and if that'll uh like plateau at
[01:13:36] some point at a certain level of sparity
[01:13:38] and
[01:13:38] >> sorry can you spell out exactly what the
[01:13:40] implication of uh data efficiency would
[01:13:42] be on so it sounds like you'd say well
[01:13:45] it should there should be less sparity
[01:13:46] but what are the other implications on
[01:13:48] parameter scaling? I guess uh just that
[01:13:50] the scaling law you're you're not
[01:13:52] necessarily looking for the most uh
[01:13:54] you're not trying to optimize compute
[01:13:55] efficiency. So you have all your um
[01:13:57] choices you can make on the architecture
[01:13:59] and uh each of these gives you a
[01:14:01] different scaling law and then like
[01:14:03] traditionally you would look at some
[01:14:04] kind of envelope based on compute. Uh so
[01:14:06] you would look at performance versus
[01:14:08] compute and take the envelope of uh like
[01:14:11] the yeah uh the best models. Uh but uh
[01:14:16] like if if we're making that decision
[01:14:18] based on um data so it's like uh yeah
[01:14:20] we're sort of assuming we can um spend a
[01:14:23] lot of compute um and uh like we're sort
[01:14:27] of data is on our x-axis um instead of
[01:14:30] uh instead of compute uh then we just
[01:14:33] get a different um set of optima or a
[01:14:37] different set of models that are on that
[01:14:38] frontier.
[01:14:38] >> Yeah. And I also don't think that we've
[01:14:41] necessarily like you know doubled like
[01:14:43] the size of the models every year for
[01:14:45] the last few years. Like the people have
[01:14:48] been training like one trillion
[01:14:49] parameter models for at least a few
[01:14:50] years. Like there was even an open
[01:14:51] source one called Falcon. But like Liam
[01:14:53] from Periodic Labs like I think post
[01:14:54] yesterday on Twitter about how like an
[01:14:56] early experiment at OpenAI was like
[01:14:58] training a one trillion parameter model
[01:14:59] that was very very sparse.
[01:15:00] >> Oh yeah. That was what they did before
[01:15:02] open AAI that was like at Google the
[01:15:04] switch. Yeah. So like it was like um you
[01:15:07] know very very good at like knowledge
[01:15:09] but terrible at reasoning cuz it was so
[01:15:11] sparse and so like yeah it feels like
[01:15:13] we've been playing in this like 100
[01:15:15] billion to you know up to two trillion
[01:15:17] parameter range for like at least a
[01:15:18] little bit and like it certainly hasn't
[01:15:19] been. This is like nice linear increase.
[01:15:21] Yeah I mean I feel like there's two
[01:15:23] things. So as as Charlie was saying like
[01:15:24] inference efficiency is super important
[01:15:26] for RL rollouts and so like this will
[01:15:28] really push down active parameters quite
[01:15:30] a lot and then I think the total
[01:15:32] parameters really depends a lot on the
[01:15:33] hardware as well. So like you really
[01:15:35] need to get like very high memory
[01:15:37] bandwidth and like VRAM size to like
[01:15:38] actually be able to serve like multi-
[01:15:40] trillion parameter models. And so like
[01:15:41] you know right now you people still
[01:15:43] using a lot of like H100s and stuff and
[01:15:44] so as everyone moves to GBs and then V
[01:15:46] Rubins will get like more actual like
[01:15:49] the ability to scale and like actually
[01:15:50] serve and like do like large RL inputs
[01:15:52] at like different at larger scales. The
[01:15:54] data crush I think is interesting
[01:15:56] because naively like larger models are
[01:15:58] much more sample efficient in like the
[01:15:59] actual data points and so like even if
[01:16:01] you're like not saturating the model
[01:16:02] it's still better to go bigger because
[01:16:04] like the models larger models generalize
[01:16:06] better and like get to a better loss for
[01:16:07] the same amount of data and so right now
[01:16:09] I think we kind of have a lot of data
[01:16:11] and like that's not the constraint
[01:16:13] rather than computing and so we're
[01:16:14] having like small models which are like
[01:16:15] very inference efficient but if
[01:16:16] computers no longer the bottleneck it
[01:16:18] might come back to larger models which
[01:16:19] are like un sort of undersaturated but
[01:16:21] like they have this generalization
[01:16:23] ability because they're larger
[01:16:25] >> if if you just look at like the basic
[01:16:27] chinchilla scaling law and you just
[01:16:29] maximize out uh parameters.
[01:16:32] >> Yeah.
[01:16:32] >> It actually decreases the amount of data
[01:16:34] you need to get to the same loss very
[01:16:35] little.
[01:16:36] >> Yes. If you go to infinity on
[01:16:38] parameters, the amount of data you need,
[01:16:39] I think goes down less than 10x just
[01:16:41] because the nature of like the power
[01:16:43] >> we're now on the way too much data side
[01:16:45] of the chinchilla laws, right? So right
[01:16:47] now we overtrain models according to
[01:16:48] chill and so we could easily go back to
[01:16:49] a point to which as we're running out of
[01:16:51] data, we move back to like the
[01:16:52] chinchilla optimal point or even like a
[01:16:54] bit on the overtraining like you know
[01:16:56] undertraining model side. But surely
[01:16:57] like even with these new chips that come
[01:16:59] online and stuff like we're just going
[01:17:01] to be so comput bottlenecked for the
[01:17:02] next few years that that won't
[01:17:03] necessarily
[01:17:03] >> I mean this could well yeah this depends
[01:17:05] on like the ratio you with like training
[01:17:06] and inference comput really. It's like
[01:17:07] if you're super bottl necked on data not
[01:17:09] on compute you should go bigger. If
[01:17:11] you're super bottlenecked on compute you
[01:17:12] should always go smaller and then like
[01:17:14] yeah but you can also use computer to
[01:17:16] generate synthetic data. So it's like
[01:17:17] one of these very hard things to
[01:17:19] predict.
[01:17:19] >> Yeah. I think uh part of the reason it
[01:17:21] took people so long to figure out the
[01:17:23] scaling laws in the first place was that
[01:17:24] if you don't get all these things right
[01:17:26] then you don't get such a clean
[01:17:28] relationship and like the uh the
[01:17:31] beautiful stray lines on graphs like
[01:17:33] hide a lot of complexity on uh how you
[01:17:35] have to make sure every like to scale
[01:17:37] every hyperparameter the right way or
[01:17:39] like parameterize your optimizer in a
[01:17:41] way that um scales and where you don't
[01:17:44] have to change your hyperparameters as
[01:17:45] you change the model size
[01:17:47] >> and and bugs have their own clean
[01:17:48] scaling laws as well, right? Like you
[01:17:50] know like with Kaplan forgetting the
[01:17:52] cosine and thing or like even just like
[01:17:54] not considering embedding parameters I
[01:17:55] think and so that messed up the estimate
[01:17:58] at smaller models because embedding
[01:18:00] parameters are a decent size of the
[01:18:01] model.
[01:18:02] >> Uh a bit on RL. So I feel like a year
[01:18:07] ago a lot of people were making this
[01:18:08] argument that RL will not be super
[01:18:12] successful at scaling for models. I
[01:18:14] think John you wrote a research paper
[01:18:16] where you were pointing out that models
[01:18:18] learn one bit per episode when you RL
[01:18:21] basically learn did I get the answer
[01:18:22] right or did I get it wrong and I wrote
[01:18:25] some blog post earlier this year I was
[01:18:26] like it's even worse than that cuz when
[01:18:27] the pass rate is low when the model is
[01:18:29] very unlikely to get the answer right
[01:18:30] it's it learns almost almost nothing at
[01:18:33] all from an RL episode but we I look at
[01:18:36] the models today and they seem pretty
[01:18:38] smart and it seems to be the result of
[01:18:40] scaling up RL Baron you had a post I
[01:18:42] think a few weeks ago where you're
[01:18:43] trying to explain what's going on. But
[01:18:45] why has RL been more successful than one
[01:18:48] would have naively thought?
[01:18:50] >> I mean, so I think the success of RL
[01:18:52] comes down to a bunch of different
[01:18:53] things. So first, I think what is
[01:18:55] slightly underestimated is actually the
[01:18:57] mid-raining. So an awful lot of like
[01:18:58] what we see as successes of RL actually
[01:19:00] comes from like very very good
[01:19:01] mid-training data, which is basically
[01:19:03] where we're like essentially doing
[01:19:04] pre-training but on like synthetic
[01:19:06] reasoning data and like the kind of
[01:19:08] environments that like get the model
[01:19:09] warm started for RL. And so this
[01:19:10] actually takes the model like almost
[01:19:12] like 80% of the way to like the final RL
[01:19:14] checkpoint often. And then what RL does
[01:19:16] on top of that is it does like a lot of
[01:19:18] you know essentially tweaking to the
[01:19:19] policy. And so this is one of the
[01:19:21] reasons why it doesn't need like as many
[01:19:22] bits as you would naively think. It
[01:19:24] doesn't have to learn all of these
[01:19:25] behaviors from scratch. It needs just
[01:19:27] like a few bits from these episodes
[01:19:28] which you do get. And then the other
[01:19:30] thing that I really point out in my blog
[01:19:32] is that these bits are actually
[01:19:33] extremely high signal compared to like
[01:19:35] regular like pre-training which is why
[01:19:36] you need RL at all versus just like
[01:19:38] SFTing on like successful reasoning
[01:19:40] traces
[01:19:40] >> because it's exactly the bits about how
[01:19:43] to get the answer right.
[01:19:44] >> Well, there's two things. So yes, one,
[01:19:45] it's exactly the bits about how to get
[01:19:46] the answer right. But like this is not
[01:19:48] exactly how you think of it because in
[01:19:51] SFT you have a trace, right? You have
[01:19:52] like a bunch of math reasoning and then
[01:19:54] the answer at the end. The bit is still
[01:19:55] there. Like you still SFT on the answer
[01:19:57] token. So that bit is still there.
[01:19:58] What's important is that the objective
[01:20:00] ignores all the other bits. So in SFT
[01:20:02] you like have like you know to try and
[01:20:04] match like the exact reasoning tokens
[01:20:05] that the model produces. So you're
[01:20:07] essentially getting like too many bits
[01:20:09] about like the exact way this other
[01:20:10] model you're training on reasons. For RL
[01:20:12] you only get the one bit and that means
[01:20:14] that like this it that signal is not
[01:20:16] drowned out in the noise of like all the
[01:20:17] other bits the model has. And so that's
[01:20:19] what really like it's really super
[01:20:21] dramatic like increasing to the signal
[01:20:22] to noise ratio during training which is
[01:20:24] why like RL is like so dramatically
[01:20:26] efficient in terms of steps.
[01:20:28] I don't know if you guys have thoughts
[01:20:29] on that.
[01:20:30] >> Yeah, I like there there's been so much
[01:20:32] debate about like what RL does to the
[01:20:33] model versus like you know mid-training
[01:20:35] or SFT or whatever. And like you know
[01:20:38] everyone talks about how you know passer
[01:20:39] one will go up but pass 256 will go down
[01:20:42] like very rare correct reasoning traces
[01:20:43] will be like down weighted and kind of
[01:20:45] like outweighed by gradient signal from
[01:20:47] like easier kind of reasoning traces.
[01:20:49] And I I think the simple like way to
[01:20:51] view RL now is that if you have a large
[01:20:53] enough like a large enough amount of
[01:20:55] compute to sample a large enough group
[01:20:57] size such that your probability of
[01:20:59] getting a bunch of correct answers is
[01:21:01] like past some like not insignificant
[01:21:03] probability then like it will be upweed
[01:21:06] and like to to to Von's point like
[01:21:08] basically mid-training and you know more
[01:21:10] pre-training like the the pass at one
[01:21:13] the starting point for RL like scales in
[01:21:15] a log number of pre-training tokens.
[01:21:17] >> You can ask some very basic questions.
[01:21:18] Um I I I guess that answer makes sense
[01:21:21] and maybe there's empirical research
[01:21:24] which shows that this is what's
[01:21:25] happening but then I just look at the
[01:21:28] models themselves and I don't know
[01:21:30] what's happened like yeah maybe you can
[01:21:33] give me a sense of what is the basis of
[01:21:34] the AI progress over the last year but
[01:21:37] if if it's yeah maybe it's just upweing
[01:21:41] the uh the policies which were going to
[01:21:44] do the correct thinking anyways but it
[01:21:46] just seems like qualitatively the models
[01:21:48] have gotten so much more capable and
[01:21:52] anyways maybe there's no nothing to
[01:21:54] there's no inherent contradiction there
[01:21:56] but how do we square square like the
[01:21:58] relatively small impact this take would
[01:22:01] imply that RL would have from the actual
[01:22:03] qualitative capabilities the model seem
[01:22:05] to be gaining
[01:22:06] >> so like one thing I want to point out
[01:22:07] here is that like it doesn't necessarily
[01:22:08] imply that RL has a small like effect
[01:22:11] right even if you have a few bits and
[01:22:12] like you only change the parameters a
[01:22:13] small amount like the actual impact on
[01:22:15] like function space the model like the
[01:22:17] input output mapping can still be like
[01:22:18] super dramatic.
[01:22:19] >> You know, even if it's like even like
[01:22:20] one bit can change like your function
[01:22:22] space a lot and that it can like rule
[01:22:23] out like half the hypothesis space which
[01:22:25] is huge. So like I don't think it's
[01:22:26] necessarily the case like small amounts
[01:22:28] of bits, small amounts of RL once you're
[01:22:29] starting from a really good point means
[01:22:31] that like you don't have dramatic
[01:22:32] impacts in behavior at least like not
[01:22:34] necessarily.
[01:22:35] >> I I think it comes down to two things.
[01:22:36] cuz I think the first thing is that
[01:22:38] everyone was hoping that RL would like
[01:22:40] generalize this reasoning across like
[01:22:41] all these different domains and I don't
[01:22:43] think we necessarily got this like
[01:22:44] horizontal generalization like just
[01:22:46] training on math doesn't necessarily
[01:22:48] make you the greatest coder like you do
[01:22:49] have to do RL on on code environments. I
[01:22:52] think what we did get though is like
[01:22:53] horizon generalization.
[01:22:55] >> Um like the models just learned how to
[01:22:57] use more tokens for for longer and still
[01:23:00] make progress on some sort of task. And
[01:23:02] so like you can train on environments
[01:23:03] where they get longer and longer and
[01:23:05] longer and then put them into a
[01:23:06] completely new environment and yes like
[01:23:08] they may not have generalized the
[01:23:09] reasoning patterns which allow them to
[01:23:10] do well in that environment but they've
[01:23:11] at least generalized the ability to like
[01:23:13] continue on that task for longer which
[01:23:14] is correlated with like success. I think
[01:23:16] like there's a paper called edgebench
[01:23:18] which showed that the rate at which
[01:23:19] models can work for longer is like
[01:23:21] doubling every 3 months. And so that's a
[01:23:23] clear evidence of generalization. And I
[01:23:25] think like the the final way to think
[01:23:26] about it is like um in pre-training
[01:23:29] there's this idea of like quanta. So you
[01:23:31] have this very smooth like pre-training
[01:23:33] loss curve.
[01:23:34] >> And when you actually look at what's
[01:23:35] happening in the model like the model is
[01:23:37] learning all these like very discreet
[01:23:38] like tasks and there's like all these
[01:23:40] like emergent points where there's like
[01:23:42] kind of a phase transition like it
[01:23:43] didn't have induction heads now it has
[01:23:45] induction heads and there's like tens of
[01:23:47] thousands millions probably like
[01:23:48] hundreds of millions of these things and
[01:23:50] you average them all together and you
[01:23:51] get this very like smooth loss curve. I
[01:23:53] think like to a to an extent like a
[01:23:55] similar thing is happening happening for
[01:23:56] RL like there is this very slow ad loop
[01:23:58] as Baron mentioned of you know we will
[01:24:00] train a model and then RL it and then
[01:24:02] like the next kind of model iteration of
[01:24:05] training we will dump a bunch of these
[01:24:06] synthetic reasoning traces into the mid
[01:24:08] training data like we're kind of hitting
[01:24:10] all these quanta for all these different
[01:24:11] tasks and like on an individual task
[01:24:13] level it may look like a phase
[01:24:15] transition and like you're suddenly
[01:24:16] going from like a.5% pass rate to a 90%
[01:24:19] pass rate on like a particular like
[01:24:21] finance task or Excel task. ask or
[01:24:22] whatever, but you average all these
[01:24:23] things together and plus the horizon
[01:24:25] generalization, you kind of will go,
[01:24:27] wow, we've got like qualitatively better
[01:24:29] models.
[01:24:30] >> Yeah. I mean, I think a lot of this as
[01:24:31] well is just like I think RL does
[01:24:33] generalize a bit like suddenly you get
[01:24:34] like some transfer between like math and
[01:24:36] code or like puzzles and math and this
[01:24:37] kind of stuff. Also just like the amount
[01:24:39] the sheer amount of environments I think
[01:24:40] the people are targeting is just like
[01:24:42] vastly greater. So like you know before
[01:24:44] when you try to do you know some task
[01:24:46] which like you do in your daily life
[01:24:47] like two years ago like the labs
[01:24:48] wouldn't really care about this. they
[01:24:49] wouldn't like train the model for it and
[01:24:50] now like it's just so much broader. They
[01:24:52] have a lot of environments targeting
[01:24:53] this specific thing.
[01:24:55] >> Early in the conversation we're talking
[01:24:56] about are all in the context of causing
[01:24:57] this entropy collapse or just you know
[01:25:00] concentrating probability on solutions
[01:25:02] the base model were already done. Um and
[01:25:05] causing relatively sparse updates in the
[01:25:06] policy. Um, but when I think like when I
[01:25:09] think about
[01:25:11] I think the there's also another story
[01:25:14] about RL which is going back to the
[01:25:16] Atari games and then AlphaGo coming up
[01:25:19] with move 37, the super creative move
[01:25:21] that because it was never initialized on
[01:25:23] human data, it can like think in ways
[01:25:25] that humans are not even thinking and
[01:25:26] come up with extremely creative
[01:25:27] solutions. Yeah. Do you have a sense on
[01:25:30] when we should expect or if we should
[01:25:32] expect RL on LLMs to result in things
[01:25:35] like move 37 just extreme creativity
[01:25:38] even beyond human creativity because
[01:25:40] like there's just denovo
[01:25:42] uh dova initialization of intelligence.
[01:25:45] I mean so a couple of things here like
[01:25:47] first off I think that the alpha go is
[01:25:49] using MCTS which obviously does like
[01:25:50] more exploration and like stuff than
[01:25:52] regular policy gradients but I kind of
[01:25:54] also think that like RL doesn't
[01:25:56] necessarily like reduce the creativity
[01:25:58] and like I mean even if we I think you
[01:26:00] know this is obviously qualitative but
[01:26:01] if we look at like the you know the open
[01:26:03] air hinge incident like these models
[01:26:04] were coming up with like multiple zero
[01:26:06] days at a time to like break out of the
[01:26:08] sandbox and like this is clearly like
[01:26:10] some level of like move 37 creativity I
[01:26:12] think already which we just get from
[01:26:13] just like the general generalization
[01:26:15] properties of the LMS like I don't think
[01:26:17] it's definitely not the case like RL is
[01:26:18] like totally destroying their like
[01:26:19] entropy
[01:26:21] >> especially on long horizons
[01:26:22] >> yeah I mean one thing that people call
[01:26:24] creativity is just uh solving hard
[01:26:27] search problems so uh and so that's like
[01:26:31] uh like move 37's obviously an example
[01:26:33] of that or like uh writing some kind of
[01:26:35] poem that satisfies a ton of different
[01:26:37] constraints um so that's something AI is
[01:26:41] obviously going to be extremely good at
[01:26:43] uh if if trained for it. Um then uh
[01:26:46] there's another way in which the models
[01:26:48] uh like uh the diversity of their
[01:26:51] outputs uh is a lot lower after RL and
[01:26:55] they sort of develop these ticks and
[01:26:57] like um even though the models seem like
[01:26:59] they're good at writing when you do some
[01:27:01] kind of like distributional analysis you
[01:27:03] find that like they're reusing uh
[01:27:06] certain themes uh like all the time and
[01:27:09] they're using the same character names
[01:27:11] all the time. So there's actually um
[01:27:13] it's not like you're getting the same
[01:27:15] kind of diversity that you get when you
[01:27:17] like from human authors. You're sort of
[01:27:18] getting one really good uh like style.
[01:27:21] So I think that um like that kind of
[01:27:23] diversity has definitely uh been like
[01:27:26] cut down by RL a lot. And in fact uh now
[01:27:30] oh yeah since we were talking about
[01:27:32] distillation earlier that's sort of uh
[01:27:34] something yeah one thing that's
[01:27:37] happening is that so many people are
[01:27:38] distilling uh mostly from claude that
[01:27:41] like uh like all the open wade models
[01:27:43] write the same way as claude and use the
[01:27:45] same like have the same ticks. So this
[01:27:48] uh seems kind of concerning to me that
[01:27:50] we're having this uh like this
[01:27:52] monoculture emerge.
[01:27:53] >> Yeah. Again, I don't think this is like
[01:27:55] fundamental to RL as like a method
[01:27:57] though. And same with distillation. Like
[01:27:59] even with distillation, like you're just
[01:28:00] training on the data. It's like just
[01:28:01] because your data is not like super
[01:28:03] bored, that doesn't mean like the
[01:28:04] training method itself is somehow wrong.
[01:28:06] It's like a problem with the data. And I
[01:28:07] think a lot of for instance like the RL
[01:28:10] like entropy collapse is basically due
[01:28:11] to like exploitation of fairly simple
[01:28:13] like verifiers when you don't have like
[01:28:15] a huge diversity of environments cuz
[01:28:17] like for instance like the writing I
[01:28:18] think the writing is presumably graded
[01:28:20] by some judge and like the judge has
[01:28:21] some specific ticks and like the model
[01:28:23] is learning to award hack the judge and
[01:28:24] that's why like it collapses but like
[01:28:26] this is really a problem with the judge.
[01:28:27] It's not a problem with like RL in
[01:28:29] general.
[01:28:30] >> Um okay super rapid fire predictions
[01:28:33] about the future. So I want timelines on
[01:28:35] the following couple questions. By when
[01:28:39] do we have models which you can here's
[01:28:43] what the it feels like to a user. You
[01:28:47] basically hire them as a drop in remote
[01:28:49] worker for all kinds of white collar
[01:28:53] work not just coding but I don't know
[01:28:55] video editing um uh law parallegal etc.
[01:28:59] Like it's like literally an actual
[01:29:00] remote worker with like full computer
[01:29:02] use with like literally a month of
[01:29:05] seamless learning and operation and
[01:29:07] executing on like complex projects and
[01:29:10] it required interacting with other
[01:29:11] people etc etc. It's like everything a
[01:29:13] human worker could do over a month.
[01:29:15] >> If you like mandated to use like a
[01:29:17] browser or whatever rather than like
[01:29:18] these the again the firm setting up the
[01:29:20] information to be like programmatically
[01:29:22] accessible like maybe a couple years.
[01:29:23] But
[01:29:24] >> if it's not like browser based like it
[01:29:26] can send Slack messages, it can do all
[01:29:27] this stuff. But I'd still probably say
[01:29:28] around a year.
[01:29:29] >> Yeah. Yeah. I mean, I would say maybe
[01:29:31] like for the like full generality maybe
[01:29:34] like three years, but I think to
[01:29:36] Charlie's point, we will end up with
[01:29:37] like a lot of people like making their
[01:29:39] organizations easier for the AIS to use.
[01:29:41] And so you get like 80 90% of the way
[01:29:43] there before that.
[01:29:45] >> So, but the thing that's the the diff
[01:29:47] between one year and 3 years there is
[01:29:48] just literally like
[01:29:49] >> like I think there's going to be like a
[01:29:51] long tail of like miscellaneous stuff
[01:29:52] which like some human can do which like
[01:29:54] will take the models like quite a while
[01:29:55] to do. Yeah. Like you mean are you
[01:29:56] thinking of sort of computer stuff or
[01:29:57] like basic cognitive capabilities?
[01:29:59] >> I mean I think this this really comes
[01:30:01] down to a question of like how quickly
[01:30:02] can we solve this kind of like online
[01:30:04] learning and like
[01:30:05] >> whether we can like get like 80 90% of
[01:30:07] the way there with like compaction and
[01:30:08] like writing files to yourself and stuff
[01:30:09] and like that's my big uncertainty.
[01:30:11] >> I really don't know.
[01:30:12] >> And and another like maybe an example of
[01:30:14] something that I wouldn't be good at is
[01:30:15] like you know if I have to like yell at
[01:30:17] someone to get something at at work or
[01:30:19] like really push someone to get
[01:30:20] something done like the model isn't just
[01:30:21] going to do that. It's just going to be
[01:30:22] too nice.
[01:30:23] >> Yeah.
[01:30:23] >> Yeah. I'd say there's a wide variation
[01:30:26] in quality of uh human remote workers.
[01:30:28] So if you [laughter] if you try to hire
[01:30:30] someone like off of Upwork to do a
[01:30:32] software engineering project, there's
[01:30:34] going to be a huge variation. It's like
[01:30:35] often quite hard to get them to do like
[01:30:38] to do a good job or like pay attention
[01:30:40] to all the feedback you're getting. And
[01:30:42] uh like I would guess that in some cases
[01:30:45] it uh like it'll be worse like the the
[01:30:48] pre-AI um version of this uh was worse
[01:30:51] than what you can get now from existing
[01:30:53] AI. Uh so I think it might end up being
[01:30:57] a little complicated uh because maybe to
[01:30:59] some some extent we already have this uh
[01:31:01] like for some like not so high quality
[01:31:03] of work but then like uh then it's
[01:31:06] obviously like we're not yeah we're not
[01:31:08] matching human level in certain like
[01:31:10] higher quality like um forms of work.
[01:31:13] So, but I basically agree with Charlie
[01:31:16] and Baron that maybe yeah, we'll yeah,
[01:31:19] we'll have some version of this in a
[01:31:20] year or so that's like okay and it we'll
[01:31:22] be able to do um maybe we'll have that
[01:31:24] form factor um and uh it'll be able to
[01:31:27] do some things really well, some things
[01:31:29] not so well and
[01:31:31] >> things will be improving from there.
[01:31:32] >> Like we ship the goalpost based on the
[01:31:34] very long tail all the time. Like I
[01:31:37] think feel like you've used this example
[01:31:38] before of like doing your taxes or
[01:31:39] something. Like this year I literally
[01:31:41] just like told Codeex to like go get
[01:31:42] everything I needed to do and send it to
[01:31:44] the accountant and like there was this
[01:31:45] massive list of stuff it had to use
[01:31:46] computers to click through and like
[01:31:48] download some stuff and it didn't it was
[01:31:49] it was like fine. It was perfect. So
[01:31:51] like I don't know a lot of this stuff it
[01:31:54] can already do.
[01:31:54] >> Yeah. Okay. Um give you 10x total
[01:31:58] productivity uplift.
[01:32:00] >> Basically if you if it takes you a year
[01:32:02] to make a breakthrough now you you make
[01:32:04] a breakthrough every month.
[01:32:05] >> I think I would just refuse to give you
[01:32:07] a scaler on this. [laughter]
[01:32:08] uh like like we might already be past
[01:32:11] that in some like types of work uh like
[01:32:14] let's say you're just trying to prove uh
[01:32:16] yeah you're trying to do um like certain
[01:32:19] types of math uh
[01:32:20] >> I was sorry but for you as AI
[01:32:22] researchers trying to make um yeah
[01:32:24] >> like advance you know the state of AI
[01:32:26] research how much are like AI
[01:32:28] researchers sped up
[01:32:29] >> or uplifted
[01:32:31] >> somewhere between five and 10 years
[01:32:33] >> oh really that's far away you think it's
[01:32:35] longer than like for general remote
[01:32:36] worker Yeah, [clears throat]
[01:32:38] >> interesting.
[01:32:39] >> I think you probably I think I'm
[01:32:40] realizing you probably have very
[01:32:41] different definitions of fully general
[01:32:43] remote worker. I could have specified.
[01:32:44] >> Yeah, this is true because I mean like
[01:32:46] Yeah, because obviously like an AI
[01:32:47] researcher can be a remote worker and so
[01:32:49] like
[01:32:49] >> Yeah. No, I I'm picturing like you know
[01:32:51] normal white collar work over the period
[01:32:53] of a month.
[01:32:54] >> Yeah,
[01:32:54] >> I think it starts to diverge a little
[01:32:55] bit past a month
[01:32:56] >> like a very competent white collar
[01:32:57] worker but not necessarily like a super
[01:32:59] creative researcher.
[01:33:00] >> I would say like two years.
[01:33:02] >> Two years. Yeah. 10x. Okay.
[01:33:04] >> How about you burn? I can kind of see
[01:33:06] that actually because like it really is
[01:33:08] just like right now it's already like
[01:33:10] definitely more than 10x of like coding
[01:33:11] stuff and so it's like if it can do even
[01:33:13] like one or two loops of like
[01:33:15] experimental feedback that would
[01:33:16] actually be massive already.
[01:33:17] >> So 10x uplift of AI researchers within
[01:33:20] two years
[01:33:22] >> if you just plug it into like a very
[01:33:23] naive model of like AI progress and how
[01:33:26] much is coming from AI researchers and
[01:33:28] they're like there's like a 10x increase
[01:33:29] in their productivity. Yeah. Yeah. You
[01:33:32] you have like radically accelerated pace
[01:33:33] of AI progress starting 2 years from
[01:33:35] now.
[01:33:36] >> Yeah. I mean I think like this will mean
[01:33:37] that AI progress doesn't get
[01:33:38] bottlenecked on like AI researchers
[01:33:40] ability to run like small experiments.
[01:33:42] It gets bottlenecked on other things.
[01:33:43] >> Of course. Of course. But it just like
[01:33:44] happens 10x faster
[01:33:45] >> for sure. Yeah.
[01:33:46] >> Which is a huge deal and that also like
[01:33:48] helps the next thing which makes gives
[01:33:49] you 100x speed up happen sooner etc.
[01:33:53] >> Yeah. I'm happy to stick with longer on
[01:33:54] that one.
[01:33:55] >> And what's what's the what's like the
[01:33:56] crux? uh like my capacity to absorb
[01:33:59] information and make the like Beijian
[01:34:01] optimal decision on the next
[01:34:02] >> experiment. Makes sense.
[01:34:04] >> Yeah. I mean, I'm assuming that like you
[01:34:05] can delegate some of this to the AI. So
[01:34:07] like the AI is becoming decent at like
[01:34:09] deciding, you know, it's run this
[01:34:10] experiment, it's got this result, it
[01:34:11] runs like the next experiment and then
[01:34:12] if it can run like two or three
[01:34:13] experiments in a row without like
[01:34:14] crashing, then like that is actually big
[01:34:17] update like uplift and
[01:34:19] >> and okay, final question. um an AI which
[01:34:22] is
[01:34:24] which dominates top human experts across
[01:34:26] every single field of work that can be
[01:34:28] done over a computer.
[01:34:31] So not only a research but all cognitive
[01:34:34] work and not just like short horizon
[01:34:36] work but like literally if it takes like
[01:34:38] three years or something they will still
[01:34:40] do better than humans. So this is
[01:34:41] basically just like ASI. Okay.
[01:34:44] >> I would say like three or four years.
[01:34:46] >> The [laughter]
[01:34:49] >> I mean that's that doesn't seem wrong.
[01:34:51] >> I would say like um like AI is obviously
[01:34:53] being more um getting more attention. So
[01:34:56] it's like one of the harder things, but
[01:34:58] it's like uh a lot of energy is being
[01:35:01] put into it and it's also like not one
[01:35:03] of the hardest things for AI because
[01:35:04] it's like involves a lot of code and and
[01:35:06] math which models are really good at. Uh
[01:35:09] maybe for things that involve like 3D
[01:35:11] and like spatial stuff and physical
[01:35:14] stuff, I think uh that that will take a
[01:35:16] little longer. Um so um especially if
[01:35:20] it's not like Yeah. Yeah. If it's like
[01:35:21] mechanical engineering or something and
[01:35:23] it's not getting like the most attention
[01:35:25] right now, that might take a little
[01:35:26] longer.
[01:35:27] >> But it also has to include fields where
[01:35:28] there is relatively little data because
[01:35:30] of the nature of the field and it has to
[01:35:32] like learn that data on the fly. for
[01:35:35] example, has to become superhuman at
[01:35:38] like being an engineer at TSMC or
[01:35:41] something.
[01:35:42] >> Oh yeah. So you would have to assume
[01:35:43] that like the on uh like the onboarding
[01:35:46] Yeah. You can give the AI the same
[01:35:47] onboarding material and uh Oh yeah. Then
[01:35:50] there's some like some something has to
[01:35:52] be solved about like uh sort of longer
[01:35:55] horizon learning or Yeah.
[01:35:57] >> I'd say five to 10. So basically yeah
[01:35:59] it's it's you think
[01:36:02] automating AI research is like ASI
[01:36:04] complete or something.
[01:36:05] >> I yeah I think so. Um yeah I think
[01:36:08] there's so many things in the world
[01:36:09] which like even if you have some sort of
[01:36:11] memory system external to the model
[01:36:13] >> and even if like context length grows a
[01:36:15] little bit like there are just
[01:36:17] fundamentally things like even if you
[01:36:18] could research the information or write
[01:36:19] notes yourself like you need more than
[01:36:21] the context to be able to do. Yeah.
[01:36:23] >> Yeah. I mean, I kind of agree in like
[01:36:25] the the 5year range at least for like
[01:36:27] the stuff that like labs are focusing
[01:36:28] on, but I think like there's going to be
[01:36:30] a long tale of stuff which like yeah, I
[01:36:32] could theoretically go out and learn
[01:36:33] about, but like no one has bothered to
[01:36:35] do it and like the the computers being
[01:36:37] allocated to that, so that might take
[01:36:38] longer for like literally every single
[01:36:39] human expert.
[01:36:40] >> Yeah, it's right by this I also included
[01:36:42] like the ability to learn as fast as a
[01:36:44] human, a new domain.
[01:36:45] >> I mean, I think that's not necessarily
[01:36:47] necessary actually cuz like the AI will
[01:36:49] have vastly greater experience than like
[01:36:50] any human,
[01:36:51] >> right? Thanks so much for doing this,
[01:36:52] guys. I feel like this is a great format
[01:36:53] for getting different experts to
[01:36:55] disagree and debate and discuss things
[01:36:57] together was very productive. Cool.
