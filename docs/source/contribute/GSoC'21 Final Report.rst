.. _gsoc_report_avishrant_sharma:

Google Summer of Code 2021 - Final Report
=========================================

Organization: AboutCode
------------------------

Project Title: Integration of Alternate Code Analysis Tools
------------------------------------------------------------

**Contributor:** `Avishrant Sharma <https://github.com/AvishrantsSh>`_

**Mentors:** `Philippe Ombredanne`_, `Thomas Druez`_, `Tushar Goel`_

Overview
--------
The purpose of this project is to provide a way to implement and integrate alternate code analysis
tools ranging from license detection to copyright scanning and beyond in ScanCode.io in the form of
installable packages and wheels.

As an example of this kind of integration, a Python wrapper package was built around
`Google License Classifier v2`_
to provide license detection as a new installable pipeline.

Implementation
--------------
Over the course of this project, spanning over three months, we worked upon several
key components. A high-level overview of these components is provided below.

Converting Google License Classifier v2 to a C-style shared library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- One of the main goals of this project was to convert Google License Classifier to a form
  that can be further compiled into a **C-shared library**.

- Since the License Classifier was written in **Golang**, there was native support for shared
  libraries. However, data marshaling and datatype conversion was required at several steps.

- A **main package** file with **cgo bindings** was written to achieve this objective.

- Further, a **copyright notification** detection function was also ported from the **v1** package
  for additional functionality.

- See `Google License Classifier with cgo bindings`_ for more details.

Building Python wrapper and generating License Key Mappings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- A Python wrapper was built around the shared library to access all the underlying functionality
  using **ctypes**.

- Data marshaling and error detection were handled by the package itself.

- Further, license key mapping between License Classifier and ScanCode.io was generated and
  integrated into the package. It helps in maintaining consistency between the two.

- This Python package is available at `GoLicense-Classifier`_

Developing a pipeline to run license detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- After developing the package, it was necessary to integrate it into a pipeline that can be used
  to execute the License Classifier from the ScanCode.io app.

- The pipeline's task was to validate the output of the package and to handle the data transaction
  to ScanCode.io models.

Packaging the pipeline and deploying to PyPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- The final goal of this project was to deploy the distribution archives to PyPI.

- It involved configuring package files, manifests, setup configurations etc.

- Final pipeline package is available at `Scancode.io GLC Plugin`_

Challenges
----------
The main hurdle during this project was to generate cgo bindings for Google License
Classifier, as there was no clear documentation available about the codebase. We spent a lot of
time digging around the codebase, trying to understand the functions and how to make them cgo
compatible.

Other Contributions
-------------------
Apart from what was stated in the proposal, I also contributed a few PRs and issues to not only
ScanCode.io but also to other tools and packages of my organization. A summary of the same is as
follows:

PRs
~~~

========================================= =================== ===========================================================
Project                                   Link                Description
========================================= =================== ===========================================================
ScanCode.io                               `#146`_             Drag and drop feature
ScanCode.io                               `#158`_             Project name cleanup before saving
ScanCode.io                               `#276`_, `#291`_    Add document section on Pipeline Packaging
ScanCode.io                               `#297`_             Update filters to include (No values detected)
ScanCode.io-pipeline-glc_scan             `#1`_               Initial setup of pipeline structure
========================================= =================== ===========================================================

Issues
~~~~~~

================================= ================== =================================================================
Project                           Link               Description
================================= ================== =================================================================
ScanCode.io                       `#224`_            Confusing documentation for ``make_codebase_resource``
ScanCode.io                       `#230`_            ``matched_rule`` key error in custom pipelines
ScanCode-Toolkit                  `#2596`_           Document ScanCode JSON output format
ScanCode-Toolkit                  `#2593`_           Babelstone IDS license not detected by ScanCode toolkit
Container-Inspector               `#34`_             Incorrect information for ``Resource`` created for a directory
================================= ================== =================================================================

Acknowledgments
----------------

I had a wonderful time working on this project this summer. I got an opportunity to learn so many
things and meet amazing people in the open-source community. It wouldn't have been possible without
the constant support and guidance of my mentors
`Philippe Ombredanne`_, `Thomas Druez`_, and `Tushar Goel`_.

Lastly, I would like to thank my family, friends, and all the people who helped me out and supported
me during the project.

Links
-----
1. `ScanCode.io`_
2. `Google License Classifier v2`_
3. `Google License Classifier with cgo bindings`_
4. `GoLicense-Classifier`_
5. `Scancode.io GLC Plugin`_
6. `GoLicense-Classifier Source Code`_
7. `ScanCode.io GLC Plugin Source Code`_

.. _#146: https://github.com/aboutcode-org/ScanCode.io/pull/146
.. _#158: https://github.com/aboutcode-org/ScanCode.io/pull/158
.. _#276: https://github.com/aboutcode-org/ScanCode.io/pull/276
.. _#291: https://github.com/aboutcode-org/scancode.io/pull/291
.. _#297: https://github.com/aboutcode-org/scancode.io/pull/297
.. _#1: https://github.com/aboutcode-org/ScanCode.io-pipeline-glc_scan/pull/1

.. _#224: https://github.com/aboutcode-org/ScanCode.io/issues/224
.. _#230: https://github.com/aboutcode-org/ScanCode.io/issues/230
.. _#2596: https://github.com/aboutcode-org/ScanCode-toolkit/issues/2596
.. _#2593: https://github.com/aboutcode-org/ScanCode-toolkit/issues/2593
.. _#34: https://github.com/aboutcode-org/container-inspector/issues/34

.. _Philippe Ombredanne: https://github.com/pombredanne
.. _Thomas Druez: https://github.com/tdruez
.. _Tushar Goel: https://github.com/TG1999

.. _ScanCode.io: https://github.com/aboutcode-org/scancode.io
.. _Google License Classifier v2: https://pkg.go.dev/github.com/google/licenseclassifier/v2
.. _GoLicense-Classifier: https://pypi.org/project/golicense-classifier/
.. _Scancode.io GLC Plugin: https://pypi.org/project/scancodeio-glc-plugin/
.. _ScanCode.io GLC Plugin Source Code: https://github.com/aboutcode-org/scancode.io-pipeline-glc_scan
.. _GoLicense-Classifier Source Code: https://github.com/AvishrantsSh/GoLicense-Classifier/
.. _Google License Classifier with cgo bindings: https://github.com/AvishrantsSh/cgo_licenseclassifier
