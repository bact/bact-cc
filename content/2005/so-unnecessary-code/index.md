---
title: "so unnecessary code"
date: "2005-08-19T21:16:00+07:00"
lastmod: "2005-08-19T21:16:00+07:00"
type: "post"
url: "/2005/so-unnecessary-code/"
description: "I’m currently (busy) working with a web UI for one project. There’s nothing much complicated, just displaying a requested document in a web browser and provide a user a way to highlight some “interesting parts” of the document interactively. Something like underline all the words with a specified ca"
tag: ["javascript", "php", "programming"]
textlang: "en"
wpid: 969
---
I’m currently (busy) working with a web UI for one project.  
There’s nothing much complicated, just displaying a requested document in a web browser and provide a user a way to highlight some “interesting parts” of the document interactively.  
Something like underline all the words with a specified category, or mark a set of words that are related to each other, or hide away sentences that are not very important. No need to calculate anything, all the information are provided in a requested document (XML).

I chose a mix of PHP, XSLT, and JavaScript to do this.  
At the first place, I tried it with PHP and JavaScript with no XSLT.  
But don’t like the idea to convert XML to HTML by PHP (or whatever language) coding. I just feel that it’s not safe to do so, in terms of long-term maintenance.  
So I moved the conversion logic to XSLT, which is quite programming language neutral (depends on the availability of the XSL library).  
We may drop the use of PHP at some point, but the conversion is still there in the stylesheet, which can be used by many programming languages.

Hope that’s a right decision.

After using XSLT, I had realized that, in fact, with the XSLT library in JavaScript (like one from Google Code), I can do everything I need by JavaScript.  
Anyway, the library seems to be not very cross-browser.  
So I just let the PHP do XSLT, also other backoffice stuffs, and let the JavaScript do the user interaction stuffs. Which is, so far, quite nice.

The problem is, I’m not a JavaScript master. My JavaScript code is ‘workable’ but far from ‘elegant’.

After a while, I found myself in a middle of repeated pieces of code.  
Most of them are just a code to traverse around my DOM tree,  
and all of these traverse codes in every functions are actually using the same logic.

There should be a more elegant way to do this.

I think it should be possible to abstract these following components away from each other:

- traverse/looping
- test logic
- action to perform

something like:

(Note: the following code is just an idea, I’m pretty sure it’s not going to work.)


    function process(objects, loop, test, trueAction, falseAction) {
      loop (objects, function (object) {
          if (test(object)) {
            if (trueAction)
              trueAction(object);
          } else {
            if (falseAction)
              falseAction(object);
          }
        });
    }

    function traverseEveryNode(nodes, perfomer) {
      for (node in nodes) { // just an example, the actual DOM is tree
        performer(node);
      }
    }

and then you call:


    process(dom, traverseEveryNode, isNoun, markYellow, false);

to paint yellow to all nouns in the given document. Given there’re functions named *traverseEveryNode()*, *isNoun()*, and *markYellow()*.

How to do this in JavaScript ?

It seems like there’s something to do with a so-called **[“closure”](http://jibbering.com/faq/faq_notes/closures.html)**.  
But I still have no idea what it actually is at the moment — now reading.

If you have any clue, I’m very much appreciated to listen to 😉
