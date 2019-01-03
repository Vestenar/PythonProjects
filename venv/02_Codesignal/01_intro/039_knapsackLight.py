def knapsackLight(value1, weight1, value2, weight2, maxW):
    mvalue = [0]
    if weight1 + weight2 <= maxW:
        mvalue.append(value1 + value2)
    else:
        if weight1 <= maxW:
            mvalue.append(value1)
        if weight2 <= maxW:
            mvalue.append(value2)

    return max(mvalue)

''' #решение virgile_f (умножение логики на число)
def knapsackLight(v1, w1, v2, w2, W):
    return max(int(w1<=W)*v1, int(w2<=W)*v2, int(w1+w2<=W)*(v1+v2))
'''
value1 = 15
weight1 = 2
value2 = 20
weight2 = 3
maxW = 2
print(knapsackLight(value1,weight1,value2,weight2,maxW))
'''
You found two items in a treasure chest! 
The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2. 
What is the total maximum value of the items you can take with you, 
assuming that your max weight capacity is maxW and you can't come back for the items later?'''