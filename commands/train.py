from commands.command import MuxCommand
from typeclasses.characters import Character

"""
class CmdTrain(MuxCommand):
    
    
   
    This is the train command, which you will use to upgrade
    your character, using your experience points.

    {cUSAGE:{n
        {ytrain [/check] <item to train> [= <sub ability> or <level>]{n

        Flags:
            {c/check{n:  Check the cost without spending xp

        Sub ability or level:
            This is only necessary when you are training an ability.
            Sub ability would be the specific power that you want to
            gain, and level would be for putting points directly into
            an ability level, such as Ritual Magic: Basic.

    Your train costs will go up based on the current value of the
    item that you are trying to train, your level, and your "tier",
    which is also based on your level.  You will gain a level for every
    10 trains, in general.  Some abilities do not count as much towards
    levelling, and knowledge skills do not count against your level at all,
    as your level is essentially representative of your basic combat skills.
    Each tier represents a fairly major jump in the amount of experience that
    you will have to spend to train anything.  The current tiers are:
        {cTiers 1 - 5{y   -   Every 20 levels{n
        {cTiers 5 - 10{y  -   Every 10 levels{n
        {cTiers 10 - 15{y -   Every 5 levels{n
        {cTiers 16+{y     -   Every level thereafter{n
    As you can see, at level 1, you are at tier 1, and so training is cheap.  At
    level 100, you've only hit tier 5, so training isn't so bad. At level
    150 you've hit tier 10, so training is much harder, whearas anything past
    level 175 will see a major jump for every level that you increase.
   
    key = "train"
    aliases = "tra"
    locks = "cmd:all()"
    help_category = "Character"

    def func(self):

        caller = self.caller
        _errormsg_ = "{cUSAGE: {ytrain [/check] <item to train> [= <sub ability> or <level>]{n"
        arg1 = self.lhs.lower()
        if self.rhs:
            arg2 = self.rhs.lower()
        else:
            arg2 = None
        found = False

        arg1 = self.det_attribute(arg1)
        if arg1 == "badatt":
            arg1 = self.lhs.lower()


        #check to make sure that there is something to train!
        if arg1 == False:
            caller.msg("You have to tell me what you want to train!")
            caller.msg(_errormsg_)
            return

        if arg2:
            if arg2 == "basic":
                for i in caller.db.abils:
                    if found == True:
                        break
                    if i == arg1:
                        tcode = "abils['" + arg1 + "']['basic']['level']"
                        basecode = "caller.db.abils['" + arg1 + "']['basic']"
                        ttype = "abi-b"
                        tname = arg1.capitalize() + " - Basic"
                        afflevel = eval("caller.db.abils['" + arg1 + "']['affects level']")
                        found = True
                        break          
            elif arg2 == "normal":
                for i in caller.db.abils:
                    if found == True:
                        break
                    if i == arg1:
                        tcode = "abils['" + arg1 + "']['normal']['level']"
                        basecode = "caller.db.abils['" + arg1 + "']['normal']"
                        ttype = "abi-n"
                        tname = arg1.capitalize() + " - Normal"
                        afflevel = eval("caller.db.abils['" + arg1 + "']['affects level']")
                        found = True
                        break
            elif arg2 == "intermediate":
                for i in caller.db.abils:
                    if found == True:
                        break
                    if i == arg1:
                        tcode = "abils['" + arg1 + "']['intermediate']['level']"
                        basecode = "caller.db.abils['" + arg1 + "']['intermediate']"
                        ttype = "abi-i"
                        tname = arg1.capitalize() + " - Intermediate"
                        afflevel = eval("caller.db.abils['" + arg1 + "']['affects level']")
                        found = True
                        break
            elif arg2 == "advanced":
                for i in caller.db.abils:
                    if found == True:
                        break
                    if i == arg1:
                        tcode = "abils['" + arg1 + "']['advanced']['level']"
                        basecode = "caller.db.abils['" + arg1 + "']['advanced']"
                        ttype = "abi-a"
                        tname = arg1.capitalize() + " - Advanced"
                        afflevel = eval("caller.db.abils['" + arg1 + "']['affects level']")
                        found = True
                        break
            elif arg2 == "master":
                for i in caller.db.abils:
                    if found == True:
                        break
                    if i == arg1:
                        tcode = "abils['" + arg1 + "']['master']['level']"
                        basecode = "caller.db.abils['" + arg1 + "']['master']"
                        ttype = "abi-m"
                        tname = arg1.capitalize() + " - Master"
                        afflevel = eval("caller.db.abils['" + arg1 + "']['affects level']")
                        found = True
                        break
            for val in caller.db.abils:
                if found == True:
                    break
                if val == arg1:
                    #Check Basic powers
                    for i in eval("caller.db.abils['" + arg1 + "']['basic']['powers']"):
                        if i == arg2:
                            caller.msg("Found " + arg2)
                            tcode = "abils['" + arg1 + "']['basic']['powers']['" + arg2 + "']"
                            ttype = "abi-b-s"
                            basecode = "caller.db.abils['" + arg1 + "']['basic']"
                            tname = arg2.capitalize()
                            curpoints = eval("caller.db.abils['" + arg1 + "']['basic']['points']")
                            found = True
                            break
                    #Check Normal powers
                    for i in eval("caller.db.abils['" + arg1 + "']['normal']['powers']"):
                        if i == arg2:
                            caller.msg("Found " + arg2)
                            tcode = "abils['" + arg1 + "']['normal']['powers']['" + arg2 + "']"
                            ttype = "abi-n-s"
                            basecode = "caller.db.abils['" + arg1 + "']['normal']"
                            tname = arg2.capitalize()
                            curpoints = eval("caller.db.abils['" + arg1 + "']['normal']['points']")                            
                            found = True
                            break
                    #Check Intermediate powers
                    for i in eval("caller.db.abils['" + arg1 + "']['intermediate']['powers']"):
                        if i == arg2:
                            caller.msg("Found " + arg2)
                            tcode = "abils['" + arg1 + "']['intermediate']['powers']['" + arg2 + "']"
                            basecode = "caller.db.abils['" + arg1 + "']['intermediate']"
                            ttype = "abi-n-s"
                            tname = arg2.capitalize()
                            curpoints = eval("caller.db.abils['" + arg1 + "']['intermediate']['points']")
                            found = True
                            break
                    #Check Advanced powers
                    for i in eval("caller.db.abils['" + arg1 + "']['advanced']['powers']"):
                        if i == arg2:
                            caller.msg("Found " + arg2)
                            tcode = "abils['" + arg1 + "']['advanced']['powers']['" + arg2 + "']"
                            ttype = "abi-a-s"
                            basecode = "caller.db.abils['" + arg1 + "']['advanced']"
                            tname = arg2.capitalize
                            curpoints = eval("caller.db.abils['" + arg1 + "']['advanced']['points']")
                            found = True
                            break
                    #Check Master powers
                    for i in eval("caller.db.abils['" + arg1 + "']['master']['powers']"):
                        if i == arg2:
                            caller.msg("Found " + arg2)
                            tcode = "abils['" + arg1 + "']['master']['powers']['" + arg2 + "']"
                            basecode = "caller.db.abils['" + arg1 + "']['master']"
                            ttype = "abi-m-s"
                            tname = arg2.capitalize()
                            curpoints = eval("caller.db.abils['" + arg1 + "']['master']['points']")
                            found = True
                            break
        else:
            for val in caller.db.atts:
                if found == True:
                    break
                if val == arg1:
                    ttype = "att"
                    tcode = self.det_attribute(arg1, "code")
                    basecode = "atts"
                    tname = self.det_attribute(arg1, "name")
                    found = True
                    break
            for val in caller.db.skills:
                if found == True:
                    break
                if val == arg1:
                    ttype = "ski"
                    tcode = "skills['" + val + "']"
                    basecode = "skills"
                    tname = arg1.capitalize()
                    found = True
                    break
            for val in caller.db.knowledges:
                if found == True:
                    break
                if val == arg1:
                    ttype = "kno"
                    tcode = "knowledges['" + val + "']"
                    basecode = "knowledges"
                    tname = arg1.capitalize()
                    found = True
                    break
        
        if found == False:
            caller.msg("Couldn't find that to train.  Try again.")
            caller.msg(_errormsg_)
            return

        traincost = self.get_traincost(tcode,ttype)

        if "check" in self.switches:
            caller.msg("It will cost you " + str(traincost) + " experience to raise your " + tname + ".")
        else:
            if len(ttype) == 3:
                self.do_train(tcode,ttype,traincost,tname,0,1,basecode)
            elif len(ttype) > 3:
                self.do_train(tcode,ttype,traincost,tname,curpoints,afflevel,basecode)
            else:
                caller.msg("Something broke, report this bug!")
   
    def det_attribute(self,titem,rettype = "code"):
        caller = self.caller
        titem = titem.lower()

        if titem == "str" or titem == "strength":
            tcode = "str"
            if rettype == "name":
                tcode = "Strength"
        elif titem == "dex" or titem == "dexterity":
            tcode = "dex"
            if rettype == "name":
                tcode = "Dexterity"
        elif titem == "con" or titem == "constitution":
            tcode = "con"
            if rettype == "name":
                tcode = "Constitution"
        elif titem == "int" or titem == "intelligence":
            tcode = "int"
            if rettype == "name":
                tcode = "Intelligence"
        elif titem == "wis" or titem == "wisdom":
            tcode = "wis"
            if rettype == "name":
                tcode = "Wisdom"
        elif titem == "cha" or titem == "charisma":
            tcode = "cha"
            if rettype == "name":
                tcode = "Charisma"
        else:
            tcode = "badatt"

        return tcode

    def get_traincost(self, tcode, ttype):
        caller = self.caller
        

       
        Training Model Setup
        
        Tier Modifier = 100 * (Tier * Tier)

        Basic Model:
            ((Current Value + Previous Value) * Level Modifier) * Type Modifier) + Tier Modifier

        Attributes:
            Multiplier = 10

        Knowledges
            Multiplier = 1
        
        Skills
            Multiplier = 4
        
        Abilities
            Multiplier = 7

            Basic
                Ability Level Adjustment = + 100
            Normal
                Ability Level Adjustment = + 250
            Intermediate
                Ability Level Adjustment = + 500
            Advanced
                Ability Level Adjustment = + 1000
            Master
                Ability Level Adjustment = + 10000

            The Sub-ability modifier is 1.5, and the Ability Level adjustment
            is 1/10 the cost for the base ability skill
        
        charlevel = caller.db.level

        if charlevel == 0:
            tier = 0
        elif charlevel >= 1 and charlevel <= 20:
            tier = 1
        elif charlevel > 20 and charlevel <= 40:
            tier = 2
        elif charlevel > 40 and charlevel <= 60:
            tier = 3
        elif charlevel > 60 and charlevel <= 80:
            tier = 4
        elif charlevel > 80 and charlevel <= 100:
            tier = 5
        elif charlevel > 100 and charlevel <= 110:
            tier = 6
        elif charlevel > 110 and charlevel <= 120:
            tier = 7
        elif charlevel > 120 and charlevel <= 130:
            tier = 8
        elif charlevel > 130 and charlevel <= 140:
            tier = 9
        elif charlevel > 140 and charlevel <= 150:
            tier = 10
        elif charlevel > 150 and charlevel <= 155:
            tier = 11
        elif charlevel > 155 and charlevel <= 160:
            tier = 12
        elif charlevel > 160 and charlevel <= 165:
            tier = 13
        elif charlevel > 165 and charlevel <= 170:
            tier = 14
        elif charlevel > 170 and charlevel <= 175:
            tier = 15
        else:
            tier = 15 + (charlevel - 175)
        
        levelmod = 1.1 * charlevel
        abillevelmod = 0
        tiermod = 100 * (tier * tier)

        if ttype == "att":
            typemod = 10
        elif ttype == "kno":
            typemod = 1           
        elif ttype == "ski":
            typemod = 4
        elif ttype == "abi-b":
            typemod = 7
            abillevelmod = 100
        elif ttype == "abi-n":
            typemod = 7
            abillevelmod = 250
        elif ttype == "abi-i":
            typemod = 7
            abillevelmod = 500
        elif ttype == "abi-a":
            typemod = 7
            abillevelmod = 1000
        elif ttype == "abi-m":
            typemod = 7
            abillevelmod = 10000
        elif ttype == "abi-b-s":
            typemod = 1.5
            abillevelmod = 10
        elif ttype == "abi-n-s":
            typemod = 1.5
            abillevelmod = 25
        elif ttype == "abi-i-s":
            typemod = 1.5
            abillevelmod = 50
        elif ttype == "abi-a-s":
            typemod = 1.5
            abillevelmod = 100
        elif ttype == "abi-m-s":
            typemod = 1.5
            abillevelmod = 1000

        tcode = "caller.db." + tcode
        current_level = eval(tcode)

        previous_level = int(str(current_level)) - 1
        if previous_level < 1:
            previous_level = 1

        if levelmod < 1:
            levelmod = 1

        if current_level == 0:
            current_level = 1

        traincost = ((((current_level + previous_level) * levelmod) * typemod) + abillevelmod) + tiermod

        return traincost

    def do_train(self, tcode, ttype, traincost, tname, curpoints = 0, afflevel = 1, basecode = ""):
        caller = self.caller
        curexp = caller.db.experience["current"]
        curlevel = caller.db.level
        curtrain = eval("caller.db." + tcode)
        pointsneeded = 0

        #Check for sufficient experience!
        if curexp < traincost:
            caller.msg("You don't have enough experience to train!")
            return

        #If ttype is greater than 5, then it is a sub-ability
        if len(ttype) > 5:
            pointsneeded = self.calc_points(curtrain)
            if pointsneeded > curpoints:
                caller.msg("You have enough experience, but not enough points!")
                return
        if ttype == "kno":
            afflevel = 0

        #Do the actual training.
        caller.db.experience['current'] -= traincost
        caller.db.experience['spent'] += traincost
        caller.db.times_trained += afflevel
        caller.db.level = caller.db.times_trained / 10
        #traincode = tcode + " = " + str(curtrain + 1)
        #traincode = "caller.attributes.add(\"" + tcode + "\"," + str(curtrain + 1) + ")"
        caller.ndb.temp = eval("caller.db." + basecode)
        caller.ndb.temp[tcode] = curtrain+1
        caller.attributes.add(eval("caller.db." + basecode + caller.ndb.temp))
        #eval(traincode)
        #if len(ttype) > 5:
           # pointcode = basecode + "['points'] = " + str(curpoints - pointsneeded)
            #eval(basecode)

        caller.msg("You raised your {y" + tname + "{n to " + str(curtrain + 1) + "!  You have {y" + str(caller.db.experience['current']) + "{n experience left to spend.")


    def calc_points(self, curtrain):
        caller = self.caller

        caller.msg("Calculating point cost...")
        caller.msg("Current level: " + str(curtrain))

        for i in range(1, curtrain):
            pointsneeded += i

        caller.msg("Points Needed: " + str(pointsneeded))
"""

