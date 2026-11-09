---
title: "Ruby NLP"
date: "2005-12-22T04:47:00+07:00"
lastmod: "2005-12-22T04:47:00+07:00"
type: "post"
url: "/2005/ruby-nlp/"
description: "NLP softwares in Ruby (old link) Ruby Linguistics Framework WordNet for Ruby Ruby on AI ตัว Ruby Linguistics นี่น่าสนใจ ตรงวิธีการใช้ .. คือมัน รูบี๊ รูบี้ น่ะ ตัวอย่าง: “box”.en.plural #=> “boxes” “mouse”.en.plural #=> “mice” “ruby”.en.plural #=> “rubies” “book”.en.a #=> “a book” “article”.en.a #=>"
tag: ["natural-language-processing", "ruby", "wordnet"]
textlang: "en"
wpid: 1130
---
- [NLP softwares in Ruby](http://www2.nict.go.jp/x/x161/members/mutiyama/software.html) <span class="small">([old link](http://www2.nict.go.jp/jt/a132/members/mutiyama/software.html))</span>
- [Ruby Linguistics Framework](http://www.deveiate.org/projects/Linguistics/)
- [WordNet for Ruby](http://www.deveiate.org/projects/Ruby-WordNet/)
- [Ruby on AI](http://web.media.mit.edu/~dustin/rubyai.html)

ตัว Ruby Linguistics นี่น่าสนใจ ตรงวิธีการใช้ .. คือมัน รูบี๊ รูบี้ น่ะ

ตัวอย่าง:

    "box".en.plural    #=> "boxes"
    "mouse".en.plural  #=> "mice"
    "ruby".en.plural   #=> "rubies"

    "book".en.a      #=> "a book"
    "article".en.a   #=> "an article"

    "runs".en.present_participle    #=> "running"
    "eats".en.present_participle    #=> "eating"
    "spies".en.present_participle   #=> "spying"

    "leaving".en.infinitive         #=> "leave"
    "left".en.infinitive            #=> "leave"
    "leaving".en.infinitive.suffix  #=> "ing"

    "cow".en.quantify( 5 )     #=> "several cows"
    "cow".en.quantify( 1005 )  #=> "thousands of cows"

อะไรทำนองนี้

**update:** (2007.04.02) update “NLP softwares in Ruby” link
