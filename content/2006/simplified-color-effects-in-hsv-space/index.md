---
title: "Simplified color effects in HSV space"
date: "2006-01-05T16:47:00+07:00"
lastmod: "2006-01-05T16:47:00+07:00"
type: "post"
url: "/2006/simplified-color-effects-in-hsv-space/"
description: "Desaturation and fading example, using HSV color space, in JavaScript. ปกติ JavaScript จะใช้ค่าสีแบบ RGB ซึ่งไม่ค่อยสะดวกนักสำหรับการทำ desaturation (อิ่มตัว?) และ fading (เลือน?) แต่ถ้าใช้ค่าสีแบบ HSV (hue, saturation, value/brightness) เราสามารถเปลี่ยนค่า s กับ v ได้โดยตรงเลย ตัวอย่าง JavaScript ใ"
categories: ["something"]
textlang: "th"
wpid: 1152
---
[Desaturation and fading example](http://split-s.blogspot.com/2005/12/simple-color-effects.html), using [HSV color space](http://en.wikipedia.org/wiki/HSV_color_space), in JavaScript.

ปกติ JavaScript จะใช้ค่าสีแบบ RGB ซึ่งไม่ค่อยสะดวกนักสำหรับการทำ desaturation (อิ่มตัว?) และ fading (เลือน?) แต่ถ้าใช้ค่าสีแบบ HSV (hue, saturation, value/brightness) เราสามารถเปลี่ยนค่า s กับ v ได้โดยตรงเลย

ตัวอย่าง JavaScript ในเว็บนั้น แสดงฟังก์ชั่นแปลง RGB \< -\> HSV, และฟังก์ชั่นทำ fading, desaturation โดยการเปลี่ยนค่าสีในแบบ HSV

- [RGB](http://en.wikipedia.org/wiki/RGB_color_model), for monitors
- [HSV](http://en.wikipedia.org/wiki/HSV_color_space)
- [HSL](http://en.wikipedia.org/wiki/HSL_color_space)
- [CMYK](http://en.wikipedia.org/wiki/CMYK_color_model), for printings