class CmdBasicTrain(MuxCommand):
    """
    This is the very basic, straightforward Train command.
    It is not intended as a permanent feature, but merely
    as a temporary solution until the more fully-featured
    train code is in place.  This one requires every new
    skill/ability/etc. to be manually added to the training
    code, whereas the eventual goal is to have a command that
    takes input, error checks it, and just works without
    having to change anything but the containing db structs.

    Usage:  +train [/check] <thingtotrain>

    The obvious advantage to this method is simple and fine-grained
    control of every aspect of training.
    """

    key = "+train"
    aliases = ['train']
    locks = "cmd:all()"

    def func(self):
        """
        Here's something fun.  Copy and paste the block between the
        hashtags below, and do the following find/replace routines 
        on it to quickly add a new whatever.
        XXXX = the long name (all lower-case) of whatever you want to train.
        YYYY = the short name (str for strength, for example)
        ZZZZ = the type:  att, ski, kno, abil[-b/n/i/a/m][-s]
        AAAA = the name on the character template for the attribute section:  atts, knowledges, abils, skills

        #########################################################################################

        if trainitem == "YYYY" or trainitem == "XXXX":
            tname = "XXXX"
            ttype = "ZZZZ"
            curlevel = caller.db.AAAA['YYYY']
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods(ttype, "abil")
            traincost = self.get_traincost(trainitem,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.AAAA['YYYY'] = curlevel + 1
            caller.db.times_trained = caller.db.times_trained + 1
            caller.db.level = caller.db.times_trained / 10
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")

        ##########################################################################################         
        """
        caller = self.caller
        if self.lhs:
            trainitem = self.lhs.lower()
        else:
            caller.msg("You have to give me something to train!")

        charlevel = caller.db.level

        #Attributes
