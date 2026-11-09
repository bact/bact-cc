---
title: "Subversion permission problem ?"
date: "2005-11-10T20:45:00+07:00"
lastmod: "2005-11-10T20:45:00+07:00"
type: "post"
url: "/2005/subversion-permission-problem/"
description: "Got this ? svn: Unable to open an ra_local session to URL svn: Unable to open repository ‘file:///svnroot/project’ svn: Berkeley DB error while opening environment for filesystem /svnroot/db: Permission denied Just open a read/write access to the repository, esp the db directory … something like (bu"
tag: ["how-to", "subversion"]
textlang: "en"
wpid: 1057
---
Got this ?

    svn: Unable to open an ra_local session to URL 
    svn: Unable to open repository 'file:///svnroot/project' 
    svn: Berkeley DB error while opening environment for filesystem /svnroot/db: 
    Permission denied

Just open a read/write access to the repository, esp the `db` directory … something like (but more fine-grained than) `chmod -R g+w /svnroot`
