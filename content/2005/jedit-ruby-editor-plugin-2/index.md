---
title: "jEdit Ruby Editor Plugin"
date: "2005-12-06T23:24:00+07:00"
lastmod: "2005-12-06T23:24:00+07:00"
type: "post"
url: "/2005/jedit-ruby-editor-plugin-2/"
description: "Ruby Editor Plugin สำหรับ jEdit ความสามารถหลัก ๆ ของ jEdit Ruby Editor Plugin syntax highlighting แสดงสีไวยากรณ์ error list บอกที่ผิด structure browser แสดงโครงสร้างโปรแกรม online API documentation คู่มือ API สด code completion ช่วยเติมโค้ด more และอื่น ๆ นอกจาก FreeRIDE กับ SciTE ที่มากับชุดติดตั้ง"
tag: ["jedit", "ruby"]
textlang: "th"
wpid: 1096
---
Ruby Editor Plugin สำหรับ jEdit  
[![Ruby Editor Plugin screenshot](https://static.flickr.com/18/70883201_6af4820cd8.jpg)](http://www.flickr.com/photos/arthit/70883201/ "Ruby Editor Plugin in action")

[ความสามารถ](http://jedit.org/ruby/features/)หลัก ๆ ของ jEdit Ruby Editor Plugin

1.  syntax highlighting แสดงสีไวยากรณ์
2.  error list บอกที่ผิด
3.  structure browser แสดงโครงสร้างโปรแกรม
4.  online API documentation คู่มือ API สด
5.  code completion ช่วยเติมโค้ด
6.  more และอื่น ๆ

นอกจาก FreeRIDE กับ SciTE ที่มากับชุดติดตั้ง Ruby แล้ว  
IDE อีกตัวที่เหมือนจะมีคนนิยม คือ [Mondrian Ruby IDE](http://www.mondrian-ide.com/) ยังเป็นเบต้าอยู่ เขียนด้วย Ruby + FOX toolkit  
เท่าที่ลองก็โอเค มี (1), (2), (3) และสั่งรัน Ruby ได้จากใน IDE เลย (ถ้ามีที่ผิด โปรแกรมจะวิ่งไปที่บรรทัดแรกที่ผิดทันที)

ถ้าแก้แต่ไฟล์ Ruby อย่างเดียว FreeRIDE น่าจะดีที่สุด  
มี (1), (2), (3), (4), สั่งรัน Ruby ได้, และใช้ IRB (Interactive Ruby) ได้ในตัวเลย

ยังไม่เห็นว่า Mondrian จะดีกว่า FreeRIDE ชัด ๆ ตรงไหน …  
อาจจะเป็นเรื่องของการจัดการโครงการ (Mondrian มีแนวคิดแบบ Project ทำนองเดียวกับ IDE ชั้นนำทั่วไป อย่าง Visual Studio, Eclipse, NetBeans, … คือเปิดไฟล์ที่เกี่ยวข้องกันเป็นกลุ่มได้)  
รวมทั้งความเร็วของตัว IDE .. เหมือน Mondrian จะเร็วกว่าหน่อย ๆ เท่าที่สังเกตตอนเปิด/ปิดโปรแกรม  
แต่ก็ยังลองเล่นทั้งสองตัวแค่แป๊บเดียว อาจจะมีอย่างอื่นที่ไม่เห็น

SciTE นี่ก็แก้ไฟล์ได้หลายแบบดี มี (1) และ (2)  
หน้าตาค่อนข้างจะดึกดำบรรพ์ไปหน่อย หรือพูดอีกอย่างคือ พื่้น ๆ ไม่มีลูกเล่นมากนัก  
ไม่มีอะไรน่าสนใจเป็นพิเศษ .. นอกจากความเบา/เล็ก (lightweight)  
นี่ว่าจะลบทิ้งอยู่

เดี๋ยวจะลองลงปลั๊กอิน shell ของ jEdit แล้วใช้ IRB ผ่าน shell plug-in  
ถ้าใช้ได้, jEdit ก็น่าจะโอเคสุดแล้ว สำหรับการแก้ไฟล์หลาย ๆ แบบ + Ruby  
แต่ต้องระวังเรื่องโหลดไฟล์ยักษ์ ๆ กรณีที่เปิดใช้ปลั๊กอินหลาย ๆ ตัว  
(เช่นเปิดไฟล์ XML ขณะใช้ปลั๊กอิน Structure Browser + XML + XML Indenter)  
เพราะถึงแม้จะเปิดใช้ได้ แต่เวลาแก้ มันจะอืด ทำงานได้ แต่รำคาญ

Emacs ? เอ่อ … ไม่รับครับ – -“
