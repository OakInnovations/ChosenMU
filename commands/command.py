"""
Commands

Commands describe the input the player can do to the game.

"""

from evennia import Command as BaseCommand
from evennia import default_cmds


class Command(BaseCommand):
    """
    Inherit from this if you want to create your own
    command styles. Note that Evennia's default commands
    use MuxCommand instead (next in this module).

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    """
    # these need to be specified

    key = "MyCommand"
    aliases = ["mycmd", "myc"]
    locks = "cmd:all()"
    help_category = "General"

    # optional
    # auto_help = False      # uncomment to deactive auto-help for this command.
    # arg_regex = r"\s.*?|$" # optional regex detailing how the part after
                             # the cmdname must look to match this command.

    # (we don't implement hook method access() here, you don't need to
    #  modify that unless you want to change how the lock system works
    #  (in that case see evennia.commands.command.Command))

    def at_pre_cmd(self):
        """
        This hook is called before `self.parse()` on all commands.
        """
        pass

    def parse(self):
        """
        This method is called by the `cmdhandler` once the command name
        has been identified. It creates a new set of member variables
        that can be later accessed from `self.func()` (see below).

        The following variables are available to us:
           # class variables:

           self.key - the name of this command ('mycommand')
           self.aliases - the aliases of this cmd ('mycmd','myc')
           self.locks - lock string for this command ("cmd:all()")
           self.help_category - overall category of command ("General")

           # added at run-time by `cmdhandler`:

           self.caller - the object calling this command
           self.cmdstring - the actual command name used to call this
                            (this allows you to know which alias was used,
                             for example)
           self.args - the raw input; everything following `self.cmdstring`.
           self.cmdset - the `cmdset` from which this command was picked. Not
                         often used (useful for commands like `help` or to
                         list all available commands etc).
           self.obj - the object on which this command was defined. It is often
                         the same as `self.caller`.
        """
        pass

    def func(self):
        """
        This is the hook function that actually does all the work. It is called
        by the `cmdhandler` right after `self.parser()` finishes, and so has access
        to all the variables defined therein.
        """
        self.caller.msg("Command called!")

    def at_post_cmd(self):
        """
        This hook is called after `self.func()`.
        """
        pass


class MuxCommand(default_cmds.MuxCommand):
    """
    This sets up the basis for Evennia's 'MUX-like' command style.
    The idea is that most other Mux-related commands should
    just inherit from this and don't have to implement parsing of
    their own unless they do something particularly advanced.

    A MUXCommand command understands the following possible syntax:

        name[ with several words][/switch[/switch..]] arg1[,arg2,...] [[=|,] arg[,..]]

    The `name[ with several words]` part is already dealt with by the
    `cmdhandler` at this point, and stored in `self.cmdname`. The rest is stored
    in `self.args`.

    The MuxCommand parser breaks `self.args` into its constituents and stores them
    in the following variables:
        self.switches = optional list of /switches (without the /).
        self.raw = This is the raw argument input, including switches.
        self.args = This is re-defined to be everything *except* the switches.
        self.lhs = Everything to the left of `=` (lhs:'left-hand side'). If
                     no `=` is found, this is identical to `self.args`.
        self.rhs: Everything to the right of `=` (rhs:'right-hand side').
                    If no `=` is found, this is `None`.
        self.lhslist - `self.lhs` split into a list by comma.
        self.rhslist - list of `self.rhs` split into a list by comma.
        self.arglist = list of space-separated args (including `=` if it exists).

    All args and list members are stripped of excess whitespace around the
    strings, but case is preserved.
    """

    def func(self):
        """
        This is the hook function that actually does all the work. It is called
        by the `cmdhandler` right after `self.parser()` finishes, and so has access
        to all the variables defined therein.
        """
        # this can be removed in your child class, it's just
        # printing the ingoing variables as a demo.
        super(MuxCommand, self).func()

