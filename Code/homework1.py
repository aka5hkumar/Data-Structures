#Akash Kumar
#Question 1
    #example1: O(1)
    #example2: O(1)
    #example3: O(n)
    #example4: O(n)
    #example5: O(n^2)
#Questions 2
def merge(a,b):
    for i in range (min(len(a), len(b))):
        yield a[i]
        yield b[i]
    if len(a) < len(b):
        for i in range(len(b)-len(a)):
            yield b[len(a)+i]
    elif len(b) < len(a):
        for i in range(len(a)-len(b)):
            yield a[len(b)+i]
    else:
        pass
#Question 3
class polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __str__(self):
        s = ''
        length=len(self.coeff)-1
        for i in range(0, len(self.coeff)):
            if self.coeff[i] != 0:
                s += ' + %gx^%d' % (self.coeff[i], length-i)
        # Fix layout
        s = s.replace('+ -', '- ')
        s = s.replace('x^0', '')
        s = s.replace(' 1*', ' ')
        if s[0:3] == ' + ':  # remove initial +
            s = s[3:]
        if s[0:3] == ' - ':  # fix spaces for initial -
            s = '-' + s[3:]
        return s
    def evaluate (self, variable):
        r = 0
        t=[0]
        f=0
        length=len(self.coeff)
        for k in range(len(coeff)):
            r += self.coeff[k]*variable**(length-k-1)
            t.append(r)
        return (r)
        if (len(t)>1):
            f=t[-1]-t[-2]
            return(f)
        else:
            f=t[-1]
            return(f)
#Question 4
def f(n):
    return 1/pow(2,n)

def sigma(f,a,b):
    totalAns=0
    for i in range(b-a+1):
        totalAns += f(i +a)
    return totalAns
