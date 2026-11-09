---
title: "นโยบาย Cloud First ของรัฐบาลสหราชอาณาจักร"
date: "2017-08-19T14:16:16+07:00"
lastmod: "2017-08-26T22:38:03+07:00"
type: "post"
url: "/2017/gov-uk-cloud-first/"
description: "รีวิวเร็วๆ นโยบาย “Cloud First” (คลาวด์มาก่อน) ของรัฐบาลสหราชาอาณาจักรพยายามทำอะไร เป็นเพียงเรื่องเทคโนโลยี จัดซื้อจัดจ้าง หรือมากกว่านั้น?"
categories: ["informatics", "politics"]
tag: ["cloud", "e-government", "gov-uk", "information-architecture", "united-kingdom"]
image: "/f/2017/08/cloud-first.jpg"
textlang: "th"
wpid: 3607
---
รีวิว **[นโยบาย *“Cloud First”* ของรัฐบาลสหราชอาณาจักร](https://www.gov.uk/guidance/government-cloud-first-policy)** แบบเร็วๆ มีประเด็นน่าสนใจดังนี้

## เน้นความคุ้มเงิน

- เน้นความคุ้มเงิน
- cloud ในที่นี้ คือ public cloud
- ให้ใช้ public cloud เป็นตัวเลือกแรก หน่วยงานจะใช้ตัวเลือกอื่นก็ได้ แต่ต้องแสดงให้เห็นได้ว่ามันคุ้มเงินกว่า (“value for money” ใช้นิยามตามกระทรวงการคลัง HM Treasury)

## ให้การจัดซื้อจัดจ้างตามมาตรฐานสะดวกขึ้น

- การแบ่งชั้นความอ่อนไหวของข้อมูลที่ชัดเจนและรู้ว่าแอปจะต้องเจอกับข้อมูลแบบไหนบ้าง จะทำให้การเลือกใช้บริการภายนอกทำได้ง่าย เพื่อช่วยกระบวนการนี้ รัฐบาลสหราชอาณาจักรได้จัดกลุ่มชั้นความลับของข้อมูลใหม่ให้ง่ายขึ้น โดยลดจำนวนจาก 6 ระดับ เหลือ 3 ระดับ คือ [Official, Secret และ Top Secret](https://digitalmarketplace.blog.gov.uk/2014/06/09/the-g-cloud-security-approach/)
- เพื่อให้การจัดซื้อจัดจ้างทำได้สะดวกขึ้น รัฐบาลได้จัดทำแนวทางข้อกำหนด G-Cloud ขึ้น (มีปรับปรุงเรื่อยๆ ล่าสุดเวอร์ชัน 9) [มีเทมเพลตสัญญาให้ด้วย](https://www.gov.uk/guidance/g-cloud-templates-and-legal-documents)
- G-Cloud เป็นระบบ self-certify ผู้ให้บริการจะต้องทดสอบระบบของตัวเอง และแสดงหลักฐานให้เห็นว่าสามารถทำตามข้อกำหนดเรื่องอะไรได้ที่ระดับไหนบ้าง เพื่อให้ผู้เลือกซื้อบริการตัดสินใจ
- เกณฑ์อันหนึ่งที่สำคัญคือเรื่องการรักษาความมั่นคงปลอดภัย G-Cloud ที่ดูแลข้อมูลชั้นความลับ Official จะใช้[หลักการ 14 ข้อ (14 Cloud Security Principles)](https://www.ncsc.gov.uk/guidance/implementing-cloud-security-principles) ซึ่งปัจจุบัน National Cyber Security Centre ดูแล

## เปิดโอกาสผู้ให้บริการหลากหลายทั้งรายเล็กรายใหญ่

- มี Digital Marketplace ให้หน่วยงานเลือกหาบริการจาก[ผู้ให้บริการที่ทำตามข้อกำหนดของ G-Cloud](https://www.digitalmarketplace.service.gov.uk/g-cloud) (มีบริการ 3 แบบ: cloud hosting, cloud software, cloud support)
- เพื่อลดเวลาและความยุ่งยากในการเริ่มต้นและจัดการแอปบน cloud ด้วยตัวเอง หน่วยงานของรัฐสามารถใช้บริการ [GOV.UK Platform as a Service (PaaS)](https://www.cloud.service.gov.uk/) ซึ่งให้บริการโดย Government Digital Service (GDS) \[บริการนี้มีฐานะเหมือนเป็น cloud hosting อันหนึ่งใน Digital Marketplace\]
- บริการ GOV.UK PaaS ใช้ซอฟต์แวร์โอเพนซอร์ส [Cloud Foundry](https://www.cloudfoundry.org/) ทำงานบน Amazon Web Service โดยใช้ศูนย์ข้อมูลที่ตั้งในไอร์แลนด์ (และใช้กฎหมายคุ้มครองข้อมูลส่วนบุคคลของสหภาพยุโรป)
- GOV.UK PaaS ได้รับการรับรองให้ประมวลผลข้อมูลส่วนบุคคลและข้อมูลชั้นความลับ Official (สำหรับข้อมูลชั้นความลับ Secret หรือ Top Secret จะใช้บริการนี้ไม่ได้)

## อื่นๆ

- ไม่ต้องทำมาตรฐานเอง ถ้ามีมาตรฐานที่ดีและแพร่หลายในอุตสาหกรรมอยู่แล้ว อย่างนิยามคำว่า cloud ก็ไม่ต้องนิยามเอง ใช้ตาม NIST ของสหรัฐอเมริกาไปเลย
- สุดท้ายเป็นเรื่องของความคุ้มเงินและความโปร่งใสรับผิดได้ (ของการจัดซื้อจัดจ้าง) มากกว่าเรื่องเทคโนโลยีเพียงอย่างเดียว
- หลังจากใช้นโยบายนี้มา 4 ปี รัฐบาลสหราชอาณาจักรกำลังพิจารณาปรับเปลี่ยนวิสัยทัศน์จาก Cloud First ไปเป็น [Cloud Native](https://governmenttechnology.blog.gov.uk/2017/02/03/clarifying-our-cloud-first-commitment/)

## ประเทศไทย

ประเทศไทยเองก็มีบริการคลาวด์ภาครัฐ ชื่อ [G-Cloud](https://www.ega.or.th/th/profile/881/) ให้บริการโดยสำนักงานรัฐบาลอิเล็กทรอนิกส์ (สรอ.) หรือ EGA – แต่ไม่แน่ใจเรื่องนโยบายในระดับรัฐบาลว่ามีการกำหนดอะไรไหม ว่าหน่วยงานรัฐต้องใช้หรือไม่อย่างไร

(ภาพประกอบจาก [GOV.UK Government technology blog](https://governmenttechnology.blog.gov.uk/2017/02/03/clarifying-our-cloud-first-commitment/))
