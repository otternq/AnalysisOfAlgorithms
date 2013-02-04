def BubbleSort(x):
    """
    Performs a bubble sort
        
    Keyword arguments:
        x -- the list of numbers to sort
    """
    
    
    #iterate through each item in the list (except the last)
    for i in range(0, len(x)-1):
        #starting from where i currently is, iterate to the end of the list
        for j in range(0, (len(x) - 1) - i):
            #if the current item is larger than the next item
            if x[j] > x[j+1]:
                #swap the items
                (x[j], x[j+1]) = (x[j+1], x[j])
        #print the current state
        print x[:len(x)-1-i], x[len(x)-1-i:]

    #return the sorted list
    return x

def SelectionSort(x):
    """
    Performs a selection sort
        
    Keyword arguments:
        x -- the list of numbers to sort
    """
    
    #iterage through each item in the list (except the last)
    for i in range(0, len(x)-1):
        
        #start with the assumption that the first item is the smallest
        #not typically a good assumption but needed
        min = i;
        
        #iterage from where the main loop is currently at until the last item
        for j in range(i+1, len(x)):
            
            #if the current item is smaller than the current min, set the
            #current item to be the minimum
            if x[j] < x[min] :
                min = j
    
        #swap the element i is currently at, with the next smallest element
        (x[i], x[min]) = (x[min], x[i])

    #return the sorted list
    return x
    

if __name__ == "__main__":
    
    l = [7,6,5,4,3,2,1];
    
    print BubbleSort(l);
    print SelectionSort(l);