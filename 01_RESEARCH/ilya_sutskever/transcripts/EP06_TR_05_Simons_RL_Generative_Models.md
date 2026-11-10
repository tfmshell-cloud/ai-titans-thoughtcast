# Simons Institute Berkeley: Ilya Sutskever — RL using Generative Models
- **YouTube URL:** https://www.youtube.com/watch?v=TlPaxVVa_WM
- **Lines:** 990

---

[00:00:00] oh fantastic okay so um it's a pleasure
[00:00:02] to introduce the next speaker Rahul Jane
[00:00:05] from
[00:00:06] USC a Berkeley grad of some some years
[00:00:10] back and well known in stochastic
[00:00:13] systems and U
[00:00:15] optimization and more recently well
[00:00:17] actually quite a while now in
[00:00:18] reinforcement learning we became buddies
[00:00:21] at uh at the Simon program two years ago
[00:00:25] um and I'll I'll just let you
[00:00:28] go Sean thank you very much for the kind
[00:00:31] kind introduction and uh uh thank you to
[00:00:34] you uh MD and Emma for organizing this
[00:00:37] uh very interesting Workshop so um uh
[00:00:41] it's a hard act to follow after
[00:00:43] excellent Talks by muner and Alex but I
[00:00:45] will try my best and the flavor of this
[00:00:48] talk is slightly different from the
[00:00:50] first two talks so I'm going to talk
[00:00:52] about uh reinforcement learning for
[00:00:54] continuous State and action Space
[00:00:55] Systems using gym leing models and it's
[00:00:59] only5 minute talk so I thought I'll
[00:01:01] focus on something very specific a
[00:01:03] specific problem uh this is work I this
[00:01:07] Builds on work that I've been doing
[00:01:08] earlier I've presented before at Simons
[00:01:11] this joint work with hesi but like I was
[00:01:13] saying it builds on prior work uh uh and
[00:01:17] I guess it's good to acknowledge the
[00:01:19] work with uh former students and post
[00:01:21] talks and other collaborators with whom
[00:01:24] uh that happened okay so let me start by
[00:01:27] just stating the obvious I think we are
[00:01:29] all we've all heard of the various
[00:01:31] successes of reinforcement learning
[00:01:33] particularly uh you know uh deep
[00:01:35] reinforcement learning on um various
[00:01:38] kinds of uh games in particular um you
[00:01:42] know it's it's been very
[00:01:44] impressive uh but I think uh you know
[00:01:47] one thing to note here is that the this
[00:01:50] success uho however imp impressive it
[00:01:52] has been has been on particular type of
[00:01:55] problems namely these are you know games
[00:01:58] mostly deterministic Move games
[00:02:00] they have large uh very large uh State
[00:02:03] and action spaces that's what makes them
[00:02:06] really challenging and but yeah like I
[00:02:09] said it's still been very impressive but
[00:02:11] that does raise the question whether you
[00:02:13] know what about other kind of problems
[00:02:16] whether you know we going to have we're
[00:02:18] going to make be able to make progress
[00:02:20] on other kind of problems particularly
[00:02:22] problems coming from Robotics and uh you
[00:02:26] know autonomous systems where physics
[00:02:28] matters so is a very prototype of very
[00:02:31] simple uh mobile robot um you know we
[00:02:35] want to be able to just have this robot
[00:02:37] walk and do various kinds of Maneuvers
[00:02:39] and this robot has uh States and action
[00:02:43] spaces that are both continuous the
[00:02:46] state
[00:02:47] spaces uh depends on the system but it's
[00:02:50] of the order of 30 to 35 Dimensions the
[00:02:53] action space also depends on the system
[00:02:55] but let's say that it's something of the
[00:02:57] order of 10 Dimensions so these are not
[00:02:59] easy problems to handle uh
[00:03:02] for uh at least uh you know uh classical
[00:03:07] uh methods including RL
[00:03:09] methods and but so and like like I was
[00:03:13] saying physics matters here and uh uh
[00:03:17] one would think that uh one would need a
[00:03:19] modelbased approach for problems like
[00:03:21] this uh but given the complexity of uh
[00:03:25] such a system I mean that has proved
[00:03:27] quite difficult now one thing I should
[00:03:30] say is that this is not to imply that
[00:03:33] Pro problems of this kind are are still
[00:03:36] open so there has been a lot of there's
[00:03:38] been work going on for quite a while on
[00:03:40] problems of this kind and there's been
[00:03:42] progress and but increasingly what's
[00:03:45] happening is that you know we are
[00:03:46] dealing with more and more sort of
[00:03:48] complicated systems that are harder to
[00:03:51] stabilize and and that and we basically
[00:03:53] pushing the
[00:03:54] envelop so surprisingly uh you know the
[00:03:58] people have so like I was saying so
[00:04:00] model based approaches have not really
[00:04:02] succeeded so people have been trying
[00:04:04] model free approaches uh and at first uh
[00:04:09] on first thought it seems that okay you
[00:04:11] know physics matters here so how can
[00:04:13] such such approaches succeed when if you
[00:04:15] ignore the physics but surprisingly
[00:04:17] there's been some
[00:04:19] success and uh but the the the
[00:04:22] performance can at times be fragile and
[00:04:25] there is also
[00:04:26] some uh skepticism whether such a
[00:04:30] approaches um are really doing anything
[00:04:33] more than random
[00:04:34] search and uh so that's sort of one
[00:04:38] point I wanted to make uh these are
[00:04:40] mostly based on such so things that work
[00:04:43] on such problem they're based on deep
[00:04:45] reinfor
[00:04:46] learning uh you know there is Long
[00:04:48] training times a lot of hyperparameter
[00:04:51] tuning that needs to happen etc etc but
[00:04:55] the other point I want to make is that
[00:04:57] on problems of this kind we train
[00:05:00] algorithms in a in simulation using you
[00:05:03] know a generative model or a simulation
[00:05:04] model this is all done offline and so
[00:05:08] there is some value in problems of this
[00:05:10] kind which is what this Workshop is
[00:05:11] about so I guess I don't need to
[00:05:12] convince people about that here uh but
[00:05:16] that's sort of the so this is the
[00:05:18] setting uh you know more or less the
[00:05:21] setting of uh standard reinforcement
[00:05:23] learning so there is a system with State
[00:05:25] uh X action U uh f is the transition
[00:05:29] function here W is the noise and given
[00:05:32] the current state XK and action UK and
[00:05:34] noise WK you get the next state XK plus
[00:05:37] one and then there is a reward R and
[00:05:40] then the agent uh takes the reward into
[00:05:43] account to determine what the next
[00:05:44] action should be so the setting here is
[00:05:48] that we are going to assume that the
[00:05:51] transition function f is strictly
[00:05:53] speaking unknown but we you know like I
[00:05:56] said I mean if this is happening in a
[00:05:58] simulation in a Sim ulator then uh you
[00:06:01] know we we have an implementation it
[00:06:03] just might be very complex and we may
[00:06:05] not be able to write it down or use it
[00:06:07] in any kind of model based approach so
[00:06:09] the point is we you know we so so we
[00:06:13] have a blackbox simulator and we can
[00:06:14] draw samples from such a simulator at
[00:06:17] will so that's sort of the setting that
[00:06:18] we're going to
[00:06:20] consider um the focus in this talk is
[00:06:23] going to be on the infinite Horizon
[00:06:24] discounted criteria and uh you know we
[00:06:27] interested in finding a policy that uh
[00:06:30] maximizes the expectation of the total
[00:06:32] discounted sum of rewards and so we're
[00:06:34] looking for let's say to start with the
[00:06:37] optimal value function P star and of
[00:06:39] course uh just uh you know one slide on
[00:06:41] stochastic control 101 uh you know we
[00:06:44] know that the optimal value function V
[00:06:46] Star it satisfies the uh the bman
[00:06:49] equation where T is the bman operator so
[00:06:52] it's a fix point of the of the bman
[00:06:54] operator and of course we know that e is
[00:06:57] a contraction and so by Bak fix Point
[00:07:00] theorem uh there exists such a fixed
[00:07:02] point and then a very simple algorithm
[00:07:05] uh you know uh Works to to find it that
[00:07:08] is you can start with any V not and then
[00:07:10] just iteratively apply the contractive
[00:07:13] operator on it and then you guarantee
[00:07:15] that that will converge to the optimal
[00:07:16] value function V Star and once you have
[00:07:19] that then from that you can infer the
[00:07:21] optimal policy which is you know which
[00:07:23] is what we're looking for I mean you
[00:07:24] want to deploy this thing uh put this
[00:07:26] thing on the robot Etc so I just want to
[00:07:29] draw draw attention to a little detail
[00:07:31] here uh so I don't know if you guys can
[00:07:33] see my
[00:07:34] cursor uh so Sean my cursor is Vis
[00:07:43] visible you're muted um yes yes okay
[00:07:47] okay great okay I don't have a poter so
[00:07:49] all right um so uh so this is you know
[00:07:53] the uh the uh the you know in some sense
[00:07:57] this is also defining the bman operator
[00:07:58] and this is second the second term in
[00:08:00] the in the bman operator is an
[00:08:02] expectation of the value function and
[00:08:05] this term is really the next stage so
[00:08:07] this expectation is with respect to next
[00:08:09] state so that is written up here so this
[00:08:11] is just a re restatement of that except
[00:08:14] that now we are taking into account that
[00:08:16] the next state is coming from some
[00:08:18] simulation model or a generative model
[00:08:21] as now it's being called and so s is
[00:08:23] such a simulation function and you know
[00:08:26] given this state X and action U and some
[00:08:28] noise Omega
[00:08:30] SX s of X U Omega gives us the next
[00:08:34] state and since the randomness is Omega
[00:08:37] then this expectation is with respect to
[00:08:39] Omega so so the the point of this uh
[00:08:42] point the point I'm trying to make here
[00:08:44] is that you know once you make this
[00:08:45] observation you can immediately see that
[00:08:48] you know you can uh use uh you know you
[00:08:51] can generate uh samples from a simulator
[00:08:55] uh and you can plug the plug those
[00:08:57] samples in uh in in place of the
[00:09:00] expectation and do a a sample average
[00:09:02] approximation and that is a one very
[00:09:05] simple way of doing value
[00:09:08] iteration all right so uh like I said so
[00:09:11] the focus of this talk is on the setting
[00:09:16] where both the state space and the
[00:09:19] action space are
[00:09:20] continuous if the state space is
[00:09:22] continuous and just for the you know for
[00:09:25] now let's assume that the action space
[00:09:27] is finite then uh we could do something
[00:09:30] like what I just said which is uh you
[00:09:32] know just do sample average
[00:09:33] approximation inside development
[00:09:34] operator and then you're essentially
[00:09:36] doing a empirical variant of value
[00:09:38] iteration uh something that we have
[00:09:40] studied before uh it seems to work quite
[00:09:43] well numerically in many many context uh
[00:09:46] there is of course a problem that you
[00:09:48] know it still doesn't scale with the
[00:09:49] state space size uh and of course for
[00:09:53] Contin State spaces you need to do uh
[00:09:55] something else so you can do combine
[00:09:56] that this idea with function
[00:09:58] approximation but the the diff there's
[00:10:01] an additional difficulty arises when you
[00:10:03] try to uh extend this to uh continuous
[00:10:07] action spaces namely that in each
[00:10:09] iteration you need to maximize over you
[00:10:13] and uh you know you don't have any
[00:10:16] derivatives or anything that are
[00:10:17] available here so so it's not really
[00:10:20] possible to actually uh do any kind of
[00:10:22] optimization so one possibility is that
[00:10:25] you know suppose you you have a compact
[00:10:28] action space uh you know you can just
[00:10:30] take some samples and take the empirical
[00:10:33] Max and plug that in and uh you know and
[00:10:36] then uh you know you can still plug in a
[00:10:40] sample average approximation for the
[00:10:42] expectation in the bman
[00:10:43] operator uh so that uh works but it's
[00:10:47] not going to scale and particularly when
[00:10:49] you go to High dimensional spaces it's
[00:10:50] not going to scale you can do sampling
[00:10:52] in smarter ways you can uh you can U you
[00:10:56] can use Monte Carlo research type
[00:10:58] methods
[00:10:59] sampling um that definitely helps but
[00:11:02] again as you go to High dimensional
[00:11:04] action spaces that again runs into
[00:11:08] difficulties so now value iteration is
[00:11:11] of course only one type of dynamic
[00:11:12] programming algorithm uh you know policy
[00:11:15] iteration and actor critic types uh
[00:11:18] Frameworks are other and so in the actor
[00:11:21] critic architecture which is really
[00:11:22] generalized policy iteration uh so
[00:11:25] what's happening is that um uh and this
[00:11:28] is a very classical architecture so what
[00:11:30] happens in such an architecture is that
[00:11:33] you uh you introduce a function
[00:11:35] approximation architecture for the Q
[00:11:38] value function which is not not too
[00:11:40] different from the the value function I
[00:11:41] was talking about so far and you also
[00:11:44] introduce a function approximation
[00:11:46] architecture for the policy uh for the
[00:11:49] policy and that's called the actor and
[00:11:52] in policy iteration type algorithm you
[00:11:54] have a policy evaluation step and then
[00:11:56] you have a policy Improvement step and
[00:11:58] now in the act critic architecture you
[00:12:00] know essentially that's what you do so
[00:12:01] you first you do the policy you first
[00:12:03] you do policy evaluation then you do
[00:12:04] policy Improvement and you know and you
[00:12:08] keep on going until you have convergence
[00:12:10] if you have
[00:12:11] convergence so um maybe uh you might be
[00:12:14] useful to kind of just elaborate on you
[00:12:17] know things a bit uh particularly since
[00:12:20] I will need uh to to use some of this
[00:12:23] notation so let's say that Q is the the
[00:12:26] current uh Q value function that we have
[00:12:29] then the operator G Pi is the policy
[00:12:32] evaluation operator with the fixed
[00:12:33] policy Pi that you know that is defined
[00:12:36] like this so it's essentially just the
[00:12:38] reward function plus gamma times
[00:12:39] expectation of the Q value function and
[00:12:42] the action is taken according to the
[00:12:44] policy Pi so so again you know as I said
[00:12:47] before there's an expectation here and U
[00:12:50] as U you know Alex also talked about
[00:12:52] this is a very you know we've been doing
[00:12:54] sample average approximation forever so
[00:12:57] we can do that here as well and so the
[00:13:01] policy evaluation operator will become
[00:13:02] an empirical policy evaluation operator
[00:13:05] and uh this is very simple idea I think
[00:13:07] this is you know in some sense it can
[00:13:10] also be regarded as being
[00:13:12] unavoidable uh but from a operator
[00:13:15] theoretic point of view something
[00:13:16] interesting has happened which is that a
[00:13:18] deterministic operator has now become a
[00:13:20] random operator and we don't really know
[00:13:23] and given that this is embedded in some
[00:13:25] algorithm where this is being iterated
[00:13:27] over and over again we don't know what's
[00:13:28] going to happen
[00:13:30] all right so this is one sort of you
[00:13:32] know the so what we're going to do is
[00:13:34] we're going to use the actor critic
[00:13:36] architecture and uh like I was saying
[00:13:39] the the both the actor and the critic
[00:13:42] the function approximation architecture
[00:13:43] I mean you can pick your favorite but
[00:13:45] they could be neural networks as well
[00:13:47] and neural networks are Universal
[00:13:49] function approximator so you know that's
[00:13:51] one attractive thing about them uh but
[00:13:54] uh you know it can be hard to make I
[00:13:57] mean you know you can make things work
[00:13:59] that's not really a problem that is
[00:14:01] really the main thing that is attractive
[00:14:03] about neural networks uh but it can be
[00:14:05] hard to prove results so what one could
[00:14:08] do and this is again not a new idea I
[00:14:11] mean these kind of ideas have been
[00:14:12] around for you know at least couple of
[00:14:15] decades um uh so what one could do is
[00:14:19] that one could uh so Alpha here for
[00:14:23] example in the policy Network the AL
[00:14:25] Alpha here are the weights in the very
[00:14:27] last layer of the neural network and
[00:14:29] Theta are represent the all the other
[00:14:32] weights and what one could do is one
[00:14:34] could pick all the other weights
[00:14:35] randomly and just only optimize over the
[00:14:38] alpha weights and so for example uh you
[00:14:41] know so you have Theta J so the Theta J
[00:14:43] is just one sample of the the weights in
[00:14:47] all layers except the last one and you
[00:14:50] get a number of such samples each such
[00:14:52] sample gives you a basis function s of X
[00:14:55] dependent on Theta J and then you just
[00:14:58] given it you know the the the alphas uh
[00:15:02] in the last layer are are to be to be
[00:15:04] determined I mean they're deterministic
[00:15:06] so Pi of X has you know such a linear
[00:15:09] function approximation form right and
[00:15:11] you can do the same thing on the the
[00:15:13] critic side so there is a neural network
[00:15:15] beta are the weights on the very last
[00:15:17] layer and then the V Theta are represent
[00:15:20] all the other weights and then you just
[00:15:22] pick them randomly and uh and then you
[00:15:26] you know QX comma U has uh this linear
[00:15:30] uh you know function approximation form
[00:15:32] except the thing to keep in mind is that
[00:15:34] these basis functions are being picked
[00:15:37] randomly so turns out that if you try to
[00:15:39] do this then you uh you know you can
[00:15:43] connect this to uh you know doing
[00:15:47] randomized function approximation in
[00:15:49] reproducible kernel Hilbert spaces and
[00:15:52] reproducible kernel hbert spaces I mean
[00:15:54] they are very nice spaces to work with
[00:15:55] they're also uh uh you know Universal
[00:15:58] function
[00:15:59] approximators uh priority Neal networks
[00:16:01] I mean those are the things that were in
[00:16:03] Vogue and but you know they do have
[00:16:06] difficulty scaling up uh
[00:16:08] computationally but you know our goal
[00:16:11] here is to both have something that is
[00:16:15] sort of computationally simple at the
[00:16:17] same time we would like to be able to
[00:16:18] prove that it's going to
[00:16:20] work okay and just to I just want to
[00:16:23] emphasize this is not a new idea
[00:16:25] basically what we're doing over here is
[00:16:27] that we are putting together number
[00:16:28] number of very simple ideas that have
[00:16:31] been around or are not difficult to
[00:16:34] imagine right uh and we basically
[00:16:37] putting them together and uh we're
[00:16:38] trying to see if we can construct an
[00:16:41] algorithm that of course not only would
[00:16:42] would like to be able to prove something
[00:16:44] about it but that actually works I mean
[00:16:46] that's really the goal that it should
[00:16:48] work and uh so now let's see if we can
[00:16:52] put all the pieces together so the first
[00:16:54] piece here is the first step here is the
[00:16:56] policy evaluation step and what you do
[00:16:59] is you uh get some samples uh uh from
[00:17:03] the product of the state and action
[00:17:04] spaces so there are NQ such samples and
[00:17:07] then you do the empirical policy
[00:17:09] evaluation the way I just explained to
[00:17:11] you before you know in the you use the
[00:17:14] empirical policy evaluation uh uh so the
[00:17:17] policy evaluation operator and then just
[00:17:19] plug in Sample average
[00:17:21] approximation uh you know from the s
[00:17:23] from the simulations for the expectation
[00:17:26] and then you you know you're basically
[00:17:27] using a random operator so that that's
[00:17:29] what gives you Q hat and you get that at
[00:17:32] these uh NQ points and then after that
[00:17:36] you just do you know function fitting L2
[00:17:38] function fitting and that's it and uh
[00:17:42] from this function fitting you know
[00:17:43] you're going to get a function Q hat
[00:17:46] that is going to correspond to the
[00:17:47] policy p k that was used to generate the
[00:17:50] actions and of course that's going to
[00:17:53] have uh to have this kind of you know
[00:17:55] linear uh uh function approximation form
[00:17:58] so beta J some basis functions where
[00:18:00] where Theta J are are
[00:18:02] random and the thing to keep in mind is
[00:18:05] that you know these These are these uh
[00:18:07] the weights are chosen randomly in every
[00:18:10] iteration so they are changing they're
[00:18:11] not they're not you know they're not
[00:18:13] fixed it's not like you choose them once
[00:18:15] and you fix them and I think that also
[00:18:18] provides some sort of uh robustness
[00:18:20] though this probably needs to be
[00:18:23] Quantified but you know if you somehow
[00:18:25] end up with a bad sample of fas you know
[00:18:28] in the beginning you're not stuck with
[00:18:29] them because you are doing this in every
[00:18:32] iteration all right so that was the
[00:18:34] policy evaluation step so at the end of
[00:18:36] this step so what you have is that for a
[00:18:39] given policy you have some evaluation of
[00:18:43] its corresponding Q value function as to
[00:18:45] how good that is and then the then uh
[00:18:48] the the second step is the policy
[00:18:49] Improvement step just like in a standard
[00:18:52] policy policy iteration uh you get
[00:18:55] samples of the state n Pi samples
[00:18:58] According to some distribution uh from
[00:19:00] the state space and then uh this is the
[00:19:04] Q uh qk hat the function that we just
[00:19:06] computed in the policy evaluation step
[00:19:09] and we just plug that in here and uh
[00:19:13] this uh this thing in here is the the
[00:19:16] policy that you're going trying to
[00:19:17] optimize over because you want to find
[00:19:18] an improved policy so the point is that
[00:19:21] you you use the current estimate of the
[00:19:23] Q value function and try to come up with
[00:19:26] an improvement uh just like you do in uh
[00:19:28] uh policy policy iteration and uh it
[00:19:32] essentially amounts to just finding
[00:19:34] these Wes Alpha so you know you can use
[00:19:37] some gradient descent algorithm your
[00:19:39] favorite gradient descent algorithm to
[00:19:40] solve this so numerically it's all very
[00:19:42] simple and that's it I mean these are
[00:19:44] the the two steps in the this algorithm
[00:19:46] which we call grand
[00:19:48] pa uh so um as you can see I mean it
[00:19:52] involves some sampling um you know L2
[00:19:56] function
[00:19:57] fitting um and that it and the key
[00:19:59] ingredients are in actor critic
[00:20:01] architecture and uh uh function
[00:20:04] approximation but in a you know with a
[00:20:06] shallow so again that the other thing I
[00:20:07] would like to emphasize is that we're
[00:20:09] not using a deep neural network this is
[00:20:11] with the shallow neural network all
[00:20:14] right so like I said you know the part
[00:20:16] of the reason for doing this is uh you
[00:20:18] know can we prove something here and uh
[00:20:21] it turns out that indeed we can and
[00:20:24] there's you know I know this is a little
[00:20:26] bit dense there are a number of things
[00:20:28] here but
[00:20:29] um so NQ and N Pi are the samples of the
[00:20:33] states and actions something that I
[00:20:35] talked about in the two steps m is the
[00:20:38] number of samples of the next state that
[00:20:40] you need in doing the sample average
[00:20:42] approximation and JQ and JPY are the
[00:20:45] samples of the weights of the neural
[00:20:47] network uh for the the actor Network and
[00:20:50] the critic Network and turns out that if
[00:20:54] uh you know these uh these uh these
[00:20:57] numbers are large enough and you do
[00:20:59] enough number of iterations then the the
[00:21:02] L1 error in your Q value function is
[00:21:04] small with high probability and you know
[00:21:07] so so one is able to get a non-
[00:21:08] asymptotic result and of course it
[00:21:10] implies asmic
[00:21:12] convergence um so so that's um yeah so
[00:21:17] that's that's the that's the main result
[00:21:19] theoretically speaking um something that
[00:21:22] I would like to point out here is that
[00:21:24] it is universal in the sense that you
[00:21:27] know it's a continuous uh mdp so uh we
[00:21:31] are going to need some regularity
[00:21:33] conditions to be able to make progress
[00:21:34] so we need some sort of lip shits
[00:21:37] continuity uh on the transition function
[00:21:40] and the reward function Etc but other
[00:21:42] than that we there is no assumption on
[00:21:44] the structure of the mdp that is being
[00:21:46] made and like I said before it is you
[00:21:49] know computationally quite simple I mean
[00:21:51] there's a you know a lot of sampling
[00:21:53] going on here for sure but uh you know
[00:21:57] uh but and and uh one probably has to
[00:22:00] run one has to run uh you know gradient
[00:22:02] descent algorithm uh in in in each
[00:22:05] iteration of the the algorithm but that
[00:22:07] that's pretty much it and uh I have not
[00:22:11] shown the constants but all the
[00:22:12] constants are known and the dependence
[00:22:14] on the key parameters is shown here and
[00:22:16] the dependence on Epsilon ends up being
[00:22:19] 1 by Epsilon Square which is quite
[00:22:20] typical and then the dependence on Delta
[00:22:22] is log of 1 by Delta which is also quite
[00:22:24] typical I mean this typically comes from
[00:22:26] the concentration inequalities that you
[00:22:27] use
[00:22:29] uh and the dependence on gamma um you
[00:22:32] know that also is sort of
[00:22:35] uh that's uh that can also be inferred
[00:22:39] here um I'm not sure if it is possible
[00:22:41] to improve upon that uh but yeah that's
[00:22:44] but we do have uh the
[00:22:46] dependence okay so this is the uh so
[00:22:51] this is theorem and maybe a quick word
[00:22:54] about uh the proof sketch and then I
[00:22:56] will talk about uh numerical performance
[00:22:58] so actually it turns out that the proof
[00:23:00] is not that difficult and uh there's you
[00:23:03] know a number of steps so first step is
[00:23:05] you just do sort of one step analysis of
[00:23:08] policy evaluation and policy Improvement
[00:23:10] uh which is actually turns out to be not
[00:23:12] difficult at all and once you do that
[00:23:15] then you should look at each iteration
[00:23:17] of the entire algorithm which is the
[00:23:19] policy evaluation and the policy
[00:23:20] Improvement step as a random operator
[00:23:23] which you can argue is probabilistically
[00:23:25] Contracting in some sense and you know
[00:23:28] there is a very precise sense in which
[00:23:30] that that uh that uh which is implied uh
[00:23:34] and then once you do that then you can
[00:23:38] uh you can construct a stochastic
[00:23:40] dominance argument in the sense that you
[00:23:42] can construct a mark of chain that
[00:23:44] dominate the error process that you want
[00:23:46] to B and then the analysis just uh
[00:23:49] reduces to analyzing this Mark of chain
[00:23:52] and you know convergence and Sample
[00:23:54] complexity everything comes from that
[00:23:55] Mark of chain and the mark of chain is
[00:23:56] also very easy to to constr constuct so
[00:23:59] there's a very natural construction of
[00:24:00] the markco chain so this is sort of the
[00:24:02] essense of the argument I mean for those
[00:24:04] of you who have seen you know uh some of
[00:24:07] my prior work I mean you know it's um
[00:24:09] some details are different but uh you
[00:24:11] know it essentially leverages you know
[00:24:13] uh these uh many of the same sort of you
[00:24:17] know uh analytical Machinery that we
[00:24:20] developed earlier which is a nice thing
[00:24:22] you know it's means that you know it's
[00:24:24] uh the proof is not difficult to
[00:24:27] operationalize all right
[00:24:28] the big question is does it
[00:24:31] work so this is on uh the the quop robot
[00:24:34] that I showed you it's in an environment
[00:24:36] called Minar uh in
[00:24:39] pet and there are four things that are
[00:24:42] being shown here so the last one is this
[00:24:44] is some random search going on and it
[00:24:46] doesn't work I mean I you know that
[00:24:48] would be at least that's what we would
[00:24:50] expect right that there random search is
[00:24:53] not going to work on such complicated
[00:24:54] problems the other two are uh so the one
[00:24:58] in green is something called ddpg Deep
[00:25:01] deterministic policy bit algorithm which
[00:25:02] is in some sense state-of-the-art policy
[00:25:04] bit algorithm and it works quite well
[00:25:08] and then uh the the one in red is po
[00:25:11] proximal policy optimization which is
[00:25:13] probably the best uh you know uh DL
[00:25:18] algorithm uh for continuous control uh
[00:25:20] as at least as far as we know and uh the
[00:25:24] one in blue is our algorithm brand Paul
[00:25:28] and and uh and what you can see is that
[00:25:31] you know it seems to have at least we
[00:25:33] can say that its performance is sort of
[00:25:35] comparable to
[00:25:36] poo and uh it does take more time so
[00:25:39] computation so it turns out that rall
[00:25:41] ends up doing well runtime is more for
[00:25:44] Randall than for po I mean poo is a
[00:25:47] really good algorithm very well designed
[00:25:49] but I think some of it has to do with
[00:25:50] the implementation as well uh you know
[00:25:52] PP is you know very naturally uses
[00:25:54] paralyzation and gpus so runtime is
[00:25:57] pretty fast whereas with Randall you
[00:25:59] know our the code that we have our code
[00:26:03] is pretty amateurish as you can imagine
[00:26:05] so I think there can be some gains that
[00:26:07] can happen by by having a sort of you
[00:26:10] know better implementation okay so this
[00:26:13] is what it looks like but again the
[00:26:16] question Still Remains does it actually
[00:26:18] work before I get to that I think I just
[00:26:20] one more thing I want to say is a couple
[00:26:22] of things I want to say is
[00:26:24] that when in problems like this reward
[00:26:27] what's called reward shaping is really
[00:26:29] uh you know sometimes is the bottom like
[00:26:31] meaning that you want the robot to have
[00:26:34] a certain kind of you know Behavior or
[00:26:37] be able to do certain Maneuvers what
[00:26:39] reward function should you pick so that
[00:26:41] you can enable that and lot of effort is
[00:26:43] spent on that but once you do that then
[00:26:46] you know you across algorithms I mean
[00:26:49] you can use that and uh that's what we
[00:26:50] did over here the other thing I want to
[00:26:53] mention here is that you know Randall as
[00:26:55] you guys as you have seen I mean there's
[00:26:57] no there are no hyper parameters or
[00:26:59] anything right it is a very natural sort
[00:27:01] of extension of multiple ideas which are
[00:27:03] well understood and you know there's no
[00:27:05] hyper parameter tuning uh
[00:27:07] needed okay does it
[00:27:15] work okay so this required about uh you
[00:27:19] know 10 to 12 hours of training uh more
[00:27:21] than what poo required so poo can also
[00:27:23] do this I should not say that PP cannot
[00:27:25] do this ddpg is less successful which is
[00:27:28] so evident in the in the plot that I
[00:27:29] showed you uh but uh I mean at least you
[00:27:33] know so uh this so I think this is this
[00:27:38] is really the the proof of the the
[00:27:39] pudding is in the eating as they say so
[00:27:41] I think uh you know theum and the plots
[00:27:45] about rewards and all that I think those
[00:27:46] are irrelevant once you see this okay uh
[00:27:51] so with that I think I'm probably out of
[00:27:53] time uh so I'll just conclude that uh
[00:27:55] you know what I presented is is um is uh
[00:28:00] belongs to a class of algorithms we've
[00:28:02] been calling empirical algorithm and
[00:28:04] these are really you know algorithms
[00:28:05] meant for uh learning with batch data or
[00:28:09] or with the generative models uh these
[00:28:11] are uh simple they in in they are
[00:28:15] Universal in the sense that you don't
[00:28:17] need any sort of assumptions on the
[00:28:19] structure of the model and they have
[00:28:22] reasonably good numerical performance uh
[00:28:25] they do need a generative model so in in
[00:28:27] that sense they a little bit far from
[00:28:29] the goal of uh reinforcement learning in
[00:28:31] that you know that you don't have you
[00:28:34] know you you have learning complete
[00:28:37] that's fully
[00:28:39] online uh so one could argue that the
[00:28:42] performance guarantees are a little bit
[00:28:43] weak because you get convergence in
[00:28:45] probability and then you know you know
[00:28:47] with high probability bounds um but uh
[00:28:51] you know once actually once you ask for
[00:28:53] non-asymptotic performance guarantees
[00:28:54] that's what you're going to get anyways
[00:28:56] but they do have good numerical
[00:28:57] performance at least comparative
[00:28:58] numerical
[00:29:00] performance uh and yeah so the the the
[00:29:03] ideas behind the algorithm are simple
[00:29:05] and I think
[00:29:06] the there is some hard work uh in in the
[00:29:09] in the analysis but I think once that is
[00:29:11] done then the algorithm is pretty simple
[00:29:14] and uh so so this is done in what uh the
[00:29:17] minitar environment on pet so what we're
[00:29:20] trying to do now is put this on an
[00:29:23] actual quadal robot But first you know
[00:29:25] we cannot do training on the on the
[00:29:27] physical robot so we we we have we
[00:29:30] working with a colleague to to train you
[00:29:34] know a very realistic model of the
[00:29:36] actual robot and if it works in the
[00:29:38] simulator then we'll put it on the on
[00:29:40] the physical robot so that's what we
[00:29:42] what's going on right now but uh it's
[00:29:45] surprising once you at least for people
[00:29:48] like me who do theory that there is such
[00:29:49] a gap between Theory and trying to make
[00:29:52] something work in practice you know
[00:29:54] there are multiple steps in the in this
[00:29:55] process but it's a fun process all all
[00:29:58] right thank you very
[00:30:00] much awesome thank you Rahul so so here
[00:30:05] here's here's what I think we should do
[00:30:06] is um since I cut off uh questions for
[00:30:09] the previous speaker uh I'll open up
[00:30:12] questions for either speaker but let's
[00:30:14] give
[00:30:15] Rahul uh I'll give him priority at the
[00:30:19] moment just because his slides are up
[00:30:20] and all that so any
[00:30:23] questions I'll open up my chat box
[00:30:32] um there are two questions by gly and
[00:30:35] Chaba in the Q&A chat box I'm having
[00:30:39] trouble finding it oh there it is there
[00:30:41] it is okay so um then so
[00:30:46] [Music]
[00:30:49] um oh so so GGO asks are you doing
[00:30:53] anything fancy for exploration are there
[00:30:56] any issues there yeah so actually a very
[00:30:58] excellent point so actually we we uh as
[00:31:00] we're trying trying to translate this to
[00:31:03] um uh you know to to having it work on a
[00:31:07] real robot so that's one of the
[00:31:08] challenges uh
[00:31:09] because um I mean you have to be data
[00:31:12] efficient right and so there is an issue
[00:31:15] of exploration so in the minitar that
[00:31:18] did not come up we did not have to do
[00:31:20] anything fancy but as we working with
[00:31:22] the more sophisticated model uh uh you
[00:31:25] know of a actual qual robot so we we are
[00:31:29] having to do some exploration so there
[00:31:30] is you know some entropy regularization
[00:31:33] stuff that we are trying to do yes okay
[00:31:35] cool and this Chaba has a sequence of
[00:31:38] questions and I'm going to start at the
[00:31:39] bottom since I had the same question
[00:31:42] about the benefit of the policy
[00:31:45] Network
[00:31:46] [Music]
[00:31:48] um uh okay
[00:31:51] sorry start the first maybe I'll start
[00:31:53] with the first one so is there an
[00:31:55] advantage using stochastic dominance
[00:31:57] arent over yeah good okay you go you go
[00:32:01] yeah so no it is just that it just
[00:32:04] really simplifies the argument uh I
[00:32:07] think otherwise it becomes um you know
[00:32:09] just too complicated uh but this is not
[00:32:11] the only way to do it I'm sure that
[00:32:13] there are other ways of doing
[00:32:15] it then the bound did not show
[00:32:18] dependence on the dimension of the state
[00:32:20] and action spaces since it was
[00:32:22] emphasized that this works no matter the
[00:32:25] mdp uh dependence will be exponential in
[00:32:28] the worst case sense uh yeah you know
[00:32:33] uh so there is definitely continuity
[00:32:36] assumption uh that we have to make that
[00:32:38] as I mentioned so you need some lip
[00:32:39] ships continuity assumption on the
[00:32:41] transition uh function or the transition
[00:32:43] probabilities and the reward
[00:32:45] function uh I think uh uh there is no
[00:32:51] explicit dependence on the dimension but
[00:32:54] it is happening implicitly through the
[00:32:57] you know through some other way you know
[00:32:59] maybe the elpus uh
[00:33:01] constants uh but yeah something we have
[00:33:04] to look at but we haven't gotten around
[00:33:06] to kind of understanding that aspect but
[00:33:09] as far as I can recall uh there is no
[00:33:12] you know dependence on the on the on the
[00:33:14] on the dimension but it is implicit the
[00:33:16] dependence is implicit
[00:33:19] somewhere then what is the benefit of
[00:33:21] the policy Network oh the why not just
[00:33:24] kernels for example yeah oh so well I
[00:33:29] interpret this question slightly
[00:33:30] differently so the the motivation for us
[00:33:32] trying to do this was when you want to
[00:33:35] go to uh continuous action spaces you
[00:33:38] know and if you you know um you uh so
[00:33:44] you know so so you can't like I
[00:33:46] mentioned you you know how how are you
[00:33:47] going to do that optimization right so
[00:33:49] one thing is you can do sampling uh you
[00:33:52] know uh you can you know do adaptive
[00:33:54] sampling you can try to use Monte Carlo
[00:33:57] research kind of things right but uh
[00:33:59] that also we tried that we actually have
[00:34:02] a paper prior to this in in a paper
[00:34:04] prior to this that's what we were doing
[00:34:06] but we could not make that work on the
[00:34:08] robot uh it was just uh for some reason
[00:34:12] you know computational scalability as
[00:34:14] well as other things it did not work and
[00:34:16] then we thought that maybe we just need
[00:34:18] to do function approximation for the
[00:34:20] policy also and uh and we decided to use
[00:34:24] uh neural networks uh so why neural NW
[00:34:27] work so that um so
[00:34:31] again uh uh I'm not sure if I can give
[00:34:34] definitive answer like but I can explain
[00:34:38] the motivation I guess but you know why
[00:34:41] one not one why not the other I I'm not
[00:34:42] sure I can say um so um we you know
[00:34:48] prior to this we have uh done function
[00:34:51] approximation um like I mentioned in the
[00:34:53] rchs space and we were not able to make
[00:34:56] it scale
[00:34:58] so again there was it was not working it
[00:35:00] was you know partly a scaling issue
[00:35:02] partly just not working on on more
[00:35:04] complicated problems and the other was
[00:35:07] computational reason that once you put
[00:35:09] things into a neural network you know
[00:35:11] you can use sort of you know you know
[00:35:14] you can have you know you don't need to
[00:35:15] program so that you can use the GPU that
[00:35:18] was really you know a key motivation
[00:35:20] actually and then we began to think
[00:35:21] about okay if you're going to use neural
[00:35:23] networks we still want to prove a
[00:35:24] theorem how is that going to happen and
[00:35:26] of course you know we were already doing
[00:35:29] randomization of various kinds so we
[00:35:30] thought okay you know in ours when we do
[00:35:32] function approximation again we are
[00:35:34] using some you know sampling idea and
[00:35:36] randomized function approximation we
[00:35:38] thought okay why not do that here as
[00:35:40] well so that I don't know if this answer
[00:35:43] this answers the question I mean I I'm
[00:35:45] explaining my motiv I'm I'm saying what
[00:35:47] our motivation is I I don't know if you
[00:35:49] know it is not to say that it this
[00:35:51] cannot be done in another
[00:35:53] way and our Focus was very much on you
[00:35:57] know at least one thing uh that was
[00:35:59] driving us was you know what can we make
[00:36:01] that'll computationally work both in
[00:36:03] terms of like runtime as well as it'll
[00:36:06] work know like what whatever comes out
[00:36:08] whatever policy comes out will actually
[00:36:10] work on on the on uh on the minute or
[00:36:15] Robot
[00:36:17] cool cool so um any other questions for
[00:36:20] H out
[00:36:24] there um um so I have questions again
[00:36:28] both moner and Alex but maybe I'll I'll
[00:36:32] start with Alex in the reverse
[00:36:35] order um so Alex you you uh thank you
[00:36:38] for discussing the notion of risk
[00:36:40] measures in uh multi-stage stochastic
[00:36:43] programming so um I think um so since we
[00:36:47] we didn't have enough time so I I I
[00:36:49] think I I still hope to get a better
[00:36:52] understanding about what's the correct
[00:36:55] notion of risk measure in multistage to
[00:36:58] has oranization so I I think ium papers
[00:37:01] was very different set of definitions of
[00:37:05] risk measures some involving time
[00:37:07] consistency some do not so um so I ask
[00:37:10] my question is in your mind what will be
[00:37:12] the right way or the most reasonable way
[00:37:14] to think about risk measures and also
[00:37:16] when we Define risk measures it seems
[00:37:18] like some risk measures are defined to
[00:37:20] make analysis straightforward but is
[00:37:23] that the way to go or or maybe this is
[00:37:26] fundamentally a hard just hard question
[00:37:28] so I I just want to hear your view on
[00:37:33] this I hope he's
[00:37:35] here oh we lost
[00:37:42] him H that's too bad oh yeah oh that's
[00:37:45] too bad
[00:37:47] yeah okay anybody else want to answer
[00:37:50] that one no I think I think I think he's
[00:37:53] he's here and uh he's probably muted so
[00:37:56] I think the the host can unmute uh I I
[00:37:59] just I just asked him to unmute
[00:38:02] yeah but you can unmute him yourself uh
[00:38:06] can I I think I'm not the host then I I
[00:38:09] cannot I can only ask to unmute
[00:38:12] him I thought we were the
[00:38:20] hosts how
[00:38:23] funny yeah also I think mother has
[00:38:26] dropped from the line
[00:38:32] okay he mo are you still
[00:38:37] there send us to chat if you're if
[00:38:39] you're there um okay that
[00:38:44] that's yeah ra do you want to answer a
[00:38:47] question
[00:38:50] sure yeah about risk measures sorry oh
[00:38:54] risk
[00:38:55] measures actually you know something
[00:38:56] about that yes okay so could you repeat
[00:38:59] the question um oh my question is that
[00:39:01] there seems to be like a a variety of
[00:39:04] definitions of risk measures for
[00:39:06] multistage programming right so I'm sure
[00:39:09] like you have seen some like we all have
[00:39:11] seen various definitions do do have a
[00:39:13] sense about like like what should be the
[00:39:16] right definition or is or how to how how
[00:39:20] to think about risk matters in
[00:39:23] general um I'm not an expert but so I
[00:39:26] can share my limited knowledge on this
[00:39:29] topic I think uh so as you probably know
[00:39:33] that um uh you know as Alex was
[00:39:36] referring to as well right so it started
[00:39:38] with the war you know value at risk
[00:39:40] measure and then carar it's also called
[00:39:43] a you know conditional value at risk so
[00:39:45] those are in practice those are kind of
[00:39:47] risk measures that are you know quite
[00:39:49] you know used very well but uh in the
[00:39:52] last uh 15 or so years there's been an
[00:39:55] attempt by INF by Alex Shapiro and then
[00:39:59] also by other people to develop a sort
[00:40:00] of exatic approach to to risk and uh uh
[00:40:06] so I mean it really depends on your
[00:40:08] preference I mean there are you know
[00:40:10] different exams and then you end up with
[00:40:11] different risk measures when you go to a
[00:40:13] dynamic setting then I think things
[00:40:15] become a lot more difficult because the
[00:40:18] moment you consider risk or you know
[00:40:20] which is not a risk neutral measure then
[00:40:23] the the um the the policy are going to
[00:40:27] be history dependent right and uh that
[00:40:31] really make you know it makes things
[00:40:33] very challenging so people have come up
[00:40:35] with their you know Notions of dynamic
[00:40:38] dynamic risk measures and Mark of risk
[00:40:40] measures and all that
[00:40:42] but it all really depends on your
[00:40:45] application and whether those are
[00:40:46] relevant so that's all I can
[00:40:50] say oh by the way I think Chaba has more
[00:40:53] questions for you in the in the chat box
[00:40:55] but probably we don't have time to
[00:40:57] answer them like now like people need a
[00:41:00] break but can you type your answers in
[00:41:03] the chat box so we can see
[00:41:05] them oh I think I answered so I can see
[00:41:08] three I answered all of them there are
[00:41:11] more
[00:41:12] questions oh no no no didn't answer them
[00:41:17] okay cool yeah well there is there is
[00:41:18] actually one more there
[00:41:21] um but uh yes so I think I think we will
[00:41:25] have to take a bit of a break so we'll
[00:41:26] return in just 12 minutes so so we just
[00:41:30] have a very brief Break um and uh look
[00:41:33] forward to
[00:41:35] rebooting thank you okay okay thank you
[00:41:39] thanks thanks to all the speakers
