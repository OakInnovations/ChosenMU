# This...is...ChosenMU!

These are the world and development files for ChosenMU, an
Evennia-based MU* set in the BuffyVerse.

Well...eventually it will be.  The beautiful part about Evennia
is that it can be modified to anything necessary.  The bad part
about Evennia is...it *has* to be modified to whatever is necessary.

I actually like that part, though, so the bad parts aren't bad, as
far as I'm concerned.  Below is the original readme from the imported
Evennia world files.

# Welcome to Evennia!

This directory is your game directory, set up to let you start with
your new game right away.

You can delete this readme file when you've read it and you can
re-arrange things in this game-directory to suit your own sense of
organisation (the only exception is the directory structure of the
server/ directory, which Evennia expects). If you change the structure
you must however also edit/add to your settings file to tell Evennia
where to look for things.

Your game's main configuration file is found in
`server/conf/settings.py` (but you don't need to change it to get
started). If you just created this directory, `cd` to this directory
then initialize a new database using

    evennia migrate

To start the server, `cd` to this directory and run

    evennia -i start

This will start the server so that it logs output to the console. Make
sure to create a superuser when asked. By default you can now connect
to your new game using a MUD client on localhost:4000.  You can also
log into the web client by pointing a browser to
http://localhost:8000.

# Getting started

It's highly recommended that you look up Evennia's extensive
documentation found here: https://github.com/evennia/evennia/wiki.

Plenty of beginner's tutorials can be found here:
http://github.com/evennia/evennia/wiki/Tutorials.
