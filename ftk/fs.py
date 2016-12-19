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

def mount_recovery():
    mount_ubi("/dev/ubi0_0")

def umount_recovery():
    umount_ubi("/dev/ubi0_0")

def is_mounted(device):
    """Check if a specific device is mounted on the system
    device -- device which will be checked if mounted
    
    Return True if the device is mounted, else return False
    """
    try:
        mount_list = subprocess.check_output(["mount"])
    except subprocess.CalledProcessError as err:
        raise StandardError("Can't check for mounted devices: %s" %
                            err.returncode)
    
    found = False
    for elem in mount_list.splitlines():
        if elem.find(device) >= 0:
            found = True
            break

    return found

def mount_ubi(ubi_device):
    if not is_mounted(ubi_device):
        try:
            subprocess.check_call(["mount", "-t", "ubifs", ubi_device, "/mnt"])
        except subprocess.CalledProcessError as err:
            raise StandardError("Can't mount ubi device %s: %s" %
                                (ubi_device, err.returncode))

def umount_ubi(ubi_device):
    if is_mounted(ubi_device):
        try:
            subprocess.check_call(["umount", ubi_device])
        except subprocess.CalledProcessError as err:
            raise StandardError("Can't umount ubi device %s: %s" %
                                (ubi_device, err.returncode))
    
