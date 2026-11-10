# NeurIPS 2024 Test of Time Lecture: Ilya Sutskever — Seq2Seq & Pretraining Era
- **YouTube URL:** https://www.youtube.com/watch?v=WQQdd6qGxNs
- **Lines:** 563

---

[00:00:01] want to thank the
[00:00:03] organizers for choosing a paper for this
[00:00:07] award it was very
[00:00:10] nice and I also want to thank my
[00:00:13] incredible co-authors and collaborators
[00:00:16] oral vineel and qule who stood right
[00:00:20] before you a moment
[00:00:22] ago and what you have here
[00:00:26] is an image a screenshot
[00:00:34] from a similar talk 10 years ago at new
[00:00:37] RPS in 2014 in
[00:00:40] Montreal and it was a much more innocent
[00:00:43] time here we are shown in the
[00:00:46] photos this is the before here's the
[00:00:49] after by the
[00:00:53] way and now we've got more
[00:00:56] experienced hopefully wiser
[00:01:00] but here I'd like to talk a little bit
[00:01:01] about the work itself and maybe a 10year
[00:01:06] retrospective on
[00:01:08] it because a lot of the things in this
[00:01:12] work were correct but some not so much
[00:01:16] and we can review them and we can see
[00:01:18] what happened and how it gently flowed
[00:01:20] to where we are
[00:01:23] today so let's begin by talking about
[00:01:27] what we did and the way we'll do it
[00:01:30] is by showing
[00:01:32] slides from the same talk 10 years
[00:01:37] ago but the summary of what we did is
[00:01:40] the following three bullet points it's
[00:01:42] an auto regressive model train on text
[00:01:45] it's a large neural network and it's a
[00:01:47] large data set and that's it now let's
[00:01:50] dive in into the details a little bit
[00:01:54] more so this was a slide 10 years ago
[00:01:58] not too bad the Deep load
[00:02:01] hypothesis and what we said here is that
[00:02:04] if you have a large neural network with
[00:02:07] 10
[00:02:08] layers then it can do anything that a
[00:02:11] human being can do in a fraction of a
[00:02:14] second like why did we have this
[00:02:16] emphasis emphasis on things that human
[00:02:19] beings can do in a fraction of a second
[00:02:21] why this thing specifically well if you
[00:02:25] believe the Deep learning Dogma so to
[00:02:28] say that artificial neurons and
[00:02:30] biological neurons are similar or at
[00:02:31] least not too
[00:02:33] different and you believe that real
[00:02:35] neurons are slow than anything that we
[00:02:37] can do quickly by we I mean human beings
[00:02:40] I even mean just one human in the entire
[00:02:42] world if there is one human in the
[00:02:44] entire world that can do some task in a
[00:02:46] fraction of a second then a 10 layer
[00:02:48] neural network can do it too right it
[00:02:50] follows you just take their connections
[00:02:52] and you embed them inside your neuronet
[00:02:54] the artificial one so this was the
[00:02:57] motivation anything that a human being
[00:02:58] can do in a fraction of a second second
[00:03:00] a big 10 10 layer neural network can do
[00:03:01] too we focused on 10 layer neural
[00:03:04] networks because this was the neural
[00:03:06] networks we knew how to train back in
[00:03:08] the
[00:03:09] day if you could go beyond in your
[00:03:12] layers somehow then you could do more
[00:03:15] but back then we could only do 10 layers
[00:03:17] which is why we emphasized whatever
[00:03:20] human beings can do in a fraction of a
[00:03:23] second a different slide from the talk a
[00:03:25] slide which says our main idea and you
[00:03:28] may be able to recognize two things or
[00:03:29] at least one thing you might be able to
[00:03:31] recognize that something Auto regressive
[00:03:33] is going on here what is it saying
[00:03:36] really what does this slide really say
[00:03:38] this slide says that if you have an auto
[00:03:41] regressive
[00:03:42] model and it predicts the next token
[00:03:45] well enough then it will in fact grab
[00:03:48] and capture and grasp the correct
[00:03:50] distribution over whatever over
[00:03:52] sequences that come next and this was a
[00:03:54] relatively new thing it wasn't literally
[00:03:57] the first
[00:03:58] ever Auto regressive neural network but
[00:04:01] I would argue it was the first Auto
[00:04:03] regressive neural network where we
[00:04:05] really believed that if you train it
[00:04:07] really well then you will get whatever
[00:04:09] you want in our case back then was the
[00:04:12] humble today humble then incredibly
[00:04:14] audacious task of
[00:04:16] translation now I'm going to show you
[00:04:18] some ancient history that many of you
[00:04:20] might have never seen before it's called
[00:04:22] the
[00:04:24] lstm to those unfamiliar an lstm is the
[00:04:28] things that poor deplan researchers did
[00:04:31] before
[00:04:32] Transformers and it's basically a res
[00:04:35] net but rotated 90° so that's an
[00:04:40] lsdm and it came before it's
[00:04:43] like it's like kind of like a slightly
[00:04:45] more complicated reset you can see there
[00:04:47] is your integrator which is now called
[00:04:51] the residual stream but you've got some
[00:04:53] multiplication going on it's a little
[00:04:55] bit more
[00:04:55] complicated but that's what we did it
[00:04:58] was a reset Ro
[00:05:01] 90° another cool feature from that Old
[00:05:04] talk that I want to highlight is that we
[00:05:05] used parallelization but not just any
[00:05:09] parallelization we used
[00:05:11] pipelining as witnessed by this one
[00:05:14] layer per
[00:05:16] GPU was it wise to pipeline as we now
[00:05:19] know pipelining is not wise but we were
[00:05:22] not as wise back then so we used that
[00:05:25] and we got a 3.5x speed up using eight
[00:05:28] gpus
[00:05:32] and the conclusion slide in some sense
[00:05:35] the conclusion slide from the talk from
[00:05:36] back then is the most important slide
[00:05:39] because it spelled out what could
[00:05:41] arguably be the beginning of the scaling
[00:05:45] hypothesis right that if you have a very
[00:05:47] big data set and you train a very big
[00:05:49] neural network then success is
[00:05:51] guaranteed and one can argue if one is
[00:05:54] charitable that this indeed has been
[00:05:58] what's been happening
[00:06:01] I want to mention one other idea and
[00:06:05] this is I claim the idea that truly
[00:06:07] stood the test of time it's the core
[00:06:09] idea of deploying itself it's the idea
[00:06:11] of connectionism it's the idea that if
[00:06:14] you allow yourself to
[00:06:17] believe that an artificial neuron is
[00:06:21] kind of sort
[00:06:23] of like a biological
[00:06:26] neuron right if you believe that one is
[00:06:29] kind of sort like the
[00:06:32] other then it gives you the confidence
[00:06:36] to believe that very large neural
[00:06:37] networks they don't need to be literally
[00:06:39] human brain scale they might be a little
[00:06:41] bit smaller but you could configure them
[00:06:44] to do pretty much all the
[00:06:46] things that we do human beings there's
[00:06:50] still a difference oh I forgot to the
[00:06:52] end there is still a difference because
[00:06:55] the human brain also figures out how to
[00:06:57] reconfigure itself whereas we are using
[00:07:00] the best learning algorithms that we
[00:07:02] have which
[00:07:04] require as many data points as there are
[00:07:07] parameters human beings are still better
[00:07:09] in this
[00:07:10] regard but what this led so I claim
[00:07:16] arguably to the age of pre-training and
[00:07:19] the age of pre-training is what we might
[00:07:21] say the gpt2 model the gpt3 model the
[00:07:25] scaling laws and I want to specifically
[00:07:28] call out my former collaborators Alec
[00:07:31] Radford also Jared Kaplan Dario
[00:07:36] mode for really making this
[00:07:39] work but that led to the age of
[00:07:41] pre-training and this is what's been the
[00:07:43] driver of all of progress all the
[00:07:45] progress that we see today extra large
[00:07:48] neural
[00:07:49] networks extraordinar large neural
[00:07:51] networks trained on huge data
[00:07:55] sets but pre-training as we know it will
[00:07:58] unquestionably end
[00:08:00] pre-training will end why will it end
[00:08:04] because while computers growing through
[00:08:06] better Hardware better
[00:08:09] algorithms and logic clusters right all
[00:08:12] those things keep increasing your
[00:08:15] compute all these things keep increasing
[00:08:17] your compute the data is not
[00:08:20] growing because we have but one
[00:08:23] internet we have but one
[00:08:26] internet you could even say you can even
[00:08:28] go as far as to say that data is the
[00:08:31] fossil fuel of
[00:08:33] AI it was like created
[00:08:36] somehow and now we use
[00:08:39] it and we've achieved Peak data and
[00:08:44] there'll be no more we have to deal with
[00:08:46] the data that we have now it still still
[00:08:48] let us go quite far but this
[00:08:52] is there's only one
[00:08:56] internet so here I'll take um a bit of
[00:09:00] Liberty to speculate about what comes
[00:09:02] next actually I don't need to speculate
[00:09:04] because many people are speculating too
[00:09:06] and I'll mention their
[00:09:08] speculations you may have heard the
[00:09:10] phrase agents it's common and I'm sure
[00:09:13] that eventually something will happen
[00:09:16] but people feel like something agents is
[00:09:18] the
[00:09:20] future more concretely but also a little
[00:09:23] bit vaguely synthetic data but what does
[00:09:26] synthetic data mean figuring this out is
[00:09:28] a big challenge
[00:09:30] and I'm sure that different people have
[00:09:32] all kinds of interesting progress there
[00:09:35] and an inference time compute or maybe
[00:09:37] what's been most recently most vividly
[00:09:39] seen in 01 the o1 model these are all
[00:09:42] examples of things of people trying to
[00:09:45] figure
[00:09:46] out what to do after
[00:09:48] pre-training and those are all very good
[00:09:50] things to
[00:09:52] do I want to mention one other example
[00:09:56] from biology which I think is really
[00:09:58] cool
[00:10:00] and the example is this so about many
[00:10:04] many years ago at this conference also I
[00:10:07] saw a talk where someone presented this
[00:10:09] graph but the graph showed the
[00:10:12] relationship between the size of the
[00:10:16] body
[00:10:18] of the size of the body of a mammal and
[00:10:21] the size of their brain in this case
[00:10:24] it's in mass and the that talk I
[00:10:27] remember vividly they were saying look
[00:10:29] it's in biology everything is so messy
[00:10:31] but here you have one rare example where
[00:10:33] there is a very tight relationship
[00:10:36] between the size of the body of the
[00:10:38] animal and their brain and totally
[00:10:41] randomly I became curious at this graph
[00:10:43] and one of the early one of the early so
[00:10:46] I went to Google to do research to to
[00:10:48] look for this graph and one of the
[00:10:50] images and Google Images was this and
[00:10:53] the interesting thing in this
[00:10:55] image is you see like I don't know is
[00:10:58] the mouse work working oh yeah the mouse
[00:11:00] is working great so you've got this
[00:11:02] mammals right all the different
[00:11:05] mammals then you've got nonhuman
[00:11:07] primates it's basically the same thing
[00:11:10] but then you've got the hominids and to
[00:11:12] my knowledge hominids are like close
[00:11:16] relatives to the humans in
[00:11:19] evolution like the
[00:11:24] neand there's a bunch of them like it's
[00:11:27] called homohabilis maybe there a whole
[00:11:29] bunch and they're all here and what's
[00:11:33] interesting is that they have a
[00:11:35] different slope on their brain to body
[00:11:38] scaling
[00:11:40] exponent so that's pretty cool what that
[00:11:43] means is that there is a precedent there
[00:11:46] is an example
[00:11:49] of biology figuring out some kind of
[00:11:53] different scaling something clearly is
[00:11:56] different so I think that is cool and by
[00:11:58] the way I want to highlight highl light
[00:12:00] this xaxis is log scale you see this is
[00:12:02] 100 this is a th000 10,000 100,000 and
[00:12:06] likewise in grams 1 g 10 G 100 g th000
[00:12:13] g
[00:12:15] so it is possible for things to be
[00:12:17] different the things that we are doing
[00:12:19] the things that we've been scaling so
[00:12:20] far is actually the first thing that we
[00:12:22] figured out how to scale and without
[00:12:25] doubt the field everyone who's working
[00:12:28] here will figure out
[00:12:30] what to do but I want to talk here I
[00:12:33] want to take a few minutes and speculate
[00:12:36] about the longer term the longer term
[00:12:38] where are we all headed right we're
[00:12:40] making all this progress it's an it's
[00:12:42] astounding progress It's really I
[00:12:47] mean those of you who' have been in the
[00:12:49] field 10 years ago and you remember just
[00:12:51] how incapable everything has
[00:12:55] been like yes you can say even if you
[00:12:58] kind of say of course learning still to
[00:13:00] see it is just
[00:13:02] unbelievable it's
[00:13:04] completely I can't convey that feeling
[00:13:06] to
[00:13:07] you you know if you joined the field in
[00:13:09] the last two years then of course you
[00:13:11] speak to computers and they talk back to
[00:13:13] you and they disagree and that's what
[00:13:15] computers are but it hasn't always been
[00:13:18] the case but I want to talk to a little
[00:13:21] bit about super intelligence just a bit
[00:13:24] cuz that is obviously where this field
[00:13:27] is headed this is obviously what's being
[00:13:29] built here and the thing about super
[00:13:32] intelligence is that it will be
[00:13:33] different qualitatively from what we
[00:13:37] have and my goal in the next minute to
[00:13:40] try to give
[00:13:42] you some concrete intuition of how it
[00:13:45] will be different so that you yourself
[00:13:47] could reason about
[00:13:48] it so right now we have our incredible
[00:13:51] language models and the unbelievable
[00:13:53] chat bot and they can even do things but
[00:13:54] they're also kind of strangely
[00:13:57] unreliable and they get confused
[00:13:59] when while also
[00:14:01] having dramatically superhuman
[00:14:04] performance on evals so it's really
[00:14:06] unclear how to reconcile this but
[00:14:09] eventually sooner or later the following
[00:14:13] will be achieved those systems are
[00:14:15] actually going to be agentic in a real
[00:14:17] ways whereas right now the systems are
[00:14:19] not agents in any meaningful sense just
[00:14:22] very that might be too strong they're
[00:14:24] very very slightly agentic just
[00:14:27] beginning it will actually reason and by
[00:14:30] the way I want to mention something
[00:14:31] about reasoning is that a system that
[00:14:35] reasons the more it reasons the more
[00:14:37] unpredictable it becomes the more it
[00:14:40] reasons the more unpredictable it
[00:14:41] becomes all the Deep learning that we've
[00:14:43] been used to is very predictable because
[00:14:45] if you've been working on replicating
[00:14:47] human intuition essentially it's like
[00:14:49] the gut fi if you come back to the 0.1
[00:14:53] second reaction time what kind of
[00:14:55] processing we do in our brains well
[00:14:59] it's our intuition so we've endowed
[00:15:02] ouris with some of that intuition but
[00:15:05] reasoning you're seeing some early signs
[00:15:07] of that reasoning is unpredictable and
[00:15:10] one reason to see that is because the
[00:15:11] chess AIS the really good ones are
[00:15:14] unpredictable to the best human chess
[00:15:16] players so we will have to be dealing
[00:15:20] with AI systems that are incredibly
[00:15:23] unpredictable they will understand
[00:15:25] things from limited data they will not
[00:15:27] get confused all the things which are
[00:15:29] really big limitations I'm not saying
[00:15:31] how by the way and I'm not saying when
[00:15:34] I'm saying that it
[00:15:36] will and when all those things will
[00:15:38] happen together with
[00:15:40] self-awareness because why not
[00:15:42] self-awareness is useful it is part your
[00:15:45] ourselves are parts of our own world
[00:15:48] models when all those things come
[00:15:50] together we will have systems of
[00:15:52] radically different qualities and
[00:15:54] properties that exist today and of
[00:15:56] course they will have incredible and
[00:15:58] amazing capabili is but the kind of
[00:16:00] issues that come up with systems like
[00:16:01] this and I'll just leave it as an
[00:16:03] exercise to um
[00:16:06] imagine it's very different from what we
[00:16:08] used to
[00:16:12] and I would say that it's definitely
[00:16:15] also impossible to predict the future
[00:16:18] really all kinds of stuff is possible
[00:16:22] but on this uplifting note I will
[00:16:25] conclude thank you so much um
[00:16:31] [Applause]
[00:16:33] [Music]
[00:16:35] [Applause]
[00:16:44] thank
[00:16:45] you um now in
[00:16:47] 2024 are there other biological
[00:16:50] structures that are part of human
[00:16:52] cognition that you think are worth
[00:16:54] exploring in a similar way or that
[00:16:57] you're interested in anyway
[00:17:03] so the way I'd answer this
[00:17:05] question is that if you are or someone
[00:17:10] is a person who has a specific insight
[00:17:12] about hey we are all being extremely
[00:17:16] silly because clearly the brain does
[00:17:18] something and we are
[00:17:19] not and that's something that can be
[00:17:21] done they should pursue it I personally
[00:17:25] don't
[00:17:29] well depends on the level of abstraction
[00:17:31] you're looking at maybe I'll answer it
[00:17:32] this way like there's been a lot of
[00:17:34] desire to make biologically inspired Ai
[00:17:38] and you could argue on some level that
[00:17:40] biologically inspired AI is incredibly
[00:17:42] successful which is all of the learning
[00:17:44] biologically inspired AI but on the
[00:17:46] other hand the biological inspiration
[00:17:48] was very very very modest it's like
[00:17:50] let's use neurons this is the full
[00:17:53] extent of the biological inspiration
[00:17:55] let's use
[00:17:56] neurons and more detailed bi iCal
[00:17:59] inspiration has been very hard to come
[00:18:01] by but I wouldn't rule it out I think if
[00:18:04] someone has a special Insight they might
[00:18:06] be able to to see something and that
[00:18:08] would be
[00:18:11] useful I have a question for you um
[00:18:14] about sort of autocorrect um so here is
[00:18:18] here's the question you mentioned
[00:18:19] reasoning as being um one of the core
[00:18:23] aspects of maybe the modeling in the
[00:18:25] future and maybe a differentiator
[00:18:29] um what we saw in some of the poster
[00:18:31] sessions is that hallucinations in
[00:18:33] today's models are the way we're
[00:18:36] analyzing I mean maybe you correct me
[00:18:37] you're the expert on this but the way
[00:18:39] we're analyzing whether a model is
[00:18:41] hallucinating today without because we
[00:18:43] know of the dangers of models not being
[00:18:45] able to reason that we're using a
[00:18:47] statistical analysis let's say some
[00:18:50] amount of standard deviations or
[00:18:51] whatever away from the mean in the
[00:18:54] future wouldn't it would do you think
[00:18:57] that a model given reasoning will be
[00:19:00] able to correct itself sort of
[00:19:01] autocorrect itself and that will be a
[00:19:04] core feature of Future model so that
[00:19:07] there won't be as many hallucinations
[00:19:09] because the model will recognize when I
[00:19:11] maybe that's too esoteric of a question
[00:19:13] but the model will be able to reason and
[00:19:15] understand when a Hallucination is
[00:19:16] occurring does the question make sense
[00:19:18] yes and the answer is also yes I think
[00:19:21] what you described is extremely highly
[00:19:24] plausible yeah I mean you should check I
[00:19:27] mean for yeah it's I wouldn't I wouldn't
[00:19:29] rule out that it might already be
[00:19:31] happening with some of the you know
[00:19:33] early reasoning models of today I don't
[00:19:36] know but longer term why not yeah I mean
[00:19:39] it's part part of like Microsoft Word
[00:19:41] like autocorrect it's a you know it's a
[00:19:43] it's a core feature yeah I just I mean I
[00:19:46] think calling it autocorrect is really
[00:19:48] doing any disservice I think you are
[00:19:51] when you say autocorrect you evoke
[00:19:55] like it's far grander than autocorrect
[00:19:58] but other than but you know this point
[00:19:59] aside the answer is yes thank
[00:20:03] you hiia I loved the ending uh
[00:20:08] mysteriously uh leaving out do they
[00:20:11] replace us or are they you know Superior
[00:20:13] do they need rights you know it's a new
[00:20:15] species of homo sapien spawned
[00:20:19] intelligence so maybe they need I mean
[00:20:21] uh I think the RL guy uh thinks they
[00:20:24] think uh you know we need rights for
[00:20:26] these things I have a UNR question to
[00:20:30] that how do you how do you create the
[00:20:32] right incentive mechanisms for Humanity
[00:20:35] to actually create it in a way that
[00:20:39] gives it the freedoms that we have as
[00:20:42] Homo
[00:20:45] sapiens you know I feel like this in
[00:20:48] some in some in some sense those are
[00:20:50] those are the kind of questions that
[00:20:52] people should be uh reflecting on
[00:20:55] more but
[00:21:05] to your question about what incentive
[00:21:07] structure should we create I I don't
[00:21:10] feel that I know I don't feel confident
[00:21:12] answering questions like this
[00:21:15] because uh it's like you're talking
[00:21:17] about creating some kind of a top down
[00:21:20] structure government thing I don't know
[00:21:23] it could be a cryptocurrency too yeah I
[00:21:26] mean there's bit tensor you know those
[00:21:29] things I don't feel like I am the right
[00:21:32] person to comment on
[00:21:34] cryptocurrency but
[00:21:39] but you know there is a chance by the
[00:21:42] way what what you're describing will
[00:21:43] happen that indeed we will have you know
[00:21:46] in some sense it's it's it's not a bad
[00:21:49] end result if you have AIS and all they
[00:21:53] want is to coexist with
[00:21:55] us and also just to have rights maybe
[00:21:58] that will be fine
[00:22:00] it's but I don't know I mean I think
[00:22:03] things are so incredibly unpredictable I
[00:22:05] I hesitate to comment but I encourage
[00:22:06] the speculation thank you uh and uh yeah
[00:22:10] thank you for the talk it's really
[00:22:12] awesome hi there thank you for the great
[00:22:15] talk my name is shalev liit from
[00:22:17] University of Toronto working with
[00:22:20] Sheila thanks for all the work you've
[00:22:22] done I wanted to ask do you think llms
[00:22:26] generalize multihop Reon reasoning out
[00:22:29] of
[00:22:32] distribution so okay the question
[00:22:36] assumes that the answer is yes or no but
[00:22:39] the question should not be answered with
[00:22:41] yes or no because what does it mean out
[00:22:44] of distribution generalization what does
[00:22:46] it mean what does it mean in
[00:22:48] distribution and what does it mean out
[00:22:49] of distribution because it's a test of
[00:22:52] time talk I'll say that long long
[00:22:56] ago before people were using deep
[00:22:59] learning they were using things like
[00:23:01] string matching engrams for machine
[00:23:04] translation people were using
[00:23:06] statistical phrase tables can you
[00:23:09] imagine they had tens of thousands of
[00:23:11] code of complexity which was I mean it's
[00:23:15] it was truly
[00:23:16] unfathomable and back then
[00:23:20] generalization meant is it literally not
[00:23:23] in this the same phrasing as in the data
[00:23:25] set now we may say well my model
[00:23:29] achieves this high score on um I don't
[00:23:32] know math competitions but maybe the
[00:23:34] math maybe some discussion in some Forum
[00:23:37] on the internet was about the same ideas
[00:23:39] and therefore it's memorized well okay
[00:23:41] you could say maybe it's in distribution
[00:23:43] maybe it's
[00:23:44] memorization but I also think that our
[00:23:46] standards for what counts as
[00:23:47] generalization have increased really
[00:23:50] quite substantially dramatically
[00:23:52] unimaginably if you keep
[00:23:54] track
[00:23:56] and so I think then answer is to some
[00:24:00] degree probably not as well as human
[00:24:02] beings I think it is true that human
[00:24:04] beings generalize much better but at the
[00:24:08] same time they definitely generalize out
[00:24:10] of distribution to some
[00:24:12] degree I hope it's a useful topological
[00:24:16] answer thank
[00:24:18] you and unfortunately we're out of time
[00:24:22] for this session I have a feeling we
[00:24:23] could go on for the next six hours uh
[00:24:26] but thank you so much Ilia for the talk
[00:24:28] thank you wonderful
[00:24:32] [Applause]
[00:24:34] [Music]
