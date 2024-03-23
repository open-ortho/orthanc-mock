FROM orthancteam/orthanc
COPY orthanc.json /etc/orthanc/
COPY import_sample_data.py /usr/local/bin/import_sample_data.py
COPY ./sample_data /tmp/sample_data
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/import_sample_data.py
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
