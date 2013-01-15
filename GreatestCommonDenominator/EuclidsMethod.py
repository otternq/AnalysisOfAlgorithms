import sys;
"""A slightly modified version of the code provided in CS395 by Prof. Heckendorn (1/11/2013 - 1/14/2013)"""


def EuclidsMethodMod(m,n):
    """Uses Euclids method to calculate the greatest common denominator"""
    
    #terminate recursion when n equals zero
    if n == 0:
        return m
        
    return EuclidsMethodMod(n, m % n )
    
def EuclidsMethodModMin(m,n):
    """A modified version of Euclids method that runs uses min()"""
    
    #terminate recursion when n equals zero
    if n == 0:
        return m
        
    return EuclidsMethodModMin(n, min( (m % n), (n - m % n) ) )
    
def EuclidsMethodMinus(m , n):

    # if m is greater, swap variables
    if m < n: (m, n) = (n, m)
        
    if n == 0:
        return m
        
    return EuclidsMethodMinus(n, m-n)
   
#this will only run if this file is being executed from command line
#and will be ignored of included by another scrips/module/project 
if __name__ == '__main__':

    #the first command line argument is considered m
    m = int(sys.argv[1])
    
    #the seconds command line argument is considered n
    n = int(sys.argv[2])
    
    print "Euclids Method Mod: "
    print EuclidsMethodMod(m, n)
    
    print "Euclids Method Minus: "
    print EuclidsMethodMinus(m, n)
    
    print "Euclids Method Mod Min: "
    print EuclidsMethodModMin(m, n)