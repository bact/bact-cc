---
title: "JavaScript in Java 6"
date: "2006-04-21T00:03:00+07:00"
lastmod: "2011-05-17T14:32:48+07:00"
type: "post"
url: "/2006/javascript-in-java-6/"
description: "อย่างที่พอจะรู้กันบ้างแล้ว ว่า Java 6 จะใช้รองรับภาษาสคริปต์อย่างเป็นทางการ (ในตัว API เลย โดยจะอยู่ในแพคเกจ javax.script แล้วก็มีเครื่องมือสนับสนุนอื่น ๆ อีก) วันนี้เผอิญไปเห็นสไลด์เกี่ยวกะเรื่องนี้ เลยเอามาฝาก: Scripting for Java Platform (JavaOne 2005) นอกจากการเรียกใช้ภาษาสคริปต์ภาษา API ได้แล้ว"
categories: ["computer"]
tag: ["java", "javascript", "jdk", "mozilla", "mozilla-rhino", "programming"]
textlang: "th"
wpid: 1440
---
อย่างที่พอจะรู้กันบ้างแล้ว ว่า Java 6 [จะใช้รองรับภาษาสคริปต์](http://blogs.sun.com/roller/page/sundararajan?entry=command_line_script_shell_in)อย่างเป็นทางการ (ในตัว API เลย โดยจะอยู่ในแพคเกจ [javax.script](http://java.sun.com/javase/6/docs/api/javax/script/package-summary.html) แล้วก็มีเครื่องมือสนับสนุนอื่น ๆ อีก) วันนี้เผอิญไปเห็นสไลด์เกี่ยวกะเรื่องนี้ เลยเอามาฝาก: [Scripting for Java Platform](https://jdk.dev.java.net/nonav/J12005/script.pdf) (JavaOne 2005)

นอกจากการเรียกใช้ภาษาสคริปต์ภาษา API ได้แล้ว ในส่วนของเครื่องมือ (ซึ่งจะมาพร้อมกับ Java 6 SDK แต่ไม่ได้เป็นส่วนหนึ่งของสเป็ค Java 6 SE) จะมีโปรแกรมเพิ่มขึ้นมาตัวนึงสำหรับเรื่องนี้โดยเฉพาะ คือ [jrunscript](http://java.sun.com/javase/6/docs/tooldocs/share/jrunscript.html) (กดเพื่อดูวิธีใช้) เอาไว้รันสคริปต์จากคอมมานด์ไลน์ (ค่าปริยายเป็น JavaScript แต่จะระบุภาษาอื่นก็ได้)

ตัวอย่าง:

ผ่านคำสั่งเป็นพารามิเตอร์ (เหมือนพวก Perl)

    jrunscript -e "print('hello world')"

ระบุภาษาด้วยออปชั่น -l / เรียกชุดคำสั่งจากไฟล์

    jrunscript -l js -f test.js

ตัว ScriptEngine ที่จะมากับ Java 6 ก็คือเอนจิ้นของภาษา JavaScript ซึ่งพัฒนามาจากตัว [Mozilla Rhino](http://en.wikipedia.org/wiki/Rhino_%28JavaScript_engine%29)

ตัว [NetBeans IDE](http://netbeans.org/) รุ่นหน้า (หลัง 5.5) ก็จะมี JavaScript editor ด้วย แต่ถ้ารอไม่ไหว [มีคนทำออกมาแล้ว](http://www.liguorien.org/jseditor/) ใช้กับ NetBeans 5 ได้เลย

ช่วงนี้ไปไหนก็มีแต่ [JavaScript](http://en.wikipedia.org/wiki/JavaScript) … อะไร ๆ ที่ Netscape ทำมันมักจะเป็นอย่างนี้รึเปล่า ? ต้องดังวูบนึงก่อน แล้วก็ฟุบ แล้วค่อยฟื้นมาใหม่ 😛
