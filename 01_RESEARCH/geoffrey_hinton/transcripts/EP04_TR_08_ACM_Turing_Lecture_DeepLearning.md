# ACM Turing Award Lecture 2018: Hinton & LeCun

- **URL:** https://www.youtube.com/watch?v=VsnQf7exv5I
- **Source VTT:** `EP04_TR_08_ACM_Turing_Lecture_DeepLearning.en-orig.vtt`

---

`[00:00:03]` Good evening.
`[00:00:06]` That worked.
`[00:00:07]` Uh I'm Vivek Sarkar from Georgia Tech
`[00:00:10]` Uh I'm Vivek Sarkar from Georgia Tech
`[00:00:10]` and it gives me great pleasure on behalf
`[00:00:13]` and it gives me great pleasure on behalf
`[00:00:13]` of all the organizers to welcome you
`[00:00:15]` of all the organizers to welcome you
`[00:00:15]` here in Phoenix for FCRC 2019 and to
`[00:00:20]` here in Phoenix for FCRC 2019 and to
`[00:00:20]` also welcome everyone connected on live
`[00:00:22]` also welcome everyone connected on live
`[00:00:23]` stream.
`[00:00:24]` stream.
`[00:00:24]` Uh as we all know and at this point all
`[00:00:27]` Uh as we all know and at this point all
`[00:00:27]` our deans, our provosts, our high-tech
`[00:00:30]` our deans, our provosts, our high-tech
`[00:00:30]` managers know
`[00:00:32]` managers know
`[00:00:32]` uh our conferences are where you find
`[00:00:34]` uh our conferences are where you find
`[00:00:35]` the cutting edge of computer science
`[00:00:36]` the cutting edge of computer science
`[00:00:36]` research.
`[00:00:38]` research.
`[00:00:38]` FCRC was created in 1993
`[00:00:41]` FCRC was created in 1993
`[00:00:41]` with the idea of having a federated
`[00:00:43]` with the idea of having a federated
`[00:00:43]` event every 3 to 4 years at which major
`[00:00:46]` event every 3 to 4 years at which major
`[00:00:46]` conferences can be co-located.
`[00:00:49]` conferences can be co-located.
`[00:00:49]` This year we have a record number of
`[00:00:52]` This year we have a record number of
`[00:00:52]` 2,700
`[00:00:54]` 2,700
`[00:00:54]` participants in 13 major conferences and
`[00:00:57]` participants in 13 major conferences and
`[00:00:57]` many related workshops and tutorials.
`[00:01:01]` many related workshops and tutorials.
`[00:01:01]` Uh that was about 20% more than what we
`[00:01:03]` Uh that was about 20% more than what we
`[00:01:03]` had planned for.
`[00:01:05]` had planned for.
`[00:01:05]` Actually, on that note, if your cell
`[00:01:07]` Actually, on that note, if your cell
`[00:01:07]` phone rings this evening, that's 2,700
`[00:01:10]` phone rings this evening, that's 2,700
`[00:01:10]` people who will remember you for the
`[00:01:11]` people who will remember you for the
`[00:01:11]` rest of your career including everyone
`[00:01:14]` rest of your career including everyone
`[00:01:14]` on live stream.
`[00:01:17]` Uh let me take a moment to read out the
`[00:01:19]` names of all the conferences to remind
`[00:01:21]` names of all the conferences to remind
`[00:01:21]` you who all are here.
`[00:01:23]` you who all are here.
`[00:01:23]` So, we have COLT,
`[00:01:25]` So, we have COLT,
`[00:01:25]` e-Energy, EC, HPDC, ICS, ISCA, ISMM,
`[00:01:32]` e-Energy, EC, HPDC, ICS, ISCA, ISMM,
`[00:01:32]` IWQoS,
`[00:01:34]` IWQoS,
`[00:01:34]` LCTES,
`[00:01:35]` LCTES,
`[00:01:35]` PLDI, SIGMETRICS, SPAA and STOC.
`[00:01:40]` PLDI, SIGMETRICS, SPAA and STOC.
`[00:01:40]` These conferences cover, as you know, a
`[00:01:43]` These conferences cover, as you know, a
`[00:01:43]` wide range of fine foundational areas of
`[00:01:46]` wide range of fine foundational areas of
`[00:01:46]` computer science research including
`[00:01:48]` computer science research including
`[00:01:48]` computer architecture, economics and
`[00:01:50]` computer architecture, economics and
`[00:01:50]` computation, embedded systems, high
`[00:01:53]` computation, embedded systems, high
`[00:01:53]` performance and supercomputing,
`[00:01:55]` performance and supercomputing,
`[00:01:55]` machine learning theory,
`[00:01:57]` machine learning theory,
`[00:01:57]` measurement and modeling,
`[00:01:59]` measurement and modeling,
`[00:01:59]` uh compilers and uh programming
`[00:02:01]` uh compilers and uh programming
`[00:02:01]` languages,
`[00:02:03]` languages,
`[00:02:03]` memory management, parallel algorithms,
`[00:02:05]` memory management, parallel algorithms,
`[00:02:05]` quality of service, smart energy
`[00:02:07]` quality of service, smart energy
`[00:02:07]` systems, theory of computing and many
`[00:02:10]` systems, theory of computing and many
`[00:02:10]` related topics.
`[00:02:12]` related topics.
`[00:02:12]` Um I'm specially pleased from an
`[00:02:14]` Um I'm specially pleased from an
`[00:02:14]` attendance perspective that we also have
`[00:02:16]` attendance perspective that we also have
`[00:02:16]` a record number of over 1,100 students
`[00:02:20]` a record number of over 1,100 students
`[00:02:20]` attending this year.
`[00:02:21]` attending this year.
`[00:02:21]` I'd like to encourage everyone,
`[00:02:23]` I'd like to encourage everyone,
`[00:02:23]` especially the students, to take
`[00:02:24]` especially the students, to take
`[00:02:24]` advantage of the unique opportunity
`[00:02:26]` advantage of the unique opportunity
`[00:02:26]` offered by FCRC
`[00:02:28]` offered by FCRC
`[00:02:28]` to attend sessions in conferences
`[00:02:30]` to attend sessions in conferences
`[00:02:30]` outside your research area as well so
`[00:02:33]` outside your research area as well so
`[00:02:33]` you can be exposed to emerging ideas in
`[00:02:36]` you can be exposed to emerging ideas in
`[00:02:36]` other fields of computer science. Just
`[00:02:38]` other fields of computer science. Just
`[00:02:38]` check out the Hoover app or the online
`[00:02:40]` check out the Hoover app or the online
`[00:02:40]` schedule to see what's going on in the
`[00:02:42]` schedule to see what's going on in the
`[00:02:42]` co-located events.
`[00:02:45]` co-located events.
`[00:02:45]` Now, a major highlight of FCRC is the
`[00:02:47]` Now, a major highlight of FCRC is the
`[00:02:47]` opportunity for you to hear plenary
`[00:02:49]` opportunity for you to hear plenary
`[00:02:49]` talks by eminent leaders from different
`[00:02:52]` talks by eminent leaders from different
`[00:02:52]` areas of computer science
`[00:02:54]` areas of computer science
`[00:02:54]` starting of course uh with today
`[00:02:56]` starting of course uh with today
`[00:02:56]` evening's Turing lecture by Geoff Hinton
`[00:02:59]` evening's Turing lecture by Geoff Hinton
`[00:02:59]` and Yann LeCun.
`[00:03:00]` and Yann LeCun.
`[00:03:00]` All plenary talks will be held in this
`[00:03:02]` All plenary talks will be held in this
`[00:03:02]` beautiful Symphony Hall space.
`[00:03:05]` beautiful Symphony Hall space.
`[00:03:05]` Uh during next week the talks are
`[00:03:07]` Uh during next week the talks are
`[00:03:07]` scheduled at 11:20 in the morning each
`[00:03:09]` scheduled at 11:20 in the morning each
`[00:03:09]` day with no conflicting events so be
`[00:03:12]` day with no conflicting events so be
`[00:03:12]` sure to attend. You have no excuse for
`[00:03:14]` sure to attend. You have no excuse for
`[00:03:14]` missing them.
`[00:03:16]` missing them.
`[00:03:16]` Uh as a reminder the plenary speakers
`[00:03:18]` Uh as a reminder the plenary speakers
`[00:03:18]` next week are Jim Smith,
`[00:03:20]` next week are Jim Smith,
`[00:03:20]` Cynthia Dwork, Sriram Krishnamurthy,
`[00:03:23]` Cynthia Dwork, Sriram Krishnamurthy,
`[00:03:23]` Jeannette Wing and Eric Lindahl and they
`[00:03:25]` Jeannette Wing and Eric Lindahl and they
`[00:03:25]` will all be introduced by Mary Hall, the
`[00:03:28]` will all be introduced by Mary Hall, the
`[00:03:28]` plenary speaker chair for FCRC.
`[00:03:31]` plenary speaker chair for FCRC.
`[00:03:31]` Uh
`[00:03:32]` Uh
`[00:03:32]` though I'll have the opportunity to give
`[00:03:34]` though I'll have the opportunity to give
`[00:03:34]` a more comprehensive round of thanks to
`[00:03:36]` a more comprehensive round of thanks to
`[00:03:36]` everyone at the end of the conference on
`[00:03:38]` everyone at the end of the conference on
`[00:03:38]` Friday,
`[00:03:39]` Friday,
`[00:03:39]` I'd like to definitely express my
`[00:03:41]` I'd like to definitely express my
`[00:03:41]` deepest appreciation to the sponsors of
`[00:03:44]` deepest appreciation to the sponsors of
`[00:03:44]` all conferences and specially the
`[00:03:46]` all conferences and specially the
`[00:03:46]` sponsors listed here for FCRC as a
`[00:03:49]` sponsors listed here for FCRC as a
`[00:03:49]` whole. Uh this is a unique
`[00:03:51]` whole. Uh this is a unique
`[00:03:51]` once-in-4-years event and that's just
`[00:03:53]` once-in-4-years event and that's just
`[00:03:53]` not possible without the companies
`[00:03:56]` not possible without the companies
`[00:03:56]` listed here stepping up to support FCRC.
`[00:03:59]` listed here stepping up to support FCRC.
`[00:03:59]` So, thanks to all of them.
`[00:04:02]` So, thanks to all of them.
`[00:04:02]` Also, the entire ACM team has been
`[00:04:03]` Also, the entire ACM team has been
`[00:04:03]` working hard to make sure that this
`[00:04:05]` working hard to make sure that this
`[00:04:05]` entire week is a success and I'd like to
`[00:04:08]` entire week is a success and I'd like to
`[00:04:08]` specially thank Donna Cappo for her
`[00:04:11]` specially thank Donna Cappo for her
`[00:04:11]` tireless leadership of the conference
`[00:04:13]` tireless leadership of the conference
`[00:04:13]` administration team.
`[00:04:15]` administration team.
`[00:04:15]` Donna's been involved uh with organizing
`[00:04:17]` Donna's been involved uh with organizing
`[00:04:17]` FCRC since its first instance in 1993
`[00:04:22]` FCRC since its first instance in 1993
`[00:04:22]` and is absolutely vital to the success
`[00:04:24]` and is absolutely vital to the success
`[00:04:24]` of FCRC. So, thank you, Donna.
`[00:04:27]` of FCRC. So, thank you, Donna.
`[00:04:27]` Yeah.
`[00:04:33]` And finally, thanks to all of you for
`[00:04:35]` coming to Phoenix for FCRC and for
`[00:04:37]` coming to Phoenix for FCRC and for
`[00:04:37]` filling this room. Uh I hope you have a
`[00:04:40]` filling this room. Uh I hope you have a
`[00:04:40]` great conference and enjoy the numerous
`[00:04:42]` great conference and enjoy the numerous
`[00:04:42]` interactions with all your CS research
`[00:04:45]` interactions with all your CS research
`[00:04:45]` colleagues.
`[00:04:46]` colleagues.
`[00:04:46]` And with that I would like to invite
`[00:04:48]` And with that I would like to invite
`[00:04:48]` Sherry Pancake, president of ACM, to the
`[00:04:51]` Sherry Pancake, president of ACM, to the
`[00:04:51]` stage to introduce the Turing lecture.
`[00:04:56]` Thank you.
`[00:05:02]` I'm delighted to be here at
`[00:05:05]` FCRC.
`[00:05:06]` FCRC.
`[00:05:06]` As Vivek mentioned, I have the honor of
`[00:05:09]` As Vivek mentioned, I have the honor of
`[00:05:09]` being president of ACM, the world's
`[00:05:12]` being president of ACM, the world's
`[00:05:12]` largest society for computing
`[00:05:14]` largest society for computing
`[00:05:14]` professionals. Did you know that ACM has
`[00:05:16]` professionals. Did you know that ACM has
`[00:05:16]` almost 100,000 members around the globe?
`[00:05:20]` almost 100,000 members around the globe?
`[00:05:20]` We serve the computing community in 190
`[00:05:24]` We serve the computing community in 190
`[00:05:24]` countries with our conferences like
`[00:05:27]` countries with our conferences like
`[00:05:27]` these, our publications, webinars and
`[00:05:30]` these, our publications, webinars and
`[00:05:30]` learning resources. ACM is also very
`[00:05:33]` learning resources. ACM is also very
`[00:05:33]` active in computing education and
`[00:05:36]` active in computing education and
`[00:05:36]` curriculum guidelines around the world.
`[00:05:40]` curriculum guidelines around the world.
`[00:05:40]` It's particularly great to be here at
`[00:05:42]` It's particularly great to be here at
`[00:05:42]` FCRC because of the reasons that Vivek
`[00:05:45]` FCRC because of the reasons that Vivek
`[00:05:45]` mentioned, what a unique opportunity it
`[00:05:48]` mentioned, what a unique opportunity it
`[00:05:48]` is. We all know that computing has
`[00:05:51]` is. We all know that computing has
`[00:05:51]` become much more interdisciplinary
`[00:05:53]` become much more interdisciplinary
`[00:05:53]` but it's not often that we have the
`[00:05:56]` but it's not often that we have the
`[00:05:56]` chance to meet and interact with leading
`[00:05:59]` chance to meet and interact with leading
`[00:05:59]` researchers from other areas outside our
`[00:06:02]` researchers from other areas outside our
`[00:06:02]` own. I really encourage you to take
`[00:06:05]` own. I really encourage you to take
`[00:06:05]` advantage of that this week.
`[00:06:08]` advantage of that this week.
`[00:06:08]` As all of us know, AI is the most
`[00:06:11]` As all of us know, AI is the most
`[00:06:11]` rapidly growing area in all the sciences
`[00:06:14]` rapidly growing area in all the sciences
`[00:06:14]` and certainly a hot topic in society at
`[00:06:17]` and certainly a hot topic in society at
`[00:06:17]` large.
`[00:06:19]` large.
`[00:06:19]` The incredible advances that we've been
`[00:06:21]` The incredible advances that we've been
`[00:06:21]` seeing in AI would not have been
`[00:06:24]` seeing in AI would not have been
`[00:06:24]` possible without some of the foundations
`[00:06:28]` possible without some of the foundations
`[00:06:28]` let
`[00:06:29]` let
`[00:06:29]` that were established by people like
`[00:06:31]` that were established by people like
`[00:06:31]` those were honoring tonight. For
`[00:06:34]` those were honoring tonight. For
`[00:06:34]` example,
`[00:06:36]` example,
`[00:06:36]` when we think about impact, think about
`[00:06:39]` when we think about impact, think about
`[00:06:39]` the research that went into development
`[00:06:42]` the research that went into development
`[00:06:42]` of GPUs originally in the gaming
`[00:06:45]` of GPUs originally in the gaming
`[00:06:45]` industry. Who would have imagined at
`[00:06:47]` industry. Who would have imagined at
`[00:06:47]` that point that later they would be
`[00:06:49]` that point that later they would be
`[00:06:49]` assembled into large arrays and used as
`[00:06:53]` assembled into large arrays and used as
`[00:06:53]` a platform for vast neural networks that
`[00:06:56]` a platform for vast neural networks that
`[00:06:56]` in turn have driven just leapfrog
`[00:07:00]` in turn have driven just leapfrog
`[00:07:00]` advances in fields like robotics and
`[00:07:03]` advances in fields like robotics and
`[00:07:03]` computer vision.
`[00:07:06]` computer vision.
`[00:07:06]` The kinds of advances that we're
`[00:07:08]` The kinds of advances that we're
`[00:07:08]` recognizing tonight are those generally
`[00:07:10]` recognizing tonight are those generally
`[00:07:10]` in the area of deep learning.
`[00:07:14]` in the area of deep learning.
`[00:07:14]` Billions of people around the world
`[00:07:16]` Billions of people around the world
`[00:07:16]` benefit from the machine learning
`[00:07:19]` benefit from the machine learning
`[00:07:19]` advantages. Anybody with a smartphone
`[00:07:22]` advantages. Anybody with a smartphone
`[00:07:22]` has access to just amazing advances in
`[00:07:25]` has access to just amazing advances in
`[00:07:25]` things like computer vision and speech
`[00:07:27]` things like computer vision and speech
`[00:07:27]` recognition that we never even dreamed
`[00:07:30]` recognition that we never even dreamed
`[00:07:30]` of just a few years ago.
`[00:07:33]` of just a few years ago.
`[00:07:33]` Even more importantly perhaps, machine
`[00:07:36]` Even more importantly perhaps, machine
`[00:07:36]` learning has been giving scientists new
`[00:07:39]` learning has been giving scientists new
`[00:07:39]` tools that are allowing them to make
`[00:07:41]` tools that are allowing them to make
`[00:07:41]` advances in fields from medicine to
`[00:07:44]` advances in fields from medicine to
`[00:07:44]` astronomy and material science.
`[00:07:49]` FCRC only happens every 4 years. So,
`[00:07:52]` when we talked about this session, we
`[00:07:54]` when we talked about this session, we
`[00:07:54]` wanted to do something special for the
`[00:07:56]` wanted to do something special for the
`[00:07:56]` welcome session. I think you'll agree
`[00:07:59]` welcome session. I think you'll agree
`[00:07:59]` with me that hearing from this year's
`[00:08:01]` with me that hearing from this year's
`[00:08:01]` laureates of the Turing Prize is the way
`[00:08:05]` laureates of the Turing Prize is the way
`[00:08:05]` to make it really special.
`[00:08:07]` to make it really special.
`[00:08:07]` The 2018
`[00:08:09]` The 2018
`[00:08:09]` ACM A.M. Turing Award was presented just
`[00:08:13]` ACM A.M. Turing Award was presented just
`[00:08:13]` last week in San Francisco to three
`[00:08:16]` last week in San Francisco to three
`[00:08:16]` pioneers of deep learning,
`[00:08:18]` pioneers of deep learning,
`[00:08:19]` Yoshua Bengio, Geoffrey Hinton and Yann
`[00:08:22]` Yoshua Bengio, Geoffrey Hinton and Yann
`[00:08:22]` LeCun.
`[00:08:24]` LeCun.
`[00:08:24]` The three of them collectively and
`[00:08:26]` The three of them collectively and
`[00:08:27]` independently worked over a 30-year
`[00:08:30]` independently worked over a 30-year
`[00:08:30]` period to develop, first of all, the
`[00:08:32]` period to develop, first of all, the
`[00:08:32]` conceptual foundations for deep neural
`[00:08:35]` conceptual foundations for deep neural
`[00:08:35]` networks
`[00:08:37]` networks
`[00:08:37]` and then performed experimentation
`[00:08:39]` and then performed experimentation
`[00:08:39]` that ended up identifying a lot of very
`[00:08:41]` that ended up identifying a lot of very
`[00:08:42]` interesting phenomena. But they didn't
`[00:08:44]` interesting phenomena. But they didn't
`[00:08:44]` stop there. They went on to develop
`[00:08:47]` stop there. They went on to develop
`[00:08:47]` engineering advances that demonstrated
`[00:08:50]` engineering advances that demonstrated
`[00:08:50]` conclusively
`[00:08:52]` conclusively
`[00:08:52]` that deep
`[00:08:54]` that deep
`[00:08:54]` neural nets could actually be applied in
`[00:08:57]` neural nets could actually be applied in
`[00:08:57]` practice and in an economic way.
`[00:09:01]` practice and in an economic way.
`[00:09:01]` This in turn allowed other people to
`[00:09:05]` This in turn allowed other people to
`[00:09:05]` develop these amazing
`[00:09:08]` develop these amazing
`[00:09:08]` concepts that we are now and advances
`[00:09:10]` concepts that we are now and advances
`[00:09:10]` that we are now benefiting from in so
`[00:09:13]` that we are now benefiting from in so
`[00:09:13]` many different areas, computer vision,
`[00:09:17]` many different areas, computer vision,
`[00:09:17]` speech recognition, natural language
`[00:09:19]` speech recognition, natural language
`[00:09:19]` processing, robotics, so many different
`[00:09:22]` processing, robotics, so many different
`[00:09:22]` other areas. So, it is with great
`[00:09:25]` other areas. So, it is with great
`[00:09:25]` pleasure that I am able to introduce
`[00:09:28]` pleasure that I am able to introduce
`[00:09:28]` tonight's speakers. The first is Geoff
`[00:09:31]` tonight's speakers. The first is Geoff
`[00:09:31]` Hinton who will be giving his Turing
`[00:09:34]` Hinton who will be giving his Turing
`[00:09:34]` lecture on the topic The Digital
`[00:09:37]` lecture on the topic The Digital
`[00:09:37]` Learning Revolution. He will be followed
`[00:09:39]` Learning Revolution. He will be followed
`[00:09:39]` by Yann LeCun who very fittingly has
`[00:09:42]` by Yann LeCun who very fittingly has
`[00:09:42]` called his
`[00:09:43]` called his
`[00:09:43]` talk
`[00:09:45]` talk
`[00:09:45]` The Deep Learning Revolution: The
`[00:09:46]` The Deep Learning Revolution: The
`[00:09:46]` Sequel. So, Geoffrey, I'd like to
`[00:09:49]` Sequel. So, Geoffrey, I'd like to
`[00:09:49]` welcome you.
`[00:09:52]` welcome you.
`[00:09:52]` [applause]
`[00:09:54]` Thank you.
`[00:09:57]` [applause]
`[00:10:05]` I'd first like to thank all the people
`[00:10:07]` at ACM who devote their time to making
`[00:10:10]` at ACM who devote their time to making
`[00:10:10]` all of this run smoothly.
`[00:10:14]` So,
`[00:10:16]` there've been two paradigms for AI.
`[00:10:19]` there've been two paradigms for AI.
`[00:10:19]` Um since the 1950s, there's been the
`[00:10:22]` Um since the 1950s, there's been the
`[00:10:22]` logic-inspired approach
`[00:10:24]` logic-inspired approach
`[00:10:24]` where the essence of intelligence is
`[00:10:26]` where the essence of intelligence is
`[00:10:26]` seen as symbolic expressions operated on
`[00:10:29]` seen as symbolic expressions operated on
`[00:10:29]` by symbolic rules,
`[00:10:31]` by symbolic rules,
`[00:10:31]` and the main problem has been reasoning.
`[00:10:34]` and the main problem has been reasoning.
`[00:10:34]` How do we get
`[00:10:36]` How do we get
`[00:10:36]` a computer to do reasoning like people
`[00:10:38]` a computer to do reasoning like people
`[00:10:38]` do?
`[00:10:40]` do?
`[00:10:40]` And there's been the biologically
`[00:10:41]` And there's been the biologically
`[00:10:41]` inspired approach,
`[00:10:42]` inspired approach,
`[00:10:42]` which is very different. Um it sees the
`[00:10:46]` which is very different. Um it sees the
`[00:10:46]` essence of intelligence as learning the
`[00:10:48]` essence of intelligence as learning the
`[00:10:48]` connection strengths within a neural
`[00:10:49]` connection strengths within a neural
`[00:10:49]` network,
`[00:10:50]` network,
`[00:10:50]` and the main things to focus on, at
`[00:10:52]` and the main things to focus on, at
`[00:10:52]` least to begin with,
`[00:10:53]` least to begin with,
`[00:10:53]` are learning and perception.
`[00:10:55]` are learning and perception.
`[00:10:55]` So, they're very different paradigms
`[00:10:57]` So, they're very different paradigms
`[00:10:57]` with very different initial goals.
`[00:11:01]` They have very different views of the
`[00:11:02]` internal representations that should be
`[00:11:04]` internal representations that should be
`[00:11:04]` used.
`[00:11:05]` used.
`[00:11:05]` So, the symbolic paradigm thinks that
`[00:11:08]` So, the symbolic paradigm thinks that
`[00:11:08]` um you should use symbolic expressions,
`[00:11:11]` um you should use symbolic expressions,
`[00:11:11]` and you can give these to the computer
`[00:11:13]` and you can give these to the computer
`[00:11:13]` if you invent a good language to express
`[00:11:15]` if you invent a good language to express
`[00:11:15]` them in,
`[00:11:16]` them in,
`[00:11:16]` and you can of course get new
`[00:11:17]` and you can of course get new
`[00:11:17]` expressions within the computer by
`[00:11:19]` expressions within the computer by
`[00:11:19]` applying rules.
`[00:11:20]` applying rules.
`[00:11:20]` The biological paradigm thinks the
`[00:11:22]` The biological paradigm thinks the
`[00:11:22]` internal representations are nothing at
`[00:11:25]` internal representations are nothing at
`[00:11:25]` all like language.
`[00:11:26]` all like language.
`[00:11:26]` They're just big vectors of neural
`[00:11:28]` They're just big vectors of neural
`[00:11:28]` activity, and these big vectors have
`[00:11:29]` activity, and these big vectors have
`[00:11:30]` causal effects on other big vectors.
`[00:11:33]` causal effects on other big vectors.
`[00:11:33]` And these vectors are going to be
`[00:11:34]` And these vectors are going to be
`[00:11:34]` learned from data. So, all the structure
`[00:11:36]` learned from data. So, all the structure
`[00:11:36]` in these vectors is going to be learned
`[00:11:38]` in these vectors is going to be learned
`[00:11:38]` from data. I'm obviously giving sort of
`[00:11:40]` from data. I'm obviously giving sort of
`[00:11:40]` caricatures of the two positions to
`[00:11:42]` caricatures of the two positions to
`[00:11:42]` emphasize how different they are.
`[00:11:46]` They lead to two very different ways of
`[00:11:47]` trying to get a computer to do what you
`[00:11:49]` trying to get a computer to do what you
`[00:11:49]` want.
`[00:11:50]` want.
`[00:11:50]` So,
`[00:11:51]` So,
`[00:11:51]` um
`[00:11:53]` um
`[00:11:53]` one method which I slightly naughtily
`[00:11:55]` one method which I slightly naughtily
`[00:11:55]` call intelligent design is what you
`[00:11:57]` call intelligent design is what you
`[00:11:57]` would call programming. Um it's you
`[00:11:59]` would call programming. Um it's you
`[00:11:59]` figure out how to solve the problem, and
`[00:12:01]` figure out how to solve the problem, and
`[00:12:01]` then you tell the computer exactly what
`[00:12:03]` then you tell the computer exactly what
`[00:12:03]` to do.
`[00:12:05]` to do.
`[00:12:05]` The other method is you just show the
`[00:12:07]` The other method is you just show the
`[00:12:07]` computer a lot of examples
`[00:12:09]` computer a lot of examples
`[00:12:09]` of inputs and the outputs it should
`[00:12:11]` of inputs and the outputs it should
`[00:12:11]` produce, and you let the computer figure
`[00:12:12]` produce, and you let the computer figure
`[00:12:12]` it out. Of course, you have to program
`[00:12:14]` it out. Of course, you have to program
`[00:12:14]` the computer there, too, but it's
`[00:12:16]` the computer there, too, but it's
`[00:12:16]` programmed once with some
`[00:12:17]` programmed once with some
`[00:12:17]` general-purpose learning algorithm.
`[00:12:20]` general-purpose learning algorithm.
`[00:12:20]` That again is a simplification.
`[00:12:23]` So, an example of a kind of thing that
`[00:12:25]` people spent 50 years trying to do with
`[00:12:27]` people spent 50 years trying to do with
`[00:12:27]` symbolic AI
`[00:12:28]` symbolic AI
`[00:12:28]` is take an image and describe what's in
`[00:12:30]` is take an image and describe what's in
`[00:12:30]` the image.
`[00:12:32]` the image.
`[00:12:32]` So, think about taking the millions of
`[00:12:35]` So, think about taking the millions of
`[00:12:35]` pixels
`[00:12:37]` pixels
`[00:12:37]` in
`[00:12:38]` in
`[00:12:38]` the image on the left
`[00:12:40]` the image on the left
`[00:12:40]` and converting them to a string of
`[00:12:41]` and converting them to a string of
`[00:12:42]` words. It's not obvious how you'd write
`[00:12:43]` words. It's not obvious how you'd write
`[00:12:43]` that program. People tried for a long
`[00:12:46]` that program. People tried for a long
`[00:12:46]` time, and they couldn't write that
`[00:12:47]` time, and they couldn't write that
`[00:12:47]` program.
`[00:12:48]` program.
`[00:12:48]` Um people doing neural nets also tried
`[00:12:51]` Um people doing neural nets also tried
`[00:12:51]` for a long time, and in the end, they
`[00:12:53]` for a long time, and in the end, they
`[00:12:53]` managed to get a system that worked
`[00:12:54]` managed to get a system that worked
`[00:12:54]` quite well, which was based on the pure
`[00:12:57]` quite well, which was based on the pure
`[00:12:57]` learning approach.
`[00:13:00]` So, the central question for neural nets
`[00:13:03]` was always
`[00:13:04]` was always
`[00:13:04]` we know that big neural nets with lots
`[00:13:06]` we know that big neural nets with lots
`[00:13:06]` of layers and non-linear processing
`[00:13:08]` of layers and non-linear processing
`[00:13:08]` elements can compute complicated things,
`[00:13:11]` elements can compute complicated things,
`[00:13:11]` at least we believe they can. Um
`[00:13:13]` at least we believe they can. Um
`[00:13:13]` but the question is, can they learn to
`[00:13:14]` but the question is, can they learn to
`[00:13:14]` do it?
`[00:13:16]` do it?
`[00:13:16]` So, can you learn a task like object
`[00:13:18]` So, can you learn a task like object
`[00:13:18]` recognition or machine translation
`[00:13:20]` recognition or machine translation
`[00:13:20]` by taking a big net and starting from
`[00:13:22]` by taking a big net and starting from
`[00:13:22]` random weights,
`[00:13:23]` random weights,
`[00:13:23]` and somehow training it so it changes
`[00:13:26]` and somehow training it so it changes
`[00:13:26]` the weights, so it changes what it
`[00:13:27]` the weights, so it changes what it
`[00:13:28]` computes?
`[00:13:31]` There's an obvious learning algorithm
`[00:13:33]` for such systems, which was proposed by
`[00:13:36]` for such systems, which was proposed by
`[00:13:36]` Turing and by Selfridge and by many
`[00:13:38]` Turing and by Selfridge and by many
`[00:13:38]` other people, variations of it.
`[00:13:40]` other people, variations of it.
`[00:13:40]` And the idea is you start with random
`[00:13:41]` And the idea is you start with random
`[00:13:41]` weights. So, this is how Turing believed
`[00:13:44]` weights. So, this is how Turing believed
`[00:13:44]` human intelligence works. You start with
`[00:13:46]` human intelligence works. You start with
`[00:13:46]` random weights, and rewards and
`[00:13:48]` random weights, and rewards and
`[00:13:48]` punishments cause you to change the
`[00:13:50]` punishments cause you to change the
`[00:13:50]` connection strengths, so you eventually
`[00:13:52]` connection strengths, so you eventually
`[00:13:52]` learn stuff.
`[00:13:53]` learn stuff.
`[00:13:53]` Um this is extremely inefficient. It
`[00:13:56]` Um this is extremely inefficient. It
`[00:13:56]` will work, but it's extremely
`[00:13:57]` will work, but it's extremely
`[00:13:57]` inefficient.
`[00:14:00]` In the 1960s,
`[00:14:02]` Rosenblatt introduced a fairly simple
`[00:14:05]` Rosenblatt introduced a fairly simple
`[00:14:05]` and efficient learning procedure, much
`[00:14:07]` and efficient learning procedure, much
`[00:14:07]` more efficient than random trial and
`[00:14:08]` more efficient than random trial and
`[00:14:08]` error,
`[00:14:09]` error,
`[00:14:09]` that could figure out how to learn the
`[00:14:11]` that could figure out how to learn the
`[00:14:11]` weights on features
`[00:14:14]` weights on features
`[00:14:14]` in which you extract features from the
`[00:14:16]` in which you extract features from the
`[00:14:16]` image, and then you combine the features
`[00:14:20]` image, and then you combine the features
`[00:14:20]` using weights to make a decision.
`[00:14:23]` using weights to make a decision.
`[00:14:23]` And he managed to show you can do some
`[00:14:25]` And he managed to show you can do some
`[00:14:25]` things like that, some moderately
`[00:14:27]` things like that, some moderately
`[00:14:27]` impressive things.
`[00:14:28]` impressive things.
`[00:14:28]` But the the in perceptrons, you don't
`[00:14:30]` But the the in perceptrons, you don't
`[00:14:30]` learn the features.
`[00:14:32]` learn the features.
`[00:14:32]` That again is a simplification.
`[00:14:33]` That again is a simplification.
`[00:14:33]` Rosenblatt had all sorts of ideas about
`[00:14:35]` Rosenblatt had all sorts of ideas about
`[00:14:35]` how you would learn the features, but he
`[00:14:36]` how you would learn the features, but he
`[00:14:36]` didn't invent backpropagation.
`[00:14:38]` didn't invent backpropagation.
`[00:14:39]` In 1969, Minsky and Papert showed that
`[00:14:42]` In 1969, Minsky and Papert showed that
`[00:14:42]` the kinds of perceptrons that Rosenblatt
`[00:14:43]` the kinds of perceptrons that Rosenblatt
`[00:14:43]` had got to work were very limited in
`[00:14:46]` had got to work were very limited in
`[00:14:46]` what they could do. There were some
`[00:14:47]` what they could do. There were some
`[00:14:47]` fairly simple things they were unable to
`[00:14:49]` fairly simple things they were unable to
`[00:14:49]` do,
`[00:14:50]` do,
`[00:14:50]` and Minsky and Papert strongly implied
`[00:14:53]` and Minsky and Papert strongly implied
`[00:14:53]` that making them deeper wouldn't help,
`[00:14:55]` that making them deeper wouldn't help,
`[00:14:55]` and better learning algorithms wouldn't
`[00:14:56]` and better learning algorithms wouldn't
`[00:14:56]` help. There was a basic limitation of
`[00:14:58]` help. There was a basic limitation of
`[00:14:58]` this way of doing things.
`[00:14:59]` this way of doing things.
`[00:14:59]` Um and that led to the first neural net
`[00:15:01]` Um and that led to the first neural net
`[00:15:01]` winter.
`[00:15:05]` In the 1970s and the 1980s, many
`[00:15:08]` different groups invented the
`[00:15:09]` different groups invented the
`[00:15:09]` backpropagation algorithm, variations of
`[00:15:11]` backpropagation algorithm, variations of
`[00:15:11]` it.
`[00:15:12]` it.
`[00:15:12]` Um and backpropagation allows a neural
`[00:15:15]` Um and backpropagation allows a neural
`[00:15:15]` network to learn the feature detectors,
`[00:15:18]` network to learn the feature detectors,
`[00:15:18]` and have multiple layers of learned
`[00:15:19]` and have multiple layers of learned
`[00:15:19]` feature detectors.
`[00:15:21]` feature detectors.
`[00:15:21]` That created a lot of excitement.
`[00:15:25]` It allowed neural networks, for example,
`[00:15:27]` to convert words into
`[00:15:31]` to convert words into
`[00:15:31]` vectors that represented the meanings of
`[00:15:33]` vectors that represented the meanings of
`[00:15:33]` the words, and they could do that just
`[00:15:35]` the words, and they could do that just
`[00:15:35]` by trying to predict the next word.
`[00:15:38]` by trying to predict the next word.
`[00:15:38]` And it looked as if it might be able to
`[00:15:40]` And it looked as if it might be able to
`[00:15:40]` solve tough problems like speech
`[00:15:43]` solve tough problems like speech
`[00:15:43]` recognition and shape recognition. And
`[00:15:45]` recognition and shape recognition. And
`[00:15:45]` indeed, it did solve it did do
`[00:15:47]` indeed, it did solve it did do
`[00:15:47]` moderately well at speech recognition,
`[00:15:49]` moderately well at speech recognition,
`[00:15:49]` and for some forms of shape recognition
`[00:15:51]` and for some forms of shape recognition
`[00:15:51]` it did very well, like Yann LeCun's
`[00:15:53]` it did very well, like Yann LeCun's
`[00:15:53]` networks that read handwriting.
`[00:15:58]` But um what I'm going to do now is
`[00:16:00]` explain
`[00:16:02]` explain
`[00:16:02]` very briefly how neural networks work. I
`[00:16:04]` very briefly how neural networks work. I
`[00:16:04]` know most of you will know this, but I
`[00:16:06]` know most of you will know this, but I
`[00:16:06]` just want to go over it just in case. Um
`[00:16:09]` just want to go over it just in case. Um
`[00:16:09]` so, we make a gross idealization of a
`[00:16:11]` so, we make a gross idealization of a
`[00:16:11]` neuron,
`[00:16:12]` neuron,
`[00:16:12]` and
`[00:16:13]` and
`[00:16:13]` the aim of this idealization is to get
`[00:16:15]` the aim of this idealization is to get
`[00:16:15]` something that can learn so that we can
`[00:16:17]` something that can learn so that we can
`[00:16:17]` study how you put all these things
`[00:16:19]` study how you put all these things
`[00:16:19]` together to learn something complicated
`[00:16:21]` together to learn something complicated
`[00:16:21]` in big networks of these things.
`[00:16:23]` in big networks of these things.
`[00:16:23]` So, it has some incoming weights that
`[00:16:24]` So, it has some incoming weights that
`[00:16:24]` you can vary, or the learning algorithm
`[00:16:27]` you can vary, or the learning algorithm
`[00:16:27]` will vary, and it gives an output that's
`[00:16:29]` will vary, and it gives an output that's
`[00:16:29]` just equal to its input provided the
`[00:16:31]` just equal to its input provided the
`[00:16:31]` input's over a certain amount. So, it's
`[00:16:33]` input's over a certain amount. So, it's
`[00:16:33]` a recti- That's a rectified linear
`[00:16:34]` a recti- That's a rectified linear
`[00:16:34]` neuron, which we actually didn't start
`[00:16:36]` neuron, which we actually didn't start
`[00:16:36]` using till later, but these are the
`[00:16:38]` using till later, but these are the
`[00:16:38]` kinds of neurons that work very well.
`[00:16:41]` And then you hook them up into a
`[00:16:43]` network,
`[00:16:44]` network,
`[00:16:44]` and you have weights on the incoming
`[00:16:48]` and you have weights on the incoming
`[00:16:48]` weights for each of these neurons. And
`[00:16:49]` weights for each of these neurons. And
`[00:16:49]` as you change those incoming weights,
`[00:16:51]` as you change those incoming weights,
`[00:16:51]` you're changing what feature that neuron
`[00:16:53]` you're changing what feature that neuron
`[00:16:53]` will respond to. So, by learning these
`[00:16:55]` will respond to. So, by learning these
`[00:16:55]` weights, you're learning the features.
`[00:16:57]` weights, you're learning the features.
`[00:16:57]` You put in a few hidden layers,
`[00:16:59]` You put in a few hidden layers,
`[00:16:59]` and then you'd like to train it so that
`[00:17:00]` and then you'd like to train it so that
`[00:17:00]` the output neurons do what you like. So,
`[00:17:03]` the output neurons do what you like. So,
`[00:17:03]` for example, we might show it images of
`[00:17:04]` for example, we might show it images of
`[00:17:04]` dogs and cats, and we might like the
`[00:17:06]` dogs and cats, and we might like the
`[00:17:06]` left neuron to turn on for a dog and the
`[00:17:08]` left neuron to turn on for a dog and the
`[00:17:08]` right one for a cat.
`[00:17:10]` right one for a cat.
`[00:17:10]` And the question is, how are we going to
`[00:17:11]` And the question is, how are we going to
`[00:17:11]` train it?
`[00:17:14]` So, there's two kinds of learning
`[00:17:16]` algorithms, mainly. Oh, there's three
`[00:17:18]` algorithms, mainly. Oh, there's three
`[00:17:18]` actually three, but the third one
`[00:17:19]` actually three, but the third one
`[00:17:19]` doesn't work very well. That's called
`[00:17:20]` doesn't work very well. That's called
`[00:17:21]` reinforcement learning. Um
`[00:17:25]` there's a wonderful reductio ad absurdum
`[00:17:27]` of reinforcement learning called
`[00:17:28]` of reinforcement learning called
`[00:17:29]` DeepMind. Um
`[00:17:30]` DeepMind. Um
`[00:17:30]` so,
`[00:17:33]` so,
`[00:17:33]` that was a joke. There's um
`[00:17:35]` that was a joke. There's um
`[00:17:35]` supervised training, where you show the
`[00:17:37]` supervised training, where you show the
`[00:17:37]` network what the output ought to be,
`[00:17:39]` network what the output ought to be,
`[00:17:39]` and you adjust the weights until it
`[00:17:42]` and you adjust the weights until it
`[00:17:42]` produces the output you want.
`[00:17:43]` produces the output you want.
`[00:17:43]` And for that, you need to know what the
`[00:17:44]` And for that, you need to know what the
`[00:17:45]` output ought to be. And there's
`[00:17:46]` output ought to be. And there's
`[00:17:46]` unsupervised learning, where you take
`[00:17:48]` unsupervised learning, where you take
`[00:17:48]` some data,
`[00:17:49]` some data,
`[00:17:49]` and you try and represent that data in
`[00:17:52]` and you try and represent that data in
`[00:17:52]` the hidden layers in such a way that you
`[00:17:53]` the hidden layers in such a way that you
`[00:17:54]` can reconstruct the data, or perhaps
`[00:17:56]` can reconstruct the data, or perhaps
`[00:17:56]` reconstruct parts of the data. If I
`[00:17:58]` reconstruct parts of the data. If I
`[00:17:58]` blank out small parts of the data, can I
`[00:17:59]` blank out small parts of the data, can I
`[00:17:59]` reconstruct them now from the hidden
`[00:18:00]` reconstruct them now from the hidden
`[00:18:01]` layers?
`[00:18:01]` layers?
`[00:18:02]` That's uns- That's the way unsupervised
`[00:18:04]` That's uns- That's the way unsupervised
`[00:18:04]` learning typically works in neural nets.
`[00:18:08]` So, here's a really inefficient way to
`[00:18:10]` do supervised learning by using a
`[00:18:12]` do supervised learning by using a
`[00:18:12]` mutational reinforcement kind of method.
`[00:18:14]` mutational reinforcement kind of method.
`[00:18:14]` What you would do is you take your
`[00:18:16]` What you would do is you take your
`[00:18:16]` neural net, you give it some a typical
`[00:18:18]` neural net, you give it some a typical
`[00:18:18]` set of examples, you'd see how well it
`[00:18:20]` set of examples, you'd see how well it
`[00:18:20]` did, you'd then take one weight, and
`[00:18:23]` did, you'd then take one weight, and
`[00:18:23]` you'd change that weight slightly, and
`[00:18:25]` you'd change that weight slightly, and
`[00:18:25]` you'd see if the neural net does better
`[00:18:26]` you'd see if the neural net does better
`[00:18:26]` or worse.
`[00:18:27]` or worse.
`[00:18:27]` If it does better, you keep that change.
`[00:18:30]` If it does better, you keep that change.
`[00:18:30]` If it does worse, um you throw it away.
`[00:18:33]` If it does worse, um you throw it away.
`[00:18:33]` Perhaps you change in the opposite
`[00:18:34]` Perhaps you change in the opposite
`[00:18:34]` direction, and that's already a factor
`[00:18:36]` direction, and that's already a factor
`[00:18:36]` of two improvement. Um
`[00:18:38]` of two improvement. Um
`[00:18:38]` but this is an incredibly slow learning
`[00:18:40]` but this is an incredibly slow learning
`[00:18:40]` algorithm. It will work,
`[00:18:42]` algorithm. It will work,
`[00:18:42]` but what it achieves can be achieved
`[00:18:44]` but what it achieves can be achieved
`[00:18:44]` many, many times faster by
`[00:18:46]` many, many times faster by
`[00:18:46]` backpropagation. So, you can think of
`[00:18:48]` backpropagation. So, you can think of
`[00:18:48]` backpropagation as just an efficient
`[00:18:49]` backpropagation as just an efficient
`[00:18:49]` version of this algorithm.
`[00:18:52]` version of this algorithm.
`[00:18:52]` So, in backpropagation,
`[00:18:54]` So, in backpropagation,
`[00:18:54]` instead of changing a weight and
`[00:18:57]` instead of changing a weight and
`[00:18:57]` measuring what effect that has on the
`[00:18:59]` measuring what effect that has on the
`[00:18:59]` performance of the network,
`[00:19:01]` performance of the network,
`[00:19:01]` what you do is you use the fact that all
`[00:19:03]` what you do is you use the fact that all
`[00:19:03]` of the weights of the network are inside
`[00:19:04]` of the weights of the network are inside
`[00:19:04]` the computer,
`[00:19:06]` the computer,
`[00:19:06]` you use that fact to compute what the
`[00:19:08]` you use that fact to compute what the
`[00:19:08]` effect of a weight change would be on
`[00:19:09]` effect of a weight change would be on
`[00:19:09]` the performance, and you do that for all
`[00:19:11]` the performance, and you do that for all
`[00:19:11]` of the weights in parallel. So, if you
`[00:19:13]` of the weights in parallel. So, if you
`[00:19:13]` have a million weights, you can compute
`[00:19:16]` have a million weights, you can compute
`[00:19:16]` for all of them in parallel what the
`[00:19:18]` for all of them in parallel what the
`[00:19:18]` effect of a small change in that weight
`[00:19:19]` effect of a small change in that weight
`[00:19:19]` would be on the performance, and then
`[00:19:21]` would be on the performance, and then
`[00:19:21]` you can update them all in parallel.
`[00:19:23]` you can update them all in parallel.
`[00:19:23]` That has its own problems, but it'll go
`[00:19:25]` That has its own problems, but it'll go
`[00:19:25]` a million times faster than the previous
`[00:19:26]` a million times faster than the previous
`[00:19:26]` algorithm.
`[00:19:28]` algorithm.
`[00:19:28]` Um
`[00:19:29]` Um
`[00:19:29]` many people in the press described that
`[00:19:31]` many people in the press described that
`[00:19:31]` as an exponential speed up. Actually,
`[00:19:33]` as an exponential speed up. Actually,
`[00:19:33]` it's a linear speed up. Um the term
`[00:19:35]` it's a linear speed up. Um the term
`[00:19:35]` exponentially is used quadratically too
`[00:19:37]` exponentially is used quadratically too
`[00:19:37]` often.
`[00:19:42]` So,
`[00:19:43]` um we get to backpropagation, where
`[00:19:47]` um we get to backpropagation, where
`[00:19:47]` you do a forward pass through the net,
`[00:19:49]` you do a forward pass through the net,
`[00:19:49]` you look to see what the outputs are,
`[00:19:51]` you look to see what the outputs are,
`[00:19:51]` and then, using the difference between
`[00:19:53]` and then, using the difference between
`[00:19:53]` what you got and what you wanted, you do
`[00:19:54]` what you got and what you wanted, you do
`[00:19:54]` a backwards pass, which has much the
`[00:19:56]` a backwards pass, which has much the
`[00:19:56]` same flavor as the forward pass. It's
`[00:19:58]` same flavor as the forward pass. It's
`[00:19:58]` just
`[00:19:59]` just
`[00:19:59]` high school calculus or
`[00:20:01]` high school calculus or
`[00:20:01]` maybe first university year calculus.
`[00:20:03]` maybe first university year calculus.
`[00:20:03]` And um
`[00:20:05]` And um
`[00:20:05]` you can now compute in parallel which
`[00:20:07]` you can now compute in parallel which
`[00:20:07]` direction you should change each weight
`[00:20:09]` direction you should change each weight
`[00:20:09]` in.
`[00:20:10]` in.
`[00:20:10]` And then very surprisingly, you don't
`[00:20:11]` And then very surprisingly, you don't
`[00:20:11]` have to do that for the whole training
`[00:20:12]` have to do that for the whole training
`[00:20:12]` set. You just take a small batch of
`[00:20:14]` set. You just take a small batch of
`[00:20:14]` examples,
`[00:20:15]` examples,
`[00:20:15]` and on that batch of examples, you
`[00:20:17]` and on that batch of examples, you
`[00:20:17]` compute how to change the connection
`[00:20:18]` compute how to change the connection
`[00:20:18]` strengths.
`[00:20:19]` strengths.
`[00:20:19]` And you might have got it wrong because
`[00:20:21]` And you might have got it wrong because
`[00:20:21]` of the quirks of that batch of examples,
`[00:20:23]` of the quirks of that batch of examples,
`[00:20:23]` but you change them anyway, and then you
`[00:20:24]` but you change them anyway, and then you
`[00:20:24]` take another batch of examples. This is
`[00:20:26]` take another batch of examples. This is
`[00:20:26]` called stochastic gradient descent.
`[00:20:28]` called stochastic gradient descent.
`[00:20:28]` And I guess the major discovery of
`[00:20:31]` And I guess the major discovery of
`[00:20:31]` of the neural net community is that
`[00:20:33]` of the neural net community is that
`[00:20:33]` stochastic gradient descent, even though
`[00:20:36]` stochastic gradient descent, even though
`[00:20:36]` it has no real right to work, actually
`[00:20:38]` it has no real right to work, actually
`[00:20:38]` works really well.
`[00:20:40]` works really well.
`[00:20:40]` And but it works really well at scale.
`[00:20:42]` And but it works really well at scale.
`[00:20:42]` If you give it lots of data and big
`[00:20:43]` If you give it lots of data and big
`[00:20:43]` nets, it really shows
`[00:20:45]` nets, it really shows
`[00:20:45]` shows its colors.
`[00:20:50]` However,
`[00:20:51]` um
`[00:20:54]` in the 1980s, we were very very pleased
`[00:20:56]` by back propagation. It seemed to have
`[00:20:58]` by back propagation. It seemed to have
`[00:20:58]` solved the problem, and we were
`[00:20:59]` solved the problem, and we were
`[00:20:59]` convinced it was going to um solve
`[00:21:01]` convinced it was going to um solve
`[00:21:01]` everything.
`[00:21:02]` everything.
`[00:21:02]` And
`[00:21:04]` And
`[00:21:04]` it did actually do quite well at speech
`[00:21:06]` it did actually do quite well at speech
`[00:21:06]` recognition and some forms of object
`[00:21:07]` recognition and some forms of object
`[00:21:07]` recognition, but it was basically a
`[00:21:09]` recognition, but it was basically a
`[00:21:09]` disappointment. It didn't work nearly as
`[00:21:10]` disappointment. It didn't work nearly as
`[00:21:10]` well as we thought.
`[00:21:12]` well as we thought.
`[00:21:12]` And the real issue was why. And at the
`[00:21:14]` And the real issue was why. And at the
`[00:21:14]` time, people had all sorts of analyses
`[00:21:16]` time, people had all sorts of analyses
`[00:21:16]` of why it didn't work, most of which
`[00:21:18]` of why it didn't work, most of which
`[00:21:18]` were wrong.
`[00:21:19]` were wrong.
`[00:21:20]` So, they said, "It's getting trapped in
`[00:21:21]` So, they said, "It's getting trapped in
`[00:21:21]` local optima." We now know that wasn't
`[00:21:23]` local optima." We now know that wasn't
`[00:21:23]` the problem.
`[00:21:24]` the problem.
`[00:21:24]` Um
`[00:21:26]` Um
`[00:21:26]` when other learning algorithms worked
`[00:21:29]` when other learning algorithms worked
`[00:21:29]` better than back propagation on
`[00:21:30]` better than back propagation on
`[00:21:30]` moderate-sized data sets,
`[00:21:32]` moderate-sized data sets,
`[00:21:32]` um most people in the machine learning
`[00:21:34]` um most people in the machine learning
`[00:21:34]` community adopted the view that
`[00:21:37]` community adopted the view that
`[00:21:37]` "What you guys are trying to do is learn
`[00:21:39]` "What you guys are trying to do is learn
`[00:21:39]` these deep multi-layer networks from
`[00:21:42]` these deep multi-layer networks from
`[00:21:42]` random weights just using stochastic
`[00:21:45]` random weights just using stochastic
`[00:21:45]` gradient descent, and this is crazy.
`[00:21:48]` gradient descent, and this is crazy.
`[00:21:48]` Um it's never going to work. You're just
`[00:21:49]` Um it's never going to work. You're just
`[00:21:49]` asking for too much.
`[00:21:52]` asking for too much.
`[00:21:52]` There's no way you're going to get
`[00:21:53]` There's no way you're going to get
`[00:21:53]` systems like this to work unless you put
`[00:21:54]` systems like this to work unless you put
`[00:21:54]` in quite a lot of hand engineering.
`[00:21:57]` in quite a lot of hand engineering.
`[00:21:57]` Um you somehow wire in some prior
`[00:21:58]` Um you somehow wire in some prior
`[00:21:58]` knowledge.
`[00:22:00]` knowledge.
`[00:22:00]` So, linguists, for example, had been
`[00:22:02]` So, linguists, for example, had been
`[00:22:02]` indoctrinated to believe that a lot of
`[00:22:04]` indoctrinated to believe that a lot of
`[00:22:04]` language is innate, and you'd never
`[00:22:06]` language is innate, and you'd never
`[00:22:06]` learn language without prior knowledge.
`[00:22:08]` learn language without prior knowledge.
`[00:22:08]` In fact, they had mathematical theorems
`[00:22:10]` In fact, they had mathematical theorems
`[00:22:10]` that proved you couldn't learn language
`[00:22:11]` that proved you couldn't learn language
`[00:22:11]` without prior knowledge. Um
`[00:22:14]` without prior knowledge. Um
`[00:22:14]` my response to that is beware of
`[00:22:17]` my response to that is beware of
`[00:22:17]` mathematicians bearing theorems.
`[00:22:23]` So, I just want to give you some really
`[00:22:25]` silly theories. I
`[00:22:27]` silly theories. I
`[00:22:27]` I'm a Monty Python fan. So, here's some
`[00:22:29]` I'm a Monty Python fan. So, here's some
`[00:22:29]` really silly theories.
`[00:22:30]` really silly theories.
`[00:22:30]` Um the continents used to be connected
`[00:22:32]` Um the continents used to be connected
`[00:22:32]` and then drifted apart. And you can
`[00:22:34]` and then drifted apart. And you can
`[00:22:34]` imagine how silly geologists thought
`[00:22:36]` imagine how silly geologists thought
`[00:22:36]` that theory was.
`[00:22:38]` that theory was.
`[00:22:38]` Um great big neural nets that start with
`[00:22:40]` Um great big neural nets that start with
`[00:22:40]` random weights and no prior knowledge
`[00:22:41]` random weights and no prior knowledge
`[00:22:41]` can learn to machine translation.
`[00:22:43]` can learn to machine translation.
`[00:22:43]` That seemed like a very very silly
`[00:22:45]` That seemed like a very very silly
`[00:22:45]` theory to many people.
`[00:22:47]` theory to many people.
`[00:22:47]` Um just write one more. If you take a
`[00:22:49]` Um just write one more. If you take a
`[00:22:49]` natural remedy and you keep diluting it,
`[00:22:51]` natural remedy and you keep diluting it,
`[00:22:51]` the more you dilute it, the more potent
`[00:22:53]` the more you dilute it, the more potent
`[00:22:53]` it gets.
`[00:22:55]` it gets.
`[00:22:55]` And some people believe that, too. Um
`[00:23:02]` So, the quote at the top was taken
`[00:23:04]` actually from the continental drift
`[00:23:05]` actually from the continental drift
`[00:23:05]` literature.
`[00:23:07]` literature.
`[00:23:07]` Um Wegener, who suggested in 1912,
`[00:23:10]` Um Wegener, who suggested in 1912,
`[00:23:10]` was kind of laughed out of town, even
`[00:23:12]` was kind of laughed out of town, even
`[00:23:12]` though he actually had very good
`[00:23:13]` though he actually had very good
`[00:23:13]` arguments. Um he didn't have a good
`[00:23:15]` arguments. Um he didn't have a good
`[00:23:15]` mechanism.
`[00:23:16]` mechanism.
`[00:23:16]` And the geological community said, you
`[00:23:18]` And the geological community said, you
`[00:23:18]` know, "We've got to keep this stuff out
`[00:23:20]` know, "We've got to keep this stuff out
`[00:23:20]` of the textbooks and out of the
`[00:23:21]` of the textbooks and out of the
`[00:23:21]` journals. It's just going to confuse
`[00:23:23]` journals. It's just going to confuse
`[00:23:23]` people."
`[00:23:24]` people."
`[00:23:24]` Um we had our own little experience of
`[00:23:26]` Um we had our own little experience of
`[00:23:26]` that in the second neural net winter.
`[00:23:29]` that in the second neural net winter.
`[00:23:29]` Um
`[00:23:30]` Um
`[00:23:30]` So, NIPS, of all conferences,
`[00:23:33]` So, NIPS, of all conferences,
`[00:23:33]` um
`[00:23:34]` um
`[00:23:34]` declined to take a paper of mine. Um
`[00:23:38]` declined to take a paper of mine. Um
`[00:23:38]` You don't forget those things.
`[00:23:40]` You don't forget those things.
`[00:23:40]` And
`[00:23:45]` And um
`[00:23:46]` like many other disappointed authors, I
`[00:23:48]` like many other disappointed authors, I
`[00:23:48]` had a word with a friend on the program
`[00:23:51]` had a word with a friend on the program
`[00:23:51]` And my friend on the program committee
`[00:23:53]` And my friend on the program committee
`[00:23:53]` told me, "Well, you see, they couldn't
`[00:23:54]` told me, "Well, you see, they couldn't
`[00:23:54]` accept this because they had two papers
`[00:23:56]` accept this because they had two papers
`[00:23:56]` on deep learning, and they had to decide
`[00:23:57]` on deep learning, and they had to decide
`[00:23:57]` which one to accept. And they had
`[00:23:59]` which one to accept. And they had
`[00:23:59]` actually accepted the other one. So,
`[00:24:01]` actually accepted the other one. So,
`[00:24:01]` they couldn't reasonably be expected to
`[00:24:02]` they couldn't reasonably be expected to
`[00:24:02]` have two papers on the same thing in the
`[00:24:03]` have two papers on the same thing in the
`[00:24:03]` same conference."
`[00:24:05]` same conference."
`[00:24:05]` Um I suggest you go to NIPS now and see
`[00:24:07]` Um I suggest you go to NIPS now and see
`[00:24:07]` whether
`[00:24:08]` whether
`[00:24:09]` Um
`[00:24:11]` Um
`[00:24:11]` Yoshua Bengio submitted a paper to ICML
`[00:24:14]` Yoshua Bengio submitted a paper to ICML
`[00:24:14]` in about 2009. I'm not certain of the
`[00:24:16]` in about 2009. I'm not certain of the
`[00:24:16]` year, but it's around then. Um And one
`[00:24:19]` year, but it's around then. Um And one
`[00:24:19]` of the reviewers said that neural
`[00:24:21]` of the reviewers said that neural
`[00:24:21]` network papers had no place in a machine
`[00:24:23]` network papers had no place in a machine
`[00:24:23]` learning conference.
`[00:24:24]` learning conference.
`[00:24:25]` So, I suggest you go to ICML. Um
`[00:24:28]` So, I suggest you go to ICML. Um
`[00:24:28]` CVPR, which is the leading computer
`[00:24:30]` CVPR, which is the leading computer
`[00:24:30]` vision conference,
`[00:24:31]` vision conference,
`[00:24:31]` that was the most outrageous of all, I
`[00:24:33]` that was the most outrageous of all, I
`[00:24:33]` think. Um Yann and his co-workers
`[00:24:36]` think. Um Yann and his co-workers
`[00:24:36]` submitted a paper doing semantic
`[00:24:38]` submitted a paper doing semantic
`[00:24:38]` segmentation that beat the state of the
`[00:24:40]` segmentation that beat the state of the
`[00:24:40]` art.
`[00:24:41]` art.
`[00:24:41]` It it beat what the mainline computer
`[00:24:43]` It it beat what the mainline computer
`[00:24:43]` vision people could do.
`[00:24:45]` vision people could do.
`[00:24:45]` Um it got rejected. And one of the
`[00:24:47]` Um it got rejected. And one of the
`[00:24:47]` reviewers said, um "This paper tells us
`[00:24:51]` reviewers said, um "This paper tells us
`[00:24:51]` nothing about computer vision because
`[00:24:53]` nothing about computer vision because
`[00:24:53]` everything's learned."
`[00:24:55]` everything's learned."
`[00:24:55]` So, the reviewer, like the field of
`[00:24:57]` So, the reviewer, like the field of
`[00:24:58]` computer vision at the time, was stuck
`[00:24:59]` computer vision at the time, was stuck
`[00:24:59]` in the frame of mind that
`[00:25:01]` in the frame of mind that
`[00:25:01]` the way you do computer vision is you
`[00:25:03]` the way you do computer vision is you
`[00:25:03]` think about the nature of the task of
`[00:25:05]` think about the nature of the task of
`[00:25:05]` vision,
`[00:25:06]` vision,
`[00:25:06]` you preferably write down some
`[00:25:07]` you preferably write down some
`[00:25:07]` equations, you think about how to do the
`[00:25:10]` equations, you think about how to do the
`[00:25:10]` computations that are required to do
`[00:25:11]` computations that are required to do
`[00:25:11]` vision, then you get some implementation
`[00:25:13]` vision, then you get some implementation
`[00:25:13]` of it, and then you see whether it
`[00:25:14]` of it, and then you see whether it
`[00:25:14]` works.
`[00:25:15]` works.
`[00:25:15]` Um
`[00:25:17]` Um
`[00:25:17]` The idea that you just learn everything
`[00:25:20]` The idea that you just learn everything
`[00:25:20]` was outside the realm of things that
`[00:25:22]` was outside the realm of things that
`[00:25:22]` were worth considering.
`[00:25:24]` were worth considering.
`[00:25:24]` And
`[00:25:26]` And
`[00:25:26]` so, the reviewer basically missed the
`[00:25:28]` so, the reviewer basically missed the
`[00:25:28]` point, which was that everything was
`[00:25:30]` point, which was that everything was
`[00:25:30]` learned.
`[00:25:31]` learned.
`[00:25:31]` Um he completely failed to see how that
`[00:25:33]` Um he completely failed to see how that
`[00:25:33]` completely changed computer vision.
`[00:25:35]` completely changed computer vision.
`[00:25:35]` Now, I shouldn't be too hard on those
`[00:25:36]` Now, I shouldn't be too hard on those
`[00:25:36]` guys cuz a little later on, they were
`[00:25:39]` guys cuz a little later on, they were
`[00:25:39]` very reasonable. With a bit more
`[00:25:40]` very reasonable. With a bit more
`[00:25:40]` evidence, they suddenly flipped.
`[00:25:44]` So, between 2005
`[00:25:46]` and 2009,
`[00:25:48]` and 2009,
`[00:25:48]` researchers, some of them in Canada,
`[00:25:51]` researchers, some of them in Canada,
`[00:25:51]` we make Yann an honorary Canadian cuz
`[00:25:53]` we make Yann an honorary Canadian cuz
`[00:25:53]` he's French. Um
`[00:25:55]` he's French. Um
`[00:25:55]` made several technical advances that
`[00:25:58]` made several technical advances that
`[00:25:58]` allowed back propagation to work better
`[00:26:00]` allowed back propagation to work better
`[00:26:00]` in feedforward nets.
`[00:26:02]` in feedforward nets.
`[00:26:02]` Um they involved using unsupervised
`[00:26:04]` Um they involved using unsupervised
`[00:26:04]` pre-training to initialize the weights
`[00:26:06]` pre-training to initialize the weights
`[00:26:06]` before you turn on back propagation.
`[00:26:08]` before you turn on back propagation.
`[00:26:08]` Things like dropping out units at random
`[00:26:10]` Things like dropping out units at random
`[00:26:10]` to make the whole thing much more
`[00:26:11]` to make the whole thing much more
`[00:26:11]` robust.
`[00:26:13]` robust.
`[00:26:13]` And introducing rectified linear units,
`[00:26:15]` And introducing rectified linear units,
`[00:26:15]` which turned out to be easier to train.
`[00:26:17]` which turned out to be easier to train.
`[00:26:17]` Um
`[00:26:19]` Um
`[00:26:19]` For us, the details of those advances
`[00:26:21]` For us, the details of those advances
`[00:26:21]` are our bread and butter. We're very
`[00:26:22]` are our bread and butter. We're very
`[00:26:22]` interested in those. But the main
`[00:26:24]` interested in those. But the main
`[00:26:24]` message is that with a few technical
`[00:26:27]` message is that with a few technical
`[00:26:27]` advances, back propagation works
`[00:26:29]` advances, back propagation works
`[00:26:29]` amazingly well, and the main reason is
`[00:26:31]` amazingly well, and the main reason is
`[00:26:31]` cuz we now have lots of labeled data and
`[00:26:34]` cuz we now have lots of labeled data and
`[00:26:34]` a lot of convenient compute power.
`[00:26:37]` a lot of convenient compute power.
`[00:26:37]` Inconvenient compute power isn't much
`[00:26:38]` Inconvenient compute power isn't much
`[00:26:38]` use. Um
`[00:26:40]` use. Um
`[00:26:40]` but things like GPUs and more recently
`[00:26:42]` but things like GPUs and more recently
`[00:26:42]` TPUs, um allow you to apply a lot of
`[00:26:45]` TPUs, um allow you to apply a lot of
`[00:26:45]` computation,
`[00:26:47]` computation,
`[00:26:47]` and they made a huge difference. So,
`[00:26:49]` and they made a huge difference. So,
`[00:26:49]` really the deciding factor, I think, was
`[00:26:52]` really the deciding factor, I think, was
`[00:26:52]` the increase in compute power.
`[00:26:54]` the increase in compute power.
`[00:26:54]` So, I think a lot of the credit for deep
`[00:26:56]` So, I think a lot of the credit for deep
`[00:26:56]` learning really goes to the people who
`[00:26:59]` learning really goes to the people who
`[00:26:59]` collected the big databases like Fei-Fei
`[00:27:01]` collected the big databases like Fei-Fei
`[00:27:01]` Li,
`[00:27:02]` Li,
`[00:27:02]` and the people who made the computers go
`[00:27:04]` and the people who made the computers go
`[00:27:04]` fast,
`[00:27:05]` fast,
`[00:27:05]` like um David Patterson and others.
`[00:27:08]` like um David Patterson and others.
`[00:27:08]` Lots of others.
`[00:27:11]` So, the killer app from my point of view
`[00:27:13]` was in 2009,
`[00:27:15]` was in 2009,
`[00:27:15]` when in my lab we got a bunch of GPUs
`[00:27:18]` when in my lab we got a bunch of GPUs
`[00:27:18]` and two graduate students
`[00:27:20]` and two graduate students
`[00:27:20]` um
`[00:27:21]` um
`[00:27:21]` made them
`[00:27:23]` made them
`[00:27:23]` do
`[00:27:24]` do
`[00:27:24]` learn to do um
`[00:27:27]` learn to do um
`[00:27:27]` acoustic modeling. Acoustic modeling
`[00:27:29]` acoustic modeling. Acoustic modeling
`[00:27:29]` means you take something like a
`[00:27:30]` means you take something like a
`[00:27:30]` spectrogram,
`[00:27:31]` spectrogram,
`[00:27:31]` and you try and figure out for the
`[00:27:32]` and you try and figure out for the
`[00:27:32]` middle frame of the spectrogram which
`[00:27:35]` middle frame of the spectrogram which
`[00:27:35]` piece of which phoneme the speaker is
`[00:27:36]` piece of which phoneme the speaker is
`[00:27:37]` trying to express.
`[00:27:38]` trying to express.
`[00:27:38]` And in this little database we used,
`[00:27:40]` And in this little database we used,
`[00:27:40]` relatively little, um there are 183
`[00:27:42]` relatively little, um there are 183
`[00:27:43]` labels for what which piece of which
`[00:27:44]` labels for what which piece of which
`[00:27:44]` pho- phoneme it might be.
`[00:27:47]` pho- phoneme it might be.
`[00:27:47]` And so, you pre-train a net
`[00:27:49]` And so, you pre-train a net
`[00:27:49]` with many layers of 2,000 hidden units.
`[00:27:52]` with many layers of 2,000 hidden units.
`[00:27:52]` Um you can't pre-train the last layer
`[00:27:54]` Um you can't pre-train the last layer
`[00:27:54]` cuz you don't know the labels yet. And
`[00:27:56]` cuz you don't know the labels yet. And
`[00:27:56]` you're training it just to be able to
`[00:27:57]` you're training it just to be able to
`[00:27:57]` reproduce what's in the layer below.
`[00:28:00]` reproduce what's in the layer below.
`[00:28:00]` And then you turn on learning in all the
`[00:28:02]` And then you turn on learning in all the
`[00:28:02]` layers, and it does slightly better than
`[00:28:05]` layers, and it does slightly better than
`[00:28:05]` the state of the art, which had taken 30
`[00:28:06]` the state of the art, which had taken 30
`[00:28:06]` years to develop.
`[00:28:09]` years to develop.
`[00:28:09]` When people in speech saw that, the
`[00:28:11]` When people in speech saw that, the
`[00:28:11]` smart people, they realized that with
`[00:28:12]` smart people, they realized that with
`[00:28:12]` more development, this stuff was going
`[00:28:13]` more development, this stuff was going
`[00:28:13]` to be amazing.
`[00:28:16]` to be amazing.
`[00:28:16]` And
`[00:28:18]` And
`[00:28:18]` my graduate students went off to various
`[00:28:20]` my graduate students went off to various
`[00:28:20]` groups like MSR and IBM and Google. In
`[00:28:23]` groups like MSR and IBM and Google. In
`[00:28:23]` particular, Navdeep Jaitly went to
`[00:28:25]` particular, Navdeep Jaitly went to
`[00:28:25]` Google,
`[00:28:27]` Google,
`[00:28:27]` and
`[00:28:30]` ported the system for acoustic
`[00:28:33]` modeling that was developed in Toronto
`[00:28:35]` modeling that was developed in Toronto
`[00:28:35]` fairly literally,
`[00:28:37]` fairly literally,
`[00:28:37]` and it came out in the Android in 2012.
`[00:28:40]` and it came out in the Android in 2012.
`[00:28:41]` There was a lot of good engineering to
`[00:28:42]` There was a lot of good engineering to
`[00:28:42]` make it run in real time,
`[00:28:44]` make it run in real time,
`[00:28:45]` and it gave a big decrease in error
`[00:28:46]` and it gave a big decrease in error
`[00:28:46]` rates. And at more or less the same
`[00:28:48]` rates. And at more or less the same
`[00:28:48]` time, all the other groups started
`[00:28:49]` time, all the other groups started
`[00:28:49]` changing the way they did speech
`[00:28:50]` changing the way they did speech
`[00:28:50]` recognition. And now all the good speech
`[00:28:53]` recognition. And now all the good speech
`[00:28:53]` recognizers use neural nets. They're not
`[00:28:56]` recognizers use neural nets. They're not
`[00:28:56]` like the neural nets we introduced
`[00:28:57]` like the neural nets we introduced
`[00:28:57]` initially. Neural nets have gradually
`[00:29:00]` initially. Neural nets have gradually
`[00:29:00]` eroded more and more parts of the
`[00:29:02]` eroded more and more parts of the
`[00:29:02]` system. Sort of putting a neural net in
`[00:29:04]` system. Sort of putting a neural net in
`[00:29:04]` your system is a bit like getting
`[00:29:05]` your system is a bit like getting
`[00:29:05]` gangrene. It'll gradually eat the whole
`[00:29:07]` gangrene. It'll gradually eat the whole
`[00:29:07]` system.
`[00:29:11]` Then in 2012,
`[00:29:13]` um two other of my graduate students
`[00:29:16]` um two other of my graduate students
`[00:29:16]` applied neural nets of the kind
`[00:29:18]` applied neural nets of the kind
`[00:29:18]` developed over many years by Yann LeCun
`[00:29:21]` developed over many years by Yann LeCun
`[00:29:21]` to object recognition on a big database
`[00:29:23]` to object recognition on a big database
`[00:29:23]` that Fei-Fei Li had put together
`[00:29:25]` that Fei-Fei Li had put together
`[00:29:25]` with a thousand different classes of
`[00:29:26]` with a thousand different classes of
`[00:29:26]` object. And it was finally a big enough
`[00:29:29]` object. And it was finally a big enough
`[00:29:29]` database of real images so you could
`[00:29:30]` database of real images so you could
`[00:29:30]` show what neural nets could do, and they
`[00:29:33]` show what neural nets could do, and they
`[00:29:33]` could do a lot.
`[00:29:34]` could do a lot.
`[00:29:34]` So, if you looked at the results,
`[00:29:36]` So, if you looked at the results,
`[00:29:36]` um all the computer vision systems, the
`[00:29:39]` um all the computer vision systems, the
`[00:29:39]` standard ones, had
`[00:29:40]` standard ones, had
`[00:29:40]` asymptoted at about 25% error.
`[00:29:43]` asymptoted at about 25% error.
`[00:29:43]` Um our system, developed by two graduate
`[00:29:45]` Um our system, developed by two graduate
`[00:29:46]` students, um
`[00:29:48]` students, um
`[00:29:48]` got 16% error. And then further work on
`[00:29:51]` got 16% error. And then further work on
`[00:29:51]` neural nets like that, by 2015 it was
`[00:29:53]` neural nets like that, by 2015 it was
`[00:29:53]` down to 5% and now it's down to
`[00:29:55]` down to 5% and now it's down to
`[00:29:55]` considerably below that.
`[00:29:58]` considerably below that.
`[00:29:58]` So then what happened was exactly what
`[00:30:00]` So then what happened was exactly what
`[00:30:00]` ought to happen in science.
`[00:30:02]` ought to happen in science.
`[00:30:02]` Um
`[00:30:03]` Um
`[00:30:03]` leaders of the computer vision community
`[00:30:05]` leaders of the computer vision community
`[00:30:05]` looked at this result and they said,
`[00:30:07]` looked at this result and they said,
`[00:30:07]` "Oh,
`[00:30:08]` "Oh,
`[00:30:08]` they really do work. We were wrong.
`[00:30:09]` they really do work. We were wrong.
`[00:30:09]` Okay, we're going to switch." And within
`[00:30:11]` Okay, we're going to switch." And within
`[00:30:11]` a year they all switched.
`[00:30:13]` a year they all switched.
`[00:30:13]` And so science finally worked like it
`[00:30:14]` And so science finally worked like it
`[00:30:14]` was meant to.
`[00:30:18]` The last thing I want to talk about is
`[00:30:20]` ironically new age to machine
`[00:30:21]` ironically new age to machine
`[00:30:21]` translation, which was introduced in
`[00:30:23]` translation, which was introduced in
`[00:30:23]` 2014 by people at Google and also in
`[00:30:26]` 2014 by people at Google and also in
`[00:30:26]` Montreal by people in Yoshua Bengio's
`[00:30:28]` Montreal by people in Yoshua Bengio's
`[00:30:28]` lab.
`[00:30:30]` lab.
`[00:30:30]` And the idea in 2014 was for each
`[00:30:32]` And the idea in 2014 was for each
`[00:30:32]` language we're going to have a neural
`[00:30:33]` language we're going to have a neural
`[00:30:33]` network. It'll be a recurrent network
`[00:30:35]` network. It'll be a recurrent network
`[00:30:35]` that is going to encode
`[00:30:38]` that is going to encode
`[00:30:38]` the string of words in that language,
`[00:30:40]` the string of words in that language,
`[00:30:40]` which it receives one at a time, into a
`[00:30:42]` which it receives one at a time, into a
`[00:30:42]` big vector.
`[00:30:43]` big vector.
`[00:30:43]` I call that big vector a thought vector.
`[00:30:45]` I call that big vector a thought vector.
`[00:30:45]` The idea is that big vector captures the
`[00:30:47]` The idea is that big vector captures the
`[00:30:47]` meaning of that string of words.
`[00:30:50]` meaning of that string of words.
`[00:30:50]` Then you take that big vector and you
`[00:30:51]` Then you take that big vector and you
`[00:30:51]` give it to a decoder network. And the
`[00:30:53]` give it to a decoder network. And the
`[00:30:53]` decoder network turns the big vector
`[00:30:55]` decoder network turns the big vector
`[00:30:55]` into a string of words in another
`[00:30:57]` into a string of words in another
`[00:30:57]` language.
`[00:30:58]` language.
`[00:30:58]` And it sort of worked.
`[00:31:00]` And it sort of worked.
`[00:31:00]` And with a bit of development it worked
`[00:31:01]` And with a bit of development it worked
`[00:31:01]` very well.
`[00:31:06]` Since 2014,
`[00:31:08]` one of the major pieces of development
`[00:31:09]` one of the major pieces of development
`[00:31:09]` has been that when you're decoding the
`[00:31:13]` has been that when you're decoding the
`[00:31:13]` meaning of a sentence, what you do is
`[00:31:14]` meaning of a sentence, what you do is
`[00:31:14]` you look back at the sentence you were
`[00:31:16]` you look back at the sentence you were
`[00:31:16]` encoding
`[00:31:17]` encoding
`[00:31:17]` and that's called soft attention. So
`[00:31:19]` and that's called soft attention. So
`[00:31:19]` each time you produce a new word, you're
`[00:31:20]` each time you produce a new word, you're
`[00:31:20]` deciding where to look in the sentence
`[00:31:23]` deciding where to look in the sentence
`[00:31:23]` that you're translating.
`[00:31:25]` that you're translating.
`[00:31:25]` Um that helps a lot.
`[00:31:27]` Um that helps a lot.
`[00:31:27]` You also now pre-train the word
`[00:31:29]` You also now pre-train the word
`[00:31:29]` embeddings and that helps a lot.
`[00:31:32]` embeddings and that helps a lot.
`[00:31:32]` And the way the pre-training works is
`[00:31:34]` And the way the pre-training works is
`[00:31:34]` you take a bunch of words
`[00:31:36]` you take a bunch of words
`[00:31:36]` and you try and reproduce these words in
`[00:31:40]` and you try and reproduce these words in
`[00:31:40]` a deep net, but you've left out some of
`[00:31:42]` a deep net, but you've left out some of
`[00:31:42]` the words. So from these words you have
`[00:31:44]` the words. So from these words you have
`[00:31:44]` to reproduce the same words, but you
`[00:31:46]` to reproduce the same words, but you
`[00:31:46]` have to fill in the blanks essentially.
`[00:31:49]` have to fill in the blanks essentially.
`[00:31:49]` Um they use things called transformers
`[00:31:52]` Um they use things called transformers
`[00:31:52]` where in this deep net, as you as each
`[00:31:55]` where in this deep net, as you as each
`[00:31:55]` word goes through the net, um it's
`[00:31:58]` word goes through the net, um it's
`[00:31:58]` looking at kind of nearby words to
`[00:32:00]` looking at kind of nearby words to
`[00:32:00]` disambiguate what it might mean. So if
`[00:32:02]` disambiguate what it might mean. So if
`[00:32:02]` you have a word like may, when it goes
`[00:32:04]` you have a word like may, when it goes
`[00:32:04]` in, you'll get an initial vector that's
`[00:32:06]` in, you'll get an initial vector that's
`[00:32:06]` sort of ambiguous between the modal and
`[00:32:08]` sort of ambiguous between the modal and
`[00:32:08]` the month.
`[00:32:09]` the month.
`[00:32:09]` But if it sees the 13th next to it, it
`[00:32:12]` But if it sees the 13th next to it, it
`[00:32:12]` knows pretty well it's the month. And so
`[00:32:15]` knows pretty well it's the month. And so
`[00:32:15]` in the next day it can disambiguate that
`[00:32:17]` in the next day it can disambiguate that
`[00:32:17]` and the meaning of that may will be the
`[00:32:18]` and the meaning of that may will be the
`[00:32:18]` month.
`[00:32:19]` month.
`[00:32:19]` Um
`[00:32:20]` Um
`[00:32:20]` and those transformer nets now work
`[00:32:22]` and those transformer nets now work
`[00:32:22]` really well for getting word embeddings.
`[00:32:25]` really well for getting word embeddings.
`[00:32:25]` They also, it turns out, learn a whole
`[00:32:27]` They also, it turns out, learn a whole
`[00:32:27]` lot of grammar. So all the stuff that
`[00:32:29]` lot of grammar. So all the stuff that
`[00:32:29]` linguists thought had to be put in
`[00:32:30]` linguists thought had to be put in
`[00:32:30]` innately, these neural nets are now
`[00:32:32]` innately, these neural nets are now
`[00:32:32]` getting in there. They're getting lots
`[00:32:33]` getting in there. They're getting lots
`[00:32:33]` of syntactic understanding.
`[00:32:35]` of syntactic understanding.
`[00:32:35]` But it's all being learned from data. If
`[00:32:38]` But it's all being learned from data. If
`[00:32:38]` you look in the early layers of
`[00:32:39]` you look in the early layers of
`[00:32:39]` transformer nets, they know what parts
`[00:32:41]` transformer nets, they know what parts
`[00:32:41]` of speech things are.
`[00:32:42]` of speech things are.
`[00:32:43]` Um if you look in later parts of the
`[00:32:44]` Um if you look in later parts of the
`[00:32:44]` nets, they know how to disambiguate
`[00:32:46]` nets, they know how to disambiguate
`[00:32:46]` pronoun references.
`[00:32:47]` pronoun references.
`[00:32:47]` Um basically,
`[00:32:49]` Um basically,
`[00:32:49]` they're learning grammar the way a
`[00:32:51]` they're learning grammar the way a
`[00:32:51]` little kid learns grammar, just by just
`[00:32:53]` little kid learns grammar, just by just
`[00:32:53]` from looking at
`[00:32:55]` from looking at
`[00:32:55]` sentences.
`[00:32:56]` sentences.
`[00:32:56]` Um
`[00:32:58]` Um
`[00:32:58]` So I think that the machine translation
`[00:33:01]` So I think that the machine translation
`[00:33:01]` was really the final nail in the coffin
`[00:33:03]` was really the final nail in the coffin
`[00:33:03]` of symbolic AI.
`[00:33:06]` of symbolic AI.
`[00:33:06]` Cuz machine translation is the ideal
`[00:33:08]` Cuz machine translation is the ideal
`[00:33:08]` task for symbolic AI. It's symbols in
`[00:33:11]` task for symbolic AI. It's symbols in
`[00:33:11]` and it's symbols out.
`[00:33:13]` and it's symbols out.
`[00:33:13]` But it turns out if you want to do it
`[00:33:14]` But it turns out if you want to do it
`[00:33:15]` well, inside what you need is big
`[00:33:17]` well, inside what you need is big
`[00:33:17]` vectors.
`[00:33:22]` Okay, I have um
`[00:33:25]` said everything I wanted to say about
`[00:33:27]` said everything I wanted to say about
`[00:33:27]` the history up to 2014 or so of neural
`[00:33:31]` the history up to 2014 or so of neural
`[00:33:31]` nets. Um I've emphasized the ideology
`[00:33:35]` nets. Um I've emphasized the ideology
`[00:33:35]` that there were these two camps
`[00:33:37]` that there were these two camps
`[00:33:37]` and that the good guys won.
`[00:33:39]` and that the good guys won.
`[00:33:39]` Um
`[00:33:42]` It's not over yet because of course what
`[00:33:45]` we need is for neural nets now
`[00:33:48]` we need is for neural nets now
`[00:33:48]` to begin to be able to explain
`[00:33:50]` to begin to be able to explain
`[00:33:50]` reasoning.
`[00:33:51]` reasoning.
`[00:33:51]` We can't do that yet. We're working on
`[00:33:53]` We can't do that yet. We're working on
`[00:33:53]` it. But reasoning is the last thing that
`[00:33:55]` it. But reasoning is the last thing that
`[00:33:55]` people do, not the first thing.
`[00:33:57]` people do, not the first thing.
`[00:33:57]` And reasoning is built on top of all
`[00:33:59]` And reasoning is built on top of all
`[00:33:59]` this other stuff. And my view's always
`[00:34:01]` this other stuff. And my view's always
`[00:34:01]` been you're never going to understand
`[00:34:02]` been you're never going to understand
`[00:34:02]` reasoning until you understand all this
`[00:34:04]` reasoning until you understand all this
`[00:34:04]` other stuff. And now we are beginning to
`[00:34:06]` other stuff. And now we are beginning to
`[00:34:06]` understand all this other stuff and
`[00:34:07]` understand all this other stuff and
`[00:34:07]` we're more or less ready to begin to
`[00:34:09]` we're more or less ready to begin to
`[00:34:09]` understand reasoning.
`[00:34:10]` understand reasoning.
`[00:34:10]` But reasoning just with sort of bare
`[00:34:12]` But reasoning just with sort of bare
`[00:34:12]` symbols, by using rules that are
`[00:34:14]` symbols, by using rules that are
`[00:34:14]` expressed as other symbols,
`[00:34:16]` expressed as other symbols,
`[00:34:16]` that seemed to me just hopeless. You're
`[00:34:18]` that seemed to me just hopeless. You're
`[00:34:18]` missing all the content. There's no
`[00:34:20]` missing all the content. There's no
`[00:34:20]` meaning there.
`[00:34:23]` Okay.
`[00:34:24]` I want to talk a little bit about the
`[00:34:25]` I want to talk a little bit about the
`[00:34:25]` future of computer vision.
`[00:34:28]` future of computer vision.
`[00:34:28]` So convolutional neural nets have been
`[00:34:29]` So convolutional neural nets have been
`[00:34:30]` very effective.
`[00:34:31]` very effective.
`[00:34:31]` And what convolutional neural nets do is
`[00:34:33]` And what convolutional neural nets do is
`[00:34:33]` they wire in
`[00:34:34]` they wire in
`[00:34:34]` the idea that if a feature is useful in
`[00:34:36]` the idea that if a feature is useful in
`[00:34:36]` one place, it's also going to be useful
`[00:34:38]` one place, it's also going to be useful
`[00:34:38]` in another place.
`[00:34:39]` in another place.
`[00:34:39]` And that allows us to accum- to combine
`[00:34:41]` And that allows us to accum- to combine
`[00:34:41]` evidence from different locations to
`[00:34:43]` evidence from different locations to
`[00:34:43]` learn a shared feature detector.
`[00:34:46]` learn a shared feature detector.
`[00:34:46]` That is to learn replicated feature
`[00:34:47]` That is to learn replicated feature
`[00:34:47]` detectors that are the same in all these
`[00:34:49]` detectors that are the same in all these
`[00:34:49]` places.
`[00:34:50]` places.
`[00:34:50]` And that's a huge win. It makes it much
`[00:34:52]` And that's a huge win. It makes it much
`[00:34:52]` more data efficient. And those things
`[00:34:54]` more data efficient. And those things
`[00:34:54]` Yang got working in the 1990s. They were
`[00:34:58]` Yang got working in the 1990s. They were
`[00:34:58]` one of the few things that worked really
`[00:34:59]` one of the few things that worked really
`[00:34:59]` well in the 1990s and they work even
`[00:35:01]` well in the 1990s and they work even
`[00:35:01]` better now.
`[00:35:03]` better now.
`[00:35:03]` But I don't think they're the way people
`[00:35:05]` But I don't think they're the way people
`[00:35:05]` do vision.
`[00:35:06]` do vision.
`[00:35:06]` I mean, I think one aspect of it that
`[00:35:08]` I mean, I think one aspect of it that
`[00:35:08]` there's replicated apparatus, that's
`[00:35:09]` there's replicated apparatus, that's
`[00:35:09]` clearly true of the brain.
`[00:35:11]` clearly true of the brain.
`[00:35:11]` Um
`[00:35:13]` Um
`[00:35:13]` but they don't recognize objects the
`[00:35:14]` but they don't recognize objects the
`[00:35:14]` same way as we do.
`[00:35:17]` same way as we do.
`[00:35:17]` And that leads to adversarial examples.
`[00:35:19]` And that leads to adversarial examples.
`[00:35:19]` So if I give you a big database, a
`[00:35:20]` So if I give you a big database, a
`[00:35:20]` convolutional neural net will do very
`[00:35:22]` convolutional neural net will do very
`[00:35:22]` well. It may do better than a person.
`[00:35:24]` well. It may do better than a person.
`[00:35:24]` But it doesn't recognize things the same
`[00:35:25]` But it doesn't recognize things the same
`[00:35:25]` way as a person does. And so I can
`[00:35:28]` way as a person does. And so I can
`[00:35:28]` change things in a way that will cause
`[00:35:30]` change things in a way that will cause
`[00:35:30]` the convolutional neural net to change
`[00:35:32]` the convolutional neural net to change
`[00:35:32]` its mind and a person can't even see the
`[00:35:34]` its mind and a person can't even see the
`[00:35:34]` changes I've made.
`[00:35:36]` changes I've made.
`[00:35:36]` They're using things much more like
`[00:35:37]` They're using things much more like
`[00:35:37]` texture and color.
`[00:35:39]` texture and color.
`[00:35:39]` They're not using the geometrical
`[00:35:41]` They're not using the geometrical
`[00:35:41]` relationships between objects and their
`[00:35:43]` relationships between objects and their
`[00:35:43]` parts.
`[00:35:45]` parts.
`[00:35:45]` Um
`[00:35:46]` Um
`[00:35:46]` I'm convinced that people, the main way
`[00:35:49]` I'm convinced that people, the main way
`[00:35:49]` in which people recognize objects, they
`[00:35:50]` in which people recognize objects, they
`[00:35:50]` obviously use texture and color, but
`[00:35:52]` obviously use texture and color, but
`[00:35:52]` they're very well aware of the
`[00:35:53]` they're very well aware of the
`[00:35:53]` geometrical relationships between an
`[00:35:55]` geometrical relationships between an
`[00:35:55]` object and its parts.
`[00:35:57]` object and its parts.
`[00:35:57]` And that geometrical relationship is
`[00:35:59]` And that geometrical relationship is
`[00:35:59]` completely independent of viewpoint.
`[00:36:02]` completely independent of viewpoint.
`[00:36:02]` And that gives you something that's very
`[00:36:04]` And that gives you something that's very
`[00:36:04]` robust that you should be able to train
`[00:36:06]` robust that you should be able to train
`[00:36:06]` from much less data.
`[00:36:08]` from much less data.
`[00:36:08]` And I actually can't resist doing a
`[00:36:09]` And I actually can't resist doing a
`[00:36:09]` little demonstration to convince you
`[00:36:13]` little demonstration to convince you
`[00:36:13]` that when you understand objects,
`[00:36:15]` that when you understand objects,
`[00:36:15]` it's not just when you're being a
`[00:36:16]` it's not just when you're being a
`[00:36:16]` scientist that you use coordinate
`[00:36:18]` scientist that you use coordinate
`[00:36:18]` frames. It's
`[00:36:20]` frames. It's
`[00:36:20]` even when you're just naively thinking
`[00:36:22]` even when you're just naively thinking
`[00:36:22]` about objects, you impose coordinate
`[00:36:24]` about objects, you impose coordinate
`[00:36:24]` frames on them.
`[00:36:25]` frames on them.
`[00:36:25]` And so I can do a little demonstration.
`[00:36:28]` And so I can do a little demonstration.
`[00:36:28]` Um and you have to participate in this
`[00:36:30]` Um and you have to participate in this
`[00:36:30]` demonstration, otherwise it's no fun.
`[00:36:33]` demonstration, otherwise it's no fun.
`[00:36:33]` Okay, so I want you to imagine sitting
`[00:36:34]` Okay, so I want you to imagine sitting
`[00:36:34]` on the tabletop in front of you,
`[00:36:36]` on the tabletop in front of you,
`[00:36:36]` there's a cube. So here's the top,
`[00:36:38]` there's a cube. So here's the top,
`[00:36:38]` here's the bottom, here's the cube. It's
`[00:36:40]` here's the bottom, here's the cube. It's
`[00:36:40]` a wireframe cube like this, okay? Matte
`[00:36:42]` a wireframe cube like this, okay? Matte
`[00:36:42]` black wires.
`[00:36:44]` black wires.
`[00:36:44]` And what I'm going to do with this cube
`[00:36:46]` And what I'm going to do with this cube
`[00:36:46]` is there's a from your point of view,
`[00:36:48]` is there's a from your point of view,
`[00:36:48]` there's a front bottom right hand corner
`[00:36:50]` there's a front bottom right hand corner
`[00:36:50]` here and there's top back left hand
`[00:36:52]` here and there's top back left hand
`[00:36:52]` corner here.
`[00:36:54]` corner here.
`[00:36:54]` Okay.
`[00:36:55]` Okay.
`[00:36:55]` And I'm going to rotate the cube
`[00:36:57]` And I'm going to rotate the cube
`[00:36:57]` so that the top back left hand corner is
`[00:37:00]` so that the top back left hand corner is
`[00:37:00]` vertically above the front bottom right
`[00:37:03]` vertically above the front bottom right
`[00:37:03]` hand corner. So here we are.
`[00:37:05]` hand corner. So here we are.
`[00:37:05]` And so now I want you to hold your
`[00:37:06]` And so now I want you to hold your
`[00:37:06]` fingertip in space,
`[00:37:08]` fingertip in space,
`[00:37:08]` probably your left fingertip, where the
`[00:37:10]` probably your left fingertip, where the
`[00:37:10]` top vertex of the cube is, okay?
`[00:37:13]` top vertex of the cube is, okay?
`[00:37:13]` And now nobody's doing it. Come on.
`[00:37:17]` And now nobody's doing it. Come on.
`[00:37:17]` Now
`[00:37:18]` Now
`[00:37:18]` with your other fingertip, I just want
`[00:37:19]` with your other fingertip, I just want
`[00:37:20]` you to point to where the other corners
`[00:37:21]` you to point to where the other corners
`[00:37:21]` of the cube are, the ones that aren't
`[00:37:22]` of the cube are, the ones that aren't
`[00:37:22]` resting on the table. So there's one on
`[00:37:24]` resting on the table. So there's one on
`[00:37:24]` the table, one vertically above it here.
`[00:37:26]` the table, one vertically above it here.
`[00:37:26]` Where are the other corners?
`[00:37:28]` Where are the other corners?
`[00:37:28]` And you have to do it. You have to point
`[00:37:29]` And you have to do it. You have to point
`[00:37:29]` them out.
`[00:37:31]` them out.
`[00:37:31]` Okay? Now, I can't see what you're
`[00:37:34]` Okay? Now, I can't see what you're
`[00:37:34]` doing, but I know that a large number of
`[00:37:37]` doing, but I know that a large number of
`[00:37:37]` you will have pointed out four other
`[00:37:39]` you will have pointed out four other
`[00:37:39]` corners, cuz I've done this before.
`[00:37:42]` corners, cuz I've done this before.
`[00:37:42]` And now I want you to imagine a cube in
`[00:37:43]` And now I want you to imagine a cube in
`[00:37:43]` the normal orientation and ask how many
`[00:37:45]` the normal orientation and ask how many
`[00:37:45]` corners does it have?
`[00:37:48]` Okay? It's got eight corners, right? So
`[00:37:50]` there's six of these guys. And what most
`[00:37:52]` there's six of these guys. And what most
`[00:37:52]` people do is they say, "Here, here, here
`[00:37:54]` people do is they say, "Here, here, here
`[00:37:54]` and here. What's the problem?"
`[00:37:56]` and here. What's the problem?"
`[00:37:56]` Well, the problem is that's not a cube.
`[00:37:58]` Well, the problem is that's not a cube.
`[00:37:58]` What you've done is you've preserved the
`[00:38:00]` What you've done is you've preserved the
`[00:38:00]` fourfold rotational symmetry that a cube
`[00:38:02]` fourfold rotational symmetry that a cube
`[00:38:02]` has
`[00:38:03]` has
`[00:38:03]` um and pointed out a completely
`[00:38:05]` um and pointed out a completely
`[00:38:05]` different shape.
`[00:38:06]` different shape.
`[00:38:06]` It's a completely different shape that
`[00:38:08]` It's a completely different shape that
`[00:38:08]` has the same number of faces as a cube
`[00:38:10]` has the same number of faces as a cube
`[00:38:10]` has corners and the same number of
`[00:38:11]` has corners and the same number of
`[00:38:11]` corners as a cube have faces. It's the
`[00:38:13]` corners as a cube have faces. It's the
`[00:38:13]` dual of a cube if you substitute corners
`[00:38:15]` dual of a cube if you substitute corners
`[00:38:15]` for faces, cuz you really like symmetry
`[00:38:16]` for faces, cuz you really like symmetry
`[00:38:16]` so much that you're prepared to really
`[00:38:18]` so much that you're prepared to really
`[00:38:18]` mangle things to preserve the
`[00:38:19]` mangle things to preserve the
`[00:38:19]` symmetries.
`[00:38:20]` symmetries.
`[00:38:20]` Um
`[00:38:22]` Um
`[00:38:22]` actually, a cube has three edges coming
`[00:38:25]` actually, a cube has three edges coming
`[00:38:25]` down like that and three edges coming up
`[00:38:27]` down like that and three edges coming up
`[00:38:27]` like that and my six fingertips are
`[00:38:29]` like that and my six fingertips are
`[00:38:29]` where the corners are, okay? And people
`[00:38:31]` where the corners are, okay? And people
`[00:38:31]` just can't see that
`[00:38:33]` just can't see that
`[00:38:33]` unless they're crystallographers or very
`[00:38:34]` unless they're crystallographers or very
`[00:38:34]` clever. Um
`[00:38:37]` clever. Um
`[00:38:37]` so
`[00:38:38]` so
`[00:38:38]` the main point of this demo is I forced
`[00:38:40]` the main point of this demo is I forced
`[00:38:40]` you by doing this rotation to use an
`[00:38:42]` you by doing this rotation to use an
`[00:38:43]` axis for the cube, the main axis that
`[00:38:45]` axis for the cube, the main axis that
`[00:38:45]` defined the orientation of the cube, was
`[00:38:47]` defined the orientation of the cube, was
`[00:38:47]` not
`[00:38:48]` not
`[00:38:49]` one of the axes of the coordinate frame
`[00:38:50]` one of the axes of the coordinate frame
`[00:38:50]` you usually use for a cube.
`[00:38:52]` you usually use for a cube.
`[00:38:52]` And by forcing you to use an unfamiliar
`[00:38:54]` And by forcing you to use an unfamiliar
`[00:38:54]` coordinate frame, I destroyed all your
`[00:38:56]` coordinate frame, I destroyed all your
`[00:38:56]` knowledge about where the parts of a
`[00:38:57]` knowledge about where the parts of a
`[00:38:57]` cube are.
`[00:38:58]` cube are.
`[00:38:58]` You understand things relative to
`[00:39:00]` You understand things relative to
`[00:39:00]` coordinate frames.
`[00:39:02]` coordinate frames.
`[00:39:02]` And if I get you to impose a different
`[00:39:04]` And if I get you to impose a different
`[00:39:04]` coordinate frame, it's just a different
`[00:39:05]` coordinate frame, it's just a different
`[00:39:05]` object as far as you're concerned.
`[00:39:07]` object as far as you're concerned.
`[00:39:07]` Now, convolutional nets don't do that.
`[00:39:10]` Now, convolutional nets don't do that.
`[00:39:10]` And because they don't do that, I don't
`[00:39:11]` And because they don't do that, I don't
`[00:39:11]` think they're the way people perceive
`[00:39:14]` think they're the way people perceive
`[00:39:14]` shapes.
`[00:39:15]` shapes.
`[00:39:15]` Um
`[00:39:16]` Um
`[00:39:16]` we've recently managed to make neural
`[00:39:18]` we've recently managed to make neural
`[00:39:18]` nets do that by doing some
`[00:39:20]` nets do that by doing some
`[00:39:20]` self-supervised training and there's an
`[00:39:23]` self-supervised training and there's an
`[00:39:23]` archive reference there, which if you're
`[00:39:26]` archive reference there, which if you're
`[00:39:26]` very quick, um you could get or you
`[00:39:28]` very quick, um you could get or you
`[00:39:28]` could um I'll send out a tweet about it
`[00:39:31]` could um I'll send out a tweet about it
`[00:39:31]` later.
`[00:39:35]` And the last thing I want to say is
`[00:39:37]` about not about shape recognition in
`[00:39:39]` about not about shape recognition in
`[00:39:39]` particular, but about the future of
`[00:39:40]` particular, but about the future of
`[00:39:40]` neural networks. There's something very
`[00:39:42]` neural networks. There's something very
`[00:39:42]` funny and very unbiological we've been
`[00:39:44]` funny and very unbiological we've been
`[00:39:44]` doing for the last 50 years,
`[00:39:46]` doing for the last 50 years,
`[00:39:46]` which is we've only been using two time
`[00:39:48]` which is we've only been using two time
`[00:39:48]` scales.
`[00:39:49]` scales.
`[00:39:49]` That is you have neural activities and
`[00:39:51]` That is you have neural activities and
`[00:39:51]` they change rapidly.
`[00:39:53]` they change rapidly.
`[00:39:53]` And you have weights and they change
`[00:39:54]` And you have weights and they change
`[00:39:54]` slowly.
`[00:39:55]` slowly.
`[00:39:55]` And that's it.
`[00:39:57]` And that's it.
`[00:39:57]` But we know that in biology synapses
`[00:40:00]` But we know that in biology synapses
`[00:40:00]` change at all sorts of time scales.
`[00:40:02]` change at all sorts of time scales.
`[00:40:02]` And the question is what happens if you
`[00:40:05]` And the question is what happens if you
`[00:40:05]` now introduce more time scales?
`[00:40:07]` now introduce more time scales?
`[00:40:08]` In particular, let's just introduce one
`[00:40:09]` In particular, let's just introduce one
`[00:40:10]` more time scale and let's say that in
`[00:40:12]` more time scale and let's say that in
`[00:40:12]` addition to these weights changing
`[00:40:13]` addition to these weights changing
`[00:40:13]` slowly, and that's what's going on in
`[00:40:16]` slowly, and that's what's going on in
`[00:40:16]` long-term learning,
`[00:40:17]` long-term learning,
`[00:40:17]` the weights the weights have a
`[00:40:18]` the weights the weights have a
`[00:40:18]` component.
`[00:40:20]` component.
`[00:40:20]` The very same weights, the very same
`[00:40:21]` The very same weights, the very same
`[00:40:21]` synapses, but there's an extra component
`[00:40:23]` synapses, but there's an extra component
`[00:40:23]` that can change more rapidly and decays
`[00:40:25]` that can change more rapidly and decays
`[00:40:25]` quite rapidly.
`[00:40:28]` quite rapidly.
`[00:40:28]` So, if you ask where's your memory of
`[00:40:30]` So, if you ask where's your memory of
`[00:40:30]` the fact that a minute ago I put my
`[00:40:32]` the fact that a minute ago I put my
`[00:40:32]` finger on this corner here,
`[00:40:34]` finger on this corner here,
`[00:40:34]` is that in a bunch of neurons that are
`[00:40:35]` is that in a bunch of neurons that are
`[00:40:36]` sitting there
`[00:40:37]` sitting there
`[00:40:37]` um
`[00:40:38]` um
`[00:40:38]` sort of being active so that you can
`[00:40:39]` sort of being active so that you can
`[00:40:40]` remember that? That seems unlikely. It's
`[00:40:41]` remember that? That seems unlikely. It's
`[00:40:41]` much more likely your memory for this
`[00:40:44]` much more likely your memory for this
`[00:40:44]` is in fast modifications to the weights
`[00:40:46]` is in fast modifications to the weights
`[00:40:46]` of the neural network that allow you to
`[00:40:48]` of the neural network that allow you to
`[00:40:48]` reconstruct this very rapidly
`[00:40:50]` reconstruct this very rapidly
`[00:40:50]` and that will decay with time.
`[00:40:52]` and that will decay with time.
`[00:40:52]` Um so, you've got a memory that's in the
`[00:40:54]` Um so, you've got a memory that's in the
`[00:40:54]` weights, that's a short-term memory.
`[00:40:56]` weights, that's a short-term memory.
`[00:40:56]` As soon as you do that all sorts of good
`[00:40:58]` As soon as you do that all sorts of good
`[00:40:58]` things happen.
`[00:40:59]` things happen.
`[00:40:59]` Um
`[00:41:01]` Um
`[00:41:01]` you can
`[00:41:02]` you can
`[00:41:02]` use that to get a better optimization
`[00:41:04]` use that to get a better optimization
`[00:41:04]` method
`[00:41:05]` method
`[00:41:05]` and you can use that to do something
`[00:41:07]` and you can use that to do something
`[00:41:07]` that may very well be relevant to the
`[00:41:10]` that may very well be relevant to the
`[00:41:10]` reasoning. You can use it to allow
`[00:41:12]` reasoning. You can use it to allow
`[00:41:12]` neural networks to do true recursion,
`[00:41:14]` neural networks to do true recursion,
`[00:41:14]` not very deep, but true recursion. And
`[00:41:16]` not very deep, but true recursion. And
`[00:41:16]` what I mean by true recursion is
`[00:41:18]` what I mean by true recursion is
`[00:41:18]` when you do the recursive call
`[00:41:21]` when you do the recursive call
`[00:41:21]` like a relative clause in a sentence,
`[00:41:24]` like a relative clause in a sentence,
`[00:41:24]` the neural net can use all the same
`[00:41:26]` the neural net can use all the same
`[00:41:26]` neurons and all the same weights that it
`[00:41:28]` neurons and all the same weights that it
`[00:41:29]` was using for the whole sentence to
`[00:41:30]` was using for the whole sentence to
`[00:41:30]` process the relative clause.
`[00:41:33]` process the relative clause.
`[00:41:33]` And of course, to do that, somehow it
`[00:41:35]` And of course, to do that, somehow it
`[00:41:35]` has to remember what was going on when
`[00:41:37]` has to remember what was going on when
`[00:41:37]` it decided to process the relative
`[00:41:39]` it decided to process the relative
`[00:41:39]` clause. So, it has to store that
`[00:41:40]` clause. So, it has to store that
`[00:41:40]` somewhere.
`[00:41:42]` somewhere.
`[00:41:42]` And I don't think it stores it in the
`[00:41:43]` And I don't think it stores it in the
`[00:41:43]` neurons. I think it stores it in
`[00:41:45]` neurons. I think it stores it in
`[00:41:45]` temporary changes to synapse strengths.
`[00:41:47]` temporary changes to synapse strengths.
`[00:41:47]` And when it's finished processing the
`[00:41:48]` And when it's finished processing the
`[00:41:48]` relative clause, it packages it up and
`[00:41:50]` relative clause, it packages it up and
`[00:41:50]` says basically it says, "Now, what was I
`[00:41:51]` says basically it says, "Now, what was I
`[00:41:52]` doing when I started doing this
`[00:41:53]` doing when I started doing this
`[00:41:53]` processing?"
`[00:41:54]` processing?"
`[00:41:54]` And it can get the information back from
`[00:41:56]` And it can get the information back from
`[00:41:56]` this associative memory in the fast
`[00:41:58]` this associative memory in the fast
`[00:41:58]` weights.
`[00:41:59]` weights.
`[00:41:59]` Um
`[00:42:00]` Um
`[00:42:00]` I wanted to finish with that because the
`[00:42:02]` I wanted to finish with that because the
`[00:42:02]` very first talk I gave in 1973
`[00:42:05]` very first talk I gave in 1973
`[00:42:05]` was about exactly that. I had a system
`[00:42:06]` was about exactly that. I had a system
`[00:42:07]` that worked on a computer that had 64K
`[00:42:09]` that worked on a computer that had 64K
`[00:42:09]` of memory. Um
`[00:42:11]` of memory. Um
`[00:42:11]` I haven't got around to publishing it
`[00:42:13]` I haven't got around to publishing it
`[00:42:13]` yet, but I think it's becoming
`[00:42:14]` yet, but I think it's becoming
`[00:42:14]` fashionable again, so I soon will.
`[00:42:17]` fashionable again, so I soon will.
`[00:42:17]` And that's the end of my talk.
`[00:42:20]` And that's the end of my talk.
`[00:42:20]` And I'm out of time.
`[00:42:21]` And I'm out of time.
`[00:42:21]` [applause]
`[00:42:29]` [applause]
`[00:42:32]` And now I'd like to introduce Yann
`[00:42:33]` LeCun,
`[00:42:35]` LeCun,
`[00:42:35]` who's not only a colleague, but a very
`[00:42:36]` who's not only a colleague, but a very
`[00:42:36]` good friend.
`[00:42:39]` [applause]
`[00:42:46]` Okay.
`[00:42:48]` I'll talk about the sequel.
`[00:42:51]` I'll talk about the sequel.
`[00:42:51]` But I'll start also with a little bit of
`[00:42:52]` But I'll start also with a little bit of
`[00:42:53]` history and sort of go through some of
`[00:42:55]` history and sort of go through some of
`[00:42:55]` the things that
`[00:42:56]` the things that
`[00:42:56]` Jeff has mentioned. So, Jeff talked
`[00:42:58]` Jeff has mentioned. So, Jeff talked
`[00:42:58]` about we
`[00:43:00]` about we
`[00:43:00]` about supervised learning and supervised
`[00:43:02]` about supervised learning and supervised
`[00:43:02]` learning works amazingly well if you
`[00:43:04]` learning works amazingly well if you
`[00:43:04]` have lots of data.
`[00:43:06]` have lots of data.
`[00:43:06]` Uh we all know this, so we can do speech
`[00:43:08]` Uh we all know this, so we can do speech
`[00:43:08]` recognition, we can do uh image
`[00:43:10]` recognition, we can do uh image
`[00:43:10]` recognition, we can do face recognition,
`[00:43:12]` recognition, we can do face recognition,
`[00:43:12]` we can do we can generate captions for
`[00:43:14]` we can do we can generate captions for
`[00:43:14]` images, we can do translation. That
`[00:43:16]` images, we can do translation. That
`[00:43:16]` works really well.
`[00:43:18]` works really well.
`[00:43:18]` Um and if you give your neural net a
`[00:43:19]` Um and if you give your neural net a
`[00:43:19]` particular structure, something like a
`[00:43:21]` particular structure, something like a
`[00:43:21]` convolutional net,
`[00:43:22]` convolutional net,
`[00:43:22]` uh as Jeff mentioned in the late '80s,
`[00:43:25]` uh as Jeff mentioned in the late '80s,
`[00:43:25]` early '90s, we could uh
`[00:43:27]` early '90s, we could uh
`[00:43:27]` train systems to recognize handwriting.
`[00:43:29]` train systems to recognize handwriting.
`[00:43:29]` That was quite successful.
`[00:43:31]` That was quite successful.
`[00:43:31]` Uh by the end of the '90s, a system of
`[00:43:32]` Uh by the end of the '90s, a system of
`[00:43:32]` this type that I built at Bell Labs uh
`[00:43:35]` this type that I built at Bell Labs uh
`[00:43:35]` was reading something like 10 to 20% of
`[00:43:37]` was reading something like 10 to 20% of
`[00:43:37]` all the checks in the US. So, uh a big
`[00:43:39]` all the checks in the US. So, uh a big
`[00:43:39]` success, even a commercial success. But
`[00:43:41]` success, even a commercial success. But
`[00:43:42]` that but by that time the entire
`[00:43:43]` that but by that time the entire
`[00:43:43]` community had basically abandoned neural
`[00:43:45]` community had basically abandoned neural
`[00:43:45]` nets, partly because of the lack of
`[00:43:48]` nets, partly because of the lack of
`[00:43:48]` large data sets for which they could
`[00:43:49]` large data sets for which they could
`[00:43:49]` work, partly because the type of
`[00:43:51]` work, partly because the type of
`[00:43:51]` software at the time that you had to
`[00:43:53]` software at the time that you had to
`[00:43:53]` write was fairly complicated and it uh
`[00:43:55]` write was fairly complicated and it uh
`[00:43:55]` it was a big investment to um to to do
`[00:43:57]` it was a big investment to um to to do
`[00:43:57]` this. Partly also because computers were
`[00:43:59]` this. Partly also because computers were
`[00:44:00]` not fast enough for
`[00:44:01]` not fast enough for
`[00:44:01]` uh all kinds of other applications.
`[00:44:04]` uh all kinds of other applications.
`[00:44:04]` But convolutional nets really are
`[00:44:06]` But convolutional nets really are
`[00:44:06]` inspired by uh biology. They're not
`[00:44:08]` inspired by uh biology. They're not
`[00:44:08]` copying biology, but there's a lot of
`[00:44:10]` copying biology, but there's a lot of
`[00:44:10]` inspiration from from biology, from the
`[00:44:12]` inspiration from from biology, from the
`[00:44:12]` architecture of the visual cortex and
`[00:44:15]` architecture of the visual cortex and
`[00:44:15]` ideas that come naturally when you study
`[00:44:17]` ideas that come naturally when you study
`[00:44:17]` signal processing, the idea that
`[00:44:20]` signal processing, the idea that
`[00:44:20]` filtering is is a good
`[00:44:22]` filtering is is a good
`[00:44:22]` way to kind of process uh signals,
`[00:44:24]` way to kind of process uh signals,
`[00:44:24]` whether they're audio signals or image
`[00:44:26]` whether they're audio signals or image
`[00:44:26]` image signals, and that convolution is a
`[00:44:27]` image signals, and that convolution is a
`[00:44:28]` way to do filtering is very natural and
`[00:44:30]` way to do filtering is very natural and
`[00:44:30]` the fact that you find this in the brain
`[00:44:31]` the fact that you find this in the brain
`[00:44:31]` is really not that surprising. Um and
`[00:44:34]` is really not that surprising. Um and
`[00:44:34]` those ideas of course were uh proposed
`[00:44:36]` those ideas of course were uh proposed
`[00:44:36]` by Hubel and Wiesel in sort of classic
`[00:44:38]` by Hubel and Wiesel in sort of classic
`[00:44:38]` work in neuroscience back in the '60s,
`[00:44:40]` work in neuroscience back in the '60s,
`[00:44:40]` as well as uh
`[00:44:42]` as well as uh
`[00:44:42]` and and sort of picked up by uh
`[00:44:43]` and and sort of picked up by uh
`[00:44:43]` Fukushima, who's um Japanese researcher
`[00:44:46]` Fukushima, who's um Japanese researcher
`[00:44:46]` who tried to uh build computer models of
`[00:44:49]` who tried to uh build computer models of
`[00:44:49]` uh the the Hubel and Wiesel model, if
`[00:44:51]` uh the the Hubel and Wiesel model, if
`[00:44:51]` you want.
`[00:44:52]` you want.
`[00:44:52]` And I found that inspiring and and sort
`[00:44:55]` And I found that inspiring and and sort
`[00:44:55]` of tried to reproduce this using uh
`[00:44:57]` of tried to reproduce this using uh
`[00:44:57]` neural nets that could be trained with
`[00:44:58]` neural nets that could be trained with
`[00:44:59]` backpropagation. That's basically what a
`[00:45:00]` backpropagation. That's basically what a
`[00:45:00]` convolutional net uh
`[00:45:01]` convolutional net uh
`[00:45:01]` is.
`[00:45:03]` is.
`[00:45:03]` And so, the idea of convolutional net is
`[00:45:04]` And so, the idea of convolutional net is
`[00:45:04]` that uh the
`[00:45:06]` that uh the
`[00:45:07]` the world the perceptual world is uh
`[00:45:09]` the world the perceptual world is uh
`[00:45:09]` compositional, that the
`[00:45:12]` compositional, that the
`[00:45:12]` the visual world
`[00:45:13]` the visual world
`[00:45:13]` objects are formed by parts and parts
`[00:45:16]` objects are formed by parts and parts
`[00:45:16]` are formed by motifs and motifs are
`[00:45:19]` are formed by motifs and motifs are
`[00:45:19]` formed by
`[00:45:20]` formed by
`[00:45:20]` uh
`[00:45:22]` uh
`[00:45:22]` textures or elementary
`[00:45:25]` textures or elementary
`[00:45:25]` combinations of edges and edges are
`[00:45:27]` combinations of edges and edges are
`[00:45:27]` formed by
`[00:45:28]` formed by
`[00:45:28]` by pixels, arrangements of pixels. And
`[00:45:30]` by pixels, arrangements of pixels. And
`[00:45:30]` so, if you have a system that's so
`[00:45:31]` so, if you have a system that's so
`[00:45:31]` hierarchically can detect uh
`[00:45:34]` hierarchically can detect uh
`[00:45:34]` uh
`[00:45:35]` uh
`[00:45:35]` unusually useful combinations of pixels
`[00:45:37]` unusually useful combinations of pixels
`[00:45:37]` into edges and edges into motifs and
`[00:45:40]` into edges and edges into motifs and
`[00:45:40]` motifs into parts of objects, then you
`[00:45:41]` motifs into parts of objects, then you
`[00:45:41]` will have a recognition system. This
`[00:45:43]` will have a recognition system. This
`[00:45:43]` idea of hierarchy actually goes back a
`[00:45:45]` idea of hierarchy actually goes back a
`[00:45:45]` long time.
`[00:45:46]` long time.
`[00:45:46]` And so, that's uh that's really the
`[00:45:48]` And so, that's uh that's really the
`[00:45:48]` principle of of convolutional nets. And
`[00:45:49]` principle of of convolutional nets. And
`[00:45:49]` it turns out that
`[00:45:51]` it turns out that
`[00:45:51]` um hierarchical representations are good
`[00:45:53]` um hierarchical representations are good
`[00:45:53]` not just for for vision, but also for
`[00:45:55]` not just for for vision, but also for
`[00:45:55]` speech, for text and for all kinds of
`[00:45:58]` speech, for text and for all kinds of
`[00:45:58]` other natural signals that are
`[00:46:00]` other natural signals that are
`[00:46:00]` comprehensible because they are
`[00:46:02]` comprehensible because they are
`[00:46:02]` compositional.
`[00:46:03]` compositional.
`[00:46:03]` Um I think there is this saying uh it's
`[00:46:05]` Um I think there is this saying uh it's
`[00:46:05]` attributed to Einstein, I believe, the
`[00:46:08]` attributed to Einstein, I believe, the
`[00:46:08]` uh
`[00:46:09]` uh
`[00:46:09]` what is most
`[00:46:11]` what is most
`[00:46:11]` uh
`[00:46:12]` uh
`[00:46:12]` mysterious about the world is that it is
`[00:46:14]` mysterious about the world is that it is
`[00:46:14]` understandable and it's probably because
`[00:46:17]` understandable and it's probably because
`[00:46:17]` of the compositional nature
`[00:46:19]` of the compositional nature
`[00:46:19]` of uh of the natural of natural signals.
`[00:46:22]` of uh of the natural of natural signals.
`[00:46:22]` So, uh in the early '90s we were able to
`[00:46:25]` So, uh in the early '90s we were able to
`[00:46:25]` do things like build recognition systems
`[00:46:26]` do things like build recognition systems
`[00:46:26]` like this one. This is a younger version
`[00:46:28]` like this one. This is a younger version
`[00:46:28]` of myself here. Uh I'm at Bell Labs.
`[00:46:30]` of myself here. Uh I'm at Bell Labs.
`[00:46:30]` This is by the way my phone number at
`[00:46:32]` This is by the way my phone number at
`[00:46:32]` Bell Labs in Holmdel, no longer
`[00:46:34]` Bell Labs in Holmdel, no longer
`[00:46:34]` operating. I'm hitting a key here and
`[00:46:37]` operating. I'm hitting a key here and
`[00:46:37]` the system captures an image with a
`[00:46:39]` the system captures an image with a
`[00:46:39]` video camera. This runs on the PC with a
`[00:46:41]` video camera. This runs on the PC with a
`[00:46:41]` special DSP card in it and it could run
`[00:46:43]` special DSP card in it and it could run
`[00:46:43]` those convolutional nets at you know,
`[00:46:45]` those convolutional nets at you know,
`[00:46:45]` several hundred characters per second at
`[00:46:47]` several hundred characters per second at
`[00:46:47]` the time, which was
`[00:46:48]` the time, which was
`[00:46:48]` amazing. We could run 20 megaflops, you
`[00:46:50]` amazing. We could run 20 megaflops, you
`[00:46:50]` know, that was just incredible. So, that
`[00:46:53]` know, that was just incredible. So, that
`[00:46:53]` worked pretty well.
`[00:46:54]` worked pretty well.
`[00:46:55]` And uh pretty soon we realized we could
`[00:46:56]` And uh pretty soon we realized we could
`[00:46:56]` use this for natural images as well to
`[00:46:58]` use this for natural images as well to
`[00:46:58]` do things like detecting uh
`[00:47:00]` do things like detecting uh
`[00:47:00]` uh faces, eventually detecting
`[00:47:02]` uh faces, eventually detecting
`[00:47:02]` pedestrians. That took um a few years.
`[00:47:05]` pedestrians. That took um a few years.
`[00:47:05]` Uh but as
`[00:47:07]` Uh but as
`[00:47:07]` uh Jeff mentioned, there was sort of a
`[00:47:08]` uh Jeff mentioned, there was sort of a
`[00:47:08]` neural net winter between the mid-'90s
`[00:47:10]` neural net winter between the mid-'90s
`[00:47:10]` and the
`[00:47:11]` and the
`[00:47:11]` uh sort of late 2000, if you want, where
`[00:47:14]` uh sort of late 2000, if you want, where
`[00:47:14]` uh almost nobody was working on neural
`[00:47:15]` uh almost nobody was working on neural
`[00:47:16]` nets except a few crazy people like us.
`[00:47:18]` nets except a few crazy people like us.
`[00:47:18]` Um
`[00:47:19]` Um
`[00:47:19]` So,
`[00:47:20]` So,
`[00:47:20]` that didn't stop us and so uh working on
`[00:47:23]` that didn't stop us and so uh working on
`[00:47:23]` face detection, pedestrian detection,
`[00:47:25]` face detection, pedestrian detection,
`[00:47:25]` even working on uh using machine
`[00:47:28]` even working on uh using machine
`[00:47:28]` learning and and convolutional net for
`[00:47:30]` learning and and convolutional net for
`[00:47:30]` uh robotics, where we we would use a
`[00:47:33]` uh robotics, where we we would use a
`[00:47:33]` convolutional net to label an entire
`[00:47:35]` convolutional net to label an entire
`[00:47:35]` image in such a way that
`[00:47:38]` image in such a way that
`[00:47:38]` uh every pixel in an image would be
`[00:47:40]` uh every pixel in an image would be
`[00:47:40]` labeled as to whether it's traversable
`[00:47:42]` labeled as to whether it's traversable
`[00:47:42]` or not traversable by a robot. And the
`[00:47:45]` or not traversable by a robot. And the
`[00:47:45]` nice thing about this is that you can
`[00:47:46]` nice thing about this is that you can
`[00:47:46]` you can collect data automatically. You
`[00:47:48]` you can collect data automatically. You
`[00:47:48]` don't need to manually label it because
`[00:47:50]` don't need to manually label it because
`[00:47:50]` uh using stereo vision, you can figure
`[00:47:52]` uh using stereo vision, you can figure
`[00:47:52]` out if uh a pixel sticks out of the
`[00:47:54]` out if uh a pixel sticks out of the
`[00:47:54]` ground or not uh using 3D
`[00:47:56]` ground or not uh using 3D
`[00:47:56]` reconstruction. But unfortunately, that
`[00:47:58]` reconstruction. But unfortunately, that
`[00:47:58]` only works at short range. So, if you
`[00:48:00]` only works at short range. So, if you
`[00:48:00]` want a system that can plan long-range
`[00:48:02]` want a system that can plan long-range
`[00:48:02]` trajectories, then you can train a
`[00:48:03]` trajectories, then you can train a
`[00:48:03]` convolutional net to make the
`[00:48:05]` convolutional net to make the
`[00:48:05]` predictions for traversability using
`[00:48:07]` predictions for traversability using
`[00:48:07]` those labels and then uh let the the
`[00:48:09]` those labels and then uh let the the
`[00:48:09]` robot drive itself around. So, it's got
`[00:48:12]` robot drive itself around. So, it's got
`[00:48:12]` This particular robot here is a
`[00:48:13]` This particular robot here is a
`[00:48:13]` combination of different uh
`[00:48:15]` combination of different uh
`[00:48:15]` uh features that it uses
`[00:48:17]` uh features that it uses
`[00:48:17]` um
`[00:48:19]` um
`[00:48:19]` uh extracted by the convolutional net
`[00:48:21]` uh extracted by the convolutional net
`[00:48:21]` and uh
`[00:48:22]` and uh
`[00:48:22]` also a a rapid stereo vision system that
`[00:48:24]` also a a rapid stereo vision system that
`[00:48:25]` allows it to
`[00:48:26]` allows it to
`[00:48:26]` avoid obstacles such as pesky graduate
`[00:48:29]` avoid obstacles such as pesky graduate
`[00:48:29]` students.
`[00:48:32]` Uh Pierson and Raya at SAIL, by the way,
`[00:48:34]` who are pretty
`[00:48:36]` who are pretty
`[00:48:36]` sure the robot is not going to run them
`[00:48:38]` sure the robot is not going to run them
`[00:48:38]` over because they actually wrote the
`[00:48:39]` over because they actually wrote the
`[00:48:39]` code.
`[00:48:40]` code.
`[00:48:40]` Um
`[00:48:44]` Okay. And then a couple years later, we
`[00:48:47]` uh used a very similar system to do
`[00:48:48]` uh used a very similar system to do
`[00:48:48]` semantic segmentation. This is actually
`[00:48:50]` semantic segmentation. This is actually
`[00:48:50]` the work that uh Jeff was talking about
`[00:48:53]` the work that uh Jeff was talking about
`[00:48:53]` that was rejected from CVPR 2011.
`[00:48:55]` that was rejected from CVPR 2011.
`[00:48:55]` Uh so, this is the a system that could
`[00:48:57]` Uh so, this is the a system that could
`[00:48:57]` in real time, using a FPGA
`[00:48:59]` in real time, using a FPGA
`[00:48:59]` implementation, uh segment, you know,
`[00:49:01]` implementation, uh segment, you know,
`[00:49:01]` basically give uh
`[00:49:03]` basically give uh
`[00:49:03]` a a category for every pixel in an image
`[00:49:06]` a a category for every pixel in an image
`[00:49:06]` um at at about 30 frames per second at
`[00:49:08]` um at at about 30 frames per second at
`[00:49:08]` sort of decent resolution. It was far
`[00:49:10]` sort of decent resolution. It was far
`[00:49:10]` from perfect, but it could sort of label
`[00:49:12]` from perfect, but it could sort of label
`[00:49:12]` with sort of reasonable accuracy, detect
`[00:49:14]` with sort of reasonable accuracy, detect
`[00:49:14]` pedestrians, detect the roads and the
`[00:49:16]` pedestrians, detect the roads and the
`[00:49:16]` trees and etc.
`[00:49:18]` trees and etc.
`[00:49:18]` Um
`[00:49:20]` Um
`[00:49:20]` But the results basically were not
`[00:49:22]` But the results basically were not
`[00:49:22]` immediately believed by the uh computer
`[00:49:25]` immediately believed by the uh computer
`[00:49:25]` vision community. Now, to measure the
`[00:49:27]` vision community. Now, to measure the
`[00:49:27]` progress that has happened
`[00:49:29]` progress that has happened
`[00:49:29]` uh since then, in the last 10 years
`[00:49:31]` uh since then, in the last 10 years
`[00:49:31]` essentially,
`[00:49:32]` essentially,
`[00:49:32]` uh this is an example of a result of a
`[00:49:34]` uh this is an example of a result of a
`[00:49:34]` very recent system that was put together
`[00:49:36]` very recent system that was put together
`[00:49:36]` by a team at Facebook um that they
`[00:49:39]` by a team at Facebook um that they
`[00:49:39]` called a panoptic feature pyramid
`[00:49:41]` called a panoptic feature pyramid
`[00:49:41]` network. So, it's basically a large
`[00:49:42]` network. So, it's basically a large
`[00:49:42]` convolutional net that has
`[00:49:43]` convolutional net that has
`[00:49:43]` uh sort of a a path that extracts
`[00:49:45]` uh sort of a a path that extracts
`[00:49:45]` features
`[00:49:46]` features
`[00:49:47]` um multi-layer paths that extract
`[00:49:48]` um multi-layer paths that extract
`[00:49:48]` features and then another path that sort
`[00:49:49]` features and then another path that sort
`[00:49:49]` of generates an output image. And the
`[00:49:51]` of generates an output image. And the
`[00:49:51]` output image basically identifies and
`[00:49:55]` output image basically identifies and
`[00:49:55]` generates a a mask for every instance of
`[00:49:57]` generates a a mask for every instance of
`[00:49:57]` every object in the image and tells you
`[00:49:58]` every object in the image and tells you
`[00:49:59]` what category they are. So, here the
`[00:50:00]` what category they are. So, here the
`[00:50:00]` name of the categories are not
`[00:50:01]` name of the categories are not
`[00:50:01]` displayed, but it can recognize
`[00:50:03]` displayed, but it can recognize
`[00:50:03]` something like a few hundred categories.
`[00:50:05]` something like a few hundred categories.
`[00:50:05]` People, vehicles of various kinds, uh
`[00:50:07]` People, vehicles of various kinds, uh
`[00:50:07]` and not just object categories, but also
`[00:50:09]` and not just object categories, but also
`[00:50:09]` sort of background uh
`[00:50:11]` sort of background uh
`[00:50:11]` uh
`[00:50:12]` uh
`[00:50:12]` sort of
`[00:50:13]` sort of
`[00:50:13]` textures or regions, things like, you
`[00:50:15]` textures or regions, things like, you
`[00:50:15]` know, grass and sand and
`[00:50:17]` know, grass and sand and
`[00:50:17]` uh trees and things like that. So, you
`[00:50:19]` uh trees and things like that. So, you
`[00:50:19]` would imagine a system like this would
`[00:50:20]` would imagine a system like this would
`[00:50:20]` be very useful for things like
`[00:50:22]` be very useful for things like
`[00:50:22]` self-driving cars if you have the
`[00:50:23]` self-driving cars if you have the
`[00:50:23]` complete segmentation identification of
`[00:50:25]` complete segmentation identification of
`[00:50:25]` all pixels in an image, uh it would make
`[00:50:28]` all pixels in an image, uh it would make
`[00:50:28]` it easier to build self-driving cars.
`[00:50:30]` it easier to build self-driving cars.
`[00:50:30]` Not just not just self-driving cars, but
`[00:50:31]` Not just not just self-driving cars, but
`[00:50:32]` also medical image analysis systems. So,
`[00:50:34]` also medical image analysis systems. So,
`[00:50:34]` this is a relatively similar
`[00:50:35]` this is a relatively similar
`[00:50:35]` architecture. People call this unit
`[00:50:38]` architecture. People call this unit
`[00:50:38]` sometimes because of the obvious U shape
`[00:50:39]` sometimes because of the obvious U shape
`[00:50:39]` of this uh
`[00:50:41]` of this uh
`[00:50:41]` of this uh convolutional net. Again, it
`[00:50:42]` of this uh convolutional net. Again, it
`[00:50:42]` has uh an encoder part that sort of
`[00:50:45]` has uh an encoder part that sort of
`[00:50:45]` extracts features and then a a sort of
`[00:50:47]` extracts features and then a a sort of
`[00:50:47]` a part that constructs the output image
`[00:50:49]` a part that constructs the output image
`[00:50:49]` where the the parts of the medical
`[00:50:52]` where the the parts of the medical
`[00:50:52]` images are segmented. This is the kind
`[00:50:54]` images are segmented. This is the kind
`[00:50:54]` of result that it's producing.
`[00:50:56]` of result that it's producing.
`[00:50:56]` Uh this is some work by uh some of my
`[00:50:58]` Uh this is some work by uh some of my
`[00:50:58]` colleagues at NYU. I was not involved in
`[00:50:59]` colleagues at NYU. I was not involved in
`[00:50:59]` this work. Uh this a different subgroup
`[00:51:02]` this work. Uh this a different subgroup
`[00:51:02]` of colleagues with some common
`[00:51:04]` of colleagues with some common
`[00:51:04]` co-authors as well and so on. Uh
`[00:51:06]` co-authors as well and so on. Uh
`[00:51:06]` detecting breast cancer from from
`[00:51:08]` detecting breast cancer from from
`[00:51:08]` imaging from from x-rays uh from
`[00:51:10]` imaging from from x-rays uh from
`[00:51:10]` mammograms.
`[00:51:12]` mammograms.
`[00:51:12]` Uh in fact, one of the most
`[00:51:14]` Uh in fact, one of the most
`[00:51:15]` sort of hottest topics in uh in in uh
`[00:51:18]` sort of hottest topics in uh in in uh
`[00:51:18]` radiology these these days is using deep
`[00:51:20]` radiology these these days is using deep
`[00:51:20]` learning for uh medical image analysis.
`[00:51:22]` learning for uh medical image analysis.
`[00:51:22]` It's a
`[00:51:23]` It's a
`[00:51:23]` it's probably going to
`[00:51:25]` it's probably going to
`[00:51:25]` affect, if not revolutionize, uh
`[00:51:27]` affect, if not revolutionize, uh
`[00:51:27]` radiology in the next few years. It's
`[00:51:28]` radiology in the next few years. It's
`[00:51:28]` already it already has to some extent.
`[00:51:31]` already it already has to some extent.
`[00:51:31]` Uh
`[00:51:32]` Uh
`[00:51:32]` some more work along those directions.
`[00:51:33]` some more work along those directions.
`[00:51:33]` Uh this is actually a collaboration
`[00:51:35]` Uh this is actually a collaboration
`[00:51:35]` between the NYU Medical School and
`[00:51:36]` between the NYU Medical School and
`[00:51:36]` Facebook AI Research in accelerating the
`[00:51:39]` Facebook AI Research in accelerating the
`[00:51:39]` data collection for MRI. So, when you uh
`[00:51:42]` data collection for MRI. So, when you uh
`[00:51:42]` go through an MRI, you have to sit in
`[00:51:43]` go through an MRI, you have to sit in
`[00:51:43]` the machine for about an hour or 20
`[00:51:45]` the machine for about an hour or 20
`[00:51:45]` minutes, depending on the kind of exam
`[00:51:47]` minutes, depending on the kind of exam
`[00:51:47]` you're going through.
`[00:51:48]` you're going through.
`[00:51:48]` And uh
`[00:51:49]` And uh
`[00:51:49]` this uh technique here
`[00:51:52]` this uh technique here
`[00:51:52]` using
`[00:51:53]` using
`[00:51:53]` those kind of uh reconstruction uh
`[00:51:55]` those kind of uh reconstruction uh
`[00:51:55]` convolutional net allows to basically
`[00:51:57]` convolutional net allows to basically
`[00:51:57]` reduce the data collection time and get
`[00:52:00]` reduce the data collection time and get
`[00:52:00]` images that are essentially of the same
`[00:52:02]` images that are essentially of the same
`[00:52:02]` quality.
`[00:52:04]` quality.
`[00:52:04]` Um so,
`[00:52:06]` Um so,
`[00:52:06]` they will not put radiology out of jobs,
`[00:52:10]` they will not put radiology out of jobs,
`[00:52:10]` um but it will make the job more
`[00:52:12]` um but it will make the job more
`[00:52:12]` interesting, probably. Um Jeff was
`[00:52:15]` interesting, probably. Um Jeff was
`[00:52:15]` mentioning uh work on uh translation
`[00:52:17]` mentioning uh work on uh translation
`[00:52:17]` with with neural nets. This is uh I
`[00:52:19]` with with neural nets. This is uh I
`[00:52:19]` think a a very surprising and
`[00:52:22]` think a a very surprising and
`[00:52:22]` interesting development of the fact that
`[00:52:24]` interesting development of the fact that
`[00:52:24]` you can use neural nets to do
`[00:52:25]` you can use neural nets to do
`[00:52:25]` translation.
`[00:52:26]` translation.
`[00:52:26]` Um and there is a a lot of innovation in
`[00:52:28]` Um and there is a a lot of innovation in
`[00:52:29]` the kind of architectures that are used
`[00:52:30]` the kind of architectures that are used
`[00:52:30]` for this. So, uh Jeff talked about the
`[00:52:32]` for this. So, uh Jeff talked about the
`[00:52:32]` attention mechanism, the transformer
`[00:52:34]` attention mechanism, the transformer
`[00:52:34]` architecture. This is uh a new one
`[00:52:36]` architecture. This is uh a new one
`[00:52:36]` called dynamic convolutions, which kind
`[00:52:37]` called dynamic convolutions, which kind
`[00:52:37]` of recycles a bit of those ideas. And
`[00:52:40]` of recycles a bit of those ideas. And
`[00:52:40]` and things work uh really well there.
`[00:52:42]` and things work uh really well there.
`[00:52:42]` Those networks are very large. They have
`[00:52:44]` Those networks are very large. They have
`[00:52:44]` a few hundred million parameters in
`[00:52:45]` a few hundred million parameters in
`[00:52:45]` them.
`[00:52:46]` them.
`[00:52:46]` And so,
`[00:52:47]` And so,
`[00:52:47]` the the some of the challenges there is
`[00:52:50]` the the some of the challenges there is
`[00:52:50]` actually running them uh on on GPUs,
`[00:52:53]` actually running them uh on on GPUs,
`[00:52:53]` having enough memory to run them. We're
`[00:52:54]` having enough memory to run them. We're
`[00:52:55]` basically limited by uh GPU memory
`[00:52:57]` basically limited by uh GPU memory
`[00:52:57]` there.
`[00:52:58]` there.
`[00:52:58]` So, those ideas of image segmentation
`[00:53:00]` So, those ideas of image segmentation
`[00:53:00]` have been used by uh people working on
`[00:53:02]` have been used by uh people working on
`[00:53:02]` self-driving cars, particularly uh
`[00:53:04]` self-driving cars, particularly uh
`[00:53:04]` people at Mobileye, going uh which is
`[00:53:07]` people at Mobileye, going uh which is
`[00:53:07]` now uh Intel, going back several years.
`[00:53:10]` now uh Intel, going back several years.
`[00:53:10]` Uh those the first convolutional nets, I
`[00:53:12]` Uh those the first convolutional nets, I
`[00:53:12]` think, that were deployed for
`[00:53:13]` think, that were deployed for
`[00:53:13]` self-driving cars or for driving
`[00:53:14]` self-driving cars or for driving
`[00:53:14]` assistance were in the uh 2015 uh Tesla
`[00:53:17]` assistance were in the uh 2015 uh Tesla
`[00:53:18]` S model.
`[00:53:19]` S model.
`[00:53:19]` Nvidia has uh devoted a large uh set of
`[00:53:22]` Nvidia has uh devoted a large uh set of
`[00:53:22]` efforts also to self-driving cars. And
`[00:53:24]` efforts also to self-driving cars. And
`[00:53:24]` so, there's a lot of interesting things
`[00:53:25]` so, there's a lot of interesting things
`[00:53:25]` going on there. But, progress
`[00:53:28]` going on there. But, progress
`[00:53:28]` is
`[00:53:29]` is
`[00:53:29]` uh
`[00:53:30]` uh
`[00:53:30]` I wouldn't say slow, but
`[00:53:32]` I wouldn't say slow, but
`[00:53:32]` auto completely autonomous driving is a
`[00:53:34]` auto completely autonomous driving is a
`[00:53:34]` hard problem. It's not as easy as people
`[00:53:36]` hard problem. It's not as easy as people
`[00:53:36]` thought initially.
`[00:53:38]` thought initially.
`[00:53:38]` Okay. So, um
`[00:53:40]` Okay. So, um
`[00:53:40]` Jeff uh kind of brushed away
`[00:53:42]` Jeff uh kind of brushed away
`[00:53:42]` reinforcement learning. But,
`[00:53:43]` reinforcement learning. But,
`[00:53:43]` reinforcement learning is something that
`[00:53:44]` reinforcement learning is something that
`[00:53:44]` a lot of people are really excited
`[00:53:45]` a lot of people are really excited
`[00:53:45]` about, particularly people at DeepMind.
`[00:53:48]` about, particularly people at DeepMind.
`[00:53:48]` Um but, there is a problem with the
`[00:53:49]` Um but, there is a problem with the
`[00:53:49]` current crop of reinforcement learning,
`[00:53:51]` current crop of reinforcement learning,
`[00:53:51]` which is that it's extremely data
`[00:53:52]` which is that it's extremely data
`[00:53:52]` inefficient. If you want to train a
`[00:53:54]` inefficient. If you want to train a
`[00:53:54]` system to do anything using
`[00:53:55]` system to do anything using
`[00:53:55]` reinforcement learning, it will have to
`[00:53:57]` reinforcement learning, it will have to
`[00:53:57]` do lots and lots of trial and errors.
`[00:53:59]` do lots and lots of trial and errors.
`[00:54:00]` So, for example, to get a machine to
`[00:54:01]` So, for example, to get a machine to
`[00:54:01]` play Atari games, classic Atari games,
`[00:54:04]` play Atari games, classic Atari games,
`[00:54:04]` to the level that any human can reach in
`[00:54:07]` to the level that any human can reach in
`[00:54:07]` about 15 minutes of training,
`[00:54:09]` about 15 minutes of training,
`[00:54:09]` uh the machine will have to play the
`[00:54:11]` uh the machine will have to play the
`[00:54:11]` equivalent of 80 hours of of real-time
`[00:54:14]` equivalent of 80 hours of of real-time
`[00:54:14]` play.
`[00:54:15]` play.
`[00:54:15]` Um
`[00:54:16]` Um
`[00:54:16]` to uh play uh Go at uh superhuman level,
`[00:54:20]` to uh play uh Go at uh superhuman level,
`[00:54:20]` it will have to to play something like
`[00:54:22]` it will have to to play something like
`[00:54:22]` 20 million games.
`[00:54:24]` 20 million games.
`[00:54:24]` To play StarCraft, this is a recent
`[00:54:26]` To play StarCraft, this is a recent
`[00:54:26]` DeepMind uh work. Um
`[00:54:29]` DeepMind uh work. Um
`[00:54:29]` It's a blog post, not a paper. Uh the
`[00:54:31]` It's a blog post, not a paper. Uh the
`[00:54:31]` AlphaStar system
`[00:54:32]` AlphaStar system
`[00:54:32]` uh took the equivalent of 200 years of
`[00:54:35]` uh took the equivalent of 200 years of
`[00:54:35]` uh real-time play to reach uh human
`[00:54:37]` uh real-time play to reach uh human
`[00:54:37]` level
`[00:54:39]` level
`[00:54:39]` on a single map for kind of a single
`[00:54:41]` on a single map for kind of a single
`[00:54:41]` type of player.
`[00:54:43]` type of player.
`[00:54:43]` Um by the way, all those systems use
`[00:54:44]` Um by the way, all those systems use
`[00:54:44]` conv nets and various other things, but
`[00:54:46]` conv nets and various other things, but
`[00:54:46]` uh that's an interesting
`[00:54:49]` uh that's an interesting
`[00:54:49]` thing. So, the problem with
`[00:54:50]` thing. So, the problem with
`[00:54:50]` reinforcement learning is that those
`[00:54:52]` reinforcement learning is that those
`[00:54:52]` those models have to try something to to
`[00:54:54]` those models have to try something to to
`[00:54:54]` know if it's going to work. And it's
`[00:54:56]` know if it's going to work. And it's
`[00:54:56]` really not practical to use in the real
`[00:54:58]` really not practical to use in the real
`[00:54:58]` world if you want to train a robot to
`[00:55:00]` world if you want to train a robot to
`[00:55:00]` grasp uh things or you want to train a
`[00:55:03]` grasp uh things or you want to train a
`[00:55:03]` car to drive itself.
`[00:55:04]` car to drive itself.
`[00:55:04]` So, you know, to figure out um
`[00:55:08]` So, you know, to figure out um
`[00:55:08]` to train a system to drive a car so it
`[00:55:10]` to train a system to drive a car so it
`[00:55:10]` doesn't run off cliffs,
`[00:55:12]` doesn't run off cliffs,
`[00:55:12]` it will actually have to drive through
`[00:55:15]` it will actually have to drive through
`[00:55:15]` you know, it will actually have to run
`[00:55:16]` you know, it will actually have to run
`[00:55:16]` off a cliff multiple times before it
`[00:55:18]` off a cliff multiple times before it
`[00:55:18]` figures out how not to do that.
`[00:55:21]` figures out how not to do that.
`[00:55:21]` First of all, to figure out it's a bad
`[00:55:23]` First of all, to figure out it's a bad
`[00:55:23]` idea, and second, to figure out how not
`[00:55:25]` idea, and second, to figure out how not
`[00:55:25]` to do it.
`[00:55:26]` to do it.
`[00:55:26]` Because it doesn't have a model of the
`[00:55:27]` Because it doesn't have a model of the
`[00:55:27]` world. It doesn't It can't imagine
`[00:55:28]` world. It doesn't It can't imagine
`[00:55:28]` what's going to happen before it
`[00:55:30]` what's going to happen before it
`[00:55:30]` happens. It has to try things to correct
`[00:55:32]` happens. It has to try things to correct
`[00:55:32]` itself. That's why it's so inefficient.
`[00:55:35]` itself. That's why it's so inefficient.
`[00:55:35]` So, that begs the question, how is it
`[00:55:37]` So, that begs the question, how is it
`[00:55:37]` that humans and animals can learn so
`[00:55:39]` that humans and animals can learn so
`[00:55:39]` efficiently, so quickly? We can learn to
`[00:55:41]` efficiently, so quickly? We can learn to
`[00:55:41]` drive a car. Most of us can learn to
`[00:55:42]` drive a car. Most of us can learn to
`[00:55:42]` drive a car in about 20 hours of
`[00:55:44]` drive a car in about 20 hours of
`[00:55:44]` training with hardly any accident.
`[00:55:46]` training with hardly any accident.
`[00:55:46]` How does that happen?
`[00:55:48]` How does that happen?
`[00:55:48]` We don't run off cliffs because we have
`[00:55:50]` We don't run off cliffs because we have
`[00:55:50]` a pretty good intuitive physics model
`[00:55:52]` a pretty good intuitive physics model
`[00:55:52]` that tells us if I turn if I'm driving
`[00:55:54]` that tells us if I turn if I'm driving
`[00:55:54]` next to a cliff and I'm turning the
`[00:55:55]` next to a cliff and I'm turning the
`[00:55:55]` wheel to the right,
`[00:55:56]` wheel to the right,
`[00:55:57]` the car is going to run off the cliff,
`[00:55:58]` the car is going to run off the cliff,
`[00:55:58]` it's going to fall, and nothing good is
`[00:56:00]` it's going to fall, and nothing good is
`[00:56:00]` going to come out of this. Okay.
`[00:56:02]` going to come out of this. Okay.
`[00:56:02]` So, we have this internal model. And the
`[00:56:04]` So, we have this internal model. And the
`[00:56:04]` question is, how do we learn this
`[00:56:05]` question is, how do we learn this
`[00:56:06]` internal model? And then and the next
`[00:56:07]` internal model? And then and the next
`[00:56:07]` question is, how do we get machines to
`[00:56:09]` question is, how do we get machines to
`[00:56:09]` learn internal models like that?
`[00:56:11]` learn internal models like that?
`[00:56:11]` Basically, just by observation.
`[00:56:14]` So, there is a
`[00:56:16]` um
`[00:56:17]` um
`[00:56:17]` gentleman called Emmanuel Dupoux in
`[00:56:19]` gentleman called Emmanuel Dupoux in
`[00:56:19]` Paris is a developmental uh
`[00:56:21]` Paris is a developmental uh
`[00:56:21]` psychologist. Um he works actually on
`[00:56:23]` psychologist. Um he works actually on
`[00:56:23]` how children learn language and speech
`[00:56:25]` how children learn language and speech
`[00:56:25]` and things like that, but also other
`[00:56:27]` and things like that, but also other
`[00:56:27]` concepts. And he made this chart about
`[00:56:29]` concepts. And he made this chart about
`[00:56:29]` the time uh the the age in months at
`[00:56:32]` the time uh the the age in months at
`[00:56:32]` which babies learn basic concepts, like
`[00:56:34]` which babies learn basic concepts, like
`[00:56:34]` things like uh distinguishing animate
`[00:56:36]` things like uh distinguishing animate
`[00:56:36]` objects from inanimate objects. That
`[00:56:38]` objects from inanimate objects. That
`[00:56:38]` happens really quickly around 3 months
`[00:56:40]` happens really quickly around 3 months
`[00:56:40]` old.
`[00:56:41]` old.
`[00:56:41]` Uh the fact that uh some objects are are
`[00:56:44]` Uh the fact that uh some objects are are
`[00:56:44]` stable, some of them will fall.
`[00:56:46]` stable, some of them will fall.
`[00:56:46]` Uh and you can sort of measure whether
`[00:56:48]` Uh and you can sort of measure whether
`[00:56:48]` babies are surprised by the behavior of
`[00:56:50]` babies are surprised by the behavior of
`[00:56:50]` some objects.
`[00:56:52]` some objects.
`[00:56:52]` And then it takes about 9 months for
`[00:56:54]` And then it takes about 9 months for
`[00:56:54]` babies to figure out that objects that
`[00:56:56]` babies to figure out that objects that
`[00:56:56]` are not supported will fall.
`[00:56:58]` are not supported will fall.
`[00:56:58]` Basically, gravity.
`[00:57:00]` Basically, gravity.
`[00:57:00]` So, if
`[00:57:02]` So, if
`[00:57:03]` you show a 6-month ba- a 6-month-old
`[00:57:05]` you show a 6-month ba- a 6-month-old
`[00:57:05]` baby the
`[00:57:06]` baby the
`[00:57:06]` the the scenario on the top left where
`[00:57:08]` the the scenario on the top left where
`[00:57:08]` there's a little car on the platform and
`[00:57:10]` there's a little car on the platform and
`[00:57:10]` you push the little car off the platform
`[00:57:11]` you push the little car off the platform
`[00:57:11]` and the car doesn't fall. It's a trick.
`[00:57:14]` and the car doesn't fall. It's a trick.
`[00:57:14]` Babies 6 months old don't even pay
`[00:57:16]` Babies 6 months old don't even pay
`[00:57:16]` attention. That's just another thing
`[00:57:17]` attention. That's just another thing
`[00:57:17]` that the world throws at them that they
`[00:57:20]` that the world throws at them that they
`[00:57:20]` you know, they have to learn.
`[00:57:22]` you know, they have to learn.
`[00:57:22]` It's fine.
`[00:57:23]` It's fine.
`[00:57:23]` A 9-month-old baby
`[00:57:24]` A 9-month-old baby
`[00:57:25]` will go like the little girl at the
`[00:57:26]` will go like the little girl at the
`[00:57:26]` bottom left.
`[00:57:28]` bottom left.
`[00:57:28]` Be very very surprised. In the meantime,
`[00:57:31]` Be very very surprised. In the meantime,
`[00:57:31]` they've learned the concept of gravity.
`[00:57:33]` they've learned the concept of gravity.
`[00:57:33]` And nobody has really told them what
`[00:57:35]` And nobody has really told them what
`[00:57:35]` gravity is. They've just kind of
`[00:57:36]` gravity is. They've just kind of
`[00:57:36]` observed the world and they they figured
`[00:57:37]` observed the world and they they figured
`[00:57:37]` out objects that are not supported just
`[00:57:39]` out objects that are not supported just
`[00:57:39]` fall. And so, when that doesn't happen,
`[00:57:41]` fall. And so, when that doesn't happen,
`[00:57:41]` they get surprised.
`[00:57:43]` they get surprised.
`[00:57:43]` How does that happen?
`[00:57:45]` How does that happen?
`[00:57:45]` It's not just humans. Animals have those
`[00:57:46]` It's not just humans. Animals have those
`[00:57:47]` models, too. You know, cats, dogs,
`[00:57:49]` models, too. You know, cats, dogs,
`[00:57:49]` rats,
`[00:57:51]` rats,
`[00:57:51]` orangutans. So, here is a baby orangutan
`[00:57:53]` orangutans. So, here is a baby orangutan
`[00:57:53]` here is being shown a magic trick. Put
`[00:57:55]` here is being shown a magic trick. Put
`[00:57:55]` an object in a cup.
`[00:57:57]` an object in a cup.
`[00:57:57]` Um
`[00:57:58]` Um
`[00:57:58]` remove the object, but he doesn't see
`[00:57:59]` remove the object, but he doesn't see
`[00:57:59]` that.
`[00:58:00]` that.
`[00:58:00]` Then,
`[00:58:02]` Then,
`[00:58:02]` show the cup. It's empty.
`[00:58:05]` show the cup. It's empty.
`[00:58:05]` He was on the floor laughing.
`[00:58:08]` So, his model of the world was violated,
`[00:58:11]` right? He has a pretty good model of the
`[00:58:13]` right? He has a pretty good model of the
`[00:58:13]` world. Object permanence, that's a very
`[00:58:14]` world. Object permanence, that's a very
`[00:58:14]` basic concept. Objects are not supposed
`[00:58:16]` basic concept. Objects are not supposed
`[00:58:16]` to disappear like that.
`[00:58:18]` to disappear like that.
`[00:58:18]` Um and when your model of the world is
`[00:58:21]` Um and when your model of the world is
`[00:58:21]` being violated,
`[00:58:23]` being violated,
`[00:58:23]` you pay attention because you're going
`[00:58:24]` you pay attention because you're going
`[00:58:24]` to learn something about the world you
`[00:58:25]` to learn something about the world you
`[00:58:25]` didn't know.
`[00:58:27]` didn't know.
`[00:58:27]` Uh
`[00:58:28]` Uh
`[00:58:28]` if it really violates a very basic thing
`[00:58:29]` if it really violates a very basic thing
`[00:58:29]` about the world,
`[00:58:31]` about the world,
`[00:58:31]` it's funny.
`[00:58:33]` it's funny.
`[00:58:33]` Uh but, it's also it might be dangerous,
`[00:58:35]` Uh but, it's also it might be dangerous,
`[00:58:35]` right? It might It's something that can
`[00:58:36]` right? It might It's something that can
`[00:58:36]` kill you cuz you you just didn't predict
`[00:58:38]` kill you cuz you you just didn't predict
`[00:58:38]` what's
`[00:58:39]` what's
`[00:58:39]` uh what what just happened.
`[00:58:41]` uh what what just happened.
`[00:58:41]` Okay. So, what's the salvation? Really,
`[00:58:42]` Okay. So, what's the salvation? Really,
`[00:58:43]` you know, how do we get machines to
`[00:58:44]` you know, how do we get machines to
`[00:58:44]` learn this this kind of stuff?
`[00:58:46]` learn this this kind of stuff?
`[00:58:46]` You know, learn all the huge amount of
`[00:58:48]` You know, learn all the huge amount of
`[00:58:48]` background knowledge we learn about the
`[00:58:49]` background knowledge we learn about the
`[00:58:49]` world by just observing in the first few
`[00:58:51]` world by just observing in the first few
`[00:58:51]` months of life.
`[00:58:52]` months of life.
`[00:58:52]` Uh and animals do this, too.
`[00:58:54]` Uh and animals do this, too.
`[00:58:54]` So, for example, if I ask you um
`[00:58:57]` So, for example, if I ask you um
`[00:58:57]` if I train myself to predict what the
`[00:59:00]` if I train myself to predict what the
`[00:59:00]` world is going to look like when I move
`[00:59:01]` world is going to look like when I move
`[00:59:01]` my head slightly to the left,
`[00:59:04]` my head slightly to the left,
`[00:59:04]` because of
`[00:59:05]` because of
`[00:59:05]` parallax motion,
`[00:59:07]` parallax motion,
`[00:59:07]` objects that are nearby and objects that
`[00:59:09]` objects that are nearby and objects that
`[00:59:09]` are far away won't move
`[00:59:12]` are far away won't move
`[00:59:12]` uh the same way relative to
`[00:59:14]` uh the same way relative to
`[00:59:14]` you know, my my uh my viewpoint.
`[00:59:17]` you know, my my uh my viewpoint.
`[00:59:17]` And so,
`[00:59:18]` And so,
`[00:59:18]` the best way to predict how the world is
`[00:59:21]` the best way to predict how the world is
`[00:59:21]` going to look when I move my head is to
`[00:59:24]` going to look when I move my head is to
`[00:59:24]` basically represent internally the
`[00:59:26]` basically represent internally the
`[00:59:26]` notion of depth.
`[00:59:28]` notion of depth.
`[00:59:28]` And conse- consequently, sort of
`[00:59:30]` And conse- consequently, sort of
`[00:59:30]` conversely, if I train a system to
`[00:59:33]` conversely, if I train a system to
`[00:59:33]` predict what the world what the world is
`[00:59:34]` predict what the world what the world is
`[00:59:34]` going to look like
`[00:59:36]` going to look like
`[00:59:36]` when it moves its camera,
`[00:59:37]` when it moves its camera,
`[00:59:37]` maybe it's going to learn the notion of
`[00:59:39]` maybe it's going to learn the notion of
`[00:59:39]` depth automatically.
`[00:59:40]` depth automatically.
`[00:59:40]` And once you have depth, you have
`[00:59:41]` And once you have depth, you have
`[00:59:41]` objects because you have objects in
`[00:59:42]` objects because you have objects in
`[00:59:43]` front of others, you have occlusion
`[00:59:44]` front of others, you have occlusion
`[00:59:44]` edges. Once you have objects, you have,
`[00:59:46]` edges. Once you have objects, you have,
`[00:59:46]` you know, things you can influence and
`[00:59:48]` you know, things you can influence and
`[00:59:48]` things that can move independently of
`[00:59:49]` things that can move independently of
`[00:59:49]` others and things like that. So,
`[00:59:51]` others and things like that. So,
`[00:59:51]` concepts can kind of build on top of
`[00:59:52]` concepts can kind of build on top of
`[00:59:52]` each other each other like this through
`[00:59:55]` each other each other like this through
`[00:59:55]` uh
`[00:59:55]` uh
`[00:59:55]` prediction.
`[00:59:57]` prediction.
`[00:59:57]` So, that's the idea of self-supervised
`[00:59:58]` So, that's the idea of self-supervised
`[00:59:59]` learning. It's prediction and
`[01:00:00]` learning. It's prediction and
`[01:00:00]` reconstruction.
`[01:00:01]` reconstruction.
`[01:00:01]` I give the machine a piece of data,
`[01:00:04]` I give the machine a piece of data,
`[01:00:04]` let's say a video clip. I mask a piece
`[01:00:06]` let's say a video clip. I mask a piece
`[01:00:06]` of that video clip,
`[01:00:08]` of that video clip,
`[01:00:08]` and I ask the system to predict the
`[01:00:10]` and I ask the system to predict the
`[01:00:10]` missing part from the part that it it
`[01:00:12]` missing part from the part that it it
`[01:00:12]` can observe.
`[01:00:14]` can observe.
`[01:00:14]` Okay, so that would be video prediction,
`[01:00:15]` Okay, so that would be video prediction,
`[01:00:15]` just predict the future.
`[01:00:17]` just predict the future.
`[01:00:17]` Um but the more general form of
`[01:00:19]` Um but the more general form of
`[01:00:19]` self-supervised learning is I don't
`[01:00:20]` self-supervised learning is I don't
`[01:00:21]` specify in advance which part I'm going
`[01:00:22]` specify in advance which part I'm going
`[01:00:22]` to mask or not. Uh I'm just going to
`[01:00:24]` to mask or not. Uh I'm just going to
`[01:00:24]` tell the system I'm going to mask a
`[01:00:25]` tell the system I'm going to mask a
`[01:00:25]` piece of it and whatever is masked, you
`[01:00:27]` piece of it and whatever is masked, you
`[01:00:27]` I'm asking you to re- reconstruct it.
`[01:00:31]` And in fact, I may not even mask it at
`[01:00:33]` all. I'm just going to
`[01:00:35]` all. I'm just going to
`[01:00:35]` virtually mask it and just ask the
`[01:00:37]` virtually mask it and just ask the
`[01:00:37]` system to reconstruct the input under
`[01:00:39]` system to reconstruct the input under
`[01:00:39]` certain constraints.
`[01:00:40]` certain constraints.
`[01:00:41]` So, the advantage of this
`[01:00:41]` So, the advantage of this
`[01:00:41]` self-supervised learning is that it's
`[01:00:43]` self-supervised learning is that it's
`[01:00:43]` not task dependent. You get the machine
`[01:00:44]` not task dependent. You get the machine
`[01:00:44]` to learn about the world without
`[01:00:46]` to learn about the world without
`[01:00:46]` training it for a particular task.
`[01:00:48]` training it for a particular task.
`[01:00:48]` And so, it can learn just by observation
`[01:00:49]` And so, it can learn just by observation
`[01:00:49]` without having to interact with the
`[01:00:50]` without having to interact with the
`[01:00:50]` world, which is much more efficient. But
`[01:00:52]` world, which is much more efficient. But
`[01:00:52]` more importantly, you're asking the
`[01:00:53]` more importantly, you're asking the
`[01:00:54]` system to predict a lot of stuff.
`[01:00:56]` system to predict a lot of stuff.
`[01:00:56]` Not just
`[01:00:58]` Not just
`[01:00:58]` a a value function like in reinforcement
`[01:01:00]` a a value function like in reinforcement
`[01:01:00]` learning where basically the only thing
`[01:01:01]` learning where basically the only thing
`[01:01:01]` you give the machine to predict is a
`[01:01:03]` you give the machine to predict is a
`[01:01:03]` scalar value once in a while.
`[01:01:05]` scalar value once in a while.
`[01:01:05]` Not reinforcement not uh supervised
`[01:01:07]` Not reinforcement not uh supervised
`[01:01:07]` learning where you ask the system to
`[01:01:09]` learning where you ask the system to
`[01:01:09]` predict a label, which is a few bits.
`[01:01:12]` predict a label, which is a few bits.
`[01:01:12]` In the case of self-supervised learning,
`[01:01:13]` In the case of self-supervised learning,
`[01:01:13]` you're asking the machine to predict a
`[01:01:15]` you're asking the machine to predict a
`[01:01:15]` lot of stuff.
`[01:01:18]` And so, that led me to this slightly
`[01:01:19]` obnoxious analogy, at least for people
`[01:01:21]` obnoxious analogy, at least for people
`[01:01:21]` working on reinforcement learning, um
`[01:01:23]` working on reinforcement learning, um
`[01:01:23]` which is the idea that if intelligence
`[01:01:25]` which is the idea that if intelligence
`[01:01:25]` or learning is a is a cake,
`[01:01:28]` or learning is a is a cake,
`[01:01:28]` the bulk of the cake, the genoise as we
`[01:01:30]` the bulk of the cake, the genoise as we
`[01:01:30]` say in French,
`[01:01:31]` say in French,
`[01:01:31]` uh is really self-supervised learning.
`[01:01:33]` uh is really self-supervised learning.
`[01:01:33]` Most of what we learn, most of the
`[01:01:34]` Most of what we learn, most of the
`[01:01:34]` knowledge we accumulate about the world
`[01:01:36]` knowledge we accumulate about the world
`[01:01:36]` is learned through self-supervised
`[01:01:37]` is learned through self-supervised
`[01:01:37]` learning.
`[01:01:38]` learning.
`[01:01:38]` Um there's a little bit of icing on the
`[01:01:40]` Um there's a little bit of icing on the
`[01:01:40]` cake, which is supervised learning,
`[01:01:42]` cake, which is supervised learning,
`[01:01:42]` where, you know, being shown a picture
`[01:01:43]` where, you know, being shown a picture
`[01:01:43]` book and we're being told the name of
`[01:01:44]` book and we're being told the name of
`[01:01:44]` objects, and with just a few examples,
`[01:01:47]` objects, and with just a few examples,
`[01:01:47]` we can uh know what the objects are. Um
`[01:01:50]` we can uh know what the objects are. Um
`[01:01:50]` we're we're taught the meaning of some
`[01:01:52]` we're we're taught the meaning of some
`[01:01:52]` words, and you know, babies can learn uh
`[01:01:56]` words, and you know, babies can learn uh
`[01:01:56]` young young children can learn
`[01:01:58]` young young children can learn
`[01:01:58]` many, many words per day.
`[01:02:00]` many, many words per day.
`[01:02:00]` New words.
`[01:02:02]` New words.
`[01:02:02]` And then the cherry on the cake is
`[01:02:03]` And then the cherry on the cake is
`[01:02:03]` reinforcement learning. It's it's a very
`[01:02:04]` reinforcement learning. It's it's a very
`[01:02:04]` small amount of of information you're
`[01:02:06]` small amount of of information you're
`[01:02:06]` asking the machine to predict, and so
`[01:02:07]` asking the machine to predict, and so
`[01:02:07]` there's no way that the machine can
`[01:02:09]` there's no way that the machine can
`[01:02:09]` learn purely from from that form of
`[01:02:12]` learn purely from from that form of
`[01:02:12]` learning. It has to be a combination of
`[01:02:14]` learning. It has to be a combination of
`[01:02:14]` uh
`[01:02:16]` uh
`[01:02:16]` probably all three forms of learning,
`[01:02:17]` probably all three forms of learning,
`[01:02:17]` but but principally um self-supervised
`[01:02:19]` but but principally um self-supervised
`[01:02:20]` learning. This idea is not new. A lot of
`[01:02:22]` learning. This idea is not new. A lot of
`[01:02:22]` people have argued for the idea of
`[01:02:23]` people have argued for the idea of
`[01:02:23]` prediction for
`[01:02:25]` prediction for
`[01:02:25]` uh for learning, the idea of uh learning
`[01:02:27]` uh for learning, the idea of uh learning
`[01:02:27]` models, um predictive models.
`[01:02:30]` models, um predictive models.
`[01:02:30]` And uh
`[01:02:31]` And uh
`[01:02:31]` uh one one such person is is Jeff, as a
`[01:02:34]` uh one one such person is is Jeff, as a
`[01:02:34]` matter of fact. This is a quote from
`[01:02:36]` matter of fact. This is a quote from
`[01:02:36]` from him, uh
`[01:02:37]` from him, uh
`[01:02:37]` which, you know, this is from a few
`[01:02:39]` which, you know, this is from a few
`[01:02:39]` years ago, but he's been saying this for
`[01:02:40]` years ago, but he's been saying this for
`[01:02:40]` about 40 years,
`[01:02:41]` about 40 years,
`[01:02:41]` at least for
`[01:02:43]` at least for
`[01:02:43]` longer than I've known him.
`[01:02:46]` longer than I've known him.
`[01:02:46]` Um and and it goes like this, "The brain
`[01:02:48]` Um and and it goes like this, "The brain
`[01:02:48]` has about 10 to the 14th synapses, and
`[01:02:49]` has about 10 to the 14th synapses, and
`[01:02:49]` we only live about uh 10 to the 9th
`[01:02:51]` we only live about uh 10 to the 9th
`[01:02:51]` seconds. So, we have a lot more
`[01:02:53]` seconds. So, we have a lot more
`[01:02:53]` parameters than data. This motivates the
`[01:02:55]` parameters than data. This motivates the
`[01:02:55]` idea that we must do a lot of
`[01:02:56]` idea that we must do a lot of
`[01:02:56]` unsupervised learning or self-supervised
`[01:02:58]` unsupervised learning or self-supervised
`[01:02:58]` learning, since the perceptual input,
`[01:02:59]` learning, since the perceptual input,
`[01:02:59]` including proprioception,
`[01:03:01]` including proprioception,
`[01:03:01]` is the only place where we can get 10 to
`[01:03:03]` is the only place where we can get 10 to
`[01:03:03]` the 50 dimensions of constraints per
`[01:03:04]` the 50 dimensions of constraints per
`[01:03:04]` second."
`[01:03:06]` second."
`[01:03:06]` If you're asked to predict everything
`[01:03:08]` If you're asked to predict everything
`[01:03:08]` that comes into your sense your your
`[01:03:09]` that comes into your sense your your
`[01:03:09]` your your senses,
`[01:03:11]` your your senses,
`[01:03:11]` uh you know, every fraction of a second,
`[01:03:13]` uh you know, every fraction of a second,
`[01:03:13]` that's a lot of information you have to
`[01:03:15]` that's a lot of information you have to
`[01:03:15]` learn, and that
`[01:03:16]` learn, and that
`[01:03:16]` might be enough to constrain all the
`[01:03:18]` might be enough to constrain all the
`[01:03:18]` synapses we have in our brain to learn
`[01:03:20]` synapses we have in our brain to learn
`[01:03:20]` things that are meaningful.
`[01:03:23]` things that are meaningful.
`[01:03:23]` So,
`[01:03:24]` So,
`[01:03:24]` the sequel of deep learning,
`[01:03:26]` the sequel of deep learning,
`[01:03:26]` uh in my opinion, is self-supervised
`[01:03:28]` uh in my opinion, is self-supervised
`[01:03:28]` learning. And in fact, historically, as
`[01:03:29]` learning. And in fact, historically, as
`[01:03:29]` Jeff has mentioned,
`[01:03:31]` Jeff has mentioned,
`[01:03:31]` the the the sort of deep learning
`[01:03:33]` the the the sort of deep learning
`[01:03:33]` conspiracy that that Yoshua, Jeff, and I
`[01:03:36]` conspiracy that that Yoshua, Jeff, and I
`[01:03:36]` started in the early 2000s was focused
`[01:03:39]` started in the early 2000s was focused
`[01:03:39]` on unsupervised learning, unsupervised
`[01:03:42]` on unsupervised learning, unsupervised
`[01:03:42]` pre-training. And it was partly
`[01:03:43]` pre-training. And it was partly
`[01:03:43]` successful, but we kind of put it
`[01:03:47]` successful, but we kind of put it
`[01:03:47]` uh on the back burner for a while, and
`[01:03:49]` uh on the back burner for a while, and
`[01:03:49]` it's coming back to the fore now.
`[01:03:51]` it's coming back to the fore now.
`[01:03:51]` It's going to create a new revolution,
`[01:03:52]` It's going to create a new revolution,
`[01:03:52]` at least that's my prediction.
`[01:03:54]` at least that's my prediction.
`[01:03:54]` And the next the revolution will not be
`[01:03:56]` And the next the revolution will not be
`[01:03:56]` supervised.
`[01:03:58]` supervised.
`[01:03:58]` So, I have to thank uh Alyosha Efros for
`[01:04:01]` So, I have to thank uh Alyosha Efros for
`[01:04:01]` this slogan. He invented it.
`[01:04:03]` this slogan. He invented it.
`[01:04:03]` Uh of of course, he got inspired by Gil
`[01:04:05]` Uh of of course, he got inspired by Gil
`[01:04:05]` Scott-Heron, you know, the the
`[01:04:07]` Scott-Heron, you know, the the
`[01:04:07]` revolution will not be televised.
`[01:04:09]` revolution will not be televised.
`[01:04:09]` You can even get a t-shirt with it now.
`[01:04:10]` You can even get a t-shirt with it now.
`[01:04:11]` Um
`[01:04:14]` So, what is self-supervised learning
`[01:04:15]` really? Self-supervised learning is
`[01:04:17]` really? Self-supervised learning is
`[01:04:17]` filling in the blanks.
`[01:04:19]` filling in the blanks.
`[01:04:19]` Uh and it works really well for natural
`[01:04:20]` Uh and it works really well for natural
`[01:04:20]` language processing. So, natural
`[01:04:22]` language processing. So, natural
`[01:04:22]` language processing uh
`[01:04:24]` language processing uh
`[01:04:24]` method has become standard over the last
`[01:04:26]` method has become standard over the last
`[01:04:26]` year
`[01:04:27]` year
`[01:04:27]` uh in models like BERT and and others is
`[01:04:29]` uh in models like BERT and and others is
`[01:04:29]` you take a a long uh
`[01:04:32]` you take a a long uh
`[01:04:32]` sequence of words extracted from a
`[01:04:33]` sequence of words extracted from a
`[01:04:33]` corpus of of text. You blank out uh some
`[01:04:37]` corpus of of text. You blank out uh some
`[01:04:37]` proportion of the words,
`[01:04:40]` proportion of the words,
`[01:04:40]` and you train a very large neural net
`[01:04:42]` and you train a very large neural net
`[01:04:42]` based on those transformer architectures
`[01:04:43]` based on those transformer architectures
`[01:04:43]` or various other architectures to
`[01:04:45]` or various other architectures to
`[01:04:45]` predict the missing words.
`[01:04:47]` predict the missing words.
`[01:04:47]` And in fact, it cannot exactly predict
`[01:04:48]` And in fact, it cannot exactly predict
`[01:04:48]` the missing words, so you're asking it
`[01:04:50]` the missing words, so you're asking it
`[01:04:50]` to predict a distribution over the
`[01:04:51]` to predict a distribution over the
`[01:04:51]` entire vocabulary for the probability
`[01:04:54]` entire vocabulary for the probability
`[01:04:54]` that every you know, each word may may
`[01:04:56]` that every you know, each word may may
`[01:04:56]` occur uh at those locations.
`[01:04:59]` occur uh at those locations.
`[01:04:59]` Um so, that's called that's a special
`[01:05:01]` Um so, that's called that's a special
`[01:05:01]` case of what we call a masked
`[01:05:02]` case of what we call a masked
`[01:05:02]` autoencoder. Okay, given an input, ask
`[01:05:04]` autoencoder. Okay, given an input, ask
`[01:05:04]` ask it to reconstruct with this part of
`[01:05:06]` ask it to reconstruct with this part of
`[01:05:06]` input that are not there's not present.
`[01:05:09]` input that are not there's not present.
`[01:05:09]` People have been trying to do this in
`[01:05:10]` People have been trying to do this in
`[01:05:10]` the context of image recognition as
`[01:05:12]` the context of image recognition as
`[01:05:12]` well. There's there's various attempts
`[01:05:13]` well. There's there's various attempts
`[01:05:13]` at doing this. So, uh this is work from
`[01:05:16]` at doing this. So, uh this is work from
`[01:05:16]` uh Pathak et al. uh from a few years ago
`[01:05:18]` uh Pathak et al. uh from a few years ago
`[01:05:18]` where you blank out some pieces of an
`[01:05:19]` where you blank out some pieces of an
`[01:05:19]` image, and then you ask the system to
`[01:05:21]` image, and then you ask the system to
`[01:05:21]` fill it to fill them in.
`[01:05:23]` fill it to fill them in.
`[01:05:23]` And it's only partially successful, not
`[01:05:25]` And it's only partially successful, not
`[01:05:25]` nearly as successful as in the context
`[01:05:27]` nearly as successful as in the context
`[01:05:27]` of natural language processing. So,
`[01:05:28]` of natural language processing. So,
`[01:05:28]` natural language processing, there's
`[01:05:30]` natural language processing, there's
`[01:05:30]` been a revolution over the last year of
`[01:05:32]` been a revolution over the last year of
`[01:05:32]` using those pre-training systems for
`[01:05:35]` using those pre-training systems for
`[01:05:35]` natural language understanding,
`[01:05:36]` natural language understanding,
`[01:05:36]` translation, all kinds of stuff, and the
`[01:05:38]` translation, all kinds of stuff, and the
`[01:05:38]` performance is amazing. It They're very,
`[01:05:40]` performance is amazing. It They're very,
`[01:05:40]` very big models, but the performance
`[01:05:41]` very big models, but the performance
`[01:05:41]` really works really well.
`[01:05:43]` really works really well.
`[01:05:43]` And there were sort of early indications
`[01:05:44]` And there were sort of early indications
`[01:05:44]` of this uh in work that uh
`[01:05:47]` of this uh in work that uh
`[01:05:48]` uh Yoshua Bengio did uh a long time ago
`[01:05:50]` uh Yoshua Bengio did uh a long time ago
`[01:05:50]` in the '90s, and uh Ronald J. Williams
`[01:05:52]` in the '90s, and uh Ronald J. Williams
`[01:05:52]` and Western did in the
`[01:05:54]` and Western did in the
`[01:05:54]` um
`[01:05:55]` um
`[01:05:55]` around 2010
`[01:05:57]` around 2010
`[01:05:57]` uh in the using neural nets for NLP.
`[01:06:00]` uh in the using neural nets for NLP.
`[01:06:00]` And then more recent work, word2vec,
`[01:06:01]` And then more recent work, word2vec,
`[01:06:01]` fastText, etc., which use this idea of
`[01:06:03]` fastText, etc., which use this idea of
`[01:06:03]` predicting words from their context,
`[01:06:05]` predicting words from their context,
`[01:06:05]` basically.
`[01:06:06]` basically.
`[01:06:06]` But really, it's sort of the this this
`[01:06:08]` But really, it's sort of the this this
`[01:06:08]` whole idea has completely taken off. So,
`[01:06:10]` whole idea has completely taken off. So,
`[01:06:10]` why does it work for natural natural
`[01:06:12]` why does it work for natural natural
`[01:06:12]` language processing, and why does it not
`[01:06:14]` language processing, and why does it not
`[01:06:14]` work so well for for in the context of
`[01:06:16]` work so well for for in the context of
`[01:06:16]` images and vision?
`[01:06:19]` images and vision?
`[01:06:19]` I think it's because of the sort of
`[01:06:22]` I think it's because of the sort of
`[01:06:22]` how we
`[01:06:23]` how we
`[01:06:23]` represent uncertainty or how we do not
`[01:06:25]` represent uncertainty or how we do not
`[01:06:25]` represent uncertainty. So, let's say we
`[01:06:27]` represent uncertainty. So, let's say we
`[01:06:27]` want to do video prediction.
`[01:06:29]` want to do video prediction.
`[01:06:29]` We um
`[01:06:30]` We um
`[01:06:30]` we have short video clips with a few
`[01:06:32]` we have short video clips with a few
`[01:06:32]` frames, in this case here, a little girl
`[01:06:34]` frames, in this case here, a little girl
`[01:06:34]` approaching a birthday cake.
`[01:06:36]` approaching a birthday cake.
`[01:06:36]` And then we ask the machine to predict
`[01:06:38]` And then we ask the machine to predict
`[01:06:38]` the next few frames in the video.
`[01:06:40]` the next few frames in the video.
`[01:06:40]` Uh if you train a a large neural net to
`[01:06:42]` Uh if you train a a large neural net to
`[01:06:42]` predict the next few frames you using
`[01:06:44]` predict the next few frames you using
`[01:06:44]` least squared error, you know, squared
`[01:06:46]` least squared error, you know, squared
`[01:06:46]` error,
`[01:06:47]` error,
`[01:06:47]` um what you get are blurry predictions.
`[01:06:50]` um what you get are blurry predictions.
`[01:06:50]` Why? Because the system cannot exactly
`[01:06:53]` Why? Because the system cannot exactly
`[01:06:53]` predict what's going to happen, and so
`[01:06:54]` predict what's going to happen, and so
`[01:06:54]` it
`[01:06:55]` it
`[01:06:55]` the best thing it can do is predict the
`[01:06:56]` the best thing it can do is predict the
`[01:06:56]` average of all the possible futures.
`[01:06:59]` average of all the possible futures.
`[01:06:59]` To be more concrete, let's say all the
`[01:07:00]` To be more concrete, let's say all the
`[01:07:00]` videos consist of someone putting a pen
`[01:07:02]` videos consist of someone putting a pen
`[01:07:02]` on the table and letting it go, and
`[01:07:04]` on the table and letting it go, and
`[01:07:04]` every time you repeat the experiment,
`[01:07:05]` every time you repeat the experiment,
`[01:07:05]` the pen falls in a different direction,
`[01:07:07]` the pen falls in a different direction,
`[01:07:07]` and you can't really predict in which
`[01:07:08]` and you can't really predict in which
`[01:07:08]` direction it's going to fall.
`[01:07:10]` direction it's going to fall.
`[01:07:10]` Then if you predict the average of all
`[01:07:12]` Then if you predict the average of all
`[01:07:12]` the outcomes, it would be a transparent
`[01:07:13]` the outcomes, it would be a transparent
`[01:07:13]` pen,
`[01:07:14]` pen,
`[01:07:15]` uh
`[01:07:15]` uh
`[01:07:15]` you know, superimposed on itself in all
`[01:07:17]` you know, superimposed on itself in all
`[01:07:17]` possible orientations. And that's not a
`[01:07:20]` possible orientations. And that's not a
`[01:07:20]` good prediction.
`[01:07:22]` good prediction.
`[01:07:22]` So,
`[01:07:23]` So,
`[01:07:23]` if you want a system to be able to
`[01:07:26]` if you want a system to be able to
`[01:07:26]` represent multiple predictions, it has
`[01:07:28]` represent multiple predictions, it has
`[01:07:28]` to have what's called a latent variable.
`[01:07:30]` to have what's called a latent variable.
`[01:07:30]` So, you have a function implemented by a
`[01:07:32]` So, you have a function implemented by a
`[01:07:32]` neural net. It takes the past, let's say
`[01:07:34]` neural net. It takes the past, let's say
`[01:07:34]` a few frames from a video, and it wants
`[01:07:36]` a few frames from a video, and it wants
`[01:07:36]` to predict the next few frames. It has
`[01:07:38]` to predict the next few frames. It has
`[01:07:38]` to have an extra variable here that's
`[01:07:40]` to have an extra variable here that's
`[01:07:40]` called Z, so that when you vary this
`[01:07:42]` called Z, so that when you vary this
`[01:07:42]` variable, the output varies over a
`[01:07:44]` variable, the output varies over a
`[01:07:44]` particular set of plausible predictions.
`[01:07:47]` particular set of plausible predictions.
`[01:07:47]` Okay, let's call it a latent variable
`[01:07:48]` Okay, let's call it a latent variable
`[01:07:48]` model.
`[01:07:49]` model.
`[01:07:49]` The problem with training those things
`[01:07:50]` The problem with training those things
`[01:07:50]` is that there's basically only two ways
`[01:07:52]` is that there's basically only two ways
`[01:07:52]` of training them
`[01:07:53]` of training them
`[01:07:53]` that we know about, or two kind of uh
`[01:07:55]` that we know about, or two kind of uh
`[01:07:55]` families of of uh
`[01:07:57]` families of of uh
`[01:07:57]` of ways to train those systems. One is a
`[01:07:59]` of ways to train those systems. One is a
`[01:08:00]` very cool idea from Ian Goodfellow and
`[01:08:03]` very cool idea from Ian Goodfellow and
`[01:08:03]` his collaborators at University of
`[01:08:04]` his collaborators at University of
`[01:08:04]` Montreal a few years ago called
`[01:08:05]` Montreal a few years ago called
`[01:08:05]` adversarial training or generative
`[01:08:07]` adversarial training or generative
`[01:08:07]` adversarial networks.
`[01:08:09]` adversarial networks.
`[01:08:09]` And the idea of uh
`[01:08:11]` And the idea of uh
`[01:08:11]` uh
`[01:08:12]` uh
`[01:08:12]` GANs, generative adversarial networks,
`[01:08:13]` GANs, generative adversarial networks,
`[01:08:14]` is to train a second neural net to tell
`[01:08:15]` is to train a second neural net to tell
`[01:08:15]` the first neural net whether its
`[01:08:16]` the first neural net whether its
`[01:08:16]` prediction is on this
`[01:08:18]` prediction is on this
`[01:08:18]` manifold or or set of plausible futures
`[01:08:20]` manifold or or set of plausible futures
`[01:08:20]` or not. And you train those two networks
`[01:08:22]` or not. And you train those two networks
`[01:08:22]` simultaneously.
`[01:08:24]` simultaneously.
`[01:08:24]` Um
`[01:08:26]` Um
`[01:08:26]` There's another technique that consists
`[01:08:27]` There's another technique that consists
`[01:08:27]` in sort of inferring what the ideal
`[01:08:30]` in sort of inferring what the ideal
`[01:08:30]` value of the latent variable would be to
`[01:08:31]` value of the latent variable would be to
`[01:08:31]` make a good prediction.
`[01:08:33]` make a good prediction.
`[01:08:33]` But if you do this, you have the danger
`[01:08:35]` But if you do this, you have the danger
`[01:08:35]` that the latent variable will capture
`[01:08:36]` that the latent variable will capture
`[01:08:37]` all the information there is to to
`[01:08:39]` all the information there is to to
`[01:08:39]` capture about about the prediction, and
`[01:08:41]` capture about about the prediction, and
`[01:08:41]` no information will actually be used
`[01:08:42]` no information will actually be used
`[01:08:43]` from the past to make that prediction.
`[01:08:46]` from the past to make that prediction.
`[01:08:46]` So, you have to regularize this latent
`[01:08:47]` So, you have to regularize this latent
`[01:08:47]` variable.
`[01:08:48]` variable.
`[01:08:48]` Okay, so um
`[01:08:50]` Okay, so um
`[01:08:50]` those ideas of things like um
`[01:08:53]` those ideas of things like um
`[01:08:53]` adversarial training work really well.
`[01:08:55]` adversarial training work really well.
`[01:08:55]` So, what you see here at the bottom is a
`[01:08:56]` So, what you see here at the bottom is a
`[01:08:56]` video prediction for a small a short
`[01:08:58]` video prediction for a small a short
`[01:08:58]` clip where the system has been trained
`[01:09:00]` clip where the system has been trained
`[01:09:00]` with this adversarial training.
`[01:09:01]` with this adversarial training.
`[01:09:01]` Uh and there are, you know, various ways
`[01:09:03]` Uh and there are, you know, various ways
`[01:09:03]` of doing those uh predictions, not just
`[01:09:05]` of doing those uh predictions, not just
`[01:09:05]` in pixel space, but also in the space of
`[01:09:07]` in pixel space, but also in the space of
`[01:09:07]` objects uh that have been already
`[01:09:09]` objects uh that have been already
`[01:09:09]` segmented.
`[01:09:10]` segmented.
`[01:09:10]` Um those adversarial uh generative
`[01:09:12]` Um those adversarial uh generative
`[01:09:12]` adversarial networks uh can generate
`[01:09:14]` adversarial networks uh can generate
`[01:09:14]` uh images that are used for kind of uh
`[01:09:17]` uh images that are used for kind of uh
`[01:09:17]` assistance to sort of artistic
`[01:09:18]` assistance to sort of artistic
`[01:09:18]` production. So, these are non-existing
`[01:09:21]` production. So, these are non-existing
`[01:09:21]` faces. You have a system here that's
`[01:09:22]` faces. You have a system here that's
`[01:09:22]` been trained to produce an an that looks
`[01:09:25]` been trained to produce an an that looks
`[01:09:25]` like a celebrity,
`[01:09:27]` like a celebrity,
`[01:09:27]` and after the system is trained, you
`[01:09:29]` and after the system is trained, you
`[01:09:29]` feed it a few hundred random numbers and
`[01:09:31]` feed it a few hundred random numbers and
`[01:09:31]` out comes a face that doesn't exist.
`[01:09:35]` out comes a face that doesn't exist.
`[01:09:35]` And they look pretty good. This is work
`[01:09:36]` And they look pretty good. This is work
`[01:09:36]` by Nvidia from uh
`[01:09:38]` by Nvidia from uh
`[01:09:39]` this year actually. It was presented
`[01:09:40]` this year actually. It was presented
`[01:09:40]` this year. Um you can use this to
`[01:09:42]` this year. Um you can use this to
`[01:09:42]` produce all kinds of different things
`[01:09:43]` produce all kinds of different things
`[01:09:43]` like, you know,
`[01:09:46]` like, you know,
`[01:09:46]` um
`[01:09:47]` um
`[01:09:47]` clothing, for example, training on a
`[01:09:49]` clothing, for example, training on a
`[01:09:49]` collection of uh
`[01:09:52]` collection of uh
`[01:09:52]` uh
`[01:09:52]` uh
`[01:09:52]` clothes from a famous designer.
`[01:09:55]` clothes from a famous designer.
`[01:09:55]` Um so, I think we need sort of new ways
`[01:09:57]` Um so, I think we need sort of new ways
`[01:09:57]` of uh represent of of sort of
`[01:10:00]` of uh represent of of sort of
`[01:10:00]` formulating this problem of unsupervised
`[01:10:01]` formulating this problem of unsupervised
`[01:10:01]` learning so that our systems can deal
`[01:10:03]` learning so that our systems can deal
`[01:10:03]` with this uh uncertainty in the
`[01:10:05]` with this uh uncertainty in the
`[01:10:05]` prediction in the context of continuous
`[01:10:07]` prediction in the context of continuous
`[01:10:07]` high-dimensional spaces. We don't have
`[01:10:09]` high-dimensional spaces. We don't have
`[01:10:09]` the problem in the context of um
`[01:10:12]` the problem in the context of um
`[01:10:12]` uh adversarial of um natural language
`[01:10:15]` uh adversarial of um natural language
`[01:10:15]` processing because it's easy to
`[01:10:17]` processing because it's easy to
`[01:10:17]` represent a distribution of our words.
`[01:10:19]` represent a distribution of our words.
`[01:10:19]` It's just a discrete distribution. It's
`[01:10:20]` It's just a discrete distribution. It's
`[01:10:20]` a long vector of numbers between 0 and 1
`[01:10:23]` a long vector of numbers between 0 and 1
`[01:10:23]` that sum to 1.
`[01:10:24]` that sum to 1.
`[01:10:24]` But it's very hard in continuous
`[01:10:26]` But it's very hard in continuous
`[01:10:26]` high-dimensional spaces. And so, we need
`[01:10:28]` high-dimensional spaces. And so, we need
`[01:10:28]` new techniques for this. And one
`[01:10:29]` new techniques for this. And one
`[01:10:29]` technique I'm proposing is something
`[01:10:30]` technique I'm proposing is something
`[01:10:31]` called energy-based uh self-supervised
`[01:10:32]` called energy-based uh self-supervised
`[01:10:33]` learning, which is imagine that uh your
`[01:10:35]` learning, which is imagine that uh your
`[01:10:35]` world is two-dimensional. You only have
`[01:10:37]` world is two-dimensional. You only have
`[01:10:37]` two input variables, two sensors.
`[01:10:39]` two input variables, two sensors.
`[01:10:39]` And your entire uh world, your entire
`[01:10:42]` And your entire uh world, your entire
`[01:10:42]` training set is composed of those dots
`[01:10:44]` training set is composed of those dots
`[01:10:44]` here in this two-dimensional space.
`[01:10:46]` here in this two-dimensional space.
`[01:10:46]` Uh what you'd like is to train a
`[01:10:48]` Uh what you'd like is to train a
`[01:10:49]` contrast function, let's call it an
`[01:10:50]` contrast function, let's call it an
`[01:10:50]` energy, that gives low energy to points
`[01:10:52]` energy, that gives low energy to points
`[01:10:52]` that are on the manifold
`[01:10:55]` that are on the manifold
`[01:10:55]` of data and higher energy outside.
`[01:10:58]` of data and higher energy outside.
`[01:10:58]` And there is basically a lot of research
`[01:11:00]` And there is basically a lot of research
`[01:11:00]` to do there to find the best method to
`[01:11:02]` to do there to find the best method to
`[01:11:02]` do this.
`[01:11:03]` do this.
`[01:11:03]` Uh my favorite one is what I call
`[01:11:05]` Uh my favorite one is what I call
`[01:11:05]` regularized latent variable models. And
`[01:11:06]` regularized latent variable models. And
`[01:11:06]` we had some success about 10 years ago
`[01:11:08]` we had some success about 10 years ago
`[01:11:08]` in using techniques of this type for
`[01:11:11]` in using techniques of this type for
`[01:11:11]` learning features in a convolutional net
`[01:11:12]` learning features in a convolutional net
`[01:11:12]` completely unsupervised,
`[01:11:14]` completely unsupervised,
`[01:11:14]` uh which is here on the left. Here is uh
`[01:11:16]` uh which is here on the left. Here is uh
`[01:11:16]` animation of a system that learns
`[01:11:19]` animation of a system that learns
`[01:11:19]` uh basically oriented filters by just
`[01:11:21]` uh basically oriented filters by just
`[01:11:21]` being trained with natural image patches
`[01:11:23]` being trained with natural image patches
`[01:11:23]` to reconstruct those under sparsity
`[01:11:24]` to reconstruct those under sparsity
`[01:11:24]` constraints. Uh and what you see on the
`[01:11:27]` constraints. Uh and what you see on the
`[01:11:27]` right is uh filters of the convolutional
`[01:11:29]` right is uh filters of the convolutional
`[01:11:29]` net that are learned um in the same uh
`[01:11:32]` net that are learned um in the same uh
`[01:11:32]` uh with the same algorithm with
`[01:11:33]` uh with the same algorithm with
`[01:11:33]` different numbers of filters.
`[01:11:35]` different numbers of filters.
`[01:11:35]` Those things kind of work. They don't
`[01:11:37]` Those things kind of work. They don't
`[01:11:37]` beat
`[01:11:38]` beat
`[01:11:38]` supervised learning if you have tons of
`[01:11:39]` supervised learning if you have tons of
`[01:11:39]` data, but the hope is that they will
`[01:11:41]` data, but the hope is that they will
`[01:11:41]` reduce the amount of necessary labeled
`[01:11:43]` reduce the amount of necessary labeled
`[01:11:43]` data.
`[01:11:45]` data.
`[01:11:45]` So, I'm going to end with um an example
`[01:11:48]` So, I'm going to end with um an example
`[01:11:48]` of how to combine combine all this to
`[01:11:50]` of how to combine combine all this to
`[01:11:50]` get a machine to learn something um
`[01:11:52]` get a machine to learn something um
`[01:11:52]` uh
`[01:11:53]` uh
`[01:11:53]` useful like a like a task of motor task.
`[01:11:56]` useful like a like a task of motor task.
`[01:11:56]` Uh so, here what I'm what I'm talking
`[01:11:58]` Uh so, here what I'm what I'm talking
`[01:11:58]` about is can we train a machine to
`[01:12:01]` about is can we train a machine to
`[01:12:01]` learn to drive by just observing
`[01:12:04]` learn to drive by just observing
`[01:12:04]` uh
`[01:12:05]` uh
`[01:12:05]` other people driving and by training a
`[01:12:07]` other people driving and by training a
`[01:12:07]` model of uh what goes on in the world.
`[01:12:10]` model of uh what goes on in the world.
`[01:12:11]` So,
`[01:12:12]` So,
`[01:12:13]` you are in your car, you can see all the
`[01:12:14]` you are in your car, you can see all the
`[01:12:14]` cars around you. And if you can predict
`[01:12:16]` cars around you. And if you can predict
`[01:12:16]` what the cars around you are going to do
`[01:12:18]` what the cars around you are going to do
`[01:12:18]` ahead of time,
`[01:12:20]` ahead of time,
`[01:12:20]` then you can drive defensively
`[01:12:21]` then you can drive defensively
`[01:12:21]` basically. You can you can decide to
`[01:12:23]` basically. You can you can decide to
`[01:12:23]` stay away from this car because you see
`[01:12:25]` stay away from this car because you see
`[01:12:25]` it swerving. You can decide to uh
`[01:12:28]` it swerving. You can decide to uh
`[01:12:28]` you know, kind of slow down because the
`[01:12:29]` you know, kind of slow down because the
`[01:12:29]` car in front of you is likely to uh to
`[01:12:31]` car in front of you is likely to uh to
`[01:12:31]` slow down cuz there's another car in
`[01:12:32]` slow down cuz there's another car in
`[01:12:32]` front of it that is is slowing down. So,
`[01:12:35]` front of it that is is slowing down. So,
`[01:12:35]` you have all those predictive models
`[01:12:36]` you have all those predictive models
`[01:12:36]` that basically keep you safe and you've
`[01:12:38]` that basically keep you safe and you've
`[01:12:38]` sort of learned to integrate them over
`[01:12:40]` sort of learned to integrate them over
`[01:12:40]` time. You don't even have to think about
`[01:12:41]` time. You don't even have to think about
`[01:12:41]` it. You it's just in your in your sort
`[01:12:43]` it. You it's just in your in your sort
`[01:12:43]` of reflexes of of driving. You can talk
`[01:12:46]` of reflexes of of driving. You can talk
`[01:12:46]` at the same time and and you you'll
`[01:12:48]` at the same time and and you you'll
`[01:12:48]` you'll work.
`[01:12:50]` you'll work.
`[01:12:50]` Um
`[01:12:52]` Um
`[01:12:52]` But the way to train a system like this
`[01:12:53]` But the way to train a system like this
`[01:12:53]` is you first have to train a forward
`[01:12:55]` is you first have to train a forward
`[01:12:55]` model. So, a forward model would be uh
`[01:12:57]` model. So, a forward model would be uh
`[01:12:57]` here is the state of the world at time
`[01:12:58]` here is the state of the world at time
`[01:12:58]` T.
`[01:12:59]` T.
`[01:12:59]` Give me the a prediction about the state
`[01:13:01]` Give me the a prediction about the state
`[01:13:01]` of the world at time T plus 1.
`[01:13:03]` of the world at time T plus 1.
`[01:13:03]` And the problem with this, of course, is
`[01:13:05]` And the problem with this, of course, is
`[01:13:05]` the world is not deterministic.
`[01:13:07]` the world is not deterministic.
`[01:13:07]` There's a lot of things that could
`[01:13:08]` There's a lot of things that could
`[01:13:08]` happen. So, it's the same problem I was
`[01:13:09]` happen. So, it's the same problem I was
`[01:13:09]` talking about with the pen. Many things
`[01:13:11]` talking about with the pen. Many things
`[01:13:11]` can happen.
`[01:13:13]` can happen.
`[01:13:13]` So, but if you had such a forward model,
`[01:13:16]` So, but if you had such a forward model,
`[01:13:16]` you could run the forward model multiple
`[01:13:18]` you could run the forward model multiple
`[01:13:18]` time steps.
`[01:13:21]` And then, if you had a an objective
`[01:13:23]` function like how far you are from the
`[01:13:25]` function like how far you are from the
`[01:13:25]` other cars, whether you are in lane,
`[01:13:26]` other cars, whether you are in lane,
`[01:13:26]` things like this,
`[01:13:28]` things like this,
`[01:13:28]` you could back propagate gradients
`[01:13:29]` you could back propagate gradients
`[01:13:29]` through this entire system to train a
`[01:13:32]` through this entire system to train a
`[01:13:32]` neural net to predict the correct course
`[01:13:34]` neural net to predict the correct course
`[01:13:34]` of action that would uh
`[01:13:37]` of action that would uh
`[01:13:37]` that would be safe over the long run.
`[01:13:39]` that would be safe over the long run.
`[01:13:39]` And this can be done completely in your
`[01:13:41]` And this can be done completely in your
`[01:13:41]` head. If you have a forward model in
`[01:13:42]` head. If you have a forward model in
`[01:13:42]` your head, you don't have to actually
`[01:13:43]` your head, you don't have to actually
`[01:13:43]` drive to train yourself to drive. You
`[01:13:45]` drive to train yourself to drive. You
`[01:13:45]` can just imagine
`[01:13:47]` can just imagine
`[01:13:47]` all of those things.
`[01:13:51]` So, that's a specific example. So,
`[01:13:53]` you put a camera looking down at a
`[01:13:55]` you put a camera looking down at a
`[01:13:55]` highway.
`[01:13:56]` highway.
`[01:13:56]` It follows every car and it extracts a
`[01:13:58]` It follows every car and it extracts a
`[01:13:58]` little rectangle around every car that
`[01:14:00]` little rectangle around every car that
`[01:14:00]` follows every car that you see at the
`[01:14:01]` follows every car that you see at the
`[01:14:01]` bottom.
`[01:14:02]` bottom.
`[01:14:02]` And uh and what you're doing now is
`[01:14:04]` And uh and what you're doing now is
`[01:14:04]` you're training a convolutional net to
`[01:14:06]` you're training a convolutional net to
`[01:14:06]` take a few frames centered
`[01:14:09]` take a few frames centered
`[01:14:09]` on a particular car and predict the next
`[01:14:11]` on a particular car and predict the next
`[01:14:11]` state of the world.
`[01:14:13]` state of the world.
`[01:14:13]` And if you do this,
`[01:14:15]` And if you do this,
`[01:14:15]` um
`[01:14:16]` um
`[01:14:16]` you get
`[01:14:17]` you get
`[01:14:18]` uh
`[01:14:19]` uh
`[01:14:19]` oops, sorry.
`[01:14:25]` You get the second column. So, the the
`[01:14:28]` the column on the left is what happens
`[01:14:29]` the column on the left is what happens
`[01:14:29]` in the real world. The second column is
`[01:14:31]` in the real world. The second column is
`[01:14:31]` what happens if you just train a
`[01:14:32]` what happens if you just train a
`[01:14:32]` convolutional net with least square to
`[01:14:34]` convolutional net with least square to
`[01:14:34]` predict what's going to happen. It can
`[01:14:35]` predict what's going to happen. It can
`[01:14:35]` only predict the average of all the
`[01:14:36]` only predict the average of all the
`[01:14:37]` possible futures and so, you get blurry
`[01:14:38]` possible futures and so, you get blurry
`[01:14:38]` predictions.
`[01:14:39]` predictions.
`[01:14:40]` If you now transform the model so that
`[01:14:41]` If you now transform the model so that
`[01:14:41]` it has a latent variable that allows it
`[01:14:43]` it has a latent variable that allows it
`[01:14:43]` to take into account the uncertainty
`[01:14:45]` to take into account the uncertainty
`[01:14:45]` about the world, and I'm not going to
`[01:14:47]` about the world, and I'm not going to
`[01:14:47]` explain exactly how that works, then you
`[01:14:48]` explain exactly how that works, then you
`[01:14:48]` get the the prediction that you just saw
`[01:14:51]` get the the prediction that you just saw
`[01:14:51]` um
`[01:14:52]` um
`[01:14:52]` on the on the right where for every
`[01:14:55]` on the on the right where for every
`[01:14:55]` drawing of this latent variable, you get
`[01:14:57]` drawing of this latent variable, you get
`[01:14:57]` different predictions, but they're
`[01:14:58]` different predictions, but they're
`[01:14:58]` crisp.
`[01:15:00]` crisp.
`[01:15:00]` Okay, so now what you can do is um you
`[01:15:02]` Okay, so now what you can do is um you
`[01:15:02]` can to do this training I was telling
`[01:15:04]` can to do this training I was telling
`[01:15:04]` you about earlier,
`[01:15:06]` you about earlier,
`[01:15:06]` you sample the latent variables. You get
`[01:15:07]` you sample the latent variables. You get
`[01:15:08]` different possible scenarios about
`[01:15:09]` different possible scenarios about
`[01:15:09]` what's going to happen in your future.
`[01:15:11]` what's going to happen in your future.
`[01:15:11]` Then through back propagation, you train
`[01:15:12]` Then through back propagation, you train
`[01:15:12]` your policy network uh to get your
`[01:15:15]` your policy network uh to get your
`[01:15:15]` system to drive.
`[01:15:16]` system to drive.
`[01:15:16]` If you do this, it doesn't work.
`[01:15:18]` If you do this, it doesn't work.
`[01:15:18]` It doesn't work because the system goes
`[01:15:20]` It doesn't work because the system goes
`[01:15:20]` into regions of the state space where
`[01:15:23]` into regions of the state space where
`[01:15:23]` you the forward model is very inaccurate
`[01:15:24]` you the forward model is very inaccurate
`[01:15:24]` and very uncertain.
`[01:15:26]` and very uncertain.
`[01:15:26]` So, what you have to do is add another
`[01:15:27]` So, what you have to do is add another
`[01:15:27]` term in the objective function that
`[01:15:30]` term in the objective function that
`[01:15:30]` prevents the system from going into
`[01:15:31]` prevents the system from going into
`[01:15:31]` parts of the space where it doesn't
`[01:15:33]` parts of the space where it doesn't
`[01:15:33]` where its predictions are bad.
`[01:15:35]` where its predictions are bad.
`[01:15:35]` Okay, so it's like an inverse curiosity
`[01:15:37]` Okay, so it's like an inverse curiosity
`[01:15:37]` uh
`[01:15:38]` uh
`[01:15:38]` constraint if you want.
`[01:15:40]` constraint if you want.
`[01:15:40]` And if you do this, it works. So, these
`[01:15:42]` And if you do this, it works. So, these
`[01:15:42]` are examples of uh the blue car is
`[01:15:44]` are examples of uh the blue car is
`[01:15:44]` driving itself. The little white dot
`[01:15:45]` driving itself. The little white dot
`[01:15:45]` indicates whether it accelerates,
`[01:15:47]` indicates whether it accelerates,
`[01:15:47]` whether it brakes, or whether it turns.
`[01:15:48]` whether it brakes, or whether it turns.
`[01:15:48]` And it kind of keeps itself safe away
`[01:15:50]` And it kind of keeps itself safe away
`[01:15:50]` from the other cars. The other cars
`[01:15:51]` from the other cars. The other cars
`[01:15:52]` can't see it. The blue car is invisible
`[01:15:53]` can't see it. The blue car is invisible
`[01:15:53]` here.
`[01:15:55]` here.
`[01:15:55]` Uh let me show you another example here.
`[01:15:57]` Uh let me show you another example here.
`[01:15:57]` Um
`[01:15:58]` Um
`[01:15:58]` So, here the yellow car is the actual
`[01:16:00]` So, here the yellow car is the actual
`[01:16:00]` car in the video. The blue car is what
`[01:16:01]` car in the video. The blue car is what
`[01:16:02]` the agent here that's been trained is uh
`[01:16:04]` the agent here that's been trained is uh
`[01:16:04]` is doing. And it's being squeezed
`[01:16:05]` is doing. And it's being squeezed
`[01:16:05]` between two cars, so it has to escape
`[01:16:07]` between two cars, so it has to escape
`[01:16:07]` because the other cars don't see it.
`[01:16:10]` because the other cars don't see it.
`[01:16:10]` So, it has to squeeze out.
`[01:16:12]` So, it has to squeeze out.
`[01:16:12]` Um
`[01:16:13]` Um
`[01:16:13]` But it works. It works reasonably well.
`[01:16:15]` But it works. It works reasonably well.
`[01:16:15]` And
`[01:16:16]` And
`[01:16:16]` basically, that system
`[01:16:18]` basically, that system
`[01:16:18]` has never interacted with the real
`[01:16:20]` has never interacted with the real
`[01:16:20]` world. It's just watched
`[01:16:22]` world. It's just watched
`[01:16:22]` other people drive.
`[01:16:24]` other people drive.
`[01:16:24]` And then it's used that for for training
`[01:16:26]` And then it's used that for for training
`[01:16:26]` its uh action plans, basically its
`[01:16:28]` its uh action plans, basically its
`[01:16:28]` policy.
`[01:16:30]` policy.
`[01:16:30]` Okay, now I'm going to go a little uh
`[01:16:32]` Okay, now I'm going to go a little uh
`[01:16:32]` uh
`[01:16:33]` uh
`[01:16:33]` philosophical if you want.
`[01:16:36]` philosophical if you want.
`[01:16:36]` Um there is through throughout history
`[01:16:38]` Um there is through throughout history
`[01:16:38]` of technology and science, there's been
`[01:16:39]` of technology and science, there's been
`[01:16:39]` this phenomenon. It's not universal, but
`[01:16:41]` this phenomenon. It's not universal, but
`[01:16:41]` it's pretty frequent where people invent
`[01:16:43]` it's pretty frequent where people invent
`[01:16:43]` an artifact and then derive a science
`[01:16:46]` an artifact and then derive a science
`[01:16:46]` out of this artifact to explain how this
`[01:16:49]` out of this artifact to explain how this
`[01:16:49]` artifact works or to kind of
`[01:16:51]` artifact works or to kind of
`[01:16:51]` uh
`[01:16:52]` uh
`[01:16:52]` uh figure out its limitations. A good
`[01:16:54]` uh figure out its limitations. A good
`[01:16:54]` example is the invention of the
`[01:16:55]` example is the invention of the
`[01:16:55]` telescope
`[01:16:56]` telescope
`[01:16:56]` in the 1600s. Optics was not developed
`[01:16:58]` in the 1600s. Optics was not developed
`[01:16:58]` until at least 50 years later.
`[01:17:01]` until at least 50 years later.
`[01:17:01]` Uh but people had a good intuition of
`[01:17:03]` Uh but people had a good intuition of
`[01:17:03]` how to build telescopes before that.
`[01:17:06]` how to build telescopes before that.
`[01:17:06]` The steam engine was invented in the
`[01:17:08]` The steam engine was invented in the
`[01:17:08]` late 1600s, early 1700s.
`[01:17:10]` late 1600s, early 1700s.
`[01:17:10]` And thermodynamics was, you know, came
`[01:17:12]` And thermodynamics was, you know, came
`[01:17:12]` up more than 100 years later, basically
`[01:17:14]` up more than 100 years later, basically
`[01:17:14]` designed to uh explain the limitations
`[01:17:17]` designed to uh explain the limitations
`[01:17:17]` of thermal engines.
`[01:17:19]` of thermal engines.
`[01:17:19]` And thermodynamics now is the foundation
`[01:17:21]` And thermodynamics now is the foundation
`[01:17:21]` of one of the most fundamental
`[01:17:23]` of one of the most fundamental
`[01:17:23]` intellectual construction of all
`[01:17:24]` intellectual construction of all
`[01:17:24]` science.
`[01:17:25]` science.
`[01:17:25]` Uh
`[01:17:26]` Uh
`[01:17:26]` so, it was purposely defined to explain
`[01:17:29]` so, it was purposely defined to explain
`[01:17:29]` a particular artifact. That's very
`[01:17:31]` a particular artifact. That's very
`[01:17:31]` interesting.
`[01:17:32]` interesting.
`[01:17:32]` Um same thing with electromagnetism,
`[01:17:35]` Um same thing with electromagnetism,
`[01:17:35]` electrodynamics with uh
`[01:17:37]` electrodynamics with uh
`[01:17:37]` you know, the invention of sailboats and
`[01:17:38]` you know, the invention of sailboats and
`[01:17:38]` airplanes and aerodynamics.
`[01:17:40]` airplanes and aerodynamics.
`[01:17:40]` Uh
`[01:17:41]` Uh
`[01:17:41]` uh
`[01:17:42]` uh
`[01:17:42]` you know, the invention of compounds and
`[01:17:44]` you know, the invention of compounds and
`[01:17:44]` chemistry to explain, etc., right?
`[01:17:46]` chemistry to explain, etc., right?
`[01:17:46]` Computers and computer science came
`[01:17:48]` Computers and computer science came
`[01:17:48]` after the invention of computers, right?
`[01:17:50]` after the invention of computers, right?
`[01:17:50]` Uh information theory came after the
`[01:17:52]` Uh information theory came after the
`[01:17:52]` invention of uh first digital
`[01:17:54]` invention of uh first digital
`[01:17:54]` communication uh through radio and
`[01:17:57]` communication uh through radio and
`[01:17:57]` teletype and things like that.
`[01:17:59]` teletype and things like that.
`[01:17:59]` So, it's quite possible that now we
`[01:18:01]` So, it's quite possible that now we
`[01:18:01]` have,
`[01:18:02]` have,
`[01:18:02]` you know, in the next few decades, we'll
`[01:18:04]` you know, in the next few decades, we'll
`[01:18:04]` have
`[01:18:05]` have
`[01:18:05]` empirical systems that are built by
`[01:18:08]` empirical systems that are built by
`[01:18:08]` uh trial and error, perhaps by
`[01:18:10]` uh trial and error, perhaps by
`[01:18:10]` systematic optimization on powerful
`[01:18:12]` systematic optimization on powerful
`[01:18:12]` machines, perhaps by intuitions, by
`[01:18:15]` machines, perhaps by intuitions, by
`[01:18:15]` empirical work,
`[01:18:17]` empirical work,
`[01:18:17]` perhaps with a little bit of theory,
`[01:18:19]` perhaps with a little bit of theory,
`[01:18:19]` perhaps a lot of theory, hopefully.
`[01:18:22]` perhaps a lot of theory, hopefully.
`[01:18:22]` And the question is whether this will
`[01:18:24]` And the question is whether this will
`[01:18:24]` lead to
`[01:18:25]` lead to
`[01:18:25]` a whole theory of intelligence.
`[01:18:28]` a whole theory of intelligence.
`[01:18:28]` The fact that we can build an artifact
`[01:18:30]` The fact that we can build an artifact
`[01:18:30]` that is intelligent might lead to a
`[01:18:32]` that is intelligent might lead to a
`[01:18:32]` general theory of
`[01:18:34]` general theory of
`[01:18:34]` information processing and intelligence.
`[01:18:36]` information processing and intelligence.
`[01:18:36]` Um
`[01:18:37]` Um
`[01:18:37]` And that's kind of a big hope. I'm not
`[01:18:40]` And that's kind of a big hope. I'm not
`[01:18:40]` sure this is going to be realized over
`[01:18:42]` sure this is going to be realized over
`[01:18:42]` the next few decades, but uh that's a
`[01:18:44]` the next few decades, but uh that's a
`[01:18:44]` good program.
`[01:18:46]` good program.
`[01:18:46]` A word of caution
`[01:18:48]` A word of caution
`[01:18:48]` about biological inspiration. So, neural
`[01:18:49]` about biological inspiration. So, neural
`[01:18:49]` nets are biologically inspired,
`[01:18:50]` nets are biologically inspired,
`[01:18:51]` convolutional nets are biologically
`[01:18:52]` convolutional nets are biologically
`[01:18:52]` inspired, but they're just inspired.
`[01:18:53]` inspired, but they're just inspired.
`[01:18:53]` They're not copied.
`[01:18:55]` They're not copied.
`[01:18:55]` Um let me give you a story of a
`[01:18:57]` Um let me give you a story of a
`[01:18:57]` gentleman called Clément Ader.
`[01:18:59]` gentleman called Clément Ader.
`[01:18:59]` Uh is there any French people in the
`[01:19:00]` Uh is there any French people in the
`[01:19:00]` room here?
`[01:19:01]` room here?
`[01:19:01]` Okay. Can you raise your hand? French
`[01:19:03]` Okay. Can you raise your hand? French
`[01:19:03]` people? No French people? Yeah, okay, a
`[01:19:05]` people? No French people? Yeah, okay, a
`[01:19:05]` couple. You heard of Clément Ader?
`[01:19:09]` Never heard of Clément Ader? Yeah, you
`[01:19:11]` have. Okay.
`[01:19:12]` have. Okay.
`[01:19:12]` Is there anyone who is not French who
`[01:19:14]` Is there anyone who is not French who
`[01:19:14]` has heard of Clément Ader?
`[01:19:17]` has heard of Clément Ader?
`[01:19:17]` Okay, one person, two person.
`[01:19:20]` Okay, one person, two person.
`[01:19:20]` Basically, nobody. You guys have no idea
`[01:19:21]` Basically, nobody. You guys have no idea
`[01:19:21]` who he is, right? Okay. So, this guy
`[01:19:24]` who he is, right? Okay. So, this guy
`[01:19:24]` built in the late 1800s a bat-shaped
`[01:19:28]` built in the late 1800s a bat-shaped
`[01:19:28]` airplane, steam-powered.
`[01:19:30]` airplane, steam-powered.
`[01:19:30]` He was a steam engine designer.
`[01:19:32]` He was a steam engine designer.
`[01:19:32]` And his airplane actually took off on
`[01:19:35]` And his airplane actually took off on
`[01:19:35]` its own power 13 years before the Wright
`[01:19:37]` its own power 13 years before the Wright
`[01:19:37]` brothers
`[01:19:38]` brothers
`[01:19:38]` uh flew for about 50 m at about 50 cm
`[01:19:41]` uh flew for about 50 m at about 50 cm
`[01:19:41]` altitude and then kind of crash landed.
`[01:19:45]` altitude and then kind of crash landed.
`[01:19:45]` Um it was basically uncontrollable. So,
`[01:19:48]` Um it was basically uncontrollable. So,
`[01:19:48]` basically, the guy just copied bats and
`[01:19:50]` basically, the guy just copied bats and
`[01:19:50]` just assumed that because it has the
`[01:19:51]` just assumed that because it has the
`[01:19:51]` shape of a bat, it would just fly,
`[01:19:53]` shape of a bat, it would just fly,
`[01:19:53]` right?
`[01:19:54]` right?
`[01:19:54]` Uh that seemed a little bit naive. It
`[01:19:56]` Uh that seemed a little bit naive. It
`[01:19:56]` was not naive at all, but it was it kind
`[01:19:58]` was not naive at all, but it was it kind
`[01:19:58]` of, you know, stuck a little bit too
`[01:19:59]` of, you know, stuck a little bit too
`[01:19:59]` close to biology and and got sort of
`[01:20:01]` close to biology and and got sort of
`[01:20:01]` hypnotized by it a little bit and didn't
`[01:20:04]` hypnotized by it a little bit and didn't
`[01:20:04]` do things like, you know, build a model
`[01:20:06]` do things like, you know, build a model
`[01:20:06]` or a glider or a kite or,
`[01:20:10]` or a glider or a kite or,
`[01:20:10]` you know, a wind tunnel like the like
`[01:20:12]` you know, a wind tunnel like the like
`[01:20:12]` the Wright brothers did.
`[01:20:13]` the Wright brothers did.
`[01:20:13]` Um so, he he stuck a little too close to
`[01:20:15]` Um so, he he stuck a little too close to
`[01:20:15]` biology. On the other hand, he had a big
`[01:20:18]` biology. On the other hand, he had a big
`[01:20:18]` legacy, which is that his second
`[01:20:20]` legacy, which is that his second
`[01:20:20]` airplane was called the Avion and that's
`[01:20:22]` airplane was called the Avion and that's
`[01:20:22]` actually the word in French, uh Spanish
`[01:20:25]` actually the word in French, uh Spanish
`[01:20:25]` and Portuguese uh for airplane. So, he
`[01:20:27]` and Portuguese uh for airplane. So, he
`[01:20:27]` had some legacy.
`[01:20:29]` had some legacy.
`[01:20:29]` Um but he was kind of a secretive guy.
`[01:20:31]` Um but he was kind of a secretive guy.
`[01:20:31]` He, you know, this was before the open
`[01:20:32]` He, you know, this was before the open
`[01:20:32]` source days. And so,
`[01:20:34]` source days. And so,
`[01:20:34]` this is why you never heard of him.
`[01:20:37]` this is why you never heard of him.
`[01:20:37]` Thank you very much.
`[01:20:39]` Thank you very much.
`[01:20:39]` [applause]
`[01:20:46]` Thank you.
`[01:20:47]` [applause]
`[01:20:49]` [applause]
`[01:20:49]` Thank you. Thank you, Jeff. Thank you,
`[01:20:51]` Thank you. Thank you, Jeff. Thank you,
`[01:20:51]` Yann. Uh
`[01:20:52]` Yann. Uh
`[01:20:52]` we have Can we get the house lights on,
`[01:20:54]` we have Can we get the house lights on,
`[01:20:54]` please? We have two microphones up and
`[01:20:56]` please? We have two microphones up and
`[01:20:56]` we have time for a couple of questions.
`[01:20:59]` we have time for a couple of questions.
`[01:20:59]` Uh house lights on, please.
`[01:21:02]` Uh house lights on, please.
`[01:21:02]` I know they came on earlier.
`[01:21:05]` Yes, so
`[01:21:07]` Well, first, let's give Yann and Jeff a
`[01:21:09]` Well, first, let's give Yann and Jeff a
`[01:21:10]` round of applause for an amazing amazing
`[01:21:11]` round of applause for an amazing amazing
`[01:21:11]` talk.
`[01:21:13]` talk.
`[01:21:13]` [applause]
`[01:21:21]` A little piece of trivia while someone
`[01:21:23]` comes up to the microphone.
`[01:21:25]` comes up to the microphone.
`[01:21:25]` Uh Alan Turing's birthday was June 23rd,
`[01:21:27]` Uh Alan Turing's birthday was June 23rd,
`[01:21:28]` 1912.
`[01:21:29]` 1912.
`[01:21:29]` So, today is the 107th birthday
`[01:21:32]` So, today is the 107th birthday
`[01:21:32]` anniversary and so it's very appropriate
`[01:21:34]` anniversary and so it's very appropriate
`[01:21:34]` that we had this memorable Turing
`[01:21:36]` that we had this memorable Turing
`[01:21:36]` lecture today. Okay, question.
`[01:21:40]` Oh, is the mic on?
`[01:21:42]` Yeah. Hi, thank you both. Um
`[01:21:44]` Yeah. Hi, thank you both. Um
`[01:21:44]` I'm really interested in the work on
`[01:21:47]` I'm really interested in the work on
`[01:21:47]` understanding reasoning. Can you give us
`[01:21:48]` understanding reasoning. Can you give us
`[01:21:48]` a little taste of what you're thinking
`[01:21:50]` a little taste of what you're thinking
`[01:21:50]` there? The the reasoning of how neural
`[01:21:53]` there? The the reasoning of how neural
`[01:21:53]` nets, you know, reason.
`[01:21:55]` nets, you know, reason.
`[01:21:55]` Okay, so um
`[01:21:58]` Okay, so um
`[01:21:58]` neural nets are pretty good at things
`[01:22:00]` neural nets are pretty good at things
`[01:22:00]` you do in parallel in 100 milliseconds.
`[01:22:03]` you do in parallel in 100 milliseconds.
`[01:22:03]` Um so far, they're not so good at things
`[01:22:05]` Um so far, they're not so good at things
`[01:22:05]` you do over longer time periods. And in
`[01:22:07]` you do over longer time periods. And in
`[01:22:07]` particular, one thing
`[01:22:10]` particular, one thing
`[01:22:10]` that people criticize neural nets for is
`[01:22:12]` that people criticize neural nets for is
`[01:22:12]` they can't do recursion.
`[01:22:14]` they can't do recursion.
`[01:22:14]` So, when we understand a sentence, we
`[01:22:17]` So, when we understand a sentence, we
`[01:22:17]` can go off into a relative clause and
`[01:22:19]` can go off into a relative clause and
`[01:22:19]` understand the relative clause and we
`[01:22:20]` understand the relative clause and we
`[01:22:20]` devote all our effort to understanding
`[01:22:22]` devote all our effort to understanding
`[01:22:22]` that relative clause and then come back
`[01:22:24]` that relative clause and then come back
`[01:22:24]` again. And that kind of thing um we're
`[01:22:27]` again. And that kind of thing um we're
`[01:22:27]` just beginning to be able to do with
`[01:22:28]` just beginning to be able to do with
`[01:22:28]` neural nets.
`[01:22:30]` neural nets.
`[01:22:30]` So, people at Facebook have done lots of
`[01:22:31]` So, people at Facebook have done lots of
`[01:22:31]` that. People at Google are doing it, but
`[01:22:33]` that. People at Google are doing it, but
`[01:22:33]` um
`[01:22:35]` um
`[01:22:35]` in order to do things like that, you
`[01:22:37]` in order to do things like that, you
`[01:22:37]` need some kind of memory. The typical
`[01:22:39]` need some kind of memory. The typical
`[01:22:39]` thing to use in a neural net is you just
`[01:22:41]` thing to use in a neural net is you just
`[01:22:41]` have another bank of neurons, which are
`[01:22:43]` have another bank of neurons, which are
`[01:22:43]` copies of neurons you already have. But
`[01:22:45]` copies of neurons you already have. But
`[01:22:45]` that's not biologically plausible.
`[01:22:48]` that's not biologically plausible.
`[01:22:48]` So, I always want something that's
`[01:22:49]` So, I always want something that's
`[01:22:49]` biologically plausible. Um and
`[01:22:53]` biologically plausible. Um and
`[01:22:53]` in the brain, it seems much more likely
`[01:22:54]` in the brain, it seems much more likely
`[01:22:54]` that this memory is not copies of neural
`[01:22:57]` that this memory is not copies of neural
`[01:22:57]` activities. It's an associative memory
`[01:22:59]` activities. It's an associative memory
`[01:22:59]` that can recreate neural activities.
`[01:23:02]` that can recreate neural activities.
`[01:23:02]` But it's it's one that's just used for
`[01:23:03]` But it's it's one that's just used for
`[01:23:03]` temporary things.
`[01:23:06]` temporary things.
`[01:23:06]` There's actually quite a lot of work on
`[01:23:07]` There's actually quite a lot of work on
`[01:23:07]` this on sort of, you know, trying to
`[01:23:09]` this on sort of, you know, trying to
`[01:23:09]` sort of fill the gap of uh neural nets
`[01:23:11]` sort of fill the gap of uh neural nets
`[01:23:11]` not being able to do long chains of
`[01:23:12]` not being able to do long chains of
`[01:23:12]` reasoning. Uh so, there's one question
`[01:23:15]` reasoning. Uh so, there's one question
`[01:23:15]` that uh
`[01:23:16]` that uh
`[01:23:16]` you know, Jeff has been sort of
`[01:23:18]` you know, Jeff has been sort of
`[01:23:18]` advocating for for a long time is the
`[01:23:19]` advocating for for a long time is the
`[01:23:19]` fact that
`[01:23:20]` fact that
`[01:23:20]` uh if you have sort of classical
`[01:23:23]` uh if you have sort of classical
`[01:23:23]` logic-based reasoning, it's discrete,
`[01:23:26]` logic-based reasoning, it's discrete,
`[01:23:26]` therefore incompatible with
`[01:23:28]` therefore incompatible with
`[01:23:28]` gradient-based learning.
`[01:23:29]` gradient-based learning.
`[01:23:29]` And so, how can you do reasoning with
`[01:23:31]` And so, how can you do reasoning with
`[01:23:31]` vectors by replacing symbols by vectors
`[01:23:34]` vectors by replacing symbols by vectors
`[01:23:34]` and replacing logic by continuous
`[01:23:37]` and replacing logic by continuous
`[01:23:37]` functions, basically parameterized
`[01:23:38]` functions, basically parameterized
`[01:23:38]` continuous functions. Uh
`[01:23:40]` continuous functions. Uh
`[01:23:40]` and then if you want long chains of
`[01:23:41]` and then if you want long chains of
`[01:23:41]` reasoning, you need to have a working
`[01:23:43]` reasoning, you need to have a working
`[01:23:43]` memory. So, Jeff was kind of mentioning
`[01:23:44]` memory. So, Jeff was kind of mentioning
`[01:23:44]` one idea using fast weights. There's a
`[01:23:46]` one idea using fast weights. There's a
`[01:23:46]` lot of people working on what's called
`[01:23:48]` lot of people working on what's called
`[01:23:48]` memory networks. So, you have
`[01:23:49]` memory networks. So, you have
`[01:23:49]` basically, what I must remember current
`[01:23:50]` basically, what I must remember current
`[01:23:50]` net, which can access a separate neural
`[01:23:53]` net, which can access a separate neural
`[01:23:53]` net, which is also differentiable, but
`[01:23:54]` net, which is also differentiable, but
`[01:23:54]` it's built the particular architecture
`[01:23:56]` it's built the particular architecture
`[01:23:56]` that turns it into an associative
`[01:23:58]` that turns it into an associative
`[01:23:58]` memory, basically. Um and those kind of
`[01:24:00]` memory, basically. Um and those kind of
`[01:24:00]` work in simple cases. They haven't
`[01:24:02]` work in simple cases. They haven't
`[01:24:02]` really been scaled up to uh big
`[01:24:04]` really been scaled up to uh big
`[01:24:04]` problems, but there is uh very
`[01:24:06]` problems, but there is uh very
`[01:24:06]` interesting work uh
`[01:24:08]` interesting work uh
`[01:24:08]` on
`[01:24:09]` on
`[01:24:09]` uh basically, neural nets that do not
`[01:24:11]` uh basically, neural nets that do not
`[01:24:11]` directly compute an answer, but they
`[01:24:13]` directly compute an answer, but they
`[01:24:13]` produce a neural net
`[01:24:16]` produce a neural net
`[01:24:16]` which is designed to answer to answer
`[01:24:17]` which is designed to answer to answer
`[01:24:17]` the question that's being asked. So, uh
`[01:24:20]` the question that's being asked. So, uh
`[01:24:20]` uh visual question answering is a
`[01:24:21]` uh visual question answering is a
`[01:24:21]` typical example of this. You you show a
`[01:24:23]` typical example of this. You you show a
`[01:24:23]` complex image to a system and you ask
`[01:24:25]` complex image to a system and you ask
`[01:24:25]` it, uh you know, is there a Chinese
`[01:24:27]` it, uh you know, is there a Chinese
`[01:24:27]` sphere that is larger than uh
`[01:24:30]` sphere that is larger than uh
`[01:24:30]` the two cubes in this picture, right?
`[01:24:32]` the two cubes in this picture, right?
`[01:24:32]` And what the neural net does is that it
`[01:24:34]` And what the neural net does is that it
`[01:24:34]` produces a neural another neural net,
`[01:24:35]` produces a neural another neural net,
`[01:24:35]` which has the right module to answer
`[01:24:37]` which has the right module to answer
`[01:24:37]` that question. You can train this whole
`[01:24:38]` that question. You can train this whole
`[01:24:39]` thing with backprop and it's kind of
`[01:24:40]` thing with backprop and it's kind of
`[01:24:40]` amazing that it works at all.
`[01:24:41]` amazing that it works at all.
`[01:24:41]` Um but it works.
`[01:24:44]` Um but it works.
`[01:24:44]` Uh one more question.
`[01:24:47]` Uh one more question.
`[01:24:47]` Oh, sorry. Yeah, go ahead.
`[01:24:49]` Oh, sorry. Yeah, go ahead.
`[01:24:49]` I'm from Northeastern University. So, I
`[01:24:52]` I'm from Northeastern University. So, I
`[01:24:52]` know many people question about neural
`[01:24:54]` know many people question about neural
`[01:24:54]` network saying that we know neural
`[01:24:56]` network saying that we know neural
`[01:24:56]` network neural network work, but we
`[01:24:59]` network neural network work, but we
`[01:24:59]` don't know how they work. So, what I
`[01:25:00]` don't know how they work. So, what I
`[01:25:00]` wonder what's your comments on this uh
`[01:25:02]` wonder what's your comments on this uh
`[01:25:02]` question.
`[01:25:04]` question.
`[01:25:04]` It's not really true. I mean, we have
`[01:25:05]` It's not really true. I mean, we have
`[01:25:05]` some understanding, of course. I mean,
`[01:25:07]` some understanding, of course. I mean,
`[01:25:07]` first of all, we have access to
`[01:25:08]` first of all, we have access to
`[01:25:09]` everything inside the machine, right? Uh
`[01:25:11]` everything inside the machine, right? Uh
`[01:25:11]` I mean, obviously, those things have
`[01:25:12]` I mean, obviously, those things have
`[01:25:12]` hundreds of millions of parameters,
`[01:25:14]` hundreds of millions of parameters,
`[01:25:14]` you know, hundreds of thousands of
`[01:25:16]` you know, hundreds of thousands of
`[01:25:16]` variables inside. It's going to be
`[01:25:17]` variables inside. It's going to be
`[01:25:17]` complicated. It has to be complicated
`[01:25:18]` complicated. It has to be complicated
`[01:25:18]` because we want them to solve
`[01:25:19]` because we want them to solve
`[01:25:19]` complicated problems. So, thinking that
`[01:25:22]` complicated problems. So, thinking that
`[01:25:22]` you're going to have a complete
`[01:25:23]` you're going to have a complete
`[01:25:23]` understanding of exactly every detail is
`[01:25:26]` understanding of exactly every detail is
`[01:25:26]` is hopeless. Um on the other hand, I
`[01:25:29]` is hopeless. Um on the other hand, I
`[01:25:29]` think there is quite a lot of
`[01:25:30]` think there is quite a lot of
`[01:25:30]` theoretical understanding of, for
`[01:25:31]` theoretical understanding of, for
`[01:25:31]` example, why optimization seems to work
`[01:25:34]` example, why optimization seems to work
`[01:25:34]` in in in large networks, why people why,
`[01:25:37]` in in in large networks, why people why,
`[01:25:37]` you know, the system doesn't seem to be
`[01:25:39]` you know, the system doesn't seem to be
`[01:25:39]` trapped in local minima, for example, uh
`[01:25:42]` trapped in local minima, for example, uh
`[01:25:42]` or, you know, the kind of
`[01:25:42]` or, you know, the kind of
`[01:25:42]` representations that are learned. I have
`[01:25:44]` representations that are learned. I have
`[01:25:44]` something to say about that, too, which
`[01:25:45]` something to say about that, too, which
`[01:25:46]` is um
`[01:25:48]` is um
`[01:25:48]` most of the things people do, we don't
`[01:25:50]` most of the things people do, we don't
`[01:25:50]` know how they work. We have no idea how
`[01:25:52]` know how they work. We have no idea how
`[01:25:53]` they do it. And so, if you replace
`[01:25:55]` they do it. And so, if you replace
`[01:25:55]` people by neural networks, you're no
`[01:25:56]` people by neural networks, you're no
`[01:25:56]` worse off than you were with people. In
`[01:25:58]` worse off than you were with people. In
`[01:25:58]` fact, you're probably you're probably
`[01:25:59]` fact, you're probably you're probably
`[01:25:59]` better off because you can correct for
`[01:26:01]` better off because you can correct for
`[01:26:01]` bias better with a neural network than
`[01:26:02]` bias better with a neural network than
`[01:26:02]` you can with a person. But the other
`[01:26:04]` you can with a person. But the other
`[01:26:04]` thing is there may be some tasks where
`[01:26:06]` thing is there may be some tasks where
`[01:26:06]` you need to use hundreds of thousands of
`[01:26:09]` you need to use hundreds of thousands of
`[01:26:09]` weak regularities in the data to make a
`[01:26:11]` weak regularities in the data to make a
`[01:26:11]` prediction.
`[01:26:13]` prediction.
`[01:26:13]` And there's no simple rules. There's
`[01:26:15]` And there's no simple rules. There's
`[01:26:15]` just lots of weak regularities. And what
`[01:26:17]` just lots of weak regularities. And what
`[01:26:17]` big neural nets do is they use the rule
`[01:26:20]` big neural nets do is they use the rule
`[01:26:20]` and they say, you know, 300,000
`[01:26:22]` and they say, you know, 300,000
`[01:26:22]` regularities say yes and 150,000
`[01:26:24]` regularities say yes and 150,000
`[01:26:24]` regularities say no, so it's probably
`[01:26:26]` regularities say no, so it's probably
`[01:26:26]` yes. And if you ask me, but how did it
`[01:26:28]` yes. And if you ask me, but how did it
`[01:26:28]` do it?
`[01:26:30]` do it?
`[01:26:30]` If you're expecting to get some lines of
`[01:26:31]` If you're expecting to get some lines of
`[01:26:31]` computer code that would compute that,
`[01:26:34]` computer code that would compute that,
`[01:26:34]` you're not going to get it. This neural
`[01:26:35]` you're not going to get it. This neural
`[01:26:35]` network has a billion weights in it and
`[01:26:37]` network has a billion weights in it and
`[01:26:37]` the way it did it was those billion
`[01:26:39]` the way it did it was those billion
`[01:26:39]` weights had these values and that may be
`[01:26:40]` weights had these values and that may be
`[01:26:40]` the best you can get. So, for that kind
`[01:26:42]` the best you can get. So, for that kind
`[01:26:42]` of decision, you're just going to have
`[01:26:44]` of decision, you're just going to have
`[01:26:44]` to live with the fact that people have
`[01:26:45]` to live with the fact that people have
`[01:26:45]` intuitions and their intuitions tell
`[01:26:47]` intuitions and their intuitions tell
`[01:26:47]` them what to do and neural nets have
`[01:26:49]` them what to do and neural nets have
`[01:26:49]` intuitions, too, and they work by having
`[01:26:51]` intuitions, too, and they work by having
`[01:26:51]` the same way they do with people, by
`[01:26:53]` the same way they do with people, by
`[01:26:53]` having large numbers of weights that
`[01:26:54]` having large numbers of weights that
`[01:26:55]` conspire together to say this is more
`[01:26:57]` conspire together to say this is more
`[01:26:57]` likely than that.
`[01:27:00]` Thanks. Uh I know you've been waiting,
`[01:27:01]` so why don't you go ahead and then we'll
`[01:27:03]` so why don't you go ahead and then we'll
`[01:27:03]` take one more from there. Sorry, just
`[01:27:05]` take one more from there. Sorry, just
`[01:27:05]` quick question on other um AI aspects
`[01:27:08]` quick question on other um AI aspects
`[01:27:08]` like evolutionary computation and stuff.
`[01:27:10]` like evolutionary computation and stuff.
`[01:27:10]` Do you have some opinion um where they
`[01:27:13]` Do you have some opinion um where they
`[01:27:13]` whether they will Sorry, I didn't hear
`[01:27:14]` whether they will Sorry, I didn't hear
`[01:27:14]` what you said.
`[01:27:15]` what you said.
`[01:27:15]` AI
`[01:27:17]` AI
`[01:27:17]` fields like evolutionary computation,
`[01:27:19]` fields like evolutionary computation,
`[01:27:19]` for example. Um do you have any opinion
`[01:27:21]` for example. Um do you have any opinion
`[01:27:21]` on those because you sort of mentioned
`[01:27:22]` on those because you sort of mentioned
`[01:27:22]` only symbolic and neural? Did you say
`[01:27:24]` only symbolic and neural? Did you say
`[01:27:24]` evolution? Um like genetic programming,
`[01:27:26]` evolution? Um like genetic programming,
`[01:27:26]` those kind of things. Uh yes. Um
`[01:27:29]` those kind of things. Uh yes. Um
`[01:27:29]` I think it's great for setting hyper
`[01:27:30]` I think it's great for setting hyper
`[01:27:31]` parameters. That is, if you're in a
`[01:27:32]` parameters. That is, if you're in a
`[01:27:32]` high-dimensional space and you want to
`[01:27:34]` high-dimensional space and you want to
`[01:27:34]` improve, if you can get a gradient,
`[01:27:36]` improve, if you can get a gradient,
`[01:27:36]` you're going to do much better than
`[01:27:37]` you're going to do much better than
`[01:27:37]` someone who can't get a gradient.
`[01:27:40]` someone who can't get a gradient.
`[01:27:40]` And the brain is a device for getting
`[01:27:41]` And the brain is a device for getting
`[01:27:41]` gradients, I believe.
`[01:27:43]` gradients, I believe.
`[01:27:43]` Evolution can't get gradients cuz a lot
`[01:27:45]` Evolution can't get gradients cuz a lot
`[01:27:45]` of what determines the relationship
`[01:27:48]` of what determines the relationship
`[01:27:48]` between the genotype and the phenotype
`[01:27:49]` between the genotype and the phenotype
`[01:27:50]` is outside your control. It's the
`[01:27:51]` is outside your control. It's the
`[01:27:51]` environment. So, evolution has to use
`[01:27:54]` environment. So, evolution has to use
`[01:27:54]` techniques like mutation, random
`[01:27:56]` techniques like mutation, random
`[01:27:56]` changes, and recombinations. Um but
`[01:27:59]` changes, and recombinations. Um but
`[01:27:59]` we're not limited to that. We can
`[01:28:00]` we're not limited to that. We can
`[01:28:01]` produce a device that can get gradients.
`[01:28:03]` produce a device that can get gradients.
`[01:28:03]` Now, obviously, if you can get
`[01:28:04]` Now, obviously, if you can get
`[01:28:04]` gradients, um
`[01:28:06]` gradients, um
`[01:28:06]` you can also use evolution to make that
`[01:28:08]` you can also use evolution to make that
`[01:28:08]` device better. And if you look at what
`[01:28:10]` device better. And if you look at what
`[01:28:10]` happens in neural nets now, um you train
`[01:28:13]` happens in neural nets now, um you train
`[01:28:13]` a neural net using gradients. But now
`[01:28:15]` a neural net using gradients. But now
`[01:28:15]` you fiddle with the hyper parameters
`[01:28:17]` you fiddle with the hyper parameters
`[01:28:17]` using something much more like an
`[01:28:18]` using something much more like an
`[01:28:19]` evolutionary technique.
`[01:28:21]` evolutionary technique.
`[01:28:21]` I think we have uh time for one more
`[01:28:23]` I think we have uh time for one more
`[01:28:23]` question from that side.
`[01:28:26]` question from that side.
`[01:28:26]` Thank you. Uh so, um Yann talk about
`[01:28:29]` Thank you. Uh so, um Yann talk about
`[01:28:29]` using CNNs or other types of neural nets
`[01:28:32]` using CNNs or other types of neural nets
`[01:28:32]` in perception for autonomous drive
`[01:28:35]` in perception for autonomous drive
`[01:28:35]` autonomous vehicles and doesn't sound uh
`[01:28:37]` autonomous vehicles and doesn't sound uh
`[01:28:37]` very positive. So, could you make some
`[01:28:39]` very positive. So, could you make some
`[01:28:39]` more comments on that?
`[01:28:41]` more comments on that?
`[01:28:41]` Well, there's been uh
`[01:28:43]` Well, there's been uh
`[01:28:43]` you know, a lot of uh declaration,
`[01:28:45]` you know, a lot of uh declaration,
`[01:28:45]` probably kind of more
`[01:28:46]` probably kind of more
`[01:28:46]` marketing-oriented than science-oriented
`[01:28:48]` marketing-oriented than science-oriented
`[01:28:48]` that uh
`[01:28:50]` that uh
`[01:28:50]` for your autonomous driving is just
`[01:28:51]` for your autonomous driving is just
`[01:28:51]` around the corner. And uh
`[01:28:54]` around the corner. And uh
`[01:28:54]` it's just a lot harder than most people
`[01:28:57]` it's just a lot harder than most people
`[01:28:57]` imagine. A lot of people in the
`[01:28:58]` imagine. A lot of people in the
`[01:28:58]` business, of course, knew it was hard
`[01:28:59]` business, of course, knew it was hard
`[01:28:59]` and it wasn't it it's not just around
`[01:29:01]` and it wasn't it it's not just around
`[01:29:01]` the corner. I think there's a similar
`[01:29:03]` the corner. I think there's a similar
`[01:29:03]` story
`[01:29:04]` story
`[01:29:05]` in a lot of areas of of AI and, you
`[01:29:07]` in a lot of areas of of AI and, you
`[01:29:07]` know, AI as a whole where
`[01:29:09]` know, AI as a whole where
`[01:29:09]` um
`[01:29:10]` um
`[01:29:10]` a lot of people had very optimistic
`[01:29:12]` a lot of people had very optimistic
`[01:29:12]` expectations about like when human-level
`[01:29:14]` expectations about like when human-level
`[01:29:14]` AI will be attained, for example. Uh in
`[01:29:17]` AI will be attained, for example. Uh in
`[01:29:17]` my opinion, it's not just around the
`[01:29:18]` my opinion, it's not just around the
`[01:29:19]` corner. There are
`[01:29:20]` corner. There are
`[01:29:21]` certainly things like,
`[01:29:22]` certainly things like,
`[01:29:22]` uh, you know, how to do self-supervision
`[01:29:24]` uh, you know, how to do self-supervision
`[01:29:24]` properly that need to be figured out
`[01:29:26]` properly that need to be figured out
`[01:29:26]` before that happens, but it's not the
`[01:29:28]` before that happens, but it's not the
`[01:29:28]` only the only obstacles. It's just the
`[01:29:30]` only the only obstacles. It's just the
`[01:29:30]` the first mountain that we see, and
`[01:29:32]` the first mountain that we see, and
`[01:29:32]` there might be a whole bunch of
`[01:29:32]` there might be a whole bunch of
`[01:29:32]` mountains behind that we haven't figured
`[01:29:34]` mountains behind that we haven't figured
`[01:29:34]` out. So, I think it's a little bit the
`[01:29:35]` out. So, I think it's a little bit the
`[01:29:35]` same for, uh,
`[01:29:37]` same for, uh,
`[01:29:37]` uh, for self-self-autonomous driving.
`[01:29:39]` uh, for self-self-autonomous driving.
`[01:29:39]` Autonomous driving, it's easy to get
`[01:29:41]` Autonomous driving, it's easy to get
`[01:29:41]` early impressive results where a car
`[01:29:44]` early impressive results where a car
`[01:29:44]` appears to drive itself pretty well for,
`[01:29:45]` appears to drive itself pretty well for,
`[01:29:45]` you know, about half an hour.
`[01:29:47]` you know, about half an hour.
`[01:29:47]` Uh, but to get the same level of
`[01:29:49]` Uh, but to get the same level of
`[01:29:49]` reliability as humans, which is one
`[01:29:50]` reliability as humans, which is one
`[01:29:51]` fatal accident per 100 miles
`[01:29:53]` fatal accident per 100 miles
`[01:29:53]` per 100 million miles, I'm sorry. Uh,
`[01:29:56]` per 100 million miles, I'm sorry. Uh,
`[01:29:56]` [laughter]
`[01:30:01]` you know, what's 10 to the 6 between
`[01:30:03]` friends? Um,
`[01:30:06]` then it, you know, it's it it it's
`[01:30:08]` really hard to get to that level. And if
`[01:30:09]` really hard to get to that level. And if
`[01:30:10]` you try to sort of extrapolate how much
`[01:30:11]` you try to sort of extrapolate how much
`[01:30:11]` data you need to get to that level by
`[01:30:14]` data you need to get to that level by
`[01:30:14]` sort of seeing how the performance
`[01:30:15]` sort of seeing how the performance
`[01:30:15]` improves as you increase the amount of
`[01:30:16]` improves as you increase the amount of
`[01:30:16]` data, it's basically impractical. So, we
`[01:30:18]` data, it's basically impractical. So, we
`[01:30:18]` have to find new ways of training those
`[01:30:20]` have to find new ways of training those
`[01:30:20]` systems, and I think self-supervision is
`[01:30:22]` systems, and I think self-supervision is
`[01:30:22]` part of the answer. Um, we'll see, okay.
`[01:30:25]` part of the answer. Um, we'll see, okay.
`[01:30:25]` Um, you know, it's
`[01:30:27]` Um, you know, it's
`[01:30:27]` it's a hard problem. You can
`[01:30:28]` it's a hard problem. You can
`[01:30:28]` over-engineer it. Uh, you can add
`[01:30:30]` over-engineer it. Uh, you can add
`[01:30:30]` sensors that make the processing easier.
`[01:30:32]` sensors that make the processing easier.
`[01:30:32]` You can do detailed maps. You can do all
`[01:30:35]` You can do detailed maps. You can do all
`[01:30:35]` kinds of stuff to kind of make it
`[01:30:37]` kinds of stuff to kind of make it
`[01:30:37]` practical in some conditions.
`[01:30:39]` practical in some conditions.
`[01:30:39]` Uh,
`[01:30:39]` Uh,
`[01:30:39]` but fully sort of level five autonomous
`[01:30:41]` but fully sort of level five autonomous
`[01:30:41]` driving is uh is hard.
`[01:30:44]` driving is uh is hard.
`[01:30:44]` Thank you very much. Okay. With that, I
`[01:30:46]` Thank you very much. Okay. With that, I
`[01:30:46]` know many of you have other conference
`[01:30:48]` know many of you have other conference
`[01:30:48]` events to go to. Now we're done with the
`[01:30:49]` events to go to. Now we're done with the
`[01:30:49]` last question. So, I would really like
`[01:30:52]` last question. So, I would really like
`[01:30:52]` to thank, uh, Yann and Jeff once again
`[01:30:54]` to thank, uh, Yann and Jeff once again
`[01:30:54]` for a most memorable Turing lecture.
`[01:30:56]` for a most memorable Turing lecture.
`[01:30:56]` Thank you.
`[01:30:58]` Thank you.
`[01:30:58]` [applause]
`[01:31:03]` [applause]
`[01:31:05]` And
`[01:31:06]` enjoy the rest of the conference,
`[01:31:08]` enjoy the rest of the conference,
`[01:31:08]` including the events that you have this
`[01:31:09]` including the events that you have this
`[01:31:09]` evening.
`[01:31:11]` evening.
`[01:31:11]` But
`[01:31:11]` But
`[01:31:11]` thank you.
