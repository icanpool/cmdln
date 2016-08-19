#!/usr/bin/env python

"""
    spawn python cmdln_help2.py help
    Usage:
        cmdln_help2.py COMMAND [ARGS...]
        cmdln_help2.py help [COMMAND]

    optional arguments:
        -h, --help  show this help message and exit

    Commands:
        documented     blah blah blah
        hashelpfunc    gobbledy gook
        help (?)       give detailed help on a specific sub-command
        undocumented


    spawn python cmdln_help2.py help documented
    documented: blah blah blah
    spawn python cmdln_help2.py ? documented
    documented: blah blah blah
    spawn python cmdln_help2.py help hashelpfunc
    hashelpfunc: gobbledy gook
    spawn python cmdln_help2.py help undocumented
    cmdln_help2.py: I don't know how to use 'undocumented'
    spawn python cmdln_help2.py help undefined
    cmdln_help2.py: wassup with this: 'undefined'
    Try 'cmdln_help2.py help' for info.
    spawn python cmdln_help2.py
    help-test> help
    Usage:
        COMMAND [ARGS...]
        help [COMMAND]

    optional arguments:
        -h, --help  show this help message and exit

    Commands:
        documented     blah blah blah
        hashelpfunc    gobbledy gook
        help (?)       give detailed help on a specific sub-command
        undocumented
    help-test> help documented
    documented: blah blah blah
    help-test> help hashelpfunc
    hashelpfunc: gobbledy gook
    help-test> help undocumented
    I don't know how to use 'undocumented'
    help-test> help undefined
    wassup with this: 'undefined'
    help-test> ^D
"""

import sys
import cmdln

class HelpShell(cmdln.RawCmdln):
    # no class doc string
    prompt = "help-test> "
    # test nohelp and unknowncmd
    nohelp = "I don't know how to use '%s'"
    unknowncmd = "wassup with this: '%s'"
    def do_documented(self, argv):
        """${cmd_name}: blah blah blah"""
    def do_undocumented(self, argv):
        pass
    def help_hashelpfunc(self):
        return "${cmd_name}: gobbledy gook"
    def do_hashelpfunc(self, argv):
        "${cmd_name}: this shouldn't show"
        pass

if __name__ == "__main__":
    sys.exit( HelpShell().main(loop=cmdln.LOOP_IF_EMPTY) )
