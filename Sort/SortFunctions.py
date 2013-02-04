def BubbleSort(x):
    #iterate through each item in the list
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

if __name__ == "__main__":
    print BubbleSort([7,6,5,4,3,2,1]);