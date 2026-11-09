---
title: "Run .jar as .exe"
date: "2005-07-20T21:41:00+07:00"
lastmod: "2005-07-20T21:41:00+07:00"
type: "post"
url: "/2005/run-jar-as-exe/"
description: "เรียกใช้งานไฟล์ .jar ของจาวา เหมือนเรียกใช้ไฟล์ .exe .com .bat ทั่ว ๆ ไปของวินโดวส์ Run Java jar file from Windows 2000/XP command-line like a native executable. A technique from James Clark (I got it from XML Hacks book). At a command-line, type these two commands: assoc .jar=jarfile ftype jarfile="
tag: ["how-to", "java", "windows"]
textlang: "en"
wpid: 902
---
เรียกใช้งานไฟล์ .jar ของจาวา เหมือนเรียกใช้ไฟล์ .exe .com .bat ทั่ว ๆ ไปของวินโดวส์

Run Java jar file from Windows 2000/XP command-line like a native executable. A technique [from James Clark](http://lists.oasis-open.org/archives/relax-ng/200203/msg00037.html) (I got it from [XML Hacks](http://www.oreilly.com/catalog/xmlhks/) book).

At a command-line, type these two commands:

<pre>
assoc .jar=jarfile
ftype jarfile=<em>(JAVA_HOME)</em>\bin\java -jar %1 %*
</pre>

Then, change PATHEXT and PATH environment variables.  
Right-clicking on *My Computer*, select *Properties*. Select *Advanced* tab, then *Environment Variables*.

Looking for *PATHEXT* variable, append “***.jar***” to its value.

Looking for *PATH* variable, insert “***.***” (dot, which means current directory) at the beginning of its value.

You got it!

Now try it. Say, if you have a file notepad.jar. To run it, instead of typing:

    java -jar notepad.jar

you can just type:

    notepad

Better? 😉
