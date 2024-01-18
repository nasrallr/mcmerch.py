import sys

def parseArguments():
    arguments = {
        "price": int(sys.argv[1]),
        "quantity": 1,
        "province": "ON"
    } //add arguments to a dictionary
    return arguments
def taxRate():
    tax ={
        "ON": 0.13
    }
    return tax[province]

def mcmerchCalculator():
    arguments = parseArguments()
    tax = taxRate(arguments['province'])
    print(arguments['price'] * arguments['quantity'] * (1 + tax))

mcmerchCalculator()