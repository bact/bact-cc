---
title: "WordPress authentication plugin for DokuWiki (updated)"
date: "2008-04-04T16:19:00+07:00"
lastmod: "2008-04-04T16:19:00+07:00"
type: "post"
url: "/2008/wordpress-authentication-plugin-for-dokuwiki-updated/"
description: "dw-wordpress-auth is an authentication plugin for DokuWiki. It let DokuWiki uses WordPress authentication instead of its own. This brings more integration in your DW+WP site. This 1.2.3 version (2008-04-04) works with DokuWiki rc2008-03-31 and WordPress 2.5 Made for Creative Commons Thailand wiki. d"
tag: ["dokuwiki", "free-softwares", "me", "open-source", "programming", "wordpress"]
textlang: "en"
wpid: 2315
---
***dw-wordpress-auth*** is an authentication plugin for [DokuWiki](http://www.splitbrain.org/projects/dokuwiki).  
It let DokuWiki uses [WordPress](http://wordpress.org/) authentication instead of its own. This brings more integration in your DW+WP site.

This 1.2.3 version (2008-04-04) works with **DokuWiki rc2008-03-31** and **WordPress 2.5**

Made for [Creative Commons Thailand wiki](http://cc.in.th/wiki/).

***dw-wordpress-auth*** เป็นปลั๊กอินระบบล็อกอินของ [DokuWiki](http://www.splitbrain.org/projects/dokuwiki) โดยมันจะทำให้ DokuWiki ใช้ระบบล็อกอินของ [WordPress](http://wordpress.org/) แทน ทำให้ระบบล็อกอินเป็นอันหนึ่งอันเดียวกันมากขึ้น สำหรับเว็บไซต์ที่ใช้ DokuWiki และ WordPress

รุ่น 1.2.3 (4 เม.ย. 2550) นี้ สำหรับใช้กับ **DokuWiki rc2008-03-31** และ **WordPress 2.5**

ทำสำหรับใช้กับ [วิกิครีเอทีฟคอมมอนส์ไทย](http://cc.in.th/wiki/)

Download/ดาวน์โหลด: [dw-wordpress-auth-1.2.3.tgz](http://arthit.googlepages.com/dw-wordpress-auth-1.2.3.tgz)

For other versions/รุ่นอื่น ๆ: <http://arthit.googlepages.com/bazaar>

------------------------------------------------------------------------

#### Version History

##### 1.2.3 (04/04/2008)

- Fix magic quotes double-kill bug, by checking MAGIC_QUOTES_STRIPPED flag.  
  Code by Jan Wessely <http://jawe.net/files/dokuwiki_wordpress/wordpress.class.phps>
- Modify DW’s `html_login()` in inc/html.php to make DW’s login form  
  send login data to WP’s wp-login.php instead (modified html.php is included,  
  copy it to inc/).  
  If you want the original form back, just remove the code block  
  between “START dw-wordpress-auth plugin” and “END dw-wordpress-auth plugin”.  
  Then uncommented the following original code block.

##### 1.2.2 (03/04/2008)

- Modified to make it works with WP 2.5 and DW rc2008-03-31.
- Updated code to use WP’s `get_currentuserinfo()`, instead of deprecated `wp_get_cookie_login()`, as suggested by Jan Wessely <http://jawe.net/2008/04/01/wordpress-upgrade/>
- Modify DW’s default template’s main.php to make its login button  
  points to WP’s login screen instead (modified main.php is included,  
  copy it to lib/tpl/default/).  
  If you want the original login button back, just remove the code block  
  between “START dw-wordpress-auth plugin” and “END dw-wordpress-auth plugin”.  
  Then uncommented the original code line:  
  `tpl_button('login')`

##### 1.2.1 (06/11/2007)

- Modified to make it works with WP 2.3.0 and DW 2007-06-26b.
- Update code to use WP’s `do_action_ref_array`, instead of `do_action`.
- Swap the order to of user logged in status checking.  
  Check for WP’s cookie first, then check for DW’s login form.  
  Also if the WP’s cookie is ok, don’t bother checking for DW’s login.
- Remove RoleID from ‘addUser’ query (don’t know it was for, but it  
  doesn’t match the number of values to be inserted)
- Disabled unrecommended queries related to add/updateUser,  
  DW will handle this smartly by hidding related buttons  
  from its web interface as well (cool).

##### 1.2 (10/10/2006)

- Original version made by Mark Cunningham. For more info, see <http://thedeadone.net/software/getting-dokuwiki-to-use-wordpress-authentication/>.

------------------------------------------------------------------------

Any issue should be reported to *art \# siit.net*. Thank you 🙂

updated 2008.04.04 19:20 ICT:  
correct typo  
~~“use WP’s wp_get_cookie_login(), instead of get_currentuserinfo()”~~  
to “use WP’s get_currentuserinfo(), instead of deprecated wp_get_cookie_login()”.  
Thanks Jan Wessely 🙂

<span class="small">technorati tags:  
[DokuWiki](http://technorati.com/tag/DokuWiki),  
[WordPress](http://technorati.com/tag/WordPress),  
[authentication](http://technorati.com/tag/authentication),  
[plugin](http://technorati.com/tag/plugin)  
</span>
