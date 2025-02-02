import os
# import subprocess

folders_name = input("Enter the name of folders with space in between: ").split()

for folders in folders_name:
    # try: 
        # using subprocess.check_output function in subprocess module 
        # folders_path = subprocess.check_output(f"find ~ -type d -name {folders}", shell=True).decode('utf-8').strip().split("\n")
        command = f"find ~ -type d -name {folders}"
        with os.popen(command) as pipe:
            folders_path = pipe.read().strip().split("\n")
        for folder in folders_path:
            try:
                files = os.listdir(folder)
                print(f"\n============ List of files in '{folders}' folder ==============\n")
            except FileNotFoundError:
                print(f"\n============ Wrong folder path or folder does not exist: {folders} ==============\n")
            except PermissionError:
                print(f"\n============ Access denied: {folders} ==============\n")
            for i in range(len(files)):
                print(i+1,":- "+files[i] + "\n")
                
    # except subprocess.CalledProcessError:
    #     print(f"\n============ No folder found with the name '{folders}' ==============\n")




