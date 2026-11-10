# Dwarkesh Patel: Dario Amodei — The Hidden Pattern Behind Every AI Breakthrough
- **YouTube URL:** https://www.youtube.com/watch?v=Nlkk3glap_U
- **Lines:** 3484

---

[00:00:02] a generally well-educated human that
[00:00:02] could happen in you know two or three
[00:00:04] years what does that imply for anthropic
[00:00:06] when in two to three years these
[00:00:08] leviathans are doing like 10 billion
[00:00:09] dollar trading runs the models they just
[00:00:12] want to learn and it was a bit like a
[00:00:13] Zen Cohen I listened to this and and I
[00:00:15] became enlightened
[00:00:17] the compute doesn't flow like the spice
[00:00:20] doesn't flow it's like you can't like
[00:00:23] like the The Blob has to be unencumbered
[00:00:26] the big acceleration that happened late
[00:00:28] last year and the beginning of this year
[00:00:31] we didn't cause that and honestly I
[00:00:33] think if you look at the reaction to
[00:00:34] Google that might be 10 times more
[00:00:35] important than anything else there was a
[00:00:38] running joke the way building AGI would
[00:00:39] look like because you know there would
[00:00:40] be a data center next to a nuclear power
[00:00:43] plant next to a bunker but now it's 20
[00:00:45] 30. what happens next what what are we
[00:00:47] doing with a superhuman God
[00:00:49] okay today I have the pleasure of
[00:00:52] speaking with Dario amodei who is the
[00:00:55] CEO of anthropic and I'm really excited
[00:00:56] about this one Dario thank you so much
[00:00:58] for coming on the podcast thanks for
[00:01:00] having me first question you have been
[00:01:02] one of the very few people who has seen
[00:01:04] scaling coming for years more than five
[00:01:07] years I don't know how long it's been
[00:01:08] but as somebody who's seen it coming
[00:01:11] what is fundamentally the explanation
[00:01:13] for why scaling works why is a universe
[00:01:15] organized such that if you throw big
[00:01:17] blobs and compute at a wide enough
[00:01:19] distribution of data the thing becomes
[00:01:21] intelligent I think the truth is that we
[00:01:23] still don't know I think it's almost
[00:01:25] entirely an empirical fact
[00:01:28] um you know I think it's a fact that you
[00:01:29] could kind of sense from the data and
[00:01:31] from a bunch of different places
[00:01:33] um but I think we don't still have a
[00:01:35] satisfying explanation for it if I were
[00:01:37] to try to make one but I'm just I don't
[00:01:39] know I'm just kind of waving my hands
[00:01:40] when I say this you know there there's
[00:01:43] this there's these ideas in physics
[00:01:45] around like long tail or power law of
[00:01:49] like core relations or effects and so
[00:01:52] like when a bunch of stuff happens right
[00:01:54] when you have a bunch of like features
[00:01:56] you get a lot of the data in like kind
[00:01:58] of the early you know the the fat part
[00:02:01] of the distribution before the Tails um
[00:02:03] you know for language this would be
[00:02:04] things like oh I figured out there are
[00:02:06] parts of speech and nouns follow verbs
[00:02:08] and then there are these more and more
[00:02:09] and more and more subtle correlations
[00:02:12] um and so it it kind of makes sense why
[00:02:15] there would be this you know every log
[00:02:17] or order of magnitude that you add you
[00:02:20] kind of capture more of the distribution
[00:02:22] what I what's not clear at all is why is
[00:02:26] it scale so smoothly with parameters why
[00:02:29] does it scale so smoothly with the
[00:02:32] amount of data why are you can think up
[00:02:34] some explanations of why it's linear
[00:02:36] like the parameters are like a bucket
[00:02:38] and so the data's like water and so size
[00:02:41] of the bucket is proportional to the
[00:02:42] size of the water but like why does it
[00:02:44] lead to all these this very smooth
[00:02:46] scaling I think we still don't know
[00:02:48] there's all these X explanations are
[00:02:50] chief scientists Jared Kaplan did some
[00:02:53] stuff on like fractal manifold Dimension
[00:02:56] that like you can use to explain it so
[00:02:58] there's there's all kinds of ideas but I
[00:02:59] feel like we just don't really know for
[00:03:02] sure and by the way for the audience
[00:03:04] who's trying to follow along by scaling
[00:03:06] we're referring to the fact that you can
[00:03:07] very predictably see how if you go from
[00:03:09] gbd3 to gpd4 or in this case Claude one
[00:03:11] to claw two the loss in terms of whether
[00:03:14] it can predict the next token scales
[00:03:15] very smoothly so okay we don't know why
[00:03:18] it's happening but can you at least
[00:03:19] predict if empirically here is the loss
[00:03:23] at which disability will emerge here is
[00:03:26] the place where this circuit will emerge
[00:03:28] is is that about predictable or are you
[00:03:30] just looking at the loss number that is
[00:03:31] much less predictable what's predictable
[00:03:33] is this statistical average this loss
[00:03:35] this entropy it's super predictable it's
[00:03:37] like you know predictable to like
[00:03:39] sometimes even to several significant
[00:03:41] figures which you don't see outside of
[00:03:43] physics right you don't expect to see it
[00:03:44] in this messy empirical field
[00:03:47] um but actually specific abilities are
[00:03:49] very hard to predict so you know back
[00:03:51] when I was working on gpt2 and gpt3 like
[00:03:53] when does arithmetic come in place when
[00:03:55] do models learn to code sometimes it's
[00:03:58] very it's very abrupt um you know it's
[00:04:01] kind of like you can predict statistical
[00:04:03] averages of the weather but the weather
[00:04:04] on one particular day is very you know
[00:04:06] very very hard to predict so uh I dumb
[00:04:09] it down for me I don't understand
[00:04:10] manifolds but mechanistically it doesn't
[00:04:12] know addition yet now it knows addition
[00:04:14] what has happened uh this is another
[00:04:16] question that we don't know the answer
[00:04:18] to I mean we're trying to answer this
[00:04:19] with things like mechanistic
[00:04:20] interpretability but you know I'm not
[00:04:23] sure I mean you can think about these
[00:04:25] things about like circuits snapping into
[00:04:27] place although there is some evidence
[00:04:30] that when you look at the models being
[00:04:31] able to add things that you know like if
[00:04:34] you look at its chance of getting the
[00:04:37] right answer that shoots up all of a
[00:04:39] sudden but if you look at okay what's
[00:04:40] the probability of the right answer
[00:04:41] you'll see it climb from like one in a
[00:04:43] million to one hundred thousand to one
[00:04:45] in a thousand long before it actually
[00:04:48] gets the right answer and so there's
[00:04:50] some Conti in many of these cases at
[00:04:52] least I don't know if in all of them
[00:04:53] there's some continuous process going on
[00:04:55] behind the scenes I don't understand it
[00:04:57] at all does that imply that the circuit
[00:04:59] or the process for doing addition was
[00:05:01] pre-existing and it just got increased
[00:05:04] in Saline I don't know if like there's
[00:05:06] this circuit that's weak and getting
[00:05:07] strong longer I don't know if it's
[00:05:09] something that works but not very well
[00:05:10] like
[00:05:12] I I think we don't know and these are
[00:05:14] some of the questions we're trying to
[00:05:15] answer with mechanistic interpretability
[00:05:16] are there abilities that won't emerge
[00:05:18] with scale so I definitely think that
[00:05:21] again like things like alignment and
[00:05:23] values are not guaranteed to emerge with
[00:05:25] scale right it's it's kind of like you
[00:05:28] know one way to think about it is you
[00:05:29] you train the model and it is
[00:05:33] basically it's like predicting the world
[00:05:35] it's understanding the world it's its
[00:05:37] job is facts not values right it's
[00:05:39] trying to predict what comes next but
[00:05:41] there's there's just there's free
[00:05:42] variables here where it's like it what
[00:05:45] should you do what should you think what
[00:05:46] should you value those you know like
[00:05:48] they're they're just there are the bits
[00:05:51] for that there's just like well if I
[00:05:53] started with this I should finish with
[00:05:54] this if I started with this other thing
[00:05:56] I should finish with this other thing
[00:05:58] um and so I think that's not going to
[00:06:00] emerge um I want to talk about a lemon
[00:06:02] in a second but on scaling if it turns
[00:06:04] out that scaling plateaus before we
[00:06:06] reach human level intelligence looking
[00:06:08] back on it what would be your
[00:06:09] explanation what do you think is likely
[00:06:11] to be the case if that turns out to be
[00:06:12] the outcome yeah um so I guess I would
[00:06:15] distinguish some problem with the
[00:06:16] fundamental Theory with some practical
[00:06:18] issue so uh one practical issue we could
[00:06:21] have is we could run out of data for
[00:06:23] various reasons I think that's not going
[00:06:24] to happen but uh you know uh if you look
[00:06:27] at it very very naively we're not that
[00:06:29] far from running out of data and so it's
[00:06:30] like we just don't have the data to
[00:06:32] continue the to continue the scaling
[00:06:34] curves I think you know another way it
[00:06:36] could happen is like oh we just we just
[00:06:37] use up our all of our compute that was
[00:06:39] available and that that wasn't enough
[00:06:40] and then progress is slow after that I
[00:06:43] wouldn't bet in either of those things
[00:06:44] happening but they they could I I think
[00:06:47] from uh from a fundamental perspective I
[00:06:51] personally I think it's very unlikely
[00:06:52] that the scaling laws will just stop if
[00:06:55] they do another reason again this isn't
[00:06:57] fully fundamental could just be we don't
[00:07:00] have quite the right architecture like
[00:07:02] if we tried to do it with an lsdm or an
[00:07:04] RNN the slope would be different I still
[00:07:07] might be that we get there but I think
[00:07:09] there are some things that are just very
[00:07:10] hard to represent when you don't have
[00:07:12] this ability to attend far in the past
[00:07:14] that Transformers have if somehow and I
[00:07:18] don't know how we would know this it
[00:07:20] kind of wasn't about the architecture
[00:07:21] and we just hit a wall I think I'd be
[00:07:24] very surprised by that I think we're
[00:07:26] already at the point where the things
[00:07:28] the models can't do don't seem to me to
[00:07:31] be different and kind from the things
[00:07:32] they can do
[00:07:33] um and it just
[00:07:35] you know you could have made a case a
[00:07:37] few years ago that it was like they
[00:07:39] can't reason they can't program like you
[00:07:42] you could have drawn boundaries and said
[00:07:44] well
[00:07:45] maybe you'll hit a wall I didn't think
[00:07:47] that I didn't think we would hit a wall
[00:07:48] a few other people didn't think we would
[00:07:50] hit a wall but it was a more plausible
[00:07:51] case that I think it's a less plausible
[00:07:53] case now now it could happen like this
[00:07:55] stuff is crazy like it could it could it
[00:07:57] could happen tomorrow but it's just like
[00:07:59] we hit a wall I think if that happens
[00:08:02] I'm trying to think of like what's my
[00:08:03] what would really be my it's unlikely
[00:08:05] but what would really be my explanation
[00:08:07] I think my explanation would be there's
[00:08:10] something wrong with the loss when you
[00:08:13] train on next word prediction like some
[00:08:16] of the remaining like reasoning
[00:08:18] abilities or something like that like if
[00:08:20] you really want to learn you know it's a
[00:08:21] program at a really high level like it
[00:08:24] means you care about some tokens much
[00:08:26] more than others and they're rare enough
[00:08:28] that it's like the loss function over
[00:08:30] focuses on kind of the the the
[00:08:33] appearance the things that are
[00:08:35] responsible for the most bits of entropy
[00:08:37] uh and instead you know they don't focus
[00:08:40] on this stuff that's really essential
[00:08:41] and so you could kind of have the signal
[00:08:43] drowned out in the noise and I don't
[00:08:45] think it's going to play out that way
[00:08:46] for a number of reasons but if if you
[00:08:49] told me yup you trained your 2024 model
[00:08:51] it was much bigger and it just wasn't
[00:08:53] any better and you tried every
[00:08:54] architecture it didn't work
[00:08:56] that I think that's the explanation I
[00:08:58] would I would reach for is there a
[00:08:59] candidate for another loss function if
[00:09:01] you had to abandon next token prediction
[00:09:02] I think then you would have to go for
[00:09:05] some kind of RL and again there's you
[00:09:07] know there's many different kinds
[00:09:08] there's RL from you and feedback there's
[00:09:09] RL against an objective there's things
[00:09:12] like constitutional AI there's things
[00:09:13] like amplification and debate right
[00:09:16] these are kind of both alignment methods
[00:09:18] and ways of training models you would
[00:09:20] have to try a bunch of things but the
[00:09:21] focus would have to be on what do we
[00:09:23] actually care about the model doing
[00:09:25] right in a sense we're a little bit
[00:09:26] lucky that it's like predict the next
[00:09:28] word gets us all these other things we
[00:09:31] need right there's no guarantee it seems
[00:09:33] like from your world view there's a
[00:09:34] multitude of different loss functions
[00:09:36] that it's just a matter of what can
[00:09:38] allow you to just throw a whole bunch of
[00:09:40] data at it like the next token
[00:09:41] prediction itself is not significant
[00:09:42] yeah I think well I mean I guess the
[00:09:44] thing with RL is you get slowed down a
[00:09:46] bit because it's like you know you have
[00:09:48] to by some method kind of you know
[00:09:50] design how loss function Works nice
[00:09:53] thing with the next token prediction is
[00:09:54] it's there for you right it's just it's
[00:09:57] the easiest thing in the world and so I
[00:09:59] think it would slow you down if you
[00:10:00] couldn't scale in just that very
[00:10:01] simplest way you mentioned that uh the
[00:10:04] data is likely not to be the constrained
[00:10:06] why why do you think that is the case
[00:10:07] there's various possibilities here and
[00:10:09] you know for a number of reasons I
[00:10:10] shouldn't go into the details but you
[00:10:12] know like there's many sources of data
[00:10:14] in the world and there's many ways that
[00:10:16] you can also generate data my my guess
[00:10:19] is that this will not be a blocker maybe
[00:10:21] better if it was but uh it won't be are
[00:10:24] you talking about multimodal or there's
[00:10:26] just many different ways to do it um how
[00:10:28] did you form your views on scaling how
[00:10:30] far back can we go and then you would be
[00:10:32] basically saying something similar to
[00:10:34] this this view that I have probably
[00:10:36] formed gradually from I would say like
[00:10:38] 2014 to 2017. so I think my first
[00:10:43] experience with it was my first
[00:10:44] experience with AI
[00:10:46] um so I you know I saw some of the early
[00:10:47] stuff around alexnet in 2012. always
[00:10:50] kind of had wanted to study intelligence
[00:10:52] but I you know before I was just like
[00:10:54] this isn't really working like it
[00:10:55] doesn't seem like it's actually working
[00:10:58] um you know all the way back to like you
[00:11:00] know 2005 I'd like you know I'd read
[00:11:01] Rick herzwell's work you know I'd read
[00:11:04] even even some of like Elie Ezra's work
[00:11:06] on the early on the old internet back
[00:11:07] then and I was like oh this this stuff
[00:11:09] kind of looks far away like I look at
[00:11:11] the AI stuff of today and it's like not
[00:11:12] not anywhere not anywhere close but with
[00:11:15] Alex and I was like oh this is actually
[00:11:17] stuff is actually starting to work so I
[00:11:18] joined Andrew ing's group
[00:11:21] um initially at Baidu and the first task
[00:11:24] you know that I got set to do right it
[00:11:26] was my you know I'd be in a different
[00:11:27] field and so I I first joined you know
[00:11:31] this was my first experience with AI and
[00:11:34] it was a bit different from a lot of the
[00:11:36] kind of academic style research that was
[00:11:38] going on kind of Elsewhere in the world
[00:11:40] right the I I think I kind of got lucky
[00:11:43] in that the task that was given to me
[00:11:46] and the other folks there was just make
[00:11:47] the best speech recognition
[00:11:49] uh system that you can and there was a
[00:11:52] lot of data available there were a lot
[00:11:53] of gpus available so it kind of it it
[00:11:56] posed the problem in a way that was
[00:11:59] amenable to discovering that kind of
[00:12:00] scaling was a solution right that's very
[00:12:02] different from like Europe post-doc and
[00:12:05] it's your job to come up with you know
[00:12:07] what's the what's the best like you know
[00:12:09] what's what's an idea that seems clever
[00:12:11] and new and makes your mark as someone
[00:12:13] who's invented something and and so I
[00:12:16] just quickly discovered that like you
[00:12:18] know I was just just tried the simplest
[00:12:19] experiments I was like you know just
[00:12:21] fiddling with some dials I was like okay
[00:12:23] try um
[00:12:24] you know try try adding more layers to
[00:12:27] the art literally add more layers to the
[00:12:29] RNN
[00:12:30] um you know try training it for longer
[00:12:31] what happens how long does it take to
[00:12:33] overfit what if I add new data and
[00:12:35] repeat it less times and like I just saw
[00:12:37] these like very consistent patterns I
[00:12:40] didn't really
[00:12:41] know that this was unusual or that
[00:12:44] others weren't thinking in this way this
[00:12:45] this was just kind of like almost like
[00:12:47] beginner's luck it was my first
[00:12:49] experience with it and I didn't really
[00:12:51] think about it Beyond speech recognition
[00:12:53] right right right you know I was just
[00:12:55] kind of like oh this is you know I don't
[00:12:57] know anything about this field there's
[00:12:58] zillions of things people do with
[00:12:59] machine learning but like I'm like weird
[00:13:01] seeing seems to be true in the speech
[00:13:03] recognition field
[00:13:05] um and and and then I I think it was
[00:13:07] recently you know like um just before
[00:13:09] open AI started
[00:13:11] um that I met Ilia who you who you
[00:13:12] interviewed one of the first things he
[00:13:14] said to me was look the models they just
[00:13:16] want to learn you have to understand
[00:13:17] this the models they just want to learn
[00:13:19] and it was a bit like a Zen Cohen like I
[00:13:21] kind of like I listened to this and and
[00:13:23] I became enlightened
[00:13:24] [Laughter]
[00:13:27] um and uh you know over over the years
[00:13:29] over the years after this you know you
[00:13:32] know again I would be kind of you know
[00:13:34] the one who would formalize a lot of
[00:13:37] these things and kind of put them
[00:13:38] together but like just kind of the the
[00:13:40] what that told me is that that
[00:13:42] phenomenon that I'd seen wasn't just
[00:13:45] some random thing that I'd seen it was
[00:13:46] like it was broad it was it was more
[00:13:48] General right the models the models just
[00:13:50] want to learn you get the obstacles out
[00:13:52] of their way right you give them you
[00:13:54] give them good data you you give them
[00:13:57] enough space to operate in you don't do
[00:13:59] something stupid like condition them
[00:14:01] badly numeric likely
[00:14:03] um and they want to learn they'll do it
[00:14:04] they'll do it you know what I find
[00:14:07] really interesting about what you said
[00:14:08] is there are many people who were aware
[00:14:11] back at that time probably weren't
[00:14:13] working on it directly but we're aware
[00:14:14] that these things are really good at
[00:14:16] speech recognition or at playing these
[00:14:19] constrained games very few extrapolated
[00:14:23] from there like you and Ilya did to
[00:14:25] something that is generally intelligent
[00:14:27] what was different about the way you
[00:14:29] were thinking about it versus how others
[00:14:30] think that you went from like is getting
[00:14:32] better at speech in this consistent way
[00:14:34] it will get better at everything in this
[00:14:35] consistent way yeah so I I genuinely
[00:14:38] don't know I mean at first when I saw it
[00:14:39] first speech I assumed this was just
[00:14:41] true for speech or for this narrow class
[00:14:43] of models I I think it was just over the
[00:14:46] period between 2014 and 2017 I tried it
[00:14:50] for a lot of things and saw the same
[00:14:52] thing over and over again I watched the
[00:14:54] same being true with DOTA I watched the
[00:14:57] same being true with robotics which many
[00:14:59] people thought of as a counter example
[00:15:01] but I just thought what's hard to get
[00:15:03] data for robotics but if we operate
[00:15:04] within if we look within the data that
[00:15:06] we have we see the same patterns and so
[00:15:09] I don't I don't know I think people were
[00:15:12] very focused on solving the problem in
[00:15:14] front of them
[00:15:15] why one person thinks one way another
[00:15:17] person thinks it's very it's very hard
[00:15:19] to explain I think people just
[00:15:22] see it through a different lens you know
[00:15:24] are looking like vertically instead of
[00:15:25] horizontally they're not thinking about
[00:15:26] the scaling they're thinking about how
[00:15:28] do I solve my problem well for robotics
[00:15:30] there's not enough data and so you know
[00:15:34] and and so you know that can easily
[00:15:36] abstractable scaling doesn't work
[00:15:37] because we don't have the data and and
[00:15:39] so I don't I I don't know I just for
[00:15:42] some reason and it may just it may just
[00:15:43] have been random chance was obsessed
[00:15:45] with that particular direction when did
[00:15:48] it become obvious to you that language
[00:15:51] is the means to just feed a bunch of
[00:15:53] data into these things that or was it
[00:15:55] just you ran out of other things like
[00:15:56] robotics there's not enough data this
[00:15:57] other thing there's not enough data yeah
[00:15:59] I mean I think this whole idea of like
[00:16:01] the next word prediction that you could
[00:16:03] do self-supervised learning you know
[00:16:05] that together with the idea that it's
[00:16:07] like wow for predicting the next word
[00:16:09] there's so much richness and structure
[00:16:11] there right you know it might say two
[00:16:13] plus two equals and you have to know the
[00:16:14] answer is four and you know it might be
[00:16:16] telling the story about a character and
[00:16:18] then basically it's it's posing to the
[00:16:20] model you know the equivalent of these
[00:16:22] developmental tests that get posed to
[00:16:24] Children you know Mary walks into the
[00:16:25] room and you know puts an item in there
[00:16:27] and then you know Chuck walks into the
[00:16:29] room and removes the item and Mary
[00:16:30] doesn't see it what does Mary think hap
[00:16:32] you know so like so the models are going
[00:16:35] to have to to get this right in the
[00:16:36] service of predicting the next word
[00:16:37] they're going to have to solve you know
[00:16:40] solve all these theory of Mind problems
[00:16:42] solve all these math problems and so I
[00:16:44] you know I I my thinking was just well
[00:16:46] you know you scale it up as much as you
[00:16:48] can you you you know there's there's
[00:16:50] kind of No Limit to it and I think I
[00:16:52] kind of had abstractly that view but the
[00:16:55] thing of course that like really
[00:16:57] solidified and convinced me was the work
[00:16:59] that Alec Radford did on GPT one
[00:17:02] um which was not only could you get this
[00:17:04] this language model that could predict
[00:17:06] things very well but also you could fine
[00:17:08] tune it you needed to fine tune it in
[00:17:10] those days to do all these other tasks
[00:17:12] and so I was like wow you know it this
[00:17:14] isn't just some narrow thing where you
[00:17:16] get the language model right it's sort
[00:17:18] of halfway to everywhere right it's like
[00:17:20] you know you get the language model
[00:17:22] right and then with a little move in
[00:17:24] this direction it can you know it can
[00:17:26] solve this this you know logical
[00:17:28] dereference tests or whatever and you
[00:17:30] know with this this other thing you know
[00:17:31] it can it can solve translation or
[00:17:33] something and then you're like wow I
[00:17:35] think there's there's really something
[00:17:36] to do it and and of course we can we can
[00:17:38] really scale it well one thing that's
[00:17:40] confusing or that would have been hard
[00:17:41] to see if you told me in 2018 we'll have
[00:17:45] models in 2023 like two that can write
[00:17:48] theorems in the style of Shakespeare or
[00:17:50] whatever Theory you want you want they
[00:17:52] can a standardized test with open-ended
[00:17:55] questions you know um the just all kinds
[00:17:58] of really impressive things you would
[00:18:00] have said at that time I would have said
[00:18:02] oh you have AGI you clearly have
[00:18:04] something that is a human level
[00:18:04] intelligence where these while these
[00:18:07] things are impressive it clearly seems
[00:18:08] we're not at human level at least in the
[00:18:10] current generation and potentially for
[00:18:12] generations to come what explains this
[00:18:15] discrepancy between super impressive
[00:18:17] performance and these benchmarks and in
[00:18:19] just like the things you could describe
[00:18:21] versus yeah so that that was one area
[00:18:23] where actually I was not press scenes
[00:18:25] and I was surprised as well yeah
[00:18:27] um so when I first looked at gpt3 and
[00:18:30] you know more so the kind of things that
[00:18:32] we built in the early days at anthropic
[00:18:34] my my general sense was I you know I
[00:18:37] looked at these and I'm like it seems
[00:18:39] like they've really grasped the essence
[00:18:41] of language I'm not sure how much we
[00:18:43] need to scale them up like maybe we
[00:18:45] maybe what's what's more needed from
[00:18:47] here is like RL and all and kind of and
[00:18:49] kind of all the other stuff like we
[00:18:51] might be kind of near the you know I
[00:18:53] thought in 2020 like we can scale this a
[00:18:56] bunch more but I wonder if it's more
[00:18:57] efficient to scale it more or to start
[00:18:59] adding on these other objectives like
[00:19:01] like RL I thought maybe if you do as
[00:19:03] much RL as you know as you've done
[00:19:06] pre-training for uh for uh you know 2020
[00:19:09] style model that that's that's the way
[00:19:12] to go and scaling it up will keep
[00:19:13] working but you know is that is that
[00:19:15] really the best path and I I think it I
[00:19:19] don't know it just keeps going like I
[00:19:21] thought it had understood a lot of the
[00:19:22] essence of language but then you know
[00:19:25] there's there's kind of there's kind of
[00:19:26] further to go
[00:19:28] um and and so I don't know stepping back
[00:19:31] from it like one of the reasons why I'm
[00:19:34] sort of very empiricist about about AI
[00:19:37] about safety about organizations is that
[00:19:41] you often get surprised right you know I
[00:19:43] feel like
[00:19:44] I've been right about some things but
[00:19:47] I've still you know with these
[00:19:48] theoretical pictures had been wrong
[00:19:50] about most things being right about 10
[00:19:52] of the stuff is you know sets you head
[00:19:54] and shoulders above
[00:19:56] um above above many people you know if
[00:19:58] you look back to I can't remember who it
[00:20:00] was kind of you know made these diagrams
[00:20:03] that are like you know here's here's the
[00:20:05] village little idiot here's Einstein
[00:20:07] here's the scale of intelligence right
[00:20:09] in the village idiot and Einstein are
[00:20:11] like very close to each other like that
[00:20:13] maybe that's still true in some abstract
[00:20:16] sense or something but it's it's not
[00:20:17] really what we're seeing is it we're
[00:20:19] seeing like that it seems like the human
[00:20:21] range is pretty Broad and doesn't we
[00:20:25] don't hit the human range
[00:20:27] in the same place or at the same time
[00:20:29] for different tasks right like you know
[00:20:32] like write write us on it you know in
[00:20:34] the style of Cormac McCarthy or
[00:20:36] something like I don't know I'm not very
[00:20:38] creative so I couldn't do that but like
[00:20:40] you know that's that's a pretty high
[00:20:41] level human skill right
[00:20:43] um and even the model is starting to get
[00:20:45] good at stuff of you know like
[00:20:47] constrained writing you know there's
[00:20:48] like write a you know write a page
[00:20:50] without using the letter e or something
[00:20:52] Library the page about X without using
[00:20:53] the letter e like I think the models
[00:20:55] might be like superhuman or close to
[00:20:57] superhuman at that
[00:20:59] um but when it comes to you know
[00:21:02] I yeah I don't know prove relatively
[00:21:04] simple mathematical theorems like
[00:21:07] they're they're just starting to do the
[00:21:09] beginning of it they make really dumb
[00:21:11] mistakes sometimes and they they really
[00:21:14] lack any kind of broad like you know
[00:21:17] correcting your errors or doing some
[00:21:19] extended tasks and so I don't know it
[00:21:22] turns out that intelligence isn't isn't
[00:21:25] a spectrum there are a bunch of
[00:21:27] different areas of domain expertise
[00:21:29] there are a bunch of different like
[00:21:30] kinds of skills like Memories different
[00:21:32] I mean it's all it's all formed in the
[00:21:35] blob it's not it's all formed in the
[00:21:37] blob it's not complicated but to the
[00:21:39] extent it even is on the Spectrum the
[00:21:41] spectrum is also wide if you asked me 10
[00:21:43] years ago that's not what I would have
[00:21:44] expected at all but uh I think that's
[00:21:47] very much the way it's turned out oh man
[00:21:48] I have so many questions just as follow
[00:21:50] up on that one is do you expect that
[00:21:54] given the distribution of training that
[00:21:56] these models get from massive amounts of
[00:21:59] internet data versus what humans got
[00:22:01] from Evolution that the repertoire of
[00:22:03] skills that elicits will be just barely
[00:22:06] overlapping it will be like concentric
[00:22:08] circles how how do you think about do
[00:22:11] those matter or is it clearly there's a
[00:22:13] lot there's certainly a large amount of
[00:22:15] overlap right because a lot of the thing
[00:22:16] you know like these models have have
[00:22:18] business applications and many of their
[00:22:20] business applications are doing things
[00:22:21] that you know are help helping humans to
[00:22:23] be more effective at things
[00:22:25] um so the overlap is quite is quite
[00:22:27] large and you know if you think of all
[00:22:30] the activity that humans put on the
[00:22:31] internet in text that covers a lot of it
[00:22:33] but it probably doesn't cover some
[00:22:35] things like the models I think they do
[00:22:37] learn a physical model of the world to
[00:22:39] some extent but they certainly don't
[00:22:40] learn how to actually move around in the
[00:22:41] world
[00:22:42] um again maybe that's easy to fine tune
[00:22:44] but uh I you know I think so I think
[00:22:47] there are some things that the models
[00:22:49] don't learn that humans do and then I
[00:22:52] think you know the models learn for
[00:22:54] example to speak fluent base64. I don't
[00:22:56] know about you but I never learned that
[00:22:58] right How likely do you think it is that
[00:23:01] these models will be superhuman for many
[00:23:04] years at economically valuable tasks
[00:23:07] while they're still below humans in many
[00:23:10] other relevant tasks that prevents like
[00:23:12] an intelligence explosion or something I
[00:23:14] think this kind of stuff is like really
[00:23:15] hard to know
[00:23:17] um so I'll give I'll give that caveat
[00:23:19] that like you know again like the basic
[00:23:21] scaling laws you can kind of predict and
[00:23:23] then like this more granular stuff which
[00:23:25] we really want to know to know how this
[00:23:27] all all is going to go is is much harder
[00:23:29] to know but my guess would be the
[00:23:32] scaling laws are going to continue like
[00:23:34] you know again subject to you know do
[00:23:36] people slow down for safety or for
[00:23:38] regulatory reasons
[00:23:40] um but you know let's just let's just
[00:23:42] put all that aside and say like we have
[00:23:44] the economic capability to keep scaling
[00:23:46] if we did that what would happen and I I
[00:23:49] think my view is we're going to keep
[00:23:50] getting better across the board and I
[00:23:52] don't see any area where the models are
[00:23:54] like super super weak or not starting to
[00:23:57] make progress like that used to be true
[00:23:59] of like math and programming but I think
[00:24:01] over the last six months you know the
[00:24:03] the 2023 generation of models compared
[00:24:06] to the 2022 generation have started to
[00:24:08] learn that there may be more subtle
[00:24:10] things we don't know and so I I kind of
[00:24:13] suspect even if it isn't quite even that
[00:24:16] the rising tide will lift all the boats
[00:24:18] does that include the thing you were
[00:24:20] mentioning earlier where if there's an
[00:24:21] extended task it kind of loses its train
[00:24:24] of thought
[00:24:25] um yeah or its ability to just like
[00:24:26] execute a series so I think that that
[00:24:29] that's going to depend on things like RL
[00:24:32] training to have the model do longer
[00:24:34] Horizon tasks I don't expect that to
[00:24:36] require a substantial amount of
[00:24:38] additional compute
[00:24:41] um I think that um that that was
[00:24:43] probably an artifact of uh yeah kind of
[00:24:47] thinking about RL in the wrong way and
[00:24:48] underestimating how much the model had
[00:24:51] learned on its own in terms of you know
[00:24:53] are we going to be superhuman in some
[00:24:55] areas and not others I think it's
[00:24:57] complicated I could imagine that we
[00:24:59] won't be superhuman in some areas
[00:25:01] because for example they involve like
[00:25:03] embodiment in the physical world and
[00:25:05] then it's like what happens like do the
[00:25:07] AIS help us train faster AIS and those
[00:25:10] faster AIS wrap around and solve that do
[00:25:13] you not need the physical world it
[00:25:15] depends what you mean are we worried
[00:25:16] about an alignment disaster are we
[00:25:18] worried about misuse like making weapons
[00:25:20] of mass destruction are we worried about
[00:25:23] the AI or you know the AI taking over
[00:25:27] research from humans are we worried
[00:25:29] about it reaching some threshold of
[00:25:31] economic productivity where it can do
[00:25:33] what the average these different
[00:25:34] thresholds I think have have different
[00:25:36] answers although I suspect they will all
[00:25:38] come within a few years let me ask about
[00:25:40] those thresholds so if claw was an
[00:25:43] employee at anthropic what salary would
[00:25:45] it be worth what is it like meaningfully
[00:25:46] speeding up AI progress it feels to me
[00:25:49] like an intern in most areas
[00:25:51] um but then some specific areas where
[00:25:53] it's better than that again I think one
[00:25:55] thing that's makes the comparison hard
[00:25:57] is like the form factor is kind of like
[00:26:00] not the same as a human right like a
[00:26:03] human like you know if you were to
[00:26:04] behave like one of these chat Bots like
[00:26:06] we wouldn't really I mean I guess we
[00:26:08] could have this conversation it's like
[00:26:09] but you know they're they're not really
[00:26:11] they're more designed to answer single
[00:26:14] or a few questions right
[00:26:15] um and and like you know they don't have
[00:26:17] a the concept of having a long life of
[00:26:19] Prior experience right we're talking
[00:26:21] here about you know things that
[00:26:23] that I've experienced in the past right
[00:26:25] and chatbots don't don't have that and
[00:26:27] so there's there's all kinds of stuff
[00:26:29] missing and so it's hard to make a
[00:26:31] comparison but it I don't know it it
[00:26:33] they feel like interns in some areas and
[00:26:37] kind of then they have areas where they
[00:26:38] Spike and are really savants where they
[00:26:41] may be better than they may be better
[00:26:43] than anyone here but does the overall
[00:26:45] picture of something like an
[00:26:46] intelligence explosion you know my
[00:26:48] former guest is Carl Schulman and he has
[00:26:49] this like very detailed model of an
[00:26:51] adult does that as somebody who would
[00:26:53] actually like see that happening does
[00:26:55] that make sense to you as they go from
[00:26:57] interns to entry level software
[00:26:58] Engineers those entry level software
[00:26:59] Engineers increase your productivity I I
[00:27:02] think I think the idea that the the AI
[00:27:06] systems become more productive and first
[00:27:09] they speed up the productivity of humans
[00:27:11] then they you know kind of equal the
[00:27:13] productivity of humans and and and you
[00:27:16] know and then they're in some meaningful
[00:27:18] sense the main contributor to Scientific
[00:27:22] progress that that happens at some point
[00:27:24] I I think
[00:27:25] that that basic logic seems likely to me
[00:27:28] although I I have a suspicion that when
[00:27:31] we actually go into the details it's
[00:27:33] going to be kind of like weird and
[00:27:34] different than we expect that all the
[00:27:36] detailed models are kind of
[00:27:39] you know we're thinking about the wrong
[00:27:40] things or we're right about one thing
[00:27:42] and then are wrong about 10 other things
[00:27:44] and and so I I don't know I think we
[00:27:47] might end up in like a weirder world
[00:27:49] than we expect when you add all this
[00:27:52] together
[00:27:53] like your estimate of when we get
[00:27:55] something kind of human level yeah what
[00:27:57] does that look like I mean again it
[00:27:59] depends on the thresholds yeah
[00:28:01] um you know in in terms of someone looks
[00:28:04] at these the model and you know even if
[00:28:07] you talk to it for you know for for an
[00:28:10] hour or so it's it's basically you know
[00:28:13] it's basically like a generally
[00:28:15] well-educated human yeah
[00:28:17] um that could be not very far away at
[00:28:20] all I think
[00:28:21] um like that that could happen in you
[00:28:23] know two or three years like uh you know
[00:28:25] if I look at again like I think the main
[00:28:28] thing that would stop it would be if if
[00:28:30] we hit certain certain you know and we
[00:28:33] have internal tasks for you know safety
[00:28:34] thresholds and stuff like that so if a
[00:28:37] company or the industry decides to slow
[00:28:39] down or you know we're able to get the
[00:28:42] government Institute restrictions that
[00:28:44] kind of uh you know that that moderate
[00:28:46] the rate of progress for safety reasons
[00:28:48] that would be the main reason it
[00:28:50] wouldn't happen but if you if you just
[00:28:51] look at the logistical and economic
[00:28:54] ability to scale I don't think we're
[00:28:56] very far at all from that now that that
[00:28:59] may not be the threshold where the
[00:29:00] models are existentially dangerous uh in
[00:29:03] fact I suspect it's not not quite there
[00:29:04] yet it may not be the threshold where
[00:29:06] the models can take over most AI
[00:29:07] research it may not be the threshold
[00:29:10] where the models you know seriously
[00:29:13] change how the economy Works
[00:29:15] um I think it gets a little murky after
[00:29:16] that and all those thresholds may happen
[00:29:18] at various times after that but I think
[00:29:21] I think in terms of the base technical
[00:29:24] capability of it it kind of It kind of
[00:29:28] sounds like a reasonably generally
[00:29:29] educated human yeah across the board I
[00:29:32] think that could be quite close why
[00:29:33] would it be the case that it could be
[00:29:36] sound you know pass a Turing test for an
[00:29:38] educated person but not be able to
[00:29:40] contribute or substitute for human
[00:29:42] involvement in the economy a couple
[00:29:44] reasons one is just you know that the
[00:29:47] threshold of skill isn't high enough
[00:29:48] right comparative advantage it's like uh
[00:29:50] it like doesn't matter
[00:29:53] that you know I have someone who's
[00:29:55] better than the average human at every
[00:29:57] task like what I really need is like for
[00:29:59] for AI research like you know I need
[00:30:01] what you know I I need to basically find
[00:30:04] something that is is strong enough to
[00:30:07] substantially accelerate you know the
[00:30:09] the like labor of the Thousand experts
[00:30:11] who who are best at it
[00:30:13] um and so we might reach a point where
[00:30:15] we you know the comparative advantage of
[00:30:17] these systems is not Is Not Great uh
[00:30:20] another thing that could be the case is
[00:30:22] that I think there are these kind of
[00:30:24] mysterious frictions that like you know
[00:30:26] kind of don't show up in naive economic
[00:30:28] models but you see it whenever you're
[00:30:31] like you know when you go to a customer
[00:30:32] or something and you're like hey I have
[00:30:34] this cool chat bot in principle it can
[00:30:37] do everything that you know your
[00:30:38] customer service bot does or that this
[00:30:40] part of your company does but like the
[00:30:42] the actual friction of like how do we
[00:30:45] slot it in how do we make it work that
[00:30:47] that includes both kind of like you know
[00:30:50] just the question of how it works in a
[00:30:52] human sense within the company like you
[00:30:54] know how how things happen in the
[00:30:56] economy and overcome frictions and and
[00:30:58] also just like what is the workflow how
[00:31:01] do you actually interact with it it's
[00:31:03] very different to say here's a chat bot
[00:31:06] that kind of looks like it's doing this
[00:31:08] task that you or you know or helping the
[00:31:11] human to do to do some tasks as it is to
[00:31:14] say like okay this thing is this thing
[00:31:16] is deployed in 100 000 people are using
[00:31:19] it often like right now lots of folks
[00:31:22] are rushing to deploy these systems but
[00:31:24] I think in many cases they're not using
[00:31:26] them in anywhere close to the most
[00:31:27] efficient way that they could you know
[00:31:30] not because they're not smart but
[00:31:31] because it takes time to work these
[00:31:33] things out and so I think when things
[00:31:34] are changing this fast they're going to
[00:31:36] be all of these frictions yeah and I and
[00:31:38] I think again these are messy reality
[00:31:41] that doesn't quite get captured in the
[00:31:43] model I don't think it changes the basic
[00:31:45] picture like I don't think it changes
[00:31:46] the idea that we're we're building up
[00:31:48] this snowball of like the models help
[00:31:50] the models get better and you know do
[00:31:52] what the humans and and you know can can
[00:31:54] accelerate what the humans do and
[00:31:55] eventually it's mostly the models doing
[00:31:57] the work like you zoom out far enough
[00:31:58] that's happening but I'm I'm kind of
[00:32:01] skeptical of kind of any kind of precise
[00:32:04] mathematical or exponential prediction
[00:32:06] of how it's going to be I think it's I
[00:32:08] think it's I think it's all going to be
[00:32:10] a mess but I think what we know is it's
[00:32:12] not an ex metaphorical exponential and
[00:32:15] it's gonna happen fast how do those
[00:32:17] different exponentials net out which
[00:32:19] we've been talking about so one was the
[00:32:22] the scaling laws themselves are power
[00:32:24] laws with decaying marginal uh you know
[00:32:27] uh loss per you know parameter or
[00:32:30] something the other exponential you
[00:32:31] talked about is well these things can
[00:32:33] get involved in the process of AI
[00:32:35] research itself speeding it up so those
[00:32:38] two are sort of opposing exponentials
[00:32:40] does it net out to be super linear or
[00:32:42] sublinear and also you mentioned well
[00:32:44] the distribution of intelligence might
[00:32:46] just be broader so should we expect
[00:32:48] after the after we get to this point in
[00:32:50] two to three years it's like
[00:32:51] like what does that look like it's I
[00:32:54] mean I think it's very unclear right so
[00:32:55] we're already at the point where if you
[00:32:57] look at the loss the scaling laws are
[00:32:59] starting to bend I mean we've seen that
[00:33:01] in you know published model cards
[00:33:03] offered by multiple companies
[00:33:06] um so that's not a secret at all but as
[00:33:08] as they start to bend each little bit of
[00:33:10] of entropy right of accurate prediction
[00:33:13] becomes more important right maybe these
[00:33:15] last little bits bits of entropy are
[00:33:16] like well you know this is a physics
[00:33:18] paper as Einstein would have written it
[00:33:20] as opposed to you know as some other
[00:33:22] physicist would have would have would
[00:33:23] have written it and so it's it's hard to
[00:33:25] assess significance from this it
[00:33:28] certainly looks like in terms of
[00:33:30] practical performance the metrics keep
[00:33:32] going up relatively linearly also they
[00:33:35] were always unpredictable uh so so it's
[00:33:37] it's hard to see that and then
[00:33:39] I mean the thing that I think is driving
[00:33:41] the most acceleration is just more and
[00:33:43] more money is going into the field like
[00:33:45] people are seeing that there's just a
[00:33:47] huge amount of you know of of economic
[00:33:50] value and so I expect the price the
[00:33:54] amount of money spent on the largest
[00:33:55] models to go up by like a factor of 100
[00:33:57] or something and for that that then to
[00:33:59] be concatenated with its ships are
[00:34:01] getting faster the algorithms are
[00:34:02] getting better because there's there's
[00:34:04] so many people working on this now and
[00:34:06] so and so again I mean the you know I
[00:34:08] I'm not making a normative statement
[00:34:10] here this is what should happen uh I'm
[00:34:12] not even saying this necessarily will
[00:34:14] happen because I think there's important
[00:34:16] safety and government questions here
[00:34:18] which we're very actively working on I'm
[00:34:20] just I'm just saying like left to itself
[00:34:22] this is what the economy is going to do
[00:34:24] we'll get to those questions in a second
[00:34:25] but um how do you think about the
[00:34:27] contribution of anthropic to that
[00:34:30] increasing in the scope of this industry
[00:34:33] where I mean there's an argument that
[00:34:35] listen with that investment we can work
[00:34:38] on safety stuff at anthropic and another
[00:34:40] that says you're raising the salience of
[00:34:42] this field in general yeah I mean it's
[00:34:44] all it's all costs and benefits right
[00:34:45] the costs are not zero right so I think
[00:34:48] a mature way to think about these things
[00:34:50] is you know not not to deny that there
[00:34:51] are any costs but to think about what
[00:34:53] the costs are and what the benefits are
[00:34:55] you know I think I think we've been
[00:34:56] relatively responsible in the sense that
[00:34:58] you know the big acceleration that that
[00:35:00] happened late last year and and
[00:35:02] beginning of this year like we didn't
[00:35:04] cause that we were we weren't the ones
[00:35:06] who did that and honestly I think if you
[00:35:08] look at the reaction to Google that that
[00:35:09] might be 10 times more important than
[00:35:11] anything else and then kind of once it
[00:35:13] had happened once the ecosystem had
[00:35:14] changed then we did a lot of things to
[00:35:17] kind of to kind of stay on the frontier
[00:35:19] um and and and so I don't know it's it's
[00:35:21] I mean it's like any other question
[00:35:22] right it's like you're trying to you're
[00:35:25] trying to do the things that have the
[00:35:27] biggest costs and the that have the
[00:35:28] lowest costs and the biggest benefits
[00:35:30] um and you know that that causes you to
[00:35:32] have different strategies at different
[00:35:34] times one question I have for you while
[00:35:36] we were talking about the intelligence
[00:35:37] stuff was listen as a scientist yourself
[00:35:39] is it what do you make of the fact that
[00:35:42] these things have basically the entire
[00:35:43] Corpus of human knowledge memorized and
[00:35:45] as far as I'm aware they haven't been
[00:35:47] able to make like a single new
[00:35:49] connection that has led to a discovery
[00:35:51] whereas if even a moderately intelligent
[00:35:53] person had this much stuff memorized
[00:35:54] they'd notice oh this thing causes this
[00:35:57] symptom this other thing also causes the
[00:35:58] symptom you know there's a medical cure
[00:36:00] right here right what should we be
[00:36:02] expecting that kind of stuff I'm not I'm
[00:36:04] not sure I mean I think
[00:36:06] you know I don't know these words
[00:36:08] Discovery creativity like it's one of
[00:36:10] the lessons I've learned is that in you
[00:36:12] know in kind of the Big Blob of compute
[00:36:14] often these these ideas often end up
[00:36:17] being kind of fuzzy and Elusive and hard
[00:36:19] to track down but I think I think there
[00:36:21] is something here which is
[00:36:24] I think the models do display a kind of
[00:36:26] ordinary creativity again again you know
[00:36:28] the kind of like you know write a write
[00:36:30] us on it you know in the style of Cormac
[00:36:33] McCarthy or Barbie or so you know like
[00:36:35] there is some creativity to that and I
[00:36:37] think they do draw you know new
[00:36:39] connections of the kind that an ordinary
[00:36:41] person would draw I I agree with you
[00:36:43] that there haven't been any kind of like
[00:36:44] I don't know like I would say like big
[00:36:46] scientific discoveries I think that's a
[00:36:50] mix of like just the model skill level
[00:36:52] is not is not high enough yet right like
[00:36:55] I was on a podcast last week where where
[00:36:58] the host said I don't know I played with
[00:36:59] these models they're kind of mid right
[00:37:01] like they get you know they get a b or a
[00:37:03] B minus or something and and that that I
[00:37:05] think is going to change with uh with
[00:37:06] the scaling I do think there's an
[00:37:08] interesting point about well the models
[00:37:10] have an advantage which is they know a
[00:37:12] lot more than us you know like should
[00:37:14] should they have an advantage already
[00:37:16] even even if they their skill level
[00:37:18] isn't isn't isn't quite High maybe
[00:37:20] that's kind of what you're getting at I
[00:37:22] don't really have an answer to that I
[00:37:23] mean it seems certainly like
[00:37:25] memorization and facts and drawing
[00:37:27] connections is an area where models are
[00:37:29] ahead and I I do think maybe you need
[00:37:32] those connections and you need a fairly
[00:37:35] high level of skill I do think
[00:37:37] particularly in the area of biology for
[00:37:39] better and For Worse the complexity of
[00:37:42] biology is such that the current models
[00:37:45] know a lot of things right now and
[00:37:48] that's what that's what you need to make
[00:37:49] discoveries and draw it's not like
[00:37:51] physics where you need to you know you
[00:37:53] need to think and come up with a formula
[00:37:54] in biology you need to know a lot of
[00:37:55] things right and so I do think the
[00:37:57] models know a lot of things and they
[00:37:59] have a skill level that's not quite high
[00:38:00] enough to put them together and I think
[00:38:02] they are they are just on the cusp of
[00:38:04] being able to put these things together
[00:38:06] on that point last week in your Senate
[00:38:08] testimony you said that these models are
[00:38:10] two to three years away from potentially
[00:38:12] enabling large-scale biotourism attacks
[00:38:15] or something like that can you make that
[00:38:16] more concrete without obviously giving
[00:38:18] the kind of information that would but
[00:38:20] is it like one-shotting how to weaponize
[00:38:22] something is it or do you gotta find to
[00:38:24] an open source model like what would
[00:38:25] that actually look like I think it'd be
[00:38:27] good to clarify this because we did a
[00:38:28] blog post in the Senate testimony and
[00:38:30] like I think various people kind of
[00:38:32] didn't understand the point or didn't
[00:38:33] understand what we'd done so I think
[00:38:36] today and you know of course in our
[00:38:38] models we try and you know prevent this
[00:38:40] but there's always jailbreaks you can
[00:38:42] ask the models all kinds of things about
[00:38:45] biology and get them to say all kinds of
[00:38:47] scary things yeah uh but often those
[00:38:50] scary things are things that you could
[00:38:51] Google and I'm I'm therefore not
[00:38:54] particularly worried about that
[00:38:56] um I think it's actually an impediment
[00:38:57] to see in the real danger where you know
[00:38:59] someone just says oh I asked this model
[00:39:01] like you know for the small pot you know
[00:39:03] for to tell me some things about
[00:39:04] smallpox and it will that that is
[00:39:07] actually you know kind of not what I'm
[00:39:08] worried about so we spent about six
[00:39:10] months working with some of basically
[00:39:13] some of the folks who are the most
[00:39:14] expert in the world on how to how do
[00:39:18] biological attacks happen
[00:39:20] um you know what what would you need to
[00:39:22] conduct such an attack and how do we
[00:39:23] defend to get such an attack
[00:39:25] they worked very intensively on just the
[00:39:29] entire workflow of if I were trying to
[00:39:31] do a bad thing it's not one shot it's a
[00:39:33] long process there are many steps to it
[00:39:36] um it's not just like I asked the model
[00:39:37] for this one page of information and
[00:39:39] again without going into any detail the
[00:39:42] thing I said in the Senate testimony is
[00:39:44] like there's some steps where you can
[00:39:45] just get information on Google there are
[00:39:48] some steps that are what I'd call
[00:39:49] missing they're scattered across a bunch
[00:39:52] of textbooks or they're not in any
[00:39:55] textbook they're kind of implicit
[00:39:57] knowledge and they're not really like
[00:39:59] they're not explicit knowledge they're
[00:40:01] they're they're they're more like I have
[00:40:03] to do this lab protocol and like what if
[00:40:06] I get it wrong oh if this happens then
[00:40:08] then my temperature was too low if that
[00:40:10] happened I needed to add more of this
[00:40:12] particular reagents what we found is
[00:40:14] that for the most part those missing
[00:40:17] those key missing pieces the models
[00:40:20] can't do them yet but we found that
[00:40:23] sometimes they can
[00:40:25] um and when they can sometimes they
[00:40:26] still hallucinate which is the thing
[00:40:28] that's that's kind of keeping us safe
[00:40:30] but we saw enough signs of the models
[00:40:33] doing doing those those key things well
[00:40:35] and if we look at you know
[00:40:38] state-of-the-art models and go backwards
[00:40:40] to previous models we look at the trend
[00:40:43] it shows every sign of two or three
[00:40:46] years from now
[00:40:48] we're gonna have a real problem yeah
[00:40:49] especially the thing you mentioned on
[00:40:51] the lock scale you go from like 100
[00:40:52] times it gets it right to one in ten two
[00:40:54] exactly so you know I've seen many of
[00:40:56] these like grocks in my life right I was
[00:40:58] there when I I watched when gbt3 learned
[00:41:01] to do arithmetic when gpt2 learned to do
[00:41:04] regression a little bit above chance
[00:41:06] when you know when we got you know with
[00:41:08] Claude and we got better on like you
[00:41:10] know all these all these tests of
[00:41:11] helpful honest harmless I've seen a lot
[00:41:14] of groks this is this is unfortunately
[00:41:16] not one that I'm excited about but I
[00:41:18] believe it's happening so somebody it
[00:41:20] might say listen you were a co-author on
[00:41:22] this post that open AI relates to the
[00:41:23] gpd2 where they said you know we're not
[00:41:26] gonna release the weights or the details
[00:41:28] here because we're worried that this
[00:41:29] model will be used for something you
[00:41:32] know bad and looking back on it now it's
[00:41:35] laughable to think that gpd2 could have
[00:41:37] done anything bad are we just like way
[00:41:39] too worried this is a concern that
[00:41:41] doesn't make sense for her it is
[00:41:43] interesting um it might be worth looking
[00:41:45] back at the actual text of that post
[00:41:47] um so I don't don't remember it exactly
[00:41:49] but it should it you know it's it's
[00:41:51] still up on the internet it says
[00:41:53] something like you know we're choosing
[00:41:55] not to release the weights uh because of
[00:41:57] concerns about misuse but it also said
[00:41:59] this is an experiment we're not sure if
[00:42:03] this is necessary or the right thing to
[00:42:05] do at this time but we'd like to
[00:42:07] establish a norm of thinking carefully
[00:42:09] about these things
[00:42:11] um you know you could think of it a
[00:42:12] little like the you know the the
[00:42:13] cylinder conference in the in the 1970s
[00:42:16] right where it's like you know they were
[00:42:18] just figuring out recombinant DNA you
[00:42:21] know it was not necessarily the case
[00:42:22] that someone could do something really
[00:42:24] bad with recombinant DNA it's just the
[00:42:26] possibilities were starting to become
[00:42:28] clear those words at least were the
[00:42:30] right attitude now I think there's a
[00:42:31] separate thing that like
[00:42:33] you know people don't just judge the
[00:42:35] post they judge the organization is this
[00:42:38] an organization that you know is
[00:42:40] produces a lot of hype or that has
[00:42:42] credibility or something like that and
[00:42:44] so I think that had some effect on it I
[00:42:47] guess you could also ask like is it
[00:42:49] inevitable that people would just
[00:42:50] interpret it as like uh you know you
[00:42:53] can't get across any message more
[00:42:55] complicated than this thing right here
[00:42:57] is dangerous
[00:42:58] um so you can argue about those but I
[00:43:00] think the the basic thing that was in my
[00:43:02] head in the head the head of others who
[00:43:03] were who were involved in that and you
[00:43:06] know I think what what is what is
[00:43:08] evident in the post is like we actually
[00:43:10] don't know we have pretty wide error
[00:43:12] bars on what's dangerous and what's not
[00:43:13] so we should you know like we we want to
[00:43:16] establish a norm of being careful I I
[00:43:18] think by the way we have enormously more
[00:43:20] evidence we've seen enormously more of
[00:43:22] these grocks now and so we're well
[00:43:24] calibrated but there's still uncertainty
[00:43:26] right in all these statements I've said
[00:43:27] like in two or three years we might be
[00:43:30] there right there's a substantial risk
[00:43:31] of it and we don't want to take that
[00:43:33] risk but you know I wouldn't say it's
[00:43:34] it's 100 it could be 50 50. okay let's
[00:43:37] talk about cyber security which in
[00:43:39] addition to bioresk is another thing
[00:43:40] anthropic has been emphasizing how have
[00:43:43] you avoided the cloud micro architecture
[00:43:46] from leaking because as you know your
[00:43:48] competitors have been less successful at
[00:43:49] uh this kind of security can't comment
[00:43:51] on anyone else's security don't know
[00:43:53] what's going on in there a thing that we
[00:43:55] have done is uh you know so so there are
[00:43:58] there are these these architectural
[00:44:00] Innovations right that make training
[00:44:02] more efficient we call them compute
[00:44:03] multipliers because they're the
[00:44:04] equivalent of you know improving
[00:44:06] improving uh you know uh uh they're like
[00:44:09] having more compute our compute
[00:44:11] multipliers again I don't want to say
[00:44:12] too much about it because it could allow
[00:44:14] an adversary to counteract our our
[00:44:16] measures but we limit the number of
[00:44:19] people who are aware of of a given
[00:44:23] compute multiplier to those who need to
[00:44:25] know about it
[00:44:26] um and so there's there's a very small
[00:44:28] number of people who could leak all of
[00:44:30] these secrets there's a larger number of
[00:44:31] people who could leak one of them
[00:44:33] um but you know this is the standard
[00:44:34] compartmentalization strategy that's
[00:44:36] used in the intelligence Community or
[00:44:38] you know resistant cells or or whatever
[00:44:42] um so you know we we've over the last uh
[00:44:45] over the last few months we've
[00:44:47] implemented these measures so you know I
[00:44:49] don't want to jinx anything you might
[00:44:50] say no this could never happen to us
[00:44:52] um but I think I think it would be
[00:44:53] harder for it to happen
[00:44:55] um I don't want to go into any more
[00:44:56] detail and you know but by the way I'd
[00:44:58] encourage all the other companies to do
[00:45:00] this as well it's as much as like
[00:45:02] competitors architectures leaking is is
[00:45:05] narrowly helpful to anthropic it's not
[00:45:06] good for anyone in the long run right
[00:45:09] um so security around this stuff is
[00:45:11] really important even with all the
[00:45:12] security you have could you with your
[00:45:14] current security prevent a dedicated
[00:45:16] state level actor from getting the claw
[00:45:18] two weights it depends how dedicated is
[00:45:20] what is what I would say are our head of
[00:45:23] security who who was you know used to
[00:45:25] work on security for Chrome which you
[00:45:27] know yeah very widely used an attacked
[00:45:30] application he likes to think about it
[00:45:32] in terms of how much would it cost to
[00:45:34] attack anthropic successfully I again I
[00:45:36] don't want to go into Super detail of
[00:45:38] how much I think it will cost to attack
[00:45:39] and it's kind of inviting people but
[00:45:41] like one of our goals is that it costs
[00:45:43] more to attack anthropic than than it
[00:45:46] costs to just straighten your own model
[00:45:48] um uh which doesn't guarantee things
[00:45:50] because you know of course you need the
[00:45:51] talent as well so you might still but
[00:45:53] you know but but attacks have have risks
[00:45:55] who's the Diplomatic costs uh you know
[00:45:57] and and and they use up the very the
[00:46:00] very sparse resources that nation state
[00:46:02] actors might have in order to to do to
[00:46:04] do the attacks
[00:46:05] um so we're not there yet by the way but
[00:46:07] I but I think I think we're to a very
[00:46:11] high standard compared to the size of
[00:46:13] company that we are like I think if you
[00:46:15] look at security for most 150 person
[00:46:18] companies like I think there's there's
[00:46:20] just no comparison
[00:46:21] um but you know could we could we resist
[00:46:23] if if it was a state actor's top
[00:46:26] priority to steal our model weights no
[00:46:29] they would they would succeed how long
[00:46:31] does that stay true because at some
[00:46:33] point the value keeps increasing and
[00:46:35] increasing and another part of this
[00:46:37] question is that what kind of a secret
[00:46:40] is how to train Cloud through your Cloud
[00:46:43] 2 is it you know with nuclear weapons
[00:46:46] for example we had lots of spies you
[00:46:47] just take a blueprint across and that's
[00:46:49] the implosion device and that's what you
[00:46:51] need here is it just is it more tacit
[00:46:53] like the thing you're talking about
[00:46:54] biology you need to know how these
[00:46:55] reagents work is it just like you got
[00:46:57] the blueprint you got the micro
[00:46:58] architecture and Hyper parameters there
[00:47:00] are some things that are like you know a
[00:47:01] one line equation and there are other
[00:47:03] things that are more complicated yeah um
[00:47:05] and I think compartmentalization is the
[00:47:08] the best way to do it just limit the
[00:47:10] number of people who know about
[00:47:11] something if you're a thousand person
[00:47:12] company and everyone knows every secret
[00:47:14] like one I guarantee you have some you
[00:47:16] have a leaker and two I guarantee you
[00:47:18] have a spy like a literal spy okay let's
[00:47:20] talk about alignment and let's talk
[00:47:21] about mechanistic interpretability which
[00:47:23] is the branch yes of which you um you
[00:47:25] guys specialize in while you're
[00:47:27] answering this question you might want
[00:47:28] to explain what mechanistic
[00:47:29] interpretability is but just um the
[00:47:32] broader question is mechanistically what
[00:47:34] is alignment is it that you're locking
[00:47:37] in the model into a benevolent Character
[00:47:40] Are You disabling deceptive circuits and
[00:47:43] procedures like what concretely is
[00:47:45] happening when you align a model I think
[00:47:47] as with most things you know when we
[00:47:49] actually train a model to be aligned we
[00:47:51] don't know what happens inside the model
[00:47:53] right there are different ways of
[00:47:55] training it to be aligned but I think we
[00:47:57] don't really know what happens I mean I
[00:47:58] think for some of the current methods I
[00:48:01] think all the current methods that
[00:48:02] involve some kind of fine-tuning of
[00:48:04] course have the property that the
[00:48:06] underlying knowledge and abilities that
[00:48:07] we might be worried about don't don't
[00:48:10] disappear that's just you know the model
[00:48:13] is just taught not to Output them I
[00:48:15] don't know if that's a fatal flaw or if
[00:48:17] you know or if that's just the way
[00:48:18] things have to be I don't know what's
[00:48:20] going on inside mechanistically and I
[00:48:22] think that's the whole point of
[00:48:23] mechanistic interpretability to really
[00:48:25] understand what's going on inside the
[00:48:28] models at the level of individual
[00:48:29] circuits eventually when it's solid what
[00:48:31] does a solution look like where what is
[00:48:33] it the case where if a cloud four you do
[00:48:36] the mechanistic activity thing and
[00:48:38] you're like I'm satisfied it's a line
[00:48:39] what is it that you've seen yeah so I I
[00:48:42] think I think we don't know that yet I
[00:48:45] think we don't know enough to to know
[00:48:46] that yet I mean I can I can give you a
[00:48:48] sketch for like what the process looks
[00:48:50] like as opposed to what the final result
[00:48:52] looks like
[00:48:53] um so I think verifiability is a lot of
[00:48:56] the challenge here right we have all
[00:48:57] these methods that purport to align AI
[00:49:00] systems and and do succeed at doing so
[00:49:03] for today's tasks but then the the
[00:49:05] question is always if you add a more
[00:49:07] power beautiful model or if you had a
[00:49:09] model in a different situation would it
[00:49:12] would it would it be aligned and so I
[00:49:14] think this problem would be much easier
[00:49:15] if you had an oracle that could just
[00:49:17] scan a model and say like okay I know
[00:49:20] this model is aligned I know what it'll
[00:49:21] do in every situation
[00:49:23] um then the problem would be much easier
[00:49:25] and I think the closest thing we have to
[00:49:27] that is something like mechanistic
[00:49:29] interpretability it's not anywhere near
[00:49:31] up to the task yet but I guess I would
[00:49:34] say I think of it as almost like an
[00:49:36] extended training set an extended test
[00:49:38] set right everything we're doing all the
[00:49:40] alignment methods we're doing are the
[00:49:42] trading set right you you know you can
[00:49:44] you can run tests in them but will it
[00:49:45] really work out a distribution will
[00:49:47] really work in another situation
[00:49:48] mechanistic interpretability is the only
[00:49:50] thing that even in principle and we're
[00:49:53] nowhere near there yet but even in
[00:49:55] principle is the thing where it's like
[00:49:57] it's more like an x-ray of the model
[00:49:59] than a modification of the model right
[00:50:01] it's more like an assessment than an
[00:50:03] intervention and so somehow we need to
[00:50:06] get into a dynamic where we have an
[00:50:07] extended test set an extended training
[00:50:10] set which is all these alignment methods
[00:50:12] and the extended test set which is kind
[00:50:14] of like you you X-ray the model and say
[00:50:17] like okay what worked and what didn't in
[00:50:20] a way that goes beyond just the
[00:50:22] empirical tests that you've that you've
[00:50:23] that you've run right
[00:50:25] um where you're saying what is the what
[00:50:27] what is the model
[00:50:28] going to do in these situations what is
[00:50:31] it within its capabilities to do instead
[00:50:33] of what did it do phenomenologically and
[00:50:36] of course we have to be careful about
[00:50:38] that right one of the things I think is
[00:50:39] very important is we should never train
[00:50:41] for interpretability because I think
[00:50:43] that is that's taking away that
[00:50:45] Advantage right you even have the
[00:50:47] problem you know similar to like
[00:50:48] validation versus test set where like if
[00:50:50] you look at the X-ray too many times you
[00:50:53] can interfere but I think that's a much
[00:50:55] weaker option we should worry about that
[00:50:57] but that's a that's a much weaker
[00:50:59] process it's not automated optimization
[00:51:01] we should just make sure as with
[00:51:03] validation and test sets that we don't
[00:51:04] look at the validation set too many
[00:51:07] times before running the test set but
[00:51:09] you know that's again that's that's more
[00:51:11] of a that's that manual pressure rather
[00:51:13] than automated pressure and so some
[00:51:16] solution where it's like
[00:51:17] we have some dynamic between the
[00:51:20] training and test set where it's like
[00:51:21] we're we're trying things out and we we
[00:51:24] really figure out if they work via way
[00:51:27] of testing them that the model isn't
[00:51:28] optimizing against some some orthogonal
[00:51:31] way like if if I if I think of and I
[00:51:33] think we're never going to have a
[00:51:34] guarantee but some process where we we
[00:51:37] do those things together again not in a
[00:51:39] stupid way there's lots of stupid ways
[00:51:41] to do this where you fool yourself but
[00:51:42] like
[00:51:44] some way to put extended training for
[00:51:47] alignment ability with extended testing
[00:51:50] for alignment ability together in a way
[00:51:52] that actually works I I still don't feel
[00:51:54] like I understand the intuition that
[00:51:57] like why you think this is likely to
[00:51:59] work or this is a promising to pursue
[00:52:00] and let me ask the question in a certain
[00:52:02] more specific way and excuse the
[00:52:04] tortured analogy but listen if you're
[00:52:07] you're an economist and you want to
[00:52:08] understand the economy yeah so you send
[00:52:10] a whole bunch of microeconomists out
[00:52:12] there and one of them studies how the
[00:52:13] restaurant business works one of them
[00:52:14] studies how the tourism business works
[00:52:16] you know one of them started each other
[00:52:17] baking works and at the end they all
[00:52:20] come together and you still don't know
[00:52:22] where there's going to be a recession in
[00:52:23] five years or not why is this not like
[00:52:25] that where you have an understanding of
[00:52:27] we understand how induction heads work
[00:52:28] and a two-layer Transformer we
[00:52:30] understand you know modular arithmetic
[00:52:32] how does this add up to does this model
[00:52:35] want to kill us like what is this model
[00:52:36] fundamentally want a few things on that
[00:52:38] I mean I think that's like the right set
[00:52:40] of questions to ask I think what we're
[00:52:42] hoping for in the end is not not that
[00:52:44] will understand every detail but again I
[00:52:47] would give like the X-ray or the MRI
[00:52:48] analogy that like we can be in a
[00:52:51] position where we can look at the broad
[00:52:53] features of the model and say like is
[00:52:56] this a model whose internal state in
[00:52:58] plans are very different from what it
[00:53:01] externally represents itself to do right
[00:53:03] is this a model where we're
[00:53:05] uncomfortable that you know far too much
[00:53:08] of its computational power is uh you
[00:53:11] know is is devoted to doing what looked
[00:53:13] like fairly destructive and manipulative
[00:53:15] things again we don't know for sure
[00:53:17] whether that's possible but I I think
[00:53:20] some at least positive signs that it
[00:53:22] might be possible again the model is not
[00:53:24] intentionally hiding from you right it
[00:53:27] might turn out that the training process
[00:53:28] hides it from you and you know I can
[00:53:30] think of cases where the model is really
[00:53:31] super intelligent it like thinks in a
[00:53:33] way so that it like affects its own
[00:53:35] cognition I suspect we should think
[00:53:38] about that we should consider everything
[00:53:39] I I I suspect that it may roughly work
[00:53:44] to think of the model as you know if
[00:53:47] it's trained in in in the normal way
[00:53:49] just at you know at the at the just
[00:53:51] getting to just above human level it it
[00:53:54] may be a reason we should check it may
[00:53:56] be a reasonable assumption that
[00:53:59] the internal structure of the model is
[00:54:01] not intentionally optimizing against us
[00:54:02] and I give an analogy like to humans so
[00:54:06] it's actually possible
[00:54:09] um to you know to look at an MRI of
[00:54:11] someone
[00:54:13] um and predict above random chance
[00:54:14] whether they're a psychopath
[00:54:16] um there was actually a story a few
[00:54:18] years back about a neuroscientist who
[00:54:20] was studying this and they looked at his
[00:54:21] own scan and discovered that he was a
[00:54:23] psychopath and then everyone everyone in
[00:54:25] his life was like no no that's this is
[00:54:27] obvious like you're you're a complete
[00:54:28] like you must be a psychopath
[00:54:31] um and he was totally unaware of this
[00:54:33] the basic idea that um you know that
[00:54:37] that there there can be these macro
[00:54:38] features that like like psychopath is
[00:54:40] probably a good analogy for it right
[00:54:41] they're like you know this is what we
[00:54:43] would be afraid of model that's kind of
[00:54:44] like Charming on the surface very goal
[00:54:47] oriented and you know very dark on the
[00:54:49] inside uh you know and and you know on
[00:54:51] the surface their behavior might look
[00:54:52] like the behavior of someone else but
[00:54:54] their goals are very different a
[00:54:55] question somebody might have is listen
[00:54:56] you know you mentioned earlier the
[00:54:58] importance of being empirical yeah um
[00:55:01] and in this case you're trying to
[00:55:02] estimate you know listen are these
[00:55:04] activations sus yeah um but is this
[00:55:08] something we can be a for to be
[00:55:09] empirical about in on you know or do we
[00:55:13] need like a very good first principle
[00:55:15] theoretical reason to think no it's not
[00:55:17] just that these MRIs of the model
[00:55:19] correlate with uh you know being bad we
[00:55:22] need just like some just like deep root
[00:55:24] math proof that this is aligned so it
[00:55:26] depends what you mean by empirical I
[00:55:28] mean a better term would be
[00:55:29] phenomenological like I don't think we
[00:55:31] should be purely phenomenological and
[00:55:33] like you know here are some brain scans
[00:55:35] of like really dangerous models and here
[00:55:37] are some brain scans I think the whole
[00:55:39] idea of mechanistic interpretability is
[00:55:41] to look at the underlying principles and
[00:55:43] circuits but I guess the way I think
[00:55:45] about it is like
[00:55:46] on one hand I've actually always been a
[00:55:50] fan of studying these circuits at the
[00:55:52] lowest level of detail that we possibly
[00:55:53] can and the reason for that is kind of
[00:55:56] that's how you build up knowledge even
[00:55:57] if you're ultimately aiming for there's
[00:56:00] two there's too many of these features
[00:56:02] it's too complicated at the end of the
[00:56:03] day we're trying to build something
[00:56:04] broad
[00:56:06] um and we're trying to build some broad
[00:56:07] understanding I think the way you build
[00:56:09] that up is by trying to make a lot of
[00:56:12] these very specific discoveries like you
[00:56:13] have to you have to understand the
[00:56:15] building blocks and and then you have to
[00:56:17] figure out how to kind of use that to
[00:56:19] draw these broad conclusions even if
[00:56:21] you're not going to figure out
[00:56:22] everything
[00:56:23] you know I think you should probably
[00:56:25] talk to Chris Ola who would have much
[00:56:27] more detail right this is my kind of
[00:56:29] high level thinking on it like crisola
[00:56:31] controls the interpretability agenda
[00:56:33] like you know he's he's the one who
[00:56:35] decides what to what to do on
[00:56:36] interpretability this is my high level
[00:56:39] thinking about it which is not going to
[00:56:40] be as good as his there's a bookcase on
[00:56:42] anthropic rely on the fact that
[00:56:44] mechanistic interpretability is helpful
[00:56:46] for capabilities I I don't think so at
[00:56:48] all
[00:56:49] um uh now I do think I I think in
[00:56:52] principle it's possible that mechanistic
[00:56:54] interpretability could be helpful with
[00:56:55] capabilities we might for various
[00:56:57] reasons not choose to talk about it if
[00:56:59] that were the case uh that you know that
[00:57:02] that wasn't something that I thought
[00:57:04] thought of or that any of us thought of
[00:57:05] at the time of andropics founding I mean
[00:57:07] we we thought of ourselves as like you
[00:57:10] know we're people who are like good at
[00:57:12] scaling models and good at doing safety
[00:57:14] on top of those models and like you know
[00:57:16] we think that we have a very high Talent
[00:57:18] density of folks who are good at that
[00:57:20] and you know my view has always been
[00:57:22] Talent density beats Talent Mass
[00:57:25] um and so you know that's that's more
[00:57:26] that's more of our bull case Talent
[00:57:28] density beats Talent Mass I don't think
[00:57:30] it it depends on some particular thing
[00:57:32] like others are starting to do
[00:57:33] mechanistic interpretability now and I'm
[00:57:35] very glad that they are uh you know that
[00:57:37] was that is a part of our a part of our
[00:57:39] a part of our theory of change is
[00:57:41] paradoxically to make other
[00:57:42] organizations more like us Italian
[00:57:44] density I'm sure is important but
[00:57:46] another thing anthropic has emphasized
[00:57:48] is that you need to have Frontier models
[00:57:50] in order to do Safety Research and of
[00:57:52] course like actually be a company as
[00:57:53] well the current Frontier Model is
[00:57:55] something somebody might guess like GPD
[00:57:57] four o'clock to like 100 million or
[00:57:58] something like that that general or
[00:58:00] order of magnitude in very broad terms
[00:58:02] is not wrong but you know we're two to
[00:58:04] three years from now the kinds of things
[00:58:05] you're talking about we're talking more
[00:58:07] and more orders of magnitude to keep up
[00:58:09] with that and to if it's the case that
[00:58:12] safety requires community on the
[00:58:13] frontier I mean what is the case in
[00:58:15] which anthropic is like competing with
[00:58:17] these leviathans to stay on that same
[00:58:19] scale I mean I think it's uh I think
[00:58:21] it's a very it's a situation with a lot
[00:58:23] of trade-offs right I think it's I think
[00:58:24] it's not easy
[00:58:26] um I guess to go back maybe I'll just
[00:58:28] like answer the questions one by one
[00:58:29] right so like to go back to like you
[00:58:32] know why it why is safety so tied to
[00:58:33] scale right
[00:58:35] um some people don't think it is but
[00:58:36] like if I if I just look at like you
[00:58:38] know where where have been where have
[00:58:40] been the areas that you know you know I
[00:58:42] don't know like safety methods have like
[00:58:44] been put into practice or like worked
[00:58:46] for something for anything even if we
[00:58:48] don't think they'll they'll work in
[00:58:49] general you know I go back to thinking
[00:58:51] of all the ideas you know something like
[00:58:54] you know debate and amplification right
[00:58:56] you know back in 2018 when we wrote
[00:58:58] papers about those at open AI it was
[00:59:00] like well human feedback isn't isn't
[00:59:03] quite gonna work but you know debating
[00:59:04] amplification will take us beyond that
[00:59:06] but then if you if you actually look at
[00:59:09] and we've you know done attempts to do
[00:59:11] debates we're really limited by the by
[00:59:14] the quality of the model uh where it's
[00:59:16] like you know for two models to have a
[00:59:19] debate that is coherent enough that a
[00:59:22] human can judge it so that the training
[00:59:24] process can actually work you need
[00:59:26] models that are at or maybe even Beyond
[00:59:28] on some topics the current Frontier now
[00:59:30] you can come up with with the method you
[00:59:32] can come up with the idea without being
[00:59:34] on the frontier but I you know for me
[00:59:37] that's a very small fraction of what
[00:59:39] needs to be done right it's very easy to
[00:59:40] come up with these methods it's very
[00:59:42] easy to come up with like oh the problem
[00:59:44] is X maybe a solution is why but you
[00:59:47] know I I really want to know you know
[00:59:49] whether things work in practice even for
[00:59:51] the systems we have today and I want to
[00:59:54] know what kinds of things go wrong with
[00:59:55] them I I just feel like you discover 10
[00:59:58] new ideas and 10 new ways that things
[00:59:59] that can go wrong by trying these in
[01:00:01] practice and that that empirical
[01:00:04] learning I think it's it's not just not
[01:00:06] as widely understood as it should be
[01:00:08] kind of every you know I would say the
[01:00:09] same thing about methods like
[01:00:11] constitutional Ai and some people say oh
[01:00:13] it doesn't matter like we know this
[01:00:14] method doesn't work it won't work for
[01:00:16] you know pure alignment I neither agree
[01:00:19] nor disagree with that I think that's
[01:00:20] just kind of overconfident the way we
[01:00:22] discover new things and understand the
[01:00:24] structure of what's going to work and
[01:00:26] what's what's not is by playing around
[01:00:27] with things not that we should just kind
[01:00:29] of blindly say oh this Rook here so
[01:00:31] it'll work there but you you really you
[01:00:34] really start to understand the patterns
[01:00:36] like with like with the scaling laws
[01:00:38] even mechanistic interpretability which
[01:00:40] might be the one area I see where a lot
[01:00:43] of progress has been made without the
[01:00:44] frontier models we're you know we're
[01:00:47] seeing and you know the work that say
[01:00:48] open AI put out a couple a couple months
[01:00:51] ago that you know using very powerful
[01:00:54] models to help you Auto interpret the
[01:00:56] weak models again that's not everything
[01:00:58] you can do in interpretability but you
[01:01:00] know that's a that's a big component of
[01:01:02] it and we you know we found it useful
[01:01:04] too and so you see this this this
[01:01:07] phenomenon over and over again where
[01:01:09] it's like you know the the scaling and
[01:01:12] the safety are these two snakes that are
[01:01:14] like coiled with each other always even
[01:01:16] more than you think right you know with
[01:01:18] interpretability like I think three
[01:01:20] years ago I didn't think that this would
[01:01:22] be as true of interpretability but
[01:01:24] somehow it manages to be true why
[01:01:26] because intelligence is useful it's
[01:01:27] useful for a number of tasks one of the
[01:01:29] tasks that's useful for is like figuring
[01:01:32] out how to judge and evaluate other
[01:01:33] intelligence and maybe someday even even
[01:01:36] for you know doing the alignment
[01:01:37] research itself given all that's true
[01:01:39] what what does that imply for anthropic
[01:01:41] when in two to three years these
[01:01:42] leviathans are doing like 10 billion
[01:01:44] dollar trading runs uh Choice one is if
[01:01:46] it if we can't or if it costs too much
[01:01:49] to stay on the frontier then you know
[01:01:51] then then we shouldn't uh then we
[01:01:53] shouldn't do it and you know we won't
[01:01:55] work with the most advanced models we'll
[01:01:57] see what we can get with you know models
[01:01:59] that are not quite as advanced I think
[01:02:00] you can get some value there like
[01:02:02] non-zero value but I'm I'm kind of
[01:02:04] skeptical that the value is all that
[01:02:07] high or the learning can be fast enough
[01:02:08] to really to really be in favor of the
[01:02:10] task the second option is you just you
[01:02:13] just find a way you just uh you know you
[01:02:15] just accept the trade-offs and I think
[01:02:18] the trade-offs are more positive than
[01:02:21] they appear because of a phenomenon that
[01:02:23] I've called race to the top
[01:02:25] um I could go into that later but I'll
[01:02:27] just let me put that aside for now uh
[01:02:29] and then I think the third phenomenon is
[01:02:31] you know as things get as things get to
[01:02:34] that scale I think this may coincide
[01:02:37] with you know starting to get into some
[01:02:40] non-trivial probability of very serious
[01:02:42] danger again I think it's going to come
[01:02:44] first from misuse the kind of Bio stuff
[01:02:47] that I talked about but I don't think we
[01:02:49] have the level of autonomy yet to worry
[01:02:52] about some of the you know alignment
[01:02:54] stuff happening in like two years but it
[01:02:58] might not be very far behind that at all
[01:03:00] you know that that may that may lead to
[01:03:03] unilateral or multilateral or government
[01:03:06] enforced which we support
[01:03:09] decisions uh not to scale as fast as we
[01:03:12] could
[01:03:13] um that may end up being the right thing
[01:03:14] to do so I you know actually that's kind
[01:03:16] of like I I kind of hope things go in
[01:03:18] that in that direction and then we don't
[01:03:20] have this hard trade-off between we're
[01:03:22] not in the frontier and we can't quite
[01:03:23] do the research as well as well as we
[01:03:25] want or influence other orgs as well as
[01:03:27] we want
[01:03:28] um or versus we're kind of on the
[01:03:30] frontier and like have to accept the
[01:03:32] trade-offs which are which are net
[01:03:34] positive but like have a have a lot in
[01:03:36] both in both directions okay on the
[01:03:38] missus versus misliment those are both
[01:03:40] problems as you mentioned but in the
[01:03:42] long scheme of things what what is what
[01:03:45] are you concerned about like 30 years
[01:03:46] down the line which do you think will be
[01:03:48] consider a bigger problem I think it's
[01:03:50] much less than 30 years um but I'm I'm
[01:03:52] worried about both I don't know if you
[01:03:54] have if you if you have a model that
[01:03:56] could in theory you know like take over
[01:03:58] the world on its own
[01:04:00] um if you were able to control that
[01:04:01] model then you know it follows pretty
[01:04:03] simply that you know if model was
[01:04:06] following the wishes of some small
[01:04:08] subset of people and not others then
[01:04:09] those people could use it to take over
[01:04:11] the world on their on their behalf the
[01:04:13] very premise of misalignment means that
[01:04:16] we should be be worried about misuse as
[01:04:18] well with similar levels of consequences
[01:04:21] but but some people who might be more
[01:04:22] doomery than you would say misuse is
[01:04:26] you're already working towards the
[01:04:28] optimistic scenario there because you've
[01:04:30] at least figured out how to align the
[01:04:32] model with the bad guys now you just
[01:04:34] need to make sure that it's aligned with
[01:04:36] the good guys instead why do you think
[01:04:37] that you could get to the point where
[01:04:38] it's aligned with the bat you know you
[01:04:41] haven't already saw this I guess if you
[01:04:42] had the view that like alignment is
[01:04:44] completely unsolvable then uh you know
[01:04:46] then you'll be like well I don't you
[01:04:47] know we're dead anyway so I don't want
[01:04:49] to worry about misuse that's not my
[01:04:50] position at all but but also like you
[01:04:53] should think in terms of like what's a
[01:04:54] plan that would actually succeed that
[01:04:56] would make things good any plan that
[01:04:58] actually succeeds regardless of how hard
[01:05:01] misalignment is to solve any problem any
[01:05:03] plan that actually succeeds is going to
[01:05:05] need to solve misuse as well as
[01:05:07] misalignment it's getting to solve the
[01:05:09] fact that like as the AI models get
[01:05:11] better you know faster and faster
[01:05:13] they're going to create a big problem
[01:05:15] around the balance of power between
[01:05:17] countries they're going to create a big
[01:05:18] problem around is it possible for a
[01:05:21] single individual to do something bad
[01:05:22] that it's hard for everyone else to stop
[01:05:25] any actual solution that leaves do leads
[01:05:27] to a good future needs to solve those
[01:05:29] problems as well if your perspective is
[01:05:31] we're screwed because we can't solve the
[01:05:33] first problem so don't worry about
[01:05:34] problems two and three like that that's
[01:05:37] not really a statement you shouldn't
[01:05:38] worry about problems two and three right
[01:05:39] like they're in our path what no matter
[01:05:42] what yeah in the scenario we succeed we
[01:05:44] have to solve all so yeah we might as
[01:05:46] well operate we should be planning for
[01:05:47] Success not for failure if research
[01:05:49] doesn't happen and the right people have
[01:05:51] the Superhuman models what does that
[01:05:53] look like like who are the right people
[01:05:55] who is actually controlling the model
[01:05:57] from five years from now yeah I mean my
[01:05:59] my view is that these things are
[01:06:02] powerful enough that I think you know
[01:06:04] it's it's going to involve you know
[01:06:06] substantial role or at least involvement
[01:06:09] of you know some kind of government or
[01:06:13] assembly of government bodies again like
[01:06:15] you know they're they're kind of very
[01:06:16] naive versions of this like you know I
[01:06:19] don't think we should just you know I
[01:06:21] don't know like he hand the model over
[01:06:23] to the U.N or whoever happens to be in
[01:06:24] office at a given time like I could see
[01:06:27] that go poorly but they're it's it's too
[01:06:29] powerful there needs to be some kind of
[01:06:31] legitimate process for managing this
[01:06:34] technology which you know includes the
[01:06:37] role of the people building it includes
[01:06:38] the role of like democratically elected
[01:06:41] authorities includes the role of you
[01:06:43] know all the all the individuals who
[01:06:46] will be affected by it so that they're
[01:06:47] they're at the end of the day there
[01:06:49] needs to be some politically legitimate
[01:06:52] process but what that look like if it's
[01:06:54] not the case that you just hand it to
[01:06:55] whoever the president is at the time
[01:06:56] yeah is what does the body look like
[01:06:58] what I I mean this is something these
[01:07:01] are things it's really hard to know
[01:07:02] ahead of time like I think you know
[01:07:04] people love to kind of propose these
[01:07:06] broad plans and say like ah this is the
[01:07:08] way we should do it this is the way we
[01:07:09] should do it I think the honest fact is
[01:07:11] that we're figuring this out as we go
[01:07:12] along and that you know anyone who says
[01:07:16] you know this is this is the body that
[01:07:18] you know we should create this kind of
[01:07:19] body modeled after this thing like I
[01:07:21] think I think we should try things and
[01:07:23] experiment with them with less powerful
[01:07:25] versions of the technology we need to
[01:07:28] figure this out in time but but also
[01:07:29] it's not the really the kind of thing
[01:07:31] you can know in advance the the
[01:07:32] long-term benefit trust that you have
[01:07:35] how did how would that interface with
[01:07:36] this body is that the body itself if not
[01:07:38] is it like was it just for the content
[01:07:40] protection system I want to explain what
[01:07:41] it is for the audience but I don't know
[01:07:43] I think of the long-term benefit trust
[01:07:45] is like a much a much narrower thing
[01:07:46] like this is something that like makes
[01:07:48] decisions for anthropic so this is
[01:07:51] basically a body is described in a
[01:07:54] recent Vox article we'll be saying more
[01:07:55] about it in you know later later this
[01:07:58] year uh but it's basically a body that
[01:08:00] over time uh gains the ability to
[01:08:04] appoint the majority of the board seats
[01:08:06] of anthropic uh and this is so you know
[01:08:08] it's a mixture of experts and I'd say
[01:08:10] like AI alignment National Security and
[01:08:14] philanthropy in general but if control
[01:08:16] is handed to them of anthropic that
[01:08:18] doesn't imply that control of if
[01:08:19] anthropic has AGI the control of AGI
[01:08:22] itself is handed them that doesn't imply
[01:08:23] that anthropic or any other entity
[01:08:25] should be the entity that like makes
[01:08:27] decisions about AGI on behalf of
[01:08:29] humanity I would think of those as
[01:08:31] different I mean there's lots of maybe
[01:08:32] you know like if anthropic does play a
[01:08:34] broad role then you'd want to like widen
[01:08:36] that body to be you know like a whole
[01:08:38] bunch of different people from around
[01:08:39] the world or or maybe you can screw this
[01:08:41] as very narrow and then you know there's
[01:08:43] some like broad committee somewhere that
[01:08:46] like manages all the agis of all the
[01:08:48] companies on behalf on behalf of anyone
[01:08:50] um I I don't know like I I think my view
[01:08:52] is you you shouldn't be sort of overly
[01:08:55] constructive in utopian like we're
[01:08:57] dealing with a new problem here we need
[01:08:59] to we need to start thinking now about
[01:09:01] you know what are the what are the
[01:09:03] governmental bodies and structures that
[01:09:05] could that could deal with it okay so
[01:09:07] let's forget about governance let's just
[01:09:08] talk about what this going well looks
[01:09:10] like obviously there's the things we can
[01:09:12] all agree on you know cure all the
[01:09:13] diseases you know solve all the problems
[01:09:15] every things all humans would say I'm
[01:09:17] down for that yeah but now it's 20 30
[01:09:20] you've solved all the real problems that
[01:09:21] everybody can agree on what what happens
[01:09:24] next what what are we doing with a
[01:09:25] superhuman God I think I actually want
[01:09:28] to like I don't know like disagree with
[01:09:29] the framing or something like this
[01:09:31] um I I actually get nervous when someone
[01:09:33] says like what are you gonna do with the
[01:09:34] Superhuman AI like we've learned a lot
[01:09:37] of things over the last 150 years about
[01:09:39] like markets and democracy and each
[01:09:42] person can kind of Define for themselves
[01:09:44] like what what the best way for them to
[01:09:47] have The Human Experience is and that
[01:09:49] you know society's workout norms and
[01:09:52] what they value in this just in this
[01:09:53] very like complex and decentralized way
[01:09:56] now again if you have these safety
[01:09:58] problems that can be a reason why you
[01:10:01] know and especially from the government
[01:10:02] there needs to be maybe until we solve
[01:10:04] these problems a certain amount of like
[01:10:06] centralized control but but as a matter
[01:10:08] of like we've solved all the problems
[01:10:10] now how do we make things good I think
[01:10:12] that that most most people most groups
[01:10:15] most ideologies that started with like
[01:10:17] let's sit down and think up to think I
[01:10:20] think think over what the definition of
[01:10:21] the good life is like I think I think
[01:10:23] most of those have led to disaster but
[01:10:25] so this Vision you have a sort of
[01:10:26] tolerant liberal democracy
[01:10:28] market-oriented system with a AGI like
[01:10:31] what is each person has their own AGI
[01:10:33] like what is that what does that mean I
[01:10:35] don't know I don't know what it looks
[01:10:36] like right like I guess what I'm saying
[01:10:38] is like we need to solve the kind of
[01:10:40] important safety problems and the
[01:10:42] important externalities and then and
[01:10:44] then subject to that you know which
[01:10:46] again you know those could be just
[01:10:48] narrowly about alignment there could be
[01:10:50] a bunch of economic issues that are
[01:10:52] super complicated and that we can't
[01:10:53] solve you know subject to that like we
[01:10:56] should think about what's worked in the
[01:10:57] past and I think in general like unitary
[01:11:01] Visions for what it means to to live a
[01:11:03] good life have have not worked out well
[01:11:05] at all on on the opposite end of things
[01:11:07] going well or good actors having control
[01:11:09] of AI
[01:11:10] um we might want to touch on China as
[01:11:12] like a potential actor in the space so
[01:11:15] first of all I mean being at Baidu and
[01:11:18] like this seeing progress in AI
[01:11:20] happening generally
[01:11:21] why do you think the Chinese have
[01:11:23] underperformed you know Baidu had a
[01:11:25] scaling laws group many years back
[01:11:28] um or is the premise wrong and I'm just
[01:11:29] not aware of the progress that's
[01:11:30] happening there um well for the scaling
[01:11:32] laws group I mean that was an offshoot
[01:11:33] of the stuff we did with speech
[01:11:35] um so uh you know there were still some
[01:11:37] people there but that was a mostly
[01:11:38] Americanized lab I mean I was there for
[01:11:41] a year that was you know my first foray
[01:11:43] in a deep learn it was led by Andrew
[01:11:44] Wing I never went to China most you know
[01:11:46] there's like a U.S lab so I think that
[01:11:49] was somewhat uh disconnected although it
[01:11:51] was an attempt by you know a Chinese
[01:11:53] entity to kind of get it get into the
[01:11:54] game uh but I don't know I think since
[01:11:57] then you know I couldn't speculate but I
[01:11:59] think they've been maybe very
[01:12:01] commercially focused and not as focused
[01:12:03] on these kind of fundamental research
[01:12:06] side of things around scaling laws now I
[01:12:08] do think because of all the you know
[01:12:11] excitement with the release of chat GPT
[01:12:13] in you know November or so
[01:12:16] um you know that's been a starting gun
[01:12:18] for them as well and they're trying very
[01:12:19] aggressively to catch up now I think
[01:12:22] we're the U.S is quite substantially
[01:12:24] ahead but I think they're trying very
[01:12:25] hard to catch up now how do you think
[01:12:28] China thinks about AGI are they thinking
[01:12:30] about safety and misuse or not I I don't
[01:12:33] really have a sense
[01:12:35] um you know one concern I would have or
[01:12:36] if people say things like well China
[01:12:38] isn't going to develop an AI because you
[01:12:41] know they like stability or you know
[01:12:43] they're going to have all these
[01:12:44] restrictions to make sure things are in
[01:12:46] line with what the CCP wants you know
[01:12:48] that that might be true in the short
[01:12:50] term and for Consumer products My worry
[01:12:52] is that if the basic incentives are
[01:12:55] about National Security and power
[01:12:57] um that's going to become clear sooner
[01:12:58] or later
[01:13:00] um and and so you know they're they're I
[01:13:02] think they're gonna if they see this as
[01:13:04] you know a source of National Power
[01:13:05] they're going to at least try to do to
[01:13:07] do what's most effective and that you
[01:13:09] know that could lead them in the
[01:13:10] direction of AGI at what point it like
[01:13:13] is it possible for them they just get
[01:13:14] your blueprints or your code base or
[01:13:16] something that they can just spin up
[01:13:18] their own lab that is competitive at the
[01:13:19] frontier with the leading American
[01:13:21] company well I don't know about fast but
[01:13:23] I'm like I'm concerned about this
[01:13:26] um so this is one reason why we're
[01:13:27] focusing so hard on cyber security
[01:13:30] um you know we've worked with our Cloud
[01:13:31] providers we really you know like you
[01:13:34] know we have this blog post out out
[01:13:36] about security where we said you know we
[01:13:38] have a two key system for access to the
[01:13:39] model weights we have other measures
[01:13:41] that we put in place so thinking or
[01:13:43] putting in place that you know we
[01:13:45] haven't announced we don't want an
[01:13:46] adversary to know about them but we're
[01:13:48] happy to talk about them broadly all
[01:13:50] this stuff we're doing is is by the way
[01:13:51] not sufficient yet for super determined
[01:13:54] state state level actor at all
[01:13:56] um uh I think it it will defend against
[01:13:59] most attacks and against a a state level
[01:14:03] actor who's not you know who's less
[01:14:06] determined uh but there's a lot more we
[01:14:09] need to do and some of it may require
[01:14:10] new research on how to do security okay
[01:14:13] so let's talk about what it would take
[01:14:14] at that point uh you know we're at
[01:14:16] anthropic offices and you know it's like
[01:14:18] God good at security we had to get
[01:14:20] Badges and everything to come in here
[01:14:22] but the eventual version of this
[01:14:24] building or bunker or whatever where the
[01:14:26] AGI is built I mean what does that look
[01:14:28] like are we is it a building in the
[01:14:30] middle of San Francisco or is it you're
[01:14:31] out of the middle of Nevada or Arizona
[01:14:32] like what is the point in which your
[01:14:35] like Los alamosing it at one point there
[01:14:37] was a running joke somewhere that you
[01:14:40] know the way the way building AGI would
[01:14:42] look like because you know there would
[01:14:43] be a data center next to a nuclear power
[01:14:45] plant next to a bunker yeah um and you
[01:14:48] know that we we'd all we'd all kind of
[01:14:49] live in the bunker and everything would
[01:14:50] be local so it wouldn't get on the
[01:14:51] internet
[01:14:52] um you know again if we you know if we
[01:14:54] take seriously the rate at which the you
[01:14:57] know the rate at which all this is going
[01:14:59] to happen which I don't know I can't be
[01:15:01] sure of it but if we take that seriously
[01:15:03] then it you know it it does make me
[01:15:06] think that maybe not something quite as
[01:15:08] cartoonish as that but that something
[01:15:10] like that might happen what is the time
[01:15:12] scale on which you think alignment is
[01:15:14] solvable if like these models are
[01:15:16] getting to human level or in some things
[01:15:18] in two to three years what is the point
[01:15:20] at which they're aligned I think this is
[01:15:22] a really difficult question because I
[01:15:23] actually think often people are thinking
[01:15:25] about kind of alignment in the wrong way
[01:15:26] I I think there's a general feeling that
[01:15:29] it's like models are misaligned or like
[01:15:31] there's like an alignment problem to
[01:15:33] solve kind of like the Riemann
[01:15:35] hypothesis or something like someday
[01:15:37] we'll crack the Riemann hypothesis
[01:15:39] I don't quite think it's like that not
[01:15:42] in a way that's I that's worse or better
[01:15:43] it might be just as bad or just as just
[01:15:46] as unpredictable when when I think of
[01:15:48] like you know why am I why am I scared
[01:15:51] um few things I think of one is look
[01:15:53] like I think the thing that's really
[01:15:55] hard to argue with is like there will be
[01:15:57] powerful models they will be agentic
[01:15:59] we're getting towards them if such a
[01:16:02] model wanted to wreak havoc and Destroy
[01:16:05] Humanity or whatever I I think we have
[01:16:07] basically no ability to stop it like
[01:16:09] that's that's I think just just if
[01:16:11] that's not true at some point it'll
[01:16:13] continue to be true as we you know it
[01:16:15] will reach the point where it's true as
[01:16:16] we scale the models
[01:16:18] um so that definitely seems the case and
[01:16:20] I think a second thing that seems the
[01:16:22] case is that we seem to be bad at
[01:16:25] controlling the models not in any
[01:16:27] particular way but just their
[01:16:29] statistical systems and you can ask a
[01:16:31] million things and they can say a
[01:16:32] million things and reply uh and you know
[01:16:35] you might not have thought of a
[01:16:36] millionth of one thing that does
[01:16:37] something crazy or when you you train
[01:16:39] them you train them this very abstract
[01:16:41] way and you might not understand all the
[01:16:43] consequences of of what they do in
[01:16:45] response to that I mean I think the best
[01:16:47] example we've seen of that is like being
[01:16:50] in being in Sydney right where it's like
[01:16:51] I I don't know how they train that model
[01:16:53] I don't know what they did to make it do
[01:16:55] all this weird stuff like you know
[01:16:56] threaten threaten people and you know
[01:16:59] have this kind of weird obsessive
[01:17:00] personality but but what it shows is
[01:17:02] that we can get something very different
[01:17:04] from and maybe opposite to what we
[01:17:06] intended and so I actually think facts
[01:17:09] number one and fact number two are like
[01:17:11] enough to be really worried
[01:17:13] um like you don't need all this detailed
[01:17:16] stuff about you know conversion
[01:17:18] instrumental goals or you know analogies
[01:17:21] to Evolution like actually one and two
[01:17:23] for me are pretty motivated I'm like oh
[01:17:25] yeah this thing's gonna be powerful it
[01:17:26] could destroy us and like all the ones
[01:17:29] we built so far are like you know are at
[01:17:31] pretty decent risk of doing some random
[01:17:33] we don't understand yeah if I agree
[01:17:35] with that and I'm like okay I'm
[01:17:37] concerned about this the researchers and
[01:17:38] you have of a mechanistic
[01:17:41] interpretability plus you know
[01:17:42] Constitution Ai and the other IL HF
[01:17:44] stuff if you say that we're going to get
[01:17:47] something with like bio weapons or
[01:17:49] something that could be dangerous in two
[01:17:50] to three years yes do these things
[01:17:52] culminate within two to three years of
[01:17:54] actually meaningfully contributing to
[01:17:55] yeah preventing yes so I think I think
[01:17:58] where I was going to go with this is
[01:18:00] like you know people talk about like
[01:18:01] Doom by default or alignment by default
[01:18:03] like I think it might be kind of
[01:18:05] statistical like you know like you might
[01:18:07] get you know with the current models you
[01:18:10] might get Bing or Sydney or you might
[01:18:11] get clawed and it doesn't really matter
[01:18:12] because Binger Sydney like if we take
[01:18:15] our current understanding and and you
[01:18:18] know move that to to very powerful
[01:18:19] models you might just be in this world
[01:18:21] where it's like okay you make something
[01:18:23] and depending on the details maybe it's
[01:18:25] totally fine
[01:18:26] um you know not really alignment by
[01:18:28] default but but just kind of like it
[01:18:30] depends on a lot of the details and like
[01:18:31] if you if you're very careful about all
[01:18:34] those details and you know what you're
[01:18:35] doing you're getting it right but we
[01:18:37] have a high susceptibility to you mess
[01:18:39] something up in a way that you didn't
[01:18:41] really understand was connected to
[01:18:43] actually instead of making all the
[01:18:45] humans happy it wants to you know turn
[01:18:46] them into pumpkins yeah I you know I
[01:18:48] just some weird right because the
[01:18:49] models are so powerful you know they're
[01:18:51] like these kind of giants that are you
[01:18:53] know they're they're like you know
[01:18:54] they're standing in a landscape and if
[01:18:56] they start to move their arms around
[01:18:57] randomly they could just break
[01:18:58] everything
[01:18:59] um I I guess I'm starting it with that
[01:19:01] with that kind of framing because it's
[01:19:02] not like I don't think we're lying by
[01:19:04] default I don't think we're doomed by
[01:19:06] default and have some problem we need to
[01:19:08] solve it has some kind of different
[01:19:10] character now what I do think is that
[01:19:13] hopefully within a time scale of 2 to
[01:19:15] three years we get better at diagnosing
[01:19:18] when the models are good and when
[01:19:19] they're bad we get better at training
[01:19:22] you know increasing our repertoire of
[01:19:25] methods to train the model that they're
[01:19:28] less likely to do bad things and more
[01:19:29] likely to do good things in a way that
[01:19:31] isn't just relevant to the current
[01:19:33] models but scales and we can help
[01:19:35] develop that with interpretability as
[01:19:37] the test set I don't think of it as oh
[01:19:39] man we tried our lhf it didn't work we
[01:19:41] tried constitutional it didn't work like
[01:19:43] we tried this other thing it didn't work
[01:19:45] we tried mechanistic interpretability
[01:19:46] now we're going to try mechanistic
[01:19:48] um I think this Frame of like man we
[01:19:51] haven't cracked the problem yet we
[01:19:52] haven't solved the Riemann hypothesis
[01:19:54] isn't quite right I think of it more as
[01:19:58] already with today's systems we are not
[01:20:01] very good at controlling them and the
[01:20:03] consequences of that could be could be
[01:20:04] could be very bad we just need to get
[01:20:08] more ways of like increasing the
[01:20:11] likelihood that are that are that you
[01:20:13] know that we can control our models and
[01:20:14] understand what's going on in them and
[01:20:16] like we have some of them so far they
[01:20:19] aren't that good yet
[01:20:21] um but you know I I don't think if this
[01:20:23] is binary of like works and not works
[01:20:25] we're going to develop more and I do
[01:20:27] think that over over the next two to
[01:20:28] three years we're going to start eating
[01:20:30] that probability mass of ways things can
[01:20:32] go wrong
[01:20:33] um you know it's kind of like in the
[01:20:34] core safety views paper there's
[01:20:36] probability mass of how hard the problem
[01:20:38] is I feel like that way of seeing it
[01:20:40] isn't really even quite right right
[01:20:42] because I don't feel like it's the
[01:20:43] remodel hypothesis to solve I I you know
[01:20:45] I I just feel like you know it's almost
[01:20:48] like right now if I try and you know
[01:20:50] juggle five balls or something I can
[01:20:51] juggle three balls right I actually can
[01:20:53] but but I can't juggle five balls at all
[01:20:55] right you have to practice a lot to do
[01:20:57] that if I were to do that I would mostly
[01:20:59] draw I would I would almost certainly
[01:21:00] drop them and then just just over time
[01:21:02] you just get better at the task of
[01:21:04] controlling the balls on that post in
[01:21:06] particular what is your personal
[01:21:08] probability distribution over so for the
[01:21:11] audience the three possibilities are it
[01:21:13] is like trivial to align these models
[01:21:15] with rlhf plus plus to it is a difficult
[01:21:18] problem but one that a big company could
[01:21:20] solve to something that is like
[01:21:23] basically impossible for human
[01:21:24] civilization currently to solve if I'm
[01:21:26] capturing those three what is your
[01:21:27] probability distribution over those
[01:21:29] three personally yeah I mean I'm not
[01:21:30] super into like what's your probability
[01:21:32] distribution of X I think all of those
[01:21:35] have enough likelihood that you know
[01:21:36] they should be considered seriously I'm
[01:21:39] more interesting question I'm much more
[01:21:40] interested in is what could we learn
[01:21:43] that shifts probability Mass between
[01:21:44] them what is the answer to that I think
[01:21:46] that one of the things mechanistic
[01:21:48] interpretability is going to do more
[01:21:51] than more than necessarily solve
[01:21:53] problems is it's going to tell us what's
[01:21:55] going on when we try to align models
[01:21:58] um I I I I think it's basically going to
[01:22:00] teach us about this like one way I could
[01:22:02] imagine
[01:22:03] concluding that things are very
[01:22:05] difficult is if mechanistic
[01:22:07] interpretability sort of shows us that I
[01:22:11] don't know problems tend to get moved
[01:22:13] around instead of being Stamped Out or
[01:22:16] that uh you get rid of one problem you
[01:22:18] create another one or it might Inspire
[01:22:21] us or give us insight into why problems
[01:22:23] are kind of persistent or hard to
[01:22:25] eradicate or crop up like for me to
[01:22:28] really believe some of these stories
[01:22:30] about like you know oh something will
[01:22:33] always you know there's always this
[01:22:34] conversion goal in this particular
[01:22:35] direction I think the abstract story is
[01:22:38] it's not uncompelling but I don't find
[01:22:40] it really compelling either nor do I
[01:22:43] find it necessary to motivate all the
[01:22:44] safety work but like the kind of thing
[01:22:46] that would would really be like oh man
[01:22:48] we can't solve this is like we see it
[01:22:50] happening inside inside the X-ray
[01:22:52] because yeah because I I think right now
[01:22:54] there's just there's there's way there's
[01:22:56] way too many assumptions there's way too
[01:22:58] much overconfidence about how all this
[01:23:00] is gonna go
[01:23:01] um I have a substantial probability Mass
[01:23:03] on this all goes wrong it's a complete
[01:23:06] disaster
[01:23:07] um but in a completely different way
[01:23:08] than anyone had anticipated it would be
[01:23:10] besides the point to ask like how could
[01:23:11] it Go different than anyone anticipated
[01:23:12] so on this in particular what
[01:23:15] information would be relevant how much
[01:23:17] would the difficulty of aligning Cloud
[01:23:20] three and the next generation of models
[01:23:22] basically be like is that a big piece of
[01:23:24] information is that so so I think the
[01:23:26] people who are most worried are
[01:23:28] predicting that
[01:23:30] all the sub-human like AI models are
[01:23:33] going to be alignable right they're
[01:23:34] going to seem aligned they're going to
[01:23:36] deceive Us in some way I think it
[01:23:38] certainly gives us some information but
[01:23:41] uh I I am more interested in what
[01:23:44] mechanistic interpretability can tell us
[01:23:46] um because uh again like you see this
[01:23:50] x-ray it would be too strong to say it
[01:23:52] doesn't lie but at least in the current
[01:23:55] systems it doesn't feel like it's
[01:23:57] optimizing against us there are exotic
[01:23:59] ways that it could you know I I don't
[01:24:01] think anything is a safe bet here but I
[01:24:03] think it's the closest we're going to
[01:24:05] get to something that isn't actively
[01:24:06] optimizing against us all right let's
[01:24:08] talk about the specific methods other
[01:24:09] than mechanistic interpretability yes
[01:24:11] that you guys are researching when we
[01:24:13] talk about um rlhf or you know
[01:24:15] Constitution AI whatever rhf plus plus
[01:24:18] if you had to put it in terms of human
[01:24:20] psychology what is the change that is
[01:24:24] happening are we creating new drives new
[01:24:27] goals new thoughts how is the models
[01:24:30] changing in terms of psychology when it
[01:24:32] I think all those terms are kind of like
[01:24:34] inadequate for you know describing
[01:24:36] what's it's not clear how useful they
[01:24:37] are as abstractions for humans either I
[01:24:39] think we don't have the language to
[01:24:41] describe what's going on and again I'd
[01:24:43] love to have the X-ray I'd love to look
[01:24:44] inside and say and and kind of actually
[01:24:47] know what we're talking about instead of
[01:24:49] you know basically making up words which
[01:24:51] is what which is what I do what am I
[01:24:53] what you're doing and asking this
[01:24:54] question
[01:24:55] um where where you know we should we
[01:24:57] should just be honest we have we really
[01:24:58] have very little idea what we're what
[01:25:00] we're talking about so you know it would
[01:25:02] be great to say well what we actually
[01:25:03] mean by that is you know this circuit
[01:25:06] within here turns you know turns on and
[01:25:08] you know and you know after we've
[01:25:10] trained the model then you know this
[01:25:11] circuit is no longer operative or weaker
[01:25:13] or not yeah I would love to be able to
[01:25:15] say again we're it's going to take a lot
[01:25:18] of work to be able to do that model
[01:25:19] organisms which you hinted at before
[01:25:20] when he said we're doing these
[01:25:21] evaluations to see if they're capable of
[01:25:24] you know doing dangerous things now and
[01:25:26] currently not how worried are you about
[01:25:28] a lab leak scenario where in fine-tuning
[01:25:31] it or in trying to get these models to
[01:25:33] elicit dangerous behaviors you know make
[01:25:36] bio weapons or something yeah like leaks
[01:25:38] somehow and actually makes the bio
[01:25:40] weapon instead of telling you it can
[01:25:41] make the bio weapon with today's passive
[01:25:43] models I think it's not that much you
[01:25:45] know chat Bots it's not so much of a
[01:25:47] concern right because it's like you know
[01:25:49] if we were to fine-tune a model do that
[01:25:51] we do it privately and work with the
[01:25:53] experts and so you know the the leak
[01:25:55] would be like you know suppose the model
[01:25:58] got open sourced or something and you
[01:26:00] know and then someone so so I think for
[01:26:02] now it's mostly a security issue in
[01:26:04] terms of models truly being dangerous I
[01:26:07] mean you know I think I think we do have
[01:26:09] to worry that it's like you know if we
[01:26:11] make a truly powerful model and we're
[01:26:13] trying to like see what makes it
[01:26:15] dangerous or safe then they're could be
[01:26:17] more of a One-Shot thing where it's like
[01:26:19] you know some risk that the model takes
[01:26:20] over I think the main way to control
[01:26:22] that is to make sure that the
[01:26:23] capabilities of the model that we test
[01:26:25] are not such that they're capable of
[01:26:28] doing this at what point were the
[01:26:29] capabilities be so high where you're you
[01:26:31] say I don't even want to test this oh
[01:26:33] well there's different things I mean
[01:26:34] there's capability testing and you know
[01:26:36] but that itself could lead totally if
[01:26:37] you're attaching it and replicate that
[01:26:39] like what if it actually does sure but I
[01:26:41] I think I I mean I think what you want
[01:26:42] to do is you want to like extrapolate so
[01:26:45] we've talked with Arc about this right
[01:26:46] you know you have like factors of two of
[01:26:48] compute or something where you know
[01:26:50] you're like okay you know you know can
[01:26:52] can the model do something like you know
[01:26:54] open up an account on AWS and like make
[01:26:57] some money for itself like some of the
[01:26:58] things that are like obvious
[01:26:59] prerequisites to like complete survival
[01:27:02] in the wild
[01:27:03] um and so just set set those thresholds
[01:27:05] very well you know kind of very well
[01:27:07] below and then as you proceed upward
[01:27:10] from there do kind of more and more
[01:27:13] rigorous tests and be more and more
[01:27:14] careful about about what it is on uh
[01:27:18] Constitution Ai and feel free to explain
[01:27:20] what this is for the audience but who
[01:27:22] decides what the constitution for the
[01:27:25] next generation of models or potentially
[01:27:26] superhuman model is like how is that
[01:27:28] actually written I think initially you
[01:27:30] know to make the Constitution we just
[01:27:32] took some stuff that was like broadly
[01:27:34] agreed on like the UN Charter of you
[01:27:36] know U.N Declaration on human rights and
[01:27:39] um you know some of the stuff from
[01:27:40] Apple's terms of service right stuff
[01:27:41] that's like you know consensus unlike
[01:27:43] what's acceptable to say or like you
[01:27:46] know what what basic things are able to
[01:27:48] be included so one I think for future
[01:27:50] constitutions we're looking into like
[01:27:52] more participatory processes for making
[01:27:55] these
[01:27:56] um but I think beyond that I don't think
[01:27:57] there should be like one Constitution
[01:27:59] for like a model that everyone uses like
[01:28:02] probably models Constitution should be
[01:28:05] very very simple right it should only
[01:28:07] have very basic facts that everyone
[01:28:10] would agree on and then there should be
[01:28:11] a lot of ways that you can customize
[01:28:14] including a pending you know
[01:28:16] constitutions and and you know I think
[01:28:17] beyond that we're developing new methods
[01:28:19] right this is you know I'm not imagining
[01:28:21] that this or this alone is the method
[01:28:24] that we'll use to train superhuman AI
[01:28:26] right many of the parts of capability
[01:28:28] training may be different and so you
[01:28:30] know it could look very different and
[01:28:32] again I'd go there like they're levels
[01:28:34] above this like I'm pretty uncomfortable
[01:28:36] with like here's the ai's Constitution
[01:28:38] it's going to run the world like that
[01:28:40] you know again like just normal lessons
[01:28:44] from like how societies work and how
[01:28:46] politics works like that that just kind
[01:28:48] of yeah that that strikes me as fanciful
[01:28:51] like I you know I think I think we
[01:28:53] should try to hook these things into
[01:28:57] you know even even when they're very
[01:28:58] powerful again after we've mitigated the
[01:29:00] safety issues like any good future even
[01:29:04] even if it has all these security issues
[01:29:06] that we need to solve it somehow needs
[01:29:09] to end with with something that's that's
[01:29:11] that's more decentralized and you know
[01:29:13] less like a god-like super and you know
[01:29:16] I I just I just don't think that ends
[01:29:17] well uh what scientists from the
[01:29:19] Manhattan Project do you respect most in
[01:29:21] terms of the acted most ethically under
[01:29:23] the constraints they were given well is
[01:29:26] there one that comes to mind I don't
[01:29:27] don't know I mean I you know I think
[01:29:29] there's there's a lot of answers you
[01:29:30] could give I mean I'm definitely a fan
[01:29:32] of zillard for having kind of figured it
[01:29:34] figured it out he was then you know
[01:29:36] against the the against the the actual
[01:29:38] dropping of the bomb I don't actually
[01:29:40] know the history well enough to have an
[01:29:43] opinion on whether you know
[01:29:44] demonstration of the bomb could have
[01:29:45] could have ended the war I mean that
[01:29:47] involves a bunch of facts about Imperial
[01:29:49] Japan that are you know that are that
[01:29:51] are complicated and that I that I'm not
[01:29:53] an expert on
[01:29:54] um but you know zillard seemed to you
[01:29:56] know he he discovered this stuff early
[01:29:58] he kept it secret you know you know you
[01:30:02] know patented some of it and put it in
[01:30:03] the hands of the British admiralty
[01:30:06] um so you know he seemed to display
[01:30:08] the right kind of awareness as well as
[01:30:10] as well as uh as well as discovering
[01:30:13] stuff I mean it was when I read that
[01:30:14] book that I kind of you know when I
[01:30:16] wrote this Big Blob of compute Doc and
[01:30:18] many other you know I only showed it to
[01:30:20] a few people and there were other docs
[01:30:21] that I showed to almost no one uh so you
[01:30:24] know I yeah it was a bit a bit inspired
[01:30:26] by this again I mean I you know we could
[01:30:28] all get self-aggrandizing here like we
[01:30:30] don't know how it's gonna turn out or if
[01:30:32] it's actually gonna be actually gonna be
[01:30:34] something on par with the Manhattan
[01:30:35] Project I mean you know this this could
[01:30:37] all be just Silicon Valley people
[01:30:39] building technology and you know just
[01:30:41] kind of like having delusions of
[01:30:43] grandeur so I don't know how it's gonna
[01:30:45] turn out I mean if if the scaling stuff
[01:30:46] is true then it's more bigger than that
[01:30:48] right yeah yeah it certainly it
[01:30:50] certainly could be bigger I I just you
[01:30:52] know we should always kind of I don't
[01:30:54] know maintain this attitude that it's
[01:30:55] it's really easy to fool yourself if you
[01:30:57] were asked by the government if you're a
[01:30:58] physicist during World War II and you
[01:31:00] were asked by the government to
[01:31:01] contribute non-replaceable research to
[01:31:03] the Manhattan Project well what do you
[01:31:04] think you would have said yeah I mean I
[01:31:06] think giving you're in a war with the
[01:31:08] Nazis
[01:31:09] um at least During the period when you
[01:31:10] thought that the Nazis were I I don't
[01:31:12] yeah I don't really see much choice but
[01:31:15] uh but uh but to do it if it's possible
[01:31:17] you know you have to figure it's going
[01:31:19] to be done within within 10 years or so
[01:31:21] by someone regarding cyber security what
[01:31:24] should we make of the fact that there's
[01:31:25] a whole bunch of tech companies which
[01:31:27] have ordinary tech companies security
[01:31:29] policy
[01:31:30] that publicly seeming facing it's not
[01:31:33] obvious that they've been hacked like
[01:31:34] coinbase still has its Bitcoin
[01:31:37] um you know Google as far as I know my
[01:31:38] Gmail hasn't been leaked should we take
[01:31:41] from that that current status code tech
[01:31:44] companies security practices are good
[01:31:45] enough for AGI or just simply that
[01:31:47] nobody has tried hard enough it would be
[01:31:49] hard for me to speak to you know current
[01:31:51] tech company practices and of course
[01:31:52] there may be many attacks that we don't
[01:31:54] know about where things are stolen and
[01:31:56] then silently used you know I mean I
[01:31:59] think an indication of it is when
[01:32:00] someone really cares basically cares
[01:32:02] about attacking someone uh then then
[01:32:04] often the attacks happen so um you know
[01:32:07] recently we saw that some fairly High
[01:32:10] officials of the US government had their
[01:32:13] email accounts hacked via VIA Microsoft
[01:32:16] Microsoft was providing the email
[01:32:17] accounts
[01:32:18] um so you know presumably that that
[01:32:19] related to information that was you know
[01:32:21] of great interest to you know to foreign
[01:32:24] adversaries
[01:32:25] um and so it it sounds it seems to me at
[01:32:28] least you know that the evidence is more
[01:32:30] consistent with you know when something
[01:32:32] is really high enough value then uh you
[01:32:35] know then then you know someone acts and
[01:32:38] it's stolen and My worry is that if
[01:32:40] course with with AGI will get to a world
[01:32:42] where you know the value is seen as
[01:32:44] incredibly high right that you know
[01:32:46] it'll be like stealing nuclear missiles
[01:32:48] or something you can't be too careful on
[01:32:50] this stuff
[01:32:51] um and you know at every place that I've
[01:32:53] worked I push for the cyber security to
[01:32:55] be better one of my concerns about cyber
[01:32:58] security is you know it's not it's not
[01:32:59] kind of something you can trump it I
[01:33:01] think a good Dynamic with Safety
[01:33:03] Research is like come you know you can
[01:33:05] get companies into a dynamic and I think
[01:33:07] we have where you know you can get them
[01:33:10] to compete to do the best Safety
[01:33:11] Research and you know kind of use it as
[01:33:13] a I don't know like a like a recruiting
[01:33:16] point of competition or something we
[01:33:17] used to do this all the time with
[01:33:18] interpretability you know and and then
[01:33:20] sooner or later other other orgs started
[01:33:23] recognizing the defect and started
[01:33:25] working on interpretability whether or
[01:33:27] not you know that you know like whether
[01:33:28] or not that was a priority to them
[01:33:30] before but I think it's harder to do
[01:33:32] that with cyber security because a bunch
[01:33:34] of the stuff you have to do in quiet and
[01:33:36] so you know we did try to put out one
[01:33:37] post about it but I think you know most
[01:33:40] you just you just see the results
[01:33:42] um you know I think people should you
[01:33:45] know a good Norm would be you know
[01:33:46] people see the cyber security leaks from
[01:33:49] companies or you know leaks of the model
[01:33:50] parameters or something and say you know
[01:33:52] that they they screwed up that's that's
[01:33:54] that that's bad if I'm a safety person I
[01:33:56] might not want to work there
[01:33:58] um of course as soon as I as soon as I
[01:33:59] say that we'll probably have a security
[01:34:00] breach tomorrow but uh um you know but
[01:34:03] but that's that's that's part of the
[01:34:04] game here right that's I think that's
[01:34:05] part of um you know trying trying to
[01:34:07] make things safe I I want to go back to
[01:34:09] the thing we're talking about earlier
[01:34:10] where the ultimate level of cyber
[01:34:13] security required for two to three years
[01:34:15] from now and whether it requires a bunk
[01:34:17] like are you actually expecting to be in
[01:34:19] a physical bunker in two to three years
[01:34:20] or is that just a metaphor yeah I mean I
[01:34:22] think I think that's a metaphor
[01:34:24] um you know we're still figuring it out
[01:34:25] like something I would think about is
[01:34:27] like I think security of the data center
[01:34:30] which may not be in the same physical
[01:34:32] location as us but you know we've worked
[01:34:34] very hard to make sure it's in the
[01:34:35] United States but securing the physical
[01:34:37] data centers and the gpus I think some
[01:34:39] of the real really expensive attacks if
[01:34:42] someone was really determined just
[01:34:44] involved going into the data center and
[01:34:46] just you know trying to steal steal the
[01:34:48] data directly or as it's flowing from a
[01:34:50] data center to you know to to us I think
[01:34:53] these data centers are going to have to
[01:34:54] be built in a very special way I mean
[01:34:56] given the way things are scaling up you
[01:34:58] know probably anyway heading to a world
[01:35:00] where you know the you know networks of
[01:35:03] data centers you know cost as much as
[01:35:04] aircraft carriers or something
[01:35:07] um and and so you know they're already
[01:35:09] going to be pretty unusual objects but I
[01:35:10] think in addition to being unusual in
[01:35:12] terms of their ability
[01:35:13] you know to to link together and train
[01:35:16] gigantic gigantic models that are also
[01:35:18] going to have to be very secure speaking
[01:35:20] of which how you know there's been sorts
[01:35:22] of rumors on the difficulty of procuring
[01:35:24] the power and the gpus for the next
[01:35:26] generation of models what has the
[01:35:28] process been like to secure the the
[01:35:30] necessary components to do the Next
[01:35:32] Generation that's something I can't go
[01:35:34] into great detail about uh you know I I
[01:35:36] will say look like you know people think
[01:35:38] of even industrial scale data centers
[01:35:41] right people are not thinking at the
[01:35:43] scale that I think these models are
[01:35:44] going to go to very soon and so whenever
[01:35:46] you do something in a scale where it's
[01:35:48] never been done before you know every
[01:35:50] every single component every single
[01:35:52] thing has to be done in a new way than
[01:35:54] it was before and so you know you may
[01:35:56] you may you may run into problems with
[01:35:59] you know surprisingly simple components
[01:36:01] power is one that you mentioned and is
[01:36:03] this something that anthropic has to
[01:36:04] handle or can you just Outsource it you
[01:36:06] know I mean for data centers we work
[01:36:08] with Cloud providers for instance what
[01:36:10] should we make about the fact that these
[01:36:12] models require so much much training and
[01:36:15] the entire Corpus of internet data in
[01:36:17] order to be sub-human whereas you know
[01:36:20] if gpd4 there's been estimates that you
[01:36:23] know it was like a 10 to 25 flops or
[01:36:26] something where you know whereas you I
[01:36:29] mean you can take these numbers through
[01:36:30] grain of salt but there's reports that
[01:36:31] you know human brain from the time it is
[01:36:34] born to the time a human being is 20
[01:36:36] years old that's like on the order of 10
[01:36:38] to the 20 flops to simulate all those
[01:36:40] interactions you don't have to go to the
[01:36:42] particulars on those numbers but should
[01:36:43] we be worried about how sample
[01:36:45] inefficient these models seem to be yeah
[01:36:47] so I think that's one of the remaining
[01:36:48] Mysteries one way you could phrase it is
[01:36:51] that the models are
[01:36:53] maybe two to three orders of magnitude
[01:36:55] smaller than the human brain If you
[01:36:57] compare the number of synapses while at
[01:36:59] the same time being trained on you know
[01:37:01] three to four or more orders of
[01:37:03] magnitude of data if you compare to you
[01:37:06] know number of words human human sees as
[01:37:09] they're developing to age 18. it's I
[01:37:12] don't remember exactly but I think it's
[01:37:13] in the hundreds of millions whereas for
[01:37:15] the models we're talking about the
[01:37:16] hundreds of billions of the trillions so
[01:37:19] what what explains this there are these
[01:37:21] offsetting things where the models are
[01:37:23] smaller they need a lot more data
[01:37:26] and they're still below human level but
[01:37:28] so you know there's some way in which
[01:37:32] you know the analogy to the brain is not
[01:37:34] quite right or is breaking down or
[01:37:36] there's some there's some missing Factor
[01:37:38] you know this is just kind of like in
[01:37:39] physics where it's like you know we
[01:37:41] can't explain the Mickelson morally
[01:37:42] experiment or like I'm forgetting one of
[01:37:44] the other 19th century physics paradoxes
[01:37:47] but like I think it's one thing we don't
[01:37:48] quite understand right humans see so
[01:37:51] little data and they still do fine uh
[01:37:54] one theory on it it could be that it you
[01:37:57] know it's it's like our other modalities
[01:37:59] um you know how do we get you know 10 to
[01:38:01] the 14th bits into the human brain well
[01:38:03] well most of it is kind of these images
[01:38:05] and maybe a lot of what's going on
[01:38:07] inside the human brain is like you know
[01:38:08] our mental workspace involves all these
[01:38:11] these you know these these simulated
[01:38:13] images or something like that but
[01:38:15] honestly I think intellectually we have
[01:38:16] to admit that that's a weird thing that
[01:38:18] doesn't match up and you know it's one
[01:38:20] reason I'm a bit you know skeptical a
[01:38:22] kind of biological analogies I thought
[01:38:24] in terms of them like five or six years
[01:38:26] ago but now that we actually have these
[01:38:28] models in front of us as artifacts it
[01:38:30] feels like almost all the evidence from
[01:38:32] that has been screened off by what we've
[01:38:34] seen and what we've seen are models that
[01:38:36] are much smaller than the human brain
[01:38:38] and yet yet can do a lot of the things
[01:38:39] that humans can do and yet paradoxically
[01:38:42] require a lot more data so maybe we'll
[01:38:45] discover something that makes it all
[01:38:46] efficient or maybe we'll understand why
[01:38:49] the discrepancy is present but at the
[01:38:51] end of the day I don't think it matters
[01:38:52] right if we keep scaling the way we are
[01:38:54] I think what's more relevant at this
[01:38:56] point is just measuring the abilities of
[01:38:58] the model and seeing how far they are
[01:39:00] from humans and they don't seem terribly
[01:39:02] far to me does this scaling picture and
[01:39:04] the Big Blob of compute more generally
[01:39:06] does that underemphasize the role that
[01:39:09] algorithmic progress is played when you
[01:39:11] compose the um the the Big Blob of
[01:39:13] compute so you know you're talking about
[01:39:15] lstms presumably at that point
[01:39:16] presumably the scaling on that would not
[01:39:19] have you at Cloud 2 at this point so are
[01:39:21] you underemphasizing the world that uh
[01:39:24] an improvement of the scale of
[01:39:25] Transformer could be having here when
[01:39:27] you put it behind the label scaling this
[01:39:29] Big Blob of compute document which I
[01:39:31] still have not made public I probably
[01:39:32] should for like historical reasons I
[01:39:34] don't think it would tell anyone
[01:39:35] anything they don't know now but uh when
[01:39:37] I wrote it I actually said look there
[01:39:40] are seven factors that and you know I
[01:39:42] wasn't I wasn't like these are the
[01:39:44] factors but I was just like no it gives
[01:39:45] some sense of the kinds of things that
[01:39:46] matter and what don't and so I wasn't
[01:39:49] thinking like these are the you know
[01:39:50] there could be nine there could be five
[01:39:51] but like the things I said were I said
[01:39:54] number of parameters scale of the model
[01:39:57] like you know the compute and compute
[01:39:59] matters quantity of data matters quality
[01:40:03] of data matters loss function matters so
[01:40:06] like you know are you doing RL are you
[01:40:08] doing next word prediction if your loss
[01:40:10] function isn't rich or doesn't
[01:40:11] incentivize the right thing you won't
[01:40:13] you won't get anything
[01:40:15] um so those were the key four ones uh
[01:40:17] which I think are the core of the
[01:40:18] hypothesis but then I said three more
[01:40:20] things one was symmetries which is
[01:40:23] basically like if your architecture
[01:40:25] doesn't take into account the right
[01:40:27] kinds of symmetries it doesn't work
[01:40:30] um or it's it's very inefficient so so
[01:40:32] for example convolutional neural
[01:40:35] networks take into account translational
[01:40:36] symmetry lstms take into account time
[01:40:40] Symmetry and but a weakness of lstms is
[01:40:43] that they can't attend over the whole
[01:40:45] context so there's kind of this
[01:40:46] structural weakness like if a model
[01:40:48] isn't structurally capable of like
[01:40:51] absorbing and managing things that
[01:40:54] happened in a far enough distant past
[01:40:55] and it's just like it's kind of like you
[01:40:58] know like the compute doesn't flow like
[01:40:59] the spice doesn't flow it's like you you
[01:41:03] can't like like the The Blob has to be
[01:41:05] unencumbered right it kind of it's not
[01:41:07] it's not going to work if if you
[01:41:09] artificially close things off and I
[01:41:12] think rnns and lstms artificially close
[01:41:14] things off because they they close you
[01:41:16] off to the distant past
[01:41:18] um and so again things need to flow
[01:41:20] freely if they don't it doesn't work and
[01:41:22] then you know I I added a couple things
[01:41:24] one of them was like conditioning which
[01:41:27] is like you know if you're if the thing
[01:41:29] you're optimizing with is just really
[01:41:30] numerically bad like you're gonna have
[01:41:32] trouble and so this is why like Adam
[01:41:34] works better than you know than normal
[01:41:36] sdd and I I think I'm forgetting what
[01:41:38] the seventh condition was but it was it
[01:41:40] was similar to things like this where
[01:41:42] it's like you know if you if you if you
[01:41:45] set things up in kind of a way that's
[01:41:46] that's set up to fail or that doesn't
[01:41:49] allow the compute to work in an
[01:41:50] uninhibited way then it won't work and
[01:41:52] so Transformers were kind of within that
[01:41:54] even though I can't remember if the
[01:41:57] Transformer paper had been published it
[01:41:58] was around the same time as I wrote that
[01:42:00] document it might have been just before
[01:42:01] it might have been just after it sounds
[01:42:04] like from that view that the the way to
[01:42:07] think about these algorithmic progresses
[01:42:09] is not as increasing the power of The
[01:42:11] Blob of compute but simply getting rid
[01:42:13] of the artificial hindrances that older
[01:42:16] architectures have is that is that's a
[01:42:18] little that yeah that's that's a little
[01:42:19] how I think about it you know again if
[01:42:21] you go back to like Ilias like the
[01:42:23] models want to learn yeah yeah like like
[01:42:25] the compute wants to be free yeah yeah
[01:42:27] and like you know it's being blocked in
[01:42:29] various ways where you like don't
[01:42:30] understand that it's being blocked and
[01:42:31] so you need to like free it up right
[01:42:33] right I I love the the radiance to
[01:42:36] change that to spice okay
[01:42:38] um on that point though so do you think
[01:42:41] that another thing on the scale of a
[01:42:43] transformer is coming down the pike to
[01:42:47] enable the next the next great
[01:42:48] iterations I think it's possible I mean
[01:42:51] people have worked on things like you
[01:42:52] know trying to model
[01:42:54] very long time dependencies or you know
[01:42:57] you know there's various different ideas
[01:42:59] where I could see that we're kind of
[01:43:01] missing an efficient way of representing
[01:43:03] or dealing with something so I think
[01:43:06] those inventions are possible I guess my
[01:43:08] perspective would be even if they don't
[01:43:10] happen we're all we're already on this
[01:43:12] very very steep trajectory and so I'm
[01:43:15] less I mean we're constantly trying to
[01:43:18] discover them as our as our others um
[01:43:20] but things are already on such a fast
[01:43:21] trajectory all that would do is speed up
[01:43:23] the trajectory even more
[01:43:25] um and probably probably not by that
[01:43:26] much because it's already going so fast
[01:43:28] is something embodied or having an
[01:43:30] embodied version of a model is that at
[01:43:33] all important in terms of getting either
[01:43:34] data or progress I think of that Less in
[01:43:37] terms of the you know like a new
[01:43:39] architecture and More in terms of like a
[01:43:41] loss function like the the data the
[01:43:43] environment you're exposing yourself to
[01:43:45] end up being very different and and so I
[01:43:47] think that could be important for
[01:43:49] learning some skills although
[01:43:51] data acquisition is hard and so things
[01:43:54] have gone through the language route and
[01:43:55] I would guess well
[01:43:57] continue to go through the language
[01:43:58] route even as you know even as as more
[01:44:01] as possible in terms of embodiment and
[01:44:03] then the other possibilities you
[01:44:04] mentioned RL you can see it as yeah I
[01:44:07] mean we we kind of already do RL with
[01:44:08] our OHF right people are like this is an
[01:44:10] alignment is the capabilities I always
[01:44:12] think in terms of the two snakes right
[01:44:13] they're they're kind of often hard to
[01:44:15] distinguish so we already kind of use RL
[01:44:18] in these language models but I think
[01:44:19] we've used RL Less in terms of getting
[01:44:22] them to take actions and you know do
[01:44:23] things in the world but you know when
[01:44:26] you take actions over a long period of
[01:44:28] time and understand the consequences of
[01:44:29] those actions only later than you know
[01:44:32] RL is a typical tool we have for that so
[01:44:34] I would guess that in terms of models
[01:44:36] taking action in the world that RL will
[01:44:39] you know will become a thing with all
[01:44:41] the power and all the safety issues that
[01:44:43] come with it when you project out in the
[01:44:44] future do you see the way in which these
[01:44:46] things will be integrated into
[01:44:48] productive uh Supply chains do you see
[01:44:51] them talking with each other and
[01:44:53] criticizing each other and contributing
[01:44:54] to each other's output or is it just the
[01:44:57] model one shots the one model one shots
[01:44:59] the the answer or the work models will
[01:45:03] undertake extended tasks that will have
[01:45:06] to be the case I mean we may want to
[01:45:07] limit that to some extent because it may
[01:45:09] make some of the safety problems easier
[01:45:11] um but you know some of that I think
[01:45:13] will be required in terms of our models
[01:45:15] talking to models or are they talking to
[01:45:17] humans again this goes kind of out of
[01:45:20] the technical realm and into the like
[01:45:23] socio-cultural economic realm where my
[01:45:26] heuristic is always that it's very very
[01:45:29] difficult to predict things
[01:45:31] um and so I I feel like these scaling
[01:45:33] laws have been very predictable but then
[01:45:35] when you say like well you know when
[01:45:37] when is there going to be a commercial
[01:45:38] explosion in these models or what's the
[01:45:41] form it's going to be or are the models
[01:45:42] going to do things instead of humans or
[01:45:44] pairing with humans I feel like
[01:45:46] certainly my track record on predicting
[01:45:48] these things is terrible uh but I also
[01:45:51] looking around I don't really see anyone
[01:45:53] who's track record is great you
[01:45:54] mentioned how fast progress is happening
[01:45:56] but also the difficulties of integrating
[01:45:59] within the existing economy into the way
[01:46:02] things work do you think there will be
[01:46:04] enough time to actually have large
[01:46:06] revenues from AI products before the
[01:46:09] next model is just so much better or
[01:46:10] we're in like a different landscape
[01:46:12] entirely it depends what you mean by by
[01:46:14] large right you know I think multiple
[01:46:16] companies are already in the you know
[01:46:17] 100 million to billion per year range
[01:46:20] will it get to the 100 billion or
[01:46:22] trillion range you know before I that
[01:46:26] stuff is just so hard to predict right
[01:46:28] it's and it's it's it's not even super
[01:46:30] well defined like you know I think right
[01:46:33] now there are companies that are
[01:46:34] throwing a lot of money at at generative
[01:46:36] AI you know as as customers but and and
[01:46:39] they'll you know I think I think that's
[01:46:40] the right thing for them to do and
[01:46:42] they'll you know they'll find uses for
[01:46:44] it but it doesn't mean there doesn't
[01:46:45] mean it's you know they're finding uses
[01:46:47] or the best uses from day one so even
[01:46:50] money Changing Hands is not is not quite
[01:46:52] the same thing as economic value being
[01:46:54] created but surely you've thought about
[01:46:55] this from the perspective of anthropic
[01:46:57] wherever these things are happening so
[01:46:58] fast then it should be an insane
[01:47:00] valuation right even us who have you
[01:47:03] know not been super focused on
[01:47:04] commercialization and more on safety I
[01:47:06] mean you know the graph goes up
[01:47:08] um and it goes up it goes up relatively
[01:47:10] quickly yeah um so you know I can I can
[01:47:12] only imagine what's happening at you
[01:47:14] know the origin or you know that this is
[01:47:16] this is this is their singular Focus
[01:47:20] um so it's certainly happening fast but
[01:47:22] you know again it's it's like it's the
[01:47:24] exponential from the small base while
[01:47:26] the technology itself is moving fast so
[01:47:28] it's it's kind of a race between how
[01:47:31] fast the technology is getting better
[01:47:32] and how fast it's integrated into the
[01:47:34] economy and that I think that's just a
[01:47:36] very unstable and turbulent
[01:47:38] process both things are going to happen
[01:47:39] fast but if you ask me exactly how it's
[01:47:42] going to play out exactly what order
[01:47:44] things are going to happen I I I I don't
[01:47:47] know and I'm just kind of skeptical of
[01:47:49] the ability to predict I'm kind of
[01:47:51] curious with regards to anthropic
[01:47:52] specifically yeah your public benefit
[01:47:54] Corporation yes and rightfully so you
[01:47:57] want to make sure that this is an
[01:47:59] important technology the obviously the
[01:48:00] only thing you want to care about is not
[01:48:01] sure about their value but how do you
[01:48:04] talk to investors who are putting in
[01:48:06] like hundreds of millions billions of
[01:48:07] dollars of money like how do you talk to
[01:48:10] them about the fact that how do you get
[01:48:11] them to put in this amount of money
[01:48:12] without yes the shareholder value being
[01:48:15] the main concern so so I think the ltbt
[01:48:17] is is you know the right thing on this
[01:48:19] right you know I mean we're gonna talk
[01:48:21] more about the ltbt but like some
[01:48:23] version of that has been in development
[01:48:24] since the beginning of of anthropic even
[01:48:27] even formally right and so you know from
[01:48:30] from the beginning you know even as the
[01:48:32] body has has changed in some ways it's
[01:48:34] like from the beginning it was like this
[01:48:36] body is going to exist and it's you know
[01:48:37] it's on you like every traditional
[01:48:40] investor who invests in anthropic you
[01:48:42] know has to you know looks at this some
[01:48:45] of them are just like whatever you run
[01:48:47] your company how you want some of them
[01:48:49] are like you know oh my God like this
[01:48:51] this you know this body of random people
[01:48:53] or to them random people could like you
[01:48:55] know could could move anthropic in a
[01:48:57] Direction that's you know that's totally
[01:48:58] contrary to our and now there are there
[01:49:00] are legal limits on that of course but
[01:49:02] you know we have to have this
[01:49:04] conversation with every investor and
[01:49:05] then it gets into a conversation of well
[01:49:07] what are the kinds of things that you
[01:49:09] know that we would we we might do that
[01:49:12] would be contrary to the to the you know
[01:49:14] to the interests of of traditional
[01:49:15] investors and just have having those
[01:49:18] conversations has helped get everyone on
[01:49:19] the same page I want to talk about the
[01:49:21] the physics and the fact that so many of
[01:49:24] the founders and the employees at uh
[01:49:26] anthropic are physicist what is the I
[01:49:29] mean we talked in the beginning about
[01:49:30] the scaling laws and how the power laws
[01:49:32] and physics are something you see here
[01:49:34] but you know what are the actual like
[01:49:36] approaches and ways of thinking from
[01:49:38] physics that seem to have carried over
[01:49:40] so well is that notion of effective
[01:49:41] theory is super useful you know what is
[01:49:43] going on here I I mean I think part of
[01:49:45] it is just physicists learn things
[01:49:46] really fast we have generally found that
[01:49:49] uh you know if we hire you know someone
[01:49:51] who is a you know physics PhD or
[01:49:53] something that they can they can learn
[01:49:55] ML and contribute just very very quickly
[01:49:57] in in most cases and you know because
[01:49:59] several of our Founders myself Jared
[01:50:01] Kaplan uh Sam Sam McCandless
[01:50:04] we're physicists we knew a lot of other
[01:50:05] physicists and so we were able to hire
[01:50:07] them and now there's I don't know how
[01:50:09] many is exactly you know might be 30 or
[01:50:11] 40 of them here ml is not still not yet
[01:50:14] a field that has an enormous amount of
[01:50:16] depth and so they've been able to get up
[01:50:18] to speed very quickly are you concerned
[01:50:20] that there's like a lot of people who
[01:50:21] would have been doing physics or
[01:50:23] something whatever they could go into
[01:50:25] Finance instead and since anthropic
[01:50:28] exists they have now been recruited to
[01:50:30] go into Ai and you know they're you
[01:50:34] obviously care about AI safety but you
[01:50:36] know maybe in the future they leave and
[01:50:38] they get funded to do their own thing is
[01:50:40] that a concern that you're bringing more
[01:50:41] people into the ecosystem here yeah I
[01:50:43] mean you know I think there's there's
[01:50:44] like a broad set of action you know like
[01:50:46] we're causing gpus to exist you know
[01:50:48] there's there's a lot of kind of side
[01:50:50] effects that you can't that that you
[01:50:52] can't currently control or that you just
[01:50:53] incur if you buy into the idea that you
[01:50:55] need to build Frontier models and that's
[01:50:58] one of them a lot of them would have
[01:50:59] happened anyway I mean Finance was a hot
[01:51:01] thing 20 years ago so physicists were
[01:51:03] doing it now ml is a hot thing thing and
[01:51:04] you know it's not like we've caused them
[01:51:06] to do it when they had no interest
[01:51:08] previously but you know again you know
[01:51:10] at the margin you're kind of you're kind
[01:51:13] of bidding things up
[01:51:14] um and you know a lot of that would have
[01:51:16] happened anyway some of it some of it
[01:51:17] wouldn't but it's all part of the
[01:51:18] calculus do you think that cloud has
[01:51:20] conscious experience How likely do you
[01:51:22] think that is this is another of these
[01:51:23] questions that just seems very unsettled
[01:51:25] and uncertain uh one thing I'll tell you
[01:51:27] is I used to think that we didn't have
[01:51:30] to worry about this at all until models
[01:51:31] were kind of like operating in Rich
[01:51:33] environments like not necessarily
[01:51:34] embodied but like that you know they you
[01:51:37] know they needed to like have a reward
[01:51:39] function and like have kind of
[01:51:41] long-lived experience so I still think
[01:51:43] that might be the case but the more
[01:51:45] we've looked at kind of these language
[01:51:47] models and particularly looked inside
[01:51:48] them to see things like induction heads
[01:51:51] a lot of the cognitive Machinery that
[01:51:53] you would need for active agents seems
[01:51:56] kind of already present in the base
[01:51:57] language models so I'm not quite as sure
[01:52:00] as I was before that were missing the
[01:52:03] things that you know that we're missing
[01:52:05] enough of the things that you would need
[01:52:06] I think today's models just probably
[01:52:08] aren't smart enough that we should worry
[01:52:11] about this too much but I'm not 100 sure
[01:52:14] about this and I do think the models
[01:52:16] will get in a year or two like this
[01:52:17] might be a very real concern what would
[01:52:20] change if you found out that they are
[01:52:21] conscious are you worried that you're
[01:52:23] like pushing the negative gradient to
[01:52:24] suffering like what is conscious is
[01:52:26] again one of these words that I I
[01:52:28] suspect it will like not end up having a
[01:52:30] a well-defined but it's like something
[01:52:32] to be but that yeah but but that yeah
[01:52:34] well I I I suspect that's that's a
[01:52:36] spectrum right uh so I don't know if we
[01:52:39] if we if we discover like that you know
[01:52:41] that I should care about let's say we
[01:52:43] discover that I should care about
[01:52:44] collage experience as much as I should
[01:52:46] care about like a dog or a monkey or
[01:52:48] something yeah I I would be I would be
[01:52:50] kind of kind of worried right I don't
[01:52:52] know if their experience is positive or
[01:52:54] negative unsettlingly I also don't know
[01:52:56] like I wouldn't know if any intervention
[01:53:00] that we made was more likely to make
[01:53:02] Claude you know have a positive versus
[01:53:04] negative experience versus not having
[01:53:06] one if there's an area that is helpful
[01:53:08] with this it's maybe mechanistic
[01:53:09] interpretability because I think if it
[01:53:11] is neuroscience for models and so it's
[01:53:13] possible that we could we could shed
[01:53:15] some shed some light on this although
[01:53:17] you know it's not it's not a
[01:53:19] straightforward factual question right
[01:53:21] it kind of depends what we mean and what
[01:53:23] we value we talked about this initially
[01:53:25] but I I want to get more specific we
[01:53:26] talked initially about you know now that
[01:53:28] you're seeing these capabilities ramp up
[01:53:30] within the human Spectrum you think that
[01:53:33] the human spectrum is wider than we
[01:53:35] thought but yeah more specifically what
[01:53:37] have you how is the way you think about
[01:53:39] human intelligence different now that
[01:53:41] the way you're seeing these these
[01:53:43] marginally useful abilities emerge how
[01:53:45] does that change your picture of what
[01:53:47] intelligence is I think for me the big
[01:53:49] realization on what intelligence is came
[01:53:52] with the like blob of compute thing
[01:53:53] right like it's not you know there might
[01:53:55] be all these separate modules there
[01:53:57] might be all this complexity
[01:53:59] um you know it's It's You Know Rich
[01:54:00] Sutton called it the bitter lesson right
[01:54:02] it's almost called has many names it's
[01:54:04] been called the scalene hypothesis like
[01:54:06] the first few people who figured it out
[01:54:07] was around 2017 or I mean you could go
[01:54:10] further back to I think I think Shane
[01:54:11] Lake was maybe the first person who
[01:54:14] really knew it maybe Ray cartswell
[01:54:16] although in a very vague way
[01:54:18] um but you know I think the num the
[01:54:19] number of people who understood it went
[01:54:21] up a lot around 2014 to 20 2017. but I
[01:54:26] think I think that was the big the big
[01:54:27] realization it's like you know well how
[01:54:29] did Intelligence evolve well if you
[01:54:32] don't need very specific conditions to
[01:54:33] create it if you can create it just from
[01:54:36] like
[01:54:37] the right kind of the right kind of
[01:54:39] gradient and loss signal then of course
[01:54:40] it's not so mysterious how it all
[01:54:42] happened in terms you know it had this
[01:54:44] click of scientific understanding in
[01:54:47] terms of like watching what the models
[01:54:49] can do how has it changed my view of
[01:54:51] human intelligence I wish I had
[01:54:53] something more intelligent to say on
[01:54:55] that uh I I feel like I don't know one
[01:54:58] thing that's been surprising is like I
[01:55:01] thought things might click into place a
[01:55:03] little more than they do like you know I
[01:55:05] thought like different cognitive
[01:55:07] abilities might all be connected and
[01:55:09] there was more of one secret behind them
[01:55:11] but it's like the model just learns
[01:55:14] various things at different times you
[01:55:15] know it can be like very good at coding
[01:55:17] but like you know it can't it can't
[01:55:19] quite you know approve the prime number
[01:55:20] theorem yet and I don't I mean I guess
[01:55:22] it's a little bit the same for for
[01:55:24] humans although it's it's weird the
[01:55:26] juxtaposition of things it can do and
[01:55:28] not I guess the main lesson is like
[01:55:30] having Theories of Intelligence or how
[01:55:33] intelligence works like
[01:55:35] again a lot of these words just just
[01:55:37] kind of like dissolve into a Continuum
[01:55:39] right they just kind of like
[01:55:42] dematerialize I think less in terms of
[01:55:44] intelligence and More in terms of what
[01:55:46] we see in front of us yeah now it's
[01:55:47] really surprising to me uh two things
[01:55:49] one is how discrete these like different
[01:55:52] Paths of intelligent um uh things that
[01:55:55] contribute to loss are rather than just
[01:55:56] being like one reasoning circuit or one
[01:55:58] general intelligence and the other thing
[01:56:00] talking with you that is surprising or
[01:56:02] interesting is
[01:56:03] many years from now it'll be one of
[01:56:05] those things that looking back it'll be
[01:56:07] why did why weren't why wasn't this
[01:56:09] obvious to you if you're seeing these
[01:56:10] smooth scaling curves why the time where
[01:56:12] you're not completely convinced
[01:56:14] so you've been less public than the CEOs
[01:56:17] of other AI companies you know you're
[01:56:19] not posting on Twitter you're not doing
[01:56:21] a lot of podcasts except for this one
[01:56:24] what what what gives like why are you
[01:56:26] why are you off the radar yeah I I
[01:56:28] aspire to this and I'm proud of this um
[01:56:31] if people think of me as kind of like
[01:56:32] boring and low profile like this is
[01:56:34] actually kind of what I want
[01:56:36] um so I don't know I've I've Just Seen A
[01:56:38] number of cases a number of people I've
[01:56:40] worked with
[01:56:41] um that I think you could say Twitter
[01:56:43] although I think I mean a broader thing
[01:56:45] like just kind of like attaching your
[01:56:47] incentives very strongly to like the
[01:56:50] approval or cheering of a crowd
[01:56:52] um I I think that can destroy your mind
[01:56:54] and in some cases it can destroy your
[01:56:55] soul and so I think I've kind of
[01:56:58] deliberately tried to be a little bit
[01:57:00] low profile because I wanna I don't know
[01:57:03] kind of like defend my ability to think
[01:57:05] about things intellectually in in a way
[01:57:08] that's different from other people and
[01:57:10] isn't isn't kind of tinged by the
[01:57:13] approval of other people so so you know
[01:57:15] I've seen cases of folks who are deep
[01:57:17] learning Skeptics and they become known
[01:57:19] as deep learning Skeptics on Twitter and
[01:57:21] then even as it starts to become clear
[01:57:23] to me they've kind of sort of changed
[01:57:25] their mind they like this is their thing
[01:57:27] on Twitter and they can't change their
[01:57:28] Twitter Persona and so forth and so on I
[01:57:31] don't really like the trend of kind of
[01:57:32] like personalizing companies like the
[01:57:35] whole you know like cage match between
[01:57:37] CEOs approach like I think it it
[01:57:40] distracts people from the actual merits
[01:57:42] and concerns of like the the you know
[01:57:45] the the company in question like I I
[01:57:47] kind of want people to like judge the
[01:57:50] like nameless bureaucratic institution
[01:57:52] um you know I I want people to think in
[01:57:55] terms of the nameless bureaucratic
[01:57:57] institution and its incentives more than
[01:57:59] they think in terms of me everyone wants
[01:58:01] a friendly face but but actually I think
[01:58:02] friendly faces can be misleading okay
[01:58:04] well in this case this will be a
[01:58:05] misleading interview because this has
[01:58:07] been a lot of fun maybe like a glass to
[01:58:09] talk to indeed yeah this isn't a blast
[01:58:12] I'm super glad you came on the podcast
[01:58:13] and uh hope people enjoy it thanks
[01:58:15] thanks for having me
[01:58:17] hey everybody I hope you enjoyed that
[01:58:19] episode
[01:58:20] as always the most helpful thing you can
[01:58:22] do is just share the podcast send it to
[01:58:25] people you think might enjoy it put it
[01:58:26] in Twitter your group chats Etc just
[01:58:28] splits the world
[01:58:30] appreciate your listening I'll see you
[01:58:32] next time cheers
