---
title: "cttex 1.30 win32-fixed"
date: "2006-12-23T14:41:00+07:00"
lastmod: "2006-12-23T14:41:00+07:00"
type: "post"
url: "/2006/cttex-1-30-win32-fixed/"
description: "สืบเนื่องจากโพสต์เรื่อง stack overflow ใน cttex 1.30 บน Windows ตอนนี้แก้ไขได้เรียบร้อยแล้วครับ 🙂 นอกจากแก้ไขเรื่อง stack overflow แล้ว ยังเพิ่ม option -W ใช้ \\wbr เป็นตัวแบ่งคำ และ -b กำหนดตัวแบ่งคำเอง ตัวอย่างเช่น ถ้าอยากแทรก ZWSP ระหว่างคำในเอกสาร ก็ใช้ # cttex -b “&#x200b;” output.html (เป็นแค่ต"
tag: ["cttex", "free-softwares", "open-source", "thai", "windows"]
textlang: "th"
wpid: 1810
---
สืบเนื่องจากโพสต์เรื่อง [stack overflow ใน cttex 1.30 บน Windows](http://bact.blogspot.com/2006/12/cttex-130-dict2state-stack-overflow-on.html) ตอนนี้แก้ไขได้เรียบร้อยแล้วครับ 🙂

นอกจากแก้ไขเรื่อง stack overflow แล้ว ยังเพิ่ม option -W ใช้ \wbr เป็นตัวแบ่งคำ และ -b กำหนดตัวแบ่งคำเอง  
ตัวอย่างเช่น ถ้าอยากแทรก ZWSP ระหว่างคำในเอกสาร ก็ใช้

    # cttex -b "&#x200b;" < input.html > output.html

(เป็นแค่ตัวอย่างนะ เอาไปใช้จริงคงต้องปรับหน่อย เพราะนี่มันจะตัดดะเลย ใน header, meta, script ทุกอย่าง ตัดหมด)

ซอร์สโค้ด: คอมไพล์ได้ด้วย Visual C++ 2005 Express Edition, Borland C++ Compiler, gcc (MinGW), gcc (GNU/Linux)  
โปรแกรม: ใช้ได้กับ Windows, Windows+MSYS (MinGW), GNU/Linux

ดาวน์โหลดตัวที่แก้ไขแล้ว ทั้ง แพตช์ ซอร์ส และไบนารี (วินโดวส์) ได้จาก **[bact’ bazaar](http://arthit.googlepages.com/bazaar)**  
(ส่งโค้ดให้กับคุณฮุ้ย ผู้ดูแลโค้ดต้นฉบับแล้ว)

การปรับปรุงนี้ ไม่มีทางเกิดขึ้นได้ หากตัวโปรแกรมต้นฉบับ cttex ไม่ได้เผยแพร่ซอร์สโค้ด  
การปรับปรุงนี้ เกิดขึ้นไม่ได้ หากผู้เขียนไม่ได้รับคำแนะนำจาก [เว็บบอร์ด LTN](http://linux.thai.net/phpbb2/viewtopic.php?t=33359 "stack overflow ใน dict2state ใน cttex 1.30")  
และเอกสาร [Compile ctTEX & dict2state on Win32](http://arthit.googlepages.com/cttex_win32.pdf) <span class="small">(PDF)</span> โดย [NuuNeoi](http://nuuneoi.com/) และ bpasu  
และ การปรับปรุงนี้ แม้จะเกิดขึ้นได้ แต่ก็ไม่อาจเผยแพร่เช่นนี้ได้ หากตัวโปรแกรมต้นฉบับไม่ได้ใช้สัญญาอนุญาตแบบเสรี

[โอเพนซอร์ส](http://th.wikipedia.org/wiki/Opensource) จงเจริญ! [ซอฟต์แวร์เสรี](http://th.wikipedia.org/wiki/Free_software) จงเจริญ!  
**การแบ่งปัน จงเจริญ! เสรีภาพ จงเจริญ!**  
😉

<span class="small">**technorati tags:**  
[cttex](http://technorati.com/tag/cttex) \|  
[open source](http://technorati.com/tag/open_source) \|  
[Windows](http://technorati.com/tag/Windows) \|  
[Thai](http://technorati.com/tag/Thai)  
</span>
