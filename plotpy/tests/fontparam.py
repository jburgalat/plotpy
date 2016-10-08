# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see plotpy/__init__.py for details)

"""FontParam test"""

SHOW = False # Do not show test in GUI-based test launcher

from plotpy.styles import FontParam

def test():
    fp = FontParam()
    fp.edit()
    fp.edit()

if __name__ == '__main__':
    import plotpy
    _app = plotpy.qapplication()
    test()
