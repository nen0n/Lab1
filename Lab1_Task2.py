import argparse


parser = argparse.ArgumentParser()
parser.add_argument("Operator", type=str)
parser.add_argument("Number1", type=int)
parser.add_argument("Number2", type=int)
args = parser.parse_args()
formula = 'print(eval(str(operator.' + args.Operator + '(' + str(args.Number1) + ', '+str(args.Number2)+'))))'
exec(formula)
