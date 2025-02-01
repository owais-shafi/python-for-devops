# functions takes input
# performs the required operation
# returns the output
# Always call the function for it to run
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
choice = int(input("Enter your choice: ")) 

def add(num1, num2):
     return num1 + num2
def sub(num1, num2):
    return num1-num2
def mul(num1, num2):
    return num1*num2
def div(num1, num2):
    return num1/num2

if choice == 1:
    print("sum:",add(num1, num2))
elif choice == 2:
    print("diff:",sub(num1, num2))
elif choice == 3:
    print("multi:",mul(num1, num2))
elif choice == 4:
    print("division:",div(num1, num2))
elif choice == 5:
    print("Bye Bye")
else:
    print("Invalid choice")

