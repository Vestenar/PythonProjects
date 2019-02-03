def pairOfShoes(shoes):
    size = list(set(shoes[i][1] for i in range(len(shoes))))
    print(size)
    for i in range(len(size)):
        if shoes.count([0, size[i]]) != shoes.count([1, size[i]]):
            return False
    return True

# sorting by lambda for future use somwhere
def pairOfShoes2(shoes):
    shoes.sort(key=lambda shoe: shoe[1])
    return shoes


shoes = [[0,23],
 [1,21],
 [1,23],
 [0,21],
 [1,22],
 [0,22]]
print(pairOfShoes(shoes))
'''
Yesterday you found some shoes in the back of your closet. 
Each shoe is described by two values:

    type indicates if it's a left or a right shoe;
    size is the size of the shoe.

Your task is to check whether it is possible to pair the shoes you found in such 
a way that each pair consists of a right and a left shoe of an equal size.

Example

    For

    shoes = [[0, 21], 
             [1, 23], 
             [1, 21], 
             [0, 23]]

    the output should be
    pairOfShoes(shoes) = true;

    For

    shoes = [[0, 21], 
             [1, 23], 
             [1, 21], 
             [1, 23]]

    the output should be
    pairOfShoes(shoes) = false.

'''
