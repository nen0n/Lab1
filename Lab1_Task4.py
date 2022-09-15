import argparse


def maxweight(W, n, w):
    '''w = [0] + w
    capacity = W + 1
    matrix = [[0 for i in range(n+1)] for i in range(capacity)]

    for i in range(0, n+1):
        for j in range(0, capacity):
            matrix[j][i] = matrix[j][i - 1]
            if w[i] <= j:
                val = matrix[j - w[i]][i - 1] + w[i]
                if matrix[j][i] < val:
                    matrix[j][i] = val
    return matrix[-1][-1]'''
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
        value = 0
    return max_value


parser = argparse.ArgumentParser()
parser.add_argument("-W", type=int)
parser.add_argument("-w", nargs='+', type=int)
parser.add_argument("-n", type=int)
args = parser.parse_args()
print(maxweight(args.W, args.n, args.w))
