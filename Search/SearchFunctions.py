def BruteForce(haystack, needle):
    """
        Searches an item in a list (finding a needle in a haystack) using a brute force method
        in class, this function was 'isin' during CS395 1/18/2012
        
        Keyword arguments:
        haystack -- the list to search
        needle -- the item to search for
        
        define: n is the size of the list
        define: p is the probability an item is in the list
        
        best case: 1
        worst case: n = Big O(n)
        average case: (p/2) + ((2-p)n)/2
    """
    
    #iterate through the list, one item at a time
    for i in range(0, len(haystack)):
        
        #is the current item the one your looking for?
        if haystack[i] == needle:
            return True
    
    #Failed to find the element
    return False
        
    