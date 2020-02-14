def gravitation(rows):
    motionless = []
    vert = [[rows[j][i] for j in range(len(rows))] for i in range(len(rows[0]))]
    dots = []
    for i in range(len(vert)):
        dots.append(vert[i][vert[i].index('#'):].count(".") if "#" in vert[i] else 0)
    m = min(dots)
    for i in range(len(dots)):
        if dots[i] == m:
            motionless.append(i)
    return motionless


rows = ["#..##",
        ".##.#",
        ".#.##",
        "....."]

print(gravitation(rows))


'''
You are given a vertical box divided into equal columns. 
Someone dropped several stones from its top through the columns. 
Stones are falling straight down at a constant speed (equal for all stones) while possible 
(i.e. while they haven't reached the ground or they are not blocked by another motionless stone). 

Given the state of the box at some moment in time, 
find out which columns become motionless first.

Example

For

rows = ["#..##",
        ".##.#",
        ".#.##",
        "....."]

the output should be gravitation(rows) = [1, 4].'''