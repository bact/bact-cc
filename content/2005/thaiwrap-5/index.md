---
title: "ThaiWrap รุ่น 5"
date: "2005-02-09T04:37:00+07:00"
lastmod: "2011-05-13T12:24:35+07:00"
type: "post"
url: "/2005/thaiwrap-5/"
description: "(บล็อกเก่า ThaiWrap bookmarklet, Auto thaiWrap()) รายการเปลี่ยนแปลง: ตัวแบ่งคำ เปลี่ยนจาก <WBR> มาใช้ zero-width space (U+200B) แทน เนื่องจาก Opera ไม่รู้จัก <WBR> เพิ่มการตรวจเบราเซอร์ เพื่อข้ามการทำงานทั้งหมด ถ้าใช้ Internet Explorer (เหตุผล: 1. จะได้ไม่เสียเวลา เพราะ IE ตัดคำได้อยู่แล้ว 2. IE แสด"
categories: ["coling", "computer"]
tag: ["javascript", "me", "programming", "text-processing", "thai", "unicode", "word-break"]
textlang: "th"
wpid: 544
---
(บล็อกเก่า [ThaiWrap bookmarklet](http://bact.blogspot.com/2004/12/thaiwrap-bookmarklet.html), [Auto thaiWrap()](http://bact.blogspot.com/2005/01/auto-thaiwrap.html))

รายการเปลี่ยนแปลง:

- ตัวแบ่งคำ เปลี่ยนจาก \<WBR\> มาใช้ [zero-width space](http://www.fileformat.info/info/unicode/char/200b/index.htm) (U+200B) แทน เนื่องจาก [Opera ไม่รู้จัก \<WBR\>](http://www.quirksmode.org/oddsandends/wbr.html)
- เพิ่ม[การตรวจเบราเซอร์](http://bact.blogspot.com/2005/02/blog-post.html) เพื่อข้ามการทำงานทั้งหมด ถ้าใช้ Internet Explorer (เหตุผล: 1. จะได้ไม่เสียเวลา เพราะ IE ตัดคำได้อยู่แล้ว 2. IE แสดงผล zero-width space ไม่ได้)

ตอนนี้ยังเหลือปัญหา เรื่องไม่ทำงานกับเฟรมที่ซ้อนเฟรม ไล่ [DOM reference](http://studio.tellme.com/dom/ref/) ตะกี้นี้ เจอละว่ามันผิดตรงไหน (เราไปใช้ window.frames ซึ่งมันจะส่งค่ากลับเฉพาะ frames ระดับบนสุดเท่านั้น, คาดว่า. นอกจากนั้น มันยังไม่อยู่ใน spec ด้วย – อันตราย) แต่ยังไม่รู้จะแก้ไง ขอค้นก่อน

[ThaiWrap bookmarklet/JavaScript, Release 5](http://www.siit.net/members/art/thaiwrap.html)
