---
title: "Ajax: A New Approach to Web Applications"
date: "2005-03-17T01:27:00+07:00"
lastmod: "2005-03-17T01:27:00+07:00"
type: "post"
url: "/2005/ajax-a-new-approach-to-web-applications/"
description: "Updated: 2005.03.18 add a report from News.com + more comments Ajax = Asynchronous JavaScript + XML (well, you can replace XML with JSON or whatever data structure you like) ใครเขียนพวกเวบแอพพลิเคชั่นอยู่ แล้วรู้สึกว่า มันน่าจะมีวิธีที่ดีกว่า เร็วกว่า สะดวกกว่า การมารีเฟรชหน้าจอบ่อยๆ ทั้งหน้า เพียงเ"
tag: ["ajax"]
textlang: "en"
wpid: 626
---
Updated: 2005.03.18 add a report from News.com + more comments

**Ajax** = Asynchronous JavaScript + XML  
(well, you can replace XML with [JSON](http://www.crockford.com/JSON/) or whatever data structure you like)

ใครเขียนพวกเวบแอพพลิเคชั่นอยู่ แล้วรู้สึกว่า มันน่าจะมีวิธีที่ดีกว่า เร็วกว่า สะดวกกว่า การมารีเฟรชหน้าจอบ่อยๆ ทั้งหน้า เพียงเพื่อจะอัพเดทข้อมูลแค่ไม่กี่บรรทัด บางทีวิธีที่เรียกว่า “Ajax” นี่ อาจจะช่วยคุณได้  
หลักๆ ก็คือ การใช้ JavaScript โหลดข้อมูลที่ต้องการผ่าน XMLHttpRequest แล้วก็เอามาอัพเดทในหน้าจอ ผ่าน DOM คือไม่ต้องมีการ GET/POST ฟอร์ม หรือว่ารีเฟรชหน้าจอทั้งหมดใหม่แต่อย่างใด แค่อัพเดทเฉพาะส่วนที่ต้องการเท่านั้น  
นอกจากนี้ก็ยังมีพูดถึงการออกแบบให้เข้ากับหลัก XHTML, CSS ด้วย (ซึ่งก็จะทำให้การเข้าถึงส่วนต่างๆ ของหน้าเว็บ ผ่าน DOM ทำได้ดี/ครอบคลุมยิ่งขึ้น)

From [this article](http://www.adaptivepath.com/publications/essays/archives/000385.php), by Jesse James Garrett, :

------------------------------------------------------------------------

***Defining Ajax***

*Ajax isn’t a technology. It’s really several technologies, each flourishing in its own right, coming together in powerful new ways. Ajax incorporates:*

- standards-based presentation using XHTML and CSS;
- dynamic display and interaction using the Document Object Model (DOM);
- data interchange and manipulation using XML and XSLT;
- asynchronous data retrieval using XMLHttpRequest;
- and JavaScript binding everything together.

------------------------------------------------------------------------

In my own words, it is more or less “a webpage with no refresh”. Hmm…

But will it works for an application that requires a lot of data to be transfered? Especially in the “low speed” area, like Thailand. Will it?  
I think currently it will be good only for low traffic application, like e-mail, instant messenging, or any text-oriented apps .. may be word processor as well.

And also what about security? I don’t think JavaScript has a strong security model (compare to Java or even .NET).

Another thing is, to my best knowledge, we still lack of a good JavaScript debugger. [Mozilla Venkman](http://www.mozilla.org/projects/venkman/) is there for a long while, true. But it still “in development”, version 0.9.something, not a production one yet.  
Thinking about building a large complex web application, millions lines of code .. without a good debugger — nightmare.

**About Ajax:**

- [Ajax Questions & Answers](http://www.adaptivepath.com/publications/essays/archives/000385.php#qanda)
- News.com: [Good-bye, computer; hello, world!](http://www.cnet.com/4520-6033_1-5759958-1.html?tag=nl.e501) — a rise of light-weighted web application. Ajax is mentioned.
- News.com: [Will AJAX help Google clean up?](http://news.com.com/Will+AJAX+help+Google+clean+up/2100-1032_3-5621010.html) — direction of Google/others on Ajax and other web app technologies (Java, Flash, XAML, XUL, WHAT-WG, etc.).
- อ่านเรื่องเกี่ยวกับเทคโนโลยีที่เกี่ยวข้องกับ Ajax (JavaScript, CSS, DHTML, etc.) ได้ที่ [pok ‘s blogger](http://pphetra.blogspot.com/).
