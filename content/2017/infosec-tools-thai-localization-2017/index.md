---
title: "Consumer information security tools – Thai localization 2017 summary"
date: "2017-12-31T18:17:41+07:00"
lastmod: "2018-01-10T06:11:43+07:00"
type: "post"
url: "/2017/infosec-tools-thai-localization-2017/"
description: "Signal แปลเสร็จแล้ว 100% ทั้งบน iOS และ Android / KeePassXC คืบหน้าไปมาก / หลายโครงการเปิดส่วนภาษาไทยให้แปลแล้ว / ทาง Localization Lab สามารถช่วยประสานกับบางโครงการที่ยังไม่อยู่บน Transifex อย่าง Gpg4win ให้ไปแปลบน Transifex ได้ เพื่อความสะดวก"
categories: ["computer", "freedom"]
tag: ["information-security", "localization", "thai", "tor"]
image: "/f/2017/12/signal-android-thai-100-translated.png"
textlang: "th"
wpid: 3626
---
การแปลโปรแกรมรักษาความปลอดภัยในการใช้คอมใช้เน็ต สำหรับผู้ใช้ทั่วไป สรุปสิ้นปี 2017

Thanks [COCONET: Southeast Asia Digital Rights Camp](https://www.engagemedia.org/Projects/camp-coconet) and [Localization Lab](https://www.localizationlab.org/) for a localization sprint this year for Thai, Bahasa Indonesia, Burmese, and Khmer. Events like that help volunteer translators get connected to people who close to developers, and it helps the translation submission goes more smooth.

## รอผู้พัฒนาดำเนินการต่อ

แปล 100% รีวิว 100% รอให้าทางผู้พัฒนาทดสอบการใช้งานในแอป

- <strong>Signal</strong> แอปแชตแบบปลอดภัย
  - <https://www.transifex.com/moxie/signal-android/> (Android)
  - <https://www.transifex.com/open-whisper-systems/signal-ios/> (iOS)
  - คาดว่าประมาณสัปดาห์ที่ 3 ของเดือนมกราคม น่าจะมีแอปที่มีภาษาไทยแล้วให้โหลดทาง app store ได้

[![A chart showing that Signal on Android 100% translated to Thai](/f/2017/12/signal-android-thai-100-translated.png)](/f/2017/12/signal-android-thai-100-translated.png)

## ยังแปลไม่เสร็จ

- <strong>KeePassXC</strong> โปรแกรมจัดการรหัสผ่าน \[71%\]  
  <https://www.transifex.com/keepassxc/keepassxc/>  
   

- <strong>Tor</strong>, <strong>Tor Browser</strong> เบราว์เซอร์ช่วยเข้าถึงเน็ตอย่างเป็นส่วนตัวมากขึ้น \[58%\]  
  <https://www.transifex.com/otf/torproject/>

  - มีโปรแกรมย่อยๆ อีก เช่น TorBirdy ส่วนเสริมให้ Thunderbird ส่งเมลผ่าน Tor
  - ดูรายละเอียดเพิ่มที่วิกิ <https://wiki.localizationlab.org/index.php/Tor>

   

- <strong>Lantern</strong> แอปทำนอง VPN \[49%\]  
  <https://www.transifex.com/otf/lantern/>  
   

- <strong>ooniprobe</strong> แอปช่วยทดสอบความเร็วและการเข้าถึงเน็ต \[41%\]  
  <https://www.transifex.com/otf/ooniprobe/>  
   

- <strong>Duplicati</strong> โปรแกรมช่วยสำรองข้อมูล \[5%\]  
  <https://www.transifex.com/duplicati/duplicati/>  
   

- <strong>VeraCrypt</strong> โปรแกรมช่วยให้เก็บข้อมูลในเครื่องอย่างปลอดภัย \[0%\]  
  <https://github.com/veracrypt/VeraCrypt/tree/master/Translations>  
  <em>— Update 2018-01-04: เปิดให้แปลภาษาไทยได้แล้ว [ผ่าน Transifex (private)](https://www.transifex.com/otf/veracrypt-1/)</em>  
   

## รอให้ทางโครงการเพิ่มภาษาไทย

- <strong>Gpg4win</strong> ชุดโปรแกรมสำหรับเข้ารหัสลับแบบ PGP (Windows)  
  <https://www.gpg4win.de/localize-gpg4win.html>

  - มีโปรแกรมย่อยอีก 4 ตัวคือ GnuPG (โปรแกรมเข้ารหัสลับ), Kleopatra (โปรแกรมจัดการกุญแจ), GpgOL (ปลั๊กอินสำหรับ Outlook – เข้ารหัสลับอีเมล), GpgEx (ปลั๊กอินสำหรับ Windows Explorer – เข้ารหัสลับแฟ้ม)
  - อาจจะมีทางให้ [Localization Lab](https://www.localizationlab.org/) ช่วยจัดการให้แปลผ่าน Transifex ได้

   

- <strong>GPG Suite</strong> ชุดโปรแกรมสำหรับเข้ารหัสลับแบบ PGP (macOS) <em>— Update 2018-01-05: เปิดให้แปลภาษาไทยได้แล้ว</em>  
  <https://www.transifex.com/gpgtools/public/>

  - มีโปรแกรมย่อยอีก 4 ตัวคือ libmacgpg (โปรแกรมเข้ารหัสลับ), GPG Keychain (โปรแกรมจัดการกุญแจ), GPGMail (ปลั๊กอินสำหรับ Mail.app), GPGPerferences (ส่วนการตั้งค่า)

   

- <strong>Orbot, Orfox</strong> แอปช่วยเข้าถึงเน็ตอย่างเป็นส่วนตัวมากขึ้น (Android)  
  <https://www.transifex.com/otf/orbot/> (เทียบได้กับ Tor) <em>— Update 2018-01-10: เปิดให้แปลภาษาไทยได้แล้ว</em>  
  <https://www.transifex.com/otf/orfox/> (เทียบได้กับ Tor Browser)

<strong><em>สำหรับโปรแกรมที่อยู่บน Transifex แล้ว ใครสนใจช่วยแปล สามารถสมัครสมาชิก Transfex (ฟรี) แล้วไปที่หน้าโครงการ กด Join Team ได้เลยครับ</em></strong><em> — ถ้าโปรแกรมเหล่านี้เป็นภาษาไทย ก็มีโอกาสที่คนไทยจะสามารถใช้โปรแกรมช่วยความปลอดภัยเหล่านี้ได้มากขึ้นครับ</em><strong><em>  
</em></strong>

สวัสดีปีใหม่ 2018 ทุกท่าน ขอให้เป็นปีที่ปลอดภัย คิด ทำ พูด ได้อย่างมั่นใจ 🙂
