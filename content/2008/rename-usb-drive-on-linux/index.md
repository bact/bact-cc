---
title: "Rename USB drive on Linux"
date: "2008-03-14T02:45:00+07:00"
lastmod: "2008-03-14T02:45:00+07:00"
type: "post"
url: "/2008/rename-usb-drive-on-linux/"
description: "It is this difficult to rename a usb drive on Ubuntu/Linux! (and you also need different labeler tool for different file system… well, …) ซื้อแฮนดี้ไดร์ฟมาใหม่ (8GB 1,500 บาท เดินถัดไปอีกไม่กี่ร้าน 1,200 บาท .. แบบเดียวกันเป๊ะ!! — ราคาของในมาบุญครองมันมั่วจริง ๆ) จะฟอร์แมตของเดิม ที่รก ๆ และมีชื่อได"
tag: ["how-to", "linux", "ubuntu"]
textlang: "th"
wpid: 2300
---
It is [this difficult](https://help.ubuntu.com/community/RenameUSBDrive) to rename a usb drive on Ubuntu/Linux! (and you also need different labeler tool for different file system… well, […](http://twitter.com/bact/statuses/771078703))

ซื้อแฮนดี้ไดร์ฟมาใหม่ (8GB 1,500 บาท เดินถัดไปอีกไม่กี่ร้าน 1,200 บาท .. แบบเดียวกันเป๊ะ!! — ราคาของในมาบุญครองมันมั่วจริง ๆ) จะฟอร์แมตของเดิม ที่รก ๆ และมีชื่อไดเรกทอรีประหลาด ๆ ที่ลบไม่ได้ (runauto…) งมหาอยู่นาน ทั้งใน mkdosfs ทั้งใน parted/gparted – ไม่เจอ

สุดท้ายไปเจอในเน็ต [โห](http://twitter.com/bact/statuses/771078703) ต้อง[เล่นท่ายาก](https://help.ubuntu.com/community/RenameUSBDrive "RenameUSBDrive @ Help.Ubuntu.com")

ปรากฎว่า แต่ละระบบไฟล์ จะใช้โปรแกรมในการเปลี่ยนชื่อไม่เหมือนกัน  
เช่น FAT ใช้ mtools, NTFS ใช้ ntfsprogs, ext2/3 ใช้ e2label, …

ผมใช้เป็น FAT32 ก็ต้องลง mtools (`sudo apt-get install mtools`)  
แล้วใช้โปรแกรมชื่อ mlabel ในการเปลี่ยนชื่อ ประมาณนี้:

`sudo mlabel -i `*`/dev/sdd1`*` ::`*`GO-BACT`*

เปลี่ยน */dev/sdd1* เป็น device ที่จะเปลี่ยน (ใน Ubuntu ลอง ls /dev/disk ดูได้)  
เปลี่ยน *GO-BACT* เป็นชื่อที่อยากได้

เสียบครั้งต่อไป ก็จะแสดงเป็นชื่อใหม่ละ

<span class="small">technorati tags:  
[rename](http://technorati.com/tag/rename),  
[usb drive](http://technorati.com/tag/usb+drive),  
[Linux](http://technorati.com/tag/Linux)  
</span>
