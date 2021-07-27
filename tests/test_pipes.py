from pathlib import Path
import unittest
from LicenseClassifier.classifier import LicenseClassifier
from scancode_glc_plugin.pipes import glc


class GLCPipeTest(unittest.TestCase):
    data_location = Path(__file__).parent / "data"

    def test_scanpipe_pipes_glc_scan_file(self):
        input_location = str(self.data_location / "apache-1.1.txt")
        classifier = LicenseClassifier()
        scan_results = glc.scan_file(classifier, input_location)
        expected_result = {
            "path": input_location,
            "licenses": [
                {
                    "key": "apache-1.1",
                    "score": 1,
                    "start_line": 1,
                    "end_line": 39,
                    "start_index": 0,
                    "end_index": 338,
                    "category": "Permissive",
                }
            ],
            "license_expressions": ["apache-1.1"],
            "copyrights": [
                {
                    "value": "Copyright (c) 2000 The Apache Software"
                    " Foundation. All rights reserved.",
                    "start_index": 25,
                    "end_index": 96,
                }
            ],
            "holders": [
                {
                    "value": "The Apache Software Foundation",
                    "start_index": 44,
                    "end_index": 74,
                }
            ],
            "scan_errors": [],
        }
        self.assertEqual(expected_result, scan_results)

    def test_scanpipe_pipes_glc_scan_directory(self):
        input_location = str(self.data_location)
        scan_results = glc.scan_directory(input_location)
        expected_keys = [
            "header",
            "files",
        ]
        self.assertEqual(sorted(expected_keys), sorted(scan_results.keys()))
        self.assertEqual(1, len(scan_results.get("files", [])))
