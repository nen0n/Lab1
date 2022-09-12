import argparse


def check(formula):
    str = formula
    for i in range(len(formula) + 1):
        if (len(formula) == 0):
            solving(str)
            break
        elif formula[-1] == "+" or formula[-1] == "-" or formula[-1] == "*" or formula[-1] == "/":
            error()
            break
        elif formula[0] == "/":
            if formula[1] == "0":
                error()
                break
            else:
                formula = formula[1:]
        elif (formula[0] == "+" or formula[0] == "-" or formula[0] == "*" or formula[0] == "/"):
            if (formula[1] == "+" or formula[1] == "-" or formula[1] == "*" or formula[1] == "/"):
                error()
                break
            else:
                formula = formula[1:]

        elif (formula[0].isdigit()):
            formula = formula[1:]
        else:

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
