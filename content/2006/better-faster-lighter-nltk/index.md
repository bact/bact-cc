---
title: "(Better, Faster,) Lighter NLTK"
date: "2006-01-03T07:12:00+07:00"
lastmod: "2011-05-22T12:09:30+07:00"
type: "post"
url: "/2006/better-faster-lighter-nltk/"
description: "NLTK-Lite is substantially simplified and streamlined version of NLTK (Natural Language Toolkit). NLTK is no longer supported. NLTK-Lite is a new collection of lightweight NLP modules designed for maximum simplicity and efficiency. NLTK-Lite only covers the simple variants of standard data structure"
categories: ["coling"]
tag: ["natural-language-processing", "nltk", "python"]
textlang: "en"
wpid: 1145
---
[NLTK-Lite](http://nltk.sourceforge.net/) is substantially simplified and streamlined version of NLTK (Natural Language Toolkit). ***NLTK is no longer supported.***

NLTK-Lite is a new collection of lightweight NLP modules designed for maximum simplicity and efficiency. NLTK-Lite only covers the simple variants of standard data structures and tasks. Simplicity and efficiency are valued over generality and extensibility.

Key differences from NLTK:

- requires Python 2.4
- tokens are represented as strings, tuples, or trees
- all tokenizers are iterators; large tasks produce output as early as possible
- more emphasis on Python constructs instead of NLTK constructs
- default pipeline processing paradigm leads to more transparent code
- taggers incorporate backoff for smaller models and faster operation
- shorter names (e.g. tokenizer.RegexpTokenizer() becomes tokenize.regexp())
- tutorials are more easily maintained now with docutils and doctest
- contributed software is more easily incorporated

unrelated: [Better, Faster, Lighter Java](http://www.oreilly.com/catalog/bfljava/)
