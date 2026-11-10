# Lex Fridman #36: Yann LeCun — Deep Learning, ConvNets & Bell Labs
- **YouTube URL:** https://www.youtube.com/watch?v=SGSOCuByo24
- **Lines:** 1839

---

[00:00:00] the following is a conversation with
[00:00:01] Jana kun he's considered to be one of
[00:00:04] the fathers of deep learning which if
[00:00:07] you've been hiding under a rock is the
[00:00:09] recent revolution in AI that's
[00:00:10] captivated the world with the
[00:00:12] possibility of what machines can learn
[00:00:14] from data he's a professor in New York
[00:00:17] University a vice president and chief AI
[00:00:19] scientist a Facebook & Co recipient of
[00:00:23] the Turing Award for his work on deep
[00:00:25] learning he's probably best known as the
[00:00:28] founding father of convolutional neural
[00:00:29] networks in particular their application
[00:00:32] to optical character recognition and the
[00:00:34] famed M NIST data set he is also an
[00:00:38] outspoken personality unafraid to speak
[00:00:41] his mind in a distinctive French accent
[00:00:43] and explore provocative ideas both in
[00:00:46] the rigorous medium of academic research
[00:00:47] and the somewhat less rigorous medium of
[00:00:51] Twitter and Facebook this is the
[00:00:53] artificial intelligence podcast if you
[00:00:55] enjoy it subscribe on YouTube give it
[00:00:58] five stars on iTunes support and on
[00:01:00] patreon we're simply gonna equip me on
[00:01:02] Twitter Alex Friedman spelled the Fri D
[00:01:04] ma N and now here's my conversation with
[00:01:08] Yann Laocoon you said that 2001 Space
[00:01:13] Odyssey is one of your favorite movies
[00:01:15] Hal 9000 decides to get rid of the
[00:01:19] astronauts for people haven't seen the
[00:01:21] movie spoiler alert because he it she
[00:01:25] believes that the astronauts they will
[00:01:29] interfere with the mission do you see
[00:01:31] how is flawed in some fundamental way or
[00:01:34] even evil or did he do the right thing
[00:01:37] neither there's no notion of evil in
[00:01:41] that in that context other than the fact
[00:01:44] that people die but it was an example of
[00:01:46] what people call value misalignment
[00:01:49] right you give an objective to a machine
[00:01:51] and the Machine strives to achieve this
[00:01:54] objective and if you don't put any
[00:01:56] constraints on this objective like don't
[00:01:58] kill people and don't do things like
[00:02:00] this
[00:02:01] the Machine given the power will do
[00:02:05] stupid things just to achieve this dis
[00:02:07] objective or damaging things to achieve
[00:02:09] its objective it's a little bit like we
[00:02:11] are used to this in the context of human
[00:02:13] society we we put in place laws to
[00:02:20] prevent people from doing bad things
[00:02:21] because fantasy did we do those bad
[00:02:23] things right so we have to shave their
[00:02:26] cost function the objective function if
[00:02:29] you want through laws to kind of correct
[00:02:31] an education obviously to sort of
[00:02:33] correct for for those so maybe just
[00:02:37] pushing a little further on on that
[00:02:39] point how you know there's a mission
[00:02:44] there's a this fuzziness around the
[00:02:46] ambiguity around what the actual mission
[00:02:48] is but you know do you think that there
[00:02:53] will be a time from a utilitarian
[00:02:55] perspective or an AI system where it is
[00:02:58] not misalignment where it is alignment
[00:03:00] for the greater good of society that
[00:03:02] kneei system will make decisions that
[00:03:04] are difficult well that's the trick I
[00:03:06] mean eventually we'll have to figure out
[00:03:10] how to do this and again we're not
[00:03:11] starting from scratch because we've been
[00:03:13] doing this with humans for four
[00:03:15] millennia
[00:03:15] so designing objective functions for
[00:03:18] people is something that we know how to
[00:03:20] do and we don't do it by you know
[00:03:23] programming things although the legal
[00:03:26] code is called code so that tells you
[00:03:30] something and it's actually the design
[00:03:32] of an object you function that's really
[00:03:33] what legal code is right it tells you
[00:03:35] you can do it what you can't do if you
[00:03:37] do it you pay that much that's that's an
[00:03:39] objective function so there is this idea
[00:03:43] somehow that it's a new thing for people
[00:03:45] to try to design objective functions are
[00:03:46] aligned with the common good but no
[00:03:48] we've been writing laws for millennia
[00:03:49] and that's exactly what it is
[00:03:51] so this that's where you know the
[00:03:54] science of lawmaking and and computer
[00:03:59] science will come together will come
[00:04:01] together so it's nothing there's nothing
[00:04:04] special about how or a I systems is just
[00:04:07] the continuation of tools used to make
[00:04:09] some of these difficult ethical
[00:04:10] judgments that laws make yeah and we and
[00:04:13] we have systems like this already that
[00:04:15] you know make many decisions for
[00:04:18] ourselves in society that you know need
[00:04:20] to be designed in a way that they like
[00:04:22] you know rules about things that
[00:04:24] sometimes sometimes have bad side
[00:04:26] effects and we have to be flexible
[00:04:28] enough about those rules so that they
[00:04:30] can be broken when it's obvious that
[00:04:31] they shouldn't be applied so you don't
[00:04:34] see this on the camera here but all the
[00:04:36] decorations in this room is all pictures
[00:04:38] from 2001 a Space Odyssey Wow
[00:04:41] and by accident or is there a lot about
[00:04:43] accident it's by design Wow so if you
[00:04:49] were if you were to build hell 10,000 so
[00:04:52] an improvement of Hal 9000 what would
[00:04:55] you improve well first of all I wouldn't
[00:04:58] ask you to hold secrets and tell lies
[00:05:01] because that's really what breaks it in
[00:05:03] the end that's the the fact that it's
[00:05:05] asking itself questions about the
[00:05:07] purpose of the mission and it's you know
[00:05:09] pieces things together that it's heard
[00:05:11] you know all the secrecy of the
[00:05:13] preparation of the mission and the fact
[00:05:14] that it was discovery and on the lunar
[00:05:17] surface that really was kept secret and
[00:05:19] and one part of Hal's memory knows this
[00:05:22] and the other part is does not know it
[00:05:24] and it's supposed to not tell anyone and
[00:05:26] that creates a internal conflict do you
[00:05:28] think there's never should be a set of
[00:05:31] things that night AI system should not
[00:05:34] be allowed like a set of facts that
[00:05:38] should not be shared with the human
[00:05:40] operators well I think no I think the I
[00:05:44] think it should be a bit like in the
[00:05:46] design of autonomous AI systems there
[00:05:52] should be the equivalent of you know the
[00:05:54] the the oath that hypocrite Oh calm
[00:05:58] yourself yeah that doctors sign up to
[00:06:01] right so the certain thing certain rule
[00:06:03] said that that you have to abide by and
[00:06:05] we can sort of hardwire this into into
[00:06:08] our into our machines to kind of make
[00:06:10] sure they don't go so I'm not you know
[00:06:11] advocate of the the 303 dollars of
[00:06:14] Robotics you know the as you move kind
[00:06:16] of thing because I don't think it's
[00:06:18] practical but but you know some some
[00:06:21] level of of limits but but to be clear
[00:06:24] this is not these are not questions that
[00:06:28] are kind of really worth asking today
[00:06:31] because we just don't have the
[00:06:33] technology to do this we don't we don't
[00:06:35] have a ton of missing teller machines we
[00:06:36] have intelligent machines so my
[00:06:37] intelligent machines that are very
[00:06:38] specialized but they don't they don't
[00:06:41] really sort of satisfy an objective
[00:06:43] they're just you know kind of trained to
[00:06:45] do one thing so until we have some idea
[00:06:49] for design of a full-fledged autonomous
[00:06:51] intelligent system asking the question
[00:06:54] of how we design use objective I think
[00:06:55] is a little a little too abstract it's a
[00:06:58] little tough rat there's useful elements
[00:07:00] to it in that it helps us understand our
[00:07:04] own ethical codes humans so even just as
[00:07:08] a thought experiment if you imagine that
[00:07:11] in a GI system is here today how would
[00:07:15] we program it is a kind of nice thought
[00:07:17] experiment of constructing how should we
[00:07:19] have a law have a system of laws far as
[00:07:23] humans
[00:07:24] it's just a nice practical tool and I
[00:07:27] think there's echoes of that idea too in
[00:07:29] the AI systems left today it don't have
[00:07:32] to be that intelligent
[00:07:33] yeah like autonomous vehicles there's
[00:07:35] these things start creeping in that were
[00:07:38] thinking about but certainly they
[00:07:39] shouldn't be framed as as hell yeah
[00:07:43] looking back what is the most I'm sorry
[00:07:47] if it's a silly question but what is the
[00:07:50] most beautiful or surprising idea and
[00:07:52] deep learning or AI in general that
[00:07:55] you've ever come across sort of
[00:07:56] personally well you said back and and
[00:08:00] just had this kind of wow that's pretty
[00:08:02] cool
[00:08:02] moment that's nice well surprising I
[00:08:05] don't know if it's an idea rather than a
[00:08:07] sort of empirical fact the fact that you
[00:08:15] gigantic neural nets trying to train
[00:08:17] them on you know relatively small
[00:08:20] amounts of data relatively with the
[00:08:23] caste grid in the center that it
[00:08:25] actually works breaks everything you
[00:08:27] read in every textbook right every pre
[00:08:30] deep learning textbook that told you you
[00:08:32] need to have fewer parameters and you
[00:08:34] have data samples you know if you have
[00:08:37] non-convex objective function you have
[00:08:38] no guarantee of convergence you know all
[00:08:40] the things that you read in textbook and
[00:08:42] they tell you stay away from this and
[00:08:43] they were all wrong huge number of
[00:08:45] parameters non-convex and somehow which
[00:08:48] is very relative to the number of
[00:08:51] parameters data it's able to learn
[00:08:54] anything right does that surprise you
[00:08:56] today well it it was kind of obvious to
[00:09:00] me before I knew anything that that's
[00:09:02] that this is a good idea and then it
[00:09:04] became surprising that it worked
[00:09:06] because I started reading those text
[00:09:07] books okay so okay you talk to the
[00:09:11] intuition of why was obviously if you
[00:09:13] remember well okay so the intuition was
[00:09:15] it's it's sort of like you know those
[00:09:17] people in the late 19th century who
[00:09:20] proved that heavier than than air flight
[00:09:23] was impossible right and of course you
[00:09:25] have birds right they do fly and so on
[00:09:29] the face of it it it's obviously wrong
[00:09:31] as an empirical question right and so we
[00:09:33] have the same kind of thing that you
[00:09:36] know the we know that the brain works we
[00:09:38] don't know how but we know it works and
[00:09:40] we know it's a large network of neurons
[00:09:42] and interaction and the learning takes
[00:09:43] place by changing the connection so kind
[00:09:46] of getting this level of inspiration
[00:09:47] without copying the details but sort of
[00:09:49] trying to derive basic principles
[00:09:54] you know that kind of gives you a clue
[00:09:56] as to which direction to go there's also
[00:09:58] the idea somehow that I've been
[00:10:00] convinced of since I was an undergrad
[00:10:02] that even before that intelligence is
[00:10:05] inseparable from running so you the idea
[00:10:08] somehow that you can create an
[00:10:10] intelligent machine by basically
[00:10:12] programming for me was a non-starter you
[00:10:16] know from the start every intelligent
[00:10:19] entity that we know about arrives at
[00:10:22] this intelligence to learning so
[00:10:25] learning you know machine learning was
[00:10:26] completely obvious path also because I'm
[00:10:30] lazy so you know it's automate basically
[00:10:34] everything and learning is the
[00:10:35] automation of intelligence right so do
[00:10:40] you think so what is learning then what
[00:10:43] what falls under learning because do you
[00:10:45] think of reasoning is learning where
[00:10:49] reasoning is certainly a consequence of
[00:10:52] learning as well just like other
[00:10:55] functions of of the brain
[00:10:57] the big question about reasoning is how
[00:10:59] do you make reasoning compatible with
[00:11:01] gradient based learning do you think
[00:11:03] neural networks can be made to reason
[00:11:05] yes that there's no question about that
[00:11:06] again we have a good example right the
[00:11:11] question is is how so the question is
[00:11:12] how much prior structure you have to put
[00:11:15] in the neural net so that something like
[00:11:17] human reasoning will emerge from it you
[00:11:19] know from running another question is
[00:11:22] all of our kind of model of what
[00:11:25] reasoning is that are based on logic are
[00:11:27] discrete and and and are therefore
[00:11:30] incompatible with gradient based
[00:11:32] learning and I was very strong believer
[00:11:34] in this idea Grandin baserunning I don't
[00:11:36] believe that other types of learning
[00:11:39] that don't use kind of gradient
[00:11:41] information if you want so you don't
[00:11:42] like discrete mathematics you don't like
[00:11:44] anything discrete
[00:11:45] well that's it's not that I don't like
[00:11:47] it it's just that it's it's incompatible
[00:11:49] with learning and I'm a big fan of
[00:11:51] running right so in fact that's perhaps
[00:11:53] one reason why deep learning has been
[00:11:56] kind of looked at with suspicion by a
[00:11:58] lot of computer scientists because the
[00:11:59] math is very different the method you
[00:12:02] use for deep running you know we kind of
[00:12:03] as more to do with you know cybernetics
[00:12:07] the kind of math you do in electrical
[00:12:09] engineering then the kind of math you
[00:12:11] doing computer science and and you know
[00:12:13] nothing in in machine learning is exact
[00:12:15] right computer science is all about sort
[00:12:18] of you know obviously compulsive
[00:12:20] attention to details of like you know
[00:12:22] every index has to be right and you can
[00:12:24] prove that an algorithm is correct right
[00:12:26] machine learning is the science of
[00:12:29] sloppiness really that's beautiful so
[00:12:34] okay maybe let's feel around in the dark
[00:12:37] of what is a neural network that reasons
[00:12:40] or a system that is works with
[00:12:45] continuous functions that's able to do
[00:12:50] build knowledge however we think about
[00:12:53] reasoning builds on previous knowledge
[00:12:55] build on extra knowledge create new
[00:12:58] knowledge generalized outside of any
[00:13:01] training set ever built what does that
[00:13:03] look like if yeah maybe
[00:13:06] do you have Inklings of thoughts of what
[00:13:09] that might look like well yeah I mean
[00:13:11] yes or no if I had precise ideas about
[00:13:13] this I think you know we'd be building
[00:13:16] it right now but and there are people
[00:13:17] working on this or whose main research
[00:13:20] interest is actually exactly that right
[00:13:22] so what you need to have is a working
[00:13:24] memory so you need to have some device
[00:13:28] if you want some subsystem they can
[00:13:31] store a relatively large number of
[00:13:34] factual episodic information for you
[00:13:38] know a reasonable amount of time so you
[00:13:41] you know in the in the brain for example
[00:13:43] it kind of three main types of memory
[00:13:45] one is the sort of memory of the the
[00:13:50] state of your cortex and that sort of
[00:13:54] disappears within 20 seconds you can't
[00:13:56] remember things for more than about 20
[00:13:57] seconds or a minute if if you don't have
[00:14:00] any other form of memory the second type
[00:14:02] of memory which is longer term is short
[00:14:04] term is the hippocampus so you can you
[00:14:07] know you came into this building you
[00:14:08] remember whether where the the exit is
[00:14:10] where the elevators are you have some
[00:14:14] map of that building that's stored in
[00:14:16] your hippocampus you might remember
[00:14:18] something about what I said you know if
[00:14:20] you
[00:14:20] minutes ago and forgot all our stars
[00:14:22] being raised but you know but that does
[00:14:25] not work in your hippocampus and then
[00:14:27] the the longer term memory is in the
[00:14:29] synapse the synapses right so what you
[00:14:33] need if you want for a system that's
[00:14:34] capable reasoning is that you want the
[00:14:36] hippocampus like thing right and that's
[00:14:40] what people have tried to do with memory
[00:14:42] networks and you know no Turing machines
[00:14:44] and stuff like that right and and now
[00:14:46] with transformers which have sort of a
[00:14:48] memory in their kind of self attention
[00:14:51] system you can you can think of it this
[00:14:52] way so so that's one element you need
[00:14:56] another thing you need is some sort of
[00:14:59] network that can access this memory get
[00:15:05] an information back and then kind of
[00:15:07] crunch on it and then do this
[00:15:09] iteratively multiple times because a
[00:15:11] chain of reasoning is a process by which
[00:15:16] you you you can you update your
[00:15:18] knowledge about the state of the world
[00:15:20] about you know what's gonna happen etc
[00:15:22] and that there has to be this sort of
[00:15:24] recurrent operation basically and you
[00:15:27] think that kind of if we think about a
[00:15:29] transformer so that seems to be too
[00:15:32] small to contain the knowledge that's
[00:15:34] that's to represent the knowledge as
[00:15:37] containing Wikipedia for example but
[00:15:39] transformer doesn't have this idea of
[00:15:40] recurrence it's got a fixed number of
[00:15:42] layers and that's number of steps that
[00:15:44] you know limits basically it's a
[00:15:46] representation but recurrence would
[00:15:48] build on the knowledge somehow I mean
[00:15:51] yeah it would evolve the knowledge and
[00:15:54] expand the amount of information perhaps
[00:15:57] or useful information within that
[00:15:59] knowledge yeah but is this something
[00:16:02] that just can emerge with size because
[00:16:04] it seems like everything we have now is
[00:16:06] just no it's not it's not it's not clear
[00:16:08] how you access and right into an
[00:16:11] associative memory in efficient way I
[00:16:13] mean sort of the original memory network
[00:16:15] maybe had something like the right
[00:16:16] architecture but if you try to scale up
[00:16:19] a memory network so that the memory
[00:16:21] contains all we keep here it doesn't
[00:16:23] quite work right so so this is a need
[00:16:26] for new ideas there okay but it's not
[00:16:29] the only form of reasoning so there's
[00:16:30] another form of reasoning which is true
[00:16:32] which is very classical so in
[00:16:34] some types of AI and it's based on let's
[00:16:39] call it energy minimization okay so you
[00:16:41] have some sort of objective some energy
[00:16:45] function that represents the the the
[00:16:50] quality or the negative quality okay
[00:16:53] energy goes up when things get bad and
[00:16:54] they get low when things get good so
[00:16:57] let's say you you want to figure out you
[00:17:00] know what gestures do I need to to do to
[00:17:04] grab an object or walk out the door if
[00:17:08] you have a good model of your own body a
[00:17:10] good model of the environment using this
[00:17:12] kind of energy minimization you can make
[00:17:14] a you can make you can do planning and
[00:17:16] it's in optimal control it's called it's
[00:17:20] called Marie put model predictive
[00:17:21] control you have a model of what's gonna
[00:17:23] happen in the world as consequence for
[00:17:24] your actions and that allows you to buy
[00:17:27] energy minimization figure out the
[00:17:29] sequence of action that optimizes a
[00:17:30] particular objective function which
[00:17:32] measures you know minimize the number of
[00:17:33] times you're gonna hit something and the
[00:17:35] energy gonna spend doing the gesture and
[00:17:37] etc so so that's performer reasoning
[00:17:42] planning is a form of reasoning and
[00:17:43] perhaps what led to the ability of
[00:17:46] humans to reason is the fact that or you
[00:17:50] know species you know that appear before
[00:17:53] us had to do some sort of planning to be
[00:17:55] able to hunt and survive and survive the
[00:17:58] winter in particular and so you know
[00:18:00] it's the same capacity that you need to
[00:18:02] have so in your intuition is if you look
[00:18:07] at expert systems in encoding knowledge
[00:18:11] as logic systems as graphs in this kind
[00:18:15] of way is not a useful way to think
[00:18:18] about knowledge graphs are your brittle
[00:18:21] or logic representation so basically you
[00:18:24] know variables that that have values and
[00:18:27] constraint between them that are
[00:18:29] represented by rules as well too rigid
[00:18:32] and too brittle right so one of the you
[00:18:33] know some of the early efforts in that
[00:18:35] respect were were to put probabilities
[00:18:40] on them so a rule you know you know if
[00:18:43] you have this in that symptom you know
[00:18:44] you have this disease with that
[00:18:46] probability and you should
[00:18:47] describe that antibiotic with that
[00:18:49] probability right this my sin system
[00:18:51] from the for the 70s and that that's
[00:18:54] what that branch of AI led to you know
[00:18:58] busy networks in graphical models and
[00:19:00] causal inference and vibrational you
[00:19:03] know method so so there there is I mean
[00:19:07] certainly a lot of interesting work
[00:19:10] going on in this area the main issue
[00:19:12] with this is is knowledge acquisition
[00:19:13] how do you reduce a bunch of data to
[00:19:18] graph of this type near relies on the
[00:19:20] expert and a human being to encode at
[00:19:23] add knowledge and that's essentially
[00:19:26] impractical yeah the question the second
[00:19:30] question is do you want to represent
[00:19:32] knowledge symbols and you want to
[00:19:35] manipulate them with logic and again
[00:19:37] that's incomparable we're learning so
[00:19:40] one suggestion with geoff hinton has
[00:19:43] been advocating for many decades is
[00:19:45] replace symbols by vectors think of it
[00:19:49] as pattern of activities in a bunch of
[00:19:51] neurons or units or whatever you wanna
[00:19:53] call them and replace logic by
[00:19:57] continuous functions okay
[00:19:59] and that becomes now compatible there's
[00:20:01] a very good set of ideas by region in a
[00:20:06] paper about 10 years ago by leon go to
[00:20:08] on who is here at face book the title of
[00:20:13] the paper is for machine learning to
[00:20:15] machine reasoning and his idea is that
[00:20:17] learning learning system should be able
[00:20:19] to manipulate objects that are in the
[00:20:21] same space in a space and then put the
[00:20:23] result back in the same space so is this
[00:20:25] idea of working memory basically and
[00:20:27] it's a very enlightening and in the
[00:20:31] sense that might learn something like
[00:20:33] the simple expert systems
[00:20:36] I mean it's with you can learn basic
[00:20:40] logic operations there yeah quite
[00:20:42] possibly yeah this is a big debate on
[00:20:44] sort of how much prior structure you
[00:20:46] have to put in for this kind of stuff to
[00:20:48] emerge that's the debate I have with
[00:20:50] Gary Marcus and people like that yeah
[00:20:51] yeah so and the other person so I just
[00:20:55] talked to judea pearl mm-hmm well you
[00:20:57] mentioned causal inference world
[00:21:00] his worry is that the current knew all
[00:21:03] networks are not able to learn what
[00:21:08] causes what causal inference between
[00:21:11] things so I think I think he's right and
[00:21:14] wrong about this if he's talking about
[00:21:16] the sort of classic type of neural nets
[00:21:21] people also didn't worry too much about
[00:21:22] this but there's a lot of people now
[00:21:24] working on causal inference and there's
[00:21:26] a paper that just came out last week by
[00:21:27] Leon Mbutu among others develop his path
[00:21:29] and push for other people exactly on
[00:21:32] that problem of how do you kind of you
[00:21:36] know get a neural net to sort of pay
[00:21:38] attention to real causal relationships
[00:21:40] which may also solve issues of bias in
[00:21:45] data and things like this so I'd like to
[00:21:48] read that paper because that ultimately
[00:21:51] the challenges also seems to fall back
[00:21:54] on the human expert to ultimately decide
[00:21:58] causality between things people are not
[00:22:02] very good at its direction causality
[00:22:03] first of all so first of all you talk to
[00:22:05] a physicist and physicists actually
[00:22:07] don't believe in causality because look
[00:22:09] at the all the busy clause or
[00:22:12] microphysics are time reversible so
[00:22:14] there is no causality the arrow of time
[00:22:16] is not right yeah it's it's as soon as
[00:22:17] you start looking at macroscopic systems
[00:22:20] where there is unpredictable randomness
[00:22:22] where there is clearly an arrow of time
[00:22:25] but it's a big mystery in physics
[00:22:26] actually well how that emerges is that
[00:22:29] emergent or is it part of the
[00:22:31] fundamental fabric of reality yeah or is
[00:22:34] it bias of intelligent systems that you
[00:22:37] know because of the second law of
[00:22:38] thermodynamics we perceive a particular
[00:22:40] arrow of time but in fact it's kind of
[00:22:43] arbitrary right so yeah physicists
[00:22:45] mathematicians they don't care about I
[00:22:48] mean the math doesn't care about the
[00:22:50] flow of time well certainly certainly
[00:22:52] macro physics doesn't people themselves
[00:22:54] are not very good at establishing causal
[00:22:57] causal relationships if you ask is I
[00:23:00] think it was in one of Seymour Papert
[00:23:02] spoken on like children learning you
[00:23:06] know he studied with Jean Piaget you
[00:23:07] know he's the guy who co-authored the
[00:23:10] book perceptron with Marvin Minsky that
[00:23:12] kind of killed the first wave
[00:23:13] but but he was actually a learning
[00:23:16] person he in the sense of studying
[00:23:20] learning in humans and machines that's
[00:23:22] what he got interested in for scepter on
[00:23:23] and he wrote that if you ask a little
[00:23:27] kid about what is the cause of the wind
[00:23:32] a lot of kids will say they will think
[00:23:35] for a while and they'll say oh it's the
[00:23:36] the branches in the trees they move and
[00:23:38] that creates wind right so they get the
[00:23:40] causal relationship backwards and it's
[00:23:42] because their understanding of the world
[00:23:44] and intuitive physics is not that great
[00:23:45] right I mean these are like you know
[00:23:47] four or five year old kids you know it
[00:23:50] gets better and then you understand that
[00:23:51] this it can't be right but there are
[00:23:54] many things which we can because of our
[00:23:58] common sense understanding of things
[00:24:00] what people call common sense yeah and
[00:24:03] we understanding of physics we can
[00:24:05] there's a lot of stuff that we can
[00:24:08] figure out causality even with diseases
[00:24:09] we can figure out what's not causing
[00:24:11] what often there's a lot of mystery of
[00:24:15] course but the idea is that you should
[00:24:17] be able to encode that into systems it
[00:24:20] seems unlikely to be able to figure that
[00:24:21] out themselves well whenever we can do
[00:24:23] intervention but you know all of
[00:24:25] humanity has been completely deluded for
[00:24:27] millennia probably since existence about
[00:24:30] a very very wrong causal relationship
[00:24:32] where whatever you can explain you
[00:24:34] attributed to you know some deity some
[00:24:36] divinity right and that's a cop-out
[00:24:39] that's the way of saying like I don't
[00:24:41] know the cause so you know God did it
[00:24:42] right so you mentioned Marvin Minsky and
[00:24:46] the irony of you know maybe causing the
[00:24:52] first day I winter you were there in the
[00:24:55] 90s you're there in the 80s of course in
[00:24:58] the 90s what do you think people lost
[00:24:59] faith and deep learning in the 90s and
[00:25:02] found it again a decade later over a
[00:25:05] decade later yeah it wasn't called
[00:25:07] dethroning yeah it was just called
[00:25:08] neural nets you know
[00:25:10] yeah they lost interests I mean I think
[00:25:14] I would put that around 1995 at least
[00:25:17] the machine learning community there was
[00:25:18] always a neural net community but it
[00:25:19] became
[00:25:22] disconnected from sort of ministry
[00:25:25] machine owning if you want
[00:25:27] there were it was basically electrical
[00:25:30] engineering that kept at it and computer
[00:25:33] science just gave up give up on neural
[00:25:37] nets I don't I don't know you know I was
[00:25:39] too close to it to really sort of
[00:25:43] analyze it with sort of a unbiased eye
[00:25:46] if you want but I would I would I would
[00:25:49] would make a few guesses so the first
[00:25:51] one is at the time neural nets were it
[00:25:56] was very hard to make them work in the
[00:25:58] sense that you would you know implement
[00:26:01] back prop in your favorite language and
[00:26:04] that favorite language was not Python it
[00:26:07] was not MATLAB it was not any of those
[00:26:08] things cuz they didn't exist right you
[00:26:10] had to write it in Fortran or C or
[00:26:13] something like this right so you would
[00:26:17] experiment with it you would probably
[00:26:19] make some very basic mistakes like you
[00:26:21] know badly initialize your weights make
[00:26:23] the network too small because you read
[00:26:24] in the textbook you know you don't want
[00:26:25] too many parameters right and of course
[00:26:28] you know and you would train on x4
[00:26:29] because you didn't have any other data
[00:26:30] set to try it on and of course you know
[00:26:32] it works half the time so we'd say you
[00:26:34] give up also 22 the batch gradient which
[00:26:37] you know isn't it sufficient so there's
[00:26:40] a lot of bag of tricks that you had to
[00:26:43] know to make those things work or you
[00:26:45] had to reinvent and a lot of people just
[00:26:47] didn't and they just couldn't make it
[00:26:49] work so that's one thing the investment
[00:26:53] in software platform to be able to kind
[00:26:56] of you know display things figure out
[00:26:58] why things don't work and I get a good
[00:27:00] intuition for how to get them to work
[00:27:01] have enough flexibility so you can
[00:27:03] create you know network architectures
[00:27:05] well completion ads and stuff like that
[00:27:07] it was hard yeah when you had to write
[00:27:09] everything from scratch and again you
[00:27:10] didn't have any Python or MATLAB or
[00:27:12] anything right so what I read that sorry
[00:27:15] to interrupt but I read he wrote in in
[00:27:17] Lisp the first versions of Lynette
[00:27:21] accomplished in your networks which by
[00:27:23] the way one of my favorite languages
[00:27:24] that's how I knew you were legit the
[00:27:27] Turing Award whatever this would be
[00:27:29] programmed and list that's still my
[00:27:31] favorite language but it's not that we
[00:27:34] programmed in Lisp it's that we had to
[00:27:35] write or this printer printer okay cuz
[00:27:38] it's not that's right that's one that
[00:27:39] existed so
[00:27:41] we wrote a lisp interpreter that we
[00:27:42] hooked up to you know back in library
[00:27:45] that we wrote also for neural net
[00:27:47] competition and then after a few years
[00:27:50] around 1991 we invented this idea of
[00:27:52] basically having modules that know how
[00:27:55] to forward propagate and back propagate
[00:27:56] gradients and then interconnecting those
[00:27:58] modules in a graph loom but who had made
[00:28:02] proposals on this about this in the late
[00:28:04] 80s and were able to implement this
[00:28:06] using all this system eventually we
[00:28:08] wanted to use that system to make build
[00:28:12] production code for character
[00:28:13] recognition at Bell Labs so we actually
[00:28:14] wrote a compiler for that disp
[00:28:16] interpreter so that Christy Martin who
[00:28:18] is now Microsoft kind of did the bulk of
[00:28:20] it with Leone and me and and so we could
[00:28:23] write our system in lisp and then
[00:28:25] compiled to seee and then we'll have a
[00:28:27] self-contained complete system that
[00:28:29] could kind of do the entire thing
[00:28:32] neither Python or turn pro can do this
[00:28:35] today yeah okay it's coming yeah I mean
[00:28:40] there's something like that in
[00:28:41] Whitehorse called you know tor script
[00:28:43] and so you know we had to write or Lisp
[00:28:46] interpreter which retinol is compiler
[00:28:47] way to invest a huge amount of effort to
[00:28:50] do this and not everybody if you don't
[00:28:53] completely believe in the concept
[00:28:54] you're not going to invest the time to
[00:28:56] do this right now at the time also you
[00:28:58] know it were today this would turn into
[00:29:01] torture by torture and so for whatever
[00:29:03] we put it in open-source everybody would
[00:29:05] use it and you know realize it's good
[00:29:07] back before 1995 working at AT&T there's
[00:29:11] no way the lawyers would let you release
[00:29:14] anything in open source of this nature
[00:29:16] and so we could not distribute our code
[00:29:19] really and at that point and sorry to go
[00:29:22] on a million tangents but on that point
[00:29:24] I also read that there was some almost
[00:29:26] pad like a patent on convolution your
[00:29:29] network yes it was labs so that first of
[00:29:34] all I mean just to actually that ran out
[00:29:38] the thankfully 8007 in 2007 that what
[00:29:45] look can we can we just talk about that
[00:29:48] first I know you're a facebook but
[00:29:49] you're also done why you and and what
[00:29:52] does it mean
[00:29:54] patent ideas like these software ideas
[00:29:58] essentially or what are mathematical
[00:30:01] ideas or what are they okay so they're
[00:30:04] not mathematical idea so there are you
[00:30:06] know algorithms and there was a period
[00:30:08] where the US Patent Office would allow
[00:30:11] the patent of software as long as it was
[00:30:14] embodied the Europeans are very
[00:30:17] different they don't they don't quite
[00:30:19] accept that they have a different
[00:30:20] concept but you know I don't I know no I
[00:30:24] mean I never actually strongly believed
[00:30:25] in this but I don't believe in this kind
[00:30:27] of patent Facebook basically doesn't
[00:30:29] believe in this kind of pattern
[00:30:33] Google Files patterns because they've
[00:30:37] been burned with Apple and so now they
[00:30:40] do this for defensive purpose but
[00:30:41] usually they say we're not going to see
[00:30:43] you if you infringe Facebook has a
[00:30:45] similar policy they say you know we file
[00:30:48] pattern on certain things for defensive
[00:30:50] purpose we're not going to see you if
[00:30:51] you infringe unless you sue us
[00:30:53] so the the industry does not believe in
[00:30:58] in patterns they are there because of
[00:31:00] you know the legal landscape and and and
[00:31:02] various things but but I don't really
[00:31:05] believe in patterns for this kind of
[00:31:06] stuff yes so that's that's a great thing
[00:31:09] so I tell you a war story yeah you so
[00:31:11] what happens was the the first the first
[00:31:14] pattern of a condition that was about
[00:31:15] kind of the early version Congress on
[00:31:18] that that didn't have separate pudding
[00:31:19] layers it had the conditional layers
[00:31:22] which tried more than one if you want
[00:31:24] right and then there was a second one on
[00:31:27] commercial nets with separate pudding
[00:31:29] layers
[00:31:30] train with back probably in 89 and 1992
[00:31:35] something like this at the time the life
[00:31:37] life of a pattern was 17 years so here's
[00:31:40] what happened over the next few years is
[00:31:42] that we started developing character
[00:31:44] recognition technology around commercial
[00:31:47] Nets
[00:31:47] and in 1994 a check reading system was
[00:31:53] deployed in ATM machines in 1995 it was
[00:31:57] for a large check reading machines in
[00:31:59] back offices etc and those systems were
[00:32:02] developed by an engineering group that
[00:32:04] we were collaborating with AT&T and they
[00:32:07] were commercialized by NCR which at the
[00:32:08] time was a subsidiary of AT&T now it
[00:32:11] ain't he split up in 1996
[00:32:15] 99 in 1996 and the lawyers just looked
[00:32:19] at all the patterns and they distributed
[00:32:21] the patterns among the various companies
[00:32:22] they gave the the commercial net pattern
[00:32:25] to NCR because they were actually
[00:32:27] selling products that used it but nobody
[00:32:29] I didn't see are at any idea where they
[00:32:30] come from that was yeah okay so between
[00:32:34] 1996 and 2007
[00:32:38] there's a whole period until 2002 I
[00:32:39] didn't actually work on machine on your
[00:32:42] couch on that I resumed working on this
[00:32:43] around 2002 and between 2002 and 2007 I
[00:32:47] was working on them crossing my finger
[00:32:49] that nobody and NCR would notice nobody
[00:32:51] noticed yeah and I and I hope that this
[00:32:54] kind of somewhat as you said lawyers
[00:32:57] decide relative openness of the
[00:33:00] community now will continue
[00:33:02] it accelerates the entire progress of
[00:33:04] the industry and you know the problems
[00:33:09] that Facebook and Google and others are
[00:33:12] facing today is not whether Facebook or
[00:33:14] Google or Microsoft or IBM or whoever is
[00:33:16] ahead of the other it's that we don't
[00:33:19] have the technology to build the things
[00:33:20] we want to build we only build
[00:33:21] intelligent virtual systems that have
[00:33:23] common sense we don't have a monopoly on
[00:33:25] good ideas for this we don't believe
[00:33:27] with you maybe others do believe they do
[00:33:29] but we don't okay if a start-up tells
[00:33:32] you they have the secret to you know
[00:33:34] human level intelligence and common
[00:33:36] sense don't believe them they don't and
[00:33:38] it's going to take the entire work of
[00:33:42] the world research community for a while
[00:33:44] to get to the point where you can go off
[00:33:47] and in each of the company is going to
[00:33:49] start to build things on this we're not
[00:33:50] there yet
[00:33:51] it's absolutely in this this calls to
[00:33:53] the the gap between the space of ideas
[00:33:56] and the rigorous testing of those ideas
[00:33:59] of practical application that you often
[00:34:02] speak to you've written advice saying
[00:34:05] don't get fooled by people who claim to
[00:34:07] have a solution to artificial general
[00:34:09] intelligence who claim to have an AI
[00:34:11] system that work just like the human
[00:34:13] brain or who claim to have figured out
[00:34:15] how the brain works ask them what the
[00:34:18] error rate they get on em 'no store
[00:34:21] imagenet this is a little dated by the
[00:34:24] way that mean five years who's counting
[00:34:28] okay but i think your opinion it's the
[00:34:30] Amna stand imagenet yes may be data
[00:34:34] there may be new benchmarks right but i
[00:34:36] think that philosophy is one you still
[00:34:39] and and somewhat hold that benchmarks
[00:34:43] and the practical testing the practical
[00:34:45] application is where you really get to
[00:34:46] test the ideas well it may not be
[00:34:48] completely practical like for example
[00:34:50] you know it could be a toy data set
[00:34:52] but it has to be some sort of task that
[00:34:54] the community as a whole has accepted as
[00:34:57] some sort of standard you know kind of
[00:34:59] benchmark if you want it doesn't need to
[00:35:01] be real so for example many years ago
[00:35:03] here at fair people you know chosen
[00:35:06] Western art one born and a few others
[00:35:07] proposed the the babbitt asks which were
[00:35:09] kind of a toy problem to test the
[00:35:12] ability of machines to reason actually
[00:35:14] to access working memory and things like
[00:35:16] this and it was very useful even though
[00:35:19] it wasn't a real task amnesties kind of
[00:35:20] halfway a real task so you know toy
[00:35:24] problems can be very useful it's just
[00:35:26] that i was really struck by the fact
[00:35:28] that a lot of people particularly our
[00:35:30] people with money to invest would be
[00:35:32] fooled by people telling them oh we have
[00:35:34] you know the algorithm of the cortex and
[00:35:37] you should give us 50 million yes
[00:35:39] absolutely so there's a lot of people
[00:35:42] who who tried to take advantage of the
[00:35:45] hype for business reasons and so on but
[00:35:48] let me sort of talk to this idea that
[00:35:52] new ideas the ideas that push the field
[00:35:55] forward
[00:35:55] may not yet have a benchmark or it may
[00:35:58] be very difficult to establish a
[00:36:00] benchmark I agree that's part of the
[00:36:01] process establishing benchmarks is part
[00:36:03] of the process so what are your thoughts
[00:36:06] about so we have these benchmarks on
[00:36:08] around stuff we can do with images from
[00:36:12] classification to captioning to just
[00:36:15] every kind of information can pull off
[00:36:16] from images and the surface level
[00:36:18] there's audio datasets there's some
[00:36:20] video what can we start natural language
[00:36:25] what kind of stuff what kind of
[00:36:27] benchmarks do you see they start
[00:36:29] creeping on to more something like
[00:36:32] intelligence like reasoning like maybe
[00:36:36] you don't like the term but AGI echoes
[00:36:38] of that kind of yeah sort of elation a
[00:36:41] lot of people are working on interactive
[00:36:43] environments in which you can you can
[00:36:45] train and test intelligent systems so so
[00:36:48] there for example you know it's the
[00:36:53] classical paradigm of supervised running
[00:36:56] is that you you have a data set you
[00:36:58] partition it into a training site
[00:36:59] validation set test set and there's a
[00:37:01] clear protocol right but what if the
[00:37:04] that assumes that this
[00:37:06] apples are statistically independent you
[00:37:08] can exchange them the order in which you
[00:37:10] see them doesn't shouldn't matter you
[00:37:12] know things like that but what if the
[00:37:14] answer you give determines the next
[00:37:16] sample you see which is the case for
[00:37:18] example in robotics right you robot does
[00:37:20] something and then it gets exposed to a
[00:37:22] new room and depending on where it goes
[00:37:24] the room would be different so that's
[00:37:26] the decrease the exploration problem
[00:37:29] the what if the samples so that creates
[00:37:33] also a dependency between samples right
[00:37:35] you you if you move if you can only move
[00:37:38] it in in space the next sample you're
[00:37:40] gonna see is going to be probably in the
[00:37:41] same building most likely so so so the
[00:37:45] all the assumptions about the validity
[00:37:47] of this training set test set a potus's
[00:37:50] break whatever a machine can take an
[00:37:52] action that has an influence in the in
[00:37:54] the world and it's what is going to see
[00:37:56] so people are setting up artificial
[00:37:58] environments where what that takes place
[00:38:01] right the robot runs around a 3d model
[00:38:05] of a house and can interact with objects
[00:38:07] and things like this how you do robotics
[00:38:09] by simulation you have those you know
[00:38:12] opening a gym type thing or mu Joko kind
[00:38:15] of simulated robots and you have games
[00:38:19] you know things like that so that that's
[00:38:21] where the field is going really this
[00:38:23] kind of environment now back to the
[00:38:27] question of a GI like I don't like the
[00:38:29] term a GI because it implies that human
[00:38:33] intelligence is general and human
[00:38:36] intelligence is nothing like general
[00:38:38] it's very very specialized we think it's
[00:38:41] general we'd like to think of ourselves
[00:38:42] as having your own science we don't
[00:38:44] we're very specialized we're only
[00:38:46] slightly more general than why does it
[00:38:47] feel general so you kind of the term
[00:38:50] general I think what's impressive about
[00:38:53] humans is ability to learn as we were
[00:38:56] talking about learning to learn in just
[00:38:59] so many different domains is perhaps not
[00:39:02] arbitrarily general but just you can
[00:39:05] learn in many domains and integrate that
[00:39:07] knowledge somehow okay that knowledge
[00:39:09] persists so let me take a very specific
[00:39:10] example yes it's not an example it's
[00:39:13] more like a a quasi mathematical
[00:39:16] demonstration so you have about 1
[00:39:17] million fibers coming out of
[00:39:19] one of your eyes okay two million total
[00:39:21] but let's let's talk about just one of
[00:39:22] them it's 1 million nerve fibers your
[00:39:25] optical nerve let's imagine that they
[00:39:28] are binary so they can be active or
[00:39:29] inactive right so the input to your
[00:39:31] visual cortex is 1 million bits
[00:39:36] now they connected to your brain in a
[00:39:38] particular way on your brain has
[00:39:40] connections that are kind of a little
[00:39:43] bit like accomplish on that they're kind
[00:39:44] of local you know in space and things
[00:39:47] like this I imagine I play a trick on
[00:39:48] you it's a pretty nasty trick I admit I
[00:39:52] I cut your optical nerve and I put a
[00:39:56] device that makes a random perturbation
[00:39:57] of a permutation of all the nerve fibers
[00:40:01] so now what comes to your to your brain
[00:40:04] is a fixed but random permutation of all
[00:40:07] the pixels there's no way in hell that
[00:40:09] your visual cortex even if I do this to
[00:40:12] you in infancy will actually learn
[00:40:16] vision to the same level of quality that
[00:40:18] you can got it and you're saying there's
[00:40:21] no way you ever learn that no because
[00:40:23] now two pixels that on your body in the
[00:40:25] world will end up in very different
[00:40:27] places in your visual cortex and your
[00:40:29] neurons there have no connections with
[00:40:31] each other because they only connect it
[00:40:32] locally so this whole our entire the
[00:40:35] hardware is built in many ways to
[00:40:37] support the locality of the real world
[00:40:39] yeah yes that's specialization yep okay
[00:40:42] it's still now really damn impressive so
[00:40:44] it's not perfect generalization I even
[00:40:46] closed no no it's it's it's it's not
[00:40:49] that it's not even close it's not at all
[00:40:50] yes it's socialize so how many boolean
[00:40:53] functions so let's imagine you want to
[00:40:55] train your visual system to you know
[00:41:00] recognize particular patterns of those 1
[00:41:02] million bits ok so that's a boolean
[00:41:04] function right either the pattern is
[00:41:06] here or not here this is a to to a
[00:41:08] classification with 1 million binary
[00:41:10] inputs
[00:41:13] how many such boolean functions are
[00:41:14] there okay if you have 2 to the 1
[00:41:18] million combinations of inputs for each
[00:41:21] of those you have an output bit and so
[00:41:24] you have 2 to the 2 to the 1 million
[00:41:26] boolean functions of this type okay
[00:41:29] which is an unimaginably large number
[00:41:32] how many of those functions can actually
[00:41:35] be computed by your visual cortex and
[00:41:36] the answer is a tiny tiny tiny tiny tiny
[00:41:39] tiny sliver like an enormous little tiny
[00:41:42] sliver yeah yeah so we are ridiculously
[00:41:46] specialized you know okay but okay
[00:41:51] that's an argument against the word
[00:41:53] general I think there's there's a I
[00:41:56] there's I agree with your intuition but
[00:41:59] I'm not sure it's it seems the breath
[00:42:01] the the brain is impressively capable of
[00:42:07] adjusting to things so it's because we
[00:42:10] can't imagine tasks that are outside of
[00:42:14] our comprehension right we think we
[00:42:17] think we are general because we're
[00:42:18] general of all the things that we can
[00:42:19] apprehend so yeah but there is a huge
[00:42:22] world out there of things that we have
[00:42:23] no idea
[00:42:24] we call that heat by the way heat heat
[00:42:27] so at least physicists call that heat or
[00:42:30] they call it entropy which is kokkonen
[00:42:32] you have a thing full of gas right call
[00:42:39] system for gas right goes on a coast it
[00:42:42] has you know pressure it has temperature
[00:42:47] has you know and you can write the
[00:42:50] equations PV equal NRT you know things
[00:42:53] like that right when you reduce a volume
[00:42:56] the temperature goes up the pressure
[00:42:57] goes up you know things like that right
[00:42:59] for perfect gas at least those are the
[00:43:02] things you can know about that system
[00:43:05] and it's a tiny tiny number of bits
[00:43:07] compared to the complete information of
[00:43:09] the state of the entire system because
[00:43:10] the state when HR system will give you
[00:43:12] the position and momentum of every every
[00:43:15] molecule of the gas and what you don't
[00:43:19] know about it is the entropy and you
[00:43:22] interpret it as heat the energy
[00:43:24] containing that thing is is what we call
[00:43:27] heat now it's very possible that in fact
[00:43:32] there is some very strong structure in
[00:43:33] how those molecules are moving is just
[00:43:35] that they are in a way that we are just
[00:43:37] not wired to perceive they are ignorant
[00:43:39] to it and there's in your infinite
[00:43:42] amount of things we're not wired to
[00:43:44] perceive any right that's a nice way to
[00:43:46] put it
[00:43:47] well general to all the things we can
[00:43:48] imagine which is a very tiny a subset of
[00:43:53] all things that are possible it was like
[00:43:55] coma growth complexity or the coma was
[00:43:56] charged in some one of complexity you
[00:44:00] know every bit string or every integer
[00:44:03] is random except for all the ones that
[00:44:06] you can actually write down yeah okay so
[00:44:12] beautifully put but you know so we can
[00:44:13] just call it artificial intelligence we
[00:44:15] don't need to have a general whatever
[00:44:18] novel
[00:44:18] human of all Nutella transmissible oh
[00:44:20] you know you'll start anytime you touch
[00:44:24] human it gets it gets interesting
[00:44:26] because you know it's just because we
[00:44:32] attach ourselves to human and it's
[00:44:33] difficult to define with human
[00:44:35] intelligences yeah
[00:44:36] nevertheless my definition is maybe damn
[00:44:41] impressive intelligence ok damn
[00:44:44] impressive demonstration of intelligence
[00:44:45] whatever and so on that topic most
[00:44:49] successes in deep learning have been in
[00:44:51] supervised learning what is your view on
[00:44:56] unsupervised learning is there a hope to
[00:44:59] reduce involvement of human input and
[00:45:02] still have successful systems that are
[00:45:05] have practically used yeah I mean
[00:45:08] there's definitely a hope is it's more
[00:45:10] than a hope actually it's it's you know
[00:45:12] mounting evidence for it and that's
[00:45:14] basically or I do like the only thing
[00:45:17] I'm interested in at the moment is
[00:45:19] I call it self supervised running not
[00:45:20] unsupervised cuz unsupervised running is
[00:45:22] a loaded term people who know something
[00:45:26] about machine learning you know tell us
[00:45:28] how you doing clustering or PCA yeah
[00:45:30] she's nice and the way public we know
[00:45:32] when you say enterprise only oh my god
[00:45:34] you know machines are gonna learn by
[00:45:35] themselves and without supervision you
[00:45:37] know there's the parents yeah so so I
[00:45:41] could sell supervised learning because
[00:45:43] in fact the underlying algorithms that I
[00:45:45] use are the same algorithms as the
[00:45:47] supervised learning algorithms except
[00:45:50] that what we trained them to do is not
[00:45:52] predict a particular set of variables
[00:45:55] like the category of an image and and
[00:46:00] not to predict a set of variables that
[00:46:02] have been provided by human labelers but
[00:46:06] what you're trying to machine to do is
[00:46:07] basically reconstruct a piece of its
[00:46:09] input that it's being this being masked
[00:46:12] masked out essentially you can think of
[00:46:14] it this way right so show a piece of a
[00:46:17] video to a machine and ask it to predict
[00:46:19] what's gonna happen next and of course
[00:46:21] after a while you can show what what
[00:46:23] happens and the machine will kind of
[00:46:25] train itself to do better at that task
[00:46:27] you can do like all the latest most
[00:46:31] successful models the natural language
[00:46:32] processing use cell supervised running
[00:46:35] you know sort of bird style systems for
[00:46:38] example right you show it a window of a
[00:46:40] thousand words on a test corpus you take
[00:46:44] out 15% of the words and then you train
[00:46:47] a machine to predict the words that are
[00:46:50] missing that's out supervised running
[00:46:52] it's not predicting the future it's just
[00:46:54] you know predicting things in middle but
[00:46:56] you could have you predict the future
[00:46:57] that's what language models do so you
[00:46:59] construct it so in an unsupervised way
[00:47:01] you construct a model of language do you
[00:47:04] think or video or the physical world or
[00:47:07] whatever right how far do you think that
[00:47:10] can take us do you think very far it
[00:47:14] understands anything to some level it
[00:47:18] has you know a shallow understanding of
[00:47:22] of text but it needs to I mean to have
[00:47:25] kind of true human level intelligence I
[00:47:26] think you need to ground language in
[00:47:28] reality so some people are attempting to
[00:47:32] do this right having systems that can I
[00:47:34] have some visual representation of what
[00:47:35] what is being talked about which is one
[00:47:37] reason you need interactive environments
[00:47:39] actually this is like a huge technical
[00:47:43] problem that is not solved and that
[00:47:45] explains why such super versioning works
[00:47:47] in the context of natural language that
[00:47:50] does not work in the context on at least
[00:47:52] not well in the context of image
[00:47:53] recognition and video although it's
[00:47:55] making progress quickly and the reason
[00:47:58] that reason is the fact that it's much
[00:48:02] easier to represent uncertainty in the
[00:48:04] prediction you know context of natural
[00:48:06] language than it is in the context of
[00:48:08] things like video and images so for
[00:48:10] example if I ask you to predict what
[00:48:13] words are missing you know 15 percent of
[00:48:14] the words that I've taken out the
[00:48:17] possibility is small that means small
[00:48:19] right there is 100,000 words in the in
[00:48:22] the lexicon and what the Machine spits
[00:48:24] out is a big probability vector right
[00:48:27] it's a bunch of numbers between 0 & 1
[00:48:29] that's 1 to 1 and we know how to do how
[00:48:31] to do this with computers so they are
[00:48:34] representing uncertainty in the
[00:48:36] prediction is relatively easy and that's
[00:48:38] in my opinion why those techniques work
[00:48:40] for NLP for images if you ask if you
[00:48:45] block a piece of an image and you as a
[00:48:47] system reconstruct that piece of the
[00:48:48] image
[00:48:49] there are many possible answers there
[00:48:51] are all perfectly legit right and how do
[00:48:55] you represent that the set of possible
[00:48:58] answers
[00:48:58] you can't train a system to make one
[00:49:00] prediction you can train a neural net to
[00:49:01] say here it is that's the image because
[00:49:04] it's there's a whole set of things that
[00:49:06] are compatible with it so how do you get
[00:49:07] the machine to represent not a single
[00:49:09] output but all set of outputs and you
[00:49:14] know similarly with video prediction
[00:49:16] there's a lot of things that can happen
[00:49:18] in the future video you're looking at me
[00:49:20] right now I'm not moving my head very
[00:49:22] much but you know I might you know what
[00:49:24] turn my my head to the left or to the
[00:49:25] right right if you don't have a system
[00:49:27] that can predict this and you train it
[00:49:31] with least Square to kind of minimize
[00:49:32] the error with the prediction and what
[00:49:33] I'm doing
[00:49:34] what you get is a blurry image of myself
[00:49:36] in all possible future positions that I
[00:49:38] might be in which is not a good
[00:49:40] prediction but so there might be other
[00:49:42] ways to do the self supervision right
[00:49:45] for visual scenes like what if i I mean
[00:49:50] if I knew I wouldn't tell you
[00:49:52] publish it first I don't know I know
[00:49:55] there might be so I mean these are kind
[00:49:58] of there might be artificial ways of
[00:50:01] like self play in games the way you can
[00:50:03] simulate part of the environment you can
[00:50:05] oh that doesn't solve the problem it's
[00:50:06] just a way of generating data but
[00:50:10] because you have more of a country might
[00:50:12] mean you can control yeah it's a way to
[00:50:15] generate data and that's right and
[00:50:16] because you can do huge amounts of data
[00:50:18] generation that doesn't you write this
[00:50:21] well it's it's a creeps up on the
[00:50:23] problem from the side of data and you
[00:50:26] don't think that's the right way to it
[00:50:27] doesn't solve this problem of handling
[00:50:29] uncertainty in the world right so if you
[00:50:31] if you have a machine learn a predictive
[00:50:34] model of the world in a game that is
[00:50:37] deterministic or quasi deterministic
[00:50:39] it's easy right just you know give a few
[00:50:43] frames of the game to a combat put a
[00:50:46] bunch of layers and then half the game
[00:50:47] generates the next few frames and and if
[00:50:50] the game is deterministic it works fine
[00:50:53] and that includes you know feeding the
[00:50:58] system with the action that your little
[00:51:00] character is going to take
[00:51:02] the problem comes from the fact that the
[00:51:06] real world and certain most games are
[00:51:08] not entirely predictable that's what
[00:51:09] they're you get those blurry predictions
[00:51:11] and you can't do planning with very
[00:51:12] predictions all right so if you have a
[00:51:15] perfect model of the world you can in
[00:51:18] your head run this model with a
[00:51:21] hypothesis for a sequence of actions and
[00:51:24] you're going to predict the outcome of
[00:51:25] that sequence of actions but if your
[00:51:28] model is imperfect how can you plan yeah
[00:51:32] it quickly explodes what are your
[00:51:35] thoughts on the extension of this which
[00:51:37] topic I'm super excited about it's
[00:51:39] connected to something you're talking
[00:51:41] about in terms of robotics is active
[00:51:43] learning so as opposed to sort of
[00:51:46] unemployed and supervisors self
[00:51:48] supervised learning you ask the system
[00:51:52] for human help right for selecting parts
[00:51:56] you want annotated next so if you talk
[00:51:58] about a robot exploring a space or a
[00:52:00] baby exploring a space or a system
[00:52:03] exploring a data set every once in a
[00:52:06] while asking for human input you see
[00:52:08] value in that kind of work I don't see
[00:52:12] transformative value it's going to make
[00:52:15] things that we can already do more
[00:52:18] efficient or they will learn slightly
[00:52:19] more efficiently but it's not going to
[00:52:21] make machines sort of significantly more
[00:52:23] intelligent I think and I and by the way
[00:52:26] there is no opposition there is no
[00:52:31] conflict between self supervisor on
[00:52:34] reinforcement learning and supervisor on
[00:52:35] your imitation learning or active
[00:52:37] learning
[00:52:37] I see sub super wrestling as a as a
[00:52:41] preliminary to all of the above yes so
[00:52:45] the example I use very often is how is
[00:52:48] it that so if you use
[00:52:53] enforcement running deep enforcement
[00:52:55] running if you want the best methods
[00:52:58] today was so-called model free
[00:53:02] enforcement training to learn to play
[00:53:03] Atari games take about 80 hours of
[00:53:06] training to reach the level that any
[00:53:08] human can reach in about 15 minutes they
[00:53:12] get better than humans but it takes a
[00:53:14] long time alpha star okay the you know
[00:53:21] are your videos and his team's the
[00:53:23] system to play to to play Starcraft
[00:53:27] plays you know a single map a single
[00:53:30] type of player and
[00:53:34] which
[00:53:36] better than human level is about the
[00:53:40] equivalent of 200 years of training
[00:53:42] playing against itself it's 200 years
[00:53:45] right it's not something that no no
[00:53:47] human can could every I'm not sure what
[00:53:50] it doesn't take away from that okay now
[00:53:53] take those algorithms the best our
[00:53:55] algorithms we have today to train a car
[00:53:59] to drive itself it would probably have
[00:54:01] to drive millions of hours you will have
[00:54:04] to kill thousands of pedestrians it will
[00:54:05] have to run into thousands of trees it
[00:54:07] will have to run off cliffs and you had
[00:54:10] to run the cliff multiple times before
[00:54:11] it figures out it's a bad idea first of
[00:54:14] all
[00:54:14] yeah and second of all the figures that
[00:54:16] had not to do it and so I mean this type
[00:54:19] of running obviously does not reflect
[00:54:21] the kind of running that animals and
[00:54:23] humans do there is something missing
[00:54:25] that's really really important there and
[00:54:26] my apart is is which have been
[00:54:29] advocating for like five years now is
[00:54:31] that we have predictive models of the
[00:54:34] world that include the ability to
[00:54:37] predict under uncertainty and what
[00:54:40] allows us to not run off a cliff when we
[00:54:44] learn to drive most of us can learn to
[00:54:46] drive in about 20 or 30 hours of
[00:54:48] training without ever crashing causing
[00:54:50] any accident if we drive next to a cliff
[00:54:53] we know that if we turn the wheel to the
[00:54:55] right the car is going to run off the
[00:54:57] cliff and nothing good is gonna come out
[00:54:59] of this because we have a pretty good
[00:55:00] model of intuitive physics that tells us
[00:55:02] you know the car is gonna fall we know
[00:55:03] we know about gravity babies run this
[00:55:05] around the age of eight or nine months
[00:55:07] that objects don't float they fall and
[00:55:12] you know we have a pretty good idea of
[00:55:14] the effect of turning the wheel of the
[00:55:15] car and you know we know we need to stay
[00:55:17] on the road so there is a lot of things
[00:55:18] that we bring to the table which is
[00:55:20] basically or predictive model of the
[00:55:22] world and that model allows us to not do
[00:55:26] stupid things and to basically stay
[00:55:28] within the context of things we need to
[00:55:30] do we still face you know unpredictable
[00:55:33] situations and that's how we learn but
[00:55:35] that allows us to learn really really
[00:55:38] really quickly so that's called
[00:55:39] model-based reinforcement running
[00:55:42] there's some imitation and supervised
[00:55:43] running because we have a driving
[00:55:45] instructor that tells us occasionally
[00:55:47] what to do but most of the learning is
[00:55:50] Mauro bass is learning the model yeah
[00:55:53] running physics that we've done since we
[00:55:55] were babies that's where all almost all
[00:55:57] are learning and the physics is somewhat
[00:55:59] transferable from is transferable from
[00:56:02] scene to scene stupid things are the
[00:56:04] same everywhere yeah I mean if you you
[00:56:06] know you have experience of the world
[00:56:08] you don't need to be particularly from a
[00:56:11] particularly intelligent species to know
[00:56:12] that if you spill water from a container
[00:56:16] you know the rest is gonna get wet and
[00:56:20] you might get wet so you know cats know
[00:56:23] this right yeah so the main problem we
[00:56:26] need to solve is how do we learn models
[00:56:29] of the world that's and that's what I'm
[00:56:30] interesting that's what's a supervised
[00:56:32] learning is all about if you were to try
[00:56:34] to construct a benchmark for let's let's
[00:56:39] look at happiness I'd love that dataset
[00:56:41] but if you do you think it's useful
[00:56:45] interesting / possible to perform well
[00:56:50] on eminence with just one example of
[00:56:52] each digit and how would we solve that
[00:56:56] problem
[00:56:58] yeah so it's probably yes the question
[00:56:59] is what other type of running are you
[00:57:02] allowed to do so if what you like to do
[00:57:04] is train on some gigantic data set of
[00:57:06] labelled digit that's called transfer
[00:57:07] running and we know that works okay
[00:57:11] we do this at Facebook like in
[00:57:12] production right we we train large
[00:57:15] commercial nets to predict hashtags that
[00:57:17] people type on Instagram and we train on
[00:57:18] billions of images literally billions
[00:57:20] and and then we chop off the last layer
[00:57:22] and fine-tune on whatever task we want
[00:57:24] that works really well you can be you
[00:57:27] know the image net record with we
[00:57:28] actually open source the whole thing
[00:57:30] like a few weeks ago yeah that's still
[00:57:32] pretty cool but yeah so what in yet
[00:57:34] won't be impressive and what's useful an
[00:57:37] impressive what kind of transfer
[00:57:38] learning would be useful impressive is
[00:57:40] it Wikipedia that kind of thing no no I
[00:57:42] don't think transfer learning is really
[00:57:45] where we should focus we should try to
[00:57:47] do
[00:57:49] you know have a kind of scenario for
[00:57:51] benchmark where you have only ball data
[00:57:54] and you can and it's very large number
[00:57:58] of enabled data it could be video clips
[00:58:01] it could be what you do you know frame
[00:58:04] prediction it could be images you could
[00:58:06] choose to you know mask a piece of it it
[00:58:11] could be whatever but they're only bold
[00:58:13] and you're not allowed to label them so
[00:58:15] you do some training on this and then
[00:58:19] you train on a particular supervised
[00:58:23] task imagenet or nist and you measure
[00:58:27] how your test our decrease or variation
[00:58:31] error decreases as you increase the
[00:58:32] number of label training samples okay
[00:58:36] and and what what you would like to see
[00:58:40] is is that you know your your error
[00:58:43] decreases much faster than if you
[00:58:45] trained from scratch from random weights
[00:58:47] so that to reach the same level of
[00:58:49] performance and a completely supervised
[00:58:51] purely supervised system would reach you
[00:58:54] would need way fewer samples so that's
[00:58:56] the crucial question because it will
[00:58:58] answer the question to like you know
[00:59:00] people are interested in medical image
[00:59:01] analysis okay you know if I want to get
[00:59:03] to a particular level of error rate for
[00:59:07] this task I know I need a million
[00:59:11] samples can I do you know soft
[00:59:14] supervised pre-training to reduce this
[00:59:15] to about 100 or something anything the
[00:59:18] answer there is soft supervised
[00:59:19] retraining yep some form some form of it
[00:59:24] telling you active learning but you
[00:59:27] disagree you know it's not useless it's
[00:59:30] just not gonna lead to a quantum leap
[00:59:32] it's just gonna make things that we
[00:59:33] already do so you're way smarter than me
[00:59:35] I just disagree with you but I don't
[00:59:37] have anything to back that it's just
[00:59:39] intuition so I've worked a lot of
[00:59:41] large-scale data sets and there's
[00:59:43] something there might be magic and
[00:59:45] active learning but okay at least I said
[00:59:48] it publicly at least some being an idea
[00:59:51] publicly okay it's not bigoted yet it's
[00:59:54] you know working with the data you have
[00:59:56] I mean I mean certainly people are doing
[00:59:57] things like okay I have three thousand
[00:59:59] hours of you know imitation running for
[01:00:02] in car but most of those are incredibly
[01:00:04] boring what I like is select you know
[01:00:07] 10% of them that are kind of the most
[01:00:08] informative and with just that I would
[01:00:10] probably reach the same so it's a weak
[01:00:13] form of of active running if you want
[01:00:16] yes but there might be a much stronger
[01:00:19] version yeah that's right that's what
[01:00:21] another notion question is the question
[01:00:24] is how much talking yet Elon Musk is
[01:00:27] confident talk to him recently
[01:00:30] he's confident that large-scale data and
[01:00:32] deep learning can solve the autonomous
[01:00:33] driving problem what are your thoughts
[01:00:36] on the limitless possibilities of deep
[01:00:39] learning in this space I was it's
[01:00:40] obviously part of the solution I mean I
[01:00:43] don't think we'll ever have a set
[01:00:44] driving system or it is not in the
[01:00:46] foreseeable future that does not use
[01:00:48] deep running you put it this way now how
[01:00:51] much of it so in the history of sort of
[01:00:54] engineering particularly is sort of sort
[01:00:58] of a I like systems is generally your
[01:01:01] first phase where everything is built by
[01:01:02] hand and it was the second phase and
[01:01:04] that was the case for autonomous driving
[01:01:06] you know 23 years ago there's a phase
[01:01:08] where this a little bit of running is
[01:01:10] used but there's a lot of engineering
[01:01:12] that's involved in kind of you know
[01:01:14] taking care of corner cases and and
[01:01:16] putting limits etc because the learning
[01:01:19] system is not perfect and then I as
[01:01:21] technology progresses we end up relying
[01:01:25] more and more on learning that's the
[01:01:26] history of character recognition is a
[01:01:27] history of speech recognition now
[01:01:29] computer vision that ronnie was
[01:01:30] processing and I think the same is going
[01:01:32] to happen with with the term is driving
[01:01:35] that currently the the the methods that
[01:01:39] are closest to providing some level of
[01:01:42] autonomy some you know a decent level of
[01:01:44] autonomy where you don't expect a driver
[01:01:46] to kind of do anything is where you
[01:01:49] constrain the world so you only run
[01:01:51] within you know 100 square kilometers or
[01:01:53] square miles in Phoenix but the weather
[01:01:55] is nice and the roads are wide it wishes
[01:01:58] what Weimer is doing you completely over
[01:02:01] engineer the car with tons of light
[01:02:04] hours and sophisticated sensors that are
[01:02:07] too expensive for consumer cars but
[01:02:09] they're fine if you just run a fleet
[01:02:12] and you engineer the thing the hell out
[01:02:15] of the everything else you you map the
[01:02:17] entire world so you have complete 3d
[01:02:19] model of everything so the only thing
[01:02:21] that the perception system has to take
[01:02:22] care of is moving objects and and and
[01:02:25] construction and sort of you know things
[01:02:27] that that weren't in your map and you
[01:02:31] can engineer a good you know slam system
[01:02:32] or eye stuff right so so that's kind of
[01:02:35] the current approach that's closest to
[01:02:36] some level of autonomy but I think
[01:02:37] eventually the long term solution is
[01:02:39] going to rely more and more on learning
[01:02:43] and possibly using a combination of
[01:02:45] supervised learning and model-based
[01:02:48] reinforcement or something like that but
[01:02:50] ultimately learning will be at not just
[01:02:54] at the core but really the fundamental
[01:02:55] part of the system yeah it already is
[01:02:58] but it'll become more and more what do
[01:03:00] you think it takes to build a system
[01:03:02] with human level intelligence you talked
[01:03:04] about the AI system and then we her
[01:03:06] being way out of reach our current reach
[01:03:09] this might be outdated as well but this
[01:03:12] is still way out of reach what would it
[01:03:16] take to build her do you think so I can
[01:03:20] tell you the first two obstacles that we
[01:03:21] have to clear but I don't know how many
[01:03:23] obstacles they are after this so the
[01:03:25] image I usually use is that there is a
[01:03:26] bunch of mountains that we have to climb
[01:03:28] and we can see the first one but we
[01:03:29] don't know if there are 50 mountains
[01:03:31] behind it or not and this might be a
[01:03:33] good sort of metaphor for why AI
[01:03:37] researchers in the past I've been overly
[01:03:38] optimistic about the result of AI you
[01:03:43] know for example New Orleans Simon
[01:03:46] Wright wrote the general problem solver
[01:03:48] and they call it the general problems
[01:03:51] you have problems okay and of course if
[01:03:53] it's you realize is that all the
[01:03:54] problems you want to solve is financial
[01:03:56] and so you can't actually use it for
[01:03:57] anything useful but you know yes oh yeah
[01:04:00] all you see is the first peak so in
[01:04:02] general what are the first couple of
[01:04:03] peaks for her so the first peak which is
[01:04:06] precisely what I'm working on is self
[01:04:09] supervisor running high how do we get
[01:04:10] machines to learn models of the world by
[01:04:12] observation kind of like babies and like
[01:04:14] young animals
[01:04:17] so I we've been working with you know
[01:04:21] cognitive scientists so this Amanda
[01:04:24] depuis who is at fair and in Paris is
[01:04:28] half-time is also a researcher and
[01:04:31] French University and he he has his
[01:04:35] chart that shows that which how many
[01:04:38] months of life baby humans kind of
[01:04:40] learned different concepts and you can
[01:04:43] met you can measure this various ways so
[01:04:47] things like distinguishing animate
[01:04:50] objects from animate inanimate object
[01:04:52] you can you can tell the difference at
[01:04:54] age to three months whether an object is
[01:04:58] going to stay stable is gonna fall you
[01:04:59] know about four months you can tell you
[01:05:03] know things like this and then things
[01:05:06] like gravity the fact that objects are
[01:05:07] not supposed to float in the air but as
[01:05:09] opposed to fall you run this around the
[01:05:11] age of eight or nine months if you look
[01:05:14] at a lot of you know eight month old
[01:05:15] babies you give them a bunch of toys on
[01:05:18] the highchair first thing they do is
[01:05:19] it's why I'm on the ground that you look
[01:05:20] at them it's because you know they're
[01:05:22] learning about actively learning about
[01:05:25] gravity gravity yeah okay so they're not
[01:05:28] trying to know you but they you know
[01:05:30] they need to do the experiment right
[01:05:32] yeah so you know how do we get machines
[01:05:34] to learn like babies mostly by
[01:05:36] observation with a little bit of
[01:05:38] interaction and learning those those
[01:05:40] those models of the world because I
[01:05:41] think that's really a crucial piece of
[01:05:43] an intelligent autonomous system so if
[01:05:46] you think about the architecture of an
[01:05:47] intelligent autonomous system it needs
[01:05:49] to have a predictive model of the world
[01:05:51] so something that says here is a wall
[01:05:53] that time T here is a stable world at
[01:05:54] time T plus one if I take this action
[01:05:56] and it's not a single answer it can be
[01:05:59] education yeah yeah well but we don't
[01:06:02] know how to represent distributions in
[01:06:03] high dimension continuous basis so it's
[01:06:05] got to be something we care that data
[01:06:06] Hey but with some summer presentation
[01:06:08] with certainty if you have that then you
[01:06:12] can do what optimal control theory is
[01:06:13] called model predictive control which
[01:06:15] means that you can run your model with
[01:06:17] the hypothesis for a sequence of action
[01:06:19] and then see the result now what you
[01:06:22] need the other thing you need is some
[01:06:23] sort of objective that you want to
[01:06:25] optimize am i reaching the goal of
[01:06:27] grabbing the subject about minimizing
[01:06:29] energy am I
[01:06:30] whatever right so there is some sort of
[01:06:32] objectives that you have to minimize and
[01:06:34] so in your head if you had this model
[01:06:36] you can figure out the sequence of
[01:06:37] action that will optimize your objective
[01:06:40] that objective is something that
[01:06:42] ultimately is rooted in your basal
[01:06:45] ganglia at least in the human brain
[01:06:46] that's that's what is available Gambia
[01:06:48] computes your level of contentment or
[01:06:50] miss contentment oh no noise that's a
[01:06:53] word unhappiness okay yeah this
[01:06:56] contentment this contentment and so your
[01:06:59] entire behavior is driven towards kind
[01:07:03] of minimizing that objective which is
[01:07:05] maximizing your contentment computed by
[01:07:07] your your basal ganglia and what you
[01:07:11] have is an objective function which is
[01:07:13] basically a predictor of what your basal
[01:07:15] ganglia is going to tell you so you're
[01:07:17] not going to put your hand on fire
[01:07:18] because you know it's gonna you know
[01:07:21] it's gonna burn and you're gonna get
[01:07:23] hurt and you're predicting this because
[01:07:24] of your model of the world and your your
[01:07:27] predictor of this objective right so you
[01:07:30] if you have those you have those three
[01:07:32] components you have four components you
[01:07:35] have the the hard-wired contentment
[01:07:38] objective good computer if you want
[01:07:42] calculator and then you have the three
[01:07:44] components one is the objective
[01:07:46] predictor which basically predicts your
[01:07:47] level of contact and one is the model of
[01:07:51] the world and there's a third module I
[01:07:53] didn't mention which is a module that
[01:07:55] will figure out the best course of
[01:07:58] action to optimize an objective given
[01:08:00] your model okay yeah cool it's a policy
[01:08:06] policy network or something like that
[01:08:07] right now you need those three
[01:08:11] components to act autonomously
[01:08:12] intelligently and you can be stupid in
[01:08:14] three different ways you can be stupid
[01:08:16] because your model of the world is wrong
[01:08:18] you can be stupid because your objective
[01:08:20] is not aligned with what you actually
[01:08:23] want to achieve okay and in humans that
[01:08:27] would be a psychopath right and then the
[01:08:30] the third thing you the third way you
[01:08:32] can be stupid is that you have the right
[01:08:34] model you have the right objective but
[01:08:36] you're unable to figure out a course of
[01:08:38] action to optimize your objective given
[01:08:40] your model
[01:08:43] some people who are in charge of big
[01:08:45] countries actually have all three that
[01:08:46] are wrong all right which countries I
[01:08:51] don't know okay so if we think about
[01:08:54] this this agent if you think about the
[01:08:56] movie her you've criticized the art
[01:09:02] project that is Sophia the robot and
[01:09:04] what that project essentially does is
[01:09:07] uses our natural inclination to
[01:09:09] anthropomorphize things that look like
[01:09:12] human and given more do you think that
[01:09:15] could be used by AI systems like in the
[01:09:18] movie her
[01:09:20] so do you think that body is needed to
[01:09:23] create a feeling of intelligence
[01:09:26] well if Sophia was just an art piece I
[01:09:29] would have no problem with it but it's
[01:09:30] presented as something else let me add
[01:09:33] that comics real quick if creators of
[01:09:36] Sofia could change something about their
[01:09:39] marketing or behavior in general what
[01:09:40] would it be what what's just about
[01:09:43] everything I mean don't you think here's
[01:09:48] a tough question I mean so I agree with
[01:09:51] you so Sofia is not in the general
[01:09:54] public feels that Sofia can do way more
[01:09:57] than she actually can that's right and
[01:10:00] the people will create a Sofia are not
[01:10:04] honestly publicly communicating trying
[01:10:08] to teach the public right but here's a
[01:10:11] tough question don't you think this the
[01:10:16] same thing is scientists in industry and
[01:10:21] research are taking advantage of the
[01:10:23] sameness misunderstanding in the public
[01:10:25] when they create AI companies or
[01:10:27] published stuff some companies yes I
[01:10:30] mean there is no sense of there's no
[01:10:33] desire to delude there's no desire to
[01:10:35] kind of over claim what something is
[01:10:38] done right you know you should paper on
[01:10:39] AI that you know has this result on
[01:10:41] image net you know it's pretty clear I
[01:10:43] mean it's not even not even interesting
[01:10:44] anymore but you know I I don't think
[01:10:47] there is that I mean the reviewers are
[01:10:49] generally not very forgiving of of you
[01:10:54] know unsupported claims of this type and
[01:10:56] but there are certainly quite a few
[01:10:59] startups that have had a huge amount of
[01:11:01] hype around this that I find extremely
[01:11:04] damaging and I've been calling it out
[01:11:06] when I've seen it so yeah but to go back
[01:11:09] to your original question like the
[01:11:11] necessity of embodiment I think I don't
[01:11:14] think embodiment is necessary I think
[01:11:15] grounding is necessary so I don't think
[01:11:18] we're gonna get machines that I really
[01:11:19] understand language without some level
[01:11:21] of grounding in the world world and it's
[01:11:22] not clear to me that language is a kind
[01:11:24] of bandwidth medium to communicate how
[01:11:26] the real world works I think what this
[01:11:30] doctor ground our grounding means so
[01:11:32] running me he's that
[01:11:34] so there is this classic problem of
[01:11:35] common sense reasoning you know the the
[01:11:38] Winograd Winograd schema right and so I
[01:11:41] tell you the the trophy doesn't fit in
[01:11:44] the suitcase because this tool is too
[01:11:45] big what the trophy doesn't fit in the
[01:11:47] suitcase because it's too small and the
[01:11:49] it in the first case refers to the
[01:11:51] trophy in the second case to the
[01:11:52] suitcase and the reason you can figure
[01:11:54] this out is because you know what the
[01:11:56] trophy in the suitcase are you know one
[01:11:57] is supposed to fit in the other one and
[01:11:58] you know the notion of size and the big
[01:12:01] object doesn't fit in a small object and
[01:12:03] this is a TARDIS you know it things like
[01:12:04] that right so you have this got this
[01:12:06] knowledge of how the world works of
[01:12:08] geometry and things like that I don't
[01:12:12] believe you can learn everything about
[01:12:14] the world by just being told in language
[01:12:16] how the world works I think you need
[01:12:18] some low-level perception of the world
[01:12:21] you know be a visual touch you know
[01:12:23] whatever but some higher bandwidth
[01:12:25] perceptions of the world but by reading
[01:12:27] all the world's text you still may not
[01:12:29] have enough information that's right
[01:12:31] there's a lot of things that just will
[01:12:34] never appear in text and that you can't
[01:12:35] really infer so I think common sense
[01:12:39] will emerge from you know certainly a
[01:12:42] lot of language interaction but also
[01:12:43] with watching videos or perhaps even
[01:12:46] interacting in the in virtual
[01:12:47] environments and possibly you know robot
[01:12:50] interacting in the real world but I
[01:12:52] don't actually believe necessarily that
[01:12:53] this last one is absolutely necessary
[01:12:55] but I think there's a need for some
[01:12:57] grounding but the final product doesn't
[01:13:02] necessarily need to be embodied you know
[01:13:04] who say no it just needs to have an
[01:13:05] awareness a grounding right but it needs
[01:13:08] to know how the world works to have you
[01:13:12] know to not be frustrated frustrating to
[01:13:13] talk to and you talked about emotions
[01:13:17] being important that's that's a whole
[01:13:20] nother topic well so you know I talked
[01:13:23] about this the the basal ganglia ganglia
[01:13:26] as the you know this thing that could
[01:13:30] you know calculates your level of miss
[01:13:31] contentment contentment and then there
[01:13:33] is this other module that sort of tries
[01:13:35] to do a prediction of whether you're
[01:13:37] going to be content or not that's the
[01:13:38] source of some emotion so here for
[01:13:40] example is an anticipation of bad things
[01:13:44] that can happen to you right
[01:13:47] you have this inkling that there is some
[01:13:48] chance that something really bad is
[01:13:50] gonna happen to you and that creates
[01:13:51] here when you know for sure that
[01:13:53] something bad is gonna happen to you you
[01:13:54] cannot give up right it's not bad
[01:13:56] anymore it's uncertainty it creates fear
[01:13:58] so so the punchline is yes we're not
[01:14:01] gonna have a ton of intelligence without
[01:14:02] emotions whatever the heck emotions are
[01:14:08] so you mentioned very practical things
[01:14:10] of fear but there's a lot of other mess
[01:14:12] around but there are kind of the results
[01:14:14] of you know drives
[01:14:16] yeah there's deeper biological stuff
[01:14:18] going on and I've talked a few folks on
[01:14:21] this there's a fascinating stuff that
[01:14:23] ultimately connects to our joy to our
[01:14:26] brain if we create an AGI system sorry
[01:14:30] interminable human level intelligence
[01:14:32] system and you get to ask her one
[01:14:35] question what would that question be you
[01:14:39] know I think the the first one we'll
[01:14:41] create would probably not be that smart
[01:14:44] did you like a four-year-old okay so you
[01:14:47] would have to ask her a question - no
[01:14:50] she's not that smart
[01:14:51] yeah well what's a good question to ask
[01:14:56] you know to be responsive wind and if
[01:15:01] she answers oh it's because the leaves
[01:15:03] of the tree are moving in that creates
[01:15:05] wind she's on to something and if she
[01:15:09] says yeah that's a stupid question
[01:15:10] she's really obtuse no and then you tell
[01:15:13] her actually you know here is the the
[01:15:16] real thing and she says oh yeah that
[01:15:19] makes sense
[01:15:19] so questions that that reveal the
[01:15:24] ability to do common-sense reasoning
[01:15:25] about the physical world yeah and you
[01:15:27] know someone will call 20 ferns causal
[01:15:30] evidence well it was a huge honor
[01:15:33] congratulations returning award you know
[01:15:35] and thank you so much for talking today
[01:15:36] thank you
[01:15:45] you
