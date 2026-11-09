---
title: "Where all the Codes come from ?"
date: "2007-02-06T12:20:00+07:00"
lastmod: "2007-02-06T12:20:00+07:00"
type: "post"
url: "/2007/where-all-the-codes-come-from/"
description: "ไปดูการศึกษาว่าโค้ดต่าง ๆ ใน FLOSS (ซอฟต์แวร์เสรี/ซอฟต์แวร์ต้นรหัสเปิด) มีที่มาจากไหนกันครับ การศึกษานี้เป็นส่วนหนึ่งของรายงานที่จัดทำโดยสหภาพยุโรป Rishab Aiyer Ghosh (November 20, 2006). Study on the: Economic impact of open source software on innovation and the competitiveness of the Information a"
tag: ["free-software-movement", "free-softwares", "open-source", "sun", "universities", "you"]
textlang: "th"
wpid: 1909
---
ไปดูการศึกษาว่าโค้ดต่าง ๆ ใน FLOSS ([ซอฟต์แวร์เสรี](http://th.wikipedia.org/wiki/Free_software)/ซอฟต์แวร์ต้นรหัสเปิด) มีที่มาจากไหนกันครับ  
การศึกษานี้เป็นส่วนหนึ่งของรายงานที่จัดทำโดยสหภาพยุโรป

Rishab Aiyer Ghosh (November 20, 2006).  
**[Study on the: Economic impact of open source software on innovation and the competitiveness of the Information and Communication Technologies (ICT) sector in the EU](http://ec.europa.eu/enterprise/ict/policy/doc/2006-11-20-flossimpact.pdf)** \[PDF\]  
the European Communities.

การศึกษานี้ ใช้ [Debian 3.1](http://en.wikipedia.org/wiki/Debian) (รุ่นปี ค.ศ. 2005) ซึ่งเป็นชุดลีนุกซ์ยี่ห้อหนึ่ง เป็นกรณีศึกษา

ตารางแรก ดูว่ามหาวิทยาลัย/ศูนย์วิจัยที่ไหน ที่มอบโค้ดให้กับ FLOSS (Debian) เยอะที่สุด  
(ผมคงเลขตารางไว้เหมือนกับต้นฉบับ เพื่อให้ง่ายต่อการอ้างอิง)  
คำว่า “Regents Of The University of California” ในตาราง คือองค์กรที่ดูแลมหาวิทยาลัยในระบบ University of California ทุก ๆ มหาวิทยาลัย (Berkeley, San Diego, …) ในตารางนี้จะนับทั้งหมดรวมกัน


<pre>
<strong>Table 4: Contribution of FLOSS code by selected universities</strong>
Rank  Person-months  University / research institution
   1           4955  Regents Of The University Of California
   2           4774  Massachusetts Institute Of Technology
   3           1687  Carnegie Mellon University
   4           1340  University Of Chicago
   5           1009  INRIA (France)
   6            982  University Of Amsterdam (the Netherlands)
   7            870  Stichting Mathematisch Centrum Amsterdam (the Netherlands)
   8            551  Ohio State University
   9            518  University Of Utah
  10            505  University Of Notre Dame
</pre>


จากตารางจะเห็นว่า อันดับ 1 และ 2 คือ UC กับ MIT นั้นใกล้เคียงกัน (ถ้าดูตามประวัติของ UNIX-based OS และ GNU แล้ว ก็คงไม่แปลก) และทิ้งอันดับถัดมาไปไกลทีเดียว  
จาก 10 มหาวิทยาลัยแรก มีที่ไม่ใช่้มหาวิทยาลัยในสหรัฐอยู่ 3 แห่ง คือจากฝรั่งเศสและเนเธอร์แลนด์ (อันดับ 5, 6, 7)

ตารางต่อมา ดูว่าบริษัทไหน ที่มอบโค้ดให้กับ FLOSS (Debian) เยอะที่สุด


<pre>
<strong>Table 5: Cost estimate for FLOSS code contributed by firms</strong>
<em>Total contribution from firms</em>
Number of firms       986
Source lines of code  31.2 million
Estimated effort      16444 person-years
Estimated cost        1.2 billion Euro
<em>Top contributors</em>
Rank  Name                  Person-months  Cost (mil euro)
   1  Sun Microsystems Inc.         51372   312
   2  IBM Corp.                     14865    90
   3  Red Hat Corp.                  9748    59
   4  Silicon Graphics Corp.         7736    47
   5  SAP AG                         7493    46
   6  MySQL AB                       5747    35
   7  Netscape Communications Corp.  5249    32
   8  Ximian Inc.                    4985    30
   9  RealNetworks Inc.              4412    27
  10  AT&T                           4286    26
</pre>


ตารางนี้อันดับ 1 (Sun) กับ 2 (IBM) ห่างกันมาก ชนิดที่ว่า เอาอันดับ 2-7 มารวมกัน ถึงจะได้เกือบ ๆ เท่าอันดับ 1  
หลัก ๆ ที่ Sun อยู่ตรงนี้ คงเป็นเพราะตัว [OpenOffice.org](http://th.wikipedia.org/wiki/OpenOffice.org) (เต็ม ๆ) และ [Mozilla](http://en.wikipedia.org/wiki/Mozilla) กับ [XFree86](http://en.wikipedia.org/wiki/XFree86) (เข้าไปช่วยอยู่หลายส่วน)  
ส่วน IBM ตัวหลักเลยน่าจะเป็น Linux kernel  
ดูตารางข้างล่างประกอบ


<pre>
<strong>Table 3: Production cost estimate for 5 largest FLOSS software products</strong>
Software package  Lines of code  Months  Person-months  Cost (million Euro)
openoffice.org          5181285     130          79237   482
kernel-source-2.6.8     4033843     160         145036   882
mozilla (firefox)       2437724      87          25339   154
gcc-3.4                 2422056     113          54048   329
xfree86                 2316842      90          27860   169
</pre>


แล้วโค้ดมาจากส่วนไหนบ้างของโลก ?  
ตารางข้างล่างนี่ บอกว่าภูมิภาคไหนมอบโค้ดมาเป็นสัดส่วนเท่าไหร่


<pre>
<strong>Figure 29: Share of code contribution by region (number of commits)</strong>
EU25                     45%
US Canada                41%
China India Korea Japan   2%
Others                   12%
</pre>


ถ้าคิดขนาดของภูมิภาคเข้าไปด้วย อียูนี่คงพุ่งปรี๊ดขึ้นไปอีก  
ไม่น่าแปลกใจ ที่ภูมิภาคนี้จะเป็นผู้ริเริ่มหลายสิ่งหลายอย่างใน FLOSS โดยเฉพาะเรื่องของการเคลื่อนไหวทางสังคมและการเมือง

เห็นตัวเลขต่าง ๆ ข้างบนแล้ว ก็เยอะดีนะครับ ทั้งแรงงานและทรัพยากรต่าง ๆ ที่ใส่ลงไปใน FLOSS จากทั้งมหาวิทยาลัยและบริษัท ตีออกมาเป็นตัวเงินได้เป็นระดับพันล้านยูโรเลยทีเดียว

แต่ดูนี่ก่อนครับ


<pre>
<strong>Figure 28: Distribution of code output by individuals, firms, universities</strong>
Individual Author  61.98%
Company            19.22%
Foundation          7.89%
University          5.62%
</pre>


สุดท้ายแล้ว แม้ว่าองค์กรต่าง ๆ ไม่้ว่าจะเป็น บริษัท มหาลัย มูลนิธิ ฯลฯ จะสนับสนุน FLOSS เป็นจำนวนมหาศาล  
แต่ท้ายที่สุดแล้ว มากกว่าครึ่ง 60% ของโค้ด ก็ยังมาจาก “บุคคลทั่วไป” (เช่น คุณ) อยู่ดี

**“เรา” มีพลังถึงขนาดนี้**

<span class="small">technorati tags:  
[free software](http://technorati.com/tag/free_software),  
[open source](http://technorati.com/tag/open_source),  
[you](http://technorati.com/tag/you)  
</span>
