# Stanford HAI Closing Keynote: Discovery Loop with Jeff Dean and Fei-Fei Li
- **YouTube URL:** https://www.youtube.com/watch?v=ooGKNwJWdb8
- **Lines:** 1329

---

[00:00:02] All right, we've spent the day on hard
[00:00:02] questions about AI, who govern it
[00:00:05] governs it, how fast it's moving, and
[00:00:07] how we design it around people. So, for
[00:00:10] our closing keynote, we'll turn to one
[00:00:12] of the most hopeful promises, using AI
[00:00:15] to accelerate scientific discovery
[00:00:17] itself.
[00:00:18] Jeff Dean is co-founder and CEO of
[00:00:20] Discovery Loop, a new company focused on
[00:00:23] AI for science and engineering. And
[00:00:25] before that, he spent 27 years at
[00:00:28] Google, where he helped build systems
[00:00:30] like rapid MapReduce, Bigtable, and
[00:00:33] create TensorFlow, and served as chief
[00:00:35] scientist
[00:00:37] and co-lead of Gemini.
[00:00:39] His talk is titled Discovery Loop,
[00:00:41] Accelerating Science and Engineering.
[00:00:44] And afterwards, he'll be joined on stage
[00:00:46] by Professor Fei-Fei Li for a closing
[00:00:49] conversation.
[00:00:50] Fei-Fei is the founding director and
[00:00:52] senior fellow at Stanford HAI, the
[00:00:54] inaugural Sequoia Professor of computer
[00:00:57] science here at Stanford, and co-founder
[00:01:00] and CEO of World Labs. She recently took
[00:01:03] on the role as special advisor on AI to
[00:01:05] President John Levin, and as the
[00:01:07] co-chair of HAI's advisory council. HAI
[00:01:10] would not be here today if it weren't
[00:01:12] for her vision and commitment to putting
[00:01:14] people at the center of AI, and that
[00:01:17] founding vision remains at the heart of
[00:01:19] what we do here at the institute. So,
[00:01:22] now please join me in welcoming Jeff
[00:01:24] Dean.
[00:01:26] >> [applause]
[00:01:34] >> All right, wonderful. Uh delightful to
[00:01:34] be here with all of you today.
[00:01:37] Um
[00:01:37] I'm going to talk to you about Discovery
[00:01:39] Loop.
[00:01:40] Our mission is that we are trying to
[00:01:42] build AI systems that can automatically
[00:01:44] solve important problems in machine
[00:01:45] learning,
[00:01:46] science and engineering.
[00:01:48] And we think this will ultimately lead
[00:01:50] to more discoveries in the world, and
[00:01:51] that's uh
[00:01:52] what we're excited about.
[00:01:54] So,
[00:01:55] there's this common cycle across many,
[00:01:57] many disciplines of kind of the
[00:02:00] universal loop of science and
[00:02:01] engineering where you propose
[00:02:02] experiments, you implement and run those
[00:02:04] experiments, you look at the results,
[00:02:06] you examine whatever you measurements
[00:02:08] you can make about them, and you decide
[00:02:11] what to do next, which often means doing
[00:02:13] another experiment.
[00:02:15] So, our approach is we want to automate
[00:02:17] these kinds of experimental loops.
[00:02:19] Um we think if you can drive down
[00:02:21] iteration time, the time to run one time
[00:02:24] time through these loops, and you can
[00:02:26] propose an automatic we run many
[00:02:28] experiments, you can learn from each
[00:02:30] evaluation so that the subsequent
[00:02:31] experiments you propose are better and
[00:02:33] are informed by the previous experiments
[00:02:35] you've run,
[00:02:37] and scale both the quality and the
[00:02:39] volume of experiments, you're going to
[00:02:41] get breakthrough results. So, that's
[00:02:44] in an essence what we're out to do.
[00:02:46] Um
[00:02:47] if you squint at this nice list of US
[00:02:50] National Academy of Academy Academy of
[00:02:52] Engineering Grand Challenge problems,
[00:02:55] and these were problems uh proposed
[00:02:57] that's really important for us to solve
[00:02:59] in the 21st century,
[00:03:00] and we're a quarter of the way through
[00:03:02] roughly.
[00:03:03] Um
[00:03:04] if you squint at kind of the subproblems
[00:03:06] that you can imagine being needed to be
[00:03:08] solved for some of these areas, and
[00:03:10] particularly the ones in red, we think
[00:03:12] these kinds of automated discovery loops
[00:03:14] can actually assist and help with all of
[00:03:16] these different kinds of areas.
[00:03:18] >> [snorts]
[00:03:22] >> Now, one of the things that's important
[00:03:22] to us and partly why we formed this as a
[00:03:24] separate company is we believe
[00:03:27] technology can have an amazingly
[00:03:29] positive impact in the world if we do it
[00:03:31] right, but that we all have to work to
[00:03:33] make sure that it has this positive
[00:03:35] impact.
[00:03:37] Um and so we established our company as
[00:03:39] a public benefit corporation, and our
[00:03:40] public mission is to develop technology
[00:03:43] that addresses important societal
[00:03:44] problems, and to provide broad access to
[00:03:48] its benefits to improve people's lives.
[00:03:54] So, a little bit about the four of us.
[00:03:54] We have I have uh three amazing
[00:03:56] co-founders, uh Ziga Murat, Kwok-leung,
[00:03:59] and Oriol Vinyals. Uh we've worked
[00:04:00] together for depending on the pairwise
[00:04:02] relation,
[00:04:03] uh, somewhere between 14 and 30 years.
[00:04:06] Uh, we really enjoy working together on
[00:04:08] difficult problems, and we've got a lot
[00:04:10] of different kinds of experience. So,
[00:04:12] we've helped build, uh, Google products.
[00:04:14] You know, we all came from Google, so
[00:04:16] these are all Google-centric things
[00:04:18] we've worked on. Um,
[00:04:20] lots of different products. You know,
[00:04:21] we've worked together on many different
[00:04:23] generations of Google Search, the
[00:04:24] initial ad system, content ads, Gmail,
[00:04:27] News, Translate, um,
[00:04:29] infrastructure
[00:04:31] in the second column. Uh, in particular,
[00:04:33] uh, focus initially at the top part of
[00:04:36] that column are things that help you,
[00:04:38] uh,
[00:04:39] organize, manage large amounts of data,
[00:04:42] run large-scale computations over data
[00:04:44] to extract interesting insights. The
[00:04:46] bottom four things there are really
[00:04:48] multiple generations of large-scale
[00:04:51] machine learning infrastructure to
[00:04:52] enable training more and more capable
[00:04:54] models, and TPUs are machine
[00:04:56] learning-focused hardware that, uh, we
[00:04:59] were involved in.
[00:05:00] Um, then we've worked on a bunch of
[00:05:01] different AI research problems, uh,
[00:05:03] including some things that are kind of
[00:05:05] at the core of lots of different, uh,
[00:05:08] sort of, uh, highly capable models
[00:05:10] today. Things like model distillation or
[00:05:12] mixture of experts models. Uh, neural
[00:05:14] architecture search is kind of a early
[00:05:17] version of these kind of automated loops
[00:05:19] that are trying to identify,
[00:05:21] uh, capable, um, you know,
[00:05:23] neural model architectures for solving
[00:05:25] problems. And then applications of AI to
[00:05:28] different, uh, domains, including common
[00:05:30] science. So, I was, uh, Kwak and I were
[00:05:32] both involved in AlphaChip, which is
[00:05:34] reinforcement learning for chip design
[00:05:36] and, uh, placement and routing in chip
[00:05:38] design.
[00:05:39] Uh, Oriol was involved in AlphaFold, um,
[00:05:42] and neural weather forecasting. So,
[00:05:44] good mix of experience.
[00:05:46] Uh, we've also managed pretty large
[00:05:48] teams. So, I managed, uh, the Google
[00:05:50] Brain team up to 600 people and, uh,
[00:05:53] Google Research and AI teams up to about
[00:05:55] 4,400 people before I decided I was
[00:05:57] spending a lot of time in meetings about
[00:06:00] Q2 OpEx spending, and I pressed send on
[00:06:02] an email that took me from
[00:06:04] 4,400 to four reports
[00:06:06] uh and then Jeff Hinton retired the next
[00:06:08] week, so then I had three.
[00:06:10] Um and uh
[00:06:13] and then I was uh Oriel and I were both
[00:06:16] uh then co-technical leads of the Gemini
[00:06:17] project.
[00:06:19] And Quoc was our post-training lead. We
[00:06:20] were we're also quite proud of many
[00:06:22] alumni of our teams who've gone off and
[00:06:24] done lots of amazing things, including
[00:06:26] founders of companies like Anthropic,
[00:06:28] OpenAI,
[00:06:30] uh Physical Intelligence, uh which is
[00:06:31] probably known here at Stanford, uh
[00:06:34] various other things. Um
[00:06:36] and we think we have a nice blend that
[00:06:39] mixes both AI research skills and
[00:06:42] distributed system uh skills. So,
[00:06:45] uh these are the most cited AI
[00:06:46] researchers and distributed systems
[00:06:48] researchers per Google Scholar.
[00:06:50] Um and there's uh us in the red boxes.
[00:06:53] Also, the people with stars have all
[00:06:56] worked in our teams, which is nice.
[00:07:03] We also have fun together. So, we've
[00:07:03] traveled in many different continents.
[00:07:05] Uh there we are in London in the upper
[00:07:07] right, Patagonia in the upper left, uh
[00:07:09] Vietnam in the bottom left. Quoc and I
[00:07:12] are coming home from dinner on Uber-like
[00:07:14] moped services in California.
[00:07:18] Um so, one of the things we've been
[00:07:20] focused a lot on is how do we assemble
[00:07:23] an amazing founding team? And so, that's
[00:07:26] what we've been up to for kind of the
[00:07:28] first uh you know, uh period of
[00:07:31] existence of the company is hiring
[00:07:33] amazing people.
[00:07:34] Um and they've come from lots of
[00:07:36] different places. You see all the logos.
[00:07:38] Um many of the people in the team have
[00:07:40] experience founding various companies or
[00:07:42] various important projects. Uh we have a
[00:07:44] lot of great team experience in
[00:07:47] you know, leading the Go programming
[00:07:49] language project, uh
[00:07:52] you know, uh key contributors to lots of
[00:07:54] different models, Gemini, Deep C,
[00:07:56] Chinchilla 3,
[00:07:58] uh the co-author of the Chinchilla 3
[00:07:59] paper and author of the attention
[00:08:01] residuals work joined us.
[00:08:03] Um recently, we We a great mix of kind
[00:08:06] of very experienced people and people
[00:08:08] who are uh rising amazing
[00:08:12] stars earlier in their career.
[00:08:14] Um and roughly 10% of the company has
[00:08:16] the ACM prize in computing and 10% have
[00:08:20] IOI Olympiad medals. So, we're we're
[00:08:22] pretty pretty excited about the team
[00:08:24] we've hired. We're having We've also
[00:08:27] really focused on hiring for
[00:08:30] kind of amazing ability to work
[00:08:33] together, which was great
[00:08:36] Um so, why now?
[00:08:39] You know, we now have these really
[00:08:40] capable frontier models that can do lots
[00:08:42] of amazing things.
[00:08:44] Um and partly that came about because
[00:08:47] there's been innovation over the last
[00:08:48] say of 10 to 15 years in the AI space
[00:08:52] of, you know, lots of different kinds of
[00:08:54] things. The hardware layer has improved
[00:08:56] tremendously in performance, both TPUs
[00:08:58] and GPUs and sort of more specialized
[00:09:00] things. Software abstractions have
[00:09:02] gotten better so that people can
[00:09:04] implement things they care about more
[00:09:06] easily easily and readily and it can be
[00:09:08] mapped onto the hardware more
[00:09:09] efficiently. Um model architectures have
[00:09:11] improved, you know,
[00:09:13] Word2Vec and then sequence-to-sequence
[00:09:15] and then transformers and MOEs have all
[00:09:17] been important innovations in what kind
[00:09:19] of models we should train.
[00:09:21] Uh training algorithms have gotten a lot
[00:09:23] better.
[00:09:24] Uh things like distillation enable very
[00:09:27] high quality but smaller models.
[00:09:30] And inference algorithms have actually
[00:09:32] improved quite a lot so you can actually
[00:09:33] apply more compute at inference time and
[00:09:36] get better results with things like
[00:09:38] chain of thought or
[00:09:39] you know, inference time compute scaling
[00:09:41] where you try many ways of solving the
[00:09:43] problem and then kind of examine
[00:09:45] what's happened.
[00:09:47] Um
[00:09:48] but a great base model isn't sufficient
[00:09:50] for solving some of the problems that we
[00:09:51] want to solve. So, in particular, we
[00:09:54] think you start with great base models,
[00:09:56] but then you want agents plus models to
[00:09:59] be able to really effectively use tools
[00:10:01] to accomplish really complicated tasks.
[00:10:04] We want the agents and models to be
[00:10:05] especially good at creativity. Like
[00:10:07] coming up with amazing scientific or
[00:10:10] engineering breakthroughs is not just
[00:10:12] kind of
[00:10:13] doing things that have already been done
[00:10:15] in a lot of cases. It's actually putting
[00:10:18] together lots of insights, coming up
[00:10:20] with something genuinely new, and seeing
[00:10:22] how well that works.
[00:10:23] And we also think agents and models
[00:10:26] should learn from the previous
[00:10:27] experiments and previous experience both
[00:10:30] in trying to solve this particular
[00:10:31] problem, but also over time you will see
[00:10:34] systems that maybe have solved 5,000
[00:10:37] problems and the 5,000 and first one
[00:10:39] they can learn from the problems that
[00:10:41] are sort of most closely related to that
[00:10:43] particular new problem they're trying to
[00:10:45] solve.
[00:10:49] So, at this traditional experimental
[00:10:49] loop, you often have a lot of manual
[00:10:51] effort at each stage. Um and when you
[00:10:54] try to solve a larger problem,
[00:10:56] uh that becomes even more complicated
[00:10:57] because you have to typically decompose
[00:11:00] those larger problems into a bunch of
[00:11:02] subproblems or subpieces. You end up
[00:11:05] with actually a difficult decomposition
[00:11:08] problem in and of itself. That's the
[00:11:10] left-hand side. And then each one of
[00:11:12] these subproblems or subareas has lots
[00:11:14] of people running experiments, figuring
[00:11:16] out what worked, what didn't work,
[00:11:18] trying different approaches.
[00:11:19] Um you end up with a lot of coordination
[00:11:21] overhead. Uh and resource conflicts can
[00:11:24] occur. Large system effects. So, this
[00:11:26] decomposition that you have to do is
[00:11:28] actually quite hard.
[00:11:30] Um and it's hard to combine the results
[00:11:31] across the subproblems you set out. And
[00:11:34] perhaps even worse, the way you've
[00:11:36] decided to decompose things in a very
[00:11:38] large-scale project is actually pretty
[00:11:40] hard to change once you've kind of got
[00:11:43] the project up and running and going.
[00:11:45] And so, you can't really revisit those
[00:11:47] early decisions very effectively when
[00:11:49] you have a uh you know, a large-scale
[00:11:52] engineering effort like building an
[00:11:53] airplane or training the best frontier
[00:11:56] model or whatever.
[00:11:58] Um
[00:11:59] So, what we think is possible is you can
[00:12:02] take a relatively small number of domain
[00:12:05] experts,
[00:12:06] use automated systems that can ideally
[00:12:09] automatically decompose into interesting
[00:12:11] subproblems, and then automatically
[00:12:14] solve those sub problems. But,
[00:12:17] it may be that human guidance helps the
[00:12:19] decomposition, and then humans sort of
[00:12:22] direct what are the important sub
[00:12:24] problems to solve, and really enable
[00:12:28] small number of people with domain
[00:12:29] expertise to really tackle large
[00:12:32] impactful problems.
[00:12:33] And we think this is possible if you
[00:12:36] build the right infrastructure. You
[00:12:38] know, you want to have tens of thousands
[00:12:40] of automated experiments. You want a
[00:12:42] system that can actually handle that,
[00:12:44] can understand what is the value of
[00:12:46] running this experiment versus running
[00:12:47] that one, and decide what to do next. Um
[00:12:52] automated decision making with
[00:12:53] reinforcement learning or evolutionary
[00:12:55] algorithms. These earlier decisions can
[00:12:57] then be more revisited more fluidly.
[00:13:00] And every earlier experiment should
[00:13:02] inform every future experiment.
[00:13:08] So, what have we done so far? First 3
[00:13:08] weeks,
[00:13:09] we did 400 interviews, mostly at Caffe
[00:13:11] Venetia on University Avenue,
[00:13:14] to find amazing people, which I talked
[00:13:17] about some of them.
[00:13:18] Finding office space. We're in the old
[00:13:20] Zibibbo restaurant. So, we have a funky
[00:13:22] funky space for us.
[00:13:25] We've built our own agent harness that
[00:13:27] we're using for all of our own
[00:13:28] development and for automation. That
[00:13:31] harness has some really nice
[00:13:32] collaboration features. So, you can
[00:13:34] think of it as a system that you
[00:13:36] interact with a
[00:13:37] model to have conversations and ask it
[00:13:40] to solve things, but you can also invite
[00:13:42] your teammate in to collaborate. And so,
[00:13:44] then the two of you can talk to
[00:13:47] a model and an agent.
[00:13:49] And you can also have other people add
[00:13:51] comments to the thing you're trying to
[00:13:53] do, or propose a design to the to the
[00:13:55] agent before you propose that.
[00:13:58] We've built really agent-first
[00:14:01] infrastructure so that it will scale to
[00:14:04] having tens, hundreds of thousands of
[00:14:06] agents doing things rather than sort of
[00:14:09] hundreds of people doing things. We
[00:14:11] think that's really important. And we've
[00:14:13] got probably on the order of 20
[00:14:15] automated improvement loops running in
[00:14:17] the way in which we imagine
[00:14:19] that we want to solve problems
[00:14:21] and there where you can see that they're
[00:14:23] running and improving evaluating methods
[00:14:25] for making these experimental iterations
[00:14:28] more effective and faster. How do you
[00:14:29] learn from the previous experimental
[00:14:32] results in the previous
[00:14:33] measurements you're able to take in
[00:14:35] order to
[00:14:36] learn faster.
[00:14:39] Um
[00:14:40] So this is kind of where we are is
[00:14:43] building this software loop to automate
[00:14:46] machine learning tasks in particular
[00:14:48] because we think that unlocks actually a
[00:14:50] lot of
[00:14:51] autonomous science but initially we're
[00:14:53] focused on how do you make automated
[00:14:56] systems that can solve machine learning
[00:14:57] research and machine learning
[00:14:59] engineering problems.
[00:15:00] And our goal is really to make domain
[00:15:02] experts 20x to 50x more productive. You
[00:15:05] know, we're not trying to take people
[00:15:06] out of what we're doing. We're just
[00:15:08] trying to make really empower amazing
[00:15:11] people or our domain experts who want to
[00:15:14] solve particular problems and enable
[00:15:16] them to solve those problems with less
[00:15:18] effort on their part.
[00:15:21] Um so
[00:15:22] we think 15 years of breakthroughs in
[00:15:24] machine learning have led to very
[00:15:26] capable models setting the stage for
[00:15:28] automating ML science and engineering to
[00:15:31] dramatically accelerate discovery.
[00:15:33] Thank you. Oh and we're hiring
[00:15:36] apply@discoveryloop.com.
[00:15:38] Thank you.
[00:15:39] >> [applause]
[00:15:48] >> Oh this one. Okay. Sorry I took your
[00:15:48] water then.
[00:15:48] >> No worries.
[00:15:50] All right. That was a great talk. Thanks
[00:15:52] Jeff. And I think this is
[00:15:56] the last session or Okay. So we're we're
[00:15:59] between
[00:16:00] the audience and snacks.
[00:16:02] >> Uh-oh. Never a good place to be.
[00:16:04] >> Yeah.
[00:16:05] So um
[00:16:07] I was hoping that we can be a little bit
[00:16:09] nerdier for this session and and get
[00:16:11] into a little bit of the tech but
[00:16:14] we're supposed to have a mutual
[00:16:16] discussion so I'm going to wear the dual
[00:16:18] hat of asking you questions, but
[00:16:20] participate in the discussion.
[00:16:24] Thanks for for that talk cuz I was going
[00:16:26] to ask you why as my first question for
[00:16:29] for Discovery Loop. Congratulations.
[00:16:32] >> Thank you.
[00:16:32] >> And pretty much all four of you are
[00:16:36] more or less Google lifers. Especially
[00:16:39] you joined Google 1999, right? So it is
[00:16:43] very clear what the macro incredible
[00:16:46] technological
[00:16:48] progress we have seen the past few
[00:16:49] years, but I'm still curious, was there
[00:16:53] a moment
[00:16:54] in the past
[00:16:56] I would have guessed a year or 2 years
[00:16:59] that the technology has moved into
[00:17:02] a state that you and Quoc and Sanjay and
[00:17:06] Oriol are like
[00:17:08] we've got to do something different and
[00:17:10] we cannot do it at Google.
[00:17:12] >> Yeah, I mean I think we all have been
[00:17:15] excited about seeing automated systems
[00:17:18] that can actually sort of help people
[00:17:21] develop software systems in a more
[00:17:23] automated way or you know, Quoc did a
[00:17:26] lot of work on neural architecture
[00:17:27] search even a decade ago, which you can
[00:17:29] think of as a very early version of that
[00:17:31] kind of recursive
[00:17:34] sort of self-improving system where you
[00:17:36] say, "Please find me great model
[00:17:37] architectures for computer vision
[00:17:39] problems or
[00:17:41] you know, language problems." And so we
[00:17:44] knew that kind of approach worked, but
[00:17:47] in that day you were sort of specifying
[00:17:49] the search space as like a junk
[00:17:51] janky kind of pile of Python code rather
[00:17:54] than natural language as you can today.
[00:17:56] You can sort of describe to a
[00:17:58] you know, a capable model plus agent
[00:18:00] system,
[00:18:02] "You know, please go off and explore
[00:18:03] model architectures that might help
[00:18:05] interpret MRI images or whatever." And
[00:18:07] it will go off and do that. And you
[00:18:10] know, I think that's just a
[00:18:12] really
[00:18:13] profound shift in what we imagine
[00:18:16] computer systems and AI systems to be
[00:18:19] able to do, right? And if you can get
[00:18:21] those things working reliably,
[00:18:23] that enables a lot of stuff. And in
[00:18:25] particular for science and engineering,
[00:18:27] we think that's a really ripe set of
[00:18:29] domains for how can you really advance
[00:18:32] positive impact in the world.
[00:18:34] >> I see. So, it [clears throat] was really
[00:18:36] the the loose, the self improvement
[00:18:40] that that got you guys feel that you
[00:18:42] want to you want to
[00:18:44] >> Some might say we're a bit loopy, but
[00:18:45] yes.
[00:18:47] >> It was
[00:18:48] >> I mean, and also I would also say that
[00:18:50] it was important to us to, you know,
[00:18:52] we've enjoyed many times starting very
[00:18:56] small projects. And that that feeling of
[00:18:59] magic when you have five people working
[00:19:01] on something and you add a sixth then
[00:19:03] then you add in a seventh and 10th and
[00:19:06] so on. That that really is fun.
[00:19:08] And you can do that in in large
[00:19:09] companies, but we also wanted to do this
[00:19:11] as a public benefit corporation. And we
[00:19:13] felt like that was an important
[00:19:14] reflection of our own values. And you
[00:19:17] know, taking a bigger plunge of now you
[00:19:20] have to figure out real estate and all
[00:19:23] the other things that involve
[00:19:25] setting up a company
[00:19:27] is kind of fun.
[00:19:28] >> Cool. Yeah, even for myself when we
[00:19:30] started World Labs, it was a moment of
[00:19:33] seeing the technology. It's different
[00:19:35] from you guys seeing computer vision and
[00:19:39] generative models have converged at the
[00:19:41] moment where we can create generative
[00:19:44] models beyond just words was the moment
[00:19:46] for for us to start World Labs.
[00:19:48] >> Yeah, I mean, like the generative models
[00:19:50] you you all produced and that are now
[00:19:52] capable possible are pretty amazing.
[00:19:55] >> Yeah. Okay, so let's talk about the self
[00:19:58] improvement and recursive self
[00:20:01] improvement. Let's let's nerd out a
[00:20:03] little bit. We're contemporaries in
[00:20:06] terms of our education through the field
[00:20:08] of machine learning. I was just thinking
[00:20:10] in my head
[00:20:12] how many names
[00:20:14] this concept has had in its lifetime.
[00:20:18] From me being a grad student, we had
[00:20:20] incremental learning. Then we had
[00:20:22] continuous learning. Then we had meta
[00:20:27] um
[00:20:28] um lifelong learning. And um and neural
[00:20:32] architecture search, you mentioned that.
[00:20:35] Now we have self-improvement and then
[00:20:38] RSI. So, do you want to just
[00:20:41] treat the audience, especially the
[00:20:44] technical part of the audience,
[00:20:46] with some more
[00:20:48] rigorous definition of what is
[00:20:50] self-improvement versus what is
[00:20:52] recursive self-improvement? And my goal
[00:20:55] here is actually to tease apart the
[00:20:58] fiction from the the facts.
[00:21:00] >> Sure. Yeah, I mean, I think if you think
[00:21:03] about those loops that I talked about,
[00:21:06] those loops can be applied to many kinds
[00:21:07] of problems. And I I think of like
[00:21:10] self-improving systems as one thing
[00:21:13] where you've given the system a goal to
[00:21:16] go off and improve you typically some
[00:21:18] measurable objective, like accuracy of
[00:21:21] an ML model, and you know, it's trying
[00:21:24] different kinds of model architectures
[00:21:26] to improve that accuracy.
[00:21:27] Um
[00:21:28] >> So, pause there. A lot of machine
[00:21:30] learning algorithm is capable of doing
[00:21:32] that.
[00:21:33] >> Yes.
[00:21:33] >> That itself is not recursive.
[00:21:35] >> Correct.
[00:21:35] >> That is a a
[00:21:36] >> So, like self-improving system might be
[00:21:39] we point our system at uh a bunch of MRI
[00:21:43] data and MRI outcomes, and we say I want
[00:21:46] to develop a model to help interpret MRI
[00:21:48] images, right? That would be a
[00:21:50] self-improving system where you can
[00:21:51] develop that model automatically and can
[00:21:54] then, you know, see the accuracy of the
[00:21:56] different approaches that are being
[00:21:57] tried, hopefully increase uh as the
[00:21:59] system runs experiments. But that's not
[00:22:01] improving the base system that is
[00:22:04] proposing what to try next, right?
[00:22:07] >> Yep.
[00:22:07] >> So, recursive self-improvement is how do
[00:22:10] you actually get that kind of
[00:22:13] self-improving approach to improve the
[00:22:15] base system that you're trying to get to
[00:22:18] propose improvements.
[00:22:21] If that makes sense.
[00:22:22] >> Yes, it makes sense to me, but I think
[00:22:24] it's
[00:22:25] it's a very confusing concept for
[00:22:27] people. And now,
[00:22:29] especially we're in the Silicon Valley,
[00:22:32] many people are just using this in a
[00:22:33] very loose way. And as a scientist,
[00:22:36] actually bothers me. So, I just want to
[00:22:38] be on the stage to make sure we define
[00:22:42] RSI really well. So, let's talk about
[00:22:45] the physical limit of RSI though,
[00:22:46] because RSI is being hyped in a way it's
[00:22:51] almost like
[00:22:54] it's almost
[00:22:56] a system it has no end. We can just
[00:22:58] accelerate and and and to the infinity.
[00:23:03] What is the hype here? What is the
[00:23:05] fiction from the
[00:23:06] >> Well, I mean, I think
[00:23:08] if you think about how humans improve
[00:23:11] the capabilities of models, which is
[00:23:12] what has been happening over the past 10
[00:23:14] or 15 years, you know, you get really
[00:23:16] capable researchers and ML engineers
[00:23:18] together.
[00:23:19] They run lots of experiments at small
[00:23:21] scale. They say, "Oh, these these ideas
[00:23:24] didn't work. These ideas did work. Then
[00:23:26] we're going to incorporate those into
[00:23:28] the next generation of the the model."
[00:23:30] That's how Gemini 2 comes to be after we
[00:23:33] had Gemini 1 is we ran the lots of
[00:23:35] experiments and and improved things.
[00:23:38] So,
[00:23:39] that is kind of a normal process of
[00:23:43] research and engineering.
[00:23:45] And I think when you start to apply
[00:23:47] automation to that, yes, you can get
[00:23:49] some
[00:23:50] improvements in how fast that can
[00:23:51] happen.
[00:23:52] You know,
[00:23:53] people will start off an experiment. If
[00:23:55] the experiment will finish at 2:00 a.m.,
[00:23:57] they're not at the desk until 8:00 a.m.
[00:23:59] to look at the results. So, if you have
[00:24:01] an automated system, it can look at the
[00:24:03] results, figure out what to do next in a
[00:24:04] much more automated way, can maybe make
[00:24:07] a lot better decisions across
[00:24:10] an entire large project than each
[00:24:12] individual making decisions about what
[00:24:13] to do next. Um
[00:24:16] So, but I think if you think about what
[00:24:19] needs to be involved in creating
[00:24:22] the base model and making it better,
[00:24:25] there's lots of actual training and
[00:24:27] experimentation that needs to be done.
[00:24:29] And that's not going to happen
[00:24:30] infinitely fast, right? Like there's
[00:24:32] just actual physics involved. You need
[00:24:35] to run some computations, you need to
[00:24:36] look at the results, the computers need
[00:24:39] to like do their thing, and you need to
[00:24:41] save the data, look at the have another
[00:24:43] model look at the results in order to
[00:24:44] decide what to do next. So, I think some
[00:24:46] people have this illusion that you're
[00:24:48] going to be able to run this loop
[00:24:51] infinitely fast, and I just find that
[00:24:54] kind of implausible.
[00:24:56] >> Yeah.
[00:24:56] >> And it's good to be grounded in reality.
[00:24:59] Having automated systems that can try to
[00:25:01] improve things is definitely going to
[00:25:03] improve the rate at which we can improve
[00:25:05] those systems,
[00:25:06] but it's not going to make them go
[00:25:07] infinitely fast.
[00:25:09] >> I think this is a really important
[00:25:11] point. Actually, I was I I was not
[00:25:13] applying for a job at Discovery Loop,
[00:25:16] but I was at the cafe of Valencia with
[00:25:18] the Jeff.
[00:25:19] >> We we have coffee for many reasons.
[00:25:22] Cuz we like coffee.
[00:25:23] >> And we have been talking about this RSI,
[00:25:26] you know, hype and facts.
[00:25:28] >> We were actually prepping for this
[00:25:29] panel, in fact.
[00:25:30] >> Apparently, but I was thinking
[00:25:32] Okay, this is something I haven't run by
[00:25:34] you, but tell me if you agree or you can
[00:25:36] disagree with me, that's totally fine. I
[00:25:38] was thinking about humans. Are we
[00:25:41] a self-improving system or are we a RSI
[00:25:44] system?
[00:25:46] And I think we're definitely a
[00:25:48] self-improving system. I suck at
[00:25:50] cooking. And if I were to try to cook
[00:25:54] omelet, the first time will really I
[00:25:57] will burn everything, and second I would
[00:25:59] have learned, and the second time I
[00:26:01] would do a little better. Maybe after 10
[00:26:03] times I'll have a reasonable omelet that
[00:26:06] I will eat, my kids will not eat. And
[00:26:08] that is self-improving.
[00:26:10] >> Mhm.
[00:26:10] >> But the RSI part has to do with my
[00:26:13] brain. In this process of learning how
[00:26:16] to cook omelet,
[00:26:18] first of all, my brain has to be somehow
[00:26:21] altered, some neuronal connectivity
[00:26:25] needs to be altered enough that I have a
[00:26:27] better system
[00:26:29] to to cook
[00:26:31] omelet. Maybe I can grow the sixth
[00:26:33] finger
[00:26:35] if if if I'm we're talking about
[00:26:37] hardware improvement. And then by
[00:26:40] cooking more omelet my brain will be
[00:26:41] further improved.
[00:26:42] >> Exactly. [laughter]
[00:26:43] And then the
[00:26:45] by cooking more omelet my brain will be
[00:26:47] further improved. And if that loop
[00:26:50] happens humans is a RSI system. Is that
[00:26:53] the right analogy?
[00:26:54] >> Yeah, I mean I I think the answer is
[00:26:56] humans are both. Right. Right. I mean I
[00:26:59] think
[00:27:00] through your life you learn a lot of
[00:27:02] things which is self-improving. Like you
[00:27:04] learn how to cook an omelet, you learn
[00:27:06] how to do calculus problems. But you
[00:27:08] also learn
[00:27:10] how you learn.
[00:27:12] >> Yeah.
[00:27:12] >> And that learning how to learn actually
[00:27:14] is what makes you self-improving
[00:27:17] and recursively self-improving because
[00:27:19] now you can learn to do more things more
[00:27:22] quickly based on you understanding what
[00:27:24] kinds of knowledge and the ways to
[00:27:27] present information presented to you
[00:27:29] actually makes you most effectively pick
[00:27:31] it up.
[00:27:31] >> Yeah. And possibly recursive
[00:27:35] self-learning
[00:27:36] recursive self-improvement is part part
[00:27:39] possibly a evolutionary algorithm.
[00:27:42] Right? So anyway, I don't want to go
[00:27:44] down the rabbit hole but I think it's
[00:27:46] just a rare opportunity to have this
[00:27:48] discussion in public because we have so
[00:27:50] much hype right now.
[00:27:51] >> Yeah, I mean there's a lot of hype about
[00:27:53] like oh it's going to go infinitely fast
[00:27:55] and it's scary. I mean I think if you
[00:27:57] look at it as a pragmatic engineering
[00:27:59] system doing things it becomes less
[00:28:03] scary and more understandable.
[00:28:04] >> Yeah. So you talked a lot about
[00:28:07] discovery loop but you were still a
[00:28:09] little vague about what scientific
[00:28:12] problem you want to work on. So I want
[00:28:14] to just push you a little bit to the
[00:28:17] extent you're willing to reveal.
[00:28:19] >> Yeah.
[00:28:20] >> There are so many scientific problems
[00:28:22] that benefits the society. Which one are
[00:28:25] you passionate about right now?
[00:28:27] >> Yeah. So
[00:28:29] uh
[00:28:30] I I I for a long time I've been very
[00:28:33] interested in AI for healthcare. I think
[00:28:34] that's an area that we will do work in
[00:28:36] not right now, but down the road because
[00:28:39] I think it's a super important area and
[00:28:41] there's that would be very aligned with
[00:28:43] our sort of
[00:28:45] public benefit corporation mission. Um
[00:28:48] right now we are focused on the kinds of
[00:28:51] science and engineering problems where
[00:28:53] you can do the entire loop in digital
[00:28:55] form cuz we think that's the one where
[00:28:57] you it's very amenable to speeding up
[00:28:59] that entire loop. If you have like
[00:29:01] actual physical processes involved, that
[00:29:03] be that becomes harder to speed up the
[00:29:05] loop. There are obviously many important
[00:29:07] disciplines where you do need physical
[00:29:09] processes. Um and we have some hybrid,
[00:29:12] you know, approaches that we can speed
[00:29:14] things up in those domains.
[00:29:16] So, let's look at digital domains of
[00:29:20] science and engineering. We are
[00:29:21] initially focused on machine learning
[00:29:23] research and machine learning
[00:29:25] engineering itself.
[00:29:27] And also hardware design cuz we think
[00:29:29] those three areas are you know, it's
[00:29:31] good to have a few different areas you
[00:29:33] focus on, not try to focus on
[00:29:34] everything. But
[00:29:36] um
[00:29:37] those are ones where we have domain
[00:29:39] expertise ourselves and we think it's a
[00:29:41] really important domain because it
[00:29:43] unlocks other things. So, for example,
[00:29:45] in healthcare, if you have a system that
[00:29:47] can automatically solve machine learning
[00:29:50] engineering tasks,
[00:29:52] then you can point it at lots of
[00:29:54] problems in in health or, you know,
[00:29:56] material science or or whatever and say
[00:29:58] I would like an amazing model
[00:30:00] specialized to this particular task.
[00:30:02] Which is say self-improvement, but not
[00:30:04] recursive self-improvement. Um so, uh
[00:30:07] that
[00:30:09] I think is how I would describe us.
[00:30:11] We're focused on those three domains
[00:30:13] right now,
[00:30:14] but we have ambitions to go beyond.
[00:30:18] >> Okay, so
[00:30:19] I was trained in physics when I was a
[00:30:22] undergrad. And um
[00:30:25] in in physics we have this
[00:30:28] division between experimentalists and
[00:30:30] theorists, right? I was just thinking
[00:30:33] about your loop, the the way you draw
[00:30:35] it, you call it propose uh experiment,
[00:30:38] but in physics we tend to call it
[00:30:39] hypothesis.
[00:30:40] >> Mhm.
[00:30:41] Sure.
[00:30:41] >> Form hypothesis and then you go through
[00:30:44] um
[00:30:45] experiments and evaluation and all that.
[00:30:47] I was just thinking the way how powerful
[00:30:50] AI agents are these uh self-improvement
[00:30:53] loops, whether it's recursive or not,
[00:30:55] doesn't matter.
[00:30:56] Is it philosophically taking a stance
[00:31:00] that
[00:31:01] it is more a experimental
[00:31:04] experimentalist approach to scientific
[00:31:06] question cuz it's very much about
[00:31:10] proposing hypothesis in parallel um
[00:31:13] parallelize experiments
[00:31:15] um
[00:31:16] as opposed to the more mysterious
[00:31:19] theoretical way of doing scientific
[00:31:22] discovery, you know, to this day you
[00:31:24] would wonder
[00:31:26] great theorists like Newton, like
[00:31:30] Einstein, they don't do that much
[00:31:32] experiments. They read about them, but
[00:31:34] they don't do it that way. So, do you
[00:31:37] feel this is
[00:31:39] skewing towards experimentalism?
[00:31:41] >> I don't think necessarily, but I
[00:31:45] it probably there's a bit more leaning
[00:31:47] in that direction. I do think you could
[00:31:48] do great theoretical work with a system
[00:31:50] like this where you can propose can you
[00:31:53] see if you can come up with a theory
[00:31:55] that explains all of this data. And I
[00:31:58] think it could iterate and try to find
[00:32:00] kind of the minimal description theory
[00:32:03] that helps explain experimental data.
[00:32:05] You know, I think a lot of experimental
[00:32:07] or theoretical physicists are seeing
[00:32:10] what's happening in the physics
[00:32:11] community in the experimental domain and
[00:32:13] then trying to come up with theories
[00:32:15] that explain, you know, some of the
[00:32:17] things that people are observing and
[00:32:18] don't understand yet. So, I I think that
[00:32:21] that's certainly possible and I think
[00:32:23] actually it's not good to think of these
[00:32:26] as separate disciplines.
[00:32:27] >> Right.
[00:32:28] >> Right? So, theoretical physics,
[00:32:29] experimental physics, you know,
[00:32:31] chemistry,
[00:32:33] if you think about a system that
[00:32:34] actually has say performed
[00:32:37] a mil- a million problems with a hundred
[00:32:40] million experiments across a hundred
[00:32:42] domains of science, you know, it's very
[00:32:45] likely going to have a lot of insights
[00:32:46] that derive from the fact that it has
[00:32:48] seen lots of different kinds of, you
[00:32:51] know, experimental results and seen like
[00:32:53] what worked and what didn't work in sort
[00:32:55] of the neighborhood of of interesting
[00:32:57] problems you're going to ask it to solve
[00:32:59] in the future. And that, I think,
[00:33:01] doesn't have hard domain boundaries the
[00:33:04] way we as people sometimes tend to
[00:33:07] instill with, you know, academic
[00:33:08] department boundaries or whatever. One
[00:33:10] of the things I like about AI is it's
[00:33:12] like a a pan-institutional
[00:33:14] thing that gets everyone talking
[00:33:16] together. So,
[00:33:17] >> Okay, well, we have to talk about math
[00:33:19] then. Um
[00:33:20] in fact, when we were proposing to have
[00:33:23] to invite you to this panel, I I
[00:33:25] actually was going to
[00:33:27] did invite Terence Tao. So, I called
[00:33:30] him, but he couldn't come. So, let's
[00:33:32] talk about math a little bit. Um
[00:33:35] I have to say
[00:33:37] I had mixed
[00:33:39] emotions when we see a serious It was
[00:33:43] first Navier-Stokes and then there's
[00:33:45] 720,
[00:33:46] you know, papers and then there's more
[00:33:48] that was just released by OpenAI
[00:33:51] yesterday that AI solving math. It's not
[00:33:55] It's obviously It's not that
[00:33:58] I don't like what's being discovered.
[00:34:00] It's just that
[00:34:02] math in these century-old,
[00:34:04] millennial-old math problem is such a
[00:34:06] pinnacle of human intelligence and and
[00:34:09] mathematicians see not only
[00:34:13] technical solutions in them, they also
[00:34:16] see beauty. They they and and now we
[00:34:19] have a completely different machinery
[00:34:21] that goes about these problems, right?
[00:34:24] So,
[00:34:26] Terence and I actually talked quite a
[00:34:28] bit about that. And he recently also
[00:34:30] just gave a talk about math 2.0 and talk
[00:34:33] about how AI can help solve certain type
[00:34:37] of math problems, but he also does
[00:34:39] insist there are other math problems
[00:34:42] that are out of the realm of AI,
[00:34:45] especially if we don't have solutions,
[00:34:47] there's no data.
[00:34:49] What's your take of this
[00:34:51] pretty
[00:34:53] big tsunami change in math in the past
[00:34:56] few, literally, weeks?
[00:34:58] >> Yeah, I mean, clearly the models and the
[00:35:02] sort of agent-based systems that can use
[00:35:05] those models in highly parallel, you
[00:35:07] know, agent uh activity are capable of
[00:35:10] solving really hard
[00:35:12] you know, unsolved problems in
[00:35:13] mathematics, and that is
[00:35:15] a a revelation of what is possible now.
[00:35:19] I think people are finding it finding it
[00:35:21] dissatisfying and a little
[00:35:24] uh
[00:35:25] uh discomforting because often those
[00:35:28] proofs involve like 500 pages of Lean or
[00:35:31] something.
[00:35:32] >> Mhm.
[00:35:32] >> So, it's machine-checked, but no one
[00:35:33] quite understands the elegant, simple
[00:35:38] way to get to that result. And so, I
[00:35:40] think
[00:35:41] um
[00:35:42] it is good to know that the problem is
[00:35:45] proven or disproven, but understanding
[00:35:48] how to develop really elegant techniques
[00:35:51] to come to that result is often what
[00:35:54] happens as mathematician human
[00:35:56] mathematician are wrestling with
[00:35:57] problems. And those often generate new
[00:36:00] kinds of mathematics that can be used to
[00:36:01] tackle other kinds of problems. So,
[00:36:04] >> So, you're saying new math solutions
[00:36:07] only come from elegant solutions?
[00:36:09] >> No, but I think the like the elegant an
[00:36:12] elegant solution often comes up with a
[00:36:14] cool technique that can then be applied
[00:36:17] to other problems.
[00:36:19] And I don't think people are necessarily
[00:36:21] seeing the crisp elegant technique in
[00:36:24] some of these very long
[00:36:25] machine-generated proofs. But, knowing
[00:36:28] that something is solvable
[00:36:30] is actually
[00:36:31] uh in lots of different domains,
[00:36:34] if you know something is possible, it
[00:36:36] actually makes you strive harder and
[00:36:38] understand that you can do it, and then
[00:36:41] you actually can do it perhaps a
[00:36:42] different way or, you know, a more
[00:36:44] elegant way. And so I think actually
[00:36:47] yes, it's kind of
[00:36:48] upsetting about
[00:36:51] you know, the way in which so many of
[00:36:53] these problems are being solved
[00:36:54] simultaneously,
[00:36:56] but I do think
[00:36:58] you know, that is now possible. So
[00:36:59] people have to figure out how does it
[00:37:01] how do we take advantage of this
[00:37:02] capability to do even more math.
[00:37:07] >> We can we can talk so much more about
[00:37:09] this, but I did promise Jeff I'm going
[00:37:11] to give him a pop quiz on stage
[00:37:14] [laughter] and I did not tell him what
[00:37:15] the problem is. Um but it's okay if you
[00:37:18] don't know how to answer it cuz I did
[00:37:19] not remember myself. Um
[00:37:22] >> Great, no pressure.
[00:37:24] >> [laughter]
[00:37:25] >> Do you remember the significance of this
[00:37:27] date, June 12th, 2017?
[00:37:32] >> June 12th, 2017.
[00:37:33] >> Don't cheat with AI.
[00:37:35] >> Oh, well is that the Transformer paper
[00:37:37] on archive?
[00:37:38] >> Amazing, A+. Okay, woo. We have to
[00:37:42] uh yes, that's uh I I had to check which
[00:37:45] day it was.
[00:37:46] >> Okay.
[00:37:47] >> Did you read the Transformer paper on
[00:37:49] June 12th?
[00:37:50] >> No, probably June 10th.
[00:37:51] >> Uh
[00:37:52] oh, yes, that's true. You had to approve
[00:37:54] that probably. So um
[00:37:58] you know, your career I I want to
[00:38:00] reflect a little bit um
[00:38:02] you know, we can talk so much you you
[00:38:05] one of your slides showed that four of
[00:38:07] you collectively have done so much at
[00:38:09] Google and for our field. And uh but
[00:38:12] let's just use that day as kind of a
[00:38:15] historical date, some kind of beginning
[00:38:18] of you know, the generative model era.
[00:38:21] Just share with us
[00:38:23] in this journey since almost 10 years, 9
[00:38:26] years now,
[00:38:28] what in your mind maybe we don't have
[00:38:31] time to say all of them, but the top
[00:38:33] most significant
[00:38:36] technical moment um that for yourself
[00:38:39] personally. And I also want to follow up
[00:38:42] by asking you
[00:38:44] what and intellectually honestly, what
[00:38:47] did you predict correctly and what did
[00:38:51] you predict incorrectly?
[00:38:52] >> Mhm.
[00:38:54] Yeah.
[00:38:55] Uh let's see.
[00:38:56] Um
[00:38:57] I mean, I think a handful of things
[00:39:00] stand out among a bunch of major
[00:39:03] improvements to all the things we did.
[00:39:05] Like that slide that had all those
[00:39:06] different advances. You know, I think
[00:39:08] obviously transformers are a much more
[00:39:11] efficient model architecture for
[00:39:14] tackling these problems. The The idea
[00:39:16] that you save all the states you went
[00:39:18] through and then you attend to them
[00:39:19] rather than trying to update a small
[00:39:21] vector with every state and and forget
[00:39:24] the previous ones was a really great
[00:39:26] insight and has led to um you know, many
[00:39:31] many many advances because the models
[00:39:34] can now learn so much more with so much
[00:39:37] less computation than earlier say
[00:39:39] LSTM-based models.
[00:39:41] Um you know, I think
[00:39:43] uh
[00:39:44] uh the distillation work that Oriol uh
[00:39:47] I and Jeff Hinton did uh which was
[00:39:50] actually rejected from NeurIPS in 2016
[00:39:52] saying it's unlikely to have any impact.
[00:39:54] >> We should have a website that collects
[00:39:56] all the rejected papers that
[00:39:58] >> I mean, that one's pretty good. We threw
[00:39:59] it on archive. It has 40,000 citations
[00:40:02] or something. Um so, I mean, that I
[00:40:04] think has been key to making really
[00:40:07] capable
[00:40:09] inference-efficient models because you
[00:40:11] can take a very large model you've
[00:40:12] trained that's really unwieldy and
[00:40:14] expensive and you can use use it as the
[00:40:17] teacher to teach your now nimble
[00:40:19] lightweight uh
[00:40:20] um
[00:40:22] student model. That's a good thing to
[00:40:23] say in the university.
[00:40:25] Um and so, that that's been good. The
[00:40:27] MoE architecture I think has proven to
[00:40:29] be good. I think one one thing I kind of
[00:40:32] thought was that was going to be the
[00:40:34] beginning of a much more exotic set of
[00:40:37] model architectures. I think, you know,
[00:40:38] the MoE architecture is you you branch
[00:40:40] out to a bunch of experts and then you
[00:40:42] come back and then you branch out again
[00:40:45] and you come back and you learn which
[00:40:46] experts are good at which things which
[00:40:48] is super useful, gives your model a lot
[00:40:50] of capacity, but you then activate only
[00:40:53] a tiny portion of it for any given token
[00:40:55] or task or whatever.
[00:40:57] But, it's still very regular. Like in
[00:40:59] most MOEs, all the experts are the same
[00:41:01] size.
[00:41:03] Uh they come back together immediately.
[00:41:05] I thought we were going to start to have
[00:41:06] like a flourishing of like really wild,
[00:41:09] exotic, more organic-looking neural
[00:41:11] network architectures with like columns
[00:41:14] of
[00:41:15] neural activity, and they come back
[00:41:16] together in some like very uh
[00:41:19] infrequent, but uh large
[00:41:22] cross-connections that would let you
[00:41:23] connect distal parts of your your neural
[00:41:26] net, but we haven't done that yet.
[00:41:28] >> I mean, we thought about that for neural
[00:41:30] architecture search, and that didn't pan
[00:41:32] out either, right?
[00:41:34] >> Yeah, I mean, the the models that come
[00:41:35] out of neural architecture search do
[00:41:37] look much more organic than the kind of
[00:41:39] human-designed ones where you have like
[00:41:41] a bunch of layers, occasionally you have
[00:41:43] a skip connection every layer. The
[00:41:46] neural architecture search ones have
[00:41:47] like these crazy like
[00:41:49] connect this one up to 17 layers above
[00:41:52] and do do something funky.
[00:41:53] >> Yep. So, so that was the one thing you
[00:41:56] think you predicted wrong.
[00:41:58] >> Well, I mean, I predicted many things
[00:41:59] wrong. Uh that's one that that kind of
[00:42:01] stands out as like I thought the MOE
[00:42:04] push would go more in that direction.
[00:42:07] >> Okay.
[00:42:07] >> Um
[00:42:09] you know, I think uh
[00:42:13] coding capability has proven to be
[00:42:15] really important. I didn't necessarily
[00:42:17] foresee that was such a key unlocker for
[00:42:20] making these models really capable in
[00:42:22] solving lots of different kinds of
[00:42:24] problems.
[00:42:25] Um so
[00:42:26] >> That That one I
[00:42:28] I'm with you. We all kind of know, but
[00:42:30] did not
[00:42:32] predict the level of
[00:42:34] >> Yeah.
[00:42:34] >> profoundness.
[00:42:35] >> So, like in the Gemini effort, it was
[00:42:37] one of the things we focused on, but it
[00:42:39] was not like
[00:42:40] the thing we focused on.
[00:42:41] >> Mhm. Okay. Well, there's one thing that
[00:42:45] obviously we'll be nerding on a little
[00:42:47] bit. There we're in a H I conference, so
[00:42:50] we have to talk about the letter H. The
[00:42:52] one thing I wonder if you predicted, and
[00:42:57] how do you feel about that, is
[00:42:59] all the societal impact of AI. And it's
[00:43:02] not just
[00:43:03] impact
[00:43:05] Part of the impact is
[00:43:07] there's jobs, there's the psychological
[00:43:09] anxiety, there's the the the the the
[00:43:13] right now the almost extreme talk about
[00:43:16] human extinction, and alignment, and all
[00:43:19] of that.
[00:43:20] Well, first of all, which one
[00:43:23] Which one worries you the most?
[00:43:25] >> Yeah, I mean, I think it there This is a
[00:43:29] incredibly powerful and general
[00:43:31] technology, and it's influencing nearly
[00:43:34] every aspect of society, right? Like all
[00:43:36] the things that it can do in
[00:43:37] mathematics, or in coding, or in
[00:43:40] generating images, or um you know,
[00:43:43] helping autonomous vehicles drive.
[00:43:46] So, it's
[00:43:47] unlike previous technological
[00:43:49] revolutions, which were a little bit
[00:43:50] more narrowly contained and affected
[00:43:52] deeply
[00:43:53] five or 10 fields, this is
[00:43:55] simultaneously affecting lots and lots
[00:43:58] of things in the world. And I think
[00:43:59] that's a
[00:44:01] you know, it's a source of excitement,
[00:44:04] apprehension, you know, fear, all the
[00:44:07] things. I actually was a co-author with
[00:44:10] an amazing set of co-authors on a paper
[00:44:12] called Shaping AI's Impact on billions
[00:44:15] of people.
[00:44:15] >> Mhm.
[00:44:16] >> Uh that's my only paper with its own
[00:44:18] website, cuz we had an inspired
[00:44:19] co-author, shapingai.com.
[00:44:22] Um but really, we looked at seven
[00:44:24] different areas, including
[00:44:26] uh employment and and economy,
[00:44:29] um AI for science, uh
[00:44:31] you know, dis- misinformation,
[00:44:33] disinformation,
[00:44:35] um media, uh and um
[00:44:39] a few other uh domains. And we talked to
[00:44:42] lots of domain experts in each of those
[00:44:43] domains, and I think that was a a great
[00:44:45] experience, cuz we got their perspective
[00:44:47] on how AI was im- already in impacting
[00:44:50] their fields, and how it was likely to
[00:44:52] impact fields in the future. I mean, the
[00:44:54] one I worry about the most is just
[00:44:57] how do we capture
[00:44:59] as much of the upsides of it what AI can
[00:45:01] do across all these different domains
[00:45:04] while minimizing the downsides in many
[00:45:06] many areas that it
[00:45:08] can affect negatively. And I think
[00:45:11] that is not purely a technical problem.
[00:45:13] That is a technical problem, a
[00:45:16] regulatory and policy-maker problem, a
[00:45:19] citizen problem, and we all need to kind
[00:45:22] of figure out how do we navigate this
[00:45:25] new technology to make sure that it
[00:45:27] serves us all extremely well and doesn't
[00:45:31] harm us in ways that we think it could
[00:45:33] in, you know, so that's things like
[00:45:35] making sure when people's jobs are
[00:45:37] affected, they have good ways to adapt
[00:45:40] to what is now needed in the world and
[00:45:43] and can
[00:45:44] you know, be um
[00:45:46] you know, gainfully employed and and
[00:45:49] have a prosperous existence. And I think
[00:45:51] that is a you know, a
[00:45:53] multi-faceted thing that needs to be
[00:45:55] tackled by lots of people in the world.
[00:45:58] >> So, one thing, this is my last question.
[00:46:00] One thing I know about you, Jeff, that
[00:46:02] most of the public doesn't know is how
[00:46:04] much you care about the young
[00:46:06] generation.
[00:46:07] We don't get to
[00:46:09] be on stage too often, but
[00:46:12] in my memory the last time we were in a
[00:46:15] conference together was Grace Hopper
[00:46:17] conference. You know, you you were going
[00:46:19] there for multiple [clears throat]
[00:46:20] years.
[00:46:21] So, right now we're on a university
[00:46:23] campus
[00:46:25] and frankly, this generation of college
[00:46:28] students are anxious.
[00:46:30] They they're even Stanford students are
[00:46:33] anxious about jobs, anxious about the
[00:46:37] future of
[00:46:38] economy. And as someone who has
[00:46:42] you know, such a successful career being
[00:46:45] an an an a pioneering AI
[00:46:48] and also, you know, just just
[00:46:51] seeing the future in ways that the
[00:46:53] public doesn't see yet.
[00:46:55] What is your parting words for for the
[00:46:58] students in this audience who were
[00:47:00] feeling the anxiety and possibly also
[00:47:03] hope?
[00:47:04] >> Yeah, I mean I think it
[00:47:07] I understand the anxiety for sure
[00:47:09] because the world is changing quickly
[00:47:11] and I think if you're planning for a
[00:47:13] future,
[00:47:14] it's very hard to plan for a future that
[00:47:16] is changing quickly.
[00:47:17] >> Yeah.
[00:47:18] >> Um
[00:47:19] and so
[00:47:20] you know, I think
[00:47:22] the general advice I have is try to
[00:47:24] understand what new technology is
[00:47:26] starting to exist or will exist
[00:47:29] relatively soon and make sure that you
[00:47:31] understand how to use that technology
[00:47:33] for whatever it is you are most
[00:47:35] passionate about.
[00:47:37] Right? That could be you know, um
[00:47:40] being a doctor, that could be, you know,
[00:47:43] uh helping write literature, that could
[00:47:45] be, you know, writing software more
[00:47:47] effectively.
[00:47:48] All of these things I think can be aided
[00:47:51] and empowered by AI, but there's still
[00:47:53] that human element of like humans figure
[00:47:55] out what we want to collectively do.
[00:47:58] And
[00:48:00] you should figure out what it is you
[00:48:01] want to do
[00:48:03] and be the best you can at it and that
[00:48:05] means using all the tools that are uh
[00:48:07] now available.
[00:48:08] >> So, human passion is still timeless in
[00:48:11] the age of AI. Thank you, Jeff. Yeah.
[00:48:14] >> Thank you.
[00:48:15] >> [applause]
