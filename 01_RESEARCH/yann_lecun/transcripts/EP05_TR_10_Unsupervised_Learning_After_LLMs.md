# Unsupervised Learning: Yann LeCun on What Comes After LLMs
- **YouTube URL:** https://www.youtube.com/watch?v=ngBraLDqzdI
- **Lines:** 2582

---

[00:00:00] You're one of the godfathers of AI.
[00:00:01] What's your kind of view of the path of
[00:00:03] progress here? Five years complete world
[00:00:04] domination. The best way to get
[00:00:06] breakthrough research is you hire the
[00:00:08] best people and you get the out of
[00:00:09] the way.
[00:00:10] >> Pardon my French.
[00:00:11] >> You shared the Turing Award with two
[00:00:12] others. When did your views start
[00:00:13] diverging? In 2023. How do you know it
[00:00:15] was time to leave Meta? It sounds like
[00:00:17] you were thinking through some of these
[00:00:17] things over a period of time.
[00:00:19] >> There is a big misconception about my
[00:00:21] role, my relation to AI and how AI was
[00:00:24] run at Meta. What's like one thing
[00:00:25] you've changed your mind on in the last
[00:00:26] year? I mean, the whole idea of uh Yann
[00:00:29] LeCun is one of the godfathers of AI.
[00:00:31] He's an absolute legend in the field, uh
[00:00:33] someone I've admired for a long time.
[00:00:35] And so it was such a treat to get him on
[00:00:37] on Unsupervised Learning.
[00:00:39] Uh he's been a noted skeptic of of LLMs
[00:00:41] in many ways, and so we dug into what
[00:00:43] LLMs can do, what they can't do, uh some
[00:00:45] of the limitations he sees, and why he
[00:00:47] ultimately decided to pursue a different
[00:00:49] architecture. Uh and we also talked
[00:00:51] about his time at Meta,
[00:00:52] um you know, the things he's proud of in
[00:00:53] in setting up FAIR, how the last few
[00:00:55] years proceeded, and what ultimately led
[00:00:57] him to uh spin out and start his own
[00:00:59] company, uh me. Um I think it's just
[00:01:01] fascinating to get Yann's thoughts on
[00:01:03] everything happening in the AI ecosystem
[00:01:05] today, this tension between basic
[00:01:07] research and then pushing LLMs forward,
[00:01:09] and how that's happening in in a bunch
[00:01:11] of organizations today, as well as his
[00:01:12] thoughts on just where the the whole
[00:01:14] space is headed. Uh he's just an
[00:01:16] absolute giant in the field, and when I
[00:01:18] started this podcast, I hoped we'd get
[00:01:19] guests like him, so it is just such a
[00:01:21] treat. I think folks will really enjoy
[00:01:23] hearing the conversation we had. Without
[00:01:24] further ado, here's Yann.
[00:01:29] Yann, this is such a pleasure. You're
[00:01:30] one of the godfathers of AI. I feel like
[00:01:32] when I started doing this podcast years
[00:01:34] ago, I was really hoping we might one
[00:01:36] day get someone like you on. You know, I
[00:01:38] don't like that term because I live in
[00:01:39] New Jersey, when you're a godfather in
[00:01:40] New Jersey, it [laughter] doesn't mean
[00:01:42] the same thing.
[00:01:43] Very fair, very fair. You know,
[00:01:45] obviously, you know, your bet on on
[00:01:46] neural nets when everyone doubted them
[00:01:47] is legendary, and I feel like today
[00:01:49] you're making uh a similar bet in many
[00:01:51] ways against LLMs and the kind of
[00:01:52] predominant generative architectures
[00:01:54] that that so many believe in.
[00:01:55] Uh you've recently started a new company
[00:01:57] uh behind this theme. And so, you know,
[00:01:59] our goal today in the conversation is to
[00:02:01] leave our listeners with a lot for more
[00:02:03] information about AMI, what you're doing
[00:02:04] there, some of your work at Tapestry,
[00:02:06] um you know, why you think the rest of
[00:02:08] the field is is is pointed in the wrong
[00:02:09] direction around some of these
[00:02:10] generative models, and then also just
[00:02:12] get your reflections on the way the
[00:02:13] field's unfolded, your time at Meta, and
[00:02:15] and all that. So, you know, modest goals
[00:02:16] for uh for for for a single podcast
[00:02:18] episode. I feel it'd be great to start
[00:02:20] with AMI um because the company feels
[00:02:22] like the clearest statement of your
[00:02:23] technical thesis going forward. And so,
[00:02:25] you recently launched the company that's
[00:02:26] focused on world models uh and scaling
[00:02:28] the Jeff bar architecture, which you
[00:02:29] obviously pioneered uh over at Meta. And
[00:02:32] so, I'm wondering if you could talk a
[00:02:32] little bit about the origins of that
[00:02:34] architecture and the extent to which you
[00:02:35] drew inspiration from the human brain
[00:02:37] and the way that works. So, first of
[00:02:38] all, I want to say there's nothing wrong
[00:02:40] with
[00:02:41] LLMs
[00:02:42] in the sense of
[00:02:44] LLMs, you know, are the basis for a lot
[00:02:46] of uh
[00:02:47] very useful AI products that all of us
[00:02:49] use,
[00:02:50] including me. Uh
[00:02:52] They're great, okay, for what they do.
[00:02:55] They're just not a path towards
[00:02:57] human-level or human-like intelligence
[00:03:00] or even animal-like intelligence.
[00:03:02] Uh so, that's my claim, okay? I'm not
[00:03:04] saying LLMs are useless, right? I'm I'm
[00:03:06] just saying
[00:03:07] they're not a path towards I mean, you
[00:03:09] helped build some of the first major
[00:03:10] open-source ones.
[00:03:11] Right. Right.
[00:03:12] >> [laughter]
[00:03:12] >> Right, absolutely. So, what is uh AMI?
[00:03:15] So, AMI really stands for advanced
[00:03:17] machine intelligence. And the the the
[00:03:21] kind of subtitle, the motto, if you
[00:03:22] want, is uh AI for the real world.
[00:03:26] So, basically, a lot of
[00:03:28] you know, AI techniques that people know
[00:03:30] about today are good for language
[00:03:32] manipulation, either human language or
[00:03:35] computer code or mathematics or or
[00:03:38] legalese,
[00:03:40] which barely qualifies as human
[00:03:42] language.
[00:03:43] >> [laughter]
[00:03:43] >> Unfortunately, a lot of human language
[00:03:44] is for it. Right. Right, sadly.
[00:03:47] You know, language is very special in a
[00:03:49] way, and it's uh particularly
[00:03:52] well suited for the type of uh you know,
[00:03:55] architectures that
[00:03:56] have been so successful uh recently, the
[00:03:59] the you know, large language models,
[00:04:01] GPT-style architectures. But what about
[00:04:04] the real world? What about like
[00:04:05] understanding
[00:04:07] the physical world? Turns out reality is
[00:04:09] way more complicated than language.
[00:04:12] Uh because it's high-dimensional, it's
[00:04:14] continuous, it's noisy, it's messy.
[00:04:18] And uh training a system to understand
[00:04:20] the real world is much, much harder. So
[00:04:21] that's really what we're after. That's
[00:04:23] what I've been after for most of my
[00:04:25] career and really kind of,
[00:04:27] you know, working on in an accelerated
[00:04:29] fashion over the last uh 5, 6 years or
[00:04:31] so and making significant progress over
[00:04:33] the last 2 years.
[00:04:35] And so, it made sense to really do a
[00:04:37] startup around it and sort of go to into
[00:04:40] high gear, you know, in pushing that.
[00:04:42] And it became clear, you know, by the
[00:04:44] end of last year that
[00:04:45] Meta was really not the right place for
[00:04:47] that.
[00:04:48] So, which is why I left and started I
[00:04:51] mean, Labs. I think it's an interesting
[00:04:53] like, you know, trend that we're seeing
[00:04:54] across the board, right? Where it feels
[00:04:56] like um there you're there's there's
[00:04:58] many folks spinning out of, you know,
[00:04:59] either some of the large companies or
[00:05:01] research labs, you know, that have a
[00:05:03] particular direction of research they're
[00:05:04] excited about and
[00:05:05] you'd have some interesting vantage
[00:05:06] point of this from your time at Fair of
[00:05:07] this
[00:05:08] uh almost tension that exists between,
[00:05:10] you know, go pursue as many different
[00:05:11] research directions as possible in these
[00:05:13] companies versus hey, something's really
[00:05:15] working. This is the thing that we're
[00:05:16] going to sell for the next 6, 12 months.
[00:05:18] Like, go focus on that. You know, I'm
[00:05:20] curious your your thoughts on that and
[00:05:21] and what you kind of seen in the
[00:05:22] industry at large. Well, it's a strange
[00:05:25] uh
[00:05:26] trade-off. There's really two modes of
[00:05:28] operating, right? There's a lot of
[00:05:29] exploratory research, a lot of research
[00:05:31] directions, right? And sometimes
[00:05:33] something
[00:05:34] kind of seems to work and you you need
[00:05:36] to push it further. And it's not
[00:05:38] research anymore. I mean,
[00:05:40] the people working on it are still
[00:05:41] researchers or they're called
[00:05:43] researchers at least in the press, but
[00:05:45] uh but really it's becoming more
[00:05:46] engineering and pushing for for
[00:05:48] products, right? So,
[00:05:51] that happened a number of times at Meta
[00:05:54] because of things that were started at
[00:05:56] FAIR, such as seeing happened in, you
[00:05:59] know, early 2023, essentially. Uh, when,
[00:06:03] you know, Llama, which was developed at
[00:06:05] FAIR, Llama 1, um, was very promising.
[00:06:09] And, uh,
[00:06:10] Meta created a a whole organization,
[00:06:12] GenAI, to turn it into something real
[00:06:15] and a series of products. Uh, and
[00:06:17] produce, you know, Llama 2, Llama 3,
[00:06:19] Llama 4, which was a bit of a
[00:06:21] disappointment. Uh, and because, you
[00:06:23] know, Mark Zuckerberg was disappointed
[00:06:25] by it, he kind of rebooted the entire
[00:06:27] organization, reorganized it, and hired
[00:06:30] new people, etc. But, what also
[00:06:32] happened,
[00:06:34] uh, over the last year is that
[00:06:36] uh,
[00:06:37] basically the company, Meta, realized
[00:06:39] that,
[00:06:40] um, they'd fallen behind a little bit,
[00:06:42] and so that kind of refocused the the
[00:06:45] strategy on trying to catch up with the
[00:06:47] industry. And the sad side effect of it
[00:06:51] is that a lot of the exploratory
[00:06:53] research
[00:06:54] was basically not
[00:06:56] given high priority anymore. I mean, it
[00:06:58] didn't concern the stuff I was working
[00:07:00] on, all the Jeppa and world models,
[00:07:02] uh, cuz, you know, Mark himself and and
[00:07:05] do buzzwords, the CTO, and a bunch of
[00:07:07] other people in the company were really
[00:07:08] interested in that project and really
[00:07:09] believed in the long-term impact. But,
[00:07:12] the rest of the company was just, you
[00:07:13] know, totally entirely focused on LLMs,
[00:07:16] and made it clear to me that Meta was
[00:07:18] really not the the right place to push
[00:07:20] on that project anymore. And then we
[00:07:22] started to have good results, and so it
[00:07:24] was clear that, you know, we had to kind
[00:07:26] of make that transition between research
[00:07:29] and actually kind of uh, developing the
[00:07:32] technology, scaling it up, and building
[00:07:33] products out of it. And we realized also
[00:07:35] that most of the
[00:07:37] applications were probably
[00:07:40] for things that Meta was not
[00:07:41] particularly interested in. A lot of
[00:07:44] applications of the kind of stuff that
[00:07:46] we've been working on is in the
[00:07:48] industry, like manufacturing industry
[00:07:50] and stuff like that. Obviously, you're
[00:07:52] you're kind of pursuing world models and
[00:07:54] and and in that broader world. And I
[00:07:55] think there's other people that have
[00:07:56] come at the world model pace from a more
[00:07:58] like generative approach. And so I think
[00:08:00] you've got folks, you know, you've got
[00:08:01] the Google folks and Genie in the video
[00:08:03] models. You've got folks, you know,
[00:08:04] building VLAs on the robotic side.
[00:08:05] You've got Feifei and and kind of like
[00:08:08] the 3D spatial models. As you think
[00:08:10] about kind of the the body of of of of
[00:08:12] evidence that got you excited about the
[00:08:14] Japa models and how you kind of compare
[00:08:15] them to what the generative folks have
[00:08:17] done, you know, where do you think we
[00:08:19] are today in in terms of like comparing
[00:08:20] these architectures and approaches?
[00:08:22] Okay, so world model is quickly becoming
[00:08:24] a buzzword right now, right? Certainly
[00:08:27] in research, but also in industry to
[00:08:28] some extent. And uh and then there are
[00:08:31] two factions, if you want. I'm not going
[00:08:33] to talk about VLA because VLA
[00:08:35] is clearly now being seen as not going
[00:08:38] anywhere.
[00:08:40] Like it's really not working. Uh so VLA
[00:08:42] is, you know,
[00:08:43] vision language action models, right? So
[00:08:45] basically use the LLM technology to
[00:08:48] train a system to produce actions for
[00:08:50] like controlling a robot or something
[00:08:52] like this, right? So you have vision in,
[00:08:54] language in, action out. Maybe language
[00:08:57] out, too.
[00:08:58] Um and that's pretty much now seen as a
[00:09:02] failure.
[00:09:03] >> [laughter]
[00:09:04] >> Uh not being reliable enough, requiring
[00:09:06] too much training data, you know, things
[00:09:07] like that.
[00:09:08] Okay, then there is world models. Okay,
[00:09:10] so what is a world model? Uh a world
[00:09:12] model at a regional level is something
[00:09:15] that
[00:09:16] allows an agentic system to anticipate
[00:09:19] the consequences of its own actions.
[00:09:22] Okay, predict the consequences of its
[00:09:24] own actions. From my point of view, I
[00:09:26] cannot imagine how you can even think of
[00:09:29] building an agentic system without that
[00:09:31] system having the ability to predict the
[00:09:33] consequences of its actions.
[00:09:35] I I that's pretty essential, right? When
[00:09:37] we
[00:09:39] act in the world, we have this ability.
[00:09:42] And when we
[00:09:43] uh take an action without thinking about
[00:09:45] the consequences,
[00:09:47] we're taking a big risk. And very often,
[00:09:49] you know, other people think we're we're
[00:09:51] an idiot.
[00:09:53] Uh we have plenty of examples on the
[00:09:55] international political scene at the
[00:09:57] moment of people who have complete, you
[00:09:59] know,
[00:10:00] no ability to predict the
[00:10:01] consequences of their actions. So,
[00:10:03] that's the one model. That's what it is,
[00:10:05] right? Ability to predict the
[00:10:06] consequences of your own actions. If you
[00:10:08] If you have this ability, then you can
[00:10:10] plan
[00:10:12] a sequence of actions to
[00:10:14] accomplish a task, to you know, satisfy
[00:10:17] a goal. And you do this by
[00:10:20] planning, reasoning,
[00:10:22] uh by a process of search and
[00:10:24] optimization. You don't do this by
[00:10:27] predicting one action after the other
[00:10:28] autoregressively, like a real AI we do.
[00:10:31] Uh you do this by searching for a
[00:10:33] sequence of actions that will accomplish
[00:10:35] the task you set you set for yourself.
[00:10:37] So, the blueprint for this is completely
[00:10:40] different from what, you know, LLMs uh
[00:10:42] can do at the moment.
[00:10:44] Uh LLMs do not have the ability to
[00:10:45] predict the consequences of their
[00:10:47] actions, and they do not have any
[00:10:48] planning abilities. Because
[00:10:50] inference is by
[00:10:52] predicting the next token, right? It's
[00:10:54] not by search. Okay, so right there,
[00:10:56] you have the two characteristics that I
[00:10:58] think are essential for intelligent
[00:11:00] behavior.
[00:11:02] Ability to predict consequences of your
[00:11:04] actions. And second, uh ability to plan
[00:11:07] by optimization, by search. Um find a
[00:11:10] good sequence of actions that will
[00:11:11] produce the correct outcome. And then
[00:11:13] there is a third characteristic, which
[00:11:15] is
[00:11:16] uh how do you pre- how do you predict
[00:11:18] the consequences of your actions?
[00:11:20] Okay, so, you know, if uh if I have a
[00:11:25] water bottle in front of me. I realize
[00:11:26] some people would just listen to this
[00:11:28] and not have the picture. So, I have an
[00:11:30] open, uncapped water bottle in front of
[00:11:33] me. If I push at the bottom, it's going
[00:11:35] to slide on the table. If I push
[00:11:38] near the top, it's probably going to
[00:11:39] flip. We can't predict exactly
[00:11:42] how the
[00:11:44] the bottle will will fall in which
[00:11:45] direction.
[00:11:47] Uh we can't exactly predict how it's
[00:11:48] going to slide, you know, how the water
[00:11:50] will spill, you know, whether the table
[00:11:52] is tilted in one way and the water will
[00:11:55] uh
[00:11:55] you know, kind of flow in one direction
[00:11:57] or another.
[00:11:58] There's no way we can predict this at
[00:12:00] the pixel level.
[00:12:01] So, our mental model of the world
[00:12:03] predicts that at an abstract level of
[00:12:06] representation. So, as you were working
[00:12:07] on this architecture, was a lot of it
[00:12:08] inspired by the human brain? I mean,
[00:12:10] obviously, like the you know, the way
[00:12:11] you're articulating things is exactly
[00:12:12] how how we do things. Right, or at least
[00:12:14] by, you know, cognitive science, right?
[00:12:16] Whether you can sort of translate this
[00:12:17] into a neural architecture and things
[00:12:19] like this, that's there's a big gap
[00:12:21] there. Um okay, so that that, you know,
[00:12:24] certainly uh cognitive science was a bit
[00:12:26] of a motivation or or, you know, what uh
[00:12:29] psychological system two, which is this
[00:12:31] idea of the way you behave in sort of
[00:12:34] deliberate reflective behavior is that
[00:12:37] you do imagine, predict the consequences
[00:12:39] of your actions, and you plan
[00:12:41] uh accordingly. Contrary to system one,
[00:12:44] where you just act, you know, reactively
[00:12:47] and instinctively. So, yeah, there is an
[00:12:49] inspiration, but also there is a lot of
[00:12:52] empirical evidence
[00:12:53] that you don't want to generate pixels.
[00:12:56] Okay, I've been I've been really
[00:12:58] interested in that problem of
[00:13:01] learning models of the world by
[00:13:03] prediction for a very long time. And
[00:13:05] then had an epiphany about 5 years ago,
[00:13:08] realizing that
[00:13:10] all of the architectures that have have
[00:13:12] been successful to learn
[00:13:14] representations of images and videos
[00:13:17] are non-generative architectures. And
[00:13:20] all the generative ones basically have
[00:13:21] been failures, right? So,
[00:13:25] VAE, right? Variational autoencoders, or
[00:13:27] auto encoders more generally,
[00:13:30] uh is kind of a natural
[00:13:32] way to think about like learning
[00:13:34] abstract representations of inputs,
[00:13:36] right? So, you put a an image at the
[00:13:38] input of a
[00:13:39] of a neural net, and then you train it
[00:13:40] to just reproduce the input on its
[00:13:43] output.
[00:13:44] Uh now, with a big neural net. Now, if
[00:13:47] you just do it this way, your neural net
[00:13:48] will not do anything interesting. It
[00:13:50] will just learn the identity function.
[00:13:51] Yeah. Completely uninteresting. It
[00:13:53] doesn't work. Now, if you train a VAE to
[00:13:55] learn representations of images, you get
[00:13:57] something, but it's really not that
[00:13:58] great. Same with sparse auto encoders.
[00:14:00] Then, you have another set of
[00:14:01] techniques,
[00:14:03] uh and it's kind of derivative of
[00:14:05] something called denoising auto encoder,
[00:14:07] uh masked auto encoder is a version of
[00:14:10] this. BERT is a version of this for NLP.
[00:14:12] So, you take the image, you corrupt it
[00:14:14] in some way, and then you train this big
[00:14:15] neural net to recover the original uh
[00:14:19] the original image. There's a huge
[00:14:20] project that at FAIR on this called MAE,
[00:14:23] masked auto encoder. It was very
[00:14:25] disappointing.
[00:14:27] A lot of computation, and not not really
[00:14:30] great satisfying result. Simultaneously,
[00:14:33] uh some of the same people working on
[00:14:35] MAE, and and some other people
[00:14:37] in Paris and in New York were working on
[00:14:39] other techniques using
[00:14:41] non-generative architecture, joint
[00:14:43] embedding architecture. So, take an
[00:14:45] image, corrupt it in some way, and then
[00:14:47] run the two images through encoders, and
[00:14:49] then try to predict the representation
[00:14:51] of the original image from the
[00:14:53] representation of the corrupted one.
[00:14:55] Uh that's JEPA. Yeah. Okay. So, JEPA
[00:14:58] means joint embedding predictive
[00:14:59] architecture, right? So, you have one
[00:15:01] encoder that makes an observation,
[00:15:03] another encoder that makes a different
[00:15:04] observation. You try to predict the
[00:15:06] representation of the first one from the
[00:15:08] second one with a predictor. And those
[00:15:11] techniques turned out to work much
[00:15:12] better for representing images and
[00:15:15] video. So, things like DINO,
[00:15:18] uh DINO V1, V2, V3, um project that is
[00:15:21] still going on at at fair in Paris.
[00:15:25] Projects like I Jepa
[00:15:27] and then V Jepa and then before that
[00:15:28] there were like Sim Siam and Moco and a
[00:15:31] bunch of different techniques mostly
[00:15:33] from Meta. There was a bunch of others
[00:15:34] from other groups.
[00:15:36] Um,
[00:15:37] but
[00:15:38] that turned out to be a much better way
[00:15:39] of learning representations of images
[00:15:42] than
[00:15:44] predicting pixels. Yeah. And so
[00:15:46] it just clicked in my in my mind but you
[00:15:48] know, not just mine.
[00:15:51] That this was the way to go and
[00:15:52] predicting pixels was kind of a a losing
[00:15:54] proposition. You know, it feels like
[00:15:56] there's all these robotics demos that
[00:15:57] are released
[00:15:59] you know, from from some of the model
[00:16:00] companies that are feel increasingly
[00:16:02] impressive and maybe you know, seem to
[00:16:04] resemble things like planning and
[00:16:05] reasoning when you know, they maybe
[00:16:07] haven't seen a a room or or a specific
[00:16:09] and you know, a version of a task before
[00:16:11] and are still able to execute that task.
[00:16:13] You know, what would you say to our
[00:16:14] listeners I guess that that observe that
[00:16:16] stuff and feel like it feels like we're
[00:16:17] trending toward some real progress with
[00:16:19] some of the general approaches. Well,
[00:16:21] there is real progress and some of those
[00:16:22] demos are really impressive. Um,
[00:16:25] but
[00:16:26] >> [laughter]
[00:16:27] >> they are trained with enormous amounts
[00:16:29] of data collected either from
[00:16:32] teleoperation
[00:16:34] or from just you know, human action with
[00:16:36] things you hold in your hand that look
[00:16:38] like grippers.
[00:16:39] Grippers that you know, and you and you
[00:16:41] collect the data for that. Or just you
[00:16:44] know, tracking hands and fingers of of a
[00:16:47] person.
[00:16:48] And then translating this into kind of
[00:16:50] commands for for a robot. And so those
[00:16:52] things are trained with imitation
[00:16:54] learning mostly, right? And a little bit
[00:16:56] with you know, reinforcement learning to
[00:16:58] fine tune in mostly in simulation. So
[00:17:01] the issue with this is that you need a
[00:17:03] lot of data to train the systems
[00:17:06] to
[00:17:07] to imitation.
[00:17:09] And it
[00:17:11] it becomes expensive and it's a little
[00:17:12] brittle
[00:17:14] in the sense that you know, you need to
[00:17:16] collect lots of data for every task you
[00:17:18] want the robot to uh uh to solve.
[00:17:21] Whereas, if the system had a world model
[00:17:23] that allowed it to predict the
[00:17:26] you know,
[00:17:27] the outcome of an action, it would just
[00:17:29] plan an action to solve a new task
[00:17:32] without actually having to be trained
[00:17:34] to accomplish this task. So, the degree
[00:17:37] of generalization you would get with a
[00:17:39] world model-based system is much, much
[00:17:41] larger
[00:17:43] uh
[00:17:43] you know, kind of wider spectrum of of
[00:17:46] tasks
[00:17:47] with less training data that would be
[00:17:49] required than a a system trained with
[00:17:51] imitation learning and
[00:17:53] and you know, fine-tuning
[00:17:54] >> No doubt those approaches require more
[00:17:56] data. And I guess this question of
[00:17:57] generalization really is is the big
[00:17:58] question, right? Of you know, and I
[00:17:59] think you know, some folks have have uh
[00:18:02] have shown some results around, you
[00:18:03] know, uh getting better at task A helps
[00:18:05] with task B, but that obviously feels
[00:18:06] like there's still the big unanswered
[00:18:08] question uh you know, around those
[00:18:09] architectures. I mean, you get this uh
[00:18:12] you know, synergy between tasks. So, the
[00:18:13] more tasks that you train the system to
[00:18:15] solve, the more tasks it's being
[00:18:17] it's going to be able to acquire with
[00:18:18] with small amount of data, regardless of
[00:18:21] what what technique you use. But, but
[00:18:22] the hope with uh
[00:18:24] world models is that the system can
[00:18:26] solve new tasks at zero shot, which
[00:18:28] humans are completely capable of doing,
[00:18:30] right? And many animals as well.
[00:18:32] So, uh so, that's really the the hope.
[00:18:35] Like, you know, solving a lot more
[00:18:36] problems with uh
[00:18:40] either a small amount of training data
[00:18:42] or or no training data at all.
[00:18:45] And just a little bit of maybe, you
[00:18:47] know, RL style uh fine-tuning. Yeah.
[00:18:49] Like, you know, how
[00:18:51] how is it that a 17-year-old can learn
[00:18:53] to drive in
[00:18:54] like, a dozen hours or maybe 20 hours?
[00:18:57] Uh we have millions of hours of training
[00:18:59] data of
[00:19:00] you know, people driving cars. We still
[00:19:02] don't have level five self-driving cars,
[00:19:04] right? So, imitation learning obviously
[00:19:06] does not work even for just the task of
[00:19:08] autonomous driving. Yeah, I guess it'll
[00:19:10] be a race between the ability to develop
[00:19:12] some of those capabilities, which may
[00:19:13] take time and lots of data versus this
[00:19:15] kind of architecture. I feel like
[00:19:16] there's this dream of using video models
[00:19:18] to just generate like tons of synthetic
[00:19:20] data for for, you know, simulation and,
[00:19:22] you know, even if it's not perfect,
[00:19:23] these video models from a physics
[00:19:24] perspective, it's like helpful enough
[00:19:26] to, you know, improve
[00:19:28] robotics and in the underlying physical
[00:19:30] world. What have you made of some of
[00:19:31] those approaches? Obviously, I think
[00:19:32] Nvidia's been focused there. Google
[00:19:33] seems to be going down that road.
[00:19:35] >> I'm sort of asking you again the
[00:19:36] question,
[00:19:37] you know,
[00:19:38] why can 17-year-old launch a driving 20
[00:19:41] hours? You don't need millions of hours
[00:19:43] of demonstration. And you don't need
[00:19:45] synthetic data. Uh you don't need any of
[00:19:47] that. So, you know, I I want a system
[00:19:49] that can learn as fast as that. If we
[00:19:51] crack that, then we don't need, you
[00:19:53] know, generated data, right? I mean, we
[00:19:55] might need to train the system in
[00:19:57] simulation, but not with the same amount
[00:19:59] of uh
[00:20:01] uh
[00:20:02] you know, of time or or trials as as
[00:20:04] current systems require. It's really a
[00:20:07] question of data efficiency.
[00:20:08] >> You know, I was interviewing Jerry
[00:20:09] Tworek on the podcast. He was at OpenAI
[00:20:11] and spun out to start his own lab, and
[00:20:13] you could sense a similar tension where
[00:20:14] I think he actually might even agree
[00:20:15] that, you know, if you continued scaling
[00:20:17] RL the way we're scaling, you get more,
[00:20:19] you know, you continue getting very
[00:20:20] impressive results. But, I think he
[00:20:22] felt, "God, there's just got to be some
[00:20:23] like way more efficient way to do this."
[00:20:25] And it's interesting. It's an
[00:20:26] interesting tension because you could
[00:20:27] imagine if you're OpenAI and you know
[00:20:29] something is going to continue like you
[00:20:30] could continue scaling it and it will
[00:20:31] keep getting better. There's not a ton
[00:20:33] of incentive necessarily from a business
[00:20:35] perspective to do something more
[00:20:36] data-efficient.
[00:20:37] >> Right. And there's there's no incentive
[00:20:39] for the other companies to do anything
[00:20:41] different either because they're all
[00:20:43] chasing the same like they can't afford
[00:20:45] to kind of fall behind the others,
[00:20:47] right? So, they all work on the same
[00:20:49] thing. Yeah. And And there's a bit of
[00:20:51] this sort of, you know,
[00:20:53] kind of
[00:20:55] herd behavior
[00:20:57] uh
[00:20:58] and and, you know, in in mostly in
[00:21:00] Silicon Valley where everybody is
[00:21:02] digging the same trench. Yeah. Uh and
[00:21:05] you know, so I pur-
[00:21:07] purposely
[00:21:09] set up the headquarters of Amy Labs
[00:21:12] in Paris. Yeah.
[00:21:13] >> [laughter]
[00:21:14] >> Uh
[00:21:16] the American office being in New York,
[00:21:18] not Silicon Valley.
[00:21:19] >> [laughter]
[00:21:19] >> It's really interesting cuz I think it
[00:21:20] it it it points to a tension that, you
[00:21:22] know, it it exists in the broader
[00:21:23] ecosystem today where
[00:21:25] uh you could imagine the other side
[00:21:26] being sure, maybe there are more
[00:21:28] data-efficient methods out there, but
[00:21:29] like almost who cares because we can
[00:21:31] keep scaling what we have to to better
[00:21:33] and better results. And then obviously I
[00:21:35] think from both, you know,
[00:21:37] new things you can accomplish from these
[00:21:39] models as well as just the joy of being
[00:21:41] a researcher and finding these new
[00:21:42] things. I get why there's such an
[00:21:43] attraction to to to these other
[00:21:45] architectures as well.
[00:21:46] >> And it's a bet.
[00:21:47] But, you know, we're pretty confident
[00:21:49] because, you know, we we have results
[00:21:51] already, actually.
[00:21:52] >> And as you think about like the the kind
[00:21:54] of um the initial spaces you're most
[00:21:56] excited about for the Amy technology,
[00:21:58] like what gets you know, where do you
[00:21:59] think you know, the the technology goes
[00:22:01] and and what are you most excited about?
[00:22:03] Well, I mean, you know, AI for the real
[00:22:04] world. Um
[00:22:07] like, you know, can
[00:22:08] where is your domestic robot? Where is
[00:22:10] your level five self-driving car? Yeah.
[00:22:12] Where is uh and that's you know
[00:22:14] >> When am I going to get a domestic robot?
[00:22:15] I'm excited about this.
[00:22:17] Well, so this is several years down the
[00:22:19] line. Okay? Despite the fact that there
[00:22:21] is like
[00:22:22] huge number of companies building
[00:22:24] robots, none of those companies
[00:22:26] actually has any idea how to make them
[00:22:28] smart enough to be useful, right? Or
[00:22:29] trusted around with a baby in the house
[00:22:31] or something or
[00:22:31] >> Certainly not that. Uh but but even for
[00:22:34] like, you know, relatively narrow
[00:22:35] manufacturing task, right? You know, I
[00:22:37] mean
[00:22:38] uh none of them really knows
[00:22:40] how how to do this reliably other than
[00:22:42] you know, for by imitation learning for
[00:22:44] a small number of tasks.
[00:22:46] Uh so, how how do we make those things
[00:22:48] useful? So, that's kind of a
[00:22:50] relatively long-term objective.
[00:22:53] Shorter term, there is a huge amount of
[00:22:55] applications in industry
[00:22:57] where you need to have
[00:22:59] a a system, an intelligent system that
[00:23:01] has the ability of
[00:23:04] you know, predicting what's going to
[00:23:05] happen if I change this
[00:23:07] control variable on this complex system,
[00:23:10] be it uh
[00:23:12] a jet engine, a chemical plant, a power
[00:23:15] plant, a some manufacturing line,
[00:23:19] a patient, a human cell, right? Those
[00:23:22] are systems
[00:23:23] that are sufficiently complex that you
[00:23:25] can't
[00:23:26] model their behavior with a small number
[00:23:28] of equations. Right? So, the traditional
[00:23:30] way of modeling
[00:23:32] does not work. And what you need to do
[00:23:34] is train a neural net, deep learning
[00:23:37] system,
[00:23:38] uh to to
[00:23:40] um you know, model the dynamics of that
[00:23:42] system
[00:23:43] from data.
[00:23:44] And what you get at the end is a a
[00:23:46] phenomenological model of of that
[00:23:49] uh process, of that
[00:23:51] uh system.
[00:23:52] Um and if it's action condition, then
[00:23:54] you get
[00:23:55] basically a a world model of that system
[00:23:58] that allows you to control it optimally
[00:24:00] for whatever purpose you have. And I
[00:24:02] think the
[00:24:04] number of applications of this in
[00:24:06] industry is mind-boggling. Where do you
[00:24:08] think we'll be with uh you know, general
[00:24:10] models over the next couple years? Are
[00:24:11] there like, you know, milestones you'd
[00:24:13] point to or like, what what's your kind
[00:24:15] of view of the path of progress here?
[00:24:16] Okay, couple of years is a little short.
[00:24:18] Like, 5 years, complete world
[00:24:19] domination, essentially. [laughter]
[00:24:21] Okay. So, somewhere between on the path
[00:24:23] to world domination in 5 years. I mean,
[00:24:25] this is kind of a joke, obviously, but
[00:24:27] uh this is a quote from Linus Torvalds,
[00:24:29] right? You know, when people ask him,
[00:24:30] "What's your goal with Linux?" He said,
[00:24:32] "Total world domination." [laughter]
[00:24:34] Um he actually managed to do that.
[00:24:36] >> Yeah, very fair. To first approximation,
[00:24:38] every computer in the world runs Linux,
[00:24:40] right? So, um so, that's kind of a joke.
[00:24:42] But but in the end, I think this is the
[00:24:44] blueprint for intelligent systems of the
[00:24:46] future.
[00:24:48] There still be a a small place for LLMs,
[00:24:51] you know, for
[00:24:52] like a language interface, basically.
[00:24:55] But uh
[00:24:56] but what we're designing are are systems
[00:24:58] that are capable of thinking. They They
[00:25:00] may not be capable of talking or
[00:25:02] listening initially,
[00:25:04] but they'll do the thinking.
[00:25:06] And then you can add the talking and
[00:25:08] listening
[00:25:10] uh on top of that. I'm sure you and the
[00:25:12] team are are are eagerly working to kind
[00:25:14] of, you know, get the early proof points
[00:25:15] of this. And obviously, you've already
[00:25:17] had some in the work you've done. How do
[00:25:18] you think about like the interim steps
[00:25:19] of what you'll be able to show on that
[00:25:21] path to to 5-year world domination?
[00:25:23] Well, so I think uh
[00:25:25] you know, within a year or so, um we'll
[00:25:28] have
[00:25:29] I think a a general methodology
[00:25:32] to train
[00:25:33] hierarchical world models
[00:25:35] on, you know, a a very wide variety of
[00:25:38] modalities.
[00:25:40] We know we can do a good job on video
[00:25:42] uh with some techniques that we're not
[00:25:44] completely happy with because they have
[00:25:46] some shortcomings, but
[00:25:48] um
[00:25:49] and we have
[00:25:50] sort of small-scale demonstration of a
[00:25:53] methodology that we think is
[00:25:55] really what we want.
[00:25:57] So, we need to scale that one up
[00:25:59] and get it to the same level of
[00:26:00] performance as the
[00:26:03] the other techniques that are not as uh
[00:26:06] satis- satisfying, if you want, on on
[00:26:08] things like video, but also on other
[00:26:10] types of data sets that we would get
[00:26:12] from industry partners. Okay, so we'll
[00:26:14] have
[00:26:15] demonstrations that we can train world
[00:26:17] models, perhaps action-conditioned world
[00:26:18] models that allow us to plan
[00:26:20] for uh a number of different use cases.
[00:26:23] Some of them will be robotics, some of
[00:26:25] them will be industrial process control
[00:26:27] of various types, maybe some of them in
[00:26:29] health um health care as well cuz we
[00:26:32] have partners in that
[00:26:33] >> Yeah. in that domain. And
[00:26:36] that should be within a year or two, 18
[00:26:38] months. Um
[00:26:40] And then we'll push the this methodology
[00:26:43] and those models into
[00:26:45] uh those use cases with partners, some
[00:26:48] of which are investors already, you
[00:26:49] know, in our company, and gain
[00:26:51] experience on how to kind of
[00:26:54] essentially build a somewhat universal
[00:26:56] world model if you want. I mean, you've
[00:26:57] obviously had this uh you know, this
[00:26:59] experience before of of kind of making
[00:27:01] this really contrarian bet on neural
[00:27:02] nets and and being certainly uh proven
[00:27:05] abundantly right uh in the in in the
[00:27:06] history books. I guess as you think
[00:27:08] about this bet which I think, you know,
[00:27:09] if you talk to the majority of people uh
[00:27:11] maybe at at at at the cutting edge of
[00:27:13] various parts of AI maybe would would
[00:27:14] say is contrarian today. In what time
[00:27:16] frame do you think it will become
[00:27:17] apparent like, you know, that this was
[00:27:19] right?
[00:27:20] I think it'll happen faster than
[00:27:24] expected perhaps because I mean, you can
[00:27:26] see that world model is already becoming
[00:27:28] a buzzword, right?
[00:27:30] At least at the research level.
[00:27:32] Uh
[00:27:34] and it's starting to kind of permeate
[00:27:35] into the industry. Yeah. And a lot of
[00:27:37] people are realizing like VLs suck
[00:27:40] and, you know, LLMs don't work for real
[00:27:42] world data. Industry has realized this
[00:27:45] already. Certainly on the on the
[00:27:48] on the user side.
[00:27:50] And I think because of the importance of
[00:27:52] the robotics industry
[00:27:54] um you know, a lot of people are kind of
[00:27:55] trying to figure out like how how do we
[00:27:57] how do we get there? How do we get how
[00:27:58] you make those robots
[00:28:00] uh
[00:28:01] useful. So so I think it's
[00:28:03] I think the realization that you need a
[00:28:05] change of paradigm is is happening as we
[00:28:07] speak and will become completely obvious
[00:28:09] to people by
[00:28:11] early 2027, I think. Yeah. Now, that
[00:28:14] doesn't mean we'll have a solution by
[00:28:15] then. We hope we will, but you know,
[00:28:17] we'll see. I guess, you know, switching
[00:28:18] gears to the LM side you mentioned some
[00:28:20] of this work you're doing with uh with
[00:28:21] Tapestry which I think would be really
[00:28:22] interesting for our listeners. And so
[00:28:24] maybe to speak to that a little bit.
[00:28:25] Okay, so this is kind of a little bit
[00:28:27] orthogonal to uh to ML Labs. Yeah, as if
[00:28:30] that wasn't enough to keep you busy.
[00:28:32] >> [laughter]
[00:28:32] >> Well, it's a it's a kind of an idea I've
[00:28:34] I've been uh forming over the last uh
[00:28:36] three years or so
[00:28:38] is the fact that uh
[00:28:41] people increasingly use AI assistants
[00:28:43] for various things, right? I mean, uh
[00:28:45] you see a decrease in the use of general
[00:28:48] traditional search engines and you just
[00:28:50] ask a question to your favorite AI
[00:28:52] assistant.
[00:28:54] Um and you know, if the plan that Meta
[00:28:58] and others are are
[00:29:00] developing of, you know, having smart
[00:29:01] devices like smart glasses and stuff
[00:29:03] like that,
[00:29:04] uh
[00:29:05] you know, is realized,
[00:29:07] basically you'd just be talking to your
[00:29:09] AI assistant, you know, by voice with,
[00:29:11] you know, to your smart glasses or maybe
[00:29:13] some other smart device.
[00:29:15] And so, all of your information diet
[00:29:18] will be mediated by AI assistants.
[00:29:22] And
[00:29:23] if you are someone, you know, somewhere
[00:29:24] in the world, let's say outside the US
[00:29:26] or China, and you have an AI assistant,
[00:29:28] and that AI assistant was built in
[00:29:29] California or
[00:29:32] you know, Beijing
[00:29:33] or Shanghai or Shenzhen, uh
[00:29:37] it's not good for you. Like you may
[00:29:39] speak a language that those systems
[00:29:41] really haven't been trained to handle
[00:29:43] particularly well.
[00:29:44] Uh you may have a culture that is not
[00:29:47] particularly well understood by people
[00:29:48] in Silicon Valley and China.
[00:29:50] Not well represented by the training
[00:29:52] data that is publicly available on the
[00:29:54] internet.
[00:29:56] Um
[00:29:57] you may have a value system that is
[00:29:58] absolutely not represented by
[00:30:01] uh you know, people building those
[00:30:02] models.
[00:30:03] And certainly you'll almost certainly
[00:30:05] have political opinions that are
[00:30:07] absolutely not represented by the
[00:30:09] handful of AI assistant you you might be
[00:30:12] able to get from the
[00:30:14] you know, um West Coast tech companies
[00:30:16] or from Chinese companies.
[00:30:19] So, what is the solution to this? Like
[00:30:21] how do you serve,
[00:30:23] uh you know, a farmer in India,
[00:30:25] uh or um even a philosopher in France,
[00:30:30] uh or Germany? And
[00:30:33] what you need is
[00:30:35] a platform
[00:30:37] which basically is uh an open free
[00:30:41] foundation model, LLM style,
[00:30:44] that is fine-tunable
[00:30:46] by anyone
[00:30:48] to cater to the interest of people
[00:30:51] speaking a particular language, having a
[00:30:53] particular culture,
[00:30:55] having particular
[00:30:57] value systems, political biases,
[00:30:59] uh
[00:31:00] creeds, whatever it is.
[00:31:03] And so, what you need is a wide
[00:31:05] diversity of AI assistants. There's a
[00:31:08] lot of countries around the world uh
[00:31:11] that are neither the US nor China, who
[00:31:14] absolutely want some level of
[00:31:16] sovereignty for AI, not just for their
[00:31:18] industry, but also for their citizen.
[00:31:20] They don't want their citizen to get
[00:31:22] brainwashed by
[00:31:24] a Chinese model or a Canadian model,
[00:31:26] actually.
[00:31:27] Uh And so,
[00:31:29] they want sovereignty. How do you get
[00:31:31] that? So, the way you get
[00:31:34] a platform like the an open platform
[00:31:36] like this to get to the frontier is you
[00:31:38] just train it on more and higher quality
[00:31:40] data than the than the proprietary
[00:31:43] systems.
[00:31:44] If you talk to
[00:31:46] people in India, in France, in Vietnam,
[00:31:49] in
[00:31:51] Morocco, in Switzerland,
[00:31:54] in Korea, Japan,
[00:31:56] uh
[00:31:57] Kazakhstan,
[00:31:59] everyone wants
[00:32:02] basically sovereignty.
[00:32:04] And you tell them like, you guys have
[00:32:06] been training your model, you know,
[00:32:08] locally. You don't have to share your
[00:32:09] data. So, that's the crucial aspect of
[00:32:11] Tapestry.
[00:32:12] You would have international contributor
[00:32:15] contributors to Tapestry
[00:32:17] contributing to training a a global
[00:32:19] model that would basically constitute a
[00:32:23] repository of all the world's knowledge
[00:32:25] and culture, if you want. But the
[00:32:26] contributors would contribute uh
[00:32:30] data and uh computing resources, but
[00:32:33] they would preserve the control on their
[00:32:35] data. They would not have to share their
[00:32:37] data with the other
[00:32:38] uh contributors.
[00:32:40] What they would contribute is
[00:32:42] parameter vectors. Interesting. So, it
[00:32:44] would be kind of a kind of federated
[00:32:46] learning style thing where uh you have a
[00:32:48] bunch of data centers. Uh
[00:32:51] you know, they they get the parameter
[00:32:53] vector from the
[00:32:55] the the global consensus of a model.
[00:32:58] Think of it as an average of all the
[00:33:01] all the parameter vectors of all the
[00:33:02] contributors, right?
[00:33:04] So, all the contributors uh periodically
[00:33:06] tell
[00:33:08] everyone else through maybe a central
[00:33:10] server, here is my parameter vector,
[00:33:13] what is yours? Okay.
[00:33:15] Uh and so, you exchange parameter
[00:33:16] vectors like this. And a local worker
[00:33:19] basically, whatever it updates its
[00:33:20] parameter vector, it tries to also
[00:33:24] makes make it as close as possible to
[00:33:26] the global consensus vector. So, as the
[00:33:30] training of this thing kind of
[00:33:31] progresses, all those parameter vectors
[00:33:34] converge towards
[00:33:36] like a a consensus model, essentially,
[00:33:38] which is kind of a repository of all
[00:33:41] human knowledge. Now, you have an open
[00:33:43] an open model
[00:33:45] that is as good as if it had been
[00:33:47] trained on all the data in the world.
[00:33:50] And now, you can fine-tune it for your
[00:33:52] own purpose, your own
[00:33:55] political, cultural, and linguistic
[00:33:56] biases.
[00:33:57] Whatever you want or centers of
[00:33:58] interest.
[00:33:59] And I think there is a natural force for
[00:34:01] this to happen
[00:34:03] uh because, you know, most countries
[00:34:05] that are not the US nor China want
[00:34:09] sovereignty, but also because
[00:34:11] uh
[00:34:12] AI is fast becoming a platform. And
[00:34:15] there is a natural tendency for
[00:34:16] platforms to become open.
[00:34:18] That's what happened with Linux,
[00:34:20] right? And that's what happened with the
[00:34:23] software infrastructure of the internet
[00:34:25] or the wireless network. It's all open
[00:34:27] source.
[00:34:28] Um
[00:34:29] it was proprietary initially, but that
[00:34:32] was all
[00:34:33] wiped out. It's a really clever way to
[00:34:34] get around you know it would seem that
[00:34:36] this trend of you know decreasing open
[00:34:38] source and and obviously I think there's
[00:34:41] been many fears that is like the closed
[00:34:42] source models get better they'll be held
[00:34:44] back and they'll be used to train the
[00:34:45] next generation and you know they'll
[00:34:46] they'll kind of be this almost like a
[00:34:48] scape scenario for for closed source
[00:34:49] models where they get you know so much
[00:34:51] better than than their open source
[00:34:52] counterparts. So remember what you know
[00:34:54] who the big players of the internet
[00:34:56] infrastructure were
[00:34:58] in 1990 six?
[00:35:01] Sun Microsystems HP
[00:35:04] Dell
[00:35:05] and a few others.
[00:35:07] Um so Sun Microsystems was selling you
[00:35:09] Solaris with their you know proprietary
[00:35:11] hardware.
[00:35:12] HP with HP-UX
[00:35:14] uh they were claiming you know Unix is
[00:35:16] so much more reliable than Windows
[00:35:17] you're not going to run a web server on
[00:35:18] Windows. Dell was doing this you know
[00:35:21] with Windows NT but like who is running
[00:35:23] Windows NT now [laughter] as a web
[00:35:25] server?
[00:35:26] All of this was totally wiped out by
[00:35:28] Linux like the entire internet runs on
[00:35:30] Linux.
[00:35:31] Um even Azure right? Even Microsoft
[00:35:34] >> [laughter]
[00:35:34] >> it runs Linux. So
[00:35:37] uh
[00:35:39] basically OpenAI and Anthropic
[00:35:41] etc. of today are the
[00:35:44] Sun Microsystem and HP-UX
[00:35:47] of yesterday.
[00:35:49] Yeah I mean I guess it it implicit in
[00:35:51] that is is obviously um you know I think
[00:35:53] your you know your view of like the
[00:35:55] limitations of of what like you know the
[00:35:57] these models can only get so good and so
[00:36:00] it'll be possible over time for for the
[00:36:01] open source folks to to catch up.
[00:36:03] They've already run out of data right? I
[00:36:04] mean the the
[00:36:06] the open openly available publicly
[00:36:08] available data text data
[00:36:11] uh
[00:36:12] is already all used.
[00:36:13] I mean there's not more of it right? So
[00:36:15] what what those companies are doing is
[00:36:17] licensing uh
[00:36:19] commercial copyrighted data
[00:36:22] or training on
[00:36:24] synthetic data. I guess I'm curious cuz
[00:36:25] obviously there's been some impressive
[00:36:27] results uh in the last few years that
[00:36:29] they that they have been able to drive,
[00:36:30] you know, post these large-scale
[00:36:31] pre-trainings. Um you know, IMO gold, uh
[00:36:34] you know, the meter
[00:36:35] task horizon benchmark keeps going up.
[00:36:37] Okay, that's Okay, that's very
[00:36:39] interesting. Now, think about those two
[00:36:40] domains, right? Mathematics and code.
[00:36:43] Those are two domains where the language
[00:36:45] itself is the substrate of reasoning.
[00:36:49] It's not the only substrate of
[00:36:50] reasoning, but a lot of
[00:36:52] when you do mathematics, right? The the
[00:36:55] formal way on a piece of paper, not the
[00:36:57] intuitive stuff, but the
[00:36:58] you manipulate language, right? And LLMs
[00:37:01] are really good at this. So,
[00:37:03] um
[00:37:03] you know, proving theorems and stuff
[00:37:05] like that, that's that's what LLMs are
[00:37:07] really good at.
[00:37:08] They're not so good at the sort of
[00:37:11] you know, coming up with uh good
[00:37:12] concepts and definitions and things like
[00:37:14] that. It it's more like, here is a
[00:37:15] problem, solve it. They're problem
[00:37:16] solvers. Mathematics is not just problem
[00:37:19] solving, right? Most of it
[00:37:21] uh is actually a creative act that those
[00:37:23] things don't do.
[00:37:25] Um
[00:37:27] and same for code. So, LLMs are good
[00:37:29] programmers. They're not software
[00:37:31] architects.
[00:37:33] They're not computer scientists, right?
[00:37:36] Uh
[00:37:37] but they can program for us.
[00:37:39] So, they they they're not in a in a
[00:37:41] state where they can just, you know,
[00:37:43] replace humans uh entirely. It changes
[00:37:46] the world of humans. So, humans now,
[00:37:48] you know, kind of go one level up in the
[00:37:50] abstraction hierarchy and
[00:37:53] our world is to decide what to build.
[00:37:54] But like building it, you know, you can
[00:37:56] you can get help from LLMs. But okay,
[00:37:59] that's the the important point is that
[00:38:01] uh LLMs are particularly successful at
[00:38:04] domains where the language itself is the
[00:38:07] substrate of reasoning.
[00:38:08] Uh not for anything else. Yeah. What
[00:38:11] would an LLM like need to do to convince
[00:38:12] you uh otherwise? So, I mean, like a
[00:38:15] zero-shot agentic system, right?
[00:38:18] You have an agentic system.
[00:38:20] Give it a new problem. It's not been
[00:38:21] trained to solve that that problem.
[00:38:23] Doesn't have a script for it.
[00:38:25] Uh
[00:38:26] is it going to be able to uh accomplish
[00:38:28] this task? That it's never been trained
[00:38:30] to solve.
[00:38:32] And unless the system has the ability of
[00:38:34] predicting the consequences of its
[00:38:36] actions and then use using use that for
[00:38:38] play for planning
[00:38:41] it's not going to be able to do it. And
[00:38:42] you're not going to do this with an LLM.
[00:38:44] You're going to do this perhaps with a
[00:38:46] significantly
[00:38:47] augmented LLM that is capable of
[00:38:50] you know, search and planning blah blah
[00:38:52] blah. And currently
[00:38:54] you know, LLMs that do math and code
[00:38:55] actually do this.
[00:38:56] >> Yeah. Right? Cuz they search for you
[00:38:58] know, sequences of tokens that actually
[00:39:00] accomplish a particular task and you
[00:39:03] know, they can run the code or verify
[00:39:05] that the proof is correct or whatever.
[00:39:08] Um so, you have like a way of checking
[00:39:10] whether something that's produced is is
[00:39:11] is correct. Um but that's not a very
[00:39:14] efficient way of of doing planning.
[00:39:16] And it only works in domains where this
[00:39:19] type of search can be performed in token
[00:39:21] space.
[00:39:22] What I'm talking about with Jeppa is you
[00:39:24] don't do this in token space. You do
[00:39:25] this in you know, abstract thoughts
[00:39:28] space. And I'm sure some people
[00:39:30] listening might think, well, you know,
[00:39:31] hey, if if even if it's inefficient and
[00:39:32] it works uh and it works at you know, at
[00:39:35] things that are done in token space,
[00:39:36] that's still a large part of the uh of
[00:39:38] the economy that
[00:39:39] >> I mean, if it works, it's fine. I mean,
[00:39:41] there's again, there's nothing wrong
[00:39:42] with you know, using an LLM for what
[00:39:44] they're good at.
[00:39:45] Uh it's just not a path towards human
[00:39:48] level AI. You're missing you know, an
[00:39:50] >> like a huge
[00:39:51] uh domain.
[00:39:52] >> You seem like you you know, hey, it's
[00:39:53] going to tap out before it can become a
[00:39:55] software architect, whereas I'm sure
[00:39:56] >> going to tap out. It's it's just going
[00:39:58] to have like a a limited you know,
[00:40:00] ability to be deployed for like an it's
[00:40:02] going to become like increasingly
[00:40:03] difficult to kind of deploy it for an
[00:40:05] increasingly large number
[00:40:07] you know, of of use cases because you're
[00:40:09] going to have to collect tons of
[00:40:10] training data for each of those use
[00:40:12] cases. And
[00:40:14] there's a basically you're not going to
[00:40:16] be able to make those systems completely
[00:40:18] reliable, you know, without
[00:40:19] hallucinations or or dangerous stuff or
[00:40:22] uh etc.
[00:40:24] Unless those systems have the ability to
[00:40:26] predict the consequences of their
[00:40:27] actions, which means they're going to
[00:40:28] have to have explicit world models.
[00:40:30] Yeah, so I guess it's a bet against, you
[00:40:31] know, the uh 100% accuracy and then also
[00:40:34] the generalization uh across different
[00:40:36] tasks.
[00:40:36] >> Right. I guess, you know, one thing that
[00:40:38] that's so interesting about the way that
[00:40:39] the field has developed is obviously you
[00:40:41] uh share the the Turing Award with two
[00:40:43] others and I feel like they seem much
[00:40:44] more convinced of like maybe the the
[00:40:46] power or potential threats or safety
[00:40:47] risks of LLMs over time. Um
[00:40:50] I'm wondering like when did your view
[00:40:51] start diverging?
[00:40:53] Uh in 2023.
[00:40:56] And what like drove that in your mind? I
[00:40:58] didn't change my mind.
[00:40:59] They changed their mind, okay?
[00:41:00] [laughter]
[00:41:01] And I just about the same time, and it
[00:41:03] was basically GPT-4.
[00:41:05] I mean, Jeff basically had
[00:41:07] was not connected to any of that. He was
[00:41:09] never really interested in
[00:41:11] LLMs and discovered uh
[00:41:14] GPT-4 or, you know, 2023 when it came
[00:41:16] out.
[00:41:17] And basically he had an epiphany and
[00:41:18] said, "Oh my god, those systems, you
[00:41:20] know, are really close to human-level
[00:41:22] intelligence and they have
[00:41:24] possibly they have subjective
[00:41:25] experience.
[00:41:26] Uh
[00:41:28] and he he did a a quick calculation
[00:41:29] saying like, "Okay, the human cortex has
[00:41:32] about 16 billion neurons. If you want to
[00:41:35] um
[00:41:37] do something like backprop, okay? The
[00:41:39] brain doesn't do
[00:41:41] backprop directly.
[00:41:42] But if it does something like backprop,
[00:41:44] like some sort of, you know, gradient
[00:41:45] estimation for some sort of objective
[00:41:47] function,
[00:41:48] you would probably need like a a network
[00:41:50] of a few neurons to kind of reproduce
[00:41:52] the functionality of a virtual neuron in
[00:41:54] a in a neural net."
[00:41:56] So he said like, "Let's assume, you
[00:41:58] know, maybe you need you need
[00:42:00] a circuit of 10
[00:42:02] actual neurons
[00:42:03] to reproduce what a a backprop neuron
[00:42:05] does.
[00:42:07] Then all of a sudden your your cortex is
[00:42:09] only 1.6 billion neurons.
[00:42:12] Oh my god, GPT-4 is really close to
[00:42:13] this. Okay, so maybe it's as smart you
[00:42:15] know, it's going to get as smart as
[00:42:16] humans. I do not believe in this claim
[00:42:18] at all. This is kind of you know, Jeff's
[00:42:22] uh
[00:42:23] way of
[00:42:25] saying
[00:42:26] Okay, basically
[00:42:28] I can retire. I can declare victory.
[00:42:31] You know,
[00:42:32] I searched for the learning algorithm of
[00:42:34] the cortex all my career.
[00:42:36] Uh
[00:42:37] maybe I didn't discover what it really
[00:42:39] was, but backprop seems to be like a
[00:42:41] good substitute for it.
[00:42:42] It works really well.
[00:42:44] And so
[00:42:45] maybe that's all we need. So, I can
[00:42:47] retire.
[00:42:49] Uh
[00:42:50] and [laughter]
[00:42:51] and go around the world and give talks
[00:42:52] about you know, the potential
[00:42:54] uh
[00:42:56] promises and dangers of uh of AI.
[00:43:00] Uh that's basically what you know, I
[00:43:02] think what his uh
[00:43:03] uh intellectual kind of trajectory has
[00:43:06] been.
[00:43:07] Uh
[00:43:08] he's much less
[00:43:10] vocal about the potential dangers now
[00:43:12] than he was
[00:43:14] uh
[00:43:15] a year or two ago.
[00:43:16] He kind of realized there's probably a
[00:43:17] way to design
[00:43:19] truly intelligent systems. So, first of
[00:43:20] all, he probably you know, he realized
[00:43:22] that
[00:43:23] current LLMs are not that smart first of
[00:43:25] all. And and second
[00:43:27] uh
[00:43:28] that there's probably a need for a few
[00:43:30] breakthroughs like conceptual
[00:43:31] breakthroughs before we get to
[00:43:33] human-like intelligence.
[00:43:35] And third, that the the blueprint of
[00:43:37] those systems will be quite different
[00:43:39] from LLMs and we have probably have a
[00:43:42] way of
[00:43:43] you know, making them controllable and
[00:43:45] things like that. Yeah. I've been saying
[00:43:47] this for years, but
[00:43:49] Okay, he's sort of discovered this
[00:43:51] recently. Yeah. Same kind of there's a
[00:43:53] similar thing with Yoshua. I think what
[00:43:55] they are both worried about is
[00:43:58] the ability of
[00:43:59] society
[00:44:01] and the political system to make sure
[00:44:04] that the benefits of of AI will be
[00:44:06] maximized.
[00:44:07] And AI would not, you know, just
[00:44:10] profit you know, make a few rich people
[00:44:13] even richer.
[00:44:14] And uh you know,
[00:44:17] accentuate inequalities and and you
[00:44:20] know, cause major catastrophes because
[00:44:23] of bad usage. Okay, this is not like the
[00:44:25] the doomer scenario of AI taking over
[00:44:27] the world. It's more bad use users. What
[00:44:31] seems possible with the LLMs of today?
[00:44:32] Which is a danger, but you know, I don't
[00:44:35] I don't think it's as
[00:44:37] apocalyptic as you know, what some
[00:44:39] people have claimed it is.
[00:44:41] Certainly not as apocalyptic as what
[00:44:43] even Anthropic has claimed.
[00:44:45] And it's trying to kind of lobby
[00:44:46] governments into you know, scaring
[00:44:48] governments into kind of regulating AI
[00:44:51] because because of that.
[00:44:52] I don't I don't I don't subscribe to
[00:44:55] this at all. They seem to genuinely
[00:44:56] believe it. I think they genuinely
[00:44:58] believe it, but also I think there is,
[00:45:01] you know, some kind of commercial good
[00:45:03] commercial reasons for them to believe
[00:45:04] that. And to kind of
[00:45:06] uh
[00:45:08] you know, brainwash
[00:45:09] some people and governments into
[00:45:11] thinking their systems are are
[00:45:12] dangerous. And it sounds like you know,
[00:45:14] with these other architectures, do you
[00:45:15] think they're cuz obviously it doesn't
[00:45:16] you know, as maybe
[00:45:18] bearish as you are on LLMs being the end
[00:45:20] state of everything, you know, you have
[00:45:22] some pretty ambitious timelines too for
[00:45:23] for these new architectures. And so it
[00:45:25] doesn't seem like you think we're
[00:45:26] particularly far away from from from
[00:45:28] some very compelling capabilities. How
[00:45:30] do you think about I guess the the
[00:45:31] safety around, you know, if it ends up
[00:45:33] if these breakthroughs end up coming
[00:45:34] from new architectures and whether that
[00:45:35] should make us rest easier or not. I'm
[00:45:38] going to say something that's again
[00:45:40] might be controversial. Uh
[00:45:42] and certainly my some of my colleagues
[00:45:44] at Meta didn't like me saying this, but
[00:45:46] I think LLMs are interestingly unsafe.
[00:45:49] I don't think they can be made
[00:45:51] reliable and safe. Okay.
[00:45:53] They cannot be made reliable because you
[00:45:55] can't stop them from hallucinating.
[00:45:57] Uh and if they're agentic, you cannot
[00:45:59] guarantee they're not going to like take
[00:46:01] an action that, you know, they didn't
[00:46:03] predict the outcome of and that
[00:46:05] >> I mean, does it surprise you they can do
[00:46:06] these like 15-hour coding tasks given
[00:46:08] the concerns around reliability?
[00:46:09] >> Well, but coding is something where you
[00:46:10] can actually verify that, you know, the
[00:46:13] the the code that you generate uh you
[00:46:15] know, satisfy your specification.
[00:46:17] Um
[00:46:19] but
[00:46:20] but not everything is coding. And and
[00:46:23] there are examples of, you know,
[00:46:25] uh
[00:46:26] coding agents like wiping up your
[00:46:28] your hard drive,
[00:46:30] like
[00:46:31] uh
[00:46:32] or or doing stupid things, right? That
[00:46:33] makes you lose a lot of money or data or
[00:46:36] whatever.
[00:46:37] So, I think I think uh you know, LLMs in
[00:46:40] their current forms
[00:46:41] uh are are intrinsically unsafe
[00:46:44] because they cannot predict the
[00:46:45] consequences of their actions and
[00:46:46] because the way the task that they
[00:46:49] accomplish is determined
[00:46:51] uh is
[00:46:53] is subject to their training. You know,
[00:46:56] you you give them a prompt
[00:46:59] and then they will accomplish a task
[00:47:01] that correspond to that prompt only to
[00:47:03] the ex-
[00:47:04] to the extent that their training
[00:47:06] has conditioned them to actually do the
[00:47:08] right task corresponding to this prompt.
[00:47:11] But there is no, like, you know,
[00:47:12] hardwired constraint that will force
[00:47:15] them to accomplish this task
[00:47:17] and then, you know, predict that the
[00:47:19] task will be accomplished properly.
[00:47:20] Yeah, I mean, I think people were saying
[00:47:21] in the early days, right? They would
[00:47:22] you'd ask them a question and they'd
[00:47:23] keep asking the they'd keep asking the
[00:47:24] question, right?
[00:47:25] >> Right. Right. For example. [laughter]
[00:47:27] Uh
[00:47:28] or I mean, also they don't have common
[00:47:29] sense. Right. So, I mean, there's the
[00:47:31] the joke that was circulating like a
[00:47:33] month ago of
[00:47:35] you know, I need to wash my car and you
[00:47:37] know, the the car wash is a 100 yards
[00:47:39] from my house, should I walk?
[00:47:43] I tried it again like maybe 2 weeks ago.
[00:47:45] Uh they all say, "Yes, you should walk."
[00:47:47] Except Gemini.
[00:47:49] Gemini says
[00:47:50] >> they're training on your video of of
[00:47:51] having done having given that speech
[00:47:53] before? The The was not my video because
[00:47:54] [laughter] I I come up with this
[00:47:55] example.
[00:47:56] >> Whoever came up with it. Yeah, right.
[00:47:57] Whoever came up with it. But they are
[00:47:58] issuing sentences, right? Where where I
[00:48:00] said like, you know, an LLM can do this
[00:48:02] and then 6 months later it was like
[00:48:03] people are doing it and it's simply
[00:48:04] because, you know, as soon as people
[00:48:07] watch the podcast of me saying LLMs can
[00:48:10] do this, they of course type it into
[00:48:12] ChatGPT. So now it becomes part of the
[00:48:14] training set. And now of course, you
[00:48:16] know, the next version has that uh you
[00:48:19] know, that that thing in the fine-tuning
[00:48:21] set and of course it can answer the
[00:48:22] question but it's not because it's it
[00:48:23] becomes smart all of a sudden. It's just
[00:48:25] because it was explicitly trained with
[00:48:27] that question. So LLMs are intrinsically
[00:48:29] unsafe. Uh I don't think there is any
[00:48:32] way to fix that in the current
[00:48:34] um paradigm.
[00:48:36] Um and what I've been proposing is
[00:48:38] the architecture I've been talking about
[00:48:40] is objective-driven AI. So basically,
[00:48:43] you give an objective to an AI system,
[00:48:46] which is accomplish this task. Now,
[00:48:48] how does the system
[00:48:50] knows
[00:48:51] it will accomplish this task? It has a
[00:48:53] world model and it predicts
[00:48:55] uh
[00:48:57] you know, the outcome
[00:48:59] of a sequence of actions it imagines
[00:49:01] taking.
[00:49:02] Uh and if this uh outcome
[00:49:05] satisfies
[00:49:07] a
[00:49:09] cost function that you know, describes
[00:49:11] to what extent the task has been
[00:49:12] accomplished or not accomplished,
[00:49:14] then that system, if
[00:49:16] if the way that system works is by
[00:49:19] optimizing by optimization, finding a
[00:49:22] sequence of actions that accomplishes
[00:49:24] this task, minimizes this cost according
[00:49:26] to its world model,
[00:49:28] it can do nothing else. Yeah. Okay. And
[00:49:32] of course there's many things that can
[00:49:33] go wrong there. In in particular,
[00:49:36] uh the cost function might be
[00:49:38] inaccurate. It could be that the cost
[00:49:40] function you think is actually measuring
[00:49:42] to what extent the task has been
[00:49:44] accomplished but perhaps
[00:49:46] it's not accurate. Okay?
[00:49:48] Uh you the world model might be
[00:49:49] inaccurate. So the prediction that the
[00:49:51] system makes is actually not the right
[00:49:52] one. So, its prediction of what was
[00:49:54] going to happen as a consequence of its
[00:49:56] action wasn't right. Okay, so the system
[00:49:58] can still make mistakes, but but it can
[00:50:01] predict the consequences of its actions
[00:50:02] to some extent, which is I think
[00:50:05] indispensable for any agentic system.
[00:50:07] Now, you can add to that system is not
[00:50:09] just
[00:50:10] a cost function that guarantees a task
[00:50:12] has been accomplished, but you can also
[00:50:14] add a bunch of other
[00:50:17] objective functions, other other cost
[00:50:18] functions, or even constraints
[00:50:21] that are safety constraints.
[00:50:23] And say, "Okay, you know, don't hurt
[00:50:24] anybody on the way, right?" And you
[00:50:26] cannot specify this at a at an abstract
[00:50:28] level, but you can have, you know,
[00:50:30] low-level objective functions that
[00:50:33] put together will guarantee that the
[00:50:34] system will not be dangerous. Uh and the
[00:50:37] system cannot violate those things by
[00:50:39] construction. It will have to satisfy
[00:50:41] those conditions.
[00:50:42] Not the case for an LLM. The LLM can
[00:50:44] always escape. There's a gap between
[00:50:47] your training error and test error.
[00:50:49] There's always going to be a prompt
[00:50:50] where the system is going to do really
[00:50:51] stupid things. To talk to one specific
[00:50:53] space around LLMs, like, you know, I I
[00:50:55] think you're obviously really excited
[00:50:56] about LLMs in healthcare, and I think
[00:50:57] you know, people have been using LLMs in
[00:50:59] healthcare for for all sorts of things.
[00:51:00] And so, I'm curious how you think about
[00:51:02] like the set of things where LLMs are
[00:51:04] just not going to work in healthcare,
[00:51:05] and you need like a
[00:51:07] model that understands the world better.
[00:51:09] So, uh I mean, designing a course of
[00:51:11] treatment for a chronic disease, for
[00:51:13] example,
[00:51:14] or even a non-chronic disease,
[00:51:17] uh for a particular patient,
[00:51:19] uh which may not completely fit into,
[00:51:22] you know, templates that you've observed
[00:51:23] before.
[00:51:24] But if you have a good mental model of
[00:51:26] the
[00:51:27] dynamics of the physiology of the
[00:51:29] patient, then you might design a course
[00:51:31] of treatment that will actually bring
[00:51:33] the the patient to a good state. Yeah.
[00:51:35] Uh when I'm saying and when I'm saying a
[00:51:36] patient, it can be
[00:51:38] a cell. Okay, how do you tell
[00:51:41] a a
[00:51:43] stem cell
[00:51:44] to turn into a
[00:51:46] uh pancreas beta cell that produces
[00:51:48] insulin.
[00:51:49] Okay, you have a patient with type 1
[00:51:51] diabetes.
[00:51:53] Um you know, they have
[00:51:55] you know, their immune system basically,
[00:51:57] you know, kind of
[00:51:59] eats up their own beta cells, right?
[00:52:01] It's autoimmune.
[00:52:02] Um how do you keep making beta cells?
[00:52:04] You know, can you send a message? Do you
[00:52:06] have a a model of a of a human cell that
[00:52:09] will allow you to figure out what
[00:52:11] sequence of message you need to send to
[00:52:14] uh a stem cell so that it turns into a a
[00:52:16] beta cell. The less LLM-pilled camp and
[00:52:18] the LLM-pilled camp talk past each
[00:52:19] other, but it's like I think it's
[00:52:21] actually very possible that both
[00:52:23] what LLMs can do, which is maybe scaling
[00:52:25] what a top doctor, the treatment you get
[00:52:27] at like the top doctor or at the top
[00:52:29] place, scaling that around the world,
[00:52:30] like unbelievable potential impact of
[00:52:32] that, right? If you're able to do that.
[00:52:34] And then, you know, I think what you're
[00:52:35] talking about, which is certainly still
[00:52:36] on the come for for a lot of these
[00:52:37] things, is okay, well, even better than
[00:52:40] the top doctor. Like, how do you how do
[00:52:41] you go do that?
[00:52:42] >> more than just a top doctor, right?
[00:52:43] Because I mean, what the LLM can do well
[00:52:45] is
[00:52:47] you know, it can it can sort of
[00:52:48] regurgitate like knowledge that you can
[00:52:50] read in books, mostly.
[00:52:52] Um but if medicine was
[00:52:55] only kind of
[00:52:57] about accumulating
[00:52:59] uh declarative language that declarative
[00:53:02] knowledge that exist in books,
[00:53:05] you can be a doctor by just reading
[00:53:06] books. And you can be a doctor by
[00:53:08] reading books. You have to do, you know,
[00:53:09] residency and, you know, actually kind
[00:53:12] of listen to the heart and like press on
[00:53:14] the belly and things like that to, you
[00:53:16] know, diagnose a disease or whatever it
[00:53:18] is. Yeah, it's interesting. I'll I'll be
[00:53:20] very curious to see whether LLMs
[00:53:21] themselves can provide like, you know,
[00:53:23] top-quality health care
[00:53:25] globally. We'll have to we'll have to
[00:53:25] check back in on that one. It seems it
[00:53:27] seems like they're pretty pretty close.
[00:53:28] You know, I definitely also want to hit
[00:53:29] on your your time at Meta cuz you spent
[00:53:30] over a decade building like one of the
[00:53:32] most respected research labs in the
[00:53:33] world. You know, obviously, you recently
[00:53:35] left. As you reflect back on on the time
[00:53:37] there, what do you think you got like
[00:53:38] most right and most wrong in your time
[00:53:40] running FAIR? So, the thing we got right
[00:53:42] is
[00:53:44] uh you know, building a a a top research
[00:53:47] lab
[00:53:48] that really sort of innovated, produced
[00:53:51] a lot of the sort of basic
[00:53:53] methods and science and tools like
[00:53:54] PyTorch
[00:53:56] um that are useful to the entire
[00:53:57] industry, right?
[00:53:59] >> [snorts]
[00:53:59] >> Uh I mean, the entire industry is built
[00:54:01] on PyTorch basically, except for a few
[00:54:03] people at Google.
[00:54:04] >> [laughter]
[00:54:05] >> And I think a a culture of
[00:54:07] uh
[00:54:08] you know, openness and and
[00:54:11] and kind of you know, scientific process
[00:54:14] which I think is is necessary for
[00:54:17] breakthrough innovation.
[00:54:19] Yeah. Um because you know, there there
[00:54:21] is a lot of there's a whole chain of
[00:54:23] innovation, right? You have blue sky
[00:54:26] research
[00:54:27] uh new concepts, a lot of that takes
[00:54:29] place in universities, some of that
[00:54:31] takes place in advanced research labs in
[00:54:33] industry
[00:54:35] which can be counted on the fingers of
[00:54:36] one hand.
[00:54:38] Uh
[00:54:38] you know, Google is a good one, uh
[00:54:40] you know, fair was a good one.
[00:54:42] Hopefully, it will still be, I'm not
[00:54:44] sure.
[00:54:44] Um
[00:54:46] and you know, a few others. Then you
[00:54:48] have okay, this is a good idea, but
[00:54:50] let's push it forward and see see if it
[00:54:52] can be
[00:54:53] uh made useful, but still at the
[00:54:56] research level. In a in a sense of
[00:54:59] we're not going to fool ourselves. We're
[00:55:00] not going to try to just you know, find
[00:55:04] a solution that just works for this
[00:55:05] problem. We we're going to see if
[00:55:08] this technique that we imagine or we
[00:55:10] picked up from other people in the
[00:55:12] community
[00:55:13] can actually be pushed and and be be
[00:55:16] made uh practical, not as a product, but
[00:55:19] like we can show that it beats some
[00:55:21] record on you know, some uh
[00:55:24] task or benchmark. And then
[00:55:26] the next stage is for the the company
[00:55:29] that hosts the research lab to say,
[00:55:30] "Okay, now we're going to push the
[00:55:31] button
[00:55:32] devote a you know, big engineering
[00:55:34] effort to that uh to that vision and
[00:55:37] push it forward.
[00:55:39] That is where a lot of projects fail.
[00:55:42] That's That's where a lot of companies
[00:55:44] kind of fail to pick up. Meta was
[00:55:46] actually pretty good at this, okay? But
[00:55:49] far from perfect.
[00:55:51] It was not like, you know, textbook
[00:55:52] example of how you do it wrong, like,
[00:55:54] you know, Xerox PARC like totally
[00:55:56] missing out on,
[00:55:57] >> Yeah. you know, you GUI interface and,
[00:55:59] you know, mouse and windowing systems,
[00:56:02] right? Meta was, you know, kind of
[00:56:04] missed a few steps, essentially. And it
[00:56:07] And it it's partly partly just
[00:56:09] organizational. It's partly because
[00:56:12] uh
[00:56:13] you need a an organization that is
[00:56:16] pretty close to research, but not
[00:56:18] completely a product organization, to
[00:56:20] take the relay
[00:56:21] of, you know, pushing the technology a
[00:56:23] little further.
[00:56:25] Not making product with a 3-month
[00:56:27] deadline, but like, you know, pushing
[00:56:28] things.
[00:56:30] And
[00:56:31] we had that at one point. Yeah. At at at
[00:56:34] Facebook and Meta.
[00:56:35] Uh and then we lost it.
[00:56:38] And
[00:56:39] FAIR was basically isolated within the
[00:56:41] company, had lots of ideas that nobody
[00:56:44] picked up on. And then in 2023, the
[00:56:46] GenAI organization was created by
[00:56:48] basically taking about 60 or 70
[00:56:52] scientists and engineers from FAIR,
[00:56:54] right? Initially, and then it built up.
[00:56:56] Um but then it was under so much
[00:56:59] short-term pressure that basically that
[00:57:01] organization, GenAI, didn't have time to
[00:57:03] talk to FAIR.
[00:57:05] And so, instead of
[00:57:07] being at the forefront and innovating in
[00:57:10] LLM,
[00:57:11] uh GenAI basically had to focus on
[00:57:14] short-term things and become very
[00:57:15] conservative.
[00:57:17] And so, there was a gap, basically, in
[00:57:18] periods of mismatch between research and
[00:57:22] uh and the Is that kind of what happened
[00:57:23] with Llama 4? Yeah.
[00:57:25] Well, even with, you know, Llama 3,
[00:57:27] starting with Llama 3.
[00:57:29] So, Llama 1 was
[00:57:31] a small project within fair. 2022 early
[00:57:33] 2023 GenAI was
[00:57:36] created. The Lama people were basically
[00:57:39] moved to GenAI.
[00:57:41] They started working on Lama 2. And then
[00:57:43] a bunch of them realized
[00:57:45] like I could do a startup.
[00:57:47] So that was the genesis of Mistral.
[00:57:50] >> Yeah. Okay. Two of the
[00:57:52] authors of
[00:57:55] Lama 1 basically created Mistral with
[00:57:57] another guy
[00:57:58] from Google. And
[00:58:01] and you know a few people kind of left
[00:58:03] and sort of did other things.
[00:58:05] This is not a kind of a happy time at uh
[00:58:08] at Meta for various reasons. And so
[00:58:10] there were you know a bunch of people
[00:58:12] kind of left. And then the the the GenAI
[00:58:15] organization was kind of took over
[00:58:17] uh
[00:58:18] Lama
[00:58:20] 2 to some extent and Lama 3 and 4 was
[00:58:23] under so much short-term pressure that
[00:58:25] they became very conservative.
[00:58:27] And you know it's a combination of what
[00:58:30] is apparently of of the groups but but
[00:58:32] like pressure from the leadership and
[00:58:36] I mean there's many ways things can go
[00:58:37] wrong and you can't blame anyone in
[00:58:39] particular but
[00:58:40] um but yeah that's kind of what
[00:58:43] happened.
[00:58:43] >> I mean it feels like a lot of these
[00:58:44] organizations obviously are under
[00:58:46] short-term pressure right now because
[00:58:47] there's just a incredible race going on.
[00:58:49] And so I'm curious like obviously this
[00:58:51] this you know fair setup you had and
[00:58:52] kind of there's similar one you know at
[00:58:54] Google for for many years and certainly
[00:58:56] many researchers running around Open AI
[00:58:57] and Anthropic trying many different
[00:58:58] things. Do you think like
[00:59:01] that is still possible going forward or
[00:59:03] like is the only you know is one of the
[00:59:04] only paths to leave and and do your own
[00:59:06] company or or you know are there still
[00:59:08] places within the industry that you
[00:59:10] think have this like original ethos of
[00:59:12] fair even amidst the race that is race
[00:59:14] dynamics that are happening? I think
[00:59:15] there are a few places within Google
[00:59:17] research and DeepMind that where where
[00:59:19] people actually do research.
[00:59:21] Um
[00:59:22] but increasingly the industry has become
[00:59:24] more kind of closed right? I mean Google
[00:59:26] has certainly climbed up and, you know,
[00:59:29] Meta and Fair even is kind of going a
[00:59:31] bit in the same direction. There are
[00:59:32] restrictions on publication now, like
[00:59:35] more restrictions.
[00:59:36] Uh and so, it's still less appealing for
[00:59:39] people who really want to kind of do
[00:59:41] breakthrough research and, you know,
[00:59:43] they they don't get as much resources.
[00:59:45] If they do something that is
[00:59:47] relevant in medium term, they are told
[00:59:49] not to talk about it. And and so, it's
[00:59:51] it's not, you know, it's not a good
[00:59:53] atmosphere, I think, for for
[00:59:55] breakthrough. It's not conducive. You
[00:59:57] you, you know,
[00:59:58] I mean, basically, the get the best way
[01:00:00] to get breakthrough research
[01:00:03] of the type that, you know, you
[01:00:05] we were getting it in the early days of
[01:00:06] Fair and
[01:00:08] uh you know, at Bell Labs in the good
[01:00:09] days and Xerox PARC is you hire the best
[01:00:12] people and those are people who have a
[01:00:13] good nose to know what to work on,
[01:00:16] what projects to kind of attack.
[01:00:18] You give them the means to succeed and
[01:00:21] you get the out of the way. All
[01:00:23] right, pardon my French.
[01:00:24] >> [laughter]
[01:00:27] >> Yeah, I mean, I'm curious like what you,
[01:00:28] you know, what impact it then ends up
[01:00:29] having on the broader research
[01:00:31] community. So, obviously, one of the
[01:00:31] legacies of Fair is you trained, you
[01:00:33] know, uh so many researchers, right? And
[01:00:35] and like they're all throughout the
[01:00:36] ecosystem. Um and it feels like now the
[01:00:38] maybe equivalent to those people that
[01:00:39] came in younger in their careers at
[01:00:41] Fair, you know, they're joining these
[01:00:42] these labs uh with maybe shorter term
[01:00:45] priorities and focus. And I guess I'm
[01:00:46] wondering like, you know, uh in this
[01:00:48] current ecosystem where it feels like a
[01:00:49] lot of younger people getting into the
[01:00:51] field are thrust much more into these
[01:00:53] like short-term dynamics. Does that
[01:00:54] change anything about the way the the
[01:00:56] ecosystem evolves? Well, I mean, the
[01:00:58] people who tend to want to work with me
[01:01:00] are generally people who
[01:01:03] uh
[01:01:04] you know, sufficiently crazy to do it,
[01:01:06] first of all.
[01:01:07] >> Very very fair. And uh or or, you know,
[01:01:09] kind of subscribe to the the whole idea
[01:01:11] that
[01:01:12] uh in academia and during your PhD, you
[01:01:15] should work on the next generation of
[01:01:18] of AI system. You shouldn't work on the
[01:01:19] current generation. Yeah.
[01:01:21] >> Like if you work on an in in academia
[01:01:23] now, it's incredibly boring. At least to
[01:01:24] me it's boring. It's basically kind of
[01:01:26] studying how how and why LLMs work and
[01:01:30] explaining why they work or what their
[01:01:32] limitations are. It's like descriptive
[01:01:34] science. It's It's really not, you know,
[01:01:36] kind of creative
[01:01:37] very creative. Like, I I don't find that
[01:01:40] particularly interesting. It's useful.
[01:01:41] Yeah. Uh
[01:01:43] And, you know, if you really want to
[01:01:45] kind of show how to do new things with
[01:01:47] LLMs, like
[01:01:49] you're not going to have the GPUs you
[01:01:50] need for that. So, like, forget that.
[01:01:52] Like, don't work on LLM if if you're
[01:01:54] doing a PhD. Like, there's no point. You
[01:01:56] cannot contribute. How do you know it
[01:01:57] was time to leave Meta? It sounds like
[01:01:58] it was, you know, uh you know, you were
[01:02:00] thinking through some of these things
[01:02:01] over a period of time. You know, was
[01:02:02] there a moment that it crystallized or
[01:02:04] Well, it was a combination of things,
[01:02:05] right? Uh So, first of all, you have to
[01:02:07] understand uh a lot of people have like
[01:02:10] completely wrong idea about what my role
[01:02:12] at
[01:02:13] uh Facebook and Meta was. So, I joined
[01:02:15] in late 2013. Really kind of started
[01:02:19] early 2014. The first 4 and 1/2 years, I
[01:02:22] was director of FAIR. So, I built the
[01:02:24] FAIR organization,
[01:02:25] uh set up the culture, hired the key
[01:02:27] people,
[01:02:28] and and sort of managed it.
[01:02:30] Um
[01:02:32] And
[01:02:33] after 4 and 1/2 years, I stepped down
[01:02:35] from that uh role
[01:02:38] for a number of reasons. I then I became
[01:02:40] chief AI scientist. Okay, so
[01:02:42] uh the the
[01:02:44] the reason is uh
[01:02:46] you know, I was
[01:02:49] basically getting close to
[01:02:52] um
[01:02:53] turning 60.
[01:02:54] >> [laughter]
[01:02:56] >> First of all, 58. And
[01:02:58] uh
[01:03:00] I just don't want to do management.
[01:03:02] Okay. I mean, I was willing to do it for
[01:03:04] a while to get the the organization
[01:03:06] started, but I'm just not good at it.
[01:03:08] It's not the thing I'm I'm more like a,
[01:03:10] you know,
[01:03:11] scientific or technical
[01:03:13] visionary and engineer and scientist.
[01:03:16] So,
[01:03:17] uh
[01:03:18] other people are much better at
[01:03:19] management than I am.
[01:03:20] >> [laughter]
[01:03:20] >> So, I basically stepped down uh
[01:03:22] you know, two other people uh Joelle
[01:03:24] Pineau and uh Antoine Bordes basically
[01:03:28] took over uh
[01:03:29] the directorship of of FAIR. And I
[01:03:32] became chief AI scientist. So, um
[01:03:35] I was reporting to the CTO.
[01:03:38] And uh
[01:03:39] and
[01:03:40] you know, had roles of
[01:03:43] uh
[01:03:45] you basically we're starting a research
[01:03:46] project that I thought
[01:03:48] was necessary because the ambition of
[01:03:50] FAIR was always to build intelligent
[01:03:52] systems.
[01:03:53] Right? And I thought
[01:03:55] you know, I put my own research in in
[01:03:57] parentheses while I was running FAIR. I
[01:03:59] just didn't didn't have the time.
[01:04:01] And I thought it was important to
[01:04:03] basically kind of
[01:04:05] design the architecture of
[01:04:08] of like human-level,
[01:04:10] you know,
[01:04:11] human-like AI systems.
[01:04:14] Uh and
[01:04:16] you know, I had come up with the
[01:04:19] concept that this was going to be based
[01:04:21] on self-supervised learning on on, you
[01:04:23] know, prediction from
[01:04:25] sensory signals like video, things like
[01:04:27] that. I mean, this is these are old
[01:04:28] ideas.
[01:04:29] And uh and world models. I actually gave
[01:04:32] a keynote at NeurIPS in 2016
[01:04:35] where I I said like this is the way AI
[01:04:37] research should go like world models
[01:04:38] predict, you know, consequences of your
[01:04:40] actions and plan. And I said like, you
[01:04:42] know, RL is not the thing that will take
[01:04:45] us there cuz it's too inefficient.
[01:04:47] Supervised learning has shown its
[01:04:49] limits. And so, the future is
[01:04:50] self-supervised learning and world
[01:04:52] models.
[01:04:53] So, how do we do self-supervised
[01:04:54] learning and world models? And and I
[01:04:56] started a few projects on this with like
[01:04:58] a few avenues that didn't pan out.
[01:05:00] Uh some projects on video prediction and
[01:05:03] stuff like that. And uh and then came up
[01:05:05] with this uh concept that you could
[01:05:07] train self-supervised learning from
[01:05:09] video. Um but you have to train the
[01:05:11] system to make prediction in your
[01:05:12] representation space. So, that's the
[01:05:14] idea of JEPA. Yeah. And if you have
[01:05:15] JEPA, you can turn it into a world model
[01:05:17] by making it action conditioned, and
[01:05:19] then you can use it for planning. So, I
[01:05:21] had this idea around 2020, and in 2022,
[01:05:23] I wrote a long vision paper. So, I said,
[01:05:25] "I'm just going to write a paper with my
[01:05:27] entire vision, okay?
[01:05:29] Spill all my secrets like I don't care.
[01:05:31] Uh, but maybe that will rally a bunch of
[01:05:33] people to to that vision."
[01:05:35] And boy, did it work.
[01:05:37] >> [laughter]
[01:05:38] >> Because not only did I
[01:05:41] rally, you know, a bunch of students who
[01:05:43] kind of came working with me at NYU or
[01:05:45] in Paris because they wanted to work on
[01:05:47] this,
[01:05:48] but also a whole team at at at FAIR who
[01:05:50] said like,
[01:05:51] "This sounds great. That's what we want
[01:05:52] to work on." And then Joel Pino
[01:05:55] uh, said, "Well, maybe this should be
[01:05:56] like a major mission of uh,
[01:05:59] of of FAIR." Uh, we called it
[01:06:01] advanced machine intelligence. Yeah.
[01:06:03] That was the internal name of the
[01:06:04] project.
[01:06:05] >> Interesting. Okay.
[01:06:06] >> And they let you leave with it.
[01:06:08] And now it's the name of the company.
[01:06:09] Um, and you know, Mark Zuckerberg, you
[01:06:12] know, kind of
[01:06:14] kind of read that paper and knew what it
[01:06:16] was about and subscribed to the project.
[01:06:18] And Andrew Bosworth, the CTO, also.
[01:06:20] And uh, Mike Schroepfer, the uh,
[01:06:23] previous CTO,
[01:06:24] uh, Chris Cox, who was my my direct
[01:06:27] manager, chief product officer, also
[01:06:28] loved the idea. So, like, you know,
[01:06:30] there was a lot of support in the
[01:06:31] leadership uh, about this project that
[01:06:34] we internally called AMI.
[01:06:35] Uh,
[01:06:37] and uh, and you know, and and
[01:06:40] and it started
[01:06:42] really kind of working uh, for for
[01:06:45] video.
[01:06:47] But then,
[01:06:48] you know, company kind of refocused all
[01:06:50] of its effort on LLM.
[01:06:52] Despite support from Mark and Andrew,
[01:06:56] uh,
[01:06:57] Bos, we call him Bos. Um,
[01:07:00] you know, the all the layers below,
[01:07:02] like,
[01:07:03] didn't see the point, I think. And so,
[01:07:06] politically, it sort of became a little
[01:07:08] difficult. Uh the applications as I as I
[01:07:11] said of
[01:07:12] Japan world model are there are
[01:07:14] applications in like, you know, wearable
[01:07:16] agents and stuff like that, but and
[01:07:18] robotics, but but Meta chose to get rid
[01:07:21] of its entire robotics AI group um that
[01:07:26] was led by Jitendra Malik who's now at
[01:07:28] Amazon.
[01:07:29] And so,
[01:07:31] you know, clearly it wasn't the right
[01:07:33] environment anymore. Most of the
[01:07:34] applications were in industry that Meta
[01:07:36] had no interest in. Uh
[01:07:39] FAIR was increasingly getting pressure
[01:07:42] to kind of basically help MSL with uh
[01:07:46] LLMs.
[01:07:47] Um so,
[01:07:49] yeah, you know, it it make clear it make
[01:07:51] clear. And and that, you know,
[01:07:54] sort of ramming uh worked really well
[01:07:57] with investors, too, because
[01:07:59] when I had to raise money for Emmy,
[01:08:02] everybody knew my story. And you Anybody
[01:08:04] knew, you know, many investors
[01:08:07] um
[01:08:08] you know, staff at various VCs that read
[01:08:10] my paper and or had listened to my talks
[01:08:13] and had bought my story. They were
[01:08:14] realizing, you know, LLMs had
[01:08:15] limitations and, you know, were kind of
[01:08:20] interested by the idea of like building
[01:08:22] the next generation AI systems.
[01:08:24] >> I guess was was like the Scale
[01:08:25] acquisition like part of this catalyst
[01:08:26] of of like the pure LLM focus
[01:08:28] internally? Yeah, definitely. I mean,
[01:08:30] there's probably some, you know, other
[01:08:31] reasons to it. I think, you know, maybe
[01:08:34] um
[01:08:35] uh [snorts] I don't have any sort of
[01:08:36] inside information to comment on this,
[01:08:38] but uh
[01:08:39] it's possible that Mark sees in Alex
[01:08:41] kind of a potential successor to
[01:08:43] himself, like a younger version of
[01:08:44] himself. Yeah, I feel like that like uh
[01:08:47] a lot of the popular narrative or or,
[01:08:49] you know, in the media has been like,
[01:08:50] oh, like, you know, when Alex comes in,
[01:08:52] it then gets harder to run like a
[01:08:53] research organization. You know, I don't
[01:08:54] know if that the extent you felt that or
[01:08:56] >> Well, okay, so here is a big
[01:08:58] misconception uh about my role, my
[01:09:01] relation to Alex, and how AI was run at
[01:09:04] Meta.
[01:09:05] I had
[01:09:06] zero
[01:09:08] technical contribution to Llama, like
[01:09:10] none whatsoever. My one contribution to
[01:09:12] Llama
[01:09:14] was to argue for open-sourcing Llama 2
[01:09:16] because there was a big internal debate
[01:09:17] whether we should open-source. Like the
[01:09:20] legal department was against it.
[01:09:22] The policy department was
[01:09:24] kind of against it. Uh
[01:09:27] the comms department was for it. All the
[01:09:29] engineering side was for it. Like Boz
[01:09:32] was for it.
[01:09:33] Uh so there were like enormous internal
[01:09:35] discussions at a very high level, you
[01:09:36] know, 40 people from Mark Zuckerberg
[01:09:39] down every week for 2 hours
[01:09:41] >> [laughter]
[01:09:41] >> for months. So So really it was, you
[01:09:45] know, kind of a a big debate internally,
[01:09:47] and I really really you know, pushed um
[01:09:50] argued for for the fact that uh
[01:09:53] you know, and and Boz also was was very
[01:09:55] vocal about it that
[01:09:57] um
[01:09:58] the uh
[01:09:59] you know,
[01:10:00] uh safety risks were basically
[01:10:02] overblown.
[01:10:03] Uh the opportunities to create an
[01:10:05] industry were
[01:10:07] extremely strong. Um
[01:10:10] and that we were going to jump-start the
[01:10:11] AI industry by open-sourcing Llama 2,
[01:10:13] and in fact, that's exactly what
[01:10:14] happened. So but I had zero contribution
[01:10:18] to to Llama
[01:10:19] positive or negative. Like I I didn't do
[01:10:21] anything to stop it or slow it down or
[01:10:22] anything. There was a lot of people
[01:10:24] working on LLMs within FAIR, and it was
[01:10:26] fine.
[01:10:27] Uh
[01:10:28] and I never said anything against it.
[01:10:30] Okay.
[01:10:31] Um
[01:10:32] Other than saying this is not a path to
[01:10:34] a human-level intelligence, but it's
[01:10:35] fine. Uh
[01:10:37] it's useful.
[01:10:38] >> [laughter]
[01:10:39] >> Uh
[01:10:40] You know, same thing for speech
[01:10:41] recognition or translation, right?
[01:10:43] Uh so
[01:10:45] uh
[01:10:46] and particularly since uh 2018 when I
[01:10:48] stepped down from being director of
[01:10:50] FAIR,
[01:10:51] uh I didn't have any direct influence on
[01:10:54] what people were working on other than
[01:10:57] you know, basically you publishing my my
[01:10:59] vision and then rallying people
[01:11:02] uh around
[01:11:03] uh around my project, but
[01:11:06] you know, they they were working with me
[01:11:07] because they wanted not because I was
[01:11:08] their boss. I wasn't telling them to
[01:11:10] work with me.
[01:11:12] Um
[01:11:13] and so
[01:11:14] um
[01:11:16] so I had no positive or negative
[01:11:17] influence on LLM.
[01:11:19] >> [laughter]
[01:11:20] >> Within
[01:11:21] within Meta.
[01:11:22] Uh
[01:11:23] uh and uh I had some influence on the
[01:11:25] strategy, but it was more like the
[01:11:27] long-term and and like how how you
[01:11:29] maintain a research lab and things like
[01:11:30] this. And in the last uh year, you know,
[01:11:33] I mean, starting maybe early '24
[01:11:36] uh and certainly in '25, the the the way
[01:11:40] FAIR was kind of
[01:11:42] the direction in which it was moved and
[01:11:44] managed basically did not correspond to
[01:11:46] what I thought was necessary to preserve
[01:11:49] um
[01:11:51] you know, innovation, research, and
[01:11:52] breakthrough and preserve the good
[01:11:54] people. Like a lot of good people have
[01:11:56] left already. Yeah. And I guess a lot
[01:11:58] of, you know, it probably was harder to
[01:11:59] get people to work on the stuff you were
[01:12:01] working on internally and and I'm sure
[01:12:02] there's pressure for your you yourself
[01:12:03] to work on a lot of the LLM stuff. Yeah.
[01:12:06] Yeah. No, but a lot of other people also
[01:12:08] have left, right? No, it's it's it's
[01:12:10] fascinating. I mean, one thing I'm
[01:12:11] struck by throughout our whole
[01:12:11] conversation is I feel like you're
[01:12:13] you've like had a remarkably consistent
[01:12:15] point of view like, you know, on the
[01:12:17] in the space like FAIR for a long time
[01:12:19] and you can go back to your, you know,
[01:12:21] to a bunch of the earlier talks you
[01:12:22] referenced.
[01:12:23] You know, obviously it is a fast-moving
[01:12:24] space and and a ton of interesting
[01:12:26] things have happened in the last year.
[01:12:28] What's like one thing you've changed
[01:12:29] your mind on in the last year? I mean,
[01:12:30] the whole idea of uh
[01:12:32] what we used to call unsupervised
[01:12:33] learning that we now call
[01:12:34] self-supervised learning.
[01:12:36] Uh you know, until about
[01:12:38] 2003, the whole idea of
[01:12:41] unsupervised pre-training
[01:12:43] where you get a good representation for
[01:12:46] the input data and then you either
[01:12:48] fine-tune the the model with a little
[01:12:50] bit of supervised labeled data. And it
[01:12:53] sort of give us, you know, some evidence
[01:12:55] that this whole technique could work. I
[01:12:56] tried to apply this to video because
[01:12:59] ultimately what I wanted to do is
[01:13:01] train a system to understand how the
[01:13:02] world works by just
[01:13:04] watching the world go by, right? I mean,
[01:13:06] that's the basic idea.
[01:13:08] Uh and sort of started to argue for this
[01:13:10] in the sort of
[01:13:12] you know, early 2010s.
[01:13:14] Um
[01:13:15] did some some work on
[01:13:17] simple video prediction. We didn't have
[01:13:19] GPUs. Okay. Um
[01:13:22] and uh
[01:13:24] and then sort of doing this more
[01:13:25] seriously about after the creation of
[01:13:27] fair
[01:13:28] um by doing pixel level video prediction
[01:13:32] realizing that wasn't working. Uh but
[01:13:34] then arguing for self-supervised
[01:13:35] learning. Okay, this whole idea of like
[01:13:37] training a system generically not to
[01:13:39] solve a task but to basically just
[01:13:41] predict and then using the
[01:13:42] representation that is learned this way
[01:13:44] as input to a downstream task that you
[01:13:47] can train supervised or reinforcement or
[01:13:49] whatever.
[01:13:50] Uh so this that was a bit of the topic
[01:13:52] of my
[01:13:53] second half of my keynote at
[01:13:55] at NIPS in 2016. It was still called
[01:13:57] NIPS at the time.
[01:13:58] >> Yeah, of course. in 2016. And then I I
[01:14:01] kept kind of, you know, kind of pushing
[01:14:02] for this idea and tried to kind of
[01:14:04] discover some methods to to get that to
[01:14:06] work. And
[01:14:08] what surprised me is that that became
[01:14:10] incredibly successful but not for video,
[01:14:12] for language.
[01:14:13] LLMs basically are
[01:14:16] a a
[01:14:18] blindingly successful example of
[01:14:21] self-supervised learning.
[01:14:23] >> No, that that they are. Well, I feel
[01:14:25] like that's a that's almost like the
[01:14:25] perfect note to end on but I want to
[01:14:27] make sure to leave the last word to you.
[01:14:29] Um I feel like there's I mean, all our
[01:14:30] listeners are are very familiar with you
[01:14:32] but I want to at least give you the mic
[01:14:33] to point them to anything that you think
[01:14:35] they should they should check out with
[01:14:36] some of the new stuff you're doing or I
[01:14:37] don't know, any of your your work you
[01:14:39] want to point to.
[01:14:40] The mic is yours. Okay, let me tell you
[01:14:43] um
[01:14:44] one thing, an LLM
[01:14:46] works because when you have a sequence
[01:14:48] of discrete symbols, making predictions
[01:14:51] is easy.
[01:14:52] There's only a finite number of possible
[01:14:54] symbols in your language.
[01:14:57] 100,000 possible tokens or something
[01:14:58] like that, right? And you can
[01:15:00] have your neural net produce a a
[01:15:02] probability distribution over all
[01:15:04] possible uh tokens, and then you can
[01:15:07] sample from that distribution, shift the
[01:15:09] token into the input, and then produce
[01:15:10] the next token, and you can do auto
[01:15:12] aggressive prediction. Okay, so that's a
[01:15:14] special case. If you have the real
[01:15:15] world, you can't use a generative model.
[01:15:17] So now you have to train a system that
[01:15:19] learns a representation and makes
[01:15:20] prediction in the representation space.
[01:15:22] There's a big issue with this, which I
[01:15:24] didn't think until about 5 years ago
[01:15:26] that was
[01:15:28] easily solvable,
[01:15:30] even though I invented one taking to
[01:15:31] solve it,
[01:15:32] yeah, you know, decades before that.
[01:15:35] Uh and it's a problem that
[01:15:37] um
[01:15:39] if you take two inputs, let's say the
[01:15:41] initial segment of a video and the
[01:15:42] continuation of that video, or you take
[01:15:45] one image and a corrupted version of it,
[01:15:47] you run them both through an encoder,
[01:15:49] and you train a predictor to predict the
[01:15:51] representation of one from the
[01:15:52] representation of the other.
[01:15:54] There's a very simple solution
[01:15:56] where the system basically predicts a
[01:15:58] constant representation, and now the
[01:15:59] prediction problem becomes trivial.
[01:16:01] That's called a collapse.
[01:16:03] Representation collapse.
[01:16:05] So the big question of self-supervised
[01:16:07] learning for Jappa, for the joint
[01:16:08] embedding architecture, is how do you
[01:16:09] prevent collapse? Yeah. The solution
[01:16:11] that uh I came up with many years ago,
[01:16:15] 1993, is uh contrastive learning.
[01:16:18] So basically you have
[01:16:20] examples of things that should be
[01:16:22] predictable from one another, and then
[01:16:23] an example of things that should not be
[01:16:25] predictable from one another.
[01:16:26] Uh it turns out this method works, but
[01:16:29] uh
[01:16:30] it doesn't scale with dimension. It
[01:16:32] doesn't scale very well.
[01:16:34] Um there's another technique that was
[01:16:35] actually invented by uh
[01:16:38] Jeff Hinton and Subbiah Ecker in the
[01:16:40] late '90s, late '80s, I'm sorry. Uh
[01:16:44] where you have those two networks and
[01:16:45] you try to maximize the mutual
[01:16:46] information between them.
[01:16:48] Uh
[01:16:49] Jürgen Schmidhuber is mad at me because
[01:16:50] he also came up with a version of this
[01:16:52] [laughter]
[01:16:53] in 1992
[01:16:55] and he says that's JEPA. It's not JEPA.
[01:16:57] It's just another way of preventing
[01:16:58] collapse of a joint embedding
[01:17:00] architecture. Okay.
[01:17:01] Uh
[01:17:03] >> [snorts]
[01:17:03] >> which is
[01:17:04] fine, but it's not
[01:17:06] you know, it's a particular way of doing
[01:17:08] it which I I don't think it's
[01:17:09] particularly good. Um so
[01:17:13] um
[01:17:15] Okay. So, now you have the JEPA
[01:17:16] architecture. You have to come up with a
[01:17:17] good way of preventing collapse.
[01:17:19] And there is a couple ways. So, as
[01:17:22] already said, contrastive methods I
[01:17:24] think is not a good uh a good approach.
[01:17:27] Uh
[01:17:27] there's another set of methods that are
[01:17:29] kind of
[01:17:30] called distillation methods.
[01:17:33] And they do prevent collapse. We we
[01:17:35] don't know why.
[01:17:36] So, a good example of that is uh DINO or
[01:17:39] DINo. Yep. Um that's a joint embedding
[01:17:42] method using the distillation method.
[01:17:44] Basically, one of the encoders trains
[01:17:45] the other one is like used as a
[01:17:48] teacher for the other encoder.
[01:17:50] Uh
[01:17:51] and the encoder that is being trained,
[01:17:53] you do backprop to it. The one that is
[01:17:55] not being trained, you don't do
[01:17:56] backprop, but you share the weight with
[01:17:58] the other one with some exponential
[01:17:59] moving average.
[01:18:00] It's a collection recipe. There was a a
[01:18:02] paper from from DeepMind about it called
[01:18:04] BYOL, Bootstrap Your Own Latent, which
[01:18:06] uses this trick. That trick is derived
[01:18:08] from some intuition from reinforcement
[01:18:10] learning. And somehow it prevents
[01:18:12] collapse, but we don't know why. Okay.
[01:18:14] There's a few theoretical papers on it
[01:18:16] that explain why it
[01:18:19] possibly might work in some simple
[01:18:20] cases, but it's not satisfactory. Uh
[01:18:25] the function the cost function you think
[01:18:26] you're minimizing, you're not actually
[01:18:28] minimizing and so you can't monitor.
[01:18:30] It actually goes up when you train. It
[01:18:32] makes sense. So, we don't like this
[01:18:34] method, but it works.
[01:18:36] And some of the models we've trained,
[01:18:38] large scale video representation
[01:18:40] learning system, VJPA, VJPA2, VJPA2.1,
[01:18:44] they train using this method.
[01:18:46] Uh I Jepa also.
[01:18:48] But we're moving away from this and now
[01:18:49] we have uh
[01:18:51] a few papers that came out recently on
[01:18:54] a a specific regularizer to prevent this
[01:18:57] collapse, which basically tries to
[01:18:58] maximize the information content coming
[01:19:00] out of the encoder. So, it's in the same
[01:19:02] family as the Becker and Hinton from '89
[01:19:06] and the Schmidhuber 1992 and a bunch of
[01:19:09] others since then. And to some extent
[01:19:11] also contrastive techniques also it's
[01:19:12] not although it's not simple
[01:19:14] contrastive.
[01:19:15] Um
[01:19:17] And then the question is how do you
[01:19:18] measure information content? How do you
[01:19:19] maximize
[01:19:21] the information content coming out of a
[01:19:23] neural net?
[01:19:24] And the problem is if you want to
[01:19:25] maximize the quantity, you
[01:19:27] either need to be able to measure it or
[01:19:29] you need to have a lower bound on it.
[01:19:31] Yeah.
[01:19:32] Uh information content, we only have
[01:19:33] upper bounds.
[01:19:35] We cannot measure it. We can only come
[01:19:37] up with upper bounds. And so, we take an
[01:19:39] upper bound and we cross our fingers.
[01:19:41] Okay. And it kind of works. So, the
[01:19:43] latest one is called SigReg.
[01:19:46] That means sketch as isotropic Gaussian
[01:19:50] regularization.
[01:19:51] We had a previous one called
[01:19:54] VCReg or VICReg, variance invariance
[01:19:56] covariance regularization.
[01:19:59] Um
[01:20:00] And the SigReg stuff is really cool.
[01:20:02] Um so, this is some work by
[01:20:04] uh
[01:20:05] Randall Balestriero who's uh was a
[01:20:07] postdoc with me. He's
[01:20:08] he's a
[01:20:09] assistant professor at Brown
[01:20:11] uh now. And uh it basically consists in
[01:20:14] forcing the distribution of variables
[01:20:17] coming out of the encoder to be
[01:20:19] uh joint Gaussian essentially. So,
[01:20:21] maximizing information if you want. It's
[01:20:24] just a very different way of doing it
[01:20:25] than, you know, what what Jürgen
[01:20:27] Schmidhuber
[01:20:28] >> [laughter]
[01:20:29] >> and Subbarao and and Jeff Hinton were
[01:20:31] doing.
[01:20:32] Um
[01:20:33] And so uh uh
[01:20:35] This this is super promising in my
[01:20:36] opinion and we have you know variations
[01:20:38] of it, you know, when that we can
[01:20:39] produce sparse representations.
[01:20:42] Another one that can produce uh
[01:20:44] uh anisotropic representations but not
[01:20:46] necessarily Gaussians. And we have uh
[01:20:48] uh a paper with Randall
[01:20:51] uh and student at at Mila uh Luca Mice
[01:20:55] that
[01:20:57] where we train a world model with this.
[01:20:58] It's still small scale.
[01:21:00] But we think it's super promising. So if
[01:21:03] you want to
[01:21:05] read one paper
[01:21:06] read that paper. It's Le World Model l e
[01:21:09] world model. Awesome. I'll definitely
[01:21:10] link to it, too. Yeah. I'm I'm not
[01:21:12] responsible for the name. Randall
[01:21:13] [laughter] picked up the name.
[01:21:15] Amazing. Well, Jan, seriously, thank you
[01:21:16] so much. It is such a privilege to get
[01:21:18] to spend the last bit of time with you
[01:21:21] and really appreciate you coming on the
[01:21:23] podcast. Thanks for having me, though.
[01:21:24] It's fun. I'm Jacob Effron and this has
[01:21:26] been unsupervised learning. A podcast
[01:21:28] where I get to talk to the smartest
[01:21:29] people on AI and ask them tons of
[01:21:32] questions about what's happening with
[01:21:33] models and what it means for businesses
[01:21:35] in the world. As I hope is clear, I have
[01:21:36] a ton of fun doing this. It's a nights
[01:21:38] and weekends project in addition to my
[01:21:40] day job as an investor at Red Point, but
[01:21:42] our ability to get these incredible
[01:21:43] guests on really comes from folks like
[01:21:46] you subscribing to the podcast, sharing
[01:21:47] it with friends. It's really what
[01:21:49] ultimately makes this whole thing work.
[01:21:50] And so please consider doing that and
[01:21:52] thank you so much for your support and
[01:21:53] listening. We'll see you next episode.
