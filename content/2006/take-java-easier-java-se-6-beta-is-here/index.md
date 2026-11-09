---
title: "Take Java easier – Java SE 6 Beta is here"
date: "2006-02-18T19:07:00+07:00"
lastmod: "2006-02-18T19:07:00+07:00"
type: "post"
url: "/2006/take-java-easier-java-se-6-beta-is-here/"
description: "ทยอยกันออกมาแล้วครับ “Java รุ่นใหม่” จะเห็นได้ชัดเลยว่า ชุดนี้ (ทั้ง Java SE, Java EE, NetBeans) เน้นความ “ง่าย” ในทุก ๆ ส่วน ทั้งส่วนของการใช้งานสำหรับผู้ใช้ (เช่น ตอบสนองเร็วขึ้น ทำตัวเหมือน native app มากขึ้น ตัวอย่าง เพิ่มเรื่อง desktop integration ให้ทำตัวเนียนไปกับโอเอสได้ดีขึ้น) สำหรับผู้พัฒน"
tag: ["ajax", "java", "netbeans"]
textlang: "th"
wpid: 1273
---
ทยอยกันออกมาแล้วครับ “Java รุ่นใหม่”  
จะเห็นได้ชัดเลยว่า ชุดนี้ (ทั้ง Java SE, Java EE, NetBeans) เน้นความ “ง่าย” ในทุก ๆ ส่วน ทั้งส่วนของการใช้งานสำหรับผู้ใช้ (เช่น ตอบสนองเร็วขึ้น ทำตัวเหมือน native app มากขึ้น <span class="small">[ตัวอย่าง](http://ensode.net/java_swing_mustang_screenshots_gtk.html)</span> เพิ่มเรื่อง desktop integration ให้ทำตัวเนียนไปกับโอเอสได้ดีขึ้น) สำหรับผู้พัฒนา ในส่วนของการพัฒนาและการติดตั้ง ก็ได้ปรับปรุงขึ้นเยอะแยะ ลองไปอ่านได้ ลิงก์ด้านล่าง

ตอนนี้ผมใช้ NetBeans 5.0 อยู่ (นอกเหนือจาก Eclipse 3.2 M4) โดยใช้ลองเขียนพวกโมดูลของ Lucene เล่น ๆ ก็คิดว่ามันใช้ง่ายกว่า 4.1 เยอะเลยนะ มีพวก refactoring, code completion ที่เทียบได้กับ Eclipse แล้ว ติดอยู่ไม่กี่อย่างที่ยังไม่ชอบใจ เช่นมี profile สำหรับ Run/Debug หลาย ๆ อันไม่ได้ และฟอนต์ของ UI ตัวมันเล็กไปหน่อย 🙁 แต่ถ้านับว่ามันมี Profiler สุดเจ๋งมาให้ด้วยนี่ ถ้าต้องเลือกแค่ตัวใดตัวนึงสำหรับงาน Java ผมคงเอา NetBeans อ่ะ (แต่ถ้าต้องใช้กับภาษาอื่นด้วย ก็คงต้องเป็น Eclipse ล่ะ NetBeans สู้ตรงนี้ไม่ได้เลย แย่จริง)

- client-side: [Java SE 6 Beta](http://java.sun.com/javase/6/) — improved user experience & increased developer productivity
- server-side: [Java EE 5 Adoption](http://java.sun.com/reference/javaee5adoption/) — focused on making development easier — based-on open source project [GlassFish](https://glassfish.dev.java.net/)
- developers: [NetBeans IDE 5.0](http://www.netbeans.org/community/releases/50/) — with Matisse (simple and easy GUI builder) and AJAX supported  
  <span class="small">+ [Mobility Pack 5.0](http://www.netbeans.org/products/mobility/) (Java ME) + [Profiler 5.0](http://www.netbeans.org/products/profiler/) (performance tuning ดีมาก ๆ)</span>

ถ้าไม่มี .NET ป่านนี้ค่ายจาวาอาจจะยังใช้ “ยาก” อยู่ 😛

หมายเหตุ:

NetBeans IDE 5.0 นี่ ออกแบบมาสนับสนุน Java SE 5 เต็มที่  
โดยรุ่นต่อไป คือ NetBeans IDE 5.5 จะสนับสนุน Java EE 5 เต็มที่  
และหลังจากนั้น คือ NetBeans IDE 6.0 ก็จะสนับสนุน Java SE 6 เต็มที่

คือ เลขรุ่น x.0 เป็นการปรับปรุงสำหรับ Java SE ตัว(เสถียร)ล่าสุด, ส่วนเลขรุ่น x.5 ก็สำหรับ Java EE  
ปีนึง NetBeans ตั้งเป้าจะออกรุ่นหลักสองครั้ง x.0 ตัวนึง 0.5 ตัวนึง ซึ่งก็จะตรงกับรอบของ Java SE และ Java EE ซึ่งแต่ละตัวออกรุ่นใหม่ปีละครั้ง พอดี
