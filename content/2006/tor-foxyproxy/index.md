---
title: "Tor + FoxyProxy"
date: "2006-09-01T04:57:00+07:00"
lastmod: "2011-04-29T05:56:46+07:00"
type: "post"
url: "/2006/tor-foxyproxy/"
description: "One of the fundamental contrasts between free democratic societies and totalitarian systems is that the totalitarian government [or other totalitarian organization] relies on secrecy for the regime but high surveillance and disclosure for all other groups, whereas in the civic culture of liberal dem"
categories: ["internet", "freedom"]
tag: ["anonymity", "circumvention", "free-softwares", "internet-censorship", "open-source", "privacy", "software", "surveillance", "tor"]
textlang: "th"
wpid: 1626
---
> One of the fundamental contrasts between free democratic societies and totalitarian systems is that the totalitarian government \[or other totalitarian organization\] relies on secrecy for the regime but high surveillance and disclosure for all other groups, whereas in the civic culture of liberal democracy, the position is approximately the reverse.  
> — Geoffrey de Q Walker <sup>[\*](http://joi.ito.com/static/emergentdemocracy.html#_ftnref6)</sup>
>
> (หนึ่งในความแตกต่างพื้นฐาน ระหว่าง สังคมเสรีประชาธิปไตย และ ระบอบเผด็จการ ก็คือ การดำรงอยู่ของ รัฐบาลเผด็จการ \[หรือองค์กรเผด็จการอื่น ๆ\] นั้น ขึ้นอยู่กับ การปกปิดความลับของฝ่ายบริหาร แต่กลับตรวจตราและเปิดโปงอย่างเข้มข้นกับกลุ่มอื่น ๆ, ในขณะที่ ในวัฒนธรรมพลเมืองของระบอบเสรีประชาธิปไตยนั้น ตำแหน่งที่ว่า เกือบจะกลับกัน)

เมื่อวานและวันนี้ ลองใช้ [Tor](http://tor.eff.org/) + [FoxyProxy extension](http://foxyproxy.mozdev.org/) ร่วมกับ Firefox ท่องเน็ตดู  
ทดสอบเทคโนโลยีเพื่อความเป็นส่วนตัวบนโลกออนไลน์

เต่าเกือบจะกัดยาง … เน็ตอืดลงอย่างเห็นได้ชัด แต่ยังพอรับได้  
คิดไม่ออกว่า ถ้าไปเล่นที่เมืองไทย ซึ่งเน็ตคงช้ากว่าที่นี่ (ตอนนี้ใช้ DSL 6 Mbits) มันจะอืดกว่านี้แค่ไหน

อีกอย่างคือ ถ้าเปิดเว็บหลาย ๆ ที่พร้อมกัน บางทีมันจะเปิดไม่ได้ เนื่องจากมันเปิืด connection ไม่ทัน

คือเท่าที่เข้าใจ Tor มันใช้วิธี “ฝาก” คำร้อง (request) ของเรา ไปยัง Tor node อื่น ๆ หลาย ๆ ต่อ ก่อนจะส่งข้อมูลที่ร้องขอย้่อนกลับมาให้เรา เพื่อพรางต้นตอของคำร้อง … นี่ก็จุดแรกของความช้า เพราะมันหลายต่อ  
อีกจุดก็คือ ถ้าเกิด node มันน้อย เรา(และคนอื่น ๆ)ก็มีโอกาสที่จะขอไปยัง node เดิมซ้ำ ๆ ซึ่ง 1) node นั้นมันก็จะรับไม่ไหว (เป็นที่มาของ failed connection) 2) โอกาสที่จะถูกตามรอยกลับมันก็ง่ายขึ้น

จากที่คิดเอาเอง คาดว่า ถ้าเกิดมีคนใช้ Tor กันมาก ๆ เข้า ความเร็ว+ความเป็นส่วนตัว มันคงดีขึ้นแน่

ตัวติดตั้งของ Tor รุ่นปัจจุบัน มีแบบขายยกชุดด้วย (Tor & Privoxy & Vidalia bundle) ซึ่งก็ใช้สะดวกดี ผมปิด Privoxy ทิ้ง เพราะเหมือนมันจะตีกับ FoxyProxy (ผมเซตไม่ค่อยเป็น) ส่วนตัว Vidalia นี่ดีมาก ทำให้เซต Tor ได้ง่ายขึ้นจมเลย เป็น GUI หมด แนะนำให้ดาวน์โหลดชุดนี้

เราเดินไปซื้อหนังสืออะไรในร้านมาอ่าน ก็ไม่มีใครคอยมาเช็ค/มีโอกาสได้เช็คน้อย (เว้นว่าเราจ่ายด้วยบัตรเครดิต/เดบิตที่เป็นชื่อเราเองหรือคนใกล้ชิด อันนี้ก็ง่ายเลย)  
แต่ทำไมเราจะเข้าไปดูเว็บไหน ต้องเปิดโอกาสให้ใครมาตามรอยด้วย ?

**Wikipedia:** [surveillance state](http://en.wikipedia.org/wiki/Surveillance_state) (?) \| [civil liberties](http://en.wikipedia.org/wiki/Civil_liberties) (เสรีภาพพลเมือง?)

**tags:**  
[privacy](http://technorati.com/tag/privacy), [civil liberties](http://technorati.com/tag/civil+liberties). [Internet](http://technorati.com/tag/internet), [ความเป็นส่วนตัว](http://technorati.com/tag/ความเป็นส่วนตัว), [เสรีภาพพลเมือง](http://technorati.com/tag/เสรีภาพพลเมือง), [surveillance](http://technorati.com/tag/surveillance), [Tor](http://technorati.com/tag/tor), [proxy](http://technorati.com/tag/proxy)
