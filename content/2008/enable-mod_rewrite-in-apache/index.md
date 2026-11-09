---
title: "enable mod_rewrite in Apache"
date: "2008-04-08T02:02:00+07:00"
lastmod: "2008-04-08T02:02:00+07:00"
type: "post"
url: "/2008/enable-mod_rewrite-in-apache/"
description: "ทดสอบ CakePHP ในเครื่อง ต้องหาทางเปิด mod_rewrite ไปเจอที่ Ubuntu Forums อีกตามเคย ขอแปลมาไว้ที่นี่: เปิดใช้ mod_rewrite ใน Apache2 (บน Ubuntu) เปิดใช้โมดูล mod_rewrite (เอาไว้ทำ url อ่านง่าย ๆ) ใน Apache ใน 3+1 ขั้นตอน: ขั้นหนึ่ง: ระบุให้โหลด rewrite โดยการทำซิมบอลิกลิงก์ไฟล์ rewrite.load ใส่ไว้ใน "
tag: ["how-to", "linux", "ubuntu"]
textlang: "th"
wpid: 2318
---
ทดสอบ [CakePHP](http://cakephp.org/ "Web MVC with PHP") ในเครื่อง ต้องหาทางเปิด mod_rewrite ไปเจอที่ [Ubuntu Forums](http://ubuntuforums.org/showthread.php?t=7304 "mod_rewrite") อีกตามเคย ขอแปลมาไว้ที่นี่:

### เปิดใช้ mod_rewrite ใน Apache2 (บน Ubuntu)

เปิดใช้โมดูล *[mod_rewrite](http://httpd.apache.org/docs/2.0/mod/mod_rewrite.html)* (เอาไว้ทำ url อ่านง่าย ๆ) ใน Apache ใน 3+1 ขั้นตอน:

**ขั้นหนึ่ง:** ระบุให้โหลด rewrite โดยการทำซิมบอลิกลิงก์ไฟล์ rewrite.load ใส่ไว้ใน /etc/apache2/mods-enabled/

    sudo ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/

**เพิ่มเติม 2008.04.08:** อ.มะนาวบอกว่า ใช้ a2enmod ก็ได้ ง่ายกว่ากันเยอะ .. จริง ๆ ด้วย! ดังนั้น ทำแบบนี้ก็ได้

    sudo a2enmod rewrite

(a2enmod ว่าตามตัวคือ apache2 *enable* module; ถ้าอยากเอาตัวไหนออก ก็ใช้ a2dismod – apache2 *disable* module)

**ขั้นสอง:** แก้ไฟล์คอนฟิกของ apache

    sudo vi /etc/apache2/sites-enabled/000-default

เปลี่ยนค่าของ **AllowOverride** ไปเป็น **all** สำหรับ document root directory ที่ต้องการ (default จะเป็น /var/www/)

ตัวอย่างเช่น:


<pre>
&lt;Directory /var/www/&gt;
    Options Indexes FollowSymLinks MultiViews
    AllowOverride <font color="Red"><b>all</b></font>
    Order allow,deny
    allow from all
&lt;/Directory&gt;
</pre>


**ขั้นสาม:** รีสตาร์ท apache

    sudo /etc/init.d/apache2 restart

อันนี้ก็จะเสร็จทางฝั่ง apache ละ ต่อไปก็เป็นทางฝั่งเว็บแอพพลิเคชัน/สคริปต์

**ขั้นสุดท้าย:** แก้/สร้างไฟล์ .htaccess ในไดเรกทอรีที่ต้องการใช้ rewrite โดยระบุค่า RewriteEngine เป็น On

    RewriteEngine On

เท่านี้ก็จะใช้ mod_rewrite ได้แล้ว

ส่วนวิธีเขียนกฎ rewrite นั้น ลองศึกษาได้จาก [URL Rewriting Guide](http://www.widexl.com/tutorials/mod_rewrite.html), [cheat sheet](http://www.ilovejackdaniels.com/cheat-sheets/mod_rewrite-cheat-sheet/)

\[credits to *[jalanbuntu](http://ubuntuforums.org/member.php?u=38012)* of Ubuntu Forums\]

<span class="small">technorati tags:  
[mod_rewrite](http://technorati.com/tag/mod_rewrite),  
[rewrite](http://technorati.com/tag/rewrite),  
[Apache](http://technorati.com/tag/Apache)  
</span>
