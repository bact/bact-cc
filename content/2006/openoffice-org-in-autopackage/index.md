---
title: "OpenOffice.org in Autopackage"
date: "2006-03-28T18:28:00+07:00"
lastmod: "2006-03-28T18:28:00+07:00"
type: "post"
url: "/2006/openoffice-org-in-autopackage/"
description: "OpenOffice.org Autopackage distribution proposal/summary | issue 46333 (vote here) Autopackage is a package management system targeted multiple Linux distributions. Unlike traditional package formats such as RPM and DEB, it checks for the presence of dependencies on the actual system files, rather t"
tag: ["openoffice-org"]
textlang: "en"
wpid: 1374
---
OpenOffice.org Autopackage distribution  
[proposal/summary](http://wiki.services.openoffice.org/wiki/Autopackage_distribution "wiki page") \|  
[issue 46333](http://www.openoffice.org/issues/show_bug.cgi?id=46333) (vote here)

------------------------------------------------------------------------

[Autopackage](http://en.wikipedia.org/wiki/Autopackage) is a package management system targeted multiple Linux distributions. Unlike traditional package formats such as RPM and DEB, it checks for the presence of dependencies *on the actual system files*, rather than querying a database of package information. This reduces compatibility issues with different package naming conventions, relaxes package version dependency.

By providing OpenOffice.org in autopackage format, **it will simplify the Linux installation process**. And will also provide the foundation for *incremental update* mechanism <span class="small">(similiar to the auto-updater in Firefox 1.5)</span>.
