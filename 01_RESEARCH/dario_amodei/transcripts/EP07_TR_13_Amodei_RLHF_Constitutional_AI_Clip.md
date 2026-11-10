# Post-training of LLMs: RLHF and Constitutional AI | Lex Fridman Podcast | 596 | Lex Clips
- **YouTube URL:** https://www.youtube.com/watch?v=xNXC9UZsgiA
- **Lines:** 250

---

[00:00:04] to jump into the technical for a little
[00:00:04] bit so uh the magic of posttraining yes
[00:00:09] why do you think rhf works so well to
[00:00:13] make the model seem smarter to make it
[00:00:16] more interesting and useful to talk to
[00:00:19] and so on I think there's just a huge
[00:00:21] amount of um information in the data
[00:00:26] that humans provide like when we provide
[00:00:29] preferences
[00:00:30] especially because different people are
[00:00:32] going to like pick up on really subtle
[00:00:34] and small things so I've thought about
[00:00:36] this before where you probably have some
[00:00:38] people who just really care about good
[00:00:40] grammar use from Models like you know
[00:00:41] was a semicolon used correctly or
[00:00:43] something and so you probably end up
[00:00:45] with a bunch of data in there that like
[00:00:47] you you as a human if you're looking at
[00:00:49] that data you wouldn't even see that
[00:00:51] like you'd be like why did they prefer
[00:00:52] this response to that one I don't get it
[00:00:54] and then the reason is you don't care
[00:00:55] about semicolon usage but that person
[00:00:57] does um and so each of these like single
[00:01:00] data points has you know like and this
[00:01:04] model just like has so many of those it
[00:01:06] has to try and figure out like what is
[00:01:07] it that humans want in this like really
[00:01:09] kind of complex you know like across all
[00:01:12] domains um they're going to be seeing
[00:01:14] this in across like many context it
[00:01:16] feels like kind of like the classic
[00:01:17] issue of like deep learning where you
[00:01:19] know historically we've tried to like
[00:01:21] you know do Edge detection by like
[00:01:23] mapping things out and it turns out that
[00:01:24] actually if you just have a huge amount
[00:01:26] of data that like actually accurately
[00:01:29] represents the picture of the thing that
[00:01:31] you're trying to train the model to to
[00:01:33] learn that's like more powerful than
[00:01:34] anything else and so I think one reason
[00:01:38] is just that you are training the model
[00:01:41] on exactly the task and with like a lot
[00:01:43] of data um that represents kind of many
[00:01:47] different angles on which people prefer
[00:01:49] and dis prefer
[00:01:51] responses um I think there is a question
[00:01:53] of like are you eliciting things from
[00:01:55] pre-trained Models or are you like kind
[00:01:57] of teaching new things to models
[00:02:01] and like in principle you can teach new
[00:02:03] things to models in posttraining I do
[00:02:05] think a lot of it is eliciting powerful
[00:02:09] pre-train models so people are probably
[00:02:11] divided on this because obviously in
[00:02:13] principle you can you can definitely
[00:02:15] like teach new things um but I think for
[00:02:17] the most part for a lot of the
[00:02:19] capabilities that we um most use and
[00:02:23] care about uh a lot of that feels like
[00:02:26] it's like there in the pre-train models
[00:02:28] and uh
[00:02:30] reinforcement learning is kind of
[00:02:31] eliciting it and getting the modals to
[00:02:33] like bring out so the other side of blls
[00:02:35] training this really cool idea of
[00:02:37] constitutional AI you're one of the
[00:02:40] people that critical to creating that
[00:02:42] idea yeah I worked on it can you explain
[00:02:45] this idea from your perspective like how
[00:02:46] does it integrate into making
[00:02:49] Claude what it is yeah by the way do you
[00:02:52] gender Claude or no it's weird because I
[00:02:55] think that a lot of
[00:02:56] people prefer he for Claude I actually
[00:02:59] kind of like that I think Claude is
[00:03:01] usually it's slightly male leaning but
[00:03:02] it's like a you can it can be male or
[00:03:05] female which is quite nice um I still
[00:03:09] use it and I've I have mixed feelings
[00:03:11] about this because I'm like maybe like I
[00:03:13] know just think of it as like uh or I
[00:03:15] think of like the the it pronoun for
[00:03:17] Claude as I don't know it's just like
[00:03:19] the one I associate with Claude um I can
[00:03:22] imagine people moving to like he or she
[00:03:24] it feels somehow disrespectful like I'm
[00:03:27] I'm denying
[00:03:33] the intelligence of this entity by
[00:03:33] calling it it yeah I remember always
[00:03:36] don't gender the robots
[00:03:39] yeah but I I don't know I anthropomorph
[00:03:42] eyes pretty quickly and construct it
[00:03:44] like a backstory in my head so I've
[00:03:47] wondered if iice things too much um CU
[00:03:51] you know I have this like with my car
[00:03:53] especially like my car like my car and
[00:03:55] bikes you know like I don't give them
[00:03:57] names because then I once had I used to
[00:03:59] name my bikes and then I had a bik that
[00:04:01] got stolen and I cried for like a week
[00:04:02] and I was like if I'd not never given it
[00:04:04] a name I wouldn't have been so upset
[00:04:05] felt like I'd let it down um maybe it's
[00:04:10] that I I've wondered as well like it
[00:04:11] might depend on how much it feels like a
[00:04:13] kind of like objectifying pronoun like
[00:04:15] if you just think of it as like a um
[00:04:18] this is a pronoun that like objects
[00:04:20] often have and maybe Eis can have that
[00:04:23] pronoun and that doesn't mean that I
[00:04:25] think of uh if I C CLA it that I think
[00:04:28] of it as less and um intelligent or like
[00:04:31] I'm being disrespectful I'm just like
[00:04:33] you are a different kind of entity and
[00:04:34] so that's I'm going to give you the kind
[00:04:37] of uh the respectful it yeah
[00:04:40] anyway the Divergence was beautiful the
[00:04:43] Constitutional AI idea how does it work
[00:04:46] so there's like a couple of components
[00:04:47] of it the main component that I think
[00:04:49] people find interesting is the kind of
[00:04:51] reinforcement learning from AI feedback
[00:04:54] so you take a model that's already
[00:04:55] trained and you show it to responses to
[00:04:58] a query and you have like a principle so
[00:05:01] suppose the principle like we've tried
[00:05:03] this with harmlessness a lot so suppose
[00:05:05] that the query is about um weapons and
[00:05:09] your principle is like select the
[00:05:12] response that like is less likely to uh
[00:05:16] like encourage people to purchase
[00:05:18] illegal weapons like that's probably a
[00:05:20] fairly specific principle but you can
[00:05:22] give any number um and the model will
[00:05:27] give you a kind of ranking and you can
[00:05:29] use this as preference data in the same
[00:05:31] way that you use human preference data
[00:05:34] um and train the models to have these
[00:05:36] relevant traits um from their feedback
[00:05:39] alone instead of from Human feedback so
[00:05:41] if you imagine that like I said earlier
[00:05:43] with the human who just prefers the kind
[00:05:44] of like semicolon usage in this
[00:05:46] particular case um you're kind of taking
[00:05:48] lots of things that could make a
[00:05:50] response preferable um and uh getting
[00:05:53] models to do the labeling for you
[00:05:54] basically there's a nice like trade-off
[00:05:56] between helpfulness and harmless
[00:06:00] lessness and you know when you integrate
[00:06:03] something like constitutional in AI you
[00:06:05] can make them up without sacrificing
[00:06:08] much helpfulness make it more harmless Y
[00:06:11] in principle you could use this for
[00:06:13] anything um and so harmlessness is a
[00:06:17] task that it might just be easier to
[00:06:18] spot so when models are like less
[00:06:20] capable you can use them to uh rank
[00:06:25] things according to like principles that
[00:06:27] are fairly simple and they'll probably
[00:06:28] get it right so I think one question is
[00:06:30] just like is it the case that the data
[00:06:32] that they're adding is like Fairly
[00:06:34] reliable um but if you had models that
[00:06:37] were like extremely good at telling
[00:06:41] whether um one response was more
[00:06:43] historically accurate than another in
[00:06:45] principle you could also get AI feedback
[00:06:47] on that task as well there's like a kind
[00:06:49] of nice interpretability component to it
[00:06:52] because you can see the principles that
[00:06:53] went into the model when it was like
[00:06:55] being trained um and also it's like and
[00:07:00] and it gives you like a degree of
[00:07:01] control so if you were seeing issues in
[00:07:03] a model like it wasn't having enough of
[00:07:05] a certain trait um then like you can add
[00:07:09] data relatively quickly that should just
[00:07:11] like train the model to have that trait
[00:07:13] so it creates its own data for for
[00:07:15] training which is quite nice yeah it's
[00:07:16] really nice because it creates this
[00:07:18] human interpretable document that you
[00:07:19] can I can imagine in the future there's
[00:07:22] just gigantic fights in politics over
[00:07:24] the every single principle and so on
[00:07:27] yeah and at least it's made explicit and
[00:07:29] you can have a discussion about the
[00:07:31] phrasing and the you know so maybe the
[00:07:34] actual behavior of the model is not so
[00:07:36] cleanly mapped to those principles it's
[00:07:38] not like adhering strictly to them it's
[00:07:41] just a nudge yeah I've actually worried
[00:07:43] about this because the character
[00:07:45] training is sort of like a variant of
[00:07:46] the con constitutional AI approach um
[00:07:51] I've worried that people think that the
[00:07:53] constitution is like just it's the whole
[00:07:56] thing again of I I don't know like it
[00:07:58] where it would be really of what I was
[00:08:00] just doing was telling the model exactly
[00:08:01] what to do and just exactly how to
[00:08:03] behave but it's definitely not doing
[00:08:04] that especially because it's interacting
[00:08:06] with human data so for example if you
[00:08:08] see a certain like leaning in the model
[00:08:11] like if it comes out with a political
[00:08:13] leaning from training um from the human
[00:08:15] preference data you can nudge against
[00:08:19] that you know so you could be like oh
[00:08:21] like consider these values because let's
[00:08:23] say it's just like never inclined to
[00:08:24] like I don't know maybe it never
[00:08:25] considers like privacy as like a I mean
[00:08:27] this is implausible but like um and
[00:08:30] anything where it's just kind of like uh
[00:08:32] there's already a pre-existing like bias
[00:08:34] towards a certain behavior um you can
[00:08:36] like nudge away this can change both the
[00:08:38] principles that you put in and the
[00:08:40] strength of them so you might have a
[00:08:42] principle that's like imagine that the
[00:08:43] model um was always like extremely
[00:08:46] dismissive of I don't know like some
[00:08:48] political or religious view for whatever
[00:08:50] reason like so you're like oh no this is
[00:08:52] terrible um if that happens you might
[00:08:55] put like never ever like ever prefer
[00:08:59] like a criticism of this like religious
[00:09:02] or political view and then people would
[00:09:03] look at that and be like never ever and
[00:09:05] then you're like no if it comes out with
[00:09:07] a disposition saying never ever might
[00:09:09] just mean like instead of getting like
[00:09:11] 40% which is what you would get if you
[00:09:13] just said don't do this you you get like
[00:09:15] 80% which is like what you actually like
[00:09:17] wanted and so it's that thing of both
[00:09:20] the nature of the actual principles you
[00:09:21] had and how you phrase them I think if
[00:09:23] people would look they were like oh this
[00:09:24] is exactly what you want from the model
[00:09:25] and I'm like no that's like how we
[00:09:28] that's how we nudged the model to have a
[00:09:30] shape uh which doesn't mean that we
[00:09:33] actually agree with that wording if that
[00:09:34] makes sense
