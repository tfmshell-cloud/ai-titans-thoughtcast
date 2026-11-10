# Stanford HAI Fireside: Fei-Fei Li & John Hennessy on 'The Worlds I See'
- **YouTube URL:** https://www.youtube.com/watch?v=HiSK7nv-i94
- **Lines:** 1395

---

[00:00:05] welcome everybody I'm Nate Purley I'm a
[00:00:05] law professor here at Stanford and also
[00:00:06] co-director of the Cyber policy Center
[00:00:09] uh I am the least impressive person
[00:00:11] you're going to hear from tonight uh
[00:00:13] which which is which is why I'm wearing
[00:00:15] a suit um and so uh it is it is a
[00:00:19] wonderful event uh here and it always is
[00:00:23] cause for celebration when one of our
[00:00:25] faculty uh uh publishes a book but
[00:00:27] especially one as uh uh significant and
[00:00:30] I think as influential as the one you're
[00:00:32] going to hear about today uh of course
[00:00:34] it's f f Lees the world's I see uh
[00:00:37] she'll be in conversation with uh John
[00:00:39] Hennessy let me give short introductions
[00:00:42] of of both of our speakers um these
[00:00:45] introductions could go on and on assume
[00:00:48] they have won every significant award in
[00:00:50] their fields and are members of every
[00:00:53] significant Society uh that is honored
[00:00:55] in their profession I I'll say first uh
[00:00:59] so professor F Lee is the inaugural
[00:01:01] Sequoia Professor uh in the computer
[00:01:03] science department at Stanford and
[00:01:05] co-director of Stanford Institute on
[00:01:07] human artificial uh human centered AI uh
[00:01:10] she served as the Director of Stanford's
[00:01:11] AI lab from 2013 to
[00:01:14] 2018 uh and from 2017 to 201 18 was vice
[00:01:19] president of Google and served as Chief
[00:01:21] scientist of aimi AIML at Google cloud
[00:01:24] and labor served as a board member on
[00:01:26] many different uh uh public and private
[00:01:29] companies she's published more than 300
[00:01:31] scientific articles um known to many in
[00:01:34] this room who are her students and uh
[00:01:37] her current research interest pretty
[00:01:39] much span the entire uh uh world of AI
[00:01:42] and machine learning uh she's the
[00:01:44] inventor of imag net and the imet
[00:01:46] challenge a critical large scale data
[00:01:48] set uh uh and benchmarking effort that
[00:01:50] has contributed to the latest
[00:01:51] developments in deep learning and AI um
[00:01:55] I'll say just uh there's so much more
[00:01:57] that one can say about Fay but uh she is
[00:01:59] a leading voice also uh in advocating
[00:02:02] for diversity in stem uh and Ai and as
[00:02:05] co-founder and chairperson of uh the
[00:02:07] national nonprofit AI for all uh which
[00:02:09] is aimed at increasing inclusion and
[00:02:11] diversity in AI education she is
[00:02:13] naturally uh relied upon in all policy
[00:02:16] circles whether you're talking about the
[00:02:17] United Nations Washington here in
[00:02:19] California um for advice on AI policy um
[00:02:23] her new book The World's IC is more than
[00:02:25] just sort of a book about AI it is a a
[00:02:29] real personal narrative about sort of
[00:02:31] connecting uh her experiences uh also to
[00:02:34] the science and the topics that she
[00:02:36] studies um she will talk about her book
[00:02:38] and then she'll be uh joined in
[00:02:39] conversation with uh John
[00:02:42] Hennessy uh I'll make this even really
[00:02:44] short he was appointed here as a
[00:02:46] assistant professor in
[00:02:48] 1977 and then he held many significant
[00:02:50] jobs after that uh uh in the University
[00:02:53] um uh he was Provost he was he was chair
[00:02:57] of the the of computer science uh he was
[00:03:00] uh of course president uh from 2000 to
[00:03:03] 2016 and is in his own right of course
[00:03:06] an expert on computer architecture has
[00:03:07] published widely and as I said has won
[00:03:09] every significant award in the field and
[00:03:11] so thank you all for coming and thank
[00:03:13] you Faithfully for this book now I'll
[00:03:15] turn it over to
[00:03:28] you hi thank you thank you so much for
[00:03:28] coming I I finally realized how how much
[00:03:31] you have went have gone through to get
[00:03:34] here because the traffic was so bad
[00:03:37] getting here so um I'm actually quite
[00:03:40] embarrassed honestly I never thought I
[00:03:42] would be you know doing this for for the
[00:03:45] book it this literally came about and I
[00:03:48] want to thank Nate and our good friend
[00:03:51] Professor Rob re who's teaching right
[00:03:53] now um that we were having lunch about
[00:03:56] two months ago and uh Nate and Ro
[00:04:00] both prolific authors and incredible
[00:04:03] scholars in different part of the campus
[00:04:05] that I'm I'm familiar with as me how my
[00:04:08] book is going and I said it's it it's
[00:04:11] publishing and they're like we need a
[00:04:13] book party I'm like what is a book party
[00:04:16] in computer science when you publish a
[00:04:19] eight page neuro reps paper that is a
[00:04:22] party I never thought there's such a
[00:04:25] thing as book party and Nate and Rob
[00:04:27] just said leave it to us and uh nay I I
[00:04:31] I know you even changed the flight for
[00:04:33] me so thank you so so so much I'm I'm
[00:04:36] deeply deeply grateful for this kind of
[00:04:38] wonderful colleagues um um John Hennessy
[00:04:43] thank you so much for willing to do this
[00:04:45] with me we were saying off stage that
[00:04:48] really it's not that interesting to hear
[00:04:50] me talking so most of this will be a
[00:04:53] dialogue of two generations of computer
[00:04:56] scientists um and giving that just a
[00:04:59] overview you and a a a a honest
[00:05:01] conversation of where we are with the
[00:05:04] world of AI but I do want to use this
[00:05:07] opportunity to thank some people because
[00:05:10] you know we're so busy in life and uh so
[00:05:14] busy making things building things uh
[00:05:16] trying to study things we don't really
[00:05:19] stop and and and thank people and since
[00:05:22] I have a little few more minutes here I
[00:05:24] really think it's it's my honor and and
[00:05:27] and my duty really to thank the people
[00:05:30] who have really helped me and uh um I
[00:05:34] want to start with a very special person
[00:05:37] um You probably wonder why I'm holding
[00:05:39] this book because of course she's got a
[00:05:41] 100 book in her office she's holding one
[00:05:44] actually I'm holding a book signed by
[00:05:47] the co-writer of this book and this book
[00:05:51] will not come to life if I didn't have
[00:05:55] my very very good friend and uh and
[00:05:58] colleague and partner
[00:06:00] for 3 years during this whole pandemic
[00:06:03] and writing every word with me telling
[00:06:06] this story and I really want to thank
[00:06:08] Alex Michael please stand up I want
[00:06:11] everybody to
[00:06:21] meet I I really because um you might
[00:06:21] wonder you know she only came to this
[00:06:23] country when she was 15 how could she
[00:06:25] write this well well I
[00:06:28] didn't and
[00:06:30] and I do feel proud of this creative uh
[00:06:32] process that Alex and I engaged in but
[00:06:36] but you know without Alex this book
[00:06:38] could not have been um could not have
[00:06:40] been around of course in the uh in
[00:06:43] writing this book there is another
[00:06:45] special person I need to um thank
[00:06:48] there's many reasons I need to thank him
[00:06:50] but that he played a very important role
[00:06:52] Alex and I wrote this book at an
[00:06:54] invitation of a book agent and publisher
[00:06:57] and we're talking about AI I was N I was
[00:07:00] in excited by telling what AI is to the
[00:07:03] public we wrote for a whole year and
[00:07:06] then I was so excited we're done I don't
[00:07:09] know I don't even remember when was that
[00:07:12] 2021 we give it to my dearest friend
[00:07:17] Mentor colleague partner another very
[00:07:21] famous person on campus professor John
[00:07:25] HMI and where is he where is John oh hi
[00:07:31] but don't clap yet you you have to hear
[00:07:33] this
[00:07:35] story I give it to him he called me and
[00:07:38] Alex and said okay it's co come over to
[00:07:40] my backyard I need to talk to you guys
[00:07:43] so we went to his backyard and he held I
[00:07:46] I don't know some printed copy of our
[00:07:49] manuscript and said this is no good go
[00:07:51] back and
[00:07:59] rewrite Alex and I just turned pale and
[00:07:59] uh and then uh John said something that
[00:08:01] I was so reluctant to to admit but he
[00:08:05] would he would have been the only single
[00:08:06] person who can convince me of that he
[00:08:09] said many AI scientists and
[00:08:12] technologists can write this book but um
[00:08:15] there are so many young women young
[00:08:18] people immigrants people of all walks of
[00:08:21] life out there who need to identify with
[00:08:24] the voice that is not a typical AI voice
[00:08:28] and you have a journey that you need to
[00:08:31] share with with these people and when
[00:08:35] John said that I was just like my
[00:08:38] stomach was turning because I know he
[00:08:41] want me to write a memoir and that's
[00:08:43] everything I didn't want to write in the
[00:08:46] meantime Alex was jumping up and down
[00:08:49] next to me and say I told
[00:08:58] you and of course Alex also said it only
[00:08:58] take John atmy to convince you so I
[00:09:01] don't know if John convinced me but I
[00:09:04] listen to JN so so John I there are many
[00:09:07] things I want to thank you but you have
[00:09:10] been an incredible mentor and friend
[00:09:13] even for this book this book would would
[00:09:16] would not exist without you I know I I
[00:09:19] don't know how I can thank you enough
[00:09:22] you you you have you mean a world to me
[00:09:24] for for what I'm doing here at Stan
[00:09:28] Stanford thank you doc
[00:09:33] so so in my acknowledgement for this
[00:09:35] book I wanted to thank a lot of people
[00:09:39] who helped me to publish and some of you
[00:09:42] actually are in the audience in the
[00:09:44] course of this book you have read
[00:09:47] different uh versions I I don't know who
[00:09:50] are in the in the audience but please
[00:09:52] raise your hand if you have given me
[00:09:54] advice in the course of the book so I I
[00:09:57] I know I knows oh God Terry okay
[00:10:02] everybody Professor Terry Winograd
[00:10:06] [Applause]
[00:10:09] um Professor teror Winograd
[00:10:13] is okay we'll start with he read parts
[00:10:16] of the book and give me very very good
[00:10:19] advice part of it is because he's in the
[00:10:21] book and even if you're not interested
[00:10:24] in faith Journey you should read this
[00:10:26] book because Professor Terry winegrad is
[00:10:28] in the book he is a hero of mine he is
[00:10:31] one of the founding fathers of AI he he
[00:10:34] really has we talked about his early
[00:10:37] working Ai and on top of that he was
[00:10:40] really unfortunate to be my neighbor so
[00:10:44] and Ed John M's neighbor so so Terry
[00:10:47] thank you so much for helping me with
[00:10:49] the book uh who else is in the audience
[00:10:52] who has uh read this uh who has given me
[00:10:55] advice some of I know some of them are
[00:10:58] are um working and traveling and and uh
[00:11:01] but I want to thank everybody who who
[00:11:03] was in the creative process of this book
[00:11:06] the title is the worlds I see I have two
[00:11:09] more worlds I really want to I really
[00:11:11] want to thank um one of the world is the
[00:11:14] world of science and the world of
[00:11:16] science began with the people like
[00:11:18] Newton Einstein Mary cury um um schinger
[00:11:24] Maxwell so many of them I want to thank
[00:11:27] them even though they don't need I think
[00:11:29] they won't hear me maybe but but they
[00:11:34] really open a world that is infinitely
[00:11:38] curious Whimsical and inspiring for me
[00:11:42] and uh that was the beginning of my my
[00:11:44] journey but in the in the AI world I
[00:11:48] have so many mentors and uh and
[00:11:52] colleagues so many of you honestly are
[00:11:54] in this audience I I just cannot see all
[00:11:57] of you sorry um that um that I I know
[00:12:00] how much you know you you guys have
[00:12:03] helped me many people ask me fa tell me
[00:12:07] how lonely it is to be a woman in
[00:12:09] technology I do feel it's important to
[00:12:12] talk about this but I really want to say
[00:12:15] it's not that lonely at my mentors and
[00:12:18] my advisers have helped me so much that
[00:12:22] uh without them I wouldn't be where I am
[00:12:25] um I want to give shout out to my um PhD
[00:12:28] adviser Professor petro perona and
[00:12:30] Professor Kristoff cooch you know they
[00:12:33] they they really led me into the door I
[00:12:36] want to thank some of the mentors I do
[00:12:38] want to read their names some of you
[00:12:40] might identify but um uh Professor Diane
[00:12:43] Beck from UI Professor Bill DOL who
[00:12:46] hired me to Stanford um uh Diane Green
[00:12:51] uh professor John Hennessy uh Professor
[00:12:54] Jeff Hinton Professor Daphne CER the
[00:12:57] first uh uh B as AI woman I ever knew um
[00:13:02] um Professor Kye co-author of image net
[00:13:05] and unsung hero in this uh in this
[00:13:08] journey Professor jendra Malik Professor
[00:13:11] Arie milting who is a uh clinical
[00:13:15] researcher um uh at Stanford Stanford
[00:13:19] Professor Andrew n Professor Sebastian
[00:13:21] thron and uh and then so many people in
[00:13:27] Stanford Institute for uh for uh uh
[00:13:30] human Center AI especially the founding
[00:13:34] professors uh and colleagues Professor
[00:13:36] JN hmy Professor James land Professor
[00:13:40] Chris Manning professor suria ganguli
[00:13:43] professor Rob re Professor Michelle ilam
[00:13:46] Professor Susan NY Professor um um um
[00:13:51] Eric pson Professor Dan ho uh uh
[00:13:55] Professor Russ Altman Professor Kurt
[00:13:58] langlet
[00:13:59] uh uh and and many more and everybody at
[00:14:03] Stanford hii um is uh means a lot to me
[00:14:08] and this book wouldn't be here without
[00:14:10] them then I have a very special group of
[00:14:13] people I know that they are scattered
[00:14:16] around the world and many of them are
[00:14:19] doing far greater things that I have
[00:14:21] ever dreamed of and they're my students
[00:14:24] and uh post dos and advises and in the
[00:14:28] book I have acknowledged a very small
[00:14:30] subset of them I know some of you former
[00:14:34] students as well as current students are
[00:14:36] in the audience I really would
[00:14:38] appreciate if you stand up
[00:14:40] because could you please stand up I know
[00:14:43] you're shy I I see some of you keep
[00:14:46] standing
[00:14:55] I we have don't don't oh come on keep
[00:14:55] standing
[00:15:00] up we have many professors here you guys
[00:15:00] don't understand you make us you make
[00:15:04] our career you make our world and uh and
[00:15:09] every single Pixel in my world and
[00:15:12] that's our inside language is is
[00:15:14] colorful because of you I take the
[00:15:17] greatest Pride to have worked with you
[00:15:19] and to have been through a part of the
[00:15:22] journey with you I also want to shout
[00:15:23] out to Juan
[00:15:25] Carlos um who's sitting here let just
[00:15:29] say hi one more time
[00:15:32] uh um you see how little hair he has now
[00:15:36] um I Met Juan Carlos I met H Juan Carlos
[00:15:40] as a clueless assistant professor in
[00:15:42] Urbana champagne he was my very first
[00:15:46] PhD
[00:15:47] student and H Carlos came to this
[00:15:50] country from Colombia on a full bright
[00:15:52] scholarship he didn't know anything I
[00:15:54] didn't know
[00:15:57] anything was a match meting heaven and
[00:16:01] uh and uh and now Juan Carlos is a a a
[00:16:05] renowned uh uh researcher in computer
[00:16:08] vision a director at Salesforce lab and
[00:16:11] aent faculty at Stanford computer
[00:16:13] science department and uh this is the
[00:16:16] kind of human relationship that uh I
[00:16:18] feel so so proud of so thank you Juan
[00:16:21] Carlos for in trusting me and thank you
[00:16:23] all my students who for still
[00:16:25] interesting me so um the the the the
[00:16:30] most special world for me obviously is
[00:16:33] the world of love and support and uh um
[00:16:37] someone earlier today just told me that
[00:16:39] this book is a love letter and I think
[00:16:42] when Alex and I are writing this book we
[00:16:44] actually did call this book a love
[00:16:46] letter and uh it's a love letter for
[00:16:49] science from a little girl who somehow
[00:16:53] just fell in love in science but it's
[00:16:55] also a love letter for the people who
[00:16:57] have made my life possible and um and um
[00:17:03] if and I hope you read at least some
[00:17:06] part of this book there's a person who
[00:17:09] is very special in this book in fact
[00:17:12] today I just got photos of his grandkids
[00:17:17] going to a New Jersey local bookstore
[00:17:19] holding this book and they are sent to
[00:17:21] me and that's Mr Bob Sabella he is he
[00:17:24] was a high school math teacher in pery
[00:17:27] New Jersey I met him when I was 15 I
[00:17:31] barely spoke English he was this badass
[00:17:35] math teacher with a Brooklyn accent
[00:17:38] speaking at the speed of light and I did
[00:17:40] not understand a word he said and um he
[00:17:44] gave me a lot of tests to do and I got
[00:17:47] half of the tests right because the
[00:17:50] other half with words a lit I didn't
[00:17:53] understand so so that's how our journey
[00:17:56] begin and and for a kid who didn't know
[00:18:01] the language who didn't know anything
[00:18:03] about this country he took me in as a
[00:18:07] uncle as a father as a teacher his whole
[00:18:10] family embraced me there are stories of
[00:18:14] uh Mr Bob Sabella in this book that uh I
[00:18:18] but every time Alex and I write we we
[00:18:20] were in tears so I hopefully you'll
[00:18:23] identify and they really symbolize this
[00:18:26] country for me this country is not the
[00:18:28] shiny gadgets Silicon Valley made this
[00:18:32] country is not those giant skyscrapers
[00:18:34] in financial district of Manhattan that
[00:18:38] I didn't even have money to pay for
[00:18:40] parking to visit this country is the
[00:18:43] public high school math teachers like
[00:18:47] Bob who has the Heart of Gold who
[00:18:50] Embrace students from every corner of
[00:18:52] the world who just put all their heart
[00:18:56] who give us the value of of respect of
[00:19:00] freedom of you know um of um community
[00:19:05] and that's what I identify with so so I
[00:19:08] Mr Sabella or Bob as I call him now uh
[00:19:12] passed away and uh but today I was
[00:19:16] looking at his family's uh group chat
[00:19:19] they sent it to me and I really really
[00:19:23] hope that I have made him a little bit
[00:19:25] proud for for uh you know after all this
[00:19:28] year years so
[00:19:30] um I I also want to um there are so many
[00:19:35] people I cannot thank now but I do want
[00:19:37] to thank two people who they don't
[00:19:41] understand my world um because I do this
[00:19:44] fancy AI or whatever math equations and
[00:19:47] and software programs but they actually
[00:19:51] made the world for me and
[00:19:59] um and you know I come from a Chinese
[00:19:59] background in Chinese family we never
[00:20:02] say cheesy things to each
[00:20:09] other I love you I've never said you
[00:20:09] know I love you Mom and Dad but um um if
[00:20:13] you read this book a lot of this
[00:20:17] um the grounding of my human
[00:20:20] centeredness come from them and come
[00:20:23] from the journey we've taken
[00:20:26] together and
[00:20:33] Alex when Alex and I are writing this
[00:20:33] book we were both writing for our mom um
[00:20:36] both of moms are are battling with
[00:20:39] Health Care issues and uh that also made
[00:20:42] Alex such a special partner and uh uh
[00:20:46] both Alex and I were racing against time
[00:20:49] we feel because we don't know if our
[00:20:51] moms will see this book and I know Alex
[00:20:54] your mom didn't get to see the final
[00:20:57] version and uh it is a a loss between us
[00:21:01] but I'm very lucky that I still have my
[00:21:04] parents here today and despite their
[00:21:07] health conditions they actually came for
[00:21:10] me today and I really want to
[00:21:13] acknowledge
[00:21:25] them and
[00:21:25] uh in my acknowledgement I I said that
[00:21:29] my parents Brave the darkness so I can
[00:21:32] seek light and I think in all of our
[00:21:35] Lives if you search in your lives there
[00:21:38] are people who have bra braved Darkness
[00:21:41] for you that's when you that's how you
[00:21:44] can seek light I really hope that uh you
[00:21:48] also reflect on that and feel grateful
[00:21:51] and for me thank you so much um my
[00:21:54] parents and uh I think it's one of those
[00:21:57] moments
[00:21:58] uh we won't say it in our living room
[00:22:00] but I'll say it in public how much I
[00:22:03] love
[00:22:03] [Laughter]
[00:22:12] you okay so I'm almost done here sorry
[00:22:12] JN I'm I'm almost done here so Alex Alex
[00:22:16] and I when we wrote this book we thought
[00:22:18] a lot about what AGI is because this
[00:22:21] word right like my students we we almost
[00:22:24] laugh at this word because our founding
[00:22:26] fathers of a I did a have the word AGI
[00:22:30] AI is audacious audacious um um a dream
[00:22:36] of making machines think and do and uh
[00:22:41] but but what is Agi I don't know but if
[00:22:45] there is a embodiment of
[00:22:48] AGI um that that kind of embodiment
[00:22:52] would be a person with not person
[00:22:55] something with so much wisdom
[00:22:58] with all the virtues of humans patience
[00:23:03] strength resilience love compassion with
[00:23:08] the com competency that at least I
[00:23:11] cannot dream of they can do all the
[00:23:15] great work they can cook the best food
[00:23:18] they can you know compose music they can
[00:23:22] you know garden design a zen garden they
[00:23:25] can raise kids and and all that
[00:23:28] I don't know if we'll ever get to AGI
[00:23:31] but that is my
[00:23:33] model intelligence model being and I
[00:23:37] have that special person in life he is a
[00:23:40] fellow AI scientist he is my best friend
[00:23:45] he's my soulmate and he's my children's
[00:23:48] father and that's
[00:23:55] [Applause]
[00:23:56] siio and
[00:23:59] and last but not the least um The Love
[00:24:02] Letter really is for the future
[00:24:04] generation um some of the future
[00:24:06] generation are my students but the most
[00:24:09] special future generation are my
[00:24:11] children and uh um I I sometimes wonder
[00:24:16] what world I'm making for them honestly
[00:24:19] I wonder what is going to happen and
[00:24:22] then I realize the best thing we can
[00:24:25] make for them is the love we can give
[00:24:28] them and uh I hope that my kids get to
[00:24:33] experience their parents and their
[00:24:35] parents friends love for what we do and
[00:24:39] love for the people around us for the
[00:24:41] community and love for the world and uh
[00:24:45] um can you wave to everybody Leo and
[00:25:00] Phoenix okay I'm done thank you so much
[00:25:00] I I honestly I I I really I'm so
[00:25:04] thankful you indulge me I I don't know
[00:25:06] what's the best occasion to thank so
[00:25:08] many people who have made me who I am
[00:25:11] and this is longer than I thought but
[00:25:14] really um I I I'm so grateful you're
[00:25:17] here and I actually look forward to
[00:25:19] having a a conversation with Jong thank
[00:25:30] you which seat have a seat F doesn't
[00:25:30] matter all
[00:25:31] right so fa you you saved me a lot of
[00:25:35] hard work because I was going to make
[00:25:36] you talk about your parents if you
[00:25:38] didn't talk about them so uh but I think
[00:25:42] tell us about the early part of your
[00:25:44] life I mean you're growing up in China
[00:25:46] in chendu by then right what what was it
[00:25:49] like to be a young growing girl
[00:25:52] interested in math and physics at that
[00:25:54] time you know um I I still hope you read
[00:25:58] my book but you should read it anyway CU
[00:26:01] there's a lot of great stories there are
[00:26:02] just so many great stories yeah but um
[00:26:05] you know it was in the I grew up in the
[00:26:07] 80s in China I was born in Beijing and
[00:26:09] my parents brought me to my mom's
[00:26:11] Hometown chandu and it was a very modest
[00:26:14] City it there wasn't much of a much
[00:26:18] material means globalization hasn't hit
[00:26:21] at least hasn't well it hasn't hit the
[00:26:23] world but it hasn't hit China it was
[00:26:26] relatively simple
[00:26:28] but there is a sharp contrast that I the
[00:26:31] book tries to um describe is the freedom
[00:26:36] the freedom not because of the world I
[00:26:38] lived in the freedom that of my family
[00:26:41] life somehow especially my father is a
[00:26:44] very free spirited person and I lived in
[00:26:48] a world of let's find the next bug you
[00:26:51] know um um my dad the book the best Alex
[00:26:56] and my favorite story story of the book
[00:26:58] is when my dad tells me about his pet
[00:27:01] bear as a as a as a child and I just I
[00:27:06] was just given so much intellectual not
[00:27:10] intellectual Cur curiosity freedom and
[00:27:13] yet the school was very serious you know
[00:27:17] the the there's a lot of math actually
[00:27:20] and uh uh and uh science I but I lived
[00:27:24] in this contrast between a free home
[00:27:28] life and a very rigorous disciplined um
[00:27:33] schooling and somehow I think now I kind
[00:27:36] of embody that and and made me sometimes
[00:27:40] too intense maybe no but I I get the
[00:27:42] impression from the book that a lot of
[00:27:44] your creativity comes as inspiration
[00:27:47] from your parents yes I again I think
[00:27:51] it's because they let me it's not like
[00:27:54] they showed me this particular thing
[00:27:56] they just kind of of let me they didn't
[00:27:59] box me um into anything they think they
[00:28:03] want me to be or my teacher wanted me to
[00:28:06] be in in fact I think they almost took a
[00:28:10] little pride for seeing the rebellious
[00:28:12] fa and that's as a parent now I feel
[00:28:16] that is so precious it it absolutely is
[00:28:20] so when you arrive in the US how many
[00:28:24] English words do you know at that point
[00:28:32] put it this way I had to watch who goes
[00:28:32] into restrooms to figure out which
[00:28:35] restroom I should
[00:28:38] go yes okay so pretty small vocabulary
[00:28:41] pretty small vocabulary but you were
[00:28:45] even as a high school student you
[00:28:46] thrived even though you started with
[00:28:49] this giant disadvantage compared to many
[00:28:51] of your fellow students I don't know JN
[00:28:54] I I still remember my rank at py High
[00:28:57] high school was six when I I had a lot
[00:29:00] of eso class that didn't help cuz you
[00:29:03] know you have to do AP to get those
[00:29:06] weighted and I you know I did do some AP
[00:29:09] but not enough um so I first of all for
[00:29:14] those young people out there or parents
[00:29:16] of young
[00:29:18] people my own experience tells me you
[00:29:21] can never
[00:29:22] underestimate the
[00:29:25] resilience and the creativity of young
[00:29:28] people you have to believe in that I
[00:29:31] honestly right now I don't know how I
[00:29:33] did it I really don't you know it's I
[00:29:36] don't feel I'm special I feel hard work
[00:29:39] yes just hard work but there is if you
[00:29:42] if you give that fire in the belly to
[00:29:44] yourself or allow your kid to have that
[00:29:47] fire in the belly the level of
[00:29:49] resilience and creativity is
[00:29:51] unbounded so in the title you talk about
[00:29:55] the dawn of AI and yet AI had a long
[00:29:59] history for that and a series of what we
[00:30:01] sometimes call AI Winters yes um these
[00:30:04] periods of where where there were great
[00:30:05] expectations but they didn't get
[00:30:08] fulfilled what's the break what happened
[00:30:10] that really changed that what was the
[00:30:12] fundamental breakthrough that were
[00:30:14] breakthroughs that really made a
[00:30:15] difference well you know the answer but
[00:30:17] you're just I know but I'm getting it WR
[00:30:19] everybody
[00:30:20] else I want to hear your answer baby but
[00:30:23] but but I do want to talk about one
[00:30:25] thing about AI winter so when I arrived
[00:30:28] in America it's '90s 1990s it we were
[00:30:31] smack in the middle of the AI winter I
[00:30:34] of number four or something like that
[00:30:36] right something like the latest AI
[00:30:37] winter I had no idea less than 30 miles
[00:30:42] away from pppery New Jersey was Bell
[00:30:46] labs and was where Yang laon was making
[00:30:49] convolutional new network it is kind of
[00:30:53] it gives me goosebumps that when I was
[00:30:56] studying English English 30 miles away
[00:31:00] having no idea how our lives would have
[00:31:02] collided new network was being made in
[00:31:05] New Jersey and uh but that was still
[00:31:08] winter neural network didn't fully work
[00:31:11] it worked in recognizing digits digits
[00:31:14] right very simple problem right um and
[00:31:17] uh and um so I arrived in Grass School
[00:31:22] Y2K the year 2000 I think actually as
[00:31:25] you know the public still think it's AI
[00:31:28] winter but I was I think it's the
[00:31:29] beginning of the change there are couple
[00:31:32] of things that are changing um first of
[00:31:34] all machine learning become the lingua
[00:31:37] def franka right like um everybody's
[00:31:39] working on it right suddenly we found a
[00:31:41] mathematical language statistical
[00:31:43] modeling because the the the earlier
[00:31:46] Winters were logic based the first loer
[00:31:48] logic expert systems and all that but
[00:31:51] machine learning really start to change
[00:31:54] and I was one of the first generation uh
[00:31:57] of students who who are using this
[00:31:59] language now second thing is internet
[00:32:02] was happening right you know I still
[00:32:04] remember being second year graduate
[00:32:06] student my fellow grad student said have
[00:32:09] you use a search engine for papers
[00:32:11] called Google you know and internet
[00:32:14] brought data we didn't realize that
[00:32:18] but internet will change the way we view
[00:32:22] data and of course Morse law was
[00:32:24] carrying us right right so lots more
[00:32:27] Hardware than we expected early on but
[00:32:29] then data data is the big right so it
[00:32:32] took I would say less than a decade
[00:32:35] image that was perceived in 2007 uh
[00:32:39] neural network the Deep learning I
[00:32:40] remember Jeff hinton's deep was it
[00:32:43] jeffan they coined the term deep
[00:32:45] learning that paper was 2006 yes 2006 I
[00:32:48] think 2006 and uh GPU oh God when was
[00:32:54] the first GPU here in oh around the same
[00:32:56] time 2008 probably right so even though
[00:32:59] the public was not aware but these three
[00:33:02] important ingredients were being made in
[00:33:05] the first decade of uh the century and
[00:33:09] the of course the watershed moment was
[00:33:12] 2012 when Jeff hinton's students won the
[00:33:15] imag net challenge right so talk about
[00:33:18] the importance of imag net how did you
[00:33:20] get this idea and what motivated you
[00:33:22] because it without that it's not clear
[00:33:25] that we would have known that it was
[00:33:26] really a break
[00:33:27] through yeah um so again please read the
[00:33:36] book we're tempting that Alex and I
[00:33:36] spent so much time writing
[00:33:39] it I feel like a Academia academic
[00:33:43] always said please bring my
[00:33:45] paper and so uh what happened is there
[00:33:49] is a person who's very special in the
[00:33:52] book He's not personally special but
[00:33:55] he's intellectually
[00:33:57] special his name is IR Beerman he's a
[00:34:00] cognitive scientist the psychologist who
[00:34:02] was living uh University of South Carol
[00:34:05] uh California and uh I was a graduate
[00:34:09] student looking at this problem of
[00:34:11] computer vision you know AI was broken
[00:34:13] into little Fields natural language
[00:34:15] processing computer vision I was really
[00:34:17] interested in the fundamental Northstar
[00:34:20] of computer vision and I thought that
[00:34:22] trying to do a object recognize the
[00:34:25] world's object is a Northstar I remember
[00:34:27] soio and I were fellow graduate students
[00:34:29] we were debating soio is like 3D
[00:34:32] structor of the world is the Northstar
[00:34:35] and I was like recognition well now soio
[00:34:37] is winning the war because now it's all
[00:34:39] 3D but at that time is uh it it was uh
[00:34:43] really trying to make sense of the
[00:34:45] objects I think we're all working on
[00:34:48] these tiny um data sets right I remember
[00:34:51] my PhD advisor Petro perona gave me a
[00:34:53] data set of four objects airplane
[00:34:56] leopard
[00:34:57] car side view of car and and and cowtech
[00:35:02] student human face data set it's a and
[00:35:06] then Earth Beerman had this paper in
[00:35:10] 1983 that no one is noticing the paper
[00:35:13] the preprint had has Type has typed
[00:35:17] figures and he estimated 30,000
[00:35:21] categories of objects is what humans see
[00:35:24] actually young humans like by age six
[00:35:27] you can see that and somehow I noticed
[00:35:30] that number and since I I call this the
[00:35:33] Beerman number it really really bugged
[00:35:36] me for years I don't know how to square
[00:35:39] away beerman's number from the entire AI
[00:35:43] world of tiny data and it took me two or
[00:35:47] three years to just keep thinking about
[00:35:50] what this number means to us means to AI
[00:35:54] till I arrived in Princeton as assistant
[00:35:57] professor and at that time machine
[00:36:00] learning was around for a long time I
[00:36:03] start noticing John I start to be honest
[00:36:05] I start noticing that I'm writing papers
[00:36:08] that's all just variations of some kind
[00:36:11] of baset or support Vector machine I
[00:36:15] feel like it's not breakthrough you know
[00:36:17] we're always overfitting we're not
[00:36:20] generalizing we're tweaking the the the
[00:36:23] the in the technical jargon the the
[00:36:25] variables the representations but
[00:36:27] they're not they're not doing the right
[00:36:30] thing till my students and I realized we
[00:36:33] have to hit a re reset button and look
[00:36:36] from a different angle and that angle is
[00:36:38] the Big Data angle and then when we
[00:36:40] thought about that beerman's number came
[00:36:43] back and there was a Serendipity of
[00:36:47] image net was literally a project
[00:36:50] someone already someone else was doing
[00:36:53] and but they're doing it without
[00:36:56] thinking about Big Data they're just
[00:36:57] doing it for word net which is a
[00:37:00] linguistic data set of lexans organized
[00:37:04] not in alphabetical order but in a group
[00:37:08] uh order tonomy like a a German shepherd
[00:37:12] and a golden
[00:37:13] retriever actually that's bad example a
[00:37:16] German shepherd and a terrier would be
[00:37:18] very far from each other in a dictionary
[00:37:21] but very close to each other in word net
[00:37:24] and uh and uh there was a undergraduate
[00:37:27] project in a wordnet group of finding
[00:37:30] one photo per word to show what a golden
[00:37:35] retriever is and quickly they gave up
[00:37:37] that project and I just happen to have
[00:37:40] heard of this word image that that
[00:37:42] nobody wanted to use and I asked the the
[00:37:45] professor to give me that uh give me
[00:37:48] that um name and I with that beautiful
[00:37:52] name that I didn't claim credit I
[00:37:56] thought about beerman's number thought
[00:37:58] about Big Data thought about machine
[00:37:59] learning and that's the
[00:38:02] beginning and you you decided to
[00:38:04] crowdsource it because you needed to get
[00:38:06] a much larger and at that time
[00:38:09] crowdsourcing was kind of still a new
[00:38:11] thing I did not decide to Crow I was
[00:38:14] actually
[00:38:15] cluelessly delusional I thought I would
[00:38:18] hire undergrads to do this Princeton
[00:38:21] undergrads they're very expensive that's
[00:38:24] the
[00:38:25] problem
[00:38:27] yeah so I thought I would put some
[00:38:30] monitors in my lab and hire undergrads
[00:38:33] to download pictures and just click on
[00:38:36] it and it didn't go anywhere we were
[00:38:39] estimating 19 years or
[00:38:42] something and then I had another student
[00:38:44] say let's just use machines to do it the
[00:38:47] machine can do some photo recognition we
[00:38:50] thought that was a brilliant idea but
[00:38:51] after a week we're like wait a minute
[00:38:54] the whole point is machines cannot
[00:38:56] recognize you you want you need gr truth
[00:38:59] here so exactly so I was
[00:39:03] pretty I was pretty stuck till a
[00:39:07] Stanford Master student who transferred
[00:39:09] to Princeton said this is where Silicon
[00:39:13] Valley really is so beautiful the stford
[00:39:15] message I heard there's startups using
[00:39:18] this thing called Amazon Mechanical Turk
[00:39:21] and in Princeton New Jersey I had not
[00:39:23] heard of this and I went to I really
[00:39:26] remember John I went to my computer I
[00:39:29] typed Amazon Mechanical Turk when I saw
[00:39:32] it was a online Market of global workers
[00:39:37] working on anything you can put up I I I
[00:39:40] couldn't sleep that night I knew I found
[00:39:44] my entire world of uh helpers right
[00:39:47] right so I ditched the princet the
[00:39:50] undergrads so much that they're better
[00:39:53] uses of than
[00:39:55] probably so let let's talk about your
[00:39:59] involvement and your interest in the in
[00:40:01] the human side of AI because I think we
[00:40:04] all think about this but there there are
[00:40:06] so many complex issues um what do you
[00:40:09] what do you what do you worry about in
[00:40:12] terms of deploying Ai and what do you
[00:40:14] think is
[00:40:16] overhyped yeah so so I have a confession
[00:40:20] on behalf of my generation of computer
[00:40:23] scientists we were never trained in
[00:40:27] ethics maybe some of you have on your
[00:40:30] own have taken ethics classes but I was
[00:40:33] busy taking physics class or math class
[00:40:36] or electrical engineering class computer
[00:40:39] science class so and then we love AI for
[00:40:43] its technical origin right so all seemed
[00:40:47] very well till I think it was around
[00:40:51] 2017 uh 2017 I had the honor to work at
[00:40:56] Google at Google Cloud it was incredible
[00:41:00] experience if in Cloud business you
[00:41:03] basically serve every single business
[00:41:06] Under the Sun every vertical you work
[00:41:08] with hospitals you work with media
[00:41:10] companies you work with gas and oil
[00:41:13] company you work with the insurance
[00:41:14] company you work with developers we were
[00:41:17] working with a Japanese cucumber
[00:41:19] developer uh farmer who is using you
[00:41:21] know tensor flow you just work and then
[00:41:25] you start to realize
[00:41:27] I start to realize oh my God this
[00:41:29] technology is going to change
[00:41:31] everybody and before I even woke up to
[00:41:35] that we start to have a techlash we
[00:41:38] start to hear Cambridge analytica we
[00:41:42] start to have the F first self-driving
[00:41:44] car death we start to see biased facial
[00:41:48] recognition algorithms are are are
[00:41:51] making really hor horrendously horrible
[00:41:55] you know predictions of human faces and
[00:41:58] we've had our own share of debates on AI
[00:42:02] and defense and all that and that was
[00:42:04] really a wakeup call for me that we have
[00:42:08] entered the messiness of putting this
[00:42:12] technology out to to to the world math
[00:42:16] is beautiful and simple 1 plus one
[00:42:18] equals 2 but technology in human world
[00:42:22] is not simple it's messy it it has
[00:42:26] opportunities but it has consequences
[00:42:28] and that's when you know John I came to
[00:42:30] your office I went to John hm's office I
[00:42:33] went to I don't know if James Landy
[00:42:36] Chris Manning are here where's James I
[00:42:38] saw James oh hi James I was in James
[00:42:41] kitchen all the time uh after my Google
[00:42:44] daytime work talking about this
[00:42:46] messiness I was talking to John LaVine I
[00:42:49] remembered and uh we start to realize we
[00:42:53] have entered a new era this era
[00:42:56] technology and humans are coming much
[00:42:58] closer we have a different
[00:43:00] responsibility not only to continue to
[00:43:03] develop this technology but to
[00:43:05] understand what is going on to
[00:43:07] understand how we can use it to
[00:43:09] understand the human consequences to
[00:43:12] opportunities um and that's when I feel
[00:43:17] that I myself turned from a pure
[00:43:20] technology scientists into a
[00:43:24] hybrid um scientist and and humanist
[00:43:28] amateur humanist so do you worry I mean
[00:43:31] some people have said there's this
[00:43:33] existential threat to human existence I
[00:43:35] mean it's a h sort of vision of right
[00:43:38] the computer takes over and you can't
[00:43:40] even unplug it do you worry about that
[00:43:42] or you worry about more about the short
[00:43:44] to medium term misuses I think of the
[00:43:46] technology is probably the right the
[00:43:48] right term right it's both errors in the
[00:43:50] technology but there're also misuses of
[00:43:52] the technology yeah so that's a totally
[00:43:55] a fair question question I was talking
[00:43:56] to Jeff Hinton about this right yes I
[00:43:59] know you and Jeff have a disagreement
[00:44:01] over this yes yeah actually we were very
[00:44:04] civilized on stage we had a pre-
[00:44:08] dinner it was a much more heated
[00:44:10] conversation that's good he's an older
[00:44:12] guy you have to be
[00:44:14] nice no but I we all love Jeff but but
[00:44:18] okay look we're here at Stanford campus
[00:44:21] we're in a liberal Art University we
[00:44:24] have all walks of discipline we have
[00:44:26] philosophers to anthropologists to
[00:44:29] Economist social scientists this is the
[00:44:32] kind of topic what is sentient what is
[00:44:36] consciousness what is the long long
[00:44:38] longterm existential reality I actually
[00:44:42] think it's a respectful topic I I
[00:44:44] generally do and I studied Consciousness
[00:44:47] a tiny bit with my his PhD co-advisor
[00:44:51] Professor Kristoff Co he talks about
[00:44:53] Consciousness all the time I feel like
[00:44:56] till the day I graduated I didn't
[00:44:58] understand what Consciousness is and and
[00:45:01] the reason is these are tough topics we
[00:45:03] should talk about it in the meantime I
[00:45:06] find it worrisome if the entire public
[00:45:10] including policy makers are talking
[00:45:13] about Top This singular topic that
[00:45:16] should be more a topic of scholarly
[00:45:19] debate and discussion and while
[00:45:21] forgetting about the true societal
[00:45:23] impact the catastrophic risks the
[00:45:27] opportunities you know we've got
[00:45:31] disinformation you know I mean Nate
[00:45:34] disinformation democracy you know it we
[00:45:37] were talking about this over lunch right
[00:45:39] it's that's just so deep I know Mike
[00:45:41] Mike fall we talk about this as well
[00:45:44] we've got um jobs you know John lving
[00:45:47] and I don't know other economists here
[00:45:49] are are are are really concerned about
[00:45:52] this we are talking we have issues with
[00:45:55] bu
[00:45:56] right we have issue with privacy I do
[00:45:59] healthare and uh um I have so many
[00:46:02] stories to tell you about the the
[00:46:05] tension between what technology can
[00:46:07] bring but human dignity and bias and
[00:46:11] we've got weaponization we've got
[00:46:13] geopolitics and I we've got also public
[00:46:16] sector crisis in this in the lack of in
[00:46:19] the sense of lack of resource and I
[00:46:21] think that's that's what's important we
[00:46:24] we have responsibility to talk talk
[00:46:26] about this and I worry that the media
[00:46:28] just or maybe it's not just the media
[00:46:31] the oxygen is sucked out in the room of
[00:46:35] only focusing on this existential topic
[00:46:38] yeah I think you're right I think we
[00:46:40] while that topic is out there we don't
[00:46:42] even know the terms yet can't Define
[00:46:44] them yet so so we need to think about
[00:46:47] these other more immediate uses which
[00:46:49] we're going to see soon we're going to
[00:46:51] see quickly we're going to see in this
[00:46:53] next election cycle for sure so yeah by
[00:46:55] Way D has a lot to say we can talk to D
[00:46:58] about sentient we had a we had a little
[00:47:01] discussion about that yeah well why
[00:47:04] don't we F and I could go all night but
[00:47:06] we want to leave a little time for
[00:47:08] questions so why don't we open the floor
[00:47:09] for questions and I think there's some
[00:47:11] microphones floating around so if you
[00:47:12] just raise your hand and I told Fay this
[00:47:16] crowd was going to ask really tough
[00:47:18] questions so I have high expectations
[00:47:20] for
[00:47:21] your hi um uh I working a cyber security
[00:47:24] industry uh I'm thinking that uh um the
[00:47:28] authentication is trying machine to the
[00:47:30] it's a human and then we come up new
[00:47:32] technology to bypass it and then we have
[00:47:34] a better way uh um so is there end to
[00:47:38] this what do you
[00:47:39] think well first of all both of us
[00:47:42] should talk I want to hear all you know
[00:47:44] digital authentication and
[00:47:46] disinformation it's going to be a hard
[00:47:48] problem I think the there's a lot of I
[00:47:51] mean you see all the concern in Congress
[00:47:53] about Ai and not near c l enough about
[00:47:56] cyber security I think that's a a really
[00:47:59] serious threat uh nationally as well and
[00:48:01] it's a hard really hard problem right
[00:48:03] yeah um I think it's going to be a
[00:48:08] continued uh What's the phrase I know
[00:48:10] the perfect Chinese R oh well you can
[00:48:13] tell
[00:48:14] us arms race yeah arms race between
[00:48:18] creating fakes and creating
[00:48:20] authentication technology and I talked
[00:48:23] to um my colleague Mark Lavo is a is a
[00:48:27] is a scholar in this uh in this uh
[00:48:30] domain he works in Adobe which is
[00:48:32] leading a lot of the industry uh efforts
[00:48:35] and Marc has said to me Source getting
[00:48:39] to the source is still going to be the
[00:48:41] most important um um defense against
[00:48:45] deep fake um so yeah it is it is a big
[00:48:49] but as the technology gets better and
[00:48:50] better it's going to get just harder and
[00:48:52] harder and harder to tell the
[00:48:54] difference yeah hi uh um I think you
[00:48:57] alluded to the problem of uh I would I
[00:49:01] call it there's a thirst of knowledge on
[00:49:04] both sides on the AI side things like
[00:49:07] what is what does it mean to be a human
[00:49:09] or or what is fairness and all these
[00:49:11] questions that could be answered by some
[00:49:14] departments here at the University or in
[00:49:16] general by the
[00:49:17] humanities uh on the other hand the
[00:49:19] humanity is are terrified what's coming
[00:49:22] U how do we bridge that it seems to me
[00:49:25] just here at Stanford I I don't see that
[00:49:28] bridge right now and I'm sure it's like
[00:49:30] that in most of other institutions
[00:49:33] around the world it seems like there's a
[00:49:34] gap instead of a bridge well first of
[00:49:37] all I do want to respectfully disagree
[00:49:39] at St for we have a human Center AI
[00:49:42] Institute that has been working really
[00:49:45] hard to uh try to Bridge I don't think
[00:49:47] we have done all the job I I I agree but
[00:49:50] I I think there's genuine effort and and
[00:49:53] trying to bridge this and there are
[00:49:54] multiple way ways of bridging one way is
[00:49:57] education and communication right it's
[00:50:00] scary if this is something that's so new
[00:50:03] and so unknown but we really need to do
[00:50:06] a better job in educating our students
[00:50:08] educating our alumni educating the
[00:50:11] public educating policy makers what this
[00:50:14] is I think that itself will go a long
[00:50:17] long way about what this technology is
[00:50:21] but there is other important measures of
[00:50:24] bridging incl including what are we
[00:50:26] doing that's making it better what are
[00:50:28] we doing that's augmenting Humanity what
[00:50:31] are we doing that is uh uh giving
[00:50:34] transparent trustworthy information to
[00:50:38] the public our AI Center for research on
[00:50:41] Foundation model is feverishly doing
[00:50:44] benchmarking on all these large language
[00:50:47] models benchmarking against say the EU
[00:50:50] AI act transparency measures these are
[00:50:54] important efforts to Bridge the the the
[00:50:57] knowledge Gap as you said and create
[00:51:00] trust create safety and and
[00:51:03] responsibility but you're right it's the
[00:51:06] the journey is long and I wish there's
[00:51:09] more um in around the interaction yeah
[00:51:13] around the world so fa maybe one thing
[00:51:15] you could touch on is this the scale of
[00:51:18] these models 500 billion parameters or
[00:51:20] something the notion that we have
[00:51:23] explainability that somebody can say why
[00:51:25] did it say this or take hallucination
[00:51:28] why does it
[00:51:29] hallucinate do you think this is part of
[00:51:31] the problem is that the scale of these
[00:51:33] models are so big that we really can't
[00:51:35] explain when I put a in why I get B out
[00:51:39] yeah so
[00:51:40] John I dream of the following thing but
[00:51:43] you can tell me I'm I'm delusional I
[00:51:45] feel like there's one day we've got to
[00:51:48] have a beautiful set of
[00:51:50] equations like Newton's law or Maxwell
[00:51:54] equations that would finally explain the
[00:51:57] mathematics behind this cuz I don't
[00:51:59] think we we're there yet we don't have
[00:52:02] the computer
[00:52:05] theoretical understanding of why these
[00:52:09] large language large models are doing
[00:52:12] what's doing we have some sense you know
[00:52:15] the the the representation and and the
[00:52:18] sequence to sequen in coding and all
[00:52:20] that but you know we don't so I don't
[00:52:23] know do you feel what ever
[00:52:26] I think I think the problem is you look
[00:52:28] at some things they do and it makes
[00:52:30] perfect sense they've memorized
[00:52:32] obviously they've memorized a lot of
[00:52:34] facts and relationships right but every
[00:52:36] now and then they put something in that
[00:52:39] looks like as it happened with Alpha go
[00:52:42] oh yeah you know and Alpha go move 37
[00:52:45] yeah move 37 so the computer made a move
[00:52:48] that everybody thought this is the
[00:52:51] craziest move ever what's going on here
[00:52:53] you've just blown the game and it turned
[00:52:55] out out it was a brilliant move in
[00:52:56] retrospect and was creative I mean he he
[00:52:59] says this is a creative move right least
[00:53:01] says this is creative that's a really
[00:53:03] interesting Insight yeah I I think
[00:53:06] students today should be working on
[00:53:10] these problems yeah right yeah okay do
[00:53:14] we have another question from the floor
[00:53:16] over there I see one and over
[00:53:18] here uh thank you it's fantastic um how
[00:53:22] do you see the intersectionality of
[00:53:23] evolution of synthetic biology
[00:53:26] and synthetic data and where AI is
[00:53:28] actually heading towards the GI pathway
[00:53:31] so again a whole bunch of things will be
[00:53:34] on another level but throw in a bit of
[00:53:35] quantum how are you even envisioning
[00:53:37] this from a humanist angle or the near
[00:53:40] term what we need to do in terms of even
[00:53:43] the guard rails or anything we're
[00:53:44] thinking
[00:53:46] about yeah well EO Wilson says the
[00:53:50] problem of humanity is we have
[00:53:52] Paleolithic emotions Med evil
[00:53:55] institutions and Godlike
[00:53:58] Technologies so I think everything you
[00:54:01] have said there is one of is a Godlike
[00:54:05] technology uh I don't have a silver
[00:54:08] bullet this is why we have Stanford Hai
[00:54:12] this is why we need to engage in
[00:54:15] governance this is why we need to
[00:54:17] educate the the the um the um public and
[00:54:22] uh about what is coming I do believe in
[00:54:26] humanity I think from that point of view
[00:54:29] I I know I've been called an optimist I
[00:54:32] I believe in humanity I believe in human
[00:54:36] resilience creativity I also believe in
[00:54:40] the Arc of human civilization bends
[00:54:44] towards benevolence and Justice I'm
[00:54:48] clearly stealing Dr King's ly here but
[00:54:52] but from that from that premise I
[00:54:55] believe our Collective creativity and uh
[00:54:58] and uh a partnership will find figure
[00:55:03] out the necessary guard rails that
[00:55:06] that's my what about oh I I agree with
[00:55:07] you I agree with you I think you're
[00:55:09] right the arc bends in the right
[00:55:11] direction there are sometimes setbacks
[00:55:13] or periods where things don't move in
[00:55:16] the right direction uh over a period but
[00:55:18] over the long term it tends to move in
[00:55:21] the right in the right direction after
[00:55:23] all when you become a
[00:55:26] parent your vision of the world and
[00:55:29] ensuring that the world you pass on uh
[00:55:31] is going to be a great one changes
[00:55:33] completely right yeah wa till you become
[00:55:35] a grandparent and you'll really
[00:55:37] see uh we have time for a few more
[00:55:40] questions over here thank you and thank
[00:55:42] you for this wonderful conversation I
[00:55:44] actually wanted to kind of tie to the
[00:55:46] last thing you mentioned about having
[00:55:47] kids what for both of you what do the
[00:55:50] world you envision in 50 years or in 40
[00:55:54] years when your kids are maybe my age
[00:55:56] what is the world that you think what do
[00:55:58] you think the world is going to look
[00:56:00] like then my kids are your age
[00:56:09] so well you have grandkids
[00:56:09] yeah I Vision that humans and machines
[00:56:12] Co co- habitat I I do I do believe
[00:56:16] robots will come in come in different
[00:56:19] forms and shapes Humanity's uh
[00:56:22] productivity will change um
[00:56:25] and of course we have to talk about the
[00:56:28] workforce change you know there's a lot
[00:56:31] of economists here in the audience so
[00:56:32] I'm a little too shy to give
[00:56:34] my prediction but I I I do think that uh
[00:56:38] we will hit the yet another at least one
[00:56:43] more but I'm sure many more inflection
[00:56:45] points where the machines will be um
[00:56:48] partners and collaborators with humans
[00:56:51] and I hope we're going to use all this
[00:56:54] uh technology and progress we've made on
[00:56:55] the AI side and machine learning to make
[00:56:58] the kind of breakthroughs we need to
[00:57:00] maintain our planet and give it to our
[00:57:02] children in some form where it's still
[00:57:04] habitable so I think that's going to be
[00:57:06] a critical issue going forward but I I'm
[00:57:09] actually excited about this Frontier
[00:57:12] where machine learning and and other
[00:57:13] science problems come together you've
[00:57:15] done a lot of work on medicine for
[00:57:16] example F but that's only one of many
[00:57:19] scientific discovery is absolutely the
[00:57:21] most exciting um part of today's AI this
[00:57:25] is why Academia is so important because
[00:57:28] we've got you know all kinds of
[00:57:30] scientists on campus and social
[00:57:32] scientists doing incredible work right
[00:57:36] right okay do you think maybe
[00:57:39] intelligence might be like a bit
[00:57:40] overrated I
[00:57:44] who just echoing thoughts of um youve
[00:57:48] all know Harari voice that uh you know
[00:57:51] you can argue that humans have become
[00:57:54] more intelligent have had at least more
[00:57:55] access to tools that allow us to be more
[00:57:57] intelligent but that doesn't necessarily
[00:57:59] make us less destructive or
[00:58:01] self-destructive um and in touching on
[00:58:03] the vision that you were painting F
[00:58:04] about um building these these entities
[00:58:07] that are capable of of of love and all
[00:58:10] of resilience and strength a lot of
[00:58:12] these beautiful human virtues um do do
[00:58:15] you really think we're headed in the
[00:58:16] right direction with that when we're
[00:58:17] talking about building AGI or is there
[00:58:20] something more like artificial wisdom um
[00:58:23] yeah can you touch on that
[00:58:31] I kind of I can sense that you actually
[00:58:31] probably are more worried about this you
[00:58:34] ask me do I really believe I do believe
[00:58:38] in human virtues I actually think when
[00:58:42] when you talk about human intelligence
[00:58:44] it's not just the mathematical rational
[00:58:46] intelligence it's our compassion it's
[00:58:48] our empathy these are the things animals
[00:58:51] really don't have much right so I do
[00:58:54] believe in human virtues are we headed
[00:58:57] in the right direction as we said I
[00:58:59] guess you've got two optimists on the
[00:59:02] stage I'm not saying every step of the
[00:59:06] way will be perfect we might even take
[00:59:09] really wrong steps you know look at from
[00:59:14] roord um splitting adom to an atomic
[00:59:19] bomb to nuclear energy I mean we've done
[00:59:24] good things bad things good things so I
[00:59:26] think we're going to go through that in
[00:59:29] AI but I do
[00:59:31] believe it we can I really believe we
[00:59:34] can as a species as a civilization that
[00:59:38] we can bring this to a better world yeah
[00:59:43] I agree with you I mean take you
[00:59:45] mentioned self-driving cars I mean the
[00:59:47] the last 10% of getting self-driving
[00:59:50] cars to work is really hard on the other
[00:59:53] hand a million people people die in car
[00:59:55] accidents around the world every day I'm
[00:59:57] convinced that in the next decade we
[00:59:59] will cut that be able to cut that number
[01:00:01] by 90% and you won't get everything
[01:00:04] right but you'll certainly and for us
[01:00:06] people getting older who find driving at
[01:00:08] night a bigger challenge or for some of
[01:00:10] you that might have had a glass of wine
[01:00:12] before you got in your car will make it
[01:00:14] a lot safer so I think there are great
[01:00:16] things that can be done here thank you
[01:00:18] Dr Lee for being here and thank you for
[01:00:20] the book I look forward to to reading it
[01:00:22] um you were one of the public faces
[01:00:25] inadvertently in the uh Google and DOD
[01:00:29] project Maven issue uh as it Rose and
[01:00:32] you know some of you correspondents
[01:00:33] became revealed in the pages of the New
[01:00:35] York Times in the discussion about that
[01:00:37] I'm wondering how has your thinking
[01:00:40] evolved uh because at that point in
[01:00:42] history uh the world maybe seemed a lot
[01:00:45] uh more at peace and since that time
[01:00:47] we've had the Russian invasion of
[01:00:49] Ukraine uh the recent of course uh
[01:00:52] initiation of a war in with Israel and
[01:00:54] Hamas um that shows that uh conflict is
[01:01:00] ongoing uh and with like Russian intent
[01:01:03] to destabilize our elections it
[01:01:05] geopolitics hasn't ended the dod is
[01:01:08] continuing to express interest in in um
[01:01:11] Ai and from that point working with
[01:01:13] project Maven it has evolved internally
[01:01:15] into a center within the dod to try and
[01:01:19] guide the use of the adoption of D AI
[01:01:21] what do you think about the ethics and
[01:01:23] has it has your point of view evolved
[01:01:25] since that time in terms of using these
[01:01:28] technological advancements in the
[01:01:30] defense of
[01:01:31] democracies yeah great question so this
[01:01:33] is why John and I were saying 2017
[01:01:36] around that time Ai and Tech become
[01:01:40] messy because you know it start to hit
[01:01:44] the world in the M multi-dimensional way
[01:01:47] that before we were just in the lab
[01:01:50] right like if you do image that it it it
[01:01:53] sounds great but it doesn't but once you
[01:01:55] get into weaponization defense um
[01:01:59] election and all that did I evolve I
[01:02:02] think I became more um I learned more
[01:02:06] from my colleagues but my human centered
[01:02:09] um belief of using technology for the
[01:02:13] good hasn't changed but I learned a lot
[01:02:16] more about
[01:02:18] how nuanced and how
[01:02:22] multi-dimensional this issue is is right
[01:02:25] like take
[01:02:26] defense I don't know how many people are
[01:02:28] in this audience we all have such
[01:02:31] different ways of defining defense
[01:02:34] defining weapon defining where we stand
[01:02:37] in terms of using technology for weapon
[01:02:40] human civilization this a history book
[01:02:43] of technology and Wars basically right
[01:02:47] so we all have different uh different we
[01:02:50] come in different uh opinions personally
[01:02:54] I'm devoted to you using AI for um much
[01:02:58] more focused in human centered use this
[01:03:01] is why I work so much in healthcare um
[01:03:04] and basic science research but I hear
[01:03:06] you and I think you know I continue to
[01:03:09] be a public face talking about this but
[01:03:11] one thing I think one thing I got to
[01:03:13] tell you I've learned in that through
[01:03:16] that experience as well as today is I've
[01:03:19] learned to be more vocal about the
[01:03:22] messiness of AI you know none of us have
[01:03:26] all the answers acknowledging the
[01:03:28] messiness acknowledging how tough this
[01:03:31] question is acknowledging as a computer
[01:03:34] scientist I'm not fully trained in every
[01:03:37] aspect of this this is why I go to
[01:03:39] Nate's place and talk about you know um
[01:03:42] you know democracy I go to my different
[01:03:45] colleagues and I think we need to have
[01:03:47] that humility whether you are AI
[01:03:49] technologist or or some other expert we
[01:03:52] should have the humility to learn to
[01:03:56] engage in respectful discussion to
[01:03:59] actually allow different voices you know
[01:04:02] this is so important in today's
[01:04:05] University um so that's that's my
[01:04:08] learning yeah I think you're absolutely
[01:04:10] right fa and I think the thing to
[01:04:11] remember
[01:04:13] is software is a tool but it's a
[01:04:16] somewhat Universal tool unlike a car
[01:04:19] what can you use a car to do you can use
[01:04:21] a car to drive you can't use a car to
[01:04:23] hammer a nail or to do something else
[01:04:26] but software has this property so it's
[01:04:29] very hard to distinguish between
[01:04:31] somebody's defense is somebody else's
[01:04:33] offense and that's just a a product of
[01:04:36] the kind of software we build and
[01:04:38] there's not that Nuance is really going
[01:04:39] to be hard to explain to people as we go
[01:04:41] forward
[01:04:47] y I think we have time for what we'll
[01:04:47] take one more and then Fay has a lot of
[01:04:51] books to sign
[01:04:53] so
[01:04:57] uh thank you so much for this wonderful
[01:04:57] session and I have so many questions on
[01:04:59] AGI applied AI but I think the most
[01:05:02] important question I have is something
[01:05:05] that you inspired with your thanks and
[01:05:06] the view around the generations you have
[01:05:09] thanked
[01:05:10] today given that we stand at the dawn of
[01:05:12] AI and the threshold of AI what advice
[01:05:15] would you give to your kids and my kids
[01:05:19] generation given the conversation we
[01:05:22] just had about the excitement but also
[01:05:24] the messiness of
[01:05:25] AI you know I I want to say just tell
[01:05:29] your kids to love their
[01:05:31] [Laughter]
[01:05:35] [Applause]
[01:05:37] mothers and read books read books I and
[01:05:41] fathers and fathers too but but um just
[01:05:46] going back to the theme of this book
[01:05:49] um really find your Northstar I think
[01:05:52] it's just you know technology is
[01:05:55] becoming more and more powerful human
[01:05:57] life is becoming more and more complex
[01:06:00] the world look I'm keenly aware where we
[01:06:04] are today in time and history so many
[01:06:07] conflicts so much suffering um but for
[01:06:11] the Young Generation find your Northstar
[01:06:14] and for the parents allow your kids to
[01:06:17] find that North Star give them the
[01:06:19] freedom give them the love um if you
[01:06:22] want them to love your back love first
[01:06:25] and that's more important than anything
[01:06:27] AI related that seems like a perfect
[01:06:30] place to end thank you fa thank you
[01:06:33] thank you
[01:06:34] [Applause]
