---
title: "How to install Tahoma font, Ubuntu Studio theme and preload in Ubuntu (+ OpenSolaris 2008.05 debut)"
date: "2008-05-07T00:22:00+07:00"
lastmod: "2011-05-05T11:59:39+07:00"
type: "post"
url: "/2008/tahoma-theme-preload-ubuntu-opensolaris/"
description: "from Ubuntu Forums – HOWTO: Tahoma Font in Breezy by Casey ถึงจะใช้โอเพนซอร์ส บางทีเราก็จำเป็นต้อง/ถูกบังคับให้ใช้ฟอนต์ที่ไม่ใช่ซอฟต์แวร์เสรี เช่น รายงานความคืบหน้าการวิจัยของเนคเทค ที่แม้จะระบุให้ใช้ OpenDocument Text (มาตรฐานเปิด-เยี่ยม) แต่ในขณะเดียวกันก็ระบุว่าให้ใช้ฟอนต์ Tahoma (เฉพาะระบบของไมโ"
categories: ["computer"]
tag: ["fonts", "free-softwares", "how-to", "linux", "open-source", "opensolaris", "ubuntu"]
textlang: "th"
wpid: 2343
---
from Ubuntu Forums – [HOWTO: Tahoma Font in Breezy](http://ubuntuforums.org/archive/index.php/t-82318.html) by Casey

ถึงจะใช้โอเพนซอร์ส บางทีเราก็จำเป็นต้อง/ถูกบังคับให้ใช้ฟอนต์ที่ไม่ใช่ซอฟต์แวร์เสรี  
เช่น รายงานความคืบหน้าการวิจัยของเนคเทค ที่แม้จะระบุให้ใช้ OpenDocument Text (มาตรฐานเปิด-เยี่ยม) แต่ในขณะเดียวกันก็ระบุว่าให้ใช้ฟอนต์ Tahoma (เฉพาะระบบของไมโครซอฟท์-เฮ้ย)

วิธีติดตั้งฟอนต์ Tahoma บน Ubuntu (กนู/ลีนุกซ์ดิสโทรอื่น ๆ ก็ปรับ ๆ เอานะครับ)

1.  ลงแพคเกจ msttcorefonts ก่อน :  
    `sudo apt-get install msttcorefonts`
2.  ดาวน์โหลดฟอนต์ Tahoma จาก <http://download.microsoft.com/download/ie6sp1/finrel/6_sp1/W98NT42KMeXP/EN-US/IELPKTH.CAB> :  
    `wget http://download.microsoft.com/download/ie6sp1/finrel/6_sp1/W98NT42KMeXP/EN-US/IELPKTH.CAB`
3.  แตกแฟ้ม IELPKTH.CAB ออกมา, ในที่นี้เราจะใส่ไว้โฟลเดอร์ชั่วคราว tahomafont :  
    `cabextract -d tahomafont IELPKTH.CAB`
4.  คัดลอกแฟ้มฟอนต์ทั้งหมดไปที่โฟลเดอร์ฟอนต์ msttcorefonts ของ Ubuntu :  
    `sudo cp tahomafont/*.ttf /usr/share/fonts/truetype/msttcorefonts/`
5.  ลบโฟลเดอร์ชั่วคราว tahomafont เมื่อสักครู่นั้นทิ้ง :  
    `rm -rf tahomafont`

เสร็จ

เกร็ด: น่าสนใจว่าแพคเกจ IELPKTH.CAB นี้ มันคือ Thai Language Pack ของ Internet Explorer ซึ่งนอกจากฟอนต์แล้ว ยังมีผังแป้นพิมพ์ไทย และรหัสอักขระไทย (CP 874) ด้วย

------------------------------------------------------------------------

แถม : [ลงธีมของ Ubuntu Studio บน Ubuntu ปกติ](http://ubuntufun.wordpress.com/2007/05/21/%E0%B9%83%E0%B8%8A%E0%B9%89-ubuntu-%E0%B9%81%E0%B8%95%E0%B9%88%E0%B8%AD%E0%B8%A2%E0%B8%B2%E0%B8%81%E0%B9%84%E0%B8%94%E0%B9%89%E0%B8%98%E0%B8%B5%E0%B8%A1-ubuntu-studio/) (เห็นใน twitter)

ถ้าจะเอาทั้งชุดเลย (รวมหน้าจอล็อกอิน, โปรแกรมเสริมบน desktop) :  
`sudo apt-get install ubuntustudio-look`

ถ้าจะเอาแค่ธีม ไอคอน พื้นหลัง :  
`sudo apt-get install ubuntustudio-theme ubuntustudio-icon-theme ubuntustudio-wallpapers`

ลงแล้วสวยดี แต่กับบางโปรแกรมใช้แล้วจะมองไม่ค่อยเห็น ปวดตาหน่อย ๆ  
เช่น Firefox 3 นี่ จะมีปัญหาเรื่องสีกับตรงช่องที่อยู่ address bar คือสีที่ไฟร์ฟ็อกซ์ใช้สำหรับลิงก์ มันเป็นสีเขียว  
แล้วสีของพื้นหลังของ widget ใน Ubuntu Studio นี่มันเป็นสีเทาดำ มันเลยอ่านยากมาก ไม่ดีเท่าไหร่ หรืออย่างเวลาทำไฮไลท์ข้อความในช่องที่อยู่ มันก็ไม่เปลี่ยนสีพื้นหลัง เปลี่ยนแต่สีอักษร ดูยากไปนิดนึง โปรแกรมอื่นไม่เป็นนะ เป็นแต่กับไฟร์ฟ็อกซ์นี่แหละ เข้าว่าเป็นเพราะไม่ได้เป็น GTK+

------------------------------------------------------------------------

แถม 2 (ใจดี) : **[OpenSolaris 2008.05](http://opensolaris.com/)** ออกแล้ว ([ข่าวที่ OSNews](http://osnews.com/story/19715/Sun_Debuts_OpenSolaris_2008.05)) เป็นดิสโทรอีกดิสโทรหนึ่งของ OpenSolaris (เอ่อ ชื่อดันเหมือนกันอีก คือนอกจาก OpenSolaris ที่เป็นดิสโทรแล้วเนี่ย ยังมีคนเอาซอร์สโค้ดจาก OpenSolaris.org ไปทำดิสโทรอื่น ๆ อีก เช่น [Nexenta](http://www.nexenta.org/)) มี Live CD ด้วย

ดิสโทร OpenSolaris นี้ ใช้ตัวจัดการแพกเกจตัวใหม่ที่ชื่อว่า [Image Packaging System](http://opensolaris.org/os/project/pkg/) (IPS) ซึ่งเจ้า IPS นี่ ใช้ประโยชน์จากระบบแฟ้ม [ZFS](http://en.wikipedia.org/wiki/ZFS) เช่นการทำ rollback กรณี โอ๊ะ ติดตั้งแพกเกจใหม่เข้าไปแล้วเจ๊ง จะย้อนกลับ ก็ใช้ความสามารถของ ZFS ทำ (ดิสโทรอย่าง Nexenta นั้นใช้ apt ซึ่งผู้ใช้ลีนุกซ์ค่าย Debian, Ubuntu จะคุ้นเคยกว่า)

[รีวิวค่อนข้างดี](http://blogs.zdnet.com/BTL/?p=8703) แต่ก็ยังมีจุดต้องปรับปรุงเช่นเรื่องการแชร์แฟ้มกับ Samba ที่ยุ่งยากเกินไป ในรีวิวนั้นมีภาพจับหน้าจอให้ดูหลายรูป ดูในรูปคล้าย Linux Desktop ทั่วไปมาก เพราะใช้ GNOME 2.22 เหมือน ๆ กัน (ในภาพนั้นใช้[ธีม Nimbus](http://www.gnome-look.org/content/show.php/Nimbus+(Ubuntu+and+Debian)?content=54755) แบบเดียวกับที่มี[ใน Java 6 Update 10](http://java.sun.com/developer/technicalArticles/javase/java6u10/index.html#nimbus))

ถ้าไม่อยากดาวน์โหลด หรืออยากได้แผ่นมาเก็บ [สั่งได้](https://www2.sun.de/dct/forms/reg_us_2307_228_0.jsp)นะครับ ฟรี ค่าส่งก็ไม่คิด ผมสั่งไปแล้ว อยากรู้ว่าจะสวยเหมือนโลโก้รึเปล่า 😀

------------------------------------------------------------------------

แถม 3 (ชิงร้อยชิงล้าน) : ในลีนุกซ์ เราสามารถเร่งความเร็วการโหลดโปรแกรมที่เราใช้บ่อย ๆ ได้โดยใช้โปรแกรม **[preload](http://pwet.fr/man/linux/administration_systeme/preload "man page")** โปรแกรมนี้มันจะคอยดูพฤติกรรมการใช้งานโปรแกรมของเรา และก็ไปโหลดบางส่วนของโปรแกรมที่เราใช้บ่อย ๆ ขึ้นมารอไว้ในหน่วยความจำล่วงหน้า (เรียกอีกอย่างก็คือ โกง น่ะ) วิธีพวกนี้เราเรียกว่า pre-fetching ใน Windows XP ก็มี

วิธีติดตั้ง preload บน Ubuntu :  
`sudo apt-get install preload`  
แค่นั้นเลย แล้วมันก็จะทำงานอัตโนมัติอยู่หลังฉาก

ถ้าอยากดูว่ามันทำอะไรอยู่ ก็ :  
`sudo tail -f /var/log/preload.log`  
หรือถ้าอยากดูละเอียด ๆ เป็นรายแฟ้มเลย ก็ :  
`sudo less /var/lib/preload/preload.state`

ที่มา : Linux Journal ฉบับล่าสุด (ล่าสุดที่เมืองไทยใน Bookazine นะ ไม่รู้ล่าสุดแค่ไหน), [LifeHacker](http://lifehacker.com/software/featured-linux-download/load-programs-faster-with-preload-269625.php), และ [Techthrob.com](http://www.techthrob.com/tech/preload.php) (อันหลังสุดนี่ละเอียดมาก มีวิธีการตั้งค่าโดยละเอียดด้วย)

<span class="small">technorati tags: [Ubuntu](http://technorati.com/tag/Ubuntu), [Tahoma](http://technorati.com/tag/Tahoma), [howto](http://technorati.com/tag/howto), [font](http://technorati.com/tag/font), [theme](http://technorati.com/tag/theme), [OpenSolaris](http://technorati.com/tag/OpenSolaris)</span>
