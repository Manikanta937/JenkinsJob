import os
import sys

#folders = input("please give the list of directories with spaces: ").split()
folders=[]


folders.append(sys.argv[1])
folders.append(sys.argv[2])

for folder in folders:
    try:
        files=os.listdir(folder)
    except FileNotFoundError:
        print("files not found")
        break
    print("files in the particular folder "+ folder)

    for f in files:
        print(f)                