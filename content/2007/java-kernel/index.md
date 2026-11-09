---
title: "Java Kernel"
date: "2007-01-14T09:23:00+07:00"
lastmod: "2007-01-14T09:23:00+07:00"
type: "post"
url: "/2007/java-kernel/"
description: "หลายคนคงเคยบ่นว่า ทำไมตัว Java Runtime มันใหญ่จัง น่าจะเล็ก ๆ กว่านี้หน่อย แล้วจะใช้อะไรเพิ่มก็ค่อยให้มันไปดาวน์โหลดเอาเอง (คิดแบบยุค always on) บัดนี้ความฝันกำลังจะเป็นจริงแล้ว ด้วยโครงการ Java Kernel (หรือชื่อเดิม “Java Browser Edition”) ซึ่งถ้าทำสำเร็จเนี่ย (เป้าหมายคือ Java 7) เราอาจจะเห็น Java "
tag: ["java", "java-kernel"]
textlang: "th"
wpid: 1858
---
หลายคนคงเคยบ่นว่า ทำไมตัว Java Runtime มันใหญ่จัง  
น่าจะเล็ก ๆ กว่านี้หน่อย แล้วจะใช้อะไรเพิ่มก็ค่อยให้มันไปดาวน์โหลดเอาเอง (คิดแบบยุค always on)

บัดนี้ความฝันกำลังจะเป็นจริงแล้ว ด้วยโครงการ [Java Kernel](http://weblogs.java.net/blog/enicholas/archive/2006/09/java_browser_ed.html "Java Browser Edition: New name, first steps") (หรือชื่อเดิม [“Java Browser Edition”](http://weblogs.java.net/blog/enicholas/archive/2006/04/java_2_browser.html))  
ซึ่งถ้าทำสำเร็จเนี่ย (เป้าหมายคือ Java 7) เราอาจจะเห็น Java Kernel ขนาด 3 MB ก็เป็นได้

อย่างไรก็ตาม ก็ยังมีคนคิดว่า[มันไม่ช่วยเท่าไหร่หรอก](http://blogs.zdnet.com/Burnette/?p=169 "Java Browser Edition: New name, wrong direction")

[คุณ Chanwit](http://chanwit.blogspot.com/ "CK's Blog") ทดลองลดขนาด rt.jar ดู เอาแค่ให้รันโปรแกรม “Hello World” ได้  
โดยใช้ `java -verbose` + โปรแกรม 7z ช่วย — [จาก 36 MB เหลือ 1.8 MB](http://chanwit.blogspot.com/2006/11/minimum-rtjar-for-hello-world.html "Minimum 'rt.jar' for Hello World") น่าสนใจ

\[ลิงก์ [“Java Browser Edition”: New name, first steps](http://weblogs.java.net/blog/enicholas/archive/2006/09/java_browser_ed.html) \| ผ่าน [CK’s Blog](http://chanwit.blogspot.com/2006/11/minimum-rtjar-for-hello-world.html "Minimum 'rt.jar' for Hello World")\]

<span class="small">technorati tags:  
[Java](http://technorati.com/tag/Java),  
[Java Kernel](http://technorati.com/tag/Java_Kernel)  
</span>
