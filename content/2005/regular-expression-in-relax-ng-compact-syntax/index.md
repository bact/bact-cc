---
title: "Regular expression in Relax NG Compact syntax"
date: "2005-07-29T19:17:00+07:00"
lastmod: "2005-07-29T19:17:00+07:00"
type: "post"
url: "/2005/regular-expression-in-relax-ng-compact-syntax/"
description: "ถ้าอยากกำหนดรูปแบบข้อมูลที่จะอนุญาตให้ใส่ใน XML ของเรา ลงไปใน schema language เพื่อที่จะได้ตรวจได้โดย XML validator ใน Relax NG นี่ เราไปยืม pattern จาก W3C XML Schema datatypes มาใช้ได้ โดยตัว pattern นี่ มันก็คือ regular expression น่ะแหละ ใช้งี้: xsd:string { pattern = “regular_expression_here” }"
tag: ["regular-expression", "relax-ng", "schema", "xml"]
textlang: "th"
wpid: 927
---
ถ้าอยากกำหนดรูปแบบข้อมูลที่จะอนุญาตให้ใส่ใน XML ของเรา ลงไปใน schema language เพื่อที่จะได้ตรวจได้โดย XML validator ใน Relax NG นี่ เราไปยืม *pattern* จาก W3C XML Schema datatypes มาใช้ได้

โดยตัว *pattern* นี่ มันก็คือ [regular expression](http://en.wikipedia.org/wiki/Regular_expression) น่ะแหละ

ใช้งี้:

`xsd:string { pattern = "`*`regular_expression_here`*`" }`

เช่น ถ้าเราเขียน:

    # ยืม datatypes ของ W3C XML Schema มาใช้
    datatypes xsd = "http://www.w3.org/2001/XMLSchema-datatypes"

    # กำหนดรูปแบบข้อมูลเอง
    Percent.data = ( xsd:string{ pattern = "(100|[1-9]?[0-9])[%]" } )

    Style = element font {
      attribute weight { Percent.data }, # เอามาใช้ตรงนี้
      attribute color { "green" | "greener" }, # ถ้าแค่นี้ ไม่ต้องใช้ pattern ก็ได้
      text
    }

ตัวอิลิเมนต์ font ก็จะเอาไปใช้ได้ประมาณนี้:

    <font color="greener" weight="80%">bact'</font>

นี่ไม่ได้เปิดหนังสือดู อาศัยมั่ว ๆ หาเอาจากเน็ต เลยยังไม่แน่ใจว่า *pattern* เนี่ย มันใช้กับอย่างอื่นนอกจาก *xsd:string* ได้รึเปล่า ?
