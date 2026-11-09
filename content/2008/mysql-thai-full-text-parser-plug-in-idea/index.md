---
title: "MySQL Thai full-text parser plug-in idea"
date: "2008-02-24T14:59:00+07:00"
lastmod: "2011-05-12T12:03:48+07:00"
type: "post"
url: "/2008/mysql-thai-full-text-parser-plug-in-idea/"
description: "MySQL 5.1 allows us to use a customized full-text parser. poakpong ถามเรื่อง fulltext ในฐานข้อมูล MySQL ว่าเอาไว้ทำอะไร ก็คือมันเอาไว้ระบุไว้ที่ช่องข้อมูล (field) ประเภทข้อความ (char, varchar, text) เพื่อบอกให้ MySQL มันทำดัชนี (index) สำหรับการค้นหาแบบ full-text search น่ะ ที่เคย ๆ เขียนกัน เวลาจะห"
categories: ["computer"]
tag: ["free-softwares", "ideas", "mysql", "natural-language-processing", "open-source", "programming", "search-engines", "thai"]
textlang: "th"
wpid: 2282
---
MySQL 5.1 allows us to use [a customized full-text parser](http://dev.mysql.com/doc/refman/5.1/en/plugin-full-text-plugins.html).

[poakpong](http://poakpong.com/ "ปกป้อง.คอม") ถามเรื่อง [fulltext](http://www.onlamp.com/pub/a/onlamp/2003/06/26/fulltext.html) ในฐานข้อมูล MySQL ว่าเอาไว้ทำอะไร

ก็คือมันเอาไว้ระบุไว้ที่ช่องข้อมูล (field) ประเภทข้อความ (char, varchar, text) เพื่อบอกให้ MySQL มันทำดัชนี (index) สำหรับการค้นหาแบบ [full-text search](http://en.wikipedia.org/wiki/Full_text_search "@ Wikipedia") น่ะ

ที่เคย ๆ เขียนกัน เวลาจะหาอะไรใน MySQL เราก็จะใช้ `LIKE "%คำที่หา%"`  
โดย LIKE มันจะวิ่งไปเปรียบเทียบข้อความในแต่ละช่องข้อมูล ทำนอง regular expression

ส่วนกรณี [full-text search](http://dev.mysql.com/doc/refman/5.1/en/fulltext-search.html) ใน MySQL จะใช้คำสั่ง `MATCH (ชื่อฟิลด์) AGAINST (คำที่หา)`  
ซึ่งมันจะค้นจากดัชนีคำที่ MySQL ทำไว้ล่วงหน้า ซึ่งการค้นหาที่ตัวดัชนีแทนที่จะไปหาในตัวข้อความทั้งหมดนี้ ก็จะทำให้การค้นหามีประสิทธิภาพดีกว่า

อย่างไรก็ตาม การใช้ full-text search นี้ ก็ยังมีปัญหาสำหรับภาษาไทย นั่นก็คือ ตัวทำดัชนีคำน่ะ มันยังไม่รองรับภาษาไทย-ภาษาที่ต้องตัดคำก่อน (มีรองรับภาษาจีน/ญี่ปุ่นนิดหน่อย)

full-text search จึงยังใช้ไม่ได้สำหรับภาษาไทย ต้องใช้ LIKE กันไปก่อน

ใน [MySQL รุ่น 5.1](http://dev.mysql.com/doc/refman/5.1/en/index.html "MySQL 5.1 Reference Manual") (ตอนนี้ยังเป็น Release Candidate อยู่) ปัญหานี้ดูเหมือนจะมีทางออกได้ (ถ้ามีคนลงแรง)  
เพราะ MySQL 5.1 เปิดช่องให้เขียน [plug-in](http://dev.mysql.com/doc/refman/5.1/en/plugin-api.html "The MySQL Plugin Interface") มาเสริมการทำงานได้ ซึ่งรวมถึง [full-text parser plug-in](http://dev.mysql.com/doc/refman/5.1/en/plugin-full-text-plugins.html "Full-Text Parser Plugins") ด้วย

full-text parser นี่ มีเอาไว้สร้างรายการคำเพื่อเอาไปใส่ในดัชนี

**ถ้าเรามี full-text parser ที่สร้างรายการคำไทยได้ เราก็จะสามารถใช้ฟังก์ชั่น full-text search บน MySQL กับภาษาไทยได้ทันที** ที่ระดับฐานข้อมูลเลย (แน่นอน เราต้องมีสิทธิลงปลั๊กอินที่ว่าลงในเซิร์ฟเวอร์ฐานข้อมูลด้วย ซึ่งในกรณีเราไปเช่าเว็บโฮสต์คนอื่นใช้ ก็คงลำบากหน่อย แต่ถ้าเป็นเครื่องเราเอง ก็ไม่มีปัญหา)

ไลบรารีตัดคำไทยที่ใช้งานได้นั้น เราก็มีแล้ว เช่นใน [libthai](http://linux.thai.net/projects/libthai/) หรือจะใช้ [ICU](http://www.icu-project.org/ "International Components for Unicode")/libicu ก็ได้ แม้ทั้งหมดนี้จะต้องมีการปรับแต่งเพื่อการสร้างดัชนีด้วย (ลักษณะของคำที่ตัดออกมาเพื่อจัดหน้ากระดาษ เพื่อทำดัชนี เพื่อการแปล เพื่องานที่ต่างกัน ก็มีลักษณะแตกต่างกัน) แต่คิดว่าน่าจะอยู่ในวิสัยที่จะทำได้

เป็นโครงงานจบการศึกษา – senior project – [Google Summer of Code](http://code.google.com/soc/) – ประกวด [NSC](http://www.nectec.or.th/nsc "National Software Contest") … ??

(ภาษาโปรแกรม C หรือ C++)

- **[วิธีเขียนปลั๊กอิน MySQL](http://dev.mysql.com/doc/refman/5.1/en/plugin-writing.html)**
- **[ตัวอย่างโครงสร้างปลั๊กอิน full-text parser](http://dev.mysql.com/doc/refman/5.1/en/plugin-api-type-specific.html)**
- [โครงการ full-text parser ต่าง ๆ ที่ MySQL Forge](http://forge.mysql.com/projects/browse-by-category.php?cat=105) (ตัว [n-gram full-text parser](http://mysqlbigram.googlepages.com/home) น่าสนใจ)

(อาจจะมีคนทำอยู่/เสร็จแล้วก็ได้ … เหมือน [อ.ธวัชชัย](http://gotoknow.org/blog/averageline) กับ [พี่สัมพันธ์](http://osdev.co.th/) เคยสนใจ (แต่ตอนนั้นโครงสร้างพื้นฐานยังไม่อำนวยให้แก้ไขได้ในลักษณะปลั๊กอินเช่นนี้) … ใครรู้อะไรก็แจ้งข่าวหน่อยครับ 😉 )

<span class="small">technorati tags: [MySQL](http://technorati.com/tag/MySQL), [Thai](http://technorati.com/tag/Thai), [plug-in](http://technorati.com/tag/plugin), [full-text search](http://technorati.com/tag/full-text+search)</span>
