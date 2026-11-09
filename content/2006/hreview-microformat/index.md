---
title: "hReview microformat"
date: "2006-06-28T05:04:00+07:00"
lastmod: "2006-06-28T05:04:00+07:00"
type: "post"
url: "/2006/hreview-microformat/"
description: "hReview เป็น microformat สำหรับบทวิจารณ์ เช่น สินค้า ภาพยนตร์ พวก Microformats นี่ สั้น ๆ ก็คือ เป็นการยัดความหมาย (semantic) ลงไปใน (X)HTML ทำให้ข้อความชิ้นเดียวกัน อ่านได้ทั้งจากเครื่องและจากคน พูดอีกแบบก็คือ มีข้อความอยู่ แล้วเราก็ติด “ป้ายอธิบาย” ให้ข้อความส่วนต่าง ๆ ตัวอย่างเช่น ระดับความน่าดู:"
tag: ["microformats"]
textlang: "th"
wpid: 1520
---
[hReview](http://microformats.org/wiki/hreview) เป็น <a href="http://en.wikipedia.org/wiki/Microformats" data-ref="tag">microformat</a> สำหรับบทวิจารณ์ เช่น สินค้า ภาพยนตร์

พวก Microformats นี่ สั้น ๆ ก็คือ เป็นการยัดความหมาย (semantic) ลงไปใน (X)HTML ทำให้ข้อความชิ้นเดียวกัน อ่านได้ทั้งจากเครื่องและจากคน พูดอีกแบบก็คือ มีข้อความอยู่ แล้วเราก็ติด “ป้ายอธิบาย” ให้ข้อความส่วนต่าง ๆ ตัวอย่างเช่น

`ระดับความน่าดู: <span><span class="rating">5</span> จาก 5 ดาว </span>`

ซึ่งจะแสดง ให้คนอ่าน เป็น “ระดับความน่าดู 5 จาก 5 ดาว”

ส่วนเครื่อง ก็จะอ่านเลข 5 ที่อยู่ใน \<span class=”rating”\>5\</span\> ไป

อย่าง \<a href=”…” rel=”tag”\>5\</a\> ที่ใช้ทำ tag นี่ก็ใช่ เป็น microformat เหมือนกัน ถ้าลิงก์ไหนมี @rel เป็น tag ก็หมายถึง ไอ้นี่คือ tag (ดูตัวอย่างด้านล่าง กดดูโค้ด HTML เอา)

via [Green Ruby](http://greenruby.blogspot.com/2006/06/hreview-microformats.html)

**tags:** [hReview](http://technorati.com/tag/hreview) [microformats](http://technorati.com/tag/microformats)
