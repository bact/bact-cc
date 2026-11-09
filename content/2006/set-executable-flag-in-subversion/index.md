---
title: "set executable flag in Subversion"
date: "2006-01-18T23:44:00+07:00"
lastmod: "2006-01-18T23:44:00+07:00"
type: "post"
url: "/2006/set-executable-flag-in-subversion/"
description: "เพิ่งจะรู้ วิธีบอกให้ Subversion มันจำเอาไว้ ว่าไฟล์นี้น่ะ รันได้นะเฟ้ย (executable) svn propset svn:executable ” filename ไม่อย่างนั้น หลังจากอัพเดท/หรือเช็คเอาท์ เพอมิสชั่นต่าง ๆ มันจะหายไปหมดเลย ต้องเซตกันใหม่ (แต่พร็อพเพอตี้นี้ ก็ใช้ได้แค่ executable อ่ะ ไม่เกี่ยวกะ read / write ใช้กะไดเรกทอรีไม"
categories: ["something"]
textlang: "th"
wpid: 1197
---
เพิ่งจะรู้ วิธีบอกให้ Subversion มันจำเอาไว้ ว่าไฟล์นี้น่ะ รันได้นะเฟ้ย (executable)

`svn propset svn:executable '' filename`

ไม่อย่างนั้น หลังจากอัพเดท/หรือเช็คเอาท์ เพอมิสชั่นต่าง ๆ มันจะหายไปหมดเลย ต้องเซตกันใหม่ (แต่พร็อพเพอตี้นี้ ก็ใช้ได้แค่ executable อ่ะ ไม่เกี่ยวกะ read / write ใช้กะไดเรกทอรีไม่ได้ด้วย)

- [Subversion properties](http://svnbook.red-bean.com/en/1.1/ch07s02.html)
- [propset command](http://svnbook.red-bean.com/en/1.0/re23.html), also links to propget, proplist, propedit, propdel, …
