# -*- coding: utf-8 -*-
#
# Copyright © 2012 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see plotpy/__init__.py for details)

"""Shows how to customize a shape created with a tool like RectangleTool"""

SHOW = True # Show test in GUI-based test launcher

import os.path as osp

from plotpy.plot import ImageDialog
from plotpy.tools import (RectangleTool, EllipseTool, SegmentTool,
                          MultiLineTool, FreeFormTool)
from plotpy.builder import make
from plotpy.styles import style_generator, update_style_attr

STYLE = style_generator()

def customize_shape(shape):
    global STYLE
    param = shape.shapeparam
    style = next(STYLE)
    update_style_attr(style, param)
    param.update_shape(shape)
    shape.plot().replot()

def create_window():
    gridparam = make.gridparam(background="black",
                               minor_enabled=(False, False),
                               major_style=(".", "gray", 1))
    win = ImageDialog(edit=False, toolbar=True,
                      wintitle="All image and plot tools test",
                      options=dict(gridparam=gridparam))
    for toolklass in (RectangleTool, EllipseTool, SegmentTool,
                      MultiLineTool, FreeFormTool):
        win.add_tool(toolklass, handle_final_shape_cb=customize_shape)
    return win

def test():
    """Test"""
    # -- Create QApplication
    import plotpy
    _app = plotpy.qapplication()
    # --
    filename = osp.join(osp.dirname(__file__), "brain.png")
    win = create_window()
    image = make.image(filename=filename, colormap="bone", alpha_mask=True)
    plot = win.get_plot()
    plot.add_item(image)
    win.exec_()

if __name__ == "__main__":
    test()
