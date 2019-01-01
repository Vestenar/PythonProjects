def printab(a,b,**kwargs):
    print(a)
    print(b)
    for key in kwargs:
        print(key, kwargs[key])

printab(10,20,c=30,d=40,new='word')

def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res

print(s(b=31))