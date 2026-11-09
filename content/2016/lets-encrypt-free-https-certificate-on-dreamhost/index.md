---
title: "ติดตั้ง HTTPS พร้อมใบรับรองฟรีจาก Let’s Encrypt บน shared host​ (DreamHost)"
date: "2016-01-06T18:49:34+07:00"
lastmod: "2016-01-07T04:51:46+07:00"
type: "post"
url: "/2016/lets-encrypt-free-https-certificate-on-dreamhost/"
description: "ติดตั้ง Secure Certificate ฟรีจาก Let’s Encrypt บน Dreamhost shared host"
categories: ["internet"]
tag: ["dreamhost", "encryption", "https", "information-security", "lets-encrypt"]
image: "/f/2016/01/letsencrypt-dreamhost.png"
textlang: "th"
wpid: 3398
---
[Let’s Encrypt](https://letsencrypt.org/) เป็นบริการออกใบรับรองการเข้ารหัสเว็บ ที่ให้บริการฟรี ที่ผ่านบริการนี้ต้องเสียเงิน ประมาณ 500 บาทไปจนถึงเกินหมื่นก็มี ซึ่งในทางเทคนิคแล้ว ใบรับรองพวกนี้เหมือนกันหมดไม่ว่าจะฟรีหรือจ่ายเท่าไรก็ตาม

Let’s Encrypt ให้บริการฟรีได้ ส่วนหนึ่งเพราะมันทำให้กระบวนการต่างๆ ทำได้ด้วยตัวเองได้โดยผู้ใช้ (มีสคริปต์มาให้รันเองได้ และในอนาคตจะเป็นระบบอัตโนมัติมากขึ้น) ค่าใช้จ่ายก็เลยถูกลง และอีกส่วนหนึ่งเพราะมี[องค์กรหลายแห่งสนับสนุนเงินทุน](https://letsencrypt.org/sponsors/) รวมๆ คือคนเหล่านี้อยากเห็นอินเทอร์เน็ตที่มันปลอดภัยขึ้น (ซึ่งพอคนมั่นใจกับการใช้งานอินเทอร์เน็ตมากขึ้น เดี๋ยวธุรกิจอะไรอื่นๆ ที่ทำตังค์ได้ มันจะตามมาเอง)

อย่างไรก็ตาม ณ ตอนนี้ สคริปต์ของ Let’s Encrypt นี่มันจะใช้บนเครื่องที่เรามี permission เข้าถึง root ของเซิร์ฟเวอร์ได้เท่านั้น คนใช้ shared host นี่หมดสิทธิ์

แต่ช้าก่อน — ถ้าใครใช้ DreamHost หรือเว็บโฮสต์ที่อนุญาตให้เราติดตั้งใบรับรองได้เองทางหน้าเว็บ ก็ไม่ต้องเสียใจ มีวิธีอยู่ คือเรารันสคริปต์นั่นในเครื่องโน๊ตบุ๊กหรือเดสก์ท็อปของเราเองก่อน (บน Linux หรือ OS X) แล้วจากนั้นก็ค่อยเอาไฟล์ต่างๆ ไปใส่ไว้ใน Dreamhost อีกที ผ่านคอนโทรลพาเนลบนหน้าเว็บปกติ

*ขั้นตอนวิธีทำเอามาจาก [Using Let’s Encrypt With Dreamhost](http://www.velvetcache.org/2015/12/08/using-lets-encrypt-with-dreamhost) โดย jmhobbs*

1.  เริ่มจากไปบอก DreamHost ก่อนว่าให้เพิ่ม secure hosting ไปที่ชื่อโดเมนของเรา  
    ล็อกอินเข้า [DreamHost panel](https://panel.dreamhost.com/) ที่ด้านซ้ายเลือก “Domains” –\> “Secure Hosting” –\> “Add Secure Hosting” (ใครใช้ shared host ยี่ห้ออื่น ลองหาทางดูครับ อาจจะมีคล้ายๆ กัน)  
    ![Add secure hosting in Dreamhost](/f/2016/01/dreamhost-add-secure-hosting.png)ตรงนี้เราก็เลือกชื่อโดเมนที่เราต้องการให้มีการเข้ารหัส  
    ![Choose domain name to add secure hosting](/f/2016/01/dreamhost-add-secure-hosting-2.png)  
    จบขั้นนี้ปุ๊บ สิ่งที่เราได้ก็คือ ชื่อโดเมนที่เราเลือก จะมีการเข้ารหัสด้วย HTTPS แล้ว แต่ใบรับรองที่ใช้จะเป็น self-signed (เซ็นรับรองด้วยตัวเราเอง) ซึ่งเวลาใครมาเข้าเว็บไซต์เรา เบราว์เซอร์มันก็จะเตือนว่า ไม่น่าเชื่อถือนะ สิ่งที่เราจะทำต่อไปก็คือ ไปขอใบรับรอง ที่ Let’s Encrypt (บุคคลที่สาม) เป็นคนเซ็นให้เรา เพื่อให้เบราว์เซอร์มันพอใจ (และคนอุ่นใจ)

2.  ก่อนจะใช้ Let’s Encrypt [ก็ต้องติดตั้ง](https://letsencrypt.readthedocs.org/en/latest/using.html)มันลงเครื่องโน๊ตบุ๊กหรือเดสก์ท็อปของเรา  
    โดยไปดึงสคริปต์มาด้วย git (ถ้ายังไม่มี [ก็ติดตั้ง git ก่อน](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))[  
    ](https://letsencrypt.readthedocs.org/en/latest/using.html)

        git clone https://github.com/letsencrypt/letsencrypt

3.  จากนั้นก็ ขอใบรับรอง ด้วยสคริปต์ของ Let’s Encrypt

        cd letsencrypt
        ./letsencrypt-auto certonly --manual --debug

    คำอธิบายอ็อปชัน

    - certonly ระบุเพื่อบอกว่า ให้สร้างใบรับรอง แต่ไม่ต้องติดตั้ง (เดี๋ยวเราติดตั้งเอง – ผ่านคอนโทรลพาเนลของ Dreamhost)
    - –manual บอกว่า เราจะทำ domain validation ยืนยันว่าเรามีสิทธิ์ในชื่อโดเมนนั้นเอง (ผ่านการเอาข้อความอันนึงไปวางไว้ที่เซิร์ฟเวอร์นั้น)
    - –debug ใส่อ็อปชันนี่ ถ้ารันบน OS X, ถ้าใช้ Linux ก็ไม่ต้องใส่

    ตรงนี้สคริปต์อาจจะติดตั้งโปรแกรมที่จำเป็นลงในเครื่อง เช่น libxml2, python2.7 (ถ้าบน OS X ก็ผ่าน homebrew) ก็ดูๆ ครับ ว่ามันสำเร็จไหม ถ้าไม่มีปัญหาอะไร สคริปต์ก็จะพาเราไปสู่ขั้นที่ 4

4.  สคริปต์จะถาม **อีเมลของเรา** (ใช้กรณีกู้กุญแจที่หาย)  
    ![Let's Encrypt asking for e-mail](/f/2016/01/letsencrypt-email.png)  
    และ **ชื่อโดเมนที่เราต้องการใบรับรอง**![Let's Encrypt asking for domain name](/f/2016/01/letsencrypt-domain-name.png)  
    ตรงขั้นนี้มันจะเตือนเราว่าทางระบบจะทำการบันทึก **ที่อยู่ไอพี (IP address)** ที่เราใช้เพื่อขอใบรับรองนะ **เราโอเคไหมที่จะให้คนอื่นรู้ที่อยู่ไอพีที่เรากำลังใช้อยู่ขณะนี้** (ของเครื่องที่เรากำลังใช้อยู่ ไม่ใช่เว็บเซิร์ฟเวอร์) ถ้าเราโอเค ก็ตอบตกลงไป  
    ![Let's Encrypt warns about IP logging](/f/2016/01/letsencrypt-ip-address.png)

5.  ถึงตรงนี้มันจะให้เรายืนยันว่า เรามีสิทธิ์ในชื่อโดเมนที่เราขอไปจริงๆ ด้วยการให้เราสร้างไฟล์ที่มีชื่อตามที่มันกำหนดในไดเรกทอรีที่กำหนด (ตรงสีเขียว) โดยในไฟล์นั้นต้องมีข้อความที่กำหนดด้วย (สีแดง) — อย่าเพิ่งกด ENTER จนกว่าเราจะสร้างไฟล์ที่ว่าเสร็จ  
    ![Let's Encrypt asking for domain validation](/f/2016/01/letsencrypt-domain-validation.png)วิธีสร้างก็ตามนี้ คือ (ในอีกหน้าจอนึง-ล็อกอินเข้าไปที่เซิร์ฟเวอร์ ไม่ได้ทำที่เครื่องเราเองนะ) เข้าไปที่ไดเรกทอรีของเว็บไซต์เราก่อน (อันนี้เป็นการแบ่งไดเรกทอรีในแบบของ Dreamhost ใครใช้โฮสต์อื่นก็ปรับไปนะครับ) จากนั้นก็สร้างไดเรกทอรีที่กำหนด แล้วก็สร้างไฟล์และเอาข้อความที่มันบอกไปใส่ เพื่อบอกว่า นี่ไง เราสร้างได้ เรามีสิทธิ์จริงๆ นะ

        cd [domain]
        mkdir -p .well-known/acme-challenge/
        echo -n "[RedContent]" > .well-known/acme-challenge/[GreenFilename]

    พอจัดการเรื่องที่เซิร์ฟเวอร์เสร็จ ก็กลับมาที่หน้าจอที่เครื่องเรา แล้วกด ENTER ได้เลย

    ถ้าระบบมันเจอไฟล์ที่เราสร้างไว้อย่างถูกต้องที่เซิร์ฟเวอร์ ระบบมันจะสร้างใบรับรองให้เรา เก็บไว้ที่ /etc/letsencrypt/live/\[domain\]  
    ข้างในไดเรกทอรีดังกล่าวจะมีไฟล์อยู่ 4 ไฟล์: cert.pem, chain.pem, fullchain.pem, privkey.pem ซึ่งเราจะเอาไปใช้ในขั้นต่อไป  
    **\*\*ไฟล์เหล่านี้อย่าให้คนอื่นรู้\*\* ไม่งั้นเขาจะปลอมตัวเป็นเว็บไซต์ของเราได้**

6.  ถึงตรงนี้เราจะเริ่มก๊อปปี้ใบรับรองต่างๆ ไปใส่ในคอนโทรลพาเนลของ Dreamhost  
    เริ่มด้วยการคลิก Edit ที่ท้ายชื่อโดเมน ในหน้า “Secure Hosting”  
    ![Add certificate in Dreamhost](/f/2016/01/dreamhost-add-certificate.png)จะเจอหน้า “Certificate Settings”  
    ให้เราเลือก “Manual configuration”  
    มันจะขึ้นช่องให้เราใส่ใบรับรองต่างๆ อยู่ 4 ช่อง  
    ![Add certificate in Dreamhost](/f/2016/01/dreamhost-add-certificate-details.png)4 ช่องนี้ ให้ใส่ดังนี้

    - Certificate Signing Request: ลบทิ้งให้ว่าง
    - Certificate: เอาข้อความในไฟล์ cert.pem มาใส่
    - Private Key: แปลง privkey.pem เป็นฟอร์แมต RSA ด้วย openssl แล้วนำข้อความมาใส่
    - Intermediate Certificate: เอาข้อความในไฟล์ chain.pem มาใส่

    วิธีดูข้อความในไฟล์

        sudo less /etc/letsencrypt/live/[domain]/cert.pem

    วิธีแปลง privkey.pem เป็นฟอร์แมต RSA แล้วเอาไปเก็บไว้ที่ privkey.key (จากนั้นก็เอาข้อความใน privkey.key ไปใช้)

        sudo openssl rsa -in /etc/letsencrypt/live/bact.cc/privkey.pem -out privkey.key

    ใส่ครบทุกช่องแล้ว ก็คลิก “Save changes now”

7.  เท่านี้ก็น่าจะเสร็จแล้ว — แต่ถ้าอยากให้ทุกครั้งที่เรียก **http**://abc.xyz แล้วให้มัน redirect ไปที่ **https**:///abc.xyz อัตโนมัติ ก็ทำขั้นนี้เพิ่มหน่อย — ใส่โค้ดนี้ลงในไฟล์ [.htaccess](http://wiki.dreamhost.com/Htaccess_tricks)

        RewriteEngine On
        RewriteCond %{HTTPS} !=on
        RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

8.  ลองเข้าเว็บไซต์ของเราดู ว่าเข้ารหัสและมีใบรับรองสวยงามอย่างที่หวังไหม หลังการแก้ไขต่างๆ อาจจะต้องรอสักพัก ไม่น่าจะเกิน 15 นาที เพื่อให้ระบบมันรีเฟรช

9.  ทดสอบความเรียบร้อยอีกที ด้วย [การทดสอบจาก SSL Labs](https://www.ssllabs.com/ssltest/) เพื่อดูว่าเรายังขาดตกตรงไหนอีก

10. อย่าลืมว่า ใบรับรองของ Let’s Encrypt จะหมดอายุทุกๆ 3 เดือน ดังนั้นพอใกล้ๆ 3 เดือนก็อย่าลืมทำซ้ำตั้งแต่ขั้นที่ 3 ใหม่นะครับ

*ส่วนใครใจไม่ร้อน รอได้ ก็รออีกหน่อย ทาง Dreamhost ประกาศแล้วว่า [จะหาทางให้สามารถใช้ Let’s Encrypt บน Dreamhost ได้แบบง่ายๆ](https://www.dreamhost.com/blog/2015/12/03/lets-encrypt-and-dreamhost/) แค่คลิกๆ ก็เสร็จ*
