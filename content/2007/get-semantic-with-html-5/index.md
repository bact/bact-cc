---
title: "get semantic with HTML 5"
date: "2007-12-06T00:04:00+07:00"
lastmod: "2011-01-12T09:17:25+07:00"
type: "post"
url: "/2007/get-semantic-with-html-5/"
description: "Lachlan Hunt รีวิว HTML 5 ให้เราดูกันว่าจะมีอะไรเปลี่ยนแปลงไปในข้อกำหนด HTML รุ่นต่อไปบ้าง พร้อมตัวอย่างและภาพประกอบ (โดย Kevin Cornell) เข้าใจง่าย เมื่อเทียบกับ HTML 4 (รุ่นปัจจุบัน) แล้ว HTML 5 นอกจากจะมีแท็กใหม่ ๆ ที่รองรับเทคโนโลยีเว็บที่พัฒนาขึ้น เช่นแท็กเกี่ยวกับไฟล์ภาพเคลื่อนไหวและเสียงแล้ว อ"
categories: ["design"]
tag: ["html", "markup-languages", "semantic-web", "semantics", "web-design"]
textlang: "th"
wpid: 2222
---
Lachlan Hunt **[รีวิว HTML 5](http://www.alistapart.com/articles/previewofhtml5 "A Preview of HTML 5")** ให้เราดูกันว่าจะมีอะไรเปลี่ยนแปลงไปในข้อกำหนด HTML รุ่นต่อไปบ้าง พร้อมตัวอย่างและภาพประกอบ (โดย Kevin Cornell) เข้าใจง่าย

เมื่อเทียบกับ HTML 4 (รุ่นปัจจุบัน) แล้ว [HTML 5](http://www.w3.org/html/wg/html5/) นอกจากจะมีแท็กใหม่ ๆ ที่รองรับเทคโนโลยีเว็บที่พัฒนาขึ้น เช่นแท็กเกี่ยวกับไฟล์ภาพเคลื่อนไหวและเสียงแล้ว อีกจุดสำคัญของ HTML 5 ก็คือ มันจะมี **โครงสร้าง** (structure) และ **ความหมาย** (semantic) ที่ชัดเจนขึ้นด้วย

เมนู ที่ปรากฎอยู่บนจอ ก็จะถูกระบุว่าเป็นเมนู ไม่ใช่แค่ตารางที่วางอยู่ด้านขวาของจอ  
ชื่อหนังสือ ที่ปรากฎอยู่บนจอ ก็จะถูกระบุว่าเป็นชื่อหนังสือ ไม่ใช่แค่ข้อความอันหนึ่งที่อยู่หลังคำว่า “ชื่อหนังสือ:”

ปัจจุบันนี้ นักออกแบบ/พัฒนาเว็บส่วนหนึ่ง พยายามที่จะเขียนโค้ดหน้าเว็บที่แยกเอา **หน้าตา** (presentation) ออกมาจาก **เนื้อหา** (content) ไม่ให้ปะปนกัน โดยส่วนของหน้าตาจะนำไปใส่ใน [Cascading Style Sheets](http://en.wikipedia.org/wiki/Cascading_Style_Sheets) (CSS) ส่วนเนื้อหาก็จะอยู่ในเซตย่อยของ HTML ที่ไม่ใช้แท็กที่เกี่ยวข้องกับหน้าตาเช่น center, b, i (โดยถ้าอยากเน้นข้อความไหน ก็ให้ใช้ strong และ em แทน)

นอกจากการแยกหน้าตากับเนื้อหาออกจากกันแล้ว ก็ยังมีความพยายามที่จะเขียนโค้ด HTML ที่มีโครงสร้างเป็นระบบขึ้น โดยอาศัยแท็กจำพวก h1, div และ li เป็นต้น และพยายามใส่ความหมายเข้าไปในโค้ด โดยอาศัยแอตทริบิวต์จำพวก class, rel และ id โดยกลุ่มนี้จะเรียกรวม ๆ ว่า [Semantic HTML](http://en.wikipedia.org/wiki/Semantic_HTML) โดยมีแนวคิดหลักอย่างน้อยสองแบบคือ [POSH](http://en.wikipedia.org/wiki/Plain_Old_Semantic_HTML "Plain Old Semantic HTML") และ [Microformats](http://microformats.org/) ซึ่งทั้งสองอย่างนี้สามารถใช้ร่วมกันได้ โดยอย่างแรกจะเป็นคำแนะนำกว้าง ๆ สำหรับหน้าเว็บทั้งหมด ส่วนอย่างหลังจะเป็นข้อกำหนดที่ชัดเจนสำหรับข้อมูลแต่ละประเภทไปเลย — กล่าวโดยรวมคือ ทั้งหมดนี้เป็นการประยุกต์ใช้ HTML รุ่นปัจจุบันที่มีอยู่ ให้บันทึกความหมายบางอย่างได้

HTML 5 จะช่วยให้รูปแบบการเขียนโค้ดลักษณะ POSH เป็นไปด้วยความสะดวกมากขึ้น เขียนได้ตรง ๆ ขึ้น (ลองดูตัวอย่างจาก [A Preview of HTML 5](http://www.alistapart.com/articles/previewofhtml5))

ร่างข้อกำหนดของ HTML 5 เริ่มพัฒนามาตั้งแต่ พ.ศ. 2547 และปัจจุบันยังอยู่ในระหว่างการพัฒนาโดยคณะทำงานสองกลุ่มคือ [W3C HTML WG](http://www.w3.org/html/) และ [WHATWG](http://www.whatwg.org/) ร่วมมือกัน — โดยคาดว่าจะสามารถประกาศเป็น W3C Recommendation ได้ประมาณปี พ.ศ. 2565 (อีกประมาณ 15 ปี! – ดู [FAQ](http://wiki.whatwg.org/wiki/FAQ#When_will_HTML_5_be_finished.3F))  
อย่างไรก็ตาม ความสามารถของ HTML 5 จะค่อย ๆ ถูกนำไปใช้ในเว็บเบราว์เซอร์และเว็บไซต์ต่าง ๆ ทีละน้อย ๆ ตัวอย่างเช่นเว็บเบราว์เซอร์จำนวนหนึ่งในปัจจุบันก็รองรับแท็ก canvas หรือความสามารถด้าน autodiscovery แล้ว

ถ้าสนใจเรื่อง [Semantic HTML](http://en.wikipedia.org/wiki/Category:Semantic_HTML) (ซึ่งคุณสามารถนำแนวคิดนี้ไปใช้ได้ตั้งแต่ตอนนี้เลย ไม่ต้องมาตรฐานใหม่ ไม่ต้องรอเบราว์เซอร์ใหม่) ลองไปดูที่เว็บไซต์ [semantichtml.org](http://semantichtml.org/) หรือค้นเว็บด้วยว่า “[semantic html](http://www.google.com/search?q=semantic+html)” ดู จะพบเว็บไซต์มากมาย ที่แนะนำและพูดคุยเกี่ยวกับเรื่องนี้

ผลพลอยได้อย่างหนึ่ง ที่น่าจะได้จากการเขียนหน้าเว็บตามแนว Semantic HTML ก็คือ [โปรแกรมอ่านหน้าจอ](http://en.wikipedia.org/wiki/Screen_reader) (screen reader) [สำหรับผู้พิการทางสายตา](http://bact.blogspot.com/2007/10/web-accessibility-thailand.html) น่าจะทำงานได้ดียิ่งขึ้น เพราะมีข้อมูลมาช่วยตัดสินใจมากขึ้นในการอ่าน (คิดง่าย ๆ ว่า Semantic HTML เน้นว่าเนื้อหา**หมายความว่าอะไร** ไม่ใช่ว่าเนื้อหาจะถูก**วาดยังไง** การ‘อ่าน’โดยตรงจากเนื้อหาจริง ๆ ย่อมง่ายและถูกต้องกว่าการอ่าน+ตีความจากภาพวาดอยู่แล้ว)

\[ ลิงก์ [A List Apart](http://www.alistapart.com/articles/previewofhtml5 "A Preview of HTML 5") \| ผ่าน [OSNews.com](http://osnews.com/story.php/19006/A-Preview-of-HTML-5 "A Preview of HTML 5") \]

<span class="small">technorati tags:  
[Semantic HTML](http://technorati.com/tag/semantic+html),  
[HTML 5](http://technorati.com/tag/html5)  
</span>
