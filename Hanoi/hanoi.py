def other(f, t): return 3 - (f + t)

def hanoi(howmany, f, to):
    
    #only recurse when from > 1 (terminating statement)
    if howmany > 1:
        hanoi(howmany - 1, f, other(f,to))

    #doing the actual work, moving a disk
    print("move", f, "to", to)
    
    #only recurse when howmany > 1 (terminating statement)
    if howmany > 1:
        hanoi(howmany - 1, other(f,to) , to)

if __name__ == "__main__":
    hanoi(8,0,2);
