---
title: "Building OOo with MS VC++ Toolkit 2003 : Issues"
date: "2004-05-10T22:26:00+07:00"
lastmod: "2004-05-10T22:26:00+07:00"
type: "post"
url: "/2004/building-ooo-with-ms-vc-toolkit-2003-issues/"
description: "Compiled from OOo mailing lists (dev-help@ja, dev@l10n) Additional Resources: openoffice.s16.xrea.com (VC++ Toolkit 2003 with OOo) [Japanese] dev-help@ja IZ #27980 (Visual Studio 2003) MS Visual C++ Toolkit 2003 do has: C++ command-line compiler and linker (the same as in VS 2003), Standard C++ libr"
tag: ["openoffice-org"]
textlang: "en"
wpid: 103
---
Compiled from OOo mailing lists (dev-help@ja, dev@l10n)

Additional Resources:

1. [openoffice.s16.xrea.com](http://openoffice.s16.xrea.com:8080/pukiwiki/pukiwiki.php?Microsoft_Visual_C%2B%2B_Toolkit_2003) (VC++ Toolkit 2003 with OOo) <span class="small">\[Japanese\]</span>
2. [dev-help@ja](http://ja.openoffice.org/servlets/ReadMsg?listName=dev&msgNo=2483)
3. [IZ \#27980](http://www.openoffice.org/issues/show_bug.cgi?id=27980) (Visual Studio 2003)

[MS Visual C++ Toolkit 2003](http://msdn.microsoft.com/visualc/vctoolkit2003/)  
**do has:** C++ command-line compiler and linker (the same as in VS 2003), Standard C++ libraries (including STL)  
**does’t has:** assembler (workaround: masm32), MFC and ATL libraries

**joerg.barfurth at sun com** reported:  
IIRC there are some modules (of ‘external’ origin) that build using a Visual Studio project file. For those projects the VC++ toolkit would be insufficient.

**tuomo at openoffice org** reported:

- *comsupp.lib* required for dtranse
- “old iostram libraries” (as MS refers to) required throughout the source.

**olivier at ig com br** reported:  
configure (winenv.set) needs adjustments to pick *mspdb71.dll*, as OOo 1.1.1 looks to *mspdb?0.dll*

more discussions will follow, in [dev@tools](http://tools.openoffice.org/servlets/ReadMsg?list=dev&msgNo=4937)
