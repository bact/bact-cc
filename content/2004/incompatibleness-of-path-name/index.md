---
title: "incompatibleness of path name"
date: "2004-05-23T07:40:00+07:00"
lastmod: "2004-05-23T07:40:00+07:00"
type: "post"
url: "/2004/incompatibleness-of-path-name/"
description: "เราก็นึกว่าเราคอมไพล์ไม่ดี มีอะไรผิด โธ่เอ๊ย กลายเป็นเพราะว่า ชื่อ path มันใช้คนละแบบกัน ระหว่าง POSIX กะ DOS (งี่เง่าจริงๆ กู) ใช้ cygwin merge คำแปลเข้า OO.o ด้วยโปรแกรม ‘localize’ แต่ทีแรกมันไม่ได้ไง crash ตลอด ไปถามใน mailing list + เวบบอร์ดปลาดาว ได้ความว่า ต้องใช้ guw.pl ซึ่งเป็น wrapper ที่จะ"
tag: ["openoffice-org", "pladao"]
textlang: "th"
wpid: 139
---
เราก็นึกว่าเราคอมไพล์ไม่ดี มีอะไรผิด

โธ่เอ๊ย กลายเป็นเพราะว่า ชื่อ path มันใช้คนละแบบกัน  
ระหว่าง POSIX กะ DOS  
(งี่เง่าจริงๆ กู)

ใช้ cygwin merge คำแปลเข้า [OO.o](http://www.openoffice.org/)  
ด้วยโปรแกรม ‘localize’  
แต่ทีแรกมันไม่ได้ไง crash ตลอด

ไปถามใน [mailing list](http://l10n.openoffice.org/servlets/ReadMsg?list=dev&msgNo=3451) + [เวบบอร์ดปลาดาว](http://pladao.org/modules.php?name=Forums&file=viewtopic&t=494)  
ได้ความว่า ต้องใช้ **guw.pl**  
ซึ่งเป็น wrapper ที่จะเปลี่ยนชื่อ path ให้

[IZ \#16650](http://www.openoffice.org/issues/show_bug.cgi?id=16650)

ขอบคุณ Simon Brouwer และ พี่นุสรณ์
