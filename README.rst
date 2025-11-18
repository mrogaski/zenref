The Zen of Reffing Roller Derby
===============================

|cc-by-nc-sa-badge|

.. |cc-by-nc-sa-badge| image:: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
    :target: http://creativecommons.org/licenses/by-nc-sa/4.0/

**The Zen of Reffing Roller Derby** is a training manual for roller derby referees.

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

This project is looking for translators. Reach out if you'd like to participate!

- Bluesky: `@skogkatt.io <https://bsky.app/profile/skogkatt.io>`_
- Discord: `skogkatt668 <https://discordapp.com/users/132196734423007232>`_
- Email: `mrogaski+zenref@pobox.com <mailto:mrogaski+zenref@pobox.com>`_

  
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

   
Build the PDF version
.....................

To build the PDF version, you first need to have a sphinx plugin installed.

.. code::
   
   uv run sphinx-build -b pdf source build


You can then view the file `build/rst2pdf.pdf`.