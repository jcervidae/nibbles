#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Jonathan Cervidae <jonathan.cervidae@gmail.com>
# PGP Fingerprint: 2DC0 0A44 123E 6CC2 EB55  EAFB B780 421F BF4C 4CB4
# Last changed: $LastEdit: 2009-05-30 22:19:35 BST$
# Last committed: $Format:%cd$
# File revision: $Id$
#
# This file is part of nibbles.
#
# nibbles is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# nibbles is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# nibbles in the file COPYING. If not, see
# <http://www.gnu.org/licenses/>.

def call(self,args, data=None):
    if data:
        proc = subprocess.Popen(
            args,
            stdin=subprocess.PIPE,stdout=subprocess.PIPE
        )
        out, err = proc.communicate(data)
    else:
        proc = subprocess.Popen(
            args,
            stdout=subprocess.PIPE
        )
        out, err = proc.communicate()
    if proc.returncode is not 0:
        raise StandardError, (
            "%s has problem:%s%s" % (
                args[0], os.linesep * 2, err
            )
        )
    return(out)
