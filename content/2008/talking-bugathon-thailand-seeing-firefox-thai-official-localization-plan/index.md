---
title: "talking BugAThon Thailand, seeing Firefox Thai Official Localization plan"
date: "2008-03-30T22:03:00+07:00"
lastmod: "2011-01-12T07:46:43+07:00"
type: "post"
url: "/2008/talking-bugathon-thailand-seeing-firefox-thai-official-localization-plan/"
description: "[Mozilla BugAThon Thailand report in English] molecularck รายงานสรุป BugAThon Thailand (ไม่ใช่ Bangkok เพราะจับได้ว่าพี่เทพก็ออนไลน์ดูอยู่ด้วย จากคอมเมนท์ในบั๊กเรื่องฟอนต์) เมื่อวันเสาร์ที่ผ่านมาเอาไว้อย่างละเอียด พร้อมรูปถ่ายบรรยากาศ (ลงใน Blognone ด้วย) เรื่องบั๊กต่าง ๆ ที่ปิดไปแล้วบ้าง หรือได้ข้อ"
categories: ["places"]
tag: ["bangkok", "bugathon", "bugs", "community", "events", "firefox", "free-softwares", "mozilla", "open-source", "thai"]
textlang: "th"
wpid: 2311
---
*\[[Mozilla BugAThon Thailand report in English](http://molecularck.com/node/53 "by molecularck")\]*

molecularck **[รายงานสรุป BugAThon Thailand](http://molecularck.com/node/52)** (ไม่ใช่ Bangkok เพราะจับได้ว่า[พี่เทพ](http://twitter.com/theppitak)ก็ออนไลน์ดูอยู่ด้วย จากคอมเมนท์ในบั๊กเรื่องฟอนต์) เมื่อวันเสาร์ที่ผ่านมาเอาไว้อย่างละเอียด พร้อมรูปถ่ายบรรยากาศ ([ลงใน Blognone ด้วย](http://blognone.com/node/7367))

เรื่องบั๊กต่าง ๆ ที่ปิดไปแล้วบ้าง หรือได้ข้อสรุปแล้วบ้าง หรือที่เปิดใหม่นิดหน่อย อ่านได้จากในรายงานเลยครับ คุณ molecularck เก็บไว้หมดแล้ว ผมขอเล่าบรรยากาศทั่ว ๆ ไปละกัน

งานนี้มี [นิตยสาร OpenSource2day](http://www.opensource2day.com/) และ[รายการ แบไต๋ไฮเทค](http://www.beartai.com/) มาร่วมด้วย (เสียดายที่พวกเราไม่ได้คุยกันซักเท่าไหร่ เพราะทุกคนก้มหน้าก้มตาทดสอบและคุยเรื่องบั๊กกันอยู่) ยังไงก็ขอขอบคุณมาก ๆ ที่ให้ความสนใจการรวมตัวของชุมชนผู้ใช้เล็ก ๆ อย่างนี้ครับ

พวกเราวันนั้นรวม ๆ กันแล้ว ประมาณ 12-13 คน (มีใครบ้าง ไปดูในรายงานของ molecularck เองนะ) บรรยากาศก็เรื่อย ๆ เป็นกันเอง อาจจะเพราะคุ้นหน้าคุ้นตากันมาก่อนบ้างแล้ว จากงาน [BarCamp Bangkok](http://www.barcampbangkok.org/ "บาร์แคมป์ บางกอก") เมื่อไม่กี่เดือนก่อน ตอนแรก ๆ อาจจะเนือยกันไปหน่อย แบบว่าไม่รู้จะเริ่มยังไง แล้วก็ติดคุยทักทายกันอยู่ จน[พี่กำธร](http://twitter.com/kamthorn)ออกปากเริ่ม งานก็เริ่มกัน พอเครื่องติด ก็เริ่มสนุก  
ตัวชูโรงของวันนั้นเห็นจะเป็น [dtinth](http://twitter.com/dtinth "น้องไทย") ([dt.in.th](http://dt.in.th/)) ที่แกะ preference แกะซอร์สโค้ด และสารพัด css, html ได้อย่างช่ำชอง แจกแจงบั๊กให้ฟัง จนพวกพี่ ๆ ตามกันแทบไม่ทัน ([Bug 425915](https://bugzilla.mozilla.org/show_bug.cgi?id=425915) นี่ก็มาจากน้องเขา) เห็นแล้วก็อดนึกไม่ได้ว่า เอ่อ.. ตอนอายุเท่าน้อง เราทำอะไรอยู่หว่า – -“

ก็ปิด ๆ ไล่กันไปเท่าที่ทำได้ คือไล่จนหมดที่มัน block (ขวางทาง) [Bug 65896](https://bugzilla.mozilla.org/show_bug.cgi?id=65896) (Thai support tracker bug เป็นบั๊กแม่ เอาไว้ตามบั๊กภาษาไทยทั้งหมด) โดยบางอันที่ไม่ได้ปิด ก็มีการพิจารณา [severity](https://bugzilla.mozilla.org/page.cgi?id=fields.html#bug_severity) (ความร้ายแรง) เสียใหม่

ระหว่างทำอยู่ [theniw](http://twitter.com/theniw) ก็เอาปลั๊กพ่วงมาเพิ่มให้อีกอัน แบตกำลังจะหมดพอดี thx thx

สรุปตอนนี้ บั๊กที่ยังเปิดอยู่คือ (แยกตามประเภท ใน \[..\] เป็น ความร้ายแรง):

Font Preferences ค่าตัวเลือกฟอนต์

- [Bug 284265](https://bugzilla.mozilla.org/show_bug.cgi?id=284265) \[ปกติ\] – ตั้งค่าเริ่มแรกของฟอนต์ไทย

Input Method การป้อนข้อมูล

- [Bug 353776](https://bugzilla.mozilla.org/show_bug.cgi?id=353776) \[ปกติ\] – การรองรับการดึงข้อความรอบ ๆ ตำแหน่งเคอร์เซอร์ เพื่อจะได้ทำการตรวจสอบลำดับการป้อน (input sequence checking) ได้
- [Bug 425900](https://bugzilla.mozilla.org/show_bug.cgi?id=425900) \[เล็กน้อย\] – ไม่ควรอนุญาตให้พิมพ์อักษรบนล่างที่ตอนต้นบรรทัด (บั๊กนี้จะถูกแก้ ถ้าบั๊ก 353776 ถูกแก้ – แต่ก็มีวิธีแก้โดยไม่ต้องมี sequence checking แบบเต็ม ๆ ก็ได้ คือเช็คแค่ตัวแรกไปเลย เป็นวิธีทื่อ ๆ)
- [Bug 425915](https://bugzilla.mozilla.org/show_bug.cgi?id=425915) \[ขอเพิ่ม\] \[บั๊กใหม่\] – ตัดคำสำหรับการเลือกข้อความและเลื่อนเคอร์เซอร์

Formatting การจัดหน้าตาเอกสาร

- [Bug 156881](https://bugzilla.mozilla.org/show_bug.cgi?id=156881) \[ขอเพิ่ม\] – ขีดเส้นใต้ไม่ควรทับอักษรล่าง พวก ฐฎฤ อุอู yqj (ต้องดูสเปค CSS [text-decoration-mode](http://www.w3.org/TR/css3-text/#text-decoration-mode) ด้วย ว่ากำหนดเรื่องนี้ไว้รึเปล่า)

UI หน้าตาโปรแกรม

- [Bug 157541](https://bugzilla.mozilla.org/show_bug.cgi?id=157541) \[เล็กน้อย\] – ช่อง textfield สูงไม่พอแสดงผลอักษรบนล่างของตัวเขียนไทย
- [Bug 425912](https://bugzilla.mozilla.org/show_bug.cgi?id=425912) \[ปกติ\] \[ไม่เกี่ยวกับภาษาไทย\] \[บั๊กใหม่\] – dropdown list ของ Minimum font size แสดงเป็นช่องว่าง ๆ (และ ผอม ๆ ในลินุกซ์) ในตอนแรกที่ยังไม่ได้กำหนดค่าอะไรไว้

พวก \[ขอเพิ่ม\] นี่คือ มีก็ดี ไม่มีก็ไม่เป็นไรมาก; ส่วน \[เล็กน้อย\] คือ ถ้าไม่แก้มันก็ขัด ๆ แต่ก็พอใช้งานได้

จริง ๆ ในตอนแรก ทุกคนก็ไม่ได้จำกัดไว้ว่า จะต้องเป็น Mozilla อย่างเดียว แต่ทำไปทำมา ในวันนั้นก็ดูกันแต่เรื่อง Mozilla แล้วก็หมดเวลาพอดี (2 ทุ่มร้านเค้าจะปิดไฟ Earth Hour โลกร้อนอะไรนั่น) แต่ก็คิดว่าเป็นเรื่องที่ทุกคนอยากดันในช่วงนี้ด้วยล่ะ เอาให้มันทัน Firefox 3 ที่จะออกเดือนมิถุนายนนี้

ตอนท้าย ๆ มี[คุณมะระ](http://twitter.com/gumara) และ[ชาว Ubuntu Club](http://ubuntuclub.com/) มาเยี่ยมเยียน แล้วก็มี [ฮันท์](http://twitter.com/hunt)+(น้องอะไรนะ) ([Zickr](http://zickr.com/)) และ [กล้า](http://twitter.com/nytonkla)+ตาล ([duocore](http://duocore.tv/)) ตามมาด้วย (พวกนี้ไปข้าวสารกันต่อ เห็นจาก twitter ของ [pittaya](http://twitter.com/pittaya) ซึ่งขานั้นเขาก็ไปด้วย)

หลังจากทำเรื่องบั๊กเสร็จกัน [kengggg](http://keng.ws/) ก็เปิดคุยประเด็นเรื่อง จะทำยังไง **ให้มี Official Localization ภาษาไทยให้ได้ ใน Firefox 3 นี้ — ซึ่งถ้าอยากให้ได้ตามนั้น ก็ต้องแปลแล้วส่งรีวิวให้ทันในช่วง RC1**

เรื่องแปลนี้ [มาร์ค](http://isriya.com/) ได้เริ่มไว้แล้วตอน Firefox 1.5 และ [พี่สัมพันธ์](http://www.osdev.co.th/) ก็ได้เอาไปทำเป็น [Thai Firefox Community Edition](http://www.osdev.co.th/index.php?option=com_remository&Itemid=54&func=fileinfo&id=19) แต่หลังจากนั้นก็ไม่ได้ทำต่อ

ระหว่างคุยกัน ก็เปิด ๆ ดูเอกสารเกี่ยวกับเรื่องการทำ Firefox localization และการจะได้เป็น official localization:

- Mozilla: *[Becoming an Official Localization](http://wiki.mozilla.org/L10n:Becoming_an_Official_Localization)*
- Firefox 3: *[L10n Requirements](http://wiki.mozilla.org/Firefox3/L10n_Requirements)*

ซึ่งจากเอกสารเหล่านั้น งานที่ต้องทำนั้น รวมถึงสิ่งเหล่านี้ด้วย:

- ปิดบั๊กต่าง ๆ ที่เป็น showstopper สำหรับ official localization (ไม่แน่ใจว่ามีไหม?)
- งานแปล อันนี้แน่นอน (ใครสนใจร่วมแปล อยากรู้ว่าจะทำได้ยังไง ลองดู รายงานพิเศษ BN: [ระดมพลนักแปล](http://blognone.com/node/7349)) โดย tracker bug สำหรับการแปลนี้คือ [Bug 226420](https://bugzilla.mozilla.org/show_bug.cgi?id=226420)
- ทำ[หน้าเว็บไฟร์ฟ็อกซ์](http://wiki.mozilla.org/L10n:Web_parts#Firefox_in-product_pages) สำหรับภาษไทย (เช่น หน้าเว็บแรก หน้า about หน้าแนะนำการปรับแต่ง)
- คัดเลือก ลิงก์ และ search plug-ins แบบไทย ๆ

ใครสนใจก็คุยกันครับ ส่งข้อความ tweet ไปหา [kengggg](http://twitter.com/kengggg) ก็ได้ หรือ[ผม](http://twitter.com/bact)ก็ได้ (แต่โอกาสที่เก่งจะตอบ มีสูงกว่าผมเยอะครับ :P)

**[Bug 299423](https://bugzilla.mozilla.org/show_bug.cgi?id=299423 "[th] Thai: Firefox")** เป็น tracker bug ที่เปิดเอาไว้สำหรับติดตามเรื่องการทำ Thai Official Localization นี้

**ใครสนใจตามข่าวบั๊กไหน คลิกเข้าไปดูบั๊กนั้น แล้วเพิ่มอีเมลของคุณลงในช่อง cc ได้ครับ**

ขอบคุณทุก ๆ คน และขอขอบคุณร้าน Coffee World สีลม สำหรับสถานที่ด้วยครับ (ขออภัยถ้าพวกเราเสียงดังเกินไปในบางครั้งครับ บางช็อตคุยกันตื่นเต้นไปหน่อย – -“) ส่วนถ้าใครได้แวะไป อยากหาอะไรหนัก ๆ ใส่ท้องหน่อย แนะนำ พานินี่โบโลญญ่าไก่ นะครับ ไก่+ชีส+พริกหวาน อร่อยมาก ๆ ชิ้นเบ้อเร่อเลย

โพสต์ที่เกี่ยวข้อง: [Call for Thai Firefox/Gecko BugAThon Day](http://bact.blogspot.com/2008/03/call-for-thai-firefoxgecko-bugathon-day.html)

<span class="small">technorati tags:  
[BugAThon](http://technorati.com/tag/BugAThon),  
[Firefox](http://technorati.com/tag/Firefox),  
[Thailand](http://technorati.com/tag/Thailand)  
</span>
