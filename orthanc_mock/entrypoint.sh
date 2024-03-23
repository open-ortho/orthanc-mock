#!/bin/bash
set -e
IMPORTED_FLAG="/var/local/import_sample_data_done"

/usr/local/bin/Orthanc /etc/orthanc/orthanc.json &
ORTHANC_PID=$!

# Wait for Orthanc to be up and running

if [ ! -f "$IMPORTED_FLAG" ]; then
    echo "Importing DICOM files..."
    sleep 5
    /usr/local/bin/import_sample_data.py
    touch "$IMPORTED_FLAG"
    rm -rf /tmp/sample_data
fi

# Continue with Orthanc's main process
wait $ORTHANC_PID