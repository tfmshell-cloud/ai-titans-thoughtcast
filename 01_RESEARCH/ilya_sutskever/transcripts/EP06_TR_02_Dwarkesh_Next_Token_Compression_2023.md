# Dwarkesh Patel: Ilya Sutskever — Why Next-Token Prediction Could Surpass Human Intelligence
- **YouTube URL:** https://www.youtube.com/watch?v=Yf1o0TQzry8
- **Lines:** 1336

---

[00:00:00] [Music]
[00:00:00] but I would not underestimate the
[00:00:02] difficulty of alignment of models that
[00:00:04] are actually smarter than us of models
[00:00:07] that are capable of misrepresenting
[00:00:09] their intentions are you worried about
[00:00:11] spies I'm really not worried about the
[00:00:13] weight it's being leaked we'll all be
[00:00:14] able to become more enlightened because
[00:00:16] we'd interact with an AGI that will help
[00:00:18] us see the world more correctly like
[00:00:21] imagine talking to the best meditation
[00:00:23] teacher in history Microsoft has been a
[00:00:25] very very good partner for us so I
[00:00:27] challenge the claim that next token
[00:00:29] prediction cannot surpass Human
[00:00:32] Performance if your base neuronet is
[00:00:34] smart enough you just ask it like what
[00:00:36] would a person is like great insight and
[00:00:39] visdom and capability
[00:00:42] do okay today I have the pleasure of
[00:00:44] interviewing Elia suit who is the
[00:00:47] co-founder and chief scientist of open
[00:00:50] AI IIA welcome to the lunar Society
[00:00:52] thank you happy to be here uh first
[00:00:54] question and no humility allowed there's
[00:00:56] many scientists or maybe not that many
[00:00:58] scientists who will make
[00:01:00] a big breakthrough in their field
[00:01:02] there's far fewer scientists who will
[00:01:03] make multiple independent breakthroughs
[00:01:05] that Define their field uh throughout
[00:01:07] their career what is the difference what
[00:01:09] like what what distinguishes you from
[00:01:10] other researchers why have you been able
[00:01:11] to find multiple breakthroughs in a
[00:01:12] field well thank you for the kind
[00:01:15] words it's hard to answer that question
[00:01:17] I
[00:01:18] mean I try really hard I gave it
[00:01:21] everything you
[00:01:22] got
[00:01:24] and that worked so far I think that's
[00:01:28] all there is to it got it um what's the
[00:01:31] explanation for why there aren't more
[00:01:33] illicit uses of GPT why aren't more
[00:01:35] foreign governments using it to spread
[00:01:37] propaganda or scam grandmothers or
[00:01:40] something I
[00:01:41] mean maybe they
[00:01:43] haven't really gotten to do it a lot but
[00:01:47] it also wouldn't surprise me if some of
[00:01:48] it was going on right now certainly I
[00:01:51] imagine they'd be taking some of the
[00:01:52] open source models and trying use them
[00:01:54] for that
[00:01:56] purpose like I sure I would expect this
[00:01:58] would be something that'd be interested
[00:02:00] in in the future it's like technically
[00:02:02] possible they just haven't thought about
[00:02:03] it enough or haven't like done it at
[00:02:06] scale using their technology or maybe
[00:02:07] it's happening but you don't know it
[00:02:09] would you be able to track it if it was
[00:02:10] happening I think large scale tracking
[00:02:13] is possible yes I mean this requires a
[00:02:15] all Special Operation that is possible
[00:02:17] MH um now there's some window in which
[00:02:21] uh AI is very economically valuable on
[00:02:23] the scale of airplanes let's say but we
[00:02:24] haven't reached AGI yet how big is that
[00:02:27] window I mean I think this window it's
[00:02:29] hard to give you precise answer but it's
[00:02:31] definitely going to be like a good
[00:02:32] multi-year window it's also a question
[00:02:34] of definition
[00:02:36] because AI before it becomes
[00:02:40] AGI is going to be increasingly more
[00:02:43] valuable year after year i' say in an
[00:02:46] exponential way so it's some in some
[00:02:48] sense it may feel like especially in
[00:02:51] hindsight it may feel like there was
[00:02:52] only one year or two years because those
[00:02:54] two years were larger than the previous
[00:02:56] years but I would say that already
[00:03:00] last year there've been a fair amount of
[00:03:05] economic value produced by Ai and next
[00:03:07] year it's going to be larger and larger
[00:03:08] after that so I think like that it's
[00:03:11] going to be a good multi multi-year
[00:03:13] chunk of time but that's going to be
[00:03:15] true I would say from now to legi pretty
[00:03:18] much okay well because I'm curious if
[00:03:20] there's a startup that's using your
[00:03:21] models right um at some point if you
[00:03:24] have hii there's only one business in
[00:03:25] the world right it's open AI how how
[00:03:27] much window do they have do any business
[00:03:29] have where they're actually producing
[00:03:31] something that AGI can't produce yeah
[00:03:33] well I mean it's the same it's the same
[00:03:35] question is asking how long until AGI
[00:03:37] yeah I think it's a hard question to
[00:03:39] answer I mean I hesitate to give you a
[00:03:40] number also because there is the stain
[00:03:43] whereare effect where people who
[00:03:45] are optimistic people who are working on
[00:03:47] the technology tend to underestimate the
[00:03:50] time it takes to get there but I think
[00:03:52] that the way I ground myself is by
[00:03:53] thinking about the self-driving car in
[00:03:55] particular there is an analogy where if
[00:03:57] you look at the a Tesla and if you look
[00:04:01] at the self-driving behavior of it it
[00:04:03] like it looks like it does
[00:04:05] everything it does everything all right
[00:04:08] but it's also clear that there is still
[00:04:09] a long way to go in terms of reliability
[00:04:12] and we might be in a similar place with
[00:04:14] respect to our models where it also
[00:04:16] looks like we can do everything and at
[00:04:18] the same time it will be we'll need to
[00:04:21] do some more work until we really iron
[00:04:24] out all the issues and make it really
[00:04:26] good and really reliable and robust and
[00:04:28] well behaved by 2030 what percent of GDP
[00:04:31] is AI oh gosh hard to answer that
[00:04:33] question very hard to answer that
[00:04:34] question give me an over
[00:04:35] under like the problem is that my AR
[00:04:37] bars in Lo scale so I could imagine like
[00:04:39] I could imagine like a huge percentage I
[00:04:41] could imagine a disappointing small
[00:04:42] percentage at the same time okay so
[00:04:44] let's take the counterfactual where it
[00:04:46] is a small percentage let's say it's
[00:04:47] 2030 and you know not that much economic
[00:04:50] value has been created by these Elms as
[00:04:51] unlikely as you think this might be what
[00:04:54] is what would be your best explanation
[00:04:55] right now why something like this might
[00:04:57] happen my best explanation so I really
[00:05:01] don't think that's a likely
[00:05:03] possibility so that's that's the preface
[00:05:05] to to the comment but if I were to take
[00:05:09] the premise of your question well like
[00:05:10] why were things disappointing in terms
[00:05:12] of the real world impact and my answer
[00:05:15] would be reliability if somehow it ends
[00:05:18] up being the case
[00:05:21] that you really want them to be reliable
[00:05:23] and they ended up not being reliable or
[00:05:25] if reliability turn out to be harder
[00:05:28] than we expect I really don't think that
[00:05:30] will be the case but if I had to pick
[00:05:32] one if I had to pick one and you tell me
[00:05:35] like hey like why didn't things work out
[00:05:37] it would be reliability that you still
[00:05:39] have to look over the answers and double
[00:05:41] check everything and that just really
[00:05:44] puts a damper on the economic value that
[00:05:46] can be produced by those systems they'll
[00:05:47] be technologically mature it's just a
[00:05:49] question of whether they'll be reliable
[00:05:51] enough yeah well in some sense not
[00:05:52] reliable means not technologically
[00:05:54] mature if you see what I mean yeah fair
[00:05:56] enough um what's after generative models
[00:05:58] right so before you're working on
[00:06:00] reinforcement learning is this is this
[00:06:02] basically it is this a paradigm that
[00:06:03] gets us to AI or is there something
[00:06:05] after this I mean I think this Paradigm
[00:06:06] is going to go really really far and I
[00:06:08] would not underestimate it I think it's
[00:06:09] quite likely that this exact Paradigm is
[00:06:12] not going to be the Qui AGI form factor
[00:06:16] I mean I hesitate to say precisely what
[00:06:18] the next Paradigm will
[00:06:20] be but I think it will probably involve
[00:06:23] integration of all the different ideas
[00:06:25] that came that came in the past is there
[00:06:27] some specific one you're referring to or
[00:06:31] I mean it's hard to be specific so you
[00:06:34] could argue that the next token
[00:06:35] prediction can only help with match
[00:06:37] Human Performance uh and maybe not
[00:06:40] surpass it what would it take to surpass
[00:06:41] Human Performance so I challenge the
[00:06:43] claim that next token prediction cannot
[00:06:45] surpass Human
[00:06:48] Performance it looks like on the surface
[00:06:51] it cannot it looks on the surface if you
[00:06:53] just learn to imitate to predict what
[00:06:57] people do it means that you can only
[00:06:59] copy people
[00:07:00] but the here is a cter argument for
[00:07:02] white might not be quite so if your
[00:07:05] neural net is if your base neural net is
[00:07:07] smart enough you just ask it like what
[00:07:10] would what would a person with great
[00:07:13] insight and visent capability do maybe
[00:07:16] such person doesn't exist but there's a
[00:07:18] pretty good chance that the neural net
[00:07:19] will be able to extrapolate how such a
[00:07:22] person should behave do you see what I
[00:07:24] mean yes although where were to get the
[00:07:26] sort of insight about what that person
[00:07:28] would do if not from from the data of
[00:07:31] regular people because like if you think
[00:07:32] about it what does it mean to predict
[00:07:34] the next token well enough what does it
[00:07:37] mean actually it's actually it's a much
[00:07:38] it's a deeper question than it seems
[00:07:40] predicting the next token well means
[00:07:42] that you
[00:07:45] understand the underlying
[00:07:48] reality that led to the creation of that
[00:07:51] token it's not statistics like it is
[00:07:54] statistics but what is
[00:07:56] statistics in order to to understand the
[00:07:59] statistics to compress them you need to
[00:08:02] understand what is it about the world
[00:08:04] that creates this those statistics and
[00:08:07] so then you say okay well I have all
[00:08:08] those people what is it about people
[00:08:10] that creates their behaviors well they
[00:08:12] have you know they they have thoughts
[00:08:13] and they have feelings and they have
[00:08:15] ideas and they do things in certain ways
[00:08:17] all of those would be deduced from next
[00:08:21] token prediction and I'd argue that this
[00:08:24] should make it possible not indefinitely
[00:08:27] but to a to a pretty decent degree to
[00:08:29] say well can you guess what you what
[00:08:31] You' do if you took a person with like
[00:08:33] this characteristic and that
[00:08:34] characteristic like such a person
[00:08:36] doesn't exist but because you're so good
[00:08:39] at predicting an nexttoken you should
[00:08:40] still be able to guess what that person
[00:08:42] would do this hypothetical imaginary
[00:08:45] person is far greater mental ability
[00:08:48] than the rest of us um when we're doing
[00:08:51] reinforcement learning on these models
[00:08:52] how long before most of the data for the
[00:08:54] reinforcement learning is coming from Ai
[00:08:56] and not
[00:08:58] humans I'm mean already most of data for
[00:09:01] reinforcement learning is coming from AI
[00:09:03] yeah well it's like the humans are being
[00:09:06] used to train the reward function but
[00:09:09] then but then the reward function inter
[00:09:12] in its interaction with the model is
[00:09:13] automatic and all the data that's
[00:09:15] generated in the during the process of
[00:09:17] reinforcement learning it's created by
[00:09:18] AI so like if you look at the
[00:09:22] current I would say technique Paradigm
[00:09:25] which is been getting some significant
[00:09:27] attention because of Chad GPT
[00:09:29] reinforcement learning from Human
[00:09:30] feedback so there is human feedback the
[00:09:32] human feedback is being used to train
[00:09:35] the reward function and then the reward
[00:09:38] function is being used to create the
[00:09:39] data which trains them up got it and is
[00:09:41] there any hope of just removing the
[00:09:42] human from the loop and have it improve
[00:09:44] itself and some sort of alpha go away
[00:09:46] yeah definitely I mean I feel like in
[00:09:47] some sense our hopes
[00:09:49] for like our plan like very much so the
[00:09:54] thing you really want is for the human
[00:09:57] teachers that tell that teach the AI for
[00:10:01] them to collaborate with an AI you might
[00:10:03] want to think about it and you might
[00:10:05] want to think of it as being in a world
[00:10:07] where the human teachers do 1% of the
[00:10:09] world and the work and the AI do 99% of
[00:10:11] the work you don't want it to be 100% AI
[00:10:14] but you do want it to be a human machine
[00:10:16] collaboration which teaches the next
[00:10:18] machine so currently I mean i' had a
[00:10:20] chance to play around these models they
[00:10:21] seem U bad at multi-step reasoning and
[00:10:24] they have them getting better but what
[00:10:25] does it take to really surpass that
[00:10:27] barrier I mean I think think dedicated
[00:10:30] training will get us there more more
[00:10:32] improvements of the base models will get
[00:10:33] us there
[00:10:37] but like fundamentally I also don't feel
[00:10:39] like they're that bad at multi-step
[00:10:41] reasoning I actually think that they are
[00:10:43] bad at mental multi-step reasoning but
[00:10:44] they're not allowed to think out loud
[00:10:47] but when they are allowed to think out
[00:10:48] loud they're quite good and I expect
[00:10:50] this to improve
[00:10:52] significantly both with better models
[00:10:55] and with special training are you
[00:10:57] running out of reasoning tokens on the
[00:10:58] internet are there enough of them I mean
[00:11:01] you know so okay so for for context on
[00:11:04] this question like there is there are
[00:11:05] claims that indeed at some point will
[00:11:07] run out of tokens in general to train
[00:11:09] those models and yeah I think this will
[00:11:11] happen one day and we by the time that
[00:11:13] happens we need to have other ways of
[00:11:15] training models other ways of
[00:11:17] productively improving their
[00:11:19] capabilities and sharpening their
[00:11:20] behavior making sure they're doing
[00:11:22] exactly precisely what we want without
[00:11:25] more data well I you haven't run out of
[00:11:28] data yet there's more yeah I would say I
[00:11:30] would say the data situation is still
[00:11:32] quite good there's still lots to go but
[00:11:34] at some point yeah at some point data
[00:11:35] will run okay where what is the most
[00:11:38] valuable source of data is it Reddit
[00:11:40] Twitter books what would you trade many
[00:11:43] other tokens of other varieties
[00:11:45] for generally speaking you'd like tokens
[00:11:47] which are speaking about smarter things
[00:11:50] tokens which are like more interesting
[00:11:53] yeah so I mean all the all the sources
[00:11:56] which you mentioned they're valuable
[00:11:57] okay so maybe not Twitter but um
[00:12:00] uh do we need to go multimodal to get
[00:12:01] more tokens or do we still have enough
[00:12:03] text tokens left I mean I think that you
[00:12:05] can still go very far in text only but
[00:12:07] going multimodel seems like a very
[00:12:08] fruitful Direction M if you're
[00:12:10] comfortable talking about this like
[00:12:11] where is the place where we haven't
[00:12:12] scraped the tokens yet oh I
[00:12:15] mean yeah obviously I mean I can't
[00:12:17] answer that question for us but I'm sure
[00:12:19] I'm sure that for everyone there's a
[00:12:21] different answer to that question how
[00:12:23] how many orders of magnitude Improvement
[00:12:24] can we get just not from scale or not
[00:12:26] from data but just from algorithmic
[00:12:28] Improv
[00:12:30] hard to answer but I'm sure there is
[00:12:32] some is some a lot or is some a little I
[00:12:35] mean it's only one way to find out okay
[00:12:38] let me get your like quick fire opinions
[00:12:39] about these different research
[00:12:40] directions retrieval Transformers so
[00:12:43] just like somehow storing the data
[00:12:44] outside of the model itself and
[00:12:46] retrieving it somehow seems promising
[00:12:49] but do you see that as a path forward or
[00:12:51] I I think it seems promising uh robotics
[00:12:53] was it the right step for open AI to
[00:12:56] leave that behind yeah it was like back
[00:12:59] then it really wasn't possible to
[00:13:01] continue working in robotics because
[00:13:03] there was so little data like back then
[00:13:06] if you wanted to do an robot if you
[00:13:07] wanted to work on robotics you needed to
[00:13:09] become a robotics company you needed to
[00:13:11] really have a giant group of people
[00:13:15] working on building robots and
[00:13:16] maintaining them and
[00:13:19] having and even then like if you only if
[00:13:22] you're going to have 100 robots it's a
[00:13:23] giant operations already but you're not
[00:13:25] going to get that much data so in a
[00:13:27] world where
[00:13:29] most of the progress comes from the
[00:13:31] combination of compute and data right
[00:13:34] that's where we've been where it was the
[00:13:36] combination of compute and data that
[00:13:38] drove the progress there was no path to
[00:13:41] data from
[00:13:43] robotics so back in the day that you
[00:13:46] made a decision to stop working in
[00:13:48] robotics there was no path
[00:13:50] forward is there one
[00:13:52] now so I'd say that now it is possible
[00:13:56] to create a path forward but one needs
[00:13:58] to really commit to the to the to the
[00:14:01] task of Robotics you really need to say
[00:14:03] I'm going to
[00:14:04] build like many thousands tens of
[00:14:08] thousands hundreds of thousands of
[00:14:09] robots and somehow collect data from
[00:14:12] them and find a gradual path where the
[00:14:14] robots are doing something slightly more
[00:14:15] useful and then the data that they get
[00:14:17] from these Rob and then the data that is
[00:14:20] obtained and used to train the models
[00:14:21] they do something slightly more useful
[00:14:22] so you could imagine this kind of
[00:14:23] gradual path of improvement you build
[00:14:25] more robots they do more things you
[00:14:27] collect more data and so on but you
[00:14:29] really need to be committed to this path
[00:14:31] if you say I want to make robotics
[00:14:33] happen that's what you need to do I
[00:14:35] believe that there are companies who are
[00:14:36] thinking about such doing exactly that
[00:14:40] but I think that you need to really love
[00:14:42] robots and need to be really willing to
[00:14:44] solve all the physical and logistical
[00:14:46] problems of dealing with them it's not
[00:14:48] the same as software at all so I think
[00:14:52] one could make progress in robotics
[00:14:53] today with enough motivation uh what
[00:14:56] ideas are you excited to try but you
[00:14:58] can't because it don't work well on
[00:14:59] current Hardware I don't think current
[00:15:02] Hardware is a limitation okay I think
[00:15:04] it's just not the case got it so but
[00:15:06] anything you want to try you can just
[00:15:07] spin it up or I mean of course like this
[00:15:10] the thing you you might say well I wish
[00:15:12] current Hardware was cheaper or maybe it
[00:15:15] had
[00:15:16] higher like may maybe it would be better
[00:15:18] if it was higher memory processor band
[00:15:20] we let's
[00:15:23] say
[00:15:24] but by and large hard way is just
[00:15:27] limitation let's talk about alignment do
[00:15:30] you think we'll ever have a mathematical
[00:15:32] definition of
[00:15:33] alignment mathematical definition I
[00:15:35] think is unlikely uhhuh like I do I do
[00:15:38] think that we will instead have multiple
[00:15:41] like like rather than rather than
[00:15:42] achieving one mathematical definition I
[00:15:45] think we'll achieve multiple definitions
[00:15:47] that look at alignment from different
[00:15:50] aspects and I think that this is how we
[00:15:52] will get the assurance that we want and
[00:15:55] by which I mean you can look at the
[00:15:56] behavior you can look at the behavior in
[00:15:59] various
[00:15:59] test um in various adversarial stress
[00:16:03] situations you can look at how the
[00:16:04] neural net operates from the
[00:16:07] inside I think you have to look at all
[00:16:09] several of these factors at the same
[00:16:12] time and how short do you have to be
[00:16:14] before you release a model in the while
[00:16:15] is it 100% 95% well depend how capable
[00:16:17] the model is the more capable the model
[00:16:20] is the more the more higher the the more
[00:16:23] confident to be okay so just say it's
[00:16:25] something that's almost AGI where is Agi
[00:16:27] well depends what your AGI can do keep
[00:16:28] in mind AGI is an ambiguous term also
[00:16:30] like like
[00:16:33] your average college undergrad is an AGI
[00:16:36] right it's yeah but you see what I mean
[00:16:40] there's significant bity in terms of
[00:16:42] what is meant by hii and so depending on
[00:16:44] where you put this Mark you need to be
[00:16:48] more or less confident well you
[00:16:50] mentioned a few of the paths towards
[00:16:51] alignment earlier what is the one you
[00:16:52] think is most promising at this point
[00:16:54] like I think that it will be a
[00:16:56] combination I really think that you will
[00:16:58] not want to have just one approach I
[00:17:00] think people want to
[00:17:02] have a combination of approaches where
[00:17:05] we you spend a lot of compute adversar
[00:17:07] probit to find any mismatch between the
[00:17:10] behavior that you wanted to teach and
[00:17:12] the behavior that it exhibits we look
[00:17:14] inside into the neural net using another
[00:17:17] neural to understand how it how it
[00:17:19] operates on the inside I think all of
[00:17:21] them will be necessary every approach
[00:17:24] like this reduces the probability of
[00:17:27] misalignment
[00:17:29] and you also want to be in a world where
[00:17:32] you're degree of alignment keeps of
[00:17:34] increasing faster than the capability of
[00:17:37] the models I would say that right now
[00:17:39] our understanding of our models is still
[00:17:42] quite rudimentary we made some progress
[00:17:45] but much more progress is possible and
[00:17:47] so I would expect that ultimately the
[00:17:48] thing that will really succeed is when
[00:17:50] we will have a small neural net that is
[00:17:53] well understood that's given the task to
[00:17:55] study the behavior of a large neural
[00:17:57] that is not understood to verify
[00:17:59] by what point is most of the research
[00:18:01] being done by AI I mean so today when
[00:18:04] you use co-pilot right what fraction how
[00:18:07] how how do you do do the how do you
[00:18:09] divide it up so I expect at some point
[00:18:11] you ask your you know descendant of chat
[00:18:14] GPT you say hey like I'm thinking about
[00:18:15] this and this can you suggest fruitful
[00:18:17] ideas I should try and you would
[00:18:19] actually get fruitful
[00:18:20] ideas right and I think that will make
[00:18:22] it possible for you to solve problems
[00:18:23] you could solve before got it but it's
[00:18:25] somehow just telling the humans giving
[00:18:27] them ideas a faster something it's not
[00:18:29] itself interacting with the one example
[00:18:31] I mean you could you could slice it in
[00:18:32] in a variety of ways but I think the
[00:18:34] bottl link there is good ideas good
[00:18:37] insights and that's something which the
[00:18:38] neural net could help with if you could
[00:18:40] design some like a billion dollar prize
[00:18:42] for some sort of alignment research
[00:18:44] results uh or product what is like the
[00:18:46] concrete Criterion set for that billion
[00:18:48] dollar price there something that makes
[00:18:49] sense for such a price I it's it's funny
[00:18:51] that you asked this I was actually
[00:18:52] thinking about this exact question I
[00:18:54] haven't I haven't come up with an exact
[00:18:55] criteria yet maybe something that be the
[00:18:59] benef maybe a prize
[00:19:01] where we could say that two years later
[00:19:06] or three year or five years later we'll
[00:19:07] look back and say like that was the main
[00:19:10] result so rather than say that there is
[00:19:12] a priz committee that decides right away
[00:19:15] be wait for five years and then award it
[00:19:17] retroactively but there's no concrete
[00:19:19] thing we can identify yet as it like you
[00:19:21] solve this particular problem and you're
[00:19:23] you made a lot of progress I think a lot
[00:19:25] of progress yes I wouldn't say that this
[00:19:27] would be the
[00:19:29] the full thing MH do you think end to
[00:19:31] end training is the right architecture
[00:19:34] for bigger and bigger models or do they
[00:19:36] do we need better ways of just
[00:19:37] connecting things together I think end
[00:19:40] to end training is very promising I
[00:19:41] think connecting things together is very
[00:19:42] promising everything is promising so
[00:19:45] open AI is projecting revenues of a
[00:19:47] billion dollars in 2024 um that might
[00:19:50] very well be correct but I'm just
[00:19:51] curious when you're talking about a new
[00:19:53] general purpose technology how do you
[00:19:55] estimate how big a windfall it will be
[00:19:58] like have why that particular number I
[00:20:00] mean you look at the current you look at
[00:20:02] the you know we we've already had a we
[00:20:04] so we've had a
[00:20:06] product for quite a while now for back
[00:20:08] from the gpt3 days from two years ago
[00:20:10] through the API and we've seen how it
[00:20:12] grew we've seen how the response to D
[00:20:15] has grown as well and so you see how the
[00:20:17] response to chat gpts and I think all of
[00:20:19] this gives us information that allows us
[00:20:21] to make a relatively sensible
[00:20:24] extrapolation to
[00:20:25] 2024 maybe that would be that' be one
[00:20:28] answer like you need to have data you
[00:20:29] can't come up with those things out of
[00:20:30] thin air because otherwise your error
[00:20:32] bars will be like off by your error bars
[00:20:36] are going to be like 100x in each
[00:20:38] Direction I mean but most exponentials
[00:20:40] don't stay exponential uh especially
[00:20:42] when they get into bigger and bigger
[00:20:43] quantities right so how do you determine
[00:20:45] in this case that I mean like would you
[00:20:48] bet against
[00:20:50] thei uh not after talking with you um
[00:20:54] let's talk about what like a post AI
[00:20:55] future looks like so are people like you
[00:20:57] you know I'm guessing you're working
[00:20:58] like 80 hour weeks towards some this
[00:21:00] Grand goal that you're really obsessed
[00:21:01] with are you going to be satisfied in a
[00:21:03] world where you're basically living in
[00:21:04] an AI retirement home or like what what
[00:21:06] is a word what is like your what are you
[00:21:08] concretly doing after AI comes I think
[00:21:11] the question of what what I'll be doing
[00:21:14] or what people will be doing after AI
[00:21:16] come it's a very tricky question you
[00:21:18] know I think where where will people
[00:21:19] find meaning but I think I think that
[00:21:21] that's something that AI could help us
[00:21:23] me
[00:21:26] like one thing I imagine is that we'll
[00:21:30] all be able to become more enlightened
[00:21:32] because we' interact with an AGI that
[00:21:34] will help us see the world more
[00:21:36] correctly become better on the inside as
[00:21:39] a result of intera like imagine talking
[00:21:41] to the best meditation teacher in
[00:21:43] history I think that will be a helpful
[00:21:45] thing but I also think that because the
[00:21:48] world will change a lot it will be very
[00:21:50] hard for people to
[00:21:51] understand what is happening precisely
[00:21:54] and how to and how to really contribute
[00:21:57] one thing that I think
[00:21:59] some people will choose to do is to
[00:22:01] become part AI in order to really expand
[00:22:04] their minds and understanding to really
[00:22:06] be able to solve the hardest problems
[00:22:08] that Society will face then are you
[00:22:10] going to become part ofi very tempting
[00:22:13] it is tempting yeah what do you think
[00:22:15] there'll be physically embodied humans
[00:22:16] in 3,000 3,000 oh how do I know what's
[00:22:20] going to happen in 3,000 like what does
[00:22:22] it look like are there still like humans
[00:22:23] walking around on Earth or have you guys
[00:22:25] thought concretely about what you
[00:22:26] actually want this world to look like
[00:22:27] 3,000 well I mean that that that the
[00:22:29] thing is here's the thing like let let
[00:22:31] me describe to you what I think is not
[00:22:33] quite right about the question like it
[00:22:34] implies like oh like we get to decide
[00:22:37] how we want the world to look like I
[00:22:40] don't think that picture is correct I
[00:22:41] think change is the only constant and so
[00:22:44] of course even after AGI is built it
[00:22:46] doesn't mean that the world will be
[00:22:48] static the world will continue to change
[00:22:50] the world will continue to evolve and it
[00:22:53] will go through all kinds of
[00:22:55] Transformations and I really have no I
[00:22:57] don't think anyone has any idea of how
[00:23:00] the world will look like in 3000 but I
[00:23:03] do hope that there will be a lot of
[00:23:05] descendants of human beings who will
[00:23:07] live happy fulfilled lives where they
[00:23:08] are free to do as their wish as they see
[00:23:11] fit or they are the ones who are solving
[00:23:14] their own problems like one of the
[00:23:15] things which I would not want one one
[00:23:17] one world which I would find very
[00:23:18] unexciting is one where you know we bu
[00:23:21] this powerful tool and then the
[00:23:22] government said okay so the AGI said
[00:23:25] that Society should be run in such a way
[00:23:27] and now we should run Society in such
[00:23:28] away I'd much rather have a world where
[00:23:32] people are still free to make their own
[00:23:34] mistakes and suffer their consequences
[00:23:36] and gradually evolve morally and
[00:23:40] progress forward on their own through
[00:23:41] their own strength see what I mean with
[00:23:43] the AGI providing more like a base
[00:23:45] safety net how much time do you spend
[00:23:47] thinking about these kinds of things
[00:23:48] versus just doing the research that I do
[00:23:51] think about those things a fair bit yeah
[00:23:52] think those are very interesting
[00:23:53] questions so in what ways have the
[00:23:56] capabilities we have today in what ways
[00:23:57] have they surpassed where you expected
[00:23:59] them to be in 2015 and in what ways are
[00:24:01] they still not where you would expected
[00:24:02] them to be by this point I mean In
[00:24:06] fairness did it surpass what I expect
[00:24:07] them to be in 2015 in in 2015 I my
[00:24:10] thinking was a lot more I just don't
[00:24:12] want to bet against deep learning I want
[00:24:14] to make the biggest possible bet on deep
[00:24:16] learning don't know how but it will
[00:24:18] figure it out but is there any specific
[00:24:20] way in which it's uh been more than you
[00:24:23] expected or less than you expected like
[00:24:25] some concrete prediction you had in 2015
[00:24:26] that's been anounced you know
[00:24:30] unfortunately I don't remember concrete
[00:24:31] predictions I made in 2015 but I
[00:24:33] definitely but I definitely think that
[00:24:35] overall in
[00:24:37] 2015 I just want to to move to make the
[00:24:42] biggest bet possible on deep learning
[00:24:44] but I didn't know exactly I didn't have
[00:24:46] a specific idea of how far things will
[00:24:48] go in seven years well I mean 2015 I did
[00:24:51] have all these best with people in 2016
[00:24:53] maybe 2017 that things will go really
[00:24:56] far but
[00:24:58] specifics so it's like it's both it's
[00:25:01] both the case that it surprised me and I
[00:25:03] was making these aggressive predictions
[00:25:06] but I think maybe I believe them only
[00:25:07] only only 50% on the inside uhhuh well
[00:25:10] what do you believe now that even most
[00:25:11] people at open a would find
[00:25:13] farfetched I mean I think that at this
[00:25:16] because we communicate a lot of open AI
[00:25:18] people have a pretty good sense of what
[00:25:19] I think and so yeah we we reached the
[00:25:22] point at open air I think we see I to ey
[00:25:24] on all these questions so Google has you
[00:25:26] know it's custom TPU Hardware it has all
[00:25:28] this data from all its users you know
[00:25:30] Gmail what um and so on does it give it
[00:25:33] an advantage in terms of training bigger
[00:25:34] models and better models than you so I
[00:25:37] think like when first at first when the
[00:25:39] TPU came out I was really impressed and
[00:25:40] I thought wow this is amazing but that's
[00:25:42] because I didn't quite understand harder
[00:25:44] back then what really turned out to be
[00:25:47] the case is that tpus and gpus are
[00:25:50] almost the same thing they are very very
[00:25:54] similar it's like I think a GPU chip is
[00:25:57] a little bit bigger I think a TPU chip
[00:26:00] is a little bit smaller it may be a
[00:26:01] little bit cheaper but then they make
[00:26:02] more gpus than tpus so I think the the
[00:26:05] gpus might be cheaper after all but
[00:26:07] fundamentally you have a big
[00:26:09] processor and you have a lot of memory
[00:26:12] and there is a bottl link between those
[00:26:14] two and the problem that both the TPU
[00:26:17] and the GPU are trying to solve is that
[00:26:19] by the the amount of time it takes you
[00:26:21] to move one floating point from the
[00:26:22] memory to the processor you can do
[00:26:25] several 100 floating Point operations on
[00:26:27] the processor which means that you have
[00:26:28] to do some kind of batch processing and
[00:26:31] in this sense both of these
[00:26:32] architectures are the same so I I really
[00:26:34] feel like Hardware like in some sense
[00:26:37] the only thing that matters about
[00:26:38] Hardware is cost cost per
[00:26:40] flop overall systems cost okay there
[00:26:43] that there isn't much that much
[00:26:45] difference well actually don't know I
[00:26:46] mean I don't know how much what what
[00:26:48] what the TPU costs are but I would
[00:26:50] suspect that probably not if anything
[00:26:53] probably use are more expensive because
[00:26:55] there is less of them when you're doing
[00:26:57] your work how much of the time is spent
[00:26:58] when you know configuring the right
[00:27:01] initializations making sure the training
[00:27:02] run goes well and getting the right
[00:27:04] hyper parameters and how much is it just
[00:27:05] coming up with whole new ideas I would
[00:27:07] say it's a combination but I think that
[00:27:09] coming up with It's a combination but
[00:27:11] coming up with whole new ideas is
[00:27:12] actually not it's it's like a Modest
[00:27:16] part of the work certainly coming up
[00:27:17] with new ideas is important but I think
[00:27:19] even more important is to understand the
[00:27:22] results to understand the existing ideas
[00:27:24] to understand what's going on because
[00:27:25] normally you have these you know neur is
[00:27:27] a very complic get a system right and
[00:27:29] you ran it and you get some Behavior
[00:27:31] which is hard to understand what's going
[00:27:34] understanding the results figuring out
[00:27:36] what next next experiment to run a lot
[00:27:38] of the time is spent on that
[00:27:40] understanding what could be wrong what
[00:27:42] could have caused the the neural net
[00:27:45] produce a result which was not expected
[00:27:48] i' say a lot of time we spend as well of
[00:27:50] course coming up with new ideas but not
[00:27:51] new ideas I think like I don't I don't
[00:27:54] like this this um framing as much it's
[00:27:58] not that it's false but I think the main
[00:28:00] activity is actually
[00:28:02] understanding how what do you see is the
[00:28:04] difference between the two so at least
[00:28:06] in my mind when you say come up with new
[00:28:08] ideas I'm like oh like what happened if
[00:28:09] it did such and such whereas
[00:28:12] understanding it's more like like what
[00:28:13] is this whole thing like what are the
[00:28:15] real
[00:28:16] underlying phenomena that are going on
[00:28:19] what are the what are the underlying
[00:28:20] effects like why why are we doing things
[00:28:23] this way not another way and of course
[00:28:24] this is very adjacent to what can be
[00:28:27] described as coming up with ideas but I
[00:28:29] think the understanding part is where
[00:28:31] the real action takes place does that
[00:28:33] describe your entire career like if you
[00:28:34] think back on like image net or
[00:28:36] something was that more a new idea or
[00:28:37] was that more understanding oh I was
[00:28:39] definitely understanding definitely
[00:28:40] understanding it was a new understanding
[00:28:42] of very old things what is the
[00:28:45] experience of training on Azure been
[00:28:48] like using Azure fantastic I mean yeah I
[00:28:51] mean Microsoft has been a very very good
[00:28:53] partner for us and they've
[00:28:55] really helped
[00:28:58] take Azure and make it bring it to a
[00:29:00] point where it's really good for
[00:29:03] ML and they're super happy with it how
[00:29:06] um how vulnerable is the whole AI
[00:29:08] ecosystem do something that might happen
[00:29:10] in Taiwan so let's say there's like a
[00:29:11] tsunami uh in Taiwan or something what
[00:29:14] would what happens to AI in general like
[00:29:16] it's it's definitely going to be a
[00:29:17] significant setback uhuh it's not going
[00:29:19] to like it might be something equivalent
[00:29:22] to like no one will be able to get more
[00:29:25] more computes for a few years but I
[00:29:27] expect comput will spring up like for
[00:29:29] example I believe that Intel has Fabs
[00:29:31] just of the previous of like a few
[00:29:32] Generations ago so that means that if
[00:29:34] intel wanted to they could produce
[00:29:36] something GPU like from like four years
[00:29:39] ago so yeah it's not the best let's say
[00:29:42] I'm actually not sure about if
[00:29:44] if if my statement about Intel is
[00:29:46] correct but I do know that there are
[00:29:48] Fabs outside of Taiwan they're just not
[00:29:50] as good but you can still use them and
[00:29:53] still go very far with them it's just it
[00:29:56] just cost it's just a setback well iner
[00:29:58] get cost prohibitive as these models get
[00:29:59] bigger and bigger so I have a different
[00:30:01] way of looking at this question yeah
[00:30:03] it's not that inference will become cost
[00:30:04] prohibitive mhm inference of better
[00:30:08] models will indeed become more expensive
[00:30:11] but is it
[00:30:12] prohibitive well it depends on how
[00:30:14] useful is it like if it is more useful
[00:30:17] then it is expensive then it is not
[00:30:18] prohibited like to give you an analogy
[00:30:20] like suppose you want to talk to a
[00:30:22] lawyer you have some case you or need
[00:30:24] some advice or something you are
[00:30:26] perfectly happy to spend $500 an hour
[00:30:29] right so if your neural net could give
[00:30:31] you like really reliable legal advice
[00:30:33] you'd say I'm happy to spend $400 for
[00:30:36] that advice and suddenly inference
[00:30:38] becomes very much non prohibited MH the
[00:30:41] question is is can can neuronet produce
[00:30:44] an answer good enough at this
[00:30:47] cost yes and you'll just have like price
[00:30:50] discrimination different different
[00:30:52] models different I mean it's already the
[00:30:54] case today so on our product the API we
[00:30:59] Ser of multiple neural Nets of different
[00:31:02] sizes and different customers use
[00:31:04] different neural Nets of different sizes
[00:31:05] depending on their use case like if
[00:31:07] someone can take a small model and fine
[00:31:09] tune it and get something that's
[00:31:11] satisfactory for them they'll use that
[00:31:13] yeah but if someone wants to do
[00:31:14] something more complicated and more
[00:31:16] interesting they'll use the biggest
[00:31:17] model how do you prevent these models
[00:31:18] from just becoming Commodities where
[00:31:20] these different companies just uh they
[00:31:22] just spit each other's prices down until
[00:31:23] it's basically the cost of the GPU run
[00:31:25] yeah I think I think there is without
[00:31:27] question a force that's trying to create
[00:31:28] that and the answer is you got to keep
[00:31:30] on making progress you got to keep
[00:31:31] improving the models you got to keep on
[00:31:33] coming up with new ideas and making our
[00:31:35] models better and more
[00:31:37] reliable more trustworthy so you can
[00:31:40] trust their
[00:31:41] answers all those things yeah but let's
[00:31:43] say it's like 2025 and the model from
[00:31:46] 2024 somebody just offering it at Cost
[00:31:48] and it's like still pretty good why why
[00:31:50] would people use a new one from 2025 if
[00:31:52] the one from just a year older is you
[00:31:54] know even better so there are several
[00:31:57] answers there for some use cases that
[00:31:59] may be true there will be a new model
[00:32:01] from 2025 which will be driving the more
[00:32:03] interesting use cases there's also going
[00:32:05] to be a question of inference cost like
[00:32:06] you can you can do research to serve the
[00:32:08] same model at less cost so they will be
[00:32:11] different the same model will be served
[00:32:14] will cost different different amounts to
[00:32:17] serve for different companies I can also
[00:32:20] imagine some degree of specialization
[00:32:21] too where some companies may try to
[00:32:23] specialize in some area and be stronger
[00:32:25] in an errow area compared to other
[00:32:27] companies and I think that to May that
[00:32:30] may be a response to commoditization to
[00:32:33] some degree uh as over time do these
[00:32:36] different companies do their research
[00:32:37] directions converge or they diverge are
[00:32:39] they doing similar and similar things
[00:32:40] over time or are they doing are they
[00:32:41] going off branching off into different
[00:32:43] areas so I'd say in the near term it
[00:32:45] looks like there is Convergence in the
[00:32:46] like I expect this going to be a
[00:32:49] convergence a Divergence convergence
[00:32:51] Behavior where there is a lot of
[00:32:54] convergence on the near term work
[00:32:56] there's going to be some Divergence on
[00:32:57] the longer term
[00:32:58] but then once the longer term work
[00:33:00] starts to fruit I think there will be
[00:33:02] conversions again got it one when one of
[00:33:04] them finds the most promising area they
[00:33:06] everybody just that's right now there is
[00:33:09] obviously less less publishing now so it
[00:33:10] will take longer before this promising
[00:33:12] Direction gets rediscovered but that's
[00:33:14] how i' imagine it I think it's going to
[00:33:15] be convergence Divergence convergence
[00:33:18] yeah we talked about this a little bit
[00:33:19] at the beginning but you know as foreign
[00:33:21] governments learn about how capable
[00:33:24] these models are how do you are you
[00:33:26] worried about spies or some sort of
[00:33:29] attack to get your weights or you know
[00:33:32] somehow abuse these models and learn
[00:33:34] about them yeah it's definitely
[00:33:36] something that you absolutely can't
[00:33:38] discount that yeah and yeah something
[00:33:42] that we right guard against the best of
[00:33:45] our ability but it's going to be a
[00:33:46] problem for everyone who's building this
[00:33:48] how do you prevent your weights from
[00:33:49] leaking what I mean you have like really
[00:33:52] good security people and like how many
[00:33:55] people have the if they wanted to just
[00:33:56] like stage into the weights
[00:33:58] how machine how many people could do
[00:33:59] that I
[00:34:01] mean like what I can say is that the
[00:34:05] security people have we have they built
[00:34:07] they've done a really good job so that
[00:34:08] I'm really not worried about the ways
[00:34:10] being leaked okay got it what kinds of
[00:34:12] emerging properties are expecting from
[00:34:14] these models at this
[00:34:15] scale is there something that just comes
[00:34:17] about
[00:34:18] denovo I'm sure things will come I'm
[00:34:21] sure really new surprising properties
[00:34:22] will come up I would not be surprised
[00:34:24] the thing which I'm really excited about
[00:34:25] or the thing which I'd like to see is
[00:34:27] reliability ility and controllability I
[00:34:29] think that this will be very very
[00:34:31] important class of emergent properties
[00:34:33] if you have reliability and
[00:34:34] controllability I think that helps you
[00:34:37] solve a lot of problems reliability
[00:34:38] means you can trust the models output
[00:34:40] controllability means you can control
[00:34:42] it and we'll see but it'll be very cool
[00:34:46] if those emerging properties did exist
[00:34:47] is there somewh you can PR it at Advance
[00:34:50] like what will happen in this parameter
[00:34:51] account what will happen that I think
[00:34:52] it's possible to make some predictions
[00:34:54] about specific specific capabilities
[00:34:56] though it's definitely not simple and
[00:34:58] you can't do it in a super fine grain
[00:35:00] way at least today but I think getting
[00:35:02] better at that is really important and
[00:35:04] anyone who is interested and who
[00:35:06] has re research ideas on how to do that
[00:35:09] I think that can be a valuable
[00:35:11] contribution how seriously do you take
[00:35:13] the scaling laws if like there's a paper
[00:35:15] that says like oh you just increase you
[00:35:17] need this many orders of magnitude more
[00:35:18] to get all the reasoning out like do do
[00:35:20] you take that seriously or do you think
[00:35:21] it breaks down at some point well the
[00:35:24] thing is that the scaling law tells you
[00:35:25] what happens as you what happens to your
[00:35:28] Lo to your next word prediction accuracy
[00:35:31] right there is a whole separate
[00:35:33] challenge of linking next word
[00:35:35] prediction accuracy to reasoning
[00:35:39] capability I do believe that indeed
[00:35:42] there is a link but this link is compli
[00:35:45] and we may find that there are other
[00:35:47] things that can give us more reasoning
[00:35:49] pre-unit
[00:35:51] effort like for example some special
[00:35:54] like you know you mentioned reasoning
[00:35:55] tokens and I think they can be helpful
[00:35:59] there can be there can be probably some
[00:36:01] things
[00:36:03] that you can is this is something you're
[00:36:05] considering just hiring humans to
[00:36:08] generate tokens for you or is it all
[00:36:09] going to come from stuff that already
[00:36:11] exists out there I mean I think that
[00:36:13] relying on people to teach our models to
[00:36:15] do things especially you know to make
[00:36:17] sure that they are well behaved and they
[00:36:19] don't produce false things I think is an
[00:36:21] extremely sensible thing to do and isn't
[00:36:24] it odd that we have the data we need at
[00:36:25] exactly the same time as we have the
[00:36:27] Transformer at the exact same time that
[00:36:29] we have these gpus like is it OD to you
[00:36:32] that all these things happen at the same
[00:36:33] time or do you not see that way I mean
[00:36:35] it it is definitely an interesting it is
[00:36:38] an interesting situation that is the
[00:36:40] case I will say that it is odd and it is
[00:36:44] less odd on some level here is why it's
[00:36:45] less odd so what is the driving force
[00:36:48] behind the fact that the data exists
[00:36:51] that the gpus exists that the
[00:36:53] Transformer exists
[00:36:55] so as the data EX this because computers
[00:36:58] became better and cheaper we've got
[00:37:00] smaller and smaller transistors and
[00:37:02] suddenly at some point it became
[00:37:03] economical for every person to have a
[00:37:05] personal computer once everyone has a
[00:37:06] personal computer you really want to
[00:37:07] connect to me the network you get the
[00:37:09] internet once you have the internet you
[00:37:11] have suddenly data appearing in great
[00:37:13] quanties the gpus were improving
[00:37:15] concurrently because you have smaller
[00:37:17] and smaller transistors and you're
[00:37:18] looking for things to do with them
[00:37:20] gaming turned out to be thing that you
[00:37:23] could do and then at some point the
[00:37:26] gaming GPU Nvidia said wait a second TR
[00:37:29] and may turn it into a general purpose
[00:37:31] GPU computer maybe someone will find you
[00:37:34] find it useful turns out it's good for
[00:37:35] neural NS so it could it could have been
[00:37:39] the case that maybe the GPU would have
[00:37:43] arrived 5 years later or 10 years later
[00:37:45] if let's suppose gaming wasn't a thing
[00:37:48] it's kind of hard to imagine what does
[00:37:49] it mean if gaming isn't a
[00:37:51] thing but it could maybe there was a
[00:37:54] counterfactual world where gpus arrived
[00:37:56] 5 years after the data or 5 years before
[00:37:58] the data in which case maybe things
[00:38:01] would move a little bit more things
[00:38:02] would have been as ready to go as there
[00:38:05] now but that's the picture which I
[00:38:07] imagine all this progress in all these
[00:38:09] Dimensions is very intertwined it's not
[00:38:11] a coincidence
[00:38:14] that like you don't get to pick and
[00:38:16] choose which dimension in which
[00:38:18] Dimensions things improve if you see
[00:38:19] what I mean how inevitable is this kind
[00:38:22] of progress so if like let's say you and
[00:38:24] Jeffrey hon and a few other Pioneers if
[00:38:26] they were never born does the Deep
[00:38:28] learning Revolution happen around the
[00:38:30] same time how much does it delay I think
[00:38:32] maybe there would have been some delay
[00:38:33] maybe like a year delay it's really hard
[00:38:35] tell it's really hard to tell I mean I I
[00:38:38] hesitate to give a lot a a longer answer
[00:38:40] because okay well then you'd have gpus
[00:38:42] would keep on improving right then at
[00:38:44] some
[00:38:45] point I can I cannot see how someone
[00:38:47] would not have discovered it because
[00:38:48] here's the other thing the if if Okay so
[00:38:51] let's suppose no one has done it
[00:38:53] computers keep getting faster and better
[00:38:55] becomes easier and easy to train these
[00:38:56] neural Nets
[00:38:58] because you have bigger gpus so it takes
[00:39:00] less engineering effort to train one you
[00:39:02] don't need to optimize your code as much
[00:39:04] you know when the when the image data
[00:39:05] set came out it was huge and it was very
[00:39:08] very difficult to use now imagine you
[00:39:10] wait for a few years and it becomes very
[00:39:11] easy to download and people can just
[00:39:13] just Tinker so I I would imagine that
[00:39:16] like a modest number of years maximum
[00:39:19] this would be my guess I hesitate I
[00:39:21] hesitate to to give to give a lot a
[00:39:23] longer answer
[00:39:25] though you know you can't you can't
[00:39:28] run you can't rerun the world you don't
[00:39:30] know with let's go back to align for a
[00:39:32] second as somebody who deeply
[00:39:34] understands these models what is your
[00:39:35] intuition of how hard alignment will be
[00:39:38] like I think with the so here's what I
[00:39:39] would say I think with the current level
[00:39:41] of capabilities I think we have a pretty
[00:39:42] good set of ideas of how to align them
[00:39:45] but I would not underestimate the
[00:39:46] difficulty of alignment of models that
[00:39:49] are actually smarter than us of models
[00:39:52] that are capable of misrepresenting
[00:39:53] their
[00:39:55] intentions like I think I think it's
[00:39:56] something
[00:39:57] to to think to think about a lot and to
[00:40:00] research I think this is one area also
[00:40:02] by the way you know like often times
[00:40:04] academic researchers asked me ask me
[00:40:06] where what what's the best place where
[00:40:07] they can contribute and I think
[00:40:09] alignment research is one place where I
[00:40:11] think academic researchers can make very
[00:40:14] meaningful contributions other than that
[00:40:16] do you think Academia will come up with
[00:40:17] important insights about actual
[00:40:19] capabilities or is that going to be just
[00:40:20] the companies at this point so the
[00:40:21] companies will realize the capabilities
[00:40:23] I think it's very possible for academic
[00:40:25] research to come up with those insights
[00:40:27] I think I think it's just it doesn't
[00:40:29] seem to happen that much for some reason
[00:40:31] but I don't I don't think there's
[00:40:33] anything fundamental about Academia like
[00:40:37] it's not like Academia can't I think
[00:40:39] maybe they're just not thinking about
[00:40:41] the right problems or something because
[00:40:43] maybe it's just easier to see what needs
[00:40:46] to be done inside these
[00:40:47] companies I see but there's a
[00:40:49] possibility that somebody could just
[00:40:50] realize yeah I totally like why why
[00:40:53] would I possibly rule this out you see
[00:40:55] what I mean what are the concrete steps
[00:40:57] by which um these language models start
[00:41:00] actually impacting the world of atoms
[00:41:02] and not just the world of vids well you
[00:41:05] see I don't think that there is a
[00:41:06] distinction clean distinction between
[00:41:08] the world of bits and the world of atoms
[00:41:10] suppose the neuronet tells you that hey
[00:41:12] like here is like something that you
[00:41:14] should do and it's going to improve your
[00:41:16] life but you need to like rearrange your
[00:41:18] apartment in a certain way then you go
[00:41:20] and you rearrange your apartment as a
[00:41:22] result did the neuronet impact the world
[00:41:24] of atoms just yeah fair enough fair
[00:41:27] enough
[00:41:28] do you think it'll take a couple of
[00:41:29] additional breakthroughs as important as
[00:41:30] a Transformer to get to superum AI or do
[00:41:33] you think we basically got the insights
[00:41:35] in the books somewhere and we just need
[00:41:37] to implement them and connect them so I
[00:41:40] don't really see such a big distinction
[00:41:42] between those two cases and let me
[00:41:43] explain why like I think what's what one
[00:41:46] of the ways in which progress has taken
[00:41:49] place in the
[00:41:50] past is that we've
[00:41:53] understood that something had a property
[00:41:57] a desirable property all along but you
[00:41:59] didn't
[00:42:00] realize so is that a breakthrough you
[00:42:02] can say yes it is is it an
[00:42:04] implementation of something on the books
[00:42:06] also yes so I I my my feeling is that a
[00:42:10] few of those are quite likely to happen
[00:42:12] but that in hindsight it will not feel
[00:42:14] like a breakthrough everybody is going
[00:42:16] to say oh well of course like it's
[00:42:17] totally obvious that such and such thing
[00:42:20] can can work you see with a Transformer
[00:42:23] the reason it's being brought up as a
[00:42:24] big as a specific Advance is because
[00:42:26] it's the kind of thing that was not
[00:42:27] obvious for almost anyone so people can
[00:42:29] say yeah like it's not something which
[00:42:31] they knew about but if an advance comes
[00:42:33] from something like let's consider the
[00:42:35] the the most fundamental advance of deep
[00:42:36] learning that a big neural network
[00:42:39] trained with back propagation can do a
[00:42:40] lot of things like where's the novelty
[00:42:43] it's not in the neural network it's not
[00:42:45] in the back
[00:42:47] propagation but then somehow it's the
[00:42:49] kind of but it was it is most definitely
[00:42:51] a giant conceptual breakthrough because
[00:42:53] for the longest time people just didn't
[00:42:54] see that but then now everyone sees it
[00:42:57] everyone's going to say well of course
[00:42:58] like it's totally obvious big neural
[00:43:01] everyone knows that they can do it what
[00:43:02] is your opinion of your former Advisor
[00:43:04] New forward forward
[00:43:06] algorithm I think that it's an attempt
[00:43:10] to brain a neural network without back
[00:43:13] propagation and I think that this is
[00:43:15] especially interesting if you are
[00:43:17] motivated to try to understand how the
[00:43:20] brain might be learning its connections
[00:43:23] the reason for that is that as far as I
[00:43:26] know neuroscientists are really
[00:43:29] convinced that the brain cannot
[00:43:30] Implement back propagation because the
[00:43:32] signals in the synaps is only moving One
[00:43:35] Direction and so if you have a
[00:43:37] neuroscience motivation and you want to
[00:43:40] say
[00:43:41] okay how can I come up with something
[00:43:44] that tries to approximate approximate
[00:43:48] the good properties of back
[00:43:50] propagation without doing back
[00:43:52] propagation that's what the forward
[00:43:53] forward algorithm is trying to do but if
[00:43:56] you are trying to just engineer a good
[00:43:58] system there is no reason to not use
[00:43:59] back propagation
[00:44:01] like it's it's it's the only algorithm
[00:44:05] really I guess I've heard you in
[00:44:06] different context talk about the need
[00:44:08] like using humans as the you know the
[00:44:11] existing example case that a you know
[00:44:14] AGI exists right so at what point do you
[00:44:17] take the metaphor less seriously and
[00:44:18] feel don't feel the need to pursue it in
[00:44:20] terms of research because it is
[00:44:22] important to you as a sort of existence
[00:44:24] case like at what point do I stop caring
[00:44:26] caring about humans as an existence case
[00:44:28] of intelligence or as the sort of as a
[00:44:33] example of the model you want to follow
[00:44:34] in terms of pursuing intelligence in
[00:44:36] models I see I mean like you got to I
[00:44:40] think it's good to be inspired by humans
[00:44:42] I think it's good to be inspired by the
[00:44:43] brain I think there is an art into being
[00:44:46] inspired by humans in the brain
[00:44:47] correctly because it's very easy to
[00:44:49] latch on to an nonessential quality of
[00:44:53] humans or of the brain and I think many
[00:44:55] people whoin who many people whose
[00:44:57] research is trying to be inspired by
[00:44:59] humans and by the brain often gets a
[00:45:01] little bit specific people get a little
[00:45:02] bit to okay so like what cognitive
[00:45:04] science model should be follow at the
[00:45:06] same time consider the idea of the
[00:45:08] neural network itself the idea of the
[00:45:10] artificial neuron this too is inspired
[00:45:12] by the brain but it turned out to be
[00:45:14] extremely fruitful so how do you do this
[00:45:18] you what what behaviors of human beings
[00:45:20] are essential that you say like this is
[00:45:22] something that proves to us that it's
[00:45:23] possible what is in essential no
[00:45:25] actually this is like some emerg
[00:45:27] phenomena of something more basic
[00:45:30] and we just need to focus on our on our
[00:45:33] on do getting our own Basics right I
[00:45:36] would say I would say that it's
[00:45:41] like I think one should one can and
[00:45:44] should be inspired by human intelligence
[00:45:47] with care final question why is there in
[00:45:50] your case such a strong correlation
[00:45:51] between being first to the Deep learning
[00:45:54] Revolution and still being one of the
[00:45:55] top researchers you would think that the
[00:45:57] two things wouldn't be that correlated
[00:45:58] but why is that that correlation I don't
[00:46:00] think those things are super correlated
[00:46:02] indeed I feel like in my
[00:46:04] case I mean honestly it's hard to answer
[00:46:06] the question you know I just kept
[00:46:09] on kept I kept trying really hard and it
[00:46:12] turned out to have sufficed thus far got
[00:46:14] it so it's a perseverance I think it's a
[00:46:17] necessary but not a sufficient condition
[00:46:19] like you know many things need to come
[00:46:20] together in order to really figure
[00:46:23] something out mm like you need to really
[00:46:26] go for it
[00:46:27] and also need to have the right way of
[00:46:29] looking at things and it's hard it's
[00:46:32] hard to give him like a really
[00:46:33] meaningful answer to this question all
[00:46:36] right um Ilia it is been a true pleasure
[00:46:38] thank you so much for coming out ler
[00:46:39] Society I appreciate you bringing us to
[00:46:41] the offices thank you yeah I really
[00:46:43] enjoyed it thank you very
[00:46:45] much hey everybody I hope you enjoyed
[00:46:47] that episode just wanted to let you know
[00:46:50] that in order to help pay for the bills
[00:46:54] associated with this podcast I'm turning
[00:46:56] on paid subscriptions on my substack at
[00:46:59] warc patel.com no important content on
[00:47:03] this podcast will ever be paywalled so
[00:47:07] please don't donate if you have to think
[00:47:08] twice before buying a cup of coffee but
[00:47:11] if you have the means and you've enjoyed
[00:47:13] this podcast or gotten some kind of
[00:47:14] value out of it I would really
[00:47:16] appreciate your support as always the
[00:47:18] most helpful thing you can do is to
[00:47:20] share the podcast send it to people you
[00:47:22] think might enjoy it put it in Twitter
[00:47:24] your group chats Etc just splits the
[00:47:26] world
[00:47:27] appreciate you listening I'll see you
[00:47:29] next time cheers
[00:47:30] [Music]
