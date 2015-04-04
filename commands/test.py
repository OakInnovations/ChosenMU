from commands.command import Command
from commands.command import MuxCommand
from evennia.utils import search
from evennia.utils import create
from evennia.server.sessionhandler import SESSION_HANDLER

class TestCheck(Command):
    """description of class"""
    key = "+test"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller

        caller.msg("This is a successful test.")

class TestSetStat(MuxCommand):
    """
    Basic test of attribute structure, utilizing .ndb.
    This is the setup command
    """

    key = "+testset"
    locks = "cmd:perm(Wizard)"

    def func(self):
        caller = self.caller

        caller.ndb.testabils = {"ritual magic":
                                {"affects level": .5,
                                 "basic":
                                 {"level": 0,
                                  "points": 0,
                                  "powers":
                                  {"minor boost": 0,
                                   "minor shield": 0,
                                   "sunvisor": 0
                                   }
                                  },
                                 "normal":
                                 {"level": 0,
                                  "points": 0,
                                  "powers":
                                  {"boost": 0,
                                   "shield": 0,
                                   "sunshade": 0
                                   }
                                  }
                                 },
                                 "elemental magic":
                                 {"affects level": 1,
                                  "basic":
                                  {"level": 0,
                                   "points": 0,
                                   "powers":
                                   {"flame dart": 0,
                                    "dazzle": 0
                                    }
                                   }
                                  }
                                 }
        caller.ndb.testatts = {"str": 1, "dex": 1, "con": 1, "int": 1, "wis": 1, "cha": 1}
        caller.ndb.testskills = {"melee weapons": 0, "martial arts": 0, "brawling": 0}
        caller.ndb.testknowledges = {"demonic lore": 0, "magical theory": 0, "history": 0}

class TestGetStat(MuxCommand):
    """
    Test command to retrieve information from the test stat previously written
    Usage:
    testtrain <attribute>
    testtrain <skill>
    testtrain <knowledge>
    testtrain <ability>
    testtrain <ability> = <power>
    """

    key = "testtrain"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller
        arg1 = self.lhs
        arg2 = self.rhs

        if arg2:
            caller.msg("Looking for a power")
            for val in caller.ndb.testabils:
                if arg1 == val:
                    caller.msg("Found " + arg1)
                    for i in eval("caller.ndb.testabils['" + arg1 + "']['basic']['powers']"):
                        if arg2 == i:
                            caller.msg("Found " + arg2 + " in " + arg1)
                            break
                    else:
                        caller.msg(arg2 + " is not in " + arg1 + " - Basic")
                    for i in eval("caller.ndb.testabils['" + arg1 + "']['normal']['powers']"):
                        if arg2 == i:
                            caller.msg("Found " + arg2 + " in " + arg1)
                            break
                    else:
                        caller.msg(arg2 + " is not in " + arg1 + " - Normal")
                else:
                    caller.msg("Not in " + val)

        else:
            caller.msg("Not looking for a power.")
            for val in caller.ndb.testabils:
                if arg1 == val:
                    caller.msg("Found " + arg1 + " in abilities")
                    break
            else:
                caller.msg("Not in abilities")
            for val in caller.ndb.testatts:
                if arg1 == val:
                    caller.msg("Found " + arg1 + " in attributes")
                    break
            else:
                caller.msg("Not in attributes")
            for val in caller.ndb.testskills:
                if arg1 == val:
                    caller.msg("Found " + arg1 + " in skills")
                    break
            else:
                caller.msg("Not in skills.")
            for val in caller.ndb.testknowledges:
                if arg1 == val:
                    caller.msg("Found " + arg1 + " in knowledges")
                    break
            else:
                caller.msg("Not in knowledges")

class TestAllChars(MuxCommand):
    """
    A quick test to try and figure out how to search all characters in the db
    """
    key = "+allchars"
    locks = "cmds:all()"

    def func(self):
        caller = self.caller
        sessions = SESSION_HANDLER.get_sessions()
        caller.msg("All Sessions")
        caller.msg(sessions)
        caller.msg("Individual sessions:")
     
        for session in sessions:
            caller.msg("Session: " + str(session))
            if not session.logged_in: continue
            character = session.get_puppet()
            caller.msg(character)
            character.msg("This is a test")

class StartHeartbeat(MuxCommand):
    """
    try and start the damned heartbeat
    """
    key="+startheart"
    locks="cmds:all()"

    def func(self):
        caller = self.caller
        
        create.create_script("world.scripts.heartbeat.Heartbeat", report_to="#1", interval="10", persistent="true")