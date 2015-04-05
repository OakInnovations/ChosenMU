"""
OOB configuration.

This module should be included in (or replace) the
default module set in settings.OOB_PLUGIN_MODULES

A function oob_error will be used as optional error management.
The available OOB commands can be extended by changing

    `settings.OOB_PLUGIN_MODULES`

CMD_MAP: This module must contain a global dictionary CMD_MAP. This is
a dictionary that maps the call-name available  to a function in this
module (this allows you to map multiple oob cmdnames to a single
actual Python function, for example).

oob functions have the following call signature:

    function(session, *args, **kwargs)

where session is the active session and *args, **kwargs are extra
arguments sent with the oob command.

A function mapped to the key "oob_error" will retrieve error strings
if it is defined. It will get the error message as its 1st argument.

    oob_error(session, error, *args, **kwargs)

This allows for customizing error handling.

Data is usually returned to the user via a return OOB call:

   session.msg(oob=(oobcmdname, (args,), {kwargs}))

Oobcmdnames are case-sensitive.  Note that args, kwargs must be
iterable. Non-iterables will be interpreted as a new command name (you
can send multiple oob commands with one msg() call))

"""

# import the contents of the default msdp module
from evennia.server.oob_cmds import *


# def oob_echo(session, *args, **kwargs):
#     """
#     Example echo function. Echoes args, kwargs sent to it.
#
#     Args:
#         session (Session): The Session to receive the echo.
#         args (list of str): Echo text.
#         kwargs (dict of str, optional): Keyed echo text
#
#     """
#     session.msg(oob=("echo", args, kwargs))
#
## oob command map
# CMD_MAP = {"ECHO": oob_echo}

#
# MSDP protocol standard commands
#
# MSDP suggests the following standard name conventions for making
# different properties available to the player

# "CHARACTER_NAME", "SERVER_ID",  "SERVER_TIME", "AFFECTS", "ALIGNMENT", "EXPERIENCE", "EXPERIENCE_MAX", "EXPERIENCE_TNL",
# "HEALTH", "HEALTH_MAX", "LEVEL", "RACE", "CLASS", "MANA", "MANA_MAX", "WIMPY", "PRACTICE", "MONEY", "MOVEMENT",
# "MOVEMENT_MAX", "HITROLL", "DAMROLL", "AC", "STR", "INT", "WIS", "DEX", "CON", "OPPONENT_HEALTH", "OPPONENT_HEALTH_MAX",
# "OPPONENT_LEVEL", "OPPONENT_NAME", "AREA_NAME", "ROOM_EXITS", "ROOM_VNUM", "ROOM_NAME", "WORLD_TIME", "CLIENT_ID",
# "CLIENT_VERSION", "PLUGIN_ID", "ANSI_COLORS", "XTERM_256_COLORS", "UTF_8", "SOUND", "MXP", "BUTTON_1", "BUTTON_2",
# "BUTTON_3", "BUTTON_4", "BUTTON_5", "GAUGE_1", "GAUGE_2","GAUGE_3", "GAUGE_4", "GAUGE_5"


# mapping from MSDP standard names to Evennia variables
OOB_SENDABLE = {
    "CHARACTER_NAME": lambda o: o.key,
    "SERVER_ID": lambda o: settings.SERVERNAME,
    "ROOM_NAME": lambda o: o.db_location.key,
    "ANSI_COLORS": lambda o: True,
    "XTERM_256_COLORS": lambda o: True,
    "UTF_8": lambda o: True,
    "HEALTH": lambda o: o.db.curhp,
    "HEALTH_MAX": lambda o: o.db.maxhp
    }

# mapping standard MSDP keys to Evennia field names
OOB_REPORTABLE = {
    "CHARACTER_NAME": "db_key",
    "ROOM_NAME": "db_location",
    "TEST" : "test",
    "HEALTH": "curhp",
    "HEALTH_MAX": "dmaxhp"
    }
