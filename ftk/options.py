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

import argparse

class Options:
    description = """
    Factory toolkit. This toolkit can be used for restoring the hole system to the factory
    default. It can although used for booting into a recovery system. Please use this tool
    with care, because it could destroy your running system"""

    prog = "ftk"

    def __init__(self):
        self.parser = argparse.ArgumentParser(prog=self.prog, description=self.description)
        self.parser.add_argument('-f', '--factory', action="store_true", dest="factory",
                            help="Perform a complete factory reset")
        self.parser.add_argument('-b', '--boot_recovery', action='store_true', dest='recovery',
                            help='Reboot into recovery image')
        self.parser.add_argument('-n', '--normalboot', action='store_true', dest='normal',
                            help='Reboot into the normal boot image')
        self.parser.add_argument('-i', '--install', action='store', dest='install',
                            help='Install new recovery image')
        self.parser.add_argument('-k', '--kernel-install', action='store', dest='kernel_install',
                            help='Flash a new Kernel Image into the corresponding flash partition')
        self.parser.add_argument('-d', '--dtb-install', action='store', dest='dtb_install',
                            help='Flash a new DeviceTreeBlob into the corresponding flash partition')

    def parse(self):
        self.args = self.parser.parse_args()
        if self.args.factory == None and self.args.recovery == None and self.args.normal == None:
            raise StandardError("Something went wrong with your arguments. Tryp -h")