class CmdStats(MuxCommand):
    """
    Test stats display
    """

    key = "stats"
    aliases = ["stat", "sco"]
    locks = "cmd:all()"
    help_category = "General"

    def func(self):
        if self.switches:
            self.showabils()
            return
        caller = self.caller
        caller.msg("=-=-=-=-=-=-=-=-=- (\o/) -=-=-=-=-=-=-=-=-=-=")
        caller.msg("Level " + str(int(caller.db.level)))
        caller.msg("Experience")
        caller.msg("--Available:  " + str(int(caller.db.experience['current'])))
        caller.msg("--Spent:      " + str(int(caller.db.experience['spent'])))
        caller.msg("--Total:      " + str(int(caller.db.experience['current'] + caller.db.experience['spent']))) 
        caller.msg("------------------ STATS --------------------")
        caller.msg(" Strength:     " + str(caller.db.atts['str']) + "    |  Intelligence: " + str(caller.db.atts['int']))
        caller.msg(" Dexterity:    " + str(caller.db.atts['dex']) + "    |  Wisdom:       " + str(caller.db.atts['wis']))
        caller.msg(" Constitution: " + str(caller.db.atts['con']) + "    |  Charisma:     " + str(caller.db.atts['cha']))
        caller.msg("------ SKILLS -------+----- KNOWLEDGES ------")
        caller.msg(" Brawling      " + str(caller.db.skills['brawling']) + "    |  Computer Science " + str(caller.db.knowledges['computer science']))
        caller.msg(" Martial Arts  " + str(caller.db.skills['martial arts']) + "    |  Demonic Lore     " + str(caller.db.knowledges['demonic lore']))
        caller.msg(" Melee         " + str(caller.db.skills['melee']) + "    |  History          " + str(caller.db.knowledges['history']))
        caller.msg(" Programming   " + str(caller.db.skills['programming']) + "    |  Magical Theory   " + str(caller.db.knowledges['magical theory']))
        
    def showabils(self):
        caller = self.caller

        caller.msg("---------------- ABILITIES ------------------")
        caller.msg(" Ritual Magic          Elemental Magic")
        caller.msg(" --Basic: " + str(caller.db.abils['ritual magic']['basic']['level']) + "            --Basic:   " + str(caller.db.abils['elemental magic']['basic']['level']))
        caller.msg(" ---Points: " + str(caller.db.abils['ritual magic']['basic']['points']) + "          ---Points: " + str(caller.db.abils['elemental magic']['basic']['points']))
        caller.msg(" ----Minor Boost:  " + str(caller.db.abils['ritual magic']['basic']['powers']['minor boost']) + "   ----Dazzle: " + str(caller.db.abils['elemental magic']['basic']['powers']['dazzle']))
        caller.msg(" ----Minor Shield: " + str(caller.db.abils['ritual magic']['basic']['powers']['minor shield']) + "   ----Flame Dart: " + str(caller.db.abils['elemental magic']['basic']['powers']['flame dart']))
        caller.msg(" ----Sunvisor:     " + str(caller.db.abils['ritual magic']['basic']['powers']['sunvisor']) + "   --Normal:  " + str(caller.db.abils['elemental magic']['normal']['level']))
        caller.msg(" --Normal: " + str(caller.db.abils['ritual magic']['basic']['level']) + "           ---Points: " + str(caller.db.abils['elemental magic']['normal']['points']))
        caller.msg(" ---Points: " + str(caller.db.abils['ritual magic']['normal']['points']) + "          --Intermediate:  " + str(caller.db.abils['elemental magic']['intermediate']['level']))
        caller.msg(" ----Boost:        " + str(caller.db.abils['ritual magic']['normal']['powers']['boost']) + "   ---Points:  " + str(caller.db.abils['elemental magic']['intermediate']['points']))
        caller.msg(" ----Shield:       " + str(caller.db.abils['ritual magic']['normal']['powers']['shield']) + "   --Advanced:  " + str(caller.db.abils['elemental magic']['advanced']['level']))
        caller.msg(" ----Sunshade:     " + str(caller.db.abils['ritual magic']['normal']['powers']['sunshade']) + "   ---Points:  " + str(caller.db.abils['elemental magic']['advanced']['points']))
        caller.msg(" --Intermediate:  " + str(caller.db.abils['ritual magic']['intermediate']['level']) + "    --Master:  " + str(caller.db.abils['elemental magic']['master']['level']))
        caller.msg(" ---Points:  " + str(caller.db.abils['ritual magic']['intermediate']['points']) + "         ---Points:  " + str(caller.db.abils['elemental magic']['master']['points']))
        caller.msg(" --Advanced:  " + str(caller.db.abils['ritual magic']['advanced']['level']))
        caller.msg(" ---Points:  " + str(caller.db.abils['ritual magic']['advanced']['points']))
        caller.msg(" --Master:  " + str(caller.db.abils['ritual magic']['master']['level']))
        caller.msg(" ---Points:  " + str(caller.db.abils['ritual magic']['master']['points']))
