from math import sqrt, pow

def dist(p1, p2):
    return sqrt( pow(p1[0] - p2[0], 2) + pow(p2[1] - p2[1], 2))

def closest(pts):

    min = (0,1)
    dmin = dist(pts[0], pts[1])
    
    for i in range(0, len(pts)):
    
        for j in range(i+1, len(pts)):
            
            curDist = dist(pts[i], pts[j])  
            
            if ( curDist <  dmin):
                min = (i, j)
                dmin = curDist;
    
    return min

print(
    closest(
        [
        (1,3),
        (2,-3),
        (1,2)
        ] 
    )
)
