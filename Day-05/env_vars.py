# There are already a lot of env vars set in the system. 
# We can access them using os.environ and by typing env in terminal.
# We can also set our own env vars using the export command in terminal.
# export var_name=value syntax is used to set an env var.
# eg: export password="password123"
# We can also set env vars in the script itself.
# To read env vars in the script/program, we need to import the os module.
# to delete env vars use this command, unset var_name, in terminal.
import os

password=os.getenv("password")
# os.getenv() is used to get the value of the env var.
print("password:",  password)
