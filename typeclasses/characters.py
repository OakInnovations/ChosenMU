"""
Characters

Characters are (by default) Objects setup to be puppeted by Players.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter
from evennia import TICKER_HANDLER
from evennia.server.sessionhandler import SESSIONS
#from server.conf.oobfuncs import *
#from evennia.server.serversession import *

class Character(DefaultCharacter):
    """
    The Character defaults to implementing some of its hook methods with the
    following standard functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead)
    at_after_move - launches the "look" command
    at_post_puppet(player) -  when Player disconnects from the Character, we
                    store the current location, so the "unconnected" character
                    object does not need to stay on grid but can be given a
                    None-location while offline.
    at_pre_puppet - just before Player re-connects, retrieves the character's
                    old location and puts it back on the grid with a "charname
                    has connected" message echoed to the room

    """

        
    def at_object_creation(self):
        #set up hook for self-healing heartbeat
        TICKER_HANDLER.add(self,10,hook_key="health_ticker")
        #set up desc attributes
        self.db.eyes = "blank"
        self.db.hair = "no"
        self.db.height_feet = 6
        self.db.height_inches = 0
        self.db.weight = 0
        self.db.sex = "Male"
        #set up bodyparts available
        self.db.bodyparts = {"head":{
                                    "desc": "",
                                    "hp": 1,
                                    "weartype": ["hat","helmet"]
                                    },
                            "left arm":{
                                        "desc": "",
                                        "hp": 1,
                                        "weartype": [None]
                                        },
                            "left hand":{
                                        "desc": "",
                                        "hp": 1,
                                        "weartype": ["glove","ring","bracelet"]
                                        },
                            "right arm":{
                                        "desc": "",
                                        "hp": 1,
                                        "weartype": [None]
                                        },
                            "right hand":{
                                        "desc": "",
                                        "hp": 1,
                                        "weartype": ["glove","ring","bracelet"]
                                        },
                            "torso":{
                                    "desc": "",
                                    "hp": 5,
                                    "weartype": ["shirt", "jacket", "cloak", "armor"]
                                    },
                            "left leg":{
                                        "desc": "",
                                        "hp": 1,
                                        "weartype": ["pants"]
                                        },
                            "left foot":{
                                        "desc": "",
                                        "hp": 1,
                                        "weartype": ["boot"]
                                        },
                            "right leg":{
                                        "desc": "",
                                        "hp": 1,
                                        "weartype": ["pants"]
                                        },
                            "right foot":{
                                        "desc": "",
                                        "hp": 1,
                                        "weartype": ["boot"]
                                        }
                            }
        #set up basic character stats
        self.db.maxHP = 10
        self.db.maxSP = 0
        self.db.curHP = 10
        self.db.curSP = 0
        self.db.times_trained = 0
        self.db.level = 0
        self.db.regen_rate = 1
        self.db.sp_regen_rate = 1
        self.db.dodgerating = 1
        #Major, character-wide benefits.  Affects everything
        self.db.atts = {"str": 1, "dex": 1, "con": 1, "int": 1, "wis": 1, "cha": 1}
        #Major, long-term benefits to characters.  Wings.  Ritual-magic giving
        #until-logout buffs, etc.  Elemental magic that gives the ability to cast
        #spells at the drop of a hat.  Etc.  This has a more complicated setup
        #than the other attributes for the characters.  
        #Each attribute has an Affect Level multiplier that directly effects how
        #much this affects your level.  Typically, the numbers will be 0, .5, or 1,
        #though more complicated additions are possible in the code.  0 would mean that
        #that particular ability does not affect your level, no matter how much you put
        #in to it.  A good example of this would be gun modification.  Ritual Magic has a 
        #.5 multiplier, because while the effects of its various skills are powerful and
        #long-lasting, they can't be used directly in combat.  Elemental magic, on the other
        #hand, has a direct effect on combat through the many combative spells that it holds,
        #and so it has a multiplier of 1, and if it seems like not enough, I may even
        #decide to increase it to a level above 1, to 1.25 or even 1.5. Every attribute has 5
        #"levels" that in general describe how powerful the individual abilities
        #are underneath that level.  Each "level" has a ratiing, which directly gives
        #points to be spent in that level.  There will be some skill synergy
        #implemented where you get additional points in these levels based
        #on knowledge skills.  Underneath each level is a list of skills.  These
        #are increased with xp, but only up to the number of points that you have
        #to spend on that level.  Basically:
        # Ability
        # --Affect Level <multiplier>
        # --Basic
        # ----Basic Level: <number>
        # ----Basic Points: <number>
        # ----Skills
        # ------Skill #1: <number>
        # ------Skill #2: <number>
        # ------Skill #3: <number>
        # ------...etc
        # --Normal
        # --...etc

        self.db.abils = {
                "ritual magic":{
                        "affects level": .5,
                        "basic":{
                                "level": 0,
                                "points": 0,
                                "powers":{
                                        "minor boost": 0,
                                        "minor shield": 0,
                                        "sunvisor": 0
                                        }
                                },
                        "normal":{
                                "level": 0,
                                "points": 0,
                                "powers":{
                                        "boost": 0,
                                        "shield": 0,
                                        "sunshade": 0
                                        }
                                },
                        "intermediate":{
                                "level": 0,
                                "points": 0,
                                "powers": {
                                        }
                                },
                        "advanced":{
                                "level": 0,
                                "points": 0,
                                "powers":{
                                        }
                                },
                        "master":{
                                "level": 0,
                                "points": 0,
                                "powers":{
                                        }
                                }
                        },
                "elemental magic":{
                        "affects level": 1,
                        "basic":{
                                "level": 0,
                                "points": 0,
                                "powers": {
                                        "flame dart": 0,
                                        "dazzle": 0
                                        }
                                },
                        "normal":{
                                "level": 0,
                                "points": 0,
                                "powers":{
                                        }
                                },
                        "intermediate":{
                                "level": 0,
                                "points": 0,
                                "powers":{
                                        }
                                },
                        "advanced":{
                                "level": 0,
                                "points": 0,
                                "powers":{
                                        }
                                },
                        "master":{
                                "level": 0,
                                "points": 0,
                                "powers":{
                                        }
                                }
                        }
                }

        #The ability to do stuff.  Pick locks. Work with a computer.  Balance a checkbook.
        self.db.skills = {"programming": 0, 
                          "martial arts": 0, 
                          "melee": 0, 
                          "brawling": 0, }
        #The ability to know things.  History.  Magical theory.  Scientific theory.
        self.db.knowledges = {"computer science": 0, 
                              "magical theory": 0, 
                              "history": 0, 
                              "demonic lore": 0}
        #Current job is where you work.  Jobs db is a list of dictionaries, describing the
        #stats of each job that you have held.  Couch potato is the default job, and pays
        #$100 per week.
        self.db.current_job = "Couch Potato"
        self.db.jobs = [{"job_title": "Couch Potato", 
                         "payscale": 100.00, 
                         "job_level": 1, 
                         "job_xp": 0}]
        #How much experience you have, and how much you have spent.  Total xp is calculate at runtime
        self.db.experience = {"current": 0, "spent": 0}

    def health_ticker(self, *args, **kwargs):
        #self.msg("Ba-bump...heartbeat") #test code.  Shows this is getting called.  Gets annoying REAL quick.
        if self.db.curhp < self.db.maxhp:
            if (self.db.maxhp - self.db.curhp) < self.db.regen_rate:
                self.db.curhp = self.db.maxhp
            else:
                self.db.curhp += self.db.regen_rate
        if self.db.cursp < self.db.maxsp:
            if (self.db.maxsp - self.db.cursp) < self.db.sp_regen_rate:
                self.db.cursp = self.db.maxsp
            else:
                self.db.cursp += self.db.sp_regen_rate
    def at_tick(self, *args, **kwargs):
        #trying to keep a " 'Character' object has no attribute 'at_tick' " error from happening.
        pass
	
    def return_appearance(self,looker):
        """
        This formats a description. It is the hook a 'look' command
        should call.

        Args:
            looker (Object): Object doing the looking.
        """
        if not looker:
            return

        # get description, build string
        mxpstr = "{lclook " + self.key + "|finger " + self.key + "|examine " + self.key + "{lt" + self.key + "{le"
        string = "{c%s{n\n" % mxpstr
                
        if self.db.sex.lower() == "male":
                pronoun = "he"
                ppronoun = "his"
                sex = "He is male."
        elif self.db.sex.lower() == "female":
                pronoun = "she"
                ppronoun = "her"
                sex = "She is female."
        else:
                pronoun = "it"
                ppronoun = "its"
                sex = "Its gender is not clear."
        
        eyes = pronoun.capitalize() + " has " + self.db.eyes + " eyes."
        hair = pronoun.capitalize() + " has " + self.db.hair + " hair."
        height = pronoun.capitalize() + " is " + str(self.db.height_feet) + " feet, " + str(self.db.height_inches) + " inches tall."
        weight = pronoun.capitalize() + " is roughly " + str(self.db.weight) + " pounds."
        """
        bodyparts = ""
        for part in self.db.bodyparts:
            if part['desc']:
                bodyparts += ppronoun.capitalize() + " " + key + " " + self.db.bodyparts[part]['desc'] + "\n"
        """
        
        desc = self.db.desc
        if eyes:
            string += "\n" + eyes
        if hair:
            string += "\n" + hair
        if height:
            string += "\n" + height
        if weight:
            string += "\n" + weight
        if desc:
            string += "\n\n%s" % desc
        string += "\n"

        return string
