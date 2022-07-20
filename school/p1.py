def np(n):
  r = c = s =0
  while n!=0:
    l = n % 10
    c += 1
    s += l
    r = r * 10 + l
    n = n // 10
   return r, c, s
    
def arm(n, c):
  t = n
  c = 0
  while n!=0:
    l = t % 10
    s = s ** l + c
    t = t // 10
    
