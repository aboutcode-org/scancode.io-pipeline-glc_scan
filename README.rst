Google Licenseclassifier pipeline for ScanCode.io
=================================================

This package contributes a new pipeline to ScanCode.io. 

Based on https://github.com/AvishrantsSh/GoLicense-Classifier.

Install as plug-in
-------------------

To use Google Licenseclassifier pipeline in your local ScanCode.io instance, use

.. code-block:: bash

    pip install scancodeio_glc_plugin

Development
-----------

To get started, clone the repository

.. code-block:: bash
        
        git clone https://github.com/nexB/scancode.io-pipeline-glc_scan.git

and, set up your development environment using

.. code-block:: bash

    ./configure --dev

Once the setup is complete, fetch the latest scancode.io instance using

.. code-block:: bash

    venv/bin/pip install scancodeio@git+https://github.com/nexb/scancode.io.git 


Once the environment is set up, you can run the tests using

.. code-block:: bash

    venv/bin/python runtests.py