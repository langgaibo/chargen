# README #

### Latest Changes ###
Migrated to Python 3. Both Character Generator and D&D Simple Dice roller now can export character stats to both JSON and CSV formats. (Version 1.8)
Added option to save out as JSON from Chargen module. (Version 1.7)
Added basic CSV output functionality for rolled attributes. (version 1.6)

### About this repository ###
Just a small project to learn python via D&D / Shadowrun dice rollers and character stat generators.

I don't even play these games!

### What is this repository for? ###

* Selfish history record so I can review the moments when I figured something out.
* People might want to see how a completely non-programmer actually learned to code, since it's hard to un-learn coding knowledge and therefore hard to teach it to other non-programmers because you lose perspective.

### How do I get set up? ###

* Just run any of the modules via Python 3 from within the repo root directory, e.g. `$ python3 chargen.py`
* There is no configuration, but the chargen.py and dddice.py modules need the dice_lib.py module in the same directory, because I pushed a bunch of grunt functions to that supplementary module.

### Planned Features ###
* Locally hosted web GUI
* Character Sheet module for use in realtime play featuring:
    * HP, XP tracking and simple inventory
    * Import stats generated via the other modules
    * Export full character sheet to JSON
* Refactor all modules into class-based OOP architecture