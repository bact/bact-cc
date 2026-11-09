---
title: "(re)CAPTCHA = Human OCR"
date: "2007-05-31T13:36:00+07:00"
lastmod: "2011-01-12T07:43:37+07:00"
type: "post"
url: "/2007/recaptcha-human-ocr/"
description: "ไอเดียโคตรดีอ่ะ CNN: Web registration tool digitizes books But von Ahn said OCR doesn’t always work on text that is older, faded or distorted. In those cases, often the only way to digitize the works is to manually type them into a computer. Von Ahn is working with the Internet Archive, which runs s"
categories: ["informatics"]
tag: ["captcha", "ideas", "natural-language-processing"]
textlang: "th"
wpid: 2104
---
ไอเดียโคตรดีอ่ะ

CNN: [Web registration tool digitizes books](http://www.cnn.com/2007/TECH/05/29/blather.to.books.ap/index.html)

> But von Ahn said **OCR doesn’t always work on text that is older, faded or distorted. In those cases, often the only way to digitize the works is to manually type them into a computer.**
>
> Von Ahn is working with the Internet Archive, which runs several book-scanning projects, to use CAPTCHAs for this instead. **Internet Archive scans 12,000 books a month and sends von Ahn hundreds of thousands of files that are images that the computer doesn’t recognize.** Those files are downloaded onto von Ahn’s server **and split up into single words that can be used as CAPTCHAs** at sites all over the Internet.
>
> **If enough users decipher the CAPTCHAs in the same way, the computer will recognize that as the correct answer.**

นักวิจัยที่ มหาวิทยาลัยคาร์เนกีเมลอน สร้างระบบให้คนช่วยงาน [OCR](http://en.wikipedia.org/wiki/Optical_character_recognition "optical character recognition") (แปลง ภาพข้อความ เป็น ข้อความ เช่นการสแกนหนังสือให้กลายเป็นไฟล์เอกสารในคอม) ผ่าน [CAPTCHA](http://en.wikipedia.org/wiki/CAPTCHA) (ภาพตัวอักษรสำหรับแยกแยะว่าผู้ใช้เป็นมนุษย์หรือคอมพิวเตอร์) ตามเว็บไซต์ต่าง ๆ บนอินเทอร์เน็ต

ไอเดียก็คือ ในการทำ OCR เนี่ย หลายครั้งที่คอมพิวเตอร์มันไม่สามารถแยะแยะตัวอักษรได้ อาจจะเพราะตัวอักษรมันบิดเบี้ยว เลือน หรือใช้ฟอนต์ประหลาด  
ถ้าเกิดกรณีนี้ ก็ต้องให้คนมานั่งพิมพ์เองล่ะ คอมมันช่วยไม่ได้

เห็นอย่างนี้แล้ว ทางทีมวิจัย ก็เลยเกิดพุทธิไอเดีย ปิ๊งขึ้นมาได้ว่า เอ้อ มันก็คล้าย ๆ กับไอ้ CAPTCHA นี่นา ที่เวลาเราจะล็อกอินหรือโพสต์ข้อความอะไรในเว็บหลาย ๆ ที่เดี๋ยวนี้ (เช่น วิกิพีเดีย หรือ Blogger ถ้าไม่ได้ล็อกอิน) เราจะต้องพิมพ์มันอยู่แล้ว – วัน ๆ นึง มีคนต้องพิมพ์ไอ้เจ้า CAPTCHA นี่ไม่รู้เท่าไหร่ต่อเท่าไหร่ – อย่ากระนั้นเลย ก็หาทางเอาแรงงานพวกนี้มาช่วยงานซะ อย่าให้เสียเปล่า

เขาก็จัดแจง ตัดแบ่งเจ้าเอกสารที่มีปัญหา ทำ OCR ตัวเครื่องไม่ได้ ออกมาเป็นคำย่อย ๆ แล้วก็เอาคำพวกนั้นไปเป็น CAPTCHA ซะ เท่านี้เอง – แล้วถ้าเกิดว่าผู้ใช้หลาย ๆ รายตอบ CAPTCHA อันเดียวกันด้วยคำตอบเหมือน ๆ กัน ก็ให้ถือว่าคำตอบนั้นเป็นคำตอบที่ถูก

เจ๋งดี

updated 2007.06.01: ดูรายละเอียดเต็ม ๆ พร้อมรูปประกอบ ได้ที่บล็อก [PRADT](http://pradt.net/?p=989)

\[ลิงก์ [reCAPTCHA](http://recaptcha.net/) \| ผ่าน [CNN](http://www.cnn.com/2007/TECH/05/29/blather.to.books.ap/index.html "Web registration tool digitizes books"), [siit.net](http://siit.net/webboard/read.php?Topic_ID=40239)\]

<span class="small">technorati tags:  
[CAPTCHA](http://technorati.com/tag/CAPTCHA),  
[OCR](http://technorati.com/tag/OCR)  
</span>
