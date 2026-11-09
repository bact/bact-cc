---
title: "CSS @media rule"
date: "2005-07-17T15:13:00+07:00"
lastmod: "2011-05-12T00:19:45+07:00"
type: "post"
url: "/2005/css-media-rule/"
description: "Ease the Pain with IE6 Printing describes how to turn some elements on on the screen, but turn them off when we going to print the page out. This is possible by using CSS @media rule, part of CSS2 standard. ถ้าใช้เท็มเพลตของ Blogger.com ก็ใส่โค้ดนี้เข้าไปหลัง <style> @media print { #header, #descrip"
categories: ["computer"]
tag: ["css", "printing", "web-design"]
textlang: "en"
wpid: 893
---
[Ease the Pain with IE6 Printing](http://blogs.msdn.com/ie/archive/2005/06/10/428149.aspx) describes how to turn some elements on *on the screen*, but turn them off when we going to *print* the page out.

This is possible by using [CSS @media rule](http://msdn.microsoft.com/workshop/author/dhtml/reference/properties/media_1.asp), part of CSS2 standard.

ถ้าใช้เท็มเพลตของ Blogger.com ก็ใส่โค้ดนี้เข้าไปหลัง \<style\>

` `

    @media print {
     #header, #description, #sidebar { display: none; }
    }

` `

 

ประหยัดกระดาษได้เหมือนกันนะ
