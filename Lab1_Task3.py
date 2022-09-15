import argparse


def check(formula):
    for i in range(len(formula)+1):
        if (len(formula) == i):
            solving(formula)
            break
        elif (formula[0] == "+" or formula[0] == "-" or formula[0] == "*" or formula[0] == "/"):
            error()
            break
        elif (formula[i] == "+" or formula[i] == "-" or formula[i] == "*" or formula[i] == "/"):
            if (formula[i+1] == "+" or formula[i+1] == "-" or formula[i+1] == "*" or formula[i+1] == "/"):
                error()
                break
        elif (formula[i] == "/"):
            if (formula[i+1] == '0'):
                error()
                break
        elif (formula[i] == "0"):
            if (formula[i+1].isnumeric()):
                error()
                break
        elif (formula[i].isdigit() == 0):
            error()
            break


def solving(formula):
    print("True,", eval(formula))


def error():
    print("False, None")

parser = argparse.ArgumentParser()
parser.add_argument("formula", type=str)
args = parser.parse_args()
check(args.formula)
