---
title: "CFLAGS for Pentium M"
date: "2004-05-11T05:00:00+07:00"
lastmod: "2011-05-05T12:26:18+07:00"
type: "post"
url: "/2004/cflags-for-pentium-m/"
description: "Some sez Pentium M is architecturally more close to Pentium 3, with few additional features from Pentium 4, and big L2 cache. Thus, in general, gcc optimization should treat it as Pentium 3. In other words, *NOT* Pentium 4. But some also reported that they got a good experience with -march=pentium4."
categories: ["computer"]
tag: ["gcc", "how-to", "programming"]
textlang: "en"
wpid: 106
---
[Some](http://groups.google.com/groups?hl=en&lr=lang_en&ie=UTF-8&oe=UTF-8&safe=off&selm=1afyv-8hH-13%40gated-at.bofh.it) sez Pentium M is architecturally more close to Pentium 3, with few additional features from Pentium 4, and big L2 cache. Thus, in general, gcc optimization should treat it as Pentium 3. In other words, \*NOT\* Pentium 4.

But some also reported that they got [a good experience](http://groups.google.com/groups?q=best+pentium+cflags&hl=en&lr=lang_en&ie=UTF-8&oe=UTF-8&safe=off&selm=c4i0am%242iqhp4%241%40ID-195945.news.uni-berlin.de&rnum=13) with -march=pentium4.

Meanwhile, Intel website [suggests -mcpu=pentium4](http://www.intel.com/software/products/compilers/clin/docs/ug/lin1035.htm) for Pentium M. But that’s probably only for its own C++ compiler (ICPC) ?

And seems like the [new gcc](http://gcc.gnu.org/ml/gcc-patches/2004-02/msg01328.html) (may be after 3.3.3 or 3.4) will support “pentium-m”.

[Gentoo CFLAGS Central](http://forums.gentoo.org/viewtopic.php?t=5717)  
[gcc’s Intel 386 and AMD x86-64 Options](http://gcc.gnu.org/onlinedocs/gcc-3.4.0/gcc/i386-and-x86-64-Options.html#i386%20and%20x86-64%20Options)

แล้วจะเชื่อใครดีล่ะเฮีย?

after few researches, may be i will go with this:

CFLAGS=”-pipe -O2 -march=pentium3 -mmmx -msse -msse2 -mfpmath=sse -maccumulate-outgoing-args -funroll-loops -fforce-addr -ftracer -fmove-all-movables -falign-functions=64 –param max-gcse-passes=4″
