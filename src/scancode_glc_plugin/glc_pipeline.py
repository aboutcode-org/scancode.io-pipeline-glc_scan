#
# Copyright (c) nexB Inc. and others.
# SPDX-License-Identifier: Apache-2.0
#
# Visit https://aboutcode.org and https://github.com/nexB/ for support and download.
# ScanCode is a trademark of nexB Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from scanpipe.pipelines import scan_codebase
from scanpipe.pipes import make_codebase_resource, rootfs

from scancode_glc_plugin.pipes import glc


class LicenseClassifierScan(scan_codebase.ScanCodebase):
    """
    Pipeline to scan codebase for Copyright and License Details
    """

    @classmethod
    def steps(cls):
        return (
            cls.copy_inputs_to_codebase_directory,
            cls.run_extractcode,
            cls.collect_and_create_codebase_resources,
            cls.run_license_classifier,
            cls.csv_output,
        )

    def collect_and_create_codebase_resources(self):
        """
        Collect and create all files as CodebaseResource.
        """
        for resource in rootfs.get_resources(str(self.project.codebase_path)):
            make_codebase_resource(
                project=self.project,
                location=resource.location,
            )

    def run_license_classifier(self):
        """
        Scan codebase for license and copyright details
        and save results as CodebaseResource
        """
        glc.scan_and_update_codebase_resources(self.project)
