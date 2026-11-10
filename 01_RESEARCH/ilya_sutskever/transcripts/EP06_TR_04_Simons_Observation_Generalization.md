# Simons Institute Berkeley: Ilya Sutskever — An Observation on Generalization
- **YouTube URL:** https://www.youtube.com/watch?v=AKMuA_TVz3A
- **Lines:** 1284

---

[00:00:00] and it has citation counts that's six
[00:00:02] digit it's more than four
[00:00:05] 139,000 um and then many more so super
[00:00:09] excited to hear what IIA has to say
[00:00:11] about llms and the future take it away
[00:00:13] okay
[00:00:18] hi hi hi everyone thank you for the
[00:00:22] introduction you know when uh when UMES
[00:00:26] invited me to to to attend this event I
[00:00:28] got really excited I saw all the the
[00:00:30] speaker relist and I thought great I'll
[00:00:31] I'll go and I'll talk about something
[00:00:33] and then I ran into a problem which
[00:00:37] is that a lot of the technical work that
[00:00:40] you're doing at open AI actually can
[00:00:41] talk
[00:00:42] about so I was really racking my head
[00:00:45] what could I talk
[00:00:46] about right now so as of not too long
[00:00:50] ago I switched all my focus to working
[00:00:53] on AI alignment all my research focus
[00:00:57] and we'll have very cool results to show
[00:00:59] there but not just yet
[00:01:00] so I'm like okay so this would have to
[00:01:02] be for the next stock but what would be
[00:01:04] good for this stock and I came up with
[00:01:08] something I'll tell you about some very
[00:01:11] old
[00:01:13] results
[00:01:17] that we had an open AI many years ago
[00:01:21] back in 2016 even which really affected
[00:01:25] the way I think about unsupervised
[00:01:28] learning and I thought that share them
[00:01:30] with you it is possible
[00:01:33] that at this point you'll all find them
[00:01:36] obvious but maybe not all of them so
[00:01:39] there is at least a small chance that
[00:01:41] you'll find it interesting so I want to
[00:01:43] set the expectations modestly and and
[00:01:45] hopefully exceed
[00:01:47] them so a theory of unsupervised
[00:01:53] learning how can such a thing
[00:01:57] exist so okay
[00:02:01] before we talk about unsupervised
[00:02:03] learning we want to talk about learning
[00:02:04] in
[00:02:05] general what is learning and why does
[00:02:07] learning work at all why should learning
[00:02:10] work at all and why should computers be
[00:02:12] able to
[00:02:13] learn and now we just used to the fact
[00:02:17] we take it for granted that neural
[00:02:18] networks learn but but why do they like
[00:02:22] mathematically why should they why would
[00:02:24] data have
[00:02:27] regularity that our machine learning
[00:02:30] models can
[00:02:31] capture so that's not an obvious
[00:02:34] question and one important conceptual
[00:02:37] advance that has taken place in machine
[00:02:41] learning many years ago by multiple
[00:02:44] people was the discovery and the
[00:02:48] formalization of supervised learning so
[00:02:51] it goes under the name of P learning or
[00:02:53] statistical learning
[00:02:55] theory and the nice thing about
[00:02:58] supervised learning is that it gives you
[00:03:01] a precise mathematical condition under
[00:03:04] which learning must
[00:03:10] succeed you're told that if you have
[00:03:12] some data from some data
[00:03:15] distribution that if you manage to
[00:03:18] achieve a low training loss and the
[00:03:20] number of your degrees of
[00:03:24] freedom is not is smaller than your
[00:03:28] training set
[00:03:30] then you will achieve low test error and
[00:03:32] you are guaranteed to do so so you have
[00:03:35] a mathematical condition where you can
[00:03:38] say well if if I did find a function out
[00:03:41] of my function class which achieves low
[00:03:43] training
[00:03:44] error then learning will succeed and you
[00:03:48] can say yeah this is a very
[00:03:51] sensible mathematical thing that we can
[00:03:54] reason about and that's why supervis
[00:03:57] learning is easy then you had all these
[00:04:00] theorems which I thought were simple you
[00:04:02] know I found them
[00:04:04] elegant you've seen maybe theorems like
[00:04:06] this if you have your basically it's
[00:04:08] like this is the sort of thing where if
[00:04:10] you know it you're going to say oh yeah
[00:04:11] that thing and if you don't know it it
[00:04:13] will not be possible to explain it in 30
[00:04:15] seconds though it it is possible to
[00:04:16] explain it in five minutes just not 30
[00:04:18] seconds none of this stuff is
[00:04:20] complicated and you've got your little
[00:04:22] proof which says well if you have some
[00:04:26] number of functions in your function
[00:04:28] class the probability that your train
[00:04:31] error will be far from your test error
[00:04:33] for at least one function there is some
[00:04:36] math and the math is simple this is all
[00:04:38] the math three lines of math so three
[00:04:40] lines of math can prove all of
[00:04:41] supervised
[00:04:42] learning well that's nice that's very
[00:04:46] nice so supervised learning is something
[00:04:48] that is well understood comparatively
[00:04:50] speaking well understood we know why it
[00:04:54] must Su must succeed so we can go forth
[00:04:57] and collect large supervised learning
[00:04:59] dat dat sets and be completely
[00:05:02] certain that models will keep getting
[00:05:06] better
[00:05:08] so that's that's the story
[00:05:12] there
[00:05:14] and yeah I forgot to mention a very
[00:05:16] important piece of this results the test
[00:05:19] distribution and training distribution
[00:05:20] need to be the same if they are the same
[00:05:23] then your theory of supervised learning
[00:05:25] kicks in and works and will be
[00:05:27] successful
[00:05:29] so conceptually it is
[00:05:32] Trivial we have an answer for why
[00:05:36] supervised learning works why speech
[00:05:38] recognition should work why image
[00:05:42] categorization should work because they
[00:05:44] all reduce to supervised learning which
[00:05:46] works which has this mathematical
[00:05:48] guarantee so this is very
[00:05:51] nice here I want to make a small side
[00:05:54] comment on VC Dimension to those of you
[00:05:56] who care about such things there may be
[00:05:58] a small subset so if you want to zone
[00:06:00] out for the next 30 seconds feel free to
[00:06:02] do
[00:06:04] so
[00:06:05] so a lot of writings
[00:06:09] about statistical learning theory
[00:06:11] emphasize the VC Dimension as a key
[00:06:15] component
[00:06:16] but the main reason the VC dimension in
[00:06:19] fact the only reason the VC Dimension
[00:06:21] was invented was to allow us to
[00:06:27] handle parameters which have infinite
[00:06:30] Precision the VC Dimension was invented
[00:06:33] to handle Precision like parameters with
[00:06:35] infinite Precision so if you have your
[00:06:36] linear classifier every parameter is
[00:06:38] infinite
[00:06:40] Precision but then of course in
[00:06:43] reality all our floats are finite
[00:06:46] precision and their Precision is
[00:06:47] shrinking so you
[00:06:49] can and you can so you have your so the
[00:06:52] number of functions that are implemented
[00:06:53] by a computer is actually small and you
[00:06:55] can reduce it back to the
[00:06:57] little this little formul which gives
[00:07:00] you pretty much all the best bounds that
[00:07:03] you can get from supervised learning so
[00:07:05] I find this to be cool I find this to be
[00:07:08] appealing because you have fewer lines
[00:07:10] of
[00:07:14] proof okay now let's talk about
[00:07:17] unsupervised
[00:07:18] learning so I claim first of all what is
[00:07:22] unsupervised learning what is
[00:07:24] it supervised learning is like yeah
[00:07:27] you've got your data that says here do
[00:07:29] do this here do that and you have all
[00:07:31] this data you do well in your training
[00:07:34] error your training error is low you
[00:07:36] have more training data than degrees of
[00:07:39] freedom in your function
[00:07:40] class parameters but maybe other things
[00:07:43] too degrees of freedom like
[00:07:46] bits and you say okay super your
[00:07:48] supervised learning will succeed but
[00:07:49] what is unsupervised learning what can
[00:07:51] you say at all about unsupervised
[00:07:54] learning and I'll say that I at least I
[00:07:56] have not seen like an exposition of
[00:07:59] unsupervised learning which you found
[00:08:01] satisfying how to reason about it
[00:08:02] mathematically we can reason about it
[00:08:04] intuitively but can we reason about it
[00:08:08] mathematically and for some context what
[00:08:10] is the old dream of unsupervised
[00:08:13] learning which by the way this dream has
[00:08:14] been fulfilled but it's fulfilled
[00:08:16] empirically like can we go just a tiny
[00:08:19] bit beyond the empirical results like
[00:08:22] the idea that you just look at the
[00:08:24] images or you just look at the text
[00:08:25] without being told what to do with them
[00:08:27] and somehow you still discuss the true
[00:08:30] hidden structure that exists in the data
[00:08:32] and somehow it helps
[00:08:34] you why why why should it happen should
[00:08:39] it happen should we expect it to
[00:08:42] happen you cannot you don't have
[00:08:44] anything remotely similar to the
[00:08:47] supervised learning guarantee the
[00:08:49] supervised learning guarantee says yeah
[00:08:50] like get your low training error and
[00:08:52] you're going to get your learning it's
[00:08:53] going to be great
[00:08:54] success on supervised learning it
[00:08:57] appears it appears that it's not this
[00:08:59] way
[00:09:00] and you know like people were talking
[00:09:01] about it for a long time in the 80s the
[00:09:03] Bolson machine was already talking about
[00:09:05] unsupervised learning and on supervis
[00:09:09] learning also did not work at small
[00:09:10] scale but the all but the old ideas were
[00:09:12] there like the noise in Auto incar to
[00:09:15] those of you who remember remember it
[00:09:17] it's like bir or the diffusion model
[00:09:19] like within it it's a tiny twist the
[00:09:21] tiniest of twists the language models of
[00:09:24] all times they also you know generated
[00:09:27] cool samples for their time but
[00:09:30] their unsupervised learning performance
[00:09:32] was not as impressive as those of
[00:09:35] today but I want to make the case that
[00:09:37] it is confusing because it's
[00:09:39] like why is it confusing you optimize
[00:09:42] like how does superv learning work you
[00:09:43] say okay let's optimize some kind of
[00:09:45] reconstruction error or let's optimize
[00:09:48] some kind of a the noising error or like
[00:09:50] some kind of self-supervised learning
[00:09:53] error you optimize one
[00:09:55] objective right oh yes I just said that
[00:09:58] but you care about a different
[00:10:00] objective so then doesn't it mean that
[00:10:02] you have no reason to expect that you'll
[00:10:08] get any kind of good un supervised
[00:10:10] learning results or rather you know you
[00:10:11] do get them empirically but like is it
[00:10:13] going to be like the level of mystery is
[00:10:16] quite High I claim like it seems totally
[00:10:19] in like a totally inaccessible
[00:10:20] phenomenon you optimize one objective
[00:10:22] but you care about another objective and
[00:10:24] yet it helps how can that be magic
[00:10:33] okay so
[00:10:34] yeah the other thing by the way is that
[00:10:37] un well I
[00:10:39] guess I'm gonna I'm going to say
[00:10:42] something which is only 90%
[00:10:44] true un supervised learning doesn't you
[00:10:47] you could say okay so you just learn the
[00:10:49] structure in the input distribution and
[00:10:51] it helped you but then you know what if
[00:10:54] you're training from the uniform
[00:10:56] distribution then all your unsupervised
[00:10:58] learning algorithms will
[00:11:00] fail how should you think about
[00:11:04] that so what can we
[00:11:06] say what can do we need to make
[00:11:08] assumptions what kind of assumptions so
[00:11:11] I'd like to present
[00:11:14] potentially a way of thinking about
[00:11:16] unsupervised learning which I think is I
[00:11:18] personally find it interesting perhaps
[00:11:20] you'll find it interesting too let's
[00:11:21] find
[00:11:23] out so I want to show you one way of
[00:11:28] doing supervised learning which is not
[00:11:31] necessarily widely known because it
[00:11:33] never became the dominant way of doing
[00:11:34] unsupervised learning but it has the
[00:11:36] cool
[00:11:37] feature that similarly to supervised
[00:11:41] learning it has to
[00:11:43] work so what kind of mysterious
[00:11:47] unsupervised learning procedure for you
[00:11:49] not given any
[00:11:51] labels to any of your inputs is still
[00:11:54] guaranteed to work distribution matching
[00:11:59] distribution
[00:12:01] matching so what is distribution
[00:12:03] matching say I've got my data I've got X
[00:12:06] and I've got Y data sources there's no
[00:12:09] correspondence between them just got two
[00:12:11] data sources data source X dat Source Y
[00:12:13] data source y language one language two
[00:12:16] text
[00:12:19] speech no correspondence between
[00:12:23] them let us look at this
[00:12:25] Criterion find the function f such that
[00:12:30] the distribution of f ofx is similar to
[00:12:33] the distribution of Y it is a constraint
[00:12:36] on F and in the case of machine
[00:12:39] translation and speech
[00:12:41] recognition for
[00:12:43] example this constraint might be
[00:12:47] meaningful like you could say yeah if I
[00:12:51] have like long
[00:12:52] sentences if if if you tell me that you
[00:12:54] have a function such that the
[00:12:56] distribution you take your distribution
[00:12:57] of English sentences
[00:12:59] you apply the function f to them and you
[00:13:01] get something which is very similar to
[00:13:03] the distribution of French sentences you
[00:13:04] can say
[00:13:10] okay I found the true constraint about F
[00:13:15] if the dimensionality of X and the
[00:13:18] dimensionality of Y is high enough
[00:13:20] that's going to give you a lot of
[00:13:21] constraints in fact you might be able to
[00:13:24] almost fully recover F from that
[00:13:27] information this is an example of
[00:13:30] supervised learning of unsupervised
[00:13:32] learning where it is still guaranteed to
[00:13:36] work in the same sense that supervised
[00:13:38] learning is guaranteed to
[00:13:41] work also substitution ciphers like
[00:13:44] little simple encryptions will also fit
[00:13:47] into this
[00:13:48] framework so that's the thing like okay
[00:13:52] and so like I I I kind
[00:13:55] of I ran into this I
[00:13:59] in independently discovered this in
[00:14:02] 2015 and I got really fascinated by it
[00:14:05] because I thought wow maybe there is
[00:14:08] something meaningful mathematically
[00:14:11] meaningful that we can say about
[00:14:13] unsupervised
[00:14:15] learning and so but let's see this the
[00:14:18] thing about this setup is that still a
[00:14:20] little bit artificial it's still real
[00:14:22] machine learning setups aren't like this
[00:14:25] and the way we like to think about
[00:14:27] unsupervised learning isn't that
[00:14:31] also okay now I'll present to you the
[00:14:35] meat the meat of what I'm going what I
[00:14:37] wanted to
[00:14:38] say
[00:14:40] how a proposed way to think about
[00:14:42] unsupervised
[00:14:44] learning that lets you that puts it on
[00:14:47] par with supervised learning says okay
[00:14:49] what is it doing mathematically how can
[00:14:51] you be sure that your un supervised
[00:14:52] learning is
[00:14:54] good compression to the
[00:14:57] rescue oh obviously it is well known I
[00:15:01] shouldn't say Obviously it is not
[00:15:03] obvious but it is well known that
[00:15:05] compression is prediction every
[00:15:07] compressor can be a predictor and vice
[00:15:09] versa there is a onetoone correspondence
[00:15:12] between all compressors and all
[00:15:15] predictors however I would argue that
[00:15:19] for the purpose of thinking about
[00:15:21] unsupervised
[00:15:24] learning the language of compression
[00:15:26] offers some advantages at least for me
[00:15:29] it did perhaps it will for you
[00:15:35] too so
[00:15:38] consider the following thought
[00:15:40] experiment this thought experiment is
[00:15:42] the most important
[00:15:44] slide say you have two data sets X and Y
[00:15:51] in two data sets two files on your big
[00:15:55] giant hard
[00:15:57] disk and say you have a a really great
[00:15:59] compression algorithm C which takes data
[00:16:02] in and outputs compressed objects
[00:16:07] out say you compress X and Y jointly you
[00:16:10] concatenate them you take the two data
[00:16:13] sets and you concatenate them and you
[00:16:14] feed them to your compressor what will
[00:16:17] happen well let's see what and in
[00:16:20] particular an important question is what
[00:16:22] will a sufficiently do good compressor
[00:16:24] will
[00:16:26] do my answer is very intuitively it will
[00:16:30] use the patterns that exist inside
[00:16:33] X to help it compress Y and vice
[00:16:37] versa you could make the same Claim
[00:16:40] about prediction but somehow it's more
[00:16:42] intuitive when you say it about
[00:16:43] compression I don't know why there is
[00:16:45] but I find it to be the case so that's
[00:16:47] our clue and you can make an equation
[00:16:51] like this where you say hey if your
[00:16:53] compression is good enough if it's like
[00:16:55] a real great compression compressor it
[00:16:57] should say that the compression of your
[00:17:00] concatenation of your giant
[00:17:02] files should be no worse than the
[00:17:05] separate compression of you two files so
[00:17:08] any additional compression that was
[00:17:10] gained by
[00:17:12] concatenation is some kind of shared
[00:17:14] structure that your compressor noticed
[00:17:18] and the better your compressor is the
[00:17:19] more shared structure it will extract
[00:17:22] the Gap is the shared structure or the
[00:17:24] algorithmic mutual information
[00:17:28] that's interesting right you can see
[00:17:30] what I'm alluding to Y is the data of
[00:17:33] your supervised task X is your
[00:17:35] unsupervised task but suddenly you have
[00:17:38] some kind of mathematical reason for the
[00:17:41] information for the patterns in X to try
[00:17:43] to help
[00:17:45] y notice also how it generalizes
[00:17:48] distribution
[00:17:49] matching
[00:17:51] if we are in the distribution matching
[00:17:54] case where you've got your X is language
[00:17:57] one and Y is language two two and you
[00:17:59] are
[00:18:00] saying and you know that there exists
[00:18:03] some simple function f that transforms
[00:18:06] one distribution into the other surely
[00:18:08] your compressor if it's good will notice
[00:18:10] that and make use of that and maybe even
[00:18:13] internally try to recover this
[00:18:19] function so I think that's pretty cool
[00:18:22] we've closed this we've closed the
[00:18:26] circle so how do we formalize it then
[00:18:29] what will be the formalization of
[00:18:30] unsupervised
[00:18:32] learning let's see let's see if I can do
[00:18:35] it consider an ml algorithm so here by
[00:18:39] the way in what follows I'll be a bit
[00:18:41] sloppy and I will use compression and
[00:18:44] prediction
[00:18:46] interchangeably say you have a machine
[00:18:48] learning algorithm a it's an algorithm a
[00:18:50] and it tries to compress
[00:18:52] Y and say it has access to x x is file
[00:18:57] number one and Y is file number two you
[00:19:01] want your machine learning algorithm
[00:19:03] your compressor to compress Y and it can
[00:19:06] Pro X as it is fit the goal is to
[00:19:09] compress y as well as
[00:19:11] possible we can ask ourselves what is
[00:19:14] our regret of using this particular
[00:19:16] algorithm they'll see where I'm getting
[00:19:19] at regret relative to what if I do a
[00:19:23] good enough
[00:19:24] job if I have like being low regret
[00:19:27] means that I've got gotten all the help
[00:19:30] they can that I can possibly get from
[00:19:32] this unlabeled data this unlabeled data
[00:19:36] has helped me as much as possible and I
[00:19:38] don't feel bad about it I don't feel bad
[00:19:39] I don't feel like I've left some
[00:19:41] prediction value on the table that
[00:19:43] someone else with a better compression
[00:19:44] algorithm could have used that's what it
[00:19:48] means and in particular it's like yeah
[00:19:50] like you can go and you can sleep
[00:19:52] happily at night knowing that if there
[00:19:54] is some information in the unlabeled
[00:19:57] data that could help my task
[00:19:59] no one else like no no one could have
[00:20:01] done as good of a job as me I've done
[00:20:03] the best job at benefiting from my
[00:20:04] unlabeled
[00:20:06] data so I think that is a step towards
[00:20:09] thinking about unsupervised learning you
[00:20:11] don't know if your unsupervised data set
[00:20:15] is actually useful it may be super
[00:20:17] useful it may have the answer it may be
[00:20:19] totally useless it may be the uniform
[00:20:22] distribution but if you have a low
[00:20:24] regret on supervised learning algorithm
[00:20:26] you can say whether it's the first case
[00:20:28] or the second case I know I've done my
[00:20:31] best I know I've done my best at
[00:20:33] benefiting from my unlabeled data and no
[00:20:36] one could have done better than
[00:20:39] me now I want to take a detour to some
[00:20:42] to to Theory land which is little
[00:20:44] obscure I think it is
[00:20:47] interesting color of complexity as the
[00:20:49] ultimate compressor gives us the
[00:20:51] ultimate low regret algorithm which is
[00:20:53] actually not an algorithm because it's
[00:20:54] not computable but you will see what I
[00:20:57] mean really quickly so kagor first of
[00:20:59] all like for some context who know who
[00:21:01] here is familiar with kagor
[00:21:04] complexity okay about 50% yeah um it's
[00:21:08] it's the comor complexity is the kind of
[00:21:10] thing which is easy to explain in one
[00:21:13] minute so I'll just do it it's
[00:21:17] like
[00:21:19] imagine if I give you some data or you
[00:21:22] give me some data and I'm going to
[00:21:23] compress it by giving you the shortest
[00:21:27] program
[00:21:28] that can possibly exist the shortest
[00:21:30] program that exists which if which if
[00:21:33] you run it outputs your
[00:21:43] data yes that is
[00:21:45] correct you got
[00:21:49] me it is the length of the shortest
[00:21:52] program which outputs
[00:21:53] X yes
[00:21:57] intuitively you can
[00:21:59] see that this
[00:22:01] compressor is quite
[00:22:03] good because you can prove this theorem
[00:22:06] which is also really easy to prove or
[00:22:09] rather it's really it's easy to feel it
[00:22:12] and once you feel it you could kind of
[00:22:13] believe me that it's easy to prove and
[00:22:15] you can basically say that your korov
[00:22:18] compressor if you use that to compress
[00:22:20] your strings you'll have very low
[00:22:22] regrets about your compression quality
[00:22:26] you can prove this result says that if
[00:22:28] you got your string X your data set
[00:22:31] database
[00:22:33] whatever the shortest program which
[00:22:35] output X is shorter than whatever your
[00:22:38] compressor needed output and however
[00:22:42] well your compressor compressed your
[00:22:43] data plus a little term which is however
[00:22:47] many like characters of Code you need to
[00:22:50] implement your
[00:22:52] compressor intuitively you can see how
[00:22:54] it makes sense simulation argument right
[00:22:57] the simulation argument if you tell me
[00:22:58] hey I've got this really great
[00:22:59] compressor C I'm going to say cool does
[00:23:02] it come with a computer program can you
[00:23:05] give this computer program to K and K is
[00:23:07] going to run your
[00:23:09] compressor because it runs computer
[00:23:11] programs you just need to pay for the
[00:23:12] program length so without giving you the
[00:23:14] details I think I gave you the feel of
[00:23:17] it color of complexity the color of
[00:23:20] compressor can simulate out the computer
[00:23:21] program simulate other compressors this
[00:23:23] is also why it's not computable it's not
[00:23:25] computable because it simulates it feels
[00:23:28] very much at Liberty to simulate all
[00:23:30] computer
[00:23:32] problems but it is the best compressor
[00:23:35] that exists and we were talking about
[00:23:38] Good compression for unsupervised
[00:23:40] learning now let
[00:23:42] us generalize a color of complexity aor
[00:23:46] of compressor to be allowed to use side
[00:23:52] information oh more than detail so I'll
[00:23:56] make this detail I I'll I I'll reader at
[00:23:58] this point several times because this
[00:24:00] point is important obviously the comoro
[00:24:02] compressor is not computable it's
[00:24:06] undecidable but like hey because it's
[00:24:08] like searches overall programs but hey
[00:24:11] did you know that if you run SGD over
[00:24:13] the parameters of some neural net with
[00:24:15] 100 layers it's like automatically like
[00:24:18] doing program search over a computer
[00:24:20] which has a certain amount of memory a
[00:24:21] certain number of steps it's kind of
[00:24:23] like micro micro
[00:24:25] micro hom like fural
[00:24:29] you kind of see the feel the
[00:24:32] similarity it's kind of magical
[00:24:36] right neural networks can simulate
[00:24:38] little programs they are little
[00:24:39] computers they're circuits circuits are
[00:24:41] computers Computing machines and SGD
[00:24:44] searches over the
[00:24:46] program and all of deep learning is
[00:24:50] hinges on top of the SGD miracle that we
[00:24:54] can actually train these computers with
[00:24:57] SGD
[00:24:59] Works actually find those circuits from
[00:25:03] data therefore we can compute our
[00:25:06] miniature color
[00:25:10] compressor and the simulation argument
[00:25:12] applies here as well by the way I just
[00:25:13] want to mention this one fact I don't
[00:25:15] know if you if you ever tried to design
[00:25:16] a better neural network architecture
[00:25:19] what you'd find is that it's kind of
[00:25:21] hard to find a better new architecture
[00:25:24] you say well let's add this connection
[00:25:25] let's add that connection and let's like
[00:25:27] modify this and that why is it hard the
[00:25:29] simulation argument because your new
[00:25:31] architecture can be pretty
[00:25:32] straightforwardly simulated by old
[00:25:34] architecture except when it can't those
[00:25:37] are rare cases and in those rare cases
[00:25:39] you have a big Improvement such as when
[00:25:41] you switch from the little RNN to the
[00:25:42] Transformer the RNN has a bottleneck the
[00:25:46] hidden state so it is a hard time
[00:25:48] implementing the Transformer however had
[00:25:51] we found a way to engineer an our with a
[00:25:54] very very large Hidden State perhaps it
[00:25:56] would become as good as a Transformer
[00:25:59] again so this is the link you start to
[00:26:02] see how we switch from the formal from
[00:26:05] the formal land to neural network land
[00:26:09] but you see the
[00:26:11] similarity so conditional Comm comor
[00:26:14] complexity as the solution to
[00:26:16] unsupervised
[00:26:17] learning you can basically have a
[00:26:21] similar theor similar theorem where I'm
[00:26:23] not going to Define what well I'm going
[00:26:24] to Define what K of Y given X is it's
[00:26:26] like the shortest progress
[00:26:28] which outputs y if it's allowed to probe
[00:26:32] X that's the length of that shortest
[00:26:35] program which outputs y if it allows to
[00:26:37] prob X and you can prove the same result
[00:26:39] and you can see immediately that yeah
[00:26:41] this is definitionally the solution to
[00:26:43] un supervised learning if you use that
[00:26:46] you can sleep very very safely at
[00:26:48] soundly at night knowing that no one
[00:26:51] does on supervised learning better than
[00:26:52] you right it's literally that so this is
[00:26:57] the ultimate low regret solution to
[00:26:59] unsupervised learning except that it's
[00:27:00] not computable but I do think it's a
[00:27:03] useful
[00:27:04] framework and here we condition on a
[00:27:06] data set not an
[00:27:08] example and this thing will extract all
[00:27:10] the value for out of X for predicting y
[00:27:14] the data set the data set not the
[00:27:17] example so this is the solution to un
[00:27:19] supervised L
[00:27:21] done
[00:27:26] success and there is one
[00:27:28] little technicality which I need to
[00:27:30] spend a little bit of time talking about
[00:27:32] which
[00:27:33] is we were talking about this
[00:27:35] conditional comor of complexity right
[00:27:37] where you are talking about compressors
[00:27:40] that get to see try try to compress one
[00:27:43] thing while having access to another
[00:27:44] thing and this is a bit unnatural in a
[00:27:47] machine learning context when you care
[00:27:51] about like fit in big data sets at least
[00:27:56] as of today although it's changing
[00:27:58] fairly rapidly but I think it's still
[00:28:00] fair to say that there is no truly good
[00:28:02] way of conditioning on a big data set
[00:28:05] you can fit a big data set but you can't
[00:28:07] condition on it not yet not
[00:28:09] truly so this result says that hey if
[00:28:13] you care about making predictions about
[00:28:16] your supervis task
[00:28:19] y
[00:28:21] using the the good old fashion color of
[00:28:24] compressor which just compresses the
[00:28:26] concatenation of X and Y is going to be
[00:28:28] just as good as using your conditional
[00:28:31] compressor there are more details and a
[00:28:34] few subtleties to what I just said and
[00:28:37] I'm happy to talk about them offline in
[00:28:39] the event someone is interested in them
[00:28:41] but that basically says that if before
[00:28:44] you're saying hey the previous slide
[00:28:47] said that you can use this conditional
[00:28:49] komogorov compressor to solve on
[00:28:51] supervised
[00:28:52] learning this says that you can also use
[00:28:54] your regular chrom compressor just throw
[00:28:57] all your data take all your files
[00:28:58] concatenate them compress them and
[00:29:00] that's going to make some great
[00:29:01] predictions on your supervis task the
[00:29:03] task that you care
[00:29:05] about there are some intuitions about
[00:29:08] why this is true this result is actually
[00:29:09] like proving this is slightly more
[00:29:12] tricky so I want do
[00:29:16] it yeah so the solution to un supervised
[00:29:18] learning just give it all to your comor
[00:29:20] complexity to your comor
[00:29:23] compressor
[00:29:25] okay and the final thing is I'll mention
[00:29:28] that this kind of joint compression is
[00:29:31] maximum likelihood if you don't overfit
[00:29:33] if you have a data set then the sum of
[00:29:36] the likelihood given your parameters is
[00:29:39] the cost of compressing the data set you
[00:29:41] also need the cost to pay the cost of
[00:29:42] compressing the parameters but you can
[00:29:44] kind of see if you now want to compress
[00:29:45] two data sets no problem just add more
[00:29:48] points to your training set to your data
[00:29:50] set and add the terms to your to the
[00:29:52] sum so this concatenation this joint
[00:29:55] compression is very natural in a machine
[00:29:57] learning context which is why it was
[00:29:59] worth the hassle of saying yeah like we
[00:30:01] have our conditional comor complexity
[00:30:04] and then I made some arguments I made
[00:30:06] some claim without fully defending it
[00:30:08] but it is possible to defend it that
[00:30:11] using regular just compress everything
[00:30:14] color complexity works also and so I
[00:30:16] think this is this is elegant I like it
[00:30:20] because then it says well okay you you
[00:30:23] if you squint hard enough you can say
[00:30:24] that this explains what our neural
[00:30:26] networks doing you can say hey SGD over
[00:30:29] big neural networks is our big program
[00:30:31] program search bigger neural networks
[00:30:33] approximate the color compressor more
[00:30:35] and more and better and better and so
[00:30:38] maybe this is also why we like big
[00:30:39] neural Nets because we approach the
[00:30:42] unapproachable idea of the color
[00:30:44] compressor which truly has no regret and
[00:30:46] we just want to have less and less
[00:30:48] regret as we train larger and larger as
[00:30:50] as we train larger and larger neural
[00:30:52] Nets as far as extracting predictive
[00:30:55] value is concerned
[00:30:59] now the way this applies to the GPT
[00:31:02] models you know I claim that it applies
[00:31:04] to the GPT models also this this Theory
[00:31:07] but the thing that's a little bit tricky
[00:31:09] with the GPT models is that the theory
[00:31:12] of their behavior can also be explain
[00:31:14] without making any references to
[00:31:18] compression or supervised you just say
[00:31:19] no it's just the conditional
[00:31:20] distribution of text on the internet if
[00:31:23] you should learning just imagine a
[00:31:24] document with some repeating patterns
[00:31:26] the pattern is probably going to
[00:31:27] continue
[00:31:28] so the GPT models can intuitively be
[00:31:31] explained at least their few shot
[00:31:34] Behavior can definitely be explained
[00:31:37] without alluding to this Theory and
[00:31:41] so thought I thought it would be nice
[00:31:43] can we find some other direct validation
[00:31:46] of this
[00:31:49] Theory now can we find a different
[00:31:52] domain like Vision like because Vision
[00:31:54] you have pixels
[00:31:58] can you show that doing this on pixels
[00:32:00] will lead to good unsupervised
[00:32:03] Le the answer is yes you can this is
[00:32:07] work we've done in
[00:32:09] 2020 which is called the igp and it's an
[00:32:12] expensive proof of concept it's not
[00:32:14] meant to be it was not meant to be a
[00:32:16] practical procedure it meant to be a
[00:32:18] paper that showed that if you have
[00:32:20] really good Next Step predictor you're
[00:32:21] going to do great and supervised D and
[00:32:23] it was proved in the image domain image
[00:32:25] domain and there I'll just spell it out
[00:32:28] you have
[00:32:29] your
[00:32:31] image you turn it into a sequence of
[00:32:34] pixels each pixel should be given some
[00:32:36] discrete value of
[00:32:38] intensity and then just the next pixel
[00:32:42] prediction with the same
[00:32:44] Transformer that's it different from
[00:32:46] bird just next token prediction because
[00:32:49] this maximizes the likelihood there for
[00:32:55] compresses and like we see one immediate
[00:32:58] result we see this is um these are
[00:33:01] results on on so these are results on C4
[00:33:03] 10 you have models of different sizes
[00:33:04] this is their next step prediction
[00:33:06] accuracy on their pixel prediction task
[00:33:09] on their unsupervised learning task and
[00:33:11] this is linear probe accuracy linear
[00:33:13] probe when you pick some layer inside
[00:33:14] your neural net the best layer fit a
[00:33:17] linear classifier and see how well it
[00:33:18] does you got these nice looking curves
[00:33:20] and they start to get more and more
[00:33:21] similar it's kind of what you want it's
[00:33:24] like it's working pixel prediction
[00:33:28] of the same variety as next word
[00:33:30] prediction next not just pixel Not Mere
[00:33:33] pixel prediction but next pixel
[00:33:36] prediction leads to
[00:33:39] better leads to better and better un
[00:33:41] supervised
[00:33:43] learning I thought it was pretty cool
[00:33:45] and we tried it we scaled it up to
[00:33:47] various degrees and we showed that
[00:33:50] indeed it
[00:33:52] learns reasonably well where we came
[00:33:55] close but we didn't like fully match the
[00:33:57] gap between our and supervised learning
[00:33:59] and the best on supervis learning of the
[00:34:00] day on imet but it was clearly a m it
[00:34:04] did feel like it scaled and it was a
[00:34:05] matter of compute was like you know
[00:34:08] these these things use large high
[00:34:09] resolution images and we use like tiny
[00:34:11] 64x 64 images with giant transformers
[00:34:15] for the day tiny by today standards but
[00:34:17] giant for the day six billion
[00:34:21] parameters so this like yeah you do your
[00:34:23] unsupervised next pixel prediction on a
[00:34:25] big image data set and you fit your
[00:34:28] linear Probe on image net and you get
[00:34:30] strong results like okay that is that is
[00:34:34] cool C far yeah like we got one of the
[00:34:37] cool things if you got 99% on Carr 10
[00:34:40] with this that was
[00:34:43] cool I was I was that you know 2020 was
[00:34:46] a different time but it was cool I'll
[00:34:51] mention I'll close with a couple of
[00:34:53] comments on linear
[00:34:56] representations you know know the the
[00:34:58] thing look I I like the compression
[00:35:00] Theory because I feel like it just
[00:35:02] bothered me for a long time that you
[00:35:04] couldn't think rigorously about
[00:35:06] unsupervised learning I claim now you
[00:35:07] can at least to some partial degree
[00:35:10] still lots of waving of hands is needed
[00:35:12] but maybe a bit less than before but it
[00:35:15] doesn't say why your representations
[00:35:17] should be linearly separable it doesn't
[00:35:18] say what linear prop should happen
[00:35:21] linear linear representations happen all
[00:35:23] the time and the reason for their
[00:35:26] information must be deep and found and I
[00:35:28] think we might be able to crisply
[00:35:30] articulate it at some
[00:35:32] point one thing which I thought was
[00:35:34] interesting is that AO these next pixel
[00:35:37] prediction Model Auto regressive model
[00:35:39] seem to have better linear
[00:35:40] representations than birt and like the
[00:35:42] blue the blue accuracy is Bird versus
[00:35:45] autoaggressive I'm not sure why that is
[00:35:48] or rather I can speculate have some
[00:35:50] speculations but it would be nice to I
[00:35:54] think it would be nice to get gain more
[00:35:55] understanding for why like really really
[00:35:57] why those linear representations are
[00:36:00] formed and yeah this is the end thank
[00:36:04] you for your
[00:36:06] [Applause]
[00:36:11] attention could you provide the
[00:36:13] speculation yeah oh yeah yeah I think
[00:36:16] the speculation is basically that if
[00:36:18] you're doing next pixel prediction
[00:36:20] you're predicting an next pixel from all
[00:36:22] the previous pixels so you need to look
[00:36:24] at the long range structure but in b
[00:36:28] you have your vector and let's say you
[00:36:30] drop 25% of the tokens of the pixels in
[00:36:34] this case then any prediction that you
[00:36:37] have can actually be done quite well by
[00:36:39] looking a little bit into the past and a
[00:36:40] little bit into the future so you remove
[00:36:43] you remove all the hard prediction tasks
[00:36:46] or you make them much easier the hardest
[00:36:48] prediction task in the next pixel
[00:36:49] prediction is a lot harder than the
[00:36:51] hardest prediction task in the birth
[00:36:53] prediction case so this is an argument
[00:36:56] you know we may be if be able to test it
[00:36:59] if we think a little if we if you try to
[00:37:02] design an experiment to test it but uh
[00:37:04] yeah that's a
[00:37:06] speculation is there more robust 2D
[00:37:09] version of next next pixel
[00:37:14] pred I would say more
[00:37:18] robust I would say
[00:37:21] any form any anything you do at all that
[00:37:26] turns a neural n Network into a
[00:37:28] probabilistic model that assigns
[00:37:31] probabilities to different inputs is
[00:37:33] that so the other big way of
[00:37:37] doing next next token prediction is
[00:37:40] diffusion models diffusion models also
[00:37:43] like not the ones that are so the the
[00:37:46] diffusion models that people use in like
[00:37:49] high quality image generators don't
[00:37:51] really maximize the likelihood of their
[00:37:53] inputs they they have a different
[00:37:54] objective but the most original
[00:37:57] formulation
[00:37:58] is maximizing likelihood and by the way
[00:38:01] the diffusion model is a counterargument
[00:38:03] to my to well rather the diffusion
[00:38:07] model also I would claim should have
[00:38:10] worse
[00:38:11] representations than an next toen
[00:38:13] prediction model for for the same reason
[00:38:16] that bird doesn't so I feel so this
[00:38:18] further in my mind increases the mystery
[00:38:21] of what cause leads to linear
[00:38:23] representations to form
[00:38:27] uh yeah thanks for the talk I like the
[00:38:30] analogy between chog complexity and uh
[00:38:34] and neural networks I guess one kind of
[00:38:37] place where it seems like there's a dis
[00:38:38] analogy is that neural networks have
[00:38:40] training Dynamics and you know if you do
[00:38:42] something like just take
[00:38:48] all complexity like the order of the
[00:38:51] data doesn't matter it clearly does for
[00:38:53] neuron Nets you know you have like
[00:38:56] simple heuristic and features that are
[00:38:58] learned early in training that probably
[00:38:59] stick around late in training um and so
[00:39:04] I guess you have thoughts on how to
[00:39:06] think about that in the context of this
[00:39:08] picture yeah I mean the analogy isn't
[00:39:12] perfect that is true and the way in
[00:39:14] which you describe it in like the place
[00:39:16] where the analogy breaks down the most
[00:39:18] is in the search procedure right this is
[00:39:20] really what you're alluding to like hey
[00:39:21] like order of data matters why because
[00:39:24] we using a vak search procedure
[00:39:28] comor compressor uses the infinitely
[00:39:31] expensive search procedure of just
[00:39:32] enumerate everything from scratch each
[00:39:35] time so yeah I mean it is I
[00:39:53] mean I would say
[00:39:59] that caution should be used with this
[00:40:00] particular analogy it's not it's very
[00:40:03] clearly not universally
[00:40:05] applicable but I do think that in the CA
[00:40:07] in I do think that there is some value
[00:40:09] here in explaining where unsupervised
[00:40:12] learning comes
[00:40:18] fromal going back and forth into
[00:40:21] compression and next prediction
[00:40:24] you connecting that
[00:40:28] unsupervised learning supervised
[00:40:29] learning so if you sort of backtrack
[00:40:31] from crypto cryptography there sort of
[00:40:34] uh Theory goes back to the 80s where
[00:40:36] they talk about compression being
[00:40:38] equivalent to next prediction being
[00:40:40] equivalent to being able to distinguish
[00:40:42] into distribution so if you
[00:40:46] have that can predict then you have an
[00:40:48] Alm that can I mean phography is the
[00:40:52] other right you're saying there is no
[00:40:53] way to compress
[00:41:01] so I wonder if this idea of being able
[00:41:03] to distinguish how could that trans
[00:41:06] would that translate anything
[00:41:09] natural
[00:41:13] so I think I understand I think I
[00:41:15] understand the question I think I let me
[00:41:16] paraphrase I'm not I'm not super well
[00:41:18] versed in the area that you that you
[00:41:21] mentioned but you're saying if you can
[00:41:23] distinguish to distribution you can use
[00:41:25] that distinguish ability to make some to
[00:41:27] predict and I guess the question would
[00:41:30] be what's the ex like I have some
[00:41:35] samples from one you have samples from
[00:41:36] the other you can
[00:41:38] tell and so I guess my question is how
[00:41:40] well can you predict well you're talking
[00:41:42] about you can predict a little bit is
[00:41:44] that what
[00:41:45] you you can you can predict what the
[00:41:47] next bit would be let's say for
[00:41:51] example so
[00:42:02] yeah I mean I can mention one thing that
[00:42:05] is related which is energy based models
[00:42:08] so energy based models offer yet another
[00:42:11] way of turning neural networks into
[00:42:13] probability
[00:42:15] distributions where energy an energy
[00:42:17] based model will say just give give me
[00:42:19] your configuration of vectors and I'm
[00:42:21] just going to tell you how like how it
[00:42:24] feels and then you normalize overall of
[00:42:26] them and feel like when it comes to
[00:42:27] energy based models in
[00:42:30] particular ratio like ratios of
[00:42:33] distributions correspond to differences
[00:42:35] of energy maybe there is some relation
[00:42:37] to what you're saying I think I'm
[00:42:39] probably not like precisely commenting
[00:42:41] on the thing that you said but I don't
[00:42:42] think I I have anything more to add
[00:42:49] unfortunately oh yeah maybe I'll just
[00:42:51] put in a tiny word to defend the honor
[00:42:54] of VC
[00:42:55] Dimension well so I mean in 2007 I had
[00:42:58] this theorem about pack learning of
[00:43:00] quantum States right and this was
[00:43:03] precisely an example where even if you
[00:43:05] don't care about infinite Precision even
[00:43:07] if you discretize the state space like
[00:43:09] you look at the VC Dimension or the fat
[00:43:11] chattering Dimension or whatever and it
[00:43:13] is exponentially smaller than the log of
[00:43:16] the size of the hypothesis class so I do
[00:43:19] think there are cases where you still
[00:43:20] want DC
[00:43:22] diens that is a cool example
[00:43:27] um so uh I didn't completely follow your
[00:43:32] uh notation capital x was a sample from
[00:43:35] a distribution the distribution the data
[00:43:37] set so then the
[00:43:41] Transformer SGD I'm not sure if you can
[00:43:44] think of it as the best program for
[00:43:47] compress maybe because it's only given
[00:43:50] one sample at a time that's true there
[00:43:51] is one other assumption that we are
[00:43:53] making so
[00:43:55] the if you
[00:43:58] if you look at the if you look at the
[00:44:00] total training loss say you have some
[00:44:03] neural network doesn't need to be
[00:44:04] Transformer some neural network which
[00:44:06] assigns log probabilities to your data
[00:44:09] and you have some large number of
[00:44:11] training
[00:44:13] cases you can run the neural net and you
[00:44:15] have some some neural network you can
[00:44:16] compute it log probability on each case
[00:44:19] and you can take their sum and that's
[00:44:21] going to be the log probability that the
[00:44:22] neural network assigns to the entire tra
[00:44:25] data set now the neural network is UN
[00:44:28] this particular formulation makes the
[00:44:30] neural network unable to explicitly
[00:44:33] notice like maybe temporal cor any kind
[00:44:36] of structure in the order of the data
[00:44:39] but in but I but I still claim it's
[00:44:41] meaningful to say that yeah like okay
[00:44:43] you can compute the entire log
[00:44:44] probability of the data set and that
[00:44:46] gives you
[00:44:48] your negative log probability literally
[00:44:51] the the the the number of bits you need
[00:44:54] to compress this data set relative to
[00:44:56] using this Network as a
[00:45:04] compressor parras I think uh you you're
[00:45:07] arguing for compression as a framework
[00:45:10] for understanding or motivating
[00:45:11] unsupervised learning and a point you
[00:45:14] made at the end was that if you apply
[00:45:16] that framework to language models to
[00:45:18] next word prediction it can feel a
[00:45:21] little maybe superficial because next
[00:45:23] word prediction you know any text task
[00:45:26] can be ConEd to next word prediction and
[00:45:28] so unsupervised learning is kind of
[00:45:31] superficially the same as supervised
[00:45:32] learning for text so then we turn to
[00:45:34] image GPT where you can't formulate any
[00:45:37] as next pixel prediction maybe you could
[00:45:39] but let's just say you can't but then
[00:45:41] you can use the linear representation as
[00:45:43] a way of showing that compression is a
[00:45:44] good way to formulate unsupervised
[00:45:46] learning but
[00:45:48] then there are highly effective
[00:45:51] compressors that wouldn't give you a
[00:45:52] useful linear representation so I'm
[00:45:54] wondering are there any cases where
[00:45:57] unsupervised learning and supervised
[00:45:59] learning are not superficially the
[00:46:01] same but that you wouldn't you don't
[00:46:03] require your compressor to give you an
[00:46:05] effective linear representation to show
[00:46:07] that compression is a good unsupervised
[00:46:09] objective yes so that's a
[00:46:13] very that I I have I have thoughts on
[00:46:16] this
[00:46:17] question so first of all I will say that
[00:46:20] the linear
[00:46:21] representation good linear
[00:46:23] representation is a bonus at no point
[00:46:26] does this argument say and therefore
[00:46:29] linear representations should emerge
[00:46:31] however I would argue that the theory
[00:46:33] does say that good fine tuning should
[00:46:36] emerge because joint compression is kind
[00:46:38] of like hacky approximate fine tuning
[00:46:41] using the bad search algorithm which is
[00:46:43] SGD now we know
[00:46:46] that the evidence from from these old
[00:46:49] experiments suggests that Bert learns
[00:46:52] worse linear representations than next
[00:46:55] pixel prediction when run on
[00:46:58] images and perhaps the same is true for
[00:47:00] diffusion models that seems highly
[00:47:01] likely I think it'll be very interesting
[00:47:03] to see how the fine diffusion models
[00:47:07] compare maybe someone knows already
[00:47:16] here so I wonder if you can take your
[00:47:19] ideas for unsupervised learning and
[00:47:21] bring them back it seems to me that
[00:47:22] there could be some insights you could
[00:47:23] take back supervised learning learning
[00:47:26] does
[00:47:32] well I think here this gives you more
[00:47:34] like a insight into the so the
[00:47:37] particular Insight you might get here is
[00:47:38] insight into the function class desired
[00:47:41] function class like you want your NE to
[00:47:42] have many layers for example right if
[00:47:45] you have many layers it can do more
[00:47:47] thinking you want those layers to be
[00:47:48] wider bigger you know bigger neural Nets
[00:47:51] I mean essentially this is like what's
[00:47:52] what the field already discovered you
[00:47:54] might not need uh more examples
[00:48:03] number like that's right so this might
[00:48:05] for example be like so there is a so so
[00:48:08] the weakness of this Theory by the way
[00:48:09] this theory is a huge practical weakness
[00:48:11] which is it ignores compute cost it only
[00:48:13] focuses on information so like you all
[00:48:16] familiar with the universal Transformer
[00:48:18] maybe it's like basically it's like it's
[00:48:20] a Transformer Ed the same weights at
[00:48:22] each
[00:48:23] layer it's a great idea except that if
[00:48:26] you have a lot of parameters you need to
[00:48:28] pay for it a lot with compute nobody
[00:48:30] wants to do that it's you you don't
[00:48:33] ignore compute cost this ignores compute
[00:48:35] cost if you ignore compute cost it gives
[00:48:39] you a recipe of how to
[00:48:44] proceed what do you think the importance
[00:48:46] is of the autor regressive modeling in
[00:48:49] particular of the probability
[00:48:51] distribution like you can view bird as
[00:48:53] sort of kind of doing maximum training
[00:48:55] right
[00:48:57] I think you can find ways to sample out
[00:48:59] a for
[00:49:01] example so certainly diffusion models
[00:49:05] can be set up to be maximum likelihood
[00:49:08] models and so all this theory predicts
[00:49:11] that diffusion models should also be it
[00:49:14] should be possible to make diffusion
[00:49:16] models to do equally great things
[00:49:17] perhaps with some constant factors of
[00:49:20] because this you this is like as the
[00:49:22] earlier answer this is not a a compute
[00:49:26] sensitive Theory so it's going to say
[00:49:27] okay like maybe you need like a factor
[00:49:29] of 10 or 15 compute and then things will
[00:49:31] be the same between the auto regressive
[00:49:33] and diffusion model the auto aggressive
[00:49:35] model has it's just simple it's
[00:49:37] convenient maybe the energy based model
[00:49:39] you'll do even greater things but from
[00:49:42] that perspective they're all the
[00:49:45] same it seems like a gp4 may be the best
[00:49:50] compressor uh at the moment which
[00:49:53] presumably is the largest model out
[00:49:55] there as well so so uh on one hand it's
[00:49:58] able to compress the better on the other
[00:50:00] hand the size of the compressor itself
[00:50:03] is
[00:50:04] increasing uh or is it that it's
[00:50:06] actually not necessarily the case from
[00:50:09] the perspective of the
[00:50:11] theory uh complexity well I mean what
[00:50:14] matters is that the cost of
[00:50:17] the
[00:50:23] like what you really what you really
[00:50:25] want is for
[00:50:32] the like there is there is another place
[00:50:36] in way in which this Theory doesn't
[00:50:38] quite correspond to reality because this
[00:50:40] Theory says okay fixed data set you want
[00:50:42] to compress but in the way we train the
[00:50:45] GPT models you say okay you have big
[00:50:47] training set and you have like test set
[00:50:49] which is assumed to be infinite if the
[00:50:52] test set is infinite and you care about
[00:50:54] compressing the test set then you don't
[00:50:55] care about this size of your compressor
[00:50:58] so long as this test set size is much
[00:51:00] larger so I would say that this is also
[00:51:03] like I would say a dis analogy where
[00:51:05] some more careful thinking could be
[00:51:08] useful to get
[00:51:10] clarity you enough to use a validation
[00:51:13] set that's independent as long as it's
[00:51:14] separate that kind of closes the
[00:51:18] Gap is it enough it's it's a good thing
[00:51:21] it's a good thing to do is it truly like
[00:51:23] the thing is
[00:51:28] I think I think it's it's
[00:51:31] also well actually like in the single
[00:51:33] EPO case right if you are in a single
[00:51:35] EPO case then you can just like you know
[00:51:37] compute your log probes as you train and
[00:51:39] that will be something like your the
[00:51:41] models compression of the data set and
[00:51:44] that gives you also a good estimate of
[00:51:45] the validation set so in the single Lio
[00:51:47] case I think things are quite
[00:51:51] similar just wanted to uh make you aware
[00:51:54] that there was a paper last month in
[00:51:55] finding
[00:51:58] Follow
[00:52:06] by compress strings just like you show
[00:52:09] concate two strings
[00:52:15] togethering
[00:52:20] the yeah my only comment on that is that
[00:52:23] jzip is not a very strong compressor of
[00:52:25] text so I think like it it does it does
[00:52:29] show that things are possible to some
[00:52:31] degree but like all the really meaty
[00:52:34] stuff happens when you like squeeze the
[00:52:35] last bits if you see what I mean it
[00:52:38] seems like it works like
[00:52:43] ay I
[00:52:46] think doesn't
[00:52:51] work since Jacob brought up curriculum
[00:52:54] effects and you know how they appear for
[00:52:57] neural Nets but not for you know you
[00:52:59] don't see it but a commor of complexity
[00:53:01] um you know we were just talking at
[00:53:03] lunch about like what is the current
[00:53:05] empirical situation about like how much
[00:53:07] do curriculum effects actually matter
[00:53:10] and none of us knew the
[00:53:11] answer well it's
[00:53:19] like so it's a bit you know I I have a
[00:53:22] take on this which
[00:53:24] is the easier
[00:53:27] so we've done so we've done a lot of
[00:53:28] work as a field to make the Transformer
[00:53:32] like the architectures that we are using
[00:53:34] to be relatively easy to optimize we
[00:53:35] found good initializations we found good
[00:53:38] hyperparameters we made changes to the
[00:53:40] architecture so that training is as easy
[00:53:43] as possible the easier is the the more
[00:53:48] easy the training optimization problem
[00:53:50] is the less susceptible you are to
[00:53:53] curriculum
[00:53:54] effects and like it's known like for
[00:53:56] example people who were training all
[00:53:58] kinds of exotic architectures like
[00:53:59] neural touring machines for example
[00:54:02] which are like these really complicated
[00:54:05] things and it's super super huge numbers
[00:54:08] of heterogeneous layers which are
[00:54:11] different and that thing you need to be
[00:54:13] very very careful with your curriculum
[00:54:15] because if you give it the full data set
[00:54:16] right away it'll just
[00:54:21] fail right um let thank again
[00:54:40] isn't
[00:54:57] I mean
[00:55:26] and I guess you know
[00:56:06] [Music]
[00:56:25] light that's
[00:57:20] I
