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
