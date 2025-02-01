# Command line args and environment variables
* What is command line args?
* Command line arguments are a powerful way to pass parameters to a program when it is executed.
* They allow users to customize the behavior of the program without modifying its source code.
* The read the command line args we need sys module which is installed in python by default. 
* Python installed frequently used modules by default or in-build module and don't need to install using pip.
* sys.argv reads the command line arguments.

** example will be in c_args.py file **


$$ Environment variable: these are the variables that are used for sensible information like password or API keys etc.It is a dynamic value that is stored in the environment and can be accessed by various programs or scripts running on the system.
* Environment variables are typically set by the operating system or by the user and are accessible to all programs and processes running on the system. They provide a way to store configuration settings, system-specific information, or sensitive data without hardcoding them directly into the code.
* Instead, the code can retrieve the values from the environment variables, allowing for flexibility, security, and portability.
* In Python, you can access and manipulate environment variables using the os module. This module provides functions and dictionaries to interact with the operating system, including the ability to retrieve the values of environment variables, set new variables, or modify existing ones.


** example in env_vars.py file **

