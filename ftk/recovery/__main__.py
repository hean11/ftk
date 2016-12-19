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

import os.path
import os

from ftk import utils, ubootenv
from image import install_image

def main():
    """ Main function for recovery function of the toolkit """

    if os.path.isfile("/var/ftk/recovery"):
        print "Starting recovery"
        os.remove("/var/ftk/recovery")
        try:
            install_image()
            ubootenv.set_alt_rootfs(False)
            utils.reboot()
        except StandardError as err:
            print "Can't install image: %s" % err
            utils.reboot()

    
if __name__ == '__main__':
    main()
