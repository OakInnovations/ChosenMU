"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
from commands.default_cmdsets import CharGenCmdSet


class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """
    pass

    #def return_appearance(self,looker):
        #pass

class CharGenRoom(Room):
    """
    This is only used by rooms in Character Generation.
    Please note that with the way that this is set up,
    somebody who knows what they're doing could theoretically
    completely create their character in the first room of
    CharGen and go 'home'.  This is WORKING AS INTENDED.  We
    don't want to penalize experienced players by making them
    wade through all of the explanations over and over.  The
    rooms themselves should be used as a tutorial to creating
    a character, and what the various statistics mean.
    """

    def at_object_creation(self):
        """
        Called only at the first creation.
        """
        self.cmdset.add(CharGenCmdSet, permanent=True)
