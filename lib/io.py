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

import sys
from argparse import *

class IO():
    
    def __init__(self):
        pass

    def getArguments(self):
        parser = ArgumentParser(description="A simple tool for creating"
                                "nya ascii art with embeded salt ")
        parser.add_argument('-s', '--salt', type=str, help="Salt message to"
                            "embed")

        args = parser.parse_args()
        return args

    def readBanner(self):
        banner = open("lib/artwork.txt", "r").read()
        return banner

