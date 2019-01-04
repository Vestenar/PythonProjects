def printab(a,b,**kwargs):

    print(kwargs)
    for key in kwargs:
        print(key, kwargs[key], end='\t')
    print()

printab(10,20,c=30,d=40,new='word')
print("*"*10, end='\n\n')
print('function s \n')

def s(a, *vs, b=10):
   res = a + b
   print(vs)
   for v in vs:
       res += v
   return res

print(s(10, 5,5,5, b=31))