---
title: "Web Graphs and P2P"
date: "2004-01-13T01:38:00+07:00"
lastmod: "2011-05-10T20:33:01+07:00"
type: "post"
url: "/2004/web-graphs-p2p/"
description: "Web Graphs All people in computer science and some fields of engineering (e.g. industrial engineering?) are very familiar with “Graphs” — those nodes and arcs. And, actually, we can represent the web as a [huge] graph. Where node=webpage, arc=(hyper)link. From this representation, it gives us a way "
categories: ["informatics", "internet"]
tag: ["graphs", "p2p", "search-engines", "web", "whatwewant"]
textlang: "en"
wpid: 37
---
**Web Graphs**

All people in computer science and some fields of engineering (e.g. industrial engineering?) are very familiar with “Graphs” — those nodes and arcs. And, actually, we can represent the web as a \[huge\] graph. Where node=webpage, arc=(hyper)link.

From this representation, it gives us a way to understand the characteristic of the web better (as we do well with normal graphs).

[graph structure in the web](http://www9.org/w9cdrom/160/160.html) \| [web graph](http://www.dcs.kcl.ac.uk/staff/ccooper/store/ESA2001.ps "C. Cooper, A. M. Frieze. (2001), A general model of web graphs") \| [more on web graph](http://www.dcs.kcl.ac.uk/staff/ccooper/papers.html)

**Peer-to-Peer**

Talking about representing document/site as a node in a graph, [Peer-to-Peer](http://www.openp2p.com/ "P2P") people already done this since their early day.

Making it more relevant to this blog, one of the most popular P2P application is obviously an IR-like system — search for mp3 song or DivX movie, given a title or singer’s name.

Searching things on P2P network is not like a traditional search engine searching its database (which is a snapshot of a part of the web at a particular time, collected by spiders/web spiders).

Rather, the P2P search visits each node, doing searching in that node, jump to other node .. and so on, in “real time”. Clearly, it is impossible to visits every nodes in the network, there are just too many nodes out there. To decide which node it will make a visit or not, it needs a routing algorithm.

As a result, we can simplified a search problem in P2P network as a routing problem, loosely.

\[ to find a document is to find a way to that document \]

There are even some more advance routing algorithm that use [semantics](http://citeseer.nj.nec.com/garcia02semantic.html "Arturo Crespo, Hector Garcia-Molina (2002), Semantic Overlay Networks for P2P Systems")!

**bact’:** I used to think about using NLP with P2P routing. But it just “thinking” anyway, never do .. lazy me 🙁
