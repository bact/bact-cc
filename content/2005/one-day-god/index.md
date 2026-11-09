---
title: "One-day God"
date: "2005-06-08T05:03:00+07:00"
lastmod: "2005-06-08T05:03:00+07:00"
type: "post"
url: "/2005/one-day-god/"
description: "Just created one Planet today. Genesis. To set it up vanilla running is not very difficult. However, not that straight forward. Basically, you modify the configuration file config.ini, upload all files to the server, add planet.py entry to cron job. And that should be all finished. But there’s a pit"
tag: ["siit"]
textlang: "en"
wpid: 795
---
Just created one [Planet](http://www.planetplanet.org/) today. Genesis.

To set it up vanilla running is not very difficult. However, not that straight forward.

Basically, you modify the configuration file `config.ini`, upload all files to the server, add `planet.py` entry to cron job. And that should be all finished.

But there’s a pitfall, it seems like the code is somewhat tied with a directory named `examples`. If you don’t want to run into a problem, you must upload that directory to your server as well – retaining its original name, unless the script will terminated in the middle of the air, reporting “IOError” something (like *examples/rss20.xml.tmpl not found*).

I don’t want to upload things I won’t use. So I tried the (silly, stupid, unnecessary) hard way.

I searched every source files, modified every lines that refer to (file in) that `examples` directory to the name of my own directory. Same error message, cannot read file in `examples` directory. (Hey! where you come from!!?)

The only way I can make it goes without problem is by removing everything but *index.html.tmpl* in *template_files* variable in `config.ini` file.

Don’t want to bother about it anymore at the moment. At least it [works](http://planet.siit.net/ "Planet SIIT") (for now).

Does God(s) creates our Earth with stylesheet ?
