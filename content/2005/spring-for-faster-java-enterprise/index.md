---
title: "Spring for Faster Java Enterprise"
date: "2005-02-10T05:54:00+07:00"
lastmod: "2005-02-10T05:54:00+07:00"
type: "post"
url: "/2005/spring-for-faster-java-enterprise/"
description: "Better, Faster, Lighter Java by Bruce A. Tate, Justin Gehtland เป็นหนังสือที่ว่า(ด่า) Java ว่า ยิ่งทำ ยิ่งเลอะเทอะ ยิ่งเต่า (bloated) โดยเฉพาะพวก enterprise application framework ทั้งหลาย ที่ทำออกมาใหญ่เทอะทะเกินความจำเป็น และทำให้เรียนรู้นานขึ้น เขียนยากขึ้น มากขึ้น แต่ได้งานเท่าเดิม (และอาจจะผิดมา"
tag: ["java", "java-ee", "programming"]
textlang: "th"
wpid: 550
---
[Better, Faster, Lighter Java](http://www.oreilly.com/catalog/bfljava/) by Bruce A. Tate, Justin Gehtland  
เป็นหนังสือที่ว่า(ด่า) Java ว่า ยิ่งทำ ยิ่งเลอะเทอะ ยิ่งเต่า (bloated) โดยเฉพาะพวก enterprise application framework ทั้งหลาย ที่ทำออกมาใหญ่เทอะทะเกินความจำเป็น และทำให้เรียนรู้นานขึ้น เขียนยากขึ้น มากขึ้น แต่ได้งานเท่าเดิม (และอาจจะผิดมากกว่าเดิม) โดยพุ่งไปที่เป้าใหญ่ๆ อย่าง [EJB (Enterprise JavaBeans)](http://java.sun.com/products/ejb/) ว่าพยายามจะจับปลาสองมือ จะทำหลายๆ อย่าง ทำให้การออกแบบยุ่งเหยิง และ อืดเกินความจำเป็น ในหลายๆ งาน

หนังสือพยายามจะอธิบายว่า ความผิดมันไม่ได้อยู่ที่ตัวภาษา Java ว่ามันไม่ดี หรือว่าเฟรมเวิร์กมันห่วยแตก ใช้ไม่ได้เลย แต่อยู่ที่คนเขียนโปรแกรมนี่แหละ ที่แห่ตามไปใช้เฟรมเวิร์ก หรือเทคโนโลยีที่ฮิตๆ กัน โดยไม่ได้ดูเลยว่า มันเหมาะกับงานตัวเองรึเปล่า (คือจริงๆ EJB มันก็ดี แต่ไม่ใช่สำหรับทุกงาน เหมือนกับใช้ XML อ่านเขียนไฟล์คอนฟิก แค่ไม่กี่บรรทัด — คำพังเพยไทยคือ <u>ขี่ช้างจับตั๊กแตน</u>)

คนเขียน เป็นส่วนหนึ่งของทีมที่ทำ [Spring](http://www.springframework.org/) ซึ่งก็เป็น Java enterprise/web application framework แบบโอเพ่นซอร์สอีกตัวนึง ซึ่งออกแบบมาอย่างระมัดระวัง ไม่ให้เป็นเหมือนที่ไปว่าคนอื่นเค้าไว้ — Spring นี่ [มีตัวสำหรับ .NET ด้วย](http://www.springframework.net/)

เฟรมเวิร์กอีกตัวที่ดังๆ ก็คือ [Apache Struts](http://struts.apache.org/) คนนิยมใช้กันเยอะ (กว่า Spring) พูดถึงเฟรมเวิร์กพวกนี้แล้ว คนเขียน Java มีทางเลือกให้เลือกมากมาย (จนบางทีก็ปวดหัว เยอะเกินไป) อย่างแค่ในโครงการ [Jakarta](http://jakarta.apache.org/) ของ Apache เอง ก็มีตั้งหลายอัน เช่น Struts, [Tapestry](http://jakarta.apache.org/tapestry/), [Turbine](http://jakarta.apache.org/turbine/) หรืออย่าง [JBoss](http://www.jboss.org/) ก็มีเสนอของตัวเองเหมือนกัน รวมถึงที่ขายอย่าง [BEA WebLogic Platform](http://dev2dev.bea.com/), [IBM WebSphere Application Server](http://www-306.ibm.com/software/webservers/appserv/was/), [Oracle Application Server](http://www.oracle.com/appserver/), etc. .. กว่าจะเลือกได้ทีคงปวดหัว (พูดถึงโมเดลส่วนใหญ่ก็เป็น [MVC](http://en.wikipedia.org/wiki/Model-view-controller) คล้ายๆ กัน แต่ก็ต้องมีปัจจัยอื่นๆ ประกอบด้วย แล้วแต่งาน ความถนัด เวลา ทรัพยากร ฯลฯ)

ถ้าเขียนอะไรพวกนี้อยู่ แล้วมีความรู้สึกว่า ได้งานออกมาน้อยกว่าแรงที่ลง ก็ลองๆ ศึกษาทางเลือกใหม่ๆ ดู
