---
title: "install Python alternatives"
date: "2008-04-14T00:32:00+07:00"
lastmod: "2008-04-14T00:32:00+07:00"
type: "post"
url: "/2008/install-python-alternatives/"
description: "สวัสดีปีใหม่ — 12-14 เม.ย. ผมและเพื่อน ๆ อยู่ที่ Thai Firefox L10n sprint po2moz ใช้กับ Python 2.5 ไม่ได้ ต้องเป็นรุ่นต่ำกว่านั้น ลง Python (และโปรแกรมอื่น ๆ) หลาย ๆ รุ่นในเครื่อง และวิธีตั้งค่ารุ่นปริยาย ลงที่รุ่นที่อยากได้ apt-get install python2.4 บอกเครื่อง ว่าเรามีหลายรุ่นนะ update-alternatives"
tag: ["how-to", "linux", "localization", "python", "ubuntu"]
textlang: "th"
wpid: 2324
---
**สวัสดีปีใหม่** — 12-14 เม.ย. ผมและเพื่อน ๆ อยู่ที่ **[Thai Firefox L10n sprint](http://poakpong.com/1130)**

[po2moz](http://translate.sourceforge.net/wiki/toolkit/moz2po) ใช้กับ Python 2.5 ไม่ได้ ต้องเป็นรุ่นต่ำกว่านั้น

ลง Python (และโปรแกรมอื่น ๆ) หลาย ๆ รุ่นในเครื่อง และวิธีตั้งค่ารุ่นปริยาย

ลงที่รุ่นที่อยากได้

    apt-get install python2.4

บอกเครื่อง ว่าเรามีหลายรุ่นนะ

    update-alternatives --install /usr/lib/python python /usr/lib/python2.3 9
    update-alternatives --install /usr/lib/python python /usr/lib/python2.4 5
    update-alternatives --install /usr/lib/python python /usr/lib/python2.5 1

(–install ลิงก์คำสั่งปริยาย ชื่อคำสั่ง ลิงก์ไปหารุ่นที่ระบุ ลำดับความสำคัญ)

จากนั้นก็เลือกรุ่นที่อยากใช้

    update-alternatives --config python

จะเมนูขึ้น เลือก

------------------------------------------------------------------------

เอามาจาก [Ubuntu Forums](http://ubuntuforums.org/archive/index.php/t-315362.html) อีกแล้ว

------------------------------------------------------------------------

**\*\*\*** ในเวลาเดียวกันนี้ ที่ IRC ห้อง \#tlwg <irc://irc.linux.in.th#tlwg> ก็มี **OSS glossary sprint** ด้วย — จัดการเก็บกวาด [คลังศัพท์กลาง Glossary for Open Source Software](http://www.opentle.org/ossglossary/) ไปแจมกันได้

รายละเอียด ข้อมูลเกี่ยวกับการแปล/localization ดูได้ที่ [l10n.opentle.org](http://l10n.opentle.org/)

<span class="small">technorati tags:  
[Ubuntu](http://technorati.com/tag/Ubuntu),  
[Linux](http://technorati.com/tag/Linux),  
[Python](http://technorati.com/tag/Python)  
</span>
