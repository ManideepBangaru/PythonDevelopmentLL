import os
from os import path
import datetime
from datetime import date,time,timedelta
import time

def main():
    # print(os.name)
    # print("Item exists : " + str(path.exists("textfile.txt")))
    # print("Item exists : " + str(path.isfile("textfile.txt")))
    # print("Item exists : " + str(path.isdir("textfile.txt")))

    # Working with file paths
    # print("Item path : " + str(path.realpath("textfile.txt")))
    # print("Item path and name : " + str(path.split(path.realpath("textfile.txt"))))

    # Get the modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # Calculate how long ago the item has been modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been " + str(td) + " since the file has been modified")
    print("Or, " + str(td.total_seconds()) + " seconds")
    print("Or, " + str(td.total_seconds()/60) + " minutes")


if __name__ == "__main__":
    main()