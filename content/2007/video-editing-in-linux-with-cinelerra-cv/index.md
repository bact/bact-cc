---
title: "Video Editing in Linux with Cinelerra CV"
date: "2007-05-28T23:40:00+07:00"
lastmod: "2011-11-11T18:37:25+07:00"
type: "post"
url: "/2007/video-editing-in-linux-with-cinelerra-cv/"
description: "ถ่ายวิดีโอมาจากสยามเมื่อวันเสาร์ อยากลองเล่นอะไรนิดหน่อย เลยมองหาโปรแกรมตัดต่อภาพเคลื่อนไหวในลีนุกซ์ หาใน package manager ของ Ubuntu เค้ามี Kino แต่พยายามจะเอาไฟล์เพลง MP3 มาใช้ประกอบภาพ มันไม่ยอม เลยไปค้นเว็บดู ว่าเค้าทำกันยังไง ค้นไปค้นมา เจอเว็บนึง เค้าว่า Kino มันก็โอเค แต่เค้าใช้ Cinelerra ความ"
categories: ["computer", "media"]
tag: ["cinelerra", "free-softwares", "linux", "mv", "open-source", "software", "ubuntu", "video"]
textlang: "th"
wpid: 2100
---
ถ่ายวิดีโอมาจากสยามเมื่อวันเสาร์ อยากลองเล่นอะไรนิดหน่อย เลยมองหาโปรแกรมตัดต่อภาพเคลื่อนไหวในลีนุกซ์

