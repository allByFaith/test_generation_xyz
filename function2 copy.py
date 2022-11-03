# Define : 
# *args     (Non-Keyword Arguments)
# **kwargs  (Keyword Arguments)

def myAddNumsFunction(*argv):
    sum = 0
    for n in argv:
        sum += n
    print(f"the sum of the two input numbers {argv[0]} & {argv[1]} is {sum}")

myAddNumsFunction(200, -10)