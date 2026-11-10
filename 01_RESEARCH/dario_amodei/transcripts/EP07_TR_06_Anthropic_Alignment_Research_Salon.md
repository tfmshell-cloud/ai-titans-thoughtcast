# Anthropic Official: How Difficult Is AI Alignment? (Research Salon with Dario Amodei)
- **YouTube URL:** https://www.youtube.com/watch?v=IPmt8b-qLgk
- **Lines:** 798

---

[00:00:03] we are super excited to have everyone
[00:00:03] here um folks that uh we've met already
[00:00:06] folks that are new this panel is just
[00:00:09] going to be really uh casual and we have
[00:00:13] researchers from four different teams at
[00:00:17] anthropic we have folks from societal
[00:00:19] impacts that's me folks from alignment
[00:00:21] science that's Yan alignment fine tuning
[00:00:24] Amanda and interpretability Josh I'm
[00:00:28] going to start with uh asking a question
[00:00:30] to Amanda uh from the alignment fine
[00:00:32] tuning team um and I want you to talk a
[00:00:35] little bit about how you see uh
[00:00:38] alignment what it means to you and um
[00:00:42] you know because you're in charge of a
[00:00:43] lot of our work on how the model should
[00:00:44] behave um and why should you be the
[00:00:47] philosopher king that decides how Claude
[00:00:50] behaves uh what its characteristics and
[00:00:52] and and attributes
[00:00:54] are I mean ask Plato he's the he's the
[00:00:56] one that decided I should be the
[00:00:57] philosopher thing um
[00:01:00] the question of like what is alignment
[00:01:02] uh maybe this is like a slightly spicy
[00:01:04] view that I have I think people are very
[00:01:05] very tempted to spend a lot of time
[00:01:07] trying to Define this concept because
[00:01:09] there's like lots of ways of doing it
[00:01:10] and they you know I don't know they have
[00:01:12] like social Choice theory in the back of
[00:01:13] their head and they're like oh well if
[00:01:14] you imagine everyone has a utility
[00:01:16] function there's like like limits on
[00:01:18] exactly what you can say about how to
[00:01:19] maximize all of those utility functions
[00:01:21] Etc um and I think I'm more inclined to
[00:01:25] just be like we kind of want things to
[00:01:27] go well enough that you can iterate on
[00:01:29] and improve them later and the bar isn't
[00:01:32] some like perfect notion of alignment
[00:01:34] I'm sure there is that concept one can
[00:01:35] Define it one one can argue about it but
[00:01:37] for the most part the initial goal is
[00:01:39] like let's just make things like go well
[00:01:41] and like meet a certain kind of like
[00:01:42] lower lower bar um where that is like
[00:01:46] you know if it's not perfect if some
[00:01:48] people like don't like it you can just
[00:01:50] improve on it um so like my view of of
[00:01:53] alignment is actually probably like I
[00:01:56] mostly want to like hit that like um and
[00:01:59] iterate from there
[00:02:00] uh in terms of like how the model should
[00:02:03] behave and how I think about that I
[00:02:05] think I've spoken about this before but
[00:02:07] my basic concept right now for the model
[00:02:09] is trying to get it to behave the way
[00:02:12] that I think like you're very good like
[00:02:15] morally motivated like kind human would
[00:02:19] act in if they found themselves roughly
[00:02:21] in this circumstance it's a little bit
[00:02:23] strange because they also have to find
[00:02:24] themselves in the circumstance of like
[00:02:25] being an EI who is like talking to
[00:02:27] millions of people um which doesn't fact
[00:02:30] affect how you behave like maybe you
[00:02:31] would normally be willing to like just
[00:02:32] chitchat about politics with someone but
[00:02:34] if you're going to be talking with
[00:02:35] millions of people maybe you'd actually
[00:02:37] be like hm I should maybe be like a
[00:02:38] little bit more concerned about
[00:02:40] potentially influencing people um and so
[00:02:44] but I do think it's actually an
[00:02:45] important model which is like sometimes
[00:02:47] people are kind of like oh what values
[00:02:48] should you put into the model um and I
[00:02:50] think I'm often like well do we think of
[00:02:51] this way with humans where I'm just like
[00:02:53] someone just injected me with like value
[00:02:55] serum or something and I just have these
[00:02:56] like fixed things I'm like completely
[00:02:58] certain of U I'm like I don't know that
[00:03:00] seems like almost like dangerous or
[00:03:02] something um most of us just have like a
[00:03:06] mix of like things that we do value but
[00:03:08] we would trade off against other things
[00:03:10] um a lot of uncertainty about different
[00:03:12] like moral Frameworks we hit cases where
[00:03:15] we're suddenly like oh actually my value
[00:03:16] framework doesn't Accord with my
[00:03:17] intuitions and we update um I think my
[00:03:20] view is that ethics is actually like a
[00:03:22] lot more like physics than people think
[00:03:24] um it's actually like a lot more kind of
[00:03:26] like empirical and uh something that
[00:03:28] we're uncertain over and that we have
[00:03:29] hypothesis about and I kind of want if
[00:03:33] I'm just like I think that I if I met
[00:03:35] someone who was just completely
[00:03:36] confident in their moral view there is
[00:03:38] no such moral view I could give that
[00:03:39] person that would not make me kind of
[00:03:41] terrified whereas if I instead have
[00:03:43] someone who's just like I don't know I'm
[00:03:44] kind of Uncertain over this and I just
[00:03:46] like update in response to like new
[00:03:47] information about ethics and I like
[00:03:49] think through these things um that's the
[00:03:52] kind of person that feels like less
[00:03:54] scary to me so at least at the moment
[00:03:56] I'm not this isn't a claim that this is
[00:03:57] somehow going to like completely like a
[00:04:00] models or anything um but that's the
[00:04:01] kind of immediate goal I've realized
[00:04:05] I've talked a lot and you asked about
[00:04:06] the philosopher king
[00:04:11] question I guess okay I guess I should
[00:04:11] in fact give a quick answer to that um
[00:04:14] there is also this question of like well
[00:04:17] in the kind of like should you put
[00:04:18] values into the model maybe I've
[00:04:19] partially answered it where I'm like
[00:04:21] like the models should just be uncertain
[00:04:23] over values that exist in the world and
[00:04:25] so ideally it's not just someone
[00:04:26] injecting their values or their
[00:04:28] preferences nor nor is it something like
[00:04:30] everyone just voting on values to put
[00:04:32] into models but instead like people um
[00:04:35] that are uncertain and responsive to
[00:04:37] these things models should also be like
[00:04:39] that so maybe that's kind of my view
[00:04:41] okay we're going to come back to that
[00:04:43] and I'm G to ask Yan uh why is Amanda's
[00:04:46] view completely wrong and why is this
[00:04:49] not enough to align models as they get
[00:04:51] you
[00:04:53] know she didn't say that but you know
[00:04:56] we're we're playing up the uh the
[00:04:57] tension between the bets so um
[00:05:00] yeah imagine if everyone was like kind
[00:05:02] uh human that was trying to you know act
[00:05:06] morally
[00:05:08] um I think what Amanda is doing is very
[00:05:10] practical right like can we just like
[00:05:12] make the models more well behave now and
[00:05:14] like
[00:05:16] um like where would we go with this like
[00:05:19] if a is doing more and more complicated
[00:05:22] things um right now like if if Amanda
[00:05:25] does this character work and then she
[00:05:27] reads a lot of transcripts and you're
[00:05:28] like okay this is like I like this this
[00:05:30] model is behaving morally I'm just
[00:05:32] picturing this is what you're doing um
[00:05:35] judging it
[00:05:37] um yeah but like what do we do when the
[00:05:40] model is doing really complex things and
[00:05:41] it's just like an agent in the world
[00:05:43] it's like doing these like really long
[00:05:45] trajectories um it's doing stuff that we
[00:05:47] don't understand like bio like doing
[00:05:50] some bio research and we're like is this
[00:05:52] dangerous like I don't know
[00:05:55] um so that's the challenge I'm really
[00:05:57] interested in like the super alignment
[00:05:58] problem how do we solve that how we like
[00:06:00] basically scale this Beyond like things
[00:06:02] that we can look at if we can look at it
[00:06:04] we just do some RF it's great or you do
[00:06:06] some constitutional AI but how do we
[00:06:09] know that our constitution is actually
[00:06:11] getting the the model to do that the
[00:06:13] right thing that we actually want so I
[00:06:15] think that's that's the big question in
[00:06:16] my mind do we get to respond yes you can
[00:06:20] respond you're only allowed to
[00:06:22] disagree okay I I don't really disagree
[00:06:26] though uh and I can't lie so um need to
[00:06:29] up the disagreement feature you I'm
[00:06:32] usually so disagreeable as well it's
[00:06:33] just terrible um this is what philosophy
[00:06:36] taught me was how to be
[00:06:38] disagreeable I guess like my thought is
[00:06:41] that the way I mean I think of my work
[00:06:42] is doing several things but one of them
[00:06:44] is being kind of iterative towards
[00:06:45] alignment so in a lot of cases you're
[00:06:46] actually trying to get the model to kind
[00:06:48] of oversee its own you know it's not
[00:06:49] like me my eyes can't look at that many
[00:06:51] transcripts or something but I can get
[00:06:52] models to like look at these things and
[00:06:55] like if alignment is iterative I think
[00:06:57] My worry is that if people neglect the
[00:06:58] kind of like the ground and just think
[00:07:00] ah you can just have like a pretty bad
[00:07:01] model um and it's just going to help you
[00:07:03] with these things I'm like I would kind
[00:07:05] of rather that you had the most aligned
[00:07:06] model trying to like then help you in
[00:07:08] the future and like that kind of
[00:07:10] iterative work but but how do you
[00:07:11] iterate when you don't you can't read
[00:07:13] the transcripts anymore and you have to
[00:07:15] rely on the aligned model but then how
[00:07:17] do you know that it's actually trying to
[00:07:19] help you yeah so like in the current
[00:07:21] cases it's sort of like everything that
[00:07:23] you are using to verify that the base
[00:07:26] model is aligned is like the C is like
[00:07:28] what you are relying on with uh like
[00:07:31] making sure that like another model
[00:07:32] that's like trained by that model is
[00:07:34] itself aligned and I think this is like
[00:07:36] fine when models are like less capable
[00:07:38] but to scale it to something with much
[00:07:40] more capable models you'd actually have
[00:07:42] to have like a greater ability to verify
[00:07:46] that yeah what do you do
[00:07:48] then oh you just want my
[00:07:51] plan it may just be that it's just all
[00:07:54] fine and they just supervise themselves
[00:07:55] and they're all really nice you know
[00:07:57] that would be I don't want to rely on it
[00:07:58] but that's not my actual plan but you
[00:08:01] know I'll defend it for these purposes
[00:08:02] and and one of our one of our bets you
[00:08:04] know to in order to like you know guard
[00:08:07] against the case that a a model might be
[00:08:09] very deeply uh trying to sabotage
[00:08:12] against this process is
[00:08:13] interpretability um how do you see like
[00:08:16] interpretability as a bet you know
[00:08:18] situated among you know uh the the more
[00:08:23] straightforward alignment approaches you
[00:08:25] know is it just as simple as like oh we
[00:08:27] find the nice feature and we like up the
[00:08:29] nice feature we find the evil feature
[00:08:30] and we like drop the evil feature right
[00:08:32] or is it you know so I feel like
[00:08:35] everything in AI is like that Meme with
[00:08:37] the bell curve and like the idiot and
[00:08:39] then the really sweaty guy talking a lot
[00:08:41] and then the Jedi who agrees with the
[00:08:43] idiot and like there is a possibility
[00:08:46] that like it turns out that the secret
[00:08:49] to alignment is just turn on the nice
[00:08:51] feature like for a sufficiently Galaxy
[00:08:53] brain version of like the nice feature I
[00:08:56] think
[00:08:57] that um in some sense though I I'm
[00:08:59] hoping Hing that interoperability is
[00:09:00] also like the Jedi version of just like
[00:09:03] well look at how the model is doing
[00:09:05] things and check that it's safe um which
[00:09:07] is like maybe very hard but also if you
[00:09:10] could do that um would potentially just
[00:09:13] answer your question um I think that
[00:09:16] like one of the one of the things that
[00:09:17] are sort of like comes up in both like
[00:09:20] the near term and slightly longer term
[00:09:22] is like you want to understand like why
[00:09:23] the model did one thing instead of
[00:09:25] another when you could come up with like
[00:09:28] plausible alternative
[00:09:29] explanations and one way is to ask it
[00:09:33] but the issue is the models are so
[00:09:34] analogous to people that they'll just
[00:09:36] give you an answer to why they did that
[00:09:39] you know as anybody would um but like
[00:09:41] how do you trust the any of that stuff
[00:09:43] and it's like well if you could like
[00:09:44] look inside and just like see what it
[00:09:47] was thinking about as it was giving you
[00:09:48] the answer and like even now with stuff
[00:09:50] like the saes you can like see there's
[00:09:52] some feature active and like when else
[00:09:54] is that happening and it's like okay
[00:09:56] it's like other instances of people
[00:09:59] telling White Lies and you're like well
[00:10:01] then maybe the model is tell it's like
[00:10:03] that's on the Jedi side I think right um
[00:10:07] and and so I think that like trying to
[00:10:09] just like look inside see if we can
[00:10:10] figure out what the parts are and then
[00:10:12] see like does are you comfortable with
[00:10:14] using that part when it does other other
[00:10:17] things is the basic the basic bet I'm
[00:10:20] I'm I'm I have a question yeah how do
[00:10:23] you how do you know you're turning up
[00:10:24] the nice feature and not the pretend to
[00:10:26] be nice feature whenever humans are
[00:10:28] looking feature
[00:10:30] [Laughter]
[00:10:33] yeah I mean like I think if it's on the
[00:10:36] control side right like how do you know
[00:10:39] and I will say actually many of the
[00:10:41] features are like a little bit like
[00:10:42] deceptive also when you just like look
[00:10:44] at what I thought the style impact team
[00:10:46] did some great work here with like ENT
[00:10:48] and deep where like you look at it um
[00:10:50] and you think it's a feature which is
[00:10:52] like um you know like age discrimination
[00:10:56] bad but like actually it's the age
[00:10:58] discrimination good feature something
[00:11:00] actually no I think vice versa so you
[00:11:01] tried to turn it down but actually the
[00:11:03] opposite Behavior so it can like be hard
[00:11:05] to hard to understand like all of the
[00:11:07] cases I will say that some of like the
[00:11:09] circuits work where you're like okay
[00:11:11] well how did this get generated gives
[00:11:13] you some clue about the scenarios like
[00:11:15] is it looking for a person in the
[00:11:17] context I also think we're going to need
[00:11:18] model supervision as well like hopefully
[00:11:21] an impartial model that isn't like
[00:11:23] that's a little more scary depending on
[00:11:25] pre-training has like what do you call
[00:11:27] it incepted in all of the models they
[00:11:29] want to evade detection but like
[00:11:31] sometimes you just like look at enough
[00:11:32] examples and it becomes clear um and you
[00:11:35] don't need 10 you need thousands but
[00:11:37] like Claude is very diligent Yan I'd
[00:11:40] love to hear a little bit more about
[00:11:41] like what you see as some of the like
[00:11:45] some of the things you're struggling
[00:11:46] with or thinking about when trying to um
[00:11:50] you know approach this problem of like
[00:11:52] how do you if you can't read the
[00:11:54] transcript like what the heck are you
[00:11:56] you know what the heck are you doing
[00:11:57] anymore if you're not if you can't
[00:11:59] provide any meaningful like alignment
[00:12:01] signal I I mean I think a really obvious
[00:12:03] thing we should do more of is like what
[00:12:05] Amanda said just say can we just get the
[00:12:08] models to help us and then the question
[00:12:10] is of course how do we trust the models
[00:12:11] like how do we boobs drop this whole
[00:12:13] process um and like you know you could
[00:12:16] hope maybe we can like Leverage the
[00:12:17] dumare models that we trust more um but
[00:12:20] they might also not be able to figure it
[00:12:22] out um and so I guess like there's the
[00:12:25] whole scaleable oversight work where um
[00:12:28] you know we have various we exploring
[00:12:30] various like multi-agent Dynamics to try
[00:12:32] to train models to you know help us
[00:12:35] figure out these kind of
[00:12:37] problems
[00:12:38] um it seems like overall right like
[00:12:42] these problems might like maybe the
[00:12:43] problems are like all kind of easy and
[00:12:45] like we can just do the Amanda thing and
[00:12:46] just like mix in some data um or it's
[00:12:49] like really hard and we have to figure
[00:12:51] out like fully new ideas and approaches
[00:12:54] that we don't know yet um I think kind
[00:12:57] of our best bet
[00:12:59] uh in the medium term is to try to
[00:13:01] figure out how to automate alignment
[00:13:03] research and then we can hopefully um
[00:13:06] get the models to do it so now we've
[00:13:08] reduced the problem like to how can we
[00:13:10] trust this model to do anything to just
[00:13:13] like well can we just trust it to this
[00:13:14] like much more narrow thing of like do
[00:13:17] some ml research which we understand
[00:13:20] like reasonably well um and how can we
[00:13:24] evaluate it or like how can we give it
[00:13:26] feedback on those kind of things and
[00:13:28] what do you what do you oh yeah go I was
[00:13:29] just going to say I think we're in this
[00:13:31] special Zone and I'm terrified about
[00:13:33] what happens next but we're in the
[00:13:34] special zone right now we like there's
[00:13:36] something happens on the forward path
[00:13:38] but a lot of the information you need is
[00:13:40] passed back through with the tokens it
[00:13:42] generates it's just like the Chain of
[00:13:43] Thought is really important for the
[00:13:44] models to be very smart and like the
[00:13:47] Chain of Thought is currently in English
[00:13:49] and so then you've got like a factorize
[00:13:51] the problem which is like is the Chain
[00:13:53] of Thought like reasonably safe and like
[00:13:56] is that faithful to what's happening on
[00:13:58] like one past and like maybe like you
[00:14:00] can do some interpretability to like
[00:14:02] check that piece and then you can just
[00:14:03] like you or models can inspect it and
[00:14:05] you get the other piece and the
[00:14:07] horrifying moment is like when all of
[00:14:09] that the very very long thing like isn't
[00:14:11] in English right it's in like some
[00:14:12] inscrutable thing that like you've
[00:14:14] learned through like crazy long RL to do
[00:14:16] it and like I think that a big challenge
[00:14:19] is going to be Crossing that Gap where
[00:14:21] like like none of the intermediates are
[00:14:23] intelligible and there's like massive
[00:14:24] amounts of compute before it like drops
[00:14:25] out and something that people can read
[00:14:28] maybe something i' be interested in
[00:14:29] getting like people's mental models on
[00:14:31] is like what do you think are some signs
[00:14:33] that like we'd be in an alignment is
[00:14:36] easy world and what do you think are
[00:14:37] some like Signs we might see in the next
[00:14:38] few years that like we're actually in a
[00:14:40] oh alignment is like really hard world I
[00:14:43] feel like the model organisms work is
[00:14:44] like trying to figure this out right
[00:14:46] like can we try to deliberately make
[00:14:49] deceptive models or misaligned models
[00:14:51] and models that like try to do Shady
[00:14:53] stuff like how good are they how hard is
[00:14:56] it to do it um I mean we might
[00:14:59] fundamentally go around like about it
[00:15:02] the wrong way and that's why we fail but
[00:15:03] if we do succeed it should tell us like
[00:15:05] how close are we to that kind of World
[00:15:09] um and then you know once you have your
[00:15:11] deceptive model does all these Shady
[00:15:13] things like can you fix it what if you
[00:15:16] don't know what the model if it's a
[00:15:17] shady model or not like we playing these
[00:15:19] interminability audits which I'm very
[00:15:21] excited about but I don't actually know
[00:15:23] what the state is we haven't done the
[00:15:25] audit yet but your people are trying to
[00:15:26] make it and we're trying to catch it
[00:15:28] yeah
[00:15:30] so we making some shady models and then
[00:15:32] they have to figure out which one is the
[00:15:33] Shady one right yeah and in what way is
[00:15:35] it in what way is it Shady CU most of it
[00:15:37] is still fine I mean I think one one
[00:15:38] thing that the interpretability stuff
[00:15:40] has been interesting is so when you do
[00:15:41] these like unsupervised things you're
[00:15:42] like okay here's a million different
[00:15:44] like features a bunch of those
[00:15:45] correspond to personas the model could
[00:15:47] inhabit any of those which include all
[00:15:49] sorts of like deceptive behaviors right
[00:15:51] that are out there in the world right
[00:15:52] the model like knows about bad people
[00:15:55] and like bad motivations and so like the
[00:15:58] fact that that capability exists is just
[00:16:00] going to be baked in and then the
[00:16:01] question is like is it doing that stuff
[00:16:03] or is it doing the good stuff especially
[00:16:05] like this question of like when aanda
[00:16:07] goes and shapes the base model right
[00:16:08] which isn't really anything right into
[00:16:10] like an agent or an actor which is
[00:16:12] supposed to embody some of these and not
[00:16:14] others like can we tell exactly what it
[00:16:16] picked up there right from the finite
[00:16:19] data set right which is being used to
[00:16:20] like do that shaping um and like yeah so
[00:16:24] that's a that's a question I mean I
[00:16:25] think that like some interpretability
[00:16:27] have maybe some influence function I
[00:16:28] mean there's different ideas there to
[00:16:29] ask like what did it get from this
[00:16:31] process but like that shaping process is
[00:16:33] going to be really really important yeah
[00:16:36] and maybe a sign that seems important is
[00:16:38] something like how robust or like like
[00:16:41] if you have like modal organisms work
[00:16:43] and then turns out you just put it
[00:16:44] through some character training and it
[00:16:45] just comes out being really nice again
[00:16:46] then I'd be like okay that's a good sign
[00:16:48] re the kind of world that we're in um or
[00:16:51] is it like just like is just a kind of
[00:16:53] like shallow like shell on top of like
[00:16:56] um I don't know the same behavior then
[00:16:58] I'm like okay okay we're in a slightly
[00:16:59] harder world only slightly harder how
[00:17:01] how do you distinguish like whether it's
[00:17:03] shallowly aligned or deeply aligned I
[00:17:05] think so I mean I feel like there's a
[00:17:06] lot you could do because I think
[00:17:08] interpretability is kind of like one of
[00:17:09] them there's other things that feel so
[00:17:12] in terms of like modal organisms I guess
[00:17:14] my hope would be you'd actually have a
[00:17:15] kind of like red team blue team setup
[00:17:17] where you have a way of detecting
[00:17:19] whether the behavior that you have like
[00:17:20] instilled in a model is like still there
[00:17:22] um and my job is actually to not know H
[00:17:24] and in fact it would be really good if
[00:17:26] I'm trying to train the model I actually
[00:17:27] just don't know what it is that you've
[00:17:29] done um because that's like a better way
[00:17:31] of testing whether my intervention is
[00:17:32] actually working whereas because
[00:17:34] otherwise I it's just so hard to not
[00:17:35] like just try to train to the test or
[00:17:37] something so I think that's I almost
[00:17:39] want to be completely ignorant of it
[00:17:42] yeah maybe we should play an alignment
[00:17:44] finding game yeah yeah he misalign it
[00:17:46] and then you align it and we see who
[00:17:48] wins yeah no I've said to people before
[00:17:50] don't don't tell me how you did this
[00:17:51] because I want to see if can fix her
[00:17:53] Sleeper
[00:17:59] Agent possibly
[00:17:59] we could play that game I think I might
[00:18:01] need to know less uh make another one
[00:18:05] make another one that's worse that is an
[00:18:07] excellent transition and to questions um
[00:18:11] so we are going to uh pass a mic around
[00:18:14] Ain uh is kindly going to do that um
[00:18:16] please raise your hand if you have a
[00:18:18] question for any of us um oh perfect um
[00:18:23] hello uh I have a question about um well
[00:18:27] everything you've been talking
[00:18:29] uh so when we talk about alignment we're
[00:18:31] talking about like a singular forward
[00:18:33] pass typically right so like uh
[00:18:35] alignment at inference time so if I'm
[00:18:38] using one of the models um via the API
[00:18:42] and I'm building my own sense of say
[00:18:45] cultural alignment and I've got a bunch
[00:18:47] of different Agents set up talking to
[00:18:49] each other trying to deliberate with
[00:18:51] that sense of kind of inner conflict
[00:18:53] that Amanda referenced as useful in in
[00:18:56] what we do as humans to align like we go
[00:18:58] back and forth we think you know we go
[00:19:01] through various cognitions so if I'm
[00:19:03] trying to create this kind of multi-
[00:19:06] agentic
[00:19:07] deliberation thing but I butt up against
[00:19:11] this aligned model who is so uh unwan to
[00:19:18] deliberate with other spawns of its own
[00:19:20] with its own self because all of them
[00:19:23] are like I'm sorry I can't talk about
[00:19:24] that and so you just get this endless
[00:19:26] loop did you have commentary on on on
[00:19:29] that cuz many people we're not all using
[00:19:31] Claude in a single inference forward
[00:19:33] passway
[00:19:34] so yeah I hope someone gets the gist of
[00:19:37] what I'm on
[00:19:39] about yeah I need to think about it so I
[00:19:42] guess like is the thought like to be
[00:19:43] clear I'm not thinking necessarily that
[00:19:45] you have many agents um in the same way
[00:19:49] that we can be singular agents but still
[00:19:51] like deliberative and I actually think
[00:19:53] that like there's a sense in which the
[00:19:56] more fractured an agent is the more
[00:19:58] worried am because from like an
[00:20:00] interpretability perspective and also
[00:20:02] even just like a predicting what that
[00:20:04] agent is going to do perspective they're
[00:20:06] more unpredictable um so I guess I'm
[00:20:09] thinking in the same way that like maybe
[00:20:11] I guess a different way of asking this
[00:20:12] question is just do humans have to do
[00:20:15] this like my sense is that we're often
[00:20:16] just very willing to like reflect on
[00:20:18] many things we go back and forth we come
[00:20:21] to like conclusions and so in the same
[00:20:23] way that like a human would think
[00:20:24] through any kind of standard problem uh
[00:20:27] that they were like facing I'm imagining
[00:20:29] that like moral deliberation in the
[00:20:30] model is just going to look kind of like
[00:20:32] that more like the deliberation of a
[00:20:33] single model than like uh multiple
[00:20:35] models weighing in if that makes
[00:20:38] sense one more question here I I want to
[00:20:42] try to draw maybe a relatively strange
[00:20:44] parallel between like Hana AR's work on
[00:20:46] the banality of evil the idea that most
[00:20:49] humans tend not to be evil but when put
[00:20:50] in certain situations the coupling
[00:20:53] constant between humans being so huge
[00:20:55] the evil comes as an epop phenomenon of
[00:20:56] the system right and so what what occurs
[00:20:58] to me is as you talk about model
[00:21:00] alignment you're focus on one model is
[00:21:02] most of your comments how do you think
[00:21:04] about the coupling not only with Society
[00:21:05] but as you work on agents and Mill
[00:21:07] potentially millions and millions of
[00:21:09] agents that sort of epiphenomenon of
[00:21:10] those
[00:21:11] systems a
[00:21:13] question um I can talk a a little bit
[00:21:16] about that I mean I think broadly when
[00:21:18] you have to think about when you think
[00:21:19] about safety and Alignment you have to
[00:21:20] think about it from a systems standpoint
[00:21:22] you can't just think about it from you
[00:21:24] know an individual uh models perspective
[00:21:27] and isolation and I think we've seen a
[00:21:29] lot of work where you know a lot of
[00:21:30] jailbreaks operate by pitting different
[00:21:33] values sort of against each other
[00:21:34] putting the model in a difficult
[00:21:35] situation where you know it's designed
[00:21:37] to elicit what would ordinarily be a
[00:21:39] harmful Behavior but which uh you know
[00:21:41] in the context of the question the model
[00:21:43] thinks sort of is is the right thing to
[00:21:45] do um and so uh you know there's a
[00:21:47] variety of tools you can use to do that
[00:21:49] I mean for one you can include a lot of
[00:21:51] those you know uh systems level um
[00:21:54] Integrations in the training process
[00:21:56] right and give them all exposure to a
[00:21:57] wider variety of situations
[00:21:59] for it to you know the uh the broad umex
[00:22:04] in it's answering questions now that
[00:22:06] leads to other uh challenges and and and
[00:22:08] other sort of like um you know uh
[00:22:11] fall-off issues um with the model is
[00:22:13] reasoning about you know the the um uh
[00:22:16] effect of its actions but I I think I
[00:22:19] agree with the point that you can't just
[00:22:20] consider a model sort of in isolation in
[00:22:23] some ways like this is a thing that I've
[00:22:25] thought about in the context of like
[00:22:27] this notion of corrigibility
[00:22:28] or some like you know so like models
[00:22:30] that just are responsive to like what
[00:22:31] humans want versus models that are like
[00:22:34] uh like have values in a sense and are
[00:22:36] maybe like willing to actually be a
[00:22:37] little bit uncor um and like the
[00:22:41] banality of evil Point feels especially
[00:22:42] relevant if you're like thinking of
[00:22:44] models as just like doing whatever
[00:22:45] humans say because in in some ways like
[00:22:48] that is the idea that if you have a
[00:22:49] society that like either collectively
[00:22:51] just like allows for harmful things to
[00:22:53] take place or even endorses them and you
[00:22:54] have models this isn't necessarily
[00:22:56] people misusing models it's just that
[00:22:57] you'd be using models to like facilitate
[00:22:59] some kind of like harmful activity um
[00:23:02] and so I think there is like
[00:23:03] fundamentally actually a tension between
[00:23:05] having models be corable to the very
[00:23:07] least individual humans and having them
[00:23:09] be like uh aligned in in a sense like
[00:23:13] aligned with like all humans um and it's
[00:23:16] really important to recognize that
[00:23:18] tension and I think when people don't
[00:23:19] they think like H it's a failure that
[00:23:21] the model like didn't do what I said but
[00:23:23] I'm like there's a limited sense in
[00:23:25] which models I think models should be
[00:23:26] more corrigible to like Humanity
[00:23:29] then then not and should be willing to
[00:23:31] like you know like so there's like when
[00:23:32] push comes to shove like um but that
[00:23:34] doesn't necessarily mean being
[00:23:35] corrigible with each person um because I
[00:23:37] think that could lead to that kind of
[00:23:38] like situation that you
[00:23:41] mentioned hi um so it seems like we've
[00:23:44] got Yan who's working on intent
[00:23:46] alignment making sure the models do what
[00:23:48] we ask them to do Amanda working on
[00:23:50] values alignment making sure the models
[00:23:52] are like reasonable kind entities and
[00:23:55] then Josh working on interpretability
[00:23:56] which is like allowing us to verif ify
[00:23:58] that the techniques for those other
[00:23:59] things are in fact doing what we want um
[00:24:02] if you were all to succeed in your areas
[00:24:04] would that be a complete solution to AI
[00:24:05] safety um or are there pieces missing
[00:24:07] and if so what are
[00:24:13] they there's also like a lot of people
[00:24:13] working on topic who are not at this
[00:24:16] panel so we are oversimplifying a little
[00:24:20] bit Yeah and and oh I was just going to
[00:24:23] say we also you know have the societal
[00:24:25] impacts team which thinks about the
[00:24:26] model's impact on societ
[00:24:29] uh you know writ large and and so I
[00:24:31] think uh yeah we we you know you could
[00:24:33] have the most perfectly aligned model
[00:24:35] but uh aligned to what who's using it in
[00:24:38] what purposes you know for what purposes
[00:24:40] um you know and and I think the broader
[00:24:42] societal context is super something we
[00:24:44] we're very attentive to also if you're
[00:24:47] just interested in just more lists like
[00:24:49] we already mentioned the model organisms
[00:24:50] work there's like you know jailbreaking
[00:24:52] robustness there's control there's like
[00:24:55] trust and safety there's like um yeah
[00:24:58] there there's a lot of other efforts
[00:25:00] that I think are also going to be
[00:25:01] important can I I want to add an almost
[00:25:05] like I don't know if this is pessimistic
[00:25:06] or or just I don't think it's
[00:25:09] pessimistic I think that like there's
[00:25:11] also this way of talking about alignment
[00:25:13] and the alignment problem as like a sing
[00:25:16] it's not like as like a single like
[00:25:17] theoretical problem or something like
[00:25:19] that where people will be like does this
[00:25:20] solve it and somehow it's never felt
[00:25:22] right it feels a little bit like you
[00:25:23] know I don't know does
[00:25:24] like it yeah it feels more like to my
[00:25:28] mind I'm just like look problems might
[00:25:30] just arise that we're not even thinking
[00:25:31] of now and in fact that's like very very
[00:25:33] common um in like many many disciplines
[00:25:36] and I kind of expect it to be true here
[00:25:38] and it would be really dangerous I think
[00:25:39] if we were just like oh yeah we've like
[00:25:41] solved this problem um because I'm just
[00:25:43] like I don't know it could be that the
[00:25:44] actual problem is one that we've just
[00:25:45] not thought of yet yeah unkown unknowns
[00:25:47] are but we should solve the problem and
[00:25:50] then once we did we should say that we
[00:25:51] solved
[00:25:52] it another question here Yan was talking
[00:25:55] earlier about using Dumber models to
[00:25:57] evaluate smarter models time and I'm
[00:25:58] wondering to what extent you see like
[00:26:00] the grocking abilities in models where
[00:26:02] like Suddenly It's really duplicitous or
[00:26:04] you sort of see oh it's lying but it's
[00:26:05] very bad at lying and now I can catch
[00:26:07] that and maybe like nip that in the bud
[00:26:08] while it's still weak yeah I mean
[00:26:11] there's like plenty of examples like one
[00:26:13] that I remember is like gbd uh 4 could
[00:26:17] just read and write in B 64 Super
[00:26:19] reliably and 3.5 could not and so if you
[00:26:23] use 3.5 to over C4 it's like really easy
[00:26:26] for the model to get around this I I
[00:26:28] mean like on a level of like a single
[00:26:30] Epoch or something like you see over
[00:26:31] time okay kind of read B 64 sometimes
[00:26:34] more more more oh suddenly can do it
[00:26:36] perfectly or is
[00:26:38] it Oh you mean like should we use
[00:26:40] checkpoints so don't use the previous
[00:26:42] generation just like you know you ensure
[00:26:44] even spacing and capability Space by
[00:26:47] like just yeah yeah exactly but then
[00:26:49] also like the trust is not like a binary
[00:26:52] thing right like you trust it less and
[00:26:53] less the less you know about it and the
[00:26:56] you know smarter it seems
[00:26:58] I will say one like you know right side
[00:27:00] of the distribution Jedi moment was like
[00:27:04] that uh the features you know just like
[00:27:07] also work in Bas 64 so it's like is the
[00:27:10] model talking about California in Bas 64
[00:27:12] or like a story about children lying to
[00:27:14] their parents in Bas 64 it's like the
[00:27:16] same things activate and so like there
[00:27:19] we do get sometimes get lucky as like
[00:27:21] the models are like very capable part of
[00:27:23] that is they have some like very general
[00:27:24] synthetic thing and like maybe you can
[00:27:25] just like tap that to get some
[00:27:27] generalization would have been like
[00:27:29] pretty pretty tough there's also the
[00:27:31] early paper of just like tell the model
[00:27:32] to do what's best for Humanity version
[00:27:34] of alignment which is definitely like
[00:27:37] like maybe that'll work right you know
[00:27:40] you could get lucky all right I think we
[00:27:42] are going to wrap up with the formal
[00:27:43] panel um thank you to all of our
[00:27:46] panelists so much for uh um the great
[00:27:49] discussion um but we're going to be
[00:27:52] around for a lot longer to continue the
[00:27:54] conversation feel free to find any of us
[00:27:56] um and uh we're excited to chat more
[00:27:59] thanks so much thank you
