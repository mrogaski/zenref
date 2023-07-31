The Zen of Reffing Roller Derby
===============================

**The Zen of Reffing Roller Derby** is a training manual for referees.

It was created by Stephen “Axis of Stevil” Lorimor and is currently maintained by Isabelle “Blocktopus” Santos.


Contributing
------------

Typos, errors,...
.................

If you are familiar with Gitlab, you can directly `create an issue <https://framagit.org/roller-derby/the-zen-of-reffing/-/issues>`_. 

You can also `email an issue to the project <gitlab-incoming+roller-derby-the-zen-of-reffing-90983-bx2ggfwyjsio1jubwwubp8u0m-issue@framagit.org>`_.

Translation
...........

This project is looking for translators. Reach out if you'd like to participate!

- Mastodon: https://framapiaf.org/@Moutmout
- Twitter: @MoutmoutInSpace
- Email: isabelle [ dot ] santos [ at ] protonmail [ dot ] com

  
Building the zen
----------------

You can download these files to your computer and build the Zen of Reffing locally.

To build, you need to have `Sphinx <https://sublime-and-sphinx-guide.readthedocs.io/en/latest/index.html>`_ installed.If you never used Sphinx before, follow the instructions on the Sphinx website to install it on your machine.

The Zen of Reffing is available in an HTML format for online viewing and a PDF format for printing.

Build the HTML version
......................

To build and view run the following in a terminal:

.. code::
   
   cd docs
   make html
   cd build/html/
   firefox index.html

   
Build the PDF version
.....................

To build the PDF version, you first need to have a sphinx plugin installed.

.. code::

   python -m pip install sphinx furo rst2pdf
   

.. code::
   
   cd docs
   sphinx-build -b pdf source build


You can then view the file `docs/build/rst2pdf.pdf`.
