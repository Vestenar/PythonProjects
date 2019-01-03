def digitsProduct(product):
    smallest = []
    if product == 0: return 10
    if product < 10: return product

    else:
        while product > 1:
            changed = False
            for i in range(9, 1, -1):
                if product % i == 0:
                    smallest.append(str(i))
                    product = product//i
                    changed = True
                    break
            if changed == False:
                return -1


        print(smallest)
        smallest = int(''.join(sorted(smallest)))
    return smallest





print(digitsProduct(21))

'''
Given an integer product, find the smallest positive
(i.e. greater than 0) integer the product of whose digits
is equal to product.
If there is no such integer, return -1 instead.

Example

    For product = 12, the output should be
    digitsProduct(product) = 26;
    For product = 19, the output should be
    digitsProduct(product) = -1.
'''
