mtg-deckbuilder
===============

mtg deckbuilder


To install, required: python 2.x, latest PyQt4, postgresql 9.3, simplejson. 

run python qt\mainwindow.py 

This will show you the basics.  A ui with a combobox/drop down box to view cards in a set.

Click a card to see info and rulings.


A mjor work in progress to clean up and get the ui to be nicer.

Changes to db coming soon to add 'colors' to the cardinfo.

And not to display info with missing data.

Organize card display info.

comment code.

Simplify code to use only bits once. (example, db.py, getCards and getRulings can use the same code pieces)
