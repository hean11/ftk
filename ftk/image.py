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

import subprocess
import os.path
import gzip
import shutil

KERNEL_PART="/dev/mtd1"
DTB_PART="/dev/mtd2"
IMAGE_PATH='/var/ftk/image.ubifs.gz'
TEMP_IMAGE='/tmp/image.ubifs'
IMAGE_MOUNT_PATH='/mnt/var/ftk/image.ubifs.gz'

def erase_partition(part):
	try:
		subprocess.check_call(["flash_erase", part, "0", "0"])
	except subprocess.CalledProcessError as err:
		raise StandardError("Can't erase flash partition %s: %i" % (part, err.returncode))

def flash_partition(part, image_file):
	if not os.path.isfile(image_file):
		raise StandardError("%s is not a valid file" % image_file)
	path = os.path.realpath(image_file)
	print "Install %s to %s" % (image_file, part)
	try:
		subprocess.check_call(["nandwrite", "-p", part, image_file])
	except subprocess.CalledProcessError as err:
		raise StandardError("Can't write flash partition %s: %i" % (part, err.returncode))


def install_kernel_image(kernel_image):
	erase_partition(KERNEL_PART)
	flash_partition(KERNEL_PART, kernel_image)

def install_dtb_image(dtb_image):
	erase_partition(DTB_PART)
	flash_partition(DTB_PART, dtb_image)

def install_recovery(image_name):
    if not os.path.isfile(image_name):
        raise StandardError("The given path %s is not a file" % image_name)

    with gzip.open(IMAGE_MOUNT_PATH, 'wb') as f_out, open(image_name, 'rb') as f_in:
        shutil.copyfileobj(f_in, f_out)
        
