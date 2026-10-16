import os
# import glob

def mkdir(path):
    if os.path.exists(path) == False:
        os.mkdir(path)

def main(path):
    mkdir(fr"{path}\output")
    mkdir(fr"{path}\output\total")
    mkdir(fr"{path}\output\growth")
    mkdir(fr"{path}\output\death")
    mkdir(fr"{path}\tmp")