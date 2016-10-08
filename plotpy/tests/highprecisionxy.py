# -*- coding: utf-8 -*-
#
# Copyright © 2011-2012 CEA
# Ludovic Aubry
# Licensed under the terms of the CECILL License
# (see plotpy/__init__.py for details)

"""Plot computations test"""

SHOW = False # Show test in GUI-based test launcher

def xyimagebug(offset):
    from plotpy.plot import ImageDialog
    from plotpy.builder import make
    import numpy
    import plotpy
    app = plotpy.qapplication()
    data = numpy.random.rand(100, 100)
    x = numpy.arange(100)+offset 
    y = numpy.arange(100)
    image = make.xyimage(x, y, data=data)
    win = ImageDialog()
    plot = win.get_plot()
    plot.add_item(image)
    plot.select_item(image) #this helps in seeing where the image should be
    win.exec_()

if __name__ == '__main__':
    xyimagebug(1e9) #offset=1e9 makes it fail, but offset=1e4 is ok
