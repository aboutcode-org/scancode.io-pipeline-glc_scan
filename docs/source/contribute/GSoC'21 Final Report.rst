.. _gsoc_report_avishrant_sharma:

Google Summer of Code 2021 - Final Report
=========================================

Organization: AboutCode
------------------------

Project Title: Integration of Alternate Code Analysis Tools
------------------------------------------------------------

**Contributor:** `Avishrant Sharma <https://github.com/AvishrantsSh>`_

**Mentors:** `Philippe Ombredanne <https://github.com/pombredanne>`_, `Thomas Druez <https://github.com/tdruez>`_,
`Tushar Goel <https://github.com/TG1999>`_

----

Overview
--------
This project's purpose is to provide a way to implement and integrate alternate code analysis tools
ranging from license detection to copyright scanning and beyond in ScanCode.io in the form of
installable packages and wheels.

As an example of this kind of integration, a Python wrapper package was built around
`Google License Classifier v2 <https://pkg.go.dev/github.com/google/licenseclassifier/v2>`__
to provide license detection as a new installable pipeline.

Implementation
--------------
Over the course of this project, spanning over three months, we worked upon several
key componenets. A high level overview of these components is provided below.

Converting Google License Classifier v2 to a C-style shared library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- One of the first goals of this project was to convert Google License Classifier to a form
  that can be further converted to a **C-shared library**.

- Since the License Classifier was written in **Golang**, there was native support for shared
  libraries. However, data marshaling and datatype conversion was required at several steps.

- A **main package** file with **cgo bindings** had to be written for proper compilation.

- Additionally, a **copyright notification** detection function was also ported from v1 package
  for additional functionality.

Building Python wrapper and generating License Key Mappings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- A Python wrapper was built around the shared library to access all the underlying functionality
  using **ctypes**.

- License key mappings, data marshaling, and error detection were handled by the package itself.

Developing a pipeline to run license detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Packaging the pipeline and deploying to PyPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Challenges
----------
A major hurdle during the course of this project was to generate cgo bindings for Google License
Classifier, as there was no clear documentation available about the codebase. We spent a lot of
time digging around the codebase, trying to understand the functions and how to make them cgo compatible.

Other Contributions
-------------------
Apart from what was stated in the proposal, I also contributed a few PRs and issues to not only
ScanCode.io but also to other tools and packages of my organization.

A summary of the same is as follows

PRs
~~~
.. list-table::
   :widths: 20 20 40
   :header-rows: 1

   * - Project
     - Link
     - Description
   * - Scancode.io
     - `#146 <https://github.com/nexB/scancode.io/pull/146>`_
     - Drag and drop feature
   * - Scancode.io
     - `#158 <https://github.com/nexB/scancode.io/pull/158>`_
     - Project name cleanup before saving
   * - Scancode.io
     - `#276 <https://github.com/nexB/scancode.io/pull/276>`_
     - Add document section on Pipeline Packaging
   * - Scancode.io-pipeline-glc_scan
     - `#1 <https://github.com/nexB/scancode.io-pipeline-glc_scan/pull/1>`_
     - Initial setup of pipeline structure
     
Issues
~~~~~~
.. list-table::
     :widths: 20 20 40
     :header-rows: 1
  
     * - Project
       - Link
       - Description
     * - Scancode.io
       - `#224 <https://github.com/nexB/scancode.io/issues/224>`_
       - **matched_rule** key error in custom pipelines
     * - Scancode.io
       - `#230 <https://github.com/nexB/scancode.io/issues/230>`_
       - Confusing documentation for **make_codebase_resource**

       
Acknowledgments
----------------

Links
-----
1. `Google License Classifier v2 <https://pkg.go.dev/github.com/google/licenseclassifier/v2>`__
2. `cgo bindings for Google License Classifier <https://github.com/AvishrantsSh/cgo_licenseclassifier>`_
3. `Go License-Classifier <https://pypi.org/project/golicense-classifier/>`_
4. `Scancode.io GLC Plugin <https://github.com/nexB/scancode.io-pipeline-glc_scan>`_
