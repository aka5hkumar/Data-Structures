from __future__ import print_function
def fib1(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib1(x - 1) + fib1(x - 2)

def fib2(x):
    A = []
    A.append(0)
    A.append(1)
    for i in range(2, x + 1):
        A.append(A[i - 1] + A[i - 2])
    return A[x]

def fib3(x):
    if x == 0:
        return 0
    else:
        a = 0
        b = 1
        for i in range(x - 1):
            a, b = b, a + b
        return(b)

for f in (fib1, fib2, fib3):
    print([f(i) for i in range(10)])


import timeit

def timeFunction(f, n, repeat=1):
    return timeit.timeit(f.__name__ + '(' + str(n) + ')', setup="from __main__ import " + f.__name__, number=repeat) / repeat

print (timeFunction(fib1,15))
print ("Hello")

# def printFunctionTimes(sequences, ranges):
#     for  n in ranges:
#         print("\n","n=",n, end=" ")
#         for sequence in sequences:
#             print (sequence.__name__,":", timeFunction((sequence),(n)),end=" ")
# printFunctionTimes((fib1,fib2,fib3), range(5,40,5))
class functionPlotter:
    def __init__(self, f, inc=1):
        self.f = f
        self.n = -1
        self.t = height
        self.lst = []

    def timeNext(self):
        self.n += 100
        self.t = height - 10000*timeFunction(self.f, self.n)
        self.lst.append(self.t)

    def plot(self):
        print(f[0][1])

    def prefix_average1(S):
        """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
        n = len(S)
        A = [0] * n                     # create new list of n zeros
        for j in range(n):
            total = 0                     # begin computing S[0] + ... + S[j]
            for i in range(j + 1):
                total += S[i]
            A[j] = total / (j + 1)          # record the average
        return A

    def runprefix_average1(n):
        prefix_average1(range(n))

    def prefix_average2(S):
        """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
        n = len(S)
        A = [0] * n                     # create new list of n zeros
        for j in range(n):
            A[j] = sum(S[0:j + 1]) / (j + 1)  # record the average
        return A

    def runprefix_average2(n):
        prefix_average2(range(n))


    def prefix_average3(S):
        """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
        n = len(S)
        A = [0] * n                   # create new list of n zeros
        total = 0                     # compute prefix sum as S[0] + S[1] + ...
        for j in range(n):
            total += S[j]               # update prefix sum to include S[j]
            A[j] = total / (j + 1)        # compute average based on current sum
        return A

    def runprefix_average3(n):
        prefix_average3(range(n))


def setup():
    size(600, 600) #sets the size of the window
    global fp
    fp=functionsPlotter((runprefix_average1,runprefix_average2,runprefix_average3),((255,0,0),(0,255,0),(0,0,255)),10)

def draw():
    global fp
    background(255) #Background is black
    fp.timeNext()
    fp.plot()
