---
title: "Nix – the \"functional\" package manager"
date: "2007-04-02T01:58:00+07:00"
lastmod: "2011-05-05T12:05:45+07:00"
type: "post"
url: "/2007/nix-the-functional-package-manager/"
description: "เฮ้ย น่าสนใจ, จาก OSNews: “NixOS is a Linux distribution based on Nix, a purely functional package management system. NixOS is an experiment to see if we can build an operating system in which software packages, configuration files, boot scripts and the like are all managed in a purely functional wa"
categories: ["computer", "informatics"]
tag: ["linux"]
textlang: "th"
wpid: 1986
---
เฮ้ย น่าสนใจ, จาก [OSNews](http://osnews.com/story.php/17601/NixOS-a-Purely-Functional-Linux-Distribution):

> “[NixOS](http://nix.cs.uu.nl/nixos/) is a Linux distribution based on [Nix](http://nix.cs.uu.nl/), a purely functional package management system. NixOS is an experiment to see if we can build an operating system in which software packages, configuration files, boot scripts and the like are all managed in a purely functional way, that is, they are all built by deterministic functions and they never change after they have been built.”

Nix เป็นระบบจัดการหีบห่อซอฟต์แวร์ (แพ็คเกจ) ตัวหนึ่ง (ทำนองเดียวกับพวก dpkg, RPM ฯลฯ บน Unix-like system หรืออย่าง gem ของ Ruby นี่ก็ใช่)  
แต่ที่มันไม่เหมือนกับระบบอื่น ๆ ก็คือ ตัวชุดคำสั่งที่ระบุค่าต่าง ๆ สำหรับติดตั้งซอฟต์แวร์ของ Nix นั้น ยืมแนวคิดมาจาก functional language – [ดูตัวอย่าง](http://nix.cs.uu.nl/dist/nix/nix-0.10.1/manual/#id3394604) (ผมก็ดูไม่ค่อยรู้เรื่องหรอกนะ)

ดู [functional programming](http://en.wikipedia.org/wiki/Functional_programming) และ [declarative programming](http://en.wikipedia.org/wiki/Declarative_programming)  
ภาษาโปรแกรมส่วนใหญ่ที่ใช้เขียน ๆ โปรแกรมที่เราใช้งานกันอยู่ (เช่น PHP, C, Java, JavaScript) เป็นแบบ procedural – imperative คือต้องอธิบายการทำงานมันเป็นขั้น ๆ บอกคอมพิวเตอร์มันว่าจะทำ “อย่างไร” ในขณะที่ภาษาแบบ declarative จะบอกว่า จะทำ “อะไร”

มี[เอกสารวิชาการ](http://nix.cs.uu.nl/docs/papers.html)ที่อธิบายแนวคิด functional package management system ให้ดูด้วย

ส่วน NixOS นั่น ก็เป็นลีนุกซ์รุ่นที่ใช้ Nix นั่นเอง

ผลงานจาก [ภาควิชาวิทยาศาสตร์สารสนเทศและการคำนวณ](http://www.cs.uu.nl/) [มหาวิทยาลัยอูเทรชท์](http://www.uu.nl/) (Universiteit Utrecht) เนเธอร์แลนด์

อูเทรชท์เป็นเมืองน่ารักนะ 🙂 — [มิฟฟี่](http://en.wikipedia.org/wiki/Miffy "Miffy") กระต่ายปากกากบาท เกิดที่นี่ 😀

\[ผ่าน [OSNews](http://osnews.com/story.php/17601/NixOS-a-Purely-Functional-Linux-Distribution "NixOS: a Purely Functional Linux Distribution")\]

<span class="small">technorati tags: [package management system](http://technorati.com/tag/package_management_system), [Nix](http://technorati.com/tag/Nix), [NixOS](http://technorati.com/tag/NixOS)</span>
