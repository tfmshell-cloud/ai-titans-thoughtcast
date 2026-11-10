# NVIDIA GTC Fireside Chat: Ilya Sutskever & Jensen Huang (March 2023)
- **YouTube URL:** https://www.youtube.com/watch?v=I6qQinoY9WM
- **Lines:** 1214

---

[00:00:04] Ilia
[00:00:05] unbelievable today is the day after
[00:00:09] gp4 it's great to have you here um I'm
[00:00:13] delighted to have you I've known you a
[00:00:14] long time the journey and just my mental
[00:00:18] H my my mental memory of your of the
[00:00:21] time that I've known you and the seminal
[00:00:24] work that you have done starting in univ
[00:00:27] University of Toronto the
[00:00:30] co-invention of Alex net uh with Alex
[00:00:34] and Jeff Hinton uh that led to the Big
[00:00:38] Bang of modern artificial intelligence
[00:00:41] uh your career that took you out here to
[00:00:43] the Bay Area the founding of open AI GPT
[00:00:49] 123 and then of course chat GPT the AI
[00:00:53] heard around the world this is this is
[00:00:57] the incredible resume of a young
[00:00:59] computer scientist
[00:01:00] um you know an entire community and
[00:01:03] Industry at all with your achievements I
[00:01:06] I guess my I just want to go back to the
[00:01:08] beginning and ask you deep
[00:01:11] learning what was your intuition around
[00:01:13] deep learning why did you know that it
[00:01:16] was going to work uh did you have any
[00:01:18] intuition that it was going to lead to
[00:01:19] this kind of
[00:01:20] success okay well first of all thank you
[00:01:24] so much for the qual for all the kind
[00:01:26] words a lot has changed thanks to the
[00:01:31] incredible power of deep
[00:01:33] learning like I think this my personal
[00:01:36] starting point I was interested in
[00:01:38] artificial intelligence for a whole
[00:01:41] variety of
[00:01:42] reasons starting
[00:01:44] from an intuitive understanding of
[00:01:47] appreciation of its impact and also I
[00:01:50] had a lot of curiosity about what is
[00:01:52] consciousness what is The Human
[00:01:54] Experience and it felt like progress in
[00:01:57] artificial intelligence will help with
[00:01:58] that
[00:02:00] The Next Step was well back then I was
[00:02:03] starting in 2002 2003 and it seemed like
[00:02:07] learning is the thing that humans can do
[00:02:09] that people can do that computers can't
[00:02:12] do at all in 2003 2002 computers could
[00:02:18] not learn
[00:02:19] anything and it wasn't even clear that
[00:02:22] it was possible in theory and so I
[00:02:25] thought that making
[00:02:28] progress in learning
[00:02:30] in artificial learning in machine
[00:02:32] learning that would lead to the greatest
[00:02:34] progress in
[00:02:35] Ai and then I started to look around for
[00:02:38] what was out there and nothing seemed
[00:02:41] too
[00:02:42] promising but to my great luck Jeff
[00:02:45] Hinton was a professor at my
[00:02:47] University and I was able to find him
[00:02:50] and he was working in neural networks
[00:02:52] and it immediately made sense because
[00:02:54] neural networks had the property that we
[00:02:57] are learning we are a automatically
[00:03:00] programming parallel computers back then
[00:03:03] the parallel computers were small but
[00:03:06] the promise was if you could somehow
[00:03:07] figure out how learning in neural
[00:03:09] networks work then you can program small
[00:03:12] parallel computers from data and it was
[00:03:15] also similar enough to the brain and the
[00:03:16] brain works so it's like you had these
[00:03:19] several factors going for it now it
[00:03:21] wasn't clear how to get it to
[00:03:24] work but of all the things that existed
[00:03:28] that seemed like it had by far the
[00:03:30] greatest long-term promise even though
[00:03:32] you know at the time that you first
[00:03:33] started at the time that you first
[00:03:35] started working with deep learning and
[00:03:36] and uh neuron networks what was what was
[00:03:39] the scale of the network what was the
[00:03:40] scale of computing at that moment in
[00:03:42] time what was it like an interesting
[00:03:44] thing to note is that the importance of
[00:03:46] scale wasn't realized back then mhm so
[00:03:49] people would just train you know neural
[00:03:50] networks with like 50 neurons 100
[00:03:52] neurons several hundred neurons that
[00:03:55] would be like a big neural network a
[00:03:58] million parameters would be considered
[00:04:00] very large we we would run our models on
[00:04:03] unoptimized CPU code because we were a
[00:04:06] bunch of researchers we didn't know
[00:04:07] about blast we used mat lab the mat lab
[00:04:10] was
[00:04:12] optimized and we just experiment like
[00:04:15] what is the what is even the right
[00:04:16] question to ask you know so you try to
[00:04:18] to gather to just find interesting
[00:04:21] phenomena interesting
[00:04:23] observation you can do this small thing
[00:04:26] and you can do that small thing you know
[00:04:27] Jeff Hinton was really excited
[00:04:30] about training neural Nets on small
[00:04:33] little digits both for classification
[00:04:36] and also he was very interested in
[00:04:38] generating them so the beginnings of
[00:04:40] generative models were right there but
[00:04:43] the question is like okay so you got all
[00:04:44] this cool stuff floating around what
[00:04:47] really gets traction and so that it
[00:04:50] wasn't so it wasn't obvious that this
[00:04:52] was the right
[00:04:53] question back then but in hindsight that
[00:04:56] turned out to be the right question now
[00:04:58] now the the here alexnet was 2012 yes
[00:05:03] 2012 now you and Alex were working on
[00:05:07] Alex net for some time before
[00:05:09] then and and uh at what point at what
[00:05:14] point was it was it clear to you that
[00:05:16] you wanted to uh build a computer vision
[00:05:19] oriented neuron Network that imag net
[00:05:22] was the right set of data to go for and
[00:05:24] to somehow go for the computer V
[00:05:28] computer vision contest
[00:05:30] yeah so I can talk about the context
[00:05:33] there it I think
[00:05:36] probably two years before that it became
[00:05:40] clear to
[00:05:41] me that supervised learning is what's
[00:05:44] going to get us the traction and I can
[00:05:47] explain precisely why it wasn't just an
[00:05:50] intuition it was I would argue an
[00:05:53] irrefutable argument which went like
[00:05:55] this if your neural network is deep and
[00:06:01] large then it could be configured to
[00:06:04] solve a hard task so that's the keyword
[00:06:08] deep and large people weren't looking at
[00:06:11] large neural networks people were you
[00:06:13] know maybe studying a little bit of
[00:06:14] depth in neural networks but most of the
[00:06:16] machine learning field wasn't even
[00:06:17] looking at neural networks at all they
[00:06:19] were looking at all kinds of basian
[00:06:21] models and kernel methods which are
[00:06:24] theoretically elegant methods which have
[00:06:26] the property that they actually can't
[00:06:29] represent a good solution no matter how
[00:06:31] you configure them whereas the large and
[00:06:33] deep neural network can represent a good
[00:06:36] solution to the problem to find a good
[00:06:40] solution you need a big data set which
[00:06:42] requires it mhm and a lot of computer to
[00:06:46] actually do the work we've also made
[00:06:48] Advan work so we've worked on
[00:06:50] optimization for for a little bit it was
[00:06:53] clear that optimization is a bottleneck
[00:06:56] and there was a breakthrough by another
[00:06:58] grad student in Jeff lab called James
[00:07:01] Martin and he came up with an
[00:07:02] optimization method which is different
[00:07:04] from the one we're doing now using now
[00:07:06] some second order method but the point
[00:07:09] about it is that it's proved that we can
[00:07:11] train those neural networks because
[00:07:13] before we didn't even know we could
[00:07:14] train them so if you can train them you
[00:07:17] make it big you find the data and you
[00:07:19] will succeed so then the next question
[00:07:21] is well what data and an imag data set
[00:07:25] back then it seemed like this
[00:07:26] unbelievably difficult data set but it
[00:07:29] was clear that if you were to train a
[00:07:32] large convolutional neural network on
[00:07:33] this data set it must succeed if it just
[00:07:36] can have the compute and right that
[00:07:38] right at that time gpus came out you and
[00:07:40] I you and I our history and our paths
[00:07:45] intersected and somehow you had the the
[00:07:49] the the observations that a GPU and at
[00:07:52] that time we had this is our couple of
[00:07:53] generations into a Cuda GPU and I think
[00:07:56] it was GTX 580 uh generation
[00:07:59] you had the you had the uh Insight that
[00:08:02] the GPU could actually be useful for
[00:08:04] training your neural network models what
[00:08:06] what was that how did that day start
[00:08:08] tell me you know you and I you never
[00:08:09] told me that moment you know how did
[00:08:11] that day start yeah so you know the the
[00:08:16] GP the
[00:08:17] gpus appeared in our in our lab in our
[00:08:20] Toronto lab thanks to Jeff and he said
[00:08:23] we got we should try these gpus and we
[00:08:24] started trying and experimenting with
[00:08:26] them and it was a of fun but the but it
[00:08:31] was
[00:08:32] unclear what to use them for exactly
[00:08:35] where are you going to get the real
[00:08:37] traction but then with the existence of
[00:08:41] the imet data
[00:08:43] set and then it was also very clear that
[00:08:46] the convolutional neural network is such
[00:08:48] a great fit for the GPU so it should be
[00:08:50] possible to make it go unbelievably fast
[00:08:53] and therefore train something which
[00:08:55] would be completely unprecedented in
[00:08:57] terms of its size
[00:09:01] and that's how it happened and you know
[00:09:03] very fortunately Alex kvki he really
[00:09:06] loved programming the GPU and he and and
[00:09:09] he was able to do it he was able to code
[00:09:12] to to program really fast convolutional
[00:09:18] kernels and and
[00:09:21] then and then train the neural on image
[00:09:23] in a data set and that led to the result
[00:09:26] but it was like it shocked the world it
[00:09:28] shocked the world it it it broke the
[00:09:30] record of computer vision by such a wide
[00:09:33] margin that that it was a clear
[00:09:36] discontinuity yeah yeah and I wouldn't I
[00:09:38] would say it's not just like there is
[00:09:39] another bit of context
[00:09:41] there it's not so much like when when we
[00:09:43] say break the record there is an import
[00:09:45] it's like I think there's a different
[00:09:47] way to phrase it it's that that data set
[00:09:52] was so obviously hard and so obviously
[00:09:55] outside of reach of anything people are
[00:09:58] making progress with some classic
[00:09:59] techniques and they were actually doing
[00:10:01] something but this thing was so much
[00:10:03] better on a data set which was so
[00:10:06] obviously hard it was it's not just that
[00:10:07] it's just some competition it was a
[00:10:10] competition which back in the day it
[00:10:12] wasn't an average Benchmark it was so
[00:10:15] obviously difficult so obviously Out Of
[00:10:18] Reach and so
[00:10:20] obviously with the property that if you
[00:10:22] did a good job that would be amazing big
[00:10:25] bang of AI fast forward to now uh you
[00:10:28] came out to the Valley you started open
[00:10:30] AI with some friends um you're the chief
[00:10:34] scientist now what was the first initial
[00:10:37] idea about what to work on at openai
[00:10:40] because you guys worked on several
[00:10:41] things some of the trails of of
[00:10:43] inventions and and work uh you could you
[00:10:47] could see led up to the chat GPT moment
[00:10:52] um but what were the initial inspiration
[00:10:55] what would you go how would you approach
[00:10:57] intelligence from that moment and led to
[00:11:01] this yeah so obviously when we started
[00:11:06] it
[00:11:08] wasn't 100% clear how to proceed and the
[00:11:12] field was also very different compared
[00:11:15] to the way it is right now so right now
[00:11:17] you already used we already used
[00:11:20] to you have these amazing artifacts
[00:11:23] these amazing neural Nets who are doing
[00:11:25] incredible things and everyone is so
[00:11:28] excited but back in 2015 2016 early 2016
[00:11:33] when we were starting
[00:11:34] out the whole thing seemed pretty crazy
[00:11:38] there were so many fewer researchers
[00:11:41] like hund maybe there were between a 100
[00:11:44] and a thousand times fewer people in the
[00:11:46] field compared to now like back then you
[00:11:49] had like 100 people most of them were
[00:11:53] working in Google deepmind and that was
[00:11:56] that then there were people picking up
[00:11:58] the skills but it was very very scars
[00:12:00] very rare
[00:12:02] still and we had
[00:12:05] two big Initial
[00:12:08] Ideas at the start of open AI that stay
[00:12:11] that had a lot of stain power and they
[00:12:13] stayed with us to this day and I'll
[00:12:16] describe them right
[00:12:17] now the first big idea that we had one
[00:12:22] which I was especially excited about
[00:12:25] very early on is the idea
[00:12:30] of unsupervised learning through
[00:12:35] compression some
[00:12:37] context today we take it for granted
[00:12:39] that unsupervised learning is this easy
[00:12:41] thing you just pre-train on everything
[00:12:43] and it all does exactly as you'd
[00:12:45] expect in
[00:12:47] 2016 unsupervised learning was an
[00:12:51] unsolved problem in machine learning
[00:12:54] that no one had any insight exactly any
[00:12:57] clue as to what to do that's right Yan
[00:13:00] lean would go around and give a talk
[00:13:02] give talk saying that you have this
[00:13:04] Grand Challenge on supervised
[00:13:06] learning and I really
[00:13:08] believed that really good compression of
[00:13:12] the data will lead to unsupervised
[00:13:14] learning
[00:13:16] now compression is not language that's
[00:13:18] commonly used to describe what is really
[00:13:21] being done until recently when suddenly
[00:13:25] it became apparent to many people that
[00:13:26] those gpts actually compress the tra
[00:13:29] training data you may recall the Ted
[00:13:32] Chang New York Times article which also
[00:13:33] alluded to this but there is a real
[00:13:36] mathematical sense in which training
[00:13:38] these Auto regressive generative models
[00:13:41] compress the data and intuitively you
[00:13:44] can see why that should work if you
[00:13:47] compress the data really well you must
[00:13:48] extract all the hidden secrets which
[00:13:50] exist in it therefore that is the key so
[00:13:55] that was the first idea that we were
[00:13:56] really excited about and that led to
[00:14:00] quite a few Works in open AI do the
[00:14:03] sentiment
[00:14:04] neuron which I'll
[00:14:07] mention very briefly it is not this work
[00:14:11] might not be well known outside of the
[00:14:14] machine learning field but it was very
[00:14:16] influential especially in our
[00:14:18] thinking this
[00:14:21] work like the the result
[00:14:24] there was that when you train a neural
[00:14:27] network back then it was a Transformer
[00:14:29] it was before the Transformer right
[00:14:31] small recurrent neural network LSD lsdm
[00:14:33] to those remember sequence work you've
[00:14:35] done I mean this some of your some of
[00:14:37] the work that you've done yourself yeah
[00:14:39] so the same lsdm with a few twists train
[00:14:43] to predict the next token in Amazon
[00:14:45] reviews next
[00:14:47] character and we discovered that if you
[00:14:49] predict the next character well enough
[00:14:52] there will be a urine inside that lstm
[00:14:55] that corresponds to its
[00:14:57] sentiment so that was really cool
[00:15:00] because it showed some traction for
[00:15:03] unsupervised learning and it validated
[00:15:06] the idea that really good
[00:15:10] next character prediction next something
[00:15:13] prediction compression yeah has the
[00:15:16] property that it discovers the secrets
[00:15:18] in the data that's what we see with
[00:15:20] these GPT models right you train and
[00:15:22] people say just statistical correlation
[00:15:24] I mean at this point should be so clear
[00:15:25] to anyone observation that observation
[00:15:27] also you know for me intuitively open up
[00:15:30] the whole world of where do I get the
[00:15:32] data for unsupervised learning because I
[00:15:36] do have a whole lot of data if I could
[00:15:38] just make you predict the next character
[00:15:40] and I know what the ground truth is I
[00:15:42] know what the answer is I could be I
[00:15:44] could train a neural network model with
[00:15:46] that so that that observation and
[00:15:48] masking and other other technology other
[00:15:51] approaches you know open open my mind
[00:15:53] about where would the world get all the
[00:15:55] data that's unsupervised for
[00:15:56] unsupervised learning well I think I
[00:15:59] think so I would I would phrase it a
[00:16:01] little
[00:16:02] differently I would say that with
[00:16:04] unsupervised learning the hard part has
[00:16:06] been less
[00:16:08] around where you get the data from
[00:16:11] though that part is there as well
[00:16:13] especially now MH but it was more about
[00:16:17] why should you do it in the first place
[00:16:20] why should you
[00:16:21] bother the hard part was to realize that
[00:16:26] training these neural Nets to predict
[00:16:28] the next stoken is a worthwhile goal at
[00:16:31] all mhm that was that it would learn a
[00:16:33] representation that it would it would be
[00:16:36] able to understand that's right that it
[00:16:38] will be useful grammar and yeah but to
[00:16:41] actually to but it just wasn't obvious
[00:16:44] MH right so people weren't doing it but
[00:16:46] the sentiment neuron work and you know I
[00:16:48] want to call out Alec Ratford is a
[00:16:50] person who
[00:16:51] really was responsible from any of the
[00:16:54] advances
[00:16:55] there the sentiment this this was this
[00:16:58] was before gpt1 it was the precursor to
[00:17:00] gpt1 and it influenced our thinking a
[00:17:03] lot then the Transformer came out and we
[00:17:06] immediately meant oh my God this is the
[00:17:08] thing and we
[00:17:10] trained we trained
[00:17:12] gpt1 now along the
[00:17:15] way you've always believed that scaling
[00:17:19] um will improve the performance of these
[00:17:21] models yes larger larger networks uh
[00:17:24] deeper networks uh more training data
[00:17:27] would scale that um there was a very
[00:17:29] important uh paper that openai wrote
[00:17:32] about the scaling laws and the
[00:17:34] relationship between um loss and uh the
[00:17:37] size of the model and the the amount of
[00:17:39] data set the size of the data set uh
[00:17:41] when Transformers came out it gave us
[00:17:43] the opportunity to train very very large
[00:17:45] models uh in very reasonable amount of
[00:17:48] time um but with the in with the did the
[00:17:52] intuition about about the scaling laws
[00:17:54] of the size of of of models and data um
[00:17:58] and your journey of gpt1 23 um which
[00:18:02] came first did you see the evidence of
[00:18:04] GPT 1 through3 first or was it the
[00:18:06] intuition about the scaling law first
[00:18:09] the intuition so I would say that the
[00:18:12] way the way I'd phrase it is that I had
[00:18:15] a very strong belief that bigger is
[00:18:19] better and that one of the goals that we
[00:18:23] had at open AI is to figure out how to
[00:18:26] use the scale correctly there was a lot
[00:18:29] of belief about in open AI about scale
[00:18:31] from the very beginning the question is
[00:18:35] what to use it for
[00:18:36] precisely because I'll mention right now
[00:18:38] we talking about the gpts but there's
[00:18:40] another very important line of work
[00:18:41] which I haven't mentioned the second big
[00:18:43] idea but I think now is a good time to
[00:18:45] make a detour and that's reinforcement
[00:18:49] learning that clearly seems important as
[00:18:51] well what do you do with it so the first
[00:18:56] really big project that was done inside
[00:18:58] open
[00:19:00] was our effort at solving a realtime
[00:19:05] strategy game and for context a
[00:19:08] real-time strategy game is like it's a
[00:19:10] competitive sport yeah right where you
[00:19:12] need to be smart you need to have fast
[00:19:15] you need to have a quick reaction time
[00:19:16] you there's
[00:19:17] teamwork and you're competing against
[00:19:19] another team and it's pretty it's pretty
[00:19:22] it's pretty
[00:19:24] involved and there is a whole
[00:19:26] competitive league for that game the
[00:19:27] game is called do too and so we train a
[00:19:30] reinforcement learning agent to play
[00:19:32] against
[00:19:33] itself to
[00:19:37] produce with the goal of reaching a
[00:19:41] level so that it could compete against
[00:19:42] the best players in the world and that
[00:19:45] was a major undertaking as well it was a
[00:19:48] very different line it was reinforcement
[00:19:50] learning yeah remember the day that that
[00:19:51] you guys announced that work and this is
[00:19:54] this by the way when I was asking
[00:19:56] earlier about about there's there's a
[00:19:58] large body work that have come out of
[00:19:59] open AI some of it seem like detours um
[00:20:03] but but in fact as you're as you're
[00:20:04] explaining now they might might have
[00:20:06] been detours it seemingly detours but
[00:20:08] they they really led up to some of the
[00:20:09] important work that we're now talking
[00:20:11] about Chad GPT yeah I mean there has
[00:20:14] been real convergence MH where the
[00:20:17] gpts produce the foundation and in
[00:20:20] reinforcement learning from DOTA morphed
[00:20:24] into reinforcement learning from Human
[00:20:25] feedback that's right and that
[00:20:27] combination gave Chad GPT you know
[00:20:29] there's a there's a there's a a
[00:20:31] misunderstanding that that uh Chad GPT
[00:20:35] is uh in itself just one giant large
[00:20:38] language model there's a system around
[00:20:40] it that's fairly complicated is could
[00:20:42] could you could you explain um briefly
[00:20:45] for the audience the the uh the
[00:20:48] fine-tuning of it the reinforcement
[00:20:50] learning of it the the um uh you know
[00:20:53] the various uh surrounding systems that
[00:20:55] allows you to uh keep it on Rails and
[00:20:58] and and uh let it let it uh uh give it
[00:21:01] knowledge and you know so on so forth
[00:21:04] yeah I can so the way to think about it
[00:21:08] is that when we train a large neural
[00:21:11] network to accurately predict the next
[00:21:15] word in lots of different texts from the
[00:21:18] internet what we are doing is that we
[00:21:21] are learning a world model it looks like
[00:21:24] we are learning this it may it may look
[00:21:27] on the surface that we are just learning
[00:21:30] statistical correlations in
[00:21:32] text but it turns out that to just learn
[00:21:36] the statistical correlations in text to
[00:21:39] compress them really well what the
[00:21:41] neural network learns is some
[00:21:44] representation of the process that
[00:21:46] produced the
[00:21:48] text this text is actually a projection
[00:21:51] of the world there is a world out there
[00:21:54] and it's has a projection on this text
[00:21:57] and so what the neural network is is
[00:21:58] learning is more and more aspects of the
[00:22:02] world of people of the human conditions
[00:22:05] their their their hopes dreams and
[00:22:08] motivations their interactions and the
[00:22:10] situations that we are in and the neural
[00:22:14] network learns a compressed abstract
[00:22:17] usable representation of that this is
[00:22:21] what's being learned from accurately
[00:22:23] predicting the next word and furthermore
[00:22:27] the more accurate you are is predicting
[00:22:28] the next word the higher a Fidelity the
[00:22:33] more resolution you get in this process
[00:22:35] so that's what the pre-training stage
[00:22:38] does but what this does not
[00:22:41] do is specify the desired behavior that
[00:22:45] we wish our neural network to
[00:22:48] exhibit you see a language model what it
[00:22:51] really tries to do is to answer the
[00:22:54] following
[00:22:55] question if I had some random piece of
[00:22:58] text on the internet which starts with
[00:23:01] some prefix some
[00:23:03] prompt what will it complete to if you
[00:23:07] just randomly end up on some text from
[00:23:09] the internet but this is different from
[00:23:12] well I want to have an assistant which
[00:23:14] will be truthful that will be helpful
[00:23:17] that will follow certain gu rules and
[00:23:19] not violate them that requires
[00:23:21] additional training this is where the
[00:23:24] fine-tuning and the reinforcement
[00:23:26] learning from Human teachers and other
[00:23:29] forms of AI assistance it's not just
[00:23:31] reinforcement learning from Human
[00:23:32] teachers it's also reinforcement
[00:23:34] learning from human and AI collaboration
[00:23:37] our teachers are working together with
[00:23:38] an AI to teach our AI to behave but here
[00:23:41] we are not teaching it new knowledge
[00:23:43] this is not what's happening we are
[00:23:45] teaching
[00:23:46] it we are communicating with it we are
[00:23:50] communicating to it what it is that we
[00:23:53] want it to be mhm and this process the
[00:23:56] second stage is also extremely important
[00:23:59] the better we do the second stage the
[00:24:01] more useful the more reliable this
[00:24:04] neural network will be so the second
[00:24:06] stage is extremely important too in
[00:24:08] addition to the first stage of the learn
[00:24:11] everything for learn everything learn as
[00:24:14] much as you can about the world from the
[00:24:16] projection of the world which is text
[00:24:20] now you could tell you could you could
[00:24:21] uh fine tune it you could uh instruct it
[00:24:24] to uh perform certain things can you
[00:24:27] instruct it to not perform certain
[00:24:28] things so that you could give it guard
[00:24:30] rails about avoid these type of behavior
[00:24:33] um you know give it some kind of a
[00:24:34] bounding box so that so that it doesn't
[00:24:37] doesn't wander out of that bounding box
[00:24:39] and and perform things that that are you
[00:24:41] know unsafe or otherwise yeah so this
[00:24:46] second stage of training is indeed where
[00:24:49] we communicate to the neural network
[00:24:52] anything we want which includes the Bing
[00:24:55] box and the better we do this training
[00:24:59] the higher the Fidelity with which we
[00:25:01] communicate this bounding box and so
[00:25:03] with constant research and Innovation on
[00:25:06] improving this
[00:25:08] Fidelity we are able we improve this
[00:25:12] Fidelity and so it becomes more and more
[00:25:15] reliable and precise in the way in which
[00:25:19] it follows the intended intended
[00:25:22] instructions Chad gbt came out just a
[00:25:24] few months ago um fastest growing
[00:25:27] application in the history of
[00:25:31] humanity uh uh lots of lots of uh uh uh
[00:25:36] interpretations about why um but some of
[00:25:39] the some of the things that that uh is
[00:25:41] clear it is it is the easiest
[00:25:44] application that anyone has ever created
[00:25:46] for anyone to use uh it performs tasks
[00:25:51] it performs things it does things that
[00:25:54] are Beyond people's expectation uh
[00:25:57] anyone can use it there are no
[00:25:59] instruction sets there are no wrong ways
[00:26:01] to use it you you just use it and uh if
[00:26:04] it's if your instructions are are
[00:26:07] prompts are ambiguous the conversation
[00:26:10] refines the ambiguity until your intents
[00:26:13] are uh understood by by the uh by the
[00:26:16] application by the AI uh the the um
[00:26:20] impact of course uh clearly remarkable
[00:26:24] now yesterday this is the day after gp4
[00:26:28] just a few uh months later the the
[00:26:32] performance of gp4 uh in many areas
[00:26:35] astounding um SAT scores gr Scores Bar
[00:26:40] exams um the the number of the number of
[00:26:44] uh um tests that it's able to perform at
[00:26:47] at very capable levels very capable
[00:26:49] human levels uh
[00:26:51] astounding what were the what were the
[00:26:53] major differences between Chad GPT and
[00:26:57] GPT 4
[00:26:58] that led to its improvements in these in
[00:27:01] these
[00:27:01] areas so
[00:27:07] gp4 is
[00:27:08] a pretty substantial Improvement on top
[00:27:12] of Chad GPT across very many dimensions
[00:27:16] with train gp4 I would
[00:27:20] say between more than 6 months ago maybe
[00:27:24] eight months ago I don't remember
[00:27:25] exactly
[00:27:28] GPT the first B big difference between
[00:27:31] Chad GPT and
[00:27:33] gp4 and that perhaps is the
[00:27:36] more the most important difference is
[00:27:39] that the base on top of gp4 is built
[00:27:42] predicts the next word with greater
[00:27:45] accuracy this is really
[00:27:48] important because the better a neural
[00:27:51] network can predict the next word in
[00:27:53] text the more it understands it this
[00:27:56] claim is now perhaps a accepted by many
[00:27:59] at this point but it might still not be
[00:28:01] intuitive or not completely intuitive as
[00:28:04] to why there is so I'd like to take a
[00:28:06] small detour and to give an analogy that
[00:28:09] will hopefully clarify why more accurate
[00:28:12] prediction of the next word leads to
[00:28:14] more understanding real
[00:28:17] understanding let's consider an example
[00:28:20] say you read a detective novel it's like
[00:28:23] a complicated plot a storyline different
[00:28:25] characters lots of events
[00:28:28] Mysteries like Clues it's unclear then
[00:28:32] let's say that at the last page of the
[00:28:34] book the detective has gathered all the
[00:28:36] clues gathered all the people and saying
[00:28:38] okay I'm going to reveal the identity of
[00:28:41] whoever committed the crime MH and that
[00:28:44] person's name is predict that word
[00:28:46] predict that word exactly my goodness
[00:28:48] right yeah right now there are many
[00:28:50] different words M but by predicting
[00:28:52] those words better and better and better
[00:28:54] the understanding of the text keeps on
[00:28:58] increasing gbd4 predicts the next word
[00:29:02] better IIA people say that that deep
[00:29:04] learning won't lead to reasoning that
[00:29:07] deep learning won't lead to reasoning
[00:29:10] but in order to predict that next word
[00:29:12] figure out from all of the agents that
[00:29:15] were there and and all of their you know
[00:29:19] strengths or weaknesses or their
[00:29:21] intentions and uh the context um and to
[00:29:25] be able to predict that word who who was
[00:29:28] the murderer that requires some amount
[00:29:31] of reasoning a fair amount of reasoning
[00:29:33] and so so how did the how did the how is
[00:29:36] it that that that it's able to to learn
[00:29:40] reasoning and and if if it learned
[00:29:43] reasoning um you know one of the one of
[00:29:45] the things that I was going to ask you
[00:29:46] is of all the tests that were that were
[00:29:48] taken um between Chad gbt and gbd4 there
[00:29:52] were some tests that gpt3 or chat GPT
[00:29:56] was already very good at there were some
[00:29:58] tests that gbd3 or chat GB was not as
[00:30:02] good at um that gbd4 was much better at
[00:30:06] and there were some tests that neither
[00:30:07] are good at yet I would love for you
[00:30:10] know and some of it has to do with
[00:30:11] reasoning it seems that you know maybe
[00:30:14] in in calculus that that it wasn't able
[00:30:16] to break maybe the problem down um into
[00:30:19] into its reasonable steps and solve it
[00:30:22] is is it but yet in some areas it it
[00:30:25] seems to demonstrate reasoning skills
[00:30:28] and so is that an area that that um uh
[00:30:32] that in predicting the next word you're
[00:30:34] you're learning reasoning and um uh what
[00:30:37] are the limitations uh now of gp4 that
[00:30:41] would enhance his ability to reason even
[00:30:43] even
[00:30:44] further you know reasoning isn't this
[00:30:49] super welldefined
[00:30:51] concept but we can try to Define It
[00:30:54] Anyway which is when you maybe maybe
[00:30:57] when you go
[00:30:58] further where you're able to somehow
[00:31:02] think about it a little bit and get a
[00:31:04] better answer because of your
[00:31:06] reasoning and I'd say I'd say that our
[00:31:10] neural Nets you know maybe there is some
[00:31:13] kind of limitation which could be
[00:31:16] addressed by for example asking the
[00:31:18] neural network to think out loud this
[00:31:20] has proven to be extremely effective for
[00:31:22] reasoning but I think it also remains to
[00:31:24] be seen just how far the basic neural
[00:31:26] network will go I think think we have
[00:31:28] yet to uh tap fully tap out its
[00:31:35] potential but yeah I mean there is
[00:31:38] definitely some sense where reasoning is
[00:31:41] still not quite at that
[00:31:44] level as some of the other capabilities
[00:31:47] of the neural network though we would
[00:31:49] like the reasoning capabilities of the
[00:31:51] neural network to be high mhm
[00:31:55] higher I think that it's fairly likely
[00:31:57] that business as usual will keep will
[00:32:00] improve the reasoning capabilities of
[00:32:01] the neural network I wouldn't I wouldn't
[00:32:05] necessarily confidently rule out this
[00:32:07] possibility mhh yeah because one of the
[00:32:10] things that that that is really cool is
[00:32:12] you ask you ask chb to a question um but
[00:32:16] before it answers the question tell me
[00:32:17] first first of what you know and then
[00:32:19] answer the question um you know usually
[00:32:22] when somebody answers a question if you
[00:32:23] give me the the foundational knowledge
[00:32:26] that you have or the foundational
[00:32:27] assumptions that you're making before
[00:32:28] you answer the question that really
[00:32:31] improves the my believability of of the
[00:32:34] answer um you're also demonstrating some
[00:32:36] level of Reason well you're
[00:32:37] demonstrating reasoning and so it seems
[00:32:39] to me that chat GPD has this inherent
[00:32:41] capability embedded in it yeah to some
[00:32:45] degree yeah this the the this the the
[00:32:48] way one way to think about what's
[00:32:49] happening now is that these neural
[00:32:53] networks have a lot of these
[00:32:54] capabilities they're just not quite very
[00:32:56] reliable mhm in fact you could say that
[00:33:00] reliability is currently the single
[00:33:02] biggest obstacle for these neural
[00:33:03] networks being useful truly useful if
[00:33:08] sometimes it is still the case that
[00:33:12] these neural networks hallucinate a
[00:33:14] little bit or maybe make some mistakes
[00:33:17] which are unexpected which you wouldn't
[00:33:19] expect the person to make it is this
[00:33:21] kind of
[00:33:22] unreliability that makes them
[00:33:24] substantially less useful but I think
[00:33:27] that perhaps with a little bit more
[00:33:29] research with the current ideas that we
[00:33:31] have and perhaps a few more of
[00:33:33] the ambitious research plans we'll be
[00:33:37] able to achieve higher reliability as
[00:33:38] well and that will be truly useful that
[00:33:41] will allow us to have very accurate
[00:33:44] guard rails which are very precise
[00:33:47] that's right and it will make it ask for
[00:33:49] clarification where it's unsure or
[00:33:53] maybe say that it doesn't know something
[00:33:56] when it does when it in doesn't know and
[00:33:58] do so extremely reliably MH so I'd say
[00:34:01] that these
[00:34:02] are some of the bottlenecks really so
[00:34:05] it's not about whether it exhibits some
[00:34:07] particular capability but more how
[00:34:10] reliably exactly yeah you know one
[00:34:13] Speaking of speaking of factualness and
[00:34:16] factfulness uh
[00:34:19] hallucination I I I saw in in uh one of
[00:34:22] the videos uh a demonstration that that
[00:34:25] um uh links to awake Wikipedia page uh
[00:34:29] to it does retrieval capability uh has
[00:34:32] that been been included in the gp4 is it
[00:34:35] able to uh retrieve information from a
[00:34:37] factful place that that could augment
[00:34:41] its response to you so the current GPT 4
[00:34:46] as released does not have a built-in
[00:34:48] retrieval capability M it is just
[00:34:51] a really really good next word predictor
[00:34:56] mhm which can also cons images by the
[00:34:58] way we haven't spoken about it but ask
[00:35:01] really good at images which is also then
[00:35:03] fine tuned with data
[00:35:06] and various reinforcement learning
[00:35:09] variants to behave in a particular way
[00:35:12] MH it is perhaps I'm I'm sure someone
[00:35:16] will will it wouldn't surprise me if
[00:35:18] some of the people who have access could
[00:35:20] perhaps request gp4 to maybe make some
[00:35:24] queries and then populate the results
[00:35:27] inside inside the context because also
[00:35:29] the context duration of gb4 is quite a
[00:35:31] bit longer now yeah that's right
[00:35:34] so in
[00:35:37] short although gbt 4 does not support
[00:35:41] built-in
[00:35:42] retrieval it is completely correct that
[00:35:45] it will get better with retrieval yeah
[00:35:48] multimodality GPT 4 has the ability to
[00:35:52] learn from text and images and uh
[00:35:56] respond to and put from text and images
[00:35:59] uh F first of all the foundation of
[00:36:02] multimodality learning
[00:36:06] um of course
[00:36:08] Transformers has made it possible for us
[00:36:10] to learn from multimodality you tokenize
[00:36:12] text and images
[00:36:17] U but at the foundational level help us
[00:36:20] understand how multimodality
[00:36:23] enhances the understanding of the world
[00:36:26] um Beyond text by itself and uh and my
[00:36:31] understanding is that that that when you
[00:36:34] when you um uh do multimodality learning
[00:36:39] that even when it is just a text prompt
[00:36:42] the text prompt the text understanding
[00:36:45] could actually be enhanced um tell us
[00:36:48] about multimodality at the foundation
[00:36:50] why it's so important and and um what
[00:36:52] was what's the major breakthrough and
[00:36:53] the and and the characteristic
[00:36:55] differences as a result
[00:36:58] so there are two Dimensions to
[00:37:00] multimodality two reasons why it is
[00:37:03] interesting the first
[00:37:05] reason is a little bit humble the first
[00:37:10] reason is that multimodality is
[00:37:13] useful it is useful for a neural network
[00:37:16] To See Vision in particular because the
[00:37:19] world is very visual human beings are
[00:37:23] very visual
[00:37:24] animals I believe that a third of the
[00:37:27] visual of the human cortex is dedicated
[00:37:30] to
[00:37:31] vision and
[00:37:35] so by not having Vision the usefulness
[00:37:39] of our neural networks though still
[00:37:41] considerable is not as big as it could
[00:37:44] be mhm so it is a very simple usefulness
[00:37:47] argument M it is simply useful to
[00:37:52] see and gp4 can see quite
[00:37:56] well the there is a second reason to
[00:37:59] division which is that we learn more
[00:38:02] about the
[00:38:03] World by learning from images in
[00:38:06] addition to learning from
[00:38:09] text that is also a powerful argument
[00:38:13] though it is not as clear-cut as it may
[00:38:15] seem I'll give you an
[00:38:17] example or rather before giving an
[00:38:19] example I'll make the general comment
[00:38:22] for a human being as human beings we get
[00:38:26] to hear about 1 billion words in our
[00:38:30] entire life only only 1 billion words
[00:38:33] that's amazing yeah that's not a lot
[00:38:35] yeah that's not a lie so we need to comp
[00:38:39] we need does that include my own words
[00:38:40] in my own
[00:38:41] head to make it two billion want but you
[00:38:45] see what I mean yeah you know we can see
[00:38:47] that because um a billion seconds is 30
[00:38:51] years so you can kind of see like we
[00:38:53] don't get to see more than a few words a
[00:38:55] second then we asleep half the time so
[00:38:57] like a couple billion words is the total
[00:38:59] we get in our entire life so it becomes
[00:39:02] really important for us to get as many
[00:39:04] sources of information as we can and we
[00:39:06] absolutely learn a lot more from
[00:39:08] Vision the same argument holds true for
[00:39:11] our neural networks as well except
[00:39:15] except for the fact that the neural
[00:39:16] network can learn from so many words
[00:39:20] so things which are hard to learn about
[00:39:23] the world from text in a few billion
[00:39:27] words
[00:39:28] may become easier from trillions of
[00:39:31] words and I'll give you an
[00:39:34] example consider
[00:39:37] colors surely one needs to see to
[00:39:41] understand
[00:39:42] colors and yet the text only neural
[00:39:45] networks who never seen a single Photon
[00:39:49] in their entire life if you ask them
[00:39:52] which colors are more similar to each
[00:39:53] other it will know that red is more
[00:39:56] similar to Orange than to Blue mhm it
[00:39:58] will know that blue is more similar to
[00:40:00] purple than to Yellow mhm how does that
[00:40:04] happen and one answer is that
[00:40:07] information about the world even the
[00:40:09] visual information slowly leaks in
[00:40:12] through text but slowly not as quickly
[00:40:15] but when you have a lot of text you can
[00:40:17] still learn a lot of course once you
[00:40:20] also add vision and learning about the
[00:40:23] world from Vision you will learn
[00:40:25] additional things which are not captured
[00:40:26] in text MH but it is not I would not say
[00:40:30] that it is a binary there are things
[00:40:32] which are impossible to learn from from
[00:40:35] text only I think this is more of an
[00:40:37] exchange rate yeah and in particular as
[00:40:39] you want to learn if if we are if you if
[00:40:42] you if you are like a human being and
[00:40:44] you want to learn from a billion words
[00:40:47] or a 100 million words then of course
[00:40:49] the other sources of information become
[00:40:51] far more
[00:40:53] important yeah and so so the the um you
[00:40:57] learn from
[00:40:58] images is there is there a sensibility
[00:41:01] that that would suggest that if we
[00:41:03] wanted to understand um also the
[00:41:05] construction of the world as in you know
[00:41:08] the arm is connected to my shoulder that
[00:41:10] my elbow's connected that somehow these
[00:41:12] things move the the the the an the the
[00:41:15] animation of the world the physics of
[00:41:17] the world if I wanted to learn that as
[00:41:19] well can I just watch videos and learn
[00:41:21] that yes yeah and and if I wanted to
[00:41:25] augment all of that with sound like for
[00:41:26] example if somebody said um the meaning
[00:41:29] of of
[00:41:30] great uh great could be great or great
[00:41:35] could be great you know so one is
[00:41:38] sarcastic one is enthusiastic uh there
[00:41:41] are many many words like that you know
[00:41:44] uh uh that's sick or you know I'm sick
[00:41:47] or I'm sick depending on how people say
[00:41:50] it would would audio also make a
[00:41:53] contribution to the learning of the the
[00:41:55] the model and and could we put that to
[00:41:57] good use soon yes yeah I think I think
[00:42:00] it's definitely the case that well you
[00:42:04] know what can we say about audio it's
[00:42:06] useful it's an additional source of
[00:42:07] information probably not as much as
[00:42:10] images or video but there is there is a
[00:42:14] case to be made for the usefulness of
[00:42:16] audio as well both on the recognition
[00:42:18] side and on the production side when you
[00:42:21] when you um I on the on the context of
[00:42:25] the scores that I saw
[00:42:27] um the the thing that was really
[00:42:28] interesting was was uh the the data that
[00:42:31] you guys published which which one of
[00:42:33] the tests were were um uh performed well
[00:42:36] by gpt3 and which one of the tests
[00:42:39] performed substantially better with GPT
[00:42:41] 4 um how did multimodality contribute to
[00:42:46] those tests do you think oh I mean in a
[00:42:49] pretty straightforward straightforward
[00:42:51] way anytime there was a test where a
[00:42:54] problem would where to understand the
[00:42:56] problem need to look at a diagram mhm
[00:42:59] like for example in some math
[00:43:00] competitions like there is
[00:43:02] a math competition for high school
[00:43:05] students called
[00:43:06] amc2 12 right and there presumably many
[00:43:11] of the problems have a diagram so gbt
[00:43:15] 3.5 does quite badly on that on that EX
[00:43:19] on that on the test gp4 with text only
[00:43:23] does I think I don't remember but it's
[00:43:26] like maybe from 2% to 20% accuracy of
[00:43:30] success rate but then when you add
[00:43:32] Vision it jumps to 40% success rate so
[00:43:34] the vision is really doing a lot of work
[00:43:36] the vision is extremely good and I think
[00:43:40] being able to reason visually as well
[00:43:42] and communicate visually will also be
[00:43:45] very powerful and very nice things which
[00:43:47] go beyond just learning about the world
[00:43:50] there have several things you got to
[00:43:51] learn you can learn about the world you
[00:43:53] can then reason about the world visually
[00:43:55] and you can communicate visually where
[00:43:58] now in the future perhaps in some future
[00:44:00] version if you ask your neural net hey
[00:44:02] like explain this to me rather than just
[00:44:04] producing four paragraphs it will
[00:44:06] produce hey like here's like a little
[00:44:08] diagram which clearly conveys to you
[00:44:10] exactly what you need to know and so
[00:44:12] yeah that's incredible you know one of
[00:44:14] the things that you said earlier about
[00:44:15] about an AI generating generating a a
[00:44:18] test to train another AI um you know
[00:44:22] there's there was a paper that was
[00:44:23] written about and I I I don't I don't
[00:44:26] completely know whether whether it's
[00:44:27] factual or not but but um that there's
[00:44:30] there's a total amount of somewhere
[00:44:31] between 4 trillion to something like 20
[00:44:33] trillion useful you know tokens in in
[00:44:39] language tokens that that the world will
[00:44:41] be able to train on you know over some
[00:44:44] period of time and that we're going to
[00:44:45] run out of tokens to train and and um I
[00:44:49] I well first of all I wonder if that's
[00:44:52] you feel the same way and then the
[00:44:53] second secondarily right whether whether
[00:44:57] whether the AI generating its own um
[00:45:02] data uh could be used to train the AI
[00:45:05] itself which you could argue is a little
[00:45:08] circular but um we train our brain with
[00:45:13] generated data all the time by uh
[00:45:18] self-reflection um working through a
[00:45:20] problem in our brain uh you know and and
[00:45:23] uh or you know some I guess I guess
[00:45:26] neuroscientist suggest sleeping uh we we
[00:45:28] do a lot of fair amount of you know
[00:45:30] developing our neurons um how do you see
[00:45:33] this this area of synthetic data
[00:45:35] generation is that going to be an
[00:45:36] important part of the future of training
[00:45:38] Ai and and the AI teaching itself well
[00:45:41] that's I
[00:45:43] think like I I wouldn't underestimate
[00:45:45] the data that exists out there mhm I
[00:45:48] think this
[00:45:49] probably I think this probably more more
[00:45:52] data Than People
[00:45:53] realize and as to your second question
[00:45:57] certainly a possibility mhm remains to
[00:45:59] be seen yeah yeah it see it it really
[00:46:02] does seem that that um uh one of these
[00:46:05] days our AIS are are um you know one
[00:46:08] we're not using it maybe generating
[00:46:11] either adversarial content for itself to
[00:46:12] learn from or imagine solving problems
[00:46:16] that that it can go off and and then and
[00:46:18] then uh improve itself uh tell tell us
[00:46:21] uh uh whatever you can about about uh uh
[00:46:25] where we are now and and where do you
[00:46:27] think we'll be in and not not too
[00:46:29] distant future but you know pick pick
[00:46:32] your your horizon a year or two what do
[00:46:35] you think this whole language Model area
[00:46:37] would be in some of the areas that
[00:46:38] you're most excited about you know
[00:46:40] predictions are hard and um it's bit
[00:46:43] it's a bit although it's a little
[00:46:45] difficult
[00:46:46] to say things which are too
[00:46:48] specific I think it's safe to
[00:46:52] assume that progress will continue and
[00:46:57] that we will keep on seeing systems
[00:46:58] which Astound us in their in the things
[00:47:02] they can do and the current Frontiers
[00:47:05] are will be centered around
[00:47:07] reliability around the system can be
[00:47:11] trusted really getting to a point where
[00:47:13] he can trust what it produces really
[00:47:16] getting to a point where if it doesn't
[00:47:19] understand something it asks for a
[00:47:21] clarification says that it doesn't know
[00:47:23] something says that he needs more
[00:47:25] information I think those are perhaps
[00:47:28] the biggest the areas where Improvement
[00:47:31] will lead to the biggest impact on the
[00:47:34] usefulness of those systems because
[00:47:36] right now that's really what stands in
[00:47:37] the way you have an you have asking
[00:47:39] neural net for you asking neural net to
[00:47:41] maybe summarize some long document and
[00:47:43] you get a
[00:47:44] summary like are you sure that some
[00:47:46] important detail wasn't omitted it's
[00:47:47] still a useful summary but it's a
[00:47:50] different story when you know that all
[00:47:52] the important points have been
[00:47:55] covered at some point like and in
[00:47:57] particular it's okay like if some if
[00:48:00] there is ambiguity it's fine but if a
[00:48:02] point is clearly important such that
[00:48:04] anyone else who saw the point would say
[00:48:06] this is really important when the neural
[00:48:08] network will also recognize that
[00:48:10] reliably that's when you know same for
[00:48:12] the guardrail same same for its ability
[00:48:14] to clearly follow the intent of the user
[00:48:18] of of its operator so I think we'll see
[00:48:21] a lot of that in the next two years yeah
[00:48:23] that's terrific because those the
[00:48:24] progress in those two areas will make
[00:48:26] this technology uh trusted by people to
[00:48:29] use and be able to apply for so many
[00:48:31] things I I was thinking that was going
[00:48:33] to be the last question but I did have
[00:48:34] another one sorry about that so so chat
[00:48:37] uh chat GPT to gp4 um gp4 when when it
[00:48:41] first when you first started using it uh
[00:48:44] what are some of the skills that it
[00:48:47] demonstrated that surprised even you
[00:48:52] well there were lots of really cool
[00:48:54] things that it demonstrated which
[00:48:59] which is which were quite cool and
[00:49:01] surprising it was it was quite good so
[00:49:06] I'll mention two ex so let's see I'm
[00:49:08] just I'm TR trying to think about the
[00:49:11] best way to go about it the short answer
[00:49:14] is that the level of its reliability was
[00:49:17] surprising mhm where the previous neural
[00:49:20] networks if you ask them a question
[00:49:23] sometimes they might misunderstand
[00:49:25] something in a kind of a
[00:49:28] silly way where it was gp4 that stopped
[00:49:30] happening its ability to solve math
[00:49:33] problems became far greater it's like
[00:49:35] you could really like say you know
[00:49:37] really do the derivation and like long
[00:49:40] complicated derivation you could convert
[00:49:41] the units and so on and that was really
[00:49:43] cool you know like many people it works
[00:49:45] through a proof it works through a proof
[00:49:47] it's pretty amazing not all proofs
[00:49:49] naturally but but quite a few or another
[00:49:52] example would be like many people
[00:49:54] noticed that it has the ability to
[00:49:58] produce poems with you know every word
[00:50:01] starting with the same letter or every
[00:50:03] word starting with some it follows
[00:50:06] instructions really really clearly not
[00:50:08] perfectly still but much better than
[00:50:10] before yeah really good and on the
[00:50:12] vision side I really love how it can
[00:50:14] explain jokes it can explain memes you
[00:50:17] show it a meme and ask it why it's funny
[00:50:19] and it will tell you and it will be
[00:50:21] correct the V the vision part I think is
[00:50:25] very was so very it's like really
[00:50:27] actually seeing it when you can ask
[00:50:29] followup questions about some
[00:50:32] complicated image with a complicated
[00:50:34] diagram and get an explanation that's
[00:50:36] really
[00:50:36] cool but yeah overall I will say to take
[00:50:39] a step back you know I've been I've been
[00:50:43] in this business for quite some time
[00:50:44] actually like almost exactly 20
[00:50:48] years
[00:50:50] and the thing which most which I find
[00:50:52] most surprising is that it actually
[00:50:55] works
[00:50:57] yeah like it it turned out to be the
[00:50:59] same little thing all along which is no
[00:51:02] longer little and it's a lot more
[00:51:04] serious and much more intense but it's
[00:51:07] the same neural network just larger
[00:51:10] trained on maybe larger data sets in
[00:51:11] different ways with the same fundamental
[00:51:14] training algorithm yeah so it's like
[00:51:18] wow I would say this is what I find the
[00:51:20] most surprising yeah whenever I take a
[00:51:22] step back I go how is it possible that
[00:51:24] those ideas those conceptual ideas is
[00:51:26] about well the brain has neurons so
[00:51:29] maybe artificial neurons are just as
[00:51:31] good and so maybe we just need to train
[00:51:33] them somehow with some learning
[00:51:34] algorithm that those arguments turned
[00:51:36] out to be so incredibly
[00:51:38] correct that would be the biggest
[00:51:42] surprise I'd say in the in the 10 years
[00:51:44] that that we've known each other uh
[00:51:47] you're you're uh the near the models
[00:51:50] that you've trained and the amount of
[00:51:51] data you've trained from uh the what you
[00:51:55] did on net to now is about a million
[00:51:59] times and and uh no no one in the world
[00:52:04] of computer science would have would
[00:52:06] have believed that the amount of
[00:52:08] computation that was done in that 10
[00:52:10] years time would be a million times
[00:52:12] larger and that that you dedicated your
[00:52:15] career to go go do that um you've done
[00:52:19] two uh many more uh your body of work is
[00:52:22] incredible but two seminal works and the
[00:52:25] invention the co-invention with Alex net
[00:52:27] and that that early work and and now
[00:52:30] with uh GPT at open AI uh it is it is
[00:52:33] truly remarkable what you've
[00:52:35] accomplished it's it's great to catch up
[00:52:37] with you again Ilia my good friend and
[00:52:40] and um uh it is uh it is quite an
[00:52:43] amazing moment and a today's today's
[00:52:46] talk the way you you uh break down the
[00:52:48] problem and describe it uh this is one
[00:52:50] of the one of the uh the the best PhD
[00:52:55] Beyond PhD description
[00:52:56] of the State ofthe art of large language
[00:52:58] models I really appreciate that it's
[00:53:00] great to see you congratulations thank
[00:53:01] you so much yeah thank had so much fun
[00:53:04] thank you yeah
