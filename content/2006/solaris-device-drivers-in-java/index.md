---
title: "Solaris device drivers in Java"
date: "2006-09-06T20:55:00+07:00"
lastmod: "2006-09-06T20:55:00+07:00"
type: "post"
url: "/2006/solaris-device-drivers-in-java/"
description: "Writing Solaris Device Drivers in Java — ฝ่ายวิจัยของซัน พอร์ต Java VM ขนาดเล็กที่ชื่อ Squawk เข้าไปใน kernel ของ Solaris จากนั้นก็ทดลองพอร์ตดีไวซ์ไดรเวอร์ง่าย ๆ ตัวนึง จากภาษาซี ไปเป็นภาษาจาวา เป็นการทดสอบอย่างนึงว่า ภาษาในระดับจาวานั้น ก็สามารถใช้ในงานที่โดยมากจะใช้แต่ซีได้ สำหรับ Squawk เองนี่ เป"
tag: ["java", "solaris"]
textlang: "th"
wpid: 1638
---
[Writing Solaris Device Drivers in Java](http://research.sun.com/techrep/2006/abstract-156.html) — ฝ่ายวิจัยของซัน พอร์ต Java VM ขนาดเล็กที่ชื่อ [Squawk](http://research.sun.com/projects/squawk/) เข้าไปใน kernel ของ Solaris จากนั้นก็ทดลองพอร์ตดีไวซ์ไดรเวอร์ง่าย ๆ ตัวนึง จากภาษาซี ไปเป็นภาษาจาวา เป็นการทดสอบอย่างนึงว่า ภาษาในระดับจาวานั้น ก็สามารถใช้ในงานที่โดยมากจะใช้แต่ซีได้

สำหรับ Squawk เองนี่ เป็น JVM ที่ออกแบบมาสำหรับอุปกรณ์ขนาดเล็ก ตัว VM เกือบทั้งหมดเขียนด้วยภาษาจาวา ([ดูภาพประกอบ](http://research.sun.com/projects/squawk/squawk-rjvm.html)) เพื่อความสะดวกในการพอร์ต VM (มีรันบน [Java Card 3.0](http://research.sun.com/projects/squawk/squawk-javacard.html) และ [Sun SPOT](http://research.sun.com/projects/squawk/squawk-sunspot.html) ซึ่งเป็น “ชุดคิท” embedded device จาก Sun Labs) ตัว VM นี่ compat กับ CLDC 1.1

**tags:**  
[Sun](http://technorati.com/tag/sun) \|  
[Java](http://technorati.com/tag/java) \|  
[Solaris](http://technorati.com/tag/solaris) \|  
[virtual machine](http://technorati.com/tag/virtual_machine)
