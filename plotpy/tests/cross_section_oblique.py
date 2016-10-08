# -*- coding: utf-8 -*-
#
# Copyright © 2009-2011 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see plotpy/__init__.py for details)

"""Oblique averaged cross section test"""

SHOW = True # Show test in GUI-based test launcher

import os.path as osp

import plotpy.cross_section
# debug mode shows the ROI in the top-left corner of the image plot:
plotpy.cross_section.DEBUG = True

from plotpy.plot import ImageDialog
from plotpy.builder import make
from plotpy.tools import ImageMaskTool
from plotpy.cross_section import ObliqueCrossSection
from plotpy.tools import ObliqueCrossSectionTool, OCSPanelTool


class OCSImageDialog(ImageDialog):
    def register_image_tools(self):
        ImageDialog.register_image_tools(self)
        for tool in (ObliqueCrossSectionTool, OCSPanelTool, ImageMaskTool):
            self.add_tool(tool)
        
    def create_plot(self, options, row=0, column=0, rowspan=1, columnspan=1):
        ImageDialog.create_plot(self, options, row, column, rowspan, columnspan)
        ra_panel = ObliqueCrossSection(self)
        splitter = self.plot_widget.xcsw_splitter
        splitter.addWidget(ra_panel)
        splitter.setStretchFactor(splitter.count()-1, 1)
        splitter.setSizes(list(splitter.sizes())+[2])
        self.add_panel(ra_panel)

def test():
    """Test"""
    # -- Create QApplication
    import plotpy
    _app = plotpy.qapplication()
    # --
    win = OCSImageDialog(toolbar=True,
                         wintitle="Oblique averaged cross section test")
    win.resize(600, 600)
    
#    from plotpy.tests.image import compute_image
#    data = np.array((compute_image(4000, grid=False)+1)*32e3, dtype=np.uint16)
#    image = make.maskedimage(data, colormap="bone", show_mask=True)

    filename = osp.join(osp.dirname(__file__), "brain_cylinder.png")
    image = make.maskedimage(filename=filename, colormap="bone")

    plot = win.get_plot()
    plot.add_item(image)
    win.exec_()

if __name__ == "__main__":
    test()
