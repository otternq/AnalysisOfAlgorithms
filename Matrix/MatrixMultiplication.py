import numpy as np

def MatrixMultiplication(a, b):
    """
        Perfoms basic matrix multiplication
    
        Keyword arguments
        a -- a two dimentional list
        b -- a two dimentional list
        
        
        worst case: n^3
    
    """
    
    c = np.zeros_like(a)
    
    for i in range(0, len(a)):
        for j in range(0, len(a)):
        
            c[i][j] = 0
        
            #dot project
            for k in range(0, len(a)):
                c[i][j] += a[i][k] * b[k][j]
                
    return c

    
if __name__ == "__main__":
    
    a = np.array([
        [1,2],
        [3,4]
    ])
    
    b = np.array([
        [2,4],
        [3,4]
    ])
    
    print MatrixMultiplication(a, b)