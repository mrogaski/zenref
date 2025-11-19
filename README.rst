The Zen of Reffing Roller Derby
===============================

|cc-badge|
|netlify-badge|

.. |cc-badge| image:: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
    :target: http://creativecommons.org/licenses/by-nc-sa/4.0/
.. |netlify-badge| image:: https://api.netlify.com/api/v1/badges/b008e4a2-1a0e-46d0-9576-3d0b2b0abe31/deploy-status
    :target: https://app.netlify.com/projects/zenref/deploys

**The Zen of Reffing Roller Derby** is a training manual for roller derby referees.

.. rubric::
    https://zenref.rollerderby.fyi/

It was created by Stephen "Axis of Stevil" Lorimor, updated by Isabelle “Blocktopus” Santos, and is currently maintained by Mark "Trampling Bias" Rogaski.

License
-------

This work is licensed under a
`Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License <http://creativecommons.org/licenses/by-nc-sa/4.0/>`_.

|cc-by-nc-sa-image|

.. |cc-by-nc-sa-image| image:: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
    :target: http://creativecommons.org/licenses/by-nc-sa/4.0/

Contributing
------------

The Zen of Reffing uses the `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ format.

Reporting errors
................

If you are familiar with Github, you can directly `create an issue <https://github.com/mrogaski/zenref/issues>`_.

You can also `email an issue to the project maintainer <mrogaski+zenref@pobox.com>`_.

Translation
...........

This project is looking for translators. Reach out in the `discussions <https://github.com/mrogaski/zenref/discussions>`_ if you'd like to participate!

Building the Zen
----------------

You can clone or download these files to your computer and build the Zen of Reffing locally.

To build, you need to have `Python <https://wiki.python.org/moin/BeginnersGuide/Download>`_ and `uv <https://docs.astral.sh/uv/getting-started/installation/>`_ installed. If you never used Sphinx before, follow the instructions on the Sphinx website to install it on your machine.

The Zen of Reffing is available in an HTML format for online viewing and a PDF format for printing.

Build the HTML version
......................

To build and view run the following in a terminal:

.. code::

   make html
   firefox build/html/index.html
