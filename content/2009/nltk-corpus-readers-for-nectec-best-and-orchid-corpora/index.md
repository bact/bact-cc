---
title: "NLTK corpus readers for NECTEC BEST and ORCHID corpora"
date: "2009-04-28T00:44:00+07:00"
lastmod: "2011-05-22T11:16:16+07:00"
type: "post"
url: "/2009/nltk-corpus-readers-for-nectec-best-and-orchid-corpora/"
description: "ความเดิมจากตอนที่แล้ว ทดลองสร้าง corpus reader ใน NLTK ตอนนี้แก้การ encode ให้ใช้ได้กับ nltk.Text() แล้ว (แทนที่จะเก็บเป็น unicode ก็เก็บเป็น utf-8 encoded str แทน) พร้อมกับเพิ่มตัวอ่านสำหรับคลังข้อความ BEST และ ORCHID ด้วย ตัวอ่านคลัง BEST ในรุ่น 0.3 นี้ เรียกดูเป็นหมวดได้ (ข่าว วรรณกรรม สารานุกรม "
categories: ["coling", "computer"]
tag: ["corpora", "linguistic-resources", "natural-language-processing", "nltk", "opendream", "programming", "python", "roti", "thai"]
textlang: "th"
wpid: 2448
---
[ความเดิมจากตอนที่แล้ว](/2009/playing-around-thai-blog-corpus-with-nltk/ "playing around Thai blog corpus with NLTK") ทดลองสร้าง corpus reader ใน [NLTK](http://www.nltk.org/)

ตอนนี้แก้การ encode ให้ใช้ได้กับ nltk.Text() แล้ว (แทนที่จะเก็บเป็น unicode ก็[เก็บเป็น utf-8 encoded str แทน](http://groups.google.com/group/nltk-users/browse_thread/thread/53bd48fb6850c549))

พร้อมกับเพิ่มตัวอ่านสำหรับคลังข้อความ [BEST](http://naist.cpe.ku.ac.th/thlta_wiki/index.php/Share#BEST_corpus) และ [ORCHID](http://naist.cpe.ku.ac.th/thlta_wiki/index.php/Share#Orchid_corpus) ด้วย

ตัวอ่านคลัง BEST ในรุ่น 0.3 นี้ เรียกดูเป็นหมวดได้ (ข่าว วรรณกรรม สารานุกรม บทความ) เรียกดูข้อมูลกำกับขอบเขตคำ (word boundaries) ได้ แต่ยังไม่รองรับ \<NE\>named-entities\</NE\> กับ \<AB\>คำย่อ\</AB\> เนื่องจาก BEST ไม่มีข้อมูลขอบเขตประโยค ตัวอ่านคลังจะสร้างขึ้นเอง โดยสมมติ \n เป็นขอบเขตประโยค

ส่วนตัวอ่านคลัง ORCHID ในรุ่น 0.3 นี้ เรียกดูข้อมูลกำกับขอบเขตคำและชนิดคำ (Part-of-Speech) ได้ แต่ยังไม่รองรับขอบเขตย่อหน้า และยังเรียกดูเป็นรายเอกสารไม่ได้ (รุ่นนี้ทำงานกับคลัง ORCHID แบบที่ถูกเอา document-related metadata ออกไป)

#### ดาวน์โหลด & ติดตั้ง

แพ็คเกจ rotic รุ่น 0.3 ซอร์สโค้ดเผยแพร่ด้วยสัญญาอนุญาต [GNU GPLv2](http://www.gnu.org/licenses/gpl-2.0.html) ตาม NLTK – ดาวน์โหลด [rotic-0.3.tar.gz](http://culturelab.in.th/files/rotic-0.3.tar.gz)

วิธีติดตั้ง อ่าน README.TXT และ INSTALL.TXT – อย่าลืมดาวน์โหลดคลังข้อความมาติดตั้งด้วย รายละเอียดและสัญญาอนุญาตของข้อมูลแต่ละชุด อยู่ใน CORPORA.TXT

**มีคำแนะนำอะไร เขียนมาบอกกันได้ครับ อยากจะลองทำให้มันเอาไปใช้ในการเรียนการสอนได้ – ไม่เฉพาะสำหรับนักเรียนคอมพิวเตอร์เท่านั้น แต่สำหรับนักเรียนภาษาศาสตร์ ฯลฯ ด้วย**

ตอนนี้ความเร็วไม่ค่อยดีเท่าไหร่ โดยเฉพาะการโหลดตัว ORCHID ซึ่งใหญ่มาก ส่วนหนึ่งเป็นเพราะโค้ดยังซ้ำซ้อนอยู่หลายจุด เช่นตรงการแปลง utf-8 ที่น่าจะทำได้ตั้งแต่ระดับแรก ๆ ที่อ่านเข้ามาเลย ไม่ใช่มาแปลงเอาตอนหลัง-ต้องวนลูปอีกหนึ่งครั้งแบบขณะนี้ โค้ดยัง refactor ได้อีกเยอะ ใครคล่อง Python ก็ช่วยดูหน่อยนะครับ ผมแค่พอเขียนไถ ๆ ได้ ขอบคุณครับ 🙂

#### ตัวอย่างจาก example.py

1\. พิมพ์ข้อความมั่ว ๆ ขึ้นมาจากตัวแบบ n-gram ที่สร้างจากคำในคลัง foosci :

    foosci_text = nltk.Text(foosci.words())
    foosci_text.generate()

ผลลัพธ์ :

> … ซึ่ง ทฤษฎี สรุป ความรู้ ของ เรา เอา ไส้เดือน ไป ปล่อย ใน พื้นที่ ๆ มี ความ สงสัย ระหว่าง ความ เชื่อ เรื่อง มิติ ใหม่ นี้ …

2\. พิมพ์ คำ/ชนิดคำ จาก 5 “ประโยค” แรกของคลัง ORCHID  
โปรดสังเกตว่า เราใช้ชุดชนิดคำ (POS/tagset) แบบง่าย สามารถสลับชุดชนิดคำได้โดยสลับค่า simplify_tags :

<pre><code>
for sent in orchid.tagged_sents(<span style="color: red;">simplify_tags=True</span>)[0:5]:
    print "[",
    for (word, tag) in sent:
        print word + "/" + tag,
    print "]"
</code></pre>

ผลลัพธ์ :

> \[ การ/FIX ประชุม/V ทาง/N วิชาการ/N /PUNC ครั้ง/C ที่\_1/DETN \]  
> \[ โครงการวิจัยและพัฒนา/N อิเล็กทรอนิกส์/N และ/CONJ คอมพิวเตอร์/N \]  
> \[ ปีงบประมาณ/N /PUNC 2531/N \]  
> \[ เล่ม/C /PUNC 1/DETN \]  
> \[ ศูนย์เทคโนโลยีอิเล็กทรอนิกส์และคอมพิวเตอร์แห่งชาติ/N \]

3\. หาค่าการกระจายของสองคำ “การ” และ “ความ” ใน 4 หมวดของคลัง BEST  
โปรดสังเกตว่า ตรงคำที่เราจะป้อนเข้าไปให้ฟังก์ชั่นต่าง ๆ ของ NLTK เราจะแปลงมันเป็น utf-8 encoded str ก่อน :

<pre><code>
cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in best.categories()
        for word in best.words(categories=genre))
genres = ['news', 'encyclopedia', 'novel', 'article']
prefixs = [<span style="color: red;">w.encode("utf-8")</span> for w in [u'การ', u'ความ']]
cfd.tabulate(conditions=genres, samples=prefixs)
</code></pre>

ผลลัพธ์ :

                 การ ความ
            news 29567 11186
    encyclopedia 25477 8541
           novel 4258 9097
         article 33200 16651

เล่นต่อเอง จากตัวอย่างใน[หนังสือ NLTK](http://www.nltk.org/book)

เดี๋ยวอาจจะให้น้องฝึกงานที่[โอเพ่นดรีม](http://opendream.co.th/)เอาไปทำต่อ เช่นทำให้มันใช้ AB, NE หรือขอบเขตประโยค/ย่อหน้าได้ .. เห็นนั่งเล่นเกมมาหลายวันละ :p

<span class="small">technorati tags: [corpus linguistics](http://technorati.com/tag/corpus+linguistics), [NLTK](http://technorati.com/tag/NLTK), [Python](http://technorati.com/tag/Python), [Thai](http://technorati.com/tag/Thai)</span>
