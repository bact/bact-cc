---
title: "Label-specific feed from Blogger"
date: "2007-05-30T01:32:00+07:00"
lastmod: "2007-05-30T01:32:00+07:00"
type: "post"
url: "/2007/label-specific-feed-from-blogger/"
description: "เวลาเรียกดูบล็อกใน Blogger/Blogspot หากต้องการดูเฉพาะโพสต์ที่มีป้าย (label) ที่กำหนดเท่านั้น เราสามารถใช้ url ลักษณะนี้: http://BLOGNAME.blogspot.com/search/LABEL เช่น http://bact.blogspot.com/search/label/quotes ส่วนถ้าหากต้องการป้อนฟีด แบบเลือกเฉพาะโพสต์ที่มีป้ายที่กำหนด ให้ใช้ url ลักษณะนี้: http"
tag: ["blogs", "new-blogger"]
textlang: "th"
wpid: 2102
---
เวลาเรียกดูบล็อกใน Blogger/Blogspot หากต้องการดูเฉพาะโพสต์ที่มีป้าย (label) ที่กำหนดเท่านั้น เราสามารถใช้ url ลักษณะนี้:

http://***BLOGNAME***.blogspot.com/search/***LABEL***

เช่น  
<http://bact.blogspot.com/search/label/quotes>

ส่วนถ้าหากต้องการป้อนฟีด แบบเลือกเฉพาะโพสต์ที่มีป้ายที่กำหนด ให้ใช้ url ลักษณะนี้:

http://***BLOGNAME***.blogspot.com/feeds/posts/***TYPE***/-/***LABEL***

TYPE นี่ เป็นได้ทั้ง “full”, “summary”, และ “default” – ปกติจะใช้ default

LABEL เราสามารถใส่ได้มากกว่าหนึ่งป้าย, โดยมันจะเอามา and กัน, เช่น:

<http://bact.blogspot.com/feeds/posts/default/-/Bangkok>  
ฟีดเฉพาะโพสต์ที่มีป้าย Bangkok

<http://bact.blogspot.com/feeds/posts/default/-/Berlin>  
ฟีดเฉพาะโพสต์ที่มีป้าย Berlin

<http://bact.blogspot.com/feeds/posts/default/-/Berlin/Bangkok>  
ฟีดเฉพาะโพสต์ที่มีทั้งป้าย Bangkok และ Berlin อยู่ด้วยกัน

ชื่อป้ายนั้น ตัวใหญ่ตัวเล็กมีความสำคัญ (case-sensitive) ใส่ผิดก็ไม่ขึ้น

Blogger Help: [Can I get site feeds for specific labels?](http://help.blogger.com/bin/answer.py?answer=53336&topic=8927)

PurpleMoggy’s Blog: [Blogger Beta Feeds](http://purplemoggy.blogspot.com/2006/09/blogger-beta-feeds.html)

<span class="small">technorati tags:  
[Blogger](http://technorati.com/tag/Blogger),  
[feed](http://technorati.com/tag/feed)  
</span>
