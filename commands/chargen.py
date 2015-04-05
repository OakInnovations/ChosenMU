"""
This file contains the commands used in CharGen rooms.
"""

from commands.command import Command

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
        caller.db.hair = self.args
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
        caller.db.eyes = self.args
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
        caller.msg("DEBUG!  args:.." + args + "..")

        if args == "male" or args == "m":
            caller.db.sex = "male"
        elif args == "female" or args == "f":
            caller.db.sex = "female"
        else:
            caller.db.sex = "other"

        caller.msg("You have set your sex to " + caller.db.sex)


class CG_SetHeight_Feet(Command):
    """
    This command sets your height in feet.

    {cUSAGE{n: setheight-feet {y<height in feet>{n
    """

    key = "setheight-feet"
    aliases = ["sheight-feet", "setfeet", "sheightf", "feet"]
    help_category = "Character Generation"

    def func(self):
        caller = self.caller
        _errormsg_ = "You have to tell me how many feet tall you are!"
        _ooberr_ = "You have to provide a height that is at least 4 feet, and no taller than 7 feet."
        if not self.args:
            caller.msg(_errormsg_)
            return
        if self.args < 4 or self.args > 7:
            caller.msg(_ooberr_)
            return
        caller.db.height_feet = self.args
        caller.msg("You have set your height in feet to: " + caller.db.height_feet)

class CG_SetHeight_Inches(Command):
    """
    This command sets your height in inches.

    {cUSAGE{n:  setheight-inches {y<height in inches>{n
    """

    key = "setheight-inches"
    aliases = ["sheight-inches", "setinches", "sheighti", "inches"]
    help_category = "Character Generation"

    def func(self):
        caller = self.caller
        _errormsg_ = "You have to tell me how many inches tall you are!"
        _ooberr_ = "You have to provide a number of inches from 0 to 11.  (12 inches would be another foot, after all)"
        if not self.args:
            caller.msg(_errormsg_)
            return
        if self.args < 0 or self.args > 11:
            caller.msg(_ooberr_)
            return
        caller.db.height_inches = self.args
        caller.msg("You have set your height in inches to: " + caller.db.height_inches)

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
        if self.args > 500 or self.args < 50:
            caller.msg(_ooberr_)
            return
        caller.db.weight = self.args
        caller.msg("You have set your weight to: " + caller.db.weight)
