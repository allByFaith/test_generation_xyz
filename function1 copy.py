# Function addTwoNums()
# Which accept two input arguments from runtime input
# i.e. inNum1 and inNum2
def addTwoNums(inNum1, inNum2):
    return(inNum1 + inNum2)

# Accept two input numbers num1 and num2
def main():
    num1 = int(input("Enter the 1st number for adding : "))
    num2 = int(input("Enter the 2nd number : "))
    
    result = addTwoNums(num1, num2)

    print(f"The sum of {num1} and {num2} is {result}")

# call the main() function
main()