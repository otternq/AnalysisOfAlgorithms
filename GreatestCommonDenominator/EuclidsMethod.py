import sys;
"""A slightly modified version of the code provided in CS395 by Prof. Heckendorn on 1/11/2013"""


def EuclidsMethod(m,n):
    """Uses Euclids method to calculate the greatest common denominator"""
    if n == 0:
        return m
    return EuclidsMethod(n, m % n)
   
#this will only run if this file is being executed from command line
#and will be ignored of included by another scrips/module/project 
if __name__ == '__main__':
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    
    print(EuclidsMethod(m, n))