import sys

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

n1=int(sys.argv[1])
op=sys.argv[2]
n2=int(sys.argv[3])

if op =="add":
    a=add(n1,n2)
    print(a)



