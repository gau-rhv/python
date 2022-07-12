def n2r(num):
  
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]
      
    thousands = m[num // 1000]
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]
  
    lol = (thousands + hundreds +
           tens + ones)
   
    return lol
  

def idk(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1
 
def r2n(str):
    res = 0
    i = 0
    while (i < len(str)):        
        s1 = idk(str[i]) 
        if (i + 1 < len(str)):            
            s2 = idk(str[i + 1]) 
            if (s1 >= s2):               
                res = res + s1
                i = i + 1
            else:             
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
    return res