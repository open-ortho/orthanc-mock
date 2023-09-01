#!/usr/bin/env python3
import os
import requests
from pathlib import Path

FOLDER_PATH = "./sample_data"  
ORTHANC_URL = "http://localhost:8201"  # replace with your Orthanc URL

def import_dcm_to_orthanc(folder_path, orthanc_url):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".dcm"):
                file_path = Path(root) / file
                with open(file_path, 'rb') as f:
                    r = requests.post(f"{orthanc_url}/instances", data=f.read())
                    if r.status_code != 200:
                        print(f"Failed to import {file_path}: {r.text}")

if __name__ == "__main__":
    import_dcm_to_orthanc(FOLDER_PATH, ORTHANC_URL)
