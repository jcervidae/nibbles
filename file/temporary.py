#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Jonathan Cervidae <jonathan.cervidae@gmail.com>
# PGP Fingerprint: 2DC0 0A44 123E 6CC2 EB55  EAFB B780 421F BF4C 4CB4
# Last changed: $LastEdit: 2009-05-25 17:40:27 BST$

class SelfDeletingTempDirectory(object):
    def __init__(self, suffix='', prefix="tmp", dir=None):
        import tempfile
        self.path = tempfile.mkdtemp(
            suffix=suffix, prefix=prefix, dir=dir
        )
    def __del__(self):
        import shutil
        shutil.rmtree(self.path,ignore_errors=True)
    def __str__(self):
        return self.path

class SelfDeletingFIFO(file):
    def __init__(self, string):
        self.temp_path = tempfile.mkdtemp()
        fifo_name = tempfile.mktemp(dir=self.temp_path)
        os.mkfifo(fifo_name,0600)
        super(Signer.FIFO, self).__init__(fifo_name, "ab+", 0)
    def __del__(self):
        self.close()
        shutil.rmtree(self.temp_path, ignore_errors=False)
