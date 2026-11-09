---
title: "Fixing Java GUI on Hardy Heron"
date: "2008-02-07T16:35:00+07:00"
lastmod: "2008-02-07T16:35:00+07:00"
type: "post"
url: "/2008/fixing-java-gui-on-hardy-heron/"
description: "เพิ่งลง Hardy Heron เมื่อคืนก่อน ปรากฎว่า NetBeans 6.0 รันไม่ได้ ปัญหาอยู่ที่ libmawt ของ JVM มันลิงก์กันไม่ได้กับ libxcb/libX11 ของ Hardy Heron แนว ๆ นี้ ดูจาก backtrace อ่ะนะ เราก็ไม่รู้ว่าจะแก้ยังไงหรอก ไปเจอ workaround ที่ Ubuntu Forums ลองดูแล้ว ใช้ได้ เอามาแบ่งกัน If you have problem with Java"
tag: ["fix", "gwt", "how-to", "java", "linux", "netbeans", "ubuntu"]
textlang: "th"
wpid: 2275
---
เพิ่งลง [Hardy Heron](https://wiki.ubuntu.com/HardyHeron) เมื่อคืนก่อน ปรากฎว่า NetBeans 6.0 รันไม่ได้

ปัญหาอยู่ที่ libmawt ของ JVM มันลิงก์กันไม่ได้กับ libxcb/libX11 ของ Hardy Heron แนว ๆ นี้ ดูจาก backtrace อ่ะนะ เราก็ไม่รู้ว่าจะแก้ยังไงหรอก

ไปเจอ [workaround ที่ Ubuntu Forums](http://ubuntuforums.org/archive/index.php/t-621864.html) ลองดูแล้ว ใช้ได้ เอามาแบ่งกัน

If you have problem with Java GUI apps (for example, NetBeans) on Hardy Heron (Ubuntu 8.04 LTS pre-release), try run this line in your terminal (as root) รันคำสั่งนี้ในเทอร์มินัล:

for 32-bit Ubuntu:  
`$ `**`sudo sed -i 's/XINERAMA/FAKEEXTN/g' /usr/lib/jvm/java-6-sun-1.6.0.04/jre/lib/i386/xawt/libmawt.so`**

for 64-bit Ubuntu:  
`$ `**`sudo sed -i 's/XINERAMA/FAKEEXTN/g' /usr/lib/jvm/java-6-sun-1.6.0.04/jre/lib/amd64/xawt/libmawt.so`**

(**Notes:** the path name may not be exactly as ones shown above, you may need to change to *version number* and/or the *architecture* of your JVM. Look your `/usr/lib/jvm` for the exact name to use. อย่าลืมเปลี่ยนชื่อพาธให้ตรงกับ JVM ที่อยู่ในเครื่องของเรา)

If that doesn’t work for you, try add this line into your `.bash_profile` file ถ้าไม่เวิร์กก็ลองเพิ่มบรรทัดนี้เข้าไปที่ `.bash_profile`:

**`export LIBXCB_ALLOW_SLOPPY_LOCK=true`**

ผมลองวิธีแล้วแล้วมันใช้ได้นะ NetBeans 6.0 + JVM 1.6.0.04 + Hardy Heron Alpha 4 — WORKSFORME

ตอนนี้กำลังลองเล่น [Google Web Toolkit](http://code.google.com/webtoolkit/) มี[สำหรับ NetBeans](https://gwt4nb.dev.java.net/) ด้วยนะ (gwt4nb)

สวัสดีปีใหม่จีน

<span class="small">technorati tags:  
[Java](http://technorati.com/tag/Java),  
[Ubuntu](http://technorati.com/tag/Ubuntu),  
[workaround](http://technorati.com/tag/workaround)  
</span>
