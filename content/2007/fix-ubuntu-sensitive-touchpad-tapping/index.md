---
title: "Touchpad tapping way too sensitive in Ubuntu – how to fix it"
date: "2007-05-25T11:39:00+07:00"
lastmod: "2011-05-07T21:25:39+07:00"
type: "post"
url: "/2007/fix-ubuntu-sensitive-touchpad-tapping/"
description: "การทดลองใช้ GNU/Linux (Ubuntu 7.04) กับโน๊ตบุ๊ค ยังคงพบปัญหาจุกจิกกวนใจอยู่ทั่วไป แต่จะพยายามแก้ไปเรื่อย ๆ จนกว่าจะทนไม่ไหว (ไม่คุ้มกับเวลาที่เสียไป) ปัญหาอย่างหนึ่งที่กวนใจมากก็คือ tapping (การ ‘คลิก’ โดยกดที่ทัชแพด แทนที่จะกดที่ปุ่ม) มันเร็วเกินไป แตะโดนนิดหน่อย ๆ ก็จะหาว่าเราคลิกซะแล้ว ทำให้ทำงาน"
categories: ["computer"]
tag: ["how-to", "linux", "ubuntu"]
textlang: "th"
wpid: 2093
---
การทดลองใช้ GNU/Linux ([Ubuntu 7.04](http://www.ubuntu.com/)) กับโน๊ตบุ๊ค ยังคงพบปัญหาจุกจิกกวนใจอยู่ทั่วไป  
แต่จะพยายามแก้ไปเรื่อย ๆ จนกว่าจะทนไม่ไหว (ไม่คุ้มกับเวลาที่เสียไป)

ปัญหาอย่างหนึ่งที่กวนใจมากก็คือ tapping (การ ‘คลิก’ โดยกดที่ทัชแพด แทนที่จะกดที่ปุ่ม) มันเร็วเกินไป แตะโดนนิดหน่อย ๆ ก็จะหาว่าเราคลิกซะแล้ว ทำให้ทำงานลำบากมาก เช่น ไล่ดูหน้าเว็บอยู่ดี ๆ มันก็จะคลิกลิงก์ให้เราเฉย หรือว่าพิมพ์เอกสารอยู่ แล้วมือเผลอไปโดน เคอร์เซอร์ก็จะเปลี่ยนตำแหน่งไปที่อื่น-บางทีก็ทำงานเละได้

วิธีแก้ (ดูจาก [Ubuntu Forums](http://ubuntuforums.org/archive/index.php/t-409520.html))

ลงแพคเกจที่ชื่อ gsynaptics  
(หรือ ksynaptics, qsynaptics ตามเดสก์ทอปที่ใช้  
– และคำว่า synaptics ในชื่อแพคเกจ มาจากชื่อ Xorg Synaptics Touch Pad Driver – ไม่เกี่ยวกับตัว Synaptic Package Manager ของ Ubuntu แต่อย่างใด)

`sudo apt-get install gsynaptics`

แพคเกจนี้จะเพิ่มตัวปรับแต่ง Touchpad ลงไปในเมนู Preferences

แต่ก่อนจะใช้ได้ ต้องไปแก้ /etc/X11/xorg.conf ก่อน,  
โดยมองหา

 

    Section "InputDevice"
     Identifier "Synaptics Touchpad"
     Driver  "synaptics"
     ...
    EndSection

 

แล้วเพิ่มบรรทัดนี้

 

     Option  "SHMConfig"  "true"

 

ต่อท้าย (ก่อน EndSection)

แล้วรีสตาร์ท X ใหม่

ได้แล้วลองปรับตรง tapping ดู  
หรือถ้าไม่ไหวจริง ๆ ก็ยกเลิกไปเลย (เอาเครื่องหมายถูก ที่ Enable tapping ออก)

ถ้าอยากปรับแต่งโดยละเอียดในไฟล์ xorg.conf  
ดูตัวอย่างได้ที่ [LinuxQuestions.org](http://www.linuxquestions.org/questions/showthread.php?t=141056)

<span class="small">technorati tags: [Ubuntu](http://technorati.com/tag/Ubuntu), [touchpad](http://technorati.com/tag/touchpad)</span>
