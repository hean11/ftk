# ftk - Managing flashing diffrent sections of the flash
# Copyright (C) 2016  Robert Lehmann <robert.lehmann@sitec-systems.de>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

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
