from evennia.utils.evtable import EvTable, EvCell
from evennia.utils.evform import *
from commands.command import Command
from evennia.utils.utils import all_from_module, to_str, to_unicode

class CharSheet(Command):
    """
    Displays an actual character sheet.
    """

    key = "+sheet"
    aliases = ["sco", "score", "sheet", "stats", "stat"]
    locks = "cmds:all()"
    help_category = "Character"

    def func(self):
        caller = self.caller
        form = EvForm("world.charsheet_template")

        charname = "{c" + caller.key + "{n"
        charlevel = caller.db.level
        #add data
        form.map(cells = {1: charname,
                          2: caller.player,
                          3: "{c" + str(int(caller.db.level)) + "{n",
                          4: "{c" + str(int(caller.db.experience['current'])) + "{n",
                          5: "{c" + str(int(caller.db.experience['current'] + caller.db.experience['spent'])) + "{n",
                          6: "{y" + str(caller.db.atts['str']) + "{n",
                          7: "{y" + str(caller.db.atts['dex']) + "{n",
                          8: "{y" + str(caller.db.atts['con']) + "{n",
                          9: "{y" + str(caller.db.atts['int']) + "{n",
                          "z": "{y" + str(caller.db.atts['wis']) + "{n",
                          "y": "{y" + str(caller.db.atts['cha']) + "{n",
                          "q": "{c" + str(caller.db.curhp) + "{n",
                          "r": "{c" + str(caller.db.maxhp) + "{n",
                          "s": "{c" + str(caller.db.cursp) + "{n",
                          "t": "{c" + str(caller.db.maxsp) + "{n"}
                 )

        #set up tables
        skillnames = []
        skilllevels = []
        knownames = []
        knowlevels = []
        for skill in caller.db.skills:
            skillnames.append(skill.title())
            skilllevels.append(caller.db.skills[skill])
        for know in caller.db.knowledges:
            knownames.append(know.title())
            knowlevels.append(caller.db.knowledges[know])
        tableA = EvTable("{cSkill{n", "{cLevel{n",
                         table = [skillnames,skilllevels],
                         border = "none")
        tableB = EvTable("{cKnowledge{n", "{cLevel{n",
                         table = [knownames,knowlevels],
                         border = "none")

        form.map(tables = {"A": tableA,
                           "B": tableB})

        #print unicode(form)
        caller.msg(unicode(form))
        return form


