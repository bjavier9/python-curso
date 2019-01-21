def d_valor(n):
    n*=2
    return n

n = 10
print(d_valor(n))
print(n)

def dob_v(r):
    for i,l in enumerate(r):
        r[i]*=2
    
ns=[10,22,34]
print(dob_v(ns))
print(ns)
