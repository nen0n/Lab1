import argparse
from time import thread_time


def maxw1(W, w, n):
    a = thread_time()
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
    print(thread_time() - a)
    return max_value

def maxw2(W, w, n):
    a = thread_time()
    subp_list = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # list that contains all subproblems exist filled with zeros
    for index in range(1, n + 1):
        for value in range(W + 1):
            if w[index - 1] <= value:
                subp_list[index][value] = max(w[index - 1] + subp_list[index - 1][value - w[index - 1]],
                                              subp_list[index - 1][value])
            # filling the row with the biggest value possible with the considered bars

            else:
                subp_list[index][value] = subp_list[index - 1][value]
            # taking the value from the previous row if the w of a bar is higher than the value we consider no
    print(thread_time() - a)
    return subp_list[n][W]




parser = argparse.ArgumentParser()
parser.add_argument("-W", type=int)
parser.add_argument("-w", nargs='+', type=int)
parser.add_argument("-n", type=int)
args = parser.parse_args()
print(maxw1(args.W, args.w, args.n))
print(maxw2(args.W, args.w, args.n))