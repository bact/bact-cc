---
title: "on various things, digital this and information that"
date: "2009-06-02T02:32:00+07:00"
lastmod: "2011-01-12T07:54:59+07:00"
type: "post"
url: "/2009/on-various-things-digital-this-and-information-that/"
description: "[ปรับปรุง 12:46: เพิ่ม Greenstone และลิงก์ libraryhub.in.th ขอบคุณ @markpeak] [ปรับปรุง 2009.07.17: แก้ไขข้อมูลเกี่ยวกับระบบบรรณารักษ์ที่คลาดเคลื่อน ขอบคุณ อ.บุญเลิศ] สี่ห้าวันที่ผ่านมา บุกตะลุยเก็บข้อมูลเกี่ยวกับห้องสมุดและระบบสารสนเทศดิจิทัลให้ :=3 ไม่ได้เน้นไปที่พวก Library 2.0 มากนัก อยากรู้เรื่"
categories: ["informatics"]
tag: ["cultural-informatics", "free-softwares", "information-and-library-sciences", "libraries", "metadata", "open-access", "open-source", "open-standards", "opendream"]
textlang: "th"
wpid: 2454
---
\[ปรับปรุง 12:46: เพิ่ม Greenstone และลิงก์ libraryhub.in.th ขอบคุณ @markpeak\]

\[ปรับปรุง 2009.07.17: แก้ไขข้อมูลเกี่ยวกับระบบบรรณารักษ์ที่คลาดเคลื่อน ขอบคุณ อ.บุญเลิศ\]

