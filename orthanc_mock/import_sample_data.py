#!/usr/bin/env python3
import os
from pathlib import Path
from urllib import request
import mimetypes

FOLDER_PATH = "/tmp/sample_data"
ORTHANC_URL = "http://localhost:8042/instances"


def import_dcm_to_orthanc(folder_path, orthanc_url):
    imported = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".dcm"):
                file_path = Path(root) / file
                content_type, _ = mimetypes.guess_type(str(file_path))
                if content_type is None:
                    content_type = 'application/octet-stream'

                with open(file_path, 'rb') as f:
                    data = f.read()
                    req = request.Request(
                        orthanc_url, data=data, method='POST')
                    req.add_header('Content-Type', content_type)
                    req.add_header('Content-Length', len(data))

                    try:
                        with request.urlopen(req) as response:
                            if response.status != 200:
                                print(f"Failed to import {file_path}: {response.reason}")
                            else:
                                imported += 1
                    except Exception as e:
                        print(f"Failed to import {file_path}: {e}")

    print(f"Imported {imported} files.")

if __name__ == "__main__":
    import_dcm_to_orthanc(FOLDER_PATH, ORTHANC_URL)
