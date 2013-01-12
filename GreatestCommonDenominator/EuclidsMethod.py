

def EuclidsMethod(m,n):
    if n == 0:
        return m
    return EuclidsMethod(n, m % n)