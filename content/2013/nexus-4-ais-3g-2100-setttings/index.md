---
title: "ตั้งค่า Nexus 4 ให้ใช้เน็ตบน AIS 3G 2100"
date: "2013-07-14T14:00:00+07:00"
lastmod: "2013-07-14T14:09:06+07:00"
type: "post"
url: "/2013/nexus-4-ais-3g-2100-setttings/"
description: "วิธีตั้งค่า Nexus 4 ให้ใช้ mobile internet และ MMS บนเครือข่าย AIS 3G ใหม่"
categories: ["computer", "internet"]
tag: ["2100mhz", "3g", "ais", "android", "nexus-4"]
textlang: "th"
wpid: 3331
---
ติดตั้ง APN เพื่อใช้อินเทอร์เน็ต/MMS บนเครือข่ายใหม่ AIS 3G 2100 MHz สำหรับ Nexus 4 (LG, Android 4.2.2) — [ในเว็บ AIS จะไม่มีข้อมูลรุ่นนี้](http://www.ais.co.th/3g/setting3g.html) (โทรถาม call center เขาก็ดูตามในเว็บ) แต่ลองเซ็ตตามนี้แล้วเวิร์กครับ

ขั้นตอนคร่าวๆ มี 3 สเต็ป

1.  อันดับแรก ลงทะเบียนใช้บริการก่อน โดยไปที่หน้าจอโทรออก กด *\*988\*เลขที่บัตรประชาชน\*1175#* แล้วกดโทรออก
2.  สักพักจะได้รับ SMS ตอบกลับ เมื่อได้รับแล้วก็ปิดเครื่อง เปิดใหม่
3.  เพิ่ม APN ใหม่ เพื่อให้ใช้เน็ต-รับส่ง MMS บนเครือข่าย 2100 MHz ได้ (เราจะเพิ่ม APN 2 ตัว ตัวนึงของเน็ต อีกตัวของ MMS) โดยไปที่ Settings -\> More… -\> Mobile networks -\> Access Point Names

การไปที่หน้า Access Point Names เพื่อเพิ่ม APN ดูตามรูปนี้ (คลิกเพื่อดูรูปใหญ่) ส่วนการใส่ค่าต่างๆ ของแต่ละ APN ดูด้านล่างครับ  
[![ตั้งค่า AIS 3G 2100 บน Nexus 4](/f/2013/07/ais-3g-2100-nexus-4-android-lg-settings-918x1024.png)](/f/2013/07/ais-3g-2100-nexus-4-android-lg-settings.png)

## เพิ่ม APN Internet

ในหน้า Access Point Names ที่เมนูมุมขวาบน กดเลือก New APN แล้วใส่ข้อมูลตามนี้

Name (ชื่อ)  
AIS Internet

APN  
internet

Authentication type (ประเภทการรับรอง)  
CHAP

APN type (ชนิด APN)  
default

เสร็จแล้วกด Save (บันทึก)

## เพิ่ม APN MMS

ในหน้า Access Point Names ที่เมนูมุมขวาบน กดเลือก New APN แล้วใส่ข้อมูลตามนี้

Name (ชื่อ)  
AIS MMS

APN  
mms

MMSC  
http://mms.ais.co.th

MMS proxy (MMS พร็อกซี)  
203.170.229.34

MMS port (พอร์ต MMS)  
8080

Authentication type (ประเภทการรับรอง)  
CHAP

APN type (ชนิด APN)  
mms

เสร็จแล้วกด Save (บันทึก)

เท่านี้ก็น่าจะใช้ได้แล้วครับ

\*\*ข้อควรระวังสำหรับผู้จะเดินทางไปต่างประเทศและจะใช้ roaming คือ ตอนนี้ตัวเครือข่าย AIS 3G ยังไม่รองรับ roaming ครอบคลุมเท่ากับเครือข่าย AIS เดิม ก่อนเดินทางควรโทรเช็คศูนย์ก่อนครับ

ข้อมูลจาก [AIS 3G 2100](http://www.ais.co.th/3g/setting3g.html) (ใช้ตาม Galaxy Nexus)
