import argparse


def maxweight(W, n, w):
    w.sort()
    max_value = 0
    value = 0
    len = n - 1
    for i in range(n):
        for j in range(i, n):
            if w[len-j] + value <= W:
                value += w[len-j]
        if max_value <= value:
            max_value = value
        if max_value == W:
            break;
        value = 0
    return max_value


parser = argparse.ArgumentParser()
parser.add_argument("-W", type=int)
parser.add_argument("-n", type=int)
parser.add_argument("-w", nargs='+', type=int)
args = parser.parse_args()
print(maxweight(args.W, args.n, args.w))
