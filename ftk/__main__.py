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

import sys

from options import Options
from ubootenv import set_alt_rootfs, set_alt_kernel
from utils import panic, reboot
from fs import mount_recovery, umount_recovery
from image import install_kernel_image, install_dtb_image
from recovery.image import install_recovery

def factory():
    try:
        set_alt_rootfs(True)
        mount_recovery()
        open("/mnt/var/ftk/recovery", 'a').close()
        umount_recovery()
        reboot()
    except StandardError as err:
        panic("", err)

def recovery():
    try:
        set_alt_rootfs(True)
        reboot()
    except StandardError as err:
        panic("", err)

def normal():
    try:
        set_alt_rootfs(False)
        reboot()
    except StandardError as err:
        panic("", err)

def install_rootfs_image(image_name):
    try:
        mount_recovery()
        install_recovery(image_name)
        umount_recovery()
    except StandardError as err:
        panic("", err)

def install_kernel(kernel_image):
    try:
        set_alt_kernel(True)
        install_kernel_image(kernel_image)
        set_alt_kernel(False)
    except StandardError as err:
        panic("", err)

def install_dtb(dtb_image):
    try:
        set_alt_kernel(True)
        install_dtb_image(dtb_image)
        set_alt_kernel(False)
    except StandardError as err:
        panic("", err)

def main():
    """ Main function for the factory toolkit
    """
    opt = Options()
    try:
        opt.parse()
    except StandardError as err:
        panic("", err)
    if opt.args.install != None:
        install_rootfs_image(opt.args.install)
    elif opt.args.kernel_install != None:
        install_kernel(opt.args.kernel_install)
    elif opt.args.dtb_install != None:
        install_dtb(opt.args.dtb_install)
    elif opt.args.factory:
        factory()
    elif opt.args.recovery:
        recovery()
    elif opt.args.normal:
        normal()

if __name__ == "__main__":
    main()
