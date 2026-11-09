---
title: "Installing NLTK \"from scratch\""
date: "2005-04-09T18:01:00+07:00"
lastmod: "2005-04-09T18:01:00+07:00"
type: "post"
url: "/2005/installing-nltk-from-scratch/"
description: "Note: This is a unfinished work, will polish it later. เข้าค้าง ๆ มานานละ ไม่เสร็จซะที โพสต์ไปก่อนละกัน เดี๋ยวมาแก้ทีหลัง ไม่งั้นลืมแน่ วิธีติดตั้ง NLTK บน UNIX, Mac OS X, และ cygwin บน Windows (ใครมี gcc และ Python 2.4 แล้ว ก็ข้ามส่วนนั้นไปได้เลย สำหรับคนใช้ cygwin เลือกลง gcc, python ได้จากโปรแกรม"
tag: ["natural-language-processing", "nltk", "python", "wordnet"]
textlang: "en"
wpid: 692
---
Note: This is a unfinished work, will polish it later.  
เข้าค้าง ๆ มานานละ ไม่เสร็จซะที โพสต์ไปก่อนละกัน เดี๋ยวมาแก้ทีหลัง ไม่งั้นลืมแน่

วิธีติดตั้ง NLTK บน UNIX, Mac OS X, และ cygwin บน Windows  
(ใครมี gcc และ Python 2.4 แล้ว ก็ข้ามส่วนนั้นไปได้เลย  
สำหรับคนใช้ cygwin เลือกลง gcc, python ได้จากโปรแกรม install ของ cygwin เลย)

## Install gcc

As most UNIX systems already has gcc, I will discussed only about Mac OS X  
  
(if your system already has gcc (or Xcode), skip this).

1.  Install [Xcode 1.5](http://developer.apple.com/tools/xcode/), for a latest gcc from Apple.  
    (You need an Apple Developer Connection account to download this)
2.  Check if your gcc need a patch or not.  
    At a command line, type `gcc -v`  
    If the build number is 1666 or lower, you have to install a [November2004gccupdater](http://developer.apple.com/tools/xcode/) package to fix Apple’s gcc bug.

## Install Python 2.4 and Tkinter

If your system already has Python 2.4 (or newer) and a working Tkinter, skip this.  
To test it, read (7).

3.  Install [PantherPythonFix](http://homepages.cwi.nl/~jack/macpython/beta.html)
4.  Install [Tcl/Tk Aqua](http://tcltkaqua.sf.net/)
5.  Install [Python 2.4 for Mac OS X](http://python.org/) from source
    1.  [download the source code]()
    2.  unzip it
    3.  ./configure
    4.  make
    5.  sudo make install
6.  change Python path and links
    1.  symbolic links
    2.  set PYTHOHPATH in .profile
    3.  test if the default Python is Python 2.4  
        `python -V`
7.  test if the Python + Tcl/Tk works?  
    run Example 2-1 of  
    http://www.pythonware.com/library/tkinter/introduction/hello-tkinter.htm

## Install NLTK

read http://nltk.sourceforge.net/install.html

1.  install [Numarray](http://www.stsci.edu/resources/software_hardware/numarray)
    1.  sudo python setup.py install
2.  install [NLTK](http://nltk.sourceforge.net/)
    1.  sudo python setup.py install
3.  install [NLTK Data Package](http://nltk.sourceforge.net/)
    1.  extract to …
    2.  change *NLTK_CORPORA* environment variable in your *.profile* file to that path
4.  install [NLTK Contributions Package](http://nltk.sourceforge.net/) (optional)

## Install PyWordNet & WordNet

UNIX, Mac OS X: Download [WordNet](http://wordnet.princeton.edu/) and install it.

Cygwin: You can install WordNet from the cygwin setup program, it is in *Utils* category.

In cygwin, a WNHOME environment variable should be set as /lib/wnres. You can do this by modify the /etc/profile file.

WNHOME=/lib/wnres  
export WNHOME

In general case, it may not necessary to do this.  
But if you also has a WordNet for Windows installed (probably in C:\Program Files\WordNet), you have to set WNHOME in cygwin explicitly. Unless the WordNet for Windows’s WNHOME will confused cygwin’s WordNet.

To install PyWordNet, type python setup.py install

When you import wordnet module, you will see several warnings say:  
*Exception exceptions.AttributeError: “DbfilenameShelf instance has no attribute ‘writeback'” in ignored.*  
You haven’t did anything wrong, [everybody faces this](https://sourceforge.net/tracker/index.php?func=detail&aid=1143590&group_id=27422&atid=390153). May be it will get fixed in next version of PyWordNet.
