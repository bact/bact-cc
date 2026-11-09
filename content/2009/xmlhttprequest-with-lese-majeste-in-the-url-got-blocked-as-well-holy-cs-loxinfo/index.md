---
title: "XMLHttpRequest with \"lese-majeste\" in the url got blocked as well – Holy CS Loxinfo"
date: "2009-02-06T14:26:00+07:00"
lastmod: "2011-04-29T05:21:37+07:00"
type: "post"
url: "/2009/xmlhttprequest-with-lese-majeste-in-the-url-got-blocked-as-well-holy-cs-loxinfo/"
description: "อัปเดตต่อจากกรณี Mashable.com got blocked – ความมั่วของ CS Loxinfo กับการบล็อคเว็บ จากการทดลองเพิ่มเติม พบว่า web api request (ซึ่งทำผ่าน url) ก็จะใช้ไม่ได้เช่นกัน เช่น ผมลองใช้บริการย่อลิงก์ ของ bit.ly โดยใช้ url : http://klongofconsciousness.wordpress.com/2009/01/23/dozing-german-arrested-for-lese"
categories: ["internet", "politics"]
tag: ["ajax", "cinema", "internet-censorship", "lese-majeste", "programming", "web-2-0"]
textlang: "th"
wpid: 2431
---
อัปเดตต่อจากกรณี [Mashable.com got blocked – ความมั่วของ CS Loxinfo กับการบล็อคเว็บ](http://bact.blogspot.com/2009/02/mashablecom-got-blocked-cs-loxinfo.html)

จากการทดลองเพิ่มเติม พบว่า web api request (ซึ่งทำผ่าน url) ก็จะใช้ไม่ได้เช่นกัน

เช่น ผมลองใช้บริการย่อลิงก์ ของ [bit.ly](http://bit.ly/) โดยใช้ url :

> [http://klongofconsciousness.wordpress.com/2009/01/23/dozing-german-arrested-for-*lese-majeste*/](http://klongofconsciousness.wordpress.com/2009/01/23/dozing-german-arrested-for-lese-majeste/ "Dozing German arrested for Lèse Majesté")<sup>\*</sup>

ปรากฎว่า bit.ly มันเงียบครับ ไม่แสดงผลลัพธ์อะไร (ตามปกติมันจะแสดงผลลัพธ์ลิงก์ที่ถูกย่อ ในช่อง “Shortened URL”)

เมื่อตรวจสอบดูก็พบว่า เมื่อกดปุ่ม “Shorten” ตัวหน้าเว็บ จะส่ง XMLHttpRequest ไปที่ <http://bit.ly/api> เรียกใช้บริการที่เซิร์ฟเวอร์ของ bit.ly เพื่อรับผลลัพธ์ (ตามลักษณะการเขียนโปรแกรมแบบ AJAX ซึ่งปัจจุบันนี้นิยมทั่วไป)

โดยในการส่ง request ที่ว่านี้ ก็จะทำในรูปของการเรียก url ปกติ ซึ่งกรณีนี้ ก็จะเป็นในรูปแบบนี้ :

> [http://bit.ly/api?method=shorten&**long_url=http%3A%2F%2Fklongofconsciousness.wordpress.com%2F2009%2F01%2F23%2Fdozing-german-arrested-for-*lese-majeste*%2F**&keyword=&history=1&t=1233903997567](http://bit.ly/api?method=shorten&long_url=http%3A%2F%2Fklongofconsciousness.wordpress.com%2F2009%2F01%2F23%2Fdozing-german-arrested-for-lese-majeste%2F&keyword=&history=1&t=1233903997567)

method=shorten นั้นคือระบุว่า ใช้เรียกใช้เมธทอดที่ชื่อ shorten; **long_url=… ก็ระบุว่าจะย่อลิงก์อะไร;** ที่เหลือก็เป็นพารามิเตอร์ต่าง ๆ

จะเห็นว่าปัญหาอยู่ตรงที่ว่า long_url นั้นไม่ได้เข้ารหัส ดังนั้นถ้าใส่ลิงก์ที่มีคำว่า “lese-majeste” เข้าไปให้ bit.ly ย่อให้หน่อย  
คำเดียวกันนี้ก็จะปรากฏอยู่ในพารามิเตอร์ที่จะส่ง XMLHttpRequest ซึ่งก็จะไปปรากฏอยู่ใน url — แล้วก็จะถูกบล็อคทันที (อย่างน้อยที่ทราบโดยไอเอสพีหนึ่งแห่ง คือ CS Loxinfo)

**ดังนั้นสิ่งที่ request ดัง url ข้างต้น (หรือ url ใด ๆ ที่มีคำว่า “lese-majeste” หรือ “lesemajeste”)  
จะได้รับ respond กลับมา  
ก็จะเป็นหน้า [“404 หลอก”](http://bact.blogspot.com/2009/02/mashablecom-got-blocked-cs-loxinfo.html) ซึ่งไม่ใช่รูปแบบข้อมูลอย่างที่โปรแกรมคาดหวังไว้ (เช่น XML หรือ JSON) โปรแกรมจึงทำงานต่อไม่ได้ … ก็เลยเงียบ**

เจ๋งไหม ?

(<sup>\*</sup> เป็นข่าวเมื่อ 22 ม.ค. 2552 Klaus Brehmer ชายชาวเยอรมันคนหนึ่งนั่งในโรงหนังที่เวิลด์เทรด แล้วในขณะนั้นมีเพลงสรรเสริญบรรเลง คนในโรงหนังเลยโห่ ตะโกน และเอาน้ำราดหัวเขา จากนั้นตำรวจก็มาจับเขาไป – โอ้ อารยะประเทศ)

------------------------------------------------------------------------

ใครที่เขียนโปรแกรมบนเว็บ/โปรแกรมที่ทำงานกับเว็บ แล้วมีผู้ใช้บริการหรือลูกค้า แจ้งมาว่าโปรแกรมทำงานผิดปกติ ลองเช็คเรื่องการบล็อคเว็บด้วย ถ้าคุณทำ request ใด ๆ ผ่านเว็บ ก็มีโอกาสจะโดนบล็อคได้เสมอ (หลายครั้งเกิดจากความมั่ว ๆ – Mashable.com ยังโดนได้เลย) ลองถามผู้ใช้บริการของคุณ ว่าใช้เน็ตยี่ห้อไหน ถ้าเป็นไปได้ ก็แนะนำให้เขาเปลี่ยนยี่ห้อไอเอสพีไปเลย ตัดปัญหา

**ส่วนใครที่บล็อคเว็บแบบเหมารวม-มักง่ายแบบนี้ ไม่ว่าจะเป็นรัฐ หน่วยงานราชการ สถานศึกษา หรือไอเอสพี ก็ขอความกรุณาปรับปรุงการทำงานด้วย ถ้ามีคำสั่งศาลมาให้บล็อคก็บล็อคตาม url ที่ศาลสั่งมาไป ไม่ใช่ใช้ keyword filtering แบบนี้ มันกระทบกับคนอื่นเว็บอื่นที่ไม่ได้เกี่ยวข้องด้วย**

**<u>อย่ามักง่าย</u>**

------------------------------------------------------------------------

อัปเดต : ผมดันไปตั้งชื่อหัวข้อของโพสต์นี้มีคำว่า “lese majeste”, ใน url ของโพสต์นี้ ก็เลยมีคำนั้นไปด้วย ใครใช้ CS Loxinfo ก็จะกดเข้ามาดูโพสต์นี้ตรง ๆ ไม่ได้นะครับ. ถ้าใช้โปรแกรมอ่าน feed ที่ทำงานที่ฝั่งไคลเอนต์ก็อาจจะไม่ได้ด้วย – เพราะใน [feed](http://feeds.feedburner.com/%7Er/bact/%7E3/533175999/xmlhttprequest-with-lese-majeste-in-url.html "http://feeds.feedburner.com/~r/bact/~3/533175999/xmlhttprequest-with-lese-majeste-in-url.html") ของโพสต์นี้ ซึ่งใช้ Feedburner มันก็มีชื่อหัวข้ออยู่ด้วย ([http://feeds.feedburner.com/%7Er/bact/%7E3/533175999/xmlhttprequest-with-*lese-majeste*-in-url.html](http://feeds.feedburner.com/%7Er/bact/%7E3/533175999/xmlhttprequest-with-lese-majeste-in-url.html)). อย่างไรก็ตาม ยังสามารถอ่านได้ในหน้ารวมของบล็อก หรืออ่านผ่าน feed reader ที่ทำงานฝั่งเซิร์ฟเวอร์ อย่าง Google Reader. ลุ่มลึกดีครับ อารยะประเทศ.

<span class="small">technorati tags:  
[XMLHttpRequest](http://technorati.com/tag/XMLHttpRequest),  
[lese majeste](http://technorati.com/tag/lese+majeste),  
[Klaus Brehmer](http://technorati.com/tag/Klaus+Brehmer),  
[bit.ly](http://technorati.com/tag/bit.ly)  
</span>
