---
title: "Coral Network"
date: "2005-05-02T15:19:00+07:00"
lastmod: "2005-05-02T15:19:00+07:00"
type: "post"
url: "/2005/coral-network/"
description: "(slightly modified from its description at Wikipedia) Coral is an open source, peer-to-peer content distribution network designed to mirror web content. Coral is designed to use the bandwidth of volunteers to reduce the load on websites and other providers of web content. To use coral, simply add .n"
tag: ["decentralization", "distributed-system", "internet"]
textlang: "en"
wpid: 726
---
(slightly modified from [its description](http://en.wikipedia.org/wiki/Coral_(network)) at Wikipedia)

[Coral](http://www.coralcdn.org/) is an open source, peer-to-peer content distribution network designed to mirror web content. Coral is designed to use the bandwidth of volunteers to reduce the load on websites and other providers of web content. To use coral, simply add **.nyud.net:8090** to the hostname in a URL. So, for, example, <http://th.wikipedia.org/wiki/CS> becomes <http://th.wikipedia.org.nyud.net:8090/wiki/CS>. The latter is known as a *coralized link*.

One of Coral’s key goals is to avoid ever creating hot spots that might dissuade volunteers from running the software for fear of load spikes. It achieves this through a novel indexing abstraction called a *distributed sloppy hash table (DSHT)*, and it creates self-organizing clusters of nodes that fetch information from each other to avoid communicating with more distant or heavily-loaded servers.
