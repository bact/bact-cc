---
title: "จุดอ่อนของ AI ในงานความมั่นคงปลอดภัยทางสารสนเทศ #infosec17"
date: "2017-06-13T10:55:31+07:00"
lastmod: "2017-06-14T12:38:44+07:00"
type: "post"
url: "/2017/adversarial-machine-learning/"
description: "ปัญญาประดิษฐ์กับความมั่นคงไซเบอร์ AI ฉลาด แต่ก็ถูกหลอกได้ ถ้าจะเอามาช่วยงานความมั่นคงปลอดภัยทางสารสนเทศต้องระวังอะไรบ้าง สรุปจากงาน Infosecurity Europe 2017"
categories: ["informatics"]
tag: ["adversarial-machine-learning", "artificial-intelligence", "cybersecurity", "giovanni-vigna", "information-security", "machine-learning"]
image: "/f/2017/06/giovanni-adversarial-ml-02.jpg"
textlang: "th"
wpid: 3577
---
ในงาน [Infosecurity Europe 2017](http://www.infosecurityeurope.com/) นอกจากคำว่า [GDPR](/2017/gdpr-data-governance/) และ [IoT](/2017/cybersecurity-iot/) ที่เดินไปไหนก็เจอแล้ว ยังมีอีก 2 คำที่มาคู่กันให้เห็นไปทั่ว คือคำว่า artificial intelligence ([ปัญญาประดิษฐ์](https://th.wikipedia.org/wiki/%E0%B8%9B%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B2%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%94%E0%B8%B4%E0%B8%A9%E0%B8%90%E0%B9%8C)) และ machine learning ([การเรียนรู้ของเครื่อง](https://th.wikipedia.org/wiki/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%99%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87))

หัวข้อหนึ่งที่ได้ไปฟังแล้วน่าสนใจคือ [Adversarial Machine Learning: The Pitfalls of Artificial Intelligence-based Security](http://www.infosecurityeurope.com/en/Sessions/41978/Adversarial-Machine-Learning-The-Pitfalls-of-Artificial-Intelligence-based-Security) โดยมี [Giovanni Vigna](https://www.cs.ucsb.edu/~vigna/) ซึ่งเป็นอาจารย์ที่ [UC Santa Barbara](https://seclab.cs.ucsb.edu/) และหนึ่งในผู้ก่อตั้งบริษัท [Lastline](https://en.wikipedia.org/wiki/Lastline) มาเป็นวิทยากร

<figure id="attachment_3578" class="wp-caption aligncenter" aria-describedby="caption-attachment-3578" style="width: 4032px">
<a href="/f/2017/06/giovanni-adversarial-ml-01.jpg"><img src="/f/2017/06/giovanni-adversarial-ml-01.jpg" alt="Machine learning and security" /></a>
<figcaption>Machine learning and security</figcaption>
</figure>

หลักๆ คือ Giovanni พูดถึงว่า การมีข้อมูลให้เครื่องมันเรียนรู้ถึงรูปแบบมัลแวร์และการโจมตีต่างๆ ก็อาจจะทำให้คอมพิวเตอร์มันเก่งขึ้นได้ในการตรวจจับความผิดปกติ (anomaly detection) โดยอัตโนมัติ ซึ่งอันนี้ก็ใช้เทคนิค classification และ clustering ทำนองเดียวกับแอปพลิเคชันอย่างการรู้จำภาพ โดยเขายกตัวอย่างการหาความผิดปกติในจาวาสคริปต์ ที่ก็อาจจะใช้การวิเคราะห์ข้อมูลจาก abstract syntax tree (AST) เพื่อเปรียบเทียบกับจุดที่เคยมีข้อมูลมาก่อนว่าเป็นอันตราย

<figure id="attachment_3580" class="wp-caption aligncenter" aria-describedby="caption-attachment-3580" style="width: 4032px">
<a href="/f/2017/06/giovanni-adversarial-ml-03.jpg"><img src="/f/2017/06/giovanni-adversarial-ml-03.jpg" alt="Identifying adversaries: Malicious evasive JavaScript" /></a>
<figcaption>Identifying adversaries: Malicious evasive JavaScript</figcaption>
</figure>

อย่างไรก็ตาม เช่นเดียวกับระบบปัญญาประดิษฐ์ทั่วไป ที่เครื่องมันก็อาจจะตอบผิดบ้าง (ทั้ง false negative – มีอันตรายจริงๆ แต่หลงหูหลงตาไป ไม่ได้แจ้งเตือน และ false positive – แจ้งเตือนว่าเป็นอันตรายทั้งที่จริงไม่ใช่) แต่นอกจากนั้นแล้ว การใช้ปัญญาประดิษฐ์ และโดยเฉพาะเจาะจงคือการเรียนรู้ของเครื่อง กับงานความมั่นคงปลอดภัยยังมีจุดอ่อนอยู่อย่างน้อยอีก 2 อย่าง หากผู้โจมตีสามารถศึกษาและเข้าใจโมเดลที่ระบบใช้ได้ (ซึ่งการได้มาซึ่งโมเดลนี่ก็อาจจะใช้วิธี reverse engineering เอาก็ได้ เช่น[ขโมยผ่าน machine learning API](https://www.wired.com/2016/09/how-to-steal-an-ai/) – [ดูเปเปอร์](https://arxiv.org/abs/1609.02943))

- อย่างแรกคือ ศึกษาหาจุดบอดของโมเดล เพื่อสามารถรู้ได้อย่างเจาะจงมากขึ้นว่า ในกรณีไหน (ด้วย feature set แบบไหน ในเงื่อนไขไหน) ที่ระบบจะถูกหลอกได้ (ทั้ง false positive และ false negative) และนำจุดอ่อนนี้ไปหาประโยชน์ และ
- อย่างที่สองคือ ศึกษาว่าการเรียนรู้ปรับปรุงโมเดลนั้นทำอย่างไร ใช้ข้อมูลทำนองไหน และหาทางป้อนข้อมูลที่สร้างขึ้นมาหลอกๆ เพื่อทำให้โมเดลเปลี่ยนไปในทางที่ต้องการ พูดอีกอย่างคือเป็นการทำให้โมเดลถูกปนเปื้อน (contaminated / polluted)

ใครอยากอ่านโดยละเอียดเกี่ยวกับเรื่องพวกนี้ เอาชื่อหัวข้อแต่ละอันในสไลด์ข้างล่างนี้ ไปค้นอินเทอร์เน็ตได้เลยครับ

<figure id="attachment_3579" class="wp-caption aligncenter" aria-describedby="caption-attachment-3579" style="width: 4032px">
<a href="/f/2017/06/giovanni-adversarial-ml-02.jpg"><img src="/f/2017/06/giovanni-adversarial-ml-02.jpg" alt="Adversarial machine learning is here" /></a>
<figcaption>Adversarial machine learning is here</figcaption>
</figure>

จริงๆ ปัญหาทั้งสองอย่างที่พูดถึงข้างบน ไม่ได้เกิดขึ้นได้เฉพาะกับแอปพลิเคชันด้านความมั่นคงปลอดภัย การใช้ปัญญาประดิษฐ์หรือการเรียนรู้ของเครื่องในงานประมวลผลภาษาธรรมชาติหรือการรู้จำรูปภาพก็เจอปัญหาแบบเดียวกันนี้ได้ เพียงแต่สิ่งต่างกันคือ

- สภาพแวดล้อม (ข้อมูล) สำหรับการใช้ภาษาหรือรูปภาพ มันเปลี่ยนแปลงช้ากว่าสภาพแวดล้อมในโลกความมั่นคงทางสารสนเทศ (ที่มีมัลแวร์ใหม่ๆ เกิดขึ้นทุกวัน) และ
- มันมีแรงจูงใจมากกว่าที่จะเอาชนะโมเดลในงานด้านความมั่นคง (ถ้าเราสามารถทำให้ Siri หรือ Google Translate ทำอะไรแปลกๆ ได้ ก็อาจจะตลกดี มีแรงจูงใจด้านความบันเทิง ความอยากรู้อยากเห็น ในขณะที่งานด้านความมั่นคงทางสารสนเทศมีแรงจูงใจด้านเศรษฐกิจหรือด้านการเมืองชัดเจน)

การใช้ AI ในงานความมั่นคงปลอดภัย จึงจำเป็นต้องระมัดระวังมากขึ้น คือมันมีคนพร้อมจะเล่นงานเมื่อคุณพลาด หรือถ้าคุณยังไม่พลาด เขาก็จะล่อลวงให้คุณพลาดให้ได้

แต่ในด้านกลับ ความรู้ที่เรียกว่า [“adversarial machine learning”](https://en.wikipedia.org/wiki/Adversarial_machine_learning) นี้ก็อาจจะถูกใช้เพื่อสร้างกับดักหรือกระทั่งตามล่าการโจมตีแบบใหม่ๆ ก็ได้ คือเอาไปหลอกคนที่จะมาโจมตีก็ได้

<figure id="attachment_3585" class="wp-caption aligncenter" aria-describedby="caption-attachment-3585" style="width: 4032px">
<a href="/f/2017/06/giovanni-adversarial-ml-08.jpg"><img src="/f/2017/06/giovanni-adversarial-ml-08.jpg" alt="From trapping to hunting" /></a>
<figcaption>From trapping to hunting</figcaption>
</figure>

ตอบจบก่อนช่วงสรุป วิทยากรบอกให้เราตั้งคำถามให้ดี เวลามีใครมาเสนอขายระบบที่ใช้ AI หรือ Deep Learning (ซึ่งตอนนี้เป็นคำฮิตอีกคำ) เพื่อปกป้องความมั่นคงปลอดภัยทางสารสนเทศ (โน๊ต: วิทยากรก็มานำเสนอในฐานะตัวแทนบริษัทขายระบบพวกนี้เหมือนกัน)  คำถามเหล่านั้นก็คือ

- ระบบดังกล่าวใช้เทคนิคอะไรมาประกอบกันบ้าง
- ระบบใช้ข้อมูลชุดใดบ้างในการสอนโมเดล
- ความสามารถในการป้องกันการถูกโจมตี (ตามที่โฆษณา) นั้นถูกประเมินอย่างไร
- ประเมินภายใต้โมเดลภัยคุกคาม (threat model) แบบไหน?
- วิธีที่ระบบใช้มี ความเที่ยง (precision) และ  การเรียกกลับ (recall) เท่าใด (ความเที่ยง หมายถึง จากจำนวนที่ระบบบอกว่าเป็นความผิดปกติ มีที่ผิดปกติจริงๆ เท่าใด, การเรียกกลับ หมายถึง จากจำนวนความผิดปกติที่มีอยู่จริงๆ ระบบสามารถพบได้เท่าใด)

ถ้าคนขายตอบสิ่งเหล่านี้ชัดๆ ไม่ได้ เราก็มีข้อมูลไม่พอจะตัดสินใจว่าระบบที่เขาอยากขายนั้นจะใช้ได้ดีกับงานของเราหรือไม่

<figure id="attachment_3583" class="wp-caption aligncenter" aria-describedby="caption-attachment-3583" style="width: 4032px">
<a href="/f/2017/06/giovanni-adversarial-ml-06.jpg"><img src="/f/2017/06/giovanni-adversarial-ml-06.jpg" alt="What to ask about AI/ML/Deep Learning-based technology" /></a>
<figcaption>What to ask about AI/ML/Deep Learning-based technology</figcaption>
</figure>

หลังนำเสนอจบ มีโอกาสเข้าไปคุยกับวิทยากรนิดหน่อย ถามเขาไปว่า มันเป็นไปได้ไหมที่จะแชร์โมเดลตรวจจับความผิดปกติทางความมั่นคงปลอดภัยกัน

บริบทคือว่า ปัจจุบันสิ่งหนึ่งที่ชุมชนความมั่นคงปลอดภัยทางสารสนเทศทำกัน เพื่อเพิ่มความปลอดภัยในภาพรวมของทุกคน ก็คือการแบ่งปันข้อมูลการโจมตีหรือจุดอ่อนต่างๆ กัน แต่ทีนี้ ข้อมูลบางชุดก็อาจจะมีข้อมูลส่วนบุคคลหรือความลับทางการค้าติดอยู่ด้วย ทำให้บริษัทไม่สะดวกที่จะแชร์ให้กับ CERT หรือกับหน่วยงานอื่น ทีนี้ ถ้าเกิดว่าแต่ละหน่วยงานต่อไปมีการเก็บข้อมูลมาสร้างโมเดลตรวจจับของตัวเอง มันเป็นไปได้ไหม ที่จะแชร์(บางส่วนของ)โมเดลออกไปให้หน่วยงานภายนอก เพื่อให้เอาไปปรับปรุงโมเดลของเขา ทำนองว่าเป็น machine learning แบบช่วยๆ กันทำ โดยไม่ต้องแชร์ข้อมูลที่ใช้เรียน แชร์เฉพาะโมเดลที่สำเร็จแล้ว (ซึ่งน่าจะไม่เหลือข้อมูลที่อ่อนไหวไม่อยากแชร์)

Giovanni ตอบสั้นๆ ว่า มีคนคิดเรื่องนี้อยู่ แต่ ณ ขณะนี้ เทคโนโลยียังไปไม่ถึงตรงนั้น

ผมถ่ายมาไม่ครบทุกสไลด์ (เกรงใจ) คิดว่าอีกสักพักเขาน่าจะอัปโหลดไปที่ไหนสักที่ครับ ทางงานประชุมมีสรุปไว้ด้วย: [**\#INFOSEC17 Machine Learning is Positive, but not a Security Solution**](https://www.infosecurity-magazine.com/news/infosec17-machine-learning/)

งาน Infosecurity Europe นี้ไม่ได้รู้จักมาก่อน (ผมไม่ใช่คนในวิชาชีพนี้โดยตรง เพียงแต่ต้องติดตามบ้างจากงานที่ทำงาน) เพิ่งจะรู้จากทวิตเตอร์ตอนที่ไปอยู่ลอนดอนได้สัปดาห์นึงแล้วนี่แหละ คือพวกผมไปกันอีกงานหนึ่งชื่องาน **[Mobile Media and Communication Practices in Southeast Asia](http://socanth.tu.ac.th/ccscs/digital-sea/events/goldsmiths-research-seminar/)** เป็นงานสัมมนาวิชาการที่คณะสังคมวิทยาและมานุษยวิทยา ที่ธรรมศาสตร์ จัดร่วมกับ [Goldsmiths Media Ethnography Group](http://www.gold.ac.uk/media-communications/research/goldsmiths-media-ethnography-group/) มหาวิทยาลัยลอนดอน ไม่ค่อยเกี่ยวกับด้านความมั่นคงปลอดภัยทางสารสนเทศเท่าไหร่ (แต่ก็มีหัวข้อนึงที่อาจารย์จาก Goldsmiths วิเคราะห์นโยบาย Thailand 4.0 และ Smart Thailand อาจจะเฉียดๆ)

อย่างไรก็ตาม ก็รู้สึกคุ้มค่าที่ได้ไป (ถ้ารู้เร็วกว่านี้อีกนิดก็จะดี จะได้ลงทะเบียนเข้าฟรี พอรู้ช้าต้องไปลงทะเบียนหน้างาน ต้องจ่าย 35 ปอนด์สำหรับงาน 3 วัน) ไปแล้วก็รู้สึกว่าอยากเขียนมาเล่า ยังไงอ่านอีกสองโพสต์ก่อนหน้าได้ครับ **[หลักการ/กลไกการคุ้มครองข้อมูลใหม่ใน GDPR ของสหภาพยุโรป](/2017/gdpr-data-governance/)** และ **[ความมั่นคงปลอดภัยของ Internet of Things – ข้อคิดจาก Bruce Schneier](/2017/cybersecurity-iot/)**

[ร่างพ.ร.บ.ว่าด้วยการรักษาความมั่นคงปลอดภัยไซเบอร์](http://www.lawamendment.go.th/index.php/component/k2/item/1013-2017-05-23-08-29-00) ใกล้จะคลอดเต็มทน ใครมีความคิดเห็นอะไรก็ส่งไปได้นะครับ แฟกซ์ 0-2281-2904 อีเมล legal@alro.go.th

<figure id="attachment_3581" class="wp-caption aligncenter" aria-describedby="caption-attachment-3581" style="width: 4032px">
<a href="/f/2017/06/giovanni-adversarial-ml-04.jpg"><img src="/f/2017/06/giovanni-adversarial-ml-04.jpg" alt="Machine learning: The last line of defense" /></a>
<figcaption>Machine learning: The last line of defense</figcaption>
</figure>

<figure id="attachment_3582" class="wp-caption aligncenter" aria-describedby="caption-attachment-3582" style="width: 4032px">
<a href="/f/2017/06/giovanni-adversarial-ml-05.jpg"><img src="/f/2017/06/giovanni-adversarial-ml-05.jpg" alt="Learn what your network does" /></a>
<figcaption>Learn what your network does</figcaption>
</figure>

<figure id="attachment_3586" class="wp-caption aligncenter" aria-describedby="caption-attachment-3586" style="width: 4032px">
<a href="/f/2017/06/giovanni-adversarial-ml-07-1.jpg"><img src="/f/2017/06/giovanni-adversarial-ml-07-1.jpg" alt="Conclusions" /></a>
<figcaption>Conclusions</figcaption>
</figure>
