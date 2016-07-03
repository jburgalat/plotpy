Migrating from version 2 to version 3
=====================================

The main change between version 2 and version 3 is the basic plotting library 
on which `plotpy` is based on:

  * `plotpy` version 2: depends on `PyQwt`, the Python bindings to `Qwt` C++ 
    library -- only supports PyQt4.

  * `plotpy` version 3: depends on `PythonQwt`, a new library written from 
    scratch to continue supporting `Qwt` API through a pure Python 
    reimplementation of its main classes (`QwtPlot`, `QwtPlotItem`, 
    `QwtPlotCanvas`, ...) -- supports PyQt4, PyQt5 and PySide (PySide support 
    is theoretical: not tested).

Another major change is the switch from old-style to new-style signals and 
slots. The :py:mod:`plotpy.signals` module is now empty because it used to 
collect strings for old-style signals: however, it still contains 
documentation on available signals.

Examples
~~~~~~~~

Switching from `PyQwt` to `PythonQwt` in your code::

    from PyQt4.Qwt5 import QwtPlot  # PyQwt (supports only PyQt4)

    from qwt import QwtPlot  # PythonQwt (supports PyQt4, PyQt5 and eventually PySide)

Switching from `plotpy 2` to `plotpy 3`::

    plot = get_plot_instance()  # plot is a QwtPlot instance
    
    ## plotpy 2:
    from plotpy.signals import SIG_ITEM_MOVED
    plot.connect(plot, SIG_ITEM_MOVED, item_was_moved)
    
    ## plotpy 3:
    plot.SIG_ITEM_MOVED.connect(item_was_moved)
