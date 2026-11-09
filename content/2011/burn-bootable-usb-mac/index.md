---
title: "burn a bootable (live) USB drive on Mac OS X"
date: "2011-04-27T16:00:36+07:00"
lastmod: "2011-05-05T12:01:13+07:00"
type: "post"
url: "/2011/burn-bootable-usb-mac/"
description: "เบิร์นแผ่นติดตั้งอูบุนตูลงไดรฟ์ยูเอสบี ให้บูตจากยูเอสบีได้ ด้วยแมค ผมไม่ประสบความสำเร็จในการใช้ Disk Utility (GUI) ของ Mac OS X ในการ burn bootable USB สำหรับติดตั้ง Ubuntu (เท่าที่ค้นดูในเน็ต ก็ไม่ค่อยมีใครประสบความสำเร็จ ไม่รู้ทำไม) ถ้าอยู่บน Windows หรือ Linux จะมีโปรแกรมสุดง่าย ชื่อ UNetbootin ใ"
categories: ["computer"]
tag: ["how-to", "mac-os-x", "ubuntu"]
textlang: "th"
wpid: 2498
---
*เบิร์นแผ่นติดตั้งอูบุนตูลงไดรฟ์ยูเอสบี ให้บูตจากยูเอสบีได้ ด้วยแมค*

ผมไม่ประสบความสำเร็จในการใช้ [Disk Utility](https://secure.wikimedia.org/wikipedia/en/wiki/Disk_Utility) (GUI) ของ Mac OS X ในการ burn bootable USB สำหรับติดตั้ง [Ubuntu](http://www.ubuntu.com/netbook/get-ubuntu/download "Ubuntu Netbook Edition") (เท่าที่ค้นดูในเน็ต ก็ไม่ค่อยมีใครประสบความสำเร็จ ไม่รู้ทำไม)

ถ้าอยู่บน Windows หรือ Linux จะมีโปรแกรมสุดง่าย ชื่อ [UNetbootin](http://unetbootin.sourceforge.net/) ให้ใช้ .. แต่บน Mac มันไม่มี

เลยใช้ diskutil + dd ทางคอมมานด์ไลน์ละกัน  
วิธีทั้งหมดดูได้จาก [4 ways to create bootable Live USB (Windows, Linux, Mac OS X)](http://www.webupd8.org/2009/04/4-ways-to-create-bootable-live-usb.html)

1. เตรียมแฟ้มอิมเมจมาก่อน .iso หรือ .img
2. ที่ Terminal สั่ง  
    `diskutil list`  
    ดูว่าไดร์ฟยูเอสบีเรา mount เชื่อมอยู่ตรงไหน (เช่น /dev/disk1) – อาจจะดูจากชื่อหรือขนาด – ถ้าไม่ชัวร์ ก็ถอดยูเอสบีออกมาก่อน แล้ว diskutil list ดูทีนึง แล้วเสียบ USB เข้าไป แล้ว diskutil list ดูอีกที ดูว่ามันมีอะไรเพิ่มมา
3. `diskutil unmountDisk /dev/disk`*`N`*  
    (N ตัวสุดท้ายนี่ แล้วแต่ว่าไดร์ฟเราอยู่ที่ไหน)
4. `sudo dd if=/path/to/image.iso of=/dev/diskN bs=1m`  
    (if= คือแฟ้มอิมเมจ of= คือไดร์ฟยูเอสบี)
5. `diskutil eject /dev/diskN`  
    แล้วก็ถอดไดร์ฟยูเอสบีออกได้ – เสร็จ