สี่ห้าวันที่ผ่านมา บุกตะลุยเก็บข้อมูลเกี่ยวกับห้องสมุดและระบบสารสนเทศดิจิทัลให้ [:=3](http://opendream.co.th/ "โอเพ่นดรีม :=3")

ไม่ได้เน้นไปที่พวก [Library 2.0](http://en.wikipedia.org/wiki/Library_2.0) มากนัก อยากรู้เรื่องระบบข้างใต้เพิ่มเติมมากกว่า การประยุกต์ข้างบนคิดว่าพอเข้าใจไอเดียบ้างแล้วส่วนหนึ่ง (ลองดู [นำเสนอ](http://library.tcdc.or.th/announce/announce.php?id=7)โดย [@iteau](http://twitter.com/iteau) และ [@projectlib](http://twitter.com/projectlib) เกี่ยวกับเรื่องนี้และ [TCDC Resource Center](http://library.tcdc.or.th/) – @iteau เขียน[ควันหลง](http://iteau.wordpress.com/2007/06/15/library2_0attcdc/)นิดนึง) เดี๋ยวลองเอามาประกอบกัน

เว็บ [DegreeTutor](http://www.degreetutor.com/library/managing-expenses/open-source-library) แนะนำโอเพ่นซอร์ส ILS (integrated library system) 3 ตัว ได้แก่ Koha, Evergreen ILS, และ VuFind ทุกตัวทำงานกับ OPAC (open public access catalog) ได้หมด :

- [Koha](http://koha.org/) เป็น ILS ที่ติดตั้งง่าย มีหลายที่ในเมืองไทยใช้แล้ว เช่น [ห้องสมุดดิจิทัลของ STKS](http://www.libraryhub.in.th/2009/05/02/libcamp1-stks-digital-library/) (โชว์ในงาน LibCamp), [ห้องสมุดวุฒิสภา](http://senatelibrary.wordpress.com/tag/koha/), ม.อุบลก็กำลังเตรียมใช้, [บล็อก STKS สวทช.](http://www.stks.or.th/blog/?tag=koha) เขียนถึงเยอะเหมือนกัน
- [Evergreen ILS](http://evergreen-ils.org/) เขาว่าเป็นระบบ fault-tolerance เลยทีเดียว มั่นใจได้
- [VuFind](http://vufind.org/) เป็น “Library Resource Portal ที่มาครอบ ILS เพื่อขยายความสามารถของ OPAC ให้เป็น OPAC 2.0” \[[อ.บุญเลิศ](http://bact.blogspot.com/2009/06/on-various-things-digital-this-and.html#comment-3505506387373687012)\] ยังอยู่ในช่วงพัฒนา (RC) อาจจะยังไม่เรียบร้อยนัก แต่มีความสามารถเยอะ ใช้ระบบค้นหาของ Apache Solr หายห่วง โครงการห้องสมุดดิจิทัลคิดดี [กำลังเล็ง](http://kids-d.org/node/128)ว่าอาจจะเอามาเป็นหน้ากากครอบฐานข้อมูลย่อย ๆ ต่าง เพื่อให้ผู้ใช้ใช้งานง่ายขึ้น

เสริมจากความเห็นโดย อ.บุญเลิศ คือ ทั้ง Koha และ Evergreen นั้น เป็น ILS ที่มีความสามารถเทียบเท่ากับ ILS ที่ขายกัน ระดับ [VTLS](http://www.vtls.com/), [InnoPAC/Millenium ILS](http://www.iii.com/), และ [Horizon/SirsiDynix](http://www.sirsidynix.com/)

ส่วน ILS รุ่นเล็กลงไป คือ [OpenBiblio](http://obiblio.sourceforge.net/) และ [PHPMyLibrary](http://sourceforge.net/projects/phpmylibrary/)

งานหลักอันนึงของห้องสมุดก็คือ การทำ catalog หนังสือ หรือป้อนข้อมูลหนังสือเข้าไปในระบบ เพื่อให้สืบค้นและยืมคืนได้ ซึ่งก็ใช้แรงงานไม่น้อย ถ้ามีเครื่องทุ่นแรงก็คงจะดี นึกไอเดียประมาณ CDDB หรือ [freeDB.org](http://www.freedb.org/) ที่เราเสียบซีดีเพลงเข้าเครื่อง แล้วโปรแกรมเล่นเพลงก็จะไปค้นฐานข้อมูลที่คนอื่นเขาใส่ข้อมูลชื่อเพลงชื่อนักร้องไว้เราแล้ว เราไม่ต้องใส่เองหมด เว้นว่าหาไม่เจอ เราก็ใส่เข้าไปหน่อย แล้วคนอื่นจะได้ใช้ด้วย เอาแบบนั้น สำหรับเมตาดาต้าหนังสือ ก็จะได้ [‡biblios.net](https://biblios.net/) โครงการเพิ่งเริ่มได้ไม่นาน แต่ดูดีทีเดียว มาจาก [LibLime](http://liblime.com/) ผู้ร่วมพัฒนา Koha

นอกจากสารสนเทศที่เป็นหนังสือเล่มแล้ว ก็ยังมีเอกสารที่ไม่ใช่หนังสือ ซึงตอนนี้ก็เป็นดิจิทัลได้จำนวนมากแล้ว  
วิธีหนึ่งที่นิยมและมีประสิทธิภาพก็คือ *self-archiving* คือเก็บของใครของมัน ใครผลิตคนนั้นก็เก็บ  
เป็น institutional repository แต่แชร์ข้อมูลค้นหากันได้ ระบบจัดเก็บสารสนเทศองค์กรที่เป็นโอเพ่นซอร์สและใช้โปรโตคอล OAI-PMH สำหรับแลกเปลี่ยนเมตาดาต้าเพื่อการค้นหา มีสองตัว :

- [DSpace](http://www.dspace.org/) เมืองไทยมีใช้หลายที่ เช่น [คลังปัญญาจุฬาฯ](http://cuir.car.chula.ac.th/) โดย สถาบันวิทยบริการ จุฬาลงกรณ์มหาวิทยาลัย, [ห้องสมุดดิจิทัลคิดดี](http://dspace.kids-d.org/) โดย เอไอที, สำนักงานคณะกรรมการการศึกษาขั้นพื้นฐาน และ มศว., [NSTDA Knowledge Repository (สวทช.)](http://library.stks.or.th:8080/dspace/) โดย ศูนย์บริการความรู้ทางวิทยาศาสตร์และเทคโนโลยี
- [EPrints](http://www.eprints.org/software/) เมืองไทยเท่าที่ทราบ ไม่มีใครใช้ ผมดูแล้วมันน่าจะลงง่ายกว่าแฮะ (จากประสบการณ์ส่วนตัว ระหว่าง [UIMA](http://incubator.apache.org/uima/) กับ [GATE](http://gate.ac.uk/) พบว่า GATE ปวดหัวน้อยกว่า ผมเลยคิดว่า จะลอง EPrints ก่อนละกัน เหตุผลแถ ๆ :p)

[@markpeak](http://twitter.com/markpeak) แนะนำอีกตัว (thx!) คือ [Greenstone](http://www.greenstone.org/) เท่าที่ค้น ๆ ดูคร่าว ๆ อันนี้ ไม่ได้เป็น institutional repository software เหมือนกับ DSpace หรือ EPrints เสียทีเดียว แต่เป็น digital library software ([ดูจากบล็อกนี้](http://www.stks.or.th/blog/?p=830) ผมเองก็ยังตอบไม่ได้ว่า แต่ละอย่างมันต่างกันชัด ๆ อย่างไร คิดว่ามันก็ทับ ๆ กันอยู่เยอะ แต่กรณีของ IR นี่ เรื่อง self-archiving น่าจะเป็นลักษณะสำคัญอันนึง) Greenstone นี่น่าสนใจมาก เขาบอกว่าสนับสนุนหลายภาษา มีภาษาไทยด้วย (ยังไม่ได้ค้นต่อว่าที่ว่า “สนับสนุนภาษา” เนี่ย แปลว่าอะไร) มี UNESCO หนุน โอเพ่นซอร์ส และสนับสนุนโปรโตคอล OAI-PMH ร่วมพัฒนาโดยมหาลัยที่สร้าง [WEKA](http://www.cs.waikato.ac.nz/ml/weka/) data mining workbench/toolkit ดูดีนะเนี่ย

open archives, collections, repositories, libraries พวกนี้ นอกจากจะเปิดให้ดูเฉย ๆ แล้ว ถ้าจะให้มีประโยชน์จริง ๆ มันก็ควรจะค้นหาได้แบบ programmable หน่อย หรืออย่างน้อยก็มีวิธีในการค้นหาเหมือน ๆ กันนิดนึง ผู้ใช้จะได้ไม่ต้องเรียนรู้เยอะ ก็เลยเป็นที่มาของมาตรฐานในการค้นหา รวมไปถึงการแลกเปลี่ยนเมตาดาต้าแบบอัตโนมัติด้วย

เอาง่ายที่สุด ก็น่าจะใช้ [OpenSearch](http://www.opensearch.org/) สืบค้นได้ (ถ้านึกไม่ออกว่า OpenSearch คืออะไร ตัวช่องค้นหาบนแถบเครื่องมือใน Internet Explorer 7+ และ Mozilla Firefox 3+ ต่างก็สืบค้นจากบริการที่เราระบุ ผ่าน OpenSearch … อืม ยังไม่ชัด แต่ก็ดูใกล้ตัวหน่อยนึง) แล้วส่งผลลัพธ์ออกมาเป็น RSS/Atom รูปแบบข้อมูลยอดนิยม, ถ้ามี JSON ล่ะก็แจ๋ว ในแง่การเขียนโปรแกรมโดยเฉพาะฝั่ง browser-side

ชุดต่อมา มาจากกลุ่ม Open Archives Initiative มีตัวชูโรงคือ OAI-PMH ที่พูดถึงก่อนหน้านี้ เอาไว้แลกเปลี่ยนเมตาดาต้า :

- [OAI Protocol for Metadata Harvesting (OAI-PMH)](http://www.openarchives.org/pmh/)
- [OAI Object Reuse and Exchange (OAI-ORE)](http://www.openarchives.org/ore/)

สำหรับการสืบค้นสารสนเทศ ดูมาตรฐาน [Z39.50](http://www.loc.gov/z3950/agency/) (ISO 23950: Information Retrieval (Z39.50): Application Service Definition and Protocol Specification) และ [SRU](http://www.loc.gov/standards/sru/) (Search/Retrieve via URL) คู่กับ [CQL](http://www.loc.gov/standards/sru/specs/cql.html) (Contextual Query Language). ‡biblios.net ที่พูดถึงก่อนหน้านี้ รองรับ SRU/CQL ด้วย

ข้อกำหนดเมตาดาต้าที่ได้รับนิยมนำไปปรับใช้มากที่สุดในเว็บนั้น คือ [Dublin Core Metadata Initiative (DMCI)](http://dublincore.org/) ซึ่งคนที่ใช้งานเอกสาร XML ต่าง ๆ อาจจะพอคุ้นเคย ใน namespace “dc:” ซึ่งถูกนำไปใช้กับรูปแบบเอกสาร XML หลายชนิด [OAI เองก็ใช้ Dublin Core](http://www.openarchives.org/OAI/openarchivesprotocol.html#dublincore)

ความเห็นเพิ่มเติมจาก อ.บุญเลิศ “ขณะนี้ DCMI ก็ยอมรับแล้วว่า DC ไม่ใช่มาตรฐานเดียวที่ใช้ได้ มีการทำ Cross กับเมทาดาทาอื่นแล้ว ลองหาอ่านได้จาก DC conference ต่างๆ ได้ครับ”

สำหรับรูปแบบข้อมูลผลลัพธ์จากการสืบค้นสารสนเทศอื่น ๆ ก็เช่น [MARCXML](http://www.loc.gov/standards/marcxml/) ซึ่งพัฒนาต่อมาจากปู่ MARC มีช่องข้อมูลมากมาย เรียกได้ว่าครบถ้วน แต่ก็ซับซ้อนปวดหัว, ต่อมาจึงมี [Metadata Object Description Schema (MODS)](http://www.loc.gov/standards/mods/) ซึ่งอยู่ระหว่างกลาง MARC กับ Dublin Core (ซึ่งมีช่องข้อมูลน้อยมาก ๆ ประมาณว่าใช้ได้กับงานอย่าง RSS Feed จะให้ใช้กับห้องสมุดก็ขาดตกไปหลายอย่าง) เรียกว่า MODS มีช่องข้อมูลที่จำเป็นต้องใช้บ่อย ๆ ในงานห้องสมุด ในขณะเดียวกันก็ไม่ซับซ้อนจนเกินไป, [Metadata Authority Description Schema (MADS)](http://www.loc.gov/standards/mads/) เป็นมาตรฐานที่ออกมาใช้คู่กับ MODS

acronyms ที่พ่นออกมามากมายข้างบน เกินครึ่งกำหนดโดยห้องสมุดรัฐสภาสหรัฐ (Library of Congress) ที่เหลือก็โดยห้องสมุดของมหาวิทยาลัยหรือศูนย์วิจัยต่าง ๆ

ใครสนใจเรื่องพวกนี้ โดยเฉพาะที่ใช้โอเพ่นซอร์ส อัปเดตข่าวสารได้จากเว็บไซต์เหล่านี้ (แนะนำเพิ่มเติมได้)

- [oss4lib](http://www.oss4lib.org/) – Open Source Systems for Libraries
- [code4lib](http://code4lib.org/) – “coders for libraries, libraries for coders” กลุ่มเป้าหมายจะเน้นนักพัฒนามากกว่า oss4lib
- [บล็อก STKS](http://www.stks.or.th/blog/) – ภาษาไทย มีเรื่องการจัดการความรู้ เรื่องห้องสมุดดิจิทัลอยู่เรื่อย ๆ โดยเฉพาะซอฟต์แวร์ที่เป็นโอเพ่นซอร์ส
- [LibraryHub](http://libraryhub.in.th/) – โดย @projectlib เรื่องห้องสมุดในแง่มุมต่าง ๆ (ไม่ได้เน้นเฉพาะเรื่องซอฟต์แวร์)

นอกจากเรื่อง digital repositories แล้วถ้ามีเรื่องการอนุรักษ์ preservation, digitization ควรดู TEI ไว้ด้วย [Text Encoding Initiative](http://www.tei-c.org/) เป็นชุดข้อแนะนำในการบันทึกข้อความมาอยู่ในระบบดิจิทัล พร้อม ๆ กับคำแนะนำในการบันทึกคำอธิบายข้อมูลต่าง ๆ (annotation) ด้วย การทำ archiving, preservation ในลักษณะนี้ ถือเป็นคีย์สำคัญสำหรับ “สาขา” ที่เรียกว่า digital humanities (มนุษยศาสตร์ดิจิทัล) ซึ่งส่วนหนึ่งเป็นการใช้เครื่องมือดิจิทัลศึกษาเอกสาร (และบันทึกผลการวิเคราะห์ไปเป็น annotation อีกชั้น layer นึงบนเอกสาร)

เอ้อ ถ้าอยากทำ OCR มีทูลคิตโอเพ่นซอร์สชื่อ [OCRopus](http://code.google.com/p/ocropus/) ลองแล้ว ใช้ได้เลย มันเชื่อมชิ้นส่วนที่จำเป็นในงาน OCR เข้าด้วยกัน ทั้งส่วนแปลงไฟล์ฟอร์แมต  
หมุนรูป ทำ layout analysis ทำตัวแบบภาษา และการแปลงภาพเป็นตัวอักษร ตัว engine ที่ใช้แปลงภาพเป็นตัวอักษร ตอนนี้ใช้ [tesseract](http://code.google.com/p/tesseract-ocr/) อยู่ โอเพ่นซอร์สเช่นกัน ทั้งหมดนี้เขียนด้วย C แต่มี Python binding ถ้าต้องการ ชุด OCRopus และ tesseract นี้มี Google สนับสนุนการวิจัยและพัฒนา คาดว่าน่าจะเป็นตัวเดียวกับที่ใช้เป็นส่วนหนึ่งของระบบ [Google Book Search]() ผมลองคอมไพล์แล้วรันเล่นดู เจ๋งดี ถ้าใช้ tesseract เฉย ๆ ผลลัพธ์จะเป็น plain text แต่ถ้าใช้ OCRopus tool chain มันได้มาเป็น HTML เลย ([hOCR](http://code.google.com/p/hocr-tools/) microformat) ซึ่งแปลว่าเราจะได้ layout และ style มาด้วย ตัวหนา ตัวเอียง มาหมด

แสกนเข้ามาแล้ว มันก็ต้องมีที่ผิดบ้างแหละ มากน้อยแล้วแต่ จะช่วยกันแก้ไขได้ยังไง ? ลองดูตัวแบบจากโครงการ [Distribute Proofreaders]() (DP) (แนะนำโดย [@thai101](http://twitter.com/thai101) ขอบคุณมาก ๆ ครับ) ซึ่งเป็นการเปิดให้อาสาสมัครบนอินเทอร์เน็ตมาช่วยกันพิสูจน์อักษร แก้ตัวสะกดผิด โดยโครงการนี้เจาะจงไปที่การแสกนหนังสือที่ไม่มีหรือพ้นการคุ้มครองลิขสิทธิ์ไปแล้ว (เป็นสมบัติสาธารณะหรืออยู่ใน Public Domain) พิสูจน์อักษร แล้วก็ส่งต่อหนังสือที่เสร็จสมบูรณ์แล้ว ให้กับ [Project Gutenberg](http://www.gutenberg.org/) ต่อไป ตัวแบบของ DP นี้อาจจะเอามาปรับใช้กับโครงการอื่น ๆ ก็ได้

ทั้งหมดที่กล่าวนี้ จะเห็นว่าในส่วนของมาตรฐานก็เป็นมาตรฐานเปิด ส่วนซอฟต์แวร์ก็มีทางเลือกที่เป็นโอเพ่นซอร์ส แรงงานหรือก็มีคนยินดีร่วมเป็นอาสาสมัคร (ถ้าระบบมันไม่ใช้ยากเกินจนท้อไปเสียก่อน) อนาคตดูดีทีเดียว วงการห้องสมุด

งงกันมาพอสมควรแล้ว โพสต์นี้ไม่ได้ช่วยให้ใครเข้าใจอะไรขึ้นมาได้แน่ ผมเองก็ไม่เข้าใจ แต่มันพอจะทำให้เห็นความเชื่อมโยง อย่างน้อยก็ของตัวย่อมหาศาลที่จะบุกรุกเข้ามาในชีวิตคุณ ถ้าอยากจะเข้าไปสนุกในสนามห้องสมุดิจิทัล โปรดสังเกตว่าผมใช้คำว่า เข้าไป ไม่ใช่ เข้ามา เพราะผมเองก็ยังไม่ได้อยู่ในสนามนั้น :p ถ้าพัฒนาโปรแกรมอินเทอร์เน็ตได้ สนใจงานพวกนี้ อาจจะเฉี่ยวไปเฉี่ยวมาหน่อย ลองดู [Jobs @Opendream](http://opendream.co.th/jobs "งาน ณ อพด.")

ถ้าอยากอ่านอีก โดดไป ~~[ProjectLib](http://projectlib.in.th/)~~ [LibraryHub](http://libraryhub.in.th/) เลย หรือแจม [LibCamp](http://www.projectlib.in.th/?p=1086) ([ภาพงาน](http://www.libraryhub.in.th/2009/05/07/gallery-for-libcamp1/)) ที่เดี๋ยวจะมีอีก ผมไม่รับผิดชอบแล้ว! มึน!

อยากมึนหนัก? เผ่นไปบล็อก [iTeau](http://iteau.wordpress.com/) โลด จริง ๆ ก็อาจจะไม่มึนนะ เขาเขียนอธิบายดีน่ะ ยกจอก 🙂

follow [@projectlib](http://twitter.com/projectlib) [@iteau](http://twitter.com/iteau) [@markpeak](http://twitter.com/markpeak) [@kengggg](http://twitter.com/kengggg) และ [@klaikong](http://twitter.com/klaikong)

อยากมีร้านสำหรับนั่งอ่านหนังสือ

<span class="small">technorati tags:  
[digital library](http://technorati.com/tag/digital+library),  
[open archive](http://technorati.com/tag/open+archive),  
[Opendream](http://technorati.com/tag/Opendream),  
[digitization](http://technorati.com/tag/digitization),  
[metadata](http://technorati.com/tag/metadata),  
[open source](http://technorati.com/tag/open+source),  
[free software](http://technorati.com/tag/free+software),  
[standards](http://technorati.com/tag/standards)  
</span>
