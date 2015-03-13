# README #

Just a small project to learn python via D&D / Shadowrun dice rollers and character stat generators.

I don't even play these games!

### What is this repository for? ###

* Selfish history record so I can review the moments when I figured something out.
* People might want to see how a completely non-programmer actually learned to code, since it's hard to un-learn coding knowledge and therefore hard to teach it to other non-programmers because you lose perspective.

### How do I get set up? ###

* Just run any of the modules via python from within the directory.
* There is no configuration, but the chargen.py module needs the racestats.py module in the same directory, because I pushed a bunch of grunt functions to that supplementary module.

### Contribution guidelines ###

* This is my thing, fork if you want but don't tell me what to do. I'm learning it on my own.

### Who do I talk to? ###

* Go fuck yourself

Latest release notes:
-Collapsed big if-loops for choosing race into dict-derived strings, and moved all other functions called by that big ugly-ass if-block into the racestats module.
-Figured out how to pull a string from dict in chargen.py, wrap it in a string, then execute the full string that calls it as the specific racestats module!
-Also condensed the half-elf custom stat choices in a similar way, they can be seen in racestats.py
-Removed Eladrin, which is redundant with High Elves. Point of the module isn't to serve up a perfect user experience, just to provide workable stats.
-Added quit() function called from racestats library that gives a universal quit message "Don't let the door hit your ass!" for user-friendliness
-I think I may have added a bug where half-elves can double-add a stat... but I don't give a shit. They should be able to for all I care. The DM can rule on that