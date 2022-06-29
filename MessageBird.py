#!/usr/bin/env python3
# +----------------------------------------------------------------------+
# |     _____   _____                                                    |
# |    / __/ | / / _ |    Copyright   : (C) 2021 SVA GmbH 2021           |
# |   _\ \ | |/ / __ |    License     : GNU General Public License v2    |
# |  /___/ |___/_/ |_|    Author      : Anonymous                        |
# | Creator Benedikt Bayer for smseagle,changed by author for MessageBird|
# +----------------------------------------------------------------------+
# |----------------------------------------------------------------------------
# | Name         : MessageBird
# | Description  : Send SMS from CheckMK using cUrl
# | Dependencies : curl
# | Script location: /omd/sites/BIS/local/share/check_mk/web/plugins/wato
# |----------------------------------------------------------------------------
register_notification_parameters(
    "messagebird",
    Dictionary(optional_keys=None,
               elements=[
                   (
                       "host",
                       ListOfStrings(
                           title=_("Hostname/IP"),
                           help=_("Hostname or IP Address of the MessageBird"),
                       ),
                   ),
                   (
                       "body", TextAscii(title=_("body"), help=_("Message text")),
                   ),
                   (                   
                       "originator", TextAscii(title=_("originator"), help=_("Message Sender")),
                   ),
                   (
                   ("access_key", TextAscii(title=_("access_key"), help=_("Access_key for MessageBird")),
                   )),
             ]))
