# Dwarkesh Patel: Dario Amodei — We Are Near the End of the Exponential
- **YouTube URL:** https://www.youtube.com/watch?v=n1E9IZfvGMA
- **Lines:** 4021

---

[00:00:02] So we talked three years ago. I'm
[00:00:02] curious in your view, what has been the
[00:00:04] biggest update of the last three years?
[00:00:05] What has been the biggest difference
[00:00:06] between what it felt like last three
[00:00:07] years versus now?
[00:00:08] >> Yeah, I would say actually the
[00:00:10] underlying technology like the
[00:00:12] exponential of the technology has has
[00:00:15] gone broadly speaking I would say about
[00:00:18] about as I expected it to go. I mean
[00:00:20] there's like plus or minus you know a
[00:00:22] couple there's plus or minus a year or
[00:00:24] two here. There's plus or minus a year
[00:00:25] or two there. I don't know that I would
[00:00:27] have predicted the specific direction of
[00:00:29] code. Um but but actually when I look at
[00:00:32] the exponential it it is roughly what I
[00:00:36] expected in terms of the march of the
[00:00:38] models from like you know smart high
[00:00:39] school student to smart college student
[00:00:41] to like you know beginning to do PhD and
[00:00:43] professional stuff and in the case of
[00:00:45] code reaching beyond that. So you know
[00:00:47] the frontier is a little bit uneven.
[00:00:49] It's roughly what I expected. I will
[00:00:51] tell you though what the most surprising
[00:00:53] thing has been. The most surprising
[00:00:55] thing has been the lack of public
[00:00:57] recognition of how close we are to the
[00:01:00] end of the exponential. To me, it is
[00:01:03] absolutely wild that, you know, you have
[00:01:06] people, you know, within the bubble and
[00:01:08] outside the bubble, you know, but but
[00:01:10] you have people talking about these
[00:01:11] these, you know, just the same tired old
[00:01:14] hot button political issues and like,
[00:01:17] you know, around us. We're like near the
[00:01:20] end of the exponential. I I want to
[00:01:22] understand what that exponential looks
[00:01:24] like right now because the first
[00:01:25] question I asked you when we recorded
[00:01:27] three years ago was, you know, what's up
[00:01:29] with scaling? How why does it work? Um I
[00:01:31] have a similar question now but I feel
[00:01:33] like it's a more complicated question
[00:01:34] because at least from the public's point
[00:01:36] of view.
[00:01:36] >> Yes.
[00:01:37] >> Three years ago there were these you
[00:01:38] know well-known public trends where
[00:01:41] across many orders of magnitude of
[00:01:43] compute you could see how the loss
[00:01:44] improves and now we have RL scaling and
[00:01:47] there's no publicly known scaling law
[00:01:49] for it. It's not even clear what exactly
[00:01:50] the story is of is this supposed to be
[00:01:53] teaching the model skills is supposed to
[00:01:54] be teaching metalarning. Um what is the
[00:01:57] scaling hypothesis at this point?
[00:01:59] >> Yeah. So, so I have actually the same
[00:02:01] hypothesis that I had even all the way
[00:02:04] back in 2017. So, in 2017, I think I
[00:02:06] talked about it last time, but I wrote a
[00:02:08] doc called the the big blob of compute
[00:02:10] hypothesis. And and and you know, it it
[00:02:13] wasn't about the scaling of language
[00:02:14] models in particular. When I when I
[00:02:16] wrote it, GPT1 had had just come out,
[00:02:19] right? So, that was you know, one among
[00:02:21] many things, right? There was back in
[00:02:23] those days there was robotics. People
[00:02:24] tried to work on reasoning as a separate
[00:02:26] thing from language models. there was
[00:02:28] scaling of the kind of RL that happened
[00:02:31] that you know kind of happened in Alph
[00:02:32] Go and uh you know that that happened at
[00:02:35] Dota at OpenAI and um you know people
[00:02:39] remember Starcraft at Deep Mind you know
[00:02:40] the Alpha Star um so uh it was written
[00:02:44] as a more general document and and the
[00:02:46] specific thing I said was the following
[00:02:48] that and you know it's it's very you
[00:02:50] know Rich Sutton put out the bitter
[00:02:52] lesson a couple years later um uh but
[00:02:54] you know the the hypothesis is is
[00:02:56] basically the same so so what it says is
[00:02:59] all the cleverness, all the techniques,
[00:03:01] all all the kind of we need a new method
[00:03:04] to to do something like that doesn't
[00:03:06] matter very much. There are only a few
[00:03:07] things that matter and I think I listed
[00:03:09] seven of them. One is like how much raw
[00:03:12] compute you have. The other is the
[00:03:14] quantity of data that you have. Then the
[00:03:17] third is kind of the quality and
[00:03:19] distribution of data, right? It needs to
[00:03:20] be a broad broad distribution of data.
[00:03:23] The fourth is I think how long you train
[00:03:26] for. Um the fifth is you need an
[00:03:29] objective function that can scale to the
[00:03:31] moon. So the pre-training objective
[00:03:33] function is one such objective function
[00:03:35] right another objective function is you
[00:03:39] know the the kind of RL objective
[00:03:41] function that says like you have a goal
[00:03:42] you're going to go out and reach the
[00:03:44] goal within that of course there's
[00:03:45] objective rewards like you know like you
[00:03:48] see in math and coding and there's more
[00:03:50] subjective rewards like you see in RL
[00:03:52] from human feedback are kind of higher
[00:03:54] order higher order versions of that and
[00:03:56] and then the sixth and seventh were
[00:03:58] things around kind of like normaliz
[00:04:01] ation or conditioning like you know just
[00:04:03] getting the numerical stability so that
[00:04:05] kind of the big blob of compute flows in
[00:04:07] this laminer way instead of instead of
[00:04:09] running into problems. So that was the
[00:04:12] hypothesis and it's a hypothesis I still
[00:04:14] hold. I I don't think I've seen very
[00:04:17] much that is not in line with that
[00:04:19] hypothesis. And so the pre-trained
[00:04:21] scaling laws were one example of what of
[00:04:24] of of kind of what we see there. And
[00:04:26] indeed those have continued going like
[00:04:29] you know uh you know I think I think now
[00:04:31] it's been it's been widely reported like
[00:04:33] you know we feel good about pre-training
[00:04:35] like pre-training is continuing to give
[00:04:37] us gains. What has changed is that now
[00:04:41] we're also seeing the same thing for RL
[00:04:44] right so we're seeing a pre-training
[00:04:45] phase and then we're seeing like an RL
[00:04:47] phase on top of that. Um and with RL
[00:04:52] it's it's actually just the same like
[00:04:54] you know even even other companies have
[00:04:56] have published um uh um like um you know
[00:05:00] in some of their in some of their
[00:05:02] releases have published things that say
[00:05:04] look you know we train the model on math
[00:05:06] contests you know aime or or the kind of
[00:05:09] other things and you know how well how
[00:05:12] well the model does is log linear and
[00:05:14] how long we've trained it and we see
[00:05:16] that as well and it's not just math
[00:05:18] contest it's a wide variety of RL tasks.
[00:05:21] And so we're seeing the same scaling in
[00:05:24] RL that we saw for pre-training. Um you
[00:05:27] mentioned Richard Sutton and the bitter
[00:05:28] lesson. Yeah,
[00:05:29] >> I interviewed him last year and he is
[00:05:33] actually very non LLM pill. And if I'm
[00:05:36] if I I don't know if this is his
[00:05:38] perspective, but one way to paraphrase
[00:05:40] this objection is something like look
[00:05:42] something which possesses the true core
[00:05:44] of human learning would not require all
[00:05:47] these billions of dollars of data and
[00:05:49] compute and these bespoke environments
[00:05:51] to learn how to use Excel or how does an
[00:05:54] you know how to how to use PowerPoint,
[00:05:56] how to navigate a web browser. And the
[00:05:58] fact that we have to build in these
[00:05:59] skills using these RL environments hints
[00:06:03] that we're actually lacking this core
[00:06:07] human learning algorithm. Uh and so
[00:06:10] we're scaling the wrong thing. And so
[00:06:12] yeah, that does raise a question. Why
[00:06:13] are we doing all this RL scaling if we
[00:06:15] do think there's something that's going
[00:06:16] to be humanlike in its ability to learn
[00:06:18] on the fly?
[00:06:19] >> Yeah. Yeah. So I think I think this kind
[00:06:21] of puts together several things that
[00:06:23] should be kind of thought of thought of
[00:06:25] differently.
[00:06:26] >> Yeah. I think there is a genuine puzzle
[00:06:28] here, but it it may not matter. Um, in
[00:06:31] fact, I would guess it probably it
[00:06:33] probably doesn't matter. So, let's take
[00:06:35] the RL out of it for a second because I
[00:06:37] actually think RL and it's a red herring
[00:06:39] to say that RL is any different from
[00:06:41] pre-training in this matter. Um, so if
[00:06:43] we if we look at pre-training scaling,
[00:06:46] um, it it was very interesting back in,
[00:06:48] you know, 2017 when Alec Radford was
[00:06:52] doing GPT1. If you look at the models
[00:06:55] before GPT1, they were trained on these
[00:06:58] data sets that didn't represent a wide,
[00:07:01] you know, distribution of text, right?
[00:07:04] You had like, you know, these very
[00:07:06] standard, you know, kind of language
[00:07:08] modeling benchmarks and GBT1 itself was
[00:07:10] trained on a bunch of, I think it was
[00:07:12] fanfiction actually. Um, but you know,
[00:07:14] it was it was like literary, you know,
[00:07:16] it's like literary text, which is a very
[00:07:17] small fraction of the text that you get.
[00:07:19] And what we found with that, you know,
[00:07:21] and in those days it was like a billion
[00:07:23] words or something. So small data sets
[00:07:26] and represented a pretty narrow
[00:07:28] distribution, right? Like a narrow
[00:07:30] distribution of kind of what what you
[00:07:31] can see what you can see in the world.
[00:07:33] And it didn't generalize well. If you
[00:07:35] did better on um you know the the you
[00:07:39] know I forget what but some some kind of
[00:07:41] fanfiction corpus um it wouldn't
[00:07:44] generalize that well to kind of the
[00:07:46] other hat. you know, we had all these
[00:07:47] measures of like, you know, how well
[00:07:49] does how well does a model do at
[00:07:51] predicting all of these other kinds of
[00:07:53] texts. You really didn't see the
[00:07:54] generalization. It was only when you
[00:07:56] trained over all the tasks on the you,
[00:07:58] you know, the internet when you when you
[00:08:00] kind of did a general internet scrape,
[00:08:01] right, from something like, you know,
[00:08:04] common crawl or scraping links on
[00:08:05] Reddit, which is what we did for GPT2.
[00:08:08] It's only when you do that that you kind
[00:08:10] of started to get generalization. Um,
[00:08:13] and I think we're seeing the same thing
[00:08:14] on RL that we're starting with first
[00:08:17] very simple RL tasks like training on
[00:08:20] math competitions. Then we're kind of
[00:08:22] moving to, you know, kind of broader
[00:08:24] broader training that involves things
[00:08:26] like code as a task. And now we're
[00:08:28] moving to do kind of many many other
[00:08:30] tasks. And then I think we're going to
[00:08:32] increasingly get generalization. So that
[00:08:36] that kind of takes out the RL versus the
[00:08:38] pre-training side of it. But I think
[00:08:40] there is a puzzle here either way which
[00:08:42] is that on pre-training when we train
[00:08:44] the model on pre-training you know we we
[00:08:47] use like trillions of tokens right and
[00:08:50] and humans don't see trillions of words
[00:08:52] so there is an actual sample efficiency
[00:08:55] difference here there is actually
[00:08:57] something different that's that's
[00:08:58] happening here which is that the models
[00:09:00] start from scratch and you know they
[00:09:02] have to get much more much more training
[00:09:06] but we also see that once they're
[00:09:08] trained if we give them a long context
[00:09:10] length. The only thing blocking a long
[00:09:12] context length is like inference. But if
[00:09:13] we give them like a context length of a
[00:09:15] million, they're very good at learning
[00:09:17] and adapting within that context length.
[00:09:19] And and so I don't know the full answer
[00:09:22] to this, but but I think there's
[00:09:24] something going on that pre-training
[00:09:26] it's it's not like the process of humans
[00:09:29] learning. It's somewhere between the
[00:09:31] process of humans learning and the
[00:09:33] process of human evolution. It's like
[00:09:35] it's somewhere between like we get many
[00:09:37] of our priors from evolution. Our brain
[00:09:39] isn't just a blank slate, right? Whole
[00:09:41] books have been written about. I think
[00:09:43] the language models, they're much more
[00:09:44] blank slates. They literally start as
[00:09:46] like random weights. Whereas the human
[00:09:48] brain starts with all these regions.
[00:09:50] It's connected to all these inputs and
[00:09:51] outputs. Um and and so maybe we should
[00:09:55] think of pre-training and for that
[00:09:56] matter RL as well as as being something
[00:09:59] that exists in the middle space between
[00:10:02] human evolution and you know kind of
[00:10:05] human on on the spot learning and as the
[00:10:09] in context learning that the models do
[00:10:12] as as something between long-term human
[00:10:15] learning and short-term human learning.
[00:10:17] So, you know, there there's this
[00:10:18] hierarchy of like there's evolution,
[00:10:20] there's long-term learning, there's
[00:10:22] short-term learning, and there's just
[00:10:23] human reaction. And the LOM phases exist
[00:10:27] along this spectrum, but not necessarily
[00:10:30] exactly at the same points that there's
[00:10:32] no analog to some of the human modes of
[00:10:35] learning. The LOMs are kind of falling
[00:10:37] between the points. Does that make
[00:10:39] sense?
[00:10:39] >> Um, yes. Although some things are still
[00:10:41] a bit confusing. For example, if the
[00:10:43] analogy is that this is like evolution,
[00:10:45] so it's fine that it's not that sample
[00:10:46] efficient, then like well, if we're
[00:10:49] going to get the kind of super sample
[00:10:50] efficient agent from in context
[00:10:52] learning, why are we bothering to build
[00:10:54] in, you know, there's RL environment
[00:10:56] companies which are it seems like what
[00:10:58] they're doing is they're teaching it how
[00:10:59] to use this API, how to use Slack, how
[00:11:01] to use whatever. It's confusing to me
[00:11:03] why there's so much emphasis on that if
[00:11:05] the kind of agent that can just learn on
[00:11:07] the fly is emerging or is going to soon
[00:11:09] emerge or has already emerged.
[00:11:10] >> Yeah. Yeah. So I I I mean I can't speak
[00:11:12] for the emphasis of anyone else. I can I
[00:11:13] can only talk about how we how we think
[00:11:16] about it. I think the way we think about
[00:11:19] it is the goal is not to teach the model
[00:11:22] every possible skill within RL just as
[00:11:25] we don't do that within pre-training.
[00:11:26] Right? Within pre-training we're not
[00:11:28] trying to expose the model to you know
[00:11:31] every every possible uh you know way
[00:11:34] that words could be put together. Right?
[00:11:35] you know, we're it's it's rather that
[00:11:37] the model trains on a lot of things and
[00:11:40] then and then it reaches generalization
[00:11:42] across pre-training, right? That was
[00:11:43] that was the transition from GPT1 to
[00:11:46] GPT2 that I saw up close which is like
[00:11:49] you know the the model reaches a point
[00:11:51] you know I I I I like had these moments
[00:11:54] where I was like oh yeah you just give
[00:11:56] the model like you just give the model a
[00:11:58] list of numbers that's like you know um
[00:12:00] you know this is the cost of the house
[00:12:02] this is the square feet of the house and
[00:12:04] the model completes the pattern and does
[00:12:06] linear regression like not great but it
[00:12:08] does it but it's never seen that exact
[00:12:10] thing before and and so to you know to
[00:12:13] to the extent that we are building these
[00:12:16] RL environments the the goal is is very
[00:12:19] similar to what is be you know to what
[00:12:21] was done five or 10 years ago with
[00:12:23] pre-training with we're trying to get a
[00:12:26] we're trying to get a whole bunch of
[00:12:28] data not because we want to cover a
[00:12:30] specific document or a specific skill
[00:12:33] but because we want to generalize. I
[00:12:35] mean I I think the framework you're
[00:12:38] laying down obviously makes sense like
[00:12:40] we're making progress towards AGI. I
[00:12:42] think the crux is something like nobody
[00:12:44] at this point disagrees that we're going
[00:12:45] to achieve AGI in this century. And the
[00:12:48] crux is you say we're hitting the end of
[00:12:50] the exponential um and somebody else
[00:12:53] looks at this and says, "Oh yeah, we
[00:12:55] we're making progress. We've been making
[00:12:56] progress since 2012 and then 2035 we'll
[00:12:58] have a humanlike agent." And so I want
[00:13:00] to understand what it is that you're
[00:13:02] seeing which makes you think um yeah
[00:13:04] obviously we're seeing the kinds of
[00:13:06] things that evolution did or that human
[00:13:08] within the human lifetime learning is
[00:13:09] like in these models and why think that
[00:13:11] it's one year away and not 10 years
[00:13:13] away.
[00:13:13] >> I I I actually think of it as like two
[00:13:17] there's kind of two cases to be made
[00:13:19] here or like two two claims you could
[00:13:21] make. One of which is like stronger and
[00:13:23] the other of which is weaker. So, I
[00:13:25] think starting starting with the weaker
[00:13:27] claim, you know, when when I first saw
[00:13:31] the scaling back in like, you know,
[00:13:33] 2019,
[00:13:34] um, you know, I wasn't sure. You know,
[00:13:36] this was the whole this was kind of a
[00:13:38] 50/50 thing, right? I thought I saw
[00:13:40] something that was, you know, and and my
[00:13:42] claim was this is much more likely than
[00:13:44] anyone thinks it is. Like, this is wild.
[00:13:46] No one else would even consider this.
[00:13:48] Maybe there's a 50% chance this happens.
[00:13:51] um on the basic hypothesis of you know
[00:13:54] as you put it within 10 years we'll get
[00:13:57] to you know you know what I call kind of
[00:14:00] country of geniuses in a data center I'm
[00:14:02] at like 90% on that um and it's hard to
[00:14:05] go much higher than 90% cuz the world is
[00:14:07] so unpredictable um maybe the
[00:14:10] irreducible uncertainty would be if we
[00:14:12] were at 95% where you get to things like
[00:14:15] I don't know may maybe multi you know
[00:14:16] multiple companies have you know kind of
[00:14:19] internal turmoil and nothing happens and
[00:14:21] then Taiwan gets invaded and like all
[00:14:23] the all the fabs get blown up by
[00:14:25] missiles and and you know and then now
[00:14:27] you scenario you know just you could
[00:14:30] construct a scenario where there's like
[00:14:32] a 5% chance that it it or you know you
[00:14:35] can construct a 5% world where like
[00:14:37] things things get delayed for for for
[00:14:39] for for 10 years that's maybe 5%.
[00:14:43] There's another 5% which is that I'm
[00:14:46] very confident on tasks that can be
[00:14:48] verified. So I think I think with coding
[00:14:51] I'm just except for that irreducible
[00:14:52] uncertainty there's just there's I mean
[00:14:54] I think we'll be there in one or two
[00:14:55] years there's no way we will not be
[00:14:57] there there in 10 years in terms of
[00:14:58] being able to do it end to end coding.
[00:15:00] My one little bit the one little bit of
[00:15:03] of fundamental uncertainty even on long
[00:15:06] time scales is this thing about tasks
[00:15:08] that aren't verifiable like planning a
[00:15:11] mission to Mars like uh you know doing
[00:15:14] some fundamental scientific discovery
[00:15:16] like like crisper like you know writing
[00:15:19] a writing a novel hard to hard to verify
[00:15:22] those tasks. I am almost certain that
[00:15:26] we have a reliable path to get there.
[00:15:29] But like if there was a little bit
[00:15:31] uncertainty, it's there. So, so, so, so,
[00:15:34] so on the 10 years, I'm like, you know,
[00:15:37] 90% which is about as certain as you can
[00:15:39] be. Like I think it's I think it's crazy
[00:15:42] to say that this won't happen by by by
[00:15:45] 2035. Like in some sane world, it would
[00:15:47] be outside the mainstream. But but the
[00:15:49] emphasis on verification hints to me as
[00:15:54] a lack of a lack of uh belief that these
[00:15:57] models are generalized. If you think
[00:15:59] about humans,
[00:16:00] >> we are good at things that both which we
[00:16:01] get verifiable reward and things which
[00:16:04] we don't. You're like you have no no
[00:16:06] this is this is why I'm almost sure we
[00:16:08] already see substantial generalization
[00:16:10] from things that that verify to things
[00:16:12] that don't ver. We're already seeing
[00:16:13] that. But but it seems like you were
[00:16:14] emphasizing this as a spectrum which
[00:16:17] will
[00:16:18] uh split apart which domains we see more
[00:16:20] progress and I'm like but that's it
[00:16:22] doesn't seem like how humans get there.
[00:16:23] >> The world in which we don't make it or
[00:16:24] or or the world in which we don't get
[00:16:26] there is the world in which we do we do
[00:16:28] all the things that are that are
[00:16:30] verifiable and then they like you know
[00:16:33] many of them generalize but but we kind
[00:16:35] of don't get fully there. We don't we
[00:16:37] don't we don't fully you know we don't
[00:16:38] fully color in this side of the box.
[00:16:41] It's it's it's not a it's not a binary
[00:16:43] thing. But but it also seems to me even
[00:16:44] if even if in the world where
[00:16:46] generalization is weak when you only say
[00:16:47] baref domains it's not clear to me in
[00:16:49] such a world you could automate software
[00:16:51] engineering because software like in
[00:16:53] some sense you are quote unquote a
[00:16:55] software engineer but part of being a
[00:16:57] software engineer for you involves
[00:16:58] writing these like long memos about your
[00:16:59] grand vision about different things and
[00:17:01] so I don't think that's part of the job
[00:17:02] of sui that's part that's part of the
[00:17:04] job of the company but I do think
[00:17:06] involves like design documents and other
[00:17:08] things like that um which by the way the
[00:17:10] models are not bad they're already
[00:17:12] pretty good at writing comments and
[00:17:13] start and so with with again I'm making
[00:17:15] like much weaker claims here than I
[00:17:17] believe to like you know to to to to
[00:17:20] kind of set up a you know to to
[00:17:22] distinguish between two things like
[00:17:24] we're we're already almost there for
[00:17:26] software engineering and we are already
[00:17:27] almost there by by what metric there's
[00:17:29] one metric which is like how many lines
[00:17:30] of code are written by AI and if you use
[00:17:32] if you consider other productivity
[00:17:34] improvements in the course of the
[00:17:35] history of software engineering
[00:17:36] compilers write all the lines of
[00:17:38] software and but we there's a difference
[00:17:40] between how many lines are written and
[00:17:41] how big the productivity improvement Oh
[00:17:43] yeah. And um and then like we're almost
[00:17:45] there, meaning like the how big is the
[00:17:47] productivity improvement, not just how
[00:17:48] many lines are written.
[00:17:49] >> Yeah. Yeah. So so I actually um I
[00:17:51] actually I actually agree with you on
[00:17:53] this. So I I've made this series of
[00:17:54] predictions on um code and software
[00:17:58] engineering and and and I think people
[00:18:00] have repeatedly kind of misunderstood
[00:18:01] them. So So let me let me let me let me
[00:18:03] let me lay out the spectrum, right? Like
[00:18:05] I think it was like you know like you
[00:18:07] know eight eight or nine months ago or
[00:18:09] something I said you know the AI model
[00:18:11] will be writing 90 90% of the lines of
[00:18:13] code in like you know 3 to 6 months
[00:18:16] which which happened at least at some
[00:18:18] places right happened happened at
[00:18:20] entropic happened with many people
[00:18:22] downstream using our models but but
[00:18:24] that's actually a very weak criterion
[00:18:27] right people thought I was saying like
[00:18:29] we won't need 90% of the software
[00:18:31] engineers those things are worlds apart
[00:18:33] right like I would put the spectrum term
[00:18:35] as 90% of code is written by the model,
[00:18:39] 100% of code is written by the model and
[00:18:41] that's a big difference in productivity.
[00:18:43] Um 90% of the end toend SWE tasks,
[00:18:46] right? Including things like compiling,
[00:18:49] including things like setting up
[00:18:51] clusters and environments, testing
[00:18:53] features, writing memos, 90% of the SU
[00:18:56] tasks are written by the models. 100% of
[00:18:58] today's suite tasks are are are written
[00:19:01] by the models. And and even when when
[00:19:02] when that happen doesn't mean software
[00:19:04] engineers are out of a job like there's
[00:19:06] like new higher level things they can do
[00:19:08] where they can they can manage and then
[00:19:10] there's a further down the spectrum like
[00:19:12] you know there's 90% less demand for
[00:19:14] SWES which I think will happen but like
[00:19:17] this is this this is a spectrum and you
[00:19:19] know I wrote about it in in the
[00:19:20] adolescence of technology where I went
[00:19:22] through this kind of spectrum with
[00:19:24] farming um uh uh and so I I actually
[00:19:27] totally agree with you on that. It's
[00:19:29] just these are very different benchmarks
[00:19:31] from each other but we're proceeding
[00:19:32] through them super fast. It seems like
[00:19:34] in part of your vision it's like going
[00:19:35] from 90 to 100 um first it's going to
[00:19:38] happen fast and two that somehow that
[00:19:42] leads to huge productivity improvements.
[00:19:45] Um whereas when I noticed even in green
[00:19:47] field projects that people start with
[00:19:48] cloud code or something people report
[00:19:50] starting a lot of projects and I'm like
[00:19:52] do we see in the world out there a
[00:19:54] renaissance of software all these new
[00:19:56] features that wouldn't exist otherwise
[00:19:58] and at least so far it doesn't seem like
[00:19:59] we see that and so that does make me
[00:20:01] wonder even if even if like I never had
[00:20:03] to intervene on cloud code um there is
[00:20:06] this thing of like there's just the
[00:20:08] world is complicated jobs are
[00:20:09] complicated and
[00:20:11] closing the loop on self-contained
[00:20:13] systems whether just writing software or
[00:20:15] something how much sort of how much
[00:20:17] broader gains we would see just from
[00:20:19] that. And so maybe that makes us this
[00:20:21] should dilute our estimation of the
[00:20:23] country of geniuses.
[00:20:24] >> I well well I actually I I like I like
[00:20:28] I simultaneously agree with you agree
[00:20:32] that it's a reason why these things
[00:20:34] don't happen instantly but at the same
[00:20:36] time I think the the the effect is going
[00:20:38] to be very fast. So like I don't know
[00:20:41] you could have these two poles right one
[00:20:43] is like um you know AI is like you know
[00:20:46] it's not going to make progress it's
[00:20:48] slow like it's going to take you know
[00:20:50] kind of forever to diffuse within the
[00:20:51] economy right economic diffusion has
[00:20:53] become one of these buzzwords that's
[00:20:55] like a a reason why we're not going to
[00:20:57] make AI progress or why AI progress
[00:20:59] doesn't matter and and you know the
[00:21:00] other axis is like we'll get recursive
[00:21:02] self-improvement you know the whole
[00:21:04] thing you know can't you just draw an
[00:21:06] exponential line on the on the curve you
[00:21:07] know it's it's we're going to have you
[00:21:09] know Dyson spheres around the sun in
[00:21:11] like you know
[00:21:13] you know so many nanconds after you know
[00:21:16] after after we get recursive I mean I'm
[00:21:18] completely caricaturing the view here
[00:21:20] but like you know there there there are
[00:21:21] these two extremes but what we've seen
[00:21:25] from from the beginning you know at
[00:21:26] least if you look within anthropic
[00:21:28] there's this bizarre 10x per year growth
[00:21:32] in revenue that we've seen right so you
[00:21:35] know in 2023 it was like 0 to 100
[00:21:37] million 2024 it was 100 million to a
[00:21:40] billion. 2025 it was a billion to like 9
[00:21:44] or 10 billion. And then
[00:21:46] >> you guys should have just bought like a
[00:21:47] billion dollars with your own product so
[00:21:48] you could just like have a clean 10V
[00:21:50] [laughter] and and the first month of
[00:21:51] this year like that that exponential is
[00:21:54] you would think it would slow down but
[00:21:55] it would like you know we added another
[00:21:57] few billion to like you know to to to we
[00:22:00] added another few billion to revenue in
[00:22:03] January and and so you know obviously
[00:22:06] that curve can't go on forever right you
[00:22:08] know the GDP is only so large I don't
[00:22:10] you know I I would even guess that it
[00:22:12] bends that it bends bends somewhat this
[00:22:15] here. But like that is like a fast
[00:22:17] curve, right? That's like a that's like
[00:22:19] a really fast curve. And I would bet it
[00:22:22] stays pretty fast even as the scale goes
[00:22:24] to the entire economy. So like I I think
[00:22:27] we should be thinking about this middle
[00:22:28] world where things are like extremely
[00:22:32] fast but not instant where they take
[00:22:35] time because of economic diffusion
[00:22:37] because of the need to close the loop
[00:22:39] because you know it's like this fiddly
[00:22:42] oh man I have to do change management
[00:22:43] within my enterprise you know I have to
[00:22:45] like you know uh uh you know I I I I
[00:22:49] like I set this up but but you know I
[00:22:51] have to change the security permissions
[00:22:52] on this in order to make it actually
[00:22:54] work or you know, I had this like old
[00:22:57] piece of software that, you know, that
[00:22:59] like, you know, checks the model before
[00:23:00] it's compiled and and and like released
[00:23:02] and I have to rewrite it. And yes, the
[00:23:04] model can do that, but I have to tell
[00:23:05] the model to do that and it has to it
[00:23:07] has to take time to do that. and and and
[00:23:10] so I think everything we've seen so far
[00:23:13] is is compatible with the idea that
[00:23:16] there's one fast exponential that's the
[00:23:18] the capability of the model and then
[00:23:20] there's another fast exponential that's
[00:23:22] downstream of that which is the
[00:23:24] diffusion of the model into the economy
[00:23:26] not instant
[00:23:28] not slow much faster than any previous
[00:23:31] technology but it has its limits and and
[00:23:34] and and this is what we you know when I
[00:23:37] when I look inside anthropic when I look
[00:23:39] at our customers fast adoption but not
[00:23:42] infinitely fast.
[00:23:43] >> Um can I try a hot take on you?
[00:23:45] >> Yeah.
[00:23:45] >> I feel like diffusion is cope that
[00:23:47] people use to say when it's like if the
[00:23:50] model isn't able to do something they're
[00:23:51] like oh but the diffus it's like a
[00:23:53] diffusion issue. But then you should use
[00:23:55] the comparison to humans. You would
[00:23:57] think that the inherent advantages that
[00:23:58] AIs have would make diffusion a much
[00:24:01] easier problem for new AIs getting
[00:24:04] onboarded than new humans getting
[00:24:05] onboarded. So an AI can read your entire
[00:24:07] Slack and your drive in minutes. They
[00:24:08] can share all the knowledge that the
[00:24:10] other copy other copies of the same
[00:24:11] instance have. You don't have this
[00:24:12] adverse selection problem when you're
[00:24:13] hiring AI because you can just hire
[00:24:15] copies of a vetted AI model. Um hiring a
[00:24:18] human is like so much more hassle. And
[00:24:20] people hire humans all the time, right?
[00:24:21] We pay humans upwards of $50 trillion in
[00:24:23] wages because they're useful. Uh even
[00:24:26] though it's like in principle it would
[00:24:28] be much easier to integrate AI into the
[00:24:30] economy than it is to hire humans. I
[00:24:32] think like the diffusion I feel like
[00:24:33] doesn't really I I think diffusion is
[00:24:36] very real and and and and and doesn't
[00:24:39] have to you know doesn't exclusively
[00:24:41] have to do with limitation limitation
[00:24:44] limitations on the AI models like again
[00:24:47] there are people who use diffusion to to
[00:24:49] you know as kind of a buzzword to say
[00:24:51] this isn't a big deal. I'm not talking
[00:24:53] about that. I'm not talking about, you
[00:24:55] know, AI will diffuse at the speed that
[00:24:57] previous I think AI will diffuse much
[00:24:59] faster than previous technologies have,
[00:25:02] but but not infinitely fast. So, I'll
[00:25:04] I'll just give an example of this,
[00:25:05] right? Like there's like claude code.
[00:25:07] Like claude code is extremely easy to
[00:25:09] set up. Um, you know, if you're a
[00:25:11] developer, you can kind of just start
[00:25:13] using cla code. There is no reason why a
[00:25:15] developer at a large enterprise should
[00:25:18] not be adopting claude code as quickly
[00:25:21] as you know individual developer
[00:25:24] developer at a startup and we do
[00:25:25] everything we can to promote it right we
[00:25:27] sell uh we sell cla code to enterprises
[00:25:30] and big enterprises like you know big
[00:25:33] big financial companies big
[00:25:35] pharmaceutical companies all of them
[00:25:37] they're adopting claude code much faster
[00:25:41] than enterprises typically adopt new
[00:25:43] technology, right? But but again, it
[00:25:46] like it it it it takes time like any
[00:25:49] given feature or any given product like
[00:25:52] claude code or like co-work will get
[00:25:54] adopted by the you know the individual
[00:25:58] developers who are on Twitter all the
[00:25:59] time by the like series A startups
[00:26:02] many months faster than than you know
[00:26:05] than they will get adopted by like you
[00:26:07] know a like large enterprise that does
[00:26:10] food sales. Um there are a number of
[00:26:12] factors like you have to go through
[00:26:14] legal, you have to provision it for
[00:26:15] everyone. It has to you know like it has
[00:26:18] to pass security and compliance. The
[00:26:21] leaders of the company who are further
[00:26:22] away from the AI revolution you know are
[00:26:25] are forwardlooking but they have to say
[00:26:27] oh it makes sense for us to spend 50
[00:26:30] million. This is what this claud code
[00:26:32] thing is. This is why it helps our
[00:26:34] company. This is why it makes us more
[00:26:36] productive. And then they have to
[00:26:37] explain to the people two levels below.
[00:26:39] and they have to say, "Okay, we have
[00:26:41] 3,000 developers. Like, here's how we're
[00:26:43] going to roll it out to our developers."
[00:26:45] And we have conversations like this
[00:26:46] every day. Like, you know, we are doing
[00:26:48] everything we can to make Anthropics
[00:26:51] revenue grow 20 or 30x a year instead of
[00:26:54] 10x a year. Um, you know, and and and
[00:26:57] again, you know, many enterprises are
[00:26:59] just saying this is so productive like,
[00:27:01] you know, we're going to take shortcuts
[00:27:03] in our usual procurement process, right?
[00:27:05] they're moving much faster than you know
[00:27:07] when we tried to sell them just the
[00:27:08] ordinary API which many of them use but
[00:27:10] quad code is a more compelling product
[00:27:13] um but it's not an infinitely compelling
[00:27:15] product and I don't think even AGI or
[00:27:18] powerful AI or country of geniuses in
[00:27:20] the data center will be an infinitely
[00:27:21] compelling product it will be a
[00:27:23] compelling product enough maybe to get
[00:27:25] three or five or 10x a year growth even
[00:27:28] when you're in the hundreds of billions
[00:27:29] of dollars which is extremely hard to do
[00:27:31] and has never been done in history
[00:27:32] before but not infinitely fast I I buy
[00:27:34] that it would be a slight slowdown and
[00:27:36] maybe this is not your claim but
[00:27:37] sometimes people talk about this like oh
[00:27:39] the capabilities are there but because
[00:27:41] of diffusion um otherwise like we're
[00:27:44] basically at AGI and then
[00:27:45] >> I I I don't believe we're basically at
[00:27:47] AGI.
[00:27:48] >> I think if you had the country of
[00:27:49] geniuses in a data center if your
[00:27:51] company didn't
[00:27:53] geniuses in a data center we would know
[00:27:55] it. We would know it if you had the
[00:27:57] country of geniuses in a data center
[00:27:59] like everyone in this room would know
[00:28:00] it. Everyone in Washington would know
[00:28:03] it. like you know people in rural rural
[00:28:06] parts might not know it but but but like
[00:28:09] we would know it we don't have that now
[00:28:11] that that's very clear as Dario was
[00:28:13] ending at to get generalization you need
[00:28:15] to train across a wide variety of
[00:28:18] realistic tasks and environments [music]
[00:28:20] for example with a sales agent the
[00:28:22] hardest part isn't teaching it to mash
[00:28:23] buttons in a specific database in
[00:28:25] Salesforce it's training the agent's
[00:28:27] judgment across ambiguous situations how
[00:28:29] do you sort through a database with
[00:28:30] thousands of leads to figure out which
[00:28:32] ones are
[00:28:33] How do you actually reach out? What do
[00:28:35] you do when you get ghosted? When an AI
[00:28:36] lab wanted to train a sales agent,
[00:28:38] Labelbox brought in dozens of Fortune
[00:28:40] 500 sales people to build a bunch of
[00:28:42] different RL environments. They created
[00:28:44] thousands of scenarios where the sales
[00:28:46] agent had to engage with the potential
[00:28:48] customer, which was roleplayed by a
[00:28:49] second AI. Limblebox made sure that this
[00:28:52] customer AI had a few different
[00:28:53] personas. Because when you cold call,
[00:28:55] you have no idea who's going to be on
[00:28:56] the other end. You need to be able to
[00:28:58] deal with a whole range of
[00:28:59] possibilities. Limblebox's sales experts
[00:29:02] monitored these conversations turn by
[00:29:03] [music] turn, tweaking the role
[00:29:04] playinging agent to ensure it did the
[00:29:06] kinds of things an actual customer would
[00:29:08] do. Label Box could iterate faster than
[00:29:10] anybody else in the industry. This is
[00:29:11] super important because RL is an
[00:29:13] empirical science. [music] It's not a
[00:29:14] solve problem. Labelbox has a bunch of
[00:29:16] tools for monitoring agent performance
[00:29:18] in real time. This lets their experts
[00:29:20] keep coming up with tasks so that the
[00:29:22] model stays in the right distribution of
[00:29:23] difficulty and [music] gets the optimal
[00:29:25] reward signal during training. Label box
[00:29:27] can do this sort of thing in almost
[00:29:28] every domain. They've got headphone
[00:29:30] managers, radiologists, even airline
[00:29:32] pilots. So, whatever you're working on,
[00:29:34] Labelbox [music]
[00:29:35] can help. Learn more at
[00:29:37] labelbox.com/vorcash.
[00:29:43] Coming back to concrete predictions
[00:29:43] because I think because there's so many
[00:29:45] different things to dis ambiguate, it
[00:29:47] can be easy to talk past each other when
[00:29:49] we're talking about capabilities. So,
[00:29:50] for example, when I interviewed 3 years
[00:29:52] ago, I asked her a prediction about what
[00:29:54] should we expect 3 years from now. I
[00:29:56] think you were right. So you said we
[00:29:59] should expect systems which if you talk
[00:30:00] to them for the course of an hour it's
[00:30:02] hard to tell them apart from a generally
[00:30:04] well educated human. Yes.
[00:30:05] >> I think you were right about that and I
[00:30:07] think spiritually I feel unsatisfied
[00:30:09] because my internal expectation was was
[00:30:12] that such a system could automate large
[00:30:14] parts of white collar work and so it
[00:30:16] might be more productive to talk about
[00:30:17] the actual end capabilities. You want
[00:30:19] such a system.
[00:30:20] >> So so I will I will I will basically
[00:30:22] tell you what what you know where where
[00:30:25] I think we are. So but let me let me ask
[00:30:26] it in a very specific question so that
[00:30:28] we can figure out exactly what kinds of
[00:30:30] capabilities we should expect soon. So
[00:30:32] maybe I'll ask about it in the context
[00:30:33] of a job I understand well not because
[00:30:35] it's the most relevant job but um just
[00:30:38] because I can evaluate the claims about
[00:30:39] it. Um take video editors right I have
[00:30:42] video editors and part of their invol
[00:30:44] job involves learning about our
[00:30:47] audience's preferences learning about my
[00:30:48] preferences and tastes and the different
[00:30:49] trade-offs we have and how just over the
[00:30:51] course of many months building up this
[00:30:53] understanding of context. And so the
[00:30:55] skill and ability they have six months
[00:30:57] into the job, a model that can pick up
[00:30:59] that skill on the job on the fly. When
[00:31:01] should we be expect such an AI system?
[00:31:03] Yeah. So I guess what you're talking
[00:31:05] about is like you know we've we're we're
[00:31:06] doing this interview for 3 hours and
[00:31:08] then like you know someone's going to
[00:31:10] come in, someone's going to edit it,
[00:31:11] they're going to be like oh you know you
[00:31:14] know I don't know Dario like you know
[00:31:15] scratched his head and you know we could
[00:31:17] we could edit that out and you magnify
[00:31:19] that. there was this like long there was
[00:31:21] this like long discussion that like is
[00:31:23] less interesting to people and then then
[00:31:25] you know then there's other thing that's
[00:31:26] like more interesting to people so you
[00:31:28] know let's let's let's kind of make this
[00:31:30] this edit so you know I think the
[00:31:32] country of geniuses in a data center w
[00:31:34] will be able to do that the the way it
[00:31:36] will be able to do that is you know it
[00:31:38] will have general control of a computer
[00:31:40] screen right like you know and and and
[00:31:41] you'll be able to feed this in and it'll
[00:31:43] be able to also use the computer screen
[00:31:45] to like go on the web look at all your
[00:31:47] previous look at all your previous
[00:31:49] interviews like look at what people are
[00:31:51] saying on Twitter in response to your
[00:31:52] interviews like talk to you ask you
[00:31:55] questions talk to your staff look at the
[00:31:57] history of kind of edits edits that you
[00:31:59] did and from that like do the job um so
[00:32:02] I think that's dependent on several
[00:32:04] things one that's dependent and and and
[00:32:06] and I think this is one of the things
[00:32:07] that's actually blocking deployment um
[00:32:10] getting to the point on computer use
[00:32:12] where the models are really masters at
[00:32:14] using the computer right and you know
[00:32:16] we've seen this climb in in benchmarks
[00:32:18] and benchmarks are always you know
[00:32:19] imperfect measures but like you know OS
[00:32:22] world is you know went from you know
[00:32:24] like 5% a you know like uh I think when
[00:32:26] we first re released you know uh uh
[00:32:29] computer use like a a year and a quarter
[00:32:32] ago it was like maybe 15% I don't
[00:32:34] remember exactly but we've climbed from
[00:32:36] that to like 65 or 70%. Um and and you
[00:32:40] know there may be harder measures as
[00:32:41] well but but I think computer use has to
[00:32:44] pass a point of reliability. Can I just
[00:32:46] ask to follow up on that before you move
[00:32:48] to the next point? Um I often for years
[00:32:50] I've been trying to build different
[00:32:51] internal LLM tools for myself and I
[00:32:54] often I have these text in text out
[00:32:57] tasks which should be dead center in the
[00:32:59] repertoire of these models and yet I
[00:33:01] still hire humans to do them just
[00:33:03] because it's if it's something like make
[00:33:05] identify what the best clips would be in
[00:33:07] this transcript and maybe they'll do
[00:33:08] like a seven out of 10 job at them but
[00:33:10] there's not this ongoing way I can
[00:33:12] engage with them to help them get better
[00:33:13] at the job the way I could with a human
[00:33:15] employee and so that missing ability
[00:33:17] even if you saw computer use would still
[00:33:20] block my ability to like offload an
[00:33:22] actual job to them.
[00:33:23] >> Again, there's there's this gets back to
[00:33:25] what to to kind to kind of what we were
[00:33:27] talking about before with learning on
[00:33:29] the job where it's it's very
[00:33:30] interesting. You know, I think I think
[00:33:32] with the coding agents like I don't
[00:33:34] think people would say that learning on
[00:33:36] the job is what is what is you know
[00:33:38] preventing the coding agents from like
[00:33:40] you know doing everything end to end
[00:33:43] like they keep they keep getting better.
[00:33:45] We have engineers at Enthropic who like
[00:33:47] don't write any code. And when I look at
[00:33:50] the productivity to your to your
[00:33:51] previous question, you know, we have
[00:33:53] folks who say this this GPU kernel, this
[00:33:56] chip, I used to write it myself. I just
[00:33:58] have Claude do it. And so there's this
[00:34:00] there's this enormous improvement in
[00:34:02] productivity. And I don't know like when
[00:34:04] I see Claude code like familiarity with
[00:34:08] the code base or like it you know or or
[00:34:11] a feeling that the model hasn't worked
[00:34:13] at the company for for a year that's not
[00:34:16] high up on the list of complaints I see.
[00:34:18] And so I think what I'm saying is we're
[00:34:20] we're like we're kind of taking a
[00:34:21] different path. Don't don't you think
[00:34:22] with coding that's because there is an
[00:34:24] external scaffold of memory which exists
[00:34:26] instantiated in the codebase which I
[00:34:29] don't know how many other jobs have
[00:34:30] coding made fast progress precisely
[00:34:33] because it has this unique um advantage
[00:34:35] that other economic activity doesn't
[00:34:37] >> but but when you say that what you're
[00:34:39] what you're implying is that by reading
[00:34:42] the code base into the context I have
[00:34:45] everything that the human needed to
[00:34:46] learn on the job. So that would be an
[00:34:49] example of whether it's written or not,
[00:34:53] whether it's available or not, a case
[00:34:55] where everything you needed to know, you
[00:34:57] got from the context window, right? And
[00:35:00] that and that what we think of as
[00:35:01] learning like, oh man, I started this
[00:35:03] job, it's going to take me 6 months to
[00:35:04] understand the codebase, the model just
[00:35:06] did it in the context.
[00:35:07] >> Yeah. I honestly don't know how to think
[00:35:09] about this because there there are
[00:35:11] people who qualitatively report what
[00:35:13] you're saying. Um there was a meter
[00:35:15] study I'm sure you saw last year where
[00:35:17] they
[00:35:18] >> had experienced developers try to close
[00:35:23] uh pull requests in repositories that
[00:35:25] they were familiar with and those
[00:35:27] developers reported an uplift. They they
[00:35:29] reported that they felt more productive
[00:35:30] with the use of these models but in fact
[00:35:32] if you look at their output and how much
[00:35:33] was actually merged back in there's a
[00:35:35] 20% downlift. They were less productive
[00:35:37] as a result of using these models. And
[00:35:38] so I'm trying to square the qualitative
[00:35:40] feeling that people feel with these
[00:35:41] models versus um one in a macro level
[00:35:44] where are all these where is this like
[00:35:45] renaissance of software and two when
[00:35:47] people do these independent evaluations
[00:35:49] why are we not seeing the creative
[00:35:52] benefits that we would expect
[00:35:53] >> within anthropic this is just really
[00:35:55] unambiguous right we're under an
[00:35:57] incredible amount of commercial pressure
[00:35:59] and make it even hard harder for
[00:36:01] ourselves because we have all this
[00:36:02] safety stuff we do that I think we do
[00:36:04] more than than than other companies so
[00:36:06] like the the the pressure to survive
[00:36:09] economically while also keeping our
[00:36:12] values is is just incredible, right?
[00:36:14] We're trying to keep this 10x revenue
[00:36:17] curve going. There's like there is zero
[00:36:19] time for There is zero time
[00:36:22] for feeling like we're productive when
[00:36:24] we're not. Like these tools make us a
[00:36:28] lot more productive. Like why why do you
[00:36:31] think we're concerned about competitors
[00:36:33] using the tools? because we think we're
[00:36:34] ahead of the competitors and like we
[00:36:37] don't we don't want to accel we we we we
[00:36:39] wouldn't be going through all this
[00:36:41] trouble if this was secretly reducing
[00:36:45] reducing our productivity like we see
[00:36:47] the end productivity every few months in
[00:36:50] the form of model launches like there's
[00:36:52] no kidding yourself about this like the
[00:36:54] models make you more productive
[00:36:56] >> um one that is people feeling like
[00:36:59] they're more productive is qualitatively
[00:37:01] predicted by studies like this but two
[00:37:03] if I Look at the end output. Obviously,
[00:37:04] you guys are making fast progress. But
[00:37:07] the fact, you know, the the the idea was
[00:37:09] supposed to be with recursive
[00:37:11] self-improvement is that you make a
[00:37:12] better AI, the AI helps you build a
[00:37:14] better next AI, etc., etc. And what I
[00:37:16] see instead, if I look at the you open
[00:37:19] AI, deep mind, is that people are just
[00:37:21] shifting around the podium every few
[00:37:22] months. And maybe you think that stops
[00:37:23] because you you won or whatever, but um
[00:37:26] but why why are we not seeing the person
[00:37:28] with the best coding model have this
[00:37:31] lasting advantage if in fact there are
[00:37:33] these enormous productivity gains from
[00:37:35] the last model?
[00:37:36] >> So no, no, no. I I I mean I mean I mean
[00:37:38] I think it's all like my my model of the
[00:37:40] situation is there's there's an
[00:37:43] advantage that's gradually growing. Like
[00:37:45] I would say right now the coding models
[00:37:48] give maybe I don't know a a like 15
[00:37:53] maybe 20% total factor speed up like
[00:37:55] that's my view. Um uh and 6 months ago
[00:37:58] it was maybe 5%. And so and so it didn't
[00:38:01] matter like 5% doesn't register. It's
[00:38:04] now just getting to the point where it's
[00:38:05] like one of several factors that that
[00:38:08] kind of matters and and that's gonna
[00:38:10] that's going to keep speeding up. And so
[00:38:12] I think 6 months ago like you know there
[00:38:15] were several there were several
[00:38:16] companies that were at roughly the same
[00:38:18] point because uh you know this this
[00:38:21] wasn't uh this wasn't a notable factor
[00:38:23] but I think it's starting to speed up
[00:38:25] more and more. I you know I I would I
[00:38:27] would also say there are multiple
[00:38:28] companies that you know write models
[00:38:30] that are used for code and you know
[00:38:32] we're not perfectly good at you know
[00:38:34] preventing some of these other companies
[00:38:35] from from from using from from from kind
[00:38:38] of using our models internally. Um, so,
[00:38:41] uh, you know, I think I think everything
[00:38:43] we're kind kind of everything we're
[00:38:45] seeing is consistent with this kind of,
[00:38:47] um, this kind of snowball model where
[00:38:49] where, you know, there's no hard. Again,
[00:38:52] my my my my theme in all of this is like
[00:38:56] all of this is soft takeoff, like soft
[00:38:59] smooth exponentials, although the
[00:39:01] exponentials are relatively steep. And
[00:39:03] so and so we're seeing this snowball
[00:39:04] gather momentum where it's like 10% 20%
[00:39:08] 25% you know for 40% and as you go yeah
[00:39:12] AMD doll's law you have to get all the
[00:39:13] like things that are preventing you from
[00:39:15] from closing the loop out of the way but
[00:39:17] like this is one of the biggest
[00:39:19] priorities within anthropic. Um
[00:39:22] stepping back I think before in the
[00:39:24] stack we were talking about um well when
[00:39:27] do we get this on the job learning and
[00:39:29] it seems like the coding the point you
[00:39:31] were making the coding thing is we
[00:39:32] actually don't need on the job learning
[00:39:34] uh that you can have tremendous
[00:39:35] productivity improvements you can have
[00:39:37] potentially trillions of dollars of
[00:39:38] revenue for AI companies without this
[00:39:40] basic human abil maybe that's not your
[00:39:42] claim you should clarify um but without
[00:39:44] this basic human ability to learn on the
[00:39:47] job but I just look at like in in in
[00:39:49] most domain of economic activity. People
[00:39:51] say, "I hired somebody. They weren't
[00:39:53] that useful for the first few months and
[00:39:54] then over time they built up the context
[00:39:57] understanding. It's actually hard to
[00:39:58] define what we're talking about here,
[00:40:00] but they they got something and then now
[00:40:02] now they're they're a power horse and
[00:40:03] they're so valuable to us." And if AI
[00:40:06] doesn't develop this ability to learn on
[00:40:08] the fly, I'm not I'm a bit skeptical
[00:40:10] that we're going to see huge changes to
[00:40:12] the world without
[00:40:14] >> So I think I think I think two things
[00:40:15] here, right? There's the state of the
[00:40:18] technology right now um which is again
[00:40:20] we have these two stages. We have the
[00:40:22] pre-training and RL stage where you
[00:40:25] throw you throw a bunch of data and
[00:40:27] tasks into the models and then they
[00:40:29] generalize. So it's like learning but
[00:40:31] it's like learning from more data and
[00:40:33] and not you know not learning over kind
[00:40:35] of one human or one model's lifetime. So
[00:40:38] again this is situated between evolution
[00:40:41] and and and human learning. But once you
[00:40:43] learn all those skills, you have them.
[00:40:45] And and just like with pre-training,
[00:40:47] just how the models know more, you know,
[00:40:50] if if I look at a pre-trained model, you
[00:40:52] know, it knows more about the history of
[00:40:54] samurai in Japan than I do. It knows
[00:40:56] more about baseball than I do. It knows,
[00:40:59] you know, it knows more about, you know,
[00:41:02] lowass filters and electronics and, you
[00:41:04] know, all all of these things. Its
[00:41:06] knowledge is way broader than mine. So I
[00:41:09] think I think even even just that um you
[00:41:12] know may get us to the point where the
[00:41:13] models are better at you know kind of
[00:41:16] better at everything and then we also
[00:41:18] have again just with scaling the kind of
[00:41:20] existing setup we have the in context
[00:41:23] learning which I would describe as kind
[00:41:25] of like human on the job learning but
[00:41:27] like a little weaker and a little short
[00:41:29] term like you look at in context
[00:41:31] learning the you give the model a bunch
[00:41:33] of examples it does get it there's real
[00:41:35] learning that happens in context and
[00:41:37] like a million tokens is a lot. That's
[00:41:40] that's you know that can be days of
[00:41:41] human learning right you know if you
[00:41:43] think about the model you know you know
[00:41:45] kind of read reading reading a million
[00:41:47] words you know you know it takes me how
[00:41:49] long would it take me to read a million
[00:41:51] I mean you know like days or weeks at
[00:41:53] least um uh so you have these two things
[00:41:56] and and I think these two these two
[00:41:58] things within the existing paradigm may
[00:42:00] just be enough to get you the country of
[00:42:01] geniuses in the data center I don't know
[00:42:03] for sure but I think they're going to
[00:42:05] get you a large fraction of it there may
[00:42:07] be gaps but I I certainly think just as
[00:42:11] things are this I believe is enough to
[00:42:13] generate trillions of dollars of
[00:42:14] revenue. That's one that's all one. Two
[00:42:17] is this idea of continual learning. This
[00:42:20] idea of a single model learning on the
[00:42:23] job. Um I think we're working on that
[00:42:25] too and I think there's a good chance
[00:42:28] that in the next year or two we also
[00:42:30] make we also solve that. Um I I again I
[00:42:34] I I I you know I think you get most of
[00:42:36] the way there without it. I think the
[00:42:39] trillions of dollars of of you know the
[00:42:42] the I think the trillions of dollars a
[00:42:44] year market maybe all the national
[00:42:46] security implications and the safety
[00:42:47] implications that I wrote about in
[00:42:49] adolescence of technology can happen
[00:42:51] without it. But I I I also think we and
[00:42:55] I imagine others are working on it. And
[00:42:57] I think there's a good chance that that
[00:43:00] you know that we get there within the
[00:43:01] next year or two. There are a bunch of
[00:43:03] ideas. I won't go into all of them in
[00:43:05] detail, but um you know, one is just
[00:43:07] make the context longer. There's there's
[00:43:10] nothing preventing longer context from
[00:43:11] working. You just have to train at
[00:43:13] longer context and then learn to to
[00:43:15] serve them at inference. And both of
[00:43:17] those are engineering problems that we
[00:43:18] are working on and that I would assume
[00:43:20] others are working on as well. Yeah. So
[00:43:22] this context length increase, it seemed
[00:43:24] like there was a period from 2020 to
[00:43:25] 2023 where from GPD3 to GP4 Turbo, there
[00:43:28] was an increase from like 2,000 context
[00:43:29] lines to 128K. I feel like for the next
[00:43:33] for the twoish years since then, we've
[00:43:34] been in the sameish ballpark. Yeah. And
[00:43:37] when model context lines get much longer
[00:43:39] than that, people report qualitative
[00:43:41] degradation in the ability of the model
[00:43:44] to consider that full context. Um, so
[00:43:47] I'm curious what you're internally
[00:43:48] seeing that makes you think like, oh, 10
[00:43:50] million context, 100 million contexts to
[00:43:51] get human like six months learning
[00:43:53] billion.
[00:43:54] >> This isn't a research problem. This is a
[00:43:56] this is an engineering and inference
[00:43:57] problem, right? If you want to serve
[00:43:59] long context, you have to like store
[00:44:01] your entire KV cache. You have to, you
[00:44:04] know, um, uh, you know, it's it's it's
[00:44:06] it's difficult to store all the memory
[00:44:08] in the GPUs to juggle the memory around.
[00:44:11] I don't even know the detail, you know,
[00:44:13] at this point. this is at a level of
[00:44:14] detail that that that that I'm no longer
[00:44:16] able to follow although you know I I
[00:44:18] knew it in the GPD3 era of like you know
[00:44:20] these are the weights these are the
[00:44:22] activations you have to store um uh but
[00:44:24] you know you know these days the whole
[00:44:26] thing has flipped because we have models
[00:44:28] and and and kind of all of that but um
[00:44:31] uh and and this degradation you're
[00:44:33] talking about like again without getting
[00:44:35] too specific like a question I would ask
[00:44:37] is like there's two things there's the
[00:44:39] context length you train at and there's
[00:44:41] a context length that you serve at if If
[00:44:43] you train at a small context length and
[00:44:45] then try to serve at a long context
[00:44:47] length like maybe you get these
[00:44:48] degradations.
[00:44:49] >> It's better than nothing. You might
[00:44:50] still offer it but you get these
[00:44:51] degradations and maybe it's harder to
[00:44:53] train at a long context length. Yeah.
[00:44:55] So, you know, there's there's a lot I I
[00:44:56] I want to at the same time ask about
[00:44:59] like maybe some rabbit holes of like
[00:45:01] well wouldn't you expect that if you had
[00:45:03] to train on longer context length that
[00:45:04] would mean that um you're able to get
[00:45:07] sort of like less samples in for the
[00:45:09] same amount of compute. But before maybe
[00:45:11] it's not worth diving deep on that. I I
[00:45:13] want to get an answer to the bigger
[00:45:14] picture question, which is like, okay,
[00:45:16] so
[00:45:18] um I don't feel a preference for a human
[00:45:21] editor that's been working for me for 6
[00:45:23] months versus an AI that's been working
[00:45:25] with me for 6 months. What year do you
[00:45:28] predict that that will be the case?
[00:45:31] >> I my I mean, you know, my guess for that
[00:45:34] is, you know, there's there's a lot of
[00:45:36] problems that are basically like we can
[00:45:37] do this when we have the country of
[00:45:38] geniuses in a data center. Um, and so,
[00:45:41] you know, my my my my picture for that
[00:45:43] is, you know, again, if you if you if
[00:45:46] you if you know, if you made me guess,
[00:45:47] it's like one to two years, maybe one to
[00:45:49] three years. It's really hard to tell. I
[00:45:51] have a I have a strong view 99 95% that
[00:45:55] like all this will happen in 10 years.
[00:45:57] Like that's I think that's just a super
[00:45:58] safe bet. And then I have a hunch this
[00:46:01] is more like a 50/50 thing that it's
[00:46:04] going to be more like 1 to two, maybe
[00:46:05] more like 1 to three.
[00:46:06] >> So 1 to three years. country of genius
[00:46:08] says um and then the slightly less
[00:46:11] economically valuable task of editing
[00:46:12] videos [laughter]
[00:46:14] I
[00:46:14] >> it seems pretty economically valuable
[00:46:16] let me tell you it's just there are a
[00:46:17] lot of use cases like that right there
[00:46:19] are a lot of similar ones so you're
[00:46:21] predicting that within 1 to 3 years um
[00:46:23] and in gerally enthropic has predicted
[00:46:25] that by late 26 early 27 we will have AI
[00:46:28] systems that are quote um have the
[00:46:31] ability to navigate interfaces available
[00:46:32] to humans doing digital work today
[00:46:34] intellectual capabilities matching or
[00:46:35] exceeding that of Nobel prize winners
[00:46:37] and the ability to interface with the
[00:46:39] physical world. And then you gave an
[00:46:41] interview two months ago with Dealbook
[00:46:43] where you were emphasizing your um your
[00:46:46] company's more responsible comput
[00:46:48] scaling as compared to your competitors.
[00:46:50] And I'm trying to square these two views
[00:46:52] where if you really believe that we're
[00:46:54] going to have a country of geniuses, you
[00:46:56] you want as big a data center as you can
[00:46:58] get, there's no reason to slow down. The
[00:47:00] TAM of a Nobel Prize winner that is
[00:47:03] actually can do everything a Nobel Prize
[00:47:04] winner can do is like trillions of
[00:47:06] dollars. And so I'm trying to square
[00:47:08] this conservatism
[00:47:10] uh which seems rational if you have more
[00:47:12] moderate timelines with your stated
[00:47:14] views about AI progress.
[00:47:16] >> Yeah. So so it actually all fits
[00:47:17] together and and we go back to this fast
[00:47:20] but not infinitely fast diffusion. So
[00:47:22] like let's say that we're making
[00:47:24] progress at this rate. Um you know the
[00:47:27] the the technology is making progress
[00:47:28] this fast. Again, I have, you know, very
[00:47:31] high conviction that like it's going,
[00:47:34] you know, the the, you know, we're going
[00:47:37] to get there within within a few years.
[00:47:39] I have a hunch that we're going to get
[00:47:40] there within a year or two. So, a little
[00:47:42] uncertainty on the technical side, but
[00:47:44] like, you know, pretty pretty strong
[00:47:46] confidence that it won't be off by much.
[00:47:48] What I'm less certain about is again the
[00:47:51] economic diffusion side. Like I really
[00:47:55] do believe that we could have models
[00:47:57] that are a country of geniuses country
[00:48:00] of geniuses in a data center in one to
[00:48:03] two years. One question is how many
[00:48:05] years after that do the trillions in you
[00:48:08] know do do the do the trillions in
[00:48:10] revenue start rolling in? Um I don't
[00:48:15] think it's guaranteed that it's going to
[00:48:17] be immediate. Um, you know, I think it
[00:48:19] could be um one year, it could be two
[00:48:23] years, I could even stretch it to five
[00:48:27] years, although I'm like I'm skeptical
[00:48:29] of that. And so we have this uncertainty
[00:48:32] which is even if the technology goes as
[00:48:35] fast as I suspect that it will, we we
[00:48:38] don't know exactly how fast it's going
[00:48:40] to drive revenue. We we know it's
[00:48:42] coming, but with the way you buy these
[00:48:45] data centers, if you're off by a couple
[00:48:47] years, that can be ruinous. It is just
[00:48:49] like how I wrote, you know, in machines
[00:48:51] of loving grace, I said, look, I think
[00:48:53] we might get this powerful AI, this
[00:48:55] country of genius in the data center.
[00:48:56] That description you gave comes from the
[00:48:58] machines of loving grace. I said, we'll
[00:49:00] get that 2026, maybe 2027. Again, that
[00:49:03] is that is my hunch. Wouldn't be
[00:49:04] surprised if I'm off by a year or two,
[00:49:05] but like that is my hunch. Let's say
[00:49:08] that happens. That's the starting gun.
[00:49:10] How long does it take to cure all the
[00:49:12] diseases, right? That's that's one of
[00:49:13] the ways that like drives a huge amount
[00:49:15] of of of of economic value, right? Like
[00:49:18] you cure you cure every disease. You
[00:49:20] know, there's a question of how much of
[00:49:22] that goes to the pharmaceutical company
[00:49:23] to the AI company, but there's an
[00:49:24] enormous consumer surplus because
[00:49:26] everyone, you know, assuming we can get
[00:49:28] access for everyone, which I care about
[00:49:30] greatly. We, you know, we we cure all of
[00:49:32] these diseases. How long does it take?
[00:49:34] You have to do the biological discovery.
[00:49:36] you have to, you know, go you have to,
[00:49:38] you know, manufacture the new drug. You
[00:49:41] have to, you know, go through the
[00:49:42] regulatory process. I mean, we saw this
[00:49:43] with like vaccines and COVID, right?
[00:49:45] Like it there's just this we we got the
[00:49:48] vaccine out to everyone, but it took a
[00:49:50] year and a half, right? And and so my
[00:49:52] question is, how long does it take to
[00:49:54] get the cure for everything, which AI is
[00:49:57] the genius that can in theory invent out
[00:50:00] to everyone? How long from when that AI
[00:50:02] first exists in the lab to when diseases
[00:50:05] have actually been cured for everyone
[00:50:08] right in in you know we've had a polio
[00:50:10] vaccine for 50 years we're still trying
[00:50:13] to eradicate it in the most remote
[00:50:15] corners of Africa and you know the
[00:50:17] Gateson nation is trying as hard as they
[00:50:18] can others are trying as hard as they
[00:50:20] can but you know that's difficult again
[00:50:23] I you know I don't expect most of the
[00:50:24] economic diffusion to be as difficult as
[00:50:26] that right that's like the most
[00:50:28] difficult case but but there's a There's
[00:50:31] a real dilemma here and and where I've
[00:50:32] settled on it is it will be it will be a
[00:50:35] it will be faster than anything we've
[00:50:38] seen in the world but it still has its
[00:50:41] limits and and so then when we go to
[00:50:44] buying data centers you know you again
[00:50:47] again again the curve I'm looking at is
[00:50:49] okay we you know we've had a 10x a year
[00:50:52] increase every year so beginning of this
[00:50:55] year we're looking at 10 billion in in
[00:50:57] in annual in you know rate of annual ize
[00:51:00] revenue at the beginning of the year. We
[00:51:02] have to decide how much compute to buy.
[00:51:04] Um
[00:51:06] and you know it takes a year or two to
[00:51:10] actually build out the data centers to
[00:51:11] reserve the data centers. So basically
[00:51:13] I'm saying like in uh 2027 how much
[00:51:17] compute do I get? Well I could assume um
[00:51:21] uh that uh the uh revenue will continue
[00:51:25] growing 10x a year. So it'll be uh one
[00:51:28] uh one uh 100 billion at the end of 2026
[00:51:32] and 1 trillion at the end of 2027. And
[00:51:35] so I could buy a trillion dollar
[00:51:37] actually would be like5 trillion dollars
[00:51:39] of compute because it would be a
[00:51:40] trillion dollar a year for for five
[00:51:42] years, right? I could buy a trillion
[00:51:44] dollars of compute that starts at the
[00:51:46] end of 2027. And if my if my revenue is
[00:51:50] not a trillion dollars, if it's even
[00:51:53] 800 billion, there's no force on earth,
[00:51:56] there's there's no hedge on earth that
[00:51:58] could stop me from going bankrupt if I
[00:52:00] if I buy that much compute. And and so
[00:52:03] even though a part of my brain wonders
[00:52:04] if it's going to keep growing 10x, I
[00:52:07] can't buy a trillion dollars a year of
[00:52:09] compute in in in in in in in
[00:52:13] 2027. If I'm just off by a year in that
[00:52:16] rate of growth, or if the the growth
[00:52:18] rate is 5x a year instead of 10x a year,
[00:52:21] then then you know that you go bankrupt.
[00:52:23] Um and and and so you end up in a world
[00:52:27] where you know you're supporting
[00:52:29] hundreds of billions not trillions and
[00:52:32] you accept you accept some risk that
[00:52:35] there's so much demand that you can't
[00:52:37] support the revenue and you accept still
[00:52:40] some risk that you know you got it wrong
[00:52:42] and it still slow and so when I talked
[00:52:44] about behaving responsibly what I meant
[00:52:46] actually was not the absolute amount
[00:52:49] that that actually was not um you know I
[00:52:52] think it is true we're spending somewhat
[00:52:53] less than some of the other players.
[00:52:55] It's actually the other things like have
[00:52:58] we been thoughtful about it or are we
[00:53:00] yoloing and saying, "Oh, we're going to
[00:53:02] do $100 billion here, hundred billion
[00:53:04] dollars there." I kind of get the
[00:53:06] impression that, you know, some of the
[00:53:08] other companies have not written down
[00:53:09] the spreadsheet that they don't really
[00:53:11] understand the risk they're taking.
[00:53:12] They're just kind of doing stuff because
[00:53:14] it sounds cool. Um uh and and we've
[00:53:17] thought carefully about it, right? We're
[00:53:19] an enterprise business. Therefore, you
[00:53:21] know, we can rely more on revenue. It's
[00:53:24] less fickle than consumer. We have
[00:53:26] better margins, which is the buffer
[00:53:28] between buying too much and buying too
[00:53:30] little. And so, I think we bought an
[00:53:32] amount that allows us to capture pretty
[00:53:35] strong upside worlds. It won't capture
[00:53:38] the full 10x a year. Um, and things
[00:53:40] would have to go pretty badly for us to
[00:53:42] be for us to be in financial trouble.
[00:53:44] So, I think we've thought carefully and
[00:53:46] we've made that balance. And and that's
[00:53:48] what I mean when I say that we're being
[00:53:49] responsible. Okay. So, it seems like um
[00:53:52] it's possible that we're we actually
[00:53:54] just have different definitions of the
[00:53:55] country of a genius in a data center
[00:53:56] because when I think of like actual
[00:53:59] human geniuses, an actual country of
[00:54:00] human geniuses in a data center, I'm
[00:54:02] like
[00:54:04] I would happily buy $5 trillion worth of
[00:54:06] compute to run actual country of human
[00:54:08] genius in a data center. So, let's say
[00:54:09] JP Morgan or Madna or whatever doesn't
[00:54:11] want to use them. Also, I've got a
[00:54:13] country of geniuses. they they'll start
[00:54:15] their own company and if like they they
[00:54:16] can't start their own company and
[00:54:17] they're bottlenecked by clinical trials.
[00:54:18] It is worth stating with clinical trials
[00:54:20] like most clinical trials fail because
[00:54:22] the drug doesn't work. There's not
[00:54:23] efficacy, right?
[00:54:24] >> And I make exactly that point in in
[00:54:26] machines of love and grace. I say the
[00:54:28] clinical trials are going to go much
[00:54:29] faster than we're used to, but not not
[00:54:31] instant not infinitely fast.
[00:54:33] >> And then suppose it takes a year to for
[00:54:35] the clinical trials to work out so that
[00:54:37] you're getting revenue from that and you
[00:54:38] can make more drugs. Okay. Hey, well,
[00:54:39] you've got a country of geniuses and
[00:54:41] you're an AI lab and you have you could
[00:54:44] use uh many more AI researchers. Um, you
[00:54:47] also think that there's these like
[00:54:49] self-reinforcing gains from, you know,
[00:54:51] smart people working on AI tech. So,
[00:54:54] like, okay, you can have the right you
[00:54:55] can have the data center working on like
[00:54:56] AI progress.
[00:54:57] >> Is there more gains from buying
[00:55:00] >> like substantially more gains from
[00:55:02] buying a trillion dollars a year of
[00:55:04] compute versus $300 billion a year of
[00:55:07] compute? If your competitor is buying a
[00:55:08] trillion, yes, there is.
[00:55:09] >> Well, no, there's some gain, but then
[00:55:11] but again, there's this chance that they
[00:55:13] go bankrupt before,
[00:55:16] you know, be again, if you're off by
[00:55:18] only a year, you destroy yourselves.
[00:55:21] That's the That's the balance. We're
[00:55:23] buying a lot. We're buying a hell of a
[00:55:25] lot. Like, we're not we're you know,
[00:55:27] we're buying an amount that's comparable
[00:55:30] to that that, you know, the the the the
[00:55:32] biggest players in the game are buying.
[00:55:34] Um but but if you're asking me why why
[00:55:37] haven't we signed you know 10 10
[00:55:40] trillion of compute starting in starting
[00:55:42] in mid 2027 first of all it can't be
[00:55:44] produced there isn't that much in the
[00:55:45] world um uh but but second um what if
[00:55:49] the country of geniuses comes but it
[00:55:51] comes in mid 2028 instead of mid2027 you
[00:55:54] go bankrupt. So if your projection is 1
[00:55:58] to 3 years, it seems like you should
[00:56:00] want $10 trillion of compute by um 2029
[00:56:03] 2020 maybe 2020 latest
[00:56:06] >> like I mean you know you are like it
[00:56:09] seems like even in your the longest
[00:56:10] version of the timelines you state the
[00:56:12] compute you are ramping up to build
[00:56:14] doesn't seem
[00:56:15] >> in accordance what what makes you think
[00:56:17] that
[00:56:18] >> well as you said you would want the 10
[00:56:19] trillion the human wages let's say are
[00:56:22] um on the order of 50 trillion a year
[00:56:24] >> if you look at so so I won't I won't
[00:56:25] talk about entropic in particular but if
[00:56:27] you talk about the industry like um the
[00:56:31] amount of compute the industry had you
[00:56:34] know the the the the amount of compute
[00:56:35] the industry is building this year is
[00:56:38] probably in the you know I don't know
[00:56:40] very low tens of you know call it 10 15
[00:56:43] gawatts next year I you know it goes up
[00:56:47] by roughly 3x a year so like next year's
[00:56:49] 30 or 40 gigawatts and um 2028 might be
[00:56:53] 100 202 might like three 300 gigawatts
[00:56:58] and like each gigawatt costs like um
[00:57:02] maybe 10 I mean I'm doing the math in my
[00:57:04] head but each gigawatt costs maybe 10
[00:57:06] billion you know order 10 to 15 billion
[00:57:09] a year so you know you kind of you you
[00:57:12] know you put that all together and
[00:57:13] you're getting about about what you
[00:57:15] described you're getting multiple
[00:57:16] trillions a year by 2028 or 2029 so
[00:57:18] you're you're getting exactly that
[00:57:20] you're getting you're getting exactly
[00:57:21] what you predict
[00:57:22] >> um that's for the industry
[00:57:24] >> that that's for the industry That's
[00:57:25] right. So suppose anthropics comput
[00:57:27] keeps 3xing a year and then by like 27
[00:57:29] you have uh or 27 28 you have 10 gawatt
[00:57:34] and like multiply that by as you say um
[00:57:37] 10 billion. So then it's like 100
[00:57:39] billion a year but then you were saying
[00:57:41] the TAM by 2028.
[00:57:43] >> I I don't want to give exact numbers for
[00:57:44] anthropic but but these numbers are too
[00:57:46] small. These numbers are too small.
[00:57:48] >> Okay. Interesting. I'm really proud that
[00:57:50] the puzzles I've worked on with Jane
[00:57:51] Street have resulted in them hiring a
[00:57:53] bunch of people for my audience. Well,
[00:57:55] they're still hiring and they just sent
[00:57:57] me another puzzle. For this one, they
[00:57:58] spent about 20,000 GPU hours training
[00:58:00] backd doors into three different
[00:58:02] language models. Each one has a hidden
[00:58:04] prompt that elicits completely different
[00:58:06] behavior. You just have to find the
[00:58:08] trigger. This is particularly cool
[00:58:09] because finding backd doorors is
[00:58:11] actually an open question in Frontier AI
[00:58:13] research. Enthropic actually released a
[00:58:15] couple of papers about sleep agents and
[00:58:16] they showed that you can build a simple
[00:58:18] classifier on the residual stream to
[00:58:21] detect when a back door is about to
[00:58:22] fire, [music] but they already knew what
[00:58:24] the triggers were because they built
[00:58:26] them. Here you don't. And it's not
[00:58:28] feasible to check the activations for
[00:58:30] all possible trigger [music] phrases.
[00:58:32] Unlike the other puzzles they made for
[00:58:33] this podcast, Jane Street isn't even
[00:58:35] sure this one is solvable, but they've
[00:58:36] set aside $50,000 for the [music] best
[00:58:39] attempts and write-ups. The puzzle's
[00:58:40] live at janestreet.com/themarcash
[00:58:44] and they're accepting submissions until
[00:58:45] April 1st. All right, back to Dario.
[00:58:48] You've told investors that you plan to
[00:58:50] be profitable starting 28 and this is
[00:58:53] the year where we're like potentially
[00:58:55] getting the country of geniuses at a
[00:58:56] data center and you know this is like
[00:58:59] going to now unlock all this uh progress
[00:59:02] and uh medicine and uh health and etc
[00:59:06] etc and new technologies. Wouldn't this
[00:59:08] be a particular exactly the time where
[00:59:10] you'd like want to reinvest in the
[00:59:12] business and build bigger countries so
[00:59:14] they can make more discoveries?
[00:59:15] >> So I mean profit profitability is this
[00:59:17] kind of like weird thing in this field.
[00:59:19] I I like like I don't think I I don't
[00:59:22] think in this field profitability is
[00:59:24] actually a measure of
[00:59:28] uh um you know kind of spending down
[00:59:32] versus investing in the business like
[00:59:33] let's let's just let's just take a model
[00:59:35] of this. I actually think profitability
[00:59:38] happens when you underestimated the
[00:59:40] amount of demand you were going to get
[00:59:41] and loss happens when you overestimated
[00:59:44] the amount of demand you were going to
[00:59:45] get. Um because you're buying the data
[00:59:47] centers ahead of time. So think about it
[00:59:49] this way. Um ideally you would like and
[00:59:52] again these are stylized facts. These
[00:59:53] numbers are not exact for I'm just
[00:59:55] trying to make a toy model here. Let's
[00:59:57] say half of your compute is for training
[00:59:59] and half of your compute is for
[01:00:00] inference. Um, and you know the
[01:00:02] inference has some gross margin that's
[01:00:04] like more than 50%. Um, and so what that
[01:00:07] means is that if you were in steady
[01:00:09] state, you build a data center, if you
[01:00:12] knew exactly exactly exactly the demand
[01:00:14] you were getting, you would um uh uh uh
[01:00:18] you know you would you would you you
[01:00:20] would you would get a certain amount of
[01:00:21] revenue. say, I don't know, uh, uh,
[01:00:23] let's say you pay $100 billion a year
[01:00:24] for compute and on $50 billion a year,
[01:00:27] you support $150 billion on of of of of
[01:00:31] revenue and the other 50 billion the
[01:00:33] other 50 billion are used for training.
[01:00:35] Um, so basically, you're profitable. You
[01:00:37] make you make you make $50 billion of
[01:00:39] profit. Those are the economics of the
[01:00:41] industry today or or sorry, not today,
[01:00:43] but like that's where we're where we're
[01:00:45] projecting forward in a year or two. The
[01:00:47] only thing that makes that not the case
[01:00:49] is if you get less demand than 50
[01:00:52] billion um then you have more than 50%
[01:00:56] of your your data center for research
[01:00:58] and you're not profitable. So you you
[01:01:00] know you train stronger models but
[01:01:01] you're like not profitable. Um if you uh
[01:01:05] get more demand than you thought then
[01:01:06] your research gets squeezed um but uh
[01:01:10] you know you're you're you're kind of
[01:01:12] able to support more inference and
[01:01:13] you're more profitable. So it's maybe
[01:01:16] I'm not explaining it well but but the
[01:01:17] thing I'm trying to say is you decide
[01:01:19] the amount of compute first and then you
[01:01:22] have some target desire of of inference
[01:01:24] versus versus training but that gets
[01:01:27] determined by demand. It doesn't get
[01:01:29] >> what I'm hearing is the reason you're
[01:01:30] predicting profit is that you are
[01:01:32] systematically underestimate uh
[01:01:34] underinvesting in compute right because
[01:01:36] if you actually
[01:01:37] >> No I'm saying I'm saying it's hard to
[01:01:38] predict. So, so these things about 2028
[01:01:41] and when it will happen, that's our
[01:01:43] that's our attempt to do the best we can
[01:01:45] with investors, all of this stuff is
[01:01:47] really uncertain because of the cone of
[01:01:49] uncertainty. Like we could be profitable
[01:01:51] in 2026 if the if the revenue grows fast
[01:01:54] enough and then and then um uh you know
[01:01:58] if we if we overestimate or
[01:02:00] underestimate the next year that could
[01:02:02] swing wildly. Like I I I what I'm trying
[01:02:04] to get at is you have a model in your
[01:02:06] head of like the the business invests
[01:02:09] invests invests invests gets scale and
[01:02:11] and and and kind of then becomes
[01:02:13] profitable. There's a single point at
[01:02:15] which things turn around. I don't think
[01:02:16] the economics of this industry work that
[01:02:18] way.
[01:02:19] >> I see. So if I'm understanding
[01:02:21] correctly, you're saying because of the
[01:02:23] discrepancy between the amount of
[01:02:24] compute we should have gotten and the
[01:02:26] amount of compute we got, we we were
[01:02:28] like sort of forced to make profit. But
[01:02:29] that that doesn't mean we're going to
[01:02:30] continue making profit. But we're going
[01:02:31] to like reinvest the money because well
[01:02:34] now AI has made so much progress and we
[01:02:35] want the bigger country of geniuses and
[01:02:37] so then back into uh revenue is high but
[01:02:41] losses are also high. If we if we
[01:02:43] predict if every year we predict exactly
[01:02:46] what the demand is going to be will be
[01:02:48] profitable every year because grow
[01:02:51] because spending spending 50% of your
[01:02:53] compute on on 50% of your compute on
[01:02:56] research roughly um plus a gross margin
[01:02:59] that's higher than 50%. And and correct
[01:03:02] demand prediction leads to profit.
[01:03:03] That's the prof that's that's the
[01:03:05] profitable business model that I think
[01:03:07] is kind of like there but like obsc
[01:03:10] obscured by these like building ahead
[01:03:12] and prediction errors. I
[01:03:13] >> I guess you're treating the 50% as a uh
[01:03:16] as a sort of like you know just like a
[01:03:18] given constant whereas you in fact if
[01:03:20] you if AI progress is fast and you can
[01:03:22] increase the progress by scaling up more
[01:03:24] you just have more than 50% and not make
[01:03:25] profit.
[01:03:25] >> Here's what I'll say. You might want to
[01:03:27] scale up it more. you might want to
[01:03:28] scale it up more, but but but you know,
[01:03:31] remember the log returns to scale,
[01:03:33] right? If if 70% would get you a very
[01:03:37] little bit of a smaller model through a
[01:03:39] factor of of 1.4x, right? like that
[01:03:42] extra $20 billion is is is is you know
[01:03:45] that each each dollar there is worth
[01:03:47] much less to you because because the log
[01:03:49] linear setup and so you might find that
[01:03:52] it's better to invest that that that
[01:03:54] that it's better to invest that $20
[01:03:56] billion in you know in in serving
[01:03:58] inference or in hiring engineers who are
[01:04:01] who who are kind of better who are who
[01:04:02] are kind of better who are kind of
[01:04:03] better at what they're doing. So the the
[01:04:05] reason I said 50% that's not that's not
[01:04:07] exactly our target. It's not exactly
[01:04:09] going to be 50%. It will probably vary
[01:04:11] vary over time. What what I'm saying is
[01:04:13] the the the the like log linear return
[01:04:16] what it leads to is you spend of order
[01:04:19] one fraction of the business, right?
[01:04:21] Like not 5% not 95%. And then it then
[01:04:27] you know then then then you get
[01:04:28] diminishing returns because of the
[01:04:29] because the walls that I'm like
[01:04:31] convincing Dario to like believe in AI
[01:04:33] progress or something but like uh okay
[01:04:35] you you don't invest in research because
[01:04:36] it has diminishing returns but you
[01:04:38] invest in the other things you mentioned
[01:04:39] >> again again we're talking about
[01:04:41] diminishing returns
[01:04:43] after you're spending 50 billion a year
[01:04:45] right like this is a point I'm sure you
[01:04:47] would make but like diminishing returns
[01:04:49] on a genius is could be quite high and
[01:04:52] more generally like what is profit put
[01:04:54] in a market economy profit is basically
[01:04:56] saying the other companies in the market
[01:04:59] can like do more things with this money
[01:05:00] that I
[01:05:01] >> yeah put aside entropic I'm just trying
[01:05:03] to like because I you know I don't want
[01:05:05] to give information about entropic is
[01:05:06] why I'm giving these stylized numbers
[01:05:08] but like let's just derive the
[01:05:10] equilibrium of the industry right I
[01:05:12] think the so so so why doesn't everyone
[01:05:15] spend 100% of their um uh you know 100%
[01:05:20] of their compute on training and not
[01:05:22] serve any customers right it's because
[01:05:24] if They didn't get any revenue. They
[01:05:25] couldn't raise money. They couldn't do
[01:05:26] comput deals. They couldn't buy more
[01:05:28] compute the next year. So, there's going
[01:05:29] to be an equilibrium where every every
[01:05:31] company spends less than 100% on on on
[01:05:35] on on training and certainly less than
[01:05:37] 100% on inference. It should be clear
[01:05:39] why you don't just serve the current
[01:05:41] models and and you know and and and
[01:05:43] never train another model because then
[01:05:45] you don't have any demand because you
[01:05:46] because you'll fall behind. So, there's
[01:05:48] some equilibrium. It's it's not going to
[01:05:50] be 10%, it's not going to be 90%. Let's
[01:05:53] just say as a stylized fact it's 50%.
[01:05:55] That's what I'm getting at. And and and
[01:05:57] I think we're going to be in a position
[01:05:59] where that equilibrium of how much you
[01:06:01] spend on training is less than the gross
[01:06:04] margins that that you're that that that
[01:06:06] you're able to get on compute. And so
[01:06:08] the the the the underlying economics are
[01:06:10] profitable. The problem is you have this
[01:06:13] this hellish demand prediction problem
[01:06:15] when you're when you're buying the next
[01:06:17] year of compute and you might guess
[01:06:19] under and be very profitable but have no
[01:06:22] compute for research or you might guess
[01:06:25] over and you know you're you're you're
[01:06:28] um uh you you are not profitable and you
[01:06:31] have all the compute compute for
[01:06:33] research in the world.
[01:06:34] >> Does does that make sense just as a
[01:06:36] dynamic model of the industry? May maybe
[01:06:38] stepping back I'm like uh I I I'm not
[01:06:41] saying I I think the country of genius
[01:06:43] is going to come in two years and
[01:06:44] therefore you should buy this compute.
[01:06:46] Um to me what you're saying the end
[01:06:49] conclusion you're arriving at makes a
[01:06:50] lot of sense but uh that's because like
[01:06:54] oh it seems like country geniuses is
[01:06:55] hard and there's a long way to go. And
[01:06:57] so the stepping back the thing I'm
[01:06:59] trying to get at is more like
[01:07:02] it seems like your worldview is
[01:07:03] compatible with somebody who says uh
[01:07:05] we're like 10 years away from a world in
[01:07:07] which like we're generating trillions of
[01:07:08] dollars.
[01:07:09] >> That's just that's just not my view.
[01:07:10] That is that is not my view. Like I I so
[01:07:13] so I'll like I'll like make another
[01:07:15] prediction. It is hard for me to see
[01:07:18] that that there won't be trillions of
[01:07:20] dollars in revenue before 2030. Um like
[01:07:23] uh I can I can construct a plausible
[01:07:25] world. It takes maybe three years. So
[01:07:28] that that you know that would be the end
[01:07:30] of what I think it's plausible like in
[01:07:31] 2028 we get the the real country of
[01:07:34] geniuses in a data center. You know the
[01:07:36] revenue's been been go you know the
[01:07:38] revenue has been going into the maybe is
[01:07:40] is in the low hundreds of billions by by
[01:07:42] by by 2028 and and and then the country
[01:07:46] of geniuses accelerates it to trillions,
[01:07:48] you know, and and we're basically we're
[01:07:50] basically on the slow end of diffusion.
[01:07:52] It takes two years to get to the
[01:07:53] trillions. that that that would that
[01:07:55] that that would be the world where it
[01:07:56] takes until that would be the world
[01:07:58] where it takes until 2030. I I I suspect
[01:08:01] even composing the technical exponential
[01:08:04] and the diffusion exponential will get
[01:08:05] there before 2030. So you laid out a
[01:08:08] model where anthropic makes profit
[01:08:11] because it seems like fundamentally
[01:08:13] we're in a computed world and so it's
[01:08:15] like eventually we keep growing comput.
[01:08:16] Well, I think I think the way the profit
[01:08:18] comes is again and and you know, let's
[01:08:21] let's just abstract the whole industry
[01:08:22] here. Like we have a you know, let's
[01:08:24] just imagine we're we're in like an
[01:08:25] economics textbook. We have a small
[01:08:27] number of firms each can invest a
[01:08:31] limited amount in you know or or or like
[01:08:33] each can invest some fra fraction in
[01:08:35] R&D. They have some marginal cost to
[01:08:37] serve. the margins on that the profit
[01:08:40] mar the gross profit margins on that
[01:08:42] marginal cost are like very high because
[01:08:44] because because because inference is
[01:08:46] efficient there's some competition but
[01:08:48] the models are also differentiated
[01:08:50] there's some there's some um you know
[01:08:52] companies will compete to push their
[01:08:54] research budgets up but like because
[01:08:56] there's a small number of players you
[01:08:58] know we have the what is it called in
[01:09:00] the corno equilibrium I think is what
[01:09:02] the what the small number of firm
[01:09:04] equilibrium is it the point is it it
[01:09:07] doesn't equilibrate to perfect
[01:09:08] competition with with with with with
[01:09:10] with
[01:09:12] zero margins. If there's like three
[01:09:14] firms, if there's three firms in the
[01:09:16] economy, all are kind of independently
[01:09:19] behaving behaving rationally, it doesn't
[01:09:21] equilibrate to zero.
[01:09:22] >> Um, help me understand that because
[01:09:24] right now we do have three leading firms
[01:09:26] and they're not making profit. Um, and
[01:09:28] so what what uh yeah, what what is
[01:09:31] changing? Yeah. So the the again the
[01:09:34] gross margins right now are very
[01:09:37] positive. What's happen what what's
[01:09:39] happening is a combination of two
[01:09:41] things. One is we're still in the
[01:09:43] exponential scale up phase of compute.
[01:09:45] Um, so what basically what that means is
[01:09:48] we're training like a model gets
[01:09:51] trained, it costs, you know, let's say a
[01:09:53] model got trained that costs uh a
[01:09:55] billion last year. Um, and then uh this
[01:09:59] year it produced uh $4 billion of
[01:10:02] revenue and cost $1 billion to to uh to
[01:10:07] to to inference from. Um so you know
[01:10:10] again I'm using stylized number here but
[01:10:11] you know that would be 75% you know
[01:10:14] gross gross gross margins and you know
[01:10:16] this this 25% tax. So that model as a
[01:10:20] whole makes $2 billion. Um but at the
[01:10:23] same time we're spending $10 billion to
[01:10:26] train the next model because there's an
[01:10:27] exponential scale up and so the company
[01:10:29] loses money. Each model makes money but
[01:10:32] the company loses money. The equilibrium
[01:10:34] I'm talking about is an equilibrium
[01:10:36] where we have the country of geniuses.
[01:10:38] We have the country of geniuses in a
[01:10:39] data center, but that that um model
[01:10:43] training scale up has equilibrated more.
[01:10:46] Maybe maybe it's still it's still going
[01:10:48] up. We're still trying to predict the
[01:10:49] demand, but it's more it's more um
[01:10:52] leveled out. Um I'll give you a couple
[01:10:55] things there. So, um let's start with
[01:10:57] the current world. Um in the current
[01:10:59] world, you're right that as you said
[01:11:01] before, if you treat each individual
[01:11:03] model as a company, it's profitable. But
[01:11:05] of course, a big part of the production
[01:11:07] function of being a frontier lab is
[01:11:11] training the next model, right? So if
[01:11:13] you didn't do that, then you'd make
[01:11:14] profit for two months and then you
[01:11:16] wouldn't have margins because you
[01:11:17] wouldn't have the best model and then so
[01:11:18] yeah, you can make profits for two
[01:11:20] months on the current at some point that
[01:11:21] reaches the biggest scale that it can
[01:11:22] reach and then and then in equilibrium
[01:11:25] we have algorithmic improvements, but
[01:11:27] we're spending roughly the same amount
[01:11:28] to train the next model as as as we
[01:11:31] spent to train the current model. Um so
[01:11:34] this equilibrium relies
[01:11:36] >> I mean at some point at some at at some
[01:11:37] point you run out of money in the
[01:11:38] economy
[01:11:39] >> uh a fixed lump of labor files the
[01:11:42] economy is going to grow right that's
[01:11:43] one of your predictions we're going to
[01:11:44] have but this is but this is another
[01:11:47] example of the theme I was talking about
[01:11:49] which is that the economy will grow much
[01:11:52] faster with AI than I think it ever has
[01:11:54] before but it's not like right now the
[01:11:57] compute is growing 3x a year I don't
[01:12:00] believe the economy is going to grow
[01:12:02] 300% % a year. Like I said this in
[01:12:04] Machines of Loving Grace, like I think
[01:12:05] we we may get 10 or 20% per year growth
[01:12:09] in the economy, but we're not going to
[01:12:11] get 300% growth in the economy. So I
[01:12:13] think I think in the end, you know, if
[01:12:15] if compute becomes the majority of what
[01:12:17] the economy produces, it's it's going to
[01:12:20] be capped by that. So okay, now let's
[01:12:22] assume a model where compute stays
[01:12:23] capped. Yeah. Um, the world where
[01:12:25] Frontier Labs are making money is one
[01:12:27] where they continue to make um, fast
[01:12:30] progress because fundamentally your
[01:12:31] margin is limited by how good the
[01:12:35] alternative is. And so you are able to
[01:12:36] make money because you have a frontier
[01:12:37] model. Um, if you didn't have frontier
[01:12:39] model, you wouldn't be making money. Um,
[01:12:41] >> and and so this this model requires
[01:12:44] there never to be a steady state like
[01:12:46] forever and ever you keep making more
[01:12:49] progress.
[01:12:49] >> I don't think that's true. True. I mean
[01:12:51] I I feel feel like we're we're like
[01:12:52] we're talk we're we're you know I feel
[01:12:54] like this is an economics uh like uh you
[01:12:56] know this is like an economics class you
[01:12:58] know quote we never stop talking about
[01:13:00] economics.
[01:13:01] >> We never we never stop talking about
[01:13:02] economics. So no but but there there are
[01:13:06] worlds in which um you know there so I I
[01:13:09] don't think this field's going to be a I
[01:13:12] monopoly. All my lawyers never want me
[01:13:13] to say the word monopoly. Um but I don't
[01:13:16] think this field's going to be a
[01:13:16] monopoly. But but you do get you get
[01:13:19] industries in which there are small
[01:13:20] number of players, not one but a small
[01:13:22] number of players. And ordinarily like
[01:13:25] the the way you get monopolies like
[01:13:28] Facebook or or Meta, I always call them
[01:13:32] Facebook but um uh uh is is these kind
[01:13:34] of is these kind of these kind of
[01:13:36] network effects. The way you get
[01:13:37] industries in which there are small
[01:13:39] number of players are very high costs of
[01:13:43] entry, right? Um so you know uh cloud is
[01:13:46] like this. I think cloud is a good
[01:13:48] example of this. You have three maybe
[01:13:50] four players within cloud. I think I
[01:13:52] think that's the same for AI. Three
[01:13:54] maybe four. Um uh and the reason is that
[01:13:57] it's it's so expensive. It requires so
[01:14:00] much expertise and so much capital to
[01:14:03] like run a cloud company, right? And so
[01:14:06] you have to put up all this capital. And
[01:14:08] then in addition to putting up all this
[01:14:09] capital, you have to get all of this
[01:14:11] other stuff that like, you know,
[01:14:13] requires a lot of skill to, you know, to
[01:14:15] make it happen. And so it's like if you
[01:14:16] go to someone and you're like, I want to
[01:14:17] disrupt this industry. Here's hundred
[01:14:19] billion dollars. You're like, okay, I'm
[01:14:21] putting $100 billion and also betting
[01:14:23] that you can do all these other things
[01:14:24] that these people have been doing
[01:14:26] >> decrease the profit in the industry.
[01:14:27] >> Yeah. And and and then and then the
[01:14:28] effect of your entering is the profit
[01:14:30] margins go down. And so you know we have
[01:14:31] equilibria like this all the time in the
[01:14:34] economy where we have a few we have a
[01:14:35] few players profits are not astronomical
[01:14:39] margins are not astronomical but they're
[01:14:41] they're not zero right um uh and and you
[01:14:44] know I think I think that's what we see
[01:14:45] on cloud cloud is very undifferentiated
[01:14:48] models are more differentiated than
[01:14:50] cloud right like everyone knows claude
[01:14:53] is claude claude is good at different
[01:14:54] things than GPT is good at is than than
[01:14:57] Gemini is good at and it's not just
[01:14:59] claude's good at coding GP PT is good at
[01:15:01] you know math and reasoning you know um
[01:15:04] uh it's more subtle than that like
[01:15:06] models are good at different types of
[01:15:08] coding models have different styles like
[01:15:10] I think I think these things are
[01:15:12] actually you know quite different from
[01:15:14] each other and so I would expect more
[01:15:16] differentiation than you see in in um
[01:15:19] cloud now there there actually is a uh
[01:15:23] counter there there there is one
[01:15:25] counterargument um and that
[01:15:26] counterargument is that if all of that
[01:15:28] the process of producing models
[01:15:31] um becomes uh if AI models can do that
[01:15:34] themselves, then that could spread
[01:15:36] throughout the economy. But that is not
[01:15:38] an argument for commoditizing AI models
[01:15:40] in general. That's kind of an argument
[01:15:42] for commoditizing the whole economy at
[01:15:44] once. Um I don't know what what quite
[01:15:46] happens in that world where basically
[01:15:48] anyone can do anything, anyone can build
[01:15:50] anything, and there's like no mode
[01:15:52] around anything at all. I mean, I don't
[01:15:54] know, maybe we want that world like like
[01:15:56] maybe that's the maybe that's the end
[01:15:57] state here. like maybe maybe um you know
[01:16:00] when maybe when when when kind of AI
[01:16:02] models can do you know when when when
[01:16:04] when AI models can do everything if
[01:16:06] we've solved all the safety and security
[01:16:08] problems like you know that's one of the
[01:16:10] one of the one of the mechanisms for for
[01:16:12] uh you know um uh uh you know just just
[01:16:15] kind of the economy flattening itself
[01:16:17] again but but that's kind of like post
[01:16:19] like far post country of geniuses in a
[01:16:22] data center. Um maybe a finer way to put
[01:16:24] that uh potential point is one um it
[01:16:28] seems like AI research is especially
[01:16:32] loaded on raw intellectual power which
[01:16:35] will be especially abundant in a world
[01:16:36] with AGI and two if you just look at the
[01:16:39] world today there's very few
[01:16:40] technologies that seem to be diffusing
[01:16:42] as fast as um as AI algorithmic progress
[01:16:47] and so that does hint that this industry
[01:16:49] is sort of structurally diffusive
[01:16:52] So I think coding is going fast but I
[01:16:54] think AI research is a supererset of
[01:16:56] coding and there are aspects of it that
[01:16:57] are not going fast. Um uh but I but I do
[01:17:00] think again once we get coding once we
[01:17:02] get AI models going fast then you know
[01:17:05] AI you know that will speed up the
[01:17:07] ability of AI models to kind to kind of
[01:17:09] do everything else. So I think while
[01:17:11] coding is going fast now I think once
[01:17:13] the AI models are building the next AI
[01:17:15] models and building everything else the
[01:17:17] kind of whole the whole economy will
[01:17:19] kind of go at the same pace. I am I am
[01:17:22] worried geographically though. I'm a
[01:17:25] little worried that like just proximity
[01:17:28] to AI having heard about AI um uh that
[01:17:32] that that may be one differentiator. And
[01:17:34] so when I said the like you know 10 or
[01:17:36] 20% growth rate a worry I have is that
[01:17:39] the growth rate could be like 50% in
[01:17:42] Silicon Valley and you know parts of the
[01:17:45] world that are kind of socially
[01:17:46] connected to Silicon Valley and you know
[01:17:49] not that much faster than its current
[01:17:51] pace elsewhere and I think that'd be a
[01:17:53] pretty messed up world. So I one of the
[01:17:54] things I think about a lot is how to
[01:17:56] prevent that.
[01:17:56] >> Yeah. Do you think that once we have uh
[01:17:58] this country of geniuses in a data
[01:18:00] center that robotics is sort of quickly
[01:18:03] solved afterwards because it seems like
[01:18:05] a big problem with robotics is that um a
[01:18:08] human can learn how to teleoperate
[01:18:09] current hardware but current AI models
[01:18:12] can't at least not not in a way that's
[01:18:14] super productive and so if we have this
[01:18:16] ability to learn like a human should it
[01:18:17] solve robotics immediately as well
[01:18:19] >> I don't think it's dependent on learning
[01:18:20] like a human it could happen in
[01:18:22] different ways again we could have
[01:18:24] trained the model on many different
[01:18:26] video games which like robotic controls
[01:18:28] or many different simulated robotics
[01:18:30] environments or just you know train them
[01:18:32] to control computer screens and they
[01:18:33] learn to generalize. So it will happen.
[01:18:38] It's not necessarily dependent on
[01:18:40] humanlike learning. Humanlike learning
[01:18:42] is one way it could happen. If the
[01:18:43] model's like, "Oh, I pick up a robot. I
[01:18:45] don't know how to use it. I learn that.
[01:18:46] That could happen because we discovered
[01:18:49] discovering continual learning." That
[01:18:51] could also happen because we train the
[01:18:52] model on a bunch of environments and
[01:18:54] then it generalized. Or it could happen
[01:18:56] because the model learns that in the
[01:18:57] context length. It it doesn't actually
[01:18:59] matter which way. If we go back to the
[01:19:01] discussion we had like like an hour ago,
[01:19:04] that type of thing can happen in that
[01:19:06] type of thing can happen in several
[01:19:07] different ways. Um uh uh but but I do
[01:19:10] think when for for whatever reason the
[01:19:13] models have those skills then uh
[01:19:15] robotics will be revolutionized both the
[01:19:18] design of robots because the models will
[01:19:19] be much better than humans at that um
[01:19:22] and also the the ability to kind of
[01:19:25] control robots. So we'll get better at
[01:19:27] the physical building the physical
[01:19:28] hardware building the physical robots
[01:19:30] and we'll also get better at controlling
[01:19:32] it. Now you know does that mean the
[01:19:34] robotics industry will also be
[01:19:36] generating trillions of dollars of
[01:19:37] revenue? My answer there is yes but
[01:19:39] there will be the same extremely fast
[01:19:42] but not infinitely fast diffusion. So
[01:19:44] will robotics be be revolutionized?
[01:19:46] Yeah, maybe tack on another year or two.
[01:19:49] >> That's that's my that's the way I think
[01:19:51] about these things.
[01:19:52] Uh there's a general skepticism about
[01:19:55] extremely fast progress. Like here
[01:19:57] here's my view which is like it sounds
[01:19:58] like you are going to solve continual
[01:20:00] learning one way or another within a
[01:20:01] matter of years. But just as people
[01:20:04] weren't talking about continual learning
[01:20:06] a couple years ago and then we realized
[01:20:07] oh why aren't these models as useful as
[01:20:09] they could be right now even though they
[01:20:10] are clearly passing the touring test and
[01:20:12] are experts in so many different
[01:20:13] domains. Maybe it's this thing. And then
[01:20:15] we solve this thing and we realize
[01:20:16] actually there's another
[01:20:18] um another thing that human intelligence
[01:20:20] can do. that's a basis of human labor
[01:20:22] that these models can't do. And then so
[01:20:24] why not think there will be more things
[01:20:25] like this? Why I think that like we're
[01:20:27] we're you know we've like found the
[01:20:29] pieces of human intelligence.
[01:20:30] >> Well well to be clear I mean I think
[01:20:32] continual learning as I've said before
[01:20:34] might not be a barrier at all right like
[01:20:36] like you know I think I think we maybe
[01:20:38] just get there by pre-training
[01:20:40] generalization and and and and and and
[01:20:43] RL generalization. Like I I think there
[01:20:45] just might not be um there basically
[01:20:48] might not be such a thing at all. In
[01:20:49] fact, I would point to the history in in
[01:20:52] ML of people coming up with things that
[01:20:55] are barriers that end up kind of
[01:20:56] dissolving within the big blob of
[01:20:58] compute, right? That, you know, people
[01:21:00] talked about, you know,
[01:21:02] you know, how do you have, you know, how
[01:21:05] do how do your models keep track of
[01:21:07] nouns and verbs and, you know, how do
[01:21:08] they, you know, they can understand
[01:21:10] semant syntactically, but they can't
[01:21:12] understand semantically. You know, it's
[01:21:14] only statistical correlations. You can
[01:21:17] understand a paragraph, but you can't
[01:21:18] understand a word. There's reasoning,
[01:21:20] you can't do reasoning, but then
[01:21:21] suddenly it turns out you can do code
[01:21:23] and math very well at all. So
[01:21:25] >> I I think there actually there's there's
[01:21:27] actually a stronger history of some of
[01:21:30] these things seeming like a big deal and
[01:21:32] then and then kind of and then kind of
[01:21:34] dissolving. Some of them are real. I
[01:21:36] mean the need for data is real. May
[01:21:38] maybe continual
[01:21:40] continual learn continual learning is a
[01:21:42] real thing. But again, I would ground us
[01:21:44] in something like code. Like I think we
[01:21:47] may get to the point in like a year or
[01:21:49] two where the models can just do end to
[01:21:51] end. Like that's a whole task. That's a
[01:21:53] whole sphere of human activity that that
[01:21:56] we're just saying models can do it now.
[01:21:58] Um when you say end to end, do you mean
[01:22:01] um setting technical direction,
[01:22:03] understanding the context of the
[01:22:05] problem, etc.? Okay. Yes. I mean all of
[01:22:07] that. Interesting. I mean that that is I
[01:22:11] feel like AGI complete um which maybe is
[01:22:14] internally consistent but um it's not
[01:22:16] like saying 90% of code or 100% of code
[01:22:18] it's like no no the other parts of the
[01:22:20] >> no no I gave this I gave the spectrum
[01:22:22] 90% of code 100% of code 90% of N10
[01:22:26] suite 100% of N10 suite new tasks are
[01:22:29] created for SWES eventually those get
[01:22:31] done as well but it's a long spectrum
[01:22:32] there but we're traversing the spectrum
[01:22:34] very quickly
[01:22:35] >> um I do think it's funny that I I've
[01:22:37] seen a couple podcasts you've done where
[01:22:39] um the host will be like a butcher wrote
[01:22:42] the essay about the control learning
[01:22:43] thing and it always makes me crack up
[01:22:44] because you're like you know you've been
[01:22:46] an AI researcher for like 10 years and
[01:22:48] I'm sure there's like some uh feeling of
[01:22:50] like okay so podcaster wrote an essay
[01:22:53] [laughter] like every interview I get
[01:22:54] asked about it
[01:22:55] >> you know the the truth of the truth of
[01:22:57] the matter is that we're all trying to
[01:22:59] figure this out together right there
[01:23:01] there are some ways in which I'm able to
[01:23:05] see things that others aren't these days
[01:23:07] That probably has more to do with like I
[01:23:09] can see a bunch of stuff within
[01:23:10] Enthropic and have to make a bunch of
[01:23:12] decisions than I have any great research
[01:23:15] insight that that that others don't.
[01:23:16] Right? I you know I'm running a 2500
[01:23:18] person company. Like it's it's actually
[01:23:20] pretty hard for me to have have concrete
[01:23:23] research insight you know much harder
[01:23:26] than you know than than it would have
[01:23:27] been you know 10 years ago or or you
[01:23:29] know or even two or three years ago. Um,
[01:23:33] as we go towards a world of a full drop
[01:23:35] in remote worker replacement, does a API
[01:23:39] pricing model still make the most sense?
[01:23:42] And if not, what is the correct way to
[01:23:43] price AGI or serve AGI?
[01:23:45] >> Yeah, I mean, I think there's going to
[01:23:46] be a bunch of different business models
[01:23:48] here sort of all at once that are going
[01:23:50] to be that are going to be experimented
[01:23:52] with. Um, I I I actually do think that
[01:23:55] the the API
[01:23:57] um
[01:23:59] model is is more durable than many
[01:24:01] people think. Um, one way I think about
[01:24:04] it is if the technology is kind of
[01:24:07] advancing quickly, if it's advancing
[01:24:09] exponentially, what that means is
[01:24:11] there's there's always kind of like a
[01:24:13] surface area of of kind of new use cases
[01:24:15] that have been developed in in the last
[01:24:17] uh in the last three months. And any
[01:24:20] kind of product surface you put in place
[01:24:22] is always at risk of sort of becoming
[01:24:26] irrelevant, right? Any given product
[01:24:28] surface probably makes sense for, you
[01:24:30] know, a range of capabilities of the
[01:24:32] model, right? The the chatbot is already
[01:24:34] running into limitations of, you know,
[01:24:37] making it smarter doesn't really help
[01:24:39] the average consumer that much. But I
[01:24:41] don't think that's a limitation of AI
[01:24:43] models. I don't think that's evidence
[01:24:45] that, you know, the models are are the
[01:24:46] models are good enough and they're
[01:24:48] they're, you know, them getting better
[01:24:50] doesn't matter to the economy. It
[01:24:51] doesn't matter to that particular
[01:24:52] product. Um, and and so I think the
[01:24:55] value of the API is the API always
[01:24:59] offers an opportunity, you know, very
[01:25:01] close to the bare metal to build on what
[01:25:04] the latest thing is. Um, and so there,
[01:25:06] you know, there's there's there's kind
[01:25:07] of always going to be this, you know,
[01:25:09] this this kind of front of new startups
[01:25:12] and new ideas that weren't possible a
[01:25:15] few months ago and are possible because
[01:25:16] the model is advancing. And and so I I
[01:25:20] actually I I I kind of actually predict
[01:25:23] that we are it's going to exist
[01:25:26] alongside other models, but we're always
[01:25:28] going to have the API business model
[01:25:31] because there's there's always going to
[01:25:32] be a need for a thousand different
[01:25:34] people to try experimenting with the
[01:25:36] model in different way and a hundred of
[01:25:38] them become startups and 10 of them
[01:25:40] become big successful startups and you
[01:25:42] know two or three really end up being
[01:25:44] the the way that people use the model of
[01:25:46] a of a given generation. So I I
[01:25:48] basically think it's always going to
[01:25:50] exist. At the same time, I'm sure
[01:25:53] there's going to be other models as
[01:25:55] well. Like not every token [snorts]
[01:25:57] that's output by the model is worth the
[01:25:59] same amount. Think about, you know, how
[01:26:02] how what is the value of the tokens that
[01:26:04] are like, you know, that the model
[01:26:06] outputs when someone, you know, call,
[01:26:09] you know, someone, you know, calls them
[01:26:10] up and says, "My Mac isn't working or
[01:26:12] something." You know, the model's like,
[01:26:13] "Restart it, right?" Yeah.
[01:26:15] >> And like you know someone hasn't heard
[01:26:16] that before but like you know the model
[01:26:18] said that like 10 million times you know
[01:26:22] that maybe that's worth like a dollar or
[01:26:24] a few cents or something. Um whereas if
[01:26:28] uh the model you know the model goes to
[01:26:31] you know one of the one of the
[01:26:32] pharmaceutical companies and it says oh
[01:26:34] you know this molecule you're developing
[01:26:36] you should take the aromatic ring from
[01:26:38] that end of the molecule and put it on
[01:26:40] that end of the molecule. Um and and you
[01:26:42] know if you do that wonderful things
[01:26:44] will happen. um uh like like those
[01:26:47] tokens could [laughter] be worth, you
[01:26:48] know, tens of millions of dollars,
[01:26:50] right? Um uh so so I think we're
[01:26:53] definitely going to see business models
[01:26:54] that that recognize that, you know, at
[01:26:57] some point we're going to see, you know,
[01:26:59] pay for results or you know, in some in
[01:27:02] some form or we may see forms of
[01:27:06] compensation that are like labor um uh
[01:27:09] you know, that that kind of work by the
[01:27:11] hour. Um I I I you know, I don't Oh, I
[01:27:14] think I think I think because it's a new
[01:27:16] industry, a lot of things are going to
[01:27:18] be tried and I you know I don't know
[01:27:19] what will turn out to be the right
[01:27:20] thing.
[01:27:20] >> Um what I find uh I I take your point
[01:27:24] that people will have to try things to
[01:27:25] figure out what is the best way to use
[01:27:26] this blob of intelligence. But what I
[01:27:29] find striking is clawed code. So I don't
[01:27:33] think in the history of startups there
[01:27:34] has been a single application that has
[01:27:37] been as hotly competed in as coding
[01:27:40] agents and um and and cloud code is a
[01:27:45] category leader here and that seems
[01:27:48] surprising to me like it doesn't seem
[01:27:49] intrinsically like enthropic had to
[01:27:51] build this and I wonder if you have an
[01:27:53] accounting of why it had to be enthropic
[01:27:55] or why how enthropic ended up building
[01:27:56] an application in addition to the model
[01:27:59] underlying it. Yeah. So it actually
[01:28:00] happened in a pretty simple way which is
[01:28:02] we had our own um you know we had our
[01:28:06] coding models which were good at coding
[01:28:08] and and you know around the beginning of
[01:28:10] 2025 I said I I think the time has come
[01:28:13] where you can have non-trivial
[01:28:15] acceleration of your own research um if
[01:28:18] you're an AI company by using these
[01:28:21] models and of course you know we you
[01:28:22] need an interface you need a harness to
[01:28:24] use them and so I encourage people
[01:28:26] internally you know I didn't say this is
[01:28:28] one thing that you know you have to use.
[01:28:31] I I just said people should experiment
[01:28:32] with this and then you know this thing I
[01:28:36] think it might have been originally
[01:28:37] called claude CLI and then the name
[01:28:40] eventually got changed to cloud code
[01:28:42] internally um was the thing that kind of
[01:28:45] everyone was using and it was seeing
[01:28:46] fast internal adoption and I looked at
[01:28:48] it and I said probably we should launch
[01:28:50] this externally right um uh you know
[01:28:53] it's it's seen such fast adoption within
[01:28:55] anthropic like you know like you know
[01:28:57] coding is a lot of what we do and and so
[01:28:59] you know we have a we have audience of
[01:29:01] many many hundreds of people that's in
[01:29:03] some ways at least representative of the
[01:29:05] external audience. So it looks like we
[01:29:07] already have product market fit. Let's
[01:29:09] launch this thing. Um and and then we
[01:29:11] launched it and and and I think you know
[01:29:13] just just the fact that we ourselves are
[01:29:16] kind of developing the model and we
[01:29:18] ourselves know what we most need to use
[01:29:20] the model. I think it's it's kind of
[01:29:22] creating this feedback loop.
[01:29:23] >> I see. in the sense that you let's say a
[01:29:26] developer at Enthropic is like ah it it
[01:29:29] would be better if it was better at this
[01:29:30] X thing and then you bake that into the
[01:29:33] next model that you build that that's
[01:29:35] that's one version of it but but then
[01:29:37] there's just the ordinary product
[01:29:38] iteration of like you know we have a
[01:29:41] bunch of we have a bunch of coders
[01:29:42] within anthropic like we um you know
[01:29:46] they like use cloud code every day and
[01:29:47] so we get fast feedback that was more
[01:29:49] important in the early days now of
[01:29:50] course there are millions of people
[01:29:51] using it um and so we get a bunch of
[01:29:54] external feedback as well. But it's, you
[01:29:56] know, it's just great to be able to get,
[01:29:57] you know, kind of kind of uh um fast
[01:30:00] fast internal feedback. You know, I
[01:30:02] think this is the reason why we launched
[01:30:04] a coding model and, you know, didn't
[01:30:06] launch a pharmaceutical company, right?
[01:30:08] It you know, you know, my background is
[01:30:09] in in my background's in in like
[01:30:12] biology, but like we don't have any of
[01:30:13] the resources that are needed to launch
[01:30:15] a pharmaceutical company. So, there's
[01:30:17] been a ton of hype around OpenClaw, and
[01:30:18] I wanted to check it out for myself.
[01:30:20] I've got a day coming up this weekend
[01:30:21] and I don't have anything planned yet.
[01:30:23] So, I gave Open Claw a Mercury debit
[01:30:26] card. I set a couple hundred limit and I
[01:30:28] said, "Surprise me." Okay, so here's the
[01:30:30] Mac Mini it's on. And besides having
[01:30:32] access to my Mercury, it's totally
[01:30:33] quarantined. They actually felt quite
[01:30:35] comfortable giving it access to a debit
[01:30:37] card because Mercury makes it super easy
[01:30:38] to set up guardrails. I was able to
[01:30:40] customize permissions, cap the spend,
[01:30:41] and restrict the category of purchases.
[01:30:43] I wanted to make sure the debit card
[01:30:44] worked, so I asked OpenCloud to just
[01:30:46] make a test transaction and decided to
[01:30:48] donate a couple bucks to Wikipedia.
[01:30:49] Besides that, I have no idea what's
[01:30:51] going to happen. I will report back on
[01:30:53] the next episode about how it goes. In
[01:30:54] the meantime, if you want a personal
[01:30:56] banking solution that can accommodate
[01:30:58] all the different ways that people use
[01:30:59] their money, even experimental ones like
[01:31:01] this one, visit mercury.com/personal.
[01:31:05] Mercury is a fintech company, not an
[01:31:07] FDIC insured bank. Banking services
[01:31:10] provided through Choice Financial Group
[01:31:11] and column NA members FDIC. You know,
[01:31:14] she thinks we're getting coffee and
[01:31:15] walking around the neighborhood.
[01:31:17] [laughter]
[01:31:18] Um let me ask you about now um making AI
[01:31:22] go well. Um it seems like whatever
[01:31:25] vision we have about how AI goes well
[01:31:28] has to be compatible with two things.
[01:31:30] One is the ability to build and run AIs
[01:31:33] is diffusing extremely rapidly and two
[01:31:36] is that the population of AIS the amount
[01:31:39] we have in their intelligence will also
[01:31:41] increase very rapidly and that means
[01:31:44] that lots of people will be able to
[01:31:46] build huge populations of misaligned AIs
[01:31:49] or uh AIs which are just like companies
[01:31:51] which are trying to increase their uh
[01:31:53] footprint or have weird psyches like
[01:31:55] Sydney Bing but now they're superhuman.
[01:31:57] What is a vision for a world in which we
[01:32:00] have an equilibrium that is compatible
[01:32:02] with lots of different AI some of which
[01:32:04] are misaligned running around?
[01:32:05] >> Yeah. Yeah. So I think you know in the
[01:32:07] adolescence of technology I was kind of
[01:32:10] you know skeptical of like the balance
[01:32:12] of power but I I think I was
[01:32:14] particularly skeptical of or the thing I
[01:32:17] was specifically skeptical of is you
[01:32:19] have like three or four of these
[01:32:21] companies like kind of all building
[01:32:24] models that are kind of derive you know
[01:32:25] sort of sort of um uh uh like derived
[01:32:29] from the like derived from the same
[01:32:32] thing and uh you know that that these
[01:32:35] would check each or or even that kind of
[01:32:37] you know any number of them would would
[01:32:38] would would uh would would check each
[01:32:40] other like we might live in a offense
[01:32:42] dominant world where you know like one
[01:32:45] person or one AI model is like smart
[01:32:47] enough to do something that like causes
[01:32:48] damage for everything else. Um I think
[01:32:51] in the I mean in the short run we have a
[01:32:54] limited number of players now. So we can
[01:32:55] start by within the limited number of
[01:32:57] players we uh you know we kind of you
[01:33:01] know we we need to put in place the you
[01:33:02] know the safeguards. We need to make
[01:33:04] sure everyone does the right alignment
[01:33:05] work. we need to make sure everyone has
[01:33:07] bio classifiers like you know those are
[01:33:09] those are kind of the immediate things
[01:33:10] we need to do. I agree that you know
[01:33:12] that that doesn't solve the problem in
[01:33:14] the long run particularly if the ability
[01:33:16] of AI models to make other AI models
[01:33:18] proliferates then you know the the whole
[01:33:22] thing can kind of um you know can become
[01:33:25] harder to solve. You know I think I
[01:33:26] think in the long run we need some
[01:33:29] architecture of governance right some
[01:33:31] some architecture of governance that
[01:33:33] preserves human freedom but but kind of
[01:33:36] also allows us to like you know govern
[01:33:38] the the very large number of kind of um
[01:33:42] you know uh uh uh human systems AI
[01:33:46] systems hybrid hybrid human human um you
[01:33:50] know hybrid hybrid human AI like you
[01:33:54] know companies or or like or like or
[01:33:56] like economic units. So, you know, we're
[01:33:58] we're going to need to think about like,
[01:34:00] you know, how do we how do we protect
[01:34:02] the world against, you know,
[01:34:04] bioteterrorism? How do we protect the
[01:34:05] world against like, you know, against
[01:34:07] like against like mirror life? Like, you
[01:34:10] know, pro probably we're going to need
[01:34:12] to, you know, need some kind of like AI
[01:34:14] monitoring system that like moni, you
[01:34:16] know, kind of monitors for for all these
[01:34:18] things, but then we need to build this
[01:34:20] in a way that like, you know, preserves
[01:34:22] civil liberties and like our
[01:34:23] constitutional rights. So I think just
[01:34:25] just as is as is anything else like it's
[01:34:28] it's like a new security landscape with
[01:34:31] a new set of you know a new set of tools
[01:34:34] and a new set of vulnerabilities. And I
[01:34:37] I think my worry is if we had a hundred
[01:34:40] years for this to happen all very
[01:34:41] slowly, we'd get used to it, you know,
[01:34:44] like we've gotten used to like, you
[01:34:46] know, the presence of, you know, the
[01:34:48] presence of explosives in society or
[01:34:50] like the, you know, the presence of
[01:34:51] various um, you know, like new weapons
[01:34:54] or the, you know, the pre the presence
[01:34:56] of video cameras. Um, we would get used
[01:34:58] to it over over over over 100 and we'd
[01:35:01] develop governance mechanisms. We'd make
[01:35:03] our mistakes. My my worry is just that
[01:35:05] this is happening all so fast and so I
[01:35:07] think maybe we need to do our thinking
[01:35:09] faster about how to make these
[01:35:11] governance mechanisms work.
[01:35:12] >> Yeah, it seems like in a offense
[01:35:14] dominant world
[01:35:17] over the course of the next century. So
[01:35:18] the idea is AI is making the progress
[01:35:20] that would happen over the next century
[01:35:21] happen in some period of 5 to 10 years.
[01:35:24] But we would still need the same
[01:35:25] mechanisms or balance of power would be
[01:35:27] similarly intractable even if humans
[01:35:30] were the only game in town. Um, and so I
[01:35:34] guess we have the advice of AI. We it
[01:35:37] fundamentally doesn't seem like a
[01:35:39] totally different ballgame here. If
[01:35:41] checks and balances were going to work,
[01:35:42] they would work with humans as well. If
[01:35:44] they aren't going to work, they wouldn't
[01:35:45] work with AIS as well. Um, and so maybe
[01:35:48] this just dooms human checks and
[01:35:49] balances as well. But yeah, again, I
[01:35:51] think there's some way to I think
[01:35:54] there's some way to make this happen.
[01:35:55] Like it, you know, it just it just, you
[01:35:58] know, the governments of the world may
[01:35:59] have to work together to make it happen.
[01:36:01] like you know we may have to you may
[01:36:03] have to talk to AIS about kind of you
[01:36:06] know building societal structures in
[01:36:08] such a way that like these these
[01:36:10] defenses are possible. I I I don't know.
[01:36:12] I mean this is so this is you know I
[01:36:14] don't want to say so far ahead in time
[01:36:15] but like so far ahead in technological
[01:36:18] ability that may happen over a short
[01:36:20] period of time that it's hard for us to
[01:36:22] anticipated in advance. Um, speaking of
[01:36:24] governments getting involved, on
[01:36:25] December 26th, the Tennessee legislature
[01:36:28] introduced a bill which uh said, quote,
[01:36:31] um, it would be an offense for a person
[01:36:32] to knowingly train artificial
[01:36:33] intelligence to provide emotional
[01:36:35] support, including through open-ended
[01:36:37] conversations with a user. And of
[01:36:39] course, one of the things that Claude
[01:36:42] attempts to do is be uh a thoughtful um
[01:36:46] thoughtful friend, thoughtful,
[01:36:47] knowledgeable friend. And in general, it
[01:36:49] seems like we're going to have this
[01:36:50] patchwork of state laws. A lot of the
[01:36:52] benefits that normal people could
[01:36:54] experience as a result of AI are going
[01:36:55] to be curtailed, especially when we get
[01:36:57] into the kinds of things you discussed
[01:36:58] in machines of love and grace,
[01:37:00] biological freedom, mental health
[01:37:01] improvements, etc., etc. It seems easier
[01:37:03] to imagine worlds in which these get
[01:37:05] whack-a-ole away by different laws. Um,
[01:37:08] whereas
[01:37:10] bills like this don't seem to address
[01:37:11] the actual existential threats that
[01:37:14] you're concerned about. So I'm curious
[01:37:16] about to understand in the context of
[01:37:18] things like this your anthropics
[01:37:19] position against the federal moratorium
[01:37:22] on state AI laws.
[01:37:23] >> Yes. So I don't know there's there's
[01:37:25] many different things going on at once,
[01:37:27] right? I think I think that that I think
[01:37:29] that particular law is is dumb. Like you
[01:37:31] know I think it was it was clearly made
[01:37:33] by legislators who just probably had
[01:37:36] little idea what AI models could do and
[01:37:38] not do. They're like AI models serving
[01:37:39] as that just sounds scary. Like I don't
[01:37:41] want I don't want that to happen. So,
[01:37:43] you know, we're we're we're not we're
[01:37:45] not in favor of that, right? But but but
[01:37:47] that, you know, that that wasn't the
[01:37:49] thing that was being voted on. The thing
[01:37:50] that was being voted on is we're going
[01:37:52] to ban all state regulation of AI for 10
[01:37:56] years with no apparent plan to to do any
[01:38:00] federal regulation of AI, which would
[01:38:02] take Congress to pass, which is a very
[01:38:04] high bar. Um so you know the idea that
[01:38:06] we'd ban states from doing anything for
[01:38:08] 10 years and people said they had a plan
[01:38:11] for federal government but you know
[01:38:12] there was no actual there was no
[01:38:14] proposal on the table. There was no
[01:38:15] actual attempt. Um given the serious
[01:38:18] dangers that I lay out in adolescence of
[01:38:21] technology around things like the you
[01:38:23] know kind of biological weapons and
[01:38:25] bioteterrorism autonomy risk and the
[01:38:29] timelines we've been talking about like
[01:38:31] 10 years is an eternity. like that's
[01:38:33] that's a that's a I I think that's a
[01:38:35] crazy thing to do. So if if that's the
[01:38:37] choice, if that's what you force us to
[01:38:39] choose, then then we're going to we're
[01:38:42] going to choose not to have that
[01:38:43] moratorum. And you know, I think the the
[01:38:46] the benefits of that position exceed the
[01:38:48] costs. But it's it's not a perfect
[01:38:50] position if that's the choice. Now, I
[01:38:52] think the thing that we should do, the
[01:38:54] thing that I would support is the
[01:38:55] federal government should step in, not
[01:38:59] saying states you can't regulate, but
[01:39:01] here's what we're going to do and and
[01:39:03] states you can't differ from this,
[01:39:05] right? Like I think preeemption is fine
[01:39:08] in the sense of saying that federal
[01:39:09] government says here's our standard.
[01:39:11] This applies to everyone. States can't
[01:39:13] do something different. That would be
[01:39:15] something I would support if it would be
[01:39:16] done in the right way. What um but but
[01:39:20] this idea of states you can't do
[01:39:22] anything and we're not doing anything
[01:39:23] either that that struck that struck us
[01:39:26] as you know very much not making sense
[01:39:29] and I think will not age well it's
[01:39:31] already starting to not age well with
[01:39:33] with all the um backlash that that
[01:39:35] you've seen now in terms of in terms of
[01:39:37] what we would want I mean you know the
[01:39:39] things we've talked about are are
[01:39:41] starting with transparency standards um
[01:39:43] uh uh you know in order to monitor some
[01:39:46] of these autonomy risks and bio
[01:39:47] terrorism risks as the risks become more
[01:39:50] serious um as we as we get more evidence
[01:39:53] for them then I think we could be more
[01:39:56] aggressive in some targeted ways and and
[01:39:58] say hey AI bioteterrorism is really a
[01:40:01] threat let's let's pass a law that kind
[01:40:03] of forces people to have classifiers and
[01:40:05] I could even imagine it it depends it
[01:40:08] depends how serious a threat it ends up
[01:40:09] being we don't know for sure and we need
[01:40:11] to pursue this in an intellectually
[01:40:13] honest way where we say ahead of time
[01:40:14] the risk has not emerged yet but I could
[01:40:17] certainly imagine with the pace that
[01:40:18] things are going that you know I could
[01:40:21] imagine a world where later this year we
[01:40:22] say hey this this AI bioteterrorism
[01:40:26] stuff is really serious we should do
[01:40:27] something about it we should put it in a
[01:40:29] federal we should you know put it in a
[01:40:30] federal standard and if the federal
[01:40:32] government won't act we should put it in
[01:40:33] a state standard I could totally see
[01:40:35] that I I I'm concerned about a world
[01:40:37] where
[01:40:39] if you just consider the the pace of
[01:40:41] progress you're expecting the life cycle
[01:40:44] of of legislation you the the benefits
[01:40:47] are, as you say, because of diffusion
[01:40:49] lag, the benefits are slow enough that I
[01:40:51] really do think this patchwork of on the
[01:40:53] current trajectory, this patchwork of
[01:40:55] state laws would prohibit. I mean,
[01:40:58] having an emotional chatbot friend is
[01:40:59] something that freaks people out, then
[01:41:01] just imagine the kinds of actual
[01:41:02] benefits from AI we want normal people
[01:41:05] to be able to experience from
[01:41:06] improvements in health and health span
[01:41:08] and improvements in mental health and so
[01:41:09] forth. whereas at the same time uh it
[01:41:12] seems like you think the dangers are
[01:41:14] already on the horizon and I just don't
[01:41:16] see that much um it seems like would be
[01:41:19] especially injurious to the benefits of
[01:41:21] AI uh as compared to the the dangers of
[01:41:23] AI and so that that's maybe the where
[01:41:25] the cost benefit makes less sense to me.
[01:41:27] So, so, so there's a few things here,
[01:41:29] right? I mean, people talk about there
[01:41:31] being thousands of these state laws.
[01:41:33] First of all, the vast vast majority of
[01:41:35] them do not pass. Um, and you know, the
[01:41:38] the the the you know, the world works a
[01:41:40] certain way in theory, but like just
[01:41:42] because a law has been passed doesn't
[01:41:43] mean it's really enforced, right? The
[01:41:44] people the people you know implementing
[01:41:47] it may be like, "Oh my god, this is
[01:41:48] stupid." It would mean shutting off
[01:41:49] like, you know, everything that's ever
[01:41:52] been built and everything that's ever
[01:41:53] been built in Tennessee. So, you know,
[01:41:55] very often laws are interpreted in like,
[01:41:57] you know, a way that makes them that
[01:41:59] that that makes them not as dangerous or
[01:42:01] not as harmful. On on the same side, of
[01:42:03] course, you have to worry if you're
[01:42:04] passing a law to stop a bad thing, you
[01:42:06] had this you had this problem as well.
[01:42:08] Yeah. Um uh look my my look I mean my
[01:42:12] basic view is you know if if if
[01:42:15] you know we could decide you know what
[01:42:17] laws were passed and how things were
[01:42:18] done which you know we're only one small
[01:42:20] input input into that you know I would
[01:42:24] deregulate a lot of the stuff around the
[01:42:26] health benefits of AI. Um I think you
[01:42:29] know I I don't worry as much about the
[01:42:31] like the the the kind of chatbot laws. I
[01:42:34] I actually worry more about the drug
[01:42:36] approval process where I think AI models
[01:42:39] are going to greatly accelerate um the
[01:42:43] rate at which we discover drugs and just
[01:42:46] the the pipeline will get jammed up like
[01:42:47] the pipeline will not be prepared to
[01:42:49] like process all all of the stuff that's
[01:42:52] going through it. So um you know I I I
[01:42:55] think I think reform of the regulatory
[01:42:57] process to buy us more towards we have a
[01:43:00] lot of things coming where the safety
[01:43:02] and the efficacy is actually going to be
[01:43:05] really crisp and clear like I mean a
[01:43:07] beautiful thing really really crisp and
[01:43:08] clear and like really really effective
[01:43:11] but you know and and and maybe we don't
[01:43:12] need all this all this um uh uh like um
[01:43:17] all this superructure around it that was
[01:43:19] designed around an era of drugs that
[01:43:21] barely work and often and have serious
[01:43:23] side effects. Um but at the same time I
[01:43:26] think we should be ramping up quite
[01:43:28] significantly the um uh you know this
[01:43:32] this kind of safety and security
[01:43:34] legislation and you know like I've said
[01:43:36] um you know starting with transparency
[01:43:38] is is my view of trying not to hamper
[01:43:42] the industry right trying to find the
[01:43:43] right balance. I'm worried about it.
[01:43:45] Some people criticize my essay for
[01:43:47] saying that's too slow. The dangers of
[01:43:49] AI will come too soon if we do that.
[01:43:51] Well, basically I kind of think like the
[01:43:54] last 6 months and maybe the next few
[01:43:56] months are going to be about
[01:43:57] transparency. And then if these ris if
[01:44:00] these risks emerge when we're more
[01:44:02] certain of them, which I think we might
[01:44:03] be as soon as as later this year, then I
[01:44:06] think we need to act very fast in the
[01:44:08] areas that we've actually seen the risk.
[01:44:10] Like I think the only way to do this is
[01:44:12] to be nimble. Now the legislative
[01:44:14] process is normally not nimble but we we
[01:44:17] need to emphasize to everyone involved
[01:44:20] the urgency of this. That's why I'm
[01:44:22] sending this message of urgency, right?
[01:44:24] That's why I wrote adolescence of
[01:44:26] technology. I wanted policy makers to
[01:44:28] read it. I wanted economists to read it.
[01:44:29] I want national security professionals
[01:44:31] to read it. You know, I want decision
[01:44:33] makers to read it so that they have some
[01:44:36] hope of acting faster than they would
[01:44:37] have otherwise. Is there anything you
[01:44:40] can do or advocate that would
[01:44:45] make it more certain that the benefits
[01:44:47] of AI are um are better instantiated
[01:44:50] where I feel like you have worked with
[01:44:52] legislators to be like okay we're going
[01:44:54] to prevent biotterism here way we're
[01:44:56] going to increase we're going to
[01:44:57] increase whistleblower protection and I
[01:44:59] just think by default the actual ben
[01:45:01] like the things we're looking forward to
[01:45:02] here it just seems very easy they seem
[01:45:04] very fragile to uh different kinds of
[01:45:07] moral panics or political economy
[01:45:09] problems.
[01:45:09] >> Yeah, I don't actually so so I don't
[01:45:11] actually agree that much in the
[01:45:13] developed world. I feel like, you know,
[01:45:15] in the developed world like markets
[01:45:17] function pretty well and when there's
[01:45:21] when there's like a lot of money to be
[01:45:23] made on something and it's clearly the
[01:45:25] best available alternative, it's
[01:45:27] actually hard for the regulatory system
[01:45:28] to stop it. You know, we're we're seeing
[01:45:30] that in AI itself, right? I you know,
[01:45:33] like a thing I've been trying to fight
[01:45:34] for is export controls on chips to
[01:45:36] China, right? And like that's in the
[01:45:39] national security interests of the US
[01:45:41] like you know that's like square within
[01:45:44] the you know the the policy beliefs of
[01:45:47] you know every almost everyone in
[01:45:48] Congress of both parties but and you
[01:45:52] know I think the case is very clear. The
[01:45:53] counterarguments against it are I'll
[01:45:56] politely call them fishy. Um uh and yet
[01:46:00] it doesn't happen and we sell the chips
[01:46:02] because there's there's so much money
[01:46:04] there's so much money riding on it. um
[01:46:06] and you know the the that money wants to
[01:46:09] be made and and in that case in my
[01:46:10] opinion that's a bad thing. Um and but
[01:46:13] but it also it also applies when when
[01:46:15] it's a good thing and and so I I don't
[01:46:18] think that if we're talking about drugs
[01:46:21] and benefits of the technology I I I I
[01:46:26] am not as worried about those benefits
[01:46:28] being hampered in the developed world. I
[01:46:30] am a little worried about them going too
[01:46:32] slow and I as I said I do think we
[01:46:35] should work to speed the approval
[01:46:38] process in the FDA. I do think we should
[01:46:40] fight against these chatbot bills that
[01:46:42] you're describing right described
[01:46:44] individually. I'm against them. I think
[01:46:46] they're stupid. Um but I actually think
[01:46:48] the bigger worry is a developing world
[01:46:51] um where we don't have functioning
[01:46:52] markets where um you know we often can't
[01:46:55] build on the technology that that we've
[01:46:57] had. I worry more that those folks will
[01:47:00] get left behind. And I worry that even
[01:47:02] if the cures are developed, you know,
[01:47:03] maybe there's someone in rural
[01:47:04] Mississippi who who doesn't get it as
[01:47:06] well. Right? That's a that's a that's a
[01:47:08] kind of smaller version of the thing the
[01:47:10] concern we have in the in the developing
[01:47:12] world. And so the things we've been
[01:47:14] doing are you know you know we work with
[01:47:16] you know we work with you know
[01:47:18] philanthropists right you know we work
[01:47:19] with folks um who you know who you know
[01:47:24] deliver you know medicine and health
[01:47:26] interventions to you know to to
[01:47:28] developing world to subsaharan Africa
[01:47:31] you know India Latin America you know
[01:47:35] you know other other developing parts of
[01:47:37] the world that's the thing I think that
[01:47:39] won't happen on its own you mentioned
[01:47:41] export controls Yeah.
[01:47:42] >> Why can't US and China both have a
[01:47:45] country of geniuses
[01:47:46] >> on a data center?
[01:47:47] >> Why can't you know why won't it happen
[01:47:49] or why should
[01:47:50] >> why shouldn't it happen?
[01:47:51] >> Why shouldn't it happen? Um, you know, I
[01:47:54] think I think if this does happen, um,
[01:47:57] you know, then then we kind of have a
[01:48:00] well, we could have a few situ if we
[01:48:02] have like an offense dominant situation.
[01:48:04] We could have a situation like nuclear
[01:48:05] weapons, but like more dangerous, right?
[01:48:07] Where it's like um, you know, kind of
[01:48:09] kind of either side could could easily
[01:48:12] destroy everything. Um, we could also
[01:48:14] have a world where it's kind of it's
[01:48:17] unstable. Like the nuclear equilibrium
[01:48:18] is stable, right? Because it's, you
[01:48:20] know, it's like deterrence. But let's
[01:48:22] say there were uncertainty about like if
[01:48:24] the two AIs fought, which AI would win.
[01:48:26] Um, that could create instability,
[01:48:28] right? You often have conflict when the
[01:48:31] two sides have a different assessment of
[01:48:32] their likelihood of winning, right? If
[01:48:34] one side is like, oh yeah, there's a 90%
[01:48:36] chance I'll win. And the other side's
[01:48:37] like, there's a 90% chance I'll win,
[01:48:40] then then a fight is much more likely.
[01:48:42] Um, they can't both be right, but they
[01:48:43] can both think that. But this seems like
[01:48:45] a fully general argument against the
[01:48:47] diffusion of AI technology which it may
[01:48:50] which is that's the implication of this
[01:48:51] world.
[01:48:52] >> Let me let me just go on because I think
[01:48:53] we will get diffusion eventually. The
[01:48:56] other concern I have is that people the
[01:48:58] governments will oppress their own
[01:48:59] people with AI and and and so um you
[01:49:03] know I'm I'm just I'm worried about some
[01:49:05] world where you have a country that's
[01:49:06] already you know kind of a uh you know
[01:49:11] you know there's there's a government
[01:49:12] that kind of kind of already um you know
[01:49:14] is is kind of kind of building a you
[01:49:17] know a tech high-tech authoritarian
[01:49:19] state. Um and to be clear this is about
[01:49:21] the government. this is not about the
[01:49:22] people like people we need to find a way
[01:49:24] for people everywhere to benefit. Um my
[01:49:26] worry here is about governments. Um so
[01:49:29] yeah my you know my my worry is the
[01:49:31] world gets carved up into two pieces one
[01:49:33] of those two pieces could be
[01:49:34] authoritarian or totalitarian in a way
[01:49:36] that's very difficult to displace. Um
[01:49:39] now will will governments eventually get
[01:49:41] powerful AI and and you know there's
[01:49:44] risk of authoritarianism? Yes. Will
[01:49:45] governments eventually get powerful AI
[01:49:47] and there's risk of um uh you know of of
[01:49:51] kind of bad bad bad equilibria? Yes, I
[01:49:54] think both things, but the initial
[01:49:55] conditions matter, right? You know, at
[01:49:58] at some point we're need we're going to
[01:50:00] need to set up the rules of the road.
[01:50:02] I'm not saying that one country, either
[01:50:04] the United States or a coalition of
[01:50:06] democracies, which I think is would be a
[01:50:08] better setup, although it requires more
[01:50:10] international cooperation than we
[01:50:11] currently seem to want to make. Um, but
[01:50:13] you know, I don't I don't think a
[01:50:15] coalition of democracies or or certainly
[01:50:17] one country should just say these are
[01:50:19] the rules of the road. There's going to
[01:50:21] be some negotiation, right? The world is
[01:50:23] going to have to grapple with this. And
[01:50:25] what I would like is that the the the
[01:50:29] democratic nations of the world, those
[01:50:31] with, you know, who are clo whose
[01:50:34] governments have represent closer to
[01:50:36] prohuman values are are holding a
[01:50:39] stronger hand then have have more
[01:50:41] leverage when the rules of the road are
[01:50:43] set. And and so I'm I'm very concerned
[01:50:45] about that initial condition. I um I was
[01:50:47] relisting to an interview from three
[01:50:49] years ago and one of the ways it aged
[01:50:52] poorly is that I kept asking questions
[01:50:53] assuming there's going to be some key
[01:50:55] fulcrum moment two to three years from
[01:50:57] now when in fact being that far out it
[01:51:00] just seems like progress continues AI
[01:51:02] improves AI is more diffused and people
[01:51:04] will use it for more things. It seems
[01:51:06] like you're imagining a world in the
[01:51:07] future where the countries get together
[01:51:09] and here's the rules of the road and
[01:51:10] here's the leverage we have, here's the
[01:51:12] leverage you have when it seems like on
[01:51:14] current trajectory, everybody will have
[01:51:16] more AI. Um, some of that AI will be
[01:51:18] used by authoritarian countries. Some of
[01:51:20] that within the authoritarian countries
[01:51:21] will be by private actors versus state
[01:51:23] actors. It's not clear who will benefit
[01:51:26] more. It's always unpredictable to tell
[01:51:27] tell in advance. You know, it seems like
[01:51:28] the internet privileged authoritarian
[01:51:30] countries more than you would have
[01:51:31] expected. Um, and maybe the AI will be
[01:51:34] the opposite way around. Um so I I I
[01:51:37] want to better understand what you're
[01:51:39] imagining here.
[01:51:40] >> Yeah. Yeah. So so just to be precise
[01:51:41] about it, I think the exponential of the
[01:51:44] underlying technology will continue as
[01:51:46] it has before, right? The models get
[01:51:48] smarter and smarter even when they get
[01:51:50] to country of geniuses in a data center.
[01:51:52] You know, I I think you can continue to
[01:51:54] make the model smarter. There's a
[01:51:56] question of like getting diminishing
[01:51:58] returns on their value in the world,
[01:52:01] right? How much does it matter after
[01:52:03] you've already solved human biology or
[01:52:06] you know you know at some point you can
[01:52:08] do harder math you can do more abstuse
[01:52:10] math problems but nothing after that
[01:52:12] matters but putting that aside I do
[01:52:14] think the the exponential will continue
[01:52:16] but there will be certain distinguished
[01:52:19] points on the exponential and companies
[01:52:23] individuals countries will reach those
[01:52:25] points at different times um and and so
[01:52:28] you know there's there's you know could
[01:52:29] there be some you know you know I talk
[01:52:31] about is a nuclear deterrent still in
[01:52:33] adolescence of technology is a nuclear
[01:52:35] deterrent still stable uh in the world
[01:52:37] of of of AI I don't know but that's
[01:52:39] that's an example of like one thing
[01:52:41] we've taken for granted that like the
[01:52:42] technology could reach such a level that
[01:52:44] it's no longer like you know we can no
[01:52:46] longer be certain of it at least um uh
[01:52:49] you know think of think of others you
[01:52:51] know there there you know there there
[01:52:53] are kind of points where if you if you
[01:52:55] reach a certain point you maybe you have
[01:52:57] offensive cyber dominance and like every
[01:52:59] every computer system is transparent to
[01:53:01] you after that. Um, unless the other
[01:53:04] side has a has a kind of equivalent
[01:53:06] defense. So, I don't know what the
[01:53:08] critical moment is or if there's a
[01:53:10] single critical moment. But I think
[01:53:12] there will be either a critical moment,
[01:53:14] a small number of critical moments or
[01:53:16] some critical window where it's like AI
[01:53:20] is AI confers some large advantage from
[01:53:25] the perspective of national security and
[01:53:28] one country or coalition has reached it
[01:53:31] before others that that you know that
[01:53:34] that that you know I'm not advocating
[01:53:35] that they're just like okay we're in
[01:53:37] charge now. That's not that's not how
[01:53:39] that's not how I think about it. you
[01:53:41] know that there's always the the other
[01:53:42] side is catching up. There's extreme
[01:53:44] actions you're not willing to take and
[01:53:46] and and it's not right to take, you
[01:53:48] know, to take complete um to take
[01:53:51] complete control anyway. But but at at
[01:53:53] the point that that happens, I think
[01:53:55] people are going to understand that the
[01:53:56] world has changed. And there there's
[01:53:58] going to be some negotiation, implicit
[01:54:01] or implicit, about what what is the what
[01:54:04] is the post AI world order look like?
[01:54:07] And and I think my interest is in,
[01:54:11] you know, making that ne negotiation
[01:54:15] be one in which, you know, classical
[01:54:19] liberal democracy has, you know, has a
[01:54:22] strong hand. Well, I want to understand
[01:54:24] what that better means because you say
[01:54:25] in the essay, quote, autocracy is simply
[01:54:28] not a form of government that people can
[01:54:30] accept in the post powerful AI. And that
[01:54:33] sounds like you're saying the CCP as an
[01:54:36] institution cannot exist after we get
[01:54:38] AGI. Um, and that seems like
[01:54:43] a like a very strong demand and it seems
[01:54:45] to imply a world where the leading lab
[01:54:47] or the leading country will be able to
[01:54:51] and by that language should get to
[01:54:53] determine how the world is governed or
[01:54:55] what kinds of governments are allowed
[01:54:58] and not allowed.
[01:55:00] >> Yeah. So when I when I um I I believe
[01:55:03] that paragraph was I think I said
[01:55:06] something like you could take it even
[01:55:08] further and say X. So I wasn't I wasn't
[01:55:10] necessarily endorsing that that that I
[01:55:13] wasn't necessarily endorsing that view.
[01:55:14] I you know I was saying like here's if
[01:55:16] first you know here here's a weaker
[01:55:18] thing that I believe you know I think I
[01:55:20] you know I think I said you know we have
[01:55:21] to worry a lot about authoritarians and
[01:55:24] you know we should try and you know kind
[01:55:25] of kind of check them and limit their
[01:55:27] power. Like you could take this kind of
[01:55:29] further much more interventionist view
[01:55:31] that says like authoritarian countries
[01:55:33] with AI are these you know the the you
[01:55:36] know the these kind of self-fulfilling
[01:55:38] cycles that that you can't that are very
[01:55:40] hard to displace and so you just need to
[01:55:41] get rid of them from from the beginning
[01:55:43] that that has exactly all the problems
[01:55:45] you say which is you know you know if
[01:55:47] you were to make a commitment to
[01:55:49] overthrowing every authoritarian country
[01:55:51] I mean they then they would take a bunch
[01:55:52] of actions now that like you know that
[01:55:54] that that could could lead to
[01:55:56] instability so that that may or you know
[01:55:59] that that just that just may not be
[01:56:01] possible. But the point I was making
[01:56:03] that I do endorse is that it is it is
[01:56:06] quite possible that you know today you
[01:56:10] know the view or at least my view or the
[01:56:13] view in most the western world is is
[01:56:14] democracy is a better form of government
[01:56:16] than authoritarianism. But it's not like
[01:56:18] if a country is authoritarian, we don't
[01:56:21] react the way we reacted if they
[01:56:23] committed a genocide or something,
[01:56:25] right? And and I'm I guess what I'm
[01:56:28] saying is I'm a little worried that in
[01:56:29] the age of AGI, authoritarianism will
[01:56:32] have a different meaning. It will be a
[01:56:34] graver thing. Um and and we have to
[01:56:36] decide one way or another how to h how
[01:56:39] to deal with that. And the
[01:56:40] interventionist view is one possible
[01:56:41] view. I was exploring such views. um you
[01:56:45] know
[01:56:46] it may end up being the right view. It
[01:56:48] it may end up being too extreme to be
[01:56:50] the right view. But I do have hope and
[01:56:52] one piece of hope I have is
[01:56:55] there there is we have seen that as new
[01:56:58] technologies are invented
[01:57:02] forms of government become obsolete. I I
[01:57:05] mentioned this in adolescence of
[01:57:07] technology where I said you know like
[01:57:10] feudalism was basically you know like a
[01:57:11] form of government right and and then
[01:57:13] when when we invented industrialization
[01:57:17] feudalism was no longer sustainable it
[01:57:19] no longer made sense why is that hope
[01:57:22] couldn't that imply that democracy is no
[01:57:24] longer going to be a competitive system
[01:57:26] >> it it could right it could go it could
[01:57:28] go either way right but but I actually
[01:57:31] so I these problems with
[01:57:35] authoritarianism, right? That the
[01:57:37] problems with authoritarianism get
[01:57:39] deeper. I just I wonder if that's an
[01:57:42] indicator of other problems that
[01:57:45] authoritarianism will have, right? In
[01:57:47] other words, people become because
[01:57:51] authoritarianism becomes worse, people
[01:57:53] are more afraid of authoritarianism.
[01:57:55] They work harder to stop it. It's it's
[01:57:58] more of a like you have to think in
[01:58:00] terms of total equilibrium, right? Um, I
[01:58:02] just wonder if it will motivate new ways
[01:58:07] of thinking about with the with with the
[01:58:09] new technology how to preserve and
[01:58:11] protect freedom
[01:58:12] >> and and even more optimistically, will
[01:58:15] it lead to a collective reckoning and,
[01:58:18] you know, a kind of a a more emphatic
[01:58:22] realization of how important some of the
[01:58:24] things we take as individual rights are,
[01:58:26] right? a more emphatic realization that
[01:58:29] we just we really can't give these away.
[01:58:32] There's there we've seen there's no
[01:58:34] other way to live that actually works.
[01:58:36] Um I I I I am actually I am actually
[01:58:40] hopeful that I I guess one way to say it
[01:58:43] it sounds too idealistic but I actually
[01:58:45] believe it could be the case is is that
[01:58:48] is that dictatorships become morally
[01:58:50] obsolete. They become morally unworkable
[01:58:52] forms of government. Um and that and
[01:58:54] that and that the the the the crisis
[01:58:57] that that creates is is is sufficient to
[01:59:00] force us to find another way. Um I I
[01:59:03] think there is genuinely a tough
[01:59:05] question here which I'm not sure how you
[01:59:06] resolve for and we've had to come out
[01:59:09] one way or another on it through history
[01:59:11] right so with China in the 70s and ' 80s
[01:59:13] we decided even though it's an
[01:59:15] authoritarian system we will engage with
[01:59:16] it and I think in retrospect that was
[01:59:18] the right call because it has stayed
[01:59:19] authoritarian system but a billion plus
[01:59:22] people are much wealthier and better off
[01:59:23] than they would have otherwise been um
[01:59:25] and it's not clear that it would have
[01:59:26] stopped being an authoritarian country
[01:59:28] otherwise you can just look at North
[01:59:29] Korea uh as an example of that, right?
[01:59:32] And I don't know if that takes that much
[01:59:34] that much intelligence to remain an
[01:59:36] authoritarian country that continues to
[01:59:39] coales its own power. And so you can
[01:59:40] just imagine a North Korea with an AI
[01:59:43] that's much worse than everybody else's
[01:59:44] but still enough to keep power and and
[01:59:46] and and then so in general it seems like
[01:59:49] should we just have this attitude of the
[01:59:51] benefits of AI will in the form of all
[01:59:53] these empowerments of humanity and
[01:59:55] health and so forth will be big and in
[01:59:58] historically we have decided it's good
[02:00:00] to spread the benefits of technology
[02:00:01] widely even with even to people whose
[02:00:04] governments are authoritarian and I
[02:00:05] think I guess it is a tough question how
[02:00:06] to think about it with AI but um
[02:00:09] historically we have said Yes, this
[02:00:10] there this is a positive some world and
[02:00:12] it's still worth diffusing technology.
[02:00:14] >> Yeah. So so there are a number of
[02:00:15] choices we have. I you know I think
[02:00:17] framing this as a kind of government to
[02:00:20] government decision and and you know in
[02:00:23] in national security terms that's like
[02:00:25] one lens but there are a lot of other
[02:00:27] lenses like you could imagine a world
[02:00:28] where you know we produce all these
[02:00:30] cures to diseases and like the you know
[02:00:32] the the the cures to diseases are fine
[02:00:34] to sell to authoritarian countries. The
[02:00:36] data centers just aren't right. the
[02:00:38] chips and the data centers just aren't
[02:00:40] um and that the AI industry itself. Um
[02:00:43] uh you know like like another
[02:00:44] possibility is and and I think folks
[02:00:47] should think about this like you know
[02:00:49] could there be developments we can make
[02:00:52] either that naturally happen as a result
[02:00:54] of AI or that we could make happen by
[02:00:57] building technology on AI. Could we
[02:00:59] create an equilibrium where where it
[02:01:02] becomes infeasible for authoritarian
[02:01:04] countries to deny their people kind of
[02:01:07] private use of the benefits of the
[02:01:08] technology? Um uh you know are there are
[02:01:11] there are there are there equilibria
[02:01:13] where we can kind of give everyone in
[02:01:15] authoritarian country their own AI model
[02:01:17] that kind of you you know like defends
[02:01:19] themselves from surveillance and there
[02:01:21] isn't a way for the authoritarian
[02:01:23] country to like crack crack down on this
[02:01:25] while while retaining power. I don't
[02:01:27] know that that sounds to me like if that
[02:01:29] went far enough it would be it would be
[02:01:31] a reason why authoritarian countries
[02:01:32] would disintegrate from the inside. Um
[02:01:34] but but maybe there's a middle world
[02:01:36] where like there there's an equilibrium
[02:01:38] where if they want to hold on to power
[02:01:39] the authoritarians can't deny kind of
[02:01:42] individualized access access to the
[02:01:44] technology. But I actually do have a
[02:01:46] hope for the for the um for the for the
[02:01:48] more radical version which is you know
[02:01:50] is it possible that the technology might
[02:01:53] inherently have properties or that by
[02:01:55] building on it in certain ways we could
[02:01:57] create properties um that that that that
[02:02:00] have this kind of dissolving effect on
[02:02:02] authoritarian structures. Now, we we
[02:02:04] hoped originally, if we think back to
[02:02:07] the beginning of the Obama
[02:02:07] administration, we thought originally
[02:02:09] that that, you know, social media and
[02:02:12] and the internet would have that
[02:02:13] property, and it turns out not to. But,
[02:02:15] but I I don't know what what if we could
[02:02:18] uh what if we could try again with with
[02:02:19] the knowledge of how many things could
[02:02:21] go wrong and that this is a different
[02:02:22] technology. I don't know that it would
[02:02:24] work, but it's worth a try.
[02:02:25] >> Yeah. I think it's just it's very
[02:02:27] unpredictable. Like there's first
[02:02:29] principles reasons why authoritarianism.
[02:02:31] >> It's all very unpredictable. I I don't
[02:02:33] think I mean we got to we we just got to
[02:02:35] we kind of we got to recognize the
[02:02:37] problem and then we got to come up with
[02:02:39] 10 things we can try and we got to try
[02:02:40] those and then assess whether they're
[02:02:42] working or which ones are working if any
[02:02:44] and and then try new ones if the old
[02:02:46] ones aren't. I guess what that nets out
[02:02:47] to today is you say we will not sell
[02:02:50] data centers or sorry chips and then the
[02:02:53] ability to make chips to China and so in
[02:02:56] some sense you are denying there would
[02:02:58] be some benefits to that's right the
[02:02:59] Chinese economy Chinese people etc
[02:03:01] because we're doing that and then
[02:03:02] there'd also be benefits to the American
[02:03:04] economy because it's a positive sum
[02:03:05] world we could trade they could have
[02:03:07] their country data centers doing one
[02:03:08] thing we could have ours doing another
[02:03:10] and already we you're saying it's not
[02:03:13] worth that positive sum
[02:03:16] stipend to empower this country's
[02:03:19] >> what what I would say is that you know
[02:03:21] we are we are about to be in a world
[02:03:23] where growth and economic value will
[02:03:26] come very easily if right if we're able
[02:03:28] to build these powerful AI models growth
[02:03:30] and economic value will come very easily
[02:03:32] what will not come easily is
[02:03:34] distribution of benefits distribution of
[02:03:37] wealth political freedom um you know
[02:03:40] these are the things that are going to
[02:03:42] be hard to achieve and so when I think
[02:03:44] about policy
[02:03:45] I think I think that the technology and
[02:03:48] the market will deliver all the
[02:03:50] fundamental benefits, you know, almost
[02:03:52] almost faster than we can take them. Um
[02:03:55] uh and and that these questions about
[02:03:57] about distribution and political freedom
[02:03:59] and rights are are are the ones that
[02:04:01] that will actually matter and that
[02:04:03] policy should focus on. Okay. So
[02:04:05] speaking of distribution, as you're
[02:04:06] mentioning, we have developing countries
[02:04:08] and
[02:04:10] >> um
[02:04:11] >> in many cases catchup growth has weak
[02:04:12] been weaker than we would have hoped
[02:04:13] for. When catchup growth does happen,
[02:04:15] it's fundamentally because they have
[02:04:17] underutilized labor and we can bring the
[02:04:19] capital and knowhow from developed
[02:04:20] countries to these countries and then
[02:04:21] they can grow quite rapidly.
[02:04:23] >> Obviously in a world where labor is no
[02:04:26] longer the constraining factor, this
[02:04:28] mechanism no longer works.
[02:04:30] >> And so is the hope basically to rely on
[02:04:32] philanthropy from the people who
[02:04:34] immediately get wealthy from AI or from
[02:04:35] the countries that get wealthy from AI?
[02:04:37] What what is the hope for? Yeah, I I
[02:04:38] mean philanthropy should obviously play
[02:04:40] some role as it has the you know as has
[02:04:43] in the past but I think growth is always
[02:04:46] growth is always better and stronger if
[02:04:48] we can make it endogenous. So you know
[02:04:50] what are the relevant industries in like
[02:04:52] in like in like in like an AI driven
[02:04:54] world. Look there's lots of stuff you
[02:04:56] know like there's you know I said I said
[02:04:58] we shouldn't build data centers in China
[02:04:59] but there's no reason we shouldn't build
[02:05:01] data centers in Africa right? Um in fact
[02:05:03] I think it'd be great to build data
[02:05:04] centers in Africa. um you know as not
[02:05:06] long as they're not owned by China. We
[02:05:08] should we should build we should build
[02:05:09] data centers in Africa. I think that's a
[02:05:11] that's that's I think that's a great
[02:05:12] thing to do. um you know we should also
[02:05:15] build you know there's no reason we
[02:05:17] can't build you know a pharmaceutical
[02:05:19] industry that's like AIdriven like you
[02:05:21] know the the if if AI is accelerating
[02:05:24] accelerating drug discovery then you
[02:05:26] know there will be a bunch of biotech
[02:05:28] startups like let's make sure some of
[02:05:29] those happen in the developing world and
[02:05:31] certainly during the transition I mean
[02:05:33] we can talk about the point where humans
[02:05:34] have no role but but humans will have
[02:05:36] still have some role in starting up
[02:05:38] these companies and supervising
[02:05:39] supervising the AI models so let's make
[02:05:42] sure some of those humans are humans in
[02:05:43] developing world so that fast growth can
[02:05:45] happen there as well.
[02:05:46] >> You guys recently announced quad is
[02:05:48] going to have a constitution that's
[02:05:49] aligned to a set of values and not
[02:05:50] necessarily just the end user and
[02:05:53] there's a world you can imagine where if
[02:05:54] it is aligned to the end user it
[02:05:56] preserves the balance of power we have
[02:05:57] in the world today because everybody
[02:05:59] gets to have their own AI that's
[02:06:00] advocating for them and so the ratio of
[02:06:03] bad actors to good actors stays
[02:06:04] constant. It seems to work out for our
[02:06:05] world today. Um why is it better not to
[02:06:09] do that but to have a specific set of
[02:06:11] values that the AI should carry forward?
[02:06:14] >> Uh yeah so I'm not sure I'd quite draw
[02:06:17] the distinction in that way. Um there
[02:06:18] there are maybe two relevant
[02:06:20] distinctions here which are I think
[02:06:22] you're talking about a mix of the two
[02:06:24] like one is should we give the model a
[02:06:27] set of instructions about do this and
[02:06:29] versus don't do this
[02:06:31] >> and the other you know versus should we
[02:06:33] give the model a set of principles for
[02:06:35] you know for kind of how to act. Um and
[02:06:38] and and there it's it's you know it's I
[02:06:42] you know it's it's just p it's kind of
[02:06:44] purely a practical and empirical thing
[02:06:46] that we've observed that by teaching the
[02:06:49] model principles getting it to learn
[02:06:51] from principles its behavior is more
[02:06:54] consistent. It's easier to cover edge
[02:06:56] cases and the model is more likely to do
[02:06:58] what people want it to do. In other
[02:07:00] words, if you, you know, if you're like,
[02:07:02] you know, don't tell people how to
[02:07:03] hotwire a car, don't speak in Korea, and
[02:07:06] don't, you know, you know, just, you
[02:07:08] know, if you give it a list of rules, it
[02:07:10] doesn't really understand the rules, and
[02:07:11] it's kind of hard to generalize from
[02:07:13] them. Um, you know, if if it's just kind
[02:07:16] of a like, you know, list of do dos and
[02:07:18] don'ts. Whereas, if you give it
[02:07:20] principles and then, you know, it has
[02:07:21] some hard guard rails like don't make
[02:07:23] biological weapons. But overall you're
[02:07:25] trying to understand
[02:07:27] what it should be aiming to do h how it
[02:07:29] should be aiming to operate. So just
[02:07:31] from a practical perspective that turns
[02:07:33] out to be just a more effective way to
[02:07:34] train the model. That's one piece of it.
[02:07:36] So that you know it's the kind of rules
[02:07:38] versus principles trade-off. Then
[02:07:40] there's another thing you're talking
[02:07:42] about which is kind of like the
[02:07:43] cageability versus um like you know I
[02:07:47] would say kind of intr intrinsic
[02:07:49] motivation trade-off which is like how
[02:07:51] much should the model be a kind of I
[02:07:54] don't know like a a skin suit or
[02:07:56] something where you know you know you
[02:07:58] know you just kind of you know it just
[02:08:00] kind of directly follows the
[02:08:02] instructions that are given to it by
[02:08:03] whoever is giving it those instructions.
[02:08:06] um versus how much should the model have
[02:08:08] an inherent set of values and and go off
[02:08:10] and do things on its own. Um and and and
[02:08:13] and and there I I would actually say
[02:08:17] everything about the model is actually
[02:08:19] closer to the direction of of like you
[02:08:21] know it should mostly do what people
[02:08:23] want. It should mostly follow the we're
[02:08:24] not trying to build something that like
[02:08:26] you know goes off and runs the world on
[02:08:28] its own. We're actually pretty far on
[02:08:30] the corable side. Now, now what we do
[02:08:32] say is there are certain things that the
[02:08:34] model won't do, right? That it's like
[02:08:37] you know that that that I think we say
[02:08:39] it in various ways in the constitution
[02:08:41] that under normal circumstances if
[02:08:43] someone asks the model to do a task it
[02:08:44] should do that task that that should be
[02:08:46] the default. Um but if you've asked it
[02:08:49] [snorts] to do something dangerous or if
[02:08:51] you've you know if you've um asked it to
[02:08:54] um you know uh uh uh to kind of harm
[02:08:58] someone else um then the model is
[02:09:00] unwilling to do that. So I I actually
[02:09:02] think of it as like a mostly a mostly
[02:09:05] corable model that has some limits but
[02:09:07] those limits are based on principles.
[02:09:10] >> Yeah. I mean then the fundamental
[02:09:11] question is how are those principles
[02:09:13] determined? And this is not a special
[02:09:14] question for anthropic. would be a
[02:09:16] question for any company but um
[02:09:19] >> uh because you have been the ones to
[02:09:21] actually write down the principles I get
[02:09:23] to ask you this question normally a
[02:09:25] constitution is like you write it down
[02:09:27] it's set in stone and there's a process
[02:09:29] of updating it and changing it and so
[02:09:32] forth in this case it seems like a
[02:09:34] document that people anthropic write
[02:09:36] that can be changed at any time that
[02:09:38] guides the behavior of systems are going
[02:09:40] to be the basis of a lot of economic
[02:09:43] activity what is H how do you think
[02:09:46] about ho how those principles should be
[02:09:48] set?
[02:09:49] >> Yes. Um so I think there's there's two
[02:09:52] there's maybe three
[02:09:54] three kind of sizes of loop here, right?
[02:09:56] Three three ways to iterate. One is you
[02:09:58] can iterate. We iterate within
[02:09:59] enthropic. We train the model. We're not
[02:10:01] happy with it and we kind of change the
[02:10:02] constitution.
[02:10:03] >> And I think that's good to do. Um and
[02:10:06] you know putting out publicly you know
[02:10:08] making updates to the constitution every
[02:10:09] once in a while saying here's a new
[02:10:10] constitution. I think that's good to do
[02:10:12] because people can comment on it. The
[02:10:14] second level of loop is different
[02:10:15] companies will have different
[02:10:17] constitutions. Um and you know I think
[02:10:20] it's useful for like anthropic puts out
[02:10:21] a constitution and you know you the
[02:10:24] Gemini model puts out a constitution and
[02:10:26] you know other companies put out a
[02:10:28] constitution and then then they can kind
[02:10:29] of look at them compare outside
[02:10:32] observers can critique and say this this
[02:10:34] I like this one this thing from this
[02:10:36] constitution and this thing for that
[02:10:38] constitution and and then kind of that
[02:10:40] that creates some kind of you know soft
[02:10:43] incentive and feedback for all the
[02:10:44] companies to like take the best of each
[02:10:46] elements and improve Then I think
[02:10:48] there's a third loop which is you know
[02:10:50] society beyond the AI companies and
[02:10:52] beyond just those who kind of you know
[02:10:54] who who comment on the constitutions
[02:10:56] without hard power and and there you
[02:10:59] know we've done some experiments like
[02:11:01] you know a couple years ago we did an
[02:11:02] experiment with I think it was called
[02:11:04] the collective intelligence project to
[02:11:06] like um you know to to basically pull
[02:11:09] people and ask them what should be in
[02:11:10] our AI constitution. um uh and and you
[02:11:13] know I think at the time we incorporated
[02:11:16] some of those changes and so you could
[02:11:17] imagine with the new approach we've
[02:11:19] taken to the constitution doing
[02:11:21] something like that it's a little harder
[02:11:23] because it's like that was actually an
[02:11:25] easier approach to take when the
[02:11:26] constitution was like a list of dos and
[02:11:27] don'ts um at the level of principles it
[02:11:30] has to have a certain amount of
[02:11:31] coherence um but but you could you could
[02:11:34] still imagine getting views from a wide
[02:11:36] variety of people and I think you could
[02:11:38] also imagine and this is like a crazy
[02:11:40] idea but hey you know this whole
[02:11:42] interview is about crazy ideas, right?
[02:11:44] So, um uh you know, you could even
[02:11:46] imagine systems of of kind of
[02:11:48] representative government having having
[02:11:50] input, right? Like, you know, I wouldn't
[02:11:52] I wouldn't do this today because the
[02:11:53] legislative process is so slow. Like
[02:11:55] this is exactly why I think we should be
[02:11:57] careful about the legislative process
[02:11:58] and AI regulation. But there's no reason
[02:12:00] you couldn't in principle say like you
[02:12:03] know all AI you know all AI models have
[02:12:06] to have a constitution that starts with
[02:12:07] like these things and then like you can
[02:12:10] append you can append other things after
[02:12:12] it but like there has to be this special
[02:12:14] section that like takes precedence. I
[02:12:16] wouldn't do that. That's too rigid. That
[02:12:17] that sounds um you know that that that
[02:12:20] that sounds kind of overly prescriptive
[02:12:23] in a way that I think overly aggressive
[02:12:25] legislation is. But like that is a thing
[02:12:27] you could you know like like that is
[02:12:28] that is a thing you could try to do. Is
[02:12:30] is there some much less heavy-handed
[02:12:32] version of that? Maybe I really like
[02:12:34] control loop too. um where obviously
[02:12:38] this is not how constitutions of actual
[02:12:40] governments do or should work where
[02:12:42] there there's not this vague sense in
[02:12:43] which the Supreme Court will feel out
[02:12:46] how people are feeling and what are
[02:12:47] their vibes and then update the of the
[02:12:49] constitution accordingly. There's with
[02:12:51] actual governments there's a more
[02:12:52] procedural process. Exactly. But you
[02:12:56] actually have a vision
[02:12:58] >> of competition between constitutions
[02:13:00] which is actually very reminiscent of
[02:13:01] how um
[02:13:02] >> some libertarian charter cities people
[02:13:04] used to talk about what an archipelago
[02:13:07] of different kinds of governments could
[02:13:08] look like and then there would be
[02:13:09] selection among them of who could
[02:13:10] operate the most effectively in which
[02:13:12] place people would be the happiest. And
[02:13:15] in a sense you're actually yeah there's
[02:13:17] this vision. I'm I'm kind of recreating
[02:13:19] that.
[02:13:19] >> Yeah. Yeah. This utopia of archipelago,
[02:13:21] >> you know, again, you know, I think I
[02:13:23] think that vision has has, you know,
[02:13:26] things to recommend it and things that
[02:13:27] things things that will kind of kind of
[02:13:28] go wrong with it. You know, I think I
[02:13:30] think it's a I think it's an interesting
[02:13:32] in some ways compelling vision, but also
[02:13:34] things will go wrong with it that you
[02:13:35] hadn't that you hadn't imagined. So, you
[02:13:38] know, I I I like loop 2 as well, but I I
[02:13:41] I feel like the whole thing has got to
[02:13:43] be some some mix of loops one, two, and
[02:13:46] three. And it's it's a matter of the
[02:13:47] proportions, right? I I think that's got
[02:13:49] to be the the answer.
[02:13:51] >> Um
[02:13:53] >> when somebody eventually writes the
[02:13:54] equivalent of the making of the atomic
[02:13:57] bomb for this era, what is the thing
[02:13:59] that will be hardest to glean from the
[02:14:01] historical record that they're most
[02:14:02] likely to miss? I think a few things.
[02:14:05] One is at every moment of this
[02:14:08] exponential, the extent to which the
[02:14:10] world outside it didn't understand it.
[02:14:12] This is this is a bias that's often
[02:14:14] present in history where anything that
[02:14:15] actually happened looks inevitable in
[02:14:18] retrospect and and so you know I I think
[02:14:21] when people when people look back it
[02:14:24] will be hard for them to put themselves
[02:14:26] in the place of people who were actually
[02:14:30] making a bet on this thing to happen
[02:14:33] that wasn't inevitable that we had these
[02:14:36] arguments like the arguments you know
[02:14:37] that I make for scaling or that
[02:14:39] continual learning will be solved um uh
[02:14:43] uh you know that that you know some of
[02:14:45] us internally in our heads put a high
[02:14:48] probability on this happening but but
[02:14:50] it's like there's there's a world
[02:14:51] outside us that's not that's not acting
[02:14:53] on it's not kind of not acting on that
[02:14:55] at all. Um uh and and and I think I
[02:14:59] think the the weirdness of it um I I I I
[02:15:02] think unfortunately like the insolerity
[02:15:04] of it like you know
[02:15:07] if if we're one year or two years away
[02:15:09] from it happening like the average
[02:15:10] person on the street has no idea and
[02:15:12] that's one of the things I'm trying to
[02:15:13] change like with the memos with talking
[02:15:15] to policy makers but like I don't know I
[02:15:18] think I I I think that's just a that's
[02:15:20] just like a crazy that's just like a
[02:15:22] crazy thing. Yeah. Um, finally I would
[02:15:26] say and and this probably applies to
[02:15:28] almost all historical moments of crisis.
[02:15:31] Um, how absolutely fast it was
[02:15:33] happening, how everything was happening
[02:15:35] all at once. And so decisions that you
[02:15:37] might think, you know, were kind of
[02:15:39] carefully calculated, well, actually you
[02:15:41] have to make that decision and then you
[02:15:43] have to make 30 other decisions on the
[02:15:44] on the same day because it's all
[02:15:46] happening so fast and and you don't even
[02:15:48] know which decisions are going to turn
[02:15:49] out to be consequential. So, you know,
[02:15:52] one of my one of my I guess worries,
[02:15:54] although it's also an insight into into,
[02:15:57] you know, into kind of what's happening
[02:15:59] is that, you know, some very critical
[02:16:01] decision will be will be some decision
[02:16:03] that, you know, someone just comes into
[02:16:05] my office and is like, Dario, you have
[02:16:07] two minutes like, you know, should we
[02:16:09] should we do, you know, should we do
[02:16:11] thing thing A or thing B on this like,
[02:16:13] you know, someone gives me this random,
[02:16:15] you know, half page half page memo and
[02:16:17] is like, should we should we do A or B?
[02:16:20] And I'm like, I don't know. I have to
[02:16:21] eat lunch. Let's do B. And and you know,
[02:16:23] that ends up being the most
[02:16:24] consequential thing ever.
[02:16:26] >> So, final question. Uh, it seems like
[02:16:28] you have
[02:16:30] there's not tech CEOs who are usually
[02:16:33] writing 50page memos every few months,
[02:16:35] and it seems like you have managed to
[02:16:36] build a role for yourself and a company
[02:16:39] around you which is compatible with this
[02:16:42] more intellectual type role of CEO. And
[02:16:47] I want to understand how you construct
[02:16:49] that and how like how does that work to
[02:16:51] be you just go away for a couple weeks
[02:16:54] and then you tell your company this is
[02:16:55] the memo like here's what we're doing.
[02:16:56] It's also reported you write a bunch of
[02:16:57] these internally.
[02:16:58] >> Yeah. So I mean for this particular one
[02:17:00] you know I wrote it over winter break.
[02:17:02] Um uh so it was the time you know and I
[02:17:04] was having a a hard time finding the
[02:17:06] time to actually find it to actually
[02:17:08] write it. But I actually think about
[02:17:09] this in a broader way. Um I actually
[02:17:11] think it relates to the culture of the
[02:17:12] company. So I probably spend a third
[02:17:15] maybe 40% of my time making sure the
[02:17:17] culture of Enthropic is good. As
[02:17:19] Enthropic has gotten larger, it's it's
[02:17:21] gotten harder to just, you know, get
[02:17:24] involved in like, you know, directly
[02:17:25] involved in like the training of the
[02:17:27] models, the launch of the models, the
[02:17:29] building of the products. Like it's 2500
[02:17:30] people. It's like, you know, there's
[02:17:32] just, you know, I have certain
[02:17:33] instincts, but like there's only, you
[02:17:35] know, I it's very difficult to get to
[02:17:37] get to get involved in every single
[02:17:39] detail. You know, I like I I try as much
[02:17:42] as possible, but one thing that's very
[02:17:44] leveraged is making sure Anthropic is a
[02:17:46] good place to work. People like working
[02:17:48] there. Everyone thinks of themselves as
[02:17:50] team members. Everyone works together
[02:17:52] instead of against each other. And you
[02:17:54] know, we've seen as some of the other AI
[02:17:56] companies have grown without naming any
[02:17:58] names, you know, we're starting to see
[02:18:00] decoherence and people fighting each
[02:18:02] other. And you know, I would argue there
[02:18:03] was even a lot of that from the
[02:18:05] beginning, but but you know, that it's
[02:18:06] it's gotten worse. But I I think we've
[02:18:08] done an extraordinarily good job, even
[02:18:11] if not perfect, of holding the company
[02:18:15] together, making everyone feel the
[02:18:17] mission, that we're sincere about the
[02:18:19] mission, and that, you know, everyone
[02:18:21] has faith that everyone else there is
[02:18:22] working for the right reason, that we're
[02:18:24] a team, that people aren't trying to get
[02:18:26] ahead at each other's expense or
[02:18:28] backstab each other, which again, I
[02:18:29] think happens a lot at some of the other
[02:18:31] places. Um, and and how do you make that
[02:18:34] the case? I mean it's a lot of things
[02:18:35] you know it's me it's it's it's Daniela
[02:18:38] who you know runs the company dayto-day
[02:18:40] it's the co-founders it's the other
[02:18:41] people we hire it's the environment we
[02:18:43] try to create but I think an important
[02:18:45] thing in the culture is I some and you
[02:18:49] know the the you know the other leaders
[02:18:51] as well but especially me have to
[02:18:54] articulate what the company is about why
[02:18:57] it's doing what it's doing what its
[02:18:59] strategy is what its values are what its
[02:19:02] mission is and what it stands for And um
[02:19:05] you know when you get to 2500 people you
[02:19:08] can't do that person by person. You have
[02:19:10] to write or you have to speak to the
[02:19:11] whole company. This is why I get up in
[02:19:13] front of the whole company every two
[02:19:15] weeks and speak for an hour. It's
[02:19:17] actually I mean I wouldn't say I write
[02:19:19] essays internally. I do two things. One
[02:19:21] I write this thing called DVQ Dario
[02:19:24] Vision Quest. Um uh uh I wasn't the one
[02:19:26] who named it that. That's the name it it
[02:19:28] it received and it's one of these names
[02:19:29] that I kind of I tried to fight it
[02:19:31] because it made it sound like I was like
[02:19:32] going off and smoking peyote or
[02:19:34] something. Um uh but but the name just
[02:19:36] stuck. Um so I get up in front of the
[02:19:38] company every two weeks. I have like a
[02:19:41] three or four page document and I just
[02:19:43] kind of talk through like three or four
[02:19:45] different topics about what's going on
[02:19:47] internally the you know the the models
[02:19:49] we're producing the products the outside
[02:19:52] industry the world as a whole as it
[02:19:54] relates to AI and geopolitically in
[02:19:56] general you know just some mix of that
[02:19:59] and I just go through very very honestly
[02:20:01] I just go through and I just I just say
[02:20:03] you know this is this is what I'm
[02:20:05] thinking this is what anthropic
[02:20:06] leadership is thinking and then I answer
[02:20:08] questions and and that direct connection
[02:20:11] I think has a lot of value that is hard
[02:20:14] to achieve when you're passing things
[02:20:15] down the chain you know six six levels
[02:20:17] deep um uh and you know large fraction
[02:20:21] of the company comes comes to attend
[02:20:23] either either in person or um either in
[02:20:25] person or virtually and you know it
[02:20:27] really means that you can communicate a
[02:20:29] lot and then the other thing I do is I
[02:20:31] just you know I have a channel in Slack
[02:20:33] where I just write a bunch of things and
[02:20:34] comment a lot um and often that's in
[02:20:37] response to you know just things I'm
[02:20:39] seeing at the company or questions
[02:20:41] people ask or like you know we do
[02:20:44] internal surveys and there are things
[02:20:46] people are concerned about and so I'll
[02:20:48] write them up and I'm like I'm you know
[02:20:50] I'm I'm I'm just I'm very honest about
[02:20:52] these things you know I just I just say
[02:20:54] them very directly and the point is to
[02:20:56] get a reputation of telling the company
[02:20:59] the truth about what's happening to call
[02:21:01] things what they are to acknowledge
[02:21:03] problems to avoid the sort of corpo
[02:21:06] speak the kind of defensive
[02:21:08] communication that often is necessary in
[02:21:11] public because you know the world is
[02:21:13] very large and full of people who are
[02:21:15] you know interpreting things in bad
[02:21:18] faith. Um but you know if you have a
[02:21:20] company of people who you trust and we
[02:21:22] try to hire people that we trust then
[02:21:24] then you know you can you can you can
[02:21:26] you know you can you can really just be
[02:21:28] entirely unfiltered. Um and uh you know
[02:21:31] I think I think that's an enormous
[02:21:32] strength of the company. It makes it a
[02:21:34] better place to work. It makes people
[02:21:35] more you know more the sum of their
[02:21:37] parts and increases likelihood that we
[02:21:39] accomplish the mission because everyone
[02:21:40] is on the same page about the mission
[02:21:42] and everyone is debating and discussing
[02:21:44] how best to accomplish the mission.
[02:21:46] >> Well in lie of an external Dario vision
[02:21:48] quest we have this interview.
[02:21:50] >> This this interview is a little like
[02:21:51] that.
[02:21:52] >> Uh this is fun Dario. Thanks for doing
[02:21:54] it.
[02:21:54] >> Yeah thank you Dash. Hey everybody I
[02:21:56] hope you enjoyed that episode. If you
[02:21:58] did the most helpful thing you can do is
[02:22:00] just share it with other people who you
[02:22:02] think might enjoy it. It's also helpful
[02:22:04] if you leave a rating or a comment on
[02:22:07] whatever platform you're listening on.
[02:22:09] If you're interested in sponsoring the
[02:22:10] podcast, you can reach out [music] at
[02:22:13] dwarcash.com/advertise.
