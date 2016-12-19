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

import subprocess

def set_alt_rootfs(set=True):
    """Set the alternative rootfs variable for the u-boot environment.
    """
    if set == True:
        set_string = "1"
    else:
        set_string = "0"

    try:
        subprocess.check_call(["fw_setenv", "root_alt", set_string])
    except subprocess.CalledProcessError as err:
        raise StandardError("Can't boot into recovery image: %s" %
                            err.returncode)

def set_alt_kernel(set=True):
    """Set the alternative kernel variable for u-boot environment
    """

    if set == True:
        set_string = "1"
    else:
        set_string = "0"

    try:
        subprocess.check_call(["fw_setenv", "kernel_alt", set_string])
    except subprocess.CalledProcessError as err:
        raise StandardError("Can't set alternative kernel: %s" %
                            err.returncode)
