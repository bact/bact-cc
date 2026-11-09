---
title: "Open source Java port for Mac OS X"
date: "2007-11-28T00:06:00+07:00"
lastmod: "2011-05-17T14:30:10+07:00"
type: "post"
url: "/2007/open-source-java-port-for-mac-os-x/"
description: "Open Source Java 6 port สำหรับ Mac OS X มาแล้ว (รุ่น Developer Preview Release 2) ใช้ได้ทั้งบน Mac OS X 10.4 และ 10.5 ทั้ง 32-bit และ 64-bit Java 6 port สำหรับ Mac OS X ตัวนี้ ไม่ได้มาจาก Apple แต่มาจากนักพัฒนาอิสระชื่อ Landon Fuller โดยใช้โค้ดจาก BSD Java port (Mac OS X มีหลายส่วนที่พัฒนาจาก BSD) ซ"
categories: ["computer"]
tag: ["free-softwares", "freebsd", "java", "jdk", "mac-os-x", "open-source", "openjdk"]
textlang: "th"
wpid: 2216
---
[Open Source Java 6 port สำหรับ Mac OS X](http://landonf.bikemonkey.org/code/macosx/) มาแล้ว (รุ่น Developer Preview Release 2) ใช้ได้ทั้งบน Mac OS X 10.4 และ 10.5 ทั้ง 32-bit และ 64-bit

Java 6 port สำหรับ Mac OS X ตัวนี้ ไม่ได้มาจาก Apple แต่มาจากนักพัฒนาอิสระชื่อ *Landon Fuller*  
โดยใช้โค้ดจาก [BSD Java port](http://www.eyesbeyond.com/freebsddom/java/jdk16.html) (Mac OS X มีหลายส่วนที่พัฒนาจาก BSD) ซึ่งใช้สัญญาอนุญาต [Java Research License](http://java.net/jrl.csp) (มาจากเจรจาระหว่างโครงการ FreeBSD และ Sun)

Landon มีแผนจะส่งโค้ดนี้เข้าโครงการ BSD Java port ต่อไป และโครงการ BSD Java port เองก็มีเป้าหมายที่จะรวมงานของตนเข้ากับโครงการ OpenJDK  
(ซึ่งใช้สัญญาอนุญาต [GPLv2+Classpath Exception](http://openjdk.java.net/legal/gplv2+ce.html))

ในเว็บไซต์ของ Landon Fuller มี[โชว์ Puzzle Pirates ที่รันบน Java 6 port ตัวนี้](http://landonf.bikemonkey.org/code/macosx/FreeBSD_Java_16_Status_Update.20071112.html)ด้วย ผมชอบเกมนี้มาก เคยติดงอมแงมอยู่พักนึง  
นอกจากนี้ก็มี[ภาพ Eclipse (ตัวอย่างของแอพพลิเคชั่น SWT) ที่ใช้ Carbon](http://landonf.bikemonkey.org/code/macosx/MacOS_Java_Native_SWT.20071122.html) ด้วย

*Charles Nutter* นักพัฒนา JRuby [ได้ทดสอบ Open Source Java 6 port ตัวนี้กับ JRuby](http://headius.blogspot.com/2007/11/java-6-port-for-os-x-tiger-and-leopard.html)  
พบว่าในการทดสอบเลขคำนวณจำนวนเต็ม (fibonacci test)  
JRuby trunk บน open source Java 6 port มีประสิทธิภาพดีกว่าบน Apple JDK 6 preview และตามหลัง Ruby 1.9 (native) ไม่ไกลนัก  
และหากให้ JRuby trunk บน open source Java 6 port ทำงานในโหมด frameless execution แล้วมันจะมีประสิทธิภาพดีกว่า Ruby 1.9 อยู่เล็กน้อย

ส่วนในการทดสอบ MatrixBenchmark  
JRuby บน open source Java 6 port ทำงานเร็วกว่า Ruby 1.9 อยู่ราว 25%

แบบนี้นักพัฒนา (จาวา) จำนวนหนึ่งอาจจะยังใช้ Mac OS X 10.4 ต่อไปได้อีกสักพักใหญ่ ๆ เลยล่ะ ไม่ต้องง้อ Apple แล้วเรื่อง JDK — เว้นว่าถ้าอยากจะเขียนโปรแกรมที่ใช้หน้าตาแบบ Cocao ด้วย Java อันนั้นก็อีกเรื่องนึง แต่ถ้าเป็นเรื่องที่ไม่เกี่ยวกับ UI ก็สบายแล้ว

(ตะกี้ได้กิน “ก๊อบ กอบ” ครั้งแรกในรอบหลายปี ได้รสชาติที่ต่างไปจากเลย์จริง ๆ เบื่อเลย์ ตอนแรกจะหยิบเทสโต แต่เหลือบไปเห็นก๊อบ กอบ ซะก่อน ได้เยอะกว่าด้วย มากกว่าตั้ง 10 กรัม :P)

\[ ลิงก์ [Landon Fuller](http://landonf.bikemonkey.org/code/macosx/ "Landon Fuller: Mac OS X") \| ผ่าน [Slashdot](http://apple.slashdot.org/apple/07/11/27/1547212.shtml "Java 6 Available on OSX Thanks to Port of OpenJDK") \]

<span class="small">technorati tags: [JDK](http://technorati.com/tag/JDK), [BSD](http://technorati.com/tag/BSD), [Mac OS X](http://technorati.com/tag/Mac_OS_X)  
</span>
