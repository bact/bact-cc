---
title: "Open Language Tools try out"
date: "2005-08-30T16:58:00+07:00"
lastmod: "2005-08-30T16:58:00+07:00"
type: "post"
url: "/2005/open-language-tools-try-out/"
description: "ตะกี้ลองเล่น Open Language Tools, เป็นโปรแกรมช่วยงานแปลภาษา ทั้งพวกเอกสาร และโปรแกรม ในชุดจะแยกเป็นสองตัว คือ XLIFF Translation Editor กะ XLIFF Filters. ตัวแรกจะเป็นตัวแก้ไข (เป็นตัวที่ผู้แปลจะใช้ทำงาน) ส่วนตัวหลังจะเป็นตัวแปลงไฟล์ต่าง ๆ ให้อยู่ในฟอร์แมต XLIFF เพื่อให้ตัวแรกใช้. (อะไรคือ XLIFF ?) ตั"
tag: ["natural-language-processing"]
textlang: "th"
wpid: 987
---
ตะกี้ลองเล่น [Open Language Tools](https://open-language-tools.dev.java.net/), เป็นโปรแกรมช่วยงานแปลภาษา ทั้งพวกเอกสาร และโปรแกรม

ในชุดจะแยกเป็นสองตัว คือ XLIFF Translation Editor กะ XLIFF Filters. ตัวแรกจะเป็นตัวแก้ไข (เป็นตัวที่ผู้แปลจะใช้ทำงาน) ส่วนตัวหลังจะเป็นตัวแปลงไฟล์ต่าง ๆ ให้อยู่ในฟอร์แมต XLIFF เพื่อให้ตัวแรกใช้. ([อะไรคือ XLIFF ?](http://developers.sun.com/dev/gadc/technicalpublications/articles/xliff.html))

ตัว editor นี่ มี Translation Memory (TM) ให้ใช้ด้วย

## ตัวอย่างการใช้งาน

สมมติเราอยากจะแปลโมดูลใน GNOME ซักอันนึง[เป็นไทย](http://gnome-th.sourceforge.net/), ซึ่งใน GNOME เนี่ย เค้าจะใช้ไฟล์ข้อความในฟอร์แมต PO. เราก็เอาไอ้ไฟล์ PO เนี่ย ไปแปลงเป็น XLIFF ก่อน ด้วย XLIFF Filters, จากนั้นพอได้ไฟล์ XLIFF แล้ว ก็แปลด้วย XLIFF Translation Editor, พอแปลเสร็จ ก็แปลงกลับเป็น PO อีกครั้ง (ด้วย XLIFF Translation Editor)

เท่าที่ลองดู **<u>สิ่งที่ต้องปรับ ถ้าต้องการใช้กับภาษาไทย</u>** ก็คือต้องไปแก้ค่า **file.encoding** ใน registry `HKEY_CURRENT_USER/Software/JavaSoft/Prefs/org/jvnet/olt/filters/gui` (กรณี Windows) หรือไฟล์ `~/.java/.userPrefs/org/jvnet/olt/filters/gui/prefs.xml` (กรณี UNIX, รวมถึง Linux และ Mac OS X) โดยแก้เป็น **utf-8** (หรืออื่น ๆ ตามไฟล์ต้นทาง) — สำหรับค่าอื่น ๆ ถ้าดูแล้วไม่ตรง (เช่นค่าสองอันสุดท้าย ซึ่งถ้าเราไม่ได้ติดตั้งในไดเรกทอรีปริยายเนี่ย มันจะไม่ตรง) ก็ปรับให้ตรงซะ, ระวังในการแก้ไขค่าด้วย ถ้าต้องการใช้ / ให้พิมพ์ // หรือถ้าต้องการใช้ A ตัวใหญ่ ให้พิมพ์ /A  
  
[![XLIFF Filters configuration](https://photos32.flickr.com/38542883_6c30a3039e_o.png)](http://www.flickr.com/photos/arthit/38542883/ "XLIFF Filters configuration")

หลังจากแก้แล้ว ก็เรียกโปรแกรม XLIFF Filters ขึ้นมา ลากไฟล์ .po ไปใส่ ก็จะได้ไฟล์ .xlz ออกมา ที่ไดเรกทอรีเดียวกัน (ไฟล์ .xlz นี้ ที่จริงเป็นแพ็คเกจ zip ข้างในจะมีไฟล์ .xlf ซึ่งเป็นไฟล์ที่เก็บข้อความจริง ๆ อีกที – ทำนองเดียวกะ [OpenDocument](http://en.wikipedia.org/wiki/OpenDocument) ที่ OpenOffice.org ใช้น่ะ)

การแก้ไข ก็เรียกโปรแกรม XLIFF Translation Editor ขึ้นมา. ก่อนจะเริ่มแปลได้ เราต้องเริ่มโครงการใหม่ซะก่อน ก็ไปที่เมนู, เลือก File → New Project… โปรแกรมจะให้ใส่ชื่อโครงการ, ภาษาต้นทาง, ภาษาปลายทาง. หรือถ้ามีโครงการเดิมอยู่แล้ว ก็เปิดขึ้นมาได้เลย

พอเปิดโครงการแล้ว ก็เลือก File → Open เพื่อเปิดไฟล์ที่จะแปล ก็คือไฟล์ .xlz ที่ได้มาตะกี้น่ะเอง  
[![XLIFF Translation Editor 1.2alpha](https://photos26.flickr.com/38544530_bd3f23fdcb.jpg)](http://www.flickr.com/photos/arthit/38544530/ "XLIFF Translation Editor")

ระหว่างแปล/แปลเสร็จ จะแปลงกลับเป็นฟอร์แมตเดิม (ก่อนจะถูกแปลงเป็น XLIFF, กรณีนี้ก็คือ PO) ก็ไปที่เมนู, เลือก Tools → Convert to Original…

## ชนิดไฟล์ XLIFF Filters แปลงได้

= ชนิดไฟล์ที่ XLIFF Translation Editor แก้ได้

ชนิดไฟล์เอกสาร: HTML, Docbook SGML, JSP, XML (ทั่วไป – ต้องการ configuration file สำหรับไฟล์ XML แต่ละชนิด), OpenOffice.org (sxw, sxc, sxi), OpenDocument (odw, odc, odi), Plain text

ชนิดไฟล์โปรแกรม: PO (gettext), Msg/tmsg (catgets), Java .properties, Java ResourceBundle, Mozilla .DTD resource files — ถ้าอยากจะใช้แปลโปรแกรมอื่น ๆ ที่ไม่ได้อยู่ในรายการนี้ ลองไปที่ [translate.sourceforge.net](http://translate.sourceforge.net/) มันจะมีตัวแปลงอยู่พอสมควร เช่นจากฟอร์แมตข้อความของ OpenOffice.org เป็น PO (แล้วค่อยแปลง PO เป็น XLIFF อีกที)

พูดถึงถ้าเกิดว่าเราแปลหลาย ๆ โปรแกรม เช่น GNOME, Mozilla, หรืออาจจะโปรแกรม Java ด้วย (สมมติเช่น Lexitron หรือโปรแกรมอื่น ๆ อย่าง Azureus, ตัว BitTorrent client ยอดนิยม) แล้วแปลโดยใช้ translation editor ตัวเดียวกัน ก็คงสะดวกขึ้น (มั้ง) แชร์ translation memory กันได้ด้วย

## ลองเอง

Open Language Tools ใช้ได้กับทุกแพลตฟอร์มที่รัน Java ได้, ที่ทดสอบวันนี้ ลองบน Java 5 + Windows XP Service Pack 2. ดาวน์โหลดได้ที่ [open-language-tools.dev.java.net](https://open-language-tools.dev.java.net/)

อ่านเพิ่ม: [Quick Start](https://open-language-tools.dev.java.net/filters/xliff-filters-quickstart.html)
