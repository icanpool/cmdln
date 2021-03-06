#!/usr/bin/env python

r"""
    spawn python cmdln_aliases.py foo
    hello from foo
    spawn python cmdln_aliases.py f
    hello from foo
    spawn python cmdln_aliases.py !
    hello from foo
    spawn python cmdln_aliases.py help
    Usage:
        cmdln_aliases.py COMMAND [ARGS...]
        cmdln_aliases.py help [COMMAND]

    usage: cmdln_aliases.py [-h]

    optional arguments:
        -h, --help  show this help message and exit

    Commands:
        foo (!, f)     shazam!
        help (?)       give detailed help on a specific sub-command


"""

import sys
import cmdln

class Shell(cmdln.RawCmdln):
    def do_foo(self, argv):
        "shazam!"
        print("hello from foo")
    do_foo.aliases = ["f", "!"]

if __name__ == "__main__":
    shell = Shell()
    retval = shell.main(loop=cmdln.LOOP_NEVER) # don't want a command loop
    sys.exit(retval)
