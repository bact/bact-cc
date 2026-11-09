---
title: "OpenURL COinS: A Convention to Embed Bibliographic Metadata in HTML"
date: "2011-05-26T14:38:00+07:00"
lastmod: "2011-07-20T23:43:57+07:00"
type: "post"
url: "/2011/openurl-coins/"
description: "ทำความรู้จักกับ markup ที่ชื่อว่า COinS เอาไว้สำหรับระบุข้อมูล metadata ทรัพยากรห้องสมุดลงในหน้าเว็บ HTML ธรรมดา ๆ"
categories: ["informatics", "internet"]
tag: ["bibliographic", "contextobjects", "html", "information-and-library-sciences", "metadata", "openurl", "semantic-web"]
textlang: "th"
wpid: 2522
---
> [COinS](http://ocoins.info/) (ContextObjects in Spans) is a simple, ad hoc community specification for publishing OpenURL references in HTML.

[OpenURL](https://secure.wikimedia.org/wikipedia/en/wiki/OpenURL) นั้นเป็นรูปแบบสำหรับที่อยู่ทรัพยากร ใช้มากในระบบห้องสมุด หน้าตาก็ประมาณนี้:

> http://resolver.example.edu/cgi?url_ver=Z39.88-2004&rft_val_fmt=info:ofi/fmt:kev:mtx:book&rft.isbn=0836218310&rft.btitle=The+Far+Side+Gallery+3

เพื่อที่จะฝังข้อมูล OpenURL ลงไปใน HTML ธรรมดา ๆ COinS ใช้วิธีเอาข้อมูล OpenURL ดังกล่าว ยัดลงในแอตทริบิวต์ *title* ของอิลิเมนต์ `<span class="Z3988"></span>`

โดยอิลิเมนต์ `<span></span>` นี้ จะเป็นอิลิเมนต์เปล่า ๆ (empty span) ก็ได้ หรือจะใส่ข้อความลงไปด้วยก็ได้ (เพื่อให้ผู้ใช้สามารมองเห็นได้ / เพื่อป้องกัน span ที่ว่าง ถูกลบโดย HTML processor บางตัว)

Z3988 ที่เป็นชื่อคลาส มาจากหมายเลขมาตรฐาน [NISO Z39.88](http://standards-catalogue.ukoln.ac.uk/index/Z3988-2004) ของ OpenURL, ‘Z’ ในชื่อคลาส ต้องเป็นตัวพิมพ์ใหญ่, และ `<span></span>` ต้องไม่ถูก minimized เป็น `<span />` เพื่อคงความเข้ากันได้กับ HTML ไว้

ลองเล่นกะ [generator](http://generator.ocoins.info/) ดูก่อนได้

เว็บไซต์ ที่ฝัง COinS ลงไปในหน้าเว็บ เช่น Wikipedia, Physical Review Online Archive, CiteULike, Citebase, Open WorldCat ฯลฯ

ส่วนซอฟต์แวร์ที่อ่าน COinS ได้ เช่น Mendeley, VuFind, ฯลฯ ซึ่งมันจะอ่าน OpenURL metadata ที่อยู่ใน COinS ออกมาได้ ทำให้เราไม่ต้องนั่งพิมพ์ citation/bibliographic metadata พวกนี้เอง
