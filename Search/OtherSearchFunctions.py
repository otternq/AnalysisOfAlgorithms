def maxelem(l):
    """
    Finds the largest element on a list and returns the value
    
    Keyword arguments:
        l -- the list to search
        
    best case: 1
    worst case: n = Big O(n)
    average case: (p/2) + ((2-p)n)/2
    
    """
    maxval = l[0]
    
    for i in range(1, len(l)):
        if (l[i] > maxval):
            maxval = l[i]
    
    return maxval;
    
def unique(l):
    """
    Checks to see if each element is unique
    
    keyword arguments:
        l -- the list to search
    """
    
    for i in range(0, len(l) - 1):
        for j in range(i+1, len(l)):
            if (l[i] == l[j]):
                return False
    return True
    
#this will only run if this file is being executed from command line
#and will be ignored of included by another scrips/module/project 
if __name__ == '__main__':
    vals = [1,5,8,7,6]
    
    print(maxelem(vals))