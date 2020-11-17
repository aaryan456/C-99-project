import os
import shutil

src = input("type out the source folder file")
destination = input("name the destination folder")

src = src+"/"
destination= destination+"/"
createlist = os.listdir(src)
for files in createlist:
    shutil.copy((src+files),destination)