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

from lib.io import IO
from lib.core import Core 

DEFAULT_SALT = "YOU MAKE THIS GAME LIKE A TRASH"

class Process():

    def __init__(self):
        self.io = IO()
        self.core = Core()

        banner = self.io.readBanner()
        args = self.io.getArguments()
        salt = args.salt
        if salt == None:
            salt = DEFAULT_SALT
            
        saltyBanner = self. core.addSalt(banner, salt)
        print(saltyBanner)


if __name__ == "__main__":
    main = Process()

