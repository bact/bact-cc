---
title: "cttex 1.30 dict2state stack overflow on Windows"
date: "2006-12-21T15:12:00+07:00"
lastmod: "2006-12-21T15:12:00+07:00"
type: "post"
url: "/2006/cttex-1-30-dict2state-stack-overflow-on-windows/"
description: "ทดลอง make cttex 1.30 บน Windows, ปรากฎว่า ตอนแปลงพจนานุกรมเป็น map (โปรแกรม dict2state) เกิด stack overflow เกิดขึ้นกับทั้ง gcc และ Visual C++ 2005 Express Edition บน GNU/Linux + gcc ไม่พบปัญหา ใครพอรู้สาเหตุ/วิธีแก้ ช่วยหน่อยนะครับ ในกระทู้ที่ LTN: stack overflow ใน dict2state ใน cttex 1.30 ขอบคุณ"
tag: ["c", "cttex", "stack-overflow", "thai", "windows", "word-break"]
textlang: "th"
wpid: 1809
---
ทดลอง make [cttex](http://vuthi.blogspot.com/2004/07/cttex.html "การตัดคำของ cttex") [1.30](http://www.mm.co.th/pub/firefox-thai/cttex-1.30.tgz "ดาวน์โหลดซอร์สโค้ด") บน Windows,  
ปรากฎว่า ตอนแปลงพจนานุกรมเป็น map (โปรแกรม dict2state) เกิด [stack overflow](http://en.wikipedia.org/wiki/Stack_overflow)  
เกิดขึ้นกับทั้ง gcc และ Visual C++ 2005 Express Edition  
บน GNU/Linux + gcc ไม่พบปัญหา

ใครพอรู้สาเหตุ/วิธีแก้ ช่วยหน่อยนะครับ ในกระทู้ที่ LTN:  
[stack overflow ใน dict2state ใน cttex 1.30](http://linux.thai.net/phpbb2/viewtopic.php?t=33359 "stack overflow ใน dict2state ใน cttex 1.30")  
ขอบคุณครับ 🙂
