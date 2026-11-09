---
title: "NetBeans 6 M7"
date: "2007-02-23T22:56:00+07:00"
lastmod: "2007-02-23T22:56:00+07:00"
type: "post"
url: "/2007/netbeans-6-m7/"
description: "NetBeans 6 Milestone 7 (รุ่นก่อนเบต้า) ออกแล้วนะครับ — มีอะไรใหม่? ผมสรุปบางอันมาไว้ข้างล่าง เดี๋ยวลงไปดูละกัน แต่ที่น่าตื่นเต้นสำหรับผมก็คือ M7 ตัวนี้ รองรับ Ruby และ Ruby on Rails แล้วครับ มาพร้อมกับ JRuby ในตัว ใครอยากลอง ก็เลือกติดตั้งได้จาก Update Center นอกเหนือจาก Ruby แล้ว ภาษาอื่น ๆ ที่รองร"
tag: ["java", "netbeans", "ruby-on-rails"]
textlang: "th"
wpid: 1927
---
NetBeans 6 Milestone 7 (รุ่นก่อนเบต้า) ออกแล้วนะครับ — [มีอะไรใหม่?](http://wiki.netbeans.org/wiki/view/NewAndNoteWorthyMilestone7)

ผมสรุปบางอันมาไว้ข้างล่าง เดี๋ยวลงไปดูละกัน

แต่ที่น่าตื่นเต้นสำหรับผมก็คือ M7 ตัวนี้ **รองรับ Ruby และ Ruby on Rails** แล้วครับ  
มาพร้อมกับ JRuby ในตัว ใครอยากลอง ก็เลือกติดตั้งได้จาก Update Center

นอกเหนือจาก Ruby แล้ว ภาษาอื่น ๆ ที่รองรับ ก็มี PHP, JavaScript, Groovy, Prolog (ใช่แล้ว Prolog!) แต่ระดับของการรองรับก็ยังไม่เท่ากับ Ruby ครับ — PHP แบบเต็ม ๆ นี่ ต้องรอ M8 ครับ

เอาล่ะ ดูรายการอัพเดท (ส่วนหนึ่ง) ของ M7 กันเลย

- สร้าง Java Web Start (JNLP) สำหรับโปรเจกต์ J2SE

- มี local history — ทำนอง version control system ในเครื่องเราน่ะ, ใครเคยใช้ VisualAge for Java สมัยก่อนคงจะชอบความสามารถนี้

- (sub-)expression stepping in debugger คือเวลาสั่งพวก step-in, step-out, step-into ตอนดีบัก เราสามารถให้มันละเอียดถึงระดับ expression ได้แล้ว เช่น

      if ( a.hasNext() && (b != EOF) ) {
      ...

  ถ้าเป็นเมื่อก่อน มันจะมอง expression ตรงหลัง if เป็นก้อนเดียวเลย แต่เดี๋ยวนี้ลงไปถึงระดับ a.hasNext() ก็ตัวนึง, b!= EOF ก็ตัวนึงได้

- Visual Web Pack ออกแบบหน้าตาเว็บแอพพลิเคชันแบบลากแล้ววาง (Matisse สำหรับเว็บ)

- รองรับ JBoss 5

- ไอคอนชุดใหม่ ออกแบบใหม่หมด ชัดเจนขึ้น ผมว่านะ

- เอดิเตอร์: กด Alt+Shift+Up, Alt+Shift+Down สำหรับไฮไลท์โค้ดตามลำดับบล็อกโปรแกรม ([ดูรูปประกอบดีกว่า](http://wiki.netbeans.org/wiki/view/NewAndNoteWorthyMilestone7#section-NewAndNoteWorthyMilestone7-EditorImprovements)) ถ้าใช้คล่อง ๆ คงมีประโยชน์เยอะ

- ฯลฯ

แถมนิด, ใน Update Center มีโมดูลน่าสนใจตัวนึงคือ **Quick File Chooser** ผมว่ามันเจ๋งดี ใช้แล้วชอบ คือเราไม่ต้องใช้เมาส์เลย พิมพ์คีย์บอร์ดอย่างเดียว พิมพ์ไปทีละตัวแล้วมันก็จะค่อย ๆ แสดงไฟล์ที่ตรงกับที่เราพิมพ์ไปขึ้นมา กด Tab ก็ได้ เหมือนอยู่ที่ shell เลยน่ะ สะดวกดี

**[ดาวน์โหลด Milestone ล่าสุด](http://wiki.netbeans.org/wiki/view/MilestoneDownloads)**

<span class="small">technorati tags:  
[NetBeans](http://technorati.com/tag/NetBeans),  
[Ruby on Rails](http://technorati.com/tag/Ruby_on_Rails),  
[Java](http://technorati.com/tag/Java)  
</span>
