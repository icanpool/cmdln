#!/usr/bin/env python

"""
    spawn python cmdln_aliases_deco.py foo
    hello from foo
    spawn python cmdln_aliases_deco.py f
    hello from foo
    spawn python cmdln_aliases_deco.py !
    hello from foo
    spawn python cmdln_aliases_deco.py bar
    hello from bar
    spawn python cmdln_aliases_deco.py ba
    hello from bar
    spawn python cmdln_aliases_deco.py b
    hello from bar
    spawn python cmdln_aliases_deco.py help
    Usage:
        cmdln_aliases_deco.py COMMAND [ARGS...]
        cmdln_aliases_deco.py help [COMMAND]

    usage: cmdln_aliases_deco.py [-h]

    optional arguments:
        -h, --help  show this help message and exit

    Commands:
        bar (b, ba)    whopee!
        foo (!, f)     shazam!
        help (?)       give detailed help on a specific sub-command

"""

import sys
import cmdln

class Shell(cmdln.Cmdln):
    @cmdln.alias('f', '!')
    def do_foo(self, argv):
        "shazam!"
        print("hello from foo")

    @cmdln.alias('ba')
    @cmdln.alias('b')
    def do_bar(self, argv):
        "whopee!"
        print("hello from bar")

if __name__ == "__main__":
    shell = Shell()
    retval = shell.main(loop=cmdln.LOOP_NEVER) # don't want a command loop
    sys.exit(retval)
