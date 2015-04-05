"""
This file contains the commands used in CharGen rooms.
"""

from commands.command import Command
from commands.command import MuxCommand

class CG_SetHair(Command):
    """
    This command will set your character's hair style and color.
    You will see this appear automatically in your description when
    someone looks at you.

    It will be prepended with "He/She/It has " and have " hair."
    appended to it.

    {cUSAGE{n:  sethair {y<your hair description>{n

    This will give:
         He has {y<your hair description>{n hair.
    """
    key = "sethair"
    aliases = ["shair", "hair"]
    help_category = "Character Generation"
    
    def func(self):
        caller = self.caller
        _errormsg_ = "You have to give a description!"
        if not self.args:
            caller.msg(_errormsg_)
            return
        caller.db.hair = self.args.strip()
        caller.msg("You have set your hair string to: {c" + self.args + "{n")


class CG_SetEyes(Command):
    """
    This command will set your character's eye desription.
    You will see this appear automatically in your description when
    someone looks at you.

    It will be prepended with "He/She/It has " and have " eyes."
    appended to it.

    {cUSAGE{n:  seteyes {y<your eyes description>{n

    This will give:
         He has {y<your hair description>{n eyes.
    """

    key = "seteyes"
    aliases = ["seyes", "eyes"]
    help_category = "Character Generation"

    def func(self):
        caller = self.caller
        _errormsg_ = "You have to give a description!"
        if not self.args:
            caller.msg(_errormsg_)
            return
        caller.db.eyes = self.args.strip()
        caller.msg("You have set your eyes string to: {c" + self.args + "{n")

class CG_SetSex(Command):
    """
    This command will set your character's sex.
    This doesn't make all that much difference code-wise,
    but can make a lot of difference for RP.  It does
    control some occasional pronoun-usage, but honestly
    we try to avoid needing that.
    """

    key = "setsex"
    aliases = ["ssex", "sex"]
    help_category = "Character Generation"

    def func(self):
        caller = self.caller
        _errormsg_ = "You chose something invalid.  Sex set to 'UNKNOWN'"
        if self.args == "":
            caller.db.sex = "UNKNOWN"
            caller.msg(_errormsg_)
            return

        args = self.args.lower().strip()
        #caller.msg("DEBUG!  args:.." + args + "..")

        if args == "male" or args == "m":
            caller.db.sex = "male"
        elif args == "female" or args == "f":
            caller.db.sex = "female"
        else:
            caller.db.sex = "other"

        caller.msg("You have set your sex to " + caller.db.sex)


class CG_SetHeight(MuxCommand):
    """
    This command sets your height in feet.

    {cUSAGE{n: setheight <"feet" or "inches"> = {y<feet or inches>{n

    For example, to make a character 6'3", you would enter:
       {ysetheight feet = 6{n
    and then...
       {ysetheight inches = 3{n
    """

    key = "setheight"
    aliases = ["sheight", "height"]
    help_category = "Character Generation"

    def func(self):
        caller = self.caller
        _errormsg_ = "You have to tell me how many tall you are!"
        _errusage_ = "{cUSAGE{n:  {ysetheight <'feet' or 'inches'> = <feet or inches>{n"
        _ooberrf_ = "You have to provide a height that is at least 4 feet, and no taller than 7 feet."
        _ooberri_ = "You have to provide a number of inches between 0 and 11...12 inches would be another foot!"
        if not self.args:
            caller.msg(_errormsg_)
            return
        if not self.rhs:
            caller.msg(_errusage_)
            return

        choice = self.lhs.lower()
        height = int(self.rhs.strip())

        if choice == "feet" or choice == "ft":
            if height < 4 or height > 7:
                caller.msg(_ooberrf_)
                return
            caller.db.height_feet = height
            caller.msg("You have set your height to " + str(caller.db.height_feet) + " feet.")
            caller.msg("This makes your height look like: " + str(caller.db.height_feet) + " feet, " + str(caller.db.height_inches) + " inches.")
        elif choice == "inches" or choice == "in":
            if height < 0 or height > 11:
                caller.msg(_ooberri_)
                return
            caller.db.height_inches = height
            caller.msg("You have set your height to " + str(caller.db.height_inches) + " inches.")
            caller.msg("This makes your height look like: " + str(caller.db.height_feet) + " feet, " + str(caller.db.height_inches) + " inches.")
        else:
            caller.msg(_errusage_)


class CG_SetWeight(Command):
    """
    This command sets your weight in pounds.

    {cUSAGE:  setweight {y<your weight>{n
    """

    key = "setweight"
    aliases = ["sweight", "weight"]
    help_category = "Character Generation"

    def func(self):
        caller = self.caller
        _errormsg_ = "You have to provide a weight!"
        _ooberr_ = "You have to provide a weight between 50 and 500"
        if not self.args:
            caller.msg(_errormsg_)
            return
        if int(self.args.strip()) > 500 or int(self.args.strip()) < 50:
            caller.msg(_ooberr_)
            return
        caller.db.weight = int(self.args.strip())
        caller.msg("You have set your weight to: " + str(caller.db.weight))
