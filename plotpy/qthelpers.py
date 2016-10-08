# -*- coding: utf-8 -*-
#
# Copyright © 2011 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see plotpy/__init__.py for details)

"""
qthelpers
---------

The ``plotpy.qthelpers`` module provides helper functions for developing 
easily Qt-based graphical user interfaces with plotpy.

Ready-to-use open/save dialogs:
    :py:data:`plotpy.qthelpers.exec_image_save_dialog`
        Executes an image save dialog box (QFileDialog.getSaveFileName)
    :py:data:`plotpy.qthelpers.exec_image_open_dialog`
        Executes an image open dialog box (QFileDialog.getOpenFileName)
    :py:data:`plotpy.qthelpers.exec_images_open_dialog`
        Executes an image*s* open dialog box (QFileDialog.getOpenFileNames)   

Reference
~~~~~~~~~

.. autofunction:: text_to_qcolor
.. autofunction:: create_action
.. autofunction:: create_toolbutton
.. autofunction:: create_groupbox
.. autofunction:: keybinding
.. autofunction:: add_separator
.. autofunction:: add_actions
.. autofunction:: get_std_icon
.. autofunction:: exec_image_save_dialog
.. autofunction:: exec_image_open_dialog
.. autofunction:: exec_images_open_dialog
"""

from __future__ import print_function

import sys
import os.path as osp

from plotpy.qt.QtGui import (QAction, QApplication, QColor, QHBoxLayout,
                             QKeySequence, QLabel, QLineEdit, QMenu, QIcon,
                             QPushButton, QStyle, QToolButton, QVBoxLayout,
                             QWidget, QGroupBox, QMessageBox)
from plotpy.qt.QtCore import Qt
from plotpy.qt.compat import getsavefilename, getopenfilename, getopenfilenames
from plotpy.py3compat import to_text_string

# Local imports
from plotpy.config import _
from plotpy import io


def text_to_qcolor(text):
    """Create a QColor from specified string"""
    color = QColor()
    if not is_text_string(text): # testing for QString (PyQt API#1)
        text = str(text)
    if text.startswith('#') and len(text)==7:
        correct = '#0123456789abcdef'
        for char in text:
            if char.lower() not in correct:
                return color
    elif text not in list(QColor.colorNames()):
        return color
    color.setNamedColor(text)
    return color

def create_action(parent, title, triggered=None, toggled=None,
                  shortcut=None, icon=None, tip=None, checkable=None,
                  context=Qt.WindowShortcut, enabled=None):
    """
    Create a new QAction
    """
    action = QAction(title, parent)
    if triggered:
        if checkable:
            action.triggered.connect(triggered)
        else:
            action.triggered.connect(lambda checked=False: triggered())
    if checkable is not None:
        # Action may be checkable even if the toggled signal is not connected
        action.setCheckable(checkable)
    if toggled:
        action.toggled.connect(toggled)
        action.setCheckable(True)
    if icon is not None:
        assert isinstance(icon, QIcon)
        action.setIcon( icon )
    if shortcut is not None:
        action.setShortcut(shortcut)
    if tip is not None:
        action.setToolTip(tip)
        action.setStatusTip(tip)
    if enabled is not None:
        action.setEnabled(enabled)
    action.setShortcutContext(context)
    return action

def create_toolbutton(parent, icon=None, text=None, triggered=None, tip=None,
                      toggled=None, shortcut=None, autoraise=True,
                      enabled=None):
    """Create a QToolButton"""
    if autoraise:
        button = QToolButton(parent)
    else:
        button = QPushButton(parent)
    if text is not None:
        button.setText(text)
    if icon is not None:
        if is_text_string(icon):
            icon = get_icon(icon)
        button.setIcon(icon)
    if text is not None or tip is not None:
        button.setToolTip(text if tip is None else tip)
    if autoraise:
        button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        button.setAutoRaise(True)
    if triggered is not None:
        button.clicked.connect(lambda checked=False: triggered())
    if toggled is not None:
        button.toggled.connect(toggled)
        button.setCheckable(True)
    if shortcut is not None:
        button.setShortcut(shortcut)
    if enabled is not None:
        button.setEnabled(enabled)
    return button
    
def create_groupbox(parent, title=None, toggled=None, checked=None,
                    flat=False, layout=None):
    """Create a QGroupBox"""
    if title is None:
        group = QGroupBox(parent)
    else:
        group = QGroupBox(title, parent)
    group.setFlat(flat)
    if toggled is not None:
        group.setCheckable(True)
        if checked is not None:
            group.setChecked(checked)
        group.toggled.connect(toggled)
    if layout is not None:
        group.setLayout(layout)
    return group

def keybinding(attr):
    """Return keybinding"""
    ks = getattr(QKeySequence, attr)
    return QKeySequence.keyBindings(ks)[0].toString()

def add_separator(target):
    """Add separator to target only if last action is not a separator"""
    target_actions = list(target.actions())
    if target_actions:
        if not target_actions[-1].isSeparator():
            target.addSeparator()

def add_actions(target, actions):
    """
    Add actions (list of QAction instances) to target (menu, toolbar)
    """
    for action in actions:
        if isinstance(action, QAction):
            target.addAction(action)
        elif isinstance(action, QMenu):
            target.addMenu(action)
        elif action is None:
            add_separator(target)

