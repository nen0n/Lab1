import argparse


parser = argparse.ArgumentParser()
parser.add_argument("Number1", type=int)
parser.add_argument("Operator", type=str)
parser.add_argument("Number2", type=int)
args = parser.parse_args()
if (args.Operator == "+" or args.Operator == "-" or args.Operator == "*"):
    print("Result is:", eval(str(args.Number1) + args.Operator + str(args.Number2)))
elif (args.Operator == "/" and args.Number2 == "0"):
    print("Division by zero")
else:
    print(eval(str(args.Number1) + args.Operator + str(args.Number2)))