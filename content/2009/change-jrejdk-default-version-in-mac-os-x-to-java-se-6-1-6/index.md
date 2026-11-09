---
title: "change JRE/JDK default version in Mac OS X to Java SE 6 (1.6)"
date: "2009-05-14T10:15:00+07:00"
lastmod: "2011-05-17T14:27:28+07:00"
type: "post"
url: "/2009/change-jrejdk-default-version-in-mac-os-x-to-java-se-6-1-6/"
description: "(Update 2009.05.16: add JAVA_JVM_VERSION setting) To build Nutch 1.0, you need JDK 1.6. Unless you’ll got [javac] class file has wrong version 50.0, should be 49.0 error message. For a system that has more than one version of JDK installed. It is possible to change to a desired version only at the t"
categories: ["computer"]
tag: ["development", "how-to", "java", "jdk", "mac-os-x"]
textlang: "th"
wpid: 2451
---
(Update 2009.05.16: add JAVA_JVM_VERSION setting)

To build [Nutch 1.0](http://lucene.apache.org/nutch/ "Apache Nutch"), you need JDK 1.6. Unless you’ll got *“\[javac\] class file has wrong version 50.0, should be 49.0” error message.*

For a system that has more than one version of JDK installed.  
It is possible to change to a desired version only at the time you need it (look for “j16” script in [this thread](http://www.nabble.com/Can%27t-build-Nutch-td23133734.html "Can't build Nutch")). I found myself more convenient with just changed the default version.

เปลี่ยนรุ่นปริยายของ Java Runtime และ JDK ใน Mac OS X ให้เป็น Java SE 6 (1.6)

1. Install Java SE 6 first. ก่อนอื่น ถ้ายังไม่มี Java SE 6 ในเครื่อง ก็ให้ติดตั้งก่อน.  
    โดย Java SE 6 จะอยู่ใน **[Java for Mac OS X 10.5 Update 2](http://support.apple.com/downloads/Java_for_Mac_OS_X_10_5_Update_2)**, ดาวน์โหลดได้ที่เว็บไซต์ [developer.apple.com/java](http://developer.apple.com/java/).  
    หรือจะปรับรุ่นผ่าน Software Update ก็ได้.

2. Run **Java Preferences** app to set the default version. หลังจากติดตั้งเรียบร้อยแล้ว ก็เรียกโปรแกรม Java Preferences ขึ้นมา <span class="small">(อยู่ใน /Applications/Utilities/Java/ หรือพิมพ์ชื่อลง spotlight เลยก็ได้)</span> เพื่อเลือกว่าจะใช้รุ่นไหนก่อนหลัง. ใช้วิธี ลาก วาง. เสร็จแล้วก็ออกจากโปรแกรม.

3. Point **CurrentJDK** dynamic link to 1.6. ไปตั้ง dynamic link ของไดเรกทอรี CurrentJDK ให้ชี้ไปหารุ่นที่ต้องการด้วย. เช่น ถ้าอยากให้ 1.6 เป็นรุ่นปริยาย ก็ทำแบบนี้ :

        cd /System/Library/Frameworks/JavaVM.framework/Versions
        sudo rm CurrentJDK
        sudo ln -s 1.6 CurrentJDK

4. Set **JAVA_JVM_VERSION** environment variable. ใน *\~/.profile* ตั้งค่าตัวแปรสภาพแวดล้อม JAVA_JVM_VERSION เป็นรุ่นที่ต้องการ โดยเพิ่มบรรทัดนี้เข้าไป :

        export JAVA_JVM_VERSION=1.6

5. \[optional ไม่ทำก็ได้\] Set **JAVA_HOME** environment variable. ใน *\~/.profile* อาจจะตั้งค่าตัวแปรสภาพแวดล้อม JAVA_HOME ไว้ด้วย เพิ่มบรรทัดนี้เข้าไป :

        export JAVA_HOME=/Library/Java/Home

6. \[optional แล้วแต่\] Set **Applet Preferences**. ถ้าอยากแก้อะไรกุ๊ก ๆ กิ๊ก ๆ เกี่ยวกับการรันแอปเพล็ต ก็เข้าไปแก้ได้ที่แฟ้ม *\~/Library/Caches/Java/deployment.properties*. ดูวิธีที่ [Java for Mac OS X 10.5 Update 2: Setting Java Applet preferences](http://support.apple.com/kb/HT3210). เช่น อาจแก้ให้ใช้ font-smoothing/anti-alias กับทุกแอปเพล็ตเลย ก็เพิ่มบรรทัดนี้เข้าไป :

        javaplugin.smoothText=true

เสร็จแว้ว

แถม : สำหรับคนที่ใช้ [MacPorts](http://www.macports.org/), [Porticus](http://porticus.alittledrop.com/) เป็น GUI ที่สะดวกดี. (ประมาณ apt กับ Synaptic Package Manager, แต่ Porticus โง่กว่านิดนึง)

<span class="small">technorati tags: [default](http://technorati.com/tag/default), [Mac OS X](http://technorati.com/tag/Mac+OS+X), [Java](http://technorati.com/tag/Java)  
</span>
