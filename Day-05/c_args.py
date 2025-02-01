# import in-built module sys
import sys
def add(num1, num2):
    return num1 + num2
# sys.argv is a list in Python, which contains the command-line arguments passed to the script.
# sys.argv[0] is the name of the script itself (it may be an empty string)
num1 = float(sys.argv[1])
# need to typecast because it returns as a string by default.
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add" :
    output=add(num1,num2)
    print("sum:",output)

# Run this code with the following command:
# python3 c_args.py 1 add 2, in terminal
