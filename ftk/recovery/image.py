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

import gzip
import os.path
import shutil
import subprocess

IMAGE_PATH='/var/ftk/image.ubifs.gz'
TEMP_IMAGE='/tmp/image.ubifs'
IMAGE_MOUNT_PATH='/mnt/var/ftk/image.ubifs.gz'

def unpack_image():
    if not os.path.isfile(IMAGE_PATH):
        raise StandardError("Factory Image is not availible")

    with open(TEMP_IMAGE, 'wb') as f_out, gzip.open(IMAGE_PATH, 'rb') as f_in:
        shutil.copyfileobj(f_in, f_out)
        
def install_image():
    unpack_image()
    try:
        subprocess.check_call(["ubiupdatevol", "/dev/ubi0_1", TEMP_IMAGE])
    except subprocess.CalledProcessError as err:
        raise StandardError("Can't write image into ubi volume: %s" %
                            err.returncode)

def install_recovery(image_name):
    if not os.path.isfile(image_name):
        raise StandardError("The given path %s is not a file" % image_name)

    with gzip.open(IMAGE_MOUNT_PATH, 'wb') as f_out, open(image_name, 'rb') as f_in:
        shutil.copyfileobj(f_in, f_out)
        
    
