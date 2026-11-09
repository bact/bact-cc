---
title: "Charset in MySQL 5"
date: "2005-11-14T19:37:00+07:00"
lastmod: "2005-11-14T19:37:00+07:00"
type: "post"
url: "/2005/charset-in-mysql-5/"
description: "MySQL 5 – Connection Character Sets and Collations มีปัญหา จะใช้ PEAR::MDB2 อ่านข้อความ utf-8 จาก MySQL (โพสต์ไว้ที่ Narisa.com) ปรากฏว่าข้อความ(ภาษาไทย, ภาษา non-Latin1)กลายเป็น ??? หมดเลย หาในเน็ตอยู่นาน ปรากฏว่า ต้องเพิ่มคำสั่งนี้เข้าไปก่อนจะเริ่ม query SELECT $db->query(“SET CHARACTER SET utf8”)"
tag: ["character-set", "mysql", "php", "thai", "utf-8"]
textlang: "th"
wpid: 1065
---
MySQL 5 – [Connection Character Sets and Collations](http://dev.mysql.com/doc/refman/5.0/en/charset-connection.html)

มีปัญหา จะใช้ [PEAR::MDB2](http://pear.php.net/package/MDB2/) อ่านข้อความ utf-8 จาก MySQL (โพสต์ไว้ที่ [Narisa.com](http://www.narisa.com/forums/index.php?showtopic=9800)) ปรากฏว่าข้อความ(ภาษาไทย, ภาษา non-Latin1)กลายเป็น ??? หมดเลย

หาในเน็ตอยู่นาน ปรากฏว่า ต้องเพิ่มคำสั่งนี้เข้าไปก่อนจะเริ่ม query SELECT

`$db->query("SET CHARACTER SET utf8");`

แต่ทำแบบนี้ก็กลายเป็นว่า ไม่รู้จะใช้ MDB2 (database abstraction layer) ไปทำไม เพราะ query นี้มันมีเฉพาะ MySQL ! 🙁

มีคนแจ้ง [“บั๊ก”](http://pear.php.net/bugs/bug.php?id=4666) (ขอเพิ่มฟีเจอร์) ไว้แล้ว
