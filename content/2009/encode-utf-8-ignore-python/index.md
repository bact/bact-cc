---
title: "encode(\"UTF-8\", \"ignore\") ข้าม ๆ เรื่องที่ทำไม่ได้ใน Python"
date: "2009-04-22T18:48:00+07:00"
lastmod: "2011-05-07T21:22:37+07:00"
type: "post"
url: "/2009/encode-utf-8-ignore-python/"
description: "หลังจากเอา python-libthai ของวีร์มาใช้กับข้อมูลที่ได้มาจากเว็บ ก็พบปัญหาเรื่อง character encoding นิดหน่อย libthai นั้นปัจจุบันทำงานกับข้อมูลที่เป็นภาษาไทย 8 บิตอยู่ (น่าจะเป็น TIS-620) ตัว python-libthai เลยมีขั้นตอนการแปลงจากยูนิโค้ดไปเป็น 8 บิตก่อน ทีนี้ ปรากฏว่า encoder “CP874”, “TIS_620” และ “I"
categories: ["coling", "computer"]
tag: ["character-set", "encoding", "libthai", "natural-language-processing", "python", "thai", "unicode"]
textlang: "th"
wpid: 2445
---
หลังจากเอา [python-libthai](http://blog.vee-u.com/2009/03/10/%E0%B9%83%E0%B8%8A%E0%B9%89-libthai-%E0%B8%88%E0%B8%B2%E0%B8%81-python/ "ใช้ libthai จาก Python") ของวีร์[มาใช้](http://bact.blogspot.com/2009/04/on-flip-side-of-hero.html "ติดตั้งบน Mac OS X + MacPorts")กับข้อมูลที่ได้มาจากเว็บ ก็พบปัญหาเรื่อง character encoding นิดหน่อย

[libthai](http://linux.thai.net/projects/libthai "libthai Library") นั้นปัจจุบันทำงานกับข้อมูลที่เป็นภาษาไทย 8 บิตอยู่ (น่าจะเป็น TIS-620) ตัว python-libthai เลยมีขั้นตอนการแปลงจากยูนิโค้ดไปเป็น 8 บิตก่อน  
ทีนี้ ปรากฏว่า encoder “CP874”, “TIS_620” และ “ISO8859_11” ของ Python มันดันแปลงตัวอักษรบางตัวไม่ได้ (เนื่องจากใน charset พวกนั้น มันไม่มีตัวอักษรดังกล่าว) โปรแกรมก็เลยจะตาย ถ้าไปเจออักษรพวกนั้น

ก่อนตายมันจะโวยทำนองว่า :

    UnicodeEncodeError: 'charmap' codec can't encode character
    u'\u200b' in position 3560: character maps to <undefined>

วิธีแก้แบบถึก ๆ คือ เอาหูไปนาเอาตาไปไร่ซะ ignore มัน ด้วยการไปแก้ แฟ้มชื่อ **libthai.c** ของ python-libthai (แฟ้มนี้เป็น wrapper ที่ไปเรียก libthai ให้)

หาบรรทัดที่เรียกฟังก์ชั่น `PyUnicode_Encode/Decode` แล้วแก้พารามิเตอร์ตัวที่สี่เป็น “ignore” ซะ

เช่น จาก

<pre><code>
PyObject *txt_cp874 =
    PyUnicode_Encode(s1, s1_len, "CP874", <span style="color: red;">NULL</span>);
tok =
    PyUnicode_Decode(buffer, tok_len, "CP874", <span style="color: red;">NULL</span>);
</code></pre>

เป็น

<pre><code>
PyObject *txt_cp874 =
    PyUnicode_Encode(s1, s1_len, "CP874", <span style="color: red;">"ignore"</span>);
tok =
    PyUnicode_Decode(buffer, tok_len, "CP874", <span style="color: red;">"ignore"</span>);
</code></pre>

แล้ว sudo python setup.py install ใหม่อีกรอบ (อย่าลืมล้าง build เก่าทิ้งก่อน) ก็น่าจะใช้ได้แล้วครับ

ลิงก์ : [Python Unicode How-to](http://www.amk.ca/python/howto/unicode)

<span class="small">technorati tags: [libthai](http://technorati.com/tag/libthai), [Python](http://technorati.com/tag/Python), [Unicode](http://technorati.com/tag/Unicode)  
</span>