หาใน package manager ของ Ubuntu เค้ามี [Kino](http://www.kinodv.org/ "Linux Digital Video") แต่พยายามจะเอาไฟล์เพลง MP3 มาใช้ประกอบภาพ มันไม่ยอม เลยไปค้นเว็บดู ว่าเค้าทำกันยังไง

ค้นไปค้นมา เจอ[เว็บนึง](http://www.robfisher.net/video/ "Rob Fisher's Linux Video Editing") เค้าว่า Kino มันก็โอเค แต่เค้าใช้ [Cinelerra](http://cinelerra.org/) ความสามารถมันเยอะกว่า ก็เลยลองดู

### ติตตั้ง Cinelerra CV ใน Ubuntu (และดิสโทรอื่น ๆ)

Cinelerra ปัจจุบันมีสอง “flavours”, คือตัว รุ่นอย่างเป็นทางการ ที่ดูแลโดยบริษัท [Heroine Virtual Ltd.](http://heroinewarrior.com/) กับอีกตัว ที่ดูแลโดยชุมชน (เรียกว่า [Cinelerra CV](http://cv.cinelerra.org/)) – เค้าพยายามจะไม่เรียก/ทำให้มันเป็น “fork”

[Ubuntu Studio](http://ubuntustudio.com/) อาจพิจารณารวม Cinelerra CV เข้าชุด แต่ต้องรอการจัดการปัญหาเรื่องลิขสิทธิ์/สัญญาอนุญาตให้เรียบร้อยก่อน

(ใครอยากรู้เรื่อง Ubuntu Studio ให้ถาม kijjaz โมโนโทน – เธอเชี่ยวชาญมาก)

ตอนนี้ต้องลงเองไปก่อน  
แต่ไม่ต้องตกใจ มีคนทำแพคเกจไว้ให้เรียบร้อยแล้ว สำหรับดิสโทรต่าง ๆ

เพียงเพิ่ม repo ตามที่กำหนดเข้าไป

สำหรับ Ubuntu 7.04 (Fiesty) ให้เพิ่มบรรทัดนี้ในไฟล์ */etc/apt/sources.list*

(หรือจะเพิ่มผ่าน Synaptic Package Manager ก็ได้):

`deb http://www.kiberpipa.org/~muzzol/cinelerra/feisty-i386/ ./`

สำหรับเวอร์ชันอื่น หรือลีนุกซ์ดิสโทรอื่น ๆ ให้ดูที่ [คู่มือติดตั้ง](http://cvs.cinelerra.org/docs/wiki/doku.php?id=english_manual:cinelerra_cv_en_2)

จากนั้นก็อัพเดทรายการ apt ใหม่

`sudo apt-get update`

แล้วก็ติดตั้งได้เลย

`sudo apt-get install cinelerra`

### ปรับแต่งหน่วยความจำ เพื่อใช้ Cinelerra

โปรแกรมสร้างงานมัลติมีเดียพวกนี้ กินแรมและฮาร์ดดิสก์มหาศาลแน่นอน – ต้องปรับแต่งค่าพวกนี้นิดหน่อย เพื่อให้มันทำงานได้ราบรื่นขึ้น

เพิ่มขนาด shared memory (จาก [Tips#Freeing more shared memory](http://cvs.cinelerra.org/docs/wiki/doku.php?id=english_manual:cinelerra_cv_en_20#freeing_more_shared_memory))

ให้เพิ่มบรรทัดข้างล่างนี้ ลงในไฟล์ */etc/sysctl.conf* :

`kernel/shmmax=0x7fffffff`

แล้วรีสตาร์ทใหม่

เพิ่มความเร็วการอ่านเขียนฮาร์ดดิสก์ (จาก [Tips#Speeding up the hard drive](http://cvs.cinelerra.org/docs/wiki/doku.php?id=english_manual:cinelerra_cv_en_20#speeding_up_the_hard_drive))

`hdparm -c3 -d1 -u1 -k1 /dev/hda`

(กรุณาปรับพารามิเตอร์อย่างระมัดระวัง เช่นบางเครื่องอาจจะใช้ -c3 ไม่ได้ หรือฮาร์ดดิสก์อยู่ที่อื่นที่ไม่ใช่ /dev/hda – ดูรายละเอียดในลิงก์ข้างบน)

สำหรับการปรับแต่งค่าอื่น ๆ ให้ดูที่ [Tips](http://cvs.cinelerra.org/docs/wiki/doku.php?id=english_manual:cinelerra_cv_en_20) (บางอันอาจจะต้องรีคอมไพล์เคอร์เนลด้วย – -“)

### ใช้งาน Cinelerra

ผมเองก็มั่ว ๆ นะครับ เพิ่งเคยใช้ครั้งแรก/ครั้งเดียว จะบอกเท่าที่ได้ลองมาละกัน ที่เหลือก็ไปมั่วต่อกันเอง – มีเอกสารพอสมควรใน [วิกิ](http://cvs.cinelerra.org/docs/wiki/doku.php) และอินเทอร์เน็ต

ในการตัดต่อ Cinelerra จะมองสื่อทุกอย่างเป็นแทร็ค (track)

การตัดต่อก็จะเป็นการตัด/ย้ายภาพใน/ระหว่างแทร็ค

ส่วนการ mix ก็จะเป็นการเปิด/ปิดแต่ละแทร็ค – เช่นการทำภาพซ้อน ก็คือเปิดภาพ 2 แทร็คพร้อมกัน (โดยตั้ง opacity ให้เห็นภาพทั้งสองแทร็คทะลุกัน)

เช่น ในไฟล์ทดสอบที่ผมทำ จะมีอยู่ 4 แทร็ค เป็นแทร็คเสียง (audio track) 2 แทร็ค, และแทร็คภาพ (video track) 2 แทร็ค

ที่แทร็คเสียงมีสอง เนื่องจากใช้ MP3 ที่นำเข้ามา เป็นแบบสเตอริโอ

ส่วนแทร็คภาพสองอัน อันหลักเป็นไฟล์วิดีโอที่ถ่ายมา ส่วนอีกอันเป็นไตเติ้ล

ผมก็วางแทร็คภาพไตเติ้ลให้เล่นก่อน แล้วตามด้วยแทร็คภาพหลัก พร้อม ๆ กับแทร็คเสียงทั้งสอง

การเลือก/เลื่อนช่วงของแทร็คนี่ จะมีเคอร์เซอร์ให้ใช้สองแบบ แบบลูกศร และแบบ I-beam (หน้าตาเหมือนตัว I น่ะ) โดยตัวแรกจะจับช่วงของแทร็คเหมือนจับสิ่งของ ลากย้ายไปมาได้ ส่วนอันหลังเอาไว้เลือกเป็นช่วงเวลา ลองดู

เวลาจะแก้ไขแทร็คนี่ ต้องกดปุ่มแดง ๆ (arm) ที่ด้านซ้ายของแทร็คก่อน

(คำสั่งต่าง ๆ ที่สั่งไป จะมีผลเฉพาะกับแทร็คที่ถูกกดปุ่มแดงเท่านั้น – จะกดปุ่มแดงหลาย ๆ แทร็คพร้อมกันก็ได้)

แรก ๆ จะงง ๆ หน่อย แต่เล่น ๆ ไปซักพักก็พอโอเค (แต่ยังงงอยู่) UI มันหน้าตาประหลาด ๆ

ทำอะไรเสร็จแล้ว อยากจะเซฟเป็นไฟล์วิดีโอแบบปกติบ้าน ๆ อย่าง .mov .avi [.ogg](http://en.wikipedia.org/wiki/Theora) เพื่อส่งให้เพื่อ ๆ ดู ก็ให้สั่ง “Render”

นี่เป็นตัวอย่างที่ลองทำ เอาวิดีโอที่ถ่ายจากกล้องดิจิทัล (.avi) มารวมกับเพลง (.mp3)

(บันไดเลื่อนบีทีเอสสยาม และเพลง “สักเท่าไร” ของโมเดิร์นด็อก)

เราก็จะได้เอ็มวีแบบบ้าน ๆ [เช่นนี้](http://www.myspace.com/video/vid/12534256):


<object width="425px" height="360px" ><param name="allowFullScreen" value="true"/><param name="wmode" value="transparent"/><param name="movie" value="http://mediaservices.myspace.com/services/media/embed.aspx/m=12534256,t=1,mt=video"/></object>


<span class="small">technorati tags: [Linux](http://technorati.com/tag/Linux), [Cinelerra](http://technorati.com/tag/Cinelerra), [video editing](http://technorati.com/tag/video_editing)</span>
