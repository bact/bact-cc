---
title: "GATE experiment at KIND Lab, SIIT"
date: "2007-07-16T18:05:00+07:00"
lastmod: "2011-05-17T14:37:24+07:00"
type: "post"
url: "/2007/gate-experiment-at-kind-lab-siit/"
description: "งานทดลองสุดสัปดาห์ที่ผ่านมา เมื่อวานทดลองเขียน wrapper ครอบ Stanford Log-linear Part-Of-Speech Tagger ให้กลายเป็นปลั๊กอินสำหรับใช้กับ GATE (หลังจากตั้งท่ามานาน) pipeline ในรูป มี 3 Processing Resources คือ tokensier, splitter และ tagger tokensier คือ net.siit.gate.DictionaryBasedTokeniser เป็นตัวตัด"
categories: ["coling", "computer"]
tag: ["gate", "java", "kind", "natural-language-processing", "part-of-speech", "programming", "siit", "thai"]
textlang: "th"
wpid: 2154
---
งานทดลองสุดสัปดาห์ที่ผ่านมา

[![POS-tagged document in GATE](https://farm2.static.flickr.com/1195/818767327_da99c8c5c1.jpg)](http://www.flickr.com/photos/arthit/818767327/ "Thai POS tagging pipeline in GATE")

เมื่อวานทดลองเขียน wrapper ครอบ [Stanford Log-linear Part-Of-Speech Tagger](http://nlp.stanford.edu/software/tagger.shtml) ให้กลายเป็นปลั๊กอินสำหรับใช้กับ [GATE](http://www.gate.ac.uk/) (หลังจากตั้งท่ามานาน)

pipeline ในรูป มี 3 Processing Resources คือ tokensier, splitter และ tagger

**tokensier** คือ net.siit.gate.DictionaryBasedTokeniser เป็นตัวตัดคำธรรมดา ๆ ใช้พจนานุกรม<sup>1</sup> และออกแบบให้ตัดได้คำที่ยาวที่สุด (longest-matching) ทำงานกับ AnnotationSet ของ GATE โดยตรง — จะสร้าง AnnotationSet ชื่อ “Token” ขึ้นมา

**splitter** คือ ANNIE Sentence Splitter เป็นตัวแบ่งประโยค โดยใช้กฎ (ภาษา JAPE เป็นลักษณะ regular expression over annotation) ตัวนี้มากับ GATE อยู่แล้ว และไม่ได้ออกแบบมาสำหรับภาษาไทย — เราเอามาใช้ไถ ๆ ไป เพื่อให้สร้าง AnnotationSet ชื่อ “Sentence” เท่านั้น (เป็นการ “สมมติว่ามี” จะได้ทดลองขั้นต่อไปได้)

**tagger** คือ net.siit.gate.StanfordPOSTagger เป็นตัวกำกับชนิดของคำ (Part-of-Speech) เป็น wrapper ไว้เรียกใช้/แปลงข้อมูลจาก edu.stanford.nlp.tagger.maxent.MaxentTagger ซึ่งเป็นตัวกำกับชนิดของคำแบบเรียนรู้จากชุดตัวอย่าง<sup>2</sup> ตัว MaxentTagger จะรับข้อมูลเข้า/ส่งข้อมูลออกเป็น List\<Sentence\> ก็ต้องแปลงให้กลายเป็น AnnotationSet (เอาคำจากชุด “Token” โดยใช้ชุด “Sentence” ระบุขอบเขตประโยค<sup>3</sup>) เพื่อให้เข้ากับ GATE — ในขั้นตอนสร้าง List\<Sentence\> ตัว wrapper นี้ จะทึกทักเอาเองว่า Annotation ทั้งหมดใน AnnotationSet นั้น ไม่ทับซ้อนกัน (overlapping), ซึ่งจริง ๆ แล้ว ใน GATE นั้นอนุญาตให้ Annotation มันทับซ้อนกันได้ เช่น ถ้า Token ดันมีซ้อนกันเป็น \[ab{cd\]efg} แบบนี้ ตอนที่ตัว tagger (wrapper) แปลงเป็น Sentence จะได้ Sentence ที่บรรจุ Word = { “abcd”, “cdefg” }

ทั้งหมดเป็น Java (ในส่วนที่พัฒนาเอง ใช้ NetBeans)

ทั้งหมดนี้ ไม่มีอะไรเป็น “ของใหม่” เป็นเพียงการทดลองหยิบชิ้นส่วนหรืออัลกอริธึมที่คนอื่นทำไว้แล้ว มาลองประกอบเข้าด้วยกันในกรอบ (framework) ของ GATE เท่านั้น (ส่วนที่มีเสริมเข้าไป ก็เพื่อให้ประกอบสนิทกันเท่านั้น)

แต่คาดหวังว่า การมีกรอบที่ชัดเจนแบบนี้ จะช่วยลดงานที่ไม่จำเป็นในการทดลอง/วิจัยในอนาคตไปได้บ้าง เพื่อจะได้มีเวลาไปเน้นเรื่อง “ใหม่ ๆ” จริง ๆ

<sup>1</sup> สามารถระบุพจนานุกรมตอนสร้าง instance ใหม่ได้ ปัจจุบันคำส่วนหนึ่งมาจากคลังข้อมูลเอกสารการแพทย์ที่ [KIND Lab](http://kind.siit.tu.ac.th/), SIIT ทำร่วมกับ เภสัช ศิลปากร อีกส่วนหนึ่งมาจากตัวตัดคำ KU Wordcut ของเกษตร (สุธี สุดประเสริฐ), ใช้ Trie เป็นโครงสร้างข้อมูลขณะตัดคำ (org.speedblue.util.Trie)

<sup>2</sup> ชุดตัวอย่างนำมาจากคลังข้อความ [ORCHID](http://www.links.nectec.or.th/orchid/) โดยเนคเทค (ทดสอบแปลงข้อมูลโดยใช้สคริปต์ [Groovy](http://groovy.codehaus.org/) บน JVM)

<sup>3</sup> จริง ๆ แล้ว เราสามารถใส่คำทั้งหมดเข้าไปประมวลผลทีเดียวได้ (คือมี 1 ประโยคใน List\<Sentence\> และทุกคำในเอกสารบรรจุอยู่ในประโยคนั้น) แต่การทำแบบนั้น คิดว่าน่าจะเปลืองหน่วยความจำ อีกเรื่องคือ ยังไม่ได้ศึกษาโดยละเอียดว่า ขอบเขตของประโยค มีส่วนต่อการคำนวณหาค่าความน่าจะเป็นในการกำกับชนิดของคำของคลาส MaxentTagger หรือไม่ (ตั้งสมมติฐานไว้ว่า น่าจะมี จึงพยายามแบ่งประโยค)

<span class="small">technorati tags: [GATE](http://technorati.com/tag/GATE), [natural language processing](http://technorati.com/tag/natural_language_processing), [Thai](http://technorati.com/tag/Thai), [tagger](http://technorati.com/tag/tagger)  
</span>
