#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Jonathan Cervidae <jonathan.cervidae@gmail.com>
# PGP Fingerprint: 2DC0 0A44 123E 6CC2 EB55  EAFB B780 421F BF4C 4CB4
# Last changed: $LastEdit: 2009-05-30 22:19:21 BST$
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

import os
import pickle

class PersistentStruct(object):

    def __init__( self, pickle_file):
        self.__dict__['_pickle_file'] = os.path.expanduser(pickle_file)
        self._load()

    def __getitem__(self, name):
        if not name in self.__dict__['_struct']:
            raise KeyError, "No such key %s" % name
        return self.__dict__['_struct'][name]

    def __setitem__(self, name, value):
        self._load()
        name = str(name)
        self.__dict__['_struct'][name] = value
        self._save()

    def __delitem__(self, name):
        self._load()
        del self.__dict__['_struct'][name]
        self._save()

    def __getattr__(self, name):
        self._load()
        if not name in self.__dict__['_struct']:
            raise KeyError, "No such key %s" % name
        return self.__dict__['_struct'][name]

    def __setattr__(self, name, value):
        self._load()
        name = str(name)
        self.__dict__['_struct'][name] = value
        self._save()

    def __delattr__(self, name):
        self._load()
        del self.__dict__['_struct'][name]
        self._save()

    def _load(self):
        if not os.path.exists(self.__dict__['_pickle_file']):
            self.__dict__['_struct'] = {}
            self._save()
        self.__dict__['_struct'] = pickle.load(
            open(self.__dict__['_pickle_file'])
        )

    def _save(self):
        pickle.dump(
            self.__dict__['_struct'],
            open(self.__dict__['_pickle_file'],"w")
        )
