import time
start_time = time.time()
def comfortableNumbers(l, r):
    mass = {}
    ans = set()
    for i in range(l,r+1):
        su = s(i)
        mass[i] = [j for j in range(i-su, i+su+1) if j != i]
    for key in mass:
        for val in mass[key]:
            if val in mass and val > key:
                if val - s(val) <= key <= val + s(val):
                    ans.add((key,val))

    return len(ans)


def s(a):
    s = sum(int(i) for i in str(a))
    return s


print(comfortableNumbers(1,1000))
print("--- %s seconds ---" % (time.time() - start_time))


'''
Let's say that number a feels comfortable with number b 
if a ≠ b and b lies in the segment [a - s(a), a + s(a)], where s(x) is the sum of x's digits.

How many pairs (a, b) are there, such that a < b, 
both a and b lie on the segment [l, r], and each number 
feels comfortable with the other (so a feels comfortable with b and b feels comfortable with a)?

Example

For l = 10 and r = 12, the output should be
comfortableNumbers(l, r) = 2.

Here are all values of s(x) to consider:

    s(10) = 1, so 10 is comfortable with 9 and 11;
    s(11) = 2, so 11 is comfortable with 9, 10, 12 and 13;
    s(12) = 3, so 12 is comfortable with 9, 10, 11, 13, 14 and 15.

Thus, there are 2 pairs of numbers comfortable with each other within the segment [10; 12]: (10, 11) and (11, 12).
'''

'''
That one was tricky. I had trouble wrapping my head around the problem. When I listed out the comfortable numbers and their pairs, it made more sense.
For example For l=1 and r=9

Comfortable Numbers:
1: Set { 0, 2 }
2: Set { 0, 1, 3, 4 }
3: Set { 0, 1, 2, 4, 5, 6 }
4: Set { 0, 1, 2, 3, 5, 6, 7, 8 }
5: Set { 0, 1, 2, 3, 4, 6, 7, 8, 9, 10 }
6: Set { 0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12 }
7: Set { 0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14 }
8: Set { 0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16 }
9: Set { 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18 }

Pairs:
(1,2)
(2,3),(2,3)
(3,4),(3,5),(3,6)
(4,5),(4,6),(4,7),(4,8)
(5,6),(5,7),(5,8),(5,9)
(6,7),(6,8),(6,9)
(7,8),(7,9)
(8,9)
'''

'''
First create a map Hashmap<Integer, ArrayList<Integer>>. 
For each number, i, between l and r inclusive, calculate the sum of the digits. 
This is the range. 
Create an ArrayList that contains numbers from i - range to i + range. 
Store this arraylist in the map with i as the key.

Now iterate over i=l to r-1 and j=i+1 to r. 
If the arraylist at i in the map contains j and the arraylist at j contains i, 
then i and j are "comfortable" with each other.
'''


