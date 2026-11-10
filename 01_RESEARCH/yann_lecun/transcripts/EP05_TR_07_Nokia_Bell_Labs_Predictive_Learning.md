# Nokia Bell Labs Keynote: Yann LeCun — Predictive Learning
- **YouTube URL:** https://www.youtube.com/watch?v=zaoL0LUctK4
- **Lines:** 2868

---

[00:00:00] [Music]
[00:00:12] [Applause]
[00:00:12] [Music]
[00:00:14] Please welcome Dunel Hernan.
[00:00:18] [Music]
[00:00:19] [Applause]
[00:00:22] [Music]
[00:00:24] Hello everyone. Welcome to the Hamming
[00:00:26] Innovation Hall here at Nokia Bell Labs.
[00:00:29] It's great to have all of you here uh
[00:00:31] for the second in our Shannon luminary
[00:00:32] lecture series. This is very exciting
[00:00:34] for us. Uh today in this uh our company
[00:00:37] we have a number of our academic
[00:00:39] collaborators. We have 50 STEM students.
[00:00:42] We have our experiments and arts and
[00:00:43] technology collaborators. We have our
[00:00:45] internal staff from the different
[00:00:47] business functions on Nokia on site and
[00:00:49] we have our global sites uh viewing this
[00:00:51] live as well. So this is a really
[00:00:53] exciting time for us to be able to share
[00:00:55] uh with this lecture globally. So just
[00:00:58] before we get started, I'll do some
[00:00:59] boring housekeeping uh before we get to
[00:01:02] the exciting lecture. So we have fire
[00:01:04] exits left and right of the stage and as
[00:01:06] you entered the building, we have
[00:01:07] restrooms at the front of the building
[00:01:09] also. And what we will do is we will ask
[00:01:11] everyone to please please please ensure
[00:01:14] you silence or turn off your phones out
[00:01:16] of respect for the speaker and also for
[00:01:18] your uh fellow colleagues here in the
[00:01:20] room. So, um, what we're going to get
[00:01:24] going, just to give you a sense of the
[00:01:25] outline, we're going to, um, have Marcus
[00:01:26] Welen come up and introduce the speaker.
[00:01:29] We'll have questions and answers at the
[00:01:30] end, and we will invite some of you
[00:01:32] former colleagues and collaborators to
[00:01:34] come down and, uh, say hello to Yan. And
[00:01:36] we also have some drinks and snacks out
[00:01:38] the front of the building also. So, with
[00:01:40] that, I'd like to introduce Marcus
[00:01:41] Weldon, the president of Bell Labs, and
[00:01:43] the CTO of Nokia to introduce Yan Lun.
[00:01:49] [Music]
[00:01:51] [Applause]
[00:01:55] Hi everyone. It's uh yeah a fantastic uh
[00:01:59] honor to have Yan here. It turns out we
[00:02:01] are more similar than than not. Uh not
[00:02:05] only because we're made from the same
[00:02:06] sort of biological systems that Yan is
[00:02:08] quickly going to turn into intelligent
[00:02:10] machine systems. But Yan joined uh
[00:02:13] joined Bell Labs around the time uh that
[00:02:17] actually he left Bell Labs around the
[00:02:18] time I joined and that's no coincidence
[00:02:20] either. Uh unfortunately it's happened
[00:02:22] multiple times. A previous Nobel Prize
[00:02:24] winner uh was called a guy called Jay
[00:02:27] Troutman similarly left uh about a year
[00:02:30] after I joined. And so uh I I like to
[00:02:32] think I was the end of of one of the
[00:02:35] great eras of Bell Labs. Hopefully this
[00:02:36] is a signature that he's dained to come
[00:02:38] back and this is the beginning of one of
[00:02:40] the next great eras of Bell Labs. But
[00:02:42] all joking aside, uh it is a privilege
[00:02:44] to have Yan here. Not only is he the
[00:02:47] founder or uh father of convolutional
[00:02:50] neural networks, sort of vision-based
[00:02:52] learning systems which he's going to
[00:02:54] talk about and the evolution of those to
[00:02:55] be predictive systems which is
[00:02:57] fascinating topic. Uh, but he's a
[00:02:59] thoroughly good guy. And it turns out I
[00:03:02] I looked on his website and I recommend
[00:03:04] you go there because it's very humorous.
[00:03:07] There's there's a there's a a lovely uh
[00:03:09] aspect to it, but there's a a not so
[00:03:11] serious part to it. So, I'm going to
[00:03:13] read you some of the not so serious
[00:03:14] parts. One is back to the the comment I
[00:03:16] made about him being a good guy. It
[00:03:18] turns out that's his name. uh lun which
[00:03:21] and I know I have to either nasal or not
[00:03:23] nasal it depending on whether it's I do
[00:03:25] the full Britain pronunciation because
[00:03:27] he's from Britany is roughly derived
[00:03:30] from lac which means nice guy.
[00:03:34] So, so that is is one of the facts
[00:03:35] there. But he's got some beautiful
[00:03:37] quotes there that I I I love because
[00:03:39] they're so sort of classically Bell Labs
[00:03:41] in that they're quirky, geeky, but
[00:03:43] really funny. And so here's here's one
[00:03:46] uh and this is very relevant to this
[00:03:48] talk. Uh it says even the smartest
[00:03:50] people think that they are not smart
[00:03:52] enough to understand the meaning of
[00:03:53] life, the universe, and everything. Yet
[00:03:55] many not so smart people think they are
[00:03:58] smart enough to do so.
[00:04:00] And I think there couldn't be a more
[00:04:02] relevant comment than that at this point
[00:04:03] in time. And of course,
[00:04:10] and of course, because he's one of us,
[00:04:13] he goes on to say, "And they don't know
[00:04:15] the answer is 42."
[00:04:18] And if you don't know what that refers
[00:04:19] to, then you should.
[00:04:21] He also goes on to say he loves Tex
[00:04:23] Avery uh the cartoonist and that uh
[00:04:27] cartoons and animation are one of the
[00:04:29] highest forms of art. Uh in fact, one of
[00:04:31] the only good forms of art coming out of
[00:04:32] the US other than jazz. That's not true.
[00:04:35] He didn't quite say it that way, but but
[00:04:36] I that was fascinating. But here's
[00:04:38] another one. This is a a great one. Fear
[00:04:41] of lawsuits will drive people to write
[00:04:43] sentences with provably zero information
[00:04:45] content.
[00:04:49] Isn't that wonderful?
[00:04:51] But enough enough of my silliness. Uh I
[00:04:54] will uh simply say that it's a great
[00:04:56] honor uh to have Yan here. He's really
[00:04:58] going to he has become the father of
[00:05:00] sort of AI not only in Facebook uh but
[00:05:03] probably globally working with his his
[00:05:05] collaborators. He did uh he was at Bell
[00:05:07] Labs from 88 to 96 then went to AT&T
[00:05:09] labs and worked in Larab Rabina's
[00:05:12] organization for about five six years
[00:05:14] then to NEC then to NYU and then got
[00:05:16] recruited by none other than Mark
[00:05:17] Zuckerberg himself. uh that's uh the
[00:05:20] level of which uh Brit Yan's renown had
[00:05:23] had risen. So he's been now director of
[00:05:24] AI at Facebook uh quite a large team
[00:05:27] there and he's going to tell you about
[00:05:28] his view of whether at least this is my
[00:05:30] view of his talk whether in fact
[00:05:31] machines will be able to emulate humans
[00:05:33] and be able to predict futures. So
[00:05:35] without further ado I'm going to welcome
[00:05:37] Yan Lakun to the stage.
[00:05:40] [Applause]
[00:05:41] [Music]
[00:05:44] [Applause]
[00:05:44] [Music]
[00:05:50] Oh, thank you for coming so nerous. It's
[00:05:51] really a pleasure to be here be here
[00:05:53] again um after so many years. Uh so I I
[00:05:59] actually have a similar story to to you.
[00:06:00] When I interviewed at Bell Labs in
[00:06:02] Homedale, I visited Steve Chu's lab and
[00:06:05] I was incredibly impressed and say, you
[00:06:07] know, I I'm going to have to join this.
[00:06:08] This is amazing. I wanted to go back to
[00:06:10] France. My wife wanted to go back to
[00:06:11] France, but I said, you know, just told
[00:06:13] my wife, not a problem. We're going to
[00:06:15] live in New Jersey, but it's just going
[00:06:16] to be for a year or two.
[00:06:19] Um, it's it's been um 28 years and and
[00:06:24] um but by the time I arrived uh at Bell
[00:06:28] Labs, Steve had left.
[00:06:32] Okay. So, um I'm going to talk about uh
[00:06:35] I guess what I call predictive learning.
[00:06:37] other people in the community may may
[00:06:40] call this something something else
[00:06:42] unsupervised learning perhaps um and but
[00:06:45] before I'm going to talk a little bit
[00:06:47] about kind of the past recent history or
[00:06:50] old history of of neural nets so I
[00:06:53] actually um I have a a couple pieces of
[00:06:56] ble memorabilia so um I joined ble in
[00:07:00] 1988 and uh um you know stayed with AT&T
[00:07:05] at the time of traverse when uh Lucent
[00:07:08] Technologies was was spun off and the
[00:07:10] group I I joined was uh led by Larry
[00:07:13] Jackal and it was uh in the electronics
[00:07:16] lab in Hondell and they were interested
[00:07:18] in fabricating neural nets and uh what
[00:07:21] you see the picture on the left here is
[00:07:23] actually one of the first kind of
[00:07:24] hardware neural nets. It's a it's a it's
[00:07:27] a resistor matrix. Uh they invented some
[00:07:30] new technology to kind of make very very
[00:07:32] small resistors. Um and then this was
[00:07:34] before I joined the lab and and then
[00:07:36] they kind of tried to figure out um they
[00:07:39] got the idea of this from John Hufffield
[00:07:42] who was a famous biohysicist who had a
[00:07:44] gig at Bell Labs. Um and Larry went to
[00:07:48] see him and asked him you know I have a
[00:07:50] new department I'm not sure what to do
[00:07:51] what should I work on. He said well
[00:07:52] there's this neural net thing you should
[00:07:54] probably look at this. So they started
[00:07:56] building propul nets out of uh uh
[00:07:58] silicon essentially silicon and kind of
[00:08:00] exotic sauces to make the resistors and
[00:08:03] then realized that uh there's two
[00:08:06] problems. First of all you have to build
[00:08:07] amplifiers you have to put around this
[00:08:09] matrix and the amplifiers are about 10
[00:08:11] times bigger than the the resistors and
[00:08:14] the second thing is that you have to
[00:08:15] talk to computers and then you have to
[00:08:16] go through converters and everything. So
[00:08:19] even though you could build those
[00:08:20] incredibly fast and compact neural nets
[00:08:22] on the chip you couldn't really talk to
[00:08:24] them. you can't really you couldn't
[00:08:25] really use them but it was sort of a
[00:08:27] really exciting period. um at the time.
[00:08:31] Uh this is uh Larry Jackekal here. U at
[00:08:34] the top u uh this is around 1994 I
[00:08:38] believe. We were actually on a sailing
[00:08:40] trip in the Virgin Islands. And a couple
[00:08:43] years later we had a few years later we
[00:08:45] had kind of a lab reunion. And you see
[00:08:47] some people here the the guy with a
[00:08:49] white shirt is is a character. His name
[00:08:51] is John Danker. He he was at Hondell. Um
[00:08:56] but he had an office in in Mar Hill here
[00:08:58] that he shared in the in the biohysics
[00:09:01] lab. I think it was in Horstomer's
[00:09:02] organization at the time and u he was
[00:09:06] sharing the office with Vilfred Denk who
[00:09:08] is now at Max Blanc institute and so
[00:09:10] there were the two names on the on the
[00:09:12] door Vinfred Denk John Danker and
[00:09:14] someone wrote below Denest.
[00:09:17] [Applause]
[00:09:23] Okay, so a lot of the pretty much all
[00:09:26] the applications that you hear about of
[00:09:29] of AI and machine learning use a mode of
[00:09:31] learning called supervised learning. So
[00:09:33] supervised learning is kind of like
[00:09:35] showing a picture book to a child. You u
[00:09:38] want to train a machine for example to
[00:09:40] recognize images to classify images of
[00:09:41] cars and airplanes and you show a car to
[00:09:45] the machine and the machine has kind of
[00:09:47] adjustable knobs on it that basically
[00:09:48] determine the input output function that
[00:09:50] uh the machine computes and what you
[00:09:53] want is you want the red light to turn
[00:09:54] on when you show a car and you want the
[00:09:56] green light to turn on when you show an
[00:09:57] airplane. And so what you do is you show
[00:09:59] a image of a car and then you kind of
[00:10:01] twiddle the nods a little bit so that
[00:10:02] the brightness of the red light goes up
[00:10:05] and the brightness of green light goes
[00:10:06] down. And then you do the reverse when
[00:10:08] when you show an image of a plane. And
[00:10:10] if the machine is built in such a way
[00:10:12] that it has enough capacity if it's
[00:10:13] powerful enough. Um and you kind of keep
[00:10:16] adjusting those those nodes just a
[00:10:17] little bit for every uh for you know
[00:10:19] thousands or millions of samples.
[00:10:21] Eventually it will figure out what
[00:10:23] really is the essence of the difference
[00:10:24] between those two things. That's pretty
[00:10:26] much as simple as that. So if you want
[00:10:27] to formulate this in a mathematical
[00:10:29] term, you're kind of minimizing some
[00:10:31] sort of objective function that measures
[00:10:33] the discrepancy between the output you
[00:10:34] want and the output you you get that the
[00:10:37] machine produces average over a number
[00:10:39] of training samples and you you minimize
[00:10:42] this loss function with respect to all
[00:10:43] the knobs uh in the machine. Now in a
[00:10:47] real machine uh a typical application of
[00:10:49] machine learning today uh you may have
[00:10:52] hundreds of millions of those knobs and
[00:10:54] of course you need efficient ways to
[00:10:56] figure out in which directions to to
[00:10:58] turn them which I'll talk about later.
[00:11:00] Um and this is the the first machine
[00:11:03] that uh was capable of learning called
[00:11:06] the perceptron. It was built by uh Frank
[00:11:08] Rosenblad and his team at Cornell and it
[00:11:12] was an analog computer. So there was um
[00:11:15] sort of a retina which is sort of an
[00:11:17] array of photo receptors and what you
[00:11:20] see in the middle here is what we would
[00:11:22] now call a feature extractor. Um it
[00:11:24] looks like a like a spaghetti plate
[00:11:26] really u and the usual joke I say is
[00:11:29] that now we replace this with spaghetti
[00:11:30] code.
[00:11:33] And then at the right is uh it's called
[00:11:37] is the classifier. So that's the part
[00:11:38] that is actually trainable. And so the
[00:11:40] classifier does a very simple thing. It
[00:11:43] takes the uh the the series of outputs
[00:11:46] that comes out of the of the feature
[00:11:48] extractor. It's a vector and it computes
[00:11:50] a weighted sum of the components of that
[00:11:52] vector. Basically computes the dot
[00:11:53] productduct between the the vector and a
[00:11:56] vector of weights. If that dot product
[00:11:58] is larger than the threshold, it's
[00:11:59] category A. If it's smaller than the
[00:12:02] threshold, it's not category A. Okay?
[00:12:05] And or category C in that case. And so
[00:12:08] the way the the the the system was
[00:12:10] implemented the the weights here, what
[00:12:12] you see Frank Obllight holding is a bank
[00:12:15] of eight weights and each weight is
[00:12:17] actually a potentiometer with a motor on
[00:12:19] it. And so to train the machine, you
[00:12:22] show a sample, then you press a button
[00:12:24] and all the motors go
[00:12:26] and you know depending on how long you
[00:12:28] press, they will turn more or less
[00:12:30] essentially. And that's how you adjust
[00:12:32] the you know the step size in the
[00:12:34] gradient descent algorithm essentially.
[00:12:36] Um and so you know only a couple years
[00:12:39] later it it became practical to really
[00:12:41] kind of write programs to do this and
[00:12:44] right now those algorithms are still
[00:12:46] used. The perceptual learning algorithm
[00:12:47] is still used and uh basically now it's
[00:12:50] a threeline Python script. Um
[00:12:54] but that was kind of the the first uh
[00:12:57] interesting kind of learning machine.
[00:12:59] There were other attempts uh at IBM for
[00:13:03] training a machine to play chess for
[00:13:05] example that uses a slightly different
[00:13:07] principle. Um and I learned about this
[00:13:10] when I was an undergrad and I was
[00:13:11] absolutely fascinated. This was in the
[00:13:13] uh early 80s 1981 or so and uh I'd never
[00:13:17] heard of the possibility of a learning
[00:13:19] machine before and that's what got me
[00:13:20] hooked into this kind of thing and I
[00:13:22] realized nobody was working on this at
[00:13:23] the time. Uh this was this had fallen
[00:13:25] out of fashion. uh essentially the the
[00:13:28] field that died in 1969
[00:13:31] uh after a book was published that
[00:13:34] proved there was dire limitations of
[00:13:35] those models and so nobody was working
[00:13:37] on this at the time.
[00:13:40] Um but really the the problem that these
[00:13:43] guys were trying to solve and the
[00:13:44] problem that uh essentially got solved
[00:13:47] to some extent in the mid mid 80s and
[00:13:50] had a little bit to do with this is the
[00:13:52] problem of not training a machine with a
[00:13:54] single layer but training a machine with
[00:13:55] multiple layers. And that's really what
[00:13:57] deep learning is about. So what you see
[00:13:58] here is at the top is the classical way
[00:14:01] of doing pattern recognition. Classical
[00:14:03] which means classical way until about
[00:14:06] five years ago. Um and at the bottom is
[00:14:10] kind of the deep learning way of doing
[00:14:12] uh pattern recognition now where
[00:14:14] supervised pattern recognition in
[00:14:15] particular where you have an image at
[00:14:17] the at the bottom and the machine is
[00:14:19] composed of a cascade of modules all of
[00:14:21] which are parameteriz parameterized have
[00:14:24] knobs on them and you train the entire
[00:14:26] machine end to end to u basically
[00:14:29] optimize your objective function compute
[00:14:31] the right answer.
[00:14:33] Um and what's magical about machine
[00:14:36] learning in general, there's a lot of
[00:14:37] theory on this is that you train on a
[00:14:39] particular set of training samples and
[00:14:42] uh the machine generally works pretty
[00:14:44] well on new examples it's never seen
[00:14:46] before as long as they are, you know,
[00:14:47] sufficiently similar to the example it's
[00:14:49] been trained on.
[00:14:52] So people back in the 50s and 60s were
[00:14:54] really kind of looking for algorithms to
[00:14:56] be able to train multi-layer systems of
[00:14:58] this type, but really um uh couldn't
[00:15:02] quite figure it out. And the reason was
[00:15:04] because the the the mindset was hooked
[00:15:06] on using binary unit binary threshold
[00:15:09] units. And if you use binary threshold
[00:15:12] units and kind of you know logic a
[00:15:15] little bit um you don't get the idea
[00:15:17] that u you have this sort of continuous
[00:15:20] function that you can adjust and you can
[00:15:21] compute gradients and adjust knobs so as
[00:15:23] to minimize an objective function. And
[00:15:26] so it took until the mid 80s for people
[00:15:29] to change the type of of uh of of units
[00:15:33] in those neural nets to use continuous
[00:15:35] functions which kind of immediately
[00:15:37] suggested the idea that we should just
[00:15:39] use gran descent essentially um to
[00:15:42] compute those. So here is what a modern
[00:15:46] neuronet looks like. And there was a
[00:15:49] wave of interest in those models uh
[00:15:51] starting around 1986 or so. And it kind
[00:15:54] of died. It it lasted for a little less
[00:15:56] than 10 years. And the sort of interest
[00:15:57] died in the in the '9s. And it's because
[00:16:01] uh partly it's not entirely clear why,
[00:16:03] but it's partly because those uh systems
[00:16:05] tend to be very very finicky. It's very
[00:16:07] hard to make them work. There's a lot of
[00:16:08] black art in it. And at the time it was
[00:16:10] difficult to distribute your code. Now
[00:16:12] it's u kind of common place to kind of
[00:16:15] distribute your code in open source.
[00:16:16] Everybody used the same platform etc.
[00:16:18] But back in the 90s it just wasn't the
[00:16:20] case and so the field died a little bit
[00:16:22] because of that and and because the more
[00:16:24] classical methods seem to work for the
[00:16:25] size of data sets that were available at
[00:16:27] the time. But here is what a modern
[00:16:28] neural net looks like. So it's a
[00:16:31] succession of two types of operators. Uh
[00:16:34] you take an input you represent it as a
[00:16:37] vector or as a multi-dimensional array.
[00:16:38] Basically just a temple of numbers. And
[00:16:40] then you're going to take this multiply
[00:16:42] by a matrix. Uh the coefficient in a
[00:16:45] matrix are the adjustable knobs and then
[00:16:47] you take the resulting vector and apply
[00:16:50] a pointwise nonlinearity to all the
[00:16:52] components of that vector. Uh so for
[00:16:54] example a typical linearity that people
[00:16:56] use nowadays is what we call the rel.
[00:16:58] It's really the halfwave rectifier. It's
[00:17:00] the positive part of a you know of a
[00:17:04] of an argument. And so that's a very
[00:17:07] elementary uh function linear
[00:17:10] parameterized linear transform then
[00:17:11] pointwise nonlinearity and then you
[00:17:13] stack multiple layers of that and you
[00:17:17] can show that a lot of functions can be
[00:17:18] approximated as close as you want with
[00:17:20] this kind of architecture. You know you
[00:17:22] only need two layers but you might need
[00:17:23] a very very wide middle layer and things
[00:17:26] become more efficient as you stack more
[00:17:28] layers. You you end up being able to
[00:17:29] compute more functions with kind of
[00:17:30] fewer fewer nodes.
[00:17:33] So then the next question is how do you
[00:17:35] adjust the knobs? How do you adjust the
[00:17:36] coefficients inside this? And u and
[00:17:39] that's done with what's called the back
[00:17:41] propagation algorithm uh which is you
[00:17:43] know an extremely sophisticated
[00:17:45] mathematical concept.
[00:17:49] It's basically chain rule. Um that
[00:17:51] that's what it comes down to. Um you
[00:17:53] know live nips could have could have
[00:17:55] figured it out. Actually he figured it
[00:17:57] out. Um so that goes back a long time
[00:18:00] but the realization that you could use
[00:18:03] uh essentially chain rule to compute the
[00:18:05] gradients in uh with respect to all the
[00:18:07] parameters in the system to do machine
[00:18:09] learning basically wasn't really sort of
[00:18:13] common place until around 1986 or so. It
[00:18:16] took a very long time for people to
[00:18:17] believe in the fact that it could work.
[00:18:19] There were papers in the 50s by Marvin
[00:18:21] Minsky and others uh who said that um uh
[00:18:25] this idea of doing gradient descent or
[00:18:28] or hill climbing they called it is never
[00:18:30] going to work because the complex
[00:18:31] systems are going to be trapped in local
[00:18:32] minima. And so there was this mindset
[00:18:34] that somehow because those systems are
[00:18:36] complex the local minima problem is
[00:18:38] would would be fatal. It turns out
[00:18:41] that's not true.
[00:18:43] Um so the idea of back prop is uh uh
[00:18:47] when you have a a system that's kind of
[00:18:49] a cascade of modules this way you put an
[00:18:51] input you propagate forward you compute
[00:18:53] the value of the cost function that
[00:18:54] measures the discrepancy between what
[00:18:56] you want and what the machine produces
[00:18:58] and then there is sort of a backward
[00:19:00] signal that goes uh you know from the
[00:19:02] from the top to the bottom that kind of
[00:19:04] propagates the gradients if you want and
[00:19:06] that's that's what is called back
[00:19:07] propagation.
[00:19:08] um old idea became popularized around
[00:19:11] 1986. Uh I had a version of it in 1984
[00:19:14] but the the main uh version was
[00:19:16] popularized by De Roart, Jeff Finton and
[00:19:19] Ron Williams around 1986.
[00:19:21] Okay. Then the next question you have to
[00:19:23] figure out is what do you put in those
[00:19:24] boxes? So you can you know it's fine to
[00:19:26] think about multiplying a vector by a
[00:19:28] matrix but when you when the input to
[00:19:30] the system is an image say a few hundred
[00:19:33] pixels by a few hundred pixels. Okay. So
[00:19:35] let's say uh 200 by 200 pixels. So that
[00:19:38] means you have uh 40,000 input variables
[00:19:42] times three if you have color 120,000
[00:19:45] input variables. So now you're going to
[00:19:46] multiply this by 120,000 by 120,000
[00:19:49] matrix and that's just not going to be
[00:19:50] practical. So you have to kind of think
[00:19:52] about how to specialize those uh linear
[00:19:55] operators to make them practical. And in
[00:19:56] the case of images, one answer to this
[00:19:59] is convolutional neural networks
[00:20:01] invented at Bell Labs around 1988. Um I
[00:20:04] actually started working on this uh when
[00:20:06] I was a postoc in Toronto just before
[00:20:07] joining Bell Labs. But this really at
[00:20:09] Bell Labs where I was able to kind of
[00:20:11] make this work. Um I was amazed actually
[00:20:14] a few months before I I joined Bell
[00:20:15] Labs. Larry calls me up and says um you
[00:20:18] know would like to buy a computer before
[00:20:19] you come so it's ready when you when you
[00:20:20] come. Um uh what would you like? Um said
[00:20:24] well you know here in Toronto we have a
[00:20:26] Sun 4. Do you guys have a Sun 4? Um said
[00:20:29] no we don't but we can buy one um before
[00:20:31] you come. And the Sun4 in Toronto was
[00:20:34] shared by the entire department, 30
[00:20:37] people. And when I come to be labs, I
[00:20:38] had a Sun4 for me, just for me.
[00:20:41] I say, what's going on? Said, well, u
[00:20:44] you know, here you don't get famous by
[00:20:46] saving money.
[00:20:48] [Applause]
[00:20:53] Um,
[00:20:55] and so we needed those machines to run
[00:20:57] those things. And the so the idea of uh
[00:21:01] converional nets is that you you
[00:21:03] basically instead of having a general
[00:21:05] matrix that you multiply the input
[00:21:07] vector by you view the image the input
[00:21:10] as as a 2D array really. And the linear
[00:21:13] operator you're going to apply is is
[00:21:14] going to be a convolution. Um so I'm
[00:21:16] sure there's a lot of people here who
[00:21:18] know what a convolution is. Um of all
[00:21:20] audiences when I talk to computer
[00:21:22] scientists I actually have to explain
[00:21:23] what a convolution is. Um so here um the
[00:21:27] what I mean by this is kind of a
[00:21:28] discrete operator operation where you
[00:21:30] you take the input image you take a a
[00:21:33] neighborhood in input image say 5 by5 in
[00:21:36] this case and you uh compute the
[00:21:39] dotproduct of the pixels within this
[00:21:41] small neighborhood of 5 by five with a
[00:21:43] weight a weight a set of weights 25
[00:21:45] weights and that gives you a weighted
[00:21:47] sum. to compare this to a threshold or
[00:21:49] pass that through to a nonlinearity and
[00:21:52] put the result in the output map. And
[00:21:53] then you take this little neighborhood
[00:21:55] and you swipe it over the entire image
[00:21:57] using the same weights all over which is
[00:21:59] why it's a a convolution operation
[00:22:02] discrete convolution in this case and
[00:22:03] that gives you the the result here the
[00:22:05] output map. So the idea of convolutional
[00:22:07] net is you the the first layer is
[00:22:10] basically a bunch of convolutional
[00:22:11] filters like this applied to the image
[00:22:14] each of which detects a particular type
[00:22:16] of feature or motif uh all over the
[00:22:19] image and kind of you know turns on or
[00:22:22] turns off depending on whether the the
[00:22:24] the local motif matches the the the
[00:22:27] weight patterns. Uh the weights of
[00:22:29] course are learned. You can compute the
[00:22:30] gradient of some objective function with
[00:22:31] respect to them using back propagation.
[00:22:33] No problem with that.
[00:22:35] Then the next layer up is what's called
[00:22:37] a pooling operation. So the the role of
[00:22:40] pooling is to aggregate the output of
[00:22:42] each filter over a small uh area. And
[00:22:45] the purpose of this is to build a little
[00:22:47] bit of shift and distortion invariance
[00:22:48] into the system. And I'll come back to
[00:22:51] this in a bit. And all of those ideas
[00:22:53] actually I was inspired by classic work
[00:22:56] in neuroscience for this as well as some
[00:22:58] work by a gentleman called Kuni Kof
[00:23:00] Fukushima. No relationship with the uh
[00:23:02] nuclear power plant. uh who uh came up
[00:23:06] with a model called the neocognitron
[00:23:07] which had this idea of filters that you
[00:23:10] replicate and kind of pulling operations
[00:23:11] which were inspired by neuroscience
[00:23:12] classic work and neuroscience from the
[00:23:14] 60s Nobel prizewinning classic work um
[00:23:18] and kind of built a simulator for it if
[00:23:20] you want but it didn't have back prop so
[00:23:22] we couldn't really train it properly um
[00:23:25] and uh and the idea of comnets is that
[00:23:28] you you kind of stack multiple stages
[00:23:30] which are those successions of uh filter
[00:23:34] bank convolutions uh nonlinearity and
[00:23:37] then pooling operation and then you
[00:23:38] repeat the process filtobank
[00:23:39] nonlinearity pooling etc. So here is one
[00:23:42] of those things in action. This is
[00:23:43] actually a vintage commercial net from
[00:23:45] you know Bellads many years ago uh has
[00:23:48] been trained to recognize Henry digits
[00:23:51] and the you see the input the first
[00:23:54] layer which is composed of those feature
[00:23:55] maps then the second layer after pulling
[00:23:57] and whenever the input shifts by two
[00:23:59] pixels then that after pulling the the
[00:24:02] shift is only one pixel and the reason
[00:24:04] is that this pooling operation
[00:24:06] essentially reduces the spatial
[00:24:07] resolution of of the image. It
[00:24:09] aggregates the response of the filters
[00:24:10] over a 2 x2 region and then you step the
[00:24:13] window over over which to do this
[00:24:14] aggregation by two by two pixels. Um and
[00:24:18] then the next layer up is again a set of
[00:24:20] convolutions. Each of those maps
[00:24:21] actually applies uh different
[00:24:24] convolution kernels to each of the
[00:24:26] feature maps on the previous layer. Add
[00:24:27] the result and then pass that through
[00:24:30] nonlinearity. You're putting again and
[00:24:31] then convolutions again and then the
[00:24:33] output layer is not shown here. Here is
[00:24:35] an example where we show the output
[00:24:36] layer. Um so this one has been trying to
[00:24:39] not just recognize a single character
[00:24:41] but kind of a string of characters which
[00:24:43] was really the first time that um you
[00:24:46] know people could use um learning
[00:24:49] techniques basically to or or any
[00:24:51] technique in fact to simultaneously
[00:24:53] segment and recognize multiple objects.
[00:24:57] So what's interesting about u about
[00:24:59] about commercial nets is that they don't
[00:25:01] just learn um or deep learning in
[00:25:04] general is that they don't just learn a
[00:25:05] classification function. They learn to
[00:25:07] represent the perceptual world. They
[00:25:09] sort of learn to extract uh the uh the
[00:25:12] features in the image that are relevant
[00:25:14] for the for the task that we're talking
[00:25:16] about.
[00:25:18] Um this is a fun video that is from 1992
[00:25:21] or 1993. It's a demo of one of the first
[00:25:24] prototype system that we had. This is
[00:25:25] actually my phone number in Homeell, New
[00:25:27] Jersey at Bell Labs, no longer
[00:25:29] operating. Uh, so I hit a key and
[00:25:32] there's a video camera that grabs the
[00:25:34] image and it goes to the 386 PC that um
[00:25:37] recognizes each of those uh characters.
[00:25:40] Uh, this is actually running not on the
[00:25:42] 386, but on a an AT&T DSP 32C, for those
[00:25:46] of you who are old enough to remember
[00:25:47] what that means, capable of the blazing
[00:25:50] speed of 20 megaflops. Um, and we really
[00:25:53] needed this kind of uh power at the time
[00:25:55] which was really extraordinary to to be
[00:25:57] able to run those systems. Uh, it was
[00:25:59] very robust. Uh, I mean there's really
[00:26:01] no other system in the world at the time
[00:26:02] that could kind of deal with this sort
[00:26:04] of uh complicated uh shapes.
[00:26:08] Um,
[00:26:10] and uh this is uh Don Henderson is one
[00:26:13] of the the lab engineers. Uh, and this
[00:26:16] is Rich Howard. And I'm sure a lot of
[00:26:18] you know Rich Howard, right? Okay.
[00:26:21] because he, you know, retired from Lucat
[00:26:25] a few years ago. Um, he was he was my
[00:26:29] boss's boss. He was the lab director.
[00:26:33] Wonderful guy. Um that actually gathered
[00:26:36] a little bit of press at some point uh
[00:26:39] in the New York Times and uh eventually
[00:26:41] we managed to hook up with a development
[00:26:43] group at at Bell Labs that uh developed
[00:26:46] a a check reading system that was
[00:26:48] deployed uh around 19 95 for various
[00:26:52] applications. It was actually really
[00:26:54] kind of well well deployed in 1996. We
[00:26:57] actually had a party at a fancy
[00:26:59] restaurant near near Homedale to
[00:27:00] celebrate the fact that our check
[00:27:02] recognition system was had been uh um
[00:27:06] fielded essentially and we came back to
[00:27:09] the lab after lunch and uh we saw
[00:27:12] everybody kind of making funny faces.
[00:27:15] This was the day of that the split of
[00:27:17] the company was announced.
[00:27:21] Um then there is an interesting story
[00:27:22] which is that uh the the product group
[00:27:24] that was working on this was at NCR
[00:27:26] which at the time was part of AT&T. The
[00:27:28] development group of course was working
[00:27:30] together with us. But when the company
[00:27:32] split all the researchers went to AT&T.
[00:27:35] It's because the president of Bell Labs
[00:27:36] at the time hated this stuff. Um so
[00:27:39] every machine learning people went to
[00:27:40] AT&T. That's why there was no machine
[00:27:41] learning at Bel Labs for a while. Um the
[00:27:44] uh development group the engineering
[00:27:46] group that was working on this uh stayed
[00:27:48] with Lucat. weren't uh given a choice
[00:27:51] and the product group went with NCR and
[00:27:53] the lawyers in their infinite uh wisdom
[00:27:56] gave all the patents to NCR which had no
[00:27:58] idea what they had. Uh thankfully those
[00:28:01] patents are expired
[00:28:06] u but not everybody was convinced. So
[00:28:08] even within our lab so there was this u
[00:28:11] guy in the lab Vladimir Vapnik he's an
[00:28:13] extremely famous u person in in machine
[00:28:17] learning um and you know he kind of
[00:28:21] basically came up with a whole theory of
[00:28:24] machine learning the the most general
[00:28:25] approach to learning theory and he was
[00:28:27] really not convinced that this was the
[00:28:29] ultimate answer to to learning he he
[00:28:31] really didn't believe in the concept of
[00:28:32] neural net and so Larry and he was
[00:28:34] working in the same lab so he is the
[00:28:36] inventor of support vector machines if
[00:28:38] you know what that is and kernel
[00:28:39] machines and we were you know two
[00:28:41] offices
[00:28:43] from each other. So commercial nets and
[00:28:44] supervisor machines were invented two
[00:28:47] years away from each other u two offices
[00:28:49] away from each other. Um uh SVMs became
[00:28:53] became kind of the dominant model for
[00:28:55] about 10 years in machine learning until
[00:28:57] until relatively recently. And so Larry
[00:29:00] Jackal um and and Vladimir had a bet in
[00:29:03] 1995.
[00:29:05] Jackal bets one fancy dinner that by
[00:29:07] March 14, 2000, people will understand
[00:29:09] quantitatively why big neural nets uh
[00:29:12] work on on you know are working on on on
[00:29:14] large databases uh working on large
[00:29:17] databases are not so bad which means you
[00:29:19] know understanding theoretically using
[00:29:20] bounds and and and theory etc. Um vet
[00:29:25] bets one fancy dinner that Jackal is
[00:29:26] wrong but if vetnik is the is the person
[00:29:29] figuring out the bounds and conditions
[00:29:31] then still wins. So,
[00:29:34] so this was a disguised incentive that
[00:29:37] Larry designed to kind of uh tell
[00:29:39] Vladimir, you know, you should work on
[00:29:41] this. Um,
[00:29:44] and uh, Vladimir lost. Uh, so
[00:29:49] uh, you know, by 2000 people were still
[00:29:51] using neural nets, although it was not
[00:29:52] as popular as five years earlier. There
[00:29:54] was a second bet. Vapik bets one fancy
[00:29:57] dinner that by March 14, 2005, no one in
[00:30:00] their right mind will use neural nets
[00:30:02] that are essentially like the ones used
[00:30:04] in 1995. And Jackal bets that Vapnik is
[00:30:07] wrong. Signed by Vapnik, Larry Jackal
[00:30:10] and me.
[00:30:12] Uh, and you know, Vapnik kind of lost
[00:30:15] that one, too. Um, oh, and sorry, Larry
[00:30:20] Jackal lost the first one. So it was it
[00:30:22] was never really proved why neural net
[00:30:25] works so well. Uh but he won the second
[00:30:27] one and so you know they kind of split
[00:30:29] the bill at the end um because they
[00:30:31] didn't they waited until 2005. And this
[00:30:33] is a picture of the dinner in 2005. The
[00:30:35] person on the left here is Leon Bu who's
[00:30:38] uh um it's been a longtime collaborator
[00:30:40] of mine and is actually at Facebook as
[00:30:42] well.
[00:30:44] So fast forward um about about 10 years
[00:30:49] and around 2013 uh 2012 2013 people
[00:30:53] figured out uh how to run very very
[00:30:56] large convolutional nets on very large
[00:30:58] data sets using GPUs. Uh GPUs were
[00:31:01] basically the only way to get cheap you
[00:31:04] know access to kind of a cheap
[00:31:05] supercomputer if you want. You could
[00:31:06] have you know a teraflop or so uh in a
[00:31:09] machine and you could stack multiple
[00:31:10] cards and and get you know a few
[00:31:12] teraflop of computation that allowed
[00:31:14] people to uh run very large
[00:31:16] computational net and I wish uh my lab
[00:31:19] at NYU had had been the first to do this
[00:31:21] but it wasn't it was our friends at
[00:31:23] University of Toronto in Jeffington's
[00:31:25] group where I done my my postto many
[00:31:26] years before and so they they they spent
[00:31:29] um
[00:31:30] you know a lot of effort trying to kind
[00:31:32] of optimize those things on GPUs and
[00:31:34] train on a newly available data set
[00:31:37] called ImageNet which had one 1 million
[00:31:39] training samples and it worked
[00:31:41] beautifully. so much um so so nicely in
[00:31:45] fact that they they won a competition
[00:31:48] called the imageet competition for
[00:31:50] object recognition. A million training
[00:31:52] samples, a thousand categories of
[00:31:54] everyday objects and they won it by such
[00:31:56] a margin that uh the computer vision
[00:31:58] community which so far had been
[00:32:01] extremely kind of skeptical about deep
[00:32:03] learning and commercial nets uh
[00:32:05] basically dropped everything they were
[00:32:06] doing and switched to using it. Um the
[00:32:08] difference was so large. So the the
[00:32:10] previous state-of-the-art was around 26%
[00:32:12] error by some measure and they got 15%.
[00:32:15] And the the 26% it was clear that the
[00:32:17] the previous methods were kind of
[00:32:18] saturating.
[00:32:20] So it created a revolution in image
[00:32:23] recognition in computer vision where um
[00:32:26] you know until 2011 2012 you would
[00:32:29] submit a paper to a computer vision
[00:32:30] conference and it would be suddenly
[00:32:32] rejected by people who would say what
[00:32:34] the hell is a convolutional net and by
[00:32:36] 2015 you cannot get a paper accepted at
[00:32:39] any vision conference unless you're
[00:32:40] using commercial nets.
[00:32:42] uh a similar revolution occurred in
[00:32:44] speech recognition a couple years
[00:32:45] earlier um where which you know our
[00:32:48] friends in Toronto also had a lot to do
[00:32:50] with so what's interesting about
[00:32:53] conversion nets is that they they kind
[00:32:54] of learn a sort of compositional
[00:32:56] hierarchical representation of the world
[00:32:59] uh elementary images you could think of
[00:33:02] of them as as being compositional in the
[00:33:04] way that in in the sense that images are
[00:33:07] composed of elementary motifs like
[00:33:08] oriented edges and then combinations of
[00:33:11] edges form
[00:33:12] simple shapes, things like corners and
[00:33:15] circles and gratings and things like
[00:33:17] that. And then combinations of those
[00:33:19] form kind of more complex shapes like
[00:33:21] parts of objects. Combination of those
[00:33:23] form objects and the multiple layers
[00:33:25] basically end up kind of learning those
[00:33:28] uh those detectors at the at the various
[00:33:30] the various levels. So those are
[00:33:33] visualizations done by my colleague Rob
[00:33:35] Fergus at the term at NYU now at at
[00:33:38] Facebook as well.
[00:33:39] at NYU uh where they kind of visualize
[00:33:43] the the type of shape that would
[00:33:45] maximally activate a particular unit in
[00:33:46] a in a layer uh within a composition net
[00:33:51] and they the reason this works is
[00:33:54] because the world is is is compositional
[00:33:56] essentially I'm sure there's lots of
[00:33:58] physicists in the room and of course you
[00:34:00] know all the physics is based on the
[00:34:01] idea that uh you know particles assemble
[00:34:04] to form bigger particles and particles
[00:34:06] assemble to for to form atoms and atoms
[00:34:08] for for molecules etc. The world is
[00:34:10] compositional but the visual world is
[00:34:12] also compositional. Um there's a a nice
[00:34:15] quote from um a colleague at Johns
[00:34:17] Hopkins uh Jason Eisner who says um
[00:34:22] you know it's it's basically a play on
[00:34:24] on one of Einstein's famous quote which
[00:34:26] is um what's the most incomprehensible
[00:34:30] thing about the world is that it is
[00:34:31] comprehensible and it's probably because
[00:34:33] it's compositional. So his form of it is
[00:34:36] the world is compositional or there is a
[00:34:38] god.
[00:34:43] It's slightly obnoxious. I I
[00:34:47] um so over the last uh three or four
[00:34:50] years since this revolution occurred
[00:34:51] people there's been a lot of really
[00:34:53] smart people kind of coming to the field
[00:34:54] and coming up with really new ideas and
[00:34:57] surprising
[00:34:59] even me on how well those things can
[00:35:01] work. Uh so there's been in particular
[00:35:03] an inflation in the number of layers
[00:35:06] that those neural nets have now nowadays
[00:35:09] uh at the top you you the top two
[00:35:11] systems VG which is from Oxford and and
[00:35:14] and the Google net which is from Google
[00:35:17] have something like like 20 or 30 layers
[00:35:20] and they were proposed around 2014 or 15
[00:35:24] and at the bottom you have a new form of
[00:35:27] of neural net called ResNet that means
[00:35:28] residual networks. Uh this was proposed
[00:35:30] by a gentleman called Kiming H who at
[00:35:32] the time was at Microsoft research Asia.
[00:35:34] This is just a year and a half ago or so
[00:35:37] uh two years ago and this works
[00:35:40] amazingly well. The basic idea behind
[00:35:41] ResNet is that by default every layer is
[00:35:44] basically the identity function and what
[00:35:46] the neuronet itself is computing is a
[00:35:48] deviation uh of the function you want to
[00:35:51] compute with respect to the identity
[00:35:53] function. And it turns out it kind of
[00:35:55] built in some sort of failsafe mechanism
[00:35:56] that makes the system survive having
[00:35:59] many many layers. And so modern
[00:36:01] commercial nets have anywhere between 50
[00:36:03] and 100 layers using this kind of trick.
[00:36:08] Uh Kaming now works at Facebook.
[00:36:12] Um so commercial nest has been applied
[00:36:14] to all kinds of different things. This
[00:36:15] is an application. So if you are on
[00:36:17] Facebook and you upload a picture of
[00:36:19] your friends, your friends are tagged
[00:36:21] automatically and the face recognition
[00:36:23] system uses a conversion net. In fact,
[00:36:26] every photo uploaded on Facebook goes
[00:36:28] through through three conviction nets
[00:36:31] and uh so one commercial net is used to
[00:36:34] recognize faces. Another one is used to
[00:36:36] essentially recognize all the objects in
[00:36:38] the image and tags and etc. Um this is
[00:36:42] used for kind of this you know ranking
[00:36:44] the image in your newsfeed. And the
[00:36:47] third one is to detect objectionable
[00:36:49] content essentially. And
[00:36:53] you realize there is kind of a slight
[00:36:54] problem with scale when you learn that
[00:36:58] people upload on the order of 1 billion
[00:37:01] to one and a half billion photos on
[00:37:02] Facebook every day.
[00:37:06] Um so we're burning a lot of cycles and
[00:37:08] a lot of uh megawws into uh turning you
[00:37:12] know running commercial nets. Um I know
[00:37:15] there are kind of you know ASIC
[00:37:17] designers in the room here. I think you
[00:37:19] do a lot of good in the world if you had
[00:37:20] some way of computing those things
[00:37:21] really cheaply in terms of power
[00:37:25] uh because it's going to get worse.
[00:37:27] We're going to apply this to video. Uh
[00:37:28] those networks are going to be
[00:37:30] everywhere in your car and you know
[00:37:33] vacuum cleaner.
[00:37:35] Um
[00:37:37] uh so a few years ago about 10 years ago
[00:37:39] uh there was a DARPA program called
[00:37:41] Lagger which means learning applied to
[00:37:42] ground robots where the idea was to use
[00:37:45] machine learning to kind of see if a
[00:37:48] robot could be trained to drive itself
[00:37:50] in nature off-road robot.
[00:37:53] And what we used there was a commercial
[00:37:55] net that is basically applied with a
[00:37:56] sliding window over an entire image and
[00:37:58] then classifies every window if you want
[00:38:01] in the in the image as to whether the
[00:38:03] central pixel is traversible or not
[00:38:05] whether the robot can drive over it or
[00:38:06] not. Uh and the interesting thing about
[00:38:09] it is that it basically self trains by u
[00:38:13] uh getting the
[00:38:15] information as to whether something is
[00:38:16] traversible using stereo vision but that
[00:38:19] only works at short range. So for long
[00:38:20] range vision uh it's using the
[00:38:22] commercial net. So it's been trained. It
[00:38:24] can label the entire image and after
[00:38:26] that uh you can test it and pisky
[00:38:29] students annoying this poor robot.
[00:38:33] So they they're actually entitled to do
[00:38:35] this because uh they are the ones who
[00:38:37] worked on the project and they're pretty
[00:38:39] sure the robot is not going to break
[00:38:40] their leg because they wrote the code.
[00:38:44] Uh so this was Rya Hatel and Pa Manet.
[00:38:48] Rya Hell leads the robotics group at
[00:38:50] DeepMind in uh in London and Pame also
[00:38:54] works on robotics at at Google in
[00:38:56] California.
[00:38:59] Uh a consequence of this project is that
[00:39:01] we uh eventually
[00:39:03] figured out how to
[00:39:06] uh apply this technique of kind of a
[00:39:08] sliding window to classify every pixel
[00:39:10] in an image with a category of the
[00:39:11] object it belongs to. Right? So here you
[00:39:14] the system this was built around 2009 uh
[00:39:17] 2010. Uh the system kind of labels the
[00:39:20] road, the sidewalk, the cars, the trees,
[00:39:23] the buildings, the windows, the doors,
[00:39:25] etc. Uh pedestrians. Uh you really don't
[00:39:28] want to miss pedestrians.
[00:39:31] Uh and this is,
[00:39:33] you know, it's not perfect. Uh there's
[00:39:35] been a lot of progress in those kind of
[00:39:36] techniques in the last few years. You
[00:39:38] know, it labels the the bottom here as
[00:39:40] desert, which is obviously wrong. This
[00:39:42] is um Washington Square Park in the
[00:39:44] middle of Manhattan. There's no beach
[00:39:46] I'm aware of and it's certainly not a
[00:39:47] desert.
[00:39:49] Uh that's as good as it as it gets or as
[00:39:52] it got back then.
[00:39:54] And it got um uh the idea kind of uh
[00:40:00] percolated in in sort of a number of
[00:40:02] different circles, particularly people
[00:40:05] working on self-driving cars. So here
[00:40:07] what you see is uh a short video from a
[00:40:10] company an Israeli company called
[00:40:12] Mobilei. It's been around for a while
[00:40:13] and they kind of adopted the religion of
[00:40:15] deep learning a few years ago and kind
[00:40:17] of retool the entire system around deep
[00:40:18] learning and now they that's that's what
[00:40:20] they use for for the vision system. For
[00:40:22] a while they were the providers of
[00:40:23] vision systems for Tesla. Uh they kind
[00:40:26] of divorced a year ago but um now Tesla
[00:40:29] is its own its own system. Another
[00:40:31] company that's really kind of gotten
[00:40:33] into this in a big way is Nvidia. the
[00:40:36] the the GPU manufacturers.
[00:40:39] And in fact,
[00:40:45] uh, Nvidia,
[00:40:48] if I can get my pointer.
[00:40:57] So, this is a a car built by Nvidia
[00:40:59] called BB-8, and it is driving itself in
[00:41:02] kind of fairly
[00:41:05] uh weird environment. This is actually
[00:41:07] in Homedale in the Bell Labs site in
[00:41:10] Homeell.
[00:41:12] This is the parking lot in Homeell, New
[00:41:13] Jersey for those of you who've been
[00:41:15] there before, right? So this is before
[00:41:17] training and and that's after training.
[00:41:20] Okay, after you know a few hours of
[00:41:22] basically observing the person driving
[00:41:24] the car around. So it's it's called
[00:41:26] imitation learning which is that which
[00:41:28] means that there is a a commercial net
[00:41:30] looking at a picture coming out of the
[00:41:31] camera and uh
[00:41:34] and then learning to predict what the
[00:41:36] steering angle is going to be of the
[00:41:38] car. Uh uh this is not in Homedale. This
[00:41:42] is in uh
[00:41:44] San Hook, I believe. Sunny Hook Park in
[00:41:46] New Jersey.
[00:41:48] So
[00:41:50] uh works pretty well. They have kind of
[00:41:52] more recent demos. If you if you look
[00:41:53] for autonomous car uh Nvidia, you'll
[00:41:56] you'll see a bunch of videos there that
[00:41:58] are kind of cool.
[00:42:02] So a lot of interesting things in this
[00:42:04] uh in this space. Uh more recently the
[00:42:07] the the group uh I lead at Facebook. So
[00:42:09] it's um it's kind of the first research
[00:42:11] lab at Facebook really that was created
[00:42:13] at the beginning of 2013
[00:42:16] beginning 2014. uh it's now grown to u
[00:42:19] about 90 people uh combination of
[00:42:23] scientists and engineers uh and we're
[00:42:25] we're strictly focused on on AI
[00:42:27] essentially um and trying to kind of
[00:42:30] push the state of the art forward. So
[00:42:32] this is a vision system that was built
[00:42:33] at Facebook that uh recognizes objects
[00:42:36] in images but doesn't just recognize
[00:42:38] them it also kind of paints their
[00:42:40] outline if you want. So it figures out
[00:42:41] where objects are and it's accomplish
[00:42:43] that that's been trained to classify
[00:42:44] object but also to generate a mask of
[00:42:46] the object it's currently recognizing
[00:42:50] and uh it's a it's very complicated
[00:42:54] combination of commercial net of various
[00:42:57] kinds trained in a very complex way. The
[00:42:59] code is open source if you are
[00:43:00] interested in playing with it. Uh it's
[00:43:02] called sharp mask and it's on GitHub
[00:43:06] and it can do things like this. So it
[00:43:08] will uh recognize objects and draw the
[00:43:10] outline of all the objects. Person, cell
[00:43:11] phone, laptop, uh you know, person even
[00:43:14] behind chicken wire, even if you see
[00:43:16] only the heads. U look at the fuzzy
[00:43:19] people in the back.
[00:43:21] Uh this thing can only handle about 80
[00:43:23] categories. Um broccoli.
[00:43:29] I actually don't like broccoli, so you
[00:43:32] can imagine a robot picking up broccoli
[00:43:33] out of Chinese dishes.
[00:43:38] And the best application of all this is
[00:43:40] counting sheeps.
[00:43:46] So if you ask a a computer vision
[00:43:48] researcher five years ago, how long is
[00:43:50] it going to take for us to be able to do
[00:43:51] this kind of stuff, they would have told
[00:43:52] you, you know, at least 10 years. Uh
[00:43:55] they would have no idea, you know, how
[00:43:57] to actually do it. And the fact that we
[00:43:58] can now essentially do this is
[00:44:01] astonishing even to me.
[00:44:05] Okay. So now let me let me talk about
[00:44:07] the
[00:44:09] meat of the subject if you want after
[00:44:11] this long preliminary which is uh really
[00:44:14] what are the obstacles to uh to to AI
[00:44:18] and how do we make progress from from
[00:44:20] here. So it looks you know if you read
[00:44:22] the media if you if you judge by how
[00:44:24] many millions venture capitalists are
[00:44:26] investing in AI companies or or how many
[00:44:30] uh billions companies like like Google
[00:44:32] Facebook Microsoft u by do you know
[00:44:36] everybody essentially are investing into
[00:44:38] AI R&D um you would think the problem is
[00:44:41] solved it's not it's not solved at all
[00:44:44] uh there is very useful applications we
[00:44:46] can build out of AI today certainly in
[00:44:48] image recognition and for transportation
[00:44:50] is There's a lot of excitement about
[00:44:52] better medical imaging system. So
[00:44:54] medical image analysis system based on
[00:44:56] conventional nets. There's already
[00:44:57] papers coming out of uh you know take a
[00:44:59] picture of your skin with a cell phone
[00:45:00] and basically can tell you what kind of
[00:45:03] skin element you have.
[00:45:05] Um but but it's not like we know how to
[00:45:08] solve AI.
[00:45:10] Uh there still pipe dream. So what are
[00:45:12] the obstacles really to kind of making
[00:45:14] real progress in AI?
[00:45:16] uh machines need to be able to learn and
[00:45:19] understand how the world works and
[00:45:21] currently they don't they don't have
[00:45:22] common sense.
[00:45:24] Uh so there's a lot of deep learning
[00:45:25] techniques that are applied to text
[00:45:27] understanding to translation. So all the
[00:45:30] translation systems that have been
[00:45:31] deployed by by Facebook and Google in in
[00:45:33] the last few months use neural nets.
[00:45:35] They're based on neural nets. They're
[00:45:36] based on deep learning. Um some of them
[00:45:39] use commercial nets. Most of them use
[00:45:40] what's called recurrent nets. Some of
[00:45:42] them use a combination. But you know
[00:45:45] basically we need machines to understand
[00:45:47] how the world works the the physical
[00:45:48] world the digital world how people work
[00:45:50] things like that and they need to
[00:45:52] acquire some level of common sense. So
[00:45:54] if you think about what's required for
[00:45:57] an intelligent system you you need the a
[00:45:59] system to be able to perceive to kind of
[00:46:01] get an estimate of the state of the
[00:46:02] world. U you need the machine to
[00:46:06] remember you need a machine to plan and
[00:46:08] reason. But one of the most important
[00:46:11] characteristic is that you need a
[00:46:12] machine to be able to predict. And I
[00:46:14] would say that um I would claim that the
[00:46:17] essence of intelligence is the ability
[00:46:18] to predict. The smarter you are, the
[00:46:21] better at predicting you are. Um
[00:46:24] it's not it's not the only thing you
[00:46:26] need to be able to do, but it's it's a
[00:46:28] very important one.
[00:46:31] So I just mentioned common sense. What
[00:46:32] does that mean really? What is common
[00:46:34] sense?
[00:46:35] So here is an example of that you know
[00:46:38] still completely from amongst most AI
[00:46:40] systems all AI systems that we know of
[00:46:42] um uh a simple sentence called a wine
[00:46:45] schema. So Winterrad is a you know a
[00:46:48] grand old father of uh of uh of AI more
[00:46:53] classical logic based AI and he came up
[00:46:55] with sentences of this type the trophy
[00:46:57] doesn't fit in the suitcase because it's
[00:46:58] too large or the trophy doesn't fit in
[00:47:00] the suitcase because it's too small. So
[00:47:02] in the first in the first form you know
[00:47:04] that the it refers to the trophy
[00:47:07] and in the second form you know the it
[00:47:09] refers to the suitcase and the reason
[00:47:10] you know this is that you know the
[00:47:12] physical constraints of the world you
[00:47:13] know what those objects are supposed to
[00:47:14] do and so that's how you can sort of
[00:47:17] lift the ambiguity about what the it
[00:47:19] refers to and there is a my colleague at
[00:47:22] at NYU um Ernie Davis has made a list of
[00:47:26] you know 150 of those things u there are
[00:47:30] data sets that that people measure the
[00:47:32] performance of AI systems on this and
[00:47:34] the best AI systems, you know, get maybe
[00:47:36] 60ish
[00:47:38] 65% correct. Humans are, you know, above
[00:47:41] 95.
[00:47:43] Um, here's another example. If I say u
[00:47:47] um Marcus picked up his bag and left the
[00:47:50] room, um,
[00:47:53] this is not a suggestion, by the way.
[00:47:55] Um,
[00:47:59] even if you don't know Marcus, even if
[00:48:01] you don't know what room I'm talking
[00:48:02] about or which shape his bag takes, just
[00:48:06] with these few words, you can imagine a
[00:48:07] sequence of event that has to occur. You
[00:48:09] your your your common sense is is
[00:48:11] filling in the blanks that are left open
[00:48:14] by this text. But because you know the
[00:48:16] physical constraints of the world, you
[00:48:17] know that uh Marcus is probably gonna
[00:48:19] stand up and extend his arm and close
[00:48:21] his hand around the handle of his bag
[00:48:23] and then it's probably going to walk and
[00:48:24] walk towards the door, open the door,
[00:48:27] etc. Uh is is very likely not going to
[00:48:31] attract his bag through telekinesis.
[00:48:33] He's not going to dematerialize like
[00:48:36] like this dude here. Oh, it's not
[00:48:38] playing um uh to get out of the room.
[00:48:41] He's not going to fly to the door. is
[00:48:43] not going to go right through the door.
[00:48:45] Uh it's going to open it. So there's a
[00:48:47] lot of things you you can infer because
[00:48:48] you know there's millions and millions
[00:48:50] of facts of this type you can infer
[00:48:51] because you know the constraints of the
[00:48:53] world. That's what machines don't have.
[00:48:54] They don't have enough knowledge about
[00:48:56] the constraints of the world to kind of
[00:48:57] have this kind of common sense and
[00:48:58] therefore they can't fill in the blanks
[00:49:00] and that's what really annoying
[00:49:03] to talk to a computer basically.
[00:49:06] Um
[00:49:11] so common sense is really the ability to
[00:49:12] fill in the blanks. It's the ability to
[00:49:14] infer the state of the world from
[00:49:15] partial information from perception to
[00:49:18] uh infer the future from the past and
[00:49:20] the present
[00:49:22] u which is really necessary for planning
[00:49:24] to infer past events from the present
[00:49:25] state of the world. Um and we do this
[00:49:29] all the time. It's in fact so automatic
[00:49:31] that we don't even realize we're doing
[00:49:33] it. Every one of us has a kind of a
[00:49:36] blind spot in your retina, which is
[00:49:38] where the optical nerve punches through
[00:49:40] your retina to get to your brain. Uh so
[00:49:43] there's one area in your visual field
[00:49:46] where you don't see anything.
[00:49:48] And it doesn't feel like we don't see
[00:49:50] anything in this location. You actually
[00:49:52] have to design an experiment to realize
[00:49:53] you can't see there. Um, and it's
[00:49:56] because our brain sort of fills in the
[00:49:58] blanks,
[00:49:59] you know, kind of infer what's in that
[00:50:02] location in the image.
[00:50:05] Um, if you only see my left profile, you
[00:50:08] can pretty much infer infer what I look
[00:50:10] like on the other side because you know
[00:50:13] that most faces are more or less
[00:50:14] symmetric. So, there's a lot of things
[00:50:16] like this that that, you know, we rely
[00:50:17] on like a lot of um, we figured out the
[00:50:20] dependencies of a lot of variables and
[00:50:22] and that's what gives us common sense.
[00:50:25] So predicting whatever you don't know
[00:50:27] from whatever you know is predictive
[00:50:30] learning or learning to predict I guess
[00:50:32] is predictive learning and in my opinion
[00:50:35] that's the key to um uh making
[00:50:39] significant progress in AI. Um so this
[00:50:44] predictive learning is unsupervised in
[00:50:46] the sense that you would like the
[00:50:47] machine to be trained by just observing
[00:50:49] the world uh the way essentially
[00:50:52] children and animals train themselves.
[00:50:53] Right? There's a lot of concepts uh that
[00:50:56] we learn as as babies that we don't
[00:50:59] realize we've learned because they're
[00:51:00] kind of subconscious. But uh but there's
[00:51:02] a lot of concepts about the world that
[00:51:04] we learned when we were babies. Uh like
[00:51:05] we learned that the world is
[00:51:06] threedimensional. We learned that there
[00:51:07] are independent objects that can move in
[00:51:09] front of each other, you know, from
[00:51:10] parallax. We have two eyes and we can
[00:51:12] move our head. Uh we uh we learn object
[00:51:15] permanence. So we learned that um when
[00:51:18] uh when an object is is is hidden behind
[00:51:20] another
[00:51:22] you know some of you can't see this uh
[00:51:24] this bottle now you you know the bottle
[00:51:26] is still there.
[00:51:28] Um that's object permanence. Babies
[00:51:31] learn this after a few months of life.
[00:51:33] You learn also that an object that's not
[00:51:35] supported is going to fall. uh babies
[00:51:38] learn this between the age of six and
[00:51:40] eight months. So all of those things
[00:51:42] that we take for granted, we all learn
[00:51:43] them and we like machines to do to learn
[00:51:45] this as well. And so there's a couple
[00:51:47] justification for the the necessity of
[00:51:50] learning through unsupervised learning
[00:51:51] which which means learning from data
[00:51:53] that just comes to us from the world
[00:51:55] without being labeled by uh teachers or
[00:51:57] humans.
[00:51:59] And uh one uh one argument is that the
[00:52:02] number of samples that are required to
[00:52:04] uh train a large learning machine for
[00:52:06] any task depends on the amount of
[00:52:08] information that we ask the machine to
[00:52:09] predict.
[00:52:11] And so Jeffington has an argument that
[00:52:13] says uh the brain has about 10 to the 14
[00:52:15] synapses and we live for only about 10^
[00:52:17] the 9 seconds. So we have a lot more
[00:52:20] parameters than data.
[00:52:22] So this motivates the idea that we must
[00:52:24] do a lot of unsupervised learning since
[00:52:25] the perceptual input including proper
[00:52:27] reception is the only place where we can
[00:52:29] get 10 to the five dimensions of
[00:52:30] constraints per second. Uh that's that's
[00:52:33] a huge argument for unsupervised
[00:52:35] learning. We don't get enough
[00:52:36] information through language. We don't
[00:52:38] get enough information through uh you
[00:52:40] know our our teachers. We get a huge
[00:52:42] amount of information for our
[00:52:43] environment by just observing.
[00:52:47] So I came to this uh slightly obnoxious
[00:52:50] uh uh slide. It's obnoxious to people
[00:52:53] who work on reinforcement learning. So
[00:52:55] there are three types of reinforce three
[00:52:56] type of learning really in machine in
[00:52:58] learning theory or machine learning. One
[00:53:00] is called reinforcement learning. So
[00:53:02] reinforcement learning is kind of like
[00:53:05] similar to when you train a pet or a
[00:53:06] circus animal. You wait you wait for the
[00:53:08] animal to do the right action and then
[00:53:11] you reward it. Okay? It's very
[00:53:13] inefficient. It requires lots of trials
[00:53:15] because if the space of possible actions
[00:53:17] is very large, then there's a good
[00:53:19] chance the animal is never g, you know,
[00:53:20] it's going to take a very long time
[00:53:21] before figuring out what the right
[00:53:22] action is. Uh, and so it's very
[00:53:24] inefficient. It works in certain
[00:53:26] situations. So, for example, for games,
[00:53:28] it works really well to train a system
[00:53:30] to play games like like go for example
[00:53:33] or or chess or things of that type. And
[00:53:37] the reason is that you can have many
[00:53:39] copies of the machine play against
[00:53:41] itself millions or millions of games
[00:53:44] uh and eventually figure out figure out
[00:53:46] what the right policy is. This was very
[00:53:48] successful for for checkers in the 50s.
[00:53:51] There's a famous work by Samuel from
[00:53:53] IBM.
[00:53:55] Uh in the 90s there were very successful
[00:53:57] series of work by Jerry Toro also from
[00:53:58] IBM. uh where he had a kind of you know
[00:54:02] grandmaster level bagaman player using
[00:54:04] reinforcement learning and neural nets
[00:54:06] and more recently of course you heard
[00:54:07] about deep mind's alpha go system uh
[00:54:09] which use a convolutional net applied to
[00:54:12] a goboard train with a combination of
[00:54:14] imitation learning on recorded games by
[00:54:17] grandmasters and then fine-tune by
[00:54:19] playing against itself millions and
[00:54:20] millions of of of games
[00:54:24] and it's you know pretty much unbeatable
[00:54:25] nowadays.
[00:54:29] So reinforcement running uh run you know
[00:54:31] works in in games. It works in certain
[00:54:33] situations for like search ranking and
[00:54:36] things like that ad ranking but it
[00:54:39] doesn't really work in the real world
[00:54:40] when you have sort of physical
[00:54:41] constraints. And the main problem uh the
[00:54:45] main reason for this is that you can't
[00:54:47] have many many trials in the real world.
[00:54:49] The main problem with the real world is
[00:54:51] that you cannot you cannot run it faster
[00:54:52] than real time.
[00:54:56] maybe thankfully. Um
[00:54:59] so supervised running we talked about it
[00:55:01] u you give more information to the
[00:55:02] machine you feed it the correct answer
[00:55:04] and then unsupervised learning there's a
[00:55:05] huge amount of information you feed to
[00:55:07] the machine but it's unreliable
[00:55:08] information it's uh you know uh I'm I'm
[00:55:13] putting this uh this bottle here in my
[00:55:16] hand. I'm going to let it go. What's
[00:55:18] going to happen? It's going to fall. So
[00:55:20] you can predict it's going to fall. You
[00:55:21] can you probably cannot predict which
[00:55:22] side. Um so we get a huge amount of
[00:55:25] information from the environment by just
[00:55:26] observing it. And so that led me to this
[00:55:29] analogy that if intelligence is a cake
[00:55:32] in this case a black forest cake. Um the
[00:55:35] uh bulk of the cake is unsupervised
[00:55:37] learning the icing on the cake is
[00:55:38] supervised learning and the cherry on
[00:55:40] the cake is reinforcement learning. And
[00:55:41] this has become a running joke in the
[00:55:43] machine learning community now. Um
[00:55:44] there's a lot of talks that have various
[00:55:46] versions of this cake. You know some of
[00:55:48] them with lots of cherries on top.
[00:55:55] Um, but reinforcement learning, you
[00:55:58] know, works for games. That's what I
[00:55:59] mentioned earlier. This is a a system to
[00:56:01] play Doom that was built at at Facebook
[00:56:03] by a gentleman called Young Dong Tian
[00:56:05] who is a research scientist at Facebook
[00:56:07] research in in California. Uh, turns out
[00:56:10] there is a early competition of this and
[00:56:12] he won it with his system. I mean his
[00:56:14] system won it.
[00:56:17] Um, so that's again pure reinforcement
[00:56:18] running. Uh another uh problem we're
[00:56:21] attacking at at Facebook uh is uh
[00:56:24] slightly more complex games like uh like
[00:56:26] like Starcraft. So Starcraft is sort of
[00:56:29] a combination strategy uh it's a
[00:56:31] real-time strategy game and there is
[00:56:34] real-time battles but you have to also
[00:56:36] build all kinds of stuff. So it's
[00:56:38] completely unsolved. It's very very
[00:56:40] challenging. It's something that both uh
[00:56:43] Google and Facebook are working on and
[00:56:44] and several other people uh and trying
[00:56:46] to figure out if it's solvable at all at
[00:56:48] the moment. This is a very simple system
[00:56:50] that was trying to just do local very
[00:56:52] simple battles.
[00:56:57] Um but here is an idea that goes back uh
[00:57:00] many years ago by Rich Sutton who is
[00:57:02] sort of one of the founding fathers of
[00:57:03] reinforcement learning. Uh and he was
[00:57:05] proposing an architecture called Dina
[00:57:07] integrated architecture for learning
[00:57:08] planning and reacting. And there's a
[00:57:10] quote from him here that says the main
[00:57:12] idea of Dina is that the old common
[00:57:14] sense is the old common sense idea that
[00:57:17] planning is training things in your head
[00:57:19] using an internal model of the world.
[00:57:21] This suggests the existence of a more
[00:57:23] primitive process for training things
[00:57:24] not in your head but through direct
[00:57:26] interaction with the world.
[00:57:28] Reinforcement learning is the name we
[00:57:29] use for this more primitive direct kind
[00:57:31] of training. And Dina is the extension
[00:57:33] of reinforcement learning to include a
[00:57:35] learned world model. So basically that's
[00:57:37] the idea that and in fact it's very
[00:57:38] classical in in control theory that when
[00:57:41] you want to control a plant or you know
[00:57:43] the the standard word that control
[00:57:45] theory is used for this you have a model
[00:57:47] of the plant the system you want to
[00:57:49] control and you use this model as a
[00:57:51] simulator to kind of see what the effect
[00:57:53] of the sequence of commands will uh will
[00:57:55] produce and that's how you do planning.
[00:57:57] uh that's how like robot planning is
[00:57:59] done for example
[00:58:01] but in the context of learning you need
[00:58:02] to learn the model control theory is
[00:58:05] called that system identification and
[00:58:07] you also need to learn the controller to
[00:58:09] you know figure out the good sequence of
[00:58:11] of commands so it's an old idea and very
[00:58:14] classical in some ways but it's only
[00:58:16] making inroads in machine learning and
[00:58:19] AI you know fairly recently so what is
[00:58:23] the architecture of an intelligent
[00:58:24] system you and and This is really sort
[00:58:27] of inspired by a little bit by how the
[00:58:29] brain is structured. You have the world
[00:58:32] and you have an agent, intelligent
[00:58:34] agent. The intelligent agent produces
[00:58:36] actions that influence the world and the
[00:58:38] world produces percepts that are
[00:58:40] interpreted by the agent. Um, and the
[00:58:44] loop is uh is complete. The agent inside
[00:58:46] of itself here it's outside but it
[00:58:49] should be inside really has an objective
[00:58:51] and it tries to kind of take the actions
[00:58:55] on the world that will put it in a state
[00:58:58] that will minimize its objective. Think
[00:59:01] of the objective as a cost not as a as
[00:59:04] happiness. Think of it as unhappiness or
[00:59:06] something. Um so it wants to minimize
[00:59:09] the value of the objective over the long
[00:59:11] run. And if you want the agent to be
[00:59:14] able to do a good job at this uh do this
[00:59:16] intelligently
[00:59:18] inside of itself, it has to have a world
[00:59:20] simulator that is going to allow it to
[00:59:22] predict what's going to happen as a
[00:59:23] consequence of its actions or just
[00:59:25] what's going to happen because the world
[00:59:26] is being the world.
[00:59:29] So that's this world simulator. Um to
[00:59:31] initialize the simulator, you need a
[00:59:33] perceptual system that estimates the
[00:59:35] state of the world well enough so that
[00:59:36] the simulator can be run accurately.
[00:59:39] And then you have a module called an
[00:59:42] actor that produces action proposals to
[00:59:44] the simulator um to kind of run it
[00:59:47] forward and a critic. And the critic is
[00:59:49] a trainable system that predicts the
[00:59:51] expected long-term value of the
[00:59:53] objective.
[00:59:54] So the critic you know tries to kind of
[00:59:56] predict in the long run if I take this
[00:59:59] action what what's going to happen to
[01:00:00] me? Is it going to be good or bad? Um if
[01:00:04] I want to be become a little philosoph
[01:00:06] philosophical a lot of emotions that we
[01:00:07] interpret as emotions are basically
[01:00:09] anticipations of things that will happen
[01:00:11] uh whether they're good or bad like fear
[01:00:13] for example is the result of predicting
[01:00:15] that something really bad is uh likely
[01:00:17] to to happen and and you know you have
[01:00:21] this prediction and you're kind of
[01:00:22] trying to figure out what to do. Elation
[01:00:24] is the anticipation of something good
[01:00:26] about to happen.
[01:00:31] So that's the idea of model based
[01:00:33] reinforcement learning
[01:00:36] and we know how to build a critic. We
[01:00:38] know how to build the actor pretty much.
[01:00:39] What we don't know how to do is build a
[01:00:41] world simulator or we don't know how to
[01:00:42] train it really. We know how to do the
[01:00:45] perception side I showed you earlier
[01:00:48] how do we learn forward models of the
[01:00:50] world? How do we learn predictive models
[01:00:51] of the world? So there is a small
[01:00:53] experiment that was done at Facebook a
[01:00:54] couple years ago by Adam Larer, Sam
[01:00:57] Gross, and Rob Fergus where they took a
[01:00:59] a 3D game engine as as kind of a virtual
[01:01:02] world if you want and plug the
[01:01:03] convolutional net on it and ask the
[01:01:05] commercial net to predict what's going
[01:01:07] to happen, you know, where the where are
[01:01:09] those blocks going to fall, how are they
[01:01:11] going to fall um by just observing what
[01:01:14] happens when you run the the simulation.
[01:01:16] And this is the kind of prediction that
[01:01:18] that occurs. So you see the initial
[01:01:20] condition on the left uh at the the top
[01:01:23] band of four uh images is what actually
[01:01:27] happens in this in the in this virtual
[01:01:29] world and below is a row of predictions
[01:01:33] at at various times in the future. And
[01:01:35] you see that the system kind of do does
[01:01:37] a fairly decent job at predicting what's
[01:01:39] going to happen except in some cases
[01:01:41] where it's not clear how to predict the
[01:01:43] the predictions are fuzzy. And it's
[01:01:45] because there are several ways things
[01:01:46] could fall and the best thing that the
[01:01:48] machine can do is kind of predict an
[01:01:49] average of all the various things that
[01:01:50] could happen.
[01:01:54] Um I'll come back to to this kind of
[01:01:56] problem in a minute. But before that
[01:01:58] I'll talk about uh why you would need a
[01:02:01] model of the world for another reason
[01:02:03] for um understanding text and answering
[01:02:07] questions having common sense about
[01:02:09] events uh given to you by text. And
[01:02:11] there is a series of work which I think
[01:02:13] is extremely interesting in the context
[01:02:14] of deep learning which is the idea of
[01:02:16] using uh neural nets that are augmented
[01:02:20] by uh a short-term memory. Um so it
[01:02:23] turns out neuronal nets are very bad at
[01:02:24] remembering things. You can train them
[01:02:26] to perform
[01:02:29] a task
[01:02:31] but they basically don't have memory. So
[01:02:33] there are recurrent nets, so networks
[01:02:34] that have loops and those have, you
[01:02:36] know, reverbering states and stuff like
[01:02:38] that that kind of give them a little bit
[01:02:39] of memory. But it turns out this memory,
[01:02:40] this memory is terrible. So even
[01:02:43] recurrent nets can't remember things
[01:02:44] for, you know, more than a few
[01:02:45] iterations. So there's been this idea
[01:02:47] that's been floating around for for a
[01:02:49] couple years now of or became more
[01:02:52] popular over the last few years of
[01:02:54] augmented recurrent networks with with a
[01:02:56] memory. There's roots of this idea in a
[01:02:59] very popular architecture called long
[01:03:00] short-term memory L at STM which is a
[01:03:02] type of recurrent net proposed by ohiter
[01:03:03] and in the late 90s. Um and more
[01:03:07] recently there's work at Facebook by
[01:03:09] Western at Al by Julian Nikolov and work
[01:03:12] at deep mind uh
[01:03:15] on neural training machine and what's
[01:03:17] generally called differentiable computer
[01:03:19] computing or differentiable neural
[01:03:20] computers. So you basically build a
[01:03:22] computer
[01:03:24] out of differentiable parts if you want
[01:03:26] which means now you can train the
[01:03:28] computer to run a particular algorithm
[01:03:30] by gradient descent. It's a very kind of
[01:03:33] interesting uh area to explore at the
[01:03:35] moment.
[01:03:37] And so here is what uh differentiable
[01:03:39] memory looks like. The memory module in
[01:03:41] one of those recurrent nets um it's
[01:03:44] basically an associative memory. And so
[01:03:46] an address comes in it's a vector. You
[01:03:48] comput the dot product of this vector
[01:03:49] with a bunch of keys and then you pass
[01:03:52] the output of those to what physicists
[01:03:55] in the room will recognize as a gib
[01:03:57] distribution. This is the formula on the
[01:03:59] left. Basically, it takes all the
[01:04:00] outputs that come out that you can
[01:04:02] interpret as as energies and it takes
[01:04:04] the exponential and normalize them. So
[01:04:06] what you get on the output is a bunch of
[01:04:07] coefficients that are between zero and
[01:04:09] one and some to one and you use them to
[01:04:11] multiply uh the values which themselves
[01:04:14] are vectors. what you get on the output
[01:04:15] of the memory is the weighted sum of
[01:04:17] those vectors weighted by those
[01:04:19] coefficients coming out of the input. So
[01:04:22] if the address exactly matches one of
[01:04:23] the vectors and the other ones are
[01:04:25] orthogonal to it then one of those
[01:04:26] values is going to be one the other one
[01:04:27] zero after the soft max is going to be a
[01:04:29] little soft but that that's okay and
[01:04:31] then at the output you will get the the
[01:04:33] vector that has been indexed by this uh
[01:04:36] by this address but the thing is all the
[01:04:38] operations there are soft and
[01:04:39] differentiable and so you can back
[01:04:40] propagate gradient to that.
[01:04:43] So people have done pretty amazing
[01:04:44] things with memory augmented networks of
[01:04:46] various kinds. Like you can have a
[01:04:48] machine read a small text like this 15
[01:04:51] sentence text which is kind of a 15
[01:04:52] sentence version of Lord of the Rings.
[01:04:55] Bilbo traveled to the cave golem drop
[01:04:56] the ring blah blah blah. Um and at the
[01:04:59] end you can ask questions. Uh where is
[01:05:01] the ring? Where is Bilbo? Etc. And the
[01:05:04] machine can answer. And what it does is
[01:05:05] that it stores each of the statements in
[01:05:07] its memory. And then it we you know it's
[01:05:10] been trained to kind of produce uh with
[01:05:13] with pairs of questions and answers and
[01:05:15] it's trained itself to to access the
[01:05:17] relevant uh memory locations to answer
[01:05:21] particular questions. And so then you
[01:05:22] can ask questions. It's never been
[01:05:23] trained on Lord of the Rings. It's been
[01:05:24] trained on kind of other kinds of
[01:05:26] stories with people moving around and
[01:05:28] carrying things which is really what
[01:05:30] Lord of the Rings is all about.
[01:05:34] Um so my my friends at Facebook um came
[01:05:38] up with a categorization of about 20
[01:05:40] types of questions that you might want
[01:05:42] to ask a machine some of which involve
[01:05:46] simple inferences like you know Brian is
[01:05:48] a lion, Julius is a lion, Julius is
[01:05:50] white, Bernard is green, what color is
[01:05:51] Brian? So if you assume that all lions
[01:05:55] are white then you can you can answer
[01:05:57] that. Um and so there's 20 types of
[01:06:01] questions and until now we had system
[01:06:04] based on memory augmented network that
[01:06:05] could essentially solve 19 types of uh
[01:06:08] out of 20 of those questions. But this
[01:06:10] uh new system that we call entity
[01:06:12] recurrent net actually can solve all 20
[01:06:14] and it's the first time of it the first
[01:06:16] system of it type that can do all 20
[01:06:19] of those so-called baby tasks.
[01:06:23] Um, it's basically a bank. I'm not going
[01:06:25] to go into the details of it, but it's
[01:06:26] basically basically a bank of recurrent
[01:06:29] nets that all take an input, which is a
[01:06:32] simple sentence like John goes to the
[01:06:33] kitchen. Okay, so the sentence go John
[01:06:37] goes to the kitchen is encoded into a
[01:06:38] vector and then it goes into each of
[01:06:39] those memory cells and each memory cells
[01:06:43] has a a gating mechanism that uh has it
[01:06:47] decide whether the information is
[01:06:48] relevant to it. And so you could imagine
[01:06:50] having a memory cell for the location of
[01:06:52] where John is and another memory cell
[01:06:54] for the content of the kitchen. And you
[01:06:56] would the system would update both of
[01:06:58] them when you see the sentence of the
[01:06:59] type John goes to the kitchen.
[01:07:02] Um and
[01:07:05] the magic thing about this is that you
[01:07:06] don't need to tell the system that the
[01:07:09] the uh the memory what the memory cell
[01:07:12] should should do. You just have it read
[01:07:14] a text and then at the end ask a
[01:07:16] question and give it the answer. and it
[01:07:18] kind of figures out how to infer the
[01:07:19] state of the world from all the all the
[01:07:22] sentences it gets. So it kind of learns
[01:07:24] how to maintain a current state of the
[01:07:25] world as the sentences that describe
[01:07:28] events come in. So it's a bit of a
[01:07:30] predictive model uh estimating the state
[01:07:32] of the world from simple sentences.
[01:07:35] Okay. Uh let me switch gear a bit and
[01:07:37] talk about the more general problem of
[01:07:38] unsupervised learning. Um so
[01:07:40] unsupervised learning really is you know
[01:07:43] discovering the structure of the world
[01:07:45] and what that means is figuring out
[01:07:47] dependencies between between variables
[01:07:49] in the world. So if your world consists
[01:07:51] of two variables okay let's imagine uh
[01:07:55] both of your eyes only have one pixel
[01:07:57] each. Okay so your entire visual world
[01:07:59] is two pixels and your entire universe
[01:08:02] is composed of percepts that are those
[01:08:05] those black dots and they distribute in
[01:08:07] those two variables in in that way.
[01:08:08] There is obviously a dependency between
[01:08:10] y1 and y2. If I give you the value of
[01:08:12] y1, you can predict more or less what
[01:08:14] the value of y2 would be with, you know,
[01:08:16] some uncertainty. The the the the
[01:08:19] converse is true as well. If you give
[01:08:20] you the value of y 2, you can sort of
[01:08:22] infer the possible values for y1.
[01:08:26] So h how do we um represent the the the
[01:08:30] fact that a machine should learn this
[01:08:31] kind of dependency not knowing in
[01:08:33] advance whether we need to predict y1
[01:08:35] from y2 or y2 from y1. And the answer to
[01:08:38] this is basically comes from physics or
[01:08:42] from mathematics implicit functions or
[01:08:44] from physics energy functions. We learn
[01:08:46] energy functions. So basically what the
[01:08:48] machine needs to learn is a an energy
[01:08:50] function, a contrast function. Let's
[01:08:52] call it an energy
[01:08:54] that gives you low values on points that
[01:08:56] you observe and higher values everywhere
[01:08:59] else.
[01:09:01] Okay. So we need to come up with a
[01:09:03] neural net of some kind which will have
[01:09:05] parameters and we'll adjust the
[01:09:08] parameters of the machine so that when
[01:09:09] it sees a data point from the world it's
[01:09:11] going to make its output as low as it
[01:09:13] can and then for everything else it's
[01:09:15] going to produce a higher value. Okay,
[01:09:17] it's a function with many inputs an
[01:09:20] image let's say and a single output the
[01:09:22] energy.
[01:09:24] So that's what the learning process
[01:09:25] should look like something like this
[01:09:27] where the surface kind of evolves as uh
[01:09:29] the system is being trained.
[01:09:36] So the big question there is it's easy
[01:09:38] to make the the function produce low
[01:09:40] values for things it observes but the
[01:09:42] question is how do we make it take
[01:09:43] higher values outside for things it
[01:09:46] doesn't observe. So one technique is to
[01:09:48] pick a good set of points contrastive
[01:09:51] points if you want and then push up
[01:09:53] their energy so change the parameters of
[01:09:55] that function so that its output goes up
[01:09:57] and that's kind of what's going on here
[01:09:59] in this little animation.
[01:10:01] Uh in fact there is sort of you know
[01:10:03] eight different ways to do this. There's
[01:10:04] seven which I'm just going to flash but
[01:10:06] not talk about. Uh and then skip to the
[01:10:09] eight eighth ones which I think is
[01:10:11] probably the most exciting idea in
[01:10:12] machine learning in the last 10 years.
[01:10:14] Um I'm allowed to do this because I
[01:10:16] didn't come up with it. Um,
[01:10:19] unfortunately,
[01:10:20] uh, this is an idea, uh, that came out
[01:10:23] of Yoshua Benjö's lab at University of
[01:10:25] Montreal a couple years ago, um, um, by
[01:10:29] a student, his former student now, Ian
[01:10:31] Goodfellow, and it's called adversarial
[01:10:32] training, and it solves the problem of
[01:10:35] predicting under a certain. So, here is
[01:10:38] a scenario where I'd like to train a
[01:10:40] machine to predict the future. Uh, so I
[01:10:43] have what's called a generator. G of X.
[01:10:46] X is the past. Z is a source of random
[01:10:49] vectors, let's say.
[01:10:51] Uh, and Y is a prediction for the state
[01:10:55] of the world, you know, half a second
[01:10:56] later, let's say. Okay. And what I
[01:10:59] trained the system with is many videos
[01:11:01] of me putting a pen on the table and
[01:11:03] letting it go. And of course, every time
[01:11:05] the the pen falls, but every time it
[01:11:07] falls in a different direction.
[01:11:09] So there is a sort of a manifold or at
[01:11:13] least a set of plausible futures which
[01:11:17] you observe in the all those training
[01:11:19] videos where where you see the pen
[01:11:21] falling in all all situations in all
[01:11:23] orientations. In fact uh the this
[01:11:26] manifold is actually a closed surface.
[01:11:28] It's topologically identical to a to a
[01:11:30] circle.
[01:11:32] Okay, which I didn't do right here.
[01:11:36] Um so if you train the predictor to in
[01:11:41] in kind of a supervised mode where you
[01:11:42] tell it you know here is the correct
[01:11:43] answer predict that here is the correct
[01:11:44] answer predict that it's going to get a
[01:11:46] lot of inconsistent uh desired outputs
[01:11:49] and the best thing you can do is predict
[01:11:50] the average of all of those which is
[01:11:51] basically a uh transparent version of
[01:11:55] this pen in all possible positions
[01:11:58] around the circle and it's not a good
[01:11:59] prediction. It's not on the manifold.
[01:12:01] It's the average of the points on the
[01:12:02] manifold. So how do we do this? What we
[01:12:05] need to do is train the machine in such
[01:12:08] a way that when it makes a wrong
[01:12:10] prediction, but it's a prediction that
[01:12:11] happens to be on the right manifold, we
[01:12:13] don't punish it for it. We said, okay,
[01:12:15] you know, you didn't predict that the
[01:12:16] pen fell in the right direction, but you
[01:12:18] actually did predict that the pen was
[01:12:19] going to fall. So, you're not wrong
[01:12:21] technically.
[01:12:23] The problem, of course, is that we don't
[01:12:25] know how to characterize this set. And
[01:12:27] so the trick in adversarial training is
[01:12:29] we're going to train a second neural net
[01:12:32] to learn to tell us if the prediction is
[01:12:36] on the manifold outside. And that's very
[01:12:38] much like the problem I just mentioned
[01:12:40] of learning an energy function, learning
[01:12:41] a contrast function that distinguishes
[01:12:44] uh things that actually occur from
[01:12:46] things that don't occur.
[01:12:50] So that's the the the basic uh process
[01:12:53] is the following. You have the
[01:12:54] discriminator. So the discriminator is
[01:12:56] the one that computes this energy
[01:12:57] function. It takes a prediction u I mean
[01:13:00] it takes the past frames and it takes a
[01:13:03] prediction from the predictor and it
[01:13:05] assesses whether this prediction is
[01:13:07] good. And the way the discriminator
[01:13:09] trains itself is that it takes an actual
[01:13:12] realization from the world and it trains
[01:13:14] itself to produce a low value. These are
[01:13:16] the the the blue beads
[01:13:20] and then when it gets a prediction from
[01:13:22] the generator it assumes it's wrong.
[01:13:24] it's assumed it's outside of the correct
[01:13:26] set of prediction. And so these are the
[01:13:28] green points and it moves up the value
[01:13:30] of the energy for those points. Okay, so
[01:13:33] after a couple iterations, you might end
[01:13:35] up with something like this where the
[01:13:37] the green points have kind of moved
[01:13:39] closer. Uh and so the predictor has so
[01:13:42] the discriminator has kind of figured
[01:13:44] out the the difference between the two
[01:13:46] that that's where the energy comes from.
[01:13:47] But now the way you train the generator
[01:13:49] is that the generator trains itself to
[01:13:51] make predictions that the discriminator
[01:13:53] cannot tell are not real and it can
[01:13:55] cheat because it knows the gradient of
[01:13:57] the output of the discriminator with
[01:13:59] respect to its input and so it can
[01:14:00] adjust its parameter its parameter its
[01:14:03] internal parameters so that uh it
[01:14:05] produces an output that will fool the
[01:14:07] discriminator into thinking it's real.
[01:14:09] So you have this interplay between those
[01:14:10] two networks that train against each
[01:14:12] other which is why it's called
[01:14:13] adversarial training. There's a proof by
[01:14:15] one of my students Michael Material
[01:14:16] which shows that uh the it basically is
[01:14:20] akin to a Nash equilibrium in the end.
[01:14:23] So you minimizing two functions with
[01:14:24] respect to the parameters of those two
[01:14:25] networks and in the end you can reach
[01:14:27] some sort of Nash equilibrium. So you
[01:14:29] can train things like this to do pretty
[01:14:31] amazing things like generate images from
[01:14:33] scratch. So here there is no past to
[01:14:36] predict from. You just give a bunch of
[01:14:37] random numbers to a neural net and have
[01:14:40] it generate an image and you train it to
[01:14:41] generate to you train it with images of
[01:14:43] bedrooms.
[01:14:45] And these are non-existing bedrooms
[01:14:47] generated by neural net. They don't look
[01:14:49] like anything in a training set but they
[01:14:51] look kind of like bedrooms.
[01:14:53] Um
[01:14:56] so the three authors are in different
[01:14:58] institution. Sumichintella is a research
[01:15:00] engineer at Facebook.
[01:15:03] Um you can learn it to you can train it
[01:15:05] to interpolate between manga characters.
[01:15:07] Um you can do face arithmetic. So this
[01:15:11] is kind of fun. You you can figure out
[01:15:13] what input vector random random vector
[01:15:17] uh would produce a particular face by
[01:15:20] gra descent. So you take a face and you
[01:15:22] figure out what input vector would have
[01:15:23] produced this face.
[01:15:26] And you do this for say three faces. a
[01:15:28] man with glasses, a man without glasses,
[01:15:31] and a woman without glasses. So you have
[01:15:33] those three vectors. When run through
[01:15:35] the network, they generate those three
[01:15:36] faces. And now you take the first vector
[01:15:40] minus the second vector plus the last
[01:15:41] vector, you generate through the
[01:15:43] network, and what you get is a woman
[01:15:44] with glasses.
[01:15:47] That's kind of amazing because that
[01:15:48] means, you know, it's figured out that a
[01:15:50] man with glasses is to a man without
[01:15:53] glasses as a woman with glasses is to
[01:15:57] another woman without glasses. You know,
[01:15:59] it's the same vector that links
[01:16:02] women with and without glasses as the
[01:16:04] vector that links men with and without
[01:16:07] glasses.
[01:16:09] There's kind of a energy based form of
[01:16:11] this. uh I talked about the Nash
[01:16:13] equilibrium and I don't want to go into
[01:16:16] formulas but uh it's sort of an energy
[01:16:20] based form of adversarial training the
[01:16:22] one I described to you and this is
[01:16:24] trained on uh a million natural images
[01:16:26] from the imageet data set and if you're
[01:16:28] in the back of the room um you kind of
[01:16:32] squint and you you kind of look at those
[01:16:33] pictures and you say oh they look nice
[01:16:34] they look natural if you're on the front
[01:16:36] row you're saying what the hell is this
[01:16:39] like there's no recognizable objects
[01:16:41] They all look kind of object-like, but
[01:16:43] there's nothing you can recognize here,
[01:16:45] right? There's this like weird looking
[01:16:48] kind of uh,
[01:16:50] you know, this dude here. It's like a
[01:16:54] fast train with a sail and with kind of
[01:16:57] an airplane wing on top of this ocean. I
[01:16:59] mean, it's like, you know, everything is
[01:17:00] kind of mashed together. So, it's
[01:17:01] figured out the low-level statistics of
[01:17:03] images, but not really quite the kind of
[01:17:06] global structure of it. Uh, this is what
[01:17:08] happens when you train on dogs.
[01:17:12] you get kind of soft dogs,
[01:17:17] several daddy dogs, you know,
[01:17:21] and here's what happens when you do
[01:17:22] video prediction. So at the top right is
[01:17:26] video prediction when you train a system
[01:17:29] a fairly large conversion net to predict
[01:17:31] using a le square uh loss essentially
[01:17:34] predict the next frame with you know le
[01:17:36] squareed error and the other six are the
[01:17:40] predictions you get uh when you train
[01:17:42] with this adversarial training
[01:17:43] criterion. So the first four frames of
[01:17:45] every animation is observed is real
[01:17:47] video and then the last two which are
[01:17:49] circled in red are predictions and it
[01:17:52] kind of extrapolates pretty well what's
[01:17:53] going on more or less.
[01:17:58] This is the same system. I'm going to
[01:18:00] show you the second one actually. Same
[01:18:01] system trained on videos taken by a
[01:18:04] camera kind of moving around in
[01:18:05] apartments in New York.
[01:18:07] Uh and so what the system has to do now
[01:18:10] is predicting five frames in the future.
[01:18:12] Again, the predicted one that's circle
[01:18:14] in red. Look at this guy. So, this is
[01:18:16] kind of a bookcase. It's kind of like a
[01:18:17] library and it has to dream up what the
[01:18:19] library looks like at the rest. You
[01:18:21] know, there's another bookcase here
[01:18:23] which is dreaming up as well.
[01:18:25] So, it sort of invents what the rest of
[01:18:27] the apartment should look like as as the
[01:18:29] camera turns. Um, so that's five frames
[01:18:32] and that's 50 frames. And that's where
[01:18:34] you realize that we haven't solved the
[01:18:35] problem because things go to hell after
[01:18:38] a few frames.
[01:18:42] Okay. Um, I think I'm going to stop here
[01:18:44] and uh take some questions and thank you
[01:18:46] for your attention.
[01:18:56] I don't know about you, but I could have
[01:18:58] stayed for the rest of the day. Uh,
[01:18:59] thanks very much, John. So, uh, okay,
[01:19:02] questions. We'll take as many as he can
[01:19:04] stomach and then actually lunch is going
[01:19:06] to be a limiting function at some point.
[01:19:08] The stomach will come into it. So, off
[01:19:10] you go, Al.
[01:19:12] first.
[01:19:12] Oh, I need a mic and then I apparently
[01:19:14] have to repeat it so that we can hear it
[01:19:16] on the camera.
[01:19:17] First, thank you for a wonderful talk.
[01:19:19] Thank you.
[01:19:20] Um, one of the uh questions that
[01:19:22] intrigues me is, do you think we'll ever
[01:19:25] be able to write a computer program to
[01:19:28] simulate human consciousness? And if so,
[01:19:32] are is this the path to it?
[01:19:34] Okay, diving right into the
[01:19:35] philosophical questions, huh? Um,
[01:19:37] so I'll repeat it. Al wanted to know if
[01:19:40] we can ever write a program that will
[01:19:41] simulate human consciousness. And the
[01:19:42] answer is
[01:19:45] the answer is I actually don't know what
[01:19:47] consciousness is.
[01:19:48] You don't know what consciousness is?
[01:19:50] No, it's it's not a well- definfined
[01:19:51] concept. So, you know, some people it's
[01:19:55] not entirely clear whether consciousness
[01:19:57] is anything more than kind of a a a
[01:20:01] model of yourself. So you know I was
[01:20:03] talking about predictive models and
[01:20:05] included in the predictive model of the
[01:20:07] world you have to include yourself
[01:20:09] because you have you know you have an
[01:20:11] agency in the world and so if you want
[01:20:13] to predict what's going to happen in the
[01:20:14] world you kind of have to include
[01:20:15] yourself as part of the world and so
[01:20:16] perhaps you need this the the fact that
[01:20:18] you have kind of a part of your brain
[01:20:20] kind of looking at another part of your
[01:20:22] brain acting as if it's you u maybe
[01:20:25] that's what consciousness is but that
[01:20:27] you know you know I'm sure if I say this
[01:20:30] if there were philosophers in the room
[01:20:31] they would kind kind of,
[01:20:35] you know, kind of take their guns. Um
[01:20:39] um there is um you know, there's there's
[01:20:43] other
[01:20:44] But yeah, if it were that yes,
[01:20:46] you would say yes.
[01:20:47] If if it were that I would say yes, but
[01:20:48] I don't know if it's that.
[01:20:50] So it could be also that consciousness
[01:20:52] is just a side effect of being smart.
[01:20:53] you know because you have good models
[01:20:55] you kind of you know include your own
[01:20:57] your own actions as
[01:21:00] I need to follow up on this
[01:21:05] whenever I have an operation that
[01:21:07] requires anesthesia I ask the
[01:21:10] anesthesiologist
[01:21:11] uh how does the anesthetic work and his
[01:21:14] response is I have no idea but I know
[01:21:18] what it's going to do to you when I
[01:21:19] inject you with it. So from a pragmatic
[01:21:22] point of view, uh there's something that
[01:21:24] an anesthetic does to you to eliminate
[01:21:27] what at least part of me thinks of as
[01:21:30] consciousness.
[01:21:30] Yeah. I mean certainly you don't have
[01:21:32] any conscience of time once you are
[01:21:33] under complete anesthesia and
[01:21:37] uh you know it's not just your
[01:21:39] consciousness that shut down. A lot of
[01:21:41] things are shut down. A lot of systems
[01:21:42] are shut down. uh your your your frontal
[01:21:45] cortex you know has a lot of the
[01:21:46] decision- making and uh your prefrontal
[01:21:49] cortex does a lot of this prediction
[01:21:50] world model type type things u all of
[01:21:53] that is turned off um so but you know I
[01:21:57] I don't view this you know I I always
[01:21:59] wonder if this is a real question in the
[01:22:01] sense that uh you know back in the 17th
[01:22:04] century when people discovered how the
[01:22:05] eye was working they they figured that
[01:22:07] you know it's a lens and then the image
[01:22:09] forms in the back of the of the eye on
[01:22:11] the retina and it you know it forms
[01:22:13] upside down and people could not
[01:22:17] fathom how it is that we see right side
[01:22:19] up right because the image is upside
[01:22:22] down and now you know what we know we
[01:22:24] realize that that question doesn't make
[01:22:25] any sense and so it could be that
[01:22:27] consciousness has this kind of flavor
[01:22:29] that the question doesn't make any sense
[01:22:31] but I don't know
[01:22:32] so I I have to ask mine now empathy
[01:22:34] same thing is is empathy a function I
[01:22:37] can transfer because it's actually uh or
[01:22:40] that I can emulate I should say because
[01:22:42] it's something that is actually my model
[01:22:44] of me trying to model to a view of
[01:22:47] that's not me but related to me but
[01:22:49] similarly is sort of a background
[01:22:51] function running
[01:22:52] right so empathy has to be built into
[01:22:54] the this objective function I was I was
[01:22:56] I was talking about right in the
[01:22:58] architecture of the intelligent system
[01:22:59] you have the word model the actor and
[01:23:03] the critic and the critic is a predictor
[01:23:05] for the ultimate objective function and
[01:23:07] to make you uh want to care about other
[01:23:11] people This has to be built into your
[01:23:12] objective function. This is not going to
[01:23:14] come naturally. There's a lot of animals
[01:23:16] who don't have this at all because
[01:23:17] they're not social animals. They don't
[01:23:19] care about empathy. Uh, you know,
[01:23:20] there's a whole bunch of species that,
[01:23:22] you know, basically eat their mate right
[01:23:24] after sex, right? So, um, you know, it's
[01:23:27] for the survival of the species.
[01:23:28] Maybe France,
[01:23:29] huh?
[01:23:32] No, I
[01:23:34] octopus for example, octopus is very
[01:23:36] smart. Uh, but very often one of the
[01:23:39] partners don't survive.
[01:23:41] And then the mother as soon as the
[01:23:43] mother lay their eggs she dies. And so
[01:23:46] uh you know empathy is a is I think is a
[01:23:49] notion that's proper to social animals.
[01:23:51] And I think it's if it's implemented
[01:23:54] somewhere it's in this object hardwired
[01:23:56] objective function we have at the bottom
[01:23:58] of our brain.
[01:23:59] And you said sociopaths clearly just
[01:24:00] miss that function for whatever reason
[01:24:02] whether it's a environmental growing up
[01:24:04] or not. And and and that's that's the
[01:24:05] problem.
[01:24:06] Right. Right. So there is this
[01:24:07] interesting discussion we had yesterday
[01:24:09] at dinner where uh you know those three
[01:24:11] module the world model the actor and the
[01:24:13] the critic and the objective function.
[01:24:15] Uh there's a lot of sort of human um you
[01:24:20] know failings of of human character that
[01:24:23] are due to uh kind of inaccurate
[01:24:26] versions or bad versions of each of
[01:24:28] those three modules. Right? So you can
[01:24:29] have a bad world model makes you kind of
[01:24:31] stupid because you can't really predict
[01:24:32] what's going to happen as a consequence
[01:24:33] of your actions. Um you can have a bad
[01:24:36] objective function which kind of makes
[01:24:38] you evil um possibly or uh and then you
[01:24:42] can have a bad uh uh action generator
[01:24:45] generator which means that even though
[01:24:47] you can predict even though you want to
[01:24:49] do the right thing you can't figure out
[01:24:50] how to get there. Okay. And then there
[01:24:53] are you know some people for which like
[01:24:55] all three of those things are wrong and
[01:24:56] you know sometimes we elect them to
[01:24:58] official
[01:25:00] we'll draw veil we'll draw a veil over
[01:25:02] that one. I think we have one good uh
[01:25:04] example of that. Uh so uh
[01:25:08] off we go.
[01:25:09] Um the question I have is you know
[01:25:11] recently they applied you know game
[01:25:15] learning program to the game of go. Now
[01:25:17] go does not succumb to brute force
[01:25:19] techniques like for chess and I think
[01:25:22] they use some kind of deep learning
[01:25:23] technique and
[01:25:25] and um you know recursively playing
[01:25:27] itself until it got better and better.
[01:25:29] Right. Could you say something about
[01:25:30] those algorithms and how they're related
[01:25:32] to what you covered?
[01:25:33] Yeah, I said just a few words about this
[01:25:34] earlier, but uh so basically there's
[01:25:36] this two or three phases of of training
[01:25:38] of the system. Uh and kind of two
[01:25:41] different neural nets inside. So there
[01:25:42] is one neural net. It's a convolutional
[01:25:43] net very similar to the one we use for
[01:25:44] image recognition that takes the the go
[01:25:47] which is you could think of it as a 19
[01:25:49] by9 image with three possible values for
[01:25:52] each pixel. Okay, so it's a very simple
[01:25:54] image in a way. Um, and then you you
[01:25:56] have this commercial net that's plugged
[01:25:57] on it. And that commercial net is
[01:25:58] trained, supervised on a catalog of
[01:26:02] recorded uh games between uh masters.
[01:26:05] Okay, there's there's thousands and
[01:26:07] thousands of those games around. In
[01:26:08] fact, I think a few million. Um, and so
[01:26:12] you basically you do the same kind of
[01:26:14] training that uh the the Nvidia people
[01:26:16] use for the car. you you uh you show a
[01:26:18] go position and you train the system to
[01:26:21] predict what would be the the move in in
[01:26:24] this recorded game. You know train the
[01:26:26] the system to predict the the next move
[01:26:29] essentially. Uh so that's the first
[01:26:31] phase. If you train a system to do this,
[01:26:33] it plays um there's a number of teams
[01:26:36] that have done this uh at the same time
[01:26:38] more or less as as deep and you get a
[01:26:41] system that performs at a level of about
[01:26:43] two dans or so. Okay, which is actually
[01:26:46] good. you know, it would beat me. Um, I
[01:26:48] mean, I'm terrible, so of course it
[01:26:50] doesn't mean anything. Um, then there is
[01:26:53] a second uh uh kind of a second
[01:26:56] component which is um what's called uh
[01:26:59] what you call a tree search MCTS. So
[01:27:01] this is a classical technique that the
[01:27:03] go playing machine used to use before
[01:27:05] AlphaGo and uh that's basically a sort
[01:27:08] of arborcent search kind of you know
[01:27:10] similar to what's used in chess except
[01:27:12] it's it's kind of multiolor sampling. So
[01:27:14] instead of exploring the entire tree,
[01:27:16] you kind of sample parts of the tree uh
[01:27:19] in in sort of various ways. Um because
[01:27:21] the branching factor is so large, you
[01:27:22] can't possibly do the exhaustive one. Um
[01:27:25] and so you you do that and and what you
[01:27:28] can do with this is that you can
[01:27:29] fine-tune your you can train an
[01:27:31] objective function, another neural net
[01:27:33] to predict whether a particular position
[01:27:36] is going to be a winning position or
[01:27:37] not. Okay? And you don't have to
[01:27:40] actually train this. you can just use
[01:27:42] MCTS with the uh the predictor to uh to
[01:27:46] have a pretty good player. So there's a
[01:27:48] a couple go players that use uh
[01:27:51] supervised pre-training plus MCTS uh and
[01:27:54] that the best ones play at a level of
[01:27:56] about six dans six or seven dance
[01:27:57] amateur which is quite good. It's among
[01:27:59] the best go uh programs in the world
[01:28:03] before AlphaGo. Uh there's a system out
[01:28:06] of Facebook actually that works exactly
[01:28:07] this way. The additional ingredient that
[01:28:09] AlphaGo from deep mind has is the is
[01:28:12] this reinforcement learning procedure.
[01:28:14] So it trains a second neural net to
[01:28:16] evaluate whether a position is a winning
[01:28:18] position or not. And the way it trains
[01:28:20] that is by playing lots and lots and
[01:28:21] lots of games against it itself using
[01:28:23] the combination of commercial net plus
[01:28:25] NCTS and then eventually kind of adding
[01:28:28] the the trained strategy uh with uh with
[01:28:31] reinforcement running. And the more this
[01:28:33] thing trains the better the better it
[01:28:34] is. So now it's uh you know several Dan
[01:28:37] clicks above the best human players.
[01:28:41] So next next question.
[01:28:47] One of the things that baby has is arms
[01:28:50] and legs and feels the real world. Do we
[01:28:53] need to include those kinds of inputs as
[01:28:56] we go forward with artificial
[01:28:59] intelligence?
[01:28:59] Yeah, that's a good question that I
[01:29:01] don't think has a clear answer yet. Uh
[01:29:03] so there are experiments that seem to
[01:29:04] show that certain animals need to act in
[01:29:06] the world to be able to learn. There's
[01:29:08] an experiment that was done a long time
[01:29:09] ago where you have you put a baby cat on
[01:29:12] a kind of a carousel and and another
[01:29:16] baby cat on the other side of the
[01:29:17] carousel and the first cat can can kind
[01:29:19] of walk around and move the carousel and
[01:29:21] the the second one can just watch and
[01:29:23] the second one doesn't develop normally.
[01:29:26] So this seems to suggest that for cats
[01:29:28] to develop normally they have to be able
[01:29:30] to act in the world. But you know there
[01:29:32] could be all kinds of other artifacts of
[01:29:34] the experiment. Um it's not entirely
[01:29:36] clear for for machines whether there
[01:29:39] there is a a need for action. Certainly
[01:29:42] action allows us to uh uh kind of ask
[01:29:46] questions to the world. Right? If you
[01:29:49] are just observing the world then the
[01:29:50] world has to be curated to some extent
[01:29:52] so that you see the things that are
[01:29:53] important because if you don't do
[01:29:55] anything most of the things you observe
[01:29:56] are very boring right? Um, so if you are
[01:29:59] kind of just sitting uh in a in a room
[01:30:01] and not doing anything, I don't think
[01:30:03] you're going to learn very, you know,
[01:30:04] very much. But if you watch uh, you
[01:30:06] know, YouTube video all days, maybe
[01:30:07] you'll learn something about the world.
[01:30:08] I don't know. It's possible.
[01:30:11] That's interesting because I I tend to
[01:30:13] think you do need that sensory input,
[01:30:14] but you you would say it's possible that
[01:30:16] you could watch the act of someone
[01:30:18] touching and not have to touch.
[01:30:20] Possibly.
[01:30:21] Yeah, possibly.
[01:30:22] Uh, okay. Other other questions.
[01:30:26] So this is obviously a dual use.
[01:30:28] You need to wait for the mic. John,
[01:30:32] obviously like many things of physics
[01:30:34] and else there's dual uses to this. Can
[01:30:37] you just comment? I mean obviously uh
[01:30:39] you know we're all really excited by
[01:30:40] this but we all in the back of our minds
[01:30:42] think about the military consequences of
[01:30:44] this.
[01:30:45] So how are we going to handle that? I
[01:30:47] mean just asking naively.
[01:30:49] Well minority report future crime right?
[01:30:52] uh that that was that that is premised
[01:30:54] on on similar idea.
[01:30:55] Yeah, there are you know a few startup
[01:30:58] companies in various countries that uh
[01:31:01] thankfully not so much in the US
[01:31:02] although there are a few of those that
[01:31:03] try to do things like predict recidivism
[01:31:06] or uh horrible things like you know tell
[01:31:09] if a person is likely to be a terrorist
[01:31:10] just by their face.
[01:31:12] I mean this is basically automated
[01:31:14] racial profiling. Um and so a lot of us
[01:31:18] in the community became kind of very
[01:31:20] annoyed by things like this and um not
[01:31:22] just because it it gives a bad name to
[01:31:24] the technology but because it's
[01:31:25] ethically wrong and someone has to say
[01:31:28] that and uh at this time the people who
[01:31:31] are informed about what the technology
[01:31:32] can do are us and so um I was uh
[01:31:36] instrumental in in forming something
[01:31:38] called a partnership for AI uh which is
[01:31:40] a a sort of industry group. It's not
[01:31:42] just industry but it's you know funded
[01:31:44] by by industry. uh so the the funding
[01:31:48] companies are uh Facebook, Google,
[01:31:50] Amazon, IBM and Microsoft and then Apple
[01:31:53] also joined as as a founding member and
[01:31:56] there's a board formed by
[01:31:58] representatives from those companies as
[01:31:59] well as people from the CLU the I
[01:32:02] believe a lot of non- NOS's essentially
[01:32:05] that that worry about ethics um
[01:32:08] economical impact economic impact and
[01:32:11] and things like that. So the economist
[01:32:13] on the on the board is GO Chis Furman
[01:32:15] who was the director of the council of
[01:32:18] economic adviser for the Obama
[01:32:19] administration. So this a very sort of
[01:32:22] deep reflection among some governments
[01:32:25] uh certainly the Obama administration
[01:32:27] while it was still there that produced a
[01:32:29] report late last year about the the
[01:32:31] potential impact of AI and how the our
[01:32:34] governments would uh you know would need
[01:32:35] to kind of uh deal with this problem and
[01:32:38] and perhaps encourage it. uh and um it's
[01:32:42] probably being ignored by the current
[01:32:43] one um is being very widely read outside
[01:32:47] of the US. There's a lot of governments
[01:32:48] who are thinking about this as well. Um
[01:32:50] but I think we as technologists need to
[01:32:53] kind of come up with guidelines for
[01:32:56] proper use of this kind of technology.
[01:32:58] We're not going to be able to stop the
[01:32:59] military from using it, but there are,
[01:33:02] you know, perhaps safety guidelines that
[01:33:04] we should tell them. So none of us is
[01:33:06] really, at least I'm not worried about
[01:33:08] the terminator scenario. It's more it's
[01:33:11] more like misuse and and sort of you
[01:33:13] know short-term eth ethical problems.
[01:33:16] Couple more questions.
[01:33:18] Mark. Yeah.
[01:33:19] Yan. I have another applied question. Um
[01:33:22] today especially in uh social networking
[01:33:25] and media. There's a lot of uh talk
[01:33:28] about and discussion of alternative
[01:33:30] facts almost alternative reality,
[01:33:32] right?
[01:33:33] How can these techniques be applied to
[01:33:35] that or is work already underway? uh
[01:33:38] yeah there is work underway to apply
[01:33:40] machine learning and today machine
[01:33:42] learning to a large extent means deep
[01:33:44] learning neural nets etc. So there's
[01:33:46] quite a lot of work uh you know at
[01:33:48] Facebook, at Google, various other
[01:33:49] companies on sort of identifying the you
[01:33:52] know potential reliability or
[01:33:54] unreliability of of a piece of news. Uh
[01:33:57] and it's not just you know you can't do
[01:33:59] this just based on content. You have to
[01:34:00] kind of correlate that content with
[01:34:03] other stories on the same topic from
[01:34:05] sources that you might trust. And then
[01:34:07] there is an issue of how you design uh
[01:34:10] the product so that people will believe
[01:34:12] in the predictions that are done by the
[01:34:14] system and trust them because maybe half
[01:34:17] the population believes the New York
[01:34:18] Times is a reliable source of
[01:34:20] information but there's a half of the
[01:34:21] population in the US that believe it's
[01:34:23] fake news. So how you know how do you
[01:34:25] kind of design a system so that uh the
[01:34:29] the indication of reliability are are
[01:34:31] done properly? So, Facebook is actually
[01:34:33] rolling out uh as we speak in uh in
[01:34:37] France and Germany um two systems to
[01:34:40] kind of identify fake news. There's a
[01:34:42] little bit of automation in it, but it's
[01:34:43] mostly rely it mostly relies on sort of
[01:34:46] traditional media to kind of help assess
[01:34:48] the reliability of of news. uh and the
[01:34:51] reason why it's uh deployed in France
[01:34:54] and Germany is because they have
[01:34:55] upcoming elections
[01:34:57] um that they really would like external
[01:35:01] uh countries not to interfere with and
[01:35:06] uh and uh and and they they sort of come
[01:35:09] to the realization it could be a big
[01:35:11] problem for them because you know of the
[01:35:12] same issues there is in the US. So
[01:35:14] related to that one though uh I think
[01:35:16] one of the problems in that is you there
[01:35:18] will be another uh uh deep learning
[01:35:21] network that proves that is wrong for
[01:35:24] those who want to believe that. So what
[01:35:27] we have to then have is uh that I think
[01:35:30] it gets back to the empathy function
[01:35:32] where we have to actually somehow find a
[01:35:34] way of saying regardless of what you
[01:35:35] believe you should have a world model
[01:35:37] that incorporates that other view and
[01:35:38] then then you can behave better right
[01:35:40] because I think the newsy part is a
[01:35:43] symptom but not the cause then we need
[01:35:45] to go after the cause part would you
[01:35:47] agree or not? Yeah, I it's you know it's
[01:35:49] a very difficult issue that has more to
[01:35:51] do today with uh product design I would
[01:35:55] say or user interface than it has with
[01:35:57] technology really. I mean certainly
[01:35:59] technology is going to help more and
[01:36:00] more with this these questions but I
[01:36:02] think it's more how you get this I mean
[01:36:04] this is really not my specialty I have
[01:36:06] to admit you know I'm a research
[01:36:07] scientist most of the research we do is
[01:36:09] you know open research and we work with
[01:36:11] public data we don't actually work that
[01:36:13] much with Facebook data um so this is
[01:36:16] actually taken care of by other people
[01:36:17] within the company
[01:36:20] two more these will be the last two I
[01:36:22] think and then we'll have to wrap up
[01:36:23] otherwise
[01:36:25] we're favoring people at the back it's
[01:36:26] Eve back there isn't Yeah,
[01:36:29] they've been patient. So, Eve, off you
[01:36:31] go.
[01:36:31] Yeah. Uh, just a curiosity. Um, you
[01:36:34] mentioned that we have 10 to the 14
[01:36:36] synapses in our brain. Now, our brain
[01:36:40] only consumes couple watt, I would
[01:36:42] assume. So, how power efficient are your
[01:36:46] current systems compared to the human
[01:36:48] brain? Because if you want to have these
[01:36:49] systems everywhere, obviously they need
[01:36:51] to be at least within a couple orders of
[01:36:54] magnitude. So how how are they how
[01:36:56] efficient are they and what are people
[01:36:58] doing to make them more efficient?
[01:37:00] It's terrible. It's it's horrible. It
[01:37:03] it's terrible for various reasons. It's
[01:37:04] terrible. Uh so to give you an idea, a
[01:37:07] typical GPU card which is kind of you
[01:37:11] know in terms of numerical computation
[01:37:14] maybe as efficient as it as it gets is
[01:37:16] about 10 teraflops and it's about 200
[01:37:18] watts. So you know um the brain is
[01:37:25] roughly if you really want to make a
[01:37:27] kind of global estimate of how many
[01:37:29] operations you need in the brain to kind
[01:37:31] of get a functioning brain that's about
[01:37:32] 10 to the 10 to the 17 operations per
[01:37:35] second.
[01:37:37] U it's a lot of teraflops.
[01:37:40] Uh and um you know it's 100,000
[01:37:44] teraflops and that's 25 watts in the
[01:37:46] brain. So there is you know at least six
[01:37:49] orders of magnitude difference between
[01:37:52] uh you know white sauce and uh GPUs.
[01:37:58] Now a lot of that can be bridged with uh
[01:38:02] you know just the progress of technology
[01:38:05] in the sense that GPUs are very very far
[01:38:07] from being the kind of uh you know
[01:38:09] optimal things to do to to run neural
[01:38:11] nets. So if you want to run a neural net
[01:38:13] without training it uh just you know in
[01:38:16] operation you don't actually need that
[01:38:18] much accuracy in the computation you
[01:38:19] don't need 32-bit floating point you can
[01:38:21] get away with just a few bits on the on
[01:38:23] the weights and and the and the states
[01:38:25] in fact there were chips of this type
[01:38:26] that were built in the department I was
[01:38:28] in at at Homeell in the early 90s
[01:38:30] there's a chip called ANA which means
[01:38:32] analog neural network accelerator and it
[01:38:36] had it was it was capable of four
[01:38:38] billion uh operations per second where
[01:38:40] an operation was a multip apply ad
[01:38:42] essentially and the states in the neural
[01:38:44] net. So it was a conventional net
[01:38:45] accelerator basically and it it used
[01:38:48] four bits for the the states of the
[01:38:49] units and six bits for the weights and
[01:38:51] it was good enough to do character
[01:38:53] recognition probably not good enough for
[01:38:55] you know full-fledged image recognition
[01:38:57] but you don't need much more than that.
[01:38:59] So reducing the precision gives you a
[01:39:01] huge win. uh then kind of tailoring the
[01:39:03] architecture to run commercial nets as
[01:39:05] opposed to run kind of general you know
[01:39:07] video rendering or whatever will give
[01:39:09] you another win because what costs
[01:39:11] energy is not so much the competition
[01:39:13] itself but it's moving data around so if
[01:39:15] you can have data locally stored where
[01:39:18] the competition takes place then you
[01:39:19] save a huge amount of energy uh of power
[01:39:23] uh so there's going to be a lot of
[01:39:24] progress I think over the next few years
[01:39:25] on this there's quite a few startup
[01:39:26] companies and larger companies that are
[01:39:28] that are building uh you know low low
[01:39:31] Our u uh commercial net accelerator is
[01:39:36] essentially chips for uh embedded
[01:39:39] applications, you know, for mobile
[01:39:41] phones, for uh cars, for toys, for
[01:39:45] vacuum cleaners, lawnmowers, you know,
[01:39:48] whatever maintenance robots. You're
[01:39:50] going to have those vision chips
[01:39:51] everywhere within five years. That's my
[01:39:53] guess. Do you think the
[01:39:55] as the world model gets better the agent
[01:39:59] can get smaller or the objective
[01:40:00] function can be well objective function
[01:40:02] is probably is not the largest part
[01:40:04] right but is if if the world model gets
[01:40:06] better the agent can be simpler and that
[01:40:07] then saves some computational power I
[01:40:10] would imagine
[01:40:10] I'm not sure that would be a good way of
[01:40:12] saving saving computation but but I
[01:40:15] think the now that people have a model
[01:40:17] for how to do perception there's a lot
[01:40:20] of u you know people interested in
[01:40:22] hardware who are kind focusing a lot of
[01:40:23] energy on trying to make this efficient
[01:40:25] and cheap. And uh I have actually a bet
[01:40:29] that I I another bet of this type.
[01:40:31] It's going to be a fancy dinner.
[01:40:32] It's a fancy dinner
[01:40:35] uh with Larry Jackal. Uh the bet was uh
[01:40:38] was was signed in in 2013. And uh what I
[01:40:45] what I said was that by 2023 which is
[01:40:48] not that far in the future
[01:40:50] your your smartphone will have enough
[01:40:52] power to uh drive your car.
[01:40:56] So basically you you know the hardware
[01:40:59] may not be there but the uh I mean the
[01:41:00] the connection between the phone and the
[01:41:02] car may not be there but in principle
[01:41:04] you you should be able to just you know
[01:41:06] hold your phone uh in front of you and
[01:41:09] have it drive your car. Now, of course,
[01:41:12] real self-driving cars will not use your
[01:41:13] cell phone, but u but it's kind of a
[01:41:16] statement of of how technology will
[01:41:17] evolve.
[01:41:19] Last one and then I think we'll have to
[01:41:20] wrap up. Okay, we'll go back.
[01:41:23] So, this is maybe a little bit of the uh
[01:41:25] Terminator type thought, but um when and
[01:41:29] what are your thoughts on how will AI
[01:41:32] reach a point where it begins to
[01:41:33] replicate itself and will we be able to
[01:41:35] understand it or how will we be able to
[01:41:38] control it?
[01:41:40] Yeah, this is a a question that some
[01:41:42] some people in the in in in the business
[01:41:45] are kind of interested in. Uh to me it's
[01:41:48] a little abstract because we don't have
[01:41:51] we're not you know close
[01:41:55] you know we're very very far from having
[01:41:56] a technology to have intelligent
[01:41:58] systems. Uh self-replication requires
[01:42:00] something else which is you know
[01:42:02] physical interaction with the world and
[01:42:04] kind of fabrication all that stuff. uh
[01:42:07] so what you know why would we give this
[01:42:09] kind of ability to uh to robots I mean I
[01:42:13] think most of AI of the future will be
[01:42:16] virtual AI it won't be robots it'll be
[01:42:18] kind of intelligent virtual assistants
[01:42:19] you can talk to things that kind of you
[01:42:22] know run the world basically but not um
[01:42:25] but don't have kind of much physical
[01:42:26] interaction with it. So um so that's
[01:42:30] that's point number one. uh there's
[01:42:32] there's quite a lot of people who are
[01:42:33] worried about kind of the the
[01:42:35] theoretical aspects of controllability.
[01:42:37] So for example, is it enough to
[01:42:39] construct a robot or an AI system with
[01:42:42] an objective function that is hardwired
[01:42:44] and sort of cryptographically protected
[01:42:47] for example so that the robot or the AI
[01:42:49] system cannot modify it and so if it
[01:42:52] cannot modify it objective function that
[01:42:53] means it has to abide by it. it can you
[01:42:56] know it can't you can't you know if you
[01:42:58] can you can self modify it and so in
[01:43:00] those objective functions how do you
[01:43:01] design them so that there are kind of uh
[01:43:04] u you know fences that prevent the
[01:43:07] system from doing bad things so there's
[01:43:10] a book by a guy called Nick Bstrom he's
[01:43:11] a philosopher at Oxford and he wrote a
[01:43:13] book called super intelligence and this
[01:43:15] by reading this book that people like
[01:43:16] Elon Musk and Stephen Hawking and Bill
[01:43:19] Gates uh you know made those declaration
[01:43:21] that you know maybe AI will kill us and
[01:43:23] we have to be careful
[01:43:25] Um, and frankly the scenarios that I
[01:43:28] described in this book to me are
[01:43:29] completely unrealistic. So there's a
[01:43:31] scenario, this is the so-called
[01:43:32] paperclip scenario where you know you
[01:43:35] build a machine to build paperclip and
[01:43:36] all it wants to do is optimize the
[01:43:38] maximize number of paper clips it
[01:43:39] produces and it's super intelligent. So
[01:43:41] it kind of convince everybody to not
[01:43:43] turn it off and ends up turning the
[01:43:45] entire galaxy into paper clips um or the
[01:43:48] solar system or just the planet earth.
[01:43:50] Okay, that's enough. But um I you know I
[01:43:54] think I think we would have to be uh
[01:43:58] extremely stupid first and extremely
[01:44:00] unlucky for this to happen. It's hard
[01:44:02] enough to get a machine to work at all.
[01:44:04] So
[01:44:07] after this you're not so sure about
[01:44:09] Yeah. Right. No. I mean do you do you
[01:44:11] give you know uh you know do do you put
[01:44:15] a a child in front of a like a nuclear
[01:44:18] uh button? No. um you don't give
[01:44:21] infinite power to things for which you
[01:44:22] know you don't have uh complete trust
[01:44:25] you know except presidents maybe
[01:44:30] okay I think uh anyone else anyone else
[01:44:32] at last bid for a question okay yes
[01:44:34] there last hand
[01:44:36] just wait for the microphone and then
[01:44:41] thank you for your lecture my question
[01:44:43] was um a lot of your examples were
[01:44:46] visually related do you see
[01:44:49] um uh research for for example
[01:44:54] um
[01:44:55] speech um
[01:44:58] stuff like that um translation from one
[01:45:01] language to another.
[01:45:02] Uhhuh. Yeah. So there's a lot of work on
[01:45:03] translation. There's a lot of work on
[01:45:05] natural language understanding uh a lot
[01:45:07] of work on uh dialogue systems for
[01:45:11] virtual assistants. So that's kind of a
[01:45:13] big prize for a lot of companies that
[01:45:14] are involved in AI which is how to build
[01:45:16] the underlying technology for useful
[01:45:18] virtual assistants. We're not talking
[01:45:20] about the the current version of you
[01:45:22] know you know Alexa, Google Home or Siri
[01:45:26] um which are very scripted. You know
[01:45:28] there is only a certain number of
[01:45:29] questions they can answer and if you go
[01:45:30] outside of that they you know they
[01:45:32] answer with a joke. Um and and all of
[01:45:34] those are all of those kind of u
[01:45:37] scenarios are are scripted by humans.
[01:45:39] the you know there's databases that can
[01:45:41] be accessed for the answers. It's it's
[01:45:42] it's not there's not a huge amount of AI
[01:45:45] behind this I have to admit. So the
[01:45:48] question is you know when will we have
[01:45:50] machines that have enough background
[01:45:52] knowledge and common sense so that we
[01:45:54] will be able to talk to them and not be
[01:45:56] incredibly frustrated when we talk to
[01:45:58] them because you know they'll be
[01:46:00] sufficiently intelligent to uh
[01:46:02] understand what what we mean. So,
[01:46:04] Facebook has um has been running an
[01:46:05] experiment uh which is sort of a a bit
[01:46:08] of a um wizard of Os type experiment.
[01:46:11] It's a project called M and it's a
[01:46:15] intelligent virtual assistant. Uh so you
[01:46:17] have you have your phone you communicate
[01:46:19] with it through Facebook Messenger and
[01:46:21] you can ask it anything even to kind of
[01:46:24] renegotiate your cable bill or
[01:46:25] something. Uh and it's you know it's
[01:46:28] humans doing the job which is why it's
[01:46:29] only available to about 10,000 people.
[01:46:33] uh but part of it is automated by um
[01:46:36] kind of AI system that kind of figure
[01:46:38] out what kind of question it is and sort
[01:46:39] of produce an answer and then it's kind
[01:46:41] of you know u more or less automated. So
[01:46:44] there's a certain percentage of those
[01:46:46] questions that can be automated. But the
[01:46:48] lesson from this project is that there
[01:46:49] is a very very very long tale of very
[01:46:51] complicated things that people want out
[01:46:53] of a virtual assistant for which the
[01:46:54] technology just doesn't exist yet. Uh,
[01:46:57] and it's going to take, you know, uh,
[01:47:00] decades. I'd say at least one decade.
[01:47:04] We should have a, uh, fancy dinner bet
[01:47:06] on that.
[01:47:08] With that, we will wrap up and thank Yan
[01:47:11] once again. Thank you very much.
[01:47:19] So, I I have to give Yan something. So,
[01:47:21] before you leave, I have to give him
[01:47:22] what he came here for, which isn't you.
[01:47:25] No, it of course it is in part. This is
[01:47:27] the Shannon Luminary Award uh that you
[01:47:29] are the second recipient of the year and
[01:47:31] it's a trophy we've had specially uh
[01:47:33] created for this series. So well done
[01:47:36] and uh it was a fabulous fabulous. It's
[01:47:38] been lovely having you here.
[01:47:38] Thank you very much.
[01:47:40] [Applause]
[01:47:42] [Music]
[01:47:45] [Applause]
[01:47:47] Heat.
[01:47:49] [Applause]
[01:47:57] [Music]
[01:47:59] Heat.
[01:48:01] [Music]
