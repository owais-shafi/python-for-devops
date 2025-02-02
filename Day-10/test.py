import os
import subprocess

folders_name = input("Enter the name of folders with space in between: ").split()

for folders in folders_name:
    try:
        folders_path = subprocess.check_output(f"find ~ -type d -name {folders}", shell=True).decode('utf-8').strip().split("\n")

        for folder in folders_path:
            try:
                files = os.listdir(folder)
                print(f"\n============ List of files in '{folders}' folder ==============\n")
            except FileNotFoundError:
                print(f"\n============ Wrong folder path or folder does not exist: {folders} ==============\n")
            except PermissionError:
                print(f"\n============ Access denied: {folders} ==============\n")
            for i in range(len(files)):
                print(i+1,":- "+files[i])
                
    except subprocess.CalledProcessError:
        print(f"\n============ No folder found with the name '{folders}' ==============\n")