def get_std_icon(name, size=None):
    """
    Get standard platform icon
    Call 'show_std_icons()' for details
    """
    if not name.startswith('SP_'):
        name = 'SP_'+name
    icon = QWidget().style().standardIcon( getattr(QStyle, name) )
    if size is None:
        return icon
    else:
        return QIcon( icon.pixmap(size, size) )

class ShowStdIcons(QWidget):
    """
    Dialog showing standard icons
    """
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        layout = QHBoxLayout()
        row_nb = 14
        cindex = 0
        for child in dir(QStyle):
            if child.startswith('SP_'):
                if cindex == 0:
                    col_layout = QVBoxLayout()
                icon_layout = QHBoxLayout()
                icon = get_std_icon(child)
                label = QLabel()
                label.setPixmap(icon.pixmap(32, 32))
                icon_layout.addWidget( label )
                icon_layout.addWidget( QLineEdit(child.replace('SP_', '')) )
                col_layout.addLayout(icon_layout)
                cindex = (cindex+1) % row_nb
                if cindex == 0:
                    layout.addLayout(col_layout)                    
        self.setLayout(layout)
        self.setWindowTitle('Standard Platform Icons')
        self.setWindowIcon(get_std_icon('TitleBarMenuButton'))

def show_std_icons():
    """
    Show all standard Icons
    """
    app = QApplication(sys.argv)
    dialog = ShowStdIcons(None)
    dialog.show()
    sys.exit(app.exec_())


#===============================================================================
# Ready-to-use open/save dialogs
#===============================================================================
def exec_image_save_dialog(parent, data, template=None,
                           basedir='', app_name=None):
    """
    Executes an image save dialog box (QFileDialog.getSaveFileName)
        * parent: parent widget (None means no parent)
        * data: image pixel array data
        * template: image template (pydicom dataset) for DICOM files
        * basedir: base directory ('' means current directory)
        * app_name (opt.): application name (used as a title for an eventual 
          error message box in case something goes wrong when saving image)
    
    Returns filename if dialog is accepted, None otherwise
    """
    saved_in, saved_out, saved_err = sys.stdin, sys.stdout, sys.stderr
    sys.stdout = None
    filename, _filter = getsavefilename(parent, _("Save as"), basedir,
        io.iohandler.get_filters('save', dtype=data.dtype, template=template))
    sys.stdin, sys.stdout, sys.stderr = saved_in, saved_out, saved_err
    if filename:
        filename = to_text_string(filename)
        kwargs = {}
        if osp.splitext(filename)[1].lower() == '.dcm':
            kwargs['template'] = template
        try:
            io.imwrite(filename, data, **kwargs)
            return filename
        except Exception as msg:
            import traceback
            traceback.print_exc()
            QMessageBox.critical(parent,
                 _('Error') if app_name is None else app_name,
                 (_("%s could not be written:") % osp.basename(filename))+\
                 "\n"+str(msg))
            return

def exec_image_open_dialog(parent, basedir='', app_name=None,
                           to_grayscale=True, dtype=None):
    """
    Executes an image open dialog box (QFileDialog.getOpenFileName)
        * parent: parent widget (None means no parent)
        * basedir: base directory ('' means current directory)
        * app_name (opt.): application name (used as a title for an eventual 
          error message box in case something goes wrong when saving image)
        * to_grayscale (default=True): convert image to grayscale
    
    Returns (filename, data) tuple if dialog is accepted, None otherwise
    """
    saved_in, saved_out, saved_err = sys.stdin, sys.stdout, sys.stderr
    sys.stdout = None
    filename, _filter = getopenfilename(parent, _("Open"), basedir,
                                io.iohandler.get_filters('load', dtype=dtype))
    sys.stdin, sys.stdout, sys.stderr = saved_in, saved_out, saved_err
    filename = to_text_string(filename)
    try:
        data = io.imread(filename, to_grayscale=to_grayscale)
    except Exception as msg:
        import traceback
        traceback.print_exc()
        QMessageBox.critical(parent,
             _('Error') if app_name is None else app_name,
             (_("%s could not be opened:") % osp.basename(filename))+\
             "\n"+str(msg))
        return
    return filename, data

def exec_images_open_dialog(parent, basedir='', app_name=None,
                            to_grayscale=True, dtype=None):
    """
    Executes an image*s* open dialog box (QFileDialog.getOpenFileNames)
        * parent: parent widget (None means no parent)
        * basedir: base directory ('' means current directory)
        * app_name (opt.): application name (used as a title for an eventual 
          error message box in case something goes wrong when saving image)
        * to_grayscale (default=True): convert image to grayscale
    
    Yields (filename, data) tuples if dialog is accepted, None otherwise
    """
    saved_in, saved_out, saved_err = sys.stdin, sys.stdout, sys.stderr
    sys.stdout = None
    filenames, _filter = getopenfilenames(parent, _("Open"), basedir,
                                io.iohandler.get_filters('load', dtype=dtype))
    sys.stdin, sys.stdout, sys.stderr = saved_in, saved_out, saved_err
    filenames = [to_text_string(fname) for fname in list(filenames)]
    for filename in filenames:
        try:
            data = io.imread(filename, to_grayscale=to_grayscale)
        except Exception as msg:
            import traceback
            traceback.print_exc()
            QMessageBox.critical(parent,
                 _('Error') if app_name is None else app_name,
                 (_("%s could not be opened:") % osp.basename(filename))+\
                 "\n"+str(msg))
            return
        yield filename, data
    

if __name__ == "__main__":
    from plotpy.utils import pairs
    print(list( pairs( list(range(5)) ) ))
    show_std_icons()
