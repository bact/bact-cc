---
title: "experimental jibjib"
date: "2008-12-14T05:57:00+07:00"
lastmod: "2008-12-14T05:57:00+07:00"
type: "post"
url: "/2008/experimental-jibjib/"
description: "jibjib จิ๊บจิ๊บ เป็นโปรแกรมทวิตเตอร์บนมือถือ Java ME พัฒนาโดย @sugree เมื่อวานและวันนี้ ลองแก้ ๆ โค้ดเล่นเองดู อยากจได้นั่นได้นี่ แต่เกรงใจสุกรี ไม่อยากขอเยอะ :p ก็ลองทำเองดู มั่ว ๆ ส่งแพตช์ไปครั้งแรกแบบไม่เคยลองคอมไพล์ วันนี้มาลองคอมไพล์ดู เอ้อ ไม่ผ่านจริง ๆ :p กว่าจะ build ได้ต้องลงเครื่องมือเพิ่ม"
tag: ["free-softwares", "java-me", "jibjib", "open-source", "twitter"]
textlang: "th"
wpid: 2420
---
**[jibjib](http://sugree.com/project/jibjib "a tiny mobile twitter client")** จิ๊บจิ๊บ เป็นโปรแกรมทวิตเตอร์บนมือถือ Java ME พัฒนาโดย [@sugree](http://twitter.com/sugree)

เมื่อวานและวันนี้ ลองแก้ ๆ โค้ดเล่นเองดู อยากจได้นั่นได้นี่ แต่เกรงใจสุกรี ไม่อยากขอเยอะ :p ก็ลองทำเองดู มั่ว ๆ

ส่งแพตช์ไปครั้งแรกแบบไม่เคยลองคอมไพล์ วันนี้มาลองคอมไพล์ดู เอ้อ ไม่ผ่านจริง ๆ :p กว่าจะ build ได้ต้องลงเครื่องมือเพิ่มนิดหน่อย คือ [ant-google](http://code.google.com/p/ant-googlecode/), [J2ME Polish](http://www.j2mepolish.org/), และ [Antenna](http://antenna.sourceforge.net/) ไล่ดูเอาจากแฟ้ม [build.xml](http://code.google.com/p/jibjib/source/browse/trunk/build.xml) ไดเรกทอรีอะไรต่าง ๆ ก็ ln -s เลียนแบบใน build.xml เอาเลย ง่ายดี จะได้ไม่ต้องตั้งใหม่

ที่อยากได้คือ:

1.  แก้บั๊ก retweet ข้อความที่พอรวมกับ “rt @xxx: ” แล้วยาวเกิน 140 ตัวอักษร (ก่อนหน้านี้ ใช้วิธีเพิ่มขนาดช่องข้อความเป็น 160 ตัวอักษร แก้ขัดไปก่อน)
2.  ใช้ปุ่มตัวเลขเป็นปุ่มลัดต่าง ๆ ได้ เช่น 2 = tweet, 4 = reply, 5 = retweet, \* = favorite
3.  ความสามารถ ‘ย่อ’ ข้อความให้สั้นลงหน่อย

สุดท้ายแล้ว (2) ไม่เวิร์ก เพราะ keyPressed() มันใช้ได้เฉพาะ Canvas subclass, ตัว jibjib ใช้ Form สำหรับหน้าอ่านทวีต, List สำหรับหน้าดูรายการทวีต – ถ้าอยากได้ ต้องใช้ Polish GUI .. ซึ่งมันจะทำให้ jibjib อ้วนขึ้น จาก 52K ไปเป็น 104K ทันที = สองเท่า! ก็เลย เอาไว้ก่อนละกัน เดี๋ยวหาทางดี ๆ ก่อน

\(1\) นี่ทำงานได้ตามที่อยากได้ ส่วน (3) ก็พอไหว แต่ก็ไม่รู้ว่ามันจะมีปัญหาในการใช้งานจริงไหม จะไปย่ออะไรที่ไม่น่าย่อรึเปล่า

แถมเพิ่มมาคือ ตรงหัวเรื่อง title ของแต่ละหน้าจอ แทนที่จะเป็นคำว่า jibjib ไปตลอด ก็ให้หัวเรื่องมันสื่อถึงหน้าปัจจุบันหน่อย เช่นถ้ากำลังแสดง Friends Timeline อยู่ ก็จะขึ้นหัวว่า Friends

ลองทดสอบดูครับ

ตอนคอมไพล์/บิวด์ ใช้ ant compile ตามด้วย ant polish ตัวหลังนี้มันจะช่วยสร้างแฟ้ม jad และ jar สำหรับมือถือสเป็กต่าง ๆ ให้อัตโนมัติ มี preprocessor ให้ใช้ได้ด้วย เพื่อความสะดวกในการจะเรียกใช้บางฟังก์ชั่นที่มีเฉพาะในโทรศัพท์บางรุ่น

ตอนจะทดสอบในเครื่องคอมด้วยอีมูเลเตอร์ ต้องไปแก้แฟ้ม jad นิดหน่อย ตรง MIDlet-Jar-URL เอาให้มันชี้ไปที่ไหนซักที่ ที่เราเอาแฟ้มไปวางอยู่ (ถ้าไม่แก้ มันจะไปเรียกจาก jibjib.googlecode.com)

ทดสอบด้วยอีมูเลเตอร์ ใช้คำสั่ง j2mewtk/bin/emulator -Xdescriptor:dist/ชื่อแฟ้ม.jad

ส่ง[แพตช์](http://code.google.com/p/jibjib/issues/detail?id=18 "#18")เข้า issue tracker ไปแล้ว

build มาให้ทดลองใช้ชั่วคราวครับ ระหว่างรอ @sugree ตรวจโค้ดแพตช์

- MIDP 2.0 / CLDC 1.0 [jad](http://culturelab.in.th/files/jibjib-midp20_cldc10.jad "descriptor") \| [jar](http://culturelab.in.th/files/jibjib-midp20_cldc10.jar "archive")
- MIDP 2.0 / CLDC 1.1 [jad](http://culturelab.in.th/files/jibjib-midp20_cldc11.jad "descriptor") \| [jar](http://culturelab.in.th/files/jibjib-midp20_cldc11.jar "archive")
- MIDP 2.1 / CLDC 1.1 [jad](http://culturelab.in.th/files/jibjib-midp21_cldc11.jad "descriptor") \| [jar](http://culturelab.in.th/files/jibjib-midp21_cldc11.jar "archive")

**ย้ำว่านี่เป็นรุ่นทดลอง-ทดสอบนะครับ** ตัวโปรแกรมรุ่นอย่างเป็นทางการอยู่ที่เว็บสุกรี [sugree.com/project/jibjib](http://sugree.com/project/jibjib)

มีซอร์สโค้ดให้ดูให้แก้ได้ เราก็มีโอกาสได้ลงมือเอง ถ้าอยากทำ/ต้องทำ

<span class="small">technorati tags:  
[jibjib](http://technorati.com/tag/jibjib),  
[Twitter](http://technorati.com/tag/Twitter),  
[Java](http://technorati.com/tag/Java)  
</span>
