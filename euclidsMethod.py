import sys;

def euclide(m,n):
    if n == 0:
        return m
    return euclide(n, m % n)
    
m = int(sys.argv[1])
n = int(sys.argv[2])

print(euclide(m, n))