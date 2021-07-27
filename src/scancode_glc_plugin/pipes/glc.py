from LicenseClassifier.classifier import LicenseClassifier
from scanpipe.pipes import scancode


def scan_directory(location):
    """
    Run a license and copyright scan on directory at `location`,
    using golicense-classifier.

    Parameters
    ----------
    location : str
        Location of directory to scan.
    """
    classifier = LicenseClassifier()
    result = classifier.scan_directory(location)
    return result


def scan_file(classifier, location):
    """
    Run a license and copyright scan on file at `location`,
    using golicense-classifier.

    Parameters
    ----------
    classifier : LicenseClassifier()
        `LicenseClassifier` instance for scanning files

    location : str
        Location of the file
    """
    result = classifier.scan_file(location)
    return result


def scan_and_update_codebase_resources(project, scan_threshold=0.8):
    """
    Run Golicense-classifier on `project` and save results in CodebaseResources model

    Parameter
    ----------
    project : Project()
            Instance of `Project` to scan

    scan_threshold : float
            Threshold for license scan results `0 < scan_threshold <= 1.0`.
            Higher threshold gives more accurate results but takes more time in return.
    """
    classifier = LicenseClassifier(threshold=scan_threshold)

    for resource in project.codebaseresources.no_status():
        data = scan_file(classifier, location=resource.location)
        scancode.save_scan_file_results(
            codebase_resource=resource,
            scan_results=data,
            scan_errors=data.get("scan_errors", []),
        )
