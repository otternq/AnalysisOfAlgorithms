def num2bin(n):
    str = ""
    while n > 0:
        if n% 2 ==1:
            str = "1" + str
        else:
            str = "0" + str
        
        n = n//2
    return str
    
def num2binRec(n):
    if n == 0: return ""
    elif n % 2 == 1: return num2binRec(n//2) + "1"
    else: return num2binRec(n//2) + "0"
    
if __name__ == "__main__":
    
    print num2bin(3)
    print num2binRec(3)
    
    