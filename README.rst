Google License Classifier pipeline for ScanCode.io
==================================================

|pypi-version| |code-style| |license|

This package contributes a new pipeline based on `Google License Classifier
<https://pkg.go.dev/github.com/google/licenseclassifier/v2>`_ to ScanCode.io. The pipeline is
capable of identifying license expressions as well as copyright statements within the code,
without compromising with speed and accuracy.

Based on `GoLicense Classifier <https://github.com/AvishrantsSh/GoLicense-Classifier>`_.

Installation
------------

To use Google License Classifier pipeline in your local ScanCode.io instance,
install the python package from PyPI using

.. code-block:: bash

    pip install scancodeio_glc_plugin

The newly installed pipeline will now be available for use in ScanCode.io.

Development
-----------

To get started, create a fork of this project and clone it to your local machine.

Set up your development environment using

.. code-block:: bash

    ./configure --dev

Once the setup is complete, fetch the latest scancode.io instance from GitHub. This step is required
to ensure that all the dependencies of the pipeline are met.

.. code-block:: bash

    venv/bin/pip install scancodeio@git+https://github.com/nexb/scancode.io.git


Once the environment is set up, run the test suite to ensure that everything is in
working order.

.. code-block:: bash

    venv/bin/python runtests.py


.. |pypi-version| image:: https://img.shields.io/pypi/v/scancodeio_glc_plugin.svg?style=for-the-badge
    :alt: PyPI Version
.. |license| image:: https://img.shields.io/badge/License-Apache%202.0-green.svg?style=for-the-badge
    :alt: License
.. |code-style| image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
    :alt: Code Style
