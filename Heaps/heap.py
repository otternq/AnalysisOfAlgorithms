from random import *


def isheap(h):
    for i in range(1, len(h)):
        if 2 * i < len(h) and h[i] < h[2 * i]:
            return False
        elif 2 * i + 1 < len(h) and h[i] < h[2*i+1]:
            return False
        else:
            return True


def heapdown(h, k):
    """
    Move element k down the tree to the correct position
    """

    #put this value in the correct place
    v = h[k]

    while 2 * k < len(h):

        #assign j to be the left child
        j = 2 * k

        #is there a child to the right
        if j + 1 < len(h):

            #is the left child smaller than the right child
            if h[j] < h[j+1]:
                j = j + 1

        #if v is greater than its larger child
        if v >= h[j]:
            break
        else:
            h[k] = h[j]
            k = j

    h[k] = v


def heapup(h, k):
    v = h[k]

    #keep within bounds
    while k > 1:
        #if the parent is less than the child
        if h[k//2] < v:
            #move the parent down to where the child is
            h[k] = h[k//2]
            k = k//2
        #the parent is greater than the child
        else:
            break


def makeheap(h):
    for i in range(len(h)//2, 0, -1):
        heapdown(h, i)
    return h


def addheap(h, v):
    h.append(v)
    heapup(h, len(h) - 1)


def main():
    x = [-1]
    for i in range(1, 10):
        x.append(int(uniform(0, 1000)))
    print(x)
    makeheap(x)
    print(x)


if __name__ == "__main__":
    main()
