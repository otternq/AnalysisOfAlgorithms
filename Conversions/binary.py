def num2bin(n):
    str = ""
    while n > 0:
        if n% 2 ==1:
            str = "1" + str
        else:
            str = "0" + str
        
        n = n//2
    return str
#END def numb2bin

def num2binRec(n):
    if n == 0: return ""
    elif n % 2 == 1: return num2binRec(n//2) + "1"
    else: return num2binRec(n//2) + "0"
#END def num2binRec
    
def num2binSize(n, size):
    """
    Converts a number to binary and allows a output size to be defined
    
    Keyword arguments:
        n -- the base 10 number to convert
        size -- the number of digits in the output
    """
    
    str = ""
    
    for i in range(0, size):
    
        if n % 2 == 1:
            str = "1" + str
        else:
            str = "0" + str
            
        n = n//2 #integer divide
    
    return str
#END def numb2binSize
    
def num2binSizeRec(n, size):
    """
    Recursively converts a number to binary and allow a output size to be defined
    
    Keyword arguments:
        n -- the base 10 number to convert
        size -- the number of digits in the output
    
    M(0) = 0
    M(size) = M(size-1) + size
    M(size) = BigO(size^2)
    """
    
    if size == 0:
        return ""
    elif n % 2 == 1:
        return num2binSizeRec(n//2, size - 1)
    else:
        return num2binSizeRec(n//2, size - 1) + "0"
    
#END def num2binSizeRec

def num2binSizeRec2(n, size):
    """
    Recursively converts a number to binary and allow a output size to be defined
    
    Keyword arguments:
        n -- the base 10 number to convert
        size -- the number of digits in the output
        
    M(size) = size + M(size+size2) + M(size2)
    
    consider size = 2^k
    
    M(2^k) = 2M(2^(k-1)) + 2^k
           = 2 (2M(2^(k-2) + 2^k) + (2^k)
           = 4(M(2^(k-2)) + 2(2^k)
           = ....
           = (2^k) * M(2^(k-k)) + k(2^k)
           = M(2^(k-k)) + (k+1)(2^k)
           = (k+1)(2^k)
           = (log2(size) + 1) size
           = (log2(size)size + size)
           = BigO(log(size) * size)
    """
    
    if size == 1:
        if n % 2 == 1:
            print "x"
            return "1"
        else:
            print "x"
            return "0"
        
    size2 = size//2
    
    return num2binSizeRec2( n/(2 ** size2), size - size2 ) + num2binSizeRec2(n, size2)
    
#END def num2binSizeRec2
    
def num2binSizeWithPrint(n, size):
    """
    Converts a number to binary and and allows a output size to be defined
    
    Keyword arguments:
        n -- the base 10 number to convert
        size -- the number of digits in the output
    """
    
    str = ""
    
    count = 0
    
    for i in range(0, size):
    
        count += (i+1)
    
        if n % 2 == 1:
            str = "1" + str
        else:
            str = "0" + str
            
        n = n//2 #integer divide
    
    print count
    return str
    
if __name__ == "__main__":
    
    import sys;

    #the first command line argument is considered m
    m = int(sys.argv[1])
    size = int(sys.argv[2])
    
    print num2bin(m)
    print num2binRec(m)
    print num2binSizeWithPrint(m, size)
    print num2binSizeRec2(m, size)
    
    