import time
start_time = time.time()
'''def crosswordFormation(words):
    from itertools import permutations
    ans = 0
    v1 = words[0]

    for p in permutations(words[1:]):
        print(p)
        h1,v2,h2 = p
        for i in range(len(v1)):
            for j in range(len(h1)):
                if v1[i] == h1[j] and i < len(v1)-2 and j < len(h1)-2:
                    # print('1=',v1[i])
                    for k in range(len(h1)):
                        if k <= j-2 or k >= j+2:
                            for l in range(len(v2)):
                                if h1[k]==v2[l]:
                                    # print('2=',h1[k])
                                    for m in range(len(v1)):
                                        if m <= i-2 or m >= i+2:
                                            for n in range(len(h2)):
                                                if v1[m] == h2[n] and 0<l+(m-i)<len(v2) and 0<n+(k-j)<len(h2):
                                                    if v2[l+(m-i)]==h2[n+(k-j)]:
                                                        ans+=1
                                                        # print('3+4=',h2[n],h2[n+(k-j)])

    return ans*2'''

def crosswordFormation(words):
    from itertools import permutations as p
    c = 0
    for l in p(words):
        for d1 in range(len(l[0])-2):
            s1 = [i for i,j in enumerate(l[1]) if j == l[0][d1]]
            print("s1",s1)
            for d2 in range(d1+2, len(l[0])):
                s2 = [i for i,j in enumerate(l[2]) if j == l[0][d2]]
                print("s2",s2)
                for cw1 in s1:
                    for cw2 in s2:
                        for c1, c2 in zip(l[1][cw1+2:],l[2][cw2+2:]):
                            for c3, c4 in zip(l[3],l[3][d2-d1:]):
                                c += c1 == c3 and c2 == c4
    return c

words = ["aaaaaaaaaaaaaa",
 "baaaaaaaaaaaaa",
 "caaaaaaaaaaaaa",
 "daaaaaaaaaaaaa"]

print(crosswordFormation(words))
print("--- %s seconds ---" % (time.time() - start_time))
'''
You're a crossword fanatic, and have finally decided to try and create your own. 
However, you also love symmetry and good design, so you come up with a set of rules they should follow:

    the crossword must contain exactly four words;
    these four words should form four pairwise intersections;
    all words must be written either left-to-right or top-to-bottom;
    the area of the rectangle formed by empty cells inside the intersections isn't equal to zero.

Given 4 words, find the number of ways to make a crossword following the above-described rules. 
Note that two crosswords which differ by rotation are considered different.

Example

For words = ["crossword", "square", "formation", "something"], the output should be
crosswordFormation(words) = 6.

The six crosswords can be formed as shown below:

  f                         f                             f
  o                     c r o s s w o r d     c r o s s w o r d
c r o s s w o r d           r   o                   q     r
  m   q                     m   m                   u     m
  a   u            ;  s q u a r e          ;        a     a
  t   a                     t   t                   r     t
  i   r                     i   h             s o m e t h i n g
s o m e t h i n g           o   i                         o
  n                         n   n                         n
                                g                               
                                                              
    c         s               s                                      
f o r m a t i o n       c     q               c         s          
    o         m         r     u               r         o      
    s q u a r e       f o r m a t i o n       o         m            
    s         t    ;    s     r            ;  s q u a r e                  
    w         h         s o m e t h i n g     s         t         
    o         i         w                     w         h     
    r         n         o                   f o r m a t i o n            
    d         g         r                     r         n         
                        d                     d   
'''
