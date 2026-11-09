---
title: "super(\"Robot Wars\");"
date: "2008-02-23T00:49:00+07:00"
lastmod: "2008-02-23T00:49:00+07:00"
type: "post"
url: "/2008/superrobot-wars/"
description: "ตอนนี้ที่ภาคกำลังสนุกกับ Robocode น้อง ๆ ที่ลงเรียนแลบ AI (ปี 3) กับแลบ OOP (ปี 2) ต้องส่งโปรแกรมหุ่นยนต์ลงแข่ง จัดเป็นทัวร์นาเมนต์ (กติกา) เดินไปไหนมาไหน หรือขึ้นรถ ก็จะต้องได้ยินคนคุยกันเรื่องหุ่นเป็นไงมั่ง แข่งกับของคนนั้นคนนี้แล้วเป็นไง (ดูตัวอย่างที่ idiotao, d0m3z) — ปีที่แล้วก็มีแข่งเหมือนกัน"
tag: ["games", "java", "programming", "robotics", "siit"]
textlang: "th"
wpid: 2281
---
ตอนนี้ที่ภาคกำลังสนุกกับ [Robocode](http://en.wikipedia.org/wiki/Robocode "@ Wikipedia")  
น้อง ๆ ที่ลงเรียนแลบ AI (ปี 3) กับแลบ OOP (ปี 2)  
ต้องส่งโปรแกรมหุ่นยนต์ลงแข่ง จัดเป็นทัวร์นาเมนต์ ([กติกา](http://cholwich.org/robocode/Site/Welcome.html)) เดินไปไหนมาไหน หรือขึ้นรถ ก็จะต้องได้ยินคนคุยกันเรื่องหุ่นเป็นไงมั่ง แข่งกับของคนนั้นคนนี้แล้วเป็นไง (ดูตัวอย่างที่ [idiotao](http://www.idiotao.in.th/), [d0m3z](http://www.dome.in.th/?p=56)) — ปีที่แล้วก็มีแข่งเหมือนกัน (ผมไม่ได้แข่งกะเค้าหรอก แพ้น้องเปล่า ๆ :P)

**[Robocode](http://robocode.sourceforge.net/ "official home")** เป็นเกมเพื่อการศึกษาการเขียนโปรแกรม โดยผู้เล่นจะเขียนโปรแกรมด้วย[ภาษาจาวา](http://en.wikipedia.org/wiki/Java_(programming_language)) ควบคุมหุ่นยนต์รถถังให้สู้กัน ซึ่งก็เป็นการทำให้คนที่หัดเขียนจาวารู้สึกสนุกไปกับการเขียนโปรแกรมมากขึ้น อีกทั้งเห็นภาพชัด ๆ เลยว่า ที่เขียนไปมันจะมีผลลัพธ์ออกมายังไงบ้าง

[![Robocode battle](https://farm3.static.flickr.com/2294/2283568541_578a9198dd_o.png)](http://www.flickr.com/photos/arthit/2283568541/ "เปลี่ยน สนามรบ เป็น สนามความรู้ :P")

ตอนผมหัดเขียนโปรแกรมใหม่ ๆ ก็เคยเล่นเกมทำนองนี้  
ชื่อ **P-ROBOTS** ([download \#1](http://pascal.sources.ru/gamestxt/probots.htm), [download \#2](http://www.programmersheaven.com/download/4263/download.aspx) – ไม่แน่ใจว่าอันไหนใหม่กว่า) ต่างกันตรงเป็น[ภาษาปาสคาล](http://en.wikipedia.org/wiki/Pascal_(programming_language) "Pascal") (ภาษายอดนิยมในสมัยนั้น สำหรับเริ่มเรียนเขียนโปรแกรม) และเป็นเท็กซ์โหมด ไม่ใช่กราฟิกโหมดอย่าง Robocode — แต่จำได้ว่า แค่นั้นก็สนุกแล้ว ดูตัว \# วิ่งไปวิ่งมา

เว็บ [RoboWiki](http://robowiki.net/)  
รวบรวมเรื่องเกี่ยวกะ RoboCode พร้อมข้อมูลเกี่ยวกับหุ่นยนต์ตัวดัง ๆ ไว้ครบครัน (บางตัวมีซอร์สโค้ดให้ด้วย)  
โค้ดหุ่นหลายตัวเข้าขั้น \|nw มาก ๆ  
มีเอาเทคนิคการวิเคราะห์เชิงสถิติ หรือพวก [ข่ายงานประสาทเทียม](http://en.wikipedia.org/wiki/Artificial_neural_network "ANN") ไปใช้ด้วย จริงจังมาก แบบว่าทำนายเส้นทางการเดินของคู่ต่อสู้ได้ เขามีจัดเป็นลีกแข่งด้วยนะ

ใครสนใจ เสาร์อาทิตย์อยากหาอะไรสนุก ๆ เล่น ก็ลองไปโหลดมาเล่นกันครับ 🙂 เขามีตัวอย่างหุ่นมาให้จำนวนนึง เอาตรงนั้นมาแก้ ๆ ก็ได้ เพลิน ๆ

ข้างล่างนี่เป็นเอกสารที่อาจารย์ + น้องปี 4 เค้าทำให้น้องปี 2,3

- [Robocode Tutorial](http://cholwich.org/robocode/Site/Welcome_files/RoboCode.pdf) \[pdf\] by [Cholwich](http://cholwich.org/)
- [Robocode Basic Tactic for 1-vs-1](http://cholwich.org/robocode/Site/Welcome_files/robocode_tactic.pdf) \[pdf\] by [Kobkrit](http://kindml.siit.tu.ac.th/~kobkrit/)

<span class="small">technorati tags:  
[Java](http://technorati.com/tag/Java),  
[games](http://technorati.com/tag/games),  
[Robocode](http://technorati.com/tag/Robocode)  
</span>
