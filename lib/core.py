#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import re

class Core():

    def __init__(self):
        pass

    def addSalt(self, banner, salt):
        bufferLength = banner.count("F")

        if len(salt) > bufferLength + 2: 
            print("Salt string to long!!!")
            exit(1)
        salt = '"' + salt + '"'
        saltyBanner = re.sub("F" * bufferLength, salt.center(bufferLength + 2, " "), banner)
        return saltyBanner




