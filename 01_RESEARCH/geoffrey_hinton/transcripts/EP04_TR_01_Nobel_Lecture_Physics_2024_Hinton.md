# Nobel Prize Lecture: Geoffrey Hinton (Physics 2024 — Boltzmann Machines)

- **URL:** https://www.youtube.com/watch?v=XDE9DjpcSdI
- **Source VTT:** `EP04_TR_01_Nobel_Lecture_Physics_2024_Hinton.en-orig.vtt`

---

`[00:00:00]` it is now my pleasure and great honor to
`[00:00:03]` introduce our second speaker Jeffrey
`[00:00:06]` introduce our second speaker Jeffrey
`[00:00:07]` Hinton Jeffrey Hinton was born in London
`[00:00:10]` Hinton Jeffrey Hinton was born in London
`[00:00:10]` UK in
`[00:00:11]` UK in
`[00:00:11]` 1947 he received a bachelor degree in
`[00:00:14]` 1947 he received a bachelor degree in
`[00:00:14]` experimental Psychology from Cambridge
`[00:00:17]` experimental Psychology from Cambridge
`[00:00:17]` University in
`[00:00:19]` University in
`[00:00:19]` 1970 1978 he he was awarded a PhD in
`[00:00:23]` 1970 1978 he he was awarded a PhD in
`[00:00:23]` artificial intelligence from the
`[00:00:26]` artificial intelligence from the
`[00:00:26]` University of
`[00:00:27]` University of
`[00:00:27]` Edinburgh after post-doctoral research
`[00:00:31]` Edinburgh after post-doctoral research
`[00:00:31]` he worked for 5 years as a faculty
`[00:00:34]` he worked for 5 years as a faculty
`[00:00:34]` member in computer science at
`[00:00:37]` member in computer science at
`[00:00:37]` Carnegie melon University in Pittsburgh
`[00:00:41]` Carnegie melon University in Pittsburgh
`[00:00:41]` in
`[00:00:42]` in
`[00:00:42]` 1987 he was appointed professor of
`[00:00:45]` 1987 he was appointed professor of
`[00:00:45]` computer science at the University of
`[00:00:48]` computer science at the University of
`[00:00:48]` Toronto Canada where he presently is a
`[00:00:52]` Toronto Canada where he presently is a
`[00:00:52]` Meritus
`[00:00:54]` Meritus
`[00:00:54]` Professor between
`[00:00:56]` Professor between
`[00:00:56]` 2013 and
`[00:00:58]` 2013 and
`[00:00:58]` 2023 he shared his time between academic
`[00:01:02]` 2023 he shared his time between academic
`[00:01:02]` research and Google
`[00:01:04]` research and Google
`[00:01:05]` brain please join me in welcoming
`[00:01:08]` brain please join me in welcoming
`[00:01:08]` Jeffrey Hinton to the stage to tell us
`[00:01:11]` Jeffrey Hinton to the stage to tell us
`[00:01:11]` about the developments that led to this
`[00:01:14]` about the developments that led to this
`[00:01:14]` year's Nobel Prize in physics
`[00:01:34]` so today I'm going to do something very
`[00:01:35]` foolish I'm going to try and describe a
`[00:01:38]` foolish I'm going to try and describe a
`[00:01:38]` complicated technical idea for a general
`[00:01:40]` complicated technical idea for a general
`[00:01:40]` audience without using any
`[00:01:43]` audience without using any
`[00:01:43]` equations so first I have to explain
`[00:01:46]` equations so first I have to explain
`[00:01:46]` hopfield Nets and I'm going to explain
`[00:01:48]` hopfield Nets and I'm going to explain
`[00:01:48]` the version with binary neurons that
`[00:01:49]` the version with binary neurons that
`[00:01:49]` have states of one or zero so on the
`[00:01:52]` have states of one or zero so on the
`[00:01:52]` right there you'll see a little hopfield
`[00:01:53]` right there you'll see a little hopfield
`[00:01:53]` net and the most important thing is the
`[00:01:56]` net and the most important thing is the
`[00:01:56]` neurons have symmetrically weighted
`[00:01:58]` neurons have symmetrically weighted
`[00:01:58]` connections between them
`[00:02:02]` the global state of a whole network is
`[00:02:04]` called a configuration just so we seem a
`[00:02:06]` called a configuration just so we seem a
`[00:02:06]` bit like physics um and each
`[00:02:11]` bit like physics um and each
`[00:02:11]` configuration has a goodness and the
`[00:02:13]` configuration has a goodness and the
`[00:02:13]` goodness of configuration is simply the
`[00:02:15]` goodness of configuration is simply the
`[00:02:15]` sum of all pairs of units that of
`[00:02:18]` sum of all pairs of units that of
`[00:02:18]` neurons that are both on of the weights
`[00:02:20]` neurons that are both on of the weights
`[00:02:20]` between them so those weights in red
`[00:02:22]` between them so those weights in red
`[00:02:22]` boxes you add those up and you get um
`[00:02:25]` boxes you add those up and you get um
`[00:02:25]` four hopefully that's the goodness of
`[00:02:28]` four hopefully that's the goodness of
`[00:02:28]` that configuration of the network
`[00:02:30]` that configuration of the network
`[00:02:30]` and the energy is just minus the
`[00:02:35]` goodness so these networks will settle
`[00:02:37]` to energy Minima the whole point of a
`[00:02:39]` to energy Minima the whole point of a
`[00:02:39]` hop Field net is that each neuron can
`[00:02:42]` hop Field net is that each neuron can
`[00:02:42]` locally compute what it needs to do in
`[00:02:45]` locally compute what it needs to do in
`[00:02:45]` order to reduce the
`[00:02:46]` order to reduce the
`[00:02:46]` energy um where energy is
`[00:02:49]` energy um where energy is
`[00:02:49]` Badness so um if the total weighted
`[00:02:53]` Badness so um if the total weighted
`[00:02:53]` input coming from other active neurons
`[00:02:56]` input coming from other active neurons
`[00:02:56]` is positive the neuron should turn on if
`[00:02:59]` is positive the neuron should turn on if
`[00:02:59]` the total weighted input coming from
`[00:03:00]` the total weighted input coming from
`[00:03:00]` other active neurons is negative it
`[00:03:02]` other active neurons is negative it
`[00:03:02]` should turn
`[00:03:04]` should turn
`[00:03:04]` off and if each neuron just keeps using
`[00:03:07]` off and if each neuron just keeps using
`[00:03:07]` that rule and we pick them at random and
`[00:03:09]` that rule and we pick them at random and
`[00:03:09]` keep applying that rule we will
`[00:03:10]` keep applying that rule we will
`[00:03:10]` eventually settle to an energy minimum
`[00:03:12]` eventually settle to an energy minimum
`[00:03:12]` so the configuration on the right there
`[00:03:14]` so the configuration on the right there
`[00:03:14]` is actually an energy minimum it has an
`[00:03:17]` is actually an energy minimum it has an
`[00:03:17]` energy of minus 4 and if you take any
`[00:03:20]` energy of minus 4 and if you take any
`[00:03:20]` neuron there the ones that are on want
`[00:03:22]` neuron there the ones that are on want
`[00:03:22]` to stay on they get total positive input
`[00:03:24]` to stay on they get total positive input
`[00:03:24]` the ones that are off want to stay off
`[00:03:25]` the ones that are off want to stay off
`[00:03:25]` they get total negative input but it's
`[00:03:27]` they get total negative input but it's
`[00:03:27]` not the only energy minimum um a hot
`[00:03:31]` not the only energy minimum um a hot
`[00:03:31]` Field net can have many energy Minima
`[00:03:33]` Field net can have many energy Minima
`[00:03:33]` and where it ends up depends on um where
`[00:03:35]` and where it ends up depends on um where
`[00:03:35]` you start it and also on the sequence of
`[00:03:37]` you start it and also on the sequence of
`[00:03:37]` random decisions you make um if sorry
`[00:03:41]` random decisions you make um if sorry
`[00:03:41]` the sequence of random decisions about
`[00:03:43]` the sequence of random decisions about
`[00:03:43]` which neuron to
`[00:03:45]` which neuron to
`[00:03:45]` update so that's a better energy minimum
`[00:03:48]` update so that's a better energy minimum
`[00:03:48]` now we've turned on the triangle of
`[00:03:49]` now we've turned on the triangle of
`[00:03:49]` units on the right and that's got a
`[00:03:52]` units on the right and that's got a
`[00:03:52]` goodness of 3 + 3 - 1 is five and so an
`[00:03:57]` goodness of 3 + 3 - 1 is five and so an
`[00:03:57]` energy minus 5 that's a better minimum
`[00:04:00]` energy minus 5 that's a better minimum
`[00:04:00]` now hopfield proposed that a good way to
`[00:04:03]` now hopfield proposed that a good way to
`[00:04:03]` use such networks is to make the energy
`[00:04:05]` use such networks is to make the energy
`[00:04:05]` Minima correspond to memories and then
`[00:04:08]` Minima correspond to memories and then
`[00:04:08]` using that binary decision rule about
`[00:04:10]` using that binary decision rule about
`[00:04:10]` whether you should turn a urine on or
`[00:04:11]` whether you should turn a urine on or
`[00:04:11]` off that can clean up incomplete
`[00:04:13]` off that can clean up incomplete
`[00:04:13]` memories so you start with a partial
`[00:04:16]` memories so you start with a partial
`[00:04:16]` memory and then you just keep applying
`[00:04:18]` memory and then you just keep applying
`[00:04:18]` this decision Rule and it will clean it
`[00:04:20]` this decision Rule and it will clean it
`[00:04:20]` up so settling to energy Minima when
`[00:04:23]` up so settling to energy Minima when
`[00:04:23]` they represent memories is a way of
`[00:04:25]` they represent memories is a way of
`[00:04:25]` having a Content addressable memory you
`[00:04:28]` having a Content addressable memory you
`[00:04:28]` can access an item in the memory by just
`[00:04:30]` can access an item in the memory by just
`[00:04:30]` turning on some of the item and then
`[00:04:32]` turning on some of the item and then
`[00:04:32]` using this Rule and it'll fill it
`[00:04:35]` using this Rule and it'll fill it
`[00:04:35]` out Terry soski and I Terry was a
`[00:04:38]` out Terry soski and I Terry was a
`[00:04:38]` student of hopfields um proposed a
`[00:04:41]` student of hopfields um proposed a
`[00:04:41]` different use for these kinds of Nets
`[00:04:44]` different use for these kinds of Nets
`[00:04:44]` instead of using them to storm memories
`[00:04:46]` instead of using them to storm memories
`[00:04:46]` we could use them to construct
`[00:04:48]` we could use them to construct
`[00:04:48]` interpretations of sensory
`[00:04:50]` interpretations of sensory
`[00:04:50]` input so the idea is you have a net it
`[00:04:53]` input so the idea is you have a net it
`[00:04:53]` has both visible neurons and hidden
`[00:04:54]` has both visible neurons and hidden
`[00:04:54]` neurons the visible neurons are where
`[00:04:56]` neurons the visible neurons are where
`[00:04:56]` you show it a sensory input maybe a
`[00:04:59]` you show it a sensory input maybe a
`[00:04:59]` binary image the hidden neurons are
`[00:05:01]` binary image the hidden neurons are
`[00:05:02]` where it constructs the interpretation
`[00:05:03]` where it constructs the interpretation
`[00:05:03]` of that sensory
`[00:05:06]` of that sensory
`[00:05:06]` input and the energy of a configuration
`[00:05:09]` input and the energy of a configuration
`[00:05:09]` of the network represents the Badness of
`[00:05:11]` of the network represents the Badness of
`[00:05:11]` the interpretation so we want low energy
`[00:05:14]` the interpretation so we want low energy
`[00:05:14]` interpretations so I'm going to give you
`[00:05:16]` interpretations so I'm going to give you
`[00:05:16]` a con concrete example consider that
`[00:05:18]` a con concrete example consider that
`[00:05:18]` ambiguous line drawing at the top people
`[00:05:21]` ambiguous line drawing at the top people
`[00:05:21]` have two ways of seeing that um there's
`[00:05:23]` have two ways of seeing that um there's
`[00:05:24]` interpretation one which is normally
`[00:05:26]` interpretation one which is normally
`[00:05:26]` what you see first there's another
`[00:05:27]` what you see first there's another
`[00:05:27]` interpretation and when you see it as
`[00:05:29]` interpretation and when you see it as
`[00:05:29]` convex object that's clearly a different
`[00:05:31]` convex object that's clearly a different
`[00:05:31]` 3D interpretation of the same 2D line
`[00:05:34]` 3D interpretation of the same 2D line
`[00:05:34]` drawing so could we make one of these
`[00:05:36]` drawing so could we make one of these
`[00:05:36]` networks come up with two different
`[00:05:38]` networks come up with two different
`[00:05:38]` interpretations of the same line
`[00:05:40]` interpretations of the same line
`[00:05:40]` drawing well we need to start by
`[00:05:42]` drawing well we need to start by
`[00:05:42]` thinking what a line in an image tells
`[00:05:44]` thinking what a line in an image tells
`[00:05:44]` you about 3D
`[00:05:46]` you about 3D
`[00:05:46]` edges so that green line is the image
`[00:05:49]` edges so that green line is the image
`[00:05:49]` plane imagine you're looking through a
`[00:05:50]` plane imagine you're looking through a
`[00:05:50]` window and you're drawing the edges in
`[00:05:52]` window and you're drawing the edges in
`[00:05:52]` the scene out there in the world on the
`[00:05:54]` the scene out there in the world on the
`[00:05:54]` window so that little black line is a
`[00:05:57]` window so that little black line is a
`[00:05:57]` line in the image
`[00:06:00]` line in the image
`[00:06:00]` and the two red lines are the lines of
`[00:06:01]` and the two red lines are the lines of
`[00:06:01]` sight that come from your eye through
`[00:06:03]` sight that come from your eye through
`[00:06:03]` the ends of that line and if you ask
`[00:06:06]` the ends of that line and if you ask
`[00:06:06]` well what Edge in the world could have
`[00:06:07]` well what Edge in the world could have
`[00:06:07]` caused that well there's many edges that
`[00:06:10]` caused that well there's many edges that
`[00:06:10]` could have caused it there's one Edge
`[00:06:12]` could have caused it there's one Edge
`[00:06:12]` that could have caused that 2D line but
`[00:06:14]` that could have caused that 2D line but
`[00:06:14]` there's another one and there's another
`[00:06:16]` there's another one and there's another
`[00:06:16]` one and there's another one all of these
`[00:06:18]` one and there's another one all of these
`[00:06:18]` edges will cause the same line in the
`[00:06:20]` edges will cause the same line in the
`[00:06:20]` image so the problem of vision is to go
`[00:06:22]` image so the problem of vision is to go
`[00:06:22]` backwards from the single line in the
`[00:06:23]` backwards from the single line in the
`[00:06:23]` image to figure out which of these edges
`[00:06:25]` image to figure out which of these edges
`[00:06:25]` is really out
`[00:06:28]` is really out
`[00:06:28]` there you can only see one of them at a
`[00:06:30]` there you can only see one of them at a
`[00:06:30]` time if objects are opaque because they
`[00:06:32]` time if objects are opaque because they
`[00:06:32]` all get in each other's way so you know
`[00:06:34]` all get in each other's way so you know
`[00:06:34]` that that line in the image has to
`[00:06:35]` that that line in the image has to
`[00:06:35]` depict one of these edges but you don't
`[00:06:37]` depict one of these edges but you don't
`[00:06:37]` know which
`[00:06:38]` know which
`[00:06:38]` one we could build a network where we
`[00:06:42]` one we could build a network where we
`[00:06:42]` started off by turning the lines into
`[00:06:44]` started off by turning the lines into
`[00:06:44]` activations of line neurons so let's
`[00:06:47]` activations of line neurons so let's
`[00:06:47]` suppose we already have that we have a
`[00:06:49]` suppose we already have that we have a
`[00:06:49]` large number of neurons to represent
`[00:06:50]` large number of neurons to represent
`[00:06:50]` lines in the image and we turn on just a
`[00:06:52]` lines in the image and we turn on just a
`[00:06:52]` few of them to represent the lines in
`[00:06:54]` few of them to represent the lines in
`[00:06:54]` this particular image now each of those
`[00:06:57]` this particular image now each of those
`[00:06:57]` lines could depict a number of different
`[00:06:59]` lines could depict a number of different
`[00:06:59]` 3D edges so what we do is we connect
`[00:07:02]` 3D edges so what we do is we connect
`[00:07:02]` that line neuron to a whole bunch of 3D
`[00:07:04]` that line neuron to a whole bunch of 3D
`[00:07:04]` Edge neurons with excitatory connections
`[00:07:07]` Edge neurons with excitatory connections
`[00:07:07]` those are the green ones but we know we
`[00:07:09]` those are the green ones but we know we
`[00:07:09]` can only see one of those at a time so
`[00:07:11]` can only see one of those at a time so
`[00:07:11]` we make those Edge neurons inhibit each
`[00:07:13]` we make those Edge neurons inhibit each
`[00:07:13]` other so now we captured a lot about the
`[00:07:16]` other so now we captured a lot about the
`[00:07:16]` sort of Optics of
`[00:07:17]` sort of Optics of
`[00:07:18]` perception um we do that for all of our
`[00:07:20]` perception um we do that for all of our
`[00:07:20]` line
`[00:07:21]` line
`[00:07:21]` neurons and now the question is which of
`[00:07:24]` neurons and now the question is which of
`[00:07:24]` those Edge Ur should we turn on for that
`[00:07:26]` those Edge Ur should we turn on for that
`[00:07:27]` we need more information and the
`[00:07:29]` we need more information and the
`[00:07:29]` principles we use in interpreting images
`[00:07:32]` principles we use in interpreting images
`[00:07:32]` if you see two lines in an image you
`[00:07:34]` if you see two lines in an image you
`[00:07:34]` assume that if they join in the image
`[00:07:37]` assume that if they join in the image
`[00:07:37]` they join in depth where they join that
`[00:07:39]` they join in depth where they join that
`[00:07:39]` is they're at the same depth where the
`[00:07:40]` is they're at the same depth where the
`[00:07:40]` two lines join in the image so we can
`[00:07:44]` two lines join in the image so we can
`[00:07:44]` put in extra connections for that we
`[00:07:46]` put in extra connections for that we
`[00:07:46]` could put in a connection between every
`[00:07:49]` could put in a connection between every
`[00:07:49]` pair of 3D Edge neurons that join in
`[00:07:53]` pair of 3D Edge neurons that join in
`[00:07:53]` depth um at the point where they have
`[00:07:56]` depth um at the point where they have
`[00:07:56]` the same end um we could put in a
`[00:07:58]` the same end um we could put in a
`[00:07:59]` stronger connection if they join at
`[00:08:00]` stronger connection if they join at
`[00:08:00]` right angles we really like to see
`[00:08:02]` right angles we really like to see
`[00:08:02]` images in which things join at right
`[00:08:04]` images in which things join at right
`[00:08:04]` angles so we put in a whole bunch of
`[00:08:06]` angles so we put in a whole bunch of
`[00:08:06]` connections like that and now what we
`[00:08:08]` connections like that and now what we
`[00:08:08]` hope is if we set the connection
`[00:08:10]` hope is if we set the connection
`[00:08:10]` strengths right that we've got a network
`[00:08:12]` strengths right that we've got a network
`[00:08:12]` which has two alternative states that
`[00:08:14]` which has two alternative states that
`[00:08:14]` can settle to corresponding to those two
`[00:08:16]` can settle to corresponding to those two
`[00:08:16]` alternative interpretations of the necer
`[00:08:18]` alternative interpretations of the necer
`[00:08:18]` cube this gives rise to two main
`[00:08:22]` cube this gives rise to two main
`[00:08:22]` problems um the first problem if we're
`[00:08:26]` problems um the first problem if we're
`[00:08:26]` going to use hidden neurons to come up
`[00:08:28]` going to use hidden neurons to come up
`[00:08:28]` with interpretations of IM
`[00:08:30]` with interpretations of IM
`[00:08:30]` represented in the states of the visible
`[00:08:31]` represented in the states of the visible
`[00:08:31]` neurons is the search issue how do we
`[00:08:35]` neurons is the search issue how do we
`[00:08:35]` avoid getting trapped in local Optima we
`[00:08:37]` avoid getting trapped in local Optima we
`[00:08:37]` might settle to a rather poor
`[00:08:38]` might settle to a rather poor
`[00:08:38]` interpretation and not be able to jump
`[00:08:40]` interpretation and not be able to jump
`[00:08:40]` out of it to a better
`[00:08:41]` out of it to a better
`[00:08:41]` interpretation and the second problem is
`[00:08:44]` interpretation and the second problem is
`[00:08:44]` learning I sort of implied I'd put in
`[00:08:47]` learning I sort of implied I'd put in
`[00:08:47]` all those connections by hand but we
`[00:08:49]` all those connections by hand but we
`[00:08:49]` like a neural network to put in all
`[00:08:50]` like a neural network to put in all
`[00:08:50]` those
`[00:08:53]` connections so the first the search
`[00:08:56]` problem we solve more or less by making
`[00:08:59]` problem we solve more or less by making
`[00:08:59]` making the neurons
`[00:09:00]` making the neurons
`[00:09:00]` noisy so if you have deterministic
`[00:09:03]` noisy so if you have deterministic
`[00:09:03]` neurons like in a standard hot Field net
`[00:09:06]` neurons like in a standard hot Field net
`[00:09:06]` if the system settled into one energy
`[00:09:08]` if the system settled into one energy
`[00:09:08]` minimum like a um so the ball there is
`[00:09:11]` minimum like a um so the ball there is
`[00:09:11]` the state of the whole is the
`[00:09:12]` the state of the whole is the
`[00:09:12]` configuration of the whole system it
`[00:09:15]` configuration of the whole system it
`[00:09:15]` can't get from A to B because the
`[00:09:17]` can't get from A to B because the
`[00:09:17]` decision rule for the neurons only
`[00:09:18]` decision rule for the neurons only
`[00:09:18]` allows things to go downhill in energy
`[00:09:20]` allows things to go downhill in energy
`[00:09:20]` and the graph on the right is the
`[00:09:22]` and the graph on the right is the
`[00:09:22]` decision rule if the inputs positive
`[00:09:24]` decision rule if the inputs positive
`[00:09:24]` turn on if the input's negative turn
`[00:09:27]` turn on if the input's negative turn
`[00:09:27]` off we would like to be able to get from
`[00:09:30]` off we would like to be able to get from
`[00:09:30]` A to B but that means we have to go
`[00:09:31]` A to B but that means we have to go
`[00:09:31]` uphill in energy and the solution to
`[00:09:34]` uphill in energy and the solution to
`[00:09:34]` that is to have noisy neurons stochastic
`[00:09:36]` that is to have noisy neurons stochastic
`[00:09:36]` binary neurons they still only have
`[00:09:38]` binary neurons they still only have
`[00:09:38]` binary States their states are either
`[00:09:40]` binary States their states are either
`[00:09:40]` one or zero but they're probabilistic if
`[00:09:44]` one or zero but they're probabilistic if
`[00:09:44]` they get if they get a big positive
`[00:09:46]` they get if they get a big positive
`[00:09:46]` input they almost always turn on with a
`[00:09:47]` input they almost always turn on with a
`[00:09:47]` big negative input they almost always
`[00:09:49]` big negative input they almost always
`[00:09:49]` turn off but if the input is soft if
`[00:09:51]` turn off but if the input is soft if
`[00:09:51]` it's somewhere near zero then they
`[00:09:53]` it's somewhere near zero then they
`[00:09:53]` behave probabilistically if it's
`[00:09:54]` behave probabilistically if it's
`[00:09:55]` positive they usually turn on but
`[00:09:56]` positive they usually turn on but
`[00:09:56]` occasionally turn off and if it's small
`[00:09:58]` occasionally turn off and if it's small
`[00:09:58]` negative input they usually turn off but
`[00:10:00]` negative input they usually turn off but
`[00:10:00]` occasionally turn on but they don't have
`[00:10:02]` occasionally turn on but they don't have
`[00:10:03]` real values they're always binary but
`[00:10:04]` real values they're always binary but
`[00:10:04]` they make just these probabilistic
`[00:10:08]` they make just these probabilistic
`[00:10:08]` decisions and so now if we want to
`[00:10:10]` decisions and so now if we want to
`[00:10:10]` interpret a binary image using these
`[00:10:14]` interpret a binary image using these
`[00:10:14]` hidden neurons what we do is we clamp
`[00:10:17]` hidden neurons what we do is we clamp
`[00:10:17]` the binary image on the visible units
`[00:10:20]` the binary image on the visible units
`[00:10:20]` that's specifies what the input is and
`[00:10:22]` that's specifies what the input is and
`[00:10:23]` then we pick a hidden neuron at random
`[00:10:25]` then we pick a hidden neuron at random
`[00:10:25]` we look at the total input it's getting
`[00:10:27]` we look at the total input it's getting
`[00:10:27]` from the other active hidden neuron
`[00:10:29]` from the other active hidden neuron
`[00:10:29]` and we start them all off in random
`[00:10:31]` and we start them all off in random
`[00:10:31]` States and if it gets total positive
`[00:10:33]` States and if it gets total positive
`[00:10:33]` input we probably turn it on but we
`[00:10:35]` input we probably turn it on but we
`[00:10:35]` might just turn it off if it's only a
`[00:10:36]` might just turn it off if it's only a
`[00:10:36]` small positive input so we keep
`[00:10:39]` small positive input so we keep
`[00:10:39]` implementing this rule of turn them on
`[00:10:41]` implementing this rule of turn them on
`[00:10:41]` if they big positive input off if
`[00:10:43]` if they big positive input off if
`[00:10:43]` they're big negative input but if
`[00:10:44]` they're big negative input but if
`[00:10:44]` they're soft make probabilistic
`[00:10:45]` they're soft make probabilistic
`[00:10:46]` decisions and if we go around and we
`[00:10:48]` decisions and if we go around and we
`[00:10:48]` keep picking hidden neurons and doing
`[00:10:49]` keep picking hidden neurons and doing
`[00:10:49]` that the system will eventually approach
`[00:10:52]` that the system will eventually approach
`[00:10:52]` what's called thermal equilibrium that's
`[00:10:54]` what's called thermal equilibrium that's
`[00:10:54]` a difficult concept for non- physicist
`[00:10:56]` a difficult concept for non- physicist
`[00:10:56]` and I'll explain it later um once it's
`[00:10:59]` and I'll explain it later um once it's
`[00:10:59]` reach thermal equilibrium the states of
`[00:11:01]` reach thermal equilibrium the states of
`[00:11:01]` the Hidden neurons are then an
`[00:11:03]` the Hidden neurons are then an
`[00:11:03]` interpretation of that
`[00:11:05]` interpretation of that
`[00:11:05]` input so in the case of that line
`[00:11:08]` input so in the case of that line
`[00:11:08]` drawing the hidden neurons you'd
`[00:11:10]` drawing the hidden neurons you'd
`[00:11:10]` hopefully have one hidden neuron turned
`[00:11:11]` hopefully have one hidden neuron turned
`[00:11:11]` on for each line unit and you get an
`[00:11:13]` on for each line unit and you get an
`[00:11:13]` interpretation which will be one of
`[00:11:15]` interpretation which will be one of
`[00:11:15]` those two interpretations of the necer
`[00:11:16]` those two interpretations of the necer
`[00:11:16]` cube and what we hope is that the low
`[00:11:19]` cube and what we hope is that the low
`[00:11:19]` energy interpretations will be good
`[00:11:21]` energy interpretations will be good
`[00:11:21]` interpretations of the
`[00:11:23]` interpretations of the
`[00:11:23]` data so for this line drawing um if we
`[00:11:27]` data so for this line drawing um if we
`[00:11:27]` could learn the right weights between
`[00:11:30]` could learn the right weights between
`[00:11:30]` the 2D line neurons and the 3D Edge
`[00:11:32]` the 2D line neurons and the 3D Edge
`[00:11:32]` neurons and learn the right weights
`[00:11:34]` neurons and learn the right weights
`[00:11:34]` between the 3D Edge neurons then
`[00:11:36]` between the 3D Edge neurons then
`[00:11:36]` hopefully the low energy states of the
`[00:11:39]` hopefully the low energy states of the
`[00:11:39]` network would correspond to good
`[00:11:41]` network would correspond to good
`[00:11:41]` interpretations namely seeing 3D
`[00:11:44]` interpretations namely seeing 3D
`[00:11:44]` rectangular
`[00:11:46]` rectangular
`[00:11:46]` objects so thermal equilibrium um it's
`[00:11:50]` objects so thermal equilibrium um it's
`[00:11:50]` not what you first expect which is that
`[00:11:52]` not what you first expect which is that
`[00:11:52]` the system is settled to a stable State
`[00:11:54]` the system is settled to a stable State
`[00:11:54]` um what's stabilized is not the state of
`[00:11:57]` um what's stabilized is not the state of
`[00:11:57]` the system what's stabilized is a far
`[00:11:59]` the system what's stabilized is a far
`[00:11:59]` more abstract thing that's hard to think
`[00:12:01]` more abstract thing that's hard to think
`[00:12:01]` about it's the probability distribution
`[00:12:03]` about it's the probability distribution
`[00:12:04]` over configurations of the system um
`[00:12:07]` over configurations of the system um
`[00:12:07]` that's very hard for a normal person to
`[00:12:09]` that's very hard for a normal person to
`[00:12:09]` think about um it settles to a
`[00:12:11]` think about um it settles to a
`[00:12:11]` particular distribution called the
`[00:12:12]` particular distribution called the
`[00:12:12]` boltzman distribution and in the
`[00:12:14]` boltzman distribution and in the
`[00:12:14]` boltzman distribution the probability
`[00:12:16]` boltzman distribution the probability
`[00:12:16]` once it's settled to thermal equilibrium
`[00:12:18]` once it's settled to thermal equilibrium
`[00:12:18]` of finding the system in a particular
`[00:12:20]` of finding the system in a particular
`[00:12:20]` configuration is determined solely by
`[00:12:22]` configuration is determined solely by
`[00:12:22]` the energy of that configuration and you
`[00:12:24]` the energy of that configuration and you
`[00:12:24]` have more probability of finding it in
`[00:12:26]` have more probability of finding it in
`[00:12:26]` lower energy configurations so thermally
`[00:12:29]` lower energy configurations so thermally
`[00:12:29]` equilibrium the good States the low
`[00:12:31]` equilibrium the good States the low
`[00:12:31]` energy states are more probable than the
`[00:12:33]` energy states are more probable than the
`[00:12:33]` bad
`[00:12:34]` bad
`[00:12:34]` States now to think about thermal
`[00:12:36]` States now to think about thermal
`[00:12:36]` equilibrium there's a trick physicists
`[00:12:38]` equilibrium there's a trick physicists
`[00:12:38]` use and it allows ordinary people to
`[00:12:41]` use and it allows ordinary people to
`[00:12:41]` understand this concept hopefully um you
`[00:12:45]` understand this concept hopefully um you
`[00:12:45]` just imagine a very large Ensemble
`[00:12:47]` just imagine a very large Ensemble
`[00:12:47]` gazillions of them of identical networks
`[00:12:50]` gazillions of them of identical networks
`[00:12:50]` you have these gazillion hopfield
`[00:12:52]` you have these gazillion hopfield
`[00:12:52]` networks they all have exactly the same
`[00:12:54]` networks they all have exactly the same
`[00:12:54]` weights so they're the same system
`[00:12:56]` weights so they're the same system
`[00:12:56]` essentially but you start them all off
`[00:12:58]` essentially but you start them all off
`[00:12:58]` in different random States and they all
`[00:13:00]` in different random States and they all
`[00:13:00]` make their own independent random
`[00:13:03]` make their own independent random
`[00:13:03]` decisions and there'll be a certain
`[00:13:05]` decisions and there'll be a certain
`[00:13:05]` fraction of the systems that have each
`[00:13:07]` fraction of the systems that have each
`[00:13:07]` configuration and to begin with that
`[00:13:09]` configuration and to begin with that
`[00:13:09]` fraction will just depend on how you
`[00:13:10]` fraction will just depend on how you
`[00:13:10]` started them off maybe you start them
`[00:13:12]` started them off maybe you start them
`[00:13:12]` off randomly so all configurations are
`[00:13:14]` off randomly so all configurations are
`[00:13:14]` equally likely and in this huge Ensemble
`[00:13:17]` equally likely and in this huge Ensemble
`[00:13:18]` um you'll get equal numbers of systems
`[00:13:20]` um you'll get equal numbers of systems
`[00:13:20]` in every possible configuration but then
`[00:13:22]` in every possible configuration but then
`[00:13:22]` you start running this algorithm of
`[00:13:23]` you start running this algorithm of
`[00:13:24]` update neurons in such a way that they
`[00:13:25]` update neurons in such a way that they
`[00:13:25]` tend to lower the energy but
`[00:13:27]` tend to lower the energy but
`[00:13:27]` occasionally all to go up and and
`[00:13:29]` occasionally all to go up and and
`[00:13:29]` gradually what will happen is the
`[00:13:31]` gradually what will happen is the
`[00:13:31]` fraction of the systems in any one
`[00:13:33]` fraction of the systems in any one
`[00:13:33]` configuration will stabilize so any one
`[00:13:36]` configuration will stabilize so any one
`[00:13:36]` system will be jumping between
`[00:13:38]` system will be jumping between
`[00:13:38]` configurations but the fraction of all
`[00:13:40]` configurations but the fraction of all
`[00:13:40]` the systems in a particular particular
`[00:13:42]` the systems in a particular particular
`[00:13:42]` configuration will be stable so one
`[00:13:44]` configuration will be stable so one
`[00:13:44]` system may leave a configuration but
`[00:13:47]` system may leave a configuration but
`[00:13:47]` other systems will go into that
`[00:13:48]` other systems will go into that
`[00:13:48]` configuration this is called detailed
`[00:13:50]` configuration this is called detailed
`[00:13:50]` balance and the fraction of systems will
`[00:13:52]` balance and the fraction of systems will
`[00:13:52]` stay
`[00:13:53]` stay
`[00:13:53]` stable that's it for the
`[00:13:55]` stable that's it for the
`[00:13:56]` physics um so let's imine generating an
`[00:14:00]` physics um so let's imine generating an
`[00:14:00]` image now not interpreting an image but
`[00:14:02]` image now not interpreting an image but
`[00:14:02]` generating an image to generate an image
`[00:14:05]` generating an image to generate an image
`[00:14:05]` you start by picking random States for
`[00:14:07]` you start by picking random States for
`[00:14:07]` all of the neurons the hidden neurons
`[00:14:08]` all of the neurons the hidden neurons
`[00:14:08]` and the visible neurons um then you pick
`[00:14:11]` and the visible neurons um then you pick
`[00:14:11]` a hidden or visible neuron and you
`[00:14:13]` a hidden or visible neuron and you
`[00:14:13]` update it State using the usual
`[00:14:15]` update it State using the usual
`[00:14:15]` stochastic rule if it's got lots of
`[00:14:16]` stochastic rule if it's got lots of
`[00:14:16]` positive input probably turn it on lots
`[00:14:18]` positive input probably turn it on lots
`[00:14:18]` of negative input probably turn it off
`[00:14:20]` of negative input probably turn it off
`[00:14:20]` if it's soft it behaves a bit
`[00:14:22]` if it's soft it behaves a bit
`[00:14:22]` stochastically and you keep doing
`[00:14:25]` stochastically and you keep doing
`[00:14:25]` that and if you keep doing that
`[00:14:28]` that and if you keep doing that
`[00:14:28]` repeatedly until the systems approach
`[00:14:29]` repeatedly until the systems approach
`[00:14:29]` thermal
`[00:14:30]` thermal
`[00:14:30]` equilibrium then you look at the states
`[00:14:32]` equilibrium then you look at the states
`[00:14:32]` of the visible units and that's now an
`[00:14:36]` of the visible units and that's now an
`[00:14:36]` image generated by this network from the
`[00:14:39]` image generated by this network from the
`[00:14:39]` distribution it believes in the boltzman
`[00:14:41]` distribution it believes in the boltzman
`[00:14:41]` distribution in which low low energy
`[00:14:44]` distribution in which low low energy
`[00:14:44]` configurations are much more likely than
`[00:14:45]` configurations are much more likely than
`[00:14:45]` high energy configurations but um it
`[00:14:49]` high energy configurations but um it
`[00:14:49]` believes in many possible alternative
`[00:14:51]` believes in many possible alternative
`[00:14:51]` images and you can pick one of them one
`[00:14:53]` images and you can pick one of them one
`[00:14:53]` of the things it Believes In by running
`[00:14:55]` of the things it Believes In by running
`[00:14:55]` this
`[00:14:56]` this
`[00:14:56]` process okay
`[00:14:59]` process okay
`[00:14:59]` so now what's the aim of learning in a
`[00:15:01]` so now what's the aim of learning in a
`[00:15:01]` Boltz machine the aim of learning in a
`[00:15:04]` Boltz machine the aim of learning in a
`[00:15:04]` bolts machine is to make it so when the
`[00:15:06]` bolts machine is to make it so when the
`[00:15:06]` networks's generating images think of it
`[00:15:08]` networks's generating images think of it
`[00:15:08]` as dreaming it's just randomly imagining
`[00:15:12]` as dreaming it's just randomly imagining
`[00:15:12]` things um when it's generating images
`[00:15:15]` things um when it's generating images
`[00:15:15]` those images look like the images it
`[00:15:17]` those images look like the images it
`[00:15:18]` perceives when it's doing perception on
`[00:15:20]` perceives when it's doing perception on
`[00:15:20]` real
`[00:15:21]` real
`[00:15:21]` images um if we can achieve that then
`[00:15:24]` images um if we can achieve that then
`[00:15:25]` the states of the Hidden neurons will
`[00:15:26]` the states of the Hidden neurons will
`[00:15:26]` actually be a good way to interpret the
`[00:15:29]` actually be a good way to interpret the
`[00:15:30]` real images they'll capture the
`[00:15:32]` real images they'll capture the
`[00:15:32]` underlying causes of the image at least
`[00:15:34]` underlying causes of the image at least
`[00:15:34]` that's the Hope another way of saying
`[00:15:36]` that's the Hope another way of saying
`[00:15:36]` that is um learning the weights in the
`[00:15:39]` that is um learning the weights in the
`[00:15:39]` network is equivalent to figuring out
`[00:15:42]` network is equivalent to figuring out
`[00:15:42]` how to use those hidden neurons so that
`[00:15:44]` how to use those hidden neurons so that
`[00:15:44]` the network will generate images that
`[00:15:47]` the network will generate images that
`[00:15:47]` look like the real images that seems
`[00:15:49]` look like the real images that seems
`[00:15:49]` like an extremely hard problem everybody
`[00:15:51]` like an extremely hard problem everybody
`[00:15:51]` thought that's going to be very
`[00:15:52]` thought that's going to be very
`[00:15:52]` complicated it turns out um Terry and I
`[00:15:57]` complicated it turns out um Terry and I
`[00:15:57]` um had an outrageously optimistic
`[00:15:59]` um had an outrageously optimistic
`[00:15:59]` approach um the question is could you
`[00:16:02]` approach um the question is could you
`[00:16:02]` start with a neural net a hopfield net
`[00:16:04]` start with a neural net a hopfield net
`[00:16:04]` of this stochastic kind of hopfield net
`[00:16:07]` of this stochastic kind of hopfield net
`[00:16:07]` that has lots of hidden neurons and they
`[00:16:08]` that has lots of hidden neurons and they
`[00:16:09]` just have random weights between them
`[00:16:11]` just have random weights between them
`[00:16:11]` and they have random weights connecting
`[00:16:12]` and they have random weights connecting
`[00:16:12]` them to the visible neurons so it's a
`[00:16:14]` them to the visible neurons so it's a
`[00:16:14]` big random neural net and then you just
`[00:16:16]` big random neural net and then you just
`[00:16:16]` show it lots of images and we're hoping
`[00:16:19]` show it lots of images and we're hoping
`[00:16:19]` for something that seems ridiculous
`[00:16:21]` for something that seems ridiculous
`[00:16:21]` which is
`[00:16:22]` which is
`[00:16:22]` that on perceiving lots of real images
`[00:16:26]` that on perceiving lots of real images
`[00:16:26]` it will create all the connections
`[00:16:28]` it will create all the connections
`[00:16:28]` between the hidden units and between the
`[00:16:29]` between the hidden units and between the
`[00:16:29]` hidden units and the visible units it'll
`[00:16:31]` hidden units and the visible units it'll
`[00:16:31]` waight those connections correctly so
`[00:16:33]` waight those connections correctly so
`[00:16:33]` that it comes up with sensible
`[00:16:35]` that it comes up with sensible
`[00:16:35]` interpretations of images in terms of
`[00:16:37]` interpretations of images in terms of
`[00:16:37]` causes like 3D edges that join at right
`[00:16:39]` causes like 3D edges that join at right
`[00:16:39]` angles um that sounds very optimistic
`[00:16:43]` angles um that sounds very optimistic
`[00:16:43]` and you might have thought that the
`[00:16:45]` and you might have thought that the
`[00:16:45]` learning algorithm to do that would be
`[00:16:46]` learning algorithm to do that would be
`[00:16:46]` very complicated the amazing thing about
`[00:16:48]` very complicated the amazing thing about
`[00:16:48]` boltson machines is there's a very
`[00:16:50]` boltson machines is there's a very
`[00:16:50]` simple learning algorithm that will do
`[00:16:53]` simple learning algorithm that will do
`[00:16:53]` that um this was discovered by ter
`[00:16:57]` that um this was discovered by ter
`[00:16:57]` sinowski and me in 1983
`[00:16:59]` sinowski and me in 1983
`[00:16:59]` um and the learning algorithm goes like
`[00:17:02]` um and the learning algorithm goes like
`[00:17:02]` this it has two phases there's a wake
`[00:17:05]` this it has two phases there's a wake
`[00:17:05]` phase that's the phase when the network
`[00:17:07]` phase that's the phase when the network
`[00:17:07]` is being presented with images you clamp
`[00:17:10]` is being presented with images you clamp
`[00:17:10]` an image on the visible units you let
`[00:17:12]` an image on the visible units you let
`[00:17:12]` the hidden units rattle around and
`[00:17:13]` the hidden units rattle around and
`[00:17:13]` settle down to thermal
`[00:17:15]` settle down to thermal
`[00:17:15]` equilibrium and then once the hidden
`[00:17:17]` equilibrium and then once the hidden
`[00:17:17]` units are at thermal equilibrium with
`[00:17:19]` units are at thermal equilibrium with
`[00:17:19]` the visible neurons um for every pair of
`[00:17:22]` the visible neurons um for every pair of
`[00:17:22]` connected neurons either two hidd or a
`[00:17:24]` connected neurons either two hidd or a
`[00:17:24]` visible and a hidden um if they're both
`[00:17:27]` visible and a hidden um if they're both
`[00:17:27]` on you add a small amount to the weight
`[00:17:29]` on you add a small amount to the weight
`[00:17:29]` between them that's a pretty simple
`[00:17:31]` between them that's a pretty simple
`[00:17:31]` learning rule um that's a learning rule
`[00:17:33]` learning rule um that's a learning rule
`[00:17:33]` that people who believe in Donald HEB
`[00:17:35]` that people who believe in Donald HEB
`[00:17:35]` would
`[00:17:37]` would
`[00:17:37]` like then there's a sleep phase
`[00:17:40]` like then there's a sleep phase
`[00:17:40]` obviously if you just
`[00:17:41]` obviously if you just
`[00:17:41]` run yeah if you just run the Wake phase
`[00:17:44]` run yeah if you just run the Wake phase
`[00:17:44]` the weights will only get bigger and
`[00:17:46]` the weights will only get bigger and
`[00:17:46]` pretty soon they'll all be positive and
`[00:17:47]` pretty soon they'll all be positive and
`[00:17:47]` all the neurons will turn on all the
`[00:17:49]` all the neurons will turn on all the
`[00:17:49]` time that's not much good you need to
`[00:17:51]` time that's not much good you need to
`[00:17:51]` combine it with a sleep phase and in the
`[00:17:53]` combine it with a sleep phase and in the
`[00:17:53]` Sleep phase um you can think of the
`[00:17:56]` Sleep phase um you can think of the
`[00:17:56]` network as dreaming you're settling to
`[00:17:58]` network as dreaming you're settling to
`[00:17:58]` Thermal equal
`[00:17:59]` Thermal equal
`[00:17:59]` by updating the states of all the
`[00:18:00]` by updating the states of all the
`[00:18:00]` neurons the hidden ones and the visible
`[00:18:02]` neurons the hidden ones and the visible
`[00:18:02]` ones and once you've done that and
`[00:18:04]` ones and once you've done that and
`[00:18:04]` reached thermal equilibrium for every
`[00:18:07]` reached thermal equilibrium for every
`[00:18:07]` pair of connected neurons if they're
`[00:18:09]` pair of connected neurons if they're
`[00:18:09]` both on you subtract a small amount from
`[00:18:11]` both on you subtract a small amount from
`[00:18:11]` the weight between them that's a pretty
`[00:18:13]` the weight between them that's a pretty
`[00:18:13]` simple learning algorithm and it's
`[00:18:15]` simple learning algorithm and it's
`[00:18:15]` pretty amazing that it does the right
`[00:18:18]` pretty amazing that it does the right
`[00:18:18]` thing so on
`[00:18:21]` thing so on
`[00:18:21]` average that learning algorithm changes
`[00:18:23]` average that learning algorithm changes
`[00:18:23]` the weights so as to increase the
`[00:18:25]` the weights so as to increase the
`[00:18:25]` probability that the images the network
`[00:18:27]` probability that the images the network
`[00:18:27]` generates when it's dreaming
`[00:18:29]` generates when it's dreaming
`[00:18:29]` will look like the images it sees when
`[00:18:30]` will look like the images it sees when
`[00:18:31]` it's perceiving and not for the general
`[00:18:33]` it's perceiving and not for the general
`[00:18:33]` audience so you mustn't read this next
`[00:18:35]` audience so you mustn't read this next
`[00:18:35]` two lines um for statisticians and
`[00:18:38]` two lines um for statisticians and
`[00:18:38]` machine learning people what that
`[00:18:40]` machine learning people what that
`[00:18:40]` algorithm is doing is in expectation
`[00:18:43]` algorithm is doing is in expectation
`[00:18:43]` that means it's doing it very noisily
`[00:18:44]` that means it's doing it very noisily
`[00:18:44]` and often does the wrong thing but on
`[00:18:45]` and often does the wrong thing but on
`[00:18:46]` average in expectation um it follows the
`[00:18:49]` average in expectation um it follows the
`[00:18:49]` gradient of the log likelihood that is
`[00:18:52]` gradient of the log likelihood that is
`[00:18:52]` in expectation what it's doing is making
`[00:18:54]` in expectation what it's doing is making
`[00:18:54]` it more likely that the network will
`[00:18:56]` it more likely that the network will
`[00:18:56]` generate when it's dreaming the kinds of
`[00:18:58]` generate when it's dreaming the kinds of
`[00:18:58]` images it sees when it's awake or to put
`[00:19:01]` images it sees when it's awake or to put
`[00:19:01]` it another way the weights change so
`[00:19:03]` it another way the weights change so
`[00:19:04]` that the images the network finds
`[00:19:05]` that the images the network finds
`[00:19:05]` plausible low energy images resemble the
`[00:19:08]` plausible low energy images resemble the
`[00:19:08]` images that it sees when it's awake and
`[00:19:10]` images that it sees when it's awake and
`[00:19:10]` what the learning is doing of course
`[00:19:12]` what the learning is doing of course
`[00:19:12]` what's happening in that learning
`[00:19:14]` what's happening in that learning
`[00:19:14]` algorithm is in the Wake you're lowering
`[00:19:16]` algorithm is in the Wake you're lowering
`[00:19:16]` the energy of the whole configurations
`[00:19:19]` the energy of the whole configurations
`[00:19:19]` of the network that it arrives at when
`[00:19:22]` of the network that it arrives at when
`[00:19:22]` it sees real data and when it's asleep
`[00:19:24]` it sees real data and when it's asleep
`[00:19:24]` you're raising the energy of those
`[00:19:26]` you're raising the energy of those
`[00:19:26]` configurations so what you're trying to
`[00:19:28]` configurations so what you're trying to
`[00:19:28]` make it do is believe in what you see
`[00:19:29]` make it do is believe in what you see
`[00:19:29]` when you're awake and unbelieve in what
`[00:19:31]` when you're awake and unbelieve in what
`[00:19:31]` you dream when you're
`[00:19:35]` asleep okay um so if you ask what the
`[00:19:39]` process of settling to thermal
`[00:19:40]` process of settling to thermal
`[00:19:40]` equilibrium achieves it achieves
`[00:19:42]` equilibrium achieves it achieves
`[00:19:42]` something amazing which is that
`[00:19:44]` something amazing which is that
`[00:19:44]` everything that one weight in the
`[00:19:46]` everything that one weight in the
`[00:19:46]` network needs to know about all the
`[00:19:47]` network needs to know about all the
`[00:19:47]` other weights and to know how to change
`[00:19:49]` other weights and to know how to change
`[00:19:49]` one weight you need to know something
`[00:19:50]` one weight you need to know something
`[00:19:50]` about all the other weights they all
`[00:19:51]` about all the other weights they all
`[00:19:52]` interact but everything you need to know
`[00:19:54]` interact but everything you need to know
`[00:19:54]` shows up in the difference between two
`[00:19:57]` shows up in the difference between two
`[00:19:57]` correlations it shows up in the
`[00:19:58]` correlations it shows up in the
`[00:19:58]` difference between how often the two
`[00:20:01]` difference between how often the two
`[00:20:01]` neurons are on together when the
`[00:20:02]` neurons are on together when the
`[00:20:02]` Network's observing data and how often
`[00:20:05]` Network's observing data and how often
`[00:20:05]` they're on together when the network
`[00:20:06]` they're on together when the network
`[00:20:06]` isn't observing data when it's dreaming
`[00:20:09]` isn't observing data when it's dreaming
`[00:20:09]` and somehow those correlations measured
`[00:20:11]` and somehow those correlations measured
`[00:20:11]` in those two situations tell a weight
`[00:20:14]` in those two situations tell a weight
`[00:20:14]` everything it needs to know about all
`[00:20:15]` everything it needs to know about all
`[00:20:15]` the other weights the reason that's
`[00:20:17]` the other weights the reason that's
`[00:20:17]` surprising is because in an algorithm
`[00:20:19]` surprising is because in an algorithm
`[00:20:19]` like back propagation which is what all
`[00:20:21]` like back propagation which is what all
`[00:20:22]` the neural Nets now actually use um you
`[00:20:24]` the neural Nets now actually use um you
`[00:20:24]` require a backward pass to convey
`[00:20:26]` require a backward pass to convey
`[00:20:26]` information about the other weights and
`[00:20:28]` information about the other weights and
`[00:20:28]` that backward pass behaves very
`[00:20:30]` that backward pass behaves very
`[00:20:30]` differently from the forward pass in the
`[00:20:32]` differently from the forward pass in the
`[00:20:33]` forward pass you're communicating
`[00:20:34]` forward pass you're communicating
`[00:20:34]` activities of neurons to later layers of
`[00:20:37]` activities of neurons to later layers of
`[00:20:37]` neurons in the backward path you're
`[00:20:39]` neurons in the backward path you're
`[00:20:39]` conveying sensitivities you're conveying
`[00:20:42]` conveying sensitivities you're conveying
`[00:20:42]` um a different kind of quantity
`[00:20:43]` um a different kind of quantity
`[00:20:43]` altogether and that makes back
`[00:20:45]` altogether and that makes back
`[00:20:45]` propagation rather implausible as a
`[00:20:47]` propagation rather implausible as a
`[00:20:47]` theory of how the brain works and so
`[00:20:49]` theory of how the brain works and so
`[00:20:49]` when Terry came up with this Theory this
`[00:20:52]` when Terry came up with this Theory this
`[00:20:52]` learning procedure for boltzman machines
`[00:20:55]` learning procedure for boltzman machines
`[00:20:55]` um we were completely convinced that
`[00:20:58]` um we were completely convinced that
`[00:20:58]` must be how the brain works and we
`[00:21:00]` must be how the brain works and we
`[00:21:00]` decided we were going to get The Nobel
`[00:21:02]` decided we were going to get The Nobel
`[00:21:02]` Prize in physiology or medicine
`[00:21:06]` Prize in physiology or medicine
`[00:21:06]` um it never occurred to us that if it
`[00:21:09]` um it never occurred to us that if it
`[00:21:09]` wasn't how the brain works we could get
`[00:21:11]` wasn't how the brain works we could get
`[00:21:11]` The Nobel Prize in
`[00:21:13]` The Nobel Prize in
`[00:21:13]` physics okay there's only one problem
`[00:21:17]` physics okay there's only one problem
`[00:21:17]` and the problem is that settling to
`[00:21:19]` and the problem is that settling to
`[00:21:19]` thermal equilibrium is a very slow
`[00:21:21]` thermal equilibrium is a very slow
`[00:21:21]` process for very big networks with large
`[00:21:23]` process for very big networks with large
`[00:21:23]` weights if the weights are very small
`[00:21:25]` weights if the weights are very small
`[00:21:25]` you can do it quickly but when the
`[00:21:26]` you can do it quickly but when the
`[00:21:26]` weights are big after it's learned some
`[00:21:27]` weights are big after it's learned some
`[00:21:27]` stuff it's slow so actually bolts
`[00:21:30]` stuff it's slow so actually bolts
`[00:21:30]` machines are a wonderful romantic idea
`[00:21:32]` machines are a wonderful romantic idea
`[00:21:32]` they this beautifully simple learning
`[00:21:35]` they this beautifully simple learning
`[00:21:35]` algorithm um which is doing something
`[00:21:38]` algorithm um which is doing something
`[00:21:38]` very complicated it's constructing these
`[00:21:39]` very complicated it's constructing these
`[00:21:39]` whole networks of hidden units that
`[00:21:40]` whole networks of hidden units that
`[00:21:40]` interpret the data um in a very by using
`[00:21:43]` interpret the data um in a very by using
`[00:21:43]` a very simple algorithm and the only
`[00:21:45]` a very simple algorithm and the only
`[00:21:45]` thing is that they're just much too slow
`[00:21:47]` thing is that they're just much too slow
`[00:21:47]` so that was that for bolts machines
`[00:21:50]` so that was that for bolts machines
`[00:21:50]` um and the lecture should really have
`[00:21:53]` um and the lecture should really have
`[00:21:53]` ended there but 17 years later I
`[00:21:57]` ended there but 17 years later I
`[00:21:57]` realized that if you restrict both
`[00:21:58]` realized that if you restrict both
`[00:21:58]` machines a lot and just have hidden
`[00:22:00]` machines a lot and just have hidden
`[00:22:00]` units that aren't connected to each
`[00:22:02]` units that aren't connected to each
`[00:22:02]` other then you can get a much faster
`[00:22:05]` other then you can get a much faster
`[00:22:05]` learning algorithm so if there's no
`[00:22:07]` learning algorithm so if there's no
`[00:22:07]` connections between the hidden neurons
`[00:22:09]` connections between the hidden neurons
`[00:22:09]` then the Wake phase becomes very
`[00:22:11]` then the Wake phase becomes very
`[00:22:11]` simple what you do is you clamp an input
`[00:22:14]` simple what you do is you clamp an input
`[00:22:14]` on the visible units to represent an
`[00:22:15]` on the visible units to represent an
`[00:22:15]` image and then in parallel now you can
`[00:22:19]` image and then in parallel now you can
`[00:22:19]` update all the hidden
`[00:22:20]` update all the hidden
`[00:22:20]` neurons and you've now reach thermal
`[00:22:23]` neurons and you've now reach thermal
`[00:22:23]` equilibrium you just update them all
`[00:22:24]` equilibrium you just update them all
`[00:22:24]` once they just look at the visible input
`[00:22:26]` once they just look at the visible input
`[00:22:26]` and randomly pick one of their two
`[00:22:28]` and randomly pick one of their two
`[00:22:28]` states based on how much input they're
`[00:22:29]` states based on how much input they're
`[00:22:29]` getting and now you're at thermal
`[00:22:31]` getting and now you're at thermal
`[00:22:31]` equilibrium in one step that's great for
`[00:22:35]` equilibrium in one step that's great for
`[00:22:35]` the hidden neurons you still have a
`[00:22:38]` the hidden neurons you still have a
`[00:22:38]` problem in the Sleep phase you have to
`[00:22:41]` problem in the Sleep phase you have to
`[00:22:41]` um put the network in some random State
`[00:22:44]` um put the network in some random State
`[00:22:44]` update the hidden neurons update the
`[00:22:45]` update the hidden neurons update the
`[00:22:45]` visible neurons update the hidden
`[00:22:47]` visible neurons update the hidden
`[00:22:47]` neurons update the visible neurons and
`[00:22:48]` neurons update the visible neurons and
`[00:22:48]` you have to go on a long time to reach
`[00:22:50]` you have to go on a long time to reach
`[00:22:50]` thermal equilibrium and so the algorithm
`[00:22:52]` thermal equilibrium and so the algorithm
`[00:22:52]` is still hopeless but it turns out
`[00:22:54]` is still hopeless but it turns out
`[00:22:54]` there's a shortcut the shortcut doesn't
`[00:22:57]` there's a shortcut the shortcut doesn't
`[00:22:57]` quite do the right thing um which is
`[00:23:00]` quite do the right thing um which is
`[00:23:00]` embarrassing but it works pretty well in
`[00:23:01]` embarrassing but it works pretty well in
`[00:23:01]` practice so the shortcut works like this
`[00:23:04]` practice so the shortcut works like this
`[00:23:04]` you put data on the visible units that's
`[00:23:07]` you put data on the visible units that's
`[00:23:07]` an image and then you update all the
`[00:23:09]` an image and then you update all the
`[00:23:09]` hidden neurons in parallel um and
`[00:23:12]` hidden neurons in parallel um and
`[00:23:12]` they've now reached thermal equilibrium
`[00:23:13]` they've now reached thermal equilibrium
`[00:23:13]` with the data you now update all the
`[00:23:17]` with the data you now update all the
`[00:23:17]` visible units and you get what we call a
`[00:23:19]` visible units and you get what we call a
`[00:23:19]` reconstruction it's going to be like the
`[00:23:21]` reconstruction it's going to be like the
`[00:23:21]` data but not quite the same now you
`[00:23:24]` data but not quite the same now you
`[00:23:24]` update all the hidden units again and
`[00:23:26]` update all the hidden units again and
`[00:23:26]` then you stop that's it you're done
`[00:23:29]` then you stop that's it you're done
`[00:23:29]` and the way you do
`[00:23:31]` and the way you do
`[00:23:31]` learning is you measure how often the
`[00:23:35]` learning is you measure how often the
`[00:23:35]` neurons IJ the visible neuron I and the
`[00:23:37]` neurons IJ the visible neuron I and the
`[00:23:37]` hidden neuron J are on together when
`[00:23:40]` hidden neuron J are on together when
`[00:23:40]` you're showing it data and it's reached
`[00:23:41]` you're showing it data and it's reached
`[00:23:41]` equilibrium with data and you measure
`[00:23:44]` equilibrium with data and you measure
`[00:23:44]` how often they're on together when
`[00:23:46]` how often they're on together when
`[00:23:46]` you're showing it reconstructions and
`[00:23:47]` you're showing it reconstructions and
`[00:23:47]` it's reached equilibrium with the
`[00:23:49]` it's reached equilibrium with the
`[00:23:49]` Reconstruction and that difference is
`[00:23:51]` Reconstruction and that difference is
`[00:23:51]` your learning algorithm you just change
`[00:23:54]` your learning algorithm you just change
`[00:23:54]` the weights in proportion to that
`[00:23:55]` the weights in proportion to that
`[00:23:56]` difference and that actually works
`[00:23:58]` difference and that actually works
`[00:23:58]` pretty well and it's much much faster
`[00:24:00]` pretty well and it's much much faster
`[00:24:00]` it's fast enough to make bolts machines
`[00:24:02]` it's fast enough to make bolts machines
`[00:24:02]` finally practical so
`[00:24:07]` finally practical so
`[00:24:07]` um okay so um Netflix actually used
`[00:24:11]` um okay so um Netflix actually used
`[00:24:11]` restricted bolts machines um combined
`[00:24:14]` restricted bolts machines um combined
`[00:24:14]` with other methods to decide which new
`[00:24:18]` with other methods to decide which new
`[00:24:18]` movies to suggest you look at based on
`[00:24:20]` movies to suggest you look at based on
`[00:24:20]` the preferences of of all sorts of other
`[00:24:22]` the preferences of of all sorts of other
`[00:24:22]` users who are a bit like you and they
`[00:24:24]` users who are a bit like you and they
`[00:24:24]` actually worked they won the competition
`[00:24:26]` actually worked they won the competition
`[00:24:26]` this combination of bolts machines and
`[00:24:28]` this combination of bolts machines and
`[00:24:28]` these methods won the Netflix
`[00:24:29]` these methods won the Netflix
`[00:24:29]` competition for how well can you predict
`[00:24:32]` competition for how well can you predict
`[00:24:32]` what users will
`[00:24:34]` what users will
`[00:24:34]` like but of course with just hidden
`[00:24:36]` like but of course with just hidden
`[00:24:36]` neurons aren't connected to each other
`[00:24:38]` neurons aren't connected to each other
`[00:24:38]` you can't build layers of feature
`[00:24:40]` you can't build layers of feature
`[00:24:40]` detectors which are what you need um for
`[00:24:44]` detectors which are what you need um for
`[00:24:44]` doing recognizing objects in images or
`[00:24:47]` doing recognizing objects in images or
`[00:24:47]` recognizing words in speech and it looks
`[00:24:49]` recognizing words in speech and it looks
`[00:24:49]` like this a strong restriction of having
`[00:24:51]` like this a strong restriction of having
`[00:24:51]` just one layer of hidden units without
`[00:24:53]` just one layer of hidden units without
`[00:24:53]` connections between them but actually
`[00:24:55]` connections between them but actually
`[00:24:55]` you can get round
`[00:24:56]` you can get round
`[00:24:56]` that so what you can do is you can stack
`[00:25:00]` that so what you can do is you can stack
`[00:25:00]` these restricted Bots
`[00:25:01]` these restricted Bots
`[00:25:01]` machines what you do is you take your
`[00:25:03]` machines what you do is you take your
`[00:25:04]` data you show the restricted bolts
`[00:25:06]` data you show the restricted bolts
`[00:25:06]` machine RBM the data it has just one
`[00:25:09]` machine RBM the data it has just one
`[00:25:09]` hidden layer and using this contrasting
`[00:25:11]` hidden layer and using this contrasting
`[00:25:11]` Divergence algorithm that just goes up
`[00:25:13]` Divergence algorithm that just goes up
`[00:25:13]` and down and up again you learn some
`[00:25:15]` and down and up again you learn some
`[00:25:15]` weights so that the hidden units capture
`[00:25:18]` weights so that the hidden units capture
`[00:25:18]` structure in the data the hidden units
`[00:25:20]` structure in the data the hidden units
`[00:25:20]` turn into feature detectors that capture
`[00:25:23]` turn into feature detectors that capture
`[00:25:23]` commonly correlated things in the
`[00:25:25]` commonly correlated things in the
`[00:25:25]` data then you take those hidden hidden
`[00:25:29]` data then you take those hidden hidden
`[00:25:29]` activity patterns the binary activity
`[00:25:31]` activity patterns the binary activity
`[00:25:31]` patterns in the hidden units and you
`[00:25:33]` patterns in the hidden units and you
`[00:25:33]` treat those as data so you just copy
`[00:25:35]` treat those as data so you just copy
`[00:25:35]` those into another RBM and they're the
`[00:25:38]` those into another RBM and they're the
`[00:25:38]` data for the other RBM and that second
`[00:25:41]` data for the other RBM and that second
`[00:25:41]` RBM looks at these features that have
`[00:25:44]` RBM looks at these features that have
`[00:25:44]` captured correlations in the data and it
`[00:25:46]` captured correlations in the data and it
`[00:25:46]` captures correlations between those
`[00:25:48]` captures correlations between those
`[00:25:48]` features and you keep going like that so
`[00:25:50]` features and you keep going like that so
`[00:25:50]` you're capturing more and more
`[00:25:51]` you're capturing more and more
`[00:25:51]` complicated
`[00:25:52]` complicated
`[00:25:52]` correlations and so you can learn the
`[00:25:54]` correlations and so you can learn the
`[00:25:54]` second set of Weights W2 and you can do
`[00:25:56]` second set of Weights W2 and you can do
`[00:25:56]` it as many times as you like let's learn
`[00:25:58]` it as many times as you like let's learn
`[00:25:58]` a third set of
`[00:26:00]` a third set of
`[00:26:00]` Weights so now we've got a bunch of
`[00:26:02]` Weights so now we've got a bunch of
`[00:26:02]` separate bolts machines Each of which is
`[00:26:04]` separate bolts machines Each of which is
`[00:26:04]` finding structure Among the Hidden units
`[00:26:07]` finding structure Among the Hidden units
`[00:26:07]` of the previous boltzman machine then
`[00:26:10]` of the previous boltzman machine then
`[00:26:10]` what you can do is you can stack up
`[00:26:13]` what you can do is you can stack up
`[00:26:13]` these boltzman machines um and just
`[00:26:16]` these boltzman machines um and just
`[00:26:16]` treat them as a feedforward net so
`[00:26:18]` treat them as a feedforward net so
`[00:26:18]` ignore the fact the connections are
`[00:26:19]` ignore the fact the connections are
`[00:26:19]` symmetrical just use the connections in
`[00:26:21]` symmetrical just use the connections in
`[00:26:21]` One Direction now because you've got a
`[00:26:23]` One Direction now because you've got a
`[00:26:23]` way of getting in your first hidden
`[00:26:24]` way of getting in your first hidden
`[00:26:25]` layer you've extracted features that
`[00:26:27]` layer you've extracted features that
`[00:26:27]` capture correlations In The Raw data and
`[00:26:29]` capture correlations In The Raw data and
`[00:26:29]` then in your second hidden layer you've
`[00:26:31]` then in your second hidden layer you've
`[00:26:31]` extracted features that capture
`[00:26:33]` extracted features that capture
`[00:26:33]` correlations in the features extracted
`[00:26:34]` correlations in the features extracted
`[00:26:34]` in the first hidden layer and so on so
`[00:26:37]` in the first hidden layer and so on so
`[00:26:37]` you're getting more and more abstract
`[00:26:38]` you're getting more and more abstract
`[00:26:38]` features correlations among
`[00:26:41]` features correlations among
`[00:26:41]` correlations once you've stacked them up
`[00:26:43]` correlations once you've stacked them up
`[00:26:43]` like that then you can just add a final
`[00:26:46]` like that then you can just add a final
`[00:26:46]` hidden layer like this and you can do
`[00:26:49]` hidden layer like this and you can do
`[00:26:49]` supervised learning that is now you can
`[00:26:51]` supervised learning that is now you can
`[00:26:51]` start telling it about the names of
`[00:26:52]` start telling it about the names of
`[00:26:52]` things like cat and dog those are the
`[00:26:55]` things like cat and dog those are the
`[00:26:55]` class labels and you're going to have to
`[00:26:58]` class labels and you're going to have to
`[00:26:58]` learn the weights to those class labels
`[00:27:00]` learn the weights to those class labels
`[00:27:00]` but you start with this network that
`[00:27:02]` but you start with this network that
`[00:27:02]` you've initialized by learning a stack
`[00:27:04]` you've initialized by learning a stack
`[00:27:04]` of bolts machines and two beautiful
`[00:27:07]` of bolts machines and two beautiful
`[00:27:07]` things happen the first beautiful thing
`[00:27:09]` things happen the first beautiful thing
`[00:27:09]` is if you initialize this way the
`[00:27:11]` is if you initialize this way the
`[00:27:11]` network learns much faster than if you
`[00:27:13]` network learns much faster than if you
`[00:27:13]` initialize with random weights because
`[00:27:15]` initialize with random weights because
`[00:27:15]` it's already learned a whole bunch of
`[00:27:17]` it's already learned a whole bunch of
`[00:27:17]` sensible features for modeling structure
`[00:27:19]` sensible features for modeling structure
`[00:27:19]` in the data it hasn't learned anything
`[00:27:22]` in the data it hasn't learned anything
`[00:27:22]` about what things are called but it's
`[00:27:24]` about what things are called but it's
`[00:27:24]` learned about the structure in the data
`[00:27:25]` learned about the structure in the data
`[00:27:25]` and then learning what things are called
`[00:27:27]` and then learning what things are called
`[00:27:27]` is relatively quick
`[00:27:29]` is relatively quick
`[00:27:29]` just like with small children they don't
`[00:27:31]` just like with small children they don't
`[00:27:31]` have to be told that's a cow 2,000 times
`[00:27:35]` have to be told that's a cow 2,000 times
`[00:27:35]` before they know that's a cow they
`[00:27:37]` before they know that's a cow they
`[00:27:37]` figure out the concept of cow for
`[00:27:39]` figure out the concept of cow for
`[00:27:39]` themselves and then their mother says
`[00:27:40]` themselves and then their mother says
`[00:27:40]` that's a cow and they've got it well
`[00:27:43]` that's a cow and they've got it well
`[00:27:43]` maybe twice
`[00:27:47]` maybe twice
`[00:27:47]` um so it makes it much faster to learn
`[00:27:51]` um so it makes it much faster to learn
`[00:27:51]` for example to recognize objects in
`[00:27:53]` for example to recognize objects in
`[00:27:53]` images um it also makes the networks
`[00:27:56]` images um it also makes the networks
`[00:27:56]` generalize much better because done most
`[00:27:58]` generalize much better because done most
`[00:27:58]` of the learning without using labels
`[00:28:00]` of the learning without using labels
`[00:28:00]` they don't need many labels now they're
`[00:28:03]` they don't need many labels now they're
`[00:28:03]` not extracting all the information from
`[00:28:05]` not extracting all the information from
`[00:28:05]` the labels they're extracting the
`[00:28:07]` the labels they're extracting the
`[00:28:07]` information from the correlations in the
`[00:28:09]` information from the correlations in the
`[00:28:09]` data and that makes them generalize much
`[00:28:12]` data and that makes them generalize much
`[00:28:12]` better with needing far fewer
`[00:28:15]` better with needing far fewer
`[00:28:15]` labels so that was all very nice and
`[00:28:19]` labels so that was all very nice and
`[00:28:19]` between about 2006 and
`[00:28:22]` between about 2006 and
`[00:28:22]` 2011 people were using particularly in
`[00:28:25]` 2011 people were using particularly in
`[00:28:25]` my lab and yoshu beno's lab and Yan's
`[00:28:27]` my lab and yoshu beno's lab and Yan's
`[00:28:27]` lab people were using um stacks of rbms
`[00:28:31]` lab people were using um stacks of rbms
`[00:28:31]` to pre-train feed forward neural
`[00:28:34]` to pre-train feed forward neural
`[00:28:34]` networks and then they would apply back
`[00:28:36]` networks and then they would apply back
`[00:28:36]` propagation and in 2009 two students in
`[00:28:40]` propagation and in 2009 two students in
`[00:28:40]` my lab George Dar and Abdul rahan
`[00:28:42]` my lab George Dar and Abdul rahan
`[00:28:42]` Muhammad showed that this technique
`[00:28:44]` Muhammad showed that this technique
`[00:28:44]` worked a little bit better than the best
`[00:28:45]` worked a little bit better than the best
`[00:28:45]` existing techniques for recognizing
`[00:28:48]` existing techniques for recognizing
`[00:28:48]` fragments of phones in
`[00:28:50]` fragments of phones in
`[00:28:50]` speech um and that then changed the
`[00:28:53]` speech um and that then changed the
`[00:28:53]` speech recognition Community my graduate
`[00:28:56]` speech recognition Community my graduate
`[00:28:56]` students went went off to the very
`[00:28:58]` students went went off to the very
`[00:28:58]` leading speech groups and in
`[00:29:00]` leading speech groups and in
`[00:29:00]` 2012 um Things based on exactly this
`[00:29:04]` 2012 um Things based on exactly this
`[00:29:04]` stacked up restricted bolts machines um
`[00:29:06]` stacked up restricted bolts machines um
`[00:29:06]` went into production at Google and they
`[00:29:08]` went into production at Google and they
`[00:29:08]` got better speech recognition suddenly
`[00:29:10]` got better speech recognition suddenly
`[00:29:10]` the speech recognition on the Android
`[00:29:11]` the speech recognition on the Android
`[00:29:11]` got a lot
`[00:29:13]` got a lot
`[00:29:13]` better
`[00:29:15]` better
`[00:29:15]` um unfortunately for boltzman machines
`[00:29:18]` um unfortunately for boltzman machines
`[00:29:18]` um once we' shown that these deep neural
`[00:29:20]` um once we' shown that these deep neural
`[00:29:20]` networks really worked very well if you
`[00:29:21]` networks really worked very well if you
`[00:29:21]` pre-trained them with stacks of Bolt
`[00:29:23]` pre-trained them with stacks of Bolt
`[00:29:23]` restricted bolts machines people found
`[00:29:25]` restricted bolts machines people found
`[00:29:25]` other ways of initializing the weights
`[00:29:27]` other ways of initializing the weights
`[00:29:27]` and they no no longer use stacks of Bol
`[00:29:29]` and they no no longer use stacks of Bol
`[00:29:29]` machines um but if you're a chemist you
`[00:29:32]` machines um but if you're a chemist you
`[00:29:32]` know that enzymes are useful things and
`[00:29:35]` know that enzymes are useful things and
`[00:29:35]` even though rbms are no longer used they
`[00:29:38]` even though rbms are no longer used they
`[00:29:38]` allowed us to make the transition from
`[00:29:40]` allowed us to make the transition from
`[00:29:40]` thinking that deep neural networks would
`[00:29:41]` thinking that deep neural networks would
`[00:29:41]` never work to seeing that deep neural
`[00:29:43]` never work to seeing that deep neural
`[00:29:43]` networks actually could be made to work
`[00:29:45]` networks actually could be made to work
`[00:29:45]` rather easily if you initialize them
`[00:29:47]` rather easily if you initialize them
`[00:29:47]` this way um once you've made the
`[00:29:49]` this way um once you've made the
`[00:29:49]` transition you don't need the enzyme
`[00:29:50]` transition you don't need the enzyme
`[00:29:50]` anymore so think of them as historical
`[00:29:53]` anymore so think of them as historical
`[00:29:53]` enzymes
`[00:29:54]` enzymes
`[00:29:54]` um the idea of using unlearning during
`[00:29:57]` um the idea of using unlearning during
`[00:29:57]` sleep though to get an algorithm that's
`[00:30:00]` sleep though to get an algorithm that's
`[00:30:00]` more biologically plausible and avoids
`[00:30:03]` more biologically plausible and avoids
`[00:30:03]` the backward path of back propagation I
`[00:30:05]` the backward path of back propagation I
`[00:30:05]` still think there's a lot of mileage in
`[00:30:06]` still think there's a lot of mileage in
`[00:30:06]` that um idea and I'm still optimistic
`[00:30:10]` that um idea and I'm still optimistic
`[00:30:10]` that when we do eventually understand
`[00:30:13]` that when we do eventually understand
`[00:30:13]` how the brain learns um it will turn out
`[00:30:16]` how the brain learns um it will turn out
`[00:30:16]` to involve using sleep to do unlearning
`[00:30:19]` to involve using sleep to do unlearning
`[00:30:19]` um so I'm still
`[00:30:21]` um so I'm still
`[00:30:21]` optimistic and I think I'm done
`[00:30:55]` very nice thank you very much
`[00:31:18]` so please join me now in welcoming both
`[00:31:20]` laurates on the stage to join jointly
`[00:31:24]` laurates on the stage to join jointly
`[00:31:24]` receive our warmest applaud
`[00:31:27]` receive our warmest applaud
`[00:31:27]` [Applause]
