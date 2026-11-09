---
title: "แปะ embed ง่าย ด้วย oEmbed"
date: "2009-07-22T10:45:00+07:00"
lastmod: "2011-01-12T09:30:49+07:00"
type: "post"
url: "/2009/แปะ-embed-ง่าย-ด้วย-oembed/"
description: "oEmbed is a format for allowing an embedded representation of a URL on third party sites. The simple API allows a website to display embedded content (such as photos or videos) when a user posts a link to that resource, without having to parse the resource directly. ไอเดียแก่นของ social media หรือ ส"
categories: ["media"]
tag: ["api", "programming", "social-media"]
textlang: "th"
wpid: 2457
---
> oEmbed is a format for allowing an embedded representation of a URL on third party sites. The simple API allows a website to display embedded content (such as photos or videos) when a user posts a link to that resource, without having to parse the resource directly.

ไอเดียแก่นของ social media หรือ สื่อทางสังคม ก็คือมัน(ต้อง) share หรือ แบ่งปัน ได้ง่าย การบอกต่อมันถึงจะไปได้ไกล

[oEmbed](http://www.oembed.com/ "oEmbed") เป็นข้อตกลงสำหรับรูปแบบการ “แปะ” สื่อ embed (เช่น วิดีโอ เสียง แฟลช) ที่ทำให้ผู้ใช้แปะเพียง url ไม่ต้องแปะโค้ด html ยาว ๆ ซึ่งนอกจากจะงงแล้ว ยังมีโอกาสผิดพลาดด้วย

เมื่อเว็บไซต์พบ url ที่ผู้ใช้ใส่เข้ามา ก็จะวิ่งไปถามตัวผู้ให้บริการสื่อชิ้นนั้น ว่าควรจะใช้โค้ด html แบบไหน แล้วจัดการที่เหลือให้อัตโนมัติ เช่น:

1. ผู้ใช้แปะลิงก์รูป *http://www.flickr.com/photos/bees/2341623661/* ในเว็บบอร์ด

2. เว็บบอร์ดพบว่า ลิงก์ดังกล่าว เข้าแก๊ป URL scheme: *http://\*.flickr.com/photos/\** ซึ่งแปลว่าเป็น embed representation ซึ่งเชื่อมอยู่กับ API endpoint: *http://www.flickr.com/services/oembed/*

3. เว็บบอร์ดจึงถามข้อมูลของ embed ตัวนี้ ไปที่ API endpoint โดยใช้ request ดังนี้ *http://www.flickr.com/services/oembed/?url=http%3A//www.flickr.com/photos/bees/2341623661/*

4. ตัว API ส่งข้อมูลกลับมาให้เว็บบอร์ด เป็น XML หรือ JSON เช่น

        {
         "version": "1.0",
         "type": "photo",
         "width": 240,
         "height": 160,
         "title": "ZB8T0193",
         "url": "http://farm4.static.flickr.com/3123/2341623661_7c99f48bbf_m.jpg",
         "author_name": "Bees",
         "author_url": "http://www.flickr.com/photos/bees/",
         "provider_name": "Flickr",
         "provider_url": "http://www.flickr.com/"
        }

5. ตัวเว็บบอร์ด ก็จะเอาข้อมูลตรงนี้ ไปสร้างโค้ด embed ให้เอง

ในมุมมองของผู้ใช้แล้ว แบบนี้ง่ายกว่าเยอะ

ในมุมมองของนักพัฒนาเว็บ แบบนี้ก็ปลอดภัยกว่าด้วย เนื่องจากการได้ข้อมูลของสื่อ embed ผ่าน oEmbed API ทำให้เราไม่ต้องเดาข้อมูลต่าง ๆ เอง หรือ parse ข้อมูลแบบ hack ๆ กันเอาเอง ซึ่งแม้จะใช้งานได้ แต่ถ้าเมื่อไหร่ url หรือ html ของหน้าสื่อนั้นเปลี่ยน ก็จะเกิด dead link ทันที

มีบริการรับฝากสื่อออนไลน์หลายแห่งใช้ oEmbed แล้ว เช่น Flickr สำหรับภาพ และ Vimeo สำหรับภาพเคลื่อนไหว

Providers (ตอบ request oEmbed ได้):  
[Flickr](http://flickr.com/services/oembed?url=http%3A//flickr.com/photos/bees/2362225867/), [Viddler](http://wiki.developers.viddler.com/index.php/OEMBED "documentation"), [Qik](http://qik.com/api/oembed.xml?url=http%3A//qik.com/video/49565), [Pownce](http://api.pownce.com/2.1/oembed.xml?url=http%3A//pownce.com/mmalone/notes/1756545/), [Revision3](http://revision3.com/api/oembed/?url=http%3A//revision3.com/diggnation/2008-04-17xsanned/&format=xml), [Hulu](http://www.hulu.com/api/oembed.xml?url=http%3A//www.hulu.com/watch/20807/late-night-with-conan-obrien-wed-may-21-2008), [Vimeo](http://vimeo.com/api/docs/oembed), [oohEmbed](http://oohembed.com/) — ตัวหลังสุดนี้ มันเป็นประมาณ wrapper ของหลาย ๆ บริการอีกทีนึง เช่น Amazon (Ars Technica ใช้บริการจาก oohEmbed ตัวนี้)

Consumers (แสดงลิงก์ oEmbed ได้): [Pownce](http://pownce.com/), [Buckybase](http://buckybase.appspot.com/) , [280 Slides](http://280slides.com/), [Dumble](http://oohembed.com/dumble/)

สำหรับ WordPress มีปลั๊กอินสำหรับ oEmbed แล้วหนึ่งตัว คือ [NFB Video Plugin](http://wordpress.org/extend/plugins/nfb-video-plugin/) ใช้งานได้กับ NFB (National Film Board of Canada) และ Vimeo (เป็นวิดีโอทั้งคู่)

Drupal มีก็มีโมดูล [oEmbed](http://drupal.org/project/oembed)

ถ้าอยากจะเขียนเล่นเอง ก็มีไลบรารีอำนวยความสะดวกสำหรับหลายภาษา:

- [django-oembed](http://code.google.com/p/django-oembed/)
- [ruby-oembed](http://github.com/judofyr/ruby-oembed/tree/master)
- [oembed_links gem](http://github.com/netshade/oembed_links/tree/master)
- [jquery-oembed](http://code.google.com/p/jquery-oembed/)
- [drupal-oembed](http://github.com/voxpelli/drupal-oembed/tree/master)

น่าเอาไปใช้กะโปรเจกต์ของ[โอเพ่นดรีม](http://opendream.co.th/)มั่ง

<span class="small">technorati tags:  
[oEmbed](http://technorati.com/tag/oEmbed),  
[embed](http://technorati.com/tag/embed),  
[social media](http://technorati.com/tag/social+media)  
</span>
