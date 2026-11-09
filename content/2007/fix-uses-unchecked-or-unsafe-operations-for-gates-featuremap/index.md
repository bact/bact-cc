---
title: "Fix \"uses unchecked or unsafe operations\" for GATE’s FeatureMap"
date: "2007-01-10T17:50:00+07:00"
lastmod: "2007-01-10T17:50:00+07:00"
type: "post"
url: "/2007/fix-uses-unchecked-or-unsafe-operations-for-gates-featuremap/"
description: "วันนี้นั่งไล่โค้ดตัวปลั๊กอิน GATE ทั้งวัน กำลังเขียนปลั๊กอินเพื่อเอามาใช้กับโครงการที่กำลังทำอยู่ตอนนี้ที่ SIIT (เอ๊ะ ผมบอกรึยังนะ ว่าผมมาเป็นผู้ช่วยวิจัยอยู่นี่ ไว้ค่อยเล่าว่าทำอะไรละกัน ทีหลัง) ก็ใช้ GATE นี่แหละ วันนี้พยายามแก้ warning ที่เจอมาตั้งแต่วันก่อน แต่ปล่อย ๆ ไปก่อน วันนี้ได้โอกาส ก็มาต"
tag: ["fix", "gate", "java"]
textlang: "th"
wpid: 1853
---
วันนี้นั่งไล่โค้ดตัวปลั๊กอิน [GATE](http://www.gate.ac.uk/ "General Architecture for Text Engineering") ทั้งวัน

กำลังเขียนปลั๊กอินเพื่อเอามาใช้กับโครงการที่กำลังทำอยู่ตอนนี้ที่ SIIT (เอ๊ะ ผมบอกรึยังนะ ว่าผมมาเป็นผู้ช่วยวิจัยอยู่นี่ ไว้ค่อยเล่าว่าทำอะไรละกัน ทีหลัง) ก็ใช้ GATE นี่แหละ

วันนี้พยายามแก้ warning ที่เจอมาตั้งแต่วันก่อน แต่ปล่อย ๆ ไปก่อน วันนี้ได้โอกาส ก็มาตามเก็บให้เรียบร้อย

โค้ดมันคล้าย ๆ นี้:

    1: FeatureMap features = Factory.newFeatureMap();
    2: features.put("key", object);

บรรทัดที่ 2 เนี่ย พอคอมไพล์ จะทำให้เกิด warning:

    Note: MyJava.java uses unchecked or unsafe operations.
    Note: Recompile with -Xlint:unchecked for details.

ไปเจอใน [forum.java.sun.com](http://forum.java.sun.com/thread.jspa?threadID=584311) เค้าบอกว่า มันเกิดเพราะ เราไม่ได้กำหนด parameter ให้กับตัว Map (เรื่อง [generic](http://en.wikipedia.org/wiki/Generic_programming))

ลองแก้ที่โค้ดตัวเอง ไม่สำเร็จ  
ก็เลยต้องไปแก้โค้ดของ FeatureMap ของตัว GATE ซะ

ดังนี้:

ที่ไฟล์ gate/SimpleFeatureMap.java:

แก้  
`public interface SimpleFeatureMap extends Map`  
เป็น  
`public interface SimpleFeatureMap extends Map<Object, Object>`

ที่ไฟล์ gate/util/SimpleMapImpl.java:

แก้  
`class SimpleMapImpl implements Map`  
เป็น  
`class SimpleMapImpl implements Map<Object, Object>`

ลอง build GATE ดู ใช้ได้ build ผ่าน, ทดสอบรัน GATE โอเค

ลองคอมไพล์โปรแกรมตัวเอง (ที่เรียกใช้ FeatureMap) โอเค ไม่มี warning ละ เยี่ยม

ถ้าไม่มีซอร์สโค้ดแจกมา ให้ดู ให้แก้ คงทำงี้เองไม่ได้เนอะ ต้องรอเขาลูกเดียว ตั้งตา

เมลถาม(เอง)-ตอบ(เอง) เรื่องนี้เข้า[เมลกลุ่ม](http://news.gmane.org/gmane.comp.ai.gate.general) ไปละ – -“

ไปประชุมเรื่อง [YouMedia](http://bact.blogspot.com/2006/12/youfest-youmedia.html "YouFest : YouMedia - งานของคุณ : สื่อของคุณ") ก่อนนะ 😉

หมายเหตุ: นั่งเขียนที่ร้าน Cup B หยุดอยู่ที่ร้านนี้ เพราะหยุดดูข่าว iPhone ที่เค้าเปิดให้ดูหน้าร้าน (จอคอม) แล้วคนในร้านออกมาชวนคุย เราเลยนั่งทำงานอยู่ร้านนี้มันซะเลย หาที่นั่งทำงานเงียบ ๆ อยู่พอดี / Mac Cafe Mini @ Cup B

update: [Ian Roberts](http://www.dcs.shef.ac.uk/~ian/) หนึ่งในผู้ดูแล GATE [ตอบรับแล้ว](http://comments.gmane.org/gmane.comp.ai.gate.general/2606) เดี๋ยวจะแก้โค้ดใน main GATE tree ให้ 🙂

<span class="small">technorati tags:  
[GATE](http://technorati.com/tag/GATE),  
[fix](http://technorati.com/tag/fix)  
</span>
