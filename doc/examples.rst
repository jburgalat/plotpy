.. _examples:

Examples
========

The test launcher
-----------------

A lot of examples are available in the `plotpy` test module ::

    from plotpy import tests
    tests.run()

The two lines above execute the `plotpy test launcher`:

.. image:: images/screenshots/__init__.png


Curve plotting
--------------

Basic curve plotting
~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ../plotpy/tests/plot.py
   :start-after: SHOW
   :end-before: Workaround for Sphinx v0.6 bug: empty 'end-before' directive

.. image:: images/screenshots/plot.png

Computations on curves
~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ../plotpy/tests/computations.py
   :start-after: SHOW
   :end-before: Workaround for Sphinx v0.6 bug: empty 'end-before' directive

.. image:: images/screenshots/computations.png


Curve fitting
-------------

.. literalinclude:: ../plotpy/tests/fit.py
   :start-after: SHOW
   :end-before: Workaround for Sphinx v0.6 bug: empty 'end-before' directive

.. image:: images/screenshots/fit.png


Image visualization
-------------------

Image contrast adjustment
~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ../plotpy/tests/contrast.py
   :start-after: SHOW
   :end-before: Workaround for Sphinx v0.6 bug: empty 'end-before' directive

.. image:: images/screenshots/contrast.png

Image cross-sections
~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ../plotpy/tests/cross_section.py
   :start-after: SHOW
   :end-before: Workaround for Sphinx v0.6 bug: empty 'end-before' directive

.. image:: images/screenshots/cross_section.png

Transformable images
~~~~~~~~~~~~~~~~~~~~

Affine transforms example on 3000x3000 images (real-time transforms):

.. literalinclude:: ../plotpy/tests/transform.py
   :start-after: SHOW
   :end-before: Workaround for Sphinx v0.6 bug: empty 'end-before' directive

.. image:: images/screenshots/transform.png

Image rectangular filter
~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ../plotpy/tests/imagefilter.py
   :start-after: SHOW
   :end-before: Workaround for Sphinx v0.6 bug: empty 'end-before' directive

.. image:: images/screenshots/imagefilter.png


Histograms
----------

2-D histogram
~~~~~~~~~~~~~

.. literalinclude:: ../plotpy/tests/hist2d.py
   :start-after: SHOW
   :end-before: Workaround for Sphinx v0.6 bug: empty 'end-before' directive

.. image:: images/screenshots/hist2d.png


Other examples
--------------

Dot Array Demo
~~~~~~~~~~~~~~

.. literalinclude:: ../plotpy/tests/dotarraydemo.py
   :start-after: SHOW
   :end-before: Workaround for Sphinx v0.6 bug: empty 'end-before' directive

.. image:: images/screenshots/dotarraydemo.png

Image plot tools
~~~~~~~~~~~~~~~~

.. literalinclude:: ../plotpy/tests/image_plot_tools.py
   :start-after: SHOW
   :end-before: Workaround for Sphinx v0.6 bug: empty 'end-before' directive

.. image:: images/screenshots/image_plot_tools.png

Real-time Mandelbrot plotting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ../plotpy/tests/mandelbrot.py
   :start-after: SHOW
   :end-before: Workaround for Sphinx v0.6 bug: empty 'end-before' directive

.. image:: images/screenshots/mandelbrot.png

Simple application
~~~~~~~~~~~~~~~~~~

.. literalinclude:: ../plotpy/tests/simple_window.py
   :start-after: SHOW
   :end-before: Workaround for Sphinx v0.6 bug: empty 'end-before' directive

.. image:: images/screenshots/simple_window.png
