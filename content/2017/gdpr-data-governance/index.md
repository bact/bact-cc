---
title: "หลักการ/กลไกการคุ้มครองข้อมูลใหม่ใน GDPR ของสหภาพยุโรป #infosec17"
date: "2017-06-08T01:03:04+07:00"
lastmod: "2017-06-08T21:15:52+07:00"
type: "post"
url: "/2017/gdpr-data-governance/"
description: "หลักการ Security และ Accountability ใน GDPR เป็นความพยายามให้เกิดสภาพแวดล้อมที่ลดความเสี่ยงในการรั่วไหลของข้อมูล ไม่ได้มาเน้นเฉพาะการลงโทษหลังข้อมูลรั่วแล้ว นอกจากนี้ ในส่วนของ Security ก็ยังมีการกำหนดมาตรฐานการแจ้งเตือนในกรณีที่พบข้อมูลรั่วไหล"
categories: ["politics", "freedom"]
tag: ["data-protection", "general-data-protection-regulation", "information-commissioners-office", "information-security", "privacy"]
image: "/f/2017/06/readyforgdpr-1.jpg"
textlang: "th"
wpid: 3567
---
วันนี้เป็นวันที่ 2 ที่มางาน Infosecurity Europe ที่ลอนดอน ได้ฟังหลักๆ 2 เวที เป็น Keynote ทั้งคู่ อันแรกตอนเช้า ฟัง Bruce Schneier พูดหัวข้อ [Artificial Intelligence & Machine Learning: Cybersecurity Risk vs Opportunity?](http://www.infosecurityeurope.com/en/Sessions/41960/Artificial-Intelligence-Machine-Learning-Cybersecurity-Risk-vs-Opportunity) ส่วนตอนบ่ายฟัง [EU GDPR Special Focus – Extended Session](http://www.infosecurityeurope.com/en/Sessions/41963/EU-GDPR-Special-Focus--Extended-Session) โพสต์นี้เล่าของตอนบ่ายก่อน ส่วนของตอนเช้ากับของงานวันแรกยังไม่ได้เขียนถึง เดี๋ยวทยอยลงนะ

เรื่อง **[General Data Protection Regulation (GDPR)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)** ซึ่งเป็นกฎหมายคุ้มครองข้อมูลตัวใหม่ของสหภาพยุโรปที่ประกาศเมื่อปีที่แล้วและจะมีผลบังคับใช้ในวันที่ 25 พฤษภาคม 2018 นี่มาแรงมากๆ เดินไปไหนในงานก็เห็นคำนี้ มีในเกือบทุกทอล์ก เพราะเหลือเวลาอีกไม่ถึง 1 ปีแล้ว ที่ทุกบริษัท ทุกหน่วยงาน จะต้องปฏิบัติตามกฎหมายดังกล่าว ซึ่งมีผลบังคับใช้เหมือนกันหมดทั่วสหภาพยุโรป (หัวข้อตอนบ่ายที่ไปฟังมาอันนี้ฮิตมาก คนต่อแถวยาวเหยียด และเวลาก็ได้ยืดมากกว่าหัวข้ออื่น เป็น extended session)

![Ready for GDPR (?)](/f/2017/06/readyforgdpr-1.jpg)

**Peter Brown** ซึ่งเป็นเจ้าหน้าที่เทคโนโลยีอาวุโสของ [Information Commissioner’s Office](https://ico.org.uk/) (ICO – สำนักงานคณะกรรมการข้อมูลข่าวสารของสหราชอาณาจักร) เป็นคนพูดเปิด เล่าถึงหลักการทั่วไปของ GDPR กับความพร้อมของ ICO ในฐานะองค์กรกำกับและคุ้มครองข้อมูลส่วนบุคคลของสหราชอาณาจักร ว่าได้เตรียมข้อแนะนำและหลักปฏิบัติอะไรต่างๆ ให้กับภาคธุรกิจปรับตัวและเปลี่ยนผ่านอย่างไรบ้าง

Peter บอกว่าหลักการคุ้มครองข้อมูลของ GDPR นั้น ไม่ต่างจากที่กฎหมายคุ้มครองข้อมูล หรือ Data Protection Act (DPA) ที่สหราชอาณาจักรมีอยู่ในปัจจุบัน เพียงแต่เพิ่มหลักการขึ้นมา 2 เรื่อง คือ [**Security**](https://iapp.org/news/a/top-10-operational-impacts-of-the-gdpr-part-1-data-security-and-breach-notification/) และ [**Accountability & Governance**](https://ico.org.uk/for-organisations/data-protection-reform/overview-of-the-gdpr/accountability-and-governance/)

อธิบายต่อ (ผมพูดเอง) ก็คือ เดิม DPA นั้นพูดถึงเฉพาะตัวข้อมูลและการประมวลผลข้อมูล แต่ GDPR ยังพูดถึงระบบที่ใช้ประมวลผลข้อมูล (เน้นเชิงเทคนิค – technical measures) และความรับผิดและการบริหารจัดการของผู้ที่เกี่ยวข้อง (เน้นเชิงกระบวนการ – organizational measures)

จริงๆ ข้อคำนึงเหล่านี้ มีอยู่แล้วเงียบๆ ใน DPA แต่ GDPR ระบุให้มันแยกออกมาอย่างชัดเจน

พูดอีกแบบ DPA หรือหลักการคุ้มครองข้อมูลส่วนบุคคลโดยทั่วไปที่ผ่านมา จะเน้นการไม่เก็บ ไม่บันทึก ไม่ส่งต่อ ไม่ประมวลผล ข้อมูลที่ไม่จำเป็น ไม่เกี่ยวข้อง ไม่ได้รับความยินยอม และกำหนดบทลงหากมีการทำเช่นว่า

แต่ GDPR คิดละเอียดกว่านั้น โดยเฉพาะในบริบทที่ข้อมูลจำนวนมากอยู่ในระบบเครือข่ายและสารสนเทศ คือแม้จะเก็บและใช้อย่างถูกต้องทุกอย่าง แต่ถ้าระบบที่ยุ่งเกี่ยวกับข้อมูลนั้นมีการจัดการที่ไม่ได้มาตรฐาน ไม่มีมาตรการป้องกันที่ควรมี ก็มีความผิดได้

สิ่ง “ใหม่” ที่ถูกพูดถึงในหลักการ Accountability & Governance ของ GPDR ก็คือหลัก **data protection by design**, **data protection by default**, และ **data protection impact assessment** **(DPIA)** — “ใหม่” ในที่นี้ หมายถึงมันไม่เคยถูกบังคับในกฎหมายมาก่อน

(เรื่อง data protection by design นี่ มีหลายบริษัทที่มาออกงานพูดถึง ตั้งแต่การออกแบบ user experience ที่สนับสนุน security, การทำระบบให้ลด cognitive load เพื่อให้คนทำงานอยู่ในภาวะมีสติ, การออกแบบให้ AI มาช่วยคนตัดสินใจได้ดีขึ้น)

ทั้งหลักการ Security และ Accountability ที่มีใน GDPR เรียกว่าเป็นความพยายามให้เกิดสภาพแวดล้อมที่ลดความเสี่ยงในการรั่วไหลของข้อมูล ไม่ได้มาเน้นเฉพาะการลงโทษหลังข้อมูลรั่วแล้ว นอกจากนี้ ในส่วนของ Security ก็ยังมีการกำหนดมาตรฐานการแจ้งเตือนในกรณีที่พบข้อมูลรั่วไหล ([ทาง Article 29 Working Party จะออกแนวปฏิบัติมาภายในปีนี้](https://ico.org.uk/for-organisations/data-protection-reform/overview-of-the-gdpr/breach-notification/))

พูดอีกแบบคือจะหวังว่า “เราจะโชคดี” “มันไม่เกิดกับเราหรอก” ไม่ได้ — ต่อให้ข้อมูลยังไม่รั่ว แต่ถ้าพบว่าไม่มีมาตรการที่เพียงพอก็มีความผิด

หน้าที่ของผู้ประมวลผล-ผู้ควบคุมข้อมูลคือ จะต้องสามารถแสดงหลักฐาน (evidence) ให้ได้ว่า ตัวเองได้ทำสิ่งที่ควรทำทั้งหมดแล้ว

ลองคิดถึงกฎหมายเกี่ยวกับความปลอดภัยของอาคาร ที่ต่อให้ไฟยังไม่ไหม้ แต่ถ้าพบว่าไม่มีทางหนีไฟ ไม่มีอุปกรณ์จับควัน-แจ้งเตือน-ดับเพลิง ที่ได้มาตรฐานอย่างเพียงพอ ก็มีความผิดอยู่ดี

ใน GDPR หากมีกรณีข้อมูลรั่วไหล หากผู้ประมวลผล/ผู้ควบคุมข้อมูลสามารถแสดงได้ว่า ได้ทำตามมาตรฐานที่กำหนด ยังมีโอกาสได้รับลดหย่อนโทษลงด้วย

สำหรับผู้ประกอบการในประเทศไทย ถ้าทำมาค้าขายกับคู่ค้าในสหภาพยุโรป ต้องประมวลผลข้อมูลของพลเมืองของสหภาพยุโรป ก็ต้องศึกษากฎหมาย GDPR นี้ไว้ด้วย เพราะกฎหมายครอบคลุมถึงข้อมูลของพลเมืองของเขา ไม่ว่าข้อมูลนั้นจะถูกส่งไปประมวลผลหรือจัดเก็บที่ใดก็ตามครับ

> ICO’s Peter Brown looks at impact of GDPR on cyber security during his [\#cyberresilience](https://twitter.com/hashtag/cyberresilience?src=hash) speech. More here: <https://t.co/egGINAdZvX> [pic.twitter.com/zuXRHre9Tj](https://t.co/zuXRHre9Tj)
>
> — ICO (@ICOnews) [February 7, 2017](https://twitter.com/ICOnews/status/828984505306378240)

<script async="" src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
