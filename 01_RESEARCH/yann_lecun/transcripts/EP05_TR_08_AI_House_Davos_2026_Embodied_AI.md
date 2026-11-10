# AI House Davos 2026: Yann LeCun — Embodied AI & World Models
- **YouTube URL:** https://www.youtube.com/watch?v=pJyoqapCRZE
- **Lines:** 1719

---

[00:00:00] It's great to have you here, Jan, just
[00:00:01] in time.
[00:00:03] Or, well, a few minutes late, but
[00:00:04] anyways.
[00:00:05] So, today we'll talk about embodied AI.
[00:00:09] I know that's a topic that's, you know,
[00:00:10] you're passionate about. Also a topic
[00:00:13] topic that I'm I'm also
[00:00:15] quite excited about.
[00:00:17] Actually, both of us, I think, for many
[00:00:19] years.
[00:00:20] But I think now a lot more people,
[00:00:22] you know, this is really kind of coming
[00:00:24] a lot of There's a lot of excitement, a
[00:00:27] lot of investments, a lot of things
[00:00:29] going on. And so I think we'll dig a
[00:00:31] little bit deeper in what's already
[00:00:34] possible,
[00:00:36] what we see on the horizon, the gaps
[00:00:38] that we see,
[00:00:39] the kind of things that are needed,
[00:00:40] etc., etc. So, um
[00:00:43] So maybe first embodied AI, what are we
[00:00:45] talking about? So it's really
[00:00:47] um
[00:00:48] you know, AI that can actually
[00:00:51] perceive in the world, understand the
[00:00:53] situation, be able to reason about that,
[00:00:56] plan
[00:00:57] based on that, and then act in the
[00:01:00] world. So that's really what we're
[00:01:01] talking about. This can
[00:01:02] go from
[00:01:04] self-driving vehicles to then also, you
[00:01:06] know, humanoid robots and and things
[00:01:08] like that, and anything in between, I
[00:01:10] would say.
[00:01:11] um
[00:01:13] So, Jan,
[00:01:14] you know, like maybe we can start
[00:01:16] where are we today? Like what can we do?
[00:01:18] What can't we do? Can
[00:01:20] So we're not very far.
[00:01:22] uh
[00:01:23] You know, we have So first of all, it's
[00:01:25] not just embodied AI in the in the sense
[00:01:28] of you know, robots and things like
[00:01:30] that. It's also disembodied physical AI.
[00:01:33] AI for the real world, right? So there's
[00:01:35] a lot of systems
[00:01:36] in the world that need to be understood,
[00:01:39] predicted, controlled, which are not
[00:01:41] necessarily bodies, right? It could be
[00:01:45] it could be a manufacturing process,
[00:01:47] could be a turbojet engine, it could be
[00:01:50] you know, any kind of um industrial
[00:01:53] process.
[00:01:54] um Anything that's physical, anything
[00:01:56] for which the data
[00:01:59] comes to you in a form of
[00:02:01] a sequence of high-dimensional,
[00:02:03] continuous, noisy um signals. Video is
[00:02:06] the best example.
[00:02:08] Proprioceptive sensors on a robot is
[00:02:11] another good example.
[00:02:13] But there is a lot of applications of
[00:02:14] this that have nothing to do with with
[00:02:15] robotics, right? So, um So it's anything
[00:02:18] that is not language-related. That's
[00:02:19] that's really the the better definition,
[00:02:21] right?
[00:02:22] So,
[00:02:24] the real world is fundamentally
[00:02:25] different from language. And the reason
[00:02:29] language has been like LLMs have been so
[00:02:31] successful is because language is easy.
[00:02:34] um
[00:02:35] You know, we have
[00:02:37] systems that can pass the bar exam.
[00:02:40] I'm not going to say they're as smart as
[00:02:41] a lawyer. I don't know if there's any
[00:02:42] lawyer in the room here. No, we're all
[00:02:44] scientists and engineers here, so I can
[00:02:45] say that.
[00:02:46] um
[00:02:48] And
[00:02:50] so we have systems that can pass the bar
[00:02:51] exam.
[00:02:52] They can also, you know, do math, right?
[00:02:54] Solve equations, they can write code.
[00:02:57] Many of us here write code, too.
[00:02:59] uh
[00:03:00] But
[00:03:01] they don't really deal with the real
[00:03:03] world, right? Which is the reason why we
[00:03:05] don't have domestic robots, we don't
[00:03:06] have level five self-driving cars still.
[00:03:09] um At least not at the consumer level.
[00:03:11] And so we and, you know, human humanoid
[00:03:14] robots
[00:03:15] >> but not level five. No level five. And
[00:03:18] uh
[00:03:19] And even at level four, you know, we
[00:03:21] cheat a lot.
[00:03:22] I think level four less than way more. I
[00:03:24] think you can claim that they achieve
[00:03:25] level four. They do.
[00:03:27] >> But not level five. They need full maps,
[00:03:29] they need control of where they are and
[00:03:31] when they operate.
[00:03:32] >> And they need, you know, exotic sensors,
[00:03:34] lidars, and complete
[00:03:36] >> okay. That's okay. That's fine.
[00:03:37] >> can cheat. It's It's perfectly I don't
[00:03:38] think that's cheating, by the way. No,
[00:03:40] no. I mean, it's okay.
[00:03:42] But it's expensive in the sense that how
[00:03:44] is it that a 17-year-old can learn to
[00:03:46] drive in, you know, 10 to 20 hours of
[00:03:49] practice?
[00:03:50] uh And we have millions of hours of
[00:03:52] training data that we could, in
[00:03:54] principle, train a machine learning
[00:03:56] system by imitation to imitate human
[00:03:58] drivers. But that doesn't work. You
[00:04:00] don't get reliable
[00:04:02] driving systems this way. And so,
[00:04:04] um
[00:04:06] that sort of leads me to another
[00:04:07] statement about
[00:04:08] robotics. There's a lot of companies
[00:04:10] building humanoid robots, and they do
[00:04:11] those kinds of, you know, they play kung
[00:04:13] fu and,
[00:04:14] you know, impressive thing. This is all
[00:04:16] precomputed.
[00:04:17] Okay? uh
[00:04:20] None of those company, absolutely none
[00:04:22] of them, has any idea how to make those
[00:04:25] robots smart enough to be useful.
[00:04:28] Right? It's a big secret of
[00:04:30] robotics industry.
[00:04:32] um You can train them on very narrow
[00:04:34] tasks.
[00:04:35] And you have to to collect lots and lots
[00:04:37] of data the same way, you know, people
[00:04:39] thought they would build self-driving
[00:04:40] cars.
[00:04:41] um And it's expensive, and it's only
[00:04:44] practical for a small number of narrow
[00:04:45] tasks, and you you don't have robots
[00:04:48] that, you know, have nearly as good as a
[00:04:51] common sense as your house cat,
[00:04:53] let alone human intelligence, right? So,
[00:04:55] um that's the
[00:04:57] you know, that's the challenge for the
[00:04:58] next few years, right? Getting a system
[00:05:00] to really understand the real world. And
[00:05:02] the problem is that the approaches that
[00:05:05] have been successful for language do not
[00:05:06] work for high-dimensional, continuous,
[00:05:09] noisy data. You have to use something
[00:05:11] else.
[00:05:13] So, um you know, so let's let's actually
[00:05:16] start with
[00:05:18] you know, with what people are trying
[00:05:19] now in in robotics and in in in embodied
[00:05:21] AI. So,
[00:05:22] you know, and and I know your positions
[00:05:25] on on LLMs and what what you can do with
[00:05:26] them. uh I agree with you, language is
[00:05:29] is easy because in a sense we
[00:05:31] immediately start at a semantic level.
[00:05:33] We have, you know, tokens are
[00:05:35] essentially very close to like a
[00:05:36] semantic concept. um And so directly by
[00:05:40] working at that level, we can ignore a
[00:05:42] lot of the noisy, complicated,
[00:05:44] real-world kind of things. You know, we
[00:05:45] say car, and we can imagine many many
[00:05:47] different things, and so on. uh But, you
[00:05:49] know, for an LLM, it's just kind of a
[00:05:51] car with, you know, some dimensions with
[00:05:52] it, but kind of some concepts associated
[00:05:54] with it, but but but like no
[00:05:56] understanding what it actually is,
[00:05:57] right? um
[00:05:59] just having correlations to other stuff.
[00:06:01] Anyway, so there's LLMs, there's then
[00:06:03] there's then VLMs,
[00:06:05] and there's VLAs now that there's a lot
[00:06:07] of excitement around, right? uh I Well,
[00:06:11] you know, not by you, but but by others.
[00:06:14] So, but but I'd like you to a little bit
[00:06:15] kind of
[00:06:17] explain like the relationship between
[00:06:18] all of those those three, and and you
[00:06:20] know, also where you see the
[00:06:21] shortcomings there. Right. So VLM is,
[00:06:24] you know, basically the idea of
[00:06:25] mixing in
[00:06:27] visual representations together with
[00:06:30] language, with tokens that come from
[00:06:32] language. um And then use the machinery
[00:06:35] of LLMs basically to do to do that. uh
[00:06:37] VLAs
[00:06:39] are kind of a version of this where the
[00:06:40] output of the system is a sequence of
[00:06:42] actions.
[00:06:43] There's a major flaw with those
[00:06:45] approaches, and they're extremely
[00:06:46] difficult extremely difficult to make
[00:06:48] them work. The VLAs or or so-called
[00:06:51] agentic systems only work in situations
[00:06:54] where
[00:06:55] the actions obey a
[00:06:57] a script that you have to basically
[00:07:00] repeat all the time.
[00:07:02] um
[00:07:03] You know, repetitive task of some kind.
[00:07:05] So it's a new way of just designing
[00:07:07] automating a task, which is data-driven
[00:07:09] instead of being, you know,
[00:07:11] programmatic. uh But it's very brittle,
[00:07:13] it's very restricted to very narrow
[00:07:15] applications for which there is a you
[00:07:17] know, a script that you can follow.
[00:07:20] That's not what you want. You want a
[00:07:22] system that can accomplish a new task
[00:07:23] it's never been trained to accomplish,
[00:07:25] which every human is capable of doing,
[00:07:27] every animal even, uh facing a new
[00:07:29] situation using
[00:07:32] their mental model of the world. Okay,
[00:07:33] so here we're going to talk about world
[00:07:34] models. A world model is a big buzzword
[00:07:36] now, but mostly
[00:07:39] but people mean different things for
[00:07:40] this. And And it's mostly a buzzword in
[00:07:43] research, not so much in industry. The
[00:07:45] AI industry is completely LLM-pilled, as
[00:07:48] they say.
[00:07:49] uh
[00:07:51] And and in Silicon Valley, everybody is
[00:07:53] working on the same thing. They're all
[00:07:54] digging the same trench. They're
[00:07:56] stealing each other's engineers so that
[00:07:59] they they can't afford to do something
[00:08:00] different because if they start going on
[00:08:02] a tangent, they're going to,
[00:08:04] you know, fall behind the other guys.
[00:08:06] And so they're all doing the same thing,
[00:08:07] and that's one big reason I left Meta,
[00:08:09] right? Because Meta also became
[00:08:11] LLM-pilled.
[00:08:12] um
[00:08:13] You know, with sort of recent research
[00:08:15] thing.
[00:08:16] And it's fine, you know, it's a
[00:08:17] strategic decision that
[00:08:19] maybe makes sense for for them. Just not
[00:08:21] what I'm interested in. uh And so, um
[00:08:27] I cannot imagine that we can build
[00:08:29] agentic systems without those systems
[00:08:31] having an ability to predict in advance
[00:08:34] what the consequences of their actions
[00:08:36] are going to be.
[00:08:38] The way
[00:08:39] we act in the world is that we know what
[00:08:41] the we can predict the consequence
[00:08:44] consequences of our actions.
[00:08:46] And that's what allows us to plan.
[00:08:48] um So what is a world model? Given the
[00:08:49] state of a environment, a system you
[00:08:52] want to control at time T, and given an
[00:08:54] action or intervention you imagine
[00:08:56] taking,
[00:08:57] can you predict the state of the world
[00:08:59] or the of the or the system at time T
[00:09:00] plus one? If you have, that's a world
[00:09:03] model. You don't do this at the pixel
[00:09:04] level if it's video.
[00:09:06] uh You do this in an abstract
[00:09:08] representation space. And that's a
[00:09:10] crucial key
[00:09:12] insight that you you you know, you need
[00:09:15] to really understand. You cannot predict
[00:09:17] every detail, for example, what is going
[00:09:19] to happen in the video.
[00:09:21] I can take a video of this room, rotate
[00:09:24] the camera, and stop here, and then ask
[00:09:26] the system continue the video. System
[00:09:28] will predict, you know, where the room
[00:09:30] is, probably, you know, a door at some
[00:09:31] point. There's no way it can predict
[00:09:33] what all of you looks like. There's
[00:09:35] absolutely no way in hell I can predict
[00:09:36] the texture of your beautiful
[00:09:39] uh
[00:09:39] dress here, which is, you know, very
[00:09:42] shiny, and uh
[00:09:44] which has, you know, a huge amount of
[00:09:45] information. It's just impossible,
[00:09:46] right? So if you train a generative
[00:09:49] architecture, which is supposed to
[00:09:51] predict at the pixel level, it fails. It
[00:09:53] doesn't do anything useful for you. I
[00:09:55] mean, it might produce cute videos or
[00:09:57] cute pictures with diffusion models, but
[00:10:00] that's it.
[00:10:01] And it it will not understand the
[00:10:03] underlying structure of of the world.
[00:10:05] For that, you need to find an abstract
[00:10:08] representation of of uh
[00:10:10] of reality that allows you to make
[00:10:12] predictions and eliminate all the
[00:10:13] details you cannot predict. And we'll
[00:10:15] come we'll come back to that. I first
[00:10:17] want to take a step back to um you know,
[00:10:19] to the the VLM and and VLA world uh and
[00:10:23] and LM world. I think you said like you
[00:10:26] can only do things that are essentially
[00:10:27] scripted and this and that.
[00:10:29] But I would say in industry, there are
[00:10:30] many many things that are useful and
[00:10:32] that are scripted and you know, you have
[00:10:33] to carry out a certain task and most of
[00:10:35] the time you have to do it. So
[00:10:36] So, I would say there is probably a lot
[00:10:38] of potential for the current this
[00:10:40] current technology to actually deliver
[00:10:41] value
[00:10:43] uh with today's state. Like if you look
[00:10:45] at you know, VLMs essentially, you know,
[00:10:46] we it's it's it's text and I agree it's
[00:10:49] actually really text first and then you
[00:10:51] know, an image is worth a thousand uh
[00:10:53] tokens literally pretty much. Um and so
[00:10:56] uh and then you know, with with action
[00:10:58] it's you still essentially take a
[00:10:59] picture. This is the situation.
[00:11:02] This is what I want to do and then you
[00:11:03] know, like from that you kind of if it's
[00:11:06] all scripted kind of in a sense, you can
[00:11:07] kind of carry it out, right? And you can
[00:11:09] build
[00:11:10] you can program it. It's probably a
[00:11:11] simpler way to program than maybe what
[00:11:13] we used to do before. So So So, let's
[00:11:15] say you know, like if if if you would be
[00:11:17] an advocate of VLAs or so, like what do
[00:11:19] you think we can all achieve already
[00:11:20] with what we have today? Well, I mean,
[00:11:22] it's like LLMs. Those things are useful.
[00:11:24] And there is probably a number of uh
[00:11:26] applications probably relatively
[00:11:28] narrow narrower than what people are
[00:11:30] thinking
[00:11:31] for which those things would be useful
[00:11:33] and practical and deployable. But you
[00:11:36] know, I old enough to remember what
[00:11:38] happened in the 1980s with the expert
[00:11:40] systems. Okay, expert systems, you know,
[00:11:42] you
[00:11:43] you were going to
[00:11:45] the coolest job at the time was going to
[00:11:47] be uh knowledge engineer. You were you
[00:11:49] were going to sit down next to a human
[00:11:50] expert and then trans translate the
[00:11:53] knowledge of the human expert in rules
[00:11:55] and facts. Okay, in a and then use a
[00:11:58] inference engine to basically replace
[00:12:00] the expert or you know, kind of clone
[00:12:02] the expert if you want. No machine
[00:12:04] learning whatsoever. It was entirely
[00:12:05] human.
[00:12:06] That approach to AI essentially failed
[00:12:09] because the the brittleness of the
[00:12:11] resulting system and the cost of
[00:12:14] of this, you know, knowledge transfer
[00:12:16] into a machine was just too high. So,
[00:12:17] there was a very narrow number of
[00:12:19] applications for which it it was
[00:12:21] practical. It's going to be the same
[00:12:23] thing for VLA. It's going to be a
[00:12:25] relatively small number of applications
[00:12:27] where you have scripted, you know,
[00:12:29] scenarios where those things are going
[00:12:30] to be useful. Um but in the end, if you
[00:12:33] are interested like I am in, you know,
[00:12:35] building systems that have the
[00:12:36] intelligence of let's say a cat, you
[00:12:38] know, let alone humans. Um
[00:12:41] you need common sense. You need the
[00:12:42] ability to predict
[00:12:44] uh the consequences of your actions. You
[00:12:45] need the ability to plan. You need the
[00:12:47] ability to reason. And you're not going
[00:12:49] to get this with a with VLA or VLM or
[00:12:51] LLMs or any generative architectures.
[00:12:53] >> I agree, but I would say, you know, I
[00:12:55] see a lot of potential industry of just
[00:12:57] you know, doing what you're supposed to
[00:12:58] do.
[00:12:58] >> I mean, LLMs are super useful for
[00:13:00] coding, you know, no question. Well,
[00:13:02] okay. So So, back to um you know, to
[00:13:04] world models. Um so you said like you
[00:13:08] need to you know, maybe not predict at a
[00:13:11] pixel level. Now, sometimes you can I
[00:13:13] mean like video models actually do very
[00:13:15] nice work in particular when you know,
[00:13:17] say like like with a VLA when you're
[00:13:19] given a starting position. You know,
[00:13:21] this is the situation and I have to
[00:13:23] predict now I'm I just need to do a
[00:13:24] relatively simple task. I need to move a
[00:13:26] few things around, kind of assemble
[00:13:27] something or so.
[00:13:29] There I can probably predict at a pixel
[00:13:30] level exactly how it should look like,
[00:13:32] right?
[00:13:33] Um so So, I think sometimes, you know,
[00:13:35] there are situations where you can
[00:13:36] actually go to the pixel level.
[00:13:39] Um I know of course, you know, like
[00:13:40] you're a strong proponent of of all the
[00:13:43] of the Jepa framework of of going to um
[00:13:46] you know, I agree with you. You don't
[00:13:47] have to predict every pixel for most
[00:13:50] situations. I think sometimes you do
[00:13:51] like when you really want a fine scale
[00:13:53] thing in the end, you might need detail.
[00:13:55] My question is actually where
[00:13:57] you know, how do we find What is the
[00:13:59] right level at which we and I think it's
[00:14:01] not always the same necessarily for for
[00:14:03] every task. So, what is the right level
[00:14:05] of abstraction at which we need to
[00:14:06] predict? I mean, we as humans
[00:14:09] we do indeed always or you know, our
[00:14:10] whole brain seems to be dedicated to
[00:14:12] predicting the future.
[00:14:13] And then we look at the differences,
[00:14:15] right? And and and we might care about
[00:14:16] them or not. Uh and indeed we we I think
[00:14:19] we actually don't predict I mean, even
[00:14:21] most of the Jepa maybe I'm wrong, but
[00:14:23] it's predicting at a certain level of
[00:14:24] abstraction. Uh mostly at a fixed level
[00:14:27] that's learned of abstraction. Um
[00:14:29] intuitively, I would actually like to be
[00:14:31] able to predict throughout the levels
[00:14:32] and go to the level I want. Yeah.
[00:14:33] >> Yeah, totally. No, I mean, you
[00:14:36] you know, picking the right level of
[00:14:37] abstraction is absolutely essential to
[00:14:40] understanding the world around us.
[00:14:42] Um in fact, we don't know any other way
[00:14:44] of doing it. It's it's something that,
[00:14:45] you know, not many people realize, but
[00:14:48] um
[00:14:49] let's say
[00:14:50] let's say I want to plan a trip from New
[00:14:53] York to Paris. Let's say I'm sitting in
[00:14:55] my office in New York. It's midday and I
[00:14:57] want to be in Paris tomorrow.
[00:14:59] Uh I cannot possibly plan my entire trip
[00:15:02] to Paris in terms of elementary actions
[00:15:05] for humans, which are millisecond by
[00:15:06] millisecond muscle control.
[00:15:08] Right? Cuz
[00:15:09] it's too complicated. I have a planning
[00:15:10] issue and I just don't have the
[00:15:12] information.
[00:15:13] You know, I don't know
[00:15:15] if someone is going to run into me when
[00:15:17] I walk to the elevator. I don't know if
[00:15:18] how long I'm going to have to wait for a
[00:15:20] taxi. Right? So, I cannot plan, but I
[00:15:22] can plan at a very abstract level.
[00:15:24] At the abstract level, I can say, well,
[00:15:26] I need to go to the airport and catch a
[00:15:27] plane. Okay, now I have a sub goal,
[00:15:29] being at the airport.
[00:15:30] My new objective is being close to the
[00:15:32] airport, right? Um I'm in New York, so I
[00:15:34] go down on the street and hail a taxi.
[00:15:36] Okay, that's a two-action plan, but it's
[00:15:38] very high level.
[00:15:39] Very little information I need to know
[00:15:42] uh other than maybe the condition of
[00:15:44] traffic. It would determine whether I
[00:15:45] take a taxi or subway or helicopter. Um
[00:15:49] then
[00:15:50] you know, then how do I go to on the
[00:15:52] street? I go to the elevator, push the
[00:15:54] button, walk out walk out of the
[00:15:55] building. How do I go to the elevator?
[00:15:57] You know, so at some point in the
[00:15:58] hierarchy you get down to a point where
[00:16:00] you can just take the action because you
[00:16:02] know how to stand up from your chair and
[00:16:03] walk to the door and open the door and
[00:16:04] things like that, right? So, this this
[00:16:07] is called hierarchical planning. It's
[00:16:08] completely unsolved problem in AI.
[00:16:10] People have
[00:16:11] you know, mostly given up.
[00:16:13] But that's basically what really is uh
[00:16:16] a big challenge that we we should crack
[00:16:19] uh for for kind of future AI systems
[00:16:21] that can behave properly. Animals do
[00:16:23] this all the time. Humans are much
[00:16:25] better at abstractions than humans, but
[00:16:27] but animals do this.
[00:16:29] Um
[00:16:30] so, that requires
[00:16:32] a multi-level
[00:16:34] world model. Right? A low-level world
[00:16:36] model that predicts short-term with a
[00:16:38] lot of details, with low-level actions.
[00:16:40] Okay, if I send a particular command to
[00:16:42] my muscle, it's going to move my arm in
[00:16:44] a particular way, right? Or high-level
[00:16:46] actions, you know, uh
[00:16:47] um
[00:16:48] hailing a taxi to go to the airport.
[00:16:49] That's more of a high-level action.
[00:16:51] Um the low level is not describable in
[00:16:54] language.
[00:16:55] Uh some part of the high level is and if
[00:16:57] it's a normal script, maybe VLA will,
[00:17:00] you know, do something like that. But um
[00:17:02] but really what you need for all of this
[00:17:04] is a mental model that allows you to
[00:17:06] predict what the consequence of your
[00:17:08] actions, regardless of the levels, are
[00:17:09] going to be. So, how do you train a
[00:17:11] hierarchical model of this type? So,
[00:17:13] first of all, you have to realize that
[00:17:14] you cannot make prediction
[00:17:16] in pixel space, in input space. You have
[00:17:17] to make prediction in that abstract
[00:17:19] representation space.
[00:17:20] And when you train that, so this is
[00:17:22] called this is the Jepa architecture
[00:17:24] that uh Mark was just mentioning, right?
[00:17:26] So, Jepa means joint embedding
[00:17:27] predictive architecture and it means
[00:17:30] learning an abstract representation of
[00:17:32] the input signal
[00:17:34] and making prediction in that abstract
[00:17:35] representation space and training this
[00:17:37] whole thing at once.
[00:17:38] Uh
[00:17:39] and the prediction might be conditioned
[00:17:41] by an action that you imagine taking,
[00:17:42] which gives you a world model.
[00:17:44] Um so
[00:17:46] the abstraction level
[00:17:48] that this system is going to learn
[00:17:50] depends on the horizon that you train it
[00:17:52] to make predictions at, right? If you
[00:17:55] train the system to make prediction
[00:17:57] you know, 10 milliseconds in the future,
[00:17:58] it's going to make very accurate
[00:18:00] predictions in the short term. Those
[00:18:02] predictions are going to diverge from
[00:18:03] reality really quickly. So, there you
[00:18:05] have to go
[00:18:06] one level up.
[00:18:07] Maybe predict 1/10 of a second or a
[00:18:09] second in the future. And then the
[00:18:11] higher you go in the hierarchy, the
[00:18:12] longer term
[00:18:14] uh the predictions are. I could in
[00:18:15] principle describe everything that is
[00:18:17] taking place in this room here between
[00:18:18] us
[00:18:19] in terms of uh quantum field theory.
[00:18:23] All right, that'd be crazy.
[00:18:25] But it would be a
[00:18:26] you know, a very accurate description of
[00:18:28] everything that takes place here,
[00:18:29] including the neurochemistry of our
[00:18:32] brain processes and what we think and
[00:18:34] everything, right? But it's completely
[00:18:35] impractical. I would need to measure the
[00:18:37] wave function
[00:18:38] you know, of of this room and probably
[00:18:40] like a cubic kilometer around us. Um
[00:18:43] and then you're using use some
[00:18:45] ridiculously powerful quantum computer
[00:18:46] to actually do the simulation. Like we
[00:18:48] don't do this, right?
[00:18:49] Uh
[00:18:50] so, we invent abstractions in science,
[00:18:52] but also that's what we do when we
[00:18:55] perceive and understand the world. We
[00:18:56] invent abstractions like particles,
[00:18:58] atoms, molecules. In the living world,
[00:19:00] it's proteins, organelles, cells,
[00:19:03] organisms,
[00:19:05] societies, ecosystems.
[00:19:07] And the the right level at which to
[00:19:09] describe what's going on in this room
[00:19:11] now is, you know, psychology, economics
[00:19:13] and science, right? It's pretty high in
[00:19:15] the hierarchy. We're not going to
[00:19:17] predict like, you know, the reaction of
[00:19:19] all of us in terms of particle physics.
[00:19:22] Uh that's impossible. So, being able to
[00:19:24] ignore details that are irrelevant that
[00:19:26] you cannot predict so that you can make
[00:19:28] long-term prediction is absolutely
[00:19:29] crucial to intelligence and
[00:19:32] generative models do not allow you to do
[00:19:34] this. This is what Jepa enables.
[00:19:37] But Jepa at this point still is
[00:19:38] typically at a particular for particular
[00:19:41] task, it learns a particular level of
[00:19:43] abstraction that's Well, that's what you
[00:19:45] see in publications, but
[00:19:47] Okay.
[00:19:48] We're working on multi-level Okay. Okay.
[00:19:50] >> hierarchies. Okay. So,
[00:19:53] in terms of
[00:19:54] you know, to to act in the
[00:19:57] uh
[00:19:57] you know, in in in the physical world,
[00:20:00] um
[00:20:00] what are the sensing modalities that,
[00:20:04] you know, that you think
[00:20:05] uh we need? So, like now we narrow it
[00:20:07] down a little bit to like, you know,
[00:20:08] maybe more like really robot like
[00:20:10] robotics applications, right? Um What do
[00:20:12] you see as as kind of um useful um
[00:20:16] kind of you know, where where both have
[00:20:18] a background in vision or so so we of
[00:20:20] course will use cameras or or you know,
[00:20:22] vision sensors, but but what else is
[00:20:24] needed uh to to make things work? So,
[00:20:27] what what is a you know, what would be
[00:20:29] the appropriate world model for for
[00:20:31] robot? Um there's several component.
[00:20:34] There's first
[00:20:35] a a model a mechanical sort of
[00:20:37] mechanical dynamical model of the robot,
[00:20:39] which, you know, you apply a torque to a
[00:20:42] a motor in one of the joints, right? And
[00:20:43] the
[00:20:45] the arm or the legs moving a particular
[00:20:46] way.
[00:20:47] You can actually write down such
[00:20:49] dynamical models with a bunch of
[00:20:50] equations. This is what classical
[00:20:52] robotics uh is about, and you can use
[00:20:54] this model to do motion planning to some
[00:20:56] extent. It doesn't work that well
[00:20:58] actually for complex actions. But all
[00:21:00] those those videos of, you know, kung fu
[00:21:03] playing robots, that's that's what they
[00:21:04] do. It's all planned in advance using
[00:21:07] handwritten models.
[00:21:09] They're fine-tuned a little bit using
[00:21:11] reinforcement learning and stuff, but
[00:21:12] it's kind of a minor
[00:21:13] minor step. Um
[00:21:16] But then there is the model of the world
[00:21:18] around the robot. Can you predict what,
[00:21:20] you know, other people are going to do,
[00:21:21] you know, whether this object is about
[00:21:24] to fall, you know, going to catch it,
[00:21:26] you know, things like that. So, it's a
[00:21:27] model of intuitive physics. How do you
[00:21:29] learn that? You learn that We learn that
[00:21:31] as babies by watching the world go by.
[00:21:33] And it takes 9 months for a human baby
[00:21:36] to learn gravity, to learn that objects
[00:21:38] that are not supported fall.
[00:21:40] Um 6-month-old babies haven't yet
[00:21:43] integrated the idea that objects, you
[00:21:45] know, don't float in the air.
[00:21:47] Uh
[00:21:48] but 10-month-olds do. You know, the but
[00:21:50] by the by the time they have.
[00:21:51] Uh and so we we acquire in the first few
[00:21:53] months of life all of those basic
[00:21:55] concepts about the world. The world is
[00:21:56] three-dimensional. There are objects
[00:21:58] that can move independently. There are
[00:21:59] you know, objects that, you know, move
[00:22:02] that are not animated, so they follow
[00:22:03] certain rules. There is, you know,
[00:22:05] categories of objects. You don't need to
[00:22:07] give names to them. We know the
[00:22:08] difference between a table and a chair.
[00:22:10] Um you know, and and then there you
[00:22:12] know, objects have inertia, conservation
[00:22:14] of momentum, things like that, right?
[00:22:15] So, we learn this intuitively. Can we
[00:22:18] train a system from video that will
[00:22:21] acquire this type of common sense that,
[00:22:23] you know, animals learn in days and and
[00:22:26] humans months?
[00:22:29] And the answer is yes. So, we have those
[00:22:30] video systems, those Jepa architectures,
[00:22:32] right? And, you know, and we determine
[00:22:34] the level of abstraction at which we
[00:22:35] train them.
[00:22:36] Um so, they learn a representation of
[00:22:38] the video from a window of 64 frames or
[00:22:40] something like this, and
[00:22:42] and they're trained you you take a piece
[00:22:43] of video, you corrupt it
[00:22:45] uh by masking a piece of it, and then
[00:22:47] you run the full video to an encoder,
[00:22:50] run the
[00:22:51] corrupted video to another encoder,
[00:22:54] uh and train a predictor to predict the
[00:22:56] representation of the full video from
[00:22:57] the partially corrupted one.
[00:22:59] Uh and you train the whole thing end to
[00:23:01] end simultaneously, and the system comes
[00:23:03] up with a good abstract representation
[00:23:05] of the world that only contains
[00:23:06] information that is predictable.
[00:23:08] Okay, and it only predicts
[00:23:11] the information the part of the of the
[00:23:13] world that is predictable. It's going to
[00:23:14] ignore all the noise and details of, you
[00:23:17] know, texture of your dress. Uh
[00:23:20] although you should not ignore that
[00:23:21] actually.
[00:23:23] And and you know, and this kind of this
[00:23:26] kind of detail. And so, um
[00:23:30] So, that that's really the the way the
[00:23:32] way to proceed. We've trained these
[00:23:33] models. It's called V-Jepa 2, V for
[00:23:36] video.
[00:23:37] And it was trained on the equivalent of
[00:23:40] 100 years of video.
[00:23:42] That seems like a lot, okay?
[00:23:45] Cuz it doesn't learn as much as a almost
[00:23:47] a human as a 2-year-old.
[00:23:49] >> [laughter]
[00:23:50] >> No.
[00:23:51] Uh so, it doesn't learn for that long.
[00:23:53] And
[00:23:55] um
[00:23:56] and it's not it's not a lot of video.
[00:23:57] It's about It's about a day of YouTube
[00:23:59] uploads. I mean, we we have like
[00:24:01] enormous amounts of video. If you put a
[00:24:03] number on it, it's about um
[00:24:05] 10 to the 15 to 10 to the 16 bytes at 2
[00:24:08] megabytes per second.
[00:24:10] This is
[00:24:11] 100 times more than the biggest LLMs,
[00:24:14] okay? Cuz there's not that much text on
[00:24:16] the internet. It's only about 10 to the
[00:24:17] 14 bytes.
[00:24:19] Um and so, using video, you can train
[00:24:21] with way more data than any LLMs, which
[00:24:24] is why we're never going to get to human
[00:24:25] level intelligence by training LLMs or
[00:24:28] by training on text only, right? We need
[00:24:29] the real world.
[00:24:31] Okay, so you train this system on 100
[00:24:33] years of video, and then we can test
[00:24:34] whether the systems have acquired some
[00:24:36] common sense. So, you show them a video
[00:24:37] where something impossible happens. This
[00:24:39] is, by the way, how we test babies
[00:24:43] to figure out if they've learned a
[00:24:44] particular concept like like like
[00:24:46] gravity. You show babies scenario where
[00:24:49] like a little car is on a on a platform,
[00:24:52] and you push the car off the platform,
[00:24:53] and the car appears to float in the air.
[00:24:56] 6-month-old babies don't pay attention.
[00:24:57] 10-month-olds go like this.
[00:25:00] And I pay attention to it because, you
[00:25:01] know, we're programmed to pay attention
[00:25:03] to
[00:25:04] the violations of our
[00:25:06] prediction of our internal world model.
[00:25:08] That's how That's how we know we have a
[00:25:09] world model. Um and that's how you know,
[00:25:12] psychologists test that. And so, we can
[00:25:14] show a video where something impossible
[00:25:15] occurs, like someone threw a ball in the
[00:25:17] air a ball in the air, and the ball
[00:25:19] stops, or it changes its shape to a
[00:25:20] cube, or it disappears.
[00:25:23] And the prediction error goes to the
[00:25:24] roof
[00:25:25] when you run the model on it
[00:25:27] because it thinks it's like, I didn't
[00:25:29] predict anything like this. That's
[00:25:30] impossible. And so, that's the first
[00:25:32] time I've I've seen
[00:25:33] any kind of model that has some level of
[00:25:35] common sense, and I think it's, you
[00:25:36] know, But before we I think if you run
[00:25:39] it for a a video prediction model,
[00:25:42] it those scenarios, as as you say, if
[00:25:44] you have the starting position and you
[00:25:45] see it happen, you could also run it at
[00:25:48] a full pixel level, and you would you
[00:25:50] would probably very nicely also there be
[00:25:52] able to measure that suddenly there's a
[00:25:53] discrepancy with what your video model
[00:25:56] predicts and what
[00:25:58] um you know, like what you see in the
[00:26:00] video.
[00:26:01] I hope you'll pardon my French, but
[00:26:03] absolutely no way in hell.
[00:26:05] No, I I I don't agree. Like I think so I
[00:26:07] think so if you if you have the starting
[00:26:09] the starting, you know, point of the
[00:26:10] video, and you run from that frame, you
[00:26:13] run it forward, so you have a few
[00:26:15] frames, and you run it forward the video
[00:26:16] model, you will suddenly see that
[00:26:18] there's a big deviation between what you
[00:26:19] predict at the pixel. No, it's only
[00:26:21] because you have the starting frame and
[00:26:23] and this and that, but you could also
[00:26:24] predict. Now, I agree with you that this
[00:26:26] is like complete overkill for the task,
[00:26:28] but I think you can also do it. You can
[00:26:30] essentially do it up to the level that
[00:26:32] you are you don't have enough
[00:26:33] abstraction anymore.
[00:26:34] >> It simply does not work.
[00:26:36] We've tried to do this. I've tried to do
[00:26:38] self-supervised learning from video for
[00:26:39] 15 years. The first 10 years I tried to
[00:26:41] use generative models with latent
[00:26:42] variables, okay? And the best method
[00:26:45] that we have to do this today is
[00:26:46] diffusion models. And with this, you
[00:26:48] know, you can produce good videos.
[00:26:49] There's no question. Uh it never worked
[00:26:51] for natural videos. It worked for
[00:26:53] stylized videos like video games,
[00:26:56] um you know, basically already abstract
[00:26:58] representations of video or like
[00:26:59] segmentation maps, you know, to some
[00:27:01] extent. But it never really worked, and
[00:27:02] the reason it doesn't work is because
[00:27:04] there is an infinite number of plausible
[00:27:05] things that can happen in a video. And
[00:27:07] when you train the system to make
[00:27:08] predictions at the pixel level, the best
[00:27:11] thing it can do, it can't represent a
[00:27:13] distribution over all possible frames.
[00:27:14] And so, the best thing it can do is,
[00:27:16] uh you know, produce an average of all
[00:27:18] the possible futures. So, if you use
[00:27:19] diffusion models, you get around that
[00:27:20] problem, but not entirely because the
[00:27:23] your predictor can be completely wood
[00:27:25] collapsed. So, it will produce a nice
[00:27:26] video, but it's not going to understand
[00:27:28] the underlying dynamics. So, um why do
[00:27:31] we know this? We know this because we
[00:27:33] have lots and lots of empirical evidence
[00:27:35] of training generative models for
[00:27:39] image representation. Okay, so there is
[00:27:40] a very good example, which works great
[00:27:43] for text, doesn't work for images. I
[00:27:44] mean, it works, but not well. You take a
[00:27:47] you take a piece of data, you corrupt it
[00:27:48] by masking a piece of it, similar to
[00:27:50] what I was describing earlier, and then
[00:27:52] you train
[00:27:53] some big model, basically an
[00:27:55] autoencoder, to reconstruct the the full
[00:27:59] input, whether it's text or images. In
[00:28:01] the context of NLP, that's called BERT.
[00:28:03] In the context of images, that's called
[00:28:05] MAE, masked autoencoder.
[00:28:07] Um and you do get some representation of
[00:28:11] the text or the image. For images,
[00:28:13] though, it's very expensive to train,
[00:28:15] and the representation you get out of it
[00:28:17] sucks. It really doesn't work very well.
[00:28:19] The stuff that the method that produced
[00:28:21] the best image representations are all
[00:28:24] joint embedding architectures, which
[00:28:26] means architectures that are trained
[00:28:28] without a a criterion that attempts to
[00:28:31] reconstruct pixels. You have to allow
[00:28:33] the system to ignore information that
[00:28:36] cannot be predicted. And if you put a
[00:28:39] reconstruction criterion, it will have
[00:28:40] to reconstruct everything, and you kill
[00:28:42] it by doing it. And we know this. We
[00:28:44] have lots of comparisons of MAE with
[00:28:46] DINO, so you know about DINO.
[00:28:48] Uh probably the best method for
[00:28:50] self-supervised learning of image
[00:28:51] representation. Probably the best method
[00:28:53] for feature extraction,
[00:28:56] you know,
[00:28:58] Mhm.
[00:28:59] Whatever, right? Whatever method you
[00:29:01] use,
[00:29:01] uh it this beats supervised learning
[00:29:03] now, right? Self-supervised learning for
[00:29:05] images with joint embedding architecture
[00:29:07] beat
[00:29:08] all approaches to supervised learning,
[00:29:10] even those for which we have tons of
[00:29:11] data. Uh this is new. Only happened in
[00:29:13] the last year. Um so, DINO is one of
[00:29:15] them. I-Jepa is another one. Uh I mean,
[00:29:18] there's a bunch of you know, a small
[00:29:20] number of methods like this that,
[00:29:22] you know, beat
[00:29:23] generative approaches for image
[00:29:25] representation, and there's tons of
[00:29:27] benchmarks for which we have images. So,
[00:29:29] we I started realizing this about 5
[00:29:31] years ago, and basically started, you
[00:29:34] know, kind of
[00:29:36] bashing generative models and completely
[00:29:38] kind of try to brainwash everyone into
[00:29:40] abandoning
[00:29:41] generative AI, which is difficult
[00:29:44] because, you know, everyone talks about
[00:29:45] generative AI as
[00:29:47] the thing.
[00:29:48] Uh it didn't make me very popular among
[00:29:50] some of my colleagues who work on LLMs.
[00:29:53] So,
[00:29:54] um you know, so so coming back to um
[00:29:57] to to trying to solve robotics,
[00:30:00] uh you mentioned a little bit uh
[00:30:02] reinforcement learning. Um you know,
[00:30:04] there are there's uh
[00:30:06] you know, big fan of unsupervised
[00:30:08] learning. There's also supervised
[00:30:09] learning. Let's say in the mix of those
[00:30:11] different things like um you know,
[00:30:15] they probably have to work together in
[00:30:16] some way, right? Like you you want to
[00:30:19] figure out how the world work, probably
[00:30:21] unsupervised.
[00:30:22] Uh you want to learn how to kind of do
[00:30:25] some tasks. That's probably has some
[00:30:27] supervisory signal for sure.
[00:30:29] Um and then, you know, reinforcement
[00:30:31] learning is probably the thing that
[00:30:32] actually gets it all to kind of you
[00:30:33] know, fine-tune and the kind of all the
[00:30:35] the actual moving parts of the robot and
[00:30:38] and so on. So, how how would you kind of
[00:30:40] see those things coming together? So,
[00:30:41] about 10 years ago, uh
[00:30:43] whenever I give a uh talk, I would show
[00:30:46] a slide with a cake.
[00:30:47] All right? I'm sure some of you have
[00:30:49] seen it. Who has seen the cake?
[00:30:53] Okay, great.
[00:30:54] Uh that was about 10 years ago, and the
[00:30:56] cake is an analogy.
[00:30:58] I was trying to make the point.
[00:31:00] Everybody at the time was like
[00:31:01] completely into reinforcement learning.
[00:31:02] I was telling people like reinforcement
[00:31:03] learning is so inefficient in terms of
[00:31:05] samples.
[00:31:07] It's never going to amount to much. Um
[00:31:09] except for games. Cuz for games, you can
[00:31:11] generate so much data that it's fine.
[00:31:13] Uh and that turned out to be true. Okay,
[00:31:15] so the bulk of the cake, the genoise of
[00:31:18] the cake, if you want,
[00:31:20] is self-supervised learning. You learn
[00:31:21] about the world, you learn to represent
[00:31:22] it, you learn world models, you learn
[00:31:24] prediction. Um that's self-supervised.
[00:31:28] You don't need to
[00:31:29] observe an expert, you don't need to
[00:31:31] learn from anyone else. You just observe
[00:31:33] the world go by. Okay?
[00:31:35] Um that's the bulk of it. Most of your
[00:31:37] parameters or whatever, your
[00:31:39] intelligence, most of what you learn,
[00:31:40] you learn this way.
[00:31:41] Then there is a thin
[00:31:42] >> And by the way, that would also be
[00:31:44] embodiment agnostic. It would be yeah.
[00:31:46] Yeah.
[00:31:47] Um then there is a thin layer of either
[00:31:50] supervised learning or imitation
[00:31:51] learning or behavior cloning or inverse
[00:31:54] reinforcement learning. There's several
[00:31:55] names for it, but it's basically trying
[00:31:57] to imitate or reproduce
[00:32:00] uh
[00:32:00] behavior of an expert, right? Or human.
[00:32:03] Um that's a thin layer. Um
[00:32:06] Most animals never go to that phase
[00:32:09] because they never meet their parents.
[00:32:10] >> [laughter]
[00:32:11] >> So,
[00:32:12] um [snorts] like octopus never meet
[00:32:14] their parents. They get really smart in
[00:32:15] just a few months. They live only 2
[00:32:17] years. Um and then there is the cherry
[00:32:19] on the cake, and that's reinforcement
[00:32:20] learning. It's just like minor
[00:32:22] fine-tuning because it's so inefficient.
[00:32:24] Like if you if you were to train a
[00:32:26] self-driving car from scratch to learn
[00:32:28] to drive,
[00:32:29] it's completely impractical. People
[00:32:31] thought this was a possibility, you
[00:32:32] know, back then 12 years ago.
[00:32:34] Um and realized quickly that that was
[00:32:37] completely impractical. Um it would
[00:32:39] require too many trials. A car, you
[00:32:41] know, driving next to a cliff would have
[00:32:43] to run off the cliff a few dozen times
[00:32:45] before realizing it's a bad idea. And
[00:32:47] then a few other dozen times very
[00:32:49] dangerous in Switzerland. Um
[00:32:51] you know,
[00:32:52] and then a few more dozen times to
[00:32:53] realize how to not run off that cliff.
[00:32:56] And then you're next to another cliff,
[00:32:58] and you have to do it again, right?
[00:32:59] Because it doesn't necessarily transfer
[00:33:01] to the new situation. So,
[00:33:03] you know,
[00:33:04] reinforcement learning would work if I
[00:33:05] learned at the right abstraction level,
[00:33:06] you might have been able to generalize.
[00:33:07] Yeah, but then this abstraction level is
[00:33:09] given to you by self-supervised
[00:33:10] learning, right? So, Yeah, but you can
[00:33:11] build on top of it, let's say, like
[00:33:13] Sure. Yeah. No, I mean, it's it's
[00:33:14] necessary, right? I mean, clearly we
[00:33:16] adjust our behavior uh you know, from
[00:33:19] you know, action that we do in the world
[00:33:20] and we realize we're not doing it right.
[00:33:21] So, yeah, that that's a required cherry,
[00:33:24] but it's only a minor But then, you
[00:33:26] know, I have some colleagues that are
[00:33:28] kind of big in reinforcement learning
[00:33:29] and and um and the way they do it is
[00:33:31] they use simulation to do it. And of
[00:33:32] course, you know, there's still a little
[00:33:33] bit of a gap,
[00:33:35] but you know, they get kind of robots
[00:33:37] with all kinds of things kind of they
[00:33:38] figure out their their gait and this and
[00:33:40] that and they you know, and then of
[00:33:41] course, there's the gait of just walking
[00:33:43] on a flat surface, that's pretty you
[00:33:44] could design that.
[00:33:45] But then, they also figure out how to
[00:33:47] kind of crawl in very interesting ways,
[00:33:49] you know, from over things and so on.
[00:33:51] So, simulation is a thing that a little
[00:33:52] bit decouples that cost. There's still a
[00:33:54] cost to simulation, but it's not the
[00:33:55] same cost as actually throwing the robot
[00:33:57] off the you know, off the
[00:33:58] you know, the [snorts] bricks or you
[00:33:59] know, down the cliff or whatever, right?
[00:34:01] I mean, for any particular set of task
[00:34:04] or domain
[00:34:05] or engineering problem, you're going to
[00:34:07] have a very specific solution to it
[00:34:09] that's going to you know, solve the
[00:34:10] problem. Uh which is why, you know, we
[00:34:12] have you know,
[00:34:14] 30 30 year old gadgets that can beat us
[00:34:16] at chess,
[00:34:18] uh but they're not necessarily
[00:34:19] intelligent, right? Um so,
[00:34:21] same thing same thing here, right? We
[00:34:23] can we can cheat our way out or we can
[00:34:25] engineer the hell out of it. Uh and you
[00:34:28] know, solve problems of this type. So, I
[00:34:31] mean, to train a set of reinforcement
[00:34:32] learning to control a humanoid robot,
[00:34:34] you basically have to simulate thousands
[00:34:35] of copies of that humanoid robot in in
[00:34:38] parallel on supercomputers and have them
[00:34:40] do all kinds of stuff. And still in the
[00:34:42] end,
[00:34:42] >> Thousands you might do on one GPU, but
[00:34:43] That's right. Possibly. Maybe well
[00:34:46] well, not if you have perception. That
[00:34:47] would be more expensive, but uh
[00:34:49] but you know, in the end, it will only
[00:34:51] be trained for this particular task,
[00:34:52] this particular environment, and you
[00:34:54] know, it'll be be brittle. A much more
[00:34:56] efficient way to approach this is is
[00:34:57] this idea of training world models. So,
[00:35:00] you know,
[00:35:01] ask a 10 year old
[00:35:04] who's never done it before to accomplish
[00:35:06] a new task. And you know, 10 year old
[00:35:08] tend to accomplish new tasks pretty
[00:35:10] often. But like, you know, ask a 10 year
[00:35:11] old to clear the dinner table and fill
[00:35:14] up the dishwasher. 10 year old can do it
[00:35:15] the first time. Doesn't need to be
[00:35:17] trained for it.
[00:35:18] Um
[00:35:19] you know, it might become more efficient
[00:35:22] at doing it if you if it you know, does
[00:35:24] it multiple times, but can do it the
[00:35:26] first time. Why? Because of a world
[00:35:28] model.
[00:35:29] Um same thing for the
[00:35:32] you know, 17 year old learning to drive.
[00:35:34] The world model allows the 17 year old
[00:35:37] to predict that
[00:35:38] you know, if you're driving next to a
[00:35:40] cliff and turn the turn the wheel to the
[00:35:42] right, the car will run off the cliff
[00:35:44] and nothing good will come out of this.
[00:35:46] That's the that's a world model. That's
[00:35:48] what allows us to solve a new task zero
[00:35:50] shot without being trained
[00:35:52] or to learn new tasks like driving
[00:35:54] extremely quickly or skiing, right? Same
[00:35:56] thing.
[00:35:57] Uh first time you ski, you're kind of
[00:35:58] hesitant and you kind of think about
[00:36:00] everything you're supposed to do, and
[00:36:02] then you become familiar and it becomes
[00:36:04] kind of second nature, but that's the
[00:36:05] second phase, right? That's the
[00:36:07] difference that
[00:36:08] uh psychologists call this system one
[00:36:10] and system two. System one is tasks that
[00:36:11] you can accomplish automatically without
[00:36:13] thinking. System two is you use your
[00:36:15] mental world model, that's all your
[00:36:16] prefrontal cortex essentially. Um and
[00:36:19] then you accomplish uh you can plan what
[00:36:22] actions and you accomplish that task.
[00:36:25] So, for you know, unsupervised learning,
[00:36:28] I think you can you know, you can learn
[00:36:30] from corpus of data, kind of understand
[00:36:32] how the world works and so. But still
[00:36:33] translating that to a particular
[00:36:35] embodiment,
[00:36:37] um there are challenges there, right?
[00:36:39] Like because there you don't have an
[00:36:41] unlimited amount of data anymore to kind
[00:36:42] of just learn basic principles of how
[00:36:44] the world functions and so on. So,
[00:36:46] so how do you see that kind of
[00:36:48] connection to the specific embodiment uh
[00:36:51] to the you know, like people train
[00:36:53] something on one embodiment and then
[00:36:55] they have to transfer to another
[00:36:56] embodiment, and you know, you have to
[00:36:58] start all over. So, like not for
[00:37:00] understanding the world, but for
[00:37:01] understanding how you kind of do
[00:37:02] something in the world. Okay, so here's
[00:37:04] the experiment we did with V-JEPA 2.
[00:37:07] And we have a new version coming out,
[00:37:08] V-JEPA 2.1,
[00:37:10] soon. So, V-JEPA 2, you you pretrain on
[00:37:14] these 100 years of natural videos,
[00:37:16] right? And the system learns to
[00:37:17] represent video, it learns to fill in
[00:37:18] the blanks in the video. That's the
[00:37:20] first phase. Now you have a really good
[00:37:22] representation of uh
[00:37:24] of of you know, physical reality and a
[00:37:27] good abstract representation and an
[00:37:28] ability to predict, but not action
[00:37:31] conditioned. So, it's not related to any
[00:37:32] particular embodiment or you know,
[00:37:34] there's no robot arm the system is
[00:37:36] controlling. So, there's a second phase
[00:37:38] where you fix the encoder
[00:37:40] and you fine-tune the predictor and you
[00:37:42] add an input, which is an action, right?
[00:37:44] So, you have
[00:37:46] position of the robot and state of the
[00:37:49] world
[00:37:50] and action that you observe um or that
[00:37:53] you
[00:37:54] send to the robot, and then you observe
[00:37:56] the state of the world and the robot uh
[00:37:58] right after. That requires
[00:38:01] two sub models, a model of the robot
[00:38:03] itself and a robot of the environment
[00:38:04] and then maybe a model of the robot
[00:38:06] itself, a model of the environment
[00:38:09] cuz the environment might evolve by
[00:38:10] itself, and maybe a model of the
[00:38:11] interaction between the two, right? So,
[00:38:13] if I if I move my hand here and I
[00:38:16] close my hand, nothing happens. Okay?
[00:38:19] That's completely under my control. But
[00:38:20] if I move it next, you know, around the
[00:38:23] the glass and I close my hand, now I
[00:38:24] pick up the glass. So, that's an
[00:38:25] interaction between the environment and
[00:38:27] the the thing you the system
[00:38:29] has to model all that. Now, it turns out
[00:38:31] that fine-tuning phase where you have
[00:38:33] state, action, next state, does not
[00:38:36] require that much data.
[00:38:37] And the data you can obtain through
[00:38:40] simulation.
[00:38:41] But it's not a simulation of a task, a
[00:38:42] simulation of just the dynamics of a
[00:38:44] system. So, you don't need a huge amount
[00:38:46] of data. And the model that you get at
[00:38:48] the end is generic, you can use it for
[00:38:50] any task. So, now you can use that for
[00:38:52] planning
[00:38:53] motion of a robot to actually pick up a
[00:38:55] glass or or pour water into a glass, and
[00:38:58] then actually works.
[00:39:00] So,
[00:39:01] I switch to something something else,
[00:39:02] like I want to
[00:39:04] first go back in time
[00:39:06] to you know, when computer vision
[00:39:08] started working, at least you know, the
[00:39:10] geometric parts are working long before
[00:39:11] that, but let's say the semantic
[00:39:12] understanding of the world. Uh I would
[00:39:14] say that's essentially you know, CNNs
[00:39:16] started making that work
[00:39:18] about 15 years ago.
[00:39:20] Um the
[00:39:22] um
[00:39:23] you know, so there we had a very useful
[00:39:26] clear inductive bias
[00:39:28] of hey, you know, like if I see
[00:39:30] something here or there, it doesn't
[00:39:32] matter. I want the same filters, the
[00:39:33] same thing, the same understanding.
[00:39:35] So,
[00:39:36] are there things like this?
[00:39:39] Um you You then then there's also of
[00:39:41] course, uh what is it? The the the the
[00:39:43] bitter lesson that's saying like forget
[00:39:45] all of that, you know, like if I see a
[00:39:46] cat up there, it's probably like a
[00:39:48] floating cat. So, it's something very
[00:39:49] different than when I see it. I should
[00:39:51] not see a cat up there. So, I suppress
[00:39:52] that and so I don't want the same
[00:39:53] filters up there than I want them down
[00:39:54] there and and stuff like that. And so,
[00:39:56] eventually if you have enough data,
[00:39:58] you know, like forget about all these
[00:40:00] inductive biases and so on.
[00:40:02] On the other hand, I'm very frustrated
[00:40:04] in robotics, you know, like this is now
[00:40:06] with relay and stuff like that also, but
[00:40:08] you know, indeed a big part of the field
[00:40:09] is like, "Okay, I've trained this relay
[00:40:11] with like a camera up here and like my
[00:40:13] arm is exactly up there and this exact
[00:40:15] configuration. And actually, by the way,
[00:40:17] I have a fixed background. Nobody can,
[00:40:18] you know, this wouldn't work here. I
[00:40:20] need the exact background, the exact
[00:40:21] pixel, by the way, indeed in their cases
[00:40:23] often, which is completely, but
[00:40:25] um
[00:40:26] but essentially, um
[00:40:29] you know, a lot of that is essentially
[00:40:31] perfectly predictable with, you know, we
[00:40:33] have methods to kind of, you know,
[00:40:35] [snorts] transfer that to predict it and
[00:40:36] so on. Um
[00:40:37] Where do you see the, you know, like the
[00:40:40] you know, are there inductive biases
[00:40:42] similar to what we had with, um you
[00:40:45] know, with with the convolutional kind
[00:40:47] of um shift invariance essentially that
[00:40:49] we're bringing in? Like are there
[00:40:50] similar things that you see on the
[00:40:52] horizon or like things that could be
[00:40:53] applicable for the things we're trying
[00:40:54] out now in embodied AI?
[00:40:56] So, you you can always, as you say, you
[00:40:58] can always uh replace
[00:41:01] inductive biases in your architecture or
[00:41:04] prior knowledge in your architecture
[00:41:06] like, you know, convolutional nature
[00:41:08] >> [snorts]
[00:41:08] >> um
[00:41:10] by more data.
[00:41:12] And if your training is mostly
[00:41:13] self-supervised, perhaps
[00:41:15] you know, you have essentially from
[00:41:16] video, you have an infinite supply of
[00:41:18] data. You have more data than you can
[00:41:20] you can you can you can manage.
[00:41:22] Uh so, maybe there are the
[00:41:24] the type of
[00:41:26] uh prior knowledge that we, you know,
[00:41:27] put into encoders like like the
[00:41:30] convolutional nature
[00:41:32] are no longer necessary. And we see
[00:41:33] this, you know, in the
[00:41:35] Okay, here's an interesting uh
[00:41:37] uh piece of data.
[00:41:39] The
[00:41:40] in the academic world, in the
[00:41:41] publications,
[00:41:43] uh the the best computer vision systems,
[00:41:46] most of the papers use transformers,
[00:41:49] vision transformer VITs, or some
[00:41:51] variation variation of it.
[00:41:53] Uh
[00:41:54] video not quite the case because
[00:41:56] transformers on video start to become
[00:41:58] really expensive if you want to do high
[00:41:59] resolution.
[00:42:01] Um but
[00:42:03] you can get the same performance with
[00:42:04] convolutional nets.
[00:42:06] And you will get it with less data. But
[00:42:08] if you have data, why would you kind of
[00:42:12] you know, take the risk of getting a
[00:42:13] lower performance. And also, there is uh
[00:42:15] work by very interesting work by my NYU
[00:42:18] colleague, former fair colleague
[00:42:19] actually, Saining Xie, uh
[00:42:21] uh something called ConvNeXt. So, he is
[00:42:23] sort of carefully fine-tuned the all the
[00:42:25] tricks, you know, in the convolutional
[00:42:27] net
[00:42:28] uh transposing some of the tricks that
[00:42:29] are used in transformer and say, "Look,
[00:42:30] you know, you actually get, you know,
[00:42:32] the same performance with ConvNeXts as
[00:42:33] you do with transformers if you do all
[00:42:35] the right tricks if you send the spend
[00:42:37] the same amount of effort on them." So,
[00:42:38] it's not there's nothing really
[00:42:39] intrinsic uh about the architecture
[00:42:41] there,
[00:42:42] uh at least for images and certainly for
[00:42:44] video.
[00:42:45] Um the thing is it starts getting
[00:42:47] impractical
[00:42:48] when you deal with video. If you have,
[00:42:50] you know, high resolution video, um high
[00:42:52] frame rate, then the number of tokens
[00:42:54] that you need to feed to your
[00:42:56] transformer for that becomes sort of
[00:42:58] impractically large. And so, then the
[00:43:00] computation is ridiculous. And here is a
[00:43:02] piece of data that's important. Every
[00:43:04] single real-time vision system uses
[00:43:08] convolutional nets. They don't use
[00:43:09] transformers. Your car, your
[00:43:11] self-driving car has in Europe, every
[00:43:13] car sold in Europe has to have a
[00:43:15] uh automatic emergency braking system.
[00:43:18] And it's a camera looking at the
[00:43:19] windshield uh that stops the car when
[00:43:21] there is an obstacle. Most of them have
[00:43:23] something that allows you to drive more
[00:43:25] or less automatically on the highway.
[00:43:27] Every single one of them uses
[00:43:28] convolutional net. Every single one of
[00:43:29] them. Because you need real time and
[00:43:31] you're not going to get that from
[00:43:32] transformers.
[00:43:33] At least not today.
[00:43:36] So, um
[00:43:37] you know, if we look at, you know, we're
[00:43:40] also embodied, obviously. Um we have
[00:43:42] our, you know, our brain up there that's
[00:43:45] helping us figure out how to act in the
[00:43:47] world.
[00:43:48] We're using, you know, whatever 20 watts
[00:43:50] of power for doing that. Um
[00:43:53] I think part of it is really to have a
[00:43:55] very adaptive, you know, level at which
[00:43:57] we actually read out the, you know, like
[00:43:59] abstraction level um
[00:44:01] um and so on. But like what do you see
[00:44:04] on the horizon? What are the kind of
[00:44:05] things that can bring us to or what is
[00:44:07] still missing actually? What what are
[00:44:09] the things that we should as a maybe
[00:44:10] research community really focus on uh to
[00:44:13] to to, you know, to get to something
[00:44:15] like that? It's a hardware issue. It's a
[00:44:17] it's actually a device issue. It's not
[00:44:20] just uh you know, computer architecture
[00:44:22] issue.
[00:44:22] >> the algorithms are solved?
[00:44:24] I mean, I think the algorithms are are
[00:44:26] not the issue the main issue for like
[00:44:29] power consumption. Here is the problem.
[00:44:32] Um
[00:44:33] the in the brain,
[00:44:35] The weights are in place. Uh The weights
[00:44:37] are in place. The weights are in place,
[00:44:39] right? Exactly. So,
[00:44:41] uh in the brain, you
[00:44:43] you know, the number of parameters in a
[00:44:45] neural net is like a synapse in the
[00:44:46] brain. It's not quite the same analogy,
[00:44:48] but let's let's make this assumption,
[00:44:50] right?
[00:44:51] Um
[00:44:53] So, we have one physical synapse and one
[00:44:55] physical [snorts] neuron per
[00:44:59] virtual neuron, if you want. Okay. Um
[00:45:03] Whereas in a computer implementation of
[00:45:05] a neural net or deep learning system,
[00:45:08] we reuse the same
[00:45:10] piece of hardware, the same silicon, to
[00:45:13] compute the output of multiple neurons
[00:45:15] and multiple synapses.
[00:45:17] Okay? So, what that means and the reason
[00:45:19] we need to do this is because our
[00:45:20] fabrication technology is too big and
[00:45:22] too fast.
[00:45:23] So, we have to use what's called
[00:45:25] hardware multiplexing. You have to reuse
[00:45:26] the same piece of hardware to compute
[00:45:28] multiple parts of of the neural net.
[00:45:32] And what that means is that you have to
[00:45:33] get data from memory and shuffle it
[00:45:35] through the
[00:45:37] computational engine,
[00:45:38] right? And put the result back to
[00:45:40] memory.
[00:45:41] All the energy, all the power is spent
[00:45:44] getting data from the memory and writing
[00:45:45] it back.
[00:45:46] So, the difference between a classical
[00:45:49] CPU and the GPUs that are optimized for
[00:45:53] for for neural nets is that the GPUs
[00:45:56] have this kind of hierarchical memory
[00:45:58] that allows to kind of minimize the
[00:45:59] amount of traffic to memories that is
[00:46:02] far away and slower so that you you save
[00:46:05] quite a bit of energy, but you cannot
[00:46:08] with current technology, you simply
[00:46:09] cannot
[00:46:10] have
[00:46:12] one computing device per neuron or
[00:46:15] synapse in your neural net.
[00:46:17] You would have to go to like some sort
[00:46:19] of exotic analog technology for this
[00:46:21] which does not exist, you know, it might
[00:46:22] pop up in the future. It could be
[00:46:24] spintronics, it could be carbon
[00:46:26] nanotubes, it could be, you know,
[00:46:28] whatever some optical widget, but it
[00:46:31] doesn't exist at the moment. If you're
[00:46:32] going to use CMOS, the technology is too
[00:46:35] big and too fast and you have to reuse
[00:46:36] the same piece of hardware for different
[00:46:38] parts of your neural net. You have to
[00:46:39] shuffle data. That's where all your
[00:46:41] energy is going to go. So, in other
[00:46:42] words, if we could have an analog
[00:46:44] asynchronous
[00:46:46] three-dimensional stacking of elements,
[00:46:47] we might actually get there. Yeah, and
[00:46:50] uh you know, possibly.
[00:46:52] And it would have to be
[00:46:54] it wouldn't have to be as fast as our
[00:46:55] current electronics because it would be
[00:46:57] massively parallel and way more than
[00:46:59] current systems. But you would need to
[00:47:01] >> do we run at? Uh we run at like 10
[00:47:04] hertz. Okay. In the sense of your retina
[00:47:08] works at about 15 hertz, which is why,
[00:47:10] you know, cinema is at 24 frames per
[00:47:13] second because you can't see
[00:47:15] you know,
[00:47:16] uh you you perceive the frames as
[00:47:18] motion, right? Uh
[00:47:20] And and the the whole process of going
[00:47:22] from your retina to your if
[00:47:24] inferotemporal cortex or your motor
[00:47:25] cortex for reacting to a visual stimulus
[00:47:28] is is 100 milliseconds for perception,
[00:47:30] another 100 milliseconds to figure out
[00:47:32] what to do. So, your your feedback loop
[00:47:34] when you
[00:47:35] see an obstacle in the street and you
[00:47:36] need to brake, you know, hit the brake
[00:47:38] pedal for your for your car, that's like
[00:47:39] 300 milliseconds, a third of a second.
[00:47:41] Incredibly slow.
[00:47:42] Uh cats are faster.
[00:47:45] Okay, which is why because they have
[00:47:46] small brains, which is why, you know,
[00:47:48] they can stand in front of a cobra and
[00:47:50] when the cobra starts to attack, they go
[00:47:52] boom, right? We can't do this as humans.
[00:47:54] We're just too slow. Um so, uh
[00:47:58] you know, we we're going to require some
[00:48:00] some non-volatile memory storage
[00:48:03] technology that is incredibly compact,
[00:48:06] right? We're talking like, you know,
[00:48:08] nanometers for
[00:48:09] you know, a single analog memory type
[00:48:12] thing.
[00:48:13] Which, you know, biology figured out how
[00:48:14] to do, but we don't know what to do what
[00:48:16] to do with current fabrication.
[00:48:18] >> other part, so that would be like, you
[00:48:19] know,
[00:48:20] potentially like a frozen brain or
[00:48:22] something, right? A key thing about us
[00:48:24] is we can adapt. We can keep adjusting.
[00:48:26] We don't have to first learn and then,
[00:48:28] you know, infer. Well, this this thing
[00:48:30] would be would have to be,
[00:48:32] you know, to learn in the loop. In fact,
[00:48:34] there is this concept that people were,
[00:48:35] you know, kind of thinking of in the
[00:48:37] 1980s and and 90s where people were
[00:48:39] working on analog neural net
[00:48:40] implementations.
[00:48:42] And it was
[00:48:44] the fact that when you start to get to
[00:48:46] these small devices, the characteristic
[00:48:48] of each device is different.
[00:48:50] Um you have a lot of variability from
[00:48:52] one device to a to another on a single
[00:48:53] chip. And so, you can't just program the
[00:48:56] system with, you know, known weights
[00:48:58] that have been trained offline
[00:49:00] uh because the characteristic of the
[00:49:02] components uh vary so much. And so, you
[00:49:04] have to train the system in the loop
[00:49:06] with the characteristic of the of of the
[00:49:08] chip itself, which means that that
[00:49:11] system is not reproducible. It's unique.
[00:49:14] It's it's mortal, if you want. Okay?
[00:49:17] Like like human brain, you can't copy a
[00:49:20] make another copy of human brain.
[00:49:22] So, so
[00:49:24] okay. So, so, you know, like so
[00:49:26] essentially, what do you see on the
[00:49:27] like, you know, is there anything out
[00:49:29] there on the horizon where, you know,
[00:49:31] not not back to the hardware in in in
[00:49:32] the 80s or so, but more in in
[00:49:34] algorithmically of of bringing learning
[00:49:36] in the loop. Uh for you know, for
[00:49:39] embedded systems or for systems that act
[00:49:40] in the world and have to keep adjusting
[00:49:42] and also
[00:49:44] partially also based on their own um you
[00:49:46] know, like if we get hurt and then you
[00:49:49] know, like we can actually adapt and we
[00:49:50] change our gait a bit and this and that
[00:49:52] and so on. Um
[00:49:54] what's what's what's there? Like can we
[00:49:57] expect to see kind of learning systems
[00:50:00] in the loop essentially coming
[00:50:01] >> I think the answer is clearly yes and I
[00:50:03] actually don't think it's particularly
[00:50:05] challenging conceptual
[00:50:07] uh problem. I mean, I don't think we
[00:50:08] need to invent anything new to be able
[00:50:10] to do you know, online adaptation. We do
[00:50:13] this all the time, right? If
[00:50:15] uh
[00:50:15] you know, you
[00:50:17] you know, you you you try to pick up a
[00:50:19] pick up an object and you realize the
[00:50:21] object is like way heavier than you
[00:50:22] realize. This is actually way heavier
[00:50:24] than I thought.
[00:50:25] >> [laughter]
[00:50:26] >> It's like pretty thick glass actually.
[00:50:29] Um
[00:50:31] and you know, you immediately adapt.
[00:50:33] Your world model that predicted like you
[00:50:34] know, how how much force you had to
[00:50:36] apply to lift this object
[00:50:38] you know, adapts in milliseconds. This
[00:50:39] is done actually most probably possibly
[00:50:42] not entirely clear but probably in the
[00:50:43] cerebellum. Cerebellum is a
[00:50:45] very special
[00:50:47] piece of the brain that actually has
[00:50:49] most of our neurons in a in a human
[00:50:50] brain actually in the cerebellum not in
[00:50:52] the cortex.
[00:50:53] Uh
[00:50:53] it's like 50 million neurons in the
[00:50:55] cerebellum only 16 million in the cortex
[00:50:57] which is weird.
[00:50:58] Uh but they you know, mostly the the
[00:51:00] theories about the cerebellum is fast
[00:51:02] adaptation to kind of changing
[00:51:04] situations. So
[00:51:06] again also when we observe something
[00:51:07] that violates our internal model of the
[00:51:09] world, we're programmed to pay attention
[00:51:11] to it because you know, we need to learn
[00:51:13] from it.
[00:51:14] Cuz that means our world model was
[00:51:15] inaccurate. Also, it could be a tiger
[00:51:17] jumping at us, right? That we didn't
[00:51:19] foresee. It can kill us, right? So we
[00:51:21] have to pay attention to
[00:51:23] uh distortion from prediction. So that's
[00:51:25] the cherry, right? That's not the
[00:51:27] cherry. That's the adjustment of your
[00:51:29] world model. It's not supervised. It's
[00:51:30] completely self-supervised. This is not
[00:51:32] related to a task.
[00:51:33] >> That's reinforcement learning, right?
[00:51:34] It's not reinforcement learning.
[00:51:35] Absolutely not. It's self-supervised
[00:51:37] learning. It's Okay, I observe something
[00:51:39] going on in the world and my prediction
[00:51:41] was wrong and now I wait a little. I
[00:51:43] observe what actually occurred. I adjust
[00:51:46] my prediction my predictor. You know,
[00:51:47] it's a Jeff architecture. There's no
[00:51:49] task to accomplish. There's no
[00:51:50] reinforcement. There's no value
[00:51:51] function. Nothing like that. Just
[00:51:53] prediction error.
[00:51:54] Okay? And you adapt your your model and
[00:51:57] that's generic. It doesn't it's not task
[00:51:59] dependent. Welcome to the AI House
[00:52:02] Davos.
[00:52:03] Our next panel on the summit stage will
[00:52:05] begin in 15 minutes. Okay, we still have
[00:52:08] I guess I guess we have some time.
[00:52:10] >> [laughter]
[00:52:11] >> Okay, so anyways, I think we have to
[00:52:13] wrap it up. So so maybe to finish um
[00:52:15] where do you see things like 10 years
[00:52:17] from now? Like in in embodied AI in
[00:52:19] particular, right? In terms of robots,
[00:52:20] in terms of what what can they do and
[00:52:24] what's still out what's still unsolved?
[00:52:26] So I'm I'm just you know, starting a a
[00:52:28] new very ambitious company
[00:52:30] uh with the idea that we're going to be
[00:52:32] able to solve that problem within a few
[00:52:34] years and basically have systems that
[00:52:36] understand the physical world or any
[00:52:37] modality you throw at them
[00:52:39] um can build world models, can use those
[00:52:41] world models to plan,
[00:52:42] uh can build hierarchical world models,
[00:52:44] so you can do hierarchical planning Mhm.
[00:52:45] and then basically be the blueprint for
[00:52:48] the future
[00:52:50] AI systems um that are much more
[00:52:52] powerful than you know, LLMs that we
[00:52:54] have currently. It's completely
[00:52:56] different paradigm, non-generative as I
[00:52:58] said because it's those Jeff
[00:52:59] architectures. Um
[00:53:01] not
[00:53:02] not using autoregressive token
[00:53:03] prediction but using planning. Okay, so
[00:53:06] systems that can predict the
[00:53:07] consequences of their actions which I
[00:53:08] think is the only
[00:53:10] decent way to build agentic systems
[00:53:13] uh except for real world applications.
[00:53:15] And so I'm seeing a future where this is
[00:53:17] going to be the next AI revolution.
[00:53:19] Okay? We're going to have another AI
[00:53:20] revolution
[00:53:22] brought about by this and I'm building a
[00:53:24] company around this idea with and I
[00:53:27] think it's the right time to do it
[00:53:28] because we already have results that
[00:53:29] show that this approach works. You know,
[00:53:31] we can train from video. We get systems
[00:53:33] that have some level of common sense. We
[00:53:35] can train predictive models on top of
[00:53:36] them. World models, we can use them for
[00:53:38] planning. And so that points to the
[00:53:40] direction that you know, we we see a
[00:53:42] clear path to much more powerful AI
[00:53:45] systems than we currently have.
[00:53:47] When you say they're not generative,
[00:53:48] they're generative but across the
[00:53:49] different level at at different levels
[00:53:50] of abstraction in a sense. Well,
[00:53:52] generative my definition of generative
[00:53:53] is that you reproduce the input signals
[00:53:55] or you predict the input signals. Here
[00:53:57] you make predictions at representational
[00:53:58] level. Mhm. Okay? That's not generative
[00:54:01] in my in my world but Yeah, yeah, but I
[00:54:04] mean okay. Good. Thank you very much.
[00:54:06] Thank you. Thank you.
