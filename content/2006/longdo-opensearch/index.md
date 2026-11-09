---
title: "Longdo OpenSearch"
date: "2006-07-19T23:56:00+07:00"
lastmod: "2006-07-19T23:56:00+07:00"
type: "post"
url: "/2006/longdo-opensearch/"
description: "Thai OpenSearch plugins นั่งทำอยู่ซักพัก เป็นปลั๊กอินเปิดพจนานุกรม Longdo โดยใช้ OpenSearch ลองทดสอบกันดูครับ มีแนะคำโดยใช้ Google Suggest ช่วยด้วย(!) ควรจะใช้งานได้กับทั้ง Mozilla Firefox 2 และ Internet Explorer 7 (ผมไม่ได้ลองกะ IE7) ไม่รู้ Opera ได้รึเปล่า สำหรับ Firefox 2 ตัวเบราว์เซอร์มันควรจะ d"
tag: ["dictionary", "me", "search-engines"]
textlang: "th"
wpid: 1563
---
[Thai OpenSearch plugins](http://siit.net/members/art/searchplugins/)

นั่งทำอยู่ซักพัก เป็นปลั๊กอินเปิดพจนานุกรม [Longdo](http://dict.longdo.org/) โดยใช้ [OpenSearch](http://en.wikipedia.org/wiki/OpenSearch) ลองทดสอบกันดูครับ  
มีแนะคำโดยใช้ [Google Suggest](http://labs.google.com/suggest/faq.html) ช่วยด้วย(!)

ควรจะใช้งานได้กับทั้ง Mozilla Firefox 2 และ Internet Explorer 7 (ผมไม่ได้ลองกะ IE7) ไม่รู้ Opera ได้รึเปล่า  
สำหรับ Firefox 2 ตัวเบราว์เซอร์มันควรจะ detect ปลั๊กอินให้อัตโนมัติ ให้สังเกตว่ารูปแว่นขยายมันจะเปลี่ยนเป็นสีส้ม ๆ ลองกดดู จะมีคำว่า “Add Longdo” ให้เลือก (พี่อ็อท: ก็อปโค้ดไปแปะ HTML head ของเว็บ Longdo ได้เลยครับ อันนี้:

    <link rel="search" title="Longdo"
    href="http://siit.net/members/art/searchplugins/longdo.xml"
    type="application/opensearchdescription+xml">

ข้างล่างนี้คือเอกสารที่อ่านตอนทำ ตอนแรกงง ๆ หน่อย เพราะ MozSearch มันตีกะ OpenSearch (ใครว่า Mozilla ชอบมาตรฐานเปิด? – -“):

- [Creating MozSearch plugins](http://developer.mozilla.org/en/docs/Creating_MozSearch_plugins) (+OpenSearch)
- [Supporting search suggestions in search plugins](http://developer.mozilla.org/en/docs/Supporting_search_suggestions_in_search_plugins)
- [Adding search engines from web pages](http://developer.mozilla.org/en/docs/Adding_search_engines_from_web_pages)
- แถม: [OpenSearch Icon (a proposal, Feed Icon-like)](http://www.unto.net/unto/opensearch/an-opensearch-icon/)

OpenSearch กับ MozSearch นั้นคล้ายกันมาก แต่ดู MozSearch จะเขียนง่ายกว่า และเจ้าฟังก์ชั่น  
suggestions นี่ ใน OpenSearch ยังไม่มี ([กำลังเสนออยู่ โดยอิง MozSearch](http://www.unto.net/wiki/OpenSearch_suggestions_extension))

Longdo OpenSearch <span class="small">(เป็นคำประกอบ หมายถึงปลั๊กอินค้นหาแบบ OpenSearch สำหรับบริการพจนานุกรม Longdo ไม่ได้เป็นชื่อเฉพาะ “Longdo OpenSearch” นะ เพราะจะผิด[สัญญาอนุญาตของ Longdo](http://dict.longdo.org/download/license.txt) น่ะ)</span> นั้น ตั้งใจเขียนให้เป็น OpenSearch แต่มีใช้ suggestions ด้วย — ซึ่งมันยังไม่มีใน[ข้อกำหนด OpenSearch](http://opensearch.a9.com/spec/1.1/) —  
แต่ก็ไม่น่าจะเป็นปัญหา เพราะว่าฟังก์ชั่นนี้เรียกใช้โดยการระบุอีเลเมนต์ Url เพิ่มอีกหนึ่งชุด  
โดยกำหนดแอตทริบิวต์ type เป็น “application/x-suggestions+json”  
ซึ่งอีเลเมนต์ Url นั้น อยู่ใน [schema ของ OpenSearch](http://opensearch.a9.com/spec/1.1/description/) อยู่แล้ว (= XML ยัง valid)

และโดยข้อกำหนดถ้าตัว application ไม่รองรับ type แบบไหน ก็จะข้ามไป ไม่สนใจ จึงไม่น่าจะมีปัญหากับ IE คือ IE ก็แค่ไม่มีความสามารถเรื่องแนะคำเฉย ๆ อย่างอื่นยังใช้ได้ (แต่ผมยังไม่ได้ทดสอบอยู่ดี เมื่อคืนลง IE7 เสร็จ เปิดมาแล้วแฮงค์ตลอด ใช้ไม่ได้เลย ลองเป็นสิบรอบแล้ว แค่้จะเปิดโปรแกรมยังไม่ได้ … beta quality จริง ๆ – -“)

ตอนเขียนก็ดู ๆ เอกสาร ประกอบกับตัวอย่าง google.xml ที่มากับ Firefox 2

ตรงส่วนอีเลเมนต์ Image นั้น ในตัวอย่าง google.xml (ซึ่งเป็น MozSearch) ใช้เป็น base64 เก็บข้อมูลตรง ๆ เลย:

    <Image width="16"
    height="16">data:image/x-icon;base64,(ข้อมูลรูปภาพ)</Image>

แต่ใน [ตัวอย่างที่เว็บ OpenSearch](http://opensearch.a9.com/spec/1.1/description/) เห็นใช้เป็นลิงก์:

    <Image height="64" width="64"
    type="image/png">http://example.com/websearch.png</Image>

(ตรง type จะเป็นภาพแบบไหนก็ได้ gif, jpg, png, ico)

ตัว Longdo OpenSearch นี่ ใช้ base64 😛 โดยข้อมูลรูปภาพนั้น ก็ก็อปมาจากปลั๊กอินเก่า

คือใน Firefox 2 นี่ เวลาเราติดตั้งปลั๊กอิน Mycroft มันจะแปลงเป็น MozSearch/OpenSearch  
<span class="small">(root element เป็นของ MozSearch แต่มีใช้ XML namespace OpenSearch ด้วย)</span>  
ให้อัตโนมัติ รูปที่เคยเป็นไฟล์แยกต่างหาก มันก็จะแปลงเป็น base64 ยัดลงมาใน XML ให้  
.. เราก็ไปก็อปไอ้ข้อมูลตรงนั้นแหละมาใช้  
แต่ถ้าจะแปลงเองจากรูปโดยตรงเลย ที่เว็บมอซิลล่าเค้าแนะนำให้ใช้เว็บ [URI kitchen](http://software.hixie.ch/utilities/cgi/data/data) ช่วยแปลง

พูดถึงวิธีเก็บรูป ไม่แน่ใจว่า MozSearch กับ OpenSearch มันต่างกันตรงนี้มั๊ย หรือว่าใช้แบบไหนก็ได้ทั้งคู่  
ตรงนี้ถ้ามองว่าอันไหนโปร่งใส/transparent กว่า ก็ต้องบอกว่า เก็บ url รูปน่ะโปร่งใสดูดีกว่า  
แต่ถ้าพูดถึงประสิทธิภาพ รูปไอคอนขนาดเล็ก ๆ แบบนี้ จะให้เปิด connection อีกหนึ่งอันเพื่อดาวน์โหลด มันก็ อืม คงไม่คุ้ม ก็เก็บรวมมันไว้ในไฟล์เดียวเลยละกัน เป็นไบนารี/base64 … แต่แบบนี้มันก็ ไม่ค่อยจะ XML ?

ก็แล้วแต่เลือกล่ะ

**จะทำ:** ทำรายการแนะคำจากข้อมูลพจนานุกรมโดยเฉพาะ ?

**ปรับปรุง:**

- 2006.07.21 – ชี้แจ้งเรื่องชื่อปลั๊กอิน+สัญญาอนุญาต, เพิ่ม “จะทำ”
- 2006.07.20 – เพิ่มข้อมูลเทคนิก

**tags:**  
[Longdo](http://technorati.com/tag/longdo)  
[search](http://technorati.com/tag/search)  
[plugins](http://technorati.com/tag/plugins)  
[OpenSearch](http://technorati.com/tag/opensearch)  
[MozSearch](http://technorati.com/tag/mozsearch)  
[Firefox](http://technorati.com/tag/firefox)  
[IE7](http://technorati.com/tag/ie7)
