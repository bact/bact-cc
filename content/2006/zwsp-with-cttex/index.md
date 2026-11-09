---
title: "ZWSP with cttex"
date: "2006-12-26T10:57:00+07:00"
lastmod: "2006-12-26T10:57:00+07:00"
type: "post"
url: "/2006/zwsp-with-cttex/"
description: "แทรก ZWSP (Zero Width Space ช่องว่างความกว้างศูนย์) ระหว่างคำไทยในเอกสาร HTML # cttex -b “&#x200b;” output.html คำสั่งข้างบน ใช้กับ cttex-1.30w (ตั้งชื่อไว้งี้ชั่วคราว ย้ำว่าตัวนี้ไม่ใช่ตัวอย่างเป็นทางการ เป็นเพียง “hack” อันนึงเท่านั้น) ที่มีตัวเลือกใหม่ -b ไว้ให้กำหนดตัวแบ่งคำเองได้ แม้จะไม่น่าจะใ"
tag: ["cttex", "thai", "word-break", "zwsp"]
textlang: "th"
wpid: 1815
---
แทรก [ZWSP](http://lewcpe.com/blog/tag/zwsp) (Zero Width Space ช่องว่างความกว้างศูนย์) ระหว่างคำไทยในเอกสาร HTML

    # cttex -b "&#x200b;" < input.html > output.html

คำสั่งข้างบน ใช้กับ [cttex-1.30w](http://bact.blogspot.com/2006/12/cttex-130-win32-fixed.html) <span class="small">(ตั้งชื่อไว้งี้ชั่วคราว ย้ำว่าตัวนี้ไม่ใช่ตัวอย่างเป็นทางการ เป็นเพียง “hack” อันนึงเท่านั้น)</span> ที่มีตัวเลือกใหม่ -b ไว้ให้กำหนดตัวแบ่งคำเองได้

แม้จะไม่น่าจะใช้ได้ทันทีกับทุกกรณี (เพราะนี่มันจะตัดดะไปหมดเลย ทั้ง head, meta, script ทุกส่วนในไฟล์ อาจจะทำให้เกิดอาการข้างเคียงได้) แต่ก็น่าจะทำให้สะดวกขึ้นบ้าง นิดหน่อย

<span class="small">technorati tags:  
[ZWSP](http://technorati.com/tag/ZWSP),  
[cttex](http://technorati.com/tag/cttex),  
[Thai](http://technorati.com/tag/thai),  
[word break](http://technorati.com/tag/word_break)  
</span>
