---
title: "REXML Nodes and Elements"
date: "2006-04-03T22:14:00+07:00"
lastmod: "2006-04-03T22:14:00+07:00"
type: "post"
url: "/2006/rexml-nodes-and-elements/"
description: "REXML, a Ruby-style XML toolkit What’s the difference between results from code (1) and (2) below ? (element is an XML element) Code (1), use Element#elements : element.elements.each do |e| puts e.inspect end Code (2), use Element#to_a : element.to_a.each do |e| puts e.inspect end Update: We can act"
tag: ["ruby", "xml"]
textlang: "en"
wpid: 1393
---
[REXML](http://www.germane-software.com/software/rexml/), a Ruby-style XML toolkit

What’s the difference between results from code (1) and (2) below ?  
(`element` is an XML element)

Code (1), use Element#elements :

    element.elements.each do |e|
     puts e.inspect
    end

Code (2), use Element#to_a :

    element.to_a.each do |e|
     puts e.inspect
    end

<span class="small">Update: We can actually use just `element.each` .. no `.to_a` requied — thanks to [P’Pok]() for this</span>

Code (2) will give us *texts*, *elements* (as well as other nodes).  
Where code (1) will give us only *elements*.

If our input is:

    <p><b>bold</b> text</p>

Code (1) will give:

    <b> ... </>

While code (2) will give:

    <b> ... </>
    " text"

This tiny difference already wasted me hours, shamed 🙁  
I was thought that *text* is a kind of *element*, … that’s plain wrong,  
both *text* and *element* are kinds of *node* !

For several REXML tutorials/examples I’ve found, where I copied and pasted codes from for my quick-n-dirty-self-education, all of them show only the use of Element#elements but not Element#to_a.

This is probably because all of them only deal with a data-oriented XML, where a use of [‘mix content’](http://www.itworld.com/nl/xml_prac/07112002/) is rare (and indeed not recommended).  
But that’s no longer true for document/text-oriented XML — for example, XHTML.

If you going to process a XML with mix content, beware of \#elements.

Correct me if I do anything wrong here.  
REXML veteran? Share! 😉

------------------------------------------------------------------------

Tutorials:  
[REXML Home](http://www.germane-software.com/software/rexml/docs/tutorial.html) \|  
[XML.com](http://www.xml.com/pub/a/2005/11/09/rexml-processing-xml-in-ruby.html) \|  
[developerWorks](http://www-128.ibm.com/developerworks/xml/library/x-matters18.html)  
[API docs](http://www.germane-software.com/software/XML/rexml/doc/)
