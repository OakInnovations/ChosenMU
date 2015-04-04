from commands.command import Command
from commands.command import MuxCommand

class WizCmdAddxp(MuxCommand):
    """
    This is a wizard command to add xp to a character.

    USAGE:
        +addxp [character] = [amount]
    """

    key = "+addxp"
    locks = "cmd:perm(Wizard)"
    help_category = "Admin"

    def func(self):
        caller = self.caller
        _errormsg_ = "{y+addxp {cUSAGE:{w  +addxp <character> = <amount>{n"

        #ERROR TRAPPING
        if not self.args:            
            caller.msg(_errormsg_)
            return
        elif not self.rhs:
            caller.msg(_errormsg_)
            return
        elif not self.lhs:
            caller.msg(_errormsg_)
            return
        
        target = caller.search(self.lhs)
        xpgiven = int(self.rhs)
        #DEBUGGING
        caller.msg("##### DEBUG TEXT #####")
        caller.msg("Add XP Called")
        caller.msg("Arguments: ")
        for i in self.arglist:
            caller.msg("    : " + i)
        caller.msg("Target: " + target.key)        
        caller.msg("Has experience attribute?  " + str(target.attributes.has("experience")))
        caller.msg("Value of experience attribute:")
        caller.msg(target.db.experience["current"])
        caller.msg("***** END DEBUG TEXT *****")
        #/DEBUGGING
        
        target.msg(caller.key + " has given you " + str(xpgiven) + " experience points!")
        caller.msg("Granted " + str(xpgiven) + " xp to " + target.key)
        target.db.experience["current"] += xpgiven
  
        
class WizCmdCheckAtts(MuxCommand):
    """
    This command will return all set attributes on an object.
    
    Please note that this is a debugging command, and will either be
    removed or prettied up in the future.  Right now, it is really,
    REALLY rough.  Deal with it.
    """

    key = "checkatts"
    aliases = ["checkatt", "chkatt", "chka"]
    locks = "cmd:perm(Wizard)"
    help_category = "Admin"

    def func(self):
        caller = self.caller
        _errormsg_ = "{ycheckatts {cUSAGE{n: checkatts <character>"

        if not self.args:
            caller.msg(_errormsg_)
            return

        char_checked = caller.search(self.args)
        caller.msg(char_checked.attributes.all())

class WizHurtChar(MuxCommand):
    """
    THIS COMMAND IS PRIMARILY FOR TESTING PURPOSES!

    This will allow you to administratively "hurt" a character.

    USAGE:  +hurt <character> = <amount>
    """
    key = "+hurt"
    locks = "cmd:perm(Wizard)"
    help_category = "wizard"

    def func(self):
        caller = self.caller
        _errormsg_ = "Invalid syntax.  {cUSAGE{n:  +hurt <character> = <amount hurt>"

        if not self.lhs:
            caller.msg(_errormsg_)
            return
        if not self.rhs:
            caller.msg(_errormsg_)
            return

        target_char = caller.search(self.lhs)
        target_amt = self.rhs

        target_char.db.curhp = int(target_char.db.curhp) - int(target_amt)
