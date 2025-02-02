# try to include find command to find the path of folders instead of asking user for path.
import os
while True:
  folders_paths = input("please enter the path of the folders with space in between:").split()
  for folder in folders_paths :
    try:
     files=os.listdir(folder)
     print("\n============ List of files in " + "'" + folder + "'" + " folder ==============\n")
    except FileNotFoundError:
      print("\n============ Wrong folder path or folder does not exist: " + folder + "==============\n")
      continue
    except PermissionError:
      print("\n============Access denied: " + folder + "===============")
      continue
    
    for i in range(len(files)):
      print(i+1,":- "+files[i])
  choice=input("\n>>>>>Do you want to continue y/n: ")
  if(choice=="n"):
    break

# What does this command do:

# find ~/Downloads -type d -name 'day2' -exec ls {} \;

# Let's break it down step by step:

# 1. find: This is a powerful Unix command used to search for files and directories within a specified directory.

# 2. ~/Downloads: This specifies the directory where the search will start.

# The ~ symbol represents your home directory (/home/owais), so ~/Downloads means /home/owais/Downloads.

# 3. -type d: This option tells find to only look for directories. In this case, we're interested in finding directories (like day2), not files.

# 4. -name 'day2': This specifies the name of the directory you're looking for. The find command will search for directories named day2.

# 5. -exec ls {} \;: This part is what happens after find locates the directory. The -exec option allows you to run a command (in this case, ls) on the results of the find command.

# ls: Lists the contents of the directory.

# {}: This is a placeholder for the result of the find command. It represents the path of each directory that find locates.

# \;: This marks the end of the -exec command.