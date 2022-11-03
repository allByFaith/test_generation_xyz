# Define : 
# *args     (Non-Keyword Arguments)
# **kwargs  (Keyword Arguments)

def keyWordFunction(**kwargs):

    print("\nPrint the monthly expenditures below:-")
    print("----------------------------------------")
    for nKey, nValue in kwargs.items():
        print("%s \t = \t%d" % (nKey, nValue))
    print("----------------------------------------")

keyWordFunction(Expense=10000, TutitionFee=2000, RentalFee=800, Electricity=150, CouncilTax=120)
