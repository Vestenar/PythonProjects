def Divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Divizion by zero")
    else:
        print("result is", result)
    finally:
        print("Finally")

Divide(1,2)
Divide(2,0)
Divide(2,[])