import argparse


def check(formula):
    if (formula):
        if check_error(formula, 0): #check first and last digit
            error()
        else:
            for i in range(1, len(formula) + 1):
                if len(formula) == i:
                    #Printing Result
                    solving(formula)
                    break
                elif check_error(formula, len(formula) - i):
                    error()
                    break
    else:
        error()
        #If line is empty
def check_error(args, i):
    return args[i] not in ("+", "-") and args[i].isdigit() == 0 or \
           args[i - 1] in ("+", "-") and args[i] == '0' and args[i].isnumeric() or \
           args[i] in ("+", "-") and args[i-1] in ("+", "-") or \
           args[0] in ("+", "-") or args[0] == '0' and args[1].isnumeric() or \
           args[-1] in ("+", "-")


        # Not included symbol
        # Zero on first position of number
        # Reusing operators
        # First symbol not + - or 0
        # Last symbol not + -
def solving(formula):
    print("True,", eval(formula))


def error():
    print("False, None")


parser = argparse.ArgumentParser()
parser.add_argument("formula", nargs="?", type=str)
args = parser.parse_args()
check(args.formula)
