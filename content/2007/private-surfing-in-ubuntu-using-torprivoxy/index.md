---
title: "Private surfing in Ubuntu – using Tor+Privoxy"
date: "2007-05-26T02:16:00+07:00"
lastmod: "2011-04-29T05:26:07+07:00"
type: "post"
url: "/2007/private-surfing-in-ubuntu-using-torprivoxy/"
description: "ท่องเว็บเงียบ ๆ ในอูบุนตูลีนุกซ์ (สำหรับวินโดวส์ ดูที่ http://wonam.exteen.com/20060923/tor ) Tor (ตอร์) เป็นเครือข่ายและโปรแกรมช่วยเพิ่มความเป็นส่วนตัวในการท่องเว็บ นอกจากนี้ยังอาจช่วยให้เราสามารถเข้าเว็บที่ถูกบล็อกได้อีกด้วย Privoxy (ไพรว็อกซี่) เป็นโปรแกรมพร็อกซี่ที่ช่วยเพิ่มความเป็นส่วนตัวในการท"
categories: ["internet", "politics", "freedom"]
tag: ["anonymity", "circumvention", "how-to", "internet-censorship", "linux", "privacy", "tor", "ubuntu"]
textlang: "th"
wpid: 2095
---
ท่องเว็บเงียบ ๆ ในอูบุนตูลีนุกซ์

(สำหรับวินโดวส์ ดูที่ <http://wonam.exteen.com/20060923/tor> )

**[Tor](http://th.wikipedia.org/wiki/Tor)** (ตอร์) เป็นเครือข่ายและโปรแกรมช่วยเพิ่มความเป็นส่วนตัวในการท่องเว็บ นอกจากนี้ยังอาจช่วยให้เราสามารถเข้าเว็บที่ถูกบล็อกได้อีกด้วย

**[Privoxy](http://en.wikipedia.org/wiki/Privoxy)** (ไพรว็อกซี่) เป็นโปรแกรมพร็อกซี่ที่ช่วยเพิ่มความเป็นส่วนตัวในการท่องเว็บเช่นกัน โดยสามารถดักจับ [‘คุกกี้’](http://th.wikipedia.org/wiki/%E0%B8%84%E0%B8%B8%E0%B8%81%E0%B8%81%E0%B8%B5%E0%B9%89_%28%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%80%E0%B8%97%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B9%80%E0%B8%99%E0%B9%87%E0%B8%95%29 "cookie") และกรองเนื้อหาบางอย่าง เช่น โฆษณา ออกไปได้

### ติดตั้ง Tor และ Privoxy ใน Ubuntu

1 – ติดตั้งแพคเกจ “tor” และ “privoxy”  
จะใช้เมนู System -\> Administration -\> Synaptic Package Manager  
หรือจะใช้คำสั่งที่คอมมานด์ไลน์ก็ได้ คือ:

`sudo apt-get install tor privoxy`

2 – ปรับตั้งค่าของ Privoxy โดยแก้ไฟล์ /etc/privoxy/config:

`sudo gedit /etc/privoxy/config`

3 – เพิ่มบรรทัดนี้เข้าไป (รวม จุด ตรงท้ายสุดด้วย):

`forward-socks4a / localhost:9050 .`

โดยจะเพิ่มเข้าไปที่ไหนของไฟล์ก็ได้  
(เพื่อความอ่านง่าย แนะนำให้เพิ่มแถว ๆ ส่วนที่ชื่อว่า “FORWARDING” / “forward-socks4”)

4 – (ทำหรือไม่ก็ได้) หากไม่ต้องการให้บันทึกปูมการทำงานของโปรแกรม (log) ให้ใส่ \# หน้าบรรทัดที่เขียนว่า “logfile logfile”

5 – (ทำหรือไม่ก็ได้) หากไม่ต้องการให้บันทึกคุกกี้ที่ถูกดักจับ ให้ใส่ \# หน้าบรรทัดที่เขียนว่า “jarfile jarfile”

6 – รีสตาร์ท Privoxy ใหม่ โดยใช้คำสั่ง:

`sudo /etc/init.d/privoxy restart`

------------------------------------------------------------------------

### ตั้งค่า Firefox ให้ใช้งาน Tor

ในที่นี้ จะใช้ปลั๊กอิน [Torbutton](https://addons.mozilla.org/en-US/firefox/addon/2275) เนื่องจากไม่ซับซ้อน ติดตั้งง่าย.  
ปลั๊กอินอื่น ๆ ที่ใช้ได้เช่นกัน โดยอาจมีลูกเล่นมากกว่า/ซับซ้อนกว่า เช่น [FoxyProxy](https://addons.mozilla.org/en-US/firefox/addon/2464)

1 – ติดตั้ง Torbutton โดยไปที่หน้าเว็บ: <https://addons.mozilla.org/en-US/firefox/addon/2275>

2 – ปิดไฟร์ฟ็อกซ์ และเปิดใหม่

3 – ที่มุมล่างขวา จะเห็นข้อความว่า “Tor Disabled” (ตอร์ปิดใช้งาน)

4 – เมื่อต้องการความเป็นส่วนตัวมากขึ้น หรือต้องการเข้าเว็บที่ถูกบล็อก ให้คลิกที่ข้อความข้างต้น มันจะเปลี่ยนเป็นคำว่า “Tor Enabled” (ตอร์เปิดใช้งาน)

5 – ท่องเว็บได้ 🙂

------------------------------------------------------------------------

เรียบเรียงจาก [Step by step with Tor](http://ubuntuforums.org/showthread.php?p=2702743) ที่ Ubuntu Forums  
ลีนุกซ์ดิสโทรอื่น ๆ ทำคล้าย ๆ กัน แต่จะแตกต่างกันเรื่องตำแหน่งไฟล์ตั้งค่า (คอนฟิก)

updated 2007.05.30: เอกสารโดยละเอียด (ภาษาอังกฤษ) ดูที่:  
[Running the Tor client on Linux/BSD/Unix](http://security.ngoinabox.org/Documentation/Misc/tor.eff.org/doc/tor-doc-unix.html) – ติดตั้ง client (สำหรับใช้งานดูเว็บ); และ  
[Configuring a Tor server](http://security.ngoinabox.org/Documentation/Misc/tor.eff.org/doc/tor-doc-server.html) – ติดตั้ง server (เพื่อช่วยให้คนอื่นดูเว็บได้ดีขึ้น – ยิ่งมี Tor server เยอะ ก็ยิ่งทำให้เครือข่าย Tor มีประสิทธิภาพดี)

updated 2007.05.31: เพิ่งเห็นว่า ที่ [ubuntuclub ก็มีลงไปแล้ว](http://ubuntuclub.com/node/35 "วิธีติด Tor บน Ubuntu")

<span class="small">technorati tags:  
[Tor](http://technorati.com/tag/Tor),  
[Privoxy](http://technorati.com/tag/Privoxy),  
[Ubuntu](http://technorati.com/tag/Ubuntu)  
</span>
