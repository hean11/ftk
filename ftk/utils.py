# Copyright (c) 2016 sitec systems GmbH.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys

from subprocess import check_call, CalledProcessError

def panic(msg, err):
    if msg != "":
        print "Error: %s : %s" % (msg,err)
    else:
        print "Error: %s" % err
    sys.exit(1)

def reboot(delay=0):
    """Reboot the hole system.
    delay -- The delay for the reboot (default 0)

    Throws StandardError if the command can't reboot the hole system
    """

    if delay != 0:
        from time import sleep
        sleep(delay)

    try:
        check_call(["reboot"])
    except CalledProcessError as err:
        raise StandardError("Can't reboot the hole system: %s" %
                            err.returncode)
