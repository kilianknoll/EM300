em300
==========



Introduction
------------

This Python library provides a pure Python interface to access the EM300 Energymanager from TQ Automation (which seems to be similar / identical to Kostal EM300LR)

Based on:

https://www.tq-automation.com/Service-Support/Downloads/Downloads-Energiemanagement

Using the JSON Documentation: https://www.tq-automation.com/content/download/10996/file/TQ%20Energy%20Manager%20-%20JSON-API.0104.pdf

Tested  with Python version 3.5, 3.6 and 3.8.




Features
~~~~~~~~

* Read variety of the OBIS Codes from the  Energy Manager and puts them into a list


Tested with 
~~~~~~~~~~~~~~~~

* Windows
* Raspberry






Installation
------------
Clone / Download repo and use em300.py 


Getting started
---------------

To use ``em300`` in a project take a look at the __main__ section in em300.py how to include it in your environment



Disclaimer
----------

.. Warning::

   Please note that any incorrect or careless usage of this module as well as
   errors in the implementation may harm your Smart Energy Manager !

   Therefore, the author does not provide any guarantee or warranty concerning
   to correctness, functionality or performance and does not accept any liability
   for damage caused by this module, examples or mentioned information.

   **Thus, use it on your own risk!**


License
-------

Distributed under the terms of the `GNU General Public License v3 <https://www.gnu.org/licenses/gpl-3.0.en.html>`_.
