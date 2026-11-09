---
title: "i18n ใน PHP"
date: "2004-11-02T05:56:00+07:00"
lastmod: "2004-11-02T05:56:00+07:00"
type: "post"
url: "/2004/i18n-ใน-php/"
description: "ตอนนี้ความสามารถเรื่อง internationalization ใน PHP ยังไม่ค่อยดี .. อืม เรียกว่ายังไม่มีจะดีกว่า ใน PEAR มีโครงการ i18n อยู่ 3 ตัว แต่ก็เป็นแค่เรื่องพื้นๆ อย่าง encoding, locale และ translation (resource) ส่วนเรื่องที่ซับซ้อนกว่านั้น เช่น text iterator ยังไม่มี จริงๆ ก็มีคนพยายามทำแล้วนะ ชื่อ php-i18"
tag: ["localization", "php"]
textlang: "th"
wpid: 419
---
ตอนนี้ความสามารถเรื่อง internationalization ใน PHP ยังไม่ค่อยดี .. อืม เรียกว่ายังไม่มีจะดีกว่า

ใน PEAR มีโครงการ i18n อยู่ [3 ตัว](http://pear.php.net/packages.php?catpid=28&catname=Internationalization) แต่ก็เป็นแค่เรื่องพื้นๆ อย่าง encoding, locale และ translation (resource) ส่วนเรื่องที่ซับซ้อนกว่านั้น เช่น text iterator ยังไม่มี

จริงๆ ก็มีคนพยายามทำแล้วนะ ชื่อ [php-i18n](http://www.php.gr.jp/project/i18n/README.i18n_eng.html) เป็น patch สำหรับ PHP 3 โดยมีความสามารถต่างๆ [คล้ายๆ i18n ของ Java](http://computingnews.com/article/php.i18n/20) — แต่: รองรับเฉพาะภาษาญี่ปุ่น (เพิ่มภาษาอื่นได้ แต่ยังไม่มี), ต้องคอมไพล์ตัว PHP runtime ใหม่ (ใครเช่าโฮสต์อยู่ ก็หมดสิทธิ์), ใช้ได้กับ PHP 3 เท่านั้น (lib หลักๆ ส่วนใหญ่ตอนนี้ต้องเป็น PHP 4 ขึ้นไปหมดแล้ว)

ใน PHP 4 มี [mbstring](http://php.net/mbstring) (Multibyte String) มาให้ใช้ แต่ก็ไม่ได้เป็น default extension, ต้อง –enable-mbstring=all ตอนคอมไพล์เอง .. ส่วนใหญ่โฮสต์ที่เช่า เค้าก็ลงแต่ตัวที่เป็น default .. ว้า

อะไรเนี่ย อย่าให้ถึงกับต้องหนีไปใช้ JSP เลยน่า นอกจากค่าเช่าโฮสต์มันจะแพงแล้ว ความสามารถที่อยากใช้หลายๆ อย่าง มันมีคนเขียนให้เรียบร้อยแล้ว เป็น PHP (อย่างพวก Smarty, Markdown) อยากให้ระบบ autheticate ของ [Drupal](http://drupal.org/) ด้วยอ่ะ ไม่รู้ใน Java มีคนทำไว้รึยัง ให้เขียนเองหมดนี่ท่าจะงานเยอะ

ช่วงนี้ก็หาอะไรโน่นนี่ไปเรื่อยๆ อยากทำระบบ online publishing ซักตัว เดือนที่ผ่านมาลองมาหลายตัว ถูำกใจก็หลายตัว แต่ตัวละอย่างสองอย่าง ลองนึกคร่าวๆ ไล่ๆ ว่าถ้าจะทำเองต้องทำอะไรบ้าง เยอะเหมือนกันนะ

งงๆ เดี๋ยวค่อยหาต่อ

[PHP i18n to improve?](http://www.sitepoint.com/blog-post-view.php?id=188871)
