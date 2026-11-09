---
title: "Newline in GATE"
date: "2007-01-08T16:00:00+07:00"
lastmod: "2011-05-13T12:07:50+07:00"
type: "post"
url: "/2007/newline-in-gate/"
description: "ใน GATE, ถ้าเราอยากรู้ว่า เอกสารที่เรากำลังทำงานอยู่เนี่ย มันใช้ อักขระขึ้นบรรทัดใหม่ (newline) แบบไหน ก็เรียกดูได้จากฟีเจอร์ที่ชื่อ “docNewLineType” โดย docNewLineType นี้ เป็น String มีค่าได้ 4 อย่าง: { “CR”, “LF”, “CRLF”, “LFCR” } CR คือ Carriage Return — ปัดแคร่(ไปซ้ายสุด) (\\r ในหลายภาษาโปรแกรม)"
categories: ["coling"]
tag: ["gate", "natural-language-processing", "newline", "text-processing"]
textlang: "th"
wpid: 1849
---
ใน [GATE](http://gate.ac.uk/ "General Architecture for Text Engineering"), ถ้าเราอยากรู้ว่า เอกสารที่เรากำลังทำงานอยู่เนี่ย มันใช้ อักขระขึ้นบรรทัดใหม่ ([newline](http://en.wikipedia.org/wiki/Newline)) แบบไหน ก็เรียกดูได้จากฟีเจอร์ที่ชื่อ “docNewLineType”  
โดย docNewLineType นี้ เป็น String มีค่าได้ 4 อย่าง: { “CR”, “LF”, “CRLF”, “LFCR” }

CR คือ [Carriage Return](http://en.wikipedia.org/wiki/Carriage_return) — ปัดแคร่(ไปซ้ายสุด) (`\r` ในหลายภาษาโปรแกรม),  
LF คือ [Line Feed](http://en.wikipedia.org/wiki/Line_feed) — เลื่อนบรรทัดใหม่ (`\n`)

เพื่อขึ้นบรรทัดใหม่ เครือญาติ UNIX อย่าง Linux กับ Mac OS X ใช้ LF ตัวเดียว,  
ใน Mac OS (จนถึงรุ่น 9) ใช้ CR ตัวเดียว,  
ส่วนเพื่อนรัก Windows ของเรา เป็นเด็กนอย ใช้มันสองตัวเลย CRLF กันเหนียว\*, DOS ก็เช่นกัน  
(\* พูดจริง ๆ แล้ว DOS/Windows ทำตัวเลียนแบบเครื่องพิมพ์ดีดจักรกลได้เหมือนที่สุด คือต้องปัดแคร่ไปซ้ายสุดก่อน จากนั้นจึงค่อยเลื่อนกระดาษไปหนึ่งบรรทัดได้ เป็นการเริ่มบรรทัดใหม่)

นอกเรื่องซะไกล อ่ะ เขียนโค้ดได้อย่างนี้ (ตรงที่เป็นตัวหนา)


<pre><code>
int nllen = 1;
<strong>String nl = (String) document.getFeatures().get("docNewLineType");</strong>
if (nl.equals("CRLF") || nl.equals("LFCR")) {
  nllen = 2;
}
</code></pre>


ผมหาเจ้าความยาวของอักขระขึ้นบรรทัดใหม่ (nllen) นี่ไป เพื่อไปชดเชยออฟเซตเวลาประมวลผลเอกสาร  
คือ ผมใช้เมทธอด readLine() ในคลาส \*Reader ซึ่งมันจะอ่านทีละบรรทัดให้อัตโนมัติ สบายดี  
แต่เวลานับตำแหน่งเนี่ย ต้องอย่าลืมนับเจ้าตัวอักขระขึ้นบรรทัดใหม่เข้าไปด้วย ไม่งั้นตำแหน่งมันจะคลาดกัน  
ก็เลยต้องรู้ว่า ใช้อักขระขึ้นบรรทัดใหม่แบบไหน จะได้ชดเชยถูก

<span class="small">technorati tags: [GATE](http://technorati.com/tag/GATE), [text processing](http://technorati.com/tag/text+processing), [newline](http://technorati.com/tag/newline)</span>
