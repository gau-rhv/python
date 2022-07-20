def np(n):
  r = c = s =0
  while n!=0:
    l = n%10
    r = r * 10 + l
    c += 1
    s += l
    n = n // 10
   return r, c, s
    
