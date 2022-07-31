def temperatureConverter(c,m):
    if m == 1:
        C = round(float(((5/9)*(c-32))),2)
        return C
    else:
        F = round(float(((c*(9/5))+32)),2)
        return F

def Vowels(word):
    vowels=["a","e","i","o","u","A","E","I","O","U",]
    counter = 0
    for char in word:
        if char in vowels:
            counter += 1
    if counter > 1:
        return True
    else:
        return False
            
def Force(v):
    m = 2
    r = 3
    T = ((m*(v**2))/r)
    if T>60:
        return T
    else:
        return T
