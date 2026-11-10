# Anthropic Official: Building Anthropic — Conversation with Co-Founders Dario Amodei et al.
- **YouTube URL:** https://www.youtube.com/watch?v=om2lIWXLLN4
- **Lines:** 2184

---

[00:00:00] - Why are we working on
[00:00:00] AI in the first place?
[00:00:03] I'm just gonna arbitrarily pick Jared.
[00:00:05] Why are you doing AI at all?
[00:00:07] - I mean, I was working
[00:00:07] on physics for a long time
[00:00:09] and I got bored,
[00:00:10] and I wanted to hang out
[00:00:10] with more of my friends,
[00:00:12] so yeah.
[00:00:14] - Yeah, I thought Dario pitched you on it.
[00:00:15] - I don't think I explicitly
[00:00:15] pitched you at any point.
[00:00:17] I just kind of, like, showed
[00:00:17] you results of, like, AI models
[00:00:21] and then was trying to
[00:00:21] make the point that, like,
[00:00:24] they're very general and they
[00:00:24] don't only apply to one thing
[00:00:27] and then just at some point,
[00:00:28] after I showed you enough
[00:00:28] of them, you were like,
[00:00:30] "Oh yeah, that seems like it's right."
[00:00:32] - How long had you been
[00:00:32] a professor before?
[00:00:34] Like, when you started?
[00:00:34] - I think like six years or so.
[00:00:36] I think I helped recruit Sam.
[00:00:37] - I talked to you and you were like,
[00:00:38] "I think I've created a good bubble here-"
[00:00:40] - Yeah.
[00:00:41] - "And like my goal is
[00:00:41] to get Tom to come back."
[00:00:43] That worked.
[00:00:43] - And did you meet everyone through Google
[00:00:45] when you were doing the
[00:00:45] interpretability stuff, Chris?
[00:00:48] - No.
[00:00:49] So I guess
[00:00:50] I actually met a bunch
[00:00:50] of you when I was 19
[00:00:52] and I was visiting-
[00:00:52] - Oh yeah?
[00:00:53] - In the Bay Area for the first time.
[00:00:54] So I guess I met Dario and Jared then,
[00:00:57] and I guess they were postdocs,
[00:00:58] which I thought was very cool at the time.
[00:01:00] And then I was working at
[00:01:00] Google Brain and Dario joined
[00:01:03] and we sat side by side,
[00:01:03] actually, for a while.
[00:01:05] We had desks beside each other,
[00:01:07] and I worked with Tom there as well.
[00:01:08] And then, of course,
[00:01:09] I got to work with all of you
[00:01:09] at OpenAI when I went there.
[00:01:13] - Yeah.
[00:01:14] - So I guess I've known
[00:01:14] a lot of you for, like,
[00:01:15] more than a decade, which is kind of wild.
[00:01:17] - If I remember correctly,
[00:01:18] I met Dario in 2015 when I went
[00:01:18] to a conference you were at
[00:01:22] and I tried to interview
[00:01:22] you and Google PR said
[00:01:24] I would've read all of
[00:01:24] your research papers
[00:01:27] that you needed to-
[00:01:27] - Uh, yeah, I think I was writing
[00:01:29] "Concrete problems in AI safety"
[00:01:31] when I was at Google.
[00:01:32] - I think you wrote a
[00:01:32] story about that paper.
[00:01:34] - I did.
[00:01:35] - I remember right before
[00:01:35] I started working with you,
[00:01:38] I think you invited me to the office
[00:01:40] and I got to like come chat
[00:01:41] and just like tell me everything about AI.
[00:01:44] And you like explained,
[00:01:46] I remember afterwards being like,
[00:01:48] "Oh, I guess this stuff is
[00:01:50] much more serious than I realized.
[00:01:51] And you were, like,
[00:01:53] probably explaining
[00:01:53] the big blob of compute
[00:01:54] and like parameter counting
[00:01:56] and how many neurons are in
[00:01:56] the brain and everything.
[00:01:58] - And I feel like Dario often
[00:01:58] has that effect on people;
[00:02:00] "This is much more
[00:02:00] serious than I realized."
[00:02:02] - Yeah, I'm the bringer of happy tidings.
[00:02:06] - But I remember when we were at OpenAI
[00:02:09] when there was the scaling law stuff
[00:02:11] and just making things bigger
[00:02:12] and it started to feel
[00:02:12] like it was working,
[00:02:14] and then it kind of kept on eerily working
[00:02:16] on a bunch of different projects,
[00:02:18] which I think is how we all ended up
[00:02:20] working closely together,
[00:02:22] 'cause it was first GPT-2
[00:02:24] and then scaling laws and
[00:02:24] GPT-3 and we ended up-
[00:02:26] - Yeah, we were the blob of people
[00:02:28] that were making things work.
[00:02:28] - Yeah.
[00:02:30] - That's right.
[00:02:31] - I think we're also excited about safety,
[00:02:32] 'cause in that era there
[00:02:32] was sort of this idea that
[00:02:34] AI would become very powerful
[00:02:37] but, like, potentially not
[00:02:37] understand human values
[00:02:41] or not even be able to
[00:02:41] communicate with us.
[00:02:42] And so I think we were
[00:02:42] all pretty excited about
[00:02:44] language models as a
[00:02:44] way to kind of guarantee
[00:02:48] that AI systems would have to understand
[00:02:50] kind of implicit knowledge that-
[00:02:52] - And RL from human feedback
[00:02:52] on top of language models,
[00:02:56] which was the whole reason
[00:02:56] for scaling these models up
[00:02:59] was that, you know, the
[00:02:59] models weren't smart enough
[00:03:03] to do RLHF on top of,
[00:03:06] so that's the kind of intertwinement of
[00:03:08] safety and scaling of the
[00:03:08] models that we, you know,
[00:03:10] still believe in today.
[00:03:11] - Yeah, I think there was
[00:03:11] also an element of like
[00:03:14] the scaling work was done
[00:03:14] as part of the safety team
[00:03:17] that, you know-
[00:03:17] - Mm-hmm.
[00:03:18] - Dario started at OpenAI,
[00:03:19] because we thought that
[00:03:19] forecasting AI trends
[00:03:22] was important to be able
[00:03:22] to have us taken seriously
[00:03:25] and take safety seriously as a problem.
[00:03:27] - Correct.
[00:03:28] - Yeah, and we took,
[00:03:29] I remember being in
[00:03:29] some airport in England
[00:03:31] sampling from GPT-2 and using
[00:03:31] it to write fake news articles
[00:03:35] and Slacking Dario and being like,
[00:03:37] "Oh, this stuff actually works.
[00:03:38] It might have, like,
[00:03:39] huge policy implications."
[00:03:41] I think Dario said something like, "Yes."
[00:03:46] His typical way.
[00:03:48] But then we worked on that a bunch
[00:03:49] as well as the release stuff,
[00:03:49] which was kind of wild.
[00:03:51] - Yeah, I remember the release stuff.
[00:03:52] I think that was when we first
[00:03:52] started working together.
[00:03:54] - Yeah.
[00:03:54] - That was a fun time.
[00:03:56] - Yes.
[00:03:56] - The GPT-2 launch.
[00:03:57] - Yeah.
[00:03:58] But I think it was good for
[00:03:58] us 'cause we did a kind of
[00:04:00] slightly strange,
[00:04:00] safety-oriented thing altogether,
[00:04:03] and then we ended up doing Anthropic,
[00:04:05] which is a much larger, slightly strange,
[00:04:08] safety-oriented thing-
[00:04:09] - That's right.
[00:04:09] - Together.
[00:04:10] - So I guess just like going
[00:04:10] back to the concrete problems,
[00:04:13] 'cause I remember,
[00:04:14] so I joined OpenAI in like 2016,
[00:04:17] like one of the first
[00:04:17] 20 employees or whatever
[00:04:19] with you, Dario,
[00:04:20] and I remember at that time
[00:04:21] the concrete problems in AI safety
[00:04:23] seemed like it was like the
[00:04:23] first mainstream AI safety-
[00:04:26] - Yes.
[00:04:26] - Paper, I guess?
[00:04:27] I don't really know if I ever
[00:04:27] asked you what the story was
[00:04:29] for how that came about.
[00:04:31] - Chris knows the story,
[00:04:31] 'cause he was involved in it.
[00:04:34] I think, you know, we were both at Google.
[00:04:36] I forget what other
[00:04:36] project I was working on,
[00:04:38] but like with many things,
[00:04:40] it was my attempt to kind
[00:04:40] of procrastinate from
[00:04:43] whatever other project I was working on
[00:04:44] that I've now
[00:04:45] completely forgotten what it was.
[00:04:47] But I think it was like Chris
[00:04:47] and I decided to write down
[00:04:52] what are some open problems
[00:04:52] in terms of AI safety,
[00:04:55] and also AI safety you
[00:04:55] usually talked about
[00:04:57] in this very kind of
[00:04:57] abstruse, abstract way.
[00:05:01] Can we kind of ground it in the ML
[00:05:03] that was going on at the time?
[00:05:04] I mean, now there's been, like,
[00:05:04] you know, six, seven years
[00:05:08] of work in that vein,
[00:05:10] but it was almost a
[00:05:10] strange idea at the time.
[00:05:12] - Yeah, I think there's a
[00:05:12] way in which it was almost a
[00:05:14] kind of political project,
[00:05:14] where at the time,
[00:05:18] a lot of people didn't
[00:05:18] take safety seriously.
[00:05:20] So I think that there
[00:05:20] was sort of this goal
[00:05:21] to collate a list of problems
[00:05:23] that sort of people
[00:05:23] agreed were reasonable,
[00:05:26] often already existed in literature,
[00:05:28] and then get a bunch of people
[00:05:28] across different institutions
[00:05:33] who are credible to be authors.
[00:05:34] And like, I remember I
[00:05:34] had this whole long period
[00:05:37] where I just talked to 20
[00:05:37] different researchers at Brain
[00:05:39] to build support for publishing the paper.
[00:05:42] Like in some ways,
[00:05:42] if you look at it in terms of the problems
[00:05:44] and a lot of things that emphasized,
[00:05:45] I think it, you know,
[00:05:45] hasn't held up that well
[00:05:47] in that it's, you know,
[00:05:48] I think it's not really
[00:05:48] the right problems,
[00:05:49] but I think if you sort
[00:05:49] of see it instead as
[00:05:52] a consensus-building exercise,
[00:05:53] that there's something here that is real
[00:05:56] and that is worth taking seriously,
[00:05:58] then it was a pretty important moment.
[00:06:00] - I mean, you end up in this
[00:06:00] really weird sci-fi world
[00:06:02] where I remember at
[00:06:02] the start of Anthropic,
[00:06:04] we were talking about constitutional AI
[00:06:06] and I think Jared said,
[00:06:07] "Oh, we're just gonna write a constitution
[00:06:09] for a language model
[00:06:10] and that'll change all of its behavior."
[00:06:12] And I remember that
[00:06:12] sounded incredibly crazy
[00:06:15] at the time,
[00:06:16] but why did you guys
[00:06:16] think that was gonna work?
[00:06:18] Because I remember that was
[00:06:18] one of the first early, like,
[00:06:21] big research ideas we had at the company.
[00:06:23] - Yeah, I mean,
[00:06:24] I think Dario and I had
[00:06:24] talked about it for a while.
[00:06:25] I guess I think simple things
[00:06:27] just work really, really well in AI.
[00:06:29] And so like, I think the
[00:06:29] first versions of that
[00:06:32] were quite complicated,
[00:06:33] but then we kind of like
[00:06:33] whittled away into, like,
[00:06:36] just use the fact that
[00:06:36] AI systems are good at
[00:06:38] solving multiple choice exams
[00:06:40] and give them a prompt that tells them
[00:06:42] what they're looking for and
[00:06:42] that was kind of a lot of
[00:06:46] what we needed.
[00:06:47] - And then we were able to just
[00:06:47] write down these principles.
[00:06:50] - I mean, it goes back to,
[00:06:50] like, the big blob of compute
[00:06:52] or the bitter lesson or
[00:06:52] the scaling hypothesis.
[00:06:55] If you can identify, you know,
[00:06:57] something that you can
[00:06:57] give the AI data for
[00:07:00] and that's kind of a clear target,
[00:07:01] you'll get it to do it.
[00:07:02] So like here's this set of instructions,
[00:07:05] here's this set of principles.
[00:07:07] AI language models can like
[00:07:07] read that set of principles
[00:07:10] and they can compare it to the behavior
[00:07:12] that they themselves are engaging in.
[00:07:14] And so like you've got
[00:07:14] your training target there,
[00:07:16] so once you know that,
[00:07:17] I think my view and Jared's view is
[00:07:19] there's a way to get it to work;
[00:07:20] you just have to fiddle
[00:07:20] with enough of the details.
[00:07:23] - Yeah.
[00:07:23] I think it was always weird for me,
[00:07:25] especially in these early eras,
[00:07:26] 'cause like I was in physics
[00:07:26] and then coming from physics,
[00:07:30] and I think now we forget about this
[00:07:32] 'cause everyone's excited about AI,
[00:07:34] but like, I remember
[00:07:34] talking to Dario about
[00:07:37] concrete problems and other things,
[00:07:38] and I just got the sense
[00:07:38] that AI researchers
[00:07:41] were very, very kind of
[00:07:41] psychologically damaged
[00:07:43] by the AI winter
[00:07:45] where they just kind of felt like
[00:07:47] having really ambitious
[00:07:47] ideas or ambitious visions
[00:07:50] was, like, very disallowed.
[00:07:52] And that's kind of how I imagine it was
[00:07:53] in terms of talking about safety.
[00:07:55] In order to care about safety,
[00:07:56] you have to believe that AI
[00:07:56] systems could actually be
[00:07:58] really powerful and really useful,
[00:08:01] and I think that there
[00:08:01] was kind of a prohibition
[00:08:02] against being ambitious.
[00:08:04] - And I think
[00:08:05] one of the benefits is that
[00:08:05] physicists are very arrogant
[00:08:07] and so they're constantly
[00:08:09] doing really ambitious things
[00:08:10] and talking about things
[00:08:10] in terms of grand schemes,
[00:08:12] and so-
[00:08:14] - Yeah.
[00:08:15] - I mean, I think that's definitely true.
[00:08:17] Like I remember in 2014,
[00:08:18] it was like there were
[00:08:18] just like, I don't know,
[00:08:21] there were just some things
[00:08:21] you couldn't say, right?
[00:08:23] But I actually think it was
[00:08:23] kind of an extension of problems
[00:08:26] that exist across academia,
[00:08:28] other than maybe theoretical physics,
[00:08:30] where they've kind of evolved into
[00:08:32] very risk-averse institutions
[00:08:32] for a number of reasons.
[00:08:35] And even the industrial parts of AI
[00:08:37] had kind of transplanted or
[00:08:37] fork lifted that mentality.
[00:08:40] And it took a long time.
[00:08:41] I think it took it until like 2022
[00:08:43] to get out of that mentality.
[00:08:45] - There's a weird thing about like,
[00:08:46] what does it mean to be
[00:08:46] conservative and respectful,
[00:08:49] where you might think like,
[00:08:51] one version you could have is that
[00:08:53] what it means to be conservative
[00:08:53] is to take the risks
[00:08:55] or the potential harms
[00:08:55] of what you're doing
[00:08:57] really seriously and worry about that.
[00:08:59] But another kind of
[00:08:59] conservatism is to be like,
[00:09:01] "Ah, you know, taking
[00:09:01] an idea too seriously
[00:09:04] and believing that it might succeed
[00:09:05] is sort of like scientific arrogance."
[00:09:07] And so I think there's like
[00:09:07] kind of two different kinds of
[00:09:11] conservatism or caution,
[00:09:12] and I think we were sort of in a regime
[00:09:14] that was very controlled by that one.
[00:09:15] I mean, you see it historically, right?
[00:09:17] Like if you look at the
[00:09:17] early discussions in 1939
[00:09:20] between, you know, people
[00:09:20] involved in nuclear physics
[00:09:22] about what the nuclear bombs were,
[00:09:24] sort of a serious concern.
[00:09:25] You see exactly the same thing
[00:09:27] with Fermi resisting these ideas,
[00:09:30] because it just seemed
[00:09:30] kind of like a crazy thing.
[00:09:32] And other people, like Szilard or Teller,
[00:09:34] taking the ideas seriously
[00:09:36] because they were worried about the risks.
[00:09:37] - Yeah.
[00:09:38] Perhaps the deepest lesson
[00:09:40] that I've learned in the last 10 years,
[00:09:42] and probably, you know,
[00:09:43] all of you have learned
[00:09:43] some form of it as well,
[00:09:45] is there can be this kind
[00:09:45] of seeming consensus,
[00:09:48] these things that kind of everyone knows,
[00:09:51] that, I don't know,
[00:09:52] seem sort of wise, seem
[00:09:52] like they're common sense,
[00:09:55] but really, they're just
[00:09:55] kind of herding behavior
[00:09:59] masquerading as maturity
[00:09:59] and sophistication.
[00:10:02] - Mm-hmm.
[00:10:02] - And when you've seen the
[00:10:02] consensus can change overnight-
[00:10:06] And when you've seen it
[00:10:06] happen a number of times,
[00:10:08] you suspected but you
[00:10:08] didn't really bet on it
[00:10:11] and you're like, "Oh man,
[00:10:11] I kind of thought this,
[00:10:13] but what do I know?"
[00:10:14] You know, "How how can I be right
[00:10:16] and all these people are wrong?"
[00:10:17] You see that a few times,
[00:10:17] then you just start saying,
[00:10:19] "Nope, this is the bet we're gonna make.
[00:10:21] I don't know for sure if we're right,
[00:10:22] but like, just ignore all this
[00:10:22] other stuff, see it happen,
[00:10:26] and, I don't know, even if
[00:10:26] you're right 50% of the time
[00:10:28] being right 50% of the time
[00:10:28] contributes so much," right?
[00:10:32] You're adding so much
[00:10:33] that is not being added by anyone else.
[00:10:35] - Yeah.
[00:10:36] - And it feels like
[00:10:36] that's where we are today
[00:10:37] with some safety stuff,
[00:10:39] where there's like a consensus view that
[00:10:40] a lot of this safety stuff is unusual
[00:10:42] or doesn't naturally fall
[00:10:42] out of the technology.
[00:10:45] And then at Anthropic, we
[00:10:45] do all of this research
[00:10:47] where weird safety misalignment problems
[00:10:49] fall out as a natural dividend
[00:10:49] of the tech we're building,
[00:10:53] so it feels like we're in that
[00:10:54] counter-consensus view right now.
[00:10:56] - But I feel like that has
[00:10:56] been shifting over the past,
[00:10:58] even just like 18-
[00:11:00] - We've been helping to shift-
[00:11:00] - We've definitely been helping.
[00:11:01] - No, I mean-
[00:11:01] - Yeah.
[00:11:02] - By publishing and doing research.
[00:11:03] - Constant publishing.
[00:11:03] - This constant force.
[00:11:04] Yeah.
[00:11:04] - But I also think, just,
[00:11:06] world sentiment around AI has
[00:11:06] shifted really dramatically,
[00:11:09] and, you know,
[00:11:10] it's more common in the
[00:11:10] user research that we do
[00:11:12] to hear just customers,
[00:11:12] regular people say,
[00:11:15] "I'm really worried about what
[00:11:15] the impact of AI on the world
[00:11:18] more broadly is going to be."
[00:11:19] And sometimes that means, you know,
[00:11:21] jobs or bias or toxicity, but
[00:11:21] it also sometimes means like,
[00:11:24] is this just gonna mess
[00:11:24] up the world, right?
[00:11:26] How is this gonna contribute
[00:11:26] to fundamentally changing
[00:11:29] how humans work together, operate?
[00:11:31] Which is, I wouldn't have
[00:11:31] predicted that actually,
[00:11:33] you know?
[00:11:33] - Oh yeah.
[00:11:34] But yeah, for whatever reason,
[00:11:35] it seems like people in
[00:11:35] the ML research sphere
[00:11:37] have always been more pessimistic about
[00:11:40] AI becoming very powerful-
[00:11:41] - Yeah.
[00:11:41] - Than the general public.
[00:11:43] - Maybe it's a weird-
[00:11:44] - General public's just like-
[00:11:44] - Humility or something, yeah.
[00:11:45] - When Dario and I went to
[00:11:45] the White House in 2023,
[00:11:48] in that meeting, like Harris
[00:11:48] and Raimondo and stuff
[00:11:50] basically said, I'll paraphrase,
[00:11:53] but basically said like,
[00:11:53] "We've got our eye on you guys.
[00:11:55] Like, AI's gonna be a really big deal
[00:11:57] and we're now actually paying attention,"
[00:11:58] which is-
[00:11:58] - And they're right.
[00:11:59] - They're right.
[00:12:01] - They're absolutely right.
[00:12:02] Absolutely right.
[00:12:02] - But I think in 2018
[00:12:03] you wouldn't have been like,
[00:12:04] "The President will call
[00:12:04] you to the White House
[00:12:06] to tell you
[00:12:07] they're paying close attention to
[00:12:08] the development of language models."
[00:12:10] - Yeah.
[00:12:11] - Which is like a crazy place-
[00:12:11] - That was not on the bingo card.
[00:12:13] - That was like 2018.
[00:12:15] - One thing that I think
[00:12:15] is interesting, too,
[00:12:17] just is, I guess, like all
[00:12:17] of us kind of got into this
[00:12:22] when it didn't seem like there was-
[00:12:24] - Mm-hmm.
[00:12:25] - Like we thought that it
[00:12:25] could happen, but yeah,
[00:12:27] it was like Fermi being
[00:12:27] skeptical of the atomic bomb.
[00:12:30] It was like he was just a good scientist
[00:12:33] and there was some evidence
[00:12:33] that it could happen,
[00:12:35] but there also was a lot of
[00:12:35] evidence against it happening.
[00:12:38] - Mm-hmm.
[00:12:39] - And he, I guess, decided
[00:12:39] that it would be worthwhile
[00:12:41] because if it was true,
[00:12:41] then it would be a big deal.
[00:12:44] And I think for all of
[00:12:44] us, it was like, yeah,
[00:12:45] like 2015, 2016, 2017,
[00:12:45] there was some evidence
[00:12:49] and increasing evidence that
[00:12:49] this might be a big deal,
[00:12:51] but I remember in 2016, like
[00:12:51] talking to all my advisors-
[00:12:55] - Yeah, yeah.
[00:12:55] - And I was like, "I've
[00:12:55] done startup stuff.
[00:12:57] I wanna help out with AI safety,
[00:12:59] but I'm not great at math.
[00:13:01] I don't exactly know
[00:13:03] how I can do it."
[00:13:04] And I think at the time
[00:13:04] people either were like,
[00:13:07] "Well, you need to be super
[00:13:07] good at decision theory
[00:13:09] in order to help out."
[00:13:10] And I was like, "Eh, that's
[00:13:10] probably not gonna work."
[00:13:12] Or they were like,
[00:13:14] "It doesn't really seem like
[00:13:14] we're gonna get some crazy AI thing,"
[00:13:17] and so I had only a few people, basically,
[00:13:20] that were like,
[00:13:21] "Yeah, okay, that seems
[00:13:21] like a good thing to do."
[00:13:24] - I remember in 2014
[00:13:25] making graphs of ImageNet
[00:13:25] results over time
[00:13:27] when I was a journalist
[00:13:28] and trying to get stories published about
[00:13:31] and people thought I was completely mad.
[00:13:32] And then I remember in 2015
[00:13:34] trying to persuade Bloomberg
[00:13:35] to let me write a story about NVIDIA,
[00:13:37] because every AI research
[00:13:37] paper had started mentioning
[00:13:40] the use of GPUs,
[00:13:41] and they said that was completely mad.
[00:13:43] And then in 2016 when I left
[00:13:43] journalism to go into AI,
[00:13:46] I have these emails saying,
[00:13:48] "You're making the worst
[00:13:48] mistake of your life,"
[00:13:51] which I now occasionally look back on,
[00:13:55] but it was like it all
[00:13:55] seemed crazy at the time,
[00:13:58] from many perspectives,
[00:13:59] to go and take this seriously,
[00:13:59] that scaling was gonna work,
[00:14:02] and something was maybe different about
[00:14:04] the technology paradigm.
[00:14:06] - You're like Michael
[00:14:06] Jordan and that coach
[00:14:07] that didn't believe in him in high school.
[00:14:09] - How did you actually
[00:14:09] make the decision, though?
[00:14:11] Was it did you feel torn
[00:14:11] or was it obvious to you?
[00:14:14] - I did a crazy counter-bet where I said,
[00:14:16] "Let me become your full-time AI reporter
[00:14:19] and double my salary,"
[00:14:20] which I knew that they
[00:14:20] wouldn't say yes to.
[00:14:22] And then I went to sleep and
[00:14:22] then I woke up and resigned.
[00:14:25] It was all fairly relaxed.
[00:14:27] - You're just a decisive guy.
[00:14:29] - In that instance, I was.
[00:14:31] I think it's because I
[00:14:31] was like going to work,
[00:14:33] reading archive papers,
[00:14:35] and then printing archive papers off
[00:14:36] and coming home and
[00:14:36] reading archive papers,
[00:14:39] including Dario's papers
[00:14:39] from the Baidu stuff
[00:14:42] and being like,
[00:14:43] "Something completely
[00:14:43] crazy is happening here."
[00:14:46] And at some point I thought
[00:14:46] you should bet with conviction,
[00:14:48] which I think everyone here
[00:14:48] has done in their careers,
[00:14:50] is just betting with conviction
[00:14:50] that this is gonna work.
[00:14:53] - Yeah.
[00:14:54] - I definitely was not as decisive of you.
[00:14:56] I spent, like, six months
[00:14:58] flip flopping, like,
[00:14:58] "Okay, should I, actually?
[00:15:01] Should I do it?
[00:15:01] Should I try to do a startup?
[00:15:02] Should I try to do this thing?"
[00:15:04] - But I also feel like back then,
[00:15:05] there wasn't as much talk of engineers
[00:15:08] and the impact that an engineer can have
[00:15:10] on AI, right?
[00:15:10] - Yeah, yeah, no way.
[00:15:10] - That feels so natural to us now.
[00:15:12] And we're at the same sort of talent raise
[00:15:14] for engineers of all different types,
[00:15:17] but at the time, it was
[00:15:17] like, you're a researcher,
[00:15:19] and that's the only people
[00:15:20] that can work on AI.
[00:15:20] - Yeah.
[00:15:21] - So I don't think it was crazy
[00:15:22] that you were spending
[00:15:22] time thinking about that.
[00:15:24] - Yeah.
[00:15:25] Yeah, and I think that that
[00:15:25] was basically the thing
[00:15:27] that got me to join OpenAI,
[00:15:28] was like I messaged the people
[00:15:28] there and they were like,
[00:15:31] "Yeah, we actually think
[00:15:31] that you can help out-"
[00:15:33] - Yeah.
[00:15:33] - "By doing engineering work."
[00:15:34] - Yeah.
[00:15:35] - "And that you can help out
[00:15:35] with AI safety in that way."
[00:15:37] - Mm-hmm.
[00:15:37] - Which I think
[00:15:38] there hadn't really been
[00:15:38] an opportunity for that,
[00:15:40] so that was what-
[00:15:41] - That's right.
[00:15:41] - Brought me there.
[00:15:42] - You were my manager at OpenAI.
[00:15:44] - I was, that's right.
[00:15:44] - I think I joined after
[00:15:44] you'd been there for a while.
[00:15:47] - A little bit.
[00:15:48] - 'Cause I was at Brain for a bit.
[00:15:49] - Yeah.
[00:15:50] - I don't know if I ever asked you
[00:15:50] what it was that got you to join?
[00:15:53] - Yeah, so I had been at Stripe
[00:15:55] for about five and a half years
[00:15:57] and I knew Greg; he had been my boss.
[00:15:59] He was my boss at Stripe for a while,
[00:16:01] and I actually introduced him and Dario,
[00:16:04] because I said, when
[00:16:04] he was starting OpenAI,
[00:16:06] I was like, "The smartest
[00:16:06] person that I know is Dario.
[00:16:10] You would be really lucky to get him."
[00:16:12] So Dario was at OpenAI,
[00:16:13] I had a few friends from Stripe
[00:16:13] that had gone there, too.
[00:16:16] And I think sort of like you,
[00:16:18] I'd been thinking about what
[00:16:18] I wanted to do after Stripe.
[00:16:22] I had gone there just 'cause
[00:16:22] I wanted to get more skills
[00:16:24] after working in, you know,
[00:16:26] nonprofit and international development,
[00:16:28] and I actually thought I was
[00:16:28] gonna go back to doing that.
[00:16:31] Like, essentially, I
[00:16:31] had always been working.
[00:16:33] I was like, "I really wanna
[00:16:33] help people that have, you know,
[00:16:36] less than I do,"
[00:16:37] but I didn't have the skills
[00:16:38] when I was doing it before Stripe.
[00:16:39] - Yep.
[00:16:40] - And so I looked at going
[00:16:40] back to public health.
[00:16:42] I thought about going back
[00:16:42] into politics very briefly,
[00:16:44] but I was also looking around
[00:16:44] at other tech companies
[00:16:47] and other sort of ways of having impact,
[00:16:50] and OpenAI, at the time,
[00:16:51] felt like it was a
[00:16:51] really nice intersection.
[00:16:52] It was a nonprofit,
[00:16:54] they were working on this
[00:16:54] really big, lofty mission.
[00:16:56] I really believed in sort of
[00:16:56] the AI, you know, potential,
[00:16:59] because, I mean, I know
[00:16:59] Dario a little bit,
[00:17:01] and so he was-
[00:17:02] - And they needed management help.
[00:17:04] - The definitely needed help.
[00:17:06] That is a fact.
[00:17:07] And so I think that it
[00:17:07] felt very me-shaped, right?
[00:17:10] I was like, "Oh, there's this nonprofit
[00:17:12] and there's all these really great people
[00:17:14] with these really good intentions,
[00:17:16] but it seems like they're
[00:17:16] a little bit of a mess."
[00:17:18] - Yeah.
[00:17:19] And that felt really exciting to me,
[00:17:21] to get to come in and even, you know,
[00:17:23] just I was such a utility player, right?
[00:17:25] I was running people,
[00:17:27] but I was also running some
[00:17:27] of the technical teams-
[00:17:29] - Scaling orgs, yep.
[00:17:29] - Yeah, the scaling org,
[00:17:30] I worked on the language team,
[00:17:31] I took over-
[00:17:32] - You worked on policy-
[00:17:33] - I worked on some policy stuff,
[00:17:34] I worked with Chris,
[00:17:35] and I felt like there
[00:17:35] was just so much goodness
[00:17:38] in so many of the employees there,
[00:17:40] and I felt a very strong desire to come
[00:17:42] and sort of just try to
[00:17:42] help make the company
[00:17:44] a little more functional.
[00:17:46] - I remember towards the
[00:17:46] end, after we'd done GPT-3,
[00:17:49] you were like,
[00:17:50] "Have you guys heard of something
[00:17:50] called trust and safety?"
[00:17:51] - Yes, I remember that!
[00:17:55] That did happen.
[00:17:55] - Yeah.
[00:17:57] - I said, you know,
[00:17:58] "I used to run some trust
[00:17:58] and safety teams at Stripe.
[00:18:00] There's a thing called trust and safety
[00:18:02] that you might wanna consider
[00:18:02] for a technology like this."
[00:18:05] And it's funny because it's
[00:18:05] sort of is the intermediary step
[00:18:08] between, you know, AI
[00:18:08] safety research, right,
[00:18:11] which is how do you
[00:18:11] actually make the model safe
[00:18:13] to something just much more practical.
[00:18:15] I do think there was a
[00:18:15] value in saying, you know,
[00:18:18] this is gonna be a big thing;
[00:18:19] we also have to be doing
[00:18:19] this sort of practical work
[00:18:21] day to day to build the muscles
[00:18:23] for when things are gonna
[00:18:23] be a lot higher stakes.
[00:18:26] - That might be a good transition point
[00:18:28] to talk about things like the
[00:18:28] responsible scaling policy
[00:18:31] and how we came up with that,
[00:18:33] or why we came up with it
[00:18:33] and how we're using it now,
[00:18:35] especially given how much
[00:18:35] trust and safety work
[00:18:37] we do on today's models.
[00:18:39] So whose idea was the RSP?
[00:18:41] Was you and Paul?
[00:18:41] - So, yeah,
[00:18:43] it was me and Paul first
[00:18:43] talked about it in late,
[00:18:47] Paul Christiano, in late 2022.
[00:18:49] - Mm-hmm.
[00:18:50] - First it was like, oh,
[00:18:50] should we cap scaling at a,
[00:18:52] you know, particular point
[00:18:54] until we've discovered how to
[00:18:54] solve certain safety problems?
[00:18:57] And then it was like, well, you know,
[00:18:59] it's kind of strange
[00:18:59] to have this one place
[00:19:01] where you cap it and then you uncap it,
[00:19:02] so let's have a bunch of thresholds,
[00:19:05] and then at each threshold
[00:19:05] you have to do certain tests
[00:19:07] to see if the model is capable
[00:19:09] and you have to take
[00:19:10] increasing safety and security measures.
[00:19:12] But originally we had this idea,
[00:19:14] and then the thought
[00:19:14] was just look, you know,
[00:19:17] this'll go better if it's
[00:19:17] done by some third party.
[00:19:20] Like, we shouldn't be
[00:19:20] the ones to do it, right?
[00:19:23] It shouldn't come from one company,
[00:19:24] 'cause then other companies
[00:19:24] are less likely to adopt it.
[00:19:26] So Paul actually went off and designed it,
[00:19:28] and, you know, many, many
[00:19:28] features of it changed
[00:19:31] and we were kind of, on our side,
[00:19:33] working on how it should work.
[00:19:36] And, you know, once Paul
[00:19:36] had something together,
[00:19:39] then pretty much immediately
[00:19:39] after he announced the concept,
[00:19:42] we announced ours within a month or two.
[00:19:44] I mean, many of us were
[00:19:44] heavily involved in it.
[00:19:46] I remember writing at least
[00:19:46] one draft of it myself,
[00:19:49] but there were several drafts of it.
[00:19:50] - There were so many drafts.
[00:19:54] - I think it's gone through
[00:19:54] the most drafts of any doc.
[00:19:56] - Yeah.
[00:19:56] - Which makes sense, right?
[00:19:57] It's like, I feel like it is
[00:19:59] in the same way that the US
[00:19:59] treats like the Constitution,
[00:20:03] as like the holy document.
[00:20:04] - Yeah.
[00:20:04] - Which like,
[00:20:05] I think is just a big thing
[00:20:05] that like strengthens the US.
[00:20:07] - Yes.
[00:20:08] - And like we don't expect
[00:20:08] the US to go off the rails,
[00:20:10] in part, because just like
[00:20:10] every single person in the US
[00:20:12] is like, "The Constitution is a big deal,
[00:20:14] and if you tread on that-"
[00:20:14] - Yeah.
[00:20:15] - "Like, I'm mad."
[00:20:16] - Yeah, yeah.
[00:20:17] - Like I think that the RSP is our,
[00:20:19] like, it holds that thing.
[00:20:21] It's like the holy document for Anthropic.
[00:20:22] So it's worth doing a lot of
[00:20:22] iterations getting it right.
[00:20:26] - Some of what I think
[00:20:26] has been so cool to watch
[00:20:27] about the RSP development
[00:20:27] at Anthropic, too,
[00:20:31] is it feels like it has gone through
[00:20:32] so many different phases
[00:20:33] and there's so many different skills
[00:20:34] that are needed to make it work, right?
[00:20:36] There's like the big ideas,
[00:20:37] which I feel like Dario
[00:20:37] and Paul and Sam and Jared
[00:20:40] and so many others are like,
[00:20:40] "What are the principles?
[00:20:43] Like what are we trying to say?
[00:20:45] How do we know if we're right?"
[00:20:46] But there's also this
[00:20:46] very operational approach
[00:20:49] to just iterating
[00:20:50] where we're like, "Well, we thought that
[00:20:51] we were gonna see this at
[00:20:51] this, you know, safety level,
[00:20:54] and we didn't,
[00:20:55] so should we change it so
[00:20:55] that we're making sure that
[00:20:57] we're holding ourselves accountable?"
[00:20:58] And then there's all kinds of
[00:20:58] organizational things, right?
[00:21:01] We just were like,
[00:21:01] "Let's change the structure
[00:21:01] of the RSP organization
[00:21:03] for clearer accountability."
[00:21:05] And I think my sense
[00:21:05] is that for a document
[00:21:08] that's as important as this, right,
[00:21:09] I love the Constitution analogy,
[00:21:11] it's like there's all of
[00:21:11] these bodies and systems
[00:21:13] that exist in the US
[00:21:15] to make sure that we follow
[00:21:15] the Constitution, right?
[00:21:17] There's the courts,
[00:21:17] there's the Supreme Court,
[00:21:18] there's the presidency,
[00:21:20] there's, you know, both houses of Congress
[00:21:23] and they do all kinds of
[00:21:23] other things, of course,
[00:21:26] but there's like all of this
[00:21:26] infrastructure that you need
[00:21:28] around this one document,
[00:21:29] and I feel like we're also
[00:21:29] learning that lesson here.
[00:21:31] - I think it sort of reflects a view
[00:21:33] a lot of us have about safety,
[00:21:34] which is that it's a solvable problem.
[00:21:37] - Mm-hmm.
[00:21:37] - It's just a very, very hard problem
[00:21:39] that's gonna take tons and tons of work.
[00:21:40] - Mm-hmm.
[00:21:40] - Yeah.
[00:21:41] - All of these institutions
[00:21:41] that we need to build up,
[00:21:43] like there's all sorts of
[00:21:43] institutions built up around
[00:21:46] like automotive safety, built
[00:21:46] up over many, many years.
[00:21:49] But we're like, "Do we
[00:21:49] have the time to do that?
[00:21:51] We've gotta go as fast
[00:21:51] as we can to figure out
[00:21:54] what the institutions we
[00:21:54] need for AI safety are,
[00:21:56] and build those and try
[00:21:56] to build them here first,
[00:21:58] but make it exportable."
[00:22:00] - That's right.
[00:22:00] - It it forces unity also,
[00:22:01] because if any part of the org
[00:22:04] is not kind of in line
[00:22:04] with our safety values,
[00:22:08] it shows up through
[00:22:08] kind of the RSP, right?
[00:22:10] The RSP is gonna block them
[00:22:10] from doing what they want to do,
[00:22:13] and so it's a way to remind
[00:22:13] everyone over and over again,
[00:22:16] basically, to make safety
[00:22:16] a product requirement,
[00:22:20] part of the product planning process.
[00:22:22] And so, like, it's not just
[00:22:22] a bunch of kind of like
[00:22:24] bromides that we repeat;
[00:22:26] it's something that you actually,
[00:22:27] if you show up here
[00:22:27] and you're not aligned,
[00:22:30] you actually run into it.
[00:22:31] - Yeah.
[00:22:32] - And you either have to
[00:22:32] learn to get with the program
[00:22:34] or it doesn't work out.
[00:22:34] - Yeah.
[00:22:37] - The RSPs become kind of funny over time
[00:22:39] because we spend thousands
[00:22:39] of hours of work on it,
[00:22:42] and then I go and talk to
[00:22:42] senators and I explain the RSP,
[00:22:44] and I'm like, "We have some stuff
[00:22:46] that means it's hard
[00:22:46] to steal what we make,
[00:22:49] and also that it's safe."
[00:22:50] And they're like,
[00:22:51] "Yes, that's a completely
[00:22:51] normal thing to do.
[00:22:55] Are you telling me not
[00:22:55] everyone does this?"
[00:22:57] You're like, "Oh, okay, yeah."
[00:22:58] Yeah.
[00:23:01] - It's half true that that
[00:23:01] not everyone does this.
[00:23:03] - Yeah.
[00:23:03] - But that kind of,
[00:23:04] it's amazing because we've
[00:23:04] spent so much effort on it here
[00:23:07] and when you boil it down, they're like,
[00:23:08] "Yes, that sounds like a normal way
[00:23:10] to do that."
[00:23:10] - Yeah, that sounds good.
[00:23:12] - That's been the goal.
[00:23:13] Like Daniela was saying,
[00:23:14] "Let's make this as boring and normal.
[00:23:16] Like let's make this a finance thing."
[00:23:17] - Yeah, imagine it's like an audit.
[00:23:19] - Yeah, yeah.
[00:23:19] - Right?
[00:23:20] Yeah.
[00:23:20] - No, boring and normal
[00:23:22] is what we want,
[00:23:23] certainly in retrospect.
[00:23:23] - Yeah.
[00:23:25] Well also, Dario,
[00:23:26] I think in addition to driving alignment,
[00:23:27] it also drives clarity-
[00:23:27] - Mm-hmm.
[00:23:29] - Because it's written down
[00:23:29] what we're trying to do
[00:23:32] and it's legible to
[00:23:32] everyone in the company,
[00:23:34] and it's legible externally
[00:23:36] what we think we're supposed
[00:23:36] to be aiming towards
[00:23:38] from a safety perspective.
[00:23:39] It's not perfect.
[00:23:40] We're iterating on it,
[00:23:40] we're making it better,
[00:23:42] but I think there's some
[00:23:42] value in saying like,
[00:23:44] "This is what we're worried
[00:23:44] about, this thing over here."
[00:23:46] Like you can't just use
[00:23:46] this word to sort of
[00:23:49] derail something in
[00:23:49] either direction, right?
[00:23:51] To say, "Oh, because of
[00:23:51] safety, we can't do X,
[00:23:53] or because of safety, we have to do X."
[00:23:55] We're really trying to make
[00:23:55] it clearer what we mean.
[00:23:57] - Yeah, it prevents
[00:23:57] you from worrying about
[00:24:00] every last little thing under the sun.
[00:24:02] - That's right.
[00:24:03] - Because it's actually the fire drills
[00:24:05] that damage the cause of
[00:24:05] safety in the long run.
[00:24:07] - Right.
[00:24:08] - I've said like, "If there's a building,
[00:24:08] and, you know, the fire
[00:24:08] alarm goes off every week,
[00:24:12] like, that's a really unsafe building."
[00:24:13] - Mm-hmm.
[00:24:14] - 'Cause when there's
[00:24:14] like actually a fire,
[00:24:15] you're just gonna be like-
[00:24:15] - No ones gonna care.
[00:24:16] - "Oh, it just goes off all the time."
[00:24:17] So-
[00:24:17] - Yeah.
[00:24:18] - It's very important to be calibrated.
[00:24:20] - Yeah.
[00:24:20] - That's right.
[00:24:21] - Yeah.
[00:24:22] A slightly different frame
[00:24:22] that I find kind of clarifying
[00:24:24] is that I think that RSP
[00:24:24] creates healthy incentives
[00:24:27] at a lot of levels.
[00:24:27] - Mm.
[00:24:28] - So I think internally it aligns
[00:24:30] the incentives of every team with safety
[00:24:32] because it means that if we
[00:24:32] don't make progress on safety,
[00:24:34] we're gonna block.
[00:24:36] I also think that externally
[00:24:38] it creates a lot of healthier incentives
[00:24:40] than other possibilities,
[00:24:40] at least that I see,
[00:24:42] because it means that, you
[00:24:42] know, if we at some point
[00:24:44] have to take some kind of dramatic action,
[00:24:45] like, if at some point we have to say,
[00:24:46] "You know, our model,
[00:24:46] we've reached some point
[00:24:48] and we can't yet make a model safe,"
[00:24:50] it aligns that with
[00:24:50] sort of the point where
[00:24:52] there's evidence that
[00:24:52] supports that decision
[00:24:54] and there's sort of a
[00:24:54] preexisting framework
[00:24:57] for thinking about it, and it's legible.
[00:24:58] And so I think there's a lot
[00:24:58] of levels at which the RSP,
[00:25:01] I think in ways that maybe I
[00:25:01] didn't initially understand
[00:25:04] when we were talking about
[00:25:04] the early versions of it,
[00:25:07] it creates a better framework
[00:25:08] than any of the other ones
[00:25:08] that I've thought about.
[00:25:11] - I think this is all true,
[00:25:12] but I feel like it undersells sort of like
[00:25:15] how challenging it's been
[00:25:15] to sort of figure out
[00:25:18] what the right policies and evaluations
[00:25:21] and what the lines should be.
[00:25:24] I think that we have and continue to
[00:25:26] sort of iterate a lot on that,
[00:25:27] and I think there is a
[00:25:27] question also that's difficult
[00:25:30] of sort of you could be at a point where
[00:25:32] it's very clear something's dangerous
[00:25:34] or very clear that something's safe,
[00:25:35] but with some technology that's so new,
[00:25:37] there's actually like a big gray area.
[00:25:39] And so I think that has been, like,
[00:25:41] all the things that we're saying
[00:25:43] were things that made me
[00:25:45] really, really excited about
[00:25:45] the RSP at the beginning,
[00:25:47] and still do,
[00:25:48] but also I think enacting this
[00:25:51] in a clear way and making it work
[00:25:54] has been much harder and more complicated
[00:25:56] than I anticipated.
[00:25:58] - Yeah, I think this is exactly the point.
[00:25:59] Like-
[00:25:59] - Yeah.
[00:26:00] - Like the gray areas are
[00:26:00] impossible to predict.
[00:26:02] There's so many of them.
[00:26:03] Like, until you actually
[00:26:03] try to implement everything,
[00:26:05] you don't know what's going to go wrong.
[00:26:07] So what we're trying to do is
[00:26:07] go and implement everything
[00:26:09] so we can see as early as
[00:26:09] possible what's going to go wrong,
[00:26:12] so-
[00:26:12] - Yeah, you have to-
[00:26:13] - The gray areas are-
[00:26:14] - You have to do three
[00:26:14] or four passes before-
[00:26:15] - Yeah.
[00:26:16] - Before you really, really get it right.
[00:26:17] Like, iteration is just
[00:26:17] very powerful and, you know,
[00:26:20] you're not gonna get it
[00:26:20] right on the first time.
[00:26:23] And so, you know, if the
[00:26:23] stakes are increasing,
[00:26:25] you want to get your iterations in early;
[00:26:27] you don't want to get them in late.
[00:26:28] - You're also building
[00:26:29] the internal institutions and processes,
[00:26:32] so the specifics might change a lot,
[00:26:34] but building the muscle of just doing it
[00:26:36] is the really valuable thing.
[00:26:37] - I'm responsible for, like,
[00:26:37] compute at Anthropic, and so-
[00:26:41] - That's important.
[00:26:42] - So, thank you.
[00:26:43] I think so.
[00:26:44] So like for me,
[00:26:48] like I guess we have to
[00:26:48] deal with external folks-
[00:26:51] - Yeah.
[00:26:51] - And different external folks
[00:26:53] kind of are on different
[00:26:53] spectrums of the, like,
[00:26:55] how fast do they think stuff is gonna get?
[00:26:56] - Mm-hmm.
[00:26:56] - And like,
[00:26:57] I think that's also been a thing,
[00:26:58] where I started out
[00:26:58] like not thinking stuff
[00:27:00] would be that fast and
[00:27:00] have changed over time.
[00:27:02] And so, I have sympathy for that.
[00:27:04] And so I think the RSP has
[00:27:04] been extremely useful for me
[00:27:07] in communicating with people
[00:27:08] who think that things might take longer
[00:27:10] because then we have a
[00:27:10] thing where it's like,
[00:27:12] we don't need to do
[00:27:12] extreme safety measures
[00:27:15] until stuff gets really intense,
[00:27:18] and then they might be like,
[00:27:21] "I don't think stuff will
[00:27:21] get intense for a long time."
[00:27:22] And then I'll be like,
[00:27:23] "Okay, yeah, we don't have to
[00:27:23] do extreme safety measures."
[00:27:25] And so that makes it a lot easier
[00:27:27] to communicate with
[00:27:27] other folks externally.
[00:27:29] - Yeah, yeah, it makes it like
[00:27:30] a normal thing you can talk about,
[00:27:33] rather than something really strange.
[00:27:34] - Yeah.
[00:27:35] How else is it showing up for people?
[00:27:37] You are-
[00:27:38] - Evals, evals, evals.
[00:27:40] - Good.
[00:27:41] - It's all about evals.
[00:27:42] Everyone's doing evals.
[00:27:43] Like, your training team is
[00:27:43] doing evals all the time.
[00:27:45] We're trying to figure out, like,
[00:27:47] has this model gotten enough better
[00:27:48] that it has the potential to be dangerous?
[00:27:51] So how many teams do we
[00:27:51] have that are evals teams?
[00:27:54] You have Frontier Red Team.
[00:27:56] There must be, I mean
[00:27:56] there's a lot of people-
[00:27:58] - Every team produces evals, basically.
[00:28:00] - And that means you're just
[00:28:00] measuring against the RSP,
[00:28:03] like measuring for certain signs of
[00:28:05] things that would concern
[00:28:05] you or not concern you.
[00:28:07] - Exactly.
[00:28:08] Like it's easy to lower bound
[00:28:08] the abilities of a model,
[00:28:14] but it's hard to upper bound,
[00:28:15] so we just put tons and
[00:28:15] tons of research effort
[00:28:17] into saying, like,
[00:28:19] "Can this model do this
[00:28:19] dangerous thing or not?
[00:28:21] Maybe there's some trick
[00:28:21] that we haven't thought of,
[00:28:23] like chain of thought or best event
[00:28:25] or some kind of tool
[00:28:25] use that's gonna make it
[00:28:27] so it can help you do
[00:28:27] something very dangerous."
[00:28:30] - It's been really useful in policy,
[00:28:31] because it's been a
[00:28:31] really abstract concept,
[00:28:34] what safety is,
[00:28:35] and when I'm like, "We have an eval
[00:28:37] which changes whether we
[00:28:37] deploy the model or not,"
[00:28:39] and then you can go and calibrate with
[00:28:40] policymakers or experts
[00:28:40] in national security
[00:28:43] or some of these CBRN areas that we do,
[00:28:45] to actually help us build
[00:28:45] evals that are well-calibrated
[00:28:48] and that, counter-factually,
[00:28:50] just wouldn't have happened otherwise,
[00:28:52] but once you've got the specific thing,
[00:28:54] people are a lot more motivated
[00:28:55] to help you make it accurate,
[00:28:56] so it's been useful for that.
[00:28:58] How has it shown up for-
[00:28:58] - The RSP shows up for me,
[00:28:59] for sure.
[00:29:01] Often.
[00:29:03] I actually think, weirdly,
[00:29:04] the way that I think about
[00:29:04] the RSP the most is like
[00:29:08] what it sounds like-
[00:29:09] - Mm-hmm?
[00:29:10] - Just like the tone.
[00:29:10] I think we just did a big
[00:29:10] rewrite of the tone of the RSP
[00:29:13] because it felt overly technocratic,
[00:29:15] and even a little bit adversarial.
[00:29:17] I spent a lot of time thinking about like,
[00:29:18] how do you build a system
[00:29:19] that people just wanna be a part of?
[00:29:21] - Mm-hmm.
[00:29:21] - Right?
[00:29:21] It's so much better if
[00:29:21] the RSP is something
[00:29:23] that everyone in the company
[00:29:23] can walk around and tell you,
[00:29:26] you know, just like with OKRs
[00:29:28] like we do right now-
[00:29:28] - Yeah.
[00:29:29] - Like, what are the top goals of the RSP?
[00:29:32] How do we know if we're meeting them?
[00:29:32] What AI safety level are we at right now?
[00:29:35] Are we at ASL-2?
[00:29:35] Are we at ASL-3?
[00:29:37] That people know what to look for
[00:29:38] because that is how you're going to have
[00:29:40] good, common knowledge of
[00:29:40] if something's going wrong,
[00:29:42] right?
[00:29:43] If it's overly technocratic,
[00:29:44] and it's something that
[00:29:45] only particular people in the company
[00:29:47] feel is accessible to them,
[00:29:48] it's just like not as productive, right?
[00:29:50] And I think it's been really cool
[00:29:52] to watch it sort of
[00:29:52] transition into this document
[00:29:54] where I actually think most,
[00:29:56] if not everybody at the company,
[00:29:56] regardless of their role,
[00:29:58] could read it and say, "This
[00:29:58] feels really reasonable.
[00:30:00] I wanna make sure that we're building AI
[00:30:03] in the following ways,
[00:30:04] and I see why I would be
[00:30:04] worried about these things,
[00:30:07] and I also kind of know what to look for
[00:30:08] if I bump into something," right?
[00:30:10] It's almost like make it simple enough
[00:30:11] that if you are working
[00:30:11] at a manufacturing plant
[00:30:15] and you're like,
[00:30:15] "Huh, it looks like the
[00:30:15] safety seatbelt on this
[00:30:17] should connect this way,
[00:30:17] but it doesn't connect,"
[00:30:19] that you can spot it.
[00:30:20] - Mm-hmm.
[00:30:21] - And that there's just
[00:30:21] like healthy feedback flow
[00:30:23] between leadership and the board
[00:30:25] and the rest of the company
[00:30:26] and the people that are
[00:30:26] actually building it,
[00:30:28] because I actually think the
[00:30:28] way this stuff goes wrong
[00:30:30] in most cases is just, like,
[00:30:30] the wires don't connect
[00:30:34] or like they get crossed,
[00:30:35] and that would just be like
[00:30:37] a really sad way for
[00:30:37] things to go wrong, right?
[00:30:39] It's just all about operationalizing it,
[00:30:41] making it easy for people to understand.
[00:30:42] - Yeah, the thing I would say is
[00:30:43] none of us wanted to found a company.
[00:30:45] We just felt like it was our duty, right?
[00:30:49] - It felt like we had to.
[00:30:51] - Like, we have to do this thing.
[00:30:52] This is the way we're gonna
[00:30:52] make things go better with AI.
[00:30:55] Like that's also why we
[00:30:55] did the pledge, right?
[00:30:57] - Yeah.
[00:30:57] - Because we're like
[00:30:59] the reason we're doing this
[00:30:59] is it feels like our duty.
[00:31:01] - I wanted to invent and discover things
[00:31:05] in some kind of beneficial way.
[00:31:06] That was how I came to it,
[00:31:06] and that led to working on AI,
[00:31:10] and AI required a lot of engineering
[00:31:12] and eventually AI
[00:31:12] required a lot of capital,
[00:31:15] but what I found was that
[00:31:19] if you don't do this in a way where
[00:31:22] you're setting the environment,
[00:31:23] where you set up the company,
[00:31:26] then a lot of it gets done,
[00:31:27] a lot of it repeats the same mistakes
[00:31:30] that I found so alienating
[00:31:30] about the tech community.
[00:31:35] It's the same people,
[00:31:36] it's the same attitude,
[00:31:38] it's the same pattern-matching,
[00:31:39] And so at some point it
[00:31:39] just seemed inevitable
[00:31:42] that we need to do it in a different way.
[00:31:44] - When we were hanging
[00:31:44] out in graduate school,
[00:31:45] I remember you had kind
[00:31:45] of this whole program
[00:31:48] of trying to figure out how to do science
[00:31:50] in a way that would sort
[00:31:50] of advance the public good.
[00:31:52] And I think that's pretty similar to
[00:31:54] how we we think about this.
[00:31:57] I think you had this like
[00:31:57] Project Vannevar or something,
[00:31:59] to do that.
[00:32:01] I was a professor.
[00:32:02] I think basically I just
[00:32:02] looked at the situation
[00:32:04] and I was convinced that AI
[00:32:06] was on a very, very, very steep trajectory
[00:32:09] in terms of impact,
[00:32:10] didn't seem like because of
[00:32:10] the necessity for capital,
[00:32:14] and as a physics professor,
[00:32:14] I could continue doing that
[00:32:16] and I kind of wanted to work
[00:32:16] with people that I trusted
[00:32:20] in building an institution
[00:32:20] to try to make AI go well.
[00:32:24] But yeah, I would never
[00:32:24] recommend founding a company.
[00:32:29] Or really want to do it.
[00:32:30] I mean, yeah, I think it's
[00:32:30] just a means to an end.
[00:32:32] I mean,
[00:32:33] I think that's like usually
[00:32:33] how things go well, though.
[00:32:35] If you're doing something
[00:32:35] just to sort of like
[00:32:37] enrich yourself or gain power or, like,
[00:32:39] you have to sort of actually care about
[00:32:41] accomplishing a real goal in the world
[00:32:43] and then you find whatever
[00:32:43] means you have to.
[00:32:46] - Well, something I think about a lot
[00:32:47] as just a strategic advantage for us is,
[00:32:50] I mean, it sounds really funny to say,
[00:32:52] but just like how much trust
[00:32:52] there is at this table,
[00:32:55] right?
[00:32:55] - Mm-hmm.
[00:32:56] - Like I think that's not, I mean,
[00:32:57] Tom, you were at other startups.
[00:32:58] I was never a founder before,
[00:33:00] but it's actually really
[00:33:00] hard to get a group of,
[00:33:02] like, a big group of people,
[00:33:02] to have like the same mission.
[00:33:07] Right?
[00:33:08] And I think the thing that I
[00:33:08] feel like the happiest about
[00:33:10] when I come into work,
[00:33:11] and probably the most
[00:33:11] proud of at Anthropic,
[00:33:13] is how well that has
[00:33:13] scaled to a lot of people.
[00:33:16] It feels to me like in this group
[00:33:18] and with the rest of leadership,
[00:33:19] everyone is here for the mission,
[00:33:21] and our mission is really clear-
[00:33:22] - Yep.
[00:33:22] - And it's very pure, right?
[00:33:25] And I think that is something
[00:33:25] that I don't see as often,
[00:33:27] to Dario's point, in sort
[00:33:27] of the tech industry.
[00:33:29] It feels like there's just a wholesomeness
[00:33:32] to what we're trying to do.
[00:33:33] Like, no, I agree, none of us were like,
[00:33:35] "Let's just go found a company!"
[00:33:37] I felt like we had to do it, right?
[00:33:39] It just felt like
[00:33:40] we couldn't keep doing what we were doing
[00:33:41] at the place we were doing it.
[00:33:42] We had to do it by ourselves.
[00:33:44] - And it felt like with GPT-3,
[00:33:46] you know, which all of us had
[00:33:46] like touched or worked on,
[00:33:48] and scaling laws and everything else,
[00:33:50] we could see it in front of us in 2020.
[00:33:53] And it felt like, well,
[00:33:54] if we don't do something
[00:33:54] soon, all together,
[00:33:56] you're gonna hit the point of no return.
[00:33:58] And you have to do something
[00:34:00] to have any ability to
[00:34:00] change the environment.
[00:34:02] - Mm-hmm.
[00:34:03] - I think, building off Daniela,
[00:34:05] I do think that there's
[00:34:05] just like a lot of trust-
[00:34:07] - Mm-hmm.
[00:34:07] - In this group.
[00:34:08] I think each of us knows
[00:34:08] that we got into this
[00:34:11] because we wanna help out with the world.
[00:34:13] - Yeah.
[00:34:14] - We did the the 80% pledge thing,
[00:34:17] and that was like a thing
[00:34:17] that everybody was just like,
[00:34:20] "Yes, obviously we're gonna do this."
[00:34:21] - Mm-hmm.
[00:34:21] - Yeah, yeah.
[00:34:22] - And yeah, I do think
[00:34:22] that the trust thing
[00:34:26] is a special thing that's extremely rare.
[00:34:29] - Yeah.
[00:34:29] - I credit Daniela with
[00:34:29] keeping the bar high.
[00:34:33] I credit you with the fact-
[00:34:34] - Keeping out the clowns.
[00:34:37] - Chief clown wrangler!
[00:34:39] That's my job.
[00:34:40] - No, but you're the reason
[00:34:40] the culture scaled, I think.
[00:34:41] - Yeah.
[00:34:42] People say how nice people are here.
[00:34:43] - Yeah.
[00:34:44] - Which is actually a
[00:34:44] wildly important thing.
[00:34:47] - I think Anthropic is
[00:34:47] really low politics,
[00:34:49] and of course,
[00:34:50] we all have a different
[00:34:50] vantage point than average,
[00:34:52] and I try to remember that.
[00:34:52] - It's because of low ego.
[00:34:54] - But it's low ego,
[00:34:55] and I think I do think
[00:34:55] our interview process
[00:34:57] and just the type of people who work here,
[00:34:59] like, there's almost a like
[00:34:59] allergic reaction to politics.
[00:35:03] - And unity.
[00:35:04] - Mm-hmm.
[00:35:04] - Unity is so important.
[00:35:06] The idea that the product
[00:35:06] team, the research team-
[00:35:09] - Yes.
[00:35:10] - The trust and safety team,
[00:35:12] you know, the go-to market
[00:35:12] team, the policy team-
[00:35:14] - Yeah.
[00:35:15] - Like, the safety folks,
[00:35:18] they're all trying to contribute
[00:35:18] to kind of the same goal,
[00:35:22] the same mission of the company,
[00:35:23] right?
[00:35:23] - Yes.
[00:35:24] - I think it's dysfunctional when
[00:35:26] different parts of the company
[00:35:28] think they're trying to
[00:35:28] accomplish different things-
[00:35:30] - Yeah.
[00:35:31] - Think the company's
[00:35:31] about different things
[00:35:32] or think that other parts of the company
[00:35:34] are trying to undermine
[00:35:34] what they're doing.
[00:35:36] - Yeah.
[00:35:37] - And I think the most important thing
[00:35:38] we've managed to preserve is,
[00:35:40] and again, things like the RSP drive it,
[00:35:42] this idea that it's not, you know,
[00:35:45] there's some parts of the
[00:35:45] company causing damage
[00:35:47] and other parts of the
[00:35:47] company trying to repair it,
[00:35:50] but that there are different
[00:35:50] parts of the company
[00:35:52] doing different functions
[00:35:54] and that they all function
[00:35:54] under a single theory of change.
[00:35:57] - Extreme pragmatism, right?
[00:35:58] - Yeah.
[00:35:59] - You know, the reason I went
[00:35:59] to OpenAI in the first place,
[00:36:02] you know, it was a nonprofit,
[00:36:03] it was a place where I could
[00:36:03] go and focus on safety,
[00:36:06] and I think over time, you know,
[00:36:08] that maybe wasn't as good a fit
[00:36:10] and there were some difficult decisions.
[00:36:12] And I think, in a lot of ways,
[00:36:13] I really trusted Dario
[00:36:13] and Daniela on that,
[00:36:16] but I didn't want to leave.
[00:36:18] That was something that
[00:36:18] I think I was actually
[00:36:21] pretty reluctant to go along with,
[00:36:24] because I think, for one thing,
[00:36:25] I didn't know that it
[00:36:25] was good for the world
[00:36:27] to have more AI labs.
[00:36:29] And I think it was something that
[00:36:30] I was pretty, pretty reluctant for.
[00:36:32] And I think, as well, when we did leave,
[00:36:34] I think I was, you know, I was
[00:36:34] reluctant to start a company.
[00:36:38] I think I was arguing for a long time
[00:36:40] that we should do a nonprofit instead,
[00:36:41] and just focus on safety research.
[00:36:42] - Yes.
[00:36:43] - And I think it really took pragmatism
[00:36:46] and confronting the constraints
[00:36:49] and just being honest about
[00:36:49] what the constraints implied
[00:36:52] for accomplishing that mission-
[00:36:53] - Mm-hmm.
[00:36:54] - That led to Anthropic.
[00:36:55] - I think just a really important lesson
[00:36:57] that we were good about early on
[00:36:59] is make less promises
[00:36:59] and keep more of them.
[00:37:02] - Yeah.
[00:37:02] - Right?
[00:37:03] - Yeah.
[00:37:03] - Like, try to be
[00:37:03] calibrated, be realistic,
[00:37:08] confront the trade-offs,
[00:37:08] because, you know,
[00:37:11] trust and credibility
[00:37:12] are more important than
[00:37:12] any particular policy.
[00:37:14] - Yeah.
[00:37:15] - It is so unusual to have what we have,
[00:37:19] and watching Mike Krieger
[00:37:19] defend safety things,
[00:37:23] of like reasons why we
[00:37:23] shouldn't ship a product yet,
[00:37:25] but also then to watch
[00:37:25] Vinay sort of say like,
[00:37:28] "Okay, we have to do the
[00:37:28] right thing for the business.
[00:37:31] Like how do we get this
[00:37:31] across the finish line?"
[00:37:32] - Mm-hmm, yep.
[00:37:33] - And to hear, you know,
[00:37:34] people like deep in the
[00:37:34] technical safety org
[00:37:36] talking about how it's also
[00:37:36] important that we build things
[00:37:39] that are practical for people,
[00:37:41] and hearing, you know,
[00:37:42] engineers on inference talk about safety.
[00:37:43] That's amazing.
[00:37:44] Like, I think that is, again,
[00:37:47] one of the most special
[00:37:47] things about working here,
[00:37:48] is everybody with that unity
[00:37:48] is prioritizing the pragmatism,
[00:37:52] the safety, the business.
[00:37:54] That's wild.
[00:37:55] - The safest move-
[00:37:55] - I think about it as-
[00:37:56] - Yeah.
[00:37:57] - Spreading the trade-offs-
[00:37:57] - Yeah.
[00:37:59] - From just the leadership
[00:37:59] of the company to everyone,
[00:38:04] right?
[00:38:04] - Yeah.
[00:38:04] - I think the dysfunctional world is like,
[00:38:06] you have a bunch of people
[00:38:06] who only see a big, you know,
[00:38:10] safety is like, "We
[00:38:10] always have to do this,"
[00:38:11] and product is like, "We
[00:38:11] always have to do this,"
[00:38:13] and research is like, you know,
[00:38:15] "This is the only thing we care about."
[00:38:17] And then you're stuck at the top,
[00:38:19] right?
[00:38:19] - Yeah.
[00:38:20] - You're stuck at the top.
[00:38:20] You have to decide between
[00:38:21] you don't have as much
[00:38:21] information as either of them.
[00:38:24] That's the dysfunctional world.
[00:38:25] The functional world is when
[00:38:26] you're able to communicate to everyone,
[00:38:29] "There are these trade-offs
[00:38:29] we're all facing together."
[00:38:31] - Yeah.
[00:38:32] - The world is a far from perfect place.
[00:38:34] There's just trade-offs.
[00:38:36] Everything you do is gonna be suboptimal.
[00:38:40] some attempt to get the best
[00:38:40] of both worlds that, you know,
[00:38:43] doesn't work out as well
[00:38:43] as you thought it was,
[00:38:46] and everyone is on the same page about
[00:38:48] confronting those trade-offs together,
[00:38:50] and they just feel like
[00:38:50] they're confronting them
[00:38:53] from a particular post.
[00:38:54] - Mm-hmm.
[00:38:55] - From a particular job, as
[00:38:55] part of the overall job of
[00:38:57] confronting all the trade-offs.
[00:38:59] - It's a bet on race to the top, right?
[00:39:00] - It's a bet on race to the top, yeah.
[00:39:02] - Like it's not a pure upside bet.
[00:39:03] Things could go wrong, but-
[00:39:04] - Yeah.
[00:39:04] - Like,
[00:39:05] we're all aligned on like,
[00:39:06] "This is the bet that we're making."
[00:39:08] - And markets are pragmatic,
[00:39:10] so if the more successful
[00:39:10] Anthropic becomes as a company,
[00:39:14] the more incentive there
[00:39:14] is for people to copy
[00:39:16] the things that make us successful.
[00:39:18] And the more that success is tied to
[00:39:20] actual safety stuff we do,
[00:39:22] the more it just creates
[00:39:23] a gravitational force in the industry
[00:39:25] that will actually get the
[00:39:25] rest of industry to compete.
[00:39:28] And it's like, "Sure,
[00:39:28] we'll build seat belts
[00:39:30] and everyone else can copy them."
[00:39:32] That's good.
[00:39:33] Yeah.
[00:39:34] - That's like good world.
[00:39:34] - That's really good.
[00:39:34] - Yeah.
[00:39:36] This is the race to the top, right?
[00:39:37] But if you're saying,
[00:39:38] "Well, we're not gonna
[00:39:38] build the technology,
[00:39:40] you're not gonna build it
[00:39:40] better than someone else,"
[00:39:42] that in the end,
[00:39:44] that just doesn't work
[00:39:44] because you're not proving
[00:39:46] that it's possible to
[00:39:46] get from here to there.
[00:39:48] - Mm-hmm.
[00:39:49] - Where the world needs to get,
[00:39:50] nevermind the industry,
[00:39:50] nevermind one company,
[00:39:53] is it needs to get us
[00:39:53] successfully through from
[00:39:56] this technology does-doesn't exist
[00:39:58] to the technology exists
[00:39:58] in a very powerful way
[00:40:01] and society has actually managed it.
[00:40:04] And I think the only
[00:40:04] way that's gonna happen
[00:40:05] is that if you have, at the
[00:40:05] level of a single company,
[00:40:09] and eventually at the
[00:40:09] level of the industry,
[00:40:11] you're actually confronting
[00:40:11] those trade-offs.
[00:40:13] You have to find a way to
[00:40:13] actually be competitive,
[00:40:18] to actually lead the
[00:40:18] industry, in some cases,
[00:40:20] and yet manage to do things safely.
[00:40:22] And if you can do that,
[00:40:24] the gravitational pull
[00:40:24] you exert is so great.
[00:40:28] There's so many factors,
[00:40:29] from the regulatory environment,
[00:40:31] to the kinds of people who
[00:40:31] wanna work at different places,
[00:40:34] to, even sometimes,
[00:40:34] the views of customers-
[00:40:36] - Yeah.
[00:40:37] - That kind of drive in the direction of
[00:40:39] if you can show that you
[00:40:39] can do well on safety
[00:40:43] without sacrificing
[00:40:43] competitiveness, right,
[00:40:45] if you can find these kind of win-wins,
[00:40:48] then others are incentivized
[00:40:48] to do the same thing.
[00:40:50] - Yeah, I mean I think that's why
[00:40:52] getting things like the
[00:40:52] RSP right is so important,
[00:40:55] because I think that we ourselves,
[00:40:59] seeing where the technology
[00:40:59] is headed, have often thought,
[00:41:02] "Oh wow, we need to be really
[00:41:02] careful of this thing,"
[00:41:05] but at the same time we
[00:41:05] have to be even more careful
[00:41:07] not to be crying wolf,
[00:41:09] saying that like, "Innovation
[00:41:09] needs to stop here."
[00:41:12] We need to sort of find a way
[00:41:12] to make AI useful, innovative,
[00:41:19] delightful for customers,
[00:41:20] but also figure out what the
[00:41:20] constraints really have to be
[00:41:24] that we can stand behind,
[00:41:24] that makes systems safe,
[00:41:27] so that it's possible
[00:41:27] for others to think that
[00:41:30] they can do that too,
[00:41:31] and they can succeed,
[00:41:31] they can compete with us.
[00:41:34] - We're not doomers, right?
[00:41:35] Like, we wanna build the positive thing.
[00:41:37] - Yeah.
[00:41:38] - We wanna like build the good thing.
[00:41:38] - And we've seen it happen in practice.
[00:41:40] A few months after we
[00:41:40] came out with our RSP,
[00:41:43] the three most prominent AI
[00:41:43] companies had one, right?
[00:41:46] Interpretability research,
[00:41:48] that's another area we've done it.
[00:41:49] Just the focus on safety overall,
[00:41:52] like collaboration with
[00:41:52] the AI safety institutes,
[00:41:54] other areas.
[00:41:56] - Yeah, the Frontier Red Team
[00:41:56] got cloned almost immediately,
[00:41:59] which is good.
[00:42:00] You want all the labs
[00:42:00] to be testing for like,
[00:42:02] very, very security-scary risks.
[00:42:04] - Export the seat belts.
[00:42:05] - Yeah, exactly.
[00:42:05] - Mm-hmm,
[00:42:06] export the seat belts.
[00:42:07] Well, Jack also mentioned it earlier,
[00:42:08] but customers also really
[00:42:08] care about safety, right?
[00:42:12] Customers don't want models
[00:42:12] that are hallucinating.
[00:42:14] They don't want models
[00:42:14] that are easy to jailbreak.
[00:42:16] They want models that
[00:42:16] are helpful and harmless,
[00:42:19] right?
[00:42:19] - Yeah.
[00:42:20] - And so a lot of the time,
[00:42:21] what we hear in customer calls is just,
[00:42:22] "We're going with Claude
[00:42:22] because we know it's safer."
[00:42:24] I think that is also a
[00:42:24] huge market impact, right,
[00:42:26] because our ability to have models
[00:42:29] that are trustworthy and reliable,
[00:42:31] that matters for the market pressure
[00:42:33] that it puts on competitors, too.
[00:42:35] - Maybe to unpack
[00:42:35] something that Dario said
[00:42:37] a little bit more,
[00:42:38] I think there's this
[00:42:38] narrative or this idea
[00:42:40] that maybe the virtuous thing
[00:42:42] is to almost like nobly fail, right?
[00:42:45] It's like you should go
[00:42:46] and like put safety,
[00:42:48] you should go and put things,
[00:42:50] you should sort of demonstrate
[00:42:50] like in an impragmatic way
[00:42:53] so that you can sort of demonstrate
[00:42:54] your purity to the cause
[00:42:54] or something like this.
[00:42:58] And I think if you do that,
[00:43:00] it's actually very self-defeating.
[00:43:02] For one thing, it means that
[00:43:03] you're gonna have the
[00:43:03] people who are are deciding,
[00:43:05] making decisions,
[00:43:06] be self-selected for being
[00:43:06] people who don't care,
[00:43:09] and for people who aren't
[00:43:09] prioritizing safety
[00:43:11] and who don't care about it.
[00:43:13] And I think, on the other hand,
[00:43:14] if you try really hard to find the way
[00:43:17] to align the incentives
[00:43:19] and make it so that if
[00:43:19] there are hard decisions,
[00:43:22] they happen at the points where
[00:43:23] there is the most force to go and support
[00:43:26] making the correct hard decisions,
[00:43:28] and where there's the most evidence,
[00:43:29] then you can sort of start to
[00:43:29] trigger this race to the top
[00:43:32] that Dario is describing,
[00:43:33] where instead of going
[00:43:33] and having, you know,
[00:43:37] the people who care get
[00:43:37] pushed out of influence,
[00:43:39] you instead pull other people
[00:43:39] to have to go and follow.
[00:43:43] - So what are you all excited about
[00:43:45] when it comes to the next
[00:43:45] things we'll be working on?
[00:43:48] - Well, I think there's a bunch of reasons
[00:43:50] you can be excited about interpretability.
[00:43:52] One is obviously safety,
[00:43:54] but there's another one
[00:43:54] that I think I find,
[00:43:56] at an emotional level, you know,
[00:43:58] equally exciting or
[00:43:58] equally meaningful to me,
[00:44:02] which is just that I think
[00:44:02] neural networks are beautiful
[00:44:05] and I think that there's
[00:44:05] a lot of beauty in them
[00:44:07] that we don't see.
[00:44:08] We treat them like these black boxes that
[00:44:10] we're not particularly
[00:44:10] interested in the internal stuff,
[00:44:14] but when you start to
[00:44:14] go and look inside them,
[00:44:15] they're just full of
[00:44:15] amazing, beautiful structure.
[00:44:19] You know, it's sort of like
[00:44:19] if people looked at biology
[00:44:22] and they were like, "You know,
[00:44:22] evolution is really boring.
[00:44:27] It's just a simple thing that
[00:44:27] goes and runs for a long time,
[00:44:31] and then it makes animals,"
[00:44:32] and like, instead,
[00:44:33] it's like, actually, you know,
[00:44:34] each one of those animals
[00:44:34] that evolution produces,
[00:44:36] and I think that, you know,
[00:44:36] it's an optimization process,
[00:44:39] like training a neural network.
[00:44:40] You know,
[00:44:41] they're full of incredible
[00:44:41] complexity and structure,
[00:44:43] and we have an entire
[00:44:43] sort of artificial biology
[00:44:47] inside of neural networks.
[00:44:48] If you're just willing
[00:44:48] to look inside them,
[00:44:51] there's all of this amazing stuff.
[00:44:52] And I think that we're just
[00:44:52] starting to slowly unpack it,
[00:44:55] and it's incredible, and
[00:44:55] there's so much there,
[00:44:57] but there's just so much
[00:44:57] we discovered there.
[00:44:59] We're just starting to crack it open
[00:45:01] and I think it's gonna
[00:45:01] be amazing and beautiful.
[00:45:04] And sometimes I imagine, you know,
[00:45:07] like a decade in the future,
[00:45:08] walking into a bookstore
[00:45:08] and buying, you know,
[00:45:10] the textbook on neural
[00:45:10] network interpretability
[00:45:12] or really, like, on the
[00:45:12] biology of neural networks,
[00:45:15] and just the kind of wild things
[00:45:17] that are gonna be inside of it.
[00:45:18] And I think that in the next decade,
[00:45:20] in the next couple of years even,
[00:45:22] we're gonna go and start to go in
[00:45:23] and really discover all of those things.
[00:45:26] And it's gonna be wild and incredible.
[00:45:29] - It's also gonna be great
[00:45:31] that you get to buy your own textbook.
[00:45:34] - Just have your face on it.
[00:45:35] - I mean, yeah.
[00:45:38] - I'm excited that a few years
[00:45:38] ago if you had said like,
[00:45:41] "Governments will set up new bodies
[00:45:44] to test and evaluate AI systems
[00:45:46] and they will actually
[00:45:46] be competent and good,"
[00:45:49] you would've not thought that
[00:45:49] was going to be the case.
[00:45:51] But it's happened,
[00:45:52] it's kind of like governments have built
[00:45:55] these new embassies, almost,
[00:45:57] to deal with this new kind
[00:45:57] of class of technology
[00:46:00] or, like, thing that Chris studies.
[00:46:02] And I'm just very excited
[00:46:02] to see where that goes.
[00:46:05] I think it actually means
[00:46:05] that we have state capacity
[00:46:08] to deal with this kind
[00:46:08] of societal transition,
[00:46:10] so it's not just companies.
[00:46:12] And I'm excited to help with that.
[00:46:14] - I'm already excited
[00:46:14] about this to, you know,
[00:46:17] to a certain extent today,
[00:46:18] but I think just
[00:46:18] imagining the future world
[00:46:20] of what AI is going to
[00:46:20] be able to do for people
[00:46:24] is it's impossible to not
[00:46:24] feel excited about that.
[00:46:28] Dario talks about this a lot,
[00:46:30] but I think even just
[00:46:30] the sort of glimmers of
[00:46:32] Claude being able to help with, you know,
[00:46:35] vaccine development and cancer research
[00:46:37] and biological research
[00:46:39] is crazy, like, just to be able
[00:46:39] to watch what it can do now,
[00:46:42] but when I fast forward, you know,
[00:46:44] three years in the future
[00:46:44] or five years in the future,
[00:46:46] imagining that Claude could actually solve
[00:46:48] so many of the fundamental problems
[00:46:50] that we just face as humans.
[00:46:53] Even just from a health perspective alone,
[00:46:56] even if you sort of take
[00:46:56] everything else out,
[00:46:58] feels really exciting to me,
[00:47:00] just like thinking back to
[00:47:01] my international development times.
[00:47:03] It would be amazing if
[00:47:03] Claude was responsible for
[00:47:05] helping to do a lot of the
[00:47:05] work that I was trying to do
[00:47:07] a lot less effectively
[00:47:07] when I was, like, 25.
[00:47:10] - I mean, I guess similarly,
[00:47:11] I'm excited to build Claude for work.
[00:47:13] Like, I'm excited to build
[00:47:13] Claude into the company
[00:47:17] and into companies all over the world.
[00:47:19] - I guess I'm excited just
[00:47:19] for, I guess like, personally,
[00:47:23] like I like using Claude a lot
[00:47:26] at work,
[00:47:27] and so like, definitely,
[00:47:29] there's been increasing
[00:47:29] amounts of like home times
[00:47:31] with like me just like chatting
[00:47:31] with Claude about stuff.
[00:47:34] I think the biggest recent
[00:47:34] thing has been code-
[00:47:39] - Mm-hmm.
[00:47:39] - Where like six months ago,
[00:47:41] I didn't use Claude to do any coding work.
[00:47:43] Like,
[00:47:44] our teams didn't really use
[00:47:44] Claude that much for coding,
[00:47:46] and now it's like just phase difference.
[00:47:48] Like, I gave a talk at
[00:47:48] YCU like week before last,
[00:47:52] and at the beginning I just asked like,
[00:47:54] "Okay, so how many folks here
[00:47:54] use Claude for coding now?"
[00:47:59] And literally 95% of hands-
[00:48:01] - Wow.
[00:48:02] - Like, all the hands in the room,
[00:48:03] which just is totally
[00:48:03] different than how it was
[00:48:05] four months ago or whatever.
[00:48:06] - Mm-hmm.
[00:48:06] - Yeah.
[00:48:07] - So when I think about
[00:48:07] what I'm excited about,
[00:48:09] I think about places where,
[00:48:09] you know, like I said before,
[00:48:12] where there's this kind
[00:48:12] of consensus that, again,
[00:48:15] seems like consensus,
[00:48:17] seems like what everyone wise thinks,
[00:48:18] and then it just kind of breaks,
[00:48:21] and so places where I think
[00:48:21] that's about to happen
[00:48:23] and it hasn't happened yet.
[00:48:25] One of them is interpretability.
[00:48:27] I think interpretability
[00:48:27] is both the key to
[00:48:30] steering and making safe AI systems,
[00:48:33] and we're about to understand,
[00:48:35] and interpretability
[00:48:35] contains insights about
[00:48:39] intelligent optimization problems
[00:48:40] and about how the human brain works.
[00:48:43] I've said, and I'm really not joking,
[00:48:45] Chris Olah is gonna be a
[00:48:45] future Nobel Medicine Laureate.
[00:48:48] - Aw, yeah.
[00:48:49] - I'm serious.
[00:48:50] I'm serious,
[00:48:51] because a lot of these,
[00:48:53] I used to be a neuroscientist,
[00:48:54] a lot of these mental illnesses,
[00:48:56] the ones we haven't figured out, right,
[00:48:58] schizophrenia or the mood disorders,
[00:49:00] I suspect there's some higher
[00:49:00] level system thing going on
[00:49:04] and that it's hard to make
[00:49:04] sense of those with brains
[00:49:06] because brains are so mushy
[00:49:08] and hard to open up and interact with.
[00:49:11] Neural nets are not like this;
[00:49:12] they're not a perfect analogy,
[00:49:13] but as time goes on, they
[00:49:13] will be a better analogy.
[00:49:16] That's one area.
[00:49:17] Second is, related to that,
[00:49:19] I think just the use of AI for biology.
[00:49:22] Biology is an incredibly
[00:49:22] difficult problem.
[00:49:26] People continue to be skeptical,
[00:49:26] for a number of reasons.
[00:49:31] I think that consensus
[00:49:31] is starting to break.
[00:49:33] We saw a Nobel Prize in chemistry
[00:49:34] awarded for AlphaFold;
[00:49:34] remarkable accomplishment.
[00:49:37] We should be trying to build things
[00:49:39] that can help us create
[00:49:39] a hundred AlphaFolds.
[00:49:42] And then finally, using
[00:49:42] AI to enhance democracy.
[00:49:46] We worry about if AI is
[00:49:46] built in the wrong way,
[00:49:49] it can be a tool for authoritarianism.
[00:49:52] How can AI be a tool for
[00:49:52] freedom and self-determination?
[00:49:56] I think that one is
[00:49:56] earlier than the other two,
[00:49:59] but it's gonna be just as important.
[00:50:01] - Yeah, I mean, I guess two things that
[00:50:04] at least connect to what
[00:50:04] you were saying earlier,
[00:50:05] I mean, one is I feel like
[00:50:05] people frequently join Anthropic
[00:50:12] because they're sort of
[00:50:13] scientifically really curious about AI
[00:50:17] and then kind of get
[00:50:17] convinced by AI progress
[00:50:21] to sort of share the vision of the need,
[00:50:24] not just to advance the technology,
[00:50:26] but to understand it more deeply
[00:50:28] and to make sure that it's safe.
[00:50:31] And I feel like it's actually
[00:50:31] just sort of exciting
[00:50:33] to have people that you're working with
[00:50:36] kind of more and more
[00:50:36] united in their vision
[00:50:39] for both what AI development looks like
[00:50:41] and the sort of sense of
[00:50:41] responsibility associated with it.
[00:50:44] And I feel like that's
[00:50:44] been happening a lot
[00:50:46] due to a lot of advances
[00:50:47] that have happened in the last year,
[00:50:48] like what Tom talked about.
[00:50:50] Another is that, I mean,
[00:50:51] going back really to concrete problems,
[00:50:53] I feel like we've done a
[00:50:53] lot of work on AI safety
[00:50:56] up until this point.
[00:50:57] A lot of it's really important,
[00:50:59] but I think we're now, with
[00:50:59] some recent developments,
[00:51:01] really getting a glimmer
[00:51:01] of what kinds of risks
[00:51:04] might literally come about from systems
[00:51:06] that are very, very advanced-
[00:51:07] - Mm-hmm.
[00:51:08] - So that we can
[00:51:08] investigate and study them
[00:51:11] directly with interpretability,
[00:51:13] with other kinds of safety mechanisms,
[00:51:15] and really understand what the risks from
[00:51:17] very advanced AI might look like.
[00:51:21] And I think that that's something that is
[00:51:23] really gonna allow us to
[00:51:23] sort of further the mission
[00:51:26] in a really deeply
[00:51:26] scientific, empirical way.
[00:51:29] And so I'm excited about sort
[00:51:29] of the next six months of
[00:51:31] how we use our understanding of
[00:51:33] what can go wrong with advanced
[00:51:33] systems to characterize that
[00:51:37] and figure out how to
[00:51:37] avoid those pitfalls.
[00:51:40] - Perfect.
[00:51:41] Fin!
[00:51:41] - Yay!
[00:51:42] - We did it!
[00:51:43] - Woo!
[00:51:44] - Good time.
[00:51:44] - I know.
[00:51:45] We gotta do this more often.
