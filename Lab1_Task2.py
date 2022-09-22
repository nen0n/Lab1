import argparse
import operator
import math

parser = argparse.ArgumentParser()
parser.add_argument("Operator", type=str)
parser.add_argument("Number", type=int, nargs="+")
args = parser.parse_args()

def func(oper, *args) -> str:
    try:
        func1 = getattr(operator, oper)
        return func1(*args)
    except Exception:
        try:
            func2 = getattr(math, oper)
            return func2(*args)
        except Exception:
            return "Error"

print(func(args.Operator, *args.Number))
