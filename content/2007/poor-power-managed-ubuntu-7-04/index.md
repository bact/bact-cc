---
title: "Poor power-managed Ubuntu 7.04"
date: "2007-05-17T15:57:00+07:00"
lastmod: "2007-05-17T15:57:00+07:00"
type: "post"
url: "/2007/poor-power-managed-ubuntu-7-04/"
description: "Two days ago, I still can running Windows XP SP2 for 6 hours on my laptop battery. Today, it seems to last only 3.5 hours on Ubuntu 7.04. Obviously, something wrong with its power management. Ubuntu users have spotted this. It looks like the “CPU scaling” (powernowd) is not turned on by default in U"
tag: ["linux", "moving", "ubuntu"]
textlang: "en"
wpid: 2087
---
Two days ago, I still can running Windows XP SP2 for 6 hours on my laptop battery.  
Today, it seems to last only 3.5 hours on Ubuntu 7.04.

Obviously, something wrong with its power management. Ubuntu users have [spotted this](http://ubuntuforums.org/showthread.php?p=2654880).

It looks like the “CPU scaling” (powernowd) is not turned on by default in Ubuntu.  
And this [Bug \#14837](https://bugs.launchpad.net/ubuntu/+source/powernowd/+bug/14837 "powernowd should allow different settings for ac/batter modes") shows that even it turned on, the profile is fixed — it can’t automatically be changed accordingly to the source of power (i.e. use Profile A for battery, and B when plugged.)

Someone has set a bounty for [“Better Batter Life in Ubuntu”](https://launchpad.net/bounties/edal) since last year. And the issue has been [raised into the Blueprint](https://launchpad.net/ubuntu/+spec/reduced-power-usage) as well (proposed for [Gusty](https://launchpad.net/ubuntu/gutsy), next release of Ubuntu). Areas of improvements are ranging from hard disk access, cpu scaling, wireless lan mode, deactivation of unused devices.

For now, I need to know a way to, when I’m on battery, turn off my cd-rom drive and reduce my cpu speed. I’m using Sony VAIO PCG-V505CP. Anyone ? 🙂

(And now I exactly know why there are only download flavours of Ubuntu — Desktop and Server — as Laptop is not yet welcome here :P)

<span class="small">technorati tags:  
[Ubuntu](http://technorati.com/tag/Ubuntu),  
[power management](http://technorati.com/tag/power_management)  
</span>
