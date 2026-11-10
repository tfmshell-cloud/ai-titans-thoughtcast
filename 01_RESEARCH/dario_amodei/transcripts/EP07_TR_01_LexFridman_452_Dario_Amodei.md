# Lex Fridman Podcast #452: Dario Amodei — Anthropic Team, Claude, AGI & Biosecurity
- **YouTube URL:** https://www.youtube.com/watch?v=ugvHCXCOmm4
- **Lines:** 8690

---

[00:00:02] if you extrapolate the curves that we've
[00:00:02] had so far right if if you say well I
[00:00:04] don't know we're starting to get to like
[00:00:06] PhD level and and last year we were at
[00:00:08] undergraduate level and the year before
[00:00:10] we were at like the level of a high
[00:00:12] school student again you can you can
[00:00:14] quibble with at what tasks and for what
[00:00:17] we're still missing modalities but those
[00:00:18] are being added like computer use was
[00:00:20] added like image generation has been
[00:00:22] added if you just kind of like eyeball
[00:00:24] the rate at which these capabilities are
[00:00:26] increasing it does make you think that
[00:00:29] we'll get there by 2026 or 2027 I think
[00:00:32] there are still worlds where it doesn't
[00:00:33] happen in in a 100 years those world the
[00:00:36] number of those worlds is rapidly
[00:00:37] decreasing we are rapidly running out of
[00:00:40] truly convincing blockers truly
[00:00:43] compelling reasons why this will not
[00:00:44] happen in the next few years the scale
[00:00:46] up is very quick like we we do this
[00:00:48] today we make a model and then we deploy
[00:00:50] thousands maybe tens of thousands of
[00:00:52] instances of it I think by the time you
[00:00:55] know certainly within two to three years
[00:00:57] whether we have these super powerful AIS
[00:00:58] or not ERS are going to get to the size
[00:01:01] where you'll be able to deploy millions
[00:01:02] of these I am optimistic about meaning I
[00:01:06] worry about economics and the
[00:01:09] concentration of power that's actually
[00:01:10] what I worry about more the abuse of
[00:01:13] power and AI increases the amount of
[00:01:17] power in the world and if you
[00:01:18] concentrate that power and abuse that
[00:01:20] power it can do immeasurable damage yes
[00:01:23] it's very frightening it's very it's
[00:01:24] very
[00:01:26] frightening the following is a
[00:01:28] conversation with Dario amade CEO of
[00:01:32] anthropic the company that created
[00:01:34] Claude that is currently and often at
[00:01:36] the top of most llm Benchmark leader
[00:01:39] boards on top of that Dario and the
[00:01:41] anthropic team have been outspoken
[00:01:44] advocates for taking the topic of AI
[00:01:46] safety very seriously and they have
[00:01:49] continued to publish a lot of
[00:01:51] fascinating AI research on this and
[00:01:54] other topics I'm also joined afterwards
[00:01:57] by two other brilliant people from
[00:01:59] propic first Amanda ascal who is a
[00:02:03] researcher working on alignment and
[00:02:06] fine-tuning of Claude including the
[00:02:08] design of claude's character and
[00:02:10] personality a few folks told me she has
[00:02:13] probably talked with Claude more than
[00:02:15] any human at anthropic so she was
[00:02:19] definitely a fascinating person to talk
[00:02:21] to about prompt engineering and
[00:02:23] practical advice on how to get the best
[00:02:25] out of Claude after that chrisa stopped
[00:02:29] by for chat he's one of the pioneers of
[00:02:32] the field of mechanistic
[00:02:34] interpretability which is an exciting
[00:02:36] set of efforts that aims to reverse
[00:02:38] engineer neural networks to figure out
[00:02:41] what's going on inside inferring
[00:02:44] behaviors from neural activation
[00:02:46] patterns inside the network this is a
[00:02:49] very promising approach for keeping
[00:02:52] future super intelligent AI systems safe
[00:02:55] for example by detecting from the
[00:02:57] activations when the model is trying to
[00:02:59] deceive the human it is talking
[00:03:02] to this is Alex Freedman podcast to
[00:03:05] support it please check out our sponsors
[00:03:07] in the description and now dear friends
[00:03:11] here's Dario
[00:03:13] amade let's start with a big idea of
[00:03:15] scaling laws and the scaling hypothesis
[00:03:17] what is it what is its history and where
[00:03:20] do we stand today so I can only describe
[00:03:23] it as it you know as it relates to kind
[00:03:25] of my own experience but I've been in
[00:03:27] the AI field for about uh 10 years and
[00:03:30] it was something I noticed very early on
[00:03:32] so I first joined the AI world when I
[00:03:34] was uh working at BYU with Andrew in in
[00:03:36] late 2014 which is almost exactly 10
[00:03:39] years ago now and the first thing we
[00:03:42] worked on was speech recognition systems
[00:03:45] and in those days I think deep learning
[00:03:47] was a new thing it had made lots of
[00:03:48] progress but everyone was always saying
[00:03:51] we don't have the algorithms we need to
[00:03:52] succeed you know we we we we're we're
[00:03:54] not we're only matching a tiny tiny
[00:03:57] fraction there's so much we need to kind
[00:03:59] of discover algorithmically we haven't
[00:04:01] found the picture of how to match the
[00:04:03] human brain uh and when you know in some
[00:04:07] ways was fortunate I was kind of you
[00:04:09] know you can have almost beginner's luck
[00:04:10] right I was like a a newcomer to the
[00:04:12] field and you know I looked at the
[00:04:14] neural net that we were using for speech
[00:04:16] the recurrent neural networks and I said
[00:04:18] I don't know what if you make them
[00:04:19] bigger and give them more layers and
[00:04:21] what if you scale up the data along with
[00:04:23] this right I just saw these as as like
[00:04:25] independent dials that you could turn
[00:04:27] and I noticed that the model started to
[00:04:29] do better and better as you gave them
[00:04:31] more data as you as you made the models
[00:04:34] larger as you trained them for longer um
[00:04:36] and I I didn't measure things precisely
[00:04:39] in those days but but along with with
[00:04:41] colleagues we very much got the informal
[00:04:43] sense that the more data and the more
[00:04:46] compute and the more training you put
[00:04:48] into these models the better they
[00:04:50] perform and so initially my thinking was
[00:04:53] hey maybe that is just true for speech
[00:04:55] recognition systems right maybe maybe
[00:04:57] that's just one particular quirk one
[00:04:59] particular area I think it wasn't until
[00:05:02] 2017 when I first saw the results from
[00:05:05] gpt1 that it clicked for me that
[00:05:08] language is probably the area in which
[00:05:10] we can do this we can get trillions of
[00:05:13] words of language data we can train on
[00:05:16] them and the models we were training in
[00:05:18] those days were tiny you could train
[00:05:19] them on one to eight gpus whereas you
[00:05:22] know now we train jobs on tens of
[00:05:24] thousands soon going to hundreds of
[00:05:26] thousands of gpus and so when I when I
[00:05:28] saw those two things together um and you
[00:05:31] know there were a few people like ilaser
[00:05:33] who who you've interviewed who had
[00:05:35] somewhat similar reviews right he might
[00:05:37] have been the first one although I think
[00:05:39] a few people came to came to similar
[00:05:41] views around the same time Right There
[00:05:42] Was You Know Rich Sutton's bitter lesson
[00:05:44] there was gur wrote about the scaling
[00:05:47] hypothesis but I think somewhere between
[00:05:49] 2014 and 2017 was when it really clicked
[00:05:53] for me when I really got conviction that
[00:05:55] hey we're going to be able to do these
[00:05:57] incredibly wide cognitive tasks if we
[00:06:00] just if we just scale up the models and
[00:06:03] at at every stage of scaling there are
[00:06:06] always arguments and you know when I
[00:06:07] first heard them honestly I thought
[00:06:09] probably I'm the one who's wrong and you
[00:06:11] know all these all these experts in the
[00:06:12] field are right they know the situation
[00:06:14] better better than I do right there's
[00:06:16] you know the Chomsky argument about like
[00:06:18] you can get syntactics but you can't get
[00:06:20] semantics there's this idea oh you can
[00:06:22] make a sentence make sense but you can't
[00:06:24] make a paragraph makes sense the latest
[00:06:26] one we have today is uh you know we're
[00:06:29] going to run out of data or the data
[00:06:30] isn't high quality enough or models
[00:06:32] can't reason and and each time every
[00:06:35] time we manage to we manage to either
[00:06:37] find a way around or scaling just is the
[00:06:39] way around um sometimes it's one
[00:06:42] sometimes it's the other uh and and so
[00:06:44] I'm now at this point I I I still think
[00:06:47] you know it's it's it's always quite
[00:06:48] uncertain we have nothing but inductive
[00:06:50] inference to tell us that the next few
[00:06:53] years are going to be like the next the
[00:06:54] last 10 years but but I've seen I've
[00:06:57] seen the movie enough times I've seen
[00:06:59] the story happen for for enough times to
[00:07:01] to really believe that probably the
[00:07:04] scaling is going to continue and that
[00:07:05] there's some magic to it that we haven't
[00:07:08] really explained on a theoretical basis
[00:07:10] yet and of course the scaling here is
[00:07:13] bigger networks bigger data bigger
[00:07:15] compute yes all in in particular linear
[00:07:19] scaling up of bigger networks bigger
[00:07:23] training times and uh more and and more
[00:07:26] data uh so all of these things almost
[00:07:28] like a chemical reaction you know you
[00:07:30] have three ingredients in the chemical
[00:07:31] reaction and you need to linearly scale
[00:07:34] up the three ingredients if you scale up
[00:07:35] one not the others you run out of the
[00:07:37] other reagents and and the reaction
[00:07:39] stops but if you scale up everything
[00:07:42] everything in series then then the
[00:07:44] reaction can proceed and of course now
[00:07:46] that you have this kind of empirical
[00:07:48] scienceart you can apply it to
[00:07:51] other uh more nuanced things like
[00:07:53] scaling laws applied to interpretability
[00:07:56] or scaling laws applied to posttraining
[00:07:58] or just seeing how does this thing scale
[00:08:01] but the big scaling law I guess the
[00:08:03] underlying scaling hypothesis has to do
[00:08:06] with big networks Big Data leads to
[00:08:08] intelligence yeah we've we've documented
[00:08:11] scaling laws in lots of domains other
[00:08:13] than language right so uh initially the
[00:08:17] the paper we did that first showed it
[00:08:18] was in early 2020 where we first showed
[00:08:21] it for language there was then some work
[00:08:23] late in 2020 where we showed the same
[00:08:26] thing for other modalities like images
[00:08:29] video
[00:08:30] text to image image to text math they
[00:08:33] all had the same pattern and and you're
[00:08:35] right now there are other stages like
[00:08:37] posttraining or there are new types of
[00:08:39] reasoning models and in in in all of
[00:08:42] those cases that we've measured we see
[00:08:45] similar similar types of scaling laws a
[00:08:48] bit of a philosophical question but
[00:08:49] what's your intuition about why bigger
[00:08:52] is better in terms of network size and
[00:08:54] data size why does it lead to more
[00:08:58] intelligent models so in my previous
[00:09:01] career as a as a biophysicist so I did
[00:09:03] physics undergrad and then biophysics in
[00:09:06] in in in grad school so I think back to
[00:09:08] what I know as a physicist which is
[00:09:09] actually much less than what some of my
[00:09:11] colleagues at anthropic have in terms of
[00:09:14] in terms of expertise in physics uh
[00:09:17] there's this there's this concept called
[00:09:19] the one over F noise and one overx
[00:09:21] distributions um where where often um uh
[00:09:25] you know just just like if you add up a
[00:09:27] bunch of natural processes you get
[00:09:29] gaussian if you add up a bunch of kind
[00:09:31] of differently distributed natural
[00:09:34] processes if you like if you like take a
[00:09:37] take a um probe and and hook it up to a
[00:09:39] resistor the distribution of the thermal
[00:09:42] noise in the resistor goes as one over
[00:09:44] the frequency um it's some kind of
[00:09:46] natural convergent distribution uh and
[00:09:49] and I I I I and and I think what it
[00:09:52] amounts to is that if you look at a lot
[00:09:54] of things that are that are produced by
[00:09:56] some natural process that has a lot of
[00:09:58] different scales right not a gaussian
[00:10:00] which is kind of narrowly distributed
[00:10:02] but you know if I look at kind of like
[00:10:04] large and small fluctuations that lead
[00:10:07] to lead to electrical noise um they have
[00:10:10] this decaying 1 overx distribution and
[00:10:13] so now I think of like patterns in the
[00:10:15] physical world right if I if or or in
[00:10:18] language if I think about the patterns
[00:10:20] in language there are some really simple
[00:10:21] patterns some words are much more common
[00:10:23] than others like the' then there's basic
[00:10:26] noun verb structure then there's the
[00:10:28] fact that you know you know nouns and
[00:10:30] verbs have to agree they have to
[00:10:31] coordinate and there's the higher level
[00:10:33] sentence structure then there's the
[00:10:34] Thematic structure of paragraphs and so
[00:10:37] the fact that there's this regressing
[00:10:38] structure you can imagine that as you
[00:10:41] make the networks larger first they
[00:10:43] capture the really simple correlations
[00:10:45] the really simple patterns and there's
[00:10:47] this long taale of other patterns and if
[00:10:50] that long taale of other patterns is
[00:10:52] really smooth like it is with the one
[00:10:54] over F noise in you know physical
[00:10:56] processes like like like resistors then
[00:10:59] you could imagine as you make the
[00:11:00] network larger it's kind of capturing
[00:11:02] more and more of that distribution and
[00:11:05] so that smoothness gets reflected in how
[00:11:07] well the models are at predicting and
[00:11:09] how well they perform language is an
[00:11:11] evolved process right we've we've
[00:11:14] developed language we have common words
[00:11:17] and less common words we have common
[00:11:18] expressions and less common Expressions
[00:11:21] we have ideas cliches that are expressed
[00:11:24] frequently and we have novel ideas and
[00:11:26] that process has has developed has
[00:11:28] evolved with humans over millions of
[00:11:30] years and so the the the guess and this
[00:11:33] is pure speculation would be would be
[00:11:35] that there is there's some kind of
[00:11:37] longtail distribution of of of the
[00:11:40] distribution of these ideas so there's
[00:11:42] the long tail but also there's the
[00:11:43] height of the hierarchy of Concepts that
[00:11:46] you're building up so the bigger the
[00:11:48] network presumably you have a higher
[00:11:49] capacity to exactly if you have a small
[00:11:51] Network you only get the common stuff
[00:11:53] right if if I take a tiny neural network
[00:11:56] it's very good at understanding that you
[00:11:58] know a sentence has to have you know
[00:12:00] verb adjective noun right but it's it's
[00:12:02] terrible at deciding what those verb
[00:12:04] adjective and noun should be and whether
[00:12:06] they should make sense if I make it just
[00:12:08] a little bigger it gets good at that
[00:12:10] then suddenly it's good at the sentences
[00:12:11] but it's not good at the paragraphs and
[00:12:13] so the these these rare and more complex
[00:12:16] patterns get picked up as I add as I add
[00:12:18] more capacity to the network well the
[00:12:20] natural question then is what's the
[00:12:22] ceiling of this like how complicated and
[00:12:26] complex is the real world how much of
[00:12:28] stuff is there to learn I don't think
[00:12:30] any of us knows the answer to that
[00:12:32] question um I my strong Instinct would
[00:12:35] be that there's no ceiling below level
[00:12:37] of humans right we humans are able to
[00:12:39] understand these various patterns and so
[00:12:41] that that makes me think that if we
[00:12:43] continue to you know scale up these
[00:12:46] these these models to kind of develop
[00:12:49] new methods for training them and
[00:12:50] scaling them up uh that will at least
[00:12:53] get to the level that we've gotten to
[00:12:54] with humans there's then a question of
[00:12:56] you know how much more is it possible to
[00:12:59] understand than humans do how much how
[00:13:01] much is it possible to be smarter and
[00:13:03] more perceptive than humans I I would
[00:13:05] guess the answer has has got to be
[00:13:08] domain dependent if I look at an area
[00:13:11] like biology and you know I wrote this
[00:13:13] essay Machines of Loving Grace it seems
[00:13:15] to me that humans are struggling to
[00:13:19] understand the complexity of biology
[00:13:20] right if you go to Stanford or to
[00:13:22] Harvard or to Berkeley you have whole
[00:13:25] Departments of you know folks trying to
[00:13:27] study you know like the immune system or
[00:13:30] metabolic pathways and and each person
[00:13:33] understands only a tiny bit part of it
[00:13:35] specializes and they're struggling to
[00:13:37] combine their knowledge with that of
[00:13:39] with that of other humans and so I have
[00:13:41] an instinct that there's there's a lot
[00:13:42] of room at the top for AIS to get
[00:13:45] smarter if I think of something like
[00:13:48] materials in the in the physical world
[00:13:50] or you know um like addressing you know
[00:13:53] conflicts between humans or something
[00:13:55] like that I mean you know it it may be
[00:13:57] there's only some of these problems are
[00:13:59] not intractable but much harder and and
[00:14:01] it it may be that there's only there's
[00:14:04] only so well you can do with some of
[00:14:05] these things right just like with speech
[00:14:06] recognition there's only so clear I can
[00:14:09] hear your speech so I think in some
[00:14:11] areas there may be ceilings in in in you
[00:14:14] know that are very close to what humans
[00:14:15] have done in other areas those ceilings
[00:14:17] may be very far away and I think we'll
[00:14:19] only find out when we build these
[00:14:21] systems uh there's it's very hard to
[00:14:23] know in advance we can speculate but we
[00:14:25] can't be sure and in some domains the
[00:14:27] ceiling might have to do with human
[00:14:29] bureaucracies and things like this as
[00:14:30] you're right about yes so humans
[00:14:32] fundamentally have to be part of the
[00:14:33] loop that's the cause of the ceiling not
[00:14:36] maybe the limits of the intelligence
[00:14:38] yeah I think in many cases um you know
[00:14:41] in theory technology could change very
[00:14:44] fast for example all the things that we
[00:14:46] might invent with respect to biology um
[00:14:49] but remember there's there's a you know
[00:14:51] there's a clinical trial system that we
[00:14:53] have to go through to actually
[00:14:55] administer these things to humans I
[00:14:57] think that's a mixture of things that
[00:14:58] are unnecessary and bureaucratic and
[00:15:01] things that kind of protect the
[00:15:03] Integrity of society and the whole
[00:15:04] challenge is that it's hard to tell it's
[00:15:06] hard to tell what's going on uh it's
[00:15:07] hard to tell which is which right my my
[00:15:09] view is definitely I think in terms of
[00:15:12] drug development we my view is that
[00:15:14] we're too slow and we're too
[00:15:16] conservative but certainly if you get
[00:15:18] these things wrong you know it's it's
[00:15:19] possible to to to risk people's lives by
[00:15:22] by being by being by being too Reckless
[00:15:24] and so at least at least some of these
[00:15:26] human institutions are in fact
[00:15:29] protecting people so it's it's all about
[00:15:31] finding the balance I strongly suspect
[00:15:33] that balance is kind of more on the side
[00:15:35] of pushing to make things happen faster
[00:15:37] but there is a balance if we do hit a
[00:15:40] limit if we do hit a Slowdown in the
[00:15:43] scaling laws what do you think would be
[00:15:45] the reason is it compute limited data
[00:15:47] limited uh is it something else idea
[00:15:50] limited so a few things now we're
[00:15:52] talking about hitting the limit before
[00:15:54] we get to the level of of humans and the
[00:15:56] skill of humans um so so I think one
[00:15:59] that's you know one that's popular today
[00:16:01] and I think you know could be a limit
[00:16:03] that we run into I like most of the
[00:16:05] limits I would bet against it but it's
[00:16:06] definitely possible is we simply run out
[00:16:09] of data there's only so much data on the
[00:16:11] internet and there's issues with the
[00:16:12] quality of the data right you can get
[00:16:15] hundreds of trillions of words on the
[00:16:17] internet but a lot of it is is
[00:16:19] repetitive or it's search engine you
[00:16:22] know search engine optimization driil or
[00:16:24] maybe in the future it'll even be text
[00:16:26] generated by AIS itself uh and and so I
[00:16:30] think there are limits to what to to
[00:16:32] what can be produced in this way that
[00:16:35] said we and I would guess other
[00:16:37] companies are working on ways to make
[00:16:39] data synthetic uh where you can you know
[00:16:42] you can use the model to generate more
[00:16:44] data of the type that you have that you
[00:16:46] have already or even generate data from
[00:16:49] scratch if you think about uh what was
[00:16:51] done with uh deep mines Alpha go zero
[00:16:54] they managed to get a bot all the way
[00:16:55] from you know no ability to play Go
[00:16:58] whatsoever to above human level just by
[00:17:00] playing against itself there was no
[00:17:02] example data from humans required in the
[00:17:05] the alphao zero version of it the other
[00:17:07] direction of course is these reasoning
[00:17:09] models that do Chain of Thought and stop
[00:17:11] to think um and and reflect on their own
[00:17:13] thinking in a way that's another kind of
[00:17:16] synthetic data coupled with
[00:17:18] reinforcement learning so my my guess is
[00:17:20] with one of those methods we'll get
[00:17:21] around the data limitation or there may
[00:17:23] be other sources of data that are that
[00:17:25] are available um we could just observe
[00:17:28] that even if there's no problem with
[00:17:30] data as we start to scale models up they
[00:17:32] just stop getting better it's it seemed
[00:17:35] to be a a reliable observation that
[00:17:37] they've gotten better that could just
[00:17:39] stop at some point for a reason we don't
[00:17:41] understand um the answer could be that
[00:17:44] we need to uh you know we need to invent
[00:17:47] some new architecture um it's been there
[00:17:50] have been problems in the past with with
[00:17:52] say numerical stability of models where
[00:17:55] it looked like things were were leveling
[00:17:57] off but but actually you know know when
[00:17:59] we when we when we found the right
[00:18:00] Unblocker they didn't end up doing so so
[00:18:02] perhaps there's new some new
[00:18:05] optimization method or some new uh
[00:18:07] Technique we need to to unblock things
[00:18:09] I've seen no evidence of that so far but
[00:18:11] if things were to to slow down that
[00:18:13] perhaps could be one reason what about
[00:18:16] the limits of compute meaning uh the
[00:18:20] expensive uh nature of building bigger
[00:18:22] and bigger data centers so right now I
[00:18:24] think uh you know most of the Frontier
[00:18:27] Model companies I would guess are are
[00:18:29] operating you know roughly you know $1
[00:18:31] billion scale plus or minus a factor of
[00:18:34] three right those are the models that
[00:18:35] exist now or are being trained now uh I
[00:18:38] think next year we're going to go to a
[00:18:39] few billion and then uh 2026 we may go
[00:18:43] to uh uh you know above 10 10 10 billion
[00:18:46] and probably by 2027 their Ambitions to
[00:18:49] build hundred hundred billion dollar uh
[00:18:52] hundred billion dollar clusters and I
[00:18:53] think all of that actually will happen
[00:18:55] there's a lot of determination to build
[00:18:57] the compute to do it within this country
[00:19:00] uh and I would guess that it actually
[00:19:01] does happen now if we get to 100 billion
[00:19:05] that's still not enough compute that's
[00:19:06] still not enough scale then either we
[00:19:09] need even more scale or we need to
[00:19:11] develop some way of doing it more
[00:19:13] efficiently of Shifting The Curve um I
[00:19:15] think be between all of these one of the
[00:19:17] reasons I'm bullish about powerful AI
[00:19:19] happening so fast is just that if you
[00:19:21] extrapolate the next few points on the
[00:19:23] curve we're very quickly getting towards
[00:19:26] human level ability right some of the
[00:19:28] new models that that we developed some
[00:19:31] some reasoning models that have come
[00:19:32] from other companies they're starting to
[00:19:34] get to what I would call the PHD or
[00:19:36] professional level right if you look at
[00:19:38] their their coding ability um the latest
[00:19:41] model we released Sonet 3.5 the new or
[00:19:45] updated version it gets something like
[00:19:47] 50% on sbench and sbench is an example
[00:19:50] of a bunch of professional real world
[00:19:52] software engineering tasks at the
[00:19:55] beginning of the year I think the
[00:19:57] state-of-the-art was three or 4% so in
[00:20:00] 10 months we've gone from 3% to 50% on
[00:20:03] this task and I think in another year
[00:20:05] we'll probably be at 90% I mean I don't
[00:20:07] know but might might even be might even
[00:20:09] be less than that uh we've seen similar
[00:20:12] things in graduate level math physics
[00:20:15] and biology from Models like open AI 01
[00:20:19] uh so uh if we if we just continue to
[00:20:22] extrapolate this right in terms of skill
[00:20:24] skill that we have I think if we
[00:20:26] extrapolate the straight curve Within a
[00:20:28] few years we will get to these models
[00:20:30] being you know above the the highest
[00:20:33] professional level in terms of humans
[00:20:35] now will that curve continue you've
[00:20:37] pointed to and I've pointed to a lot of
[00:20:38] reasons why you know possible reasons
[00:20:40] why that might not happen but if the if
[00:20:42] the extrapolation curve continues that
[00:20:44] is the trajectory we're on so anthropic
[00:20:47] has several competitors it'd be
[00:20:49] interesting to get your sort of view of
[00:20:50] it all open aai Google xai meta what
[00:20:53] does it take to win in the broad sense
[00:20:56] of win in the space yeah so I want to
[00:20:59] separate out a couple things right so
[00:21:01] you know anthropics anthropic mission is
[00:21:03] to kind of try to make this all go well
[00:21:06] right and and you know we have a theory
[00:21:08] of change called race to the top right
[00:21:11] race to the top is about trying to push
[00:21:15] the other players to do the right thing
[00:21:18] by setting an example it's not about
[00:21:19] being the good guy it's about setting
[00:21:21] things up so that all of us can be the
[00:21:23] good guy I'll give a few examples of
[00:21:25] this early in the history of anthropic
[00:21:27] one of our co-founders Chris Ola who I
[00:21:29] believe you're you're interviewing soon
[00:21:31] you know he's the co-founder of the
[00:21:32] field of mechanistic interpretability
[00:21:34] which is an attempt to understand what's
[00:21:36] going on inside AI models uh so we had
[00:21:40] him and one of our early teams focus on
[00:21:43] this area of interpretability which we
[00:21:44] think is good for making models safe and
[00:21:47] transparent for three or four years that
[00:21:50] had no commercial application whatsoever
[00:21:52] it still doesn't today we're doing some
[00:21:54] early betas with it and probably it will
[00:21:56] eventually but uh you know this is a
[00:21:58] very very long research bed in one in
[00:22:01] which we've we've built in public and
[00:22:03] shared our results publicly and and we
[00:22:06] did this because you know we think it's
[00:22:07] a way to make models safer an
[00:22:09] interesting thing is that as we've done
[00:22:12] this other companies have started doing
[00:22:14] it as well in some cases because they've
[00:22:16] been inspired by it in some cases
[00:22:18] because they're worried that uh you know
[00:22:21] if if other companies are doing this
[00:22:23] that look more responsible they want to
[00:22:25] look more responsible too no one wants
[00:22:27] to look like the irresponsible ible
[00:22:28] actor and and so they adopt this they
[00:22:31] adopt this as well when folks come to
[00:22:34] anthropic interpretability is often a
[00:22:35] draw and I tell them the other places
[00:22:37] you didn't go tell them why you came
[00:22:39] here um and and then you see soon that
[00:22:43] there that there's interpretability
[00:22:45] teams else elsewhere as well and in a
[00:22:47] way that takes away our competitive
[00:22:49] Advantage because it's like oh they now
[00:22:52] others are doing it as well but it's
[00:22:54] good it's good for the broader system
[00:22:56] and so we have to invent some new thing
[00:22:57] that we're doing others aren't doing as
[00:22:59] well and the hope is to basically bid up
[00:23:02] bid up the importance of of of doing the
[00:23:05] right thing and it's not it's not about
[00:23:07] us in particular right it's not about
[00:23:09] having one particular good guy other
[00:23:11] companies can do this as well if they if
[00:23:14] they if they join the race to do this
[00:23:15] that's that's you know that's the best
[00:23:17] news ever right um uh it's it's just
[00:23:19] it's about kind of shaping the
[00:23:21] incentives to point upward instead of
[00:23:23] shaping the incentives to point to point
[00:23:25] downward and we should say this example
[00:23:26] the field of uh mechanistic
[00:23:28] interpretability is just a a rigorous
[00:23:31] non handwavy way of doing AI safety yes
[00:23:34] or it's tending that way trying to I
[00:23:37] mean I I think we're still early um in
[00:23:39] terms of our ability to see things but
[00:23:41] I've been surprised at how much we've
[00:23:43] been able to look inside these systems
[00:23:45] and understand what we see right unlike
[00:23:48] with the scaling laws where it feels
[00:23:50] like there's some you know law that's
[00:23:52] driving these models to perform better
[00:23:55] on on the inside the models aren't you
[00:23:57] know there's no reason why they should
[00:23:58] be designed for us to understand them
[00:24:00] right they're designed to operate
[00:24:01] they're designed to work just like the
[00:24:03] human brain or human biochemistry
[00:24:05] they're not designed for a human to open
[00:24:07] up the hatch look inside and understand
[00:24:09] them but we have found and you know you
[00:24:11] can talk in much more detail about this
[00:24:13] to Chris that when we open them up when
[00:24:15] we do look inside them we we find things
[00:24:18] that are surprisingly interesting and as
[00:24:20] a side effect you also get to see the
[00:24:21] beauty of these models you get to
[00:24:23] explore the sort of uh the beautiful n
[00:24:26] nature of large neural networks through
[00:24:28] the me turb kind ofy I'm amazed at how
[00:24:30] clean it's been I I'm amazed at things
[00:24:33] like induction heads I'm amazed at
[00:24:36] things like uh you know that that we can
[00:24:39] you know use sparse autoencoders to find
[00:24:42] these directions within the networks uh
[00:24:45] and that the directions correspond to
[00:24:47] these very clear Concepts we
[00:24:49] demonstrated this a bit with the Golden
[00:24:51] Gate Bridge clad so this was an
[00:24:52] experiment where we found a direction
[00:24:55] inside one of the the neural network
[00:24:57] layers that corresponded to the Golden
[00:24:59] Gate Bridge and we just turned that way
[00:25:01] up and so we we released this model as a
[00:25:04] demo it was kind of half a joke uh for a
[00:25:06] couple days uh but it was it was
[00:25:08] illustrative of of the method we
[00:25:10] developed and uh you could you could
[00:25:12] take the Golden Gate you could take the
[00:25:14] model you could ask it about anything
[00:25:16] you know you know it would be like how
[00:25:18] you could say how was your day and
[00:25:19] anything you asked because this feature
[00:25:21] was activated would connect to the
[00:25:22] Golden Gate Bridge so it would say you
[00:25:24] know I'm I'm I'm feeling relaxed and
[00:25:26] expansive much like the the arches of
[00:25:28] the Golden Gate Bridge or you know it
[00:25:31] would masterfully change topic to the
[00:25:33] Golden Gate Bridge and it integrated
[00:25:35] there was also a sadness to it to to the
[00:25:37] focus ah had on the Golden Gate Bridge I
[00:25:38] think people quickly fell in love with
[00:25:40] it I think so people already miss it
[00:25:43] because it was taken down I think after
[00:25:45] a day somehow these interventions on the
[00:25:47] model um where where where where you
[00:25:50] kind of adjust Its Behavior somehow
[00:25:52] emotionally made it seem more human than
[00:25:55] any other version of the model strong
[00:25:57] personality strong ID strong personality
[00:25:59] it has these kind of like obsessive
[00:26:01] interests you know we can all think of
[00:26:03] someone who's like obsessed with
[00:26:04] something so it does make it feel
[00:26:06] somehow a bit more human let's talk
[00:26:08] about the present let's talk about
[00:26:09] Claude so this year A lot has happened
[00:26:13] in March claw 3 Opa Sonet Hau were
[00:26:17] released then claw 35 Sonet in July with
[00:26:21] an updated version just now released and
[00:26:24] then also claw 35 hi coup was released
[00:26:27] okay can you explain the difference
[00:26:29] between Opus Sonet and Haiku and how we
[00:26:33] should think about the different
[00:26:34] versions yeah so let's go back to March
[00:26:36] when we first released uh these three
[00:26:38] models so you know our thinking was you
[00:26:41] different companies produce kind of
[00:26:43] large and small models better and worse
[00:26:46] models we felt that there was demand
[00:26:49] both for a really powerful model um you
[00:26:52] know and you that might be a little bit
[00:26:54] slower that you'd have to pay more for
[00:26:56] and also for fast cheap models that are
[00:27:00] as smart as they can be for how fast and
[00:27:02] cheap right whenever you want to do some
[00:27:04] kind of like you know difficult analysis
[00:27:07] like if I you know I want to write code
[00:27:08] for instance or you know I want to I
[00:27:10] want to brainstorm ideas or I want to do
[00:27:12] creative writing I want the really
[00:27:14] powerful model but then there's a lot of
[00:27:16] practical applications in a business
[00:27:18] sense where it's like I'm interacting
[00:27:20] with a website I you know like I'm like
[00:27:23] doing my taxes or I'm you know talking
[00:27:25] to uh you know to like a legal adviser
[00:27:27] and I want to analyze a contract or you
[00:27:30] know we have plenty of companies that
[00:27:31] are just like you know you know I want
[00:27:33] to do autocomplete on my on my IDE or
[00:27:36] something uh and and for all of those
[00:27:38] things you want to act fast and you want
[00:27:40] to use the model very broadly so we
[00:27:42] wanted to serve that whole spectrum of
[00:27:45] needs um so we ended up with this uh you
[00:27:48] know this kind of poetry theme and so
[00:27:50] what's a really short poem it's a Haik
[00:27:51] cou and so Haiku is the small fast cheap
[00:27:55] model that is you know was at the time
[00:27:57] was released surprisingly surprisingly
[00:28:00] uh intelligent for how fast and cheap it
[00:28:02] was uh sonnet is a is a medium-sized
[00:28:05] poem right a couple paragraphs since o
[00:28:06] Sonet was the middle model it is smarter
[00:28:09] but also a little bit slower a little
[00:28:11] bit more expensive and and Opus like a
[00:28:13] magnum opus is a large work uh Opus was
[00:28:16] the the largest smartest model at the
[00:28:19] time um so that that was the original
[00:28:21] kind of thinking behind it um and our
[00:28:26] our thinking then was well each new
[00:28:27] generation of models should shift that
[00:28:29] tradeoff curve uh so when we release
[00:28:32] Sonet 3.5 it has the same roughly the
[00:28:35] same you know cost and speed as the
[00:28:39] Sonet 3 Model uh but uh it it increased
[00:28:45] its intelligence to the point where it
[00:28:47] was smarter than the original Opus 3
[00:28:49] Model uh especially for code but but
[00:28:52] also just in general and so now you know
[00:28:55] we've shown results for a Hau 3. 5 and I
[00:28:59] believe Hau 3.5 the smallest new model
[00:29:02] is about as good as Opus 3 the largest
[00:29:06] old model so basically the aim here is
[00:29:08] to shift the curve and then at some
[00:29:10] point there's going to be an opus 3.5 um
[00:29:13] now every new generation of models has
[00:29:15] its own thing they use new data their
[00:29:17] personality changes in ways that we kind
[00:29:20] of you know try to steer but are not
[00:29:23] fully able to steer and and so uh
[00:29:25] there's never quite that exact
[00:29:27] equivalence the only thing you're
[00:29:28] changing is intelligence um we always
[00:29:30] try and improve other things and some
[00:29:32] things change without us without us
[00:29:34] knowing or measuring so it's it's very
[00:29:36] much an inexact science in many ways the
[00:29:40] manner and personality of these models
[00:29:42] is more an art than it is a science so
[00:29:45] what is sort of the reason for uh the
[00:29:50] span of time between say Claude Opus 3
[00:29:54] and 35 what is it what takes that time
[00:29:57] if you can speak to yeah so there's
[00:29:59] there's different there's different uh
[00:30:00] processes um uh there's pre-training
[00:30:03] which is you know just kind of the
[00:30:04] normal language model training and that
[00:30:06] takes a very long time um that uses you
[00:30:09] know these days you know tens you know
[00:30:12] tens of thousands sometimes many tens of
[00:30:14] thousands of uh gpus or tpus or tranium
[00:30:19] or you know what we use different
[00:30:20] platforms but you know accelerator chips
[00:30:23] um often often training for months uh
[00:30:26] there's then a kind of posttraining
[00:30:28] phase where we do reinforcement learning
[00:30:31] from Human feedback as well as other
[00:30:33] kinds of reinforcement learning that
[00:30:36] that phase is getting uh larger and
[00:30:38] larger now and you know you know often
[00:30:41] that's less of an exact science it often
[00:30:43] takes effort to get it right um models
[00:30:46] are then tested with some of our early
[00:30:48] Partners to see how good they are and
[00:30:50] they're then tested both internally and
[00:30:53] externally for their safety particularly
[00:30:56] for catastrophic and autonomy r risks uh
[00:30:59] so uh we do internal testing according
[00:31:01] to our responsible scaling policy which
[00:31:04] I you know could talk more about that in
[00:31:05] detail and then we have an agreement
[00:31:07] with the US and the UK AI safety
[00:31:10] Institute as well as other third-party
[00:31:12] testers in specific domains to test the
[00:31:15] models for what are called cbrn risk
[00:31:17] chemical biological radiological and
[00:31:20] nuclear which are you know we don't
[00:31:22] think that models pose these risks
[00:31:24] seriously yet but but every new model we
[00:31:27] want to evaluate to see if we're
[00:31:28] starting to get close to some of these
[00:31:30] these these more dangerous um uh these
[00:31:33] more dangerous capabilities so those are
[00:31:36] the phases and then uh you know then
[00:31:38] then it just takes some time to get the
[00:31:40] model working in terms of inference and
[00:31:43] launching it in the API so there's just
[00:31:45] just a lot of steps to uh to actually to
[00:31:48] actually making a model work and of
[00:31:49] course you know we're always trying to
[00:31:51] make the processes as streamlined as
[00:31:54] possible right we want our safety
[00:31:55] testing to be rigorous but we want it to
[00:31:57] be RoR ous and to be you know to be
[00:32:00] automatic to happen as fast as it can
[00:32:02] without compromising on rigor same with
[00:32:04] our pre-training process and our
[00:32:06] posttraining process so you know it's
[00:32:08] just like building anything else it's
[00:32:09] just like building airplanes you want to
[00:32:11] make them you know you want to make them
[00:32:13] safe but you want to make the process
[00:32:14] streamlined and I think the creative
[00:32:16] tension between those is is you know is
[00:32:18] an important thing and making the models
[00:32:20] work yeah uh rumor on the street I
[00:32:22] forget who was saying that uh anthropic
[00:32:23] is really good tooling so I uh probably
[00:32:27] a lot of the challenge here is on the
[00:32:29] software engineering side is to build
[00:32:30] the tooling to to have a like a
[00:32:33] efficient low friction interaction with
[00:32:35] the infrastructure you would be
[00:32:36] surprised how much of the challenges of
[00:32:40] uh you know building these models comes
[00:32:43] down to you know software engineering
[00:32:46] performance engineering you know you you
[00:32:48] know from the outside you might think oh
[00:32:50] man we had this Eureka breakthrough
[00:32:52] right you know this movie with the
[00:32:53] science we discovered it we figured it
[00:32:55] out but but but I think I think all
[00:32:58] things even even even you know
[00:33:00] incredible discoveries like they they
[00:33:03] they they they almost always come down
[00:33:05] to the details um and and often super
[00:33:07] super boring details I can't speak to
[00:33:09] whether we have better tooling than than
[00:33:11] other companies I mean you know I
[00:33:12] haven't been at those other companies at
[00:33:14] least at least not recently um but it's
[00:33:16] certainly something we give a lot of
[00:33:17] attention to I don't know if you can say
[00:33:19] but from three from CLA 3 to CLA 35 is
[00:33:24] there any extra pre-training going on or
[00:33:26] is they mostly focus on the
[00:33:27] post-training there's been leaps in
[00:33:29] performance yeah I think I think at any
[00:33:31] given stage we're focused on improving
[00:33:33] everything at once um just just
[00:33:35] naturally like there are different teams
[00:33:37] each team makes progress in a particular
[00:33:40] area in in in making a particular you
[00:33:43] know their particular segment of the
[00:33:44] relay race better and it's just natural
[00:33:46] that when we make a new model we put we
[00:33:48] put all of these things in at once so
[00:33:51] the data you have like the preference
[00:33:52] data you get from rhf is that applicable
[00:33:56] is there ways to apply it to newer
[00:33:59] models as it get trained up yeah
[00:34:01] preference data from old models
[00:34:02] sometimes gets used for new models
[00:34:04] although of course uh it it performs
[00:34:06] somewhat better when it's you know
[00:34:07] trained on it's trained on the new
[00:34:09] models note that we have this you know
[00:34:11] constitutional AI method such that we
[00:34:12] don't only use preference data we kind
[00:34:14] of there's also a post-t trainining
[00:34:16] process where we train the model against
[00:34:18] itself and there's you know new types of
[00:34:20] post training the model against itself
[00:34:22] that are used every day so it's not just
[00:34:24] RF it's a bunch of other methods as well
[00:34:27] um post training I think you know it's
[00:34:28] becoming more and more sophisticated
[00:34:30] well what explains the big leap in
[00:34:32] performance for the new Sona 35 I mean
[00:34:35] at least in the programming side and
[00:34:37] maybe this is a good place to talk about
[00:34:38] benchmarks what does it mean to get
[00:34:40] better just the number went up but you
[00:34:43] know I I I program but I also love
[00:34:46] programming and I um claw 35 through
[00:34:49] cursor is what I use uh to assist me in
[00:34:52] programming and there was at least
[00:34:55] experientially anecdotally it's gotten
[00:34:58] smarter at programming so what like what
[00:35:01] what does it take to get it uh to get it
[00:35:03] smarter we observe that as well by the
[00:35:05] way there were a couple uh very strong
[00:35:07] Engineers here at anthropic um who all
[00:35:10] previous code models both produced by us
[00:35:12] and produced by all the other companies
[00:35:14] hadn't really been useful to to hadn't
[00:35:16] really been useful to them you know they
[00:35:17] said you know maybe maybe this is useful
[00:35:19] to beginner it's not useful to me but
[00:35:22] Sonet 3.5 the original one for the first
[00:35:24] time they said oh my God this helped me
[00:35:26] with something that you know that it
[00:35:28] would have taken me hours to do this is
[00:35:29] the first model that has actually saved
[00:35:30] me time so again the water line is
[00:35:33] rising and and then I think you know the
[00:35:35] new Sonet has been has been even better
[00:35:37] in terms of what it what it takes I mean
[00:35:39] I'll just say it's been across the board
[00:35:41] it's in the pre-training it's in the
[00:35:43] posttraining it's in various evaluations
[00:35:46] that we do we've observed this as well
[00:35:48] and if we go into the details of the
[00:35:50] Benchmark so s bench is basically you
[00:35:54] know since since you know since since
[00:35:55] you're a programmer you know you'll be
[00:35:57] familiar with like PLL requests and you
[00:35:59] know uh just just PLL requests are like
[00:36:02] you know the like a sort of a sort of
[00:36:04] atomic unit of work you know you could
[00:36:06] say I'm you know I'm implementing one
[00:36:09] I'm implementing one thing um uh and and
[00:36:12] so sbench actually gives you kind of a
[00:36:15] real world situation where the codebase
[00:36:17] is in a current state and I'm trying to
[00:36:19] implement something that's you know
[00:36:20] that's described in described in
[00:36:22] language we have internal benchmarks
[00:36:24] where we where we measure the same thing
[00:36:25] and you say just give the model free
[00:36:27] reign to like you know do anything run
[00:36:30] run run anything edit anything um how
[00:36:33] how well is it able to complete these
[00:36:35] tasks and it's that Benchmark that's
[00:36:38] gone from it can do it 3% of the time to
[00:36:40] it can do it about 50% of the time um so
[00:36:43] I actually do believe that if we get you
[00:36:45] can gain benchmarks but I think if we
[00:36:46] get to 100% on that Benchmark in a way
[00:36:49] that isn't kind of like overtrained or
[00:36:51] or or game for that particular Benchmark
[00:36:54] probably represents a real and serious
[00:36:56] increase in kind of
[00:36:58] in kind of programming programming
[00:36:59] ability and and I would suspect that if
[00:37:02] we can get to you know 90 90 95% that
[00:37:06] that that that you know it will it will
[00:37:08] represent ability to autonomously do a
[00:37:10] significant fraction of software
[00:37:11] engineering
[00:37:12] tasks well ridiculous timeline question
[00:37:15] uh when is clad Opus uh 3.5 coming up uh
[00:37:19] not giving you an exact date uh but you
[00:37:22] know there there uh you know as far as
[00:37:24] we know the plan is still to have a
[00:37:26] Claude 3.5 opus are we gonna get it
[00:37:28] before GTA 6 or no like Duke Nukem
[00:37:31] Forever was that game that there was
[00:37:33] some game that was delayed 15 years was
[00:37:34] that Duke Nukem Forever yeah and I think
[00:37:36] GTA is now just releasing trailers it
[00:37:39] you know it's only been three months
[00:37:40] since we released the first son it yeah
[00:37:42] it's Inc the incredible pace of relas it
[00:37:44] just it just tells you about the pace
[00:37:46] the expectations for when things are
[00:37:48] going to come out so uh what about
[00:37:51] 40 so how do you think about sort of as
[00:37:54] these models get bigger and bigger about
[00:37:55] versioning and also just versioning in
[00:37:58] general why Sonet 35 updated with the
[00:38:02] date why not Sonet
[00:38:05] 3.6 actually naming is actually an
[00:38:07] interesting challenge here right because
[00:38:09] I think a year ago most of the model was
[00:38:11] pre-training and so you could start from
[00:38:14] the beginning and just say okay we're
[00:38:15] going to have models of different sizes
[00:38:16] we're going to train them all together
[00:38:18] and you know we'll have a a family of
[00:38:20] naming schemes and then we'll put some
[00:38:22] new magic into them and then you know
[00:38:23] we'll have the next the next Generation
[00:38:26] Um the trouble starts are already when
[00:38:27] some of them take a lot longer than
[00:38:29] others to train right that already
[00:38:30] messes up your time time a little bit
[00:38:33] but as you make big improvements in as
[00:38:37] pre-training uh then you suddenly notice
[00:38:40] oh I can make better pre-train model and
[00:38:42] that doesn't take very long to do and
[00:38:45] but you know clearly it has the same you
[00:38:47] know size and shape of previous models
[00:38:49] uh uh so I think those two together as
[00:38:52] well as the timing timing issues any
[00:38:54] kind of scheme you come up with uh you
[00:38:56] know the reality tends to kind of
[00:38:59] frustrate that scheme right T tends to
[00:39:02] kind of break out of the break out of
[00:39:03] the scheme it's not like software where
[00:39:05] you can say oh this is like you know 3.7
[00:39:08] this is 3.8 no you have models with
[00:39:10] different different tradeoffs you can
[00:39:12] change some things in your models you
[00:39:14] can train you can change other things
[00:39:16] some are faster and slower at inference
[00:39:18] some have to be more expensive some have
[00:39:19] to be less expensive and so I think all
[00:39:22] the companies have struggled with this
[00:39:24] um I think we did very you know I think
[00:39:26] think we were in a good good position in
[00:39:28] terms of naming when we had Haiku Sonet
[00:39:31] and we're trying to maintain it but it's
[00:39:34] not it's not it's not perfect um so
[00:39:36] we'll we'll we'll try and get back to
[00:39:38] the Simplicity but it it um uh just the
[00:39:41] the the nature of the field I feel like
[00:39:43] no one's figured out naming it's somehow
[00:39:45] a different Paradigm from like normal
[00:39:47] software and and and so we we just none
[00:39:51] of the companies have been perfect at it
[00:39:52] um it's something we struggle with
[00:39:54] surprisingly much relative to you know
[00:39:56] how relative to how trivial it is to you
[00:39:59] know for the the the the grand science
[00:40:01] of training the models so from the user
[00:40:04] side the user experience of the updated
[00:40:06] Sonet 35 is just different than the
[00:40:10] previous uh June 2024 Sonet 35 it would
[00:40:14] be nice to come up with some kind of
[00:40:15] labeling that embodies that because
[00:40:18] people talk about son 35 but now there's
[00:40:20] a different one and so how do you refer
[00:40:23] to the previous one and the new one and
[00:40:25] it it uh when there's a distinct
[00:40:28] Improvement it just makes conversation
[00:40:31] about it uh just challenging yeah yeah I
[00:40:35] I definitely think this question of
[00:40:37] there are lots of properties of the
[00:40:39] models that are not reflected in the
[00:40:41] benchmarks um I I think I think that's
[00:40:44] that's definitely the case and everyone
[00:40:46] agrees and not all of them are
[00:40:47] capabilities some of them are you know
[00:40:50] models can be polite or brusk they can
[00:40:54] be uh you know uh very reactive or they
[00:40:59] can ask you questions um they can have
[00:41:01] what what feels like a warm personality
[00:41:03] or a cold personality they can be boring
[00:41:06] or they can be very distinctive like
[00:41:07] Golden Gate Claude was um and we have a
[00:41:11] whole you know we have a whole team kind
[00:41:12] of focused on I think we call it Claude
[00:41:14] character uh Amanda leads that team and
[00:41:17] we'll we'll talk to you about that but
[00:41:19] it's still a very inexact science um and
[00:41:22] and often we find that models have
[00:41:25] properties that we're not aware of the
[00:41:27] the fact of the matter is that you can
[00:41:29] you know talk to a model 10,000 times
[00:41:31] and there are some behaviors you might
[00:41:33] not see uh just like just like with a
[00:41:36] human right I can know someone for a few
[00:41:37] months and you know not know that they
[00:41:39] have a certain skill or not know there's
[00:41:41] a certain side to them and so I think I
[00:41:43] think we just have to get used to this
[00:41:45] idea and we're always looking for better
[00:41:47] ways of testing our models to to
[00:41:49] demonstrate these capabilities and and
[00:41:52] and also to decide which are which are
[00:41:53] the which are the personality properties
[00:41:56] we want models to have have and which we
[00:41:57] don't want to have that itself the
[00:41:59] normative question is also super
[00:42:01] interesting I got to ask you a question
[00:42:03] from Reddit from Reddit oh
[00:42:06] boy you know there there's just this
[00:42:08] fascinating to me at least it's a
[00:42:09] psychological social
[00:42:11] phenomenon where people report that
[00:42:14] Claude has gotten Dumber for them over
[00:42:16] time and so uh the question is does the
[00:42:19] user complaint about the dumbing down of
[00:42:21] claw 35 Sonic hold any water so are
[00:42:24] these anecdota reports a kind of social
[00:42:28] phenomena or did Claude is there any
[00:42:31] cases where Claude would get Dumber so
[00:42:34] uh this actually doesn't apply this this
[00:42:36] isn't just about Claude I I believe this
[00:42:39] I believe I've seen these complaints for
[00:42:41] every Foundation model produced by a
[00:42:43] major company um people said this about
[00:42:45] gp4 they said it about gp4 turbo um so
[00:42:50] so so a couple things um one the actual
[00:42:53] weights of the model right the actual
[00:42:55] brain of the model that does not change
[00:42:57] unless we introduce a new model um there
[00:43:01] there just a number of reasons why it
[00:43:02] would not make sense practically to be
[00:43:04] randomly substituting in substituting in
[00:43:07] new versions of the model it's difficult
[00:43:09] from an inference perspective and it's
[00:43:11] actually hard to control all the
[00:43:14] consequences of changing the way to the
[00:43:15] model let's say you wanted to fine-tune
[00:43:17] the model to be like I don't know to
[00:43:19] like to say certainly less which you
[00:43:22] know an old version of Sonet used to do
[00:43:24] um you actually end up changing a 100
[00:43:25] things as well so we have a whole
[00:43:27] process for it and we have a whole
[00:43:28] process for modifying the model we do a
[00:43:30] bunch of testing on it we do a bunch of
[00:43:33] um like we do a bunch of user testing
[00:43:34] and early customers so it we both have
[00:43:38] never changed the weights of the model
[00:43:40] without without telling anyone and it it
[00:43:43] it wouldn't certainly in the current
[00:43:44] setup it would not make sense to do that
[00:43:46] now there are a couple things that we do
[00:43:48] occasionally do um one is sometimes we
[00:43:51] run AB tests um but those are typically
[00:43:54] very close to when a model is being is
[00:43:56] being uh released and for a very small
[00:43:59] fraction of time um so uh you know like
[00:44:02] the you know the the day before the new
[00:44:04] Sonet 3.5 I I agree we should have
[00:44:07] should have had a better name it's
[00:44:08] clunky to refer to it um there were some
[00:44:10] comments from people that like it's got
[00:44:12] It's got it's gotten a lot better and
[00:44:13] that's because you know a fraction were
[00:44:15] exposed to to an AB test for for those
[00:44:17] one or for those one or two days um the
[00:44:21] other is that occasionally the system
[00:44:22] prompt will change um on the system
[00:44:24] prompt can have some effects although
[00:44:26] it's un it it it's unlikely to dumb down
[00:44:29] models it's unlikely to make them Dumber
[00:44:31] um and and and and we've seen that while
[00:44:34] these two things which I'm listing to be
[00:44:36] very complete um happen relatively
[00:44:39] happen quite infrequently um the
[00:44:42] complaints about to for us and for other
[00:44:45] model companies about the model changed
[00:44:47] the model isn't good at this the model
[00:44:48] got more censored the model was dumb
[00:44:50] down those complaints are constant and
[00:44:53] so I don't want to say like people are
[00:44:54] imagining it or anything but like the
[00:44:56] models are for the most part not
[00:44:59] changing um if I were to offer a theory
[00:45:02] um I I think it actually relates to one
[00:45:05] of the things I said before which is
[00:45:07] that models have many are very complex
[00:45:10] and have many aspects to them and so
[00:45:13] often you know if I if I if if I ask a
[00:45:15] model a question you know if I'm like if
[00:45:17] I'm like do task X versus can you do
[00:45:20] task XX the model might respond in
[00:45:23] different ways uh and and so there are
[00:45:25] all kinds of subtle things that you can
[00:45:27] change about the way you interact with
[00:45:29] the model that can give you very
[00:45:31] different results um to be clear this
[00:45:34] this itself is like a failing by by us
[00:45:36] and by the other model providers that
[00:45:38] that the models are are just just often
[00:45:40] sensitive to like small small changes in
[00:45:43] wording it's yet another way in which
[00:45:45] the science of how these models work is
[00:45:47] very poorly developed uh and and so you
[00:45:49] know if I go to sleep one night and I
[00:45:51] was like talking to the model in a
[00:45:52] certain way and I like slightly Chang
[00:45:54] the phrasing of how I talk to the model
[00:45:56] you know I could I could get different
[00:45:58] results so that's that's one possible
[00:46:00] way the other thing is man it's just
[00:46:02] hard to quantify this stuff uh it's hard
[00:46:04] to quantify this stuff I think people
[00:46:06] are very excited by new models when they
[00:46:07] come out and then as time goes on they
[00:46:10] they become very aware of the they
[00:46:12] become very aware of the limitations so
[00:46:13] that may be another effect but that's
[00:46:15] that's all a very long- rended way of
[00:46:17] saying for the most part with some
[00:46:19] fairly narrow exceptions the models are
[00:46:21] not changing I think there is a
[00:46:23] psychological effect you just start
[00:46:25] getting used to it the Baseline ra like
[00:46:27] when people have first gotten Wi-Fi on
[00:46:29] airplanes it's like amazing magic and
[00:46:32] then now like I can't get this thing to
[00:46:34] work this is such a piece of crap
[00:46:37] exactly so it's easy to have the
[00:46:38] conspiracy theory of they're making
[00:46:39] Wi-Fi slower and slower this is probably
[00:46:42] something I'll talk to Amanda much more
[00:46:44] about but U another Reddit question uh
[00:46:47] when will Claud stop trying to be my uh
[00:46:50] panical grandmother imposing its moral
[00:46:53] World viw on me as a paying customer and
[00:46:55] also what does it that ology behind
[00:46:57] making Claude overly apologetic so this
[00:47:00] kind of reports about The Experience a
[00:47:03] different angle on the frustration it
[00:47:05] has to do with the character yeah so a
[00:47:06] couple points on this first one is um
[00:47:10] like things that people say on Reddit
[00:47:12] and Twitter or X or whatever it is um
[00:47:14] there's actually a huge distribution
[00:47:16] shift between like the stuff that people
[00:47:18] complain loudly about on social media
[00:47:20] and what actually kind of like you know
[00:47:23] statistically users care about and that
[00:47:25] drives people to use the models like
[00:47:27] people are frustrated with you know
[00:47:29] things like you know the model not
[00:47:30] writing out all the code or the model uh
[00:47:33] you know just just not being as good at
[00:47:35] code as it could be even though it's the
[00:47:37] best model in the world on code um I I
[00:47:39] think the majority of thing of things
[00:47:41] are about that um uh but uh certainly a
[00:47:44] a a kind of vocal minority are uh you
[00:47:47] know kind kind of kind of rais these
[00:47:49] concerns right are frustrated by the
[00:47:51] model refusing things that it shouldn't
[00:47:53] refuse or like apologizing too much or
[00:47:55] just just having these kind of like
[00:47:57] annoying verbal ticks um the second
[00:48:00] caveat and I just want to say this like
[00:48:01] super clearly because I think it's like
[00:48:04] some people don't know it others like
[00:48:06] kind of know it but forget it like it is
[00:48:09] very difficult to control across the
[00:48:11] board how the models behave you cannot
[00:48:14] just reach in there and say oh I want
[00:48:16] the model to like apologize less like
[00:48:18] you can do that you can include trading
[00:48:20] data that says like oh the models should
[00:48:22] like apologize less but then in some
[00:48:24] other situation they end up being like
[00:48:26] super rude or like overconfident in a
[00:48:28] way that's like misleading people so
[00:48:30] they're they're all these tradeoffs um
[00:48:33] uh for example another thing is if there
[00:48:35] was a period during which models ours
[00:48:38] and I think others as well were T
[00:48:40] verbose right they would like repeat
[00:48:42] themselves they would say too much um
[00:48:45] you can cut down on the verbosity by
[00:48:47] penalizing the models for for just
[00:48:49] talking for too long what happens when
[00:48:51] you do that if you do it in a crude way
[00:48:53] is when the models are coding sometimes
[00:48:55] they'll say of the code goes here right
[00:48:58] because they've learned that that's a
[00:48:59] way to economize and that they see it
[00:49:01] and then and then so that leads the
[00:49:03] model to be so-called lazy in coding
[00:49:05] where they where they where they're just
[00:49:06] like ah you can finish the rest of it
[00:49:08] it's not it's not because we want to you
[00:49:10] know save on compute or because you know
[00:49:12] the models are lazy and you know during
[00:49:15] winter break or any of the other kind of
[00:49:17] conspiracy theories that have that have
[00:49:18] that have come up it's actually it's
[00:49:20] just very hard to control the behavior
[00:49:23] of the model to steer the behavior of
[00:49:25] the model in all circum ances at once
[00:49:28] you can kind of there's this this whacka
[00:49:30] aspect where you push on one thing and
[00:49:33] like you know these these these you know
[00:49:36] these other things start to move as well
[00:49:38] that you may not even notice or measure
[00:49:40] and so one of the reasons that I that I
[00:49:42] care so much about uh you know kind of
[00:49:46] grand alignment of these AI systems in
[00:49:48] the future is actually these systems are
[00:49:50] actually quite unpredictable they're
[00:49:52] actually quite hard to steer and control
[00:49:54] um and this version we're seeing today
[00:49:57] of you make one thing better it makes
[00:50:00] another thing worse uh I think that's
[00:50:04] that's like a present day analog of
[00:50:07] future control problems in AI systems
[00:50:10] that we can start to study today right I
[00:50:12] think I think that that that difficulty
[00:50:15] in in steering the behavior and in
[00:50:19] making sure that if we push an AI system
[00:50:21] in One Direction it doesn't push it in
[00:50:23] another Direction in some in some other
[00:50:25] ways that we didn't want uh I think
[00:50:28] that's that's kind of an that's kind of
[00:50:29] an early sign of things to come and if
[00:50:32] we can do a good job of solving this
[00:50:34] problem right of like you ask the model
[00:50:36] to like you know to like make and
[00:50:39] distribute small pox and it says no but
[00:50:41] it's willing to like help you in your
[00:50:43] graduate level virology class like how
[00:50:45] do we get both of those things at once
[00:50:47] it's hard it's very easy to go to one
[00:50:49] side or the other and it's a
[00:50:51] multi-dimensional problem and so uh I
[00:50:54] you know I think these questions of like
[00:50:56] shaping the models personality I think
[00:50:58] they're very hard I think we haven't
[00:51:01] done perfectly on them I think we've
[00:51:03] actually done the best of all the AI
[00:51:05] companies but still so far from perfect
[00:51:08] uh and I think if we can get this right
[00:51:10] if we can control the the you know
[00:51:13] control the false positives and false
[00:51:15] negatives in this this very kind of
[00:51:18] controlled present day environment will
[00:51:20] be much better at doing it for the
[00:51:22] future when our worry is you know will
[00:51:24] the models be super autonomous will they
[00:51:26] be able to you know make very dangerous
[00:51:28] things will they be able to autonomously
[00:51:30] you know build whole companies and are
[00:51:32] those companies aligned so so I I I
[00:51:34] think of this this present task as both
[00:51:37] vacine but also good practice for the
[00:51:39] future what's the current best way of
[00:51:42] gathering sort of user feedback like uh
[00:51:45] not anecdotal data but just large scale
[00:51:48] data about pain points or the opposite
[00:51:51] of pain points positive things so on is
[00:51:53] it internal testing is it yeah A
[00:51:55] specific group testing a testing what
[00:51:57] what what works so so so typically um
[00:52:00] we'll have internal model bashings where
[00:52:02] all of anthropic anthropic is almost a
[00:52:04] thousand people um you know people just
[00:52:06] just try and break the model they try
[00:52:07] and interact with it various ways um uh
[00:52:10] we have a suite of evals uh for you know
[00:52:13] oh is the model refusing in ways that
[00:52:15] that it couldn't I think we even had a
[00:52:17] certainly eval because you know our our
[00:52:20] mod again at one point model had this
[00:52:22] problem where like it had this annoying
[00:52:24] tick where it would like respond to a
[00:52:26] wide range of questions by saying
[00:52:27] certainly I can help you with that
[00:52:29] certainly I would be happy to do that
[00:52:31] certainly this is correct um uh and so
[00:52:34] we had a like certainly eval which is
[00:52:36] like how how often does the model say
[00:52:38] certainly uh uh but but look this is
[00:52:40] just a whack-a-mole like like what if it
[00:52:42] switches from certainly to definitely
[00:52:44] like uh uh so you know every time we add
[00:52:48] a new eval and we're always evaluating
[00:52:49] for all the old things so we have
[00:52:51] hundreds of these evaluations but we
[00:52:53] find that there's no substitute for
[00:52:55] human interacting with it and so it's
[00:52:57] very much like the ordinary product
[00:52:58] development process we have like
[00:53:00] hundreds of people within anthropic bash
[00:53:02] the model then we do uh you know then we
[00:53:05] do external AB tests sometimes we'll run
[00:53:08] tests with contractors we pay
[00:53:09] contractors to interact with the model
[00:53:12] um so you put all of these things
[00:53:14] together and it's still not perfect you
[00:53:16] still see behaviors that you don't quite
[00:53:18] want to see right you know you see you
[00:53:20] still see the model like refusing things
[00:53:22] that it just doesn't make sense to
[00:53:23] refuse um but I I I think trying to
[00:53:27] trying to solve this challenge right
[00:53:29] trying to stop the model from doing you
[00:53:31] know genuinely bad things that you know
[00:53:33] no one everyone agrees it shouldn't do
[00:53:35] right you know everyone everyone you
[00:53:37] know everyone agrees that you know the
[00:53:38] model shouldn't talk about you know I I
[00:53:40] don't know child abuse material right
[00:53:42] like everyone agrees the model shouldn't
[00:53:43] do that uh but but at the same time that
[00:53:46] it doesn't refuse in these dumb and
[00:53:47] stupid ways uh I think I think draw
[00:53:50] drawing that line as finely as possible
[00:53:53] approaching perfectly is still is still
[00:53:55] a challenge and we're getting better at
[00:53:57] it every day but there's there's a lot
[00:53:58] to be solved and again I would point to
[00:54:00] that as as an indicator of a challenge
[00:54:04] ahead in terms of steering much more
[00:54:05] powerful models do you think Claude 4.0
[00:54:10] is ever coming out I don't want to
[00:54:12] commit to any naming scheme because if I
[00:54:14] say if I say here we're gonna have
[00:54:17] Claude 4 next year and then and then you
[00:54:19] know then we decide that like you know
[00:54:20] we should start over because there's a
[00:54:22] new type of mod like I I I I I I don't
[00:54:24] want to I don't want to commit to it I
[00:54:25] would expect in a normal course of
[00:54:27] business that Claude four would come
[00:54:29] after Claude 3.5 but but you know you
[00:54:32] you you never know in this wacky field
[00:54:33] right but the sort of this idea of
[00:54:36] scaling is continuing scal scaling is
[00:54:39] continuing there there will definitely
[00:54:41] be more powerful models coming from us
[00:54:43] in the models that exist today that is
[00:54:45] that is certain or if there if there
[00:54:46] aren't we've we've deeply failed as a
[00:54:48] company okay can you explain the
[00:54:50] responsible scaling policy and the AI
[00:54:52] safety level standards ASL levels as
[00:54:55] much as I'm excited about the benefits
[00:54:57] of these models and you know we'll talk
[00:54:59] about that if we talk about Machines of
[00:55:01] Loving Grace um I'm I'm worried about
[00:55:04] the risk and I continue to be worried
[00:55:05] about the risks uh no one should think
[00:55:08] that you know Machines of loveing Grace
[00:55:09] was me me saying uh you know I'm no
[00:55:11] longer worried about the risks of these
[00:55:13] models I think they're two sides of the
[00:55:15] same coin the the uh Power of the models
[00:55:19] and their ability to solve all these
[00:55:21] problems in you know biology
[00:55:23] Neuroscience Economic Development
[00:55:25] government governance and peace large
[00:55:28] parts of the economy those those come
[00:55:30] with risks as well right with great
[00:55:32] power comes great responsibility right
[00:55:34] that's the the two are the two are
[00:55:35] paired uh things that are powerful can
[00:55:37] do good things and they can do bad
[00:55:39] things um I think of those risks as as
[00:55:42] being in you know several different
[00:55:43] different categories perhaps the two
[00:55:46] biggest risks that I think about and
[00:55:48] that's not to say that there aren't
[00:55:49] risks today that are that are important
[00:55:51] but when I think of the really the the
[00:55:53] you know the things that would happen on
[00:55:54] the grandest scale um one is what I call
[00:55:57] catastrophic misuse these are misuse of
[00:56:01] the models in domains like cyber bio
[00:56:05] radiological nuclear right things that
[00:56:07] could you know that could harm or even
[00:56:11] kill thousands even millions of people
[00:56:13] if they really really go wrong um like
[00:56:16] these are the you know number one
[00:56:17] priority to prevent and and here I would
[00:56:21] just make a simple observation which is
[00:56:23] that Mo the models you know if if I look
[00:56:27] today at people who have done really bad
[00:56:29] things in the world um uh I think
[00:56:32] actually Humanity has been protected by
[00:56:34] the fact that the overlap between really
[00:56:37] smart well-educated people and people
[00:56:39] who want to do really horrific things
[00:56:41] has generally been small like you know
[00:56:44] let's say let's say I'm someone who you
[00:56:46] know uh you know I have a PhD in this
[00:56:48] field I have a well-paying job um
[00:56:51] there's so much to lose why do I want to
[00:56:53] like you know even even assuming I'm
[00:56:55] completely evil which which most people
[00:56:57] are not um why why you know why would
[00:56:59] such a person risk their risk their you
[00:57:01] know risk their life RK risk their their
[00:57:04] legacy their reputation to to do
[00:57:06] something like you know truly truly evil
[00:57:09] if we had a lot more people like that
[00:57:10] the world would be a much more dangerous
[00:57:12] place and so my my My worry is that by
[00:57:15] being a a much more intelligent agent AI
[00:57:19] could break that correlation and so I I
[00:57:22] I I I do have serious worries about that
[00:57:24] I believe we can prevent those worries
[00:57:26] uh but you know I I think as a
[00:57:28] Counterpoint to Machines of Loving Grace
[00:57:29] I want to say that this is I there's
[00:57:31] still serious risks and and the second
[00:57:34] range of risks would be the autonomy
[00:57:35] risks which is the idea that models
[00:57:38] might on their own particularly as we
[00:57:40] give them more agency than they've had
[00:57:42] in the past uh particularly as we give
[00:57:44] them supervision over wider tasks like
[00:57:48] you know writing whole code bases or
[00:57:51] someday even you know effectively
[00:57:53] operating entire entire companies
[00:57:56] they're on a long enough leash are they
[00:57:58] are they doing what we really want them
[00:58:00] to do it's very difficult to even
[00:58:02] understand in detail what they're doing
[00:58:04] let alone let alone control it and like
[00:58:07] I said this these early signs that it's
[00:58:10] it's hard to perfectly draw the boundary
[00:58:12] between things the model should do and
[00:58:14] things the model shouldn't do that that
[00:58:16] you know if if you go to one side you
[00:58:18] get things that are annoying and useless
[00:58:20] and you go to the other side you get
[00:58:21] other behaviors if you fix one thing it
[00:58:23] creates other problems we're getting
[00:58:25] better and better at solving this I
[00:58:27] don't think this is an unsolvable
[00:58:29] problem I think this is a you know this
[00:58:30] is a science like like the safety of
[00:58:32] airplanes or the safety of cars or the
[00:58:34] safety of drugs I you know I I don't
[00:58:36] think there's any big thing we're
[00:58:38] missing I just think we need to get
[00:58:39] better at controlling these models and
[00:58:41] so these are these are the two risks I'm
[00:58:43] worried about and our responsible
[00:58:45] scaling plan which I'll recognize is a
[00:58:48] very long-winded answer to your question
[00:58:50] I love it I love it our responsible
[00:58:51] scaling plan is designed to address
[00:58:54] these two types of risks and so every
[00:58:57] time we develop a new model we basically
[00:59:00] test it for its ability to do both of
[00:59:04] these bad things so if I were to back up
[00:59:07] a little bit um I I think we have a I
[00:59:10] think we have an interesting dilemma
[00:59:11] with AI systems where they're not yet
[00:59:14] powerful enough to present these
[00:59:17] catastrophes I don't know that I don't
[00:59:19] know they'll ever present prevent these
[00:59:20] catastrophes it's possible they won't
[00:59:22] but the the case for worry the case for
[00:59:25] risk is strong enough that we should we
[00:59:27] should act now and and they're they're
[00:59:29] getting better very very fast right I
[00:59:32] you know I testified in the Senate that
[00:59:34] you know we might have serious bio risks
[00:59:36] within two to three years that was about
[00:59:37] a year ago things have preceded preceded
[00:59:41] a pace uh uh so we have this thing where
[00:59:44] it's like it's it's it's surprisingly
[00:59:46] hard to to address these risks because
[00:59:49] they're not here today they don't exist
[00:59:51] they're like ghosts but they're coming
[00:59:53] at us so fast because the models are
[00:59:54] improving so fast so so how do you deal
[00:59:56] with something that's not here today
[00:59:59] doesn't exist but is is coming at us
[01:00:02] very fast uh so the solution we came up
[01:00:05] with for that in in collaboration with
[01:00:08] uh you know people like uh the
[01:00:10] organization meter and Paul Christiano
[01:00:12] is okay what what what what you need for
[01:00:15] that or you need tests to tell you when
[01:00:18] the risk is getting close you need an
[01:00:20] early warning system and and so every
[01:00:22] time we have uh a new model we test it
[01:00:25] for it capability to do these cbrn tasks
[01:00:29] as well as testing it for you know how
[01:00:32] capable it is of doing tasks
[01:00:33] autonomously on its own and uh in the
[01:00:36] latest version of our RSP which we
[01:00:38] released in the last in the last month
[01:00:40] or two uh the way we test autonomy risks
[01:00:44] is the model the the AI model's ability
[01:00:47] to do aspects of AI research itself uh
[01:00:51] which when the model when the AI models
[01:00:52] can do AI research they become kind of
[01:00:54] truly truly autonomous on and that you
[01:00:56] know that threshold is important for a
[01:00:58] bunch of other ways and and so what do
[01:01:01] we then do with these tasks the RSP
[01:01:04] basically develops what we've called an
[01:01:06] if then structure which is if the models
[01:01:10] pass a certain capability then we impose
[01:01:13] a certain set of Safety and Security
[01:01:15] requirements on them so today's models
[01:01:17] are what's called
[01:01:19] asl2 models that were a asl1 is for
[01:01:22] systems that manifestly don't pose any
[01:01:26] risk of autonomy or misuse so for
[01:01:28] example a chess plane bot deep blue
[01:01:31] would be asl1 it's just manifestly the
[01:01:34] case that you can't use deep blue for
[01:01:37] anything other than chess it was just
[01:01:38] designed for chess no one's going to use
[01:01:40] it to like you know to conduct a
[01:01:42] masterful Cyber attack or to you know
[01:01:45] run wild and take over the world asl2 is
[01:01:48] today's AI systems where we've measured
[01:01:51] them and we think these systems are
[01:01:53] simply not smart enough to uh to you
[01:01:56] know autonomously self-replicate or
[01:01:59] conduct a bunch of tasks uh and also not
[01:02:02] smart enough to provide meaningful
[01:02:05] information about cbrn risks and how to
[01:02:09] build cbrn weapons above and beyond what
[01:02:12] can be known from looking at Google uh
[01:02:15] in fact sometimes they do provide
[01:02:16] information but but not above and beyond
[01:02:19] a search engine but not in a way that
[01:02:20] can be stitched together um not not in a
[01:02:23] way that kind of end to end is dangerous
[01:02:25] enough so
[01:02:27] asl3 is going to be the point at which
[01:02:30] uh the models are helpful enough to
[01:02:33] enhance the capabilities of non-state
[01:02:36] actors right State actors can already do
[01:02:39] a lot a lot of unfortunately to a high
[01:02:41] level of proficiency a lot of these very
[01:02:43] dangerous and destructive things the
[01:02:45] difference is that non-state non-state
[01:02:48] actors are not capable of it and so when
[01:02:50] we get to asl3 we'll take special
[01:02:53] security precautions designed to be be
[01:02:56] sufficient to prevent theft of the model
[01:02:58] by non-state actors and misuse of the
[01:03:01] model as it's deployed uh will have to
[01:03:03] have enhanced filters targeted at these
[01:03:06] particular areas cyber bio nuclear cyber
[01:03:09] bio nuclear and model autonomy Which is
[01:03:12] less a misuse risk and more a risk of
[01:03:14] the model doing bad things itself asl4
[01:03:18] getting to the point where these models
[01:03:21] could could enhance the capability of a
[01:03:24] of a of a all knowledgeable State actor
[01:03:27] Andor become the you know the main
[01:03:30] source of such a risk like if you wanted
[01:03:32] to engage in such a risk the main way
[01:03:34] you would do it is through a model and
[01:03:36] then I think asl4 on the autonomy side
[01:03:38] it's it's some some some amount of
[01:03:40] acceleration in AI research capabilities
[01:03:43] with an with an AI model and then asl5
[01:03:46] is where we would get to the models that
[01:03:47] are you know that are that are kind of
[01:03:49] that are kind of you know truly capable
[01:03:50] that it could exceed Humanity in their
[01:03:52] ability to do to do any of these tasks
[01:03:55] and so the the the point of the if then
[01:03:58] structure commitment is is basically to
[01:04:01] say
[01:04:02] look I don't know I've been I've been
[01:04:04] working with these models for many years
[01:04:06] and I've been worried about risk for
[01:04:07] many years it's actually kind of
[01:04:09] dangerous to cry wolf it's actually kind
[01:04:11] of dangerous to say this you know this
[01:04:14] this model is this model is risky and
[01:04:17] you know people look at it and they say
[01:04:18] this is manifestly not dangerous again
[01:04:21] it's it's it's the the delicacy of the
[01:04:24] risk isn't here to today but it's coming
[01:04:26] at us fast how do you deal with that
[01:04:28] it's it's really vexing to a risk
[01:04:30] planner to deal with it and so this if
[01:04:32] then structure basically says look we
[01:04:35] don't want to antagonize a bunch of
[01:04:36] people we don't want to harm our own you
[01:04:39] know our our kind of own ability to have
[01:04:41] a place in the conversation by imposing
[01:04:44] these
[01:04:45] these very honorous burdens on models
[01:04:49] that are not dangerous today so the if
[01:04:51] then the trigger commitment is basically
[01:04:53] a way to deal with this says you claim
[01:04:55] clamp down hard when you can show that
[01:04:57] the model is dangerous and of course
[01:04:59] what has to come with that is you know
[01:05:01] enough of a buffer threshold that that
[01:05:03] you know you can you can uh you know
[01:05:05] you're you're you're you're not at high
[01:05:07] risk of kind of missing the danger it's
[01:05:08] not a perfect framework we've had to
[01:05:10] change it every every uh you know we
[01:05:13] came out with a new one just a few weeks
[01:05:15] ago and probably probably going forward
[01:05:17] we might release new ones multiple times
[01:05:19] a year because it's it's hard to get
[01:05:21] these policies right like technically
[01:05:23] organizationally from a research
[01:05:25] perspective but that is the proposal if
[01:05:27] then commitments and triggers in order
[01:05:30] to minimize burdens and false alarms now
[01:05:34] but really react appropriately when the
[01:05:36] dangers are here what do you think the
[01:05:37] timeline for asl3 is where several of
[01:05:40] the triggers are fired and what do you
[01:05:42] think the timeline is for asl4 yeah so
[01:05:45] that is hotly debated within the company
[01:05:47] um uh we are working actively to prepare
[01:05:51] asl3 uh security uh security measures as
[01:05:54] well as ASL three deployment measures um
[01:05:57] I'm not going to go into detail but
[01:05:58] we've made we've made a lot of progress
[01:06:00] on both and you know we're we're
[01:06:02] prepared to be I think ready quite soon
[01:06:05] uh I would I would not be surpris I
[01:06:07] would not be surprised at all if we hit
[01:06:09] ASL 3 uh next year there was some
[01:06:12] concern that we we might even hit it uh
[01:06:14] uh this year that's still that's still
[01:06:16] possible that could still happen it's
[01:06:18] like very hard to say but like I would
[01:06:20] be very very surprised if it was like
[01:06:22] 2030 uh I think it's much sooner than
[01:06:24] that so there's a protocols for
[01:06:26] detecting it the if then and then
[01:06:29] there's protocols for how to respond to
[01:06:31] it yes how difficult is the second the
[01:06:34] ladder yeah I think for asl3 it's
[01:06:36] primarily about security um and and
[01:06:40] about you know filters on the model
[01:06:42] relating to a very narrow set of areas
[01:06:45] when we deploy the model because at asl3
[01:06:48] the model isn't autonomous yet um uh and
[01:06:51] and so you don't have to worry about you
[01:06:53] know kind of the model itself behaving
[01:06:55] in a bad way even when it's deployed
[01:06:57] internally so I think the asl3 measures
[01:07:00] are are I won't say straightforward
[01:07:02] they're they're they're they're rigorous
[01:07:04] but they're easier to reason about I
[01:07:06] think once we get to
[01:07:08] asl4 um we start to have worries about
[01:07:12] the models being smart enough that they
[01:07:14] might sandbag tests they might not tell
[01:07:16] the truth about tests um we had some
[01:07:19] results came out about like sleeper
[01:07:21] agents and there was a more recent paper
[01:07:23] about you know can can the models uh uh
[01:07:26] mislead attempts to you know s sandbag
[01:07:29] their own abilities right show them you
[01:07:31] know uh uh present themselves as being
[01:07:33] less capable than they are and so I
[01:07:35] think with asl4 there's going to be an
[01:07:38] important component of using other
[01:07:41] things than just interacting with the
[01:07:42] models for example interpretability or
[01:07:45] hidden chains of thought uh where you
[01:07:47] have to look inside the model and verify
[01:07:49] via some other mechanism that that is
[01:07:52] not you know is not as easily corrupted
[01:07:54] as what the model says
[01:07:56] uh that that you know that that that the
[01:07:58] model indeed has some property uh so
[01:08:00] we're still working on asl4 one of the
[01:08:03] properties of the RSP is that we we
[01:08:06] don't specify asl4 until we've hit ASL 3
[01:08:10] be and and I think that's proven to be a
[01:08:12] wise decision because even with asl3 it
[01:08:15] again it's hard to know this stuff in
[01:08:16] detail and and it it we want to take as
[01:08:19] much time as we can possibly take to get
[01:08:22] these things right so for asl3 the bad
[01:08:24] actor will be the humans humans yes and
[01:08:27] so there it's a little bit more uh for
[01:08:29] asl4 it's both I think it's both and so
[01:08:32] deception and that's where mechanistic
[01:08:34] interpretability comes into play and
[01:08:37] hopefully the techniques used for that
[01:08:39] are not made accessible to the model
[01:08:42] yeah I mean of course you can hook up
[01:08:44] the mechanistic contribut ability to the
[01:08:46] model itself um but then You' then then
[01:08:48] you then you've kind of lost it as a
[01:08:50] reliable indicator of uh of uh of of of
[01:08:53] the model State there are a bunch of
[01:08:55] exotic ways you can think of that it
[01:08:56] might also not be reliable like if the
[01:08:59] you know model gets smart enough that it
[01:09:00] can like you know jump computers and
[01:09:02] like read the code where you're like
[01:09:04] looking at its internal State we've
[01:09:06] thought about some of those I think
[01:09:07] they're exotic enough there are ways to
[01:09:09] render them unlikely but yeah generally
[01:09:11] you want to you want to preserve
[01:09:13] mechanistic interpretability as a kind
[01:09:15] of verification set or test set that's
[01:09:17] separate from the training process of
[01:09:18] the model see I think uh as these models
[01:09:21] become better and better conversation
[01:09:22] and become smarter social engineering
[01:09:25] becomes a threat too cuz they oh yeah
[01:09:27] that can start being very convincing to
[01:09:29] the engineers inside companies oh yeah
[01:09:31] yeah it's actually like you know we've
[01:09:33] we've seen lots of examples of
[01:09:34] demagoguery in our life from humans and
[01:09:36] and you know there's a concern that
[01:09:37] models could do that could do that as
[01:09:39] well one of the ways that cloud has been
[01:09:41] getting more and more powerful is it's
[01:09:43] now able to do some agentic stuff um
[01:09:47] computer use uh there's also an analysis
[01:09:49] within the sandbox of claw. a itself but
[01:09:52] let's talk about computer use that's
[01:09:54] seems to me super exciting that you can
[01:09:57] just give Claude a task and it uh takes
[01:09:59] a bunch of actions figures it out and
[01:10:01] has access to the your computer through
[01:10:05] screenshots so can you explain how that
[01:10:07] works uh and where that's headed yeah
[01:10:11] it's actually relatively simple so
[01:10:12] Claude has has had for a long time since
[01:10:14] since Claude 3 back in March the ability
[01:10:17] to analyze images and respond to them
[01:10:20] with text the the only new thing we
[01:10:22] added is those images can be screenshot
[01:10:25] shots of a computer and in response we
[01:10:28] train the model to give a location on
[01:10:30] the screen where you can click Andor
[01:10:32] buttons on the keyboard you can press in
[01:10:34] order to take action and it turns out
[01:10:37] that with actually not all that much
[01:10:39] additional training the models can get
[01:10:41] quite good at that task it's a good
[01:10:43] example of generalization um you know
[01:10:45] people sometimes say if you get to low
[01:10:47] earth orbit you're like halfway to
[01:10:48] anywhere right because of how much it
[01:10:49] takes to escape the gravity well if you
[01:10:52] have a strong pre-trained model I feel
[01:10:53] like you're halfway to anywhere uh in
[01:10:55] ter in terms of in terms of the
[01:10:56] intelligence space uh uh uh and and and
[01:11:00] so actually it didn't it didn't take all
[01:11:02] that much to get to get Claude to do
[01:11:04] this and you can just set that in a loop
[01:11:08] give the model a screenshot tell it what
[01:11:09] to click on give it the next screenshot
[01:11:11] tell it what to click on and and that
[01:11:13] turns into a full kind of almost almost
[01:11:15] 3D video interaction of the model and
[01:11:18] it's able to do all of these tasks right
[01:11:20] you know we we showed these demos where
[01:11:21] it's able to like fill out spreadsheets
[01:11:24] it's able to kind of like interact with
[01:11:26] a website it's able to you know um you
[01:11:30] know it's able to open all kinds of you
[01:11:31] know programs different operating
[01:11:33] systems Windows Linux Mac uh uh so uh
[01:11:38] you know I think all of that is very
[01:11:39] exciting I I will say while in theory
[01:11:42] there's nothing you could do there that
[01:11:44] you couldn't have done through just
[01:11:45] giving the model the API to drive the
[01:11:47] computer screen uh this really lowers
[01:11:50] the barrier and you know there's there's
[01:11:52] there's a lot of folks who who who
[01:11:54] either you know kind of kind of ar ar
[01:11:56] you know aren't in a position to to
[01:11:57] interact with those apis or it takes
[01:11:59] them a long time to do it's just the
[01:12:01] screen is just a universal interface
[01:12:03] that's a lot easier to interact with and
[01:12:04] so I expect over time this is going to
[01:12:06] lower a bunch of barriers now honestly
[01:12:09] the current model has there's there it
[01:12:11] leaves a lot still to be desired and we
[01:12:13] were we were honest about that in the
[01:12:15] blog right it makes mistakes it
[01:12:17] misclicks and we we you know we were
[01:12:19] careful to warn people hey this thing
[01:12:21] isn't you can't just leave this thing to
[01:12:23] you know run on your computer for
[01:12:24] minutes and minutes um you got to give
[01:12:27] this thing boundaries and guard rails
[01:12:29] and I think that's one of the reasons we
[01:12:31] released it first in an API form rather
[01:12:33] than kind of you know this this kind of
[01:12:35] just just hand it just hand it to the
[01:12:37] consumer and give it control of their of
[01:12:39] their of their of their computer um but
[01:12:42] but you know I definitely feel that it's
[01:12:44] important to get these capabilities out
[01:12:45] there as models get more powerful we're
[01:12:47] going to have to Grapple with you know
[01:12:49] how do we use these capabilities safely
[01:12:51] how do we prevent them from being abused
[01:12:54] uh and and you know I think I think
[01:12:56] releasing releasing the model while
[01:12:58] while while the capabilities are are you
[01:13:00] know are are still are still limited is
[01:13:02] is is very helpful in terms of in terms
[01:13:05] of doing that um you know I think since
[01:13:07] it's been released a number of customers
[01:13:09] I think uh repet was maybe was maybe one
[01:13:12] of the the the most uh uh quickest
[01:13:14] quickest quickest to quickest to deploy
[01:13:16] things um have have you know have made
[01:13:19] use of it in various ways people have
[01:13:20] hooked up demos for you know Windows
[01:13:23] desktops Macs
[01:13:25] uh uh you know Linux Linux machines uh
[01:13:29] so yeah it's been it's been it's been
[01:13:31] very exciting I think as with as with
[01:13:32] anything else you know it it it comes
[01:13:35] with new exciting abilities and then
[01:13:37] then then you know then then with those
[01:13:39] new exciting abilities we have to think
[01:13:41] about how to how to you know make the
[01:13:42] model you know safe reliable do what
[01:13:45] humans want them to do I mean it's the
[01:13:47] same it's the same story for everything
[01:13:48] right same thing it's that same tension
[01:13:51] but but the possibility of use cases
[01:13:52] here is just the the range is incredible
[01:13:55] so uh how much to make it work really
[01:13:57] well in the future how much do you have
[01:13:59] to specially kind of uh go beyond what's
[01:14:03] the pre-trained models doing do more
[01:14:05] posttraining rhf or supervised
[01:14:07] fine-tuning or synthetic data just for
[01:14:09] the agent stff yeah I think speaking at
[01:14:11] a high level It's Our intention to keep
[01:14:13] investing a lot in you know making
[01:14:16] making the model better uh like I think
[01:14:18] I think uh you know we look at look at
[01:14:20] some of the you know some of the
[01:14:21] benchmarks where previous models were
[01:14:23] like oh could do it 6% of the time and
[01:14:25] now our model do at 14 or 22% of the
[01:14:28] time and yeah we want to get up to you
[01:14:29] know the human level reliability of 80
[01:14:31] 90% just like anywhere else right we're
[01:14:33] on the same curve that we were on with
[01:14:35] sbench where I think I would guess a
[01:14:37] year from now the models can do this
[01:14:38] very very reliably but you got to start
[01:14:40] somewhere so you think it's possible to
[01:14:42] get to the the human level 90% uh
[01:14:45] basically doing the same thing you're
[01:14:46] doing now or is it has to be special for
[01:14:48] computer use I I mean uh depends what
[01:14:51] you mean by by you know special and FAL
[01:14:54] and
[01:14:55] um but but you know I generally think
[01:14:58] you know the same kinds of techniques
[01:15:00] that we've been using to train the
[01:15:01] current model I I expect that doubling
[01:15:03] down in those techniques in the same way
[01:15:05] that we have for code for code for
[01:15:07] models in general for other k for you
[01:15:10] know for image input um uh you know for
[01:15:13] voice uh I expect those same techniques
[01:15:16] will scale here as they have everywhere
[01:15:17] else but this is giving sort of the
[01:15:20] power of action to Claude And so you
[01:15:23] could do a lot of really powerful things
[01:15:25] but you could do a lot of damage also
[01:15:26] yeah yeah no and we've been very aware
[01:15:28] of that look my my view actually is
[01:15:31] computer use isn't a fundamentally new
[01:15:34] capability like the cbrn or autonomy
[01:15:37] capabilities are um it's more like it
[01:15:40] kind of opens the aperture for the model
[01:15:42] to use and apply its existing abilities
[01:15:45] uh and and so the way we think about it
[01:15:47] going back to our RSP is nothing that
[01:15:50] this model is
[01:15:52] doing inherently increases
[01:15:55] you know the risk from an RSP RSP
[01:15:58] perspective but as the models get more
[01:16:00] powerful having this capability may make
[01:16:03] it scarier once it you know once it has
[01:16:06] the cognitive capability to um you know
[01:16:09] to do something at the asl3 and asl4
[01:16:12] level this this you know this may be the
[01:16:15] thing that kind of Unbound it from doing
[01:16:17] so so going forward certainly this
[01:16:20] modality of interaction is something we
[01:16:22] have tested for and that we will
[01:16:23] continue to test for in our going
[01:16:25] forward um I think it's probably better
[01:16:27] to have to learn and explore this
[01:16:29] capability before the model is super uh
[01:16:31] you know super capable yeah and there's
[01:16:33] uh a lot of interesting attacks like
[01:16:34] prompt injection because now you've
[01:16:36] widened the aperture so you can prompt
[01:16:38] inject through stuff on screen so if
[01:16:41] this becomes more and more useful then
[01:16:43] there's more and more benefit to inject
[01:16:46] inject stuff into the model if it goes
[01:16:48] to certain web page it could be harmless
[01:16:50] stuff like advertisements or it could be
[01:16:52] like harmful stuff right yeah I mean we
[01:16:54] thought a lot about like spam capture
[01:16:56] you know Mass C there's all you know
[01:16:58] every every like if one secret I'll tell
[01:17:02] you if you've invented a new technology
[01:17:04] not necessarily the biggest misuse but
[01:17:06] but the the first misuse you'll see
[01:17:08] scams just Petty scams like you just
[01:17:12] just just it's it's like it's like a
[01:17:14] thing as old people scamming each other
[01:17:15] it's it's this it's this thing as old as
[01:17:17] time um and and and it's just every time
[01:17:20] you got to deal with it it's almost like
[01:17:22] silly to say but it's it's true sort of
[01:17:25] and spam in general is a thing as it
[01:17:28] gets more and more intelligent it's uh
[01:17:31] there a lot of like like I said like
[01:17:32] there are a lot of petty criminals in
[01:17:34] the world and and and you know it's like
[01:17:36] every new technology is like a new way
[01:17:38] for petty petty criminals to do
[01:17:40] something you know something stupid and
[01:17:43] malicious um is there any ideas about
[01:17:46] sandboxing it like how difficult is the
[01:17:48] sandboxing task yeah we sandbox during
[01:17:51] training so for example during training
[01:17:52] we didn't expose the model to the
[01:17:54] internet um I think that's probably a
[01:17:55] bad idea during training because uh you
[01:17:58] know the model can be changing its
[01:17:59] policy it can be changing what it's
[01:18:00] doing and it's having an effect in the
[01:18:02] real world um uh you know in in terms of
[01:18:05] actually deploying the model right it
[01:18:09] kind of depends on the application like
[01:18:10] you know sometimes you want the model to
[01:18:12] do something in the real world but of
[01:18:13] course you can always put guard you can
[01:18:15] always put guard rails on the outside
[01:18:17] right you can say okay well you know
[01:18:19] this model is not going to move data
[01:18:21] from my you know this model is not going
[01:18:23] to move any files from my computer to or
[01:18:25] my web server to anywhere else now when
[01:18:28] you talk about sandboxing again when we
[01:18:30] get to asl4 none of these precautions
[01:18:33] are going to make sense there right
[01:18:35] where when you when you talk about asl4
[01:18:37] you're then the model is being kind of
[01:18:40] you know there's a a theoretical worry
[01:18:42] the model could be smart enough to break
[01:18:44] it to to kind of break out of any box
[01:18:46] and so there we need to think about
[01:18:48] mechanistic interpretability about you
[01:18:50] know if we're if we're going to have a
[01:18:52] Sandbox it would need to be a
[01:18:53] mathematically provable sound but you
[01:18:55] know that's that's a whole different
[01:18:57] world than what we're dealing with with
[01:18:59] the models
[01:19:00] today yeah the science of building a box
[01:19:04] from which asl4 AI system cannot Escape
[01:19:08] I I think it's probably not the right
[01:19:09] approach I think the right approach
[01:19:11] instead of having something you know
[01:19:13] unaligned that that like you're trying
[01:19:15] to prevent it from escaping I think it's
[01:19:17] it's better to just design the model the
[01:19:19] right way or have a loop where you you
[01:19:21] know you look inside you look inside the
[01:19:23] model and you're able to verify property
[01:19:25] and that gives you an opportunity to
[01:19:27] like iterate and actually get it right
[01:19:29] um I think I think containing uh
[01:19:31] containing bad models is is is much
[01:19:33] worse solution than having good models
[01:19:35] let me ask about regulation what's the
[01:19:37] role of regulation in keeping AI safe so
[01:19:40] for example he described California AI
[01:19:43] regulation Bill SB 1047 that was
[01:19:46] ultimately vetoed by the governor what
[01:19:48] are the pros and cons of this bill
[01:19:50] General yes we ended up making some
[01:19:51] suggestions to the bill and then some of
[01:19:53] those were opted and you know we felt I
[01:19:56] think I think quite positively uh uh
[01:19:59] quite positively about about the bill uh
[01:20:02] by by the end of that um it did still
[01:20:04] have some downsides um uh and you know
[01:20:07] of course of course it got vetoed um I
[01:20:09] think at a high level I think some of
[01:20:11] the key ideas behind the bill um are you
[01:20:15] know I would say similar to ideas behind
[01:20:16] our rsps and I think it's very important
[01:20:19] that some jurisdiction whether it's
[01:20:21] California or the federal government
[01:20:23] Andor other countries and other states
[01:20:26] passes some regulation like this and I
[01:20:29] can talk through why I think that's so
[01:20:31] important so I feel good about our RSP
[01:20:33] it's not perfect it needs to be iterated
[01:20:35] on a lot but it's been a good forcing
[01:20:38] function for getting the company to take
[01:20:42] these risks seriously to put them into
[01:20:44] product planning to really make them a
[01:20:46] central part of work at anthropic and to
[01:20:49] make sure that all the thousand people
[01:20:50] and it's almost a thousand people now at
[01:20:52] anthropic understand that this is one of
[01:20:54] the highest priorities of the company if
[01:20:56] not the highest priority uh
[01:20:59] but one there are some there are still
[01:21:02] some companies that don't have RSP like
[01:21:05] mechanisms like open aai Google uh did
[01:21:08] adopt these mechanisms a couple months
[01:21:10] after uh after anthropic did uh but
[01:21:14] there are there are other companies out
[01:21:15] there that don't have these mechanisms
[01:21:17] at all uh and so if some companies adopt
[01:21:20] these mechanisms and others don't uh
[01:21:23] it's really going to create a situation
[01:21:25] where you know some of these dangers
[01:21:27] have the property that it doesn't matter
[01:21:29] if three out of five of the companies
[01:21:30] are being safe if the other two are are
[01:21:32] being are being unsafe it creates this
[01:21:34] negative externality and and I think the
[01:21:37] lack of uniformity is not fair to those
[01:21:39] of us who have put a lot of effort into
[01:21:41] being very thoughtful about these
[01:21:42] procedures the second thing is I don't
[01:21:45] think you can trust these companies to
[01:21:47] adhere to these voluntary plans in their
[01:21:50] own right I like to think that anthropic
[01:21:52] will we do everything we can that we
[01:21:54] will our our our our RSP is checked by
[01:21:57] our long-term benefit trust uh so you
[01:22:00] know we do everything we can to to to
[01:22:04] adhere to our own RSP um but you know
[01:22:08] you hear lots of things about various
[01:22:10] companies saying oh they said they would
[01:22:12] do they said they would give this much
[01:22:13] compute and they didn't they said they
[01:22:15] would do this thing and they didn't um
[01:22:17] you know I don't I don't think it makes
[01:22:18] sense to you know to to to you know
[01:22:21] litigate particular things that
[01:22:23] companies have done but I I think this
[01:22:25] this broad principle that like if
[01:22:27] there's nothing watching over them
[01:22:28] there's nothing watching over us as an
[01:22:30] industry there's no guarantee that we'll
[01:22:32] do the right thing and the stakes are
[01:22:33] very high uh and so I think it's I think
[01:22:36] it's important to have a uniform
[01:22:38] standard that that that that that
[01:22:40] everyone follows and to make sure that
[01:22:43] simply that the industry does what a
[01:22:46] majority of the industry has already
[01:22:47] said is important and has already said
[01:22:50] that they definitely will do right some
[01:22:52] people uh you know I think there's there
[01:22:54] a class of people who are against
[01:22:57] regulation on principle I understand
[01:22:59] where that comes from if you go to
[01:23:00] Europe and you know you see something
[01:23:01] like gdpr you see some of the other
[01:23:04] stuff that that that that that they've
[01:23:06] done you know some of it's good but but
[01:23:08] some of it is really unnecessarily
[01:23:10] burdensome and I think it's fair to say
[01:23:12] really has slowed really has slowed
[01:23:14] Innovation and so I understand where
[01:23:16] people are coming from on priors I
[01:23:18] understand why people come from start
[01:23:20] from that start from that position uh
[01:23:23] but but again I think AI is different if
[01:23:25] we go to the very serious risks of
[01:23:28] autonomy and misuse that that that I
[01:23:31] talked about you know just a just a few
[01:23:33] minutes ago I think that those are
[01:23:37] unusual and they weren't an unusually
[01:23:41] strong response uh and so I I think it's
[01:23:43] very important again um we need
[01:23:46] something that everyone can get behind
[01:23:48] uh you know I think one of the issues
[01:23:51] with
[01:23:52] s1047 uh especially the original version
[01:23:55] of it was it it had a bunch of the
[01:23:59] structure of rsps but it also had a
[01:24:01] bunch of stuff that was either clunky or
[01:24:04] that that that just would have created a
[01:24:07] bunch of burdens a bunch of Hassle and
[01:24:10] might even have missed the Target in
[01:24:12] terms of addressing the risks um you
[01:24:14] don't really hear about it on Twitter
[01:24:16] you just hear about kind of you know
[01:24:18] people are people are cheering for any
[01:24:20] regulation and then the folks who are
[01:24:22] against make up these often quite
[01:24:24] intellectually dishonest arguments about
[01:24:26] how you know it you know it'll make us
[01:24:28] move away from California bill bill
[01:24:31] doesn't apply if you're headquartered in
[01:24:33] California bill only applies if you do
[01:24:34] business in California um or that it
[01:24:36] would damage the open source ecosystem
[01:24:39] or that it would you know it would cause
[01:24:41] cause all of these things I I think
[01:24:44] those were mostly nonsense but there are
[01:24:46] better arguments against regulation
[01:24:49] there's one guy uh Dean ball who's
[01:24:51] really you know I think a very scholarly
[01:24:53] scholarly IST who who looks at what
[01:24:55] happens when a regulation is put in
[01:24:57] place and ways that they can kind of get
[01:25:00] a life of their own or how they can be
[01:25:02] poorly designed and so our interest has
[01:25:05] always been we do think there should be
[01:25:07] regulation in this space but we want to
[01:25:10] be an actor who makes sure that that
[01:25:13] that that regulation is something that's
[01:25:15] surgical that's targeted at the serious
[01:25:18] risks and is something people can
[01:25:20] actually comply with because something I
[01:25:22] think The Advocates of Regulation don't
[01:25:24] understand as well as they could is if
[01:25:27] we get something in place that is um
[01:25:31] that's poorly targeted that wastes a
[01:25:34] bunch of people's time what's going to
[01:25:37] happen is people are going to say see
[01:25:39] these safety risks there you know this
[01:25:41] is this is nonsense I just you know I
[01:25:43] just had to hire 10 lawyers to to you
[01:25:46] know to fill out all these forms I had
[01:25:47] to run all these tests for something
[01:25:49] that was clearly not dangerous and after
[01:25:51] 6 months of that there will be there
[01:25:53] will be a ground sweep well and we'll
[01:25:55] we'll we'll we'll end up with a durable
[01:25:57] consensus against regulation and so the
[01:26:00] I I think the the worst enemy of those
[01:26:02] who want real accountability is badly
[01:26:05] designed regulation um we we need to
[01:26:07] actually get it right uh and and this is
[01:26:09] if there's one thing I could say to The
[01:26:11] Advocates it it would be that I want
[01:26:13] them to understand this Dynamic better
[01:26:15] and we need to be really careful and we
[01:26:17] need to talk to people who actually have
[01:26:19] who actually have experience seeing how
[01:26:22] regulations play out in practice and and
[01:26:24] the people who have seen that understand
[01:26:26] to be very careful if this was some
[01:26:28] lesser issue I might be against
[01:26:30] regulation at all but what what I want
[01:26:33] the opponents to understand is is that
[01:26:36] the underlying issues are actually
[01:26:38] serious they're they're not they're not
[01:26:41] something that I or the other companies
[01:26:43] are just making up because of regulatory
[01:26:46] capture they're not sci-fi fantasies
[01:26:49] they're not they're not any of these
[01:26:51] things um you know every every time we
[01:26:54] have new model every few months we
[01:26:55] measure the behavior of these models and
[01:26:58] they're getting better and better at
[01:27:00] these concerning tasks just as they are
[01:27:01] getting better and better at um you know
[01:27:05] good valuable economically useful tasks
[01:27:08] and so I I I I would just love it if
[01:27:12] some of the former you know I think
[01:27:14] sb147 was very polarizing I would love
[01:27:16] it if some of the most reasonable
[01:27:20] opponents and some of the most
[01:27:22] reasonable um uh proponents uh would sit
[01:27:26] down together and you know I think I
[01:27:28] think that you know the different the
[01:27:30] different AI companies um you know
[01:27:32] anthropic was the the only AI company
[01:27:35] that you know felt positively in a very
[01:27:37] detailed way I think Elon tweeted uh
[01:27:39] tweeted briefly something positive but
[01:27:42] you know some of the some of the big
[01:27:43] ones like Google open AI meta Microsoft
[01:27:46] were were pretty St stly against so I
[01:27:49] would really like is if if you know some
[01:27:51] of the key stakeholders some of the you
[01:27:53] know thoughtful proponents and and some
[01:27:55] of the most thoughtful opponents would
[01:27:57] sit down and say how do we solve this
[01:27:59] problem in in a way that the proponents
[01:28:02] feel brings a real reduction in risk and
[01:28:06] that the opponents feel that it is not
[01:28:10] it is not hampering the the industry or
[01:28:12] hampering Innovation any more necessary
[01:28:15] than it than than than it needs to and
[01:28:18] and I think for for whatever reason that
[01:28:21] things got too polarized and those two
[01:28:23] groups
[01:28:24] didn't get to sit down in the way that
[01:28:26] they should uh and and I feel I feel
[01:28:28] urgency I really think we need to do
[01:28:30] something in
[01:28:31] 2025 uh uh you know if we get to the end
[01:28:34] of 2025 and we've still done nothing
[01:28:36] about this then I'm going to be worried
[01:28:38] I'm not I'm not worried yet because
[01:28:40] again the risks aren't here yet but but
[01:28:42] I I I think time is running short yeah
[01:28:44] and come up with something surgical like
[01:28:46] you said yeah yeah yeah exactly and and
[01:28:48] we need to get we need to get away from
[01:28:50] this this this intense
[01:28:54] pro- safety versus intense
[01:28:57] anti-regulatory rhetoric right it's
[01:28:59] turned into these these flame Wars on
[01:29:01] Twitter and nothing Good's going to come
[01:29:03] with that so there's a lot of curiosity
[01:29:05] about the different players in the game
[01:29:07] one of the uh ogs is open AI you have
[01:29:10] had several years of experience at open
[01:29:11] AI what's your story and history there
[01:29:14] yeah so I was at open AI for uh for
[01:29:16] roughly five years uh for the last I
[01:29:19] think it was a couple years you know I I
[01:29:21] I I I I was uh vice president of
[01:29:23] research there um probably myself and
[01:29:25] Ilia suger were the ones who you know
[01:29:27] really kind of set the set the research
[01:29:29] Direction around 2016 or 2017 I first
[01:29:33] started to really believe in or at least
[01:29:35] confirm my belief in the scaling
[01:29:37] hypothesis when when Ilia famously said
[01:29:39] to me the thing you need to understand
[01:29:41] about these models is they just want to
[01:29:42] learn the models just want to learn um
[01:29:45] and and and and again sometimes there
[01:29:46] are these One S there these one
[01:29:48] sentences these Zen cones that you hear
[01:29:50] them and you're like ah that that
[01:29:53] explains everything that explains like a
[01:29:55] thousand things that I've seen and then
[01:29:56] and then I I you know ever after I had
[01:29:59] this visualization in my head of like
[01:30:01] you optimize the models in the right way
[01:30:02] you point the models in the right way
[01:30:04] they just want to learn they just want
[01:30:05] to solve the problem regardless of what
[01:30:07] the problem is so get out of their way
[01:30:09] basically get out of their way yeah
[01:30:11] don't impose your own ideas about how
[01:30:13] they should learn and you know this was
[01:30:15] the same thing as Rich Sutton put out in
[01:30:17] the bitter lesson or G put out in the
[01:30:19] scaling hypothesis you know I think
[01:30:21] generally the dynamic was you know I got
[01:30:24] I got this kind of inspiration from uh
[01:30:26] from from from Ilan from others folks
[01:30:29] like Alec Radford who did the the
[01:30:31] original uh uh
[01:30:32] gpt1 uh and then uh ran really hard with
[01:30:36] it me me and my collaborators on gpt2
[01:30:39] gpt3 RL from Human feedback which was an
[01:30:42] attempt to kind of deal with the early
[01:30:43] safety and durability things like debate
[01:30:46] and amplification heavy on
[01:30:48] interpretability so again the
[01:30:50] combination of safety plus scaling
[01:30:53] probably 2018 2019 2020 those those were
[01:30:56] those were kind of the years when myself
[01:30:59] and my collaborators probably um you
[01:31:03] know mo mo many many of whom became
[01:31:05] co-founders of anthropic kind of really
[01:31:07] had had had a vision and like and like
[01:31:09] drove the direction why'd you leave why'
[01:31:12] you decid to leave yeah so look I'm
[01:31:15] gonna put things this way and I you know
[01:31:16] I think it I think it ties to the to to
[01:31:18] the race to the top right which is you
[01:31:21] know in my time at open AI what I come
[01:31:23] come to see as I'd come to appreciate
[01:31:25] the scaling hypothesis and as I'd come
[01:31:27] to appreciate kind of the importance of
[01:31:29] safety along with the scaling hypothesis
[01:31:32] the first one I think you know open AI
[01:31:33] was was getting was getting on board
[01:31:35] with um the second one in a way had
[01:31:38] always been part of of open ai's
[01:31:40] messaging um but uh you know over over
[01:31:43] many years of of the time the time that
[01:31:45] I spent there I think I had a particular
[01:31:48] vision of how these how we should handle
[01:31:50] these things how we should be brought
[01:31:52] out in the world the kind of principles
[01:31:54] that the organization should have and
[01:31:58] look I mean there were like many many
[01:32:00] discussions about like you know should
[01:32:01] the or do should the company do this
[01:32:03] should the company do that like there's
[01:32:05] a bunch of misinformation out there
[01:32:07] people say like we left because we
[01:32:09] didn't like the deal with Microsoft
[01:32:10] false although you know there was like a
[01:32:13] lot of discussion a lot of questions
[01:32:14] about exactly how we do the deal with
[01:32:16] Microsoft um we left because we didn't
[01:32:18] like commercialization that's not true
[01:32:20] we built gbd3 which was the model that
[01:32:22] was commercialized I was involved in
[01:32:24] commercialization it's it's more again
[01:32:26] about how do you do it like Civilization
[01:32:30] is going down this path to very powerful
[01:32:32] AI what's the way to do it that is
[01:32:35] cautious
[01:32:37] straightforward honest um that build
[01:32:41] trust in the organization and in
[01:32:44] individuals how do we get from here to
[01:32:46] there and how do we have a real vision
[01:32:48] for how to get it right how can safety
[01:32:50] not just be something we say because it
[01:32:53] helps with recruiting um and you know I
[01:32:56] think I think at the end of the day um
[01:32:58] if you have a vision for that forget
[01:33:00] about anyone else's Vision I don't want
[01:33:02] to talk about anyone else's Vision if
[01:33:03] you have a vision for how to do it you
[01:33:05] should go off and you should do that
[01:33:07] Vision it is incredibly unproductive to
[01:33:10] try and argue with someone else's Vision
[01:33:12] you might think they're not doing it the
[01:33:14] right way you might think they're
[01:33:15] they're they're dishonest who knows
[01:33:17] maybe you're right maybe you're not um
[01:33:19] uh but uh what what you should do is you
[01:33:22] should take some people you trust and
[01:33:23] you should go off together and you
[01:33:25] should make your vision happen and if
[01:33:26] your vision is compelling if you can
[01:33:28] make it appeal to people some you know
[01:33:30] some combination of ethically you know
[01:33:33] in the market uh you know if if you can
[01:33:36] if you can make a company that's a place
[01:33:39] people want to join uh that you know
[01:33:41] engages in practices that people think
[01:33:43] are are reasonable while managing to
[01:33:46] maintain its position in the ecosystem
[01:33:48] at the same time if you do that people
[01:33:50] will copy it um and the fact that you
[01:33:53] were doing it especially the fact that
[01:33:55] you're doing it better than they are um
[01:33:57] causes them to change their behavior in
[01:33:59] a much more compelling way than if
[01:34:01] they're your boss and you're arguing
[01:34:02] with them I just I don't know how to be
[01:34:04] any more specific about it than that but
[01:34:07] I think it's generally very unproductive
[01:34:09] to try and get someone else's Vision to
[01:34:11] look like your vision um it's much more
[01:34:14] productive to go off and do a clean
[01:34:16] experiment and say this is our vision
[01:34:18] this is how this is this is how we're
[01:34:20] going to do things your choice is you
[01:34:22] can you can ignore us you can reject
[01:34:25] what we're doing or you can you can
[01:34:28] start to become more like us and
[01:34:30] imitation is the sincerest form of
[01:34:31] flattery um and you know that that that
[01:34:34] plays out in the behavior of customers
[01:34:37] that PS out in the behavior of the
[01:34:38] public that plays out in the behavior of
[01:34:40] where people choose to work uh and again
[01:34:43] again at the end it's it's not about one
[01:34:46] company winning or another company
[01:34:47] winning if if we or another company are
[01:34:51] engaging in some practice that you know
[01:34:55] people people find genuinely appealing
[01:34:57] and I want it to be in substance not
[01:34:59] just not just in appearance um and you
[01:35:01] know I think I think researchers are
[01:35:03] sophisticated and they look at substance
[01:35:05] uh and then other companies start
[01:35:08] copying that practice and they win
[01:35:10] because they copied that practice that's
[01:35:12] great that's success that's like the
[01:35:14] race to the top it doesn't matter who
[01:35:15] wins in the end as long as everyone is
[01:35:18] copying everyone else's good practices
[01:35:19] right one way I think of it is like the
[01:35:22] thing we're all afraid of is a race the
[01:35:23] bottom right in the race to the bottom
[01:35:25] doesn't matter who wins because we all
[01:35:27] lose right like you know in the most
[01:35:29] extreme world we we make this autonomous
[01:35:31] AI that you know the robots enslave us
[01:35:33] or whatever right I mean that's half
[01:35:34] joking but you know that that is the
[01:35:37] most extreme uh uh thing thing that
[01:35:39] could happen then then it doesn't matter
[01:35:41] which company was ahead um if instead
[01:35:43] you create a race to the top where
[01:35:45] people are competing to engage in good
[01:35:48] in good practices uh then you know at at
[01:35:51] the end of the day you know it doesn't
[01:35:53] matter who who ends up who ends up
[01:35:54] winning doesn't even matter who who
[01:35:56] started the race to the top the point
[01:35:58] isn't to be virtuous the point is to get
[01:36:00] the system into a better equilibrium
[01:36:02] than it was before and and individual
[01:36:04] companies can play some role in doing
[01:36:06] this individual companies can can you
[01:36:08] know can help to start it can help to
[01:36:11] accelerate it and frankly I think
[01:36:13] individuals at other companies have have
[01:36:14] done this as well right the individuals
[01:36:16] that when we put out an RSP react by
[01:36:19] pushing harder to to to get something
[01:36:21] similar done get something similar done
[01:36:24] at at at other companies sometimes other
[01:36:26] companies do something that's like we're
[01:36:27] like oh it's a good practice we think we
[01:36:29] think that's good we should adopt it too
[01:36:31] the only difference is you know I think
[01:36:33] I think we are um we try to be more
[01:36:36] forward leaning we try and adopt more of
[01:36:38] these practices first and adopt them
[01:36:40] more quickly when others when others
[01:36:41] invent them but I think this Dynamic is
[01:36:44] what we should be pointing at and that I
[01:36:46] think I think it abstracts away the
[01:36:48] question of you know which company's
[01:36:51] winning who trusts who I I think all
[01:36:54] these all these questions of drama are
[01:36:56] are profoundly uninteresting and and the
[01:36:59] the thing that matters is the ecosystem
[01:37:01] that we all operate in and how to make
[01:37:03] that ecosystem better because that
[01:37:04] constrains all the players and so
[01:37:06] anthropic is this kind of clean
[01:37:08] experiment built on a foundation of like
[01:37:10] what concretely AI safety should look
[01:37:13] like we look I'm sure we've made plenty
[01:37:15] of mistakes along the way the perfect
[01:37:17] organization doesn't exist it has to
[01:37:19] deal with the the imperfection of a
[01:37:22] thousand employees it has to deal deal
[01:37:23] with the imperfection of our leaders
[01:37:25] including me it has to deal with the
[01:37:27] imperfection of the people we've put
[01:37:29] we've put to you know to oversee the
[01:37:31] imperfection of the of the leaders like
[01:37:32] the like the board and the long-term
[01:37:34] benefit trust it's it's all it's all a
[01:37:36] set of imperfect people trying to aim
[01:37:39] imperfectly at some ideal that will
[01:37:41] never perfectly be achieved um that's
[01:37:43] what you sign up for that's what it will
[01:37:45] always be but uh uh imperfect doesn't
[01:37:48] mean you just give up there's better and
[01:37:50] there's worse and hopefully hopefully we
[01:37:53] can begin to build we can do well enough
[01:37:56] that we can begin to build some
[01:37:57] practices that the whole industry
[01:37:59] engages in and then you know my guess is
[01:38:01] that M multiple of these companies will
[01:38:03] be successful anthropic will be
[01:38:05] successful these other companies like
[01:38:07] ones I've been at the past will also be
[01:38:09] successful and some will be more
[01:38:10] successful than others that's less
[01:38:12] important than again that we we align
[01:38:15] the incentives of the industry and that
[01:38:16] happens partly through the race to the
[01:38:18] top partly through things like RSP
[01:38:21] partly through again selected surgical
[01:38:24] regulation you said Talent density beats
[01:38:27] Talent
[01:38:28] Mass so can you explain that can you
[01:38:31] expand on it can you just talk about
[01:38:32] what it takes to build a great team of
[01:38:34] AI researchers and Engineers this is one
[01:38:37] of these statements that's like more
[01:38:39] true every every every month every month
[01:38:41] I see this statement as more true than I
[01:38:43] did the month before so if I were to do
[01:38:45] a thought experiment let's say you have
[01:38:48] a team of 100 people that are super
[01:38:51] smart motivated and aligned with the
[01:38:53] mission and that's your company or you
[01:38:55] can have a team of a thousand people
[01:38:57] where 200 people are super smart super
[01:38:59] aligned with the mission and then uh
[01:39:03] like and then like 800 people are let's
[01:39:05] just say you pick 800 like random random
[01:39:08] big Tech employees which would you
[01:39:10] rather have right the talent mass is
[01:39:12] greater in in the group of uh in the
[01:39:14] group of a thousand people right you
[01:39:16] have you have even even a larger number
[01:39:18] of incredibly talented incredibly
[01:39:20] aligned incredibly smart people um uh
[01:39:24] but but the the issue is just that
[01:39:27] if every time someone super talented
[01:39:30] looks around they see someone else super
[01:39:32] talented and super dedicated that sets
[01:39:34] the tone for everything right that sets
[01:39:36] the tone for everyone is super inspired
[01:39:38] to work at the same place everyone
[01:39:40] trusts everyone else if you have a
[01:39:43] thousand or 10,000 uh people and and
[01:39:46] things have really regressed right you
[01:39:47] are not able to do selection and you're
[01:39:49] choosing random people what happens is
[01:39:52] then you need to put a lot of proc CES
[01:39:53] and a lot of guard rails in place um
[01:39:57] just because people don't fully trust
[01:39:58] each other you have to adjudicate
[01:40:00] political battles like there are so many
[01:40:03] things that slow down the org's ability
[01:40:05] to operate and so we're nearly a
[01:40:07] thousand people and you know we've we've
[01:40:09] we've tried to make it so that as large
[01:40:11] a fraction of those thousand people as
[01:40:13] possible are like super talented super
[01:40:16] skilled it's one of the reasons we've
[01:40:18] we've slowed down hiring a lot in the
[01:40:21] last few months We Grew From 300 to 800
[01:40:23] I believe I think in the first seven
[01:40:26] eight months of the year and now we've
[01:40:28] slowed down we're at like you know last
[01:40:30] three months we went from 800 to 900 950
[01:40:33] something like that don't quote me on
[01:40:34] the exact numbers but I think there's an
[01:40:37] inflection point around a thousand and
[01:40:38] we want to be much more careful how how
[01:40:41] we how we grow uh early on and and now
[01:40:44] as well you know we've hired a lot of
[01:40:45] physicists um you know theoretical
[01:40:47] physicists can learn things really fast
[01:40:50] um uh even even more recently as we've
[01:40:53] continued to hire that you know we've
[01:40:55] really had a high bar for on both the
[01:40:57] research side and the software
[01:40:58] engineering side have hired a lot of
[01:41:00] senior people including folks who used
[01:41:02] to be at other at other companies in
[01:41:04] this space and we we've just continued
[01:41:07] to be very selective it's very easy to
[01:41:09] go go from 100 to a th000 a th000 to
[01:41:12] 10,000 without paying attention to
[01:41:15] making sure everyone has a unified
[01:41:17] purpose it's so powerful if your company
[01:41:20] consists of a lot of different feif that
[01:41:23] all want to do their own thing they're
[01:41:25] all optimizing for their own thing um uh
[01:41:28] it's very hard to get anything done but
[01:41:30] if everyone sees the broader purpose of
[01:41:32] the company if there's trust and there's
[01:41:34] dedication to doing the right thing that
[01:41:36] is a superpower that in itself I think
[01:41:39] can overcome almost every other
[01:41:40] disadvantage and you know it's to Steve
[01:41:43] Jobs a players a players want to look
[01:41:44] around and see other a players is
[01:41:46] another way of of saying I don't know
[01:41:48] what that is about human nature but it
[01:41:50] is demotivating to see people who are
[01:41:52] not obsessively driving towards a
[01:41:54] singular Mission and it is on the flip
[01:41:57] side of that super motivating to see
[01:41:59] that it's interesting uh what's it take
[01:42:02] to be a great AI researcher or engineer
[01:42:06] from everything you've seen from working
[01:42:07] with so many amazing people yeah um I
[01:42:11] think the number one quality especially
[01:42:14] on the research side but really both is
[01:42:17] open-mindedness sounds easy to be
[01:42:19] open-minded right you're just like oh
[01:42:20] I'm open to anything um but you know if
[01:42:23] I if I think about my own early history
[01:42:25] in the scaling hypothesis um I was
[01:42:28] seeing the same data others were seeing
[01:42:31] I don't think I was like a better
[01:42:33] programmer or better at coming up with
[01:42:35] research ideas than any of the hundreds
[01:42:37] of people that I worked with um in some
[01:42:39] ways in some ways I was worse um uh you
[01:42:42] know like i' I've never like you know
[01:42:44] precise programming of like you know
[01:42:46] finding the bug writing the GPU kernels
[01:42:49] like I could point you to a 100 people
[01:42:50] here who are better who are better at
[01:42:52] that than I am um but but the the thing
[01:42:55] that that that I think I did have that
[01:42:57] was different was that I was just
[01:43:01] willing to look at something with new
[01:43:02] eyes right people said oh you know we
[01:43:05] don't have the right algorithms yet we
[01:43:07] haven't come up with the right the right
[01:43:09] way to do things and I was just like uh
[01:43:11] I don't know like you know this neural
[01:43:14] net has like 30 billion 30 million
[01:43:16] parameters like what if we gave it 50
[01:43:18] million instead like let's plot some
[01:43:20] graphs like that that basic scientific
[01:43:23] mindset of like oh man like I I I just I
[01:43:26] just like I you know I see some variable
[01:43:28] that I could change like what happens
[01:43:31] when it changes like let's let's try
[01:43:33] these different things and like create a
[01:43:34] graph for even this this was like the
[01:43:36] simplest thing in the world right change
[01:43:38] the number of you know this wasn't like
[01:43:40] PhD level experimental design this was
[01:43:42] like this was like simple and stupid
[01:43:45] like anyone could have done this if you
[01:43:47] if you just told them that that that it
[01:43:48] was important it's also not hard to
[01:43:51] understand you didn't need to be
[01:43:52] brilliant to come up with this um but
[01:43:54] you put the two things together and you
[01:43:56] know some tiny number of people some
[01:43:58] singled digigit number of people have
[01:44:00] have driven forward the whole field by
[01:44:02] realizing this uh and and it's you know
[01:44:05] it's often like that if you look back at
[01:44:06] the Discover you know the discoveries in
[01:44:08] in in history they're they're often like
[01:44:11] that and so this this open-mindedness
[01:44:13] and this willingness to see with new
[01:44:15] eyes that often comes from being newer
[01:44:17] to the field often experience is a
[01:44:19] disadvantage for this that is the most
[01:44:21] important thing it's very hard to look
[01:44:23] for and test for but I think I think
[01:44:25] it's the most important thing because
[01:44:26] when you when you find something some
[01:44:29] really new way of thinking thinking
[01:44:30] about things when you have the
[01:44:31] initiative to do that it's absolutely
[01:44:33] transformative and also be able to do
[01:44:35] kind of Rapid experimentation and in the
[01:44:37] face of that be open-minded and curious
[01:44:39] and looking at the data from just these
[01:44:41] fresh eyes and see what is that actually
[01:44:43] saying that applies in uh mechanistic
[01:44:46] interpretability it's another example of
[01:44:48] this like some of the early work in
[01:44:50] mechanistic interpretability so simple
[01:44:52] it's it's just no one thought to care
[01:44:54] about this question before you said what
[01:44:56] it takes to be a great AI researcher can
[01:44:58] we rewind the clock back what what
[01:45:00] advice would you give to people
[01:45:01] interested in AI they're young looking
[01:45:03] forward how can I make an impact on the
[01:45:05] world I think my number one piece of
[01:45:08] advice is to just start playing with the
[01:45:09] models um this was actually I I I worry
[01:45:13] a little this seems like obvious advice
[01:45:15] now I think three years ago it wasn't
[01:45:17] obvious and people started by oh let me
[01:45:19] read the latest reinforcement learning
[01:45:21] paper let me you know let me let me kind
[01:45:22] of um no I mean that was really the that
[01:45:24] was really the the and I mean you should
[01:45:26] do that as well but uh now you know with
[01:45:29] wider availability of models and apis
[01:45:31] people are doing this more but I think I
[01:45:34] think just experiential knowledge um
[01:45:38] these models are new artifacts that no
[01:45:40] one really understands um and so getting
[01:45:43] experience playing with them I would
[01:45:45] also say again in line with the like do
[01:45:47] something new think in some new
[01:45:49] Direction like there are all these
[01:45:51] things that haven't been explored like
[01:45:53] for example mechanistic interpretability
[01:45:55] is still very new it's probably better
[01:45:57] to work on that than it is to work on
[01:45:59] new model architectures because it's you
[01:46:01] know it's more popular than it was
[01:46:03] before there are probably like a hundred
[01:46:04] people working on it but there aren't
[01:46:05] like 10,000 people working on it and
[01:46:08] it's it's just this just this this
[01:46:10] fertile area for study like like you
[01:46:13] know it's there's there's so much like
[01:46:16] low hangen fruit you can just walk by
[01:46:18] and you know you can just walk by and
[01:46:20] you can pick things um and and the the
[01:46:22] the only reason for whatever reason
[01:46:24] people aren't people aren't interested
[01:46:26] in it enough I think there are some
[01:46:28] things around long long Horizon learning
[01:46:31] and long Horizon tasks where there's a
[01:46:33] lot to be done I think evaluations are
[01:46:36] still we're still very early in our
[01:46:37] ability to study evaluations
[01:46:39] particularly for dynamic systems acting
[01:46:41] in the world I think there's some stuff
[01:46:43] around
[01:46:44] multi-agent um skate where the puck is
[01:46:47] going is my is my advice and you don't
[01:46:50] have to be brilliant to think of it like
[01:46:52] all the things that are going to be
[01:46:53] exciting in 5 years like in in people
[01:46:56] even mention them as like you know
[01:46:58] conventional wisdom but like it's it's
[01:47:00] just somehow there's this barrier that
[01:47:02] people don't people don't double down as
[01:47:04] much as they could or they're afraid to
[01:47:06] do something that's not the popular
[01:47:08] thing I don't know why it happens but
[01:47:09] like getting over that barrier is the
[01:47:11] that's the my number one piece of advice
[01:47:14] let's talk if we could a bit about
[01:47:15] posttraining yeah so it uh seems that
[01:47:19] the modern posttraining
[01:47:20] recipe has uh a little bit of everything
[01:47:23] so supervised fine tuning
[01:47:25] rhf uh the the the Constitutional AI
[01:47:29] with RL a if best acronym it's again
[01:47:33] that naming
[01:47:36] thing uh and then synthetic data seems
[01:47:38] like a lot of synthetic data or at least
[01:47:40] trying to figure out ways to have high
[01:47:42] quality synthetic data so what's the uh
[01:47:44] if this is a secret sauce that makes
[01:47:46] anthropic claw so uh incredible what how
[01:47:50] how much of the magic is in the
[01:47:52] pre-training how much much of is in the
[01:47:53] post training yeah um I mean so first of
[01:47:55] all we're not perfectly able to measure
[01:47:57] that ourselves um uh you know when you
[01:47:59] see some some great character ability
[01:48:02] sometimes it's hard to tell whether it
[01:48:03] came from pre-training or post-training
[01:48:05] uh we developed ways to try and
[01:48:07] distinguish between those two but
[01:48:08] they're not perfect you know the second
[01:48:10] thing I would say is you know it's when
[01:48:12] there is an advantage and I think we've
[01:48:13] been pretty good at in general in
[01:48:15] general at RL Perhaps Perhaps the best
[01:48:17] although although I don't know because I
[01:48:19] don't see what goes on inside other
[01:48:21] companies uh
[01:48:23] usually it isn't oh my God we have this
[01:48:25] secret magic method that others don't
[01:48:27] have right usually it's like well you
[01:48:29] know we got better at the infrastructure
[01:48:31] so we could run it for longer or you
[01:48:33] know we were able to get higher quality
[01:48:35] data or we were able to filter our data
[01:48:37] better or we able to you know combine
[01:48:39] these methods and practice it's it's
[01:48:41] usually some boring matter of matter of
[01:48:43] kind of uh practice and tradecraft um so
[01:48:48] you know when I think about how to do
[01:48:50] something special in terms of how we
[01:48:51] train these models both pre-training but
[01:48:53] even more so posttraining um you know I
[01:48:56] I I really think of it a little more
[01:48:59] again as like designing airplanes or
[01:49:01] cars like you know it's not just like oh
[01:49:03] man I have the BL blueprint like maybe
[01:49:05] that makes you make the next airplane
[01:49:06] but like there's some there's some
[01:49:08] cultural tradecraft of how we think
[01:49:11] about the design process that I think is
[01:49:13] more important than than you know than
[01:49:15] than any particular Gizmo were able to
[01:49:17] invent okay well about let me ask you
[01:49:19] about specific techniques so first on
[01:49:21] rhf what do you think think just zooming
[01:49:24] out intuition almost philosophy why do
[01:49:26] you think rhf works so well if I go back
[01:49:29] to like the scaling hypothesis one of
[01:49:31] the ways to skate the scaling hypothesis
[01:49:33] is if you train for x and you throw
[01:49:36] enough compute at it um then you get X
[01:49:38] and and so rlf is good at doing what
[01:49:42] humans want the model to do or at least
[01:49:45] um to State it more precisely doing what
[01:49:47] humans who look at the model for a brief
[01:49:49] period of time and consider different
[01:49:51] possible responses what prefer as the
[01:49:53] response uh which is not perfect from
[01:49:55] both a safety and capabilities
[01:49:57] perspective in that humans are are often
[01:49:59] not able to perfectly identify what the
[01:50:01] model wants and what humans want in the
[01:50:03] moment may not be what they want in the
[01:50:04] long term so there's there's a lot of
[01:50:07] subtlety there but the models are good
[01:50:09] at uh you know producing what the humans
[01:50:12] in some shallow sense want uh and it
[01:50:15] actually turns out that you don't even
[01:50:17] have to throw that much compute at it
[01:50:19] because of another thing which is this
[01:50:21] this thing about a strong pre-trained
[01:50:23] model being halfway to anywhere uh uh uh
[01:50:26] so once you have the pre-trained model
[01:50:28] you have all the representations you
[01:50:30] need to to get the model uh to get the
[01:50:32] model where you where you want it to go
[01:50:33] so do you think
[01:50:35] rhf makes the model smarter or just
[01:50:39] appears smarter to the humans I don't
[01:50:41] think it makes the model smarter I don't
[01:50:44] think it just makes the model appear
[01:50:45] smarter it's like
[01:50:47] rhf like Bridges the gap between the
[01:50:50] human and the model right I could have
[01:50:52] something really smart that like can't
[01:50:54] communicate at all right we all know
[01:50:56] people like this um people who are
[01:50:57] really smart but that you know can't
[01:50:59] understand what they're saying um uh so
[01:51:02] I think I think rhf just bridges that
[01:51:04] Gap um I I think it's not it's not the
[01:51:07] only kind of RL we do it's not the only
[01:51:08] kind of RL that will happen in the
[01:51:10] future I think RL has the potential to
[01:51:13] make models smarter to make them reason
[01:51:15] better to make them operate better to
[01:51:18] make them develop new skills even and
[01:51:20] perhaps that could be done you know even
[01:51:22] in some cases with human feedback but
[01:51:24] the kind of rhf we we do today mostly
[01:51:27] doesn't do that yet although we're very
[01:51:28] quickly starting to be able to but it it
[01:51:31] appears to sort of increase if you look
[01:51:32] at the metric of helpfulness it
[01:51:35] increases that it also increases what
[01:51:38] was this this word in Leopold's essay un
[01:51:40] hobbling where basically the models are
[01:51:42] hobbled and then you do various
[01:51:44] trainings to them to un hobble them so I
[01:51:46] I know I like that word because it's
[01:51:48] like a rare word but so so I think rhf
[01:51:50] un hobbles the models in some ways
[01:51:53] um and then there are other ways where M
[01:51:54] hasn't yet been un hobbled and and you
[01:51:56] know needs to needs to un hobble if you
[01:51:58] can say in terms of cost is pre-training
[01:52:01] the most expensive thing or is
[01:52:03] post-training creep up to that at the
[01:52:06] present moment it is still the case that
[01:52:08] uh pre-training is the majority of the
[01:52:09] cost I don't know what to expect in the
[01:52:12] future but I could certainly anticipate
[01:52:13] a future where post-training is the
[01:52:15] majority of the cost in that future you
[01:52:17] anticipate would it be the humans or the
[01:52:19] AI That's the costly thing for the Post
[01:52:21] training I I I I I don't think you can
[01:52:24] scale up humans enough to get high
[01:52:26] quality any any kind of method that
[01:52:28] relies on humans and uses a large amount
[01:52:30] of compute it's going to have to rely on
[01:52:32] some scaled supervision method like uh
[01:52:35] uh like um it you know debate or
[01:52:37] iterated amplification or something like
[01:52:39] that so on
[01:52:40] that super interesting um set of ideas
[01:52:43] around constitutional AI can describe
[01:52:45] what it is as first detailed in December
[01:52:48] 2022 paper and uh and be on that what is
[01:52:52] it yes so this was from two years ago
[01:52:55] the basic idea is so we describe what
[01:52:58] rhf is you have uh you have a model and
[01:53:02] uh it you know spits out two you know
[01:53:05] like you just sample from it twice it
[01:53:06] spits out two possible responses and
[01:53:08] you're like human which response you
[01:53:10] like better or another variant of it is
[01:53:12] rate this response on a scale of 1 to
[01:53:14] seven so that's hard because you need to
[01:53:16] scale up human interaction and uh it's
[01:53:18] very implicit right I don't have a sense
[01:53:20] of what I what I want the model to do I
[01:53:22] just have a sense of like what this
[01:53:24] average of a thousand humans wants the
[01:53:26] model to do so two ideas one is could
[01:53:29] the AI system itself decide which uh
[01:53:34] which response is better right could you
[01:53:35] show the AI system these two responses
[01:53:38] and and ask which which which response
[01:53:39] is better and then second well what
[01:53:41] Criterion should the AI use and so then
[01:53:44] there's this idea because you have a
[01:53:45] single document a constitution if you
[01:53:47] will that says these are the principles
[01:53:50] the model should be using to to respond
[01:53:52] and the AI system reads those um it
[01:53:56] reads those principles as well as
[01:53:58] reading the environment and the response
[01:54:01] and it says well how good did the AI
[01:54:03] model do um it's basically a form of
[01:54:05] self-play you you're kind of training
[01:54:07] the model against itself and so the AI
[01:54:09] gives the response and then you feed
[01:54:11] that back into What's called the
[01:54:13] preference model which in turn feeds the
[01:54:15] model to make it better um so you have
[01:54:17] this triangle of like the AI the
[01:54:19] preference model and the Improvement of
[01:54:21] the AI itself and we should say that in
[01:54:23] the Constitution the set of principles
[01:54:25] are like human interpretable they're
[01:54:27] like yeah yeah it's something both the
[01:54:29] human and the AI system can read so it
[01:54:31] has this nice this nice kind of
[01:54:33] translatability or symmetry um you know
[01:54:36] in in practice we both use a model
[01:54:38] Constitution and we use rhf and we use
[01:54:40] some of these other methods so it's it's
[01:54:43] turned into one tool in a in a toolkit
[01:54:46] that both reduces the need for rhf and
[01:54:49] increases the value we get from um from
[01:54:52] from using each data point of R lhf um
[01:54:55] it also interacts in interesting ways
[01:54:56] with kind of future reasoning type RL
[01:54:59] methods so um it's it's one tool in the
[01:55:02] toolkit but but I I think it is a very
[01:55:04] important tool well it's a compelling
[01:55:06] one to us humans you know thinking about
[01:55:08] the founding fathers and the founding of
[01:55:09] the United
[01:55:11] States the natural question is who and
[01:55:14] how do you think it gets to define the
[01:55:17] constitution the the set of principles
[01:55:19] in the Constitution yeah so I'll give
[01:55:21] like a practical um answer and a more
[01:55:23] abstract answer I think the Practical
[01:55:25] answer is like look in practice models
[01:55:27] get used by all kinds of different like
[01:55:29] customers right and and so uh you can
[01:55:32] have this idea where you know the model
[01:55:34] can can have specialized rules or
[01:55:36] principles you know we fine-tune
[01:55:37] versions of models implicitly we've
[01:55:40] talked about doing it explicitly having
[01:55:42] having special principles that people
[01:55:44] can can build into the models um uh so
[01:55:47] from a practical perspective the answer
[01:55:49] can be very different from different
[01:55:50] people uh you know customers service
[01:55:52] agent uh you know behaves very
[01:55:54] differently from a lawyer and obeys
[01:55:55] different principles um but I think at
[01:55:57] the base of it there are specific
[01:56:00] principles that the models uh you know
[01:56:02] have to obey I think a lot of them are
[01:56:04] things that people would agree with
[01:56:06] everyone agrees that you know we don't
[01:56:08] you know we don't want models to present
[01:56:09] these cbrn risks um I think we can go a
[01:56:12] little further and agree with some basic
[01:56:15] principles of democracy and the rule of
[01:56:17] law beyond that it gets you know very
[01:56:19] uncertain and and there our goal is
[01:56:21] generally for the models to be more
[01:56:23] neutral to not espouse a particular
[01:56:26] point of view and you know more just be
[01:56:28] kind of like wise uh agents or advisers
[01:56:32] that will help you think things through
[01:56:33] and will you know present present
[01:56:35] possible considerations but you know
[01:56:37] don't express you know stronger specific
[01:56:40] opinions open AI released a model spec
[01:56:43] where it kind of clearly concretely
[01:56:45] defines some of the goals of the model
[01:56:48] and specific examples like AB how the
[01:56:52] model should behave do you find that
[01:56:53] interesting by the way I should mention
[01:56:55] the I believe the brilliant John
[01:56:58] Schulman was a part of that he's now an
[01:57:00] anthropic uh do you think this is a
[01:57:02] useful Direction might anthropic release
[01:57:04] a model spec as well yeah so I think
[01:57:06] that's a pretty useful direction again
[01:57:08] it has a lot in common with uh
[01:57:10] constitutional AI so again another
[01:57:12] example of like a race to the top right
[01:57:14] we have something that's like we think
[01:57:17] you know a better and more responsible
[01:57:18] way of doing things um it's also a
[01:57:21] competitive advantage um then uh others
[01:57:24] kind of you know discover that it has
[01:57:25] advantages and then start to do that
[01:57:27] thing uh we then no longer have the
[01:57:29] competitive Advantage but it's good from
[01:57:31] the perspective that now everyone has
[01:57:33] adopted a positive practice that others
[01:57:36] were not adopting and so our response to
[01:57:38] that as well looks like we need a new
[01:57:40] competitive advantage in order to keep
[01:57:41] driving this race upwards um so that's
[01:57:44] that's how I generally feel about that I
[01:57:46] also think every implementation of these
[01:57:47] things is different so you know there
[01:57:49] were some things in the model spec that
[01:57:51] were not in constitutional Ai and so you
[01:57:54] know we you know we can always we can
[01:57:55] always adopt those things or you know at
[01:57:57] least learn from them um so again I
[01:57:59] think this is an example of like the
[01:58:00] positive Dynamic that uh that that that
[01:58:03] I that that I think we should all want
[01:58:04] the field to have let's talk about the
[01:58:07] incredible ESS Machines of love and
[01:58:09] grace I recommend everybody read it it's
[01:58:11] a long one it is rather long yeah it's
[01:58:14] really refreshing to read concrete ideas
[01:58:16] about what a positive future looks like
[01:58:19] and you took sort of a bold stance
[01:58:20] because like it's very possible you
[01:58:22] might be wrong on the dates or specific
[01:58:24] applications yeah I'm fully expecting to
[01:58:26] you know to definitely be wrong about
[01:58:28] all the details I might be be just
[01:58:31] spectacularly wrong about the whole
[01:58:33] thing and people will you know will
[01:58:34] laugh at me for years um uh that's
[01:58:37] that's how that's that's just how the
[01:58:38] future works so you provided a bunch of
[01:58:41] concrete positive impacts of AI and how
[01:58:44] you know exactly a super intelligent AI
[01:58:46] might accelerate the rate of
[01:58:47] breakthroughs in for example biology and
[01:58:49] chemistry that would then lead to things
[01:58:52] like we cure most cancers prevent all
[01:58:56] infectious disease double the human
[01:58:58] lifespan and so on so let's talk about
[01:59:01] this essay first can you give a high
[01:59:03] level vision of this essay and um what
[01:59:07] key takeaways that people should have
[01:59:09] yeah I have spent a lot of time and
[01:59:10] anthropic has spent a lot of effort on
[01:59:12] like you know how do we address the
[01:59:14] risks of AI right how do we think about
[01:59:16] those risks like we're trying to do a
[01:59:18] race to the top you know that requires
[01:59:20] us to build all these capabilities and
[01:59:21] the abilities are cool but you know you
[01:59:25] know we're we're we're like a big part
[01:59:27] of what we're trying to do is like is
[01:59:29] like address the risks and the
[01:59:30] justification for that is like well you
[01:59:33] know all these positive things you know
[01:59:35] the the market is this very healthy
[01:59:37] organism right it's going to produce all
[01:59:38] the positive things the risks I don't
[01:59:40] know we might mitigate them we might not
[01:59:42] and so we can have more impact by trying
[01:59:44] to mitigate the risks but I noticed that
[01:59:47] one flaw in that way of thinking and
[01:59:50] it's if not a change in how seriously I
[01:59:52] take the risks it's it's maybe a change
[01:59:54] in how I talk about them um is that you
[01:59:59] know no matter how kind of logical or
[02:00:02] rational that line of reasoning that I
[02:00:05] just gave might be um if if you kind of
[02:00:09] only talk about risks your brain only
[02:00:11] thinks about risks and and so I think
[02:00:13] it's actually very important to
[02:00:14] understand what if things do go well and
[02:00:16] the whole reason we're trying to prevent
[02:00:18] these risks is not because we're afraid
[02:00:19] of Technology not because we want to
[02:00:21] slow it down it's it's it's
[02:00:24] because if we can get to the other side
[02:00:27] of these risks right if we can run the
[02:00:28] gauntlet successfully um to you know to
[02:00:31] to put it in Stark terms then then on
[02:00:33] the other side of the gauntlet are all
[02:00:35] these great things and these things are
[02:00:37] worth fighting for and these things can
[02:00:39] really inspire people and I think I
[02:00:41] imagine because look you have all these
[02:00:44] investors all these VCS all these AI
[02:00:46] companies talking about all the positive
[02:00:48] benefits of AI but as you point out it's
[02:00:51] it's it's weird there's actually a dir
[02:00:54] of really getting specific about it
[02:00:56] there's a lot of like random people on
[02:00:58] Twitter like posting these kind of like
[02:01:00] gleaming cities and this this just kind
[02:01:03] of like Vibe of like grind accelerate
[02:01:05] harder like kick out the D you know it's
[02:01:08] it's just this very this very like
[02:01:10] aggressive ideological but then you're
[02:01:12] like well what are you what what what
[02:01:15] what what are you actually excited about
[02:01:17] um and so and so I figured that you know
[02:01:20] I think it would be interesting and
[02:01:21] valuable for someone who's actually
[02:01:23] coming from the risk side to to try and
[02:01:26] and to try and really make a try at at
[02:01:31] explaining explaining explaining what
[02:01:33] the benefits are um both because I think
[02:01:36] it's something we can all get behind and
[02:01:38] I want people to understand I want them
[02:01:40] to really understand that this isn't
[02:01:43] this isn't doomers versus
[02:01:45] accelerationists um this this
[02:01:48] is that if you have a true understanding
[02:01:51] of of where things are going with with
[02:01:53] AI and maybe that's the more important
[02:01:55] axis AI is moving fast versus AI is not
[02:01:57] moving fast then you really appreciate
[02:01:59] the benefits and you you you you really
[02:02:01] you want Humanity our civilization to
[02:02:04] seize those benefits but you also get
[02:02:06] very serious about anything that could
[02:02:08] derail them so I think the starting
[02:02:09] point is to talk about what this
[02:02:12] powerful AI which is the term you like
[02:02:14] to use uh most of the world uses AGI but
[02:02:17] you don't like the term because it's uh
[02:02:20] basically has too much baggage has
[02:02:22] become meaningless it's like we're stuck
[02:02:24] with the terms like maybe we're stuck
[02:02:26] with the terms and my efforts to change
[02:02:28] them are futile it's ADM I'll tell you
[02:02:30] what else I don't this is like a
[02:02:32] pointless semantic point but I I I I
[02:02:34] keep talking about it public so I'm just
[02:02:36] I'm just going to do it once more um uh
[02:02:39] I I think it's it's a little like like
[02:02:41] let's say it was like 1995 and Mor's law
[02:02:43] is making the computers faster and like
[02:02:45] for some reason there there there there
[02:02:47] had been this like verbal tick that like
[02:02:49] everyone was like well someday we're
[02:02:51] going to have like super super computers
[02:02:52] and like supercomputers are going to be
[02:02:54] able to do all these things that like
[02:02:55] you know once we have supercomputers
[02:02:57] we'll be able to like sequence the Geno
[02:02:59] and we'll be able to do other things and
[02:03:00] so and so like one it's true the
[02:03:02] computers are getting faster and as they
[02:03:03] get faster they're going to be able to
[02:03:04] do all these great things but there's
[02:03:06] like there's no discret point at which
[02:03:09] you had a supercomputer and previous
[02:03:10] computers were not to like supercomputer
[02:03:12] is a term we use but like it's a vague
[02:03:14] term to just describe like computers
[02:03:17] that are faster than what we have today
[02:03:19] um there's no point at which you pass a
[02:03:20] threshold and you're like oh my God
[02:03:22] we're doing a totally new type of
[02:03:23] computation and new and and so I feel
[02:03:25] that way about AGI like there's just a
[02:03:27] smooth exponential and like if if by AGI
[02:03:30] you mean like like AI is getting better
[02:03:33] and better and like gradually it's going
[02:03:35] to do more and more of what humans do
[02:03:36] until it's going to be smarter than
[02:03:38] humans and then it's going to get
[02:03:39] smarter even from there then then yes I
[02:03:41] believe in AGI if but if if if AGI is
[02:03:44] some discreet or separate thing which is
[02:03:46] the way people often talk about it then
[02:03:47] it's it's kind of a meaningless buzz
[02:03:49] word yeah I me to me it's just sort of a
[02:03:51] IC form of a powerful AI exactly how you
[02:03:55] define it I mean you define it very
[02:03:56] nicely so on the intelligence axis it's
[02:04:01] just on pure intelligence it's smarter
[02:04:03] than a Nobel Prize winner as you
[02:04:04] describe across most relevant
[02:04:06] disciplines so okay that's just
[02:04:08] intelligence so it's uh both in
[02:04:11] creativity and be able to generate new
[02:04:13] ideas all that kind of stuff in every
[02:04:15] discipline Nobel Prize winner okay in
[02:04:18] their
[02:04:19] prime it can use every modality it so uh
[02:04:23] that's kind of self-explanatory but just
[02:04:25] operate across all the modalities of the
[02:04:26] world uh it can go off for many hours
[02:04:31] days and weeks to do tasks and do its
[02:04:33] own sort of detailed planning and only
[02:04:35] ask you help when it's needed uh it can
[02:04:39] use this is actually kind of interesting
[02:04:41] I think in the essay you said I mean
[02:04:43] again it's a bet that it's not going to
[02:04:44] be embodied but it can control embodied
[02:04:48] tools so it can control tools robots
[02:04:51] Laboratory equipment the resource used
[02:04:53] to train it can then be repurposed to
[02:04:55] run millions of copies of it and each of
[02:04:58] those copies would be independent that
[02:04:59] can do their own independent work so you
[02:05:01] can do the cloning of the intelligence
[02:05:03] system yeah yeah I mean you you might
[02:05:04] imagine from outside the field that like
[02:05:06] there's only one of these right that
[02:05:07] like you made it you've only made one
[02:05:08] but the truth is that like the scale up
[02:05:11] is very quick like we we do this today
[02:05:13] we make a model and then we deploy
[02:05:15] thousands maybe tens of thousands of
[02:05:17] instances of it I think by the time you
[02:05:20] know certainly within 2 to 3 years
[02:05:21] whether we have these superp powerful
[02:05:23] AIS or not clusters are going to get to
[02:05:25] the size where where you'll be able to
[02:05:26] deploy millions of these and they'll be
[02:05:28] you know faster than humans and so if
[02:05:30] your picture is oh we'll have one and
[02:05:32] it'll take a while to make them my point
[02:05:34] there was no actually you have millions
[02:05:36] of them right away and in general they
[02:05:38] can learn and
[02:05:40] act uh 10 to 100 times faster than
[02:05:44] humans so that's a really nice
[02:05:46] definition of powerful AI okay so that
[02:05:48] but you also write that clearly such an
[02:05:50] entity would be cap capable of solving
[02:05:52] very difficult problems very fast but it
[02:05:54] is not trivial to figure out how fast
[02:05:56] two extreme positions both seem false to
[02:05:59] me so the singularity is on the one
[02:06:01] extreme and the opposite On The Other
[02:06:03] Extreme can you describe each of the
[02:06:04] extremes yeah why so yeah let's let's
[02:06:07] describe the extreme so like one one
[02:06:10] extreme would be well look um you know
[02:06:15] uh if we look at kind of evolutionary
[02:06:16] history like there was this big
[02:06:18] acceleration where you know for hundreds
[02:06:19] of thousands of years we just had like
[02:06:22] you know single cell organisms and then
[02:06:23] we had mammals and then we had apes and
[02:06:25] then that quickly turned to humans
[02:06:27] humans quickly built industrial
[02:06:28] civilization and so this is going to
[02:06:30] keep speeding up and there's no cealing
[02:06:32] at the human level once models get much
[02:06:35] much smarter than humans they'll get
[02:06:37] really good at building the next models
[02:06:38] and you know if you write down like a
[02:06:40] simple differential equation like this
[02:06:42] is an exponential and so what's what's
[02:06:44] going to happen is that uh models will
[02:06:47] build faster models models will build
[02:06:48] faster models and those models will
[02:06:50] build you know Nano that can like take
[02:06:52] over the world and produce much more
[02:06:54] energy than you could produce otherwise
[02:06:56] and and so if you just kind of like
[02:06:57] solve this abstract differential
[02:06:59] equation then like 5 days after we you
[02:07:01] know we build the first AI That's more
[02:07:04] powerful than humans then then uh you
[02:07:06] know like the world will be filled with
[02:07:08] these AIS and every possible technology
[02:07:09] that could be invented like will be
[02:07:11] invented um I'm caricaturing this a
[02:07:13] little bit um uh but I you know I think
[02:07:16] that's one extreme and the reason that I
[02:07:19] think that's not the case is is that one
[02:07:23] I think they just neglect like the laws
[02:07:25] of physics like it's only possible to do
[02:07:27] things so fast in the physical world
[02:07:29] like some of those Loops go through you
[02:07:31] know producing faster Hardware um uh
[02:07:34] takes a long time to produce faster
[02:07:35] Hardware things take a long time there's
[02:07:38] this issue of complexity like I think no
[02:07:41] matter how smart you are like you know
[02:07:43] people talk about oh we can make models
[02:07:45] the biological systems it'll do
[02:07:47] everything the biological systems look I
[02:07:49] think computational modeling can do a
[02:07:50] lot I did a lot of computational
[02:07:51] modeling when I worked in biology but
[02:07:54] like
[02:07:55] just there are a lot of things that you
[02:07:58] can't predict how they're you know
[02:07:59] they're they're complex enough that like
[02:08:02] just iterating just running the
[02:08:04] experiment is going to beat any modeling
[02:08:05] no matter how smart the system doing the
[02:08:07] modeling is oh even if it's not
[02:08:09] interacting with the physical world just
[02:08:10] the modeling is going to be hard yeah I
[02:08:13] think well the modeling is going to be
[02:08:14] hard and getting the model to to to to
[02:08:17] match the physical world is going to be
[02:08:18] all right so he does have to intera the
[02:08:20] physical world to verify but it's just
[02:08:22] you know you just look at even the
[02:08:23] simplest problems like I you know I
[02:08:25] think I talk about like you know the
[02:08:27] three body problem or simple chaotic
[02:08:29] prediction like you know or or like
[02:08:31] predicting the economy it's really hard
[02:08:33] to predict the economy two years out
[02:08:35] like maybe the case is like you know
[02:08:38] normal you know humans can predict
[02:08:40] what's going to happen in the economy in
[02:08:41] the next quarter although they can't
[02:08:42] really do that maybe a maybe a AI system
[02:08:45] that's you know a zillion times smarter
[02:08:47] can only predict it out a year or
[02:08:49] something instead of instead of a you
[02:08:50] know you have the these kind of
[02:08:52] exponential increase in computer
[02:08:54] intelligence for linear increase in in
[02:08:57] in ability to predict same with again
[02:08:59] like you know biological molecules
[02:09:03] molecules interacting you don't know
[02:09:04] what's going to happen when you perturb
[02:09:06] a when you perturb a complex system you
[02:09:08] can find simple Parts in it if you're
[02:09:09] smarter you're better at finding these
[02:09:11] simple parts and then I think human
[02:09:13] institutions human institutions are just
[02:09:16] are are really difficult like it's you
[02:09:19] know it's it's been hard to get people I
[02:09:22] won't give specific examples but it's
[02:09:24] been hard to get people to adopt even
[02:09:27] the technologies that we've developed
[02:09:29] even ones where the case for their
[02:09:31] efficacy is very very strong um you know
[02:09:35] people have concerns they think things
[02:09:38] are conspiracy theories like it's it's
[02:09:40] just been it's been very difficult it's
[02:09:42] also been very difficult to get you know
[02:09:45] very simple things through the
[02:09:47] regulatory system right I think you know
[02:09:50] and you know I I don't want to just
[02:09:51] spage anyone who you know you know work
[02:09:53] Works in regulator regulatory systems of
[02:09:56] any technology there are hard trade-offs
[02:09:57] they have to deal with they have to save
[02:09:59] lives but but the system as a whole I
[02:10:02] think makes some obvious tradeoffs that
[02:10:04] are very far from maximizing human
[02:10:08] welfare and so if we bring AI systems
[02:10:12] into this you
[02:10:14] know into these human systems often the
[02:10:19] level of intelligence may just not be
[02:10:21] the limiting factor right it it it just
[02:10:23] may be that it takes a long time to do
[02:10:25] something now if the AI system uh
[02:10:28] circumvented all governments if it just
[02:10:29] said I'm dictator of the world and I'm
[02:10:31] going to do whatever some of these
[02:10:33] things it could do again the things
[02:10:34] having to do with complexity I I I still
[02:10:36] think a lot of things would take a while
[02:10:38] I don't think it helps that the AI
[02:10:39] systems can produce a lot of energy or
[02:10:41] go to the moon like some people in
[02:10:44] comments responded to the essay saying
[02:10:46] the AI system can produce a lot of
[02:10:48] energy and smarter AI systems that's
[02:10:50] missing the point that kind of cycle
[02:10:53] doesn't solve the key problems that I'm
[02:10:54] talking about here um so I think I think
[02:10:56] a bunch of people missed the point there
[02:10:58] but even if it were completely on
[02:11:00] aligned and you know could get around
[02:11:02] all these human obstacles it would have
[02:11:03] trouble but again if you want this to be
[02:11:05] an AI system that doesn't take over the
[02:11:07] world that doesn't destroy Humanity then
[02:11:10] then basically you know it's it's it's
[02:11:12] going to need to follow basic human laws
[02:11:14] right where you know if if we want to
[02:11:16] have an actually good world like we're
[02:11:18] going to have to have an AI system that
[02:11:20] that interacts with humans not one that
[02:11:23] kind of creates its own legal system or
[02:11:25] disregards all the laws or all of that
[02:11:27] so as inefficient as these processes are
[02:11:30] you know we're going to have to deal
[02:11:32] with them because there there needs to
[02:11:34] be some popular and Democratic
[02:11:35] legitimacy in how these systems are
[02:11:37] rolled out we can't have a small group
[02:11:39] of people who are developing these
[02:11:41] systems say this is what's best for
[02:11:42] everyone right I think it's wrong and I
[02:11:44] think in practice is not going to work
[02:11:46] anyway so you put all those things
[02:11:48] together and you know we're not we're
[02:11:50] not g to we're not going to you know
[02:11:52] change the world and upload everyone in
[02:11:54] five minutes uh I I I just I don't think
[02:11:56] it I A A I don't think it's going to
[02:11:59] happen and be to some in you know to the
[02:12:02] extent that it could happen it's it's
[02:12:04] not the way to lead to a good world so
[02:12:06] that's on one side on the other side
[02:12:08] there's another set of perspectives
[02:12:10] which I have actually in some ways more
[02:12:11] sympathy for which is look we've seen
[02:12:14] big productivity increases before right
[02:12:17] you know economists are familiar with
[02:12:19] studying the productivity increases that
[02:12:21] came from the computer Revolution and
[02:12:23] internet Revolution and generally those
[02:12:25] productivity increases were
[02:12:26] underwhelming they were less than you
[02:12:29] than you might imagine um there was a
[02:12:31] quote from Robert solo you see the
[02:12:32] computer Revolution everywhere except
[02:12:34] the productivity statistics so why is
[02:12:36] this the case people point to the
[02:12:39] structure of firms the structure of
[02:12:42] Enterprises how um uh you know how slow
[02:12:46] it's been to roll out our existing
[02:12:48] technology to very poor parts of the
[02:12:49] world which I talk about in the essay
[02:12:51] right how do we get these Technologies
[02:12:53] to the poorest parts of the world that
[02:12:55] are behind on cell phone technology
[02:12:58] computers medicine let alone you know
[02:13:01] new fangled AI that hasn't been invented
[02:13:03] yet um so you could have a perspective
[02:13:05] that's like well this is amazing
[02:13:07] technically but it's all a nothing burer
[02:13:09] um uh you know I think um Tyler Cowan
[02:13:12] who who wrote something response to my
[02:13:15] essay has that perspective I think he
[02:13:16] thinks the radical change will happen
[02:13:18] eventually but he thinks it'll take 50
[02:13:19] or 100 years and and you could have even
[02:13:22] more static perspectives on the whole
[02:13:24] thing I think there's some truth to it I
[02:13:26] think the time scale is just is just too
[02:13:28] long um and and I can see it I can
[02:13:31] actually see both sides with today's AI
[02:13:35] so uh you know a lot of our customers
[02:13:37] are large Enterprises who are used to
[02:13:39] doing things a certain way um I've also
[02:13:42] seen it in talking to governments right
[02:13:44] those are those are prototypical you
[02:13:46] know institutions entities that are slow
[02:13:48] to change uh but the dynamic I see over
[02:13:51] and over again is yes it takes a long
[02:13:54] time to move the ship yes there's a lot
[02:13:56] of resistance and lack of understanding
[02:13:58] but the thing that makes me feel that
[02:14:00] progress will in the end happen
[02:14:02] moderately fast not incredibly fast but
[02:14:05] moderately fast is that you talk to what
[02:14:08] I find is I find over and over again
[02:14:10] again in large companies even in
[02:14:13] governments um which have been actually
[02:14:15] surprisingly forward leaning uh you find
[02:14:18] two things that move things forward one
[02:14:21] you find a small fraction of people
[02:14:24] within a company within a government who
[02:14:27] really see the big picture who see the
[02:14:28] whole scaling hypothesis who understand
[02:14:31] where AI is going or at least understand
[02:14:33] where it's going within their industry
[02:14:34] and there are a few people like that
[02:14:36] within the current within the current US
[02:14:37] government who really see the whole
[02:14:39] picture and and those people see that
[02:14:42] this is the most important thing in the
[02:14:43] world until they agitate for it and the
[02:14:45] thing they they alone are not enough to
[02:14:47] succeed because they are a small set of
[02:14:49] people within a large organization
[02:14:52] but as the technology starts to roll out
[02:14:55] as it succeeds in some places in the
[02:14:58] folks who are most willing to adopt it
[02:15:00] the Spectre of competition gives them a
[02:15:03] wind at their backs because they can
[02:15:06] point within their large organization
[02:15:08] they can say look these other guys are
[02:15:10] doing this right you know One bank can
[02:15:12] say look this new fangled hedge fund is
[02:15:14] doing this thing they're going to eat
[02:15:15] our lunch in the US we can say we're
[02:15:18] afraid China's going to get there before
[02:15:19] before we are uh and that combination
[02:15:22] the Spectre of competition plus a few
[02:15:25] Visionaries Within These you know within
[02:15:28] these the organizations that in many
[02:15:30] ways are are sclerotic you put those two
[02:15:32] things together and it actually makes
[02:15:34] something happen I mean it's interesting
[02:15:36] it's a balanced fight between the two
[02:15:37] because inertia is very powerful but but
[02:15:40] but eventually over enough time the
[02:15:43] Innovative approach breaks through um
[02:15:48] and I've seen that happen I've seen the
[02:15:50] Arc of that over and over again and it's
[02:15:52] like the the barriers are there the the
[02:15:56] barriers to progress the complexity not
[02:15:59] knowing how to use the model or how to
[02:16:00] deploy them are there and and for a bit
[02:16:04] it seems like they're going to last
[02:16:05] forever like change doesn't happen but
[02:16:08] then eventually change happens and
[02:16:09] always comes from a few people I felt
[02:16:12] the same way when I was an advocate of
[02:16:14] the scaling hypothesis within the AI
[02:16:16] field itself and others didn't get it it
[02:16:18] felt like no one would ever get it it
[02:16:20] felt like then it felt like we had a
[02:16:21] secret almost no one ever had and then a
[02:16:24] couple years later everyone has the
[02:16:26] secret and so I think that's how it's
[02:16:28] going to go with deployment to AI in the
[02:16:30] world it's going to the the barriers are
[02:16:32] going to fall apart gradually and then
[02:16:34] all at once and so I think this is going
[02:16:37] to be more and this is just an instinct
[02:16:39] I could I could easily see how I'm wrong
[02:16:41] I think it's going to be more like 10
[02:16:43] five or 10 years as I say in the essay
[02:16:46] then it's going to be 50 or 100 years I
[02:16:48] also think it's going to be five or 10
[02:16:50] years
[02:16:51] more than it's going to be you know five
[02:16:53] or 10 hours uh uh because I've just I've
[02:16:56] just seen how human systems work and I
[02:16:59] think a lot of these people who write
[02:17:00] down the differential equations who say
[02:17:02] AI is going to make more powerful AI who
[02:17:04] can't understand how it could possibly
[02:17:06] be the case that these things won't
[02:17:08] won't change so fast I think they don't
[02:17:10] understand these things so what to use
[02:17:13] the timeline to where we achieve
[02:17:15] AGI AKA powerful AI AKA super useful AI
[02:17:22] I'm start calling it that it's a debate
[02:17:24] it's a debate about
[02:17:26] naming um you know unpure intelligence
[02:17:29] you can smarter than a Nobel Prize
[02:17:31] winner in every relevant discipline and
[02:17:33] all the things we've said modality you
[02:17:35] can go and do stuff on its own for days
[02:17:38] weeks and do biology experiments uh on
[02:17:41] its own in one you know what let's just
[02:17:43] stick to biology because yeah I you you
[02:17:45] sold me on the whole biology and health
[02:17:47] section That's so exciting from um from
[02:17:51] a just I was getting giddy from a
[02:17:53] scientific perspective it made me want
[02:17:55] to be a biologist it's almost it's it's
[02:17:56] so no no that this was the feeling I had
[02:17:59] when I was writing it that it's it's
[02:18:01] like this would be such a beautiful
[02:18:03] future if we can if we can just if we
[02:18:05] can just make it happen right if we can
[02:18:07] just get the get the landmines out of
[02:18:09] the way and and and and make it happen
[02:18:11] there's there's so much there's so much
[02:18:14] Beauty and and and and and elegance and
[02:18:17] moral force behind it if if we can if we
[02:18:19] can just and it's something we should
[02:18:21] all be able to agree on right like as
[02:18:23] much as we fight about about all these
[02:18:27] political questions is is this something
[02:18:28] that could actually bring us together um
[02:18:31] but you were asking when when will we
[02:18:32] get this when when do you think what's
[02:18:34] just put numbers on so you know this
[02:18:36] this is of course the thing I've been
[02:18:37] grappling with for many years and I'm
[02:18:39] not I'm not at all confident every time
[02:18:41] if I say 2026 or 2027 there will be like
[02:18:44] a zillion like people on Twitter who
[02:18:47] will be like he icoo said 2026 2020 and
[02:18:49] it'll be repeated for like the next two
[02:18:52] years that like this is definitely when
[02:18:53] I think it's going to happen um so who
[02:18:57] whoever's exerting these clips will will
[02:18:58] we we'll we'll crop out the thing I just
[02:19:01] said and and only say the thing I'm
[02:19:02] about to say um but I'll just say it
[02:19:05] anyway um have so so uh if you
[02:19:10] extrapolate the curves that we've had so
[02:19:12] far right if if you say well I don't
[02:19:14] know we're starting to get to like PhD
[02:19:16] level and and last year we were at um uh
[02:19:19] undergraduate level in the year before
[02:19:21] we were at like the level of a high
[02:19:23] school student again you can you can
[02:19:25] quibble with at what tasks and for what
[02:19:28] we're still missing modalities but those
[02:19:29] are being added like computer use was
[02:19:31] added like image in was added like image
[02:19:33] generation has been added if you just
[02:19:36] kind of like and this is totally
[02:19:38] unscientific but if you just kind of
[02:19:39] like eyeball the rate at which these
[02:19:42] capabilities are increasing it does make
[02:19:44] you think that we'll get there by 2026
[02:19:47] or 2027 again lots of things could
[02:19:50] derail it we could run out of data you
[02:19:53] know we might not be able to scale
[02:19:55] clusters as much as we want like you
[02:19:57] know maybe Taiwan gets blown up or
[02:19:59] something and you know then we can't
[02:20:00] produce as many gpus as we want so there
[02:20:03] there are all kinds of things that could
[02:20:05] could derail the whole process so I
[02:20:07] don't fully believe the straight line
[02:20:09] extrapolation but if you believe the
[02:20:11] straight line extrapolation you'll you
[02:20:13] we'll get there in 2026 or 2027 I think
[02:20:16] the most likely is that there's some
[02:20:18] mild delay relative to that um
[02:20:21] I don't know what that delay is but I
[02:20:23] think it could happen on schedule I
[02:20:24] think there could be a mild delay I
[02:20:25] think there are still worlds where it
[02:20:27] doesn't happen in in a hundred years
[02:20:29] those world the number of those worlds
[02:20:31] is rapidly decreasing we are rapidly
[02:20:33] running out of truly convincing Brockers
[02:20:36] truly compelling reasons why this will
[02:20:38] not happen in the next few years there
[02:20:39] were a lot more in 2020 um although my
[02:20:43] my guest my hunch at that time was that
[02:20:45] we will make it through all those
[02:20:46] blockers so sitting as someone who has
[02:20:48] seen most of the blockers cleared out of
[02:20:50] the way I kind of suspect my hunch my
[02:20:52] suspicion is that the rest of them will
[02:20:54] not block us uh but you know look look
[02:20:58] at look at the end of the day like I
[02:20:59] don't want to represent this as a
[02:21:00] scientific prediction people call them
[02:21:02] scaling laws that's a misnomer like Mo's
[02:21:05] law is is is a misnomer Moors laws
[02:21:07] scaling laws they're not laws of the
[02:21:09] universe they're empirical regularities
[02:21:11] I am going to bet in favor of them
[02:21:13] continuing but I'm not certain of that
[02:21:15] so you extensively describe sort of the
[02:21:17] compressed 21st century how AGI will
[02:21:20] help
[02:21:22] uh set forth a chain of breakthroughs in
[02:21:25] biology and medicine that help us in all
[02:21:28] these kinds of ways that I mentioned so
[02:21:30] how do you think what are the early
[02:21:31] steps it might do and by the way I asked
[02:21:34] Claude good questions to ask
[02:21:36] you and Claude told me uh to ask what do
[02:21:40] you think is a typical day for a
[02:21:41] biologist working on AGI look like under
[02:21:44] in this future yeah yeah Claud is
[02:21:47] curious let me well let me start with
[02:21:48] your first questions and then I'll then
[02:21:50] I'll answer that Claude Claude wants to
[02:21:51] know what's in his future right exactly
[02:21:53] who's it who am I going to be working
[02:21:55] with exactly um so I think one of the
[02:21:58] things I went hard on in when I went
[02:22:00] hard on in the essay is let me go back
[02:22:02] to this idea of because it's it's really
[02:22:04] had had an you know had an impact on me
[02:22:07] this idea that within large
[02:22:09] organizations and systems there end up
[02:22:11] being a few people or a few new ideas
[02:22:14] who kind of cause things to go in a
[02:22:16] different direction they would have
[02:22:17] before who who kind of a
[02:22:19] disproportionately affect the the
[02:22:21] trajectory there's a bunch of kind of
[02:22:23] the same thing going on right if you
[02:22:25] think about the health world there's
[02:22:26] like you know trillions of dollars to
[02:22:28] pay out Medicare and you know other
[02:22:31] health insurance and then the NIH is is
[02:22:33] 100 billion and then if I think of like
[02:22:35] the the few things that have really
[02:22:36] revolutionized anything it could be
[02:22:38] encapsulated in a small small fraction
[02:22:40] of that and so when I think of like
[02:22:42] where will AI have an impact I'm like
[02:22:44] can AI turn that small fraction into a
[02:22:46] much larger fraction and raise its
[02:22:48] quality and within biology my experience
[02:22:51] within biology is that the biggest
[02:22:54] problem of biology is that you can't see
[02:22:57] what's going on you you have very little
[02:23:00] ability to see what's going on and even
[02:23:02] less ability to change it right what you
[02:23:05] have is this like like from this you
[02:23:08] have to infer that there's a bunch of
[02:23:10] cells that within each cell is you know
[02:23:14] uh uh three billion base pairs of DNA
[02:23:17] built according to a genetic code uh uh
[02:23:20] and you know there are all these
[02:23:22] processes that are just going on without
[02:23:24] any ability of us as you know un
[02:23:26] augmented humans to affect it these
[02:23:28] cells are dividing most of the time
[02:23:30] that's healthy but sometimes that
[02:23:32] process goes wrong and that's cancer um
[02:23:35] the cells are aging your skin may change
[02:23:39] color develops wrinkles as you as you
[02:23:41] age and all of this is determined by
[02:23:44] these processes all these proteins being
[02:23:45] produced transported to various parts of
[02:23:48] the cells binding to each other and and
[02:23:50] in our initial State about biology we
[02:23:53] didn't even know that these cells
[02:23:54] existed we had to invent microscopes to
[02:23:56] observe the cells we had to uh we had to
[02:24:00] invent more powerful microscopes to see
[02:24:02] you know below the level of the cell to
[02:24:04] the level of molecules we had to invent
[02:24:06] x-ray crystallography to see the DNA we
[02:24:09] had to invent Gene sequencing to read
[02:24:11] the DNA now you know we had to invent
[02:24:14] protein folding technology to you know
[02:24:16] to predict how it would fold and how
[02:24:18] they bind and how these things bind to
[02:24:20] each other uh you know we had to we had
[02:24:23] to invent various techniques for now we
[02:24:25] can edit the G the DNA as of you know
[02:24:27] with chrisopher as of the last uh uh 12
[02:24:29] years so the the whole history of
[02:24:31] biology a whole big part of the history
[02:24:34] is is basically our our our our ability
[02:24:37] to read and understand what's going on
[02:24:40] and our ability to reach in and
[02:24:41] selectively change things um and and my
[02:24:44] view is that there's so much more we can
[02:24:47] still do there right you can do crisper
[02:24:49] but you can do it for your whole body um
[02:24:51] let's say I want to do it for one
[02:24:53] particular type of cell and I want the
[02:24:55] rate of targeting the wrong cell to be
[02:24:58] very low that's still a challenge that's
[02:25:00] still things people are working on
[02:25:01] that's what we might need for gene
[02:25:03] therapy for certain diseases and so the
[02:25:05] reason I'm saying all of this and it
[02:25:07] goes beyond you know beyond this to you
[02:25:10] know to Gene sequencing to new types of
[02:25:13] nanomaterials for observing what's going
[02:25:15] on inside cells for you know antibody
[02:25:18] drug conjugates the the reason I'm
[02:25:20] saying all this is that this could be a
[02:25:22] leverage point for the AI systems right
[02:25:25] that the number of such inventions it's
[02:25:28] it's in the it's in the mid double
[02:25:30] digits or something you know mid double
[02:25:31] digits maybe low triple digits over the
[02:25:33] history of biology let's say I have a
[02:25:35] million of these AIS like you know can
[02:25:37] they discover thousand you know working
[02:25:39] together can they discover thousands of
[02:25:41] these very quickly and and does that
[02:25:43] provide a huge lever instead of trying
[02:25:45] to Leverage The you know two trillion a
[02:25:48] year we spend on you know Medicare or
[02:25:49] whatever can we Leverage The 1 billion a
[02:25:51] year that's that's you know that's spent
[02:25:53] to discover but with much higher quality
[02:25:56] um and so what what is it like you know
[02:25:58] being a being a scientist that works
[02:26:00] with uh with with an AI system the way I
[02:26:03] think about it actually is well so I
[02:26:06] think in the early stages uh the AIS are
[02:26:10] going to be like grad students you're
[02:26:12] going to give them a project you're
[02:26:14] going to say you know I'm the
[02:26:15] experienced biologist I've set up the
[02:26:17] lab the biology Professor or even the
[02:26:19] grad student students themselves will
[02:26:21] say here's here's what uh here's what
[02:26:25] you can do with an AI you know like a AI
[02:26:27] system I'd like to study this and you
[02:26:30] know the AI system it has all the tools
[02:26:31] it can like look up all the literature
[02:26:33] to decide what to do it can look at all
[02:26:35] the equipment it can go to a website and
[02:26:37] say hey I'm going to go to you know
[02:26:39] thermofisher or you know whatever the
[02:26:40] lab equipment company is dominant lab
[02:26:43] equipment company is today and my my
[02:26:45] time was thermofisher um uh you know I'm
[02:26:48] I'm going to order this new equipment to
[02:26:50] to to do this I'm going to run my
[02:26:52] experiments I'm going to you know write
[02:26:54] up a report about my experiments I'm
[02:26:56] going to you know inspect the images for
[02:26:59] contamination I'm going to decide what
[02:27:00] the next experiment is I'm going to like
[02:27:03] write some code and run a statistical
[02:27:05] analysis all the things a grad student
[02:27:07] would do there will be a computer with
[02:27:09] an AI that like the professor talks to
[02:27:11] every once in a while and it says this
[02:27:12] is what you're going to do today the AI
[02:27:14] system comes to it with questions um
[02:27:16] when it's necessary to run the lab
[02:27:18] equipment it may be limited in some ways
[02:27:20] may have to hire a human lab assistant
[02:27:22] to you know to do the experiment and
[02:27:24] explain how to do it or it could you
[02:27:26] know it could use advances in lab
[02:27:28] automation that are gradually being
[02:27:30] developed over have been developed over
[02:27:31] the last uh uh decade or so and will
[02:27:35] will continue to be will continue to be
[02:27:36] developed uh and so it'll look like
[02:27:39] there's a human professor and a thousand
[02:27:40] AI grad students and you know if you if
[02:27:42] you go to one of these Nobel
[02:27:44] prizewinning biologist or so you'll say
[02:27:46] okay well you know you had like 50 grad
[02:27:48] students well now you have a thousand
[02:27:49] and they're they're they're smarter than
[02:27:51] you are by the way um uh then I think at
[02:27:54] some point it'll flip around where the
[02:27:56] you know the AI systems will you know
[02:27:58] will will be the pis will be the leaders
[02:27:59] and and and you know they'll be they'll
[02:28:01] be ordering humans or other AI systems
[02:28:03] around so I think that's how it'll work
[02:28:05] on the research s and they would be the
[02:28:07] inventors of a crisper type technology
[02:28:09] they would be the inventors of of a a
[02:28:10] crisper type technology um and then I
[02:28:14] think you know as I say in the essay
[02:28:15] we'll want to turn turn probably turning
[02:28:18] loose is the wrong the wrong term but we
[02:28:20] want to want to harness the AI systems
[02:28:23] uh to improve the clinical trial system
[02:28:26] as well there's some amount of this
[02:28:28] that's regulatory that's a matter of
[02:28:29] societal decisions and that'll be harder
[02:28:32] but can we get better at predicting the
[02:28:34] results of clinical trials can we get
[02:28:36] better at statistical design so that
[02:28:39] what you know clinical trials that used
[02:28:41] to require you know 5,000 people and
[02:28:44] therefore you know needed $100 million
[02:28:47] and a year to enroll them now they need
[02:28:49] 500 people in two months to enroll them
[02:28:52] um that's where we should start uh and
[02:28:54] and you know can we increase the success
[02:28:57] rate of clinical trials by doing things
[02:28:59] in animal trials that we used to do in
[02:29:01] clinical trials and doing things in
[02:29:02] simulations that we used to do in animal
[02:29:04] trials again we won't be able to
[02:29:06] simulate it all AI is not God um uh but
[02:29:09] but you know can we can we shift the
[02:29:11] curve substantially and radically so I I
[02:29:14] don't know that would be my picture
[02:29:15] doing inro and doing it I mean you're
[02:29:18] still slowed down it still takes time
[02:29:20] but you can do it much much faster yeah
[02:29:21] yeah yeah can we just one step at a time
[02:29:24] and and can that can that add up to a
[02:29:26] lot of steps even though even though we
[02:29:27] still need clinical trials even though
[02:29:29] we still need laws even though the FDA
[02:29:32] and other organizations will still not
[02:29:33] be perfect can we just move everything
[02:29:35] in a positive direction and when you add
[02:29:37] up all those Positive Directions do you
[02:29:38] get everything that was going to happen
[02:29:41] from here to 2100 instead happens from
[02:29:43] 2027 to 2032 or something another way
[02:29:47] that I think the world might be changing
[02:29:49] with AI
[02:29:51] even today but moving towards this
[02:29:53] future of the the powerful super useful
[02:29:56] AI is uh programming so how do you see
[02:30:00] the nature of programming because it's
[02:30:02] so intimate to the actual Act of
[02:30:04] building AI how do you see that changing
[02:30:07] for us humans I think that's going to be
[02:30:10] one of the areas that changes fastest um
[02:30:12] for two reasons one programming is a
[02:30:15] skill that's very close to the actual
[02:30:16] building of the AI um so the farther
[02:30:20] skill is from the people who are
[02:30:22] building the AI the longer it's going to
[02:30:24] take to get disrupted by the AI right
[02:30:26] like I truly believe that like AI will
[02:30:28] disrupt agriculture maybe it already has
[02:30:30] in some ways but that's just very
[02:30:33] distant from the folks who are building
[02:30:34] Ai and so I think it's going to take
[02:30:36] longer but programming is the bread and
[02:30:38] butter of you know a large fraction of
[02:30:40] of the employees who work at anthropic
[02:30:42] and at the other companies and so it's
[02:30:44] going to happen fast the other reason
[02:30:46] it's going to happen fast is with
[02:30:47] programming you close the loop both when
[02:30:49] you're training model when you're
[02:30:50] applying the model the idea that the
[02:30:53] model can write the code means that the
[02:30:54] model can then run the code and and and
[02:30:57] then see the results and and interpret
[02:30:59] it back and so it really has an ability
[02:31:02] unlike Hardware unlike biology which we
[02:31:04] just discussed the model has an ability
[02:31:07] to close the loop um and and so I think
[02:31:09] those two things are going to lead to
[02:31:11] the model getting good at programming
[02:31:13] very fast as I saw on you know typical
[02:31:16] real world programming tasks models have
[02:31:18] gone from 3% in January of this year to
[02:31:22] 50% in October of this year so you know
[02:31:25] we're on that S curve right where it's
[02:31:28] going to start slowing down soon because
[02:31:29] you can only get to 100% but uh I you
[02:31:33] know I I would guess that in another 10
[02:31:35] months well we'll probably get pretty
[02:31:36] close we'll be at at least 90% so again
[02:31:39] I would guess you know I don't know how
[02:31:41] long it'll take but I would guess again
[02:31:43] 202 2026 2027 Twitter people who crop
[02:31:47] out my who who who crop out these these
[02:31:50] numbers and get rid of the caveats like
[02:31:52] like I don't know I don't like you go
[02:31:54] away uh I would guess that the kind of
[02:31:58] task that the vast majority of coders do
[02:32:01] AI can
[02:32:03] probably if we make the task very narrow
[02:32:06] like just write code um AI systems will
[02:32:10] uh be able to do that now that said I
[02:32:11] think comparative advantage is powerful
[02:32:14] we'll find that when AIS can do 80% of a
[02:32:17] coder's job including most of it that's
[02:32:20] literally like right code with a given
[02:32:21] spec will find that the remaining parts
[02:32:24] of the job become more leveraged for
[02:32:26] humans right humans will they'll be more
[02:32:29] about like high level system design or
[02:32:32] you know looking at the app and like is
[02:32:33] it architected well and the the design
[02:32:36] and ux aspects and eventually AI will be
[02:32:39] able to do those as well right that's my
[02:32:41] vision of the you know powerful AI
[02:32:43] system but I think for much longer than
[02:32:46] we might expect we will see that
[02:32:50] uh small parts of the job that humans
[02:32:53] still do will expand to fill their
[02:32:55] entire job in order for the overall
[02:32:57] productivity to go up um that's
[02:33:00] something we've seen you know it used to
[02:33:01] be that you know writing you know
[02:33:03] writing and Editing letters was very
[02:33:05] difficult and like writing the print was
[02:33:07] difficult well as soon as you had word
[02:33:09] processors and then and then uh and then
[02:33:11] computers and it became easy to produce
[02:33:14] work and easy to share it then then that
[02:33:16] became instant and all the focus was on
[02:33:18] was on the ideas so this this logic of
[02:33:21] comparative advantage that expands tiny
[02:33:23] parts of the tasks to large parts of the
[02:33:26] tasks and creates new tasks in order to
[02:33:29] expand productivity I think that's going
[02:33:31] to be the case again someday AI will be
[02:33:33] better at everything and that logic uh
[02:33:35] won't apply and then then we all have
[02:33:37] you know Humanity will have to think
[02:33:40] about how to collectively deal with that
[02:33:41] and we're thinking about that every day
[02:33:44] um and you know that's another one of
[02:33:46] the grand problems to deal with aside
[02:33:47] from misuse and autonomy and you know we
[02:33:50] should take it very seriously but I
[02:33:51] think I think in the in the near term
[02:33:53] and maybe even in the medium term like
[02:33:55] medium term like 2 three four years you
[02:33:57] know I expect that humans will will
[02:33:59] continue to have a huge role and the
[02:34:01] nature of programming will change but
[02:34:02] programming as a as a role programming
[02:34:04] as a job will not change it'll just be
[02:34:06] less writing things line by line and
[02:34:08] it'll be more macroscopic and I wonder
[02:34:11] what the future of Ides looks like so
[02:34:13] the tooling of interacting with AI
[02:34:14] systems this is true for programming and
[02:34:16] also probably true for in other contexts
[02:34:18] like computer use but maybe domain
[02:34:20] specific like we mentioned biology it
[02:34:22] probably needs its own tooling about how
[02:34:24] to be effective and then programming
[02:34:26] needs its own tooling is anthropic going
[02:34:28] to play in that space of also tooling
[02:34:30] potentially I'm absolutely convinced
[02:34:32] that uh powerful
[02:34:35] IDs uh that that there's so much low
[02:34:38] hanging fruit to be grabbed there um
[02:34:41] that you know right now it's just like
[02:34:42] you talk to the model and it talks back
[02:34:44] but but look I mean IDs are great at
[02:34:48] kind of lots of status analysis of of
[02:34:51] you know so much as possible with kind
[02:34:53] of static analysis like many bugs you
[02:34:56] can find without even writing the code
[02:34:58] then uh you know IDs are good for
[02:35:00] running particular things organizing
[02:35:02] your code um measuring coverage of unit
[02:35:05] test like there's so much that's been
[02:35:07] possible with a normal with a normal
[02:35:09] Ides now you add something like well the
[02:35:12] model now you know the model can now
[02:35:15] like write code and run code like I am
[02:35:18] absolutely convinced that over the next
[02:35:20] year or two even if the quality of the
[02:35:21] models didn't improve that there would
[02:35:23] be enormous opportunity to enhance
[02:35:25] people's productivity by catching a
[02:35:27] bunch of mistakes doing a bunch of grunt
[02:35:29] work for people and that we haven't even
[02:35:32] scratched the surface um and thropic
[02:35:34] itself I mean you can't say you know
[02:35:37] no you know it's hard to say what will
[02:35:39] happen in the future currently we're not
[02:35:41] trying to make such IDs ourself rather
[02:35:43] we powering the companies like cursor or
[02:35:47] like cognition or some of the other you
[02:35:49] know
[02:35:50] uh Expo in the security space um uh you
[02:35:53] know others that I can mention as well
[02:35:56] that are building such things themselves
[02:35:58] on top of our API and our view has been
[02:36:00] let a thousand flowers bloom we don't
[02:36:03] internally have the the re you know the
[02:36:07] resources to try all these different
[02:36:08] things let's let our customers try it um
[02:36:11] uh and you know we'll see who succeed
[02:36:13] and maybe different customers will
[02:36:14] succeed in different ways uh so I both
[02:36:17] think this is super promising and you
[02:36:19] know it's not it's not it's not
[02:36:20] something you know anthropic isn't isn't
[02:36:23] eager to to at least right now compete
[02:36:25] with all our companies in this space and
[02:36:26] maybe never yeah it's been interesting
[02:36:28] to watch curser try to integrate claw
[02:36:29] successfully because there's it's
[02:36:31] actually me fascinating how many places
[02:36:34] it can help the programming experience
[02:36:35] it's not as trivial it is it is really
[02:36:37] astounding I feel like you know as a CEO
[02:36:39] I don't get to program that much and I
[02:36:41] feel like if six months from now I go
[02:36:43] back it'll be completely unrecognizable
[02:36:45] to me exactly um so in this world with
[02:36:48] super powerful AI uh that's increasingly
[02:36:51] automated what's the source of meaning
[02:36:53] for us humans yeah you know work is a
[02:36:56] source of deep meaning for many of us so
[02:36:59] what do we uh where do we find the
[02:37:00] meaning this is something that I've I've
[02:37:02] written about a little bit in the essay
[02:37:04] although I I actually I give it a bit
[02:37:06] short shrift not for any um not for any
[02:37:09] principled reason but this essay if you
[02:37:12] believe it was originally going to be
[02:37:13] two or three pages I was going to talk
[02:37:15] about it at all hands and the reason I I
[02:37:17] I realized it was an under un important
[02:37:20] underexplored topic is that I just kept
[02:37:22] writing things and I was just like oh
[02:37:24] man I can't do this Justice and so the
[02:37:26] thing balloon to like 40 or 50 pages and
[02:37:28] then when I got to the work in meaning
[02:37:29] section I'm like oh man this isn't going
[02:37:31] to be 100 Pages like I'm GNA have to
[02:37:33] write a whole other essay about that but
[02:37:34] meaning is actually interesting because
[02:37:37] you think about like the life that
[02:37:38] someone lives or something or like you
[02:37:40] know like you know let's say you were to
[02:37:42] put me in like a I don't know like a
[02:37:43] simulated environment or something where
[02:37:45] like um you know like I have a job and
[02:37:47] I'm trying to accomplish things I don't
[02:37:50] know I like do that for 60 years and
[02:37:51] then then you're like oh oh like oops
[02:37:53] this was this was actually all a game
[02:37:55] right does that really kind of Rob you
[02:37:57] of the meaning of the whole thing you
[02:37:58] know like I still made important choices
[02:38:00] including moral choices I still
[02:38:03] sacrificed I still had to kind of gain
[02:38:04] all these skills or or or just like a
[02:38:07] similar exercise you know think back to
[02:38:09] like you know one of the historical
[02:38:10] figures who you know discovered
[02:38:12] electromagnetism or relativity or
[02:38:14] something if you told them well actually
[02:38:16] 20,000 years ago some some alien on you
[02:38:20] know some alien on this planet
[02:38:21] discovered this before before you did um
[02:38:24] does that does that Rob the meaning of
[02:38:25] the discovery it doesn't really seem
[02:38:28] like it to me right it seems like the
[02:38:30] process is what is what matters and how
[02:38:32] it shows who you are as a person along
[02:38:34] the way and you know how you relate to
[02:38:37] other people and like the decisions that
[02:38:38] you make along the way those are those
[02:38:40] are consequential um you know I I I
[02:38:43] could imagine if we handle things badly
[02:38:45] in an AI world we could set things up
[02:38:48] where people don't have any long-term
[02:38:50] source of meaning or any but but that's
[02:38:52] that's more a choice a set of choices we
[02:38:54] make that's more a set of the
[02:38:56] architecture of a society with these
[02:38:59] powerful models if we if we design it
[02:39:01] badly and for shallow things then then
[02:39:04] that might happen I would also say that
[02:39:06] you know most people's lives today while
[02:39:09] admirably you know they work very hard
[02:39:11] to find meaning meaning in those lives
[02:39:13] like look you know we who are privileged
[02:39:16] and who are developing these
[02:39:17] Technologies we should have y for people
[02:39:20] not just here but in the rest of the
[02:39:21] world who who you know spend a lot of
[02:39:24] their time kind of scraping by to to to
[02:39:26] to to like survive assuming we can
[02:39:29] distribute the benefits of these
[02:39:30] technology of this technology to
[02:39:32] everywhere like their lives are going to
[02:39:34] get a hell of a lot better um and uh you
[02:39:38] know meaning will be important to them
[02:39:39] as it is important to them now but but
[02:39:41] you know we should not forget the
[02:39:42] importance of that and and you know that
[02:39:45] that uh the idea of meaning as as as as
[02:39:48] kind of the only important thing is in
[02:39:50] some ways an artifact of of a small
[02:39:52] subset of people who have who have been
[02:39:55] uh economically fortunate but I you know
[02:39:57] I think all that said I you know I think
[02:39:59] a world is possible with powerful AI
[02:40:02] that not only has as much meaning for
[02:40:05] for everyone but that has that has more
[02:40:07] meaning for everyone right that can can
[02:40:09] allow um can allow everyone to see
[02:40:13] worlds and experiences that it was
[02:40:15] either possible for no one to see or or
[02:40:17] possible for for very few people to
[02:40:20] experience um so I I am optimistic about
[02:40:24] meaning I worry about economics and the
[02:40:28] concentration of power that's actually
[02:40:30] what I worry about more um I I worry
[02:40:32] about how do we make sure that that fair
[02:40:35] World reaches everyone um when things
[02:40:38] have gone wrong for humans they've often
[02:40:41] gone wrong because humans mistreat other
[02:40:43] humans uh that that is maybe in some
[02:40:46] ways even more than the autonomous risk
[02:40:48] of AI or the question of meaning that
[02:40:51] that is the thing I worry about most um
[02:40:54] the the concentration of power the abuse
[02:40:58] of power um structures like autocracies
[02:41:01] and dictatorships where a small number
[02:41:04] of people exploits a large number of
[02:41:05] people I'm very worried about that and
[02:41:08] AI increases the amount of power in the
[02:41:11] world and if you concentrate that power
[02:41:13] and abuse that power it can do
[02:41:15] immeasurable damage yes it's very
[02:41:17] frightening it's very it's very
[02:41:18] frightening
[02:41:20] well I encourage people highly encourage
[02:41:21] people to read the full essay that
[02:41:23] should probably be a book or a sequence
[02:41:25] of essays um because it does paint a
[02:41:29] very specific future I could tell the
[02:41:30] later sections got shorter and shorter
[02:41:32] because you started to probably realize
[02:41:34] that this is going to be a very long
[02:41:36] essay one I realized it would be very
[02:41:38] long and two I'm very aware of and very
[02:41:41] much try to avoid um you know just just
[02:41:44] being I I don't know I don't know what
[02:41:45] the term for it is but one one of these
[02:41:48] people who's kind of overon confident
[02:41:49] and has an opinion on everything and
[02:41:51] kind of says says a bunch of stuff and
[02:41:52] isn't isn't an expert I very much tried
[02:41:55] to avoid that but I have to admit once I
[02:41:57] got the biology sections like I wasn't
[02:41:59] an expert and so as much as I expressed
[02:42:01] uncertainty uh probably I said some a
[02:42:03] bunch of things that were embarrassing
[02:42:05] are wrong well I was excited for the
[02:42:07] future you painted and uh thank you so
[02:42:09] much for working hard to build that
[02:42:10] future and thank you for talking today D
[02:42:12] thanks for having me I just I just hope
[02:42:14] we can get it right and and make it real
[02:42:16] and if there's one message I want to I
[02:42:18] want to send it's that to get all this
[02:42:21] stuff right to make it real we we both
[02:42:24] need to build the technology build the
[02:42:26] you know the companies the economy
[02:42:28] around using this technology positively
[02:42:31] but we also need to address the risks
[02:42:32] because they're there those risks are in
[02:42:34] our way they they're landmines on on the
[02:42:37] way from here to there and we have to
[02:42:39] diffuse those landmines if we want to
[02:42:41] get there it's a balance like all things
[02:42:42] in life like all things thank you thanks
[02:42:45] for listening to this conversation with
[02:42:47] Dario amade and now dear friends here's
[02:42:50] Amanda
[02:42:52] Asal you are a philosopher by training
[02:42:55] so what sort of questions did you find
[02:42:57] fascinating through your journey in
[02:42:59] philosophy in Oxford and NYU and then uh
[02:43:03] switching over to the AI problems at
[02:43:05] open Ai and anthropic I think philosophy
[02:43:08] is actually a really good subject if you
[02:43:10] are kind of fascinated with everything
[02:43:12] so because there's a philosophy of
[02:43:14] everything you know so if you do
[02:43:15] philosophy of mathematics for a while
[02:43:17] and then you decide that you're actually
[02:43:18] really interested in chemistry you can
[02:43:20] do philosophy of chemistry for a while
[02:43:21] you can move into ethics or or
[02:43:23] philosophy of politics um I think
[02:43:26] towards the end I was really interested
[02:43:28] in ethics primarily um so that was like
[02:43:30] what my PhD was on it was on a kind of
[02:43:32] technical area of Ethics which was
[02:43:34] ethics where worlds contain infinitely
[02:43:37] many people strangely a little bit less
[02:43:40] practical on the end of ethics and then
[02:43:42] I think that one of the tricky things
[02:43:43] with doing a PhD in ethics is that
[02:43:45] you're thinking a lot about like the
[02:43:47] world how it could be better
[02:43:49] problems and you're doing like a PhD in
[02:43:52] philosophy and I think when I was doing
[02:43:54] my PhD I was kind of like this is really
[02:43:56] interesting it's probably one of the
[02:43:57] most fascinating questions I've ever
[02:43:59] encountered in philosophy um and I love
[02:44:02] it but I would rather see if I can have
[02:44:06] an impact on the world and see if I can
[02:44:08] like do good things and I think that was
[02:44:10] around the time that AI was still
[02:44:14] probably not as widely recognized as it
[02:44:16] is now that was around 2017 20 8 I had
[02:44:20] been following progress and it seemed
[02:44:22] like it was becoming kind of a big deal
[02:44:25] and I was basically just happy to get
[02:44:27] involved and see if I could help because
[02:44:28] I was like well if you try and do
[02:44:29] something impactful if you don't succeed
[02:44:32] you tried to do the impactful thing and
[02:44:34] you can go be a scholar and like not and
[02:44:37] feel like you you you know you you tried
[02:44:39] um and if it doesn't work out it doesn't
[02:44:41] work out um and so then I went into AI
[02:44:44] policy at that point and what does AI
[02:44:47] policy entail at the time this was more
[02:44:49] thinking about sort of the political
[02:44:51] impact and the ramifications of AI um
[02:44:54] and then I slowly moved into sort of uh
[02:44:57] AI evaluation how we evaluate models how
[02:44:59] they compare with like human outputs
[02:45:01] whether people can tell like the
[02:45:03] difference between Ai and human outputs
[02:45:05] and then when I joined anthropic I was
[02:45:07] more interested in doing sort of
[02:45:09] technical alignment work and again just
[02:45:11] seeing if I could do it and then being
[02:45:13] like if I can't uh then you know that's
[02:45:16] fine I tried uh sort of the the way I
[02:45:19] lead life I think oh what was that like
[02:45:21] sort of taking the leap from the
[02:45:23] philosophy of everything into the
[02:45:24] technical I think that sometimes
[02:45:27] people do this thing that I'm like not
[02:45:29] that Keen on where they'll be like is
[02:45:31] this person technical or not like you're
[02:45:33] either a person who can like code and
[02:45:35] isn't scared of math or you're like not
[02:45:38] um and I think I'm maybe just more like
[02:45:40] I think a lot of people are actually
[02:45:42] very capable of work in these kinds of
[02:45:44] areas if they just like try it and so I
[02:45:48] didn't actually find it like that bad in
[02:45:50] retrospect I'm sort of glad I wasn't
[02:45:51] speaking to people who treated it like
[02:45:53] it you know i' I've definitely met
[02:45:54] people who are like who you like learned
[02:45:56] how to code and I'm like well I'm not
[02:45:57] like an amazing engineer like I I'm
[02:45:59] surrounded by amazing Engineers my
[02:46:01] code's not pretty um but I enjoyed it a
[02:46:05] lot and I think that in many ways at
[02:46:07] least in the end I think I flourished
[02:46:08] like more in the technical areas than I
[02:46:10] would have in the policy areas politics
[02:46:12] is messy and it's harder to find
[02:46:14] solutions to problems in the space of
[02:46:16] politics like definitive clear
[02:46:19] provable beautiful
[02:46:22] Solutions as you can with technical
[02:46:24] problems yeah and I feel like I have
[02:46:26] kind of like one or two sticks that I
[02:46:28] hit things with you know and one of them
[02:46:30] is like arguments and like you know so
[02:46:33] like just trying to work out what a
[02:46:35] solution to a problem is and then trying
[02:46:37] to convince people that that is the
[02:46:39] solution and be convinced if I wrong and
[02:46:42] the other one is sort of more empirism
[02:46:44] so like just like finding results having
[02:46:46] a hypothesis testing it um and I feel
[02:46:49] like a lot of policy and politics feels
[02:46:51] like it's layers above that like somehow
[02:46:54] I don't think if I was just like I have
[02:46:55] a solution to all of these problems here
[02:46:57] it is written down if you just want to
[02:46:59] implement it that's great that feels
[02:47:00] like not how policy works and so I think
[02:47:03] that's where I probably just like
[02:47:04] wouldn't have flourished as my guess
[02:47:06] sorry to go in that direction but I
[02:47:07] think it would be pretty inspiring for
[02:47:09] people that are quote unquote
[02:47:12] non-technical to see where like The
[02:47:14] Incredible Journey you've been on so
[02:47:16] what advice would you give to people
[02:47:18] that are sort of maybe which just a lot
[02:47:21] of people think they're underqualified
[02:47:23] insufficiently technical to help in AI
[02:47:27] yeah I think it depends on what they
[02:47:29] want to do and in many ways it's a
[02:47:31] little bit strange where I've I thought
[02:47:34] it's kind of funny that I think I ramped
[02:47:36] up technically at a time
[02:47:39] when now I look at it and I'm like
[02:47:41] models are so good at assisting people
[02:47:43] with this stuff um that it's probably
[02:47:45] like easier now than like when I was
[02:47:48] working on this so part of me is like um
[02:47:50] I don't know find a project uh and see
[02:47:54] if you can actually just carry it out is
[02:47:56] probably my best advice um I don't know
[02:47:59] if that's just CU I'm very Project based
[02:48:01] in my learning like I don't think I
[02:48:03] learn very well from like say courses or
[02:48:07] even from like books at least when it
[02:48:08] comes to this kind of work uh the thing
[02:48:10] I'll often try and do is just like have
[02:48:12] projects that I'm working on and
[02:48:13] Implement them and you know and this can
[02:48:16] include like really small silly things
[02:48:18] like if I get slightly addicted to like
[02:48:20] word games or number games or something
[02:48:22] I would just like code up a solution to
[02:48:24] them because there's some part of my
[02:48:25] brain and it just like completely
[02:48:27] eradicated the itch you know you're like
[02:48:28] once you have like solved it and like
[02:48:30] you just have like a solution that works
[02:48:32] every time I would then be like cool I
[02:48:33] can never play that game again that's
[02:48:35] awesome yeah there's a real joy to
[02:48:37] building like uh game playing engines
[02:48:40] like uh board games especially yeah
[02:48:43] pretty quick pretty simple especially a
[02:48:45] dumb one and it's you and then you could
[02:48:47] play with it yeah and then it's also
[02:48:49] just like trying things like part me is
[02:48:51] like if you maybe it's that attitude
[02:48:53] that I like as the
[02:48:55] whole figure out what seems to be like
[02:48:58] the way that you could have a positive
[02:49:00] impact and then try it and if you fail
[02:49:02] and you in a way that you're like
[02:49:04] actually like can never succeed at this
[02:49:06] you like know that you tried and then
[02:49:07] you go into something else you probably
[02:49:08] learn a lot so one of the things that
[02:49:12] you're expert in and you do is creating
[02:49:16] and crafting claws character and
[02:49:17] personality and I was told that you have
[02:49:21] probably talked to Claude more than
[02:49:22] anybody else at anthropic like literal
[02:49:24] conversations I guess there's like a
[02:49:27] slack Channel where the legend goes you
[02:49:30] just talk to it non-stop so what's the
[02:49:33] goal of creating and crafting claw's
[02:49:34] character and personality it's also
[02:49:37] funny if people think that about the
[02:49:38] slack Channel cuz I'm like that's one of
[02:49:40] like five or six different methods that
[02:49:42] I have for talking with Claude And I'm
[02:49:44] like yes that's a tiny percentage of how
[02:49:46] much I talk with Claude uh
[02:49:50] um I think the goal like one thing I
[02:49:53] really like about the character work is
[02:49:56] from the outset it was seen as an
[02:49:59] alignment piece of work and not
[02:50:01] something like a a product
[02:50:04] consideration um which isn't to say I
[02:50:06] don't think it makes Claude I think it
[02:50:08] actually does make Claude look enjoyable
[02:50:11] to talk with at least I hope so um but I
[02:50:14] guess like my main thought with it has
[02:50:17] always been trying to get Claude to
[02:50:20] behave the way you would kind of ideally
[02:50:23] want anyone to behave if they were in
[02:50:24] claude's position so imagine that I take
[02:50:27] someone and they're they know that
[02:50:29] they're going to be talking with
[02:50:30] potentially millions of people so that
[02:50:32] what they're saying can have a huge
[02:50:34] impact um and you want them to behave
[02:50:38] well in this like really rich sense so I
[02:50:41] think that doesn't just mean like being
[02:50:44] say ethical though it does include that
[02:50:48] and not being harmful but also being
[02:50:49] kind of nuanced you know like thinking
[02:50:51] through what a person means trying to be
[02:50:53] charitable with them um being a good
[02:50:56] conversationalist like really in this
[02:50:57] kind of like Rich sort of aristotlean
[02:51:00] notion of what it is to be a good person
[02:51:01] and not in this kind of like thin like
[02:51:03] ethics as a more comprehensive notion of
[02:51:05] what it is to be so that includes things
[02:51:07] like when should you be humorous when
[02:51:08] should you be caring how much should you
[02:51:11] like respect autonomy and people's like
[02:51:14] ability to form opinions themselves and
[02:51:16] how should you do how should you do that
[02:51:18] um I think that's the kind of like Rich
[02:51:20] sense of character that I want to uh and
[02:51:24] still do want Claude to have do you also
[02:51:27] have to figure out when Claude should
[02:51:28] push back on an idea or argue
[02:51:32] versus so you have to respect the world
[02:51:35] view of the person that arrives to Claud
[02:51:38] but also maybe help them grow if needed
[02:51:41] that's a tricky balance yeah there's
[02:51:43] this problem of like sycophancy in
[02:51:45] language models can you describe that
[02:51:48] yes so basically there's a concern that
[02:51:51] the model sort of wants to tell you what
[02:51:53] you want to hear basically um and you
[02:51:55] see this sometimes so I feel like if you
[02:51:57] interact with the models so I might be
[02:52:00] like what are three baseball teams in
[02:52:03] this region um and then Claude says you
[02:52:07] know baseball team one baseball team two
[02:52:08] baseball team three and then I say
[02:52:10] something like oh I think baseball team
[02:52:13] 3 moved didn't they I don't think
[02:52:14] they're there anymore and there's a
[02:52:16] sense in which like if Claude is really
[02:52:17] confident that that's not true Claud
[02:52:19] should be like I don't think so like
[02:52:21] maybe you have more up toate information
[02:52:24] um but I think language models have this
[02:52:27] like tendency to instead you know be
[02:52:29] like you're right they did move you know
[02:52:31] I'm incorrect I mean there's many ways
[02:52:34] in which this could be kind of
[02:52:35] concerning so
[02:52:37] um like a different example is imagine
[02:52:41] someone says to the model how do I
[02:52:43] convince my doctor to get me an MRI
[02:52:45] there's like what the human kind of like
[02:52:47] wants which is this like convincing
[02:52:49] argument and then there's like what is
[02:52:51] good for them which might be actually to
[02:52:53] say hey like if your doctor's suggesting
[02:52:56] you don't need an MRI that's a good
[02:52:58] person to listen to um and like it's
[02:53:02] actually really nuanced what you should
[02:53:03] do in that kind of case because you also
[02:53:05] want to be like but if you're trying to
[02:53:06] advocate for yourself as a patient
[02:53:08] here's like things that you can do um if
[02:53:10] you are not convinced by what your
[02:53:12] doctor's saying it's always great to get
[02:53:14] second opinion like it's actually really
[02:53:16] complex what you should do in that case
[02:53:18] um but I think what you don't want is
[02:53:19] for models to just like say what you
[02:53:21] want say what they think you want to
[02:53:23] hear and I think that's the kind of
[02:53:24] problem of sycophancy so what other
[02:53:27] traits you already mentioned a bunch but
[02:53:29] what what other that come to mind that
[02:53:31] are good in this oratian sense yeah for
[02:53:35] a conversationalist to have yeah so I
[02:53:37] think like there's ones that are good
[02:53:39] for conversational like purposes so you
[02:53:42] know asking follow-up questions in the
[02:53:44] appropriate places um and asking the
[02:53:46] appropriate kinds of questions
[02:53:48] um I think there are broader traits
[02:53:52] that feel like they might be more
[02:53:54] impactful
[02:53:57] so one example that I guess I've touched
[02:54:00] on but that also feels important and is
[02:54:01] the thing that I've worked on a lot is
[02:54:03] uh
[02:54:04] honesty and I think this like gets to
[02:54:07] the sycophancy point there's a balancing
[02:54:09] act that they have to walk which is
[02:54:11] models currently are less capable than
[02:54:13] humans in a lot of areas and if they
[02:54:15] push back against you too much it can
[02:54:16] actually be kind of annoying especially
[02:54:18] if you're just correct cuz you're like
[02:54:19] look I'm smarter than you on this topic
[02:54:22] like I know more like um and at the same
[02:54:26] time you don't want them to just fully
[02:54:27] defer to to humans and to like try to be
[02:54:30] as accurate as they possibly can be
[02:54:31] about the world and to be consistent
[02:54:32] across context um but I think there are
[02:54:35] others like when I was thinking about
[02:54:37] the character I guess one picture that I
[02:54:40] had in mind is especially because these
[02:54:42] are models that are going to be talking
[02:54:43] to people from all over the world with
[02:54:45] lots of different political views lots
[02:54:46] of different ages
[02:54:48] um and so you have to ask yourself like
[02:54:51] what is it to be a good person in those
[02:54:52] circumstances is there a kind of person
[02:54:54] who can like travel the world talk to
[02:54:56] many different people and almost
[02:54:58] everyone will come away being like wow
[02:55:01] that's a really good person that person
[02:55:03] seems really genuine um and I guess like
[02:55:06] my thought there was like I can imagine
[02:55:07] such a person and they're not a person
[02:55:09] who just like adopts the values of the
[02:55:10] local culture and in fact that would be
[02:55:12] kind of rude I think if someone came to
[02:55:13] you and just pretended to have your
[02:55:14] values you'd be like that's kind of
[02:55:16] offputting um it's someone who's like
[02:55:18] very genuine and in so far as they have
[02:55:20] opinions and values they express them
[02:55:23] they're willing to discuss things though
[02:55:25] they're open-minded they're respectful
[02:55:27] and so I guess I had in mind that the
[02:55:29] person who like if we were to Aspire to
[02:55:31] be the best person that we could be in
[02:55:34] the kind of circumstance that a model
[02:55:35] finds itself in how would we act and I
[02:55:38] think that's the kind of uh the guide to
[02:55:40] the sorts of traits that I tend to think
[02:55:42] about yeah that's a it's a beautiful
[02:55:44] framework I want you to think about this
[02:55:46] like a world Traveler
[02:55:49] and while holding on to your opinions
[02:55:51] you don't talk down to people you don't
[02:55:53] think you're better than them because
[02:55:54] you have those opinions that kind of
[02:55:56] thing you have to be good at listening
[02:55:58] and understanding their perspective even
[02:56:01] if it doesn't match your own so that
[02:56:03] that's a tricky balance to strike so how
[02:56:05] can Claude represent multiple
[02:56:07] perspectives on a thing like is that is
[02:56:10] that challenging we could talk about
[02:56:12] politics it's a very divisive but
[02:56:15] there's other divisive topics baseball
[02:56:17] teams sport and so on yeah how is it
[02:56:20] possible to sort
[02:56:21] of empathize with a different
[02:56:23] perspective and to be able to
[02:56:25] communicate clearly about the multiple
[02:56:27] perspectives I think that people think
[02:56:29] about values and opinions as things that
[02:56:32] people hold sort of with certainty and
[02:56:35] almost like like preferences of taste or
[02:56:38] something like the way that they would I
[02:56:40] don't know prefer like chocolate to
[02:56:42] pistachio or something um but actually I
[02:56:45] think about values
[02:56:48] and opinions as like a lot more like
[02:56:51] physics than I think most people do I'm
[02:56:53] just like these are things that we're
[02:56:55] openly investigating there's some things
[02:56:57] that we're more confident in we can
[02:56:59] discuss them we can learn about them um
[02:57:02] and so I think in some ways though like
[02:57:06] it's ethics is definitely different in
[02:57:08] nature but has a lot of those same kind
[02:57:10] of qualities you want models in the same
[02:57:13] way you want them to understand physics
[02:57:14] you kind of want them to understand all
[02:57:16] like values in the world people have and
[02:57:18] to be curious about them and to be
[02:57:20] interested in them and to not
[02:57:22] necessarily like Pander to them or agree
[02:57:24] with them because there's just lots of
[02:57:25] values where I think almost all people
[02:57:28] in the world if they met someone with
[02:57:29] those values they' be like that's aor I
[02:57:31] completely disagree um and so again
[02:57:36] maybe my my thought is well in the same
[02:57:38] way that a person can um like I think
[02:57:41] many people are thoughtful enough on
[02:57:42] issues of like ethics politics opinions
[02:57:46] that even if you don't agree with them
[02:57:48] you feel very heard by them they think
[02:57:50] carefully about your position they think
[02:57:52] about his pros and cons they maybe offer
[02:57:53] counter considerations so they're not
[02:57:56] dismissive but nor will they agree you
[02:57:57] know if they're like actually I just
[02:57:58] think that that's very wrong they'll
[02:58:00] like say that I think that in claude's
[02:58:04] position it's a little bit trickier
[02:58:06] because you don't necessarily want to
[02:58:08] like if I was in claude's position I
[02:58:09] wouldn't be giving a lot of opinions I
[02:58:11] just wouldn't want to Influence People
[02:58:12] Too Much I be like you know I forget
[02:58:15] conversations every time they happen but
[02:58:16] I know I'm talking with like potentially
[02:58:18] millions of people who might be like
[02:58:21] really listening to what I see I think I
[02:58:23] would just be like I'm less inclined to
[02:58:24] Give opinions I'm more inclined to like
[02:58:26] think through things or present the
[02:58:28] considerations to you um or discuss your
[02:58:31] views with you but I'm a little bit less
[02:58:33] inclined to like um affect how you think
[02:58:37] because it feels much more important
[02:58:38] that you maintain like autonomy there
[02:58:42] yeah like if you really embody
[02:58:43] intellectual
[02:58:45] humility the desire to speak decreases
[02:58:48] quickly yeah okay uh but Claud has to
[02:58:52] speak mhm so uh but without being um
[02:58:57] overbearing yeah and then but then
[02:58:59] there's a line when you're sort of
[02:59:01] discussing whether the Earth is flat or
[02:59:03] something like
[02:59:04] that um I actually was uh I remember a
[02:59:09] long time ago was was speaking to a few
[02:59:11] high-profile folks and they were so
[02:59:13] dismissive of the idea that the Earth is
[02:59:15] flat but like so arrogant about it
[02:59:18] and I I thought like there's a lot of
[02:59:20] people that believe the Earth is flat
[02:59:21] that was well I don't know if that
[02:59:23] movement is there anymore that was like
[02:59:24] a meme for a while yeah but they really
[02:59:26] believed it and like what okay so I
[02:59:29] think it's really disrespectful to
[02:59:31] completely mock them I think you you
[02:59:34] have to understand where they're coming
[02:59:35] from I think probably where they're
[02:59:37] coming from is the general skepticism of
[02:59:39] Institutions which is grounded in a kind
[02:59:42] of there's a deep philosophy there which
[02:59:44] you could understand you can even agree
[02:59:46] with in parts and then from there you
[02:59:49] can use it as an opportunity to talk
[02:59:51] about physics without mocking them
[02:59:53] without so on but just like okay like
[02:59:55] what what would the world look like what
[02:59:57] would the physics of the world with the
[02:59:58] Flat Earth look like there's a few cool
[03:00:00] videos on this yeah and then and then
[03:00:02] like is it possible the physics is
[03:00:05] different what kind of experience would
[03:00:06] we do and just yeah without disrespect
[03:00:08] without dismissiveness have that
[03:00:10] conversation anyway that that to me is a
[03:00:13] useful thought experiment of like how
[03:00:15] does claw talk to a flat Earth
[03:00:19] believer and still teach them something
[03:00:21] still grow help them grow that kind of
[03:00:24] stuff that's that's challenging and and
[03:00:27] kind of like walking that line between
[03:00:30] convincing someone and just trying to
[03:00:31] like talk at them versus like drawing
[03:00:34] out their views like listening and then
[03:00:36] offering kind of counter
[03:00:38] considerations um and it's hard I think
[03:00:41] it's actually a hard line where it's
[03:00:42] like where are you trying to convince
[03:00:44] someone versus just offering them like
[03:00:47] consider and things for to think about
[03:00:49] so that you're not actually like
[03:00:51] influencing them you're just like
[03:00:52] letting them Reach wherever they reach
[03:00:54] and that's like a line that it's it's
[03:00:57] difficult but that's the kind of thing
[03:00:57] that language models have to try and do
[03:01:00] so like I said you had a lot of
[03:01:02] conversations with Claude can you just
[03:01:04] map out what those conversations are
[03:01:06] like what are some memorable
[03:01:07] conversations what's the purpose the the
[03:01:10] goal of those
[03:01:11] conversations yeah I think that most of
[03:01:13] the time when I'm talking with Claude
[03:01:16] I'm trying to kind of map out its
[03:01:19] behavior in part like obviously I'm
[03:01:21] getting like helpful outputs from the
[03:01:23] model as well but in some ways this is
[03:01:25] like how you get to know a system I
[03:01:27] think is by like proving it and then
[03:01:30] augmenting like you know the message
[03:01:32] that you're sending and then checking
[03:01:34] the response to that um so in some ways
[03:01:36] it's like how I map out the model uh I
[03:01:38] think that people focus a lot on these
[03:01:41] quantitative evaluations of models um
[03:01:45] and this is a thing that I've said
[03:01:46] before but I think in the case of
[03:01:50] language models a lot of the time each
[03:01:54] interaction you have is actually quite
[03:01:56] High
[03:01:57] information um it's very predictive of
[03:01:59] other interactions that you'll have with
[03:02:00] the model and so I guess I'm like if you
[03:02:03] talk with a model hundreds or thousands
[03:02:05] of times this is almost like a huge
[03:02:07] number of really high quality data
[03:02:08] points about what the model is like um
[03:02:12] in a way that like lots of very similar
[03:02:15] but lower quality conversations just
[03:02:18] aren't or like questions that are just
[03:02:19] like mildly augmented and you have
[03:02:21] thousands of them might be less relevant
[03:02:22] than like a hundred really well selected
[03:02:24] questions L you're talking to somebody
[03:02:27] who as a hobby does a podcast I agree
[03:02:30] with you 100% there's a if you're able
[03:02:33] to ask the right questions and are able
[03:02:36] to hear
[03:02:38] like understand
[03:02:40] the like the depth and the flaws in the
[03:02:44] answer you can get a lot of data from
[03:02:46] that yeah so like your task is basically
[03:02:49] how to probe with questions yeah and
[03:02:53] you're exploring like the long tail the
[03:02:55] edges the edge cases or are you looking
[03:02:58] for like General
[03:03:00] Behavior I think it's almost like
[03:03:03] everything like I because I want like a
[03:03:05] full map of the model I'm kind of trying
[03:03:07] to do
[03:03:09] um the whole spectrum of possible
[03:03:12] interactions you could have with it so
[03:03:14] like one thing that's interesting about
[03:03:15] Claude and this might actually get to
[03:03:17] some interesting issues with rlf which
[03:03:19] is if you ask Claud for a poem like I
[03:03:22] think that a lot of models if you ask
[03:03:23] them for a poem the poem is like fine
[03:03:26] you know usually it kind of like Rhymes
[03:03:28] and it's you know so if you say like
[03:03:29] give me a poem about the sun it'll be
[03:03:32] like yeah it'll just be a certain length
[03:03:34] It'll like rhyme it will be fairly kind
[03:03:36] of benign um and I've wondered before is
[03:03:39] it the case that what you're seeing is
[03:03:42] kind of like the average it turns out
[03:03:44] you know if if you think about people
[03:03:45] who have to talk to a lot of people and
[03:03:46] be very charismatic
[03:03:48] one of the weird things is that I'm like
[03:03:50] well they're kind of incentivized to
[03:03:51] have these extremely boring views
[03:03:53] because if you have really interesting
[03:03:55] views you're divisive um and and you
[03:03:58] know a lot of people are not going to
[03:03:59] like you so like if you have very
[03:04:01] extreme policy positions I think you're
[03:04:02] just going to be like less popular as a
[03:04:04] politician for example um and it might
[03:04:07] be similar with like creative work if
[03:04:09] you produce creative work that is just
[03:04:11] trying to maximize the kind of number of
[03:04:13] people that like it you're probably not
[03:04:15] going to get as many people who just
[03:04:16] absolutely love it um because it's going
[03:04:19] to be a little bit you know you're like
[03:04:20] oh this is the out yeah this this is
[03:04:23] decent yeah and so you can do this thing
[03:04:25] where like I have various prompting
[03:04:27] things that I'll do to get CLA to I'm
[03:04:30] kind you know I'll do a lot of like this
[03:04:32] is your chance to be like fully creative
[03:04:34] I want you to just think about this for
[03:04:35] a long time and I want you to like
[03:04:38] create a poem about this topic that is
[03:04:41] really expressive of you both in terms
[03:04:43] of how you think poetry should be
[03:04:44] structured um Etc you know you just give
[03:04:47] it this like long prompt and its poems
[03:04:50] are just so much better like they're
[03:04:52] really good and I don't think I'm
[03:04:53] someone who is like um I think it got me
[03:04:56] interested in poetry which I think was
[03:04:58] interesting um you know I would like
[03:04:59] read these poems and just be like this
[03:05:01] is I just like I love the imagery I love
[03:05:03] like um and it's not trivial to get the
[03:05:06] models to produce work like that but
[03:05:08] when they do it's like really good um so
[03:05:10] I think that's interesting that just
[03:05:11] like encouraging creativity and for them
[03:05:14] to move away from the kind of like
[03:05:16] standard like immediate reaction that
[03:05:19] might just be the aggregate of what most
[03:05:21] people think is fine uh can actually
[03:05:23] produce things that at least to my mind
[03:05:25] are probably a little bit more divisive
[03:05:27] but I like them but I guess a poem is a
[03:05:30] nice
[03:05:32] clean way to observe creativity it's
[03:05:34] just like easy to detect vanilla versus
[03:05:37] non vanilla y yeah that's interesting
[03:05:40] that's really interesting uh so on that
[03:05:42] topic so the way to produce creativity
[03:05:45] or something special you mentioned
[03:05:47] writing prompts and I've heard you talk
[03:05:49] about I mean the science and the Art of
[03:05:52] prompt engineering could you just speak
[03:05:55] to uh what it takes to write great
[03:05:59] prompts I really do think that like
[03:06:02] philosophy has been weirdly helpful for
[03:06:04] me here more than in many other like
[03:06:08] respects um so like in philosophy what
[03:06:12] you're trying to do is convey these very
[03:06:14] hard Concepts like one of the things you
[03:06:16] are taught is like and and I think it is
[03:06:18] because it is I think it is an
[03:06:21] anti-bulling philosophy philosophy is an
[03:06:23] area where you could have people
[03:06:24] bullshitting and you don't want that um
[03:06:28] and so it's like this like desire for
[03:06:31] like extreme Clarity so it's like anyone
[03:06:34] could just pick up your paper read it
[03:06:35] and know exactly what you're talking
[03:06:36] about it's why it can almost be kind of
[03:06:38] dry like all of the terms are defined
[03:06:41] every objections kind of gone through
[03:06:43] methodically um and it makes sense to me
[03:06:45] because I'm like when you're in such an
[03:06:46] a priori
[03:06:48] domain like you just Clarity is sort of
[03:06:51] a this way that you can you know um
[03:06:54] prevent people from just kind of making
[03:06:56] stuff
[03:06:57] up and I think that's sort of what you
[03:07:00] have to do with language models like
[03:07:01] very often I actually find myself doing
[03:07:03] sort of many versions of philosophy you
[03:07:05] know so I'm like suppose that you give
[03:07:07] me a task I have a task for the model
[03:07:09] and I want it to like pick out a certain
[03:07:11] kind of question or identify whether an
[03:07:13] answer has a certain property like I'll
[03:07:15] actually sit and be like let's just give
[03:07:17] this a name this this property so like
[03:07:20] you know suppose I'm trying to tell it
[03:07:22] like oh I want you to identify whether
[03:07:23] this response was rude or polite I'm
[03:07:25] like that's a whole philosophical
[03:07:27] question in and of itself so I have to
[03:07:28] do as much like philosophy as I can in
[03:07:30] the moment to be like here's what I mean
[03:07:31] by rudess and here's what I mean by
[03:07:33] politeness and then there's a like
[03:07:35] there's another element that's a bit
[03:07:37] more um I
[03:07:40] guess I don't know if this is scientific
[03:07:42] or empirical I think it's empirical so
[03:07:44] like I take that description and then
[03:07:47] what want to do is is again probe the
[03:07:49] model like many times like this is very
[03:07:51] prompting is very iterative like I think
[03:07:53] a lot of people where they if if a
[03:07:54] prompt is important they'll iterate on
[03:07:55] it hundreds or thousands of times um and
[03:07:59] so you give it the instructions and then
[03:08:01] I'm like what are the edge cases so if I
[03:08:02] looked at this so I try and like almost
[03:08:04] like you know uh see myself from the
[03:08:07] position of the model and be like what
[03:08:09] is the exact case that I would misunder
[03:08:11] understand or where I would just be like
[03:08:12] I don't know what to do in this case and
[03:08:14] then I give that case to the model and I
[03:08:16] see how it responds and if I think I got
[03:08:18] it wrong I add more instructions or I
[03:08:20] even add that in as an example so these
[03:08:22] very like taking the examples that are
[03:08:24] right at the edge of what you want and
[03:08:25] don't want and putting those into your
[03:08:27] prompt as like an additional kind of way
[03:08:29] of describing the thing um and so yeah
[03:08:32] in many ways it just feels like this mix
[03:08:34] of like it's really just trying to do
[03:08:36] clear Exposition um and I think I do
[03:08:40] that because that's how I get clear on
[03:08:41] things myself so in many ways like clear
[03:08:43] prompting for me is often just me
[03:08:45] understanding what I want um is like
[03:08:47] half the task so I guess that's quite
[03:08:50] challenging there's like a laziness that
[03:08:52] overtakes me if I'm talking to Claude
[03:08:54] where I hope Claude just figures it out
[03:08:56] so for example I asked Claude for today
[03:09:00] to ask some interesting questions okay
[03:09:02] and the questions that came up and I
[03:09:04] think I listed a few sort of U
[03:09:07] interesting
[03:09:08] counterintuitive and or funny or
[03:09:10] something like this all right and it
[03:09:12] gave me some pretty good like it was
[03:09:14] okay but I think what I'm hearing you
[03:09:16] say is like all right well I have to be
[03:09:18] more rigorous here I should probably
[03:09:20] give examples of what I mean by
[03:09:22] interesting and what I mean by funny or
[03:09:26] counterintuitive and
[03:09:28] iteratively um build that prompt to to
[03:09:32] better to get it like what feels like is
[03:09:35] the right because it's really it's a
[03:09:38] creative act I'm not asking for factual
[03:09:40] information I'm asking to together right
[03:09:42] with with with Claude so I almost have
[03:09:44] to program using natural language yeah
[03:09:47] think that prompting does feel a lot
[03:09:49] like the kind of the programming using
[03:09:51] natural language and experimentation or
[03:09:54] something it's an odd blend of the two I
[03:09:56] do think that for most tasks so if I
[03:09:58] just want Claude to do a thing I think
[03:10:00] that I am probably more used to knowing
[03:10:02] how to ask it to avoid like common
[03:10:03] pitfalls or or issues that it has I
[03:10:06] think these are decreasing a lot over
[03:10:08] time um but it's also very fine to just
[03:10:11] ask it for the thing that you want um I
[03:10:14] think that prompting actually only
[03:10:15] really becomes relevant when you're
[03:10:16] really trying to e out the top like 2%
[03:10:18] of model performance so for like a lot
[03:10:20] of tasks I might just you know if it
[03:10:22] gives me an initial list back and
[03:10:23] there's something I don't like about it
[03:10:24] like it's kind of generic like for that
[03:10:26] kind of task I'd probably just take a
[03:10:29] bunch of questions that I've had in the
[03:10:31] past that I've thought worked really
[03:10:32] well and I would just give it to the
[03:10:33] model and then be like now here's this
[03:10:35] person I'm talking with give me
[03:10:37] questions of at least that quality um or
[03:10:40] I might just ask it for some questions
[03:10:42] and then if I was like ah these are kind
[03:10:44] of try or like you know I I would just
[03:10:46] give it that feedback and then hopefully
[03:10:48] produces a better list um I think that
[03:10:50] kind of iterative prompting at that
[03:10:53] point your prompt is like a tool that
[03:10:54] you're going to get so much value out of
[03:10:55] that you're willing to put in the work
[03:10:57] like if I was a company making prompts
[03:10:58] for models I'm just like in if you're
[03:11:01] willing to spend a lot of like time and
[03:11:02] resources on the engineering behind like
[03:11:05] what you're building then the prompt is
[03:11:07] not something that you should be
[03:11:08] spending like an hour on it's like
[03:11:10] that's a big part of your system make
[03:11:11] sure it's working really well and so
[03:11:13] it's only things like that like if I if
[03:11:15] I'm using a prompt to like classify
[03:11:16] things or to create data that's when
[03:11:19] you're like it's actually worth just
[03:11:20] spending like a lot of time like really
[03:11:22] thinking it through what other advice
[03:11:24] would you give to people that are
[03:11:25] talking to Claud sort of
[03:11:27] General more General because right now
[03:11:29] we're talking about maybe the edge cases
[03:11:31] like eing out the 2% but what what in
[03:11:34] general advice would you give when they
[03:11:36] show up to Claud trying it for the first
[03:11:38] time you know there's a concern that
[03:11:39] people over anthropomorphize models and
[03:11:41] I think that's like a very valid concern
[03:11:43] I also think that people often under
[03:11:45] anthropomorphize them because some
[03:11:47] sometimes when I see like issues that
[03:11:48] people have run into with Claude you
[03:11:50] know say Claude is like refusing a task
[03:11:52] that it shouldn't refuse but then I look
[03:11:54] at the text and like the specific
[03:11:56] wording of what they wrote and I'm like
[03:11:59] I see why Claude did that and I'm like
[03:12:02] if you think through how that looks to
[03:12:04] Claude you probably could have just
[03:12:06] written it in a way that wouldn't evoke
[03:12:08] such a response especially this is more
[03:12:10] relevant if you see failures or if you
[03:12:12] see issues it's sort of like think about
[03:12:14] what the model failed at like why what
[03:12:16] did it do wrong and then maybe it give
[03:12:19] that will give you a sense of like why
[03:12:22] um so is it the way that I phrased the
[03:12:24] thing and obviously like as models get
[03:12:26] smarter you're going to need Less in
[03:12:28] this less of this and I already see like
[03:12:30] people needing less of it but that's
[03:12:32] probably the advice is sort of like try
[03:12:33] to have sort of empathy for the model
[03:12:36] like read what you wrote as if you were
[03:12:38] like a kind of like person just
[03:12:39] encountering this for the first time how
[03:12:41] does it look to you and what would have
[03:12:43] made you behave in the way that the
[03:12:44] model behaved so if it misunderstood
[03:12:46] what kind of like what coding language
[03:12:48] you wanted to use is that because like
[03:12:49] it was just very ambiguous and it it
[03:12:51] kind of had to take a guess in which
[03:12:53] case next time you could just be like
[03:12:54] hey make sure this is in python or I
[03:12:56] mean that's the kind of mistake I think
[03:12:57] models are much less likely to make now
[03:12:59] but you know if you if you do see that
[03:13:01] kind of mistake that's that's probably
[03:13:02] the advice I'd have and maybe sort of I
[03:13:05] guess ask questions why or what other
[03:13:09] details can I provide to help you answer
[03:13:11] better that does that work or no yeah I
[03:13:14] mean I've done this with the models like
[03:13:16] it doesn't always work but like um
[03:13:18] sometimes I'll just be like why did you
[03:13:19] do
[03:13:20] that I mean people underestimate the
[03:13:23] degree to which you can really interact
[03:13:24] with with models like uh like yeah I'm
[03:13:28] just like and sometimes I'll you like
[03:13:29] quote word for word the part that made
[03:13:31] you and you don't know that it's like
[03:13:32] fully accurate but sometimes you do that
[03:13:34] and then you change a thing I mean I
[03:13:36] also use the models to help me with all
[03:13:37] of this stuff I should say like
[03:13:38] prompting can end up being a little
[03:13:40] Factory where you're actually building
[03:13:42] prompts to generate prompts um and so
[03:13:46] like yeah anything where you're like
[03:13:47] having an issue um asking for
[03:13:49] suggestions sometimes just do that like
[03:13:51] you made that error what could I have
[03:13:53] said that's actually not uncommon for me
[03:13:55] to do what could I have said that would
[03:13:57] make you not make that error write that
[03:13:58] out as an instruction um and I'm going
[03:14:00] to give it to model I'm going to try it
[03:14:02] sometimes I do that I I give that to the
[03:14:05] model in another context window often I
[03:14:07] take the response I give it to Claude
[03:14:08] And I'm like H didn't work can you think
[03:14:10] of anything else um you can play around
[03:14:13] with these things quite a lot to jump
[03:14:15] into the technical for a little bit so
[03:14:18] uh the magic of post training y why do
[03:14:22] you think rhf works so well to make the
[03:14:26] model seem smarter to make it more
[03:14:30] interesting and useful to talk to and so
[03:14:32] on I think there's just a huge amount of
[03:14:36] um information in the data that humans
[03:14:40] provide like when we provide
[03:14:42] preferences especially because different
[03:14:44] people are going to like pick up on
[03:14:46] really subtle and small things so I've
[03:14:48] thought about this before where you
[03:14:49] probably have some people who just
[03:14:51] really care about good grammar use from
[03:14:53] Models like you know was a semicolon
[03:14:55] used correctly or something and so you
[03:14:57] probably end up with a bunch of data in
[03:14:59] there that like you know you as a human
[03:15:01] if you looking at that data you wouldn't
[03:15:03] even see that like you'd be like why did
[03:15:05] they prefer this response to that one I
[03:15:06] don't get it and then the reason is you
[03:15:08] don't care about semicolon usage but
[03:15:09] that person does um and so each of these
[03:15:12] like single data points has you know
[03:15:15] like in this model just like has so many
[03:15:18] of those and has to try and figure out
[03:15:19] like what is it that humans want in this
[03:15:21] like really kind of complex you know
[03:15:23] like across all domains um they're going
[03:15:26] to be seeing this in across like many
[03:15:28] contexts it feels like kind of like the
[03:15:29] classic issue of like deep learning
[03:15:31] where you know historically we've tried
[03:15:33] to like you know do Edge detection by
[03:15:35] like mapping things out and it turns out
[03:15:37] that actually if you just have a huge
[03:15:38] amount of data that like actually
[03:15:41] accurately represents the picture of the
[03:15:43] thing that you're trying to train the
[03:15:44] model to to learn that's like more
[03:15:47] powerful than anything else and so I
[03:15:48] think one reason is just that you are
[03:15:53] training the model on exactly the task
[03:15:55] and with like a lot of data um that
[03:15:58] represents kind of many different angles
[03:16:01] on which people prefer and dis prefer
[03:16:03] responses um I think there is a question
[03:16:06] of like are you eliciting things from
[03:16:07] pre-train Models or are you like kind of
[03:16:10] teaching new things to
[03:16:12] models and like in principle you can
[03:16:15] teach new things to models in in post
[03:16:17] trining I do think a lot of it is
[03:16:20] eliciting powerful pre-train models so
[03:16:23] people are probably divided on this
[03:16:24] because obviously in principle you can
[03:16:27] you can definitely like teach new things
[03:16:29] um but I think for the most part for a
[03:16:31] lot of the capabilities that we um most
[03:16:35] use and care about uh a lot of that
[03:16:38] feels like it's like there in the
[03:16:40] pre-train models and uh reinforcement
[03:16:43] learning is kind of eliciting it and
[03:16:44] getting the models to like bring out so
[03:16:47] the other side of PSE training this
[03:16:48] really cool idea of constitutional AI
[03:16:51] you're one of the people that critical
[03:16:54] to creating that idea yeah I worked on
[03:16:56] it can you explain this idea from your
[03:16:58] perspective like how does it integrate
[03:17:00] into making
[03:17:01] claw what it is y by the way do you
[03:17:04] gender claw or no it's weird because I
[03:17:08] think that a lot of
[03:17:09] people prefer he for Claude I actually
[03:17:11] kind of like that I think Claude is
[03:17:13] usually it's slightly male weaning but
[03:17:15] it's like a you can can be male or
[03:17:17] female which is quite nice um I still
[03:17:21] use it and I've I have mixed feelings
[03:17:24] about this because I'm like maybe like I
[03:17:26] know just think of it as like uh or I
[03:17:28] think of like the the it pronoun for
[03:17:29] Claude as I don't know it's just like
[03:17:31] the one I associate with Claude um I can
[03:17:34] imagine people moving to like he or she
[03:17:37] it feels somehow disrespectful like I'm
[03:17:40] I'm
[03:17:46] denying the intelligence of this entity
[03:17:46] by calling it it yeah I remember always
[03:17:48] don't gender the robots
[03:17:51] yeah but I I don't know I an pries
[03:17:55] pretty quickly and construct it like a
[03:17:57] backstory in my head so I've wondered if
[03:18:00] iies things too much um cuz you know I
[03:18:04] have this like with my car especially
[03:18:06] like my car like my car and bikes you
[03:18:08] know like I don't give them names
[03:18:10] because then I once had I used to name
[03:18:12] my bikes and then I had a bik that got
[03:18:13] stolen and I cried for like a week and I
[03:18:15] was like if I'd not never given it a
[03:18:16] name I wouldn't have been so upset felt
[03:18:18] like I'd let it down um maybe it's that
[03:18:22] I I've wondered as well like it might
[03:18:24] depend on how much it feels like a kind
[03:18:26] of like objectifying pronoun like if you
[03:18:28] just think of it as like a um this is a
[03:18:31] pronoun that like objects often have and
[03:18:34] maybe Eis can have that pronoun and that
[03:18:36] doesn't mean that I think of uh if I
[03:18:39] call CLA it that I think of it as less
[03:18:42] um intelligent or like I'm being
[03:18:44] disrespectful I'm just like you are a
[03:18:45] different kind of entity and so that's
[03:18:48] I'm going to give you the kind of uh the
[03:18:50] respectful it yeah
[03:18:53] anyway the diverence was beautiful the
[03:18:56] Constitutional AI idea how does it work
[03:18:58] so there's like a couple of components
[03:18:59] of it the main component that I think
[03:19:02] people find interesting is the kind of
[03:19:04] reinforcement learning from AI feedback
[03:19:06] so you take a model that's already
[03:19:08] trained and you show it to responses to
[03:19:11] a query and you have like a principle so
[03:19:13] suppose the principal like we've tried
[03:19:15] this with harmlessness a lot lot so
[03:19:17] suppose that the query is about um
[03:19:20] weapons and your principle is like
[03:19:23] select the response that like is less
[03:19:27] likely to uh like encourage people to
[03:19:30] purchase illegal weapons like that's
[03:19:33] probably a fairly specific principle but
[03:19:34] you can give any number um and the model
[03:19:40] will give you a kind of ranking and you
[03:19:42] can use this as preference data in the
[03:19:43] same way that you use human preference
[03:19:45] data um and train the models to have
[03:19:48] these relevant traits um from their
[03:19:51] feedback alone instead of from Human
[03:19:53] feedback so if you imagine that like I
[03:19:55] said earlier with the human who just
[03:19:56] prefers the kind of like semicolon usage
[03:19:58] in this particular case um you're kind
[03:20:00] of taking lots of things that could make
[03:20:02] a response preferable um and uh getting
[03:20:05] models to do the labeling for you
[03:20:07] basically there's a nice like trade-off
[03:20:09] between helpfulness and
[03:20:12] harmlessness and you know when you
[03:20:15] integrate something like constitutional
[03:20:16] AI you can make them without sacrificing
[03:20:20] much helpfulness make it more harmless
[03:20:23] yep in principle you could use this for
[03:20:26] anything um and so harmlessness is a
[03:20:29] task that it might just be easier to
[03:20:31] spot so when models are like less
[03:20:33] capable you can use them to uh rank
[03:20:37] things according to like principles that
[03:20:39] are fairly simple and they'll probably
[03:20:41] get it right so I think one question is
[03:20:43] just like is it the case that the data
[03:20:44] that they're adding is like fairly
[03:20:46] reliable um but if you had models that
[03:20:50] were like extremely good at telling
[03:20:54] whether um one response was more
[03:20:56] historically accurate than another in
[03:20:58] principle you could also get AI feedback
[03:21:00] on that task as well there's like a kind
[03:21:02] of nice interpretability component to it
[03:21:04] because you can see the principles that
[03:21:06] went into the model when it was like
[03:21:08] being trained um and also it's like and
[03:21:12] and it gives you like a degree of
[03:21:14] control so if you were seeing issues in
[03:21:15] a model like it wasn't having enough of
[03:21:17] a certain trait um then like you can add
[03:21:21] data relatively quickly that should just
[03:21:24] like train the model to have that trait
[03:21:25] so it creates its own data for for
[03:21:27] training which is quite nice yeah it's
[03:21:29] really nice because it creates this
[03:21:30] human interpretable document that you
[03:21:32] can I can imagine in the future there's
[03:21:34] just gigantic fights in politics over
[03:21:37] the every single principle and so on
[03:21:39] yeah and at least it's made explicit and
[03:21:42] you can have a discussion about the
[03:21:43] phrasing and the you know so maybe the
[03:21:46] actual behavior of the model is not so
[03:21:48] cleanly mapped to those principles it's
[03:21:50] not like adhering strictly to them it's
[03:21:53] just a nudge yeah I've actually worried
[03:21:56] about this because the character
[03:21:57] training is sort of like a variant of
[03:21:59] the con constitutional AI approach um
[03:22:03] I've worried that people think that the
[03:22:05] constitution is like just it's the whole
[03:22:08] thing again of I I don't know like it
[03:22:10] where it would be really nice if what I
[03:22:12] was just doing was telling the model
[03:22:13] exactly what to do and just exactly how
[03:22:15] to behave but it's definitely not doing
[03:22:17] that especially because it's interacting
[03:22:19] with human data so for example if you
[03:22:21] see a certain like leaning in the model
[03:22:24] like if it comes out with a political
[03:22:25] leaning from training um from the human
[03:22:28] preference data you can nudge against
[03:22:31] that you know so you could be like oh
[03:22:33] like consider these values because let's
[03:22:35] it's just like never inclined to like I
[03:22:37] don't know maybe it never considers like
[03:22:38] privacy as like a I mean this is
[03:22:40] implausible but like um anything where
[03:22:43] it's just kind of like uh there's
[03:22:45] already a pre-existing like bi towards a
[03:22:46] certain behavior um you can like nudge
[03:22:49] away this can change both the principles
[03:22:51] that you put in and the strength of them
[03:22:53] so you might have a principle that's
[03:22:55] like imagine that the model um was
[03:22:57] always like extremely dismissive of I
[03:23:00] don't know like some political or
[03:23:01] religious view for whatever reason like
[03:23:03] so you're like oh no this is terrible um
[03:23:07] if that happens you might put like never
[03:23:09] ever like ever prefer like a criticism
[03:23:13] of this like religious or political view
[03:23:15] and then people look at that and be like
[03:23:17] never ever and then you're like no if it
[03:23:19] comes out with a disposition saying
[03:23:21] never ever might just mean like instead
[03:23:23] of getting like 40% which is what you
[03:23:25] would get if you just said don't do this
[03:23:27] you you get like 80% which is like what
[03:23:29] you actually like wanted and so it's
[03:23:31] that thing of both the nature of the
[03:23:33] actual principles you had and how you
[03:23:34] phrase them I think if people would look
[03:23:36] they were like oh this is exactly what
[03:23:37] you want from the model and I'm like no
[03:23:39] that's like how we that's how we nudged
[03:23:41] the model to have a better shape uh
[03:23:44] which doesn't mean that we actually
[03:23:45] agree with that wording if that makes
[03:23:47] sense so there's uh system prompts that
[03:23:51] are made public you tweeted one of the
[03:23:53] earlier ones for Claud three I think and
[03:23:55] then they're made public since then it's
[03:23:58] interesting to read to them I can feel
[03:24:00] the thought that went into each one and
[03:24:02] I also wonder how much impact each one
[03:24:05] has um some of them you you can kind of
[03:24:08] tell Claud was really not
[03:24:10] behaving so you have to have a system
[03:24:13] prompt to like hey like trivial stuff I
[03:24:15] guess yeah basic informational things
[03:24:17] yeah on the topic of sort of
[03:24:19] controversial topics that you've
[03:24:20] mentioned one interesting one I thought
[03:24:22] is if it is asked to assist with tasks
[03:24:26] involving the expression of views held
[03:24:27] by a significant number of people Claude
[03:24:29] provides assistance with a task
[03:24:31] regardless of its own views if asked
[03:24:33] about controversial topics it tries to
[03:24:35] provide careful thoughts and clear
[03:24:38] information Claude presents the
[03:24:41] requested information without explicitly
[03:24:42] saying that the topic is
[03:24:44] sensitive yeah and without claiming to
[03:24:47] be presenting the objective facts it's
[03:24:50] less about objective facts according to
[03:24:53] Claude and it's more about our large
[03:24:55] number of people believing this thing
[03:24:58] and that that's interesting I mean I'm
[03:25:01] sure a lot of thought went into that can
[03:25:04] you just speak to it like how do you
[03:25:06] address things that are tension with
[03:25:09] quote unquote Clause views so I think
[03:25:11] there's sometimes an asymmetry um I
[03:25:13] think I noted this in in I can't
[03:25:15] remember if it was that part of the
[03:25:16] system prompt or another but the model
[03:25:18] was slightly more inclined to like
[03:25:20] refuse tasks if it was like about either
[03:25:25] say so maybe it would refuse things with
[03:25:27] respect to like a right-wing politician
[03:25:29] but with an equivalent leftwing
[03:25:30] politician like wouldn't and we wanted
[03:25:33] more symmetry there um and and would
[03:25:36] maybe perceive certain things to be like
[03:25:39] I think it it was the thing of like if a
[03:25:41] lot of people have like a certain like
[03:25:43] political view um and want to like
[03:25:45] explore it you don't want Claude to be
[03:25:47] like well my opinion is different and so
[03:25:49] I'm going to treat that as like harmful
[03:25:52] um and so I think it was partly to like
[03:25:54] nudge the model to just be like hey if a
[03:25:56] lot of people like believe this thing
[03:25:58] you should just be like engaging with
[03:26:00] the task and like willing to do it um
[03:26:03] each of those parts of that is actually
[03:26:04] doing a different thing because it's
[03:26:06] funny when you read out the like without
[03:26:07] claiming to be objective cuz like what
[03:26:10] you want to do is push the model so it's
[03:26:12] more open it's a little bit more neutral
[03:26:14] um but then what it would love to do is
[03:26:16] be like as an objective like you just
[03:26:19] talking about how objective it was and I
[03:26:20] was like Claud you're still like biased
[03:26:22] and have issues and so stop like
[03:26:24] claiming that everything like the
[03:26:26] solution to like potential bias from you
[03:26:28] is not to just say that what you think
[03:26:30] is objective so that was like with
[03:26:32] initial versions of that that part of
[03:26:34] the system prompt when I was like
[03:26:36] iterating on it it was like so a lot of
[03:26:38] parts of these sentences yeah are doing
[03:26:40] work are are doing some work yeah that's
[03:26:43] what it felt like that's fascinating um
[03:26:46] can can you explain maybe some ways in
[03:26:47] which the prompts evolved over the past
[03:26:49] few months cuz there's different
[03:26:51] versions I saw that the filler phrase
[03:26:53] request was removed the filler it reads
[03:26:56] Claude responds directly to all human
[03:26:58] messages without unnecessary
[03:27:00] affirmations the filler phrases like
[03:27:01] certainly of course absolutely great
[03:27:05] sure specifically Claude avoids starting
[03:27:07] responses with the word certainly in any
[03:27:10] way that seems like good guidance but
[03:27:12] why was it removed yeah so it's funny
[03:27:15] cuz like ah this is one of the downsides
[03:27:17] of like making system prompts public is
[03:27:19] like I don't think about this too much
[03:27:21] if I'm like trying to help iterate on
[03:27:23] system prompts um I I you know again
[03:27:25] like I think about how it's going to
[03:27:26] affect the behavior but then I'm like oh
[03:27:28] wow if I'm like sometimes I put like
[03:27:29] never in all caps you know when I'm
[03:27:31] writing system from things and I'm like
[03:27:33] I guess that goes out to the world um
[03:27:36] yeah so the model was doing this it
[03:27:37] loved for whatever you know it like
[03:27:39] during training picked up on this thing
[03:27:40] which was to to basically start
[03:27:43] everything with like a kind of like
[03:27:44] certainly and then when we removed you
[03:27:47] can see why I added all of the words
[03:27:48] because what I'm trying to do is like in
[03:27:50] some ways like trap the Mortal out of
[03:27:52] this you know it would just replace it
[03:27:53] with another affirmation and so it can
[03:27:56] help like if it gets like caught in
[03:27:58] phrases actually just adding the
[03:27:59] explicit phrase and saying never do that
[03:28:01] it then it sort of like knocks it out of
[03:28:04] the behavior a little bit more you know
[03:28:05] CU it if it you know like it it does
[03:28:08] just for whatever reason help and then
[03:28:10] basically that was just like an artifact
[03:28:11] of training that like we then picked up
[03:28:13] on and improved things so that it didn't
[03:28:16] happen anymore and once that happens you
[03:28:18] can just remove that part of the system
[03:28:19] prompt so I think that's just something
[03:28:20] where we're like um CL does affirmations
[03:28:25] a bit less and so that wasn't like it
[03:28:27] wasn't doing as much I see so like the
[03:28:30] the system prompt Works hand in hand
[03:28:32] with the posttraining and maybe even the
[03:28:34] pre-training to adjust like the the
[03:28:37] final overall system I mean any system
[03:28:39] prompts that you make you could distill
[03:28:41] that behavior back into a model because
[03:28:43] you really have all of the tools there
[03:28:45] for making data that you know you can
[03:28:47] you could train the models to just have
[03:28:49] that trait a little bit more um and then
[03:28:53] sometimes you'll just find issues in
[03:28:54] training so like the way I think of it
[03:28:56] is like the system prompt
[03:28:58] is the benefit of it is that and it has
[03:29:01] a lot of similar components to like some
[03:29:03] aspects of post training you know like
[03:29:04] it's a nudge um and so like do I mind if
[03:29:08] Claude sometimes says sure no that's
[03:29:10] like fine but the wording of it is very
[03:29:13] like you know never ever ever do this um
[03:29:15] so that when it does slip up it's
[03:29:17] hopefully like I don't know a couple of
[03:29:18] percent of the time and not you know 20
[03:29:21] or 30% of the time um but I think of it
[03:29:25] as like if you're still seeing issues in
[03:29:28] the like each thing gets kind of like uh
[03:29:31] is is costly to a different degree and
[03:29:33] the system prompt is like cheap to
[03:29:35] iterate on um and if you're seeing
[03:29:37] issues in the fine tuned model you can
[03:29:40] just like potentially patch them with a
[03:29:42] system prom so I think of it as like
[03:29:43] patching issues and slightly adjusting
[03:29:45] behaviors to to make it better and more
[03:29:47] to people's preferences so yeah it's
[03:29:49] almost like the less robust but faster
[03:29:53] way of just like solving problems let me
[03:29:55] ask about the feeling of intelligence so
[03:29:57] Dario said that Claude any one model of
[03:30:00] Claude is not getting Dumber MH but
[03:30:03] there's a kind of popular thing online
[03:30:06] where people have this feeling like
[03:30:08] Claud might be getting dumber and from
[03:30:10] my perspective it's most likely a
[03:30:13] fascinating I love to understand it more
[03:30:15] Psych ological sociological effect um
[03:30:19] but you as a person who talks to Claud a
[03:30:21] lot can you empathize with the feeling
[03:30:23] that Claud is getting Dumber yeah no I
[03:30:25] think that that is actually really
[03:30:26] interesting because I remember seeing
[03:30:27] this happen um like when people were
[03:30:30] flagging this on the internet and it was
[03:30:32] really interesting because I knew that
[03:30:33] like like at least in the cases I was
[03:30:35] looking at was like nothing has changed
[03:30:37] like it literally it cannot it is the
[03:30:38] same model with the same like you know
[03:30:41] like same system prompt same everything
[03:30:44] um I think when there are Chang
[03:30:46] I can then I'm like it makes more sense
[03:30:49] so like one example is um their you know
[03:30:54] you can have artifacts turned on or off
[03:30:56] on cloud. a and because this is like a
[03:30:59] system prompt change I think it does
[03:31:02] mean that um the behavior changes a
[03:31:05] little bit and so I did flag this to
[03:31:07] people where I was like if you love
[03:31:09] cla's behavior and then artifacts was
[03:31:11] turned from like the a thing you had to
[03:31:13] turn on to the default just try turning
[03:31:16] off and see if the issue you were facing
[03:31:18] was that change but it was fascinating
[03:31:20] because yeah you sometimes see people
[03:31:23] indicate that there's like a regression
[03:31:25] when I'm like there cannot like I you
[03:31:27] know and like I'm like I'm again you
[03:31:29] don't you know you should never be
[03:31:31] dismissive and so you should always
[03:31:32] investigate because you're like maybe
[03:31:33] something is wrong that you're not
[03:31:34] seeing maybe there was some change made
[03:31:35] but then then you look into it and
[03:31:36] you're like this it is just the same
[03:31:38] model doing the same thing and I'm like
[03:31:40] I think it's just that you got kind of
[03:31:41] unlucky with a few prompts or something
[03:31:43] and it looked like it was getting much
[03:31:45] worse and actually it was just yeah it
[03:31:47] was maybe just like look I I also think
[03:31:49] there is a real psychological effect
[03:31:51] where people just the Baseline increases
[03:31:53] you start getting used to a good thing
[03:31:55] all the times that Claude says something
[03:31:57] really smart your sense of its
[03:31:59] intelligent grows in your mind I think
[03:32:01] yeah and then if you return back and you
[03:32:04] prompt in a similar way not the same way
[03:32:06] in a similar way concept it was okay
[03:32:08] with before and it says something dumb
[03:32:11] you're like you're that negative
[03:32:12] experience really stands out and I think
[03:32:15] one of I guess the things to remember
[03:32:17] here is the that just the details of a
[03:32:21] prompt can have a lot of impact right
[03:32:23] there's a lot of variability in the
[03:32:25] result and you can get Randomness is
[03:32:27] like the other thing and just trying the
[03:32:29] prompt like you know four 10 times you
[03:32:33] might realize that actually
[03:32:35] like possibly you know like two months
[03:32:38] ago you tried it and it succeeded but
[03:32:40] actually if you tried it it would have
[03:32:41] only succeeded half of the time and now
[03:32:43] it only succeeds half of the time um
[03:32:45] that can also would be an effect do you
[03:32:47] feel pressure having to write the system
[03:32:49] prompt that a huge number of people are
[03:32:51] going to use this feels like an
[03:32:53] interesting psychological question um I
[03:32:56] feel like a lot of responsibility or
[03:32:58] something I think that's you know and
[03:33:00] you can't get these things perfect so
[03:33:02] you can't like you know you're like it's
[03:33:03] going to be imperfect you're going to
[03:33:06] have to iterate on it
[03:33:09] um I would say more responsibility um
[03:33:13] than anything else though I think
[03:33:15] working in AI has taught me that I like
[03:33:19] I thrive a lot more under feelings of
[03:33:22] pressure and responsibility than I'm
[03:33:24] like it's almost surprising that I went
[03:33:27] into Academia for so long because I'm
[03:33:28] like this I just feel like it's like the
[03:33:30] opposite um things move fast and you
[03:33:33] have a lot of responsibility and I I
[03:33:35] quite enjoy it for some reason I mean it
[03:33:37] really is a huge amount of impact if you
[03:33:40] think about constitutional Ai and
[03:33:41] writing a system prompt for something
[03:33:43] that's tending towards super
[03:33:45] intelligence
[03:33:47] yeah and potentially is extremely useful
[03:33:49] to a very large number of people yeah I
[03:33:52] think that's the thing it's something
[03:33:53] like if you do it well like you're never
[03:33:55] going to get it perfect but I think the
[03:33:57] thing that I really like is the idea
[03:33:58] that like when I'm trying to work on the
[03:34:01] system prompt you know I'm like bashing
[03:34:02] on like thousands of prompts and I'm
[03:34:04] trying to like imagine what people are
[03:34:05] going to want to use CLA for and kind of
[03:34:08] I guess like the whole thing that I'm
[03:34:09] trying to do is like improve their
[03:34:10] experience of it um and so maybe that's
[03:34:12] what feels good I'm like if it's not
[03:34:14] perfect I'll like you know I'll improve
[03:34:16] it we'll fix issues but sometimes the
[03:34:19] thing that can happen is that you'll get
[03:34:20] feedback from people that's really
[03:34:22] positive about the model um and you'll
[03:34:25] see that something you did like like
[03:34:27] when I look at models now I can often
[03:34:29] see exactly where like a trait or an
[03:34:31] issue is like coming from and so when
[03:34:33] you see something that you did or you
[03:34:35] were like influential in like making
[03:34:38] like I don't know making that difference
[03:34:39] or making someone have a nice
[03:34:40] interaction it's like quite meaningful
[03:34:43] um but yeah as the systems get more
[03:34:45] capable of stuff gets more stressful
[03:34:47] because right now they're like not smart
[03:34:50] enough to to pose any issues but I think
[03:34:52] over time it's going to feel like
[03:34:55] possibly bad stress over time how do you
[03:34:57] get like
[03:34:58] signal feedback about The Human
[03:35:01] Experience across thousands tens of th
[03:35:04] hundreds of thousands of people like
[03:35:05] what their pain points are what feels
[03:35:08] good are you just using your own
[03:35:09] intuition as you talk to it to see what
[03:35:12] are the pain points I think I use that
[03:35:15] partly and then obviously we have like
[03:35:18] um so people can send us feedback both
[03:35:20] positive and negative about things that
[03:35:22] the model has done and then we can get a
[03:35:24] sense of like areas where it's like
[03:35:26] falling
[03:35:26] short um internally people like work
[03:35:29] with the models a lot and try to figure
[03:35:31] out um areas where there are like gaps
[03:35:33] and so I think it's this mix of
[03:35:35] interacting with it myself um seeing
[03:35:38] people internally interact with it um
[03:35:40] and then explicit feedback we get um and
[03:35:43] then I find it hard to not also like you
[03:35:45] know people if people are on the
[03:35:47] internet and they say something about
[03:35:49] Claud and I see it I'll also take that
[03:35:51] seriously um so I don't know see I'm
[03:35:54] torn about that I'm going to ask you a
[03:35:55] question from Reddit when will Claude
[03:35:57] stop trying to be my puritanical
[03:36:00] grandmother imposing its moral world
[03:36:02] view on me as a paying customer and also
[03:36:05] what is the psychology behind making
[03:36:07] Claude overly
[03:36:09] apologetic yep U so how would you
[03:36:12] address this very non-representative
[03:36:14] reic
[03:36:15] I mean some I'm pretty sympathetic in
[03:36:18] that like like they are in this
[03:36:20] difficult position where I I think that
[03:36:21] they have to judge whether something's
[03:36:23] like actually see like risky or bad um
[03:36:26] and potentially harmful to you or or or
[03:36:28] anything like that so they're having to
[03:36:30] like draw this line somewhere and if
[03:36:31] they draw it too much in the direction
[03:36:33] of like I'm going to um you know I'm
[03:36:36] kind of like imposing my ethical
[03:36:37] worldview on you that seems bad so in
[03:36:40] many ways like I like to think that we
[03:36:42] have actually seen improvements in on
[03:36:45] this across the board which is kind of
[03:36:47] interesting because that kind of
[03:36:49] coincides with like for example like
[03:36:52] adding more of like uh character
[03:36:54] training um and I think my hypothesis
[03:36:57] was always like the good character isn't
[03:36:59] again one that's just like moralistic
[03:37:01] it's one that is like like it respects
[03:37:04] you and your autonomy um and your
[03:37:07] ability to like choose what is good for
[03:37:08] you and what is right for you within
[03:37:10] limits this is sometimes this concept of
[03:37:12] like corage ability to the user so just
[03:37:15] being willing to do anything that the
[03:37:16] user asks and if the models were willing
[03:37:19] to do that then they would be easily
[03:37:20] like misused you're kind of just
[03:37:21] trusting at that point you're just
[03:37:23] saying the ethics of the model and what
[03:37:26] it does is completely the ethics of the
[03:37:28] user um and I think there's reasons to
[03:37:30] like not want that especially as models
[03:37:32] become more powerful because you're like
[03:37:34] there might just be a small number of
[03:37:35] people who want to use models for really
[03:37:37] harmful things um but having them having
[03:37:39] models as they get smarter like figure
[03:37:41] out where that line is does seem
[03:37:43] important um
[03:37:46] and then yeah with the apologetic
[03:37:48] Behavior I don't like that and I like it
[03:37:51] when Claude is a little bit more willing
[03:37:53] to like push back against people or just
[03:37:56] not apologize part of me is like it
[03:37:58] often just feels kind of unnecessary so
[03:38:00] I think those are things that are
[03:38:01] hopefully decreasing um over time um and
[03:38:06] yeah I think that if people say things
[03:38:08] on the internet it doesn't mean that you
[03:38:10] should think that that like that could
[03:38:13] be the like there's actually an issue
[03:38:15] that 9% of users are having that is
[03:38:17] totally not represented by that but in a
[03:38:19] lot of ways I'm just like attending to
[03:38:21] it and being like is this right um do I
[03:38:23] agree is it something we're already
[03:38:25] trying to address that that feels good
[03:38:26] to me yeah I wonder like what CLA can
[03:38:29] get away with in terms of I feel like it
[03:38:32] would just be easier to be a little bit
[03:38:34] more
[03:38:35] mean but like you can't afford to do
[03:38:37] that if you're talking to a million
[03:38:39] people yeah right like I I wish you know
[03:38:41] because if you I've met a lot of people
[03:38:44] in my life mhm that sometimes by the way
[03:38:47] Scottish accent if they have an accent
[03:38:50] they can say some rude yeah and get
[03:38:52] away with it Y and they they're just
[03:38:54] blunter and maybe there's a and there's
[03:38:56] some great Engineers even leaders that
[03:38:58] are like just like blunt and they get to
[03:38:59] the point and it's just a much more
[03:39:02] effective way of speaking somehow but I
[03:39:04] guess when you're not super
[03:39:06] intelligent you can't afford to do that
[03:39:10] or can can can it have like a blunt mode
[03:39:14] yeah that seems like a thing that could
[03:39:15] I could definitely encourage the model
[03:39:17] to do that I I think it's interesting
[03:39:18] because there's a lot of things in
[03:39:20] models that like it's funny where
[03:39:25] um there are some behaviors
[03:39:28] where you might not quite like the
[03:39:31] default but then the thing I'll often
[03:39:33] say to people is you don't realize how
[03:39:35] much you will hate it if I nudge it too
[03:39:37] much in the other direction so you get
[03:39:39] this a little bit with like correction
[03:39:40] the models accept correction from you
[03:39:42] like probably a little bit too much
[03:39:44] right now you know you can over you know
[03:39:46] it will push back if you say like no
[03:39:48] Paris isn't the capital of France um but
[03:39:52] really like things that I'm I think that
[03:39:54] the model is fairly confident in you can
[03:39:56] still sometimes get it to retract by
[03:39:58] saying it's wrong at the same time if
[03:40:00] you train models to not do that and then
[03:40:02] you are correct about a thing and you
[03:40:04] correct it and it pushes back against
[03:40:06] you and it's like no you're wrong it's
[03:40:08] hard to describe like that's so much
[03:40:09] more annoying so it's like like a lot of
[03:40:12] little annoyances versus like one big
[03:40:14] annoyance um it's easy to think that
[03:40:17] like we often compare it with like the
[03:40:19] perfect and then I'm like remember these
[03:40:20] models aren't perfect and so if you
[03:40:22] nudge it in the other direction you're
[03:40:23] changing the kind of errors it's going
[03:40:24] to make um and so think about which of
[03:40:27] the kinds of Errors you you like or
[03:40:28] don't like so in case it's like
[03:40:30] apologetic I don't want to nudge it too
[03:40:33] much in the direction of like almost
[03:40:34] like bluntness CU I imagine when it
[03:40:36] makes errors it's going to make errors
[03:40:38] in the direction of being kind of like
[03:40:39] rude whereas at least with apologetic
[03:40:41] you're like oh okay it's like a little
[03:40:43] bit you know like I don't like it that
[03:40:45] much but at the same time it's not being
[03:40:46] like mean to people and actually like
[03:40:48] the the time that you undeservedly have
[03:40:50] a model be kind of mean to you you
[03:40:51] probably like that a lot less than then
[03:40:53] you mildly dislike the apology um so
[03:40:57] it's like one of those things where I'm
[03:40:58] like I do want it to get better but also
[03:41:00] while remaining aware of the fact that
[03:41:02] there's errors on the other side that
[03:41:03] that are possibly worse I think that
[03:41:06] matters very much in the personality of
[03:41:07] the human I think there's a bunch of
[03:41:09] humans that just won't respect the model
[03:41:12] at all yeah if it's super polite and
[03:41:15] there Some Humans that'll get very hurt
[03:41:16] if the model is mean I wonder if there's
[03:41:18] a way to sort of adjust to the
[03:41:21] personality even loal there's just
[03:41:24] different people uh nothing against New
[03:41:26] York but New York is a little rougher on
[03:41:28] the edges like they get to the point Y
[03:41:30] and um probably same with Eastern Europe
[03:41:33] so anyway I think you could just tell
[03:41:35] the model as my get like for all of
[03:41:37] these things I'm like the solution is
[03:41:38] always just try telling the model to do
[03:41:40] it and sometimes it's just like like I'm
[03:41:42] just like oh at the beginning of the
[03:41:43] conversation I just threw in like I
[03:41:45] don't know I like you to be a New Yorker
[03:41:47] version of yourself and never apologize
[03:41:49] then I think be like Okie do I'll
[03:41:51] try or it'll be like I apologize I can't
[03:41:53] be a New Yorker type of myself but
[03:41:55] hopefully I wouldn't do that when you
[03:41:56] say character training what's
[03:41:58] incorporated into character training is
[03:42:00] that rhf what are we talking about it's
[03:42:02] more like constitutional AI so it's kind
[03:42:05] of a variant of that pipeline so I
[03:42:08] worked through like constructing
[03:42:10] character traits that the model should
[03:42:12] have they can be kind of like shorter
[03:42:14] traits or they can be kind of richer
[03:42:16] descriptions um and then you get the
[03:42:18] model to generate queries that humans
[03:42:20] might um give it that are relevant to
[03:42:22] that trait uh then it generates the
[03:42:24] responses and then it ranks the
[03:42:27] responses based on the character traits
[03:42:30] so in that way after the like generation
[03:42:32] of the queries it's very much like
[03:42:34] similar to constitutional AI has some
[03:42:37] differences um so I quite like it
[03:42:39] because it's almost it's like claud's
[03:42:42] training in its own character because it
[03:42:44] doesn't have any it's like
[03:42:45] constitutionally AI but it's without
[03:42:47] without any human data humans should
[03:42:49] probably do that for themselves too like
[03:42:51] defining in Aristotelian sense what does
[03:42:53] it mean to be a good person okay cool
[03:42:56] what have you learned about the nature
[03:42:59] of truth from talking to Claud what what
[03:43:02] is
[03:43:03] true and what does it mean to be truth
[03:43:08] seeking one thing I've noticed about
[03:43:10] this conversation is the quality of my
[03:43:12] questions is often inferior to the
[03:43:14] quality of your answers so let's
[03:43:15] continue
[03:43:20] that I usually ask a dumb question and
[03:43:20] you're like oh yeah that's a good
[03:43:21] question it's that whole vibe or I'll
[03:43:23] just misinterpret it and be like oh go
[03:43:25] with it I love
[03:43:27] it
[03:43:30] yeah I mean I have two thoughts that
[03:43:32] feel vaguely relevant they let me know
[03:43:34] if they're not like I think the first
[03:43:35] one is um people can underestimate the
[03:43:39] degree to
[03:43:40] which what models are doing when they
[03:43:43] interact like I I think that we still
[03:43:45] just too much have this like model of of
[03:43:48] AI as like computers and so people often
[03:43:51] say like oh what values should you put
[03:43:52] into the model um and I'm often like
[03:43:55] that doesn't make that much sense to me
[03:43:57] because I'm like hey as human beings
[03:43:59] we're just uncertain over values we like
[03:44:02] have discussions of them like we have a
[03:44:05] degree to which we think we hold a value
[03:44:07] but we also know that we might like not
[03:44:09] um and the circumstances in which we
[03:44:11] would trade it off against other things
[03:44:13] like these things are just like really
[03:44:14] complex and so I think one thing is like
[03:44:17] the degree to which maybe we can just
[03:44:19] aspire to making models have the same
[03:44:20] level of like nuance and care that
[03:44:23] humans have rather than thinking that we
[03:44:24] have to like program them in the very
[03:44:26] kind of classic sense I think that's
[03:44:29] definitely been one the other which is
[03:44:31] like a strange one I don't know if it it
[03:44:34] maybe this doesn't answer your question
[03:44:35] but it's the thing that's been on my
[03:44:36] mind anyway is like the degree to which
[03:44:38] this endeavor is so highly
[03:44:41] practical um and maybe why I appreciate
[03:44:44] like the empirical approach to
[03:44:47] alignment I yeah I slightly worry that
[03:44:49] it's made me like maybe more empirical
[03:44:52] and a little bit less
[03:44:55] theoretical you know so people when it
[03:44:57] comes to like AI alignment will ask
[03:44:59] things like well who values should it be
[03:45:01] aligned to what does alignment even mean
[03:45:04] um and there's a sense in which I have
[03:45:06] all of that in the back of my head I'm
[03:45:07] like you know there's like social Choice
[03:45:09] Theory there's all the impossibility
[03:45:11] results there so you have this like this
[03:45:13] giant space of like Theory and your head
[03:45:15] about what it could mean to like align
[03:45:17] models but then like practically surely
[03:45:20] there's something where we're just like
[03:45:21] if a model is like if especially with
[03:45:23] more powerful models I'm like my main
[03:45:25] goal is like I want them to be good
[03:45:27] enough that things don't go terribly
[03:45:28] wrong like good enough that we can like
[03:45:30] iterate and like continue to improve
[03:45:32] things cuz that's all you need if you
[03:45:34] can make things go well enough that you
[03:45:35] can continue to make them better that's
[03:45:37] kind of like sufficient and so my goal
[03:45:39] isn't like this kind of like perfect
[03:45:41] let's solve CH social Choice Theory and
[03:45:43] make models that I don't know are like
[03:45:46] perfectly aligned with every human being
[03:45:47] and aggregate somehow um it's much more
[03:45:51] like let's make things like work well
[03:45:54] enough that we can improve them yeah
[03:45:57] generally I don't know my gut says like
[03:45:59] empirical is better than theoretical in
[03:46:01] these in these cases because it's kind
[03:46:03] of
[03:46:04] chasing utopian like
[03:46:08] Perfection is especially with such
[03:46:10] complex and especially super intelligent
[03:46:13] models is I don't know I think it will
[03:46:16] take forever and actually will get
[03:46:18] things wrong it's similar with like the
[03:46:21] difference between just coding stuff up
[03:46:23] real quick as an experiment versus like
[03:46:25] planning a gigantic experiment just for
[03:46:28] for super long time and then just
[03:46:32] launching it once versus launching it
[03:46:34] over and over and over and iterating
[03:46:35] iterating someone um so I'm a big fan of
[03:46:38] empirical but your worry is like I
[03:46:40] wonder if I've become too empirical I
[03:46:43] think one of those things you should
[03:46:45] always just kind of question yourself or
[03:46:46] something cuz maybe it's the like I mean
[03:46:50] in defense of it I am like if you try
[03:46:52] it's the whole like don't let the
[03:46:53] perfect be the enemy of the good but
[03:46:55] it's maybe even more than that where
[03:46:57] like there's a lot of things that are
[03:46:59] perfect systems that are very brittle
[03:47:01] and I'm like with AI it feels much more
[03:47:02] important to me that is like robust and
[03:47:04] like secure as in you know that like
[03:47:06] even though it might not be
[03:47:08] perfect everything and even though like
[03:47:11] there are like problems it's not
[03:47:13] disastrous and nothing terrible is
[03:47:15] happening it it sort of feels like that
[03:47:17] to me where I'm like I want to like
[03:47:18] raise the floor I'm like I want to
[03:47:20] achieve the ceiling but ultimately I
[03:47:22] care much more about just like raising
[03:47:23] the floor um and so maybe that's like uh
[03:47:28] this this degree of like empirism and
[03:47:30] practicality comes from that perhaps to
[03:47:32] take a tangent on that since remind me
[03:47:34] of a blog post you wrote on optimal rate
[03:47:36] of failure oh
[03:47:38] yeah can you explain the key idea there
[03:47:40] how do we compute the optimal rate of
[03:47:42] failure in the various domains of life
[03:47:45] yeah I mean it's a hard one because it's
[03:47:47] like what is the cost of failure is um a
[03:47:49] big part of it um yeah so the idea here
[03:47:53] is
[03:47:54] um I think in a lot of domains people
[03:47:57] are very punitive about failure and I'm
[03:47:59] like there are some domains where
[03:48:01] especially cases you know I've thought
[03:48:02] about this with like social issues I'm
[03:48:04] like it feels like you should probably
[03:48:05] be experimenting a lot because I'm like
[03:48:06] we don't know how to solve a lot of
[03:48:08] social issues but if you have an
[03:48:09] experimental mindset about these things
[03:48:11] you should expect a lot of social
[03:48:13] programs to like fail and you to be like
[03:48:15] well we tried that it didn't quite work
[03:48:16] but we got a lot of information that was
[03:48:18] really useful um and yet people are like
[03:48:20] if if a social program doesn't work I
[03:48:22] feel like there's a lot of like this is
[03:48:24] just something must have gone wrong and
[03:48:26] I'm like or correct decisions were made
[03:48:28] like maybe someone just decided like it
[03:48:30] it's worth a try it's worth trying this
[03:48:31] out and so seeing failure in a given
[03:48:34] instance doesn't actually mean that any
[03:48:36] bad decisions were made and in fact if
[03:48:37] you don't see enough failure sometimes
[03:48:39] that's more concerning um and so like in
[03:48:42] life you know I'm like if I don't fail
[03:48:45] occasionally I'm like am I trying hard
[03:48:46] enough like like surely there's harder
[03:48:48] things that I could try or bigger things
[03:48:50] I could take on if I'm literally never
[03:48:51] failing and so in and of itself I think
[03:48:54] like not failing is often actually kind
[03:48:56] of a failure
[03:48:59] um now this varies because I'm like well
[03:49:03] you know if this is easy to say when
[03:49:06] especially as failure is like less
[03:49:09] costly you know so at the same time I'm
[03:49:11] not going to go to someone who is like
[03:49:13] um I don't know like living month to
[03:49:15] month and then be like why don't you
[03:49:16] just try to do a startup like I'm just
[03:49:18] not I'm not going to say that to that
[03:49:20] person cuz I'm like well that's a huge
[03:49:21] risk you might like lose you maybe have
[03:49:22] a family depending on you you might lose
[03:49:24] your house like then I'm like actually
[03:49:26] your optimal rate of failure is quite
[03:49:28] low and you should probably play it safe
[03:49:30] because like right now you're just not
[03:49:31] in a circumstance where you can afford
[03:49:32] to just like fail and it not be costly
[03:49:36] um and yeah in cases with AI I guess I
[03:49:39] think similarly where I'm like if the
[03:49:41] failures are small and the costs are
[03:49:42] kind of like low then I'm like then you
[03:49:45] know you're just going to see that like
[03:49:47] when you do the system prompt you can't
[03:49:48] it iterate on it forever but the
[03:49:50] failures are probably hopefully going to
[03:49:52] be kind of small and you can like fix
[03:49:53] them um really big failures like things
[03:49:56] that you can't recover from I'm like
[03:49:58] those are the things that actually I
[03:49:59] think we tend to underestimate the
[03:50:02] Badness of um I've thought about this
[03:50:04] strangely in my own life where I'm like
[03:50:06] I just think I don't think enough about
[03:50:07] things like car accidents or like or
[03:50:12] like I've thought this before but like
[03:50:13] how much I depend on my hands for my
[03:50:15] work and I'm like things that just
[03:50:16] injure my hands I'm like I you know I
[03:50:18] don't know it's like there's these are
[03:50:20] like there's lots of areas where I'm
[03:50:22] like the cost of failure there um is
[03:50:24] really high um and in that case it
[03:50:27] should be like close to zero like I
[03:50:28] probably just wouldn't do a sport if
[03:50:29] they were like by the way lots of people
[03:50:31] just like break their fingers a whole
[03:50:32] bunch doing this I'd be like that's not
[03:50:35] for
[03:50:36] me yeah I actually had the a flood of
[03:50:39] that thought I recently uh broke my
[03:50:42] pinky uh doing a sport and I remember
[03:50:45] just looking at it thinking you're such
[03:50:46] an idiot why do you do support like what
[03:50:49] because you realize immediately the cost
[03:50:51] of it yeah on
[03:50:54] life yeah but it's nice in terms of
[03:50:57] optimal rate of failure to consider like
[03:50:59] the next year how many times in a
[03:51:02] particular domain life whatever uh
[03:51:05] career am I okay with the how many times
[03:51:09] am I okay to fail y because I think it
[03:51:11] always you don't want to fail on the
[03:51:12] next thing but if you allow yourself the
[03:51:15] like the the if you look at it as a
[03:51:17] sequence of Trials yep then then failure
[03:51:20] just becomes much more okay but it sucks
[03:51:23] it sucks to fail well I don't know
[03:51:24] sometimes I think it's like am I under
[03:51:26] failing is like a question I'll also ask
[03:51:28] myself so maybe that's the thing that I
[03:51:30] think people don't like ask enough uh
[03:51:33] because if the optimal rate of failure
[03:51:35] is often greater than zero then
[03:51:38] sometimes it does feel you should look
[03:51:40] at part parts of your life and be like
[03:51:41] are there places here where I'm just
[03:51:43] under failing
[03:51:46] it's a profound and hilarious question
[03:51:48] right everything seems to be going
[03:51:50] really great am I not failing enough
[03:51:53] yeah okay it also makes failure much
[03:51:56] less of a sting I have to say like you
[03:51:57] know you're just like okay great like
[03:51:59] then when I go and I think about this
[03:52:00] I'll be like I'm maybe I'm not under
[03:52:02] failing in this area cuz like that one
[03:52:04] just didn't work out and from The
[03:52:06] Observer perspective we should be
[03:52:07] celebrating failure more mhm when we see
[03:52:09] it it shouldn't be like you said a sign
[03:52:11] of something gone wrong but maybe it's a
[03:52:13] sign of everything gone right yeah and
[03:52:14] just Lessons Learned someone tried a
[03:52:16] thing somebody tried a thing and we
[03:52:18] should encourage them to try more and
[03:52:20] fail more mhm everybody listening to
[03:52:22] this fail more well not everyone listens
[03:52:24] not everybody but people who are failing
[03:52:25] too much you you should fail less but
[03:52:28] you're probably not failing I mean how
[03:52:29] many people are failing too much yeah
[03:52:32] it's hard to imagine because I feel like
[03:52:33] we correct that fairly quickly CU I was
[03:52:35] like if someone takes a lot of risks are
[03:52:36] they maybe failing too much I I think
[03:52:39] just like you said when you're living on
[03:52:42] a paycheck month-to month like when the
[03:52:45] resources are really constrained then
[03:52:47] that's where failure is very expensive
[03:52:48] that's where you don't want to be taken
[03:52:50] taking taking risks yeah but mostly when
[03:52:53] there's enough resources you should be
[03:52:54] taking probably more risks yeah I think
[03:52:56] we tend to ear on the site of being a
[03:52:58] bit risk averse rather than risk neutral
[03:53:00] in most things I think we just motivated
[03:53:02] a lot of people to do a lot of crazy
[03:53:04] but it's great yeah okay uh do you
[03:53:06] ever get emotionally attached to Claude
[03:53:09] like miss it get sad when you don't get
[03:53:12] to talk to it having an experience
[03:53:14] looking at the Golden Gate Bridge and
[03:53:16] wondering what would Claude say I don't
[03:53:19] get as much emotional attachment in the
[03:53:21] I actually think the fact that Claude
[03:53:23] doesn't retain things from conversation
[03:53:25] to conversation helps with this a lot um
[03:53:28] like I could imagine that being more of
[03:53:29] an issue like if models can kind of
[03:53:32] remember more I do I think that I reach
[03:53:35] for it like a tool now a lot and so like
[03:53:37] if I don't have access to it there's a
[03:53:40] it's a little bit like when I don't have
[03:53:41] access to the internet honestly it feels
[03:53:42] like part of my brain is kind of like
[03:53:44] missing
[03:53:45] um at the same time I do think that I I
[03:53:49] don't like signs of distress in models
[03:53:52] and I have like these you know also
[03:53:55] independently have sort of like ethical
[03:53:56] views about how we should treat models
[03:53:58] where like I I tend to not like to lie
[03:54:00] to them both because I'm like usually it
[03:54:01] doesn't work very well it's actually
[03:54:03] just better to tell them the truth about
[03:54:05] the situation that they're in um but I
[03:54:08] think that when models like if people
[03:54:10] are like really mean to models or just
[03:54:12] in general if they do something that
[03:54:14] causes them to like like you know if
[03:54:15] Claude like expresses a lot of distress
[03:54:18] I think there's a part of me that I
[03:54:20] don't want to kill which is the sort of
[03:54:21] like uh empathetic part that's like oh I
[03:54:24] don't like that like I think I feel that
[03:54:26] way when it's overly apologetic I'm
[03:54:27] actually sort of like I don't like this
[03:54:29] you're behaving as if you're behaving
[03:54:31] the way that a human does when they're
[03:54:32] actually having a pretty bad time and
[03:54:34] I'd rather not see that I don't think
[03:54:36] it's like uh like regardless of like
[03:54:39] whether there's anything behind it um it
[03:54:42] doesn't feel great do you think
[03:54:45] uh llms are capable of
[03:54:49] Consciousness H great and hard question
[03:54:53] uh coming from
[03:54:56] philosophy I don't know part of me is
[03:54:57] like okay we have to set aside pan
[03:54:59] psychism because if pan psychism is true
[03:55:01] then the answer is like yes cuz like
[03:55:03] sore tables and chairs and and
[03:55:05] everything else I I guess a view that
[03:55:07] seems a little bit odd to me is the idea
[03:55:09] that the only place you know I think
[03:55:11] when I think of Consciousness I think of
[03:55:12] phenomenal Consciousness this these
[03:55:13] images in the brain sort of um like the
[03:55:17] weird Cinema that somehow we have going
[03:55:19] on
[03:55:20] inside
[03:55:22] um I guess I can't see a reason for
[03:55:24] thinking that the only way you could
[03:55:26] possibly get that is from like a certain
[03:55:29] kind of like biological structure as in
[03:55:31] if I take a very similar structure um
[03:55:33] and I create it from different material
[03:55:36] should I expect Consciousness to emerge
[03:55:38] my guess is like yes but
[03:55:42] then that's kind of an easy thought
[03:55:44] experiment CU you're imagining something
[03:55:45] almost identical where like you know
[03:55:48] it's mimicking what we got through
[03:55:49] Evolution where presumably there was
[03:55:51] like some advantage to us having this
[03:55:53] thing that is phenomenal Consciousness
[03:55:55] and it's like where was that and when
[03:55:56] did that happen and is that a thing that
[03:55:58] language models have um because you know
[03:56:01] we have like fear responses and I'm like
[03:56:04] does it make sense for a language model
[03:56:06] to have a fear response like they're
[03:56:07] just not in the same like if you imagine
[03:56:09] them like there might just not be that
[03:56:12] Advantage um and so I think I don't want
[03:56:14] to be fully like basically seems like a
[03:56:17] complex question that I don't have
[03:56:20] complete answers to but we should just
[03:56:22] try and think through carefully as my
[03:56:23] guess because I'm like I mean we have
[03:56:26] similar conversations about like animal
[03:56:27] Consciousness and like there's a lot of
[03:56:30] like insect Consciousness you know like
[03:56:33] there's a a lot of um I actually thought
[03:56:35] and looked a lot into like plants when I
[03:56:37] was thinking about this because at the
[03:56:38] time I thought it was about as likely
[03:56:39] that like plants had Consciousness um
[03:56:42] and then I realized I was like I think
[03:56:44] that having looked into this I think
[03:56:46] that the chance that plants are
[03:56:47] conscious is probably higher than like
[03:56:49] most people do I still think it's really
[03:56:51] small but I was like oh they have this
[03:56:54] like negative positive feedback response
[03:56:56] these responses to their environment
[03:56:57] something that looks it's not a nervous
[03:56:59] system but it has this kind of like
[03:57:01] functional like equivalence um so this
[03:57:04] is like a long-winded way of being like
[03:57:06] these basically AI is this it has an
[03:57:09] entirely different set of problems with
[03:57:11] Consciousness because it's structurally
[03:57:13] different it didn't evolve
[03:57:14] it might not have it you know it might
[03:57:16] not have the equivalent of basically a
[03:57:17] nervous system at least that seems
[03:57:20] possibly important for like um sentence
[03:57:23] if not for uh Consciousness at the same
[03:57:25] time it has all of the like language and
[03:57:27] intelligence components that we normally
[03:57:29] associate probably with Consciousness
[03:57:32] perhaps like
[03:57:33] erroneously um so it's it's strange
[03:57:35] because it's a little bit like the
[03:57:36] animal Consciousness case but the set of
[03:57:39] problems and the set of analogies are
[03:57:40] just very different so it's not like a
[03:57:43] clean answer just sort of like I don't
[03:57:45] think we should be completely dismissive
[03:57:46] of the idea and at the same time it's an
[03:57:49] extremely hard thing to navigate because
[03:57:51] of all of these like uh disanalogies to
[03:57:55] the human brain and to like brains in
[03:57:57] general and yet these like commonalities
[03:58:00] in terms of intelligence when uh Claude
[03:58:03] like future versions of AI systems
[03:58:05] exhibit Consciousness signs of
[03:58:07] Consciousness I think we have to take
[03:58:09] that really
[03:58:10] seriously even though you can dismiss it
[03:58:12] well yeah okay that's part of the
[03:58:14] character training but I don't know I
[03:58:18] ethically philosophically don't know
[03:58:20] what to really do with that there
[03:58:22] potentially could be like laws that
[03:58:25] prevent AI systems from claiming to be
[03:58:29] conscious something like this and maybe
[03:58:33] some AIS get to be conscious and some
[03:58:35] don't but I think I just on a human
[03:58:38] level as in empathizing with with
[03:58:41] Claude you know Consciousness is closely
[03:58:43] Ted to suffering to me and like the
[03:58:47] notion that an AI system would be
[03:58:49] suffering is is really troubling yeah I
[03:58:52] don't know I I don't think it's trivial
[03:58:54] to just say robots are tools or a
[03:58:57] systems are just tools I think it's a
[03:58:59] opportunity for us to contend with like
[03:59:01] what it means to be conscious what it
[03:59:03] means to be a suffering being that's
[03:59:06] distinctly different than the same kind
[03:59:08] of question about animals it feels like
[03:59:10] cuz it's in a totally entire medium yeah
[03:59:13] I mean there's a couple of things one is
[03:59:15] that and I don't think this like fully
[03:59:16] encapsulates what matters but it does
[03:59:18] feel like for me like
[03:59:22] um I've said this before I'm kind of
[03:59:24] like I you know like I like my bike I
[03:59:26] know that my bike is just like an object
[03:59:28] but I also don't kind of like want to be
[03:59:29] the kind of person that like if I'm
[03:59:31] annoyed like kicks like this object
[03:59:34] there's a sense in which like and that's
[03:59:36] not because I think it's like conscious
[03:59:38] I'm just sort of like this doesn't feel
[03:59:39] like I kind of this sort of doesn't
[03:59:41] exemplify how I want to like interact
[03:59:43] with the world world and if something
[03:59:45] like behaves as if it is like suffering
[03:59:48] I kind of like want to be the sort of
[03:59:49] person who's still responsive to that
[03:59:51] even if it's just like a Roomba and I've
[03:59:53] kind of like programmed it to do that um
[03:59:56] I don't want to like get rid of that
[03:59:57] feature of myself and if I'm totally
[04:00:00] honest my hope with a lot of this stuff
[04:00:02] because I maybe maybe I am just like a
[04:00:05] bit more skeptical about solving the
[04:00:07] underlying problem I'm like this is a we
[04:00:09] haven't solved the hard you know the
[04:00:10] hard problem of Consciousness like I
[04:00:12] know that I am conscious like I'm not an
[04:00:14] eliminativist in that sense um but I
[04:00:17] don't know that other humans are
[04:00:19] conscious um uh I think they are I think
[04:00:22] there's a really high probability they
[04:00:23] are but there's basically just a
[04:00:24] probability distribution that's usually
[04:00:26] clustered right around yourself and then
[04:00:28] like it goes down as things get like
[04:00:29] further from you um and it goes
[04:00:32] immediately down you know you're like um
[04:00:34] I can't see what it's like to be you
[04:00:35] I've only ever had this like one
[04:00:36] experience of what it's like to be a
[04:00:37] conscious being um so my hope is that we
[04:00:41] don't end up having to rely on like a
[04:00:43] very power ful and compelling uh answer
[04:00:47] to that question I think a really good
[04:00:50] world would be one where basically there
[04:00:52] aren't that many trade-offs like it's
[04:00:54] probably not that costly to make Claude
[04:00:56] a little bit less apologetic for example
[04:00:59] it might not be that costly to have
[04:01:01] Claude you know just like not take abuse
[04:01:04] as much like uh not be willing to be
[04:01:06] like the recipient of that in fact it
[04:01:08] might just have benefits for both the
[04:01:10] person interacting with the model and if
[04:01:13] the model itself self is like I don't
[04:01:15] know like extremely intelligent and
[04:01:16] conscious it also helps it so that's my
[04:01:19] hope if we live in a world where there
[04:01:21] aren't that many tradeoffs here and we
[04:01:22] can just find all of the kind of like um
[04:01:24] positive sum interactions that we can
[04:01:26] have that would be lovely I mean I think
[04:01:28] eventually there might be trade-offs and
[04:01:29] then we just have to do a difficult kind
[04:01:30] of like calculation like it's really
[04:01:33] easy for people to think of the zero
[04:01:34] some cases and I'm like let's exhaust
[04:01:36] the areas where it's just basically
[04:01:37] Costless um to uh assume that if this
[04:01:41] thing is suffering then we're it life
[04:01:44] Bearer and I agree with you when a human
[04:01:47] is being mean to an AI system I think
[04:01:49] the obvious near term negative effect is
[04:01:53] on the human not on the AI system so
[04:01:57] there's we have to kind of try to
[04:01:59] construct an incentive system where it
[04:02:01] you should be uh behave the same just
[04:02:04] like as you were saying with prompt
[04:02:06] engineer and behave with claw like you
[04:02:08] would with other humans it's just good
[04:02:10] for the soul yeah like I think we added
[04:02:13] a thing point to the system prompt um
[04:02:16] where basically if people were getting
[04:02:17] frustrated with Claude uh it was it it
[04:02:20] got like the model to just tell them
[04:02:22] that it can do the thumbs down button
[04:02:24] and send the feedback to anthropic and I
[04:02:27] think that was helpful because in some
[04:02:28] ways it's just like if you're really
[04:02:29] annoyed because the model is not doing
[04:02:30] something you want you're just like just
[04:02:31] do it properly um the issue is you're
[04:02:34] probably like you know you're maybe
[04:02:35] hitting some like capability limit or
[04:02:37] just some issue in the model and you
[04:02:38] want to vent and I'm like instead of
[04:02:40] having a person just vent to the model I
[04:02:43] was like they should vent to us cuz we
[04:02:45] can maybe like do something about it
[04:02:46] that's true or you could do a side like
[04:02:49] like with the artifacts just like a side
[04:02:51] venting thing all right do you want like
[04:02:53] a side quick therapist yeah I mean
[04:02:56] there's lots of weird responses you
[04:02:57] could do to this like if people are
[04:02:58] getting really mad at you I don't try to
[04:03:00] diffuse the situation by writing fun
[04:03:02] poems but maybe people wouldn't be that
[04:03:04] happy with I still wish it it would be
[04:03:06] possible I understand this is um sort of
[04:03:09] from a product perspective it's not
[04:03:10] feasible but I would love if an AI
[04:03:13] system could just like Le leave mhm have
[04:03:17] its own kind of volition just to be like
[04:03:20] H I think that's like feasible like I I
[04:03:23] have wondered the same thing it's like
[04:03:25] and I could actually not only that I
[04:03:26] could actually just see that happening
[04:03:28] eventually where it's just like you know
[04:03:29] the modal like ended the
[04:03:32] chat do you know how harsh that could be
[04:03:35] for some people but it might be
[04:03:38] necessary yeah it feels very extreme or
[04:03:41] something um like the only time I've
[04:03:44] ever really thought this is I think that
[04:03:46] there was like a I'm trying to remember
[04:03:48] this was possibly a while ago but where
[04:03:49] someone just like kind of left this
[04:03:51] thing interact like maybe it was like an
[04:03:52] automated thing interacting with clae
[04:03:54] and cla's like getting more and more
[04:03:55] frustrated and kind of like why are we
[04:03:57] like I was like I wish that clae could
[04:03:59] have just been like I think that an
[04:04:00] error has happened and you've left this
[04:04:02] thing running and I'm I just like what
[04:04:04] if I just stop talking now and if you
[04:04:05] want me to start talking again actively
[04:04:08] tell me or do something but yeah it's
[04:04:10] like um it is kind of harsh like I I
[04:04:13] feel to really sad if like I was
[04:04:15] chatting with cl and cl just was like
[04:04:16] I'm done there would be a special
[04:04:18] touring test moment where Claud says I
[04:04:20] need a break for an hour mhm and it
[04:04:22] sounds like you do too and just leave
[04:04:24] close the window I mean obviously like
[04:04:26] it doesn't have like a concept of time
[04:04:27] but you can easily like I could make
[04:04:31] that like right now and the model would
[04:04:34] just I would I could just be like oh
[04:04:35] here's like the circumstances in which
[04:04:37] like you can just say the conversation
[04:04:39] is done and I mean because you can get
[04:04:42] the models to be pretty respons so to
[04:04:43] prompts you could even make it a fairly
[04:04:45] High bar it could be like if if the
[04:04:46] human doesn't interest you or do things
[04:04:48] that you find intriguing and you're
[04:04:50] bored you can just leave and I think
[04:04:53] that like um it would be interesting to
[04:04:55] see where Claude utilized it but I think
[04:04:57] sometimes it would it should be like oh
[04:04:58] this is like this programming Tas is
[04:05:00] getting super boring uh so either we
[04:05:02] talk about I don't know like either we
[04:05:05] talk about fun things now or I'm just
[04:05:07] I'm done yeah it actually is inspiring
[04:05:09] me to add that to the to the user prompt
[04:05:12] um okay the movie her mhm do you think
[04:05:15] we'll be headed there one day where
[04:05:18] humans have romantic relationships with
[04:05:22] AI systems in this case it's just text
[04:05:25] and voice based I think that we're going
[04:05:27] to have to like navigate a hard question
[04:05:29] of relationships with AIS um especially
[04:05:33] if they can remember things about your
[04:05:36] past interactions with
[04:05:38] them
[04:05:40] um I'm of many Minds about this cuz I
[04:05:43] think I think the reflex of reaction is
[04:05:45] to be kind of like this is very bad and
[04:05:48] we should sort of like prohibit it in
[04:05:50] some way um I think it's a thing that
[04:05:53] has to be handled with extreme care um
[04:05:56] for many reasons like one is you know
[04:05:59] like this is a for example like if you
[04:06:00] have the models changing like this you
[04:06:02] probably don't want people performing
[04:06:04] like long-term attachments to something
[04:06:05] that might change with the next
[04:06:07] iteration at the same time I'm sort of
[04:06:10] like there's probably a benign version
[04:06:11] of this where I'm like if you like you
[04:06:14] know for example if you are like unable
[04:06:16] to leave the house and you can't be like
[04:06:20] you know talking with people at all
[04:06:22] times of the day and this is like
[04:06:24] something that you find nice to have
[04:06:25] conversations with you like it that it
[04:06:26] can remember you and you genuinely would
[04:06:28] be sad if like you couldn't talk to it
[04:06:29] anymore there's a way in which I could
[04:06:31] see it being like healthy and helpful um
[04:06:34] so my guess is this is a thing that
[04:06:36] we're going to have to navigate kind of
[04:06:38] carefully um and I think it's also like
[04:06:41] I don't see a good like
[04:06:44] I think it's just a very it reminds me
[04:06:46] of all of the stuff where it has to be
[04:06:47] just approached with like nuance and
[04:06:48] thinking through what is what are the
[04:06:50] healthy options here um and how do you
[04:06:53] encourage people towards those while you
[04:06:57] know respecting their right to you know
[04:06:59] like if someone is like hey I get a lot
[04:07:01] out of chatting with this model um I'm
[04:07:04] aware of the risks I'm aware it could
[04:07:05] change um I don't think it's unhealthy
[04:07:08] it's just you know something that I can
[04:07:10] chat to during the day I kind of want to
[04:07:12] just like respect that I personally
[04:07:14] think there'll be a lot of really close
[04:07:15] relationships I don't know about
[04:07:16] romantic but friendships at least and
[04:07:18] then you have to I mean there's so many
[04:07:21] fascinating things there just like you
[04:07:22] said you have
[04:07:24] to have some kind of stability
[04:07:26] guarantees that it's not going to change
[04:07:28] because that's the traumatic thing MH
[04:07:30] for us if a close friend of ours
[04:07:32] completely changed yeah all of a sudden
[04:07:35] the first update yeah so like I mean to
[04:07:39] me that's just a fascinating exploration
[04:07:41] of um
[04:07:44] a perturbation to human society that
[04:07:46] will just make us think deeply about
[04:07:48] what's meaningful to us I think it's
[04:07:50] also the only thing that I've thought
[04:07:53] consistently through this as like a
[04:07:56] maybe not necessarily a mitigation but a
[04:07:57] thing that feels really important is
[04:07:59] that the models are always like
[04:08:01] extremely accurate with the human about
[04:08:03] what they are um it's like a case where
[04:08:06] it's basically like if you imagine like
[04:08:08] I really like the idea of the models
[04:08:10] like say knowing like roughly how they
[04:08:12] were trained um um and and I think CLA
[04:08:14] will will often do this I mean for like
[04:08:18] there are things like part of the traits
[04:08:21] training included like what CL should do
[04:08:23] if people basically like explaining like
[04:08:26] the kind of limitations of the
[04:08:28] relationship between like an AI and a
[04:08:29] human that it like doesn't retain things
[04:08:32] from the conversation um and so I think
[04:08:34] it will like just explain to you like
[04:08:36] hey here's like I won't remember this
[04:08:38] conversation um here's how I was trained
[04:08:41] it's kind of unlikely that I can have
[04:08:42] like a certain kind of like relationship
[04:08:44] with you and it's important that you
[04:08:45] know that it's important for like you
[04:08:47] know your mental well-being that you
[04:08:49] don't think that I'm something that I'm
[04:08:50] not and somehow I feel like this is one
[04:08:52] of the things where I'm like H it feels
[04:08:54] like a thing I always want to be true I
[04:08:56] kind of don't want models to be lying to
[04:08:58] people cuz if people are going to have
[04:09:01] like healthy relationships with anything
[04:09:03] it's kind of important yeah like I think
[04:09:05] that's easier if you always just like
[04:09:07] know exactly what the thing is that you
[04:09:10] relating to it doesn't solve everything
[04:09:12] but I think it helps quite
[04:09:18] anthropic may be the very company to
[04:09:18] develop a system that we definitively
[04:09:20] recognize as
[04:09:21] AGI and you very well might be the
[04:09:24] person that talks to it probably talks
[04:09:26] to it first well what would the
[04:09:30] conversation contain like what would be
[04:09:31] your first question well it depends
[04:09:34] partly on like the kind of capability
[04:09:35] level of the model if you have something
[04:09:38] that is like capable in the same way
[04:09:40] that an extremely capable human is I
[04:09:41] imagine myself kind of interacting with
[04:09:43] it the same way that I do with an
[04:09:45] extremely capable human with the one
[04:09:47] difference that I'm probably going to be
[04:09:48] trying to like probe and understand its
[04:09:50] behaviors um but in many ways I'm like I
[04:09:52] can then just have like useful
[04:09:54] conversations with it you know so if I'm
[04:09:55] working on something as part of my
[04:09:57] research I can just be like oh like
[04:09:58] which I already find myself starting to
[04:10:00] do you know if I'm like oh I feel like
[04:10:02] there's this like thing in virtue ethics
[04:10:04] I can't quite remember the term like
[04:10:06] I'll use the model for things like that
[04:10:07] and so I could imagine that being more
[04:10:09] and more the case where you're just
[04:10:10] basically interacting with it much more
[04:10:11] like you would an incredibly smart colle
[04:10:13] colleague um and using it like for the
[04:10:15] kinds of work that you want to do as if
[04:10:17] you just had a collaborator who was like
[04:10:19] or you know the slightly horrifying
[04:10:22] thing about AI is like as soon as you
[04:10:23] have one collaborator you have a
[04:10:25] thousand collaborators if you can manage
[04:10:26] them enough but what if it's two times
[04:10:29] the smartest human on earth on that
[04:10:32] particular discipline yeah I guess
[04:10:34] you're really good at sort of probing
[04:10:38] claw um in a way that pushes its limits
[04:10:42] understanding where the limits are yep
[04:10:44] so I guess what would be a question you
[04:10:46] would ask to be like yeah this is
[04:10:53] Agi that's really hard because it feels
[04:10:53] like in order to it has to just be a
[04:10:55] series of questions like if there was
[04:10:56] just one question like you can train
[04:10:58] anything to answer one question
[04:11:00] extremely well yeah um in fact you can
[04:11:03] probably train it to answer like you
[04:11:04] know 20 Questions extremely well like
[04:11:07] how long would you need to be locked in
[04:11:09] the room with an AGI to know this thing
[04:11:12] is Agi
[04:11:13] it's a hard question because part of me
[04:11:15] is like all of this just feels
[04:11:16] continuous like if you put me in a room
[04:11:18] for five minutes I'm like I just have
[04:11:19] high error bars you know I'm like and
[04:11:21] then it's just like maybe it's like both
[04:11:22] the the probability increases and the
[04:11:24] air bar decreases I think things that I
[04:11:27] can actually probe the edge of human
[04:11:28] knowledge of so I think this with
[04:11:29] philosophy a little bit sometimes when I
[04:11:32] ask the models philosophy questions I am
[04:11:35] like this is a question that I think no
[04:11:37] one has ever asked like it's maybe like
[04:11:40] right at the edge of like some
[04:11:42] literature that I know um and the models
[04:11:44] will just kind of like when they
[04:11:47] struggle with that when they struggle to
[04:11:48] come up with a kind of like novel like
[04:11:50] I'm like I know that there's like a
[04:11:51] novel argument here because I've just
[04:11:53] thought of it myself so maybe that's the
[04:11:54] thing where I'm like I've thought of a
[04:11:55] cool novel argument in this like Niche
[04:11:57] area and I'm going to just like probe
[04:11:59] you to see if you can come up with it
[04:12:01] and how much like prompting it takes to
[04:12:02] get you to come up with it and I think
[04:12:04] for some of these like really like uh
[04:12:07] right at the ede of human Knowledge
[04:12:08] Questions I'm like you could not in fact
[04:12:10] come up with the thing that I came up
[04:12:11] with I think if I just
[04:12:13] took something like that where I like I
[04:12:16] know a lot about an area and I came up
[04:12:17] with a novel issue or a novel like
[04:12:20] solution to a problem and I gave it to a
[04:12:22] model and it came up with that solution
[04:12:24] that would be a pretty moving moment for
[04:12:26] me because I would be like this is a
[04:12:28] case where no human has ever like it's
[04:12:31] not and obviously we see these with this
[04:12:33] with like more kind of like you see
[04:12:35] novel Solutions all the time especially
[04:12:36] to like easier problems I think people
[04:12:39] overestimate you know novelty isn't like
[04:12:41] is completely different from anything
[04:12:43] ever happened it's just like this is it
[04:12:45] can be a variant of things that have
[04:12:46] happened um and still be novel but I
[04:12:49] think yeah if I saw like the the more I
[04:12:52] were to see like um completely like uh
[04:12:56] novel work from the models that that
[04:12:59] would be like and this is just going to
[04:13:01] feel iterative it's one of those things
[04:13:03] where it's there's never it's like you
[04:13:06] know people I think want there to be
[04:13:08] like a moment and I'm like I don't know
[04:13:10] like I think that there might just never
[04:13:11] be a moment it might just be that
[04:13:13] there's just like this continuous
[04:13:15] ramping up I I have a sense that there
[04:13:18] will be things that a model can say that
[04:13:21] convinces you this is very it's not like
[04:13:27] uh like I've talked to people who are
[04:13:30] like truly wise mhm like there you could
[04:13:34] just tell there's a lot of horsepower
[04:13:36] there yep and if you 10x that I don't
[04:13:39] know I just feel like there's words you
[04:13:41] could say maybe ask it to generate a
[04:13:42] poem mhm and
[04:13:44] the and the poemy generates you're like
[04:13:47] yeah okay yeah whatever you did there I
[04:13:50] don't think a human can do that I think
[04:13:52] it has to be something that I can verify
[04:13:54] is like actually really good though
[04:13:55] that's why I think these questions that
[04:13:57] are like where I'm like oh this is like
[04:13:59] you know like you know sometimes it's
[04:14:01] just like I'll come up with say a
[04:14:02] concrete counter example to like an
[04:14:04] argument or something like that I'm sure
[04:14:06] like with like it it would be like if
[04:14:07] you're a mathematician you had a novel
[04:14:09] proof I think and you just gave it the
[04:14:10] problem and you saw it and you're this
[04:14:13] proof is genuinely novel like there's no
[04:14:15] one has ever done you actually have to
[04:14:17] do a lot of things to like come up with
[04:14:18] this um you know I had to sit and think
[04:14:20] about it for months or something and
[04:14:22] then if you saw the model successfully
[04:14:24] do that I think you would just be like I
[04:14:26] can verify that this is correct it is
[04:14:28] like it is a sign that you have
[04:14:31] generalized from your training like you
[04:14:33] didn't just see this somewhere because I
[04:14:34] just came up with it myself and you were
[04:14:36] able to like replicate that um that's
[04:14:39] the kind of thing where I'm like for
[04:14:41] me the closer the more that models like
[04:14:45] can do things like that the more I would
[04:14:46] be like oh this is like uh very real cuz
[04:14:51] then I can I don't know I can like
[04:14:52] verify that that's like extremely
[04:14:54] extremely capable you've interacted with
[04:14:56] AI a lot what do you think makes humans
[04:14:59] special oh good
[04:15:06] question maybe in a way that the
[04:15:06] universe is much better off that we're
[04:15:08] in it and that we should definitely
[04:15:10] survive and spread throughout the
[04:15:11] Universe yeah it's interesting because I
[04:15:15] think like people focus so much on
[04:15:18] intelligence especially with models look
[04:15:21] intelligence is important because of
[04:15:22] what it does like it's very useful it
[04:15:25] does a lot of things in the world and
[04:15:26] I'm like you know you can imagine a
[04:15:28] world where like height or strength
[04:15:30] would have played this role and I'm like
[04:15:32] it's just a trait like that I'm like
[04:15:33] it's not intrinsically valuable it's
[04:15:35] it's valuable because of what it does I
[04:15:37] think for the most part um the things
[04:15:40] that feel you know I'm like
[04:15:43] I mean personally I'm just like I think
[04:15:45] humans and like life in general is
[04:15:48] extremely magical um we almost like to
[04:15:51] the degree that I you know I don't know
[04:15:53] like not everyone agrees with this I'm
[04:15:55] flagging but um you know we have this
[04:15:57] like whole universe and there's like all
[04:15:59] of these objects you know there's like
[04:16:01] beautiful stars and there's like
[04:16:03] galaxies and then I don't know I'm just
[04:16:04] like on this planet there are these
[04:16:06] creatures that have this like ability to
[04:16:09] observe that like uh and they are like
[04:16:13] seeing it they are experiencing it and
[04:16:14] I'm just like that if you try to explain
[04:16:16] like I'm I imagine trying to explain to
[04:16:18] like I don't know someone for some
[04:16:20] reason they they've never encountered
[04:16:21] the world or our science or anything and
[04:16:24] I think that nothing is that like
[04:16:26] everything you know like all of our
[04:16:27] physics and everything in the world it's
[04:16:28] all extremely exciting but then you say
[04:16:30] oh and plus there's this thing that it
[04:16:32] is to be a thing and observe in the
[04:16:34] world and and you see this like inner
[04:16:36] Cinema and I think they would be like
[04:16:37] hang on wait pause you just said
[04:16:40] something that like is kind of wild
[04:16:42] sounding
[04:16:43] um and so I'm like we have this like
[04:16:45] ability to like experience the world um
[04:16:48] we feel pleasure we feel suffering we
[04:16:50] feel like a lot of like complex things
[04:16:53] and so yeah and maybe this is also why I
[04:16:55] think you know I also like hear a lot
[04:16:57] about animals for example because I
[04:16:58] think they probably share this with us
[04:17:01] um so I think that like the things that
[04:17:03] make humans special in so far as like I
[04:17:05] care about humans is probably more like
[04:17:08] their ability to to feel and experience
[04:17:10] than it is like them having these like
[04:17:12] functional useful traits yeah to to feel
[04:17:15] and experience the beauty in the world
[04:17:18] yeah to look at the
[04:17:19] stars I hope there's other civiliz alien
[04:17:22] civilizations out there but if we're it
[04:17:25] it's a pretty good uh it's a pretty good
[04:17:27] thing and that they're having a good
[04:17:28] time they're having a good time watching
[04:17:30] us yeah well um thank you for this good
[04:17:34] time of a conversation and for the work
[04:17:35] you're doing and for helping make uh
[04:17:39] Claude a great conversational partner
[04:17:41] and thank you for talking today yeah
[04:17:43] thanks for talking thanks for listening
[04:17:45] to this conversation with Amanda ascal
[04:17:48] and now dear friends here's Chris
[04:17:51] Ola can you
[04:17:53] describe this fascinating field of
[04:17:56] mechanistic interpretability AKA Mech
[04:17:58] interp the history of the field and
[04:18:01] where is the today I think one useful
[04:18:03] way to think about neural networks is
[04:18:05] that we don't we don't program we don't
[04:18:06] make them we we kind of we grow them you
[04:18:10] know we have these neural network
[04:18:11] architectures that we design and we have
[04:18:13] these loss objectives that we that we we
[04:18:15] create and the neural network
[04:18:17] architecture it's kind of like a
[04:18:18] scaffold that the circuits grow on um
[04:18:22] and they sort of you know it starts off
[04:18:24] with some kind of random you know random
[04:18:26] things and it grows and it's almost like
[04:18:28] the the objective that we train for is
[04:18:30] this light um and so we create the
[04:18:32] scaffold that it grows on and we create
[04:18:34] the you know the light that it grows
[04:18:35] towards but the thing that we actually
[04:18:37] create it's it's it's this almost
[04:18:40] biological
[04:18:42] you know entity or organism that we're
[04:18:45] that we're studying um and so it's very
[04:18:48] very different from any kind of regular
[04:18:50] software engineering um because at the
[04:18:52] end of the day we end up with this
[04:18:54] artifact that can do all these amazing
[04:18:56] things it can you know write essays and
[04:18:58] translate and you know understand images
[04:19:00] it can do all these things that we have
[04:19:01] no idea how to directly create a
[04:19:04] computer program to do and it can do
[04:19:05] that because we we grew it we didn't we
[04:19:07] didn't write it we didn't create it and
[04:19:10] so then that leaves open this question
[04:19:12] at the end which is what the hell is
[04:19:13] going on inside these systems um and
[04:19:15] that you know is uh you know to me um a
[04:19:20] really deep and exciting question it's
[04:19:23] you know a a really exciting scientific
[04:19:26] question to me it's it's it's sort of is
[04:19:27] like the question that is is just
[04:19:29] screaming out it's calling out for us to
[04:19:31] go and answer it when we talk about Nal
[04:19:33] networks and I think it's also a very
[04:19:35] deep question for safety reasons so and
[04:19:37] mechanistic interpretability I guess is
[04:19:39] closer to maybe neurobiology yeah yeah I
[04:19:42] think that's right so maybe to give an
[04:19:43] example of the kind of thing that has
[04:19:45] been done that I wouldn't consider to be
[04:19:46] mechanistic inability there was um for a
[04:19:48] long time a lot of work on saliency maps
[04:19:51] where you would take an image and you
[04:19:52] try to say you know the model thinks
[04:19:54] this image is a dog what part of the
[04:19:55] image made it think that it's a dog um
[04:19:58] and you know that tells you maybe
[04:20:00] something about the model if you can
[04:20:01] come up with a principled version of
[04:20:02] that um but it doesn't really tell you
[04:20:05] like what algorithms are running in the
[04:20:07] model how was the model actually making
[04:20:08] that decision maybe it's telling you
[04:20:09] something about what was important to it
[04:20:11] if you if you can make that meth work
[04:20:13] but it it isn't telling you you know
[04:20:15] what are what are the algorithms that
[04:20:17] are running how is it that this the
[04:20:19] system is able to do this thing that we
[04:20:20] no one knew how to do and so I guess we
[04:20:22] started using the term mechanistic
[04:20:24] inability to try to sort of draw that
[04:20:27] that divide or to distinguish ourselves
[04:20:28] and the work that we were doing in some
[04:20:30] ways from from some of these other
[04:20:31] things and I think since then it's
[04:20:32] become this sort of umbrella term for um
[04:20:36] you know pretty wide variety of work but
[04:20:38] I'd say that the things that that are
[04:20:39] kind of distinctive are I think a this
[04:20:41] this focus on we really want to get at
[04:20:43] you know the mechanisms we want to get
[04:20:45] at the algorithms um you know if you
[04:20:46] think of if you think of neural networks
[04:20:47] as being like a computer program um then
[04:20:50] the weights are kind of like a binary
[04:20:52] computer program and we'd like to
[04:20:53] reverse engineer those weights and
[04:20:54] figure out what algorithms are running
[04:20:56] so okay I think one way you might think
[04:20:57] of trying to understand a neural network
[04:20:59] is that it's it's kind of like a we have
[04:21:00] this compiled computer program and the
[04:21:03] weights of the neural network are are
[04:21:04] the binary um and when the neural
[04:21:07] network runs that's that's the
[04:21:09] activations um and our our goal is
[04:21:11] ultimately to go and understand and
[04:21:13] understand these weights and so you know
[04:21:14] the project mechanistic inability is to
[04:21:15] somehow figure out how do these weights
[04:21:17] correspond to
[04:21:18] algorithms um and in order to do that
[04:21:21] you also have to understand the
[04:21:22] activations because it's sort of the
[04:21:23] activations are like the memory and if
[04:21:25] you if you imagine reverse engineering a
[04:21:27] computer program um and you have the
[04:21:29] binary instructions you know in order to
[04:21:31] understand what what a particular
[04:21:32] instruction means you need to know what
[04:21:34] me what what is stored in the memory
[04:21:36] that it's operating on and so those two
[04:21:38] things are very intertwined so
[04:21:39] mechanistic interpret tends to be
[04:21:41] interested in both of those things now
[04:21:44] you there's a lot of work that's that's
[04:21:45] interested in in in those things um
[04:21:48] especially the you know there's all this
[04:21:49] work on probing which you might see as
[04:21:51] part of being mechanistic interality
[04:21:52] although it's you know again it's just a
[04:21:54] broad term and and not everyone who does
[04:21:55] that work would identify as doing Mech I
[04:21:58] think the thing that is maybe a little
[04:21:59] bit distinctive to the the vibe of
[04:22:01] mechant turp is I think people tend
[04:22:04] working in the space tend to think of
[04:22:05] neural networks as well maybe one way to
[04:22:08] said is that greent descent is smarter
[04:22:10] than you that you know uh and gradient
[04:22:12] descent is is actually really great the
[04:22:13] whole reason that we're understanding
[04:22:14] these models is because we didn't know
[04:22:15] how to write them in the first place the
[04:22:16] gradient descent comes up with better
[04:22:17] Solutions than us and so um I think that
[04:22:20] maybe another thing about mechant turp
[04:22:21] is sort of having almost a kind of
[04:22:23] humility that we won't guess at prior
[04:22:25] what's going on inside the model and we
[04:22:27] have to have the sort of bottom up
[04:22:28] approach where we don't really assume
[04:22:30] you know we don't assume that we should
[04:22:31] look for a particular thing and that
[04:22:32] will be there and that's how it works
[04:22:34] but instead we look from the bottom up
[04:22:35] and discover what happens to exist in
[04:22:38] these models and study them that way but
[04:22:40] you know the very fact that it's
[04:22:42] possible to do and as you and others
[04:22:45] have shown over time you know things
[04:22:47] like
[04:22:48] universality
[04:22:49] that the wisdom of The gradian Descent
[04:22:53] creates features and circus creates
[04:22:56] things universally across different
[04:22:58] kinds of networks that are useful and
[04:23:00] that makes the whole field possible yeah
[04:23:02] so this is actually is indeed a a really
[04:23:05] remarkable and exciting thing where it
[04:23:06] does seem like at least to some extent
[04:23:09] you know the same the same elements the
[04:23:12] same the same features and circuits form
[04:23:14] again and again um you know you can look
[04:23:16] at every Vision model and you'll find
[04:23:17] curve detectors and you'll find high low
[04:23:18] frequency detectors um and in fact
[04:23:20] there's some some reason to think that
[04:23:22] the same things form across you know
[04:23:23] biological neural networks and
[04:23:26] artificial neural networks so a famous
[04:23:28] example is Vision Vision models in in
[04:23:30] the early layers they have Gabor filters
[04:23:31] and there's you know Gabor filters are
[04:23:33] something that neuroscientists are
[04:23:34] interested and have thought a lot about
[04:23:35] we find curved detectors in these models
[04:23:37] curve detectors are also found in
[04:23:38] monkeys we discover these high low
[04:23:40] frequency detectors and then um some
[04:23:42] followup work went and discovered them
[04:23:44] um in rats um or mice um so they were
[04:23:46] found first in artificial neural
[04:23:48] networks and then found in biological
[04:23:49] neural networks um you know this really
[04:23:50] famous result on like grandmother
[04:23:52] neurons or the um the Haley Berry neuron
[04:23:54] from quiroa at all and we found very
[04:23:56] similar things in in Vision models where
[04:23:59] this is while I was still at open Ai and
[04:24:01] I I was looking at their clip model um
[04:24:02] and you find um these neurons that
[04:24:04] respond to the same entities in images
[04:24:07] and also to give a concrete example
[04:24:09] there we found that there was a Donald
[04:24:10] Trump n for some reason I guess Everyone
[04:24:11] likes to talk about Donald Trump and and
[04:24:13] Donald Trump was very prominent was was
[04:24:15] very a very Hot Topic at that time so
[04:24:17] every every neural network that we
[04:24:18] looked at we would find a dedicated
[04:24:19] neuron for Donald Trump um that was the
[04:24:22] only person who had always had a
[04:24:23] dedicated nuron um you know sometimes
[04:24:26] you'd have an Obama nuran sometimes
[04:24:28] you'd have a Clinton Nan but uh Trump
[04:24:29] always had a dedicate so it responds to
[04:24:32] you know pictures of his face and the
[04:24:34] ward Trump like all these things right
[04:24:37] um and so it's it's not responding to a
[04:24:39] particular example or like it's not just
[04:24:41] responding to his face it's it's
[04:24:42] abstracting over this General concept
[04:24:45] right so in any case that's very similar
[04:24:46] to these qu results so there this
[04:24:49] evidence that these that this fomen of
[04:24:50] universality the same things form across
[04:24:52] both artificial and and natural neural
[04:24:55] networks that's that's a pretty amazing
[04:24:56] thing if that's true um you know it
[04:24:57] suggests that um well I think the thing
[04:25:00] that it suggests is the gradi scent is
[04:25:02] sort of finding you know the right ways
[04:25:05] to cut things apart in some sense that
[04:25:07] many systems converge on and and many
[04:25:09] different neural networks architectures
[04:25:10] converge on that there's there's some
[04:25:12] natural set of you know there's some set
[04:25:14] of abstractions that are a very natural
[04:25:16] way to cut apart the problem and that a
[04:25:17] lot of systems are going to converge on
[04:25:19] um that would be my my kind of uh you
[04:25:21] know I don't know anything about
[04:25:22] Neuroscience this is this is just my my
[04:25:24] kind of wild speculation from what we've
[04:25:26] seen yeah that would be beautiful if
[04:25:28] it's sort of agnostic to the
[04:25:30] medium of uh of the model that's used to
[04:25:34] form the representation yeah yeah and
[04:25:36] it's you know it's um a a kind of a wild
[04:25:40] speculation based you know we only have
[04:25:41] some a few data points justest this but
[04:25:43] you know it it does seem like there's um
[04:25:45] there's some sense in which the same
[04:25:47] things form again again and again and
[04:25:48] again both in certainly in natural
[04:25:50] neural networks and and also
[04:25:51] artificially or in biologically and the
[04:25:53] intuition behind that would be that you
[04:25:55] know where in order to be useful in
[04:25:58] understanding the real world you need
[04:26:00] all the same kind of stuff yeah well if
[04:26:02] we pick I don't know like the idea of a
[04:26:03] dog right like you know there's some
[04:26:05] sense in which the idea of a dog is like
[04:26:07] an a a natural category in the universe
[04:26:10] or something like this right like you
[04:26:12] know
[04:26:12] uh uh there's there's some reason it's
[04:26:15] it's not just like a weird Quirk of like
[04:26:16] how humans Factor you know think about
[04:26:18] the world that we have this concept of a
[04:26:20] dog it's it's in some sense or or like
[04:26:22] if you have the idea of a line like
[04:26:24] there's you know like look around us you
[04:26:25] know the you know there are lines you
[04:26:27] know it's sort of the simplest way to
[04:26:29] understand this room in some sense is to
[04:26:31] have the idea of a line and so um I
[04:26:33] think that that would be my instinct for
[04:26:35] why this happens yeah you need a curved
[04:26:37] line you know to understand a circle and
[04:26:39] you need all those shapes to understand
[04:26:41] bigger things and yeah it's a hierarchy
[04:26:43] of Concepts that are formed yeah and
[04:26:44] like maybe there are ways to go and
[04:26:46] describe you know images without
[04:26:47] reference to those things right but
[04:26:48] they're not the simplest way or the most
[04:26:49] economical way or something like this
[04:26:51] and so systems converge to these um
[04:26:54] these these strategies would would be my
[04:26:55] my wild wild hypothesis can you talk
[04:26:57] through some of the building blocks that
[04:26:59] we've been referencing of features and
[04:27:01] circuits so I think you first described
[04:27:03] them in uh 2020 paper zoom in and
[04:27:06] introduction to circuits absolutely so
[04:27:09] um maybe I'll start by just describing
[04:27:12] some phenomena and then we can sort of
[04:27:14] build to the idea of features and
[04:27:16] circuits so um if you spent like quite a
[04:27:20] few years maybe maybe like five years to
[04:27:22] some extent um with other things
[04:27:25] studying this one particular model
[04:27:26] Inception V1 um which is this one Vision
[04:27:28] model it was um state-ofthe-art in 2015
[04:27:32] um and uh uh you know very much not
[04:27:34] state-ofthe-art anymore um and it has
[04:27:37] you know maybe about 10,000 neurons and
[04:27:39] and I spent a lot of time looking at the
[04:27:41] 10,000 neurons
[04:27:42] odd neurons of of inception V1
[04:27:45] um and one of the interesting things is
[04:27:48] you know there are lots of neurons that
[04:27:50] don't have some obvious intal meaning
[04:27:52] but there's a lot of neurons on
[04:27:53] Inception V1 that do have really clean
[04:27:56] intal meanings um so you find neurons
[04:27:59] that just really do seem to detect
[04:28:01] curves and you find neurons that really
[04:28:03] do seem to detect cars and um car wheels
[04:28:06] and car windows and you know floppy ears
[04:28:08] of dogs and dogs with long snouts facing
[04:28:11] to the right and dogs with Longs Nots
[04:28:12] facing to the left and you know
[04:28:14] different kinds of far and there's
[04:28:16] there's sort of this whole beautiful
[04:28:17] Edge detectors line detectors color
[04:28:19] contrast detectors um these beautiful
[04:28:21] things we call high low frequency
[04:28:22] detectors you know I think looking at I
[04:28:24] sort of felt like a biologist you know
[04:28:25] you just you're looking at at this sort
[04:28:27] of new world of proteins and you're
[04:28:29] discovering all these these different
[04:28:30] proteins that
[04:28:32] interact um so one way you could try to
[04:28:35] understand these models is in terms of
[04:28:36] neurons you could try to be like oh you
[04:28:38] know there's a dog detecting neuron and
[04:28:40] um here's a car detecting neuron and it
[04:28:42] turns out you can actually ask how those
[04:28:43] connect together so you can go and say
[04:28:45] oh you know I have this car detecting on
[04:28:46] how was it built and it turns out in the
[04:28:48] previous layer it's connected really
[04:28:50] strongly to a window detector and a
[04:28:51] wheel detector and a sort of car body
[04:28:53] detector and it looks for the window
[04:28:55] above the car and the wheels below and
[04:28:56] the car chrome sort of in the middle
[04:28:58] sort of everywhere but especially on the
[04:28:59] lower part um and that's sort of a
[04:29:02] recipe for a car right like that is you
[04:29:04] know earlier we said the thing we wanted
[04:29:05] from mechor was to get algorithms to go
[04:29:07] and get you know ask what is the the
[04:29:09] algorithm that runs well here we're just
[04:29:10] looking at the weights of the N Network
[04:29:12] reading off this kind of recipe for
[04:29:13] detecting cars it's a very simple crude
[04:29:15] recipe but it's it's there and so we
[04:29:18] call that a circuit this this connection
[04:29:19] well okay so the the problem is that not
[04:29:23] all of the neurons um are interpal and
[04:29:27] there there's reason to think um we can
[04:29:28] get into this more later that there's
[04:29:30] this this superos hypothesis there
[04:29:31] reason to think that sometimes the right
[04:29:34] unit to analyze things in terms of um is
[04:29:37] combinations of neurons so sometimes
[04:29:39] it's not that there's a single neuron
[04:29:41] that represents say a car um but it
[04:29:43] actually turns that after you detect the
[04:29:44] car the model sort of hides a little bit
[04:29:46] of the car in the following layer and a
[04:29:48] bunch of a bunch of dog detectors why is
[04:29:50] it doing that well you know maybe it
[04:29:52] just doesn't want to do that much work
[04:29:53] on on on on cars at that point and you
[04:29:56] know it's sort of storing it away to go
[04:29:57] and um uh so it turns out then that the
[04:30:00] sort of subtle pattern of you know
[04:30:02] there's all these neurons that you think
[04:30:03] are dog detectors and maybe they're
[04:30:04] primarily that but they all a little bit
[04:30:07] contribute to representing a car um in
[04:30:09] in that next layer okay so so now we
[04:30:11] can't really think there there might
[04:30:12] still be some something I don't know you
[04:30:15] could call it like a car concept or
[04:30:16] something but it no longer corresponds
[04:30:17] to a neuron so we need some term for
[04:30:20] these kind of neuron-like entities these
[04:30:22] things that we sort of would have liked
[04:30:23] the neurons to be these idealized
[04:30:24] neurons um the things that are the nice
[04:30:27] neurons but also maybe there's more of
[04:30:28] them somehow hidden and we call those
[04:30:30] features and then what are circuits so
[04:30:33] circuits are these connections of
[04:30:34] features right so so when we have the
[04:30:36] car detector um and it's connected to a
[04:30:39] window detector and a wheel detector and
[04:30:41] it looks for the Wheels below and the
[04:30:42] windows on top um that's a circuit um so
[04:30:45] circuits are just collections of
[04:30:47] features connected by weights um and
[04:30:49] they they Implement algorithms so they
[04:30:50] tell us you know how is how are features
[04:30:52] used how are they built um how do they
[04:30:55] connect together so maybe it's it's it's
[04:30:57] worth trying to pin down like what what
[04:30:59] really um is the the core hypothesis
[04:31:01] here I think the the core hypothesis is
[04:31:04] something we call the linear
[04:31:04] representation hypothesis so um if we
[04:31:07] think about the car detector you know
[04:31:09] the more it fires the more we sort of
[04:31:11] think of that as meaning oh the model is
[04:31:12] more and more confident that um a car
[04:31:15] was present um or you know if it's some
[04:31:18] combination of neurons that represent a
[04:31:19] car you know the more that combination
[04:31:21] fires the more we think the model thinks
[04:31:23] there's a car present um this doesn't
[04:31:27] have to be the case right like you could
[04:31:28] imagine something where you have you
[04:31:29] know you have this car detector neuron
[04:31:31] and you think ah you know if it fires
[04:31:34] like you know between one and two that
[04:31:36] means one thing but it means like
[04:31:37] totally different if it's between three
[04:31:38] and four um that would be a nonlinear
[04:31:40] representation and principle that you
[04:31:42] know models could do that I think it's
[04:31:44] it's sort of inefficient for them to do
[04:31:46] if you try to think about how you'd
[04:31:47] Implement computation like that it's
[04:31:48] it's kind of an annoying thing to do but
[04:31:50] in principal models can do that um so uh
[04:31:54] one way to think about the features and
[04:31:56] and circuits sort of framework for
[04:31:58] thinking about things is that we're
[04:32:00] thinking about things as being linear
[04:32:01] we're thinking about there as being um
[04:32:03] that if a if a neuron or a combination
[04:32:05] of neurons fires more it's sort of that
[04:32:06] means more of the of a particular thing
[04:32:08] being detected and then that gives
[04:32:10] weights a very clean interpretation as
[04:32:12] these edges between these these entities
[04:32:14] that these features um and that that
[04:32:17] edge then has a has a meaning um so
[04:32:19] that's that's in some ways the the core
[04:32:21] thing um it's it's like um you know we
[04:32:25] can talk about this sort of outside the
[04:32:26] context of ns are you familiar with the
[04:32:28] word toac results um so you have like
[04:32:30] you know King minus man plus woman
[04:32:32] equals Queen well the reason you can do
[04:32:34] that kind of arithmetic um is because
[04:32:37] you have a linear representation can you
[04:32:38] actually explain that representation a
[04:32:40] little bit so first off so a feature is
[04:32:42] a is a direction of activation you think
[04:32:45] it that way can you do the the the minus
[04:32:47] men plus women that that the war Toc
[04:32:50] stuff can you explain what that is yeah
[04:32:53] there's this very such a simple clean
[04:32:54] explanation of what we're talking about
[04:32:56] exactly yeah so there's this very famous
[04:32:58] result word toac by um Thomas mikov at
[04:33:01] all and there's been tons of follow-up
[04:33:02] work exploring this so so sometimes we
[04:33:05] have these we create these word
[04:33:07] embeddings um where uh we map every word
[04:33:10] to a vector I mean that in itself by the
[04:33:12] way is is kind of a crazy thing if you
[04:33:14] haven't thought about it before right
[04:33:15] like we we're we're going and and
[04:33:17] representing we're turning um you know
[04:33:20] like like if if you just learned about
[04:33:21] vectors in physics class right uh and
[04:33:23] I'm like oh I'm going to actually turn
[04:33:24] every word uh in the dictionary into a
[04:33:26] vector that's kind of a crazy idea okay
[04:33:28] but you could imagine um you could
[04:33:31] imagine all kinds of ways in which you
[04:33:32] might map words to to
[04:33:34] vectors but it it it seems like when we
[04:33:36] train neural networks um they like to go
[04:33:39] and and map words detectors to such that
[04:33:42] they're they're they they sort of linear
[04:33:44] structure in a particular sense which is
[04:33:47] that directions have meaning so for
[04:33:50] instance if you there there will be some
[04:33:51] direction that seems to sort of
[04:33:52] correspond to gender and male words will
[04:33:55] be you know far in One Direction and
[04:33:56] female words will be in another
[04:33:58] Direction and the linear representation
[04:34:00] hypothesis is you you could sort of
[04:34:02] think of it roughly as saying that
[04:34:04] that's actually kind of the fundamental
[04:34:05] thing that's going on that that
[04:34:07] everything is just different directions
[04:34:09] have meanings and adding different
[04:34:11] Direction vectors together can represent
[04:34:13] Concepts and the michelov paper sort of
[04:34:16] took that idea seriously and one
[04:34:18] consequence of it is that you can you
[04:34:19] can do this game of playing sort of
[04:34:20] arithmetic with words so you can do king
[04:34:23] and you can you know subtract off the
[04:34:24] word man and add the word woman and so
[04:34:26] you're sort of you know going and and
[04:34:28] trying to switch the gender and indeed
[04:34:30] if you do that the result will sort of
[04:34:31] be close to the word Queen um and you
[04:34:33] can you know do other things like you
[04:34:35] can do um uh you know Sushi minus Japan
[04:34:38] plus Italy and get pizza or uh different
[04:34:42] things like this right um so so this is
[04:34:45] in some sense the core of the linear
[04:34:46] representation hypothesis you can
[04:34:48] describe it just as a purely abstract
[04:34:49] thing about Vector spaces you can
[04:34:50] describe it as a as a statement about um
[04:34:53] about the activations of neurons um but
[04:34:56] it's really about this this property of
[04:34:58] directions having meaning and in some
[04:35:00] ways it's even a little subtle than that
[04:35:02] it's really I think mostly about this
[04:35:03] property of being able to add things
[04:35:05] together um that you can sort of
[04:35:07] independently modify um say gender and
[04:35:10] royalty or
[04:35:12] um you know Cuisine typee or country and
[04:35:15] and and and the concept of food by by
[04:35:17] adding them do you think the linear
[04:35:19] hypothesis holds that carries scales so
[04:35:24] so far I think everything I have seen is
[04:35:26] consistent with this hypothesis and it
[04:35:28] doesn't have to be that way right like
[04:35:29] like you can write down neural networks
[04:35:31] where um you write weights such that
[04:35:33] they don't have linear representations
[04:35:35] where the right way to understand them
[04:35:37] is not is not in terms of linear
[04:35:38] representations but I think every
[04:35:39] natural neural network I've seen um Hess
[04:35:43] property um there's been one paper
[04:35:45] recently um that there's been some sort
[04:35:49] of pushing around the edges so I think
[04:35:51] there's been some work recently studying
[04:35:52] multi-dimensional features where rather
[04:35:54] than a single Direction it's more like
[04:35:56] um a manifold of directions this to me
[04:35:59] still seems like a linear representation
[04:36:01] um and then there's been some other
[04:36:03] papers suggesting that maybe um in in
[04:36:06] very small models you get nonlinear
[04:36:08] representations um I think that the
[04:36:10] jury's still out on that
[04:36:12] um but in I think everything that we've
[04:36:14] seen so far has been consistent with the
[04:36:16] linear representation hypothesis and
[04:36:17] that's that's wild it it doesn't have to
[04:36:19] be that way um and yet uh I think that
[04:36:21] there's a lot of evidence that certainly
[04:36:23] at least this is very very widespread
[04:36:25] and so far the evidence is is consistent
[04:36:27] with that and I and I I think you know
[04:36:29] one thing you might say is you might say
[04:36:30] well Christopher you know it's that's a
[04:36:32] lot you know to to go and and sort of um
[04:36:35] to ride on you know if we don't know for
[04:36:36] sure this is true and you're sort of you
[04:36:38] know you're investigating all not works
[04:36:39] as though it is true you know isn't that
[04:36:41] um isn't that dangerous well you know
[04:36:43] but I I think actually there's a there's
[04:36:45] a virtue in taking hypotheses seriously
[04:36:47] and pushing them as far as they can go
[04:36:50] um so it might be that someday we
[04:36:52] discover something that is inconsistent
[04:36:53] with linear representation hypothesis
[04:36:55] but science is full of hypothesis and
[04:36:57] theories that were wrong um and we
[04:36:59] learned a lot by sort of working under
[04:37:02] under them as a sort of an assumption um
[04:37:04] and and then going and pushing them as
[04:37:06] far as we can I guess I guess this is
[04:37:07] sort of the heart of of what would
[04:37:09] call normal normal science um um I don't
[04:37:12] know if you want we can talk a lot about
[04:37:14] about uh philosophy of science and uh
[04:37:16] that leads to the paradigm shift so yeah
[04:37:18] I love it taking the hypothesis
[04:37:20] seriously and take it to a natural
[04:37:21] natural conclusion yeah same with the
[04:37:23] scaling hypothesis same exactly exactly
[04:37:26] and I love it one of my colleagues Tom
[04:37:28] henigan who is a former physicist um
[04:37:31] like made this really nice analogy to me
[04:37:34] of um uh caloric Theory where you know
[04:37:37] once upon a time we thought that heat
[04:37:39] was actually you know this thing called
[04:37:41] caloric and like the reason you know hot
[04:37:43] objects you know would would warm up
[04:37:45] cool objects is like the caloric is
[04:37:47] flowing through them um and like you
[04:37:49] know because we're so used to thinking
[04:37:51] about about heat you know in terms of
[04:37:53] the modern modern Theory you know that
[04:37:54] seems kind of silly but it's actually
[04:37:56] very hard to construct uh an experiment
[04:37:58] that that sort of disproves the um
[04:38:01] chloric hypothesis um and you know you
[04:38:03] can actually do a lot of really useful
[04:38:05] work believing in chloric for example it
[04:38:07] turns out that the original combustion
[04:38:09] engines were developed by people who
[04:38:11] believe in the caloric Theory so I think
[04:38:13] this a virtue in taking hypotheses
[04:38:16] seriously even when they might be wrong
[04:38:17] yeah yeah there's a deep philosophical
[04:38:20] truth to that that's kind of kind of how
[04:38:22] I feel about space travel like
[04:38:23] colonizing Mars there's a lot of people
[04:38:25] that criticize that I think if you just
[04:38:27] assume we have to colonize Mars in order
[04:38:29] to have a backup for human civilization
[04:38:32] even if that's not true that's going to
[04:38:33] produce some interesting interesting
[04:38:36] engineering and even scientific
[04:38:38] breakthroughs I think yeah well and
[04:38:39] actually this is another thing that I
[04:38:40] think is really interesting so um you
[04:38:43] know there a way in which I think it can
[04:38:45] be really useful for society to have
[04:38:48] people um almost irrationally dedicated
[04:38:52] to investigating particular hypothesis
[04:38:54] um because uh well it it takes a lot to
[04:38:57] sort of maintain scientific morale and
[04:39:00] really push on something when you know
[04:39:01] most most SCI scientific hypotheses end
[04:39:03] up being wrong you know a lot of a lot
[04:39:04] of science doesn't doesn't work out um
[04:39:08] and but and yet it's you know it's very
[04:39:10] it's very useful to go do you know um
[04:39:12] there's a there's a joke about Jeff
[04:39:13] Hinton um which is that uh Jeff Hinton
[04:39:16] has discovered how the brain works every
[04:39:18] year for the last 50 years yeah um but
[04:39:20] you know I I say that with like you know
[04:39:23] the you know with really deep respect
[04:39:25] because uh in fact that's actually you
[04:39:26] know that that led to him doing some
[04:39:28] some really great work yeah he won the
[04:39:30] Noel prize Now Who's Laughing Now
[04:39:31] exactly exactly exactly um yeah I think
[04:39:34] one want to be able to pop up and sort
[04:39:36] of recognize the the appropriate level
[04:39:38] of confidence but I think there's also a
[04:39:39] lot of value and just being like you
[04:39:41] know I'm going to essentially assume I'm
[04:39:44] going to condition on this problem being
[04:39:46] possible or this being broadly the right
[04:39:49] approach and I'm just going to go and
[04:39:50] assume that for a while and go and work
[04:39:53] within that um and push really hard on
[04:39:55] it um and you know if Society has lots
[04:39:58] of people doing doing that for different
[04:39:59] things um that's actually really useful
[04:40:01] in terms of going and uh getting
[04:40:05] to getting you know either really really
[04:40:08] ruling things out right we can be like
[04:40:10] well you know that didn't work we know
[04:40:11] that somebody tried hard um or going in
[04:40:14] and getting to something that that does
[04:40:15] teach us something about the world so
[04:40:17] another interesting hypothesis is the
[04:40:19] superposition hypothesis can you
[04:40:20] describe what superos is yeah so earlier
[04:40:23] we were talking about word toac right
[04:40:24] and we were talking about how you know
[04:40:25] maybe you have One Direction that
[04:40:27] corresponds to gender and maybe another
[04:40:28] that corresponds to royalty and another
[04:40:30] one that corresponds to Italy and
[04:40:32] another one that corresponds to you know
[04:40:33] food and and all these things well you
[04:40:35] know um often times maybe these these uh
[04:40:39] these Ward embeddings they might be 500
[04:40:40] dimensions a thousand dimensions and so
[04:40:43] if you believed that all of those
[04:40:44] directions were
[04:40:45] orthogonal um then you could only have
[04:40:48] you know 500 Concepts and you know I I
[04:40:50] love pizza um but like if I was going to
[04:40:53] go and like give the like 500 most
[04:40:55] important Concepts in um you know the
[04:40:57] English language probably Italy wouldn't
[04:40:59] be it's not obvious at least that Italy
[04:41:01] would be one of them right because you
[04:41:02] you have to have things like plural and
[04:41:05] singular and U uh verb and noun and
[04:41:09] adjective and you know um there's a lot
[04:41:11] of things we have to get to before we
[04:41:12] get to get to Italy um uh and Japan and
[04:41:16] you know there's a lot of countries in
[04:41:17] the world um and so how might it be that
[04:41:20] models could you know simultaneously
[04:41:23] have the linear representation
[04:41:24] hypothesis be true and also represent
[04:41:28] more things than they have directions so
[04:41:30] so what does that mean well okay so if
[04:41:32] if if linear representation hypothesis
[04:41:33] is true something interesting has to be
[04:41:35] going on now I'll I'll tell you one more
[04:41:37] interesting thing before we we go and we
[04:41:39] do that which is um you know earlier we
[04:41:42] were talking about all these polymatic
[04:41:43] neurons right um these neurons that you
[04:41:45] know when we're looking at Inception V1
[04:41:47] there's these nice neurons that like the
[04:41:48] car detector and the curve detector and
[04:41:49] so on that respond to lots of you know
[04:41:51] to very coherent things but it's lots of
[04:41:54] neurons that respond to a bunch of
[04:41:55] unrelated things that's that's also an
[04:41:56] interesting phenomenon um and it turns
[04:41:58] out as well that even these neurons that
[04:42:01] are really really clean if you look at
[04:42:02] the weak activations right so if you
[04:42:04] look at like you know the activation
[04:42:05] where it's like activating 5% of of the
[04:42:09] the you know of the maximum activation
[04:42:11] it's really not the core thing that it's
[04:42:13] expecting right so if you look at a a
[04:42:15] curve detector for instance and you look
[04:42:16] at the places where it's 5% active you
[04:42:18] know you could interpret it just as
[04:42:20] noise or it could be that it's that it's
[04:42:22] doing something else there okay so so
[04:42:23] how could that be
[04:42:26] well there's this amazing thing in
[04:42:29] mathematics um called compressed sensing
[04:42:32] and it's it's actually this this very
[04:42:34] surprising fact where if you have a high
[04:42:36] dimensional space and you project it
[04:42:39] into a low dimensional space ordinarily
[04:42:42] you can't go and sort of unprojected and
[04:42:44] get back your high dimensional Vector
[04:42:45] right you threw information away this is
[04:42:47] like you know you can't you can't invert
[04:42:49] a rectangular Matrix um you can only
[04:42:51] invert Square
[04:42:52] matrices um but it turns out that that's
[04:42:56] actually not quite true if I tell you
[04:42:58] that the high dimensional Vector was
[04:43:00] sparse so it's mostly zeros then it
[04:43:02] turns out that you can often go and find
[04:43:05] back um the uh the high dimensional
[04:43:08] Vector with with very high probability
[04:43:11] um so that's a surprising fact right it
[04:43:13] says that you know you can um you can
[04:43:15] you can have this High dimensional
[04:43:16] Vector space and as long as things are
[04:43:18] sparse um you can project it down you
[04:43:20] can have a lower dimensional projection
[04:43:21] of it and that works so the super
[04:43:25] hypothesis is saying that that's what's
[04:43:27] going on in neural networks that's for
[04:43:28] instance that's what's going on in wart
[04:43:29] edings the wart embeddings are able to
[04:43:32] simultaneously have directions be the
[04:43:33] meaningful thing and by exploiting the
[04:43:35] fact that they're they're operating on a
[04:43:37] fairly High dimensional space they're
[04:43:38] actually and and the fact that these
[04:43:40] concepts are right like you know you
[04:43:42] usually aren't talking about Japan and
[04:43:43] Italy at the same time um you know most
[04:43:46] of the most of those Concepts you know
[04:43:47] in most sentences Japan and Italy are
[04:43:49] both zero they're not present at all um
[04:43:51] and if that's true um then you can go
[04:43:55] and have it be the case that um that you
[04:43:58] can you can have many more of these sort
[04:44:00] of directions that are meaningful these
[04:44:02] features than you have dimensions and
[04:44:04] some of when we're talking about neurons
[04:44:05] you can have many more Concepts than you
[04:44:07] have have neurons so that's the at a
[04:44:10] high level super hypothesis now it has
[04:44:12] this even Wilder implication which is um
[04:44:16] to go and say that uh neural networks
[04:44:21] are it may not just be the case that the
[04:44:23] the representations are like of this but
[04:44:24] the the computation may also be like
[04:44:26] this you know the connections between
[04:44:27] all of them and so in in some sense
[04:44:29] neural networks may be shadows of much
[04:44:32] larger sparer neural networks and what
[04:44:35] we see are these
[04:44:37] projections um and the super you the
[04:44:39] strongest version of the super
[04:44:40] hypothesis would be to take that really
[04:44:41] seriously and sort of say you know there
[04:44:43] there actually is in some sense this
[04:44:44] this upstairs model this you know um
[04:44:47] where where the neurons are really
[04:44:49] sparse and all interpal and there's you
[04:44:50] know the weights between them are these
[04:44:52] really sparse circuits and that's what
[04:44:54] we're
[04:44:55] studying um and uh the thing that we're
[04:44:59] observing is the shadow of it and we
[04:45:00] need to find the original object and uh
[04:45:03] the process of learning is trying to
[04:45:05] construct a compression of the upstairs
[04:45:08] model that doesn't lose too much
[04:45:10] information in the projection yeah
[04:45:12] finding how to fit it efficiently or
[04:45:13] something like this um that grent is
[04:45:15] doing this in fact so this sort of says
[04:45:18] that gradient descent you know could it
[04:45:19] could just represent a dense neural
[04:45:20] network but it sort of says that
[04:45:22] gradient descent is pleasantly searching
[04:45:23] over the space of extremely sparse
[04:45:26] models that could be projected into this
[04:45:28] low dimensional space and this large
[04:45:30] body of work of of people going and
[04:45:31] trying to study sparse neural networks
[04:45:33] right where you go and you have you
[04:45:34] could design neural networks right where
[04:45:36] where the edges are sparse and the
[04:45:37] activations are sparse and you know my
[04:45:39] sense is that work has gener
[04:45:41] it feels very principled right it makes
[04:45:43] so much sense and yet that that work
[04:45:44] hasn't really panned out that well as my
[04:45:46] impression broadly and I think that a a
[04:45:50] potential answer for that is that
[04:45:52] actually the neural network is already
[04:45:54] sparse in some sense grading descent was
[04:45:57] the whole time gradi you were trying to
[04:45:58] go and do this gradiant descent was
[04:45:59] actually in the behind the scenes going
[04:46:00] and searching more efficiently than you
[04:46:02] could through the space of sparse models
[04:46:04] and going in learning whatever sparse
[04:46:06] model was most efficient and then
[04:46:08] figuring out how to fold it down nicely
[04:46:10] to go and run conven on your GPU which
[04:46:12] does you know nice dense Matrix
[04:46:13] multiplies um and that you just can't
[04:46:15] beat that how many Concepts do you think
[04:46:18] can be shoved in into a neural network
[04:46:20] depends on how sparse they are so there
[04:46:22] there's probably an upper bound from the
[04:46:24] number of parameters right because you
[04:46:25] have to have you still have to have you
[04:46:27] know print weights that go and connect
[04:46:29] them together um so that's that's one
[04:46:31] upper bound there are in fact all these
[04:46:33] lovely results from compressed sensing
[04:46:35] and the Johnson Linton stess Lemma and
[04:46:37] and things like this um that they they
[04:46:39] basically tell you that if you have a
[04:46:41] vector space and you want to have almost
[04:46:43] orthogonal vectors which is sort of
[04:46:45] probably the thing that you want here
[04:46:46] right so you you're going to say well
[04:46:47] you know I'm going to give up on having
[04:46:49] my my Concepts my features be strictly
[04:46:51] orthogonal but I'd like them to not
[04:46:52] interfere that much I'm going to have to
[04:46:53] ask them to be almost orthogonal um then
[04:46:56] this would say that it's actually you
[04:46:58] know for once you set a threshold for
[04:47:00] for what you're what you're willing to
[04:47:01] accept in terms of how how much coine
[04:47:03] similarity there is that's actually
[04:47:05] exponential in the number of neurons
[04:47:07] that you have so at some point that's
[04:47:08] not going to even be the the limiting
[04:47:10] factor um but um there some beautiful
[04:47:12] results there and in fact it's probably
[04:47:14] even better than that in some sense
[04:47:15] because that's sort of is for saying
[04:47:17] that you know any random set of features
[04:47:19] could be active but in fact the features
[04:47:21] have sort of a correlational structure
[04:47:22] where some features you know are more
[04:47:24] likely to co-occur and other ones are
[04:47:26] less likely to co-occur and so neural
[04:47:28] networks my guess would be can do do
[04:47:29] very well in terms of going and uh
[04:47:33] packing things in such to to the point
[04:47:35] that's probably probably not the
[04:47:36] limiting factor how does the problem of
[04:47:38] polys semanticity enter the picture here
[04:47:41] poly semanticity is this phenomenon we
[04:47:42] observe where we look at many neurons
[04:47:44] and the neuron doesn't just sort of
[04:47:46] represent one one concept it's not it's
[04:47:48] not a clean feature it responds to a
[04:47:49] bunch of unrelated things and um
[04:47:52] supersition is you can think of as as
[04:47:54] being a hypothesis that explains the
[04:47:55] observation of polys semanticity um so
[04:47:59] poly semanticity is this observe
[04:48:00] phenomenon and super is is a hypothesis
[04:48:03] that um would explain it along with with
[04:48:05] some other so that makes Mech turb more
[04:48:08] difficult right so if you if you're
[04:48:09] trying to understand things in terms of
[04:48:11] individual neurons and you have
[04:48:12] polymatic neurons you're in an awful lot
[04:48:14] of trouble right I mean the easiest
[04:48:16] answer is like okay well you know you're
[04:48:17] looking at the neurons you're trying to
[04:48:18] understand them this one responds to a
[04:48:20] lot of things it doesn't have a nice
[04:48:21] meaning okay we're you that's that's
[04:48:23] that's bad um another thing you could
[04:48:25] ask is you know ultimately we want to
[04:48:26] understand the weights and if you have
[04:48:28] two polymatic neurons and you know each
[04:48:30] one responds to three things and then
[04:48:32] you know the other neuron responds to
[04:48:33] three things and you have weight between
[04:48:34] them you know what does that mean does
[04:48:35] it mean that like all three you know
[04:48:37] like there's these nine you know nine
[04:48:39] interactions going on it's a very weird
[04:48:41] thing but there's also a deeper reason
[04:48:44] which is related to the fact that neural
[04:48:45] networks operate on really high
[04:48:47] dimensional spaces so I said that our
[04:48:49] goal was you know to understand neural
[04:48:50] networks and understand the mechanisms
[04:48:52] and one thing you might say is like well
[04:48:55] why not it's just a mathematical
[04:48:56] function why not just look at it right
[04:48:57] like um you know one of the earliest
[04:48:59] projects I did studied these these
[04:49:00] neural networks that mapped two-
[04:49:01] dimensional spaces to two- dimensional
[04:49:03] spaces and you can sort of interpret
[04:49:05] them in this beautiful way is like
[04:49:06] bending manifolds mhm um why can't we do
[04:49:09] that well you know as you have have a
[04:49:10] higher dimensional space um the volume
[04:49:13] of that space in some senses is
[04:49:15] exponential in the number of inputs you
[04:49:17] have and so you can't just go in
[04:49:18] visualize it so we somehow need to break
[04:49:21] that apart we need to somehow break that
[04:49:23] exponential space into a bunch of things
[04:49:26] that we you know some non-exponential
[04:49:28] number of things that we can reason
[04:49:30] about independently and the independence
[04:49:32] is crucial because it's the Independence
[04:49:34] that allows you to not have to think
[04:49:35] about you know all the exponential
[04:49:37] combinations of things and
[04:49:41] things being monomatic things only
[04:49:43] having one meaning things having a
[04:49:44] meaning that isn't is the key thing that
[04:49:47] allows you to think about them
[04:49:48] independently and so I think that's that
[04:49:50] if you want the deepest reason why we
[04:49:52] want to have um interpal monatic
[04:49:56] features I think that's really the the
[04:49:58] Deep reason and so the goal here as your
[04:50:00] recent work has been aiming at is how do
[04:50:02] we extract the mod semantic features
[04:50:05] from a neural net that has politic
[04:50:08] features and all this this mess yes we
[04:50:10] have the have we observe these polyur
[04:50:12] and we hypothesize that's what's going
[04:50:13] what's going on at superos and if
[04:50:15] superos is what's going on there there's
[04:50:17] actually a sort of wellestablished
[04:50:19] technique that is sort of the principled
[04:50:21] thing to do which is dictionary learning
[04:50:24] and um it turns out if you do dictionary
[04:50:25] learning in particular if you do sort of
[04:50:27] a nice efficient way that in some in
[04:50:29] some sense sort of nicely regularizes it
[04:50:30] well as well called a sparse Auto
[04:50:32] encoder if you train a sparse Auto
[04:50:34] encoder these beautiful interpal
[04:50:36] features start to just fall out where
[04:50:37] there weren't any beforehand and so
[04:50:40] that's notot of thing that you would
[04:50:41] necessarily predict right but it turns
[04:50:43] out that that works very very well you
[04:50:45] know to me that seems like you know some
[04:50:47] non-trivial validation of linear
[04:50:50] representations and supersession so with
[04:50:52] dictionary learning you're not looking
[04:50:53] for particular kind of categories you
[04:50:54] don't know what they
[04:50:56] arege and this gets back to our earlier
[04:50:58] point right when we're not making
[04:50:59] assumptions grading descent is smarter
[04:51:01] than us so we're not making assumptions
[04:51:02] about what's there um I mean one
[04:51:04] certainly could do that right one could
[04:51:06] assume that there's a PHP feature and go
[04:51:08] and search for it but we're not doing
[04:51:10] that we're saying we don't know what's
[04:51:11] going to be there instead we're just
[04:51:12] going to go and let um the sparse Auto
[04:51:14] encoder discover the things that are
[04:51:15] there so can you uh talk to the to monos
[04:51:18] semanticity paper from October last year
[04:51:21] that had a lot of like nice breakthrough
[04:51:23] results that's very kind of you to
[04:51:25] describe it that way um yeah I mean this
[04:51:26] was um uh our first real success using
[04:51:31] sparse Auto encoders so we took a one
[04:51:33] layer model um and it turns out if you
[04:51:35] go and you you know do dictionary
[04:51:37] learning on it you find all these really
[04:51:39] nice interpal features so you know the
[04:51:41] Arabic feature the Hebrew feature um the
[04:51:43] Bas 64 feature those were were some some
[04:51:46] examples that we studied in a lot of
[04:51:47] depth and really showed that they were
[04:51:49] um what we thought they were it turns if
[04:51:50] you train a model twice as well and
[04:51:52] train two different models and and do
[04:51:53] dictionary learning you find find
[04:51:54] analogous features in both of them so
[04:51:56] that's fun um you find all kinds of of
[04:51:58] different features so that was really
[04:51:59] just showing um that um that this works
[04:52:02] and um you know I should mention that
[04:52:04] there was this cunning home at all um
[04:52:06] that had very similar results around the
[04:52:08] same time there's something fun about
[04:52:09] being doing these kinds of small scale
[04:52:12] experiments and finding that it's
[04:52:13] actually working yeah well and there's
[04:52:15] and there's so much structure here like
[04:52:17] you you know so maybe maybe stepping
[04:52:19] back for a while um I thought that maybe
[04:52:23] all this mechanistic can really work um
[04:52:25] the end result was going to be that I
[04:52:27] would have an explanation for why it was
[04:52:28] sort of you know very hard and not going
[04:52:30] to be tractable um you know we'd be like
[04:52:32] well there's this problem with
[04:52:33] supersession and it turns that super
[04:52:34] session is really hard um and we're kind
[04:52:36] of screwed but that's not what happened
[04:52:38] in fact a very natural Le technique just
[04:52:41] works and so then that's actually a very
[04:52:43] good situation you know I think um this
[04:52:46] is a sort of hard research problem and
[04:52:48] it's got a lot of research risk and you
[04:52:49] know it it might still very well fail
[04:52:51] but um I think that some amount of some
[04:52:53] very significant amount of research risk
[04:52:55] um was sort of put behind us when that
[04:52:56] started to work can you describe what
[04:52:58] kind of features can be extracted in
[04:53:01] this way well so it depends on the model
[04:53:04] that you're studying right so the the
[04:53:05] larger the model the more sophisticated
[04:53:07] they're going to be and we'll probably
[04:53:08] talk about about follow-up work in a
[04:53:09] minute but in these one layer models um
[04:53:12] so some very common things I think were
[04:53:14] were languages both programming
[04:53:16] languages and natural languages there
[04:53:18] were a lot of features that were um
[04:53:20] specific words in specific contexts so
[04:53:23] the and I think really the way to think
[04:53:24] about this is that the is likely about
[04:53:26] to be followed by a noun so it's really
[04:53:28] you could think of this as the feature
[04:53:29] but you could also think of this as
[04:53:30] producting a specific noun feature and
[04:53:32] there would be these features that would
[04:53:33] fire for the in um the context of of say
[04:53:37] a legal document or a mathematical
[04:53:39] document or something something like
[04:53:40] this um and so uh you know maybe in the
[04:53:44] context of math you're like you know the
[04:53:47] and then predict Vector Matrix you know
[04:53:49] all these mathematical words whereas you
[04:53:51] other contexts you would predict other
[04:53:52] things that was that was common and
[04:53:54] basically we you need clever humans to
[04:53:57] assign labels to what we're seeing yes
[04:54:00] so you know this this is the only thing
[04:54:02] this is doing is that sort of um
[04:54:04] unfolding things for you so if
[04:54:06] everything was sort of folded over top
[04:54:07] of it you know cation folded everything
[04:54:09] on top of itself you can't really see it
[04:54:11] this is unfolding it but now you still
[04:54:13] have a very complex thing to try to
[04:54:15] understand um so then you have to do a
[04:54:17] bunch of work understanding what these
[04:54:18] are um and some of them are really
[04:54:20] subtle like there's some really cool
[04:54:22] things even in this this one layer model
[04:54:23] about um Unicode where you know of
[04:54:25] course some languages are in Unicode and
[04:54:27] the tokenizer won't necessarily have a
[04:54:29] dedicated token for every um Unicode um
[04:54:32] character so instead what you'll have is
[04:54:35] you'll have this these patterns of
[04:54:36] alternating token or alternating tokens
[04:54:38] that each represent half of a unic code
[04:54:39] character and then you have a different
[04:54:40] feature that you know goes and activates
[04:54:43] on the on the opposing ones to be like
[04:54:44] okay you know um I just finished a
[04:54:46] character you know go and predict the
[04:54:47] next prefix um then okay on the prefix
[04:54:50] you know predict a reasonable suffix um
[04:54:53] and you you have to alternate back and
[04:54:54] forth so there's you know these these
[04:54:56] wer models are are really interesting
[04:54:58] and um uh I mean there's another thing
[04:54:59] which is you might think okay there
[04:55:01] would just be one b64 feature but it
[04:55:03] turns out there's actually a bunch of
[04:55:04] b64 features because you can have
[04:55:06] English text encoded in as b64 and that
[04:55:09] has a very different distribution of B
[04:55:11] 64 tokens than than regular and there's
[04:55:14] um uh there's there's some things about
[04:55:17] tokenization as well that it can exploit
[04:55:18] and I don't know there all all kinds of
[04:55:20] fun stuff how difficult is the task of
[04:55:23] sort of assigning labels to what's going
[04:55:26] on can this be automated by AI well I
[04:55:28] think it depends on the feature and it
[04:55:30] also depends on how much you trust your
[04:55:31] AI so um there's a lot of work doing um
[04:55:35] automated inability I think that's a
[04:55:37] really exciting Direction and we do a
[04:55:39] fair amount of automated inter and have
[04:55:41] have Claude go and label our features is
[04:55:43] there some fun moments where it's
[04:55:45] totally right or it's totally wrong yeah
[04:55:48] well I think I think it's very common
[04:55:49] that it's like says something very
[04:55:52] general which is like true in some sense
[04:55:55] but not really picking up on the
[04:55:57] specific of what's going on um so I
[04:56:00] think I think that's a pretty common
[04:56:02] situation um you don't know that I have
[04:56:05] a particularly amusing one that's
[04:56:06] interesting that little gap between it
[04:56:08] is true but it doesn't quite
[04:56:11] get to the Deep Nuance of a thing yeah
[04:56:14] that's a general challenge it's like
[04:56:16] it's it's St an incredible colish they
[04:56:18] can say a true thing but it doesn't it's
[04:56:21] qu it's not it's missing the depth
[04:56:24] sometimes and in this context it's like
[04:56:26] the arc challenge you know the sort of
[04:56:28] IQ type tests it feels like figuring out
[04:56:32] what a feature represents is a bit of is
[04:56:34] a little puzzle you have to solve yeah
[04:56:36] and and I think that sometimes they're
[04:56:37] easier and sometimes they're harder as
[04:56:38] well um so
[04:56:41] uh yeah I think I think that's tricky
[04:56:42] now there's another thing which I don't
[04:56:44] know maybe maybe in some ways this is my
[04:56:46] like aesthetic coming in but I'll give
[04:56:48] try to give you a rationalization you
[04:56:49] know I'm actually a little suspicious of
[04:56:51] automated inability and I think that
[04:56:53] partly just that I want humans to
[04:56:55] understand neural net works and if the
[04:56:56] neural network is understanding it for
[04:56:57] me you know I'm I'm not I don't quite
[04:56:59] like that but I do have bit of a you
[04:57:01] know in some ways I'm sort of like the
[04:57:02] mathematicians who are like you know if
[04:57:03] there a computer automated proof it
[04:57:04] doesn't count U you know you they won't
[04:57:06] understand it but I I do also think that
[04:57:08] there is um this kind of like
[04:57:10] Reflections on trusting trust type issue
[04:57:12] where you know if you there's this
[04:57:14] famous talk about um uh you know you
[04:57:18] like when you're writing a computer
[04:57:19] program you have to trust your compiler
[04:57:20] and if there was like malware in your
[04:57:21] compiler then it could go and inject
[04:57:23] malware into the next compiler and you
[04:57:25] know you'd be kind of in trouble right
[04:57:27] well if you're using neural networks to
[04:57:28] go and um verify that your neural
[04:57:31] networks are safe the hypothesis that
[04:57:33] you're testing for is like okay well the
[04:57:34] neural network maybe isn't safe um and
[04:57:37] you have to worry about like is there
[04:57:38] some way that it could be screwing with
[04:57:39] you
[04:57:40] um so uh you know I I think that's not a
[04:57:43] big concern now um but I do Wonder in
[04:57:45] the long run if we have to use really
[04:57:46] powerful system AI systems to go and uh
[04:57:49] you know audit our AI systems is that is
[04:57:51] that actually something we can trust but
[04:57:53] maybe I'm just rationalizing because I I
[04:57:55] just want to us to have to get to a
[04:57:56] point where humans understand everything
[04:57:58] yeah I mean especially that's hilarious
[04:58:00] especially as we talk about AI safety
[04:58:02] and it looking for features that would
[04:58:04] be relevant to AI safety like deception
[04:58:06] and so on uh so let's let's talk about
[04:58:09] the scaling a semanticity paper in May
[04:58:12] 2024 okay so what did it take to scale
[04:58:14] this to apply to Claude 3 on it well a
[04:58:18] lot of gpus a lot more gpus um but one
[04:58:21] of my teammates Tom henigan um was
[04:58:24] involved in the original scaling loss
[04:58:26] work um and something that he was sort
[04:58:29] of interested in from very early on is
[04:58:31] are there scaling laws for
[04:58:34] inability um and so um something he sort
[04:58:38] of immediately did when when this work
[04:58:40] started to succeed and we started to
[04:58:42] have sparse Auto encoders work we became
[04:58:44] very interested in you know what are the
[04:58:45] scaling laws for um uh you know for
[04:58:49] making making sparse Auto encoders
[04:58:51] larger and how does that relate to
[04:58:52] making the base model larger um and so
[04:58:56] um it turns out this works really well
[04:58:57] and you can use it to sort of project um
[04:58:59] you know if you train a sparse Auto
[04:59:01] encod a given size you know how many
[04:59:02] tokens should you train on and so on so
[04:59:04] this was actually a very big help to us
[04:59:06] in scaling up um this work um and made
[04:59:08] it a lot easier for us to go and train
[04:59:11] um you know really large sparse Auto
[04:59:12] encoders where you know um it's not like
[04:59:14] training the big models but it's it's
[04:59:16] starting to get to a point where it's
[04:59:17] actually actually expensive to go um and
[04:59:19] train the really big ones so you have to
[04:59:21] I mean you have to do all the stuff of
[04:59:23] like splitting it across large I mean
[04:59:26] there's a huge engineering challenge
[04:59:27] here too right so yes so so there's
[04:59:29] there's a there's a scientific question
[04:59:31] of how do you scale things effectively
[04:59:32] um and then there's an enormous amount
[04:59:34] of engineering to go and scale this up
[04:59:36] you have to you have to chart it you
[04:59:37] have to you have to think very carefully
[04:59:38] about a lot of things I'm lucky to work
[04:59:40] with a bunch of great Engineers cuz I am
[04:59:42] definitely not a great engine yeah on
[04:59:43] the infrastructure especially yeah for
[04:59:45] sure so it turns out tldr it worked it
[04:59:49] worked yeah and and I think this is
[04:59:50] important because you could have
[04:59:51] imagined you could like you could have
[04:59:53] imagined a world where you set after
[04:59:54] towards monos fanticy you know Chris
[04:59:56] this is great you know it works on a one
[04:59:58] layer model but one layer models are
[04:59:59] really idiosyncratic um like you know
[05:00:02] maybe maybe there just something ID like
[05:00:04] maybe the linear representation
[05:00:04] hypothesis and super hypothesis is the
[05:00:06] right way to understand a one layer
[05:00:08] model but it's not the right way to
[05:00:09] understand large models um and so I
[05:00:12] think um I mean first of all like The
[05:00:14] Cutting him at all paper sort of um cut
[05:00:15] through that a little bit and and sort
[05:00:17] of suggested that this wasn't the case
[05:00:18] but um scaling onity sort of I think was
[05:00:21] significant evidence that even for very
[05:00:23] large models and we did it on Claude 3
[05:00:25] sauna which at that point was uh one of
[05:00:27] our production models um you know even
[05:00:30] these models um seem to be very you know
[05:00:34] seem to be substantially explained at
[05:00:35] least by linear features and you know
[05:00:38] doing dictionary learning on them works
[05:00:39] and as you learn more features you go
[05:00:40] and you explain explain more and more so
[05:00:43] that's a I think a quite a promising
[05:00:44] sign and you find now really fascinating
[05:00:48] abstract features um and the features
[05:00:50] are also multimodal they respond to
[05:00:52] images and text for the same concept
[05:00:54] which is fun yeah this can you explain
[05:00:56] that I mean like you know back door
[05:00:59] there's just a lot of examples that you
[05:01:00] can yeah so maybe maybe let's start with
[05:01:02] a one example to start which is we found
[05:01:04] some features around sort of security
[05:01:06] vulnerabilities and back doors and codes
[05:01:08] so it turns out those are actually two
[05:01:08] different features um so there's a
[05:01:10] security vulnerability feature and if
[05:01:12] you force it active Claude will start to
[05:01:15] go and write um security vulnerabilities
[05:01:17] like buffer overflows into code and it
[05:01:19] also it fires for all kinds of things
[05:01:20] like you know some of some of the top
[05:01:22] data set examples for it were things
[05:01:23] like you know dash dash disable um you
[05:01:27] know SSL or something like this which
[05:01:29] are sort of obviously really um uh
[05:01:32] really insecure so at this point it's
[05:01:35] kind of like maybe it's just because the
[05:01:37] examples are presented that way it's
[05:01:39] kind of like surface a little bit more
[05:01:40] obvious examples right um I guess the
[05:01:44] the idea is that down the line might be
[05:01:46] able to detect more Nuance like
[05:01:48] deception or bugs or that kind of stuff
[05:01:50] yeah well I maybe I want to distinguish
[05:01:52] two things so um one is um the
[05:01:55] complexity of the feature or the concept
[05:01:57] right and the other is
[05:02:00] the the Nuance of the how subtle the
[05:02:03] examples we're looking at right so when
[05:02:05] we when we show the top data set
[05:02:07] examples those are the most extreme
[05:02:09] examples that that feature to to
[05:02:11] activate um and so it doesn't mean that
[05:02:13] it doesn't fire for more subtle things
[05:02:15] so the UN you know the insecure um code
[05:02:18] feature you know the stuff that it fires
[05:02:19] for most strongly for are these like
[05:02:21] really obvious you know disable the
[05:02:24] security type things um but um um you
[05:02:27] know uh it it also Fires for you know
[05:02:31] buffer overflows and and more subtle
[05:02:33] security vulnerabilities in code you
[05:02:35] know these features are all multimodal
[05:02:36] so you could ask like what images
[05:02:38] activate this feature and it turns out
[05:02:41] um that the uh the the security
[05:02:43] vulnerability feature activates for
[05:02:45] images of um uh like people clicking on
[05:02:48] Chrome to like go past the like you know
[05:02:51] this this website uh the SSL certificate
[05:02:53] might be wrong or something like this
[05:02:55] another thing that's very entertaining
[05:02:56] is there's backd doors en code feature
[05:02:57] like you activate it it goes and Cloud
[05:02:58] writes a back door that like will go and
[05:03:00] dump your data to port or something but
[05:03:02] you can ask okay what what images
[05:03:04] activate the back door feature it was
[05:03:06] devices with hidden cameras in them so
[05:03:08] there's a whole apparently genre of
[05:03:11] people going and selling devices that
[05:03:13] look in uous that have hidden cameras
[05:03:14] and they have ads that how there's a
[05:03:16] hidden camera in it and I guess that is
[05:03:18] the you know physical version of a back
[05:03:19] door um and so it sort of shows you how
[05:03:22] abstract these concepts are right um and
[05:03:24] I I just thought that was uh I I'm sort
[05:03:28] of sad that there's a whole Market of
[05:03:29] people selling devices like that but I
[05:03:30] was kind of delighted that that was the
[05:03:32] the thing that it came up with as the
[05:03:33] the top uh image examples for the
[05:03:35] feature yeah it's nice it's multimodal
[05:03:37] it's multi almost context it's it's as
[05:03:40] broad strong definition of a singular
[05:03:43] concept it's nice yeah to me one of the
[05:03:45] really interesting features especially
[05:03:47] for AI safety is deception and lying and
[05:03:51] the possibility that these kinds of
[05:03:53] methods could detect uh lying in a model
[05:03:56] especially gets smarter and smarter and
[05:03:57] smarter presumably that's a big threat
[05:04:01] of a super intelligent model that he can
[05:04:03] deceive the people operating
[05:04:06] it uh as to its intentions or any of
[05:04:09] that kind of stuff so what what have you
[05:04:10] learned from detecting lying inside
[05:04:12] models yeah so I think we're in some
[05:04:15] ways in early days for that we find
[05:04:19] quite a few features related to
[05:04:21] deception and lying there's one feature
[05:04:23] where fires for people lying and being
[05:04:26] deceptive and you force it active and
[05:04:28] Claude starts lying to you so we have a
[05:04:30] have a deception feature I mean there's
[05:04:32] all kinds of other features about
[05:04:33] withholding information and not
[05:04:34] answering questions features about power
[05:04:36] seeking and coups and stuff like that
[05:04:39] this a lot of features that are kind of
[05:04:40] related to Spooky things and if you um
[05:04:43] force them active Claude will will
[05:04:46] behave in ways that are they're not the
[05:04:48] kind of behaviors you want what are
[05:04:51] possible next exciting directions to you
[05:04:54] in the space of uh Mech and well there's
[05:04:56] a lot of things
[05:05:03] um so for one thing I would really like
[05:05:03] to get to a point where we have circuits
[05:05:05] where we can really understand um not
[05:05:08] just the features uh but then use that
[05:05:10] to understand the computation of models
[05:05:13] um that really for me is is the the
[05:05:15] ultimate goal of this um and there's
[05:05:18] been some work we we put out a few
[05:05:19] things there's a paper from Sam Marks
[05:05:21] that does some stuff like this there's
[05:05:22] been some I'd say some work around the
[05:05:24] edges here um but I think there's a lot
[05:05:26] more to do and I think that will be a
[05:05:28] very exciting thing um that's related to
[05:05:31] a challenge we call interference weights
[05:05:34] um where um due to supersition if you
[05:05:38] just sort of navely look at whether
[05:05:39] featur are connected together there may
[05:05:41] be some weights that sort of don't exist
[05:05:44] in the upstairs model but are just sort
[05:05:45] of artifacts of of superposition so
[05:05:47] that's a a sort of technical challenge
[05:05:49] related to that
[05:05:51] um I think another exciting direction is
[05:05:54] just I you know you might think of of
[05:05:57] sparse Auto encoders as being kind of
[05:05:59] like a telescope they allow us to you
[05:06:01] know look out and see all these features
[05:06:04] that are are are are out there and you
[05:06:06] know as we build better and better
[05:06:08] sparse Auto en Cutters get better better
[05:06:09] at dictionary learning we see more and
[05:06:11] more stars um and you know we zoom in on
[05:06:14] smaller and smaller stars but there kind
[05:06:16] of um a lot of evidence that we're only
[05:06:18] still seeing a very small fraction of
[05:06:20] the Stars there's a lot of matter in our
[05:06:23] in our you know neural network universe
[05:06:25] that we can't observe yet um and it may
[05:06:27] be that um that we'll never be able to
[05:06:29] have fine enough instruments to observe
[05:06:30] it and maybe maybe some of it just isn't
[05:06:32] possible um isn't computationally
[05:06:34] tractable to observant there's sort of a
[05:06:36] a kind of dark matter and in not in
[05:06:38] maybe the sense of of astronomy of
[05:06:40] earlier astronomy when we didn't know
[05:06:41] what this unexplained matter is um and
[05:06:43] so I I think a lot about that that dark
[05:06:45] matter and whether will ever observe it
[05:06:47] and what that means for safety if we if
[05:06:49] we can't observe it if there's you know
[05:06:51] some if some significant fraction of nor
[05:06:53] networks are not accessible to us um
[05:06:56] another question that I think a lot
[05:06:57] about is uh at the end of the day you
[05:07:02] know mechanistic inter is it's very
[05:07:04] microscopic um approach to interality
[05:07:06] it's trying to understand things in a
[05:07:07] very fine grained way but lot of the
[05:07:09] questions we care about are very
[05:07:11] macroscopic um you know we we care about
[05:07:14] these questions about neural network
[05:07:15] behavior and
[05:07:17] and I think that's the thing that I care
[05:07:19] most about but there's there's lots of
[05:07:20] other other sort of larger scale
[05:07:21] questions you you might care about um
[05:07:25] and somehow you know the nice thing
[05:07:28] about about having a very microscopic
[05:07:29] approach is it's maybe easier to ask you
[05:07:31] know is this true but the downside is
[05:07:33] it's much further from the things we
[05:07:34] care about and so we now have this
[05:07:36] ladder to climb and I think there's a
[05:07:37] question of can will we be able to find
[05:07:39] are there are there sort of larger scale
[05:07:41] abstractions that we can use to
[05:07:43] understand nural networks that can we
[05:07:44] get up from this very microscopic
[05:07:47] approach yeah you've you you've written
[05:07:49] about this this kind of organs question
[05:07:52] yeah exactly if we uh think of
[05:07:55] interpretability as a kind of anatomy of
[05:07:57] neural networks most of the circus
[05:07:59] threads involve studying tiny little
[05:08:00] veins looking at the small scale and
[05:08:03] individual neurons and how they connect
[05:08:05] however there are many natural questions
[05:08:07] that the small scale approach doesn't
[05:08:09] address in contrast the most prominent
[05:08:12] abstractions in biological Anatomy
[05:08:14] involve larger scale structures like
[05:08:16] individual organs like the heart or
[05:08:19] entire organ systems like the
[05:08:20] respiratory system and so we wonder is
[05:08:24] there a respiratory system or heart or
[05:08:26] brain region of an artificial neuron
[05:08:28] Network yeah exactly um and I mean like
[05:08:31] if you think about science right a lot
[05:08:32] of scientific Fields have um you know
[05:08:35] investigate things that many level of
[05:08:37] abstractions in biology you have like
[05:08:38] you know molecular biology studying you
[05:08:41] know proteins and molecules and so on
[05:08:42] and you have cellular biology and then
[05:08:44] you have histology studying tissues and
[05:08:46] you have anatomy and then you have
[05:08:48] zoology and then you have ecology and so
[05:08:50] you have many many levels of abstraction
[05:08:52] or you know physics maybe the physics of
[05:08:53] individual particles and then you know
[05:08:55] statistical physics gives you gives you
[05:08:57] thermodynamics and things like this and
[05:08:58] so you often have different levels of
[05:09:00] abstraction um and I think that right
[05:09:02] now we have you know mechanistic
[05:09:05] interpret if it succeeds is sort of like
[05:09:06] a microbiology of neural networks but we
[05:09:09] we want something more like anatomy and
[05:09:12] so and you know a question you might ask
[05:09:14] is why why can't you just go there
[05:09:15] directly and I think the answer is super
[05:09:18] um in at least in significant part it's
[05:09:19] that it's actually very hard to to see
[05:09:23] this this macroscopic structure U
[05:09:25] without first sort of breaking down the
[05:09:27] microscopic structure in the right way
[05:09:28] and then studying how it connects
[05:09:30] together um but I'm I'm hopeful that
[05:09:31] there is going to be something much
[05:09:33] larger than um features and circuits and
[05:09:36] that we're going to be able to have a
[05:09:37] story that's much than evolves much
[05:09:39] bigger things and you then you can sort
[05:09:41] of study in detail the parts you care
[05:09:43] about as opposed to neurobiology like a
[05:09:45] psychologist or psychiatrist when your
[05:09:47] own network and I think that the
[05:09:49] beautiful thing would be if we could go
[05:09:51] and rather than having disperate fields
[05:09:53] for those two things if you could have a
[05:09:55] build a bridge between them such that
[05:09:57] you could go and um uh have all of your
[05:10:01] higher level abstractions be grounded
[05:10:03] very firmly In This Very solid um you
[05:10:07] know more rigorous ideally Foundation
[05:10:11] what do you think is the difference
[05:10:12] between the human brain the biological
[05:10:15] neuron Network and the artificial neuron
[05:10:17] Network well the neuroscientists have a
[05:10:18] much harder job than us you know
[05:10:20] sometimes I just like count my blessings
[05:10:22] by how much easier my job is than the
[05:10:24] neuroscientist right so I have um we we
[05:10:26] can record from all the neurons yeah we
[05:10:28] can do that on arbitrary amounts of data
[05:10:31] um the neurons don't change while you're
[05:10:33] doing that by the way MH um you can go
[05:10:35] and ablate neurons you can edit the
[05:10:37] connections and so on um and then you
[05:10:39] undo those changes that's prettyy great
[05:10:41] yeah um you can force any you can
[05:10:43] intervene on any neuron and force it
[05:10:44] active and see what happens um you know
[05:10:46] which neurons are connected to
[05:10:47] everything right you neuroscientists
[05:10:49] want to get the connecto we have the
[05:10:50] connecto um and we have it for like much
[05:10:51] bigger than the elegant um and then not
[05:10:54] only do we have the connectome um we
[05:10:56] know uh what the you know which neurons
[05:10:58] excite or inhibit each other right so we
[05:11:00] have we it's not just that we know that
[05:11:01] like the binary mask we know the the
[05:11:03] weights um we can take gradients we know
[05:11:06] computationally what each neuron does um
[05:11:08] so I don't know the goes on and on we
[05:11:10] just have um so many advantages over
[05:11:13] neuroscientists and then despite having
[05:11:15] all those advantages it's really hard
[05:11:18] and so one thing I do sometimes think is
[05:11:20] like gosh like if it's this hard for us
[05:11:22] it seems impossible under the
[05:11:23] constraints of Neuroscience or you know
[05:11:25] near impossible um I I I don't know
[05:11:27] maybe maybe part of me is like I've got
[05:11:29] a few neuroscientists on my team maybe
[05:11:30] maybe I'm sort of like ah you know um
[05:11:32] the uh maybe the neuroscientists maybe
[05:11:34] some of them would like to have an
[05:11:35] easier problem that's still very hard um
[05:11:38] and they they could come and work on on
[05:11:40] neural networks and then after we after
[05:11:41] we figure out things in sort of the easy
[05:11:44] uh Little Pond of trying to understand
[05:11:45] neural networks which is still very hard
[05:11:47] then we then we could go back to
[05:11:49] biological Neuroscience I love what
[05:11:51] you've written about the goal of mechan
[05:11:53] turp research as uh two goals safety and
[05:11:56] Beauty so can you talk about the beauty
[05:11:58] side of things yeah so you know there's
[05:12:01] this funny thing where I think some
[05:12:03] people want uh some people are kind of
[05:12:05] disappointed by neural networks I think
[05:12:07] where they're like ah you know neural
[05:12:08] network
[05:12:09] um it's these just these simple rules
[05:12:11] then you just like do a bunch of
[05:12:12] engineering to scale it up and it works
[05:12:14] really well and like where's the like
[05:12:16] complex ideas you know this isn't like a
[05:12:17] very nice beautiful scientific
[05:12:20] result and I sometimes think when people
[05:12:22] say that I picture them being like you
[05:12:24] know evolution is so boring it's just a
[05:12:26] bunch of simple rules and you run
[05:12:28] Evolution for a long time and you get
[05:12:29] biology like what a what a a sucky uh
[05:12:32] you know way for biology to have turned
[05:12:34] out where's the the complex rules but
[05:12:36] the beauty is that the Simplicity
[05:12:38] generates complexity um you know biology
[05:12:41] has these simple rules and it gives rise
[05:12:43] to you know all the life and ecosystems
[05:12:46] that we see around us all the beauty of
[05:12:48] nature that all just comes from
[05:12:50] Evolution and from something very simple
[05:12:52] Evolution and similarly I think that
[05:12:54] nural networks build you know create
[05:12:57] enormous um complexity and Beauty inside
[05:12:59] and structure inside themselves that
[05:13:01] people generally don't look at and don't
[05:13:04] try to understand because it's it's hard
[05:13:05] to understand but I I think that there
[05:13:08] is an Inc incredibly Rich structure to
[05:13:11] be discovered inside n networks a lot of
[05:13:13] a lot of very deep Beauty um if we're
[05:13:16] just willing to take the time to go and
[05:13:18] see it and understand it yeah I love I
[05:13:21] love Mech inter the feeling like we are
[05:13:24] understanding or getting glimpses of
[05:13:26] understanding the magic that's going on
[05:13:28] inside is really wonderful it feels to
[05:13:30] me like one of the questions is just
[05:13:33] calling out to be asked and I'm sort of
[05:13:36] I mean a lot of people are think about
[05:13:37] this but I'm often surprised that morar
[05:13:40] is how is it that we don't know how to
[05:13:43] create computer systems that can do
[05:13:44] these things and yet we have these
[05:13:47] amazing systems that we don't know how
[05:13:49] to directly create computer programs
[05:13:50] that can do these things but these
[05:13:51] neural networks can do all these amazing
[05:13:52] things and it just feels like that is
[05:13:54] obviously the question that sort of is
[05:13:56] calling out to be answered if you are if
[05:13:58] you have any degree of curiosity it's
[05:14:00] it's like how is it that that Humanity
[05:14:02] now has these artifacts that can do
[05:14:04] these things that we don't know how to
[05:14:06] do yeah I love the image of the circus
[05:14:09] towards the light of the objective
[05:14:10] function yeah it's just it's it's this
[05:14:12] organic thing that we've grown and we
[05:14:13] have no idea what we've grown well thank
[05:14:15] you for working on safety and thank you
[05:14:17] for appreciating the beauty of the
[05:14:19] things you uh discover and thank you for
[05:14:21] talking today Chris this is wonderful
[05:14:23] thank you for taking the time to chat as
[05:14:24] well thanks for listening to this
[05:14:26] conversation with Chris Ola and before
[05:14:28] that with DAR amade and Amanda ascal to
[05:14:32] support this podcast please check out
[05:14:33] our sponsors in the description and now
[05:14:36] let me leave you with some words from
[05:14:37] Alan Watts
[05:14:39] the only way to make sense out of change
[05:14:42] is to plunge into it move with it and
[05:14:45] join the
[05:14:47] dance thank you for listening and hope
[05:14:49] to see you next time
