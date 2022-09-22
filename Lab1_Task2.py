import argparse
import operator
import math

parser = argparse.ArgumentParser()
parser.add_argument("Operator", type=str)
parser.add_argument("Number", type=int, nargs="+")
args = parser.parse_args()

def func(oper, *args) -> str:
    try:
        fun1 = getattr(operator, oper)
        return fun1(*args)
    except Exception:
        try:
            fun2 = getattr(math, oper)
            return fun2(*args)
        except Exception:
            return "Error"

print(func(args.Operator, *args.Number))
