import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("textfile.txt") == True :
        # get the path of the file
        src = path.realpath("textfile.txt")

        # lets make a backup by appending "bak" to the file name
        dst = src + ".bak"

        # copy over the permissions, modification times and other info
        shutil.copy(src, dst)
        shutil.copystat(src,dst) # to copy metadata such as time created

        # rename a file
        # os.rename("textfile.txt.bak","duplicate.txt")

        # put things to zip archive folder
        # root_dir, tail = path.split(src)
        # shutil.make_archive("archive", "zip", root_dir)

        # more control over zip files
        with ZipFile("testzip.zip","w") as newzip :
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")

if __name__ == "__main__":
    main()