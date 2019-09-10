# #As an example, we'll write a program that does a find and replace action for text files
# stored in a compressed ZIP file. We'll need objects to represent the ZIP file and each
# individual text file (luckily, we don't have to write these classes, they're available in
# the Python Standard Library). The manager object will be responsible for ensuring
# three steps occur in order:
# 1.  Unzipping the compressed file.
# 2.  Performing the find and replace action.
# 3.  Zipping up the new files.


import sys
import os
import shutil
import zipfile


class ZipProsessor:

    def __init__(self, filename, search_string, replace_string):
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = "unzipped-{}".format(filename)

    def _full_filename(self, filename):
        return os.path.join(self.temp_directory, filename)

    def zip_find_replace(self):
        self.unzip_files()
        self.find_replace()
        self.zip_files()

    def unzip_files(self):
        os.mkdir(self.temp_directory)
        zip = zipfile.ZipFile(self.filename)
        try:
            zip.extractall(self.temp_directory)
        finally:
            zip.close()

    def find_replace(self):
        for filename in os.listdir(self.temp_directory):
            with open(self._full_filename(filename)) as file:
                contents = file.read()
            contents = contents.replace(
                self.search_string, self.replace_string)
            with open(
                    self._full_filename(filename), "w") as file:
                file.write(contents)

    def zip_files(self):
        file = zipfile.ZipFile(self.filename, 'w')
        for filename in os.listdir(self.temp_directory):
            file.write(
                self._full_filename(filename), filename)
        shutil.rmtree(self.temp_directory)

# following to call

from zip_processor import ZipProcessor
import sys
import os
class ZipReplace:
    def __init__(self, search_string,
            replace_string):
        self.search_string = search_string
        self.replace_string = replace_string
    def process(self, zipprocessor):
        '''perform a search and replace on all files in the
        temporary directory'''
        for filename in os.listdir(
                zipprocessor.temp_directory):
            with open(
                zipprocessor._full_filename(filename)) as file:
                contents = file.read()
            contents = contents.replace(
                self.search_string, self.replace_string)
            with open(zipprocessor._full_filename(
                    filename), "w") as file:
                file.write(contents)
if __name__ == "__main__":
    zipreplace = ZipReplace(*sys.argv[2:4])
    ZipProcessor(sys.argv[1], zipreplace).process_zip()