#!/usr/local/bin/python3

import os
import io
import zipfile
import exiftool



def extract(filename):
    num_files = 0
    num_version_files = 0
    password_file = ''
    z = zipfile.ZipFile(filename)
    for f in z.namelist():
        dirname = os.path.splitext(f)[0]
        os.mkdir(dirname)
        content = io.BytesIO(z.read(f))
        zip_file = zipfile.ZipFile(content)
        for i in zip_file.namelist():
            num_files += 1
            zip_file.extract(i, dirname)
            with exiftool.ExifTool() as et:
                meta = et.get_metadata(dirname + '/' + i)
                if 'XMP:Version' in meta and meta['XMP:Version'] == 1.1:
                    num_version_files += 1
            try:
                with open(dirname + '/' + i, 'r') as handle:
                    data = handle.read()
                    if 'password' in data:
                        password_file = dirname + '/' + i
            except UnicodeDecodeError as err:
                continue

    print('1. Number of Files: ' + str(num_files))
    print('2. Number of Files with version 1.1: ' + str(num_version_files))
    print('3. File Containing the password: ' + password_file)


extract('final-final-compressed.zip')
