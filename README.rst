Google Licenseclassifier pipeline for ScanCode.io
=================================================

This package contributes a new pipeline to ScanCode.io. It is based on https://github.com/AvishrantsSh/GoLicense-Classifier.

Install as plug-in
-------------------

To use Google Licenseclassifier pipeline in your local ScanCode.io instance, use

.. code-block:: bash

    pip install scancodeio.io-pipeline-glc_scan

Development
-----------

To get started, clone the repository

.. code-block:: bash
        
        git clone https://github.com/nexB/scancodeio.io-pipeline-glc_scan.git


and, set up your development environment using

.. code-block:: bash

    ./configure --dev

To run unit tests, use

.. code-block:: bash

    venv/bin/python runtests.py