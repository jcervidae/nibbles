#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Jonathan Cervidae <jonathan.cervidae@gmail.com>
# PGP Fingerprint: 2DC0 0A44 123E 6CC2 EB55  EAFB B780 421F BF4C 4CB4
# Last changed: $LastEdit: 2009-05-25 17:41:47 BST$

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