#STR
        if trainitem == "str" or trainitem == "strength":
            tname = "strength"
            ttype = "att"
            curlevel = caller.db.atts['str']
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods(ttype, "abil")
            traincost = self.get_traincost(trainitem,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.atts['str'] = curlevel + 1
            caller.db.times_trained = caller.db.times_trained + 1
            caller.db.level = caller.db.times_trained / 10
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#DEX
        elif trainitem == "dex" or trainitem == "dexterity":
            tname = "dexterity"
            ttype = "att"
            curlevel = caller.db.atts['dex']
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods(ttype, "abil")
            traincost = self.get_traincost(trainitem,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.dodgerating += 2
            caller.db.atts['dex'] = curlevel + 1
            caller.db.times_trained = caller.db.times_trained + 1
            caller.db.level = caller.db.times_trained / 10
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#CON
        elif trainitem == "con" or trainitem == "constitution":
            tname = "constitution"
            ttype = "att"
            curlevel = caller.db.atts['con']
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods(ttype, "abil")
            traincost = self.get_traincost(trainitem,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.maxhp += 10
            caller.db.atts['con'] = curlevel + 1
            caller.db.times_trained = caller.db.times_trained + 1
            caller.db.level = caller.db.times_trained / 10
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#INT
        elif trainitem == "int" or trainitem == "intelligence":
            tname = "intelligence"
            ttype = "att"
            curlevel = caller.db.atts['int']
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods(ttype, "abil")
            traincost = self.get_traincost(trainitem,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.atts['int'] = curlevel + 1
            caller.db.maxsp += 10
            caller.db.times_trained = caller.db.times_trained + 1
            caller.db.level = caller.db.times_trained / 10
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#WIS
        elif trainitem == "wis" or trainitem == "wisdom":
            tname = "wisdom"
            ttype = "att"
            curlevel = caller.db.atts['wis']
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods(ttype, "abil")
            traincost = self.get_traincost(trainitem,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.maxsp += 10
            caller.db.atts['wis'] = curlevel + 1
            caller.db.times_trained = caller.db.times_trained + 1
            caller.db.level = caller.db.times_trained / 10
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#CHA
        elif trainitem == "cha" or trainitem == "charisma":
            tname = "charisma"
            ttype = "att"
            curlevel = caller.db.atts['cha']
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods(ttype, "abil")
            traincost = self.get_traincost(trainitem,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.atts['cha'] = curlevel + 1
            caller.db.times_trained = caller.db.times_trained + 1
            caller.db.level = caller.db.times_trained / 10
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")

#SKILLS
#Programming
        elif trainitem == "prog" or trainitem == "programming":
            tname = "programming"
            ttype = "ski"
            curlevel = caller.db.skills['programming']
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods(ttype, "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.skills['programming'] = curlevel + 1
            caller.db.times_trained = caller.db.times_trained + 1
            caller.db.level = caller.db.times_trained / 10
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#martial arts
        elif trainitem == "martial" or trainitem == "martial arts":
            tname = "martial arts"
            ttype = "ski"
            curlevel = caller.db.skills['martial arts']
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods(ttype, "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.skills['martial arts'] = curlevel + 1
            caller.db.times_trained = caller.db.times_trained + 1
            caller.db.level = caller.db.times_trained / 10
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#melee
        elif trainitem == "mel" or trainitem == "melee":
            tname = "melee"
            ttype = "ski"
            curlevel = caller.db.skills['melee']
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods(ttype, "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.skills['melee'] = curlevel + 1
            caller.db.times_trained = caller.db.times_trained + 1
            caller.db.level = caller.db.times_trained / 10
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#brawling
        elif trainitem == "brawl" or trainitem == "brawling":
            tname = "brawling"
            ttype = "ski"
            curlevel = caller.db.skills['brawling']
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods(ttype, "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.skills['brawling'] = curlevel + 1
            caller.db.times_trained = caller.db.times_trained + 1
            caller.db.level = caller.db.times_trained / 10
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")

#KNOWLEDGES
#computer science
        elif trainitem == "compsci" or trainitem == "computer science":
            tname = "computer science"
            ttype = "kno"
            curlevel = caller.db.knowledges['computer science']
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods(ttype, "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.knowledges['computer science'] = curlevel + 1
            caller.db.times_trained = caller.db.times_trained + 1
            caller.db.level = caller.db.times_trained / 10
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#history
        elif trainitem == "hist" or trainitem == "history":
            tname = "history"
            ttype = "kno"
            curlevel = caller.db.knowledges['history']
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods(ttype, "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.knowledges['history'] = curlevel + 1
            caller.db.times_trained = caller.db.times_trained + 1
            caller.db.level = caller.db.times_trained / 10
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#magical theory
        elif trainitem == "magthe" or trainitem == "magical theory":
            tname = "magical theory"
            ttype = "kno"
            curlevel = caller.db.knowledges['magical theory']
            newlevel = curlevel + 1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods(ttype, "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.knowledges['magical theory'] = curlevel + 1
            caller.db.times_trained = caller.db.times_trained + 1
            caller.db.level = caller.db.times_trained / 10
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
            #ABILITY SYNERGY
            caller.db.abils['elemental magic']['basic']['points'] += 1
            if newlevel % 2 == 0:
                caller.db.abils['ritual magic']['basic']['points'] += 1
                caller.db.abils['elemental magic']['normal']['points'] += 1 
                caller.db.abils['elemental magic']['basic']['points'] += 1
            if newlevel % 3 == 0:
                caller.db.abils['elemental magic']['intermediate']['points'] += 1
                caller.db.abils['elemental magic']['normal']['points'] += 2
                caller.db.abils['elemental magic']['basic']['points'] += 2
            if newlevel % 4 == 0:
                caller.db.abils['ritual magic']['normal']['points'] += 1
                caller.db.abils['ritual magic']['basic']['points'] += 2
                caller.db.abils['elemental magic']['advanced']['points'] += 1
                caller.db.abils['elemental magic']['intermediate']['points'] += 2
                caller.db.abils['elemental magic']['normal']['points'] += 3
                caller.db.abils['elemental magic']['basic']['points'] += 3
            if newlevel % 5 == 0:
                caller.db.abils['elemental magic']['master']['points'] += 1
                caller.db.abils['elemental magic']['advanced']['points'] += 2
                caller.db.abils['elemental magic']['intermediate']['points'] += 3
                caller.db.abils['elemental magic']['normal']['points'] += 4
                caller.db.abils['elemental magic']['basic']['points'] += 5
            if newlevel % 6 == 0:
                caller.db.abils['ritual magic']['intermediate']['points'] += 1
                caller.db.abils['ritual magic']['normal']['points'] += 2
                caller.db.abils['ritual magic']['basic']['points'] += 3
            if newlevel % 8 == 0:
                caller.db.abils['ritual magic']['advanced']['points'] += 1
                caller.db.abils['ritual magic']['intermediate']['points'] += 2
                caller.db.abils['ritual magic']['normal']['points'] += 3
                caller.db.abils['ritual magic']['basic']['points'] += 4
            if newlevel % 10 == 0:
                caller.db.abils['ritual magic']['master']['points'] += 1
                caller.db.abils['ritual magic']['advanced']['points'] += 2
                caller.db.abils['ritual magic']['intermediate']['points'] += 3
                caller.db.abils['ritual magic']['normal']['points'] += 4
                caller.db.abils['ritual magic']['basic']['points'] += 5
#demonic lore
        elif trainitem == "demlor" or trainitem == "demonic lore":
            tname = "demonic lore"
            ttype = "kno"
            curlevel = caller.db.knowledges['demonic lore']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods(ttype, "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.knowledges['demonic lore'] = curlevel + 1
            caller.db.times_trained = caller.db.times_trained + 1
            caller.db.level = caller.db.times_trained / 10
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
            #ABILITY SYNERGY
            if newlevel % 3 == 0:
                caller.db.abils['ritual magic']['master']['points'] += 1
                caller.db.abils['ritual magic']['advanced']['points'] += 2
                caller.db.abils['ritual magic']['intermediate']['points'] += 2
                caller.db.abils['ritual magic']['normal']['points'] += 3
                caller.db.abils['ritual magic']['basic']['points'] += 3          

#ABILITIES
#ritual magic - basic
        elif trainitem == "ritmag b" or trainitem == "ritual magic basic":
            tname = "ritual magic - basic"
            afflevel = caller.db.abils['ritual magic']['affects level']
            ttype = "abi-b"
            curlevel = caller.db.abils['ritual magic']['basic']['level']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-b", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['ritual magic']['basic']['level'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['ritual magic']['basic']['points'] = caller.db.abils['ritual magic']['basic']['points'] + (5 * newlevel)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#ritual magic - basic - minor boost
        elif trainitem == "mbst" or trainitem == "minor boost":
            tname = "minor boost"
            afflevel = caller.db.abils['ritual magic']['affects level']
            ttype = "abi-b-s"
            pointmod = 1
            curlevel = caller.db.abils['ritual magic']['basic']['powers']['minor boost']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-b-s", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #if so, check for enough points
            if caller.db.abils['ritual magic']['basic']['points'] < (newlevel* pointmod):
                caller.msg("You don't have enough points to train your " + tname.capitalize() + "!")
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['ritual magic']['basic']['powers']['minor boost'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['ritual magic']['basic']['points'] = caller.db.abils['ritual magic']['basic']['points'] - (newlevel)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#ritual magic - basic - minor shield
        elif trainitem == "mshld" or trainitem == "minor shield":
            tname = "minor shield"
            afflevel = caller.db.abils['ritual magic']['affects level']
            ttype = "abi-b-s"
            pointmod = 1
            curlevel = caller.db.abils['ritual magic']['basic']['powers']['minor shield']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-b-s", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #if so, check for enough points
            if caller.db.abils['ritual magic']['basic']['points'] < (newlevel* pointmod):
                caller.msg("You don't have enough points to train your " + tname.capitalize() + "!")
            #If so do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['ritual magic']['basic']['powers']['minor shield'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['ritual magic']['basic']['points'] = caller.db.abils['ritual magic']['basic']['points'] - (newlevel * pointmod)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#ritual magic - basic - sunvisor
        elif trainitem == "visor" or trainitem == "sunvisor":
            tname = "sunvisor"
            afflevel = caller.db.abils['ritual magic']['affects level']
            ttype = "abi-b-s"
            pointmod = 1
            curlevel = caller.db.abils['ritual magic']['basic']['powers']['sunvisor']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-b-s", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #if so, check for enough points
            if caller.db.abils['ritual magic']['basic']['points'] < (newlevel* pointmod):
                caller.msg("You don't have enough points to train your " + tname.capitalize() + "!")
            #If so, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['ritual magic']['basic']['powers']['sunvisor'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['ritual magic']['basic']['points'] = caller.db.abils['ritual magic']['basic']['points'] - (newlevel * pointmod)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#ritual magic - normal
        elif trainitem == "ritmag n" or trainitem == "ritual magic normal":
            tname = "ritual magic - normal"
            afflevel = caller.db.abils['ritual magic']['affects level']
            ttype = "abi-n"
            curlevel = caller.db.abils['ritual magic']['normal']['level']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-n", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['ritual magic']['normal']['level'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['ritual magic']['normal']['points'] = caller.db.abils['ritual magic']['normal']['points'] + (5 * newlevel)
            caller.db.abils['ritual magic']['basic']['points'] = caller.db.abils['ritual magic']['basic']['points'] + (5 * newlevel)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#ritual magic - normal - boost
        elif trainitem == "bst" or trainitem == "boost":
            tname = "boost"
            afflevel = caller.db.abils['ritual magic']['affects level']
            ttype = "abi-n-s"
            pointmod = 3
            curlevel = caller.db.abils['ritual magic']['normal']['powers']['boost']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-n-s", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #if so, check for enough points
            if caller.db.abils['ritual magic']['normal']['points'] < (newlevel* pointmod):
                caller.msg("You don't have enough points to train your " + tname.capitalize() + "!")
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['ritual magic']['normal']['powers']['boost'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['ritual magic']['basic']['points'] = caller.db.abils['ritual magic']['normal']['points'] - (pointmod * newlevel)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#ritual magic - normal - shield
        elif trainitem == "shld" or trainitem == "shield":
            tname = "shield"
            afflevel = caller.db.abils['ritual magic']['affects level']
            ttype = "abi-n-s"
            pointmod = 1
            curlevel = caller.db.abils['ritual magic']['normal']['powers']['shield']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-n-s", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #if so, check for enough points
            if caller.db.abils['ritual magic']['normal']['points'] < (newlevel* pointmod):
                caller.msg("You don't have enough points to train your " + tname.capitalize() + "!")
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['ritual magic']['normal']['powers']['shield'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['ritual magic']['normal']['points'] = caller.db.abils['ritual magic']['normal']['points'] - (pointmod * newlevel)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#ritual magic - normal - sunshade
        elif trainitem == "shade" or trainitem == "sunshade":
            tname = "sunshade"
            afflevel = caller.db.abils['ritual magic']['affects level']
            ttype = "abi-b-s"
            pointmod = 3
            curlevel = caller.db.abils['ritual magic']['normal']['powers']['sunshade']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-b-s", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #if so, check for enough points
            if caller.db.abils['ritual magic']['normal']['points'] < (newlevel* pointmod):
                caller.msg("You don't have enough points to train your " + tname.capitalize() + "!")
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['ritual magic']['normal']['powers']['sunshade'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['ritual magic']['normal']['points'] = caller.db.abils['ritual magic']['normal']['points'] - (pointmod * newlevel)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#ritual magic - intermediate
        elif trainitem == "ritmag i" or trainitem == "ritual magic intermediate":
            tname = "ritual magic - intermediate"
            afflevel = caller.db.abils['ritual magic']['affects level']
            ttype = "abi-i"
            curlevel = caller.db.abils['ritual magic']['intermediate']['level']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-i", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['ritual magic']['intermediate']['level'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['ritual magic']['intermediate']['points'] = caller.db.abils['ritual magic']['intermediate']['points'] + (5 * newlevel)
            caller.db.abils['ritual magic']['normal']['points'] = caller.db.abils['ritual magic']['normal']['points'] + (5 * newlevel)
            caller.db.abils['ritual magic']['basic']['points'] = caller.db.abils['ritual magic']['basic']['points'] + (5 * newlevel)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#ritual magic - advanced
        elif trainitem == "ritmag a" or trainitem == "ritual magic advanced":
            tname = "ritual magic - advanced"
            afflevel = caller.db.abils['ritual magic']['affects level']
            ttype = "abi-a"
            curlevel = caller.db.abils['ritual magic']['advanced']['level']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-a", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['ritual magic']['advanced']['level'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['ritual magic']['advanced']['points'] = caller.db.abils['ritual magic']['advanced']['points'] + (5 * newlevel)
            caller.db.abils['ritual magic']['intermediate']['points'] = caller.db.abils['ritual magic']['intermediate']['points'] + (5 * newlevel)
            caller.db.abils['ritual magic']['normal']['points'] = caller.db.abils['ritual magic']['normal']['points'] + (5 * newlevel)
            caller.db.abils['ritual magic']['basic']['points'] = caller.db.abils['ritual magic']['basic']['points'] + (10 * newlevel)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#ritual magic - master
        elif trainitem == "ritmag m" or trainitem == "ritual magic master":
            tname = "ritual magic - master"
            afflevel = caller.db.abils['ritual magic']['affects level']
            ttype = "abi-m"
            curlevel = caller.db.abils['ritual magic']['master']['level']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-m", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['ritual magic']['master']['level'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['ritual magic']['master']['points'] = caller.db.abils['ritual magic']['master']['points'] + (5 * newlevel)
            caller.db.abils['ritual magic']['advanced']['points'] = caller.db.abils['ritual magic']['advanced']['points'] + (5 * newlevel)
            caller.db.abils['ritual magic']['intermediate']['points'] = caller.db.abils['ritual magic']['intermediate']['points'] + (5 * newlevel)
            caller.db.abils['ritual magic']['normal']['points'] = caller.db.abils['ritual magic']['normal']['points'] + (10 * newlevel)
            caller.db.abils['ritual magic']['basic']['points'] = caller.db.abils['ritual magic']['basic']['points'] + (10 * newlevel)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#elemental magic - basic
        elif trainitem == "elemag b" or trainitem == "elemental magic basic":
            tname = "elemental magic - basic"
            afflevel = caller.db.abils['elemental magic']['affects level']
            ttype = "abi-b"
            pointmod = 1
            curlevel = caller.db.abils['elemental magic']['basic']['level']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-b", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #if so, check for enough points
            if caller.db.abils['ritual magic']['basic']['points'] < (newlevel* pointmod):
                caller.msg("You don't have enough points to train your " + tname.capitalize() + "!")
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['elemental magic']['basic']['level'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['elemental magic']['basic']['points'] = caller.db.abils['elemental magic']['basic']['points'] - (newlevel * pointmod)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#elemental magic - basic - flame dart
        elif trainitem == "fdart" or trainitem == "flame dart":
            tname = "flame dart"
            afflevel = caller.db.abils['elemental magic']['affects level']
            ttype = "abi-b-s"
            pointmod = 1
            curlevel = caller.db.abils['elemental magic']['basic']['powers']['flame dart']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-b-s", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #if so, check for enough points
            if caller.db.abils['elemental magic']['basic']['points'] < (newlevel* pointmod):
                caller.msg("You don't have enough points to train your " + tname.capitalize() + "!")
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['elemental magic']['basic']['powers']['flame dart'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['elemental magic']['basic']['points'] = caller.db.abils['elemental magic']['basic']['points'] - (newlevel * pointmod)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#dazzle
        elif trainitem == "dazz" or trainitem == "dazzle":
            tname = "flame dart"
            afflevel = caller.db.abils['elemental magic']['affects level']
            ttype = "abi-b-s"
            pointmod = 1
            curlevel = caller.db.abils['elemental magic']['basic']['powers']['flame dart']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-b-s", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #if so, check for enough points
            if caller.db.abils['elemental magic']['basic']['points'] < (newlevel* pointmod):
                caller.msg("You don't have enough points to train your " + tname.capitalize() + "!")
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['elemental magic']['basic']['powers']['flame dart'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['elemental magic']['basic']['points'] = caller.db.abils['elemental magic']['basic']['points'] - (newlevel * pointmod)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#elemental magic - normal
        elif trainitem == "elemag n" or trainitem == "elemental magic normal":
            tname = "elemental magic - normal"
            afflevel = caller.db.abils['elemental magic']['affects level']
            ttype = "abi-n"
            curlevel = caller.db.abils['elemental magic']['normal']['level']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-n", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['elemental magic']['normal']['level'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['elemental magic']['normal']['points'] = caller.db.abils['elemental magic']['normal']['points'] + (5 * newlevel)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#elemental magic - intermediate
        elif trainitem == "elemag i" or trainitem == "elemental magic intermediate":
            tname = "elemental magic - intermediate"
            afflevel = caller.db.abils['elemental magic']['affects level']
            ttype = "abi-i"
            curlevel = caller.db.abils['elemental magic']['intermediate']['level']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-i", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['elemental magic']['intermediate']['level'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['elemental magic']['intermediate']['points'] = caller.db.abils['elemental magic']['intermediate']['points'] + (5 * newlevel)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#elemental magic - advanced
        elif trainitem == "elemag a" or trainitem == "elemental magic advanced":
            tname = "elemental magic - advanced"
            afflevel = caller.db.abils['elemental magic']['affects level']
            ttype = "abi-a"
            curlevel = caller.db.abils['elemental magic']['advanced']['level']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-a", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['elemental magic']['advanced']['level'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['elemental magic']['advanced']['points'] = caller.db.abils['elemental magic']['advanced']['points'] + (5 * newlevel)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")
#elemental magic - master
        elif trainitem == "elemag m" or trainitem == "elemental magic master":
            tname = "elemental magic - master"
            afflevel = caller.db.abils['elemental magic']['affects level']
            ttype = "abi-m"
            curlevel = caller.db.abils['elemental magic']['master']['level']
            newlevel = curlevel +1
            typemod = self.get_typemods(ttype)
            abilmod = self.get_typemods("abi-m", "abil")
            traincost = self.get_traincost(tname,typemod, curlevel, charlevel, abilmod)
            #See if we're just checking
            if "check" in self.switches:
                caller.msg("It will take " + str(traincost) + " experience to raise your " + tname)
                return
            #If not, check for enough xp
            if caller.db.experience['current'] < traincost:
                caller.msg("You don't have enough experience to train your " + tname.capitalize() + "!")
                return
            #If not, do the training
            caller.db.experience['current'] -= traincost
            caller.db.experience['spent'] += traincost
            caller.db.abils['elemental magic']['master']['level'] += 1
            caller.db.times_trained = caller.db.times_trained + afflevel
            caller.db.level = caller.db.times_trained / 10
            caller.db.abils['elemental magic']['master']['points'] = caller.db.abils['elemental magic']['master']['points'] + (5 * newlevel)
            caller.msg("Congratulations!  You have raised your " + tname.capitalize() + " from " + str(curlevel) + " to " + str(curlevel+1) + "!  You currently have " + str(caller.db.experience['current']) + " experience available to spend.")

    def get_traincost(self,trainitem, typemod, curlevel, charlevel, abilmod = 0):
        """
        Training Model Setup
        
        Tier Modifier = 100 * (Tier * Tier)

        Basic Model:
            ((Current Value + New Value) * Level Modifier) * Type Modifier) + Tier Modifier

        Attributes:
            Multiplier = 10

        Knowledges
            Multiplier = 1
        
        Skills
            Multiplier = 4
        
        Abilities
            Multiplier = 7

            Basic
                Ability Level Adjustment = + 100
            Normal
                Ability Level Adjustment = + 250
            Intermediate
                Ability Level Adjustment = + 500
            Advanced
                Ability Level Adjustment = + 1000
            Master
                Ability Level Adjustment = + 10000

            The Sub-ability modifier is 1.5, and the Ability Level adjustment
            is 1/10 the cost for the base ability skill
        """
        if charlevel == 0:
            tier = 0
        elif charlevel > 0 and charlevel <= 100:
            tier = (charlevel / 20) + 1
        elif charlevel > 100 and charlevel <= 150:
            tier = 5 + ((charlevel - 100) / 10) + 1
        elif charlevel > 150 and charlevel <= 175:
            tier = 10 + ((charlevel - 150) / 5) + 1
        else:
            tier = 15 + (charlevel - 175)
        
        tiermod = (tier * tier) * 100
        levelmod = charlevel * 1.1

        #((Current Value + New Value) * Level Modifier) * Type Modifier) + Tier Modifier
        return (((curlevel + (curlevel + 1)) * levelmod) * typemod )+ tiermod + abilmod

    def get_typemods(self, ttype, getopt = "base"):
        caller = self.caller

        if getopt == "base":
            if ttype == "att":
                return 10
            elif "abi" in ttype.split("-"):
                return 7
            elif ttype == "ski":
                return 4
            elif ttype == "kno":
                return 1
            else:
                return 1
        else:
           if ttype == "abi-b":
                return 100
           elif ttype == "abi-b-s":
                return 10
           elif ttype == "abi-n":
                return 250
           elif ttype == "abi-n-s":
                return 25
           elif ttype == "abi-i":
                return 500
           elif ttype == "abi-i-s":
                return 50
           elif ttype == "abi-a":
                return 1000
           elif ttype == "abi-a-s":
                return 100
           elif ttype == "abi-m":
                return 10000
           elif ttype == "abi-m-s":
                return 1000
           else:
                return 0
