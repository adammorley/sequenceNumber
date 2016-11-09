import json
import os
import sys

class Persistence(filename):
    file = None
    try:
        file = open(filename, 'w+', 0)
    except IOError:
        sys.stderr.write('error in file open')
        sys.exit(1)

    def persist(object, tag)
        os.lseek(file, 0)
        file.write(object)
        os.fsync(file)
    def read():
        os.lseek(file, 0)
        obj = file.read()
        return obj
