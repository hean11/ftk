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
import os.path

KERNEL_PART="/dev/mtd1"
DTB_PART="/dev/mtd2"

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
