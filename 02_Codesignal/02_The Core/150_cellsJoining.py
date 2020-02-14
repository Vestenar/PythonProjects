def cellsJoining(table, coords):
    plus_v = -1
    for i in range(1, len(table) - 1):
        if "+" in table[i+1]:
            plus_v += 1
        plus_h = -1
        hash = -1
        if coords[1][0] <= plus_v <= coords[0][0]:
            # print(table[i])
            line = list(table[i])
            for ch in range(len(line)):
                if line[ch] == "+": plus_h += 1
                if line[ch] == "|": hash += 1
                if line[ch] == "-" and coords[0][1] <= plus_h <= coords[1][1]:
                    line[ch] = " "
                if line[ch] == "|" and coords[0][1] < hash <= coords[1][1]:
                    line[ch] = " "
            table[i] = "".join(line)



    for i in range(2, len(table)-2):
        if "+" in table[i]:
            line = list(table[i])
            line_prv = list(table[i-1])
            line_nxt = list(table[i+1])
            for ch in range(2, len(line)-2):
                if line[ch] == "+":
                    cond = [line[ch-1] == "-", line[ch+1] == "-", line_prv[ch] == "|", line_nxt[ch] == "|"]
                    if sum(cond) < 3:
                        if sum(cond) == 0:
                            line[ch] = " "
                        elif line[ch-1] == "-" and line[ch+1] == "-":
                            line[ch] = "-"
                        elif line_prv[ch] == "|" and line_nxt[ch] == "|":
                            line[ch] = "|"
                    #     line[ch] = "|"
                    #     if line_prv[ch] != "|" and line_nxt != "|":
                    #         line[ch] = " "
                    # elif line[ch-1] == " " or line[ch+1] == " ": line[ch] = "+"
                    # else: line[ch] = "-"
            table[i] = "".join(line)
    for t in table:
        print(t)
    return # table


table = ["+----+--+-----+----+-1",
         "|abcd|56|!@#$%|qwer|",
         "|1234|78|^&=()|tyui|",
         "+----+--+-----+----+0",
         "|zxcv|90|77777|stop|",
         "+----+--+-----+----+1",
         "|asdf|~~|ghjkl|100$|",
         "+----+--+-----+----+2"]
coords = [[2, 0], [1, 1]]
print(cellsJoining(table, coords))
table = ["+-----+-----+--------+-----------+--------+",
 "|fwdaw|dddd |42      |pretty long|table   |",
 "+-----+-----+--------+-----------+--------+",
 "|is   |long |ffffffff|ff         |border  |",
 "+-----+-----+--------+-----------+--------+",
 "|     |     |        |           |        |",
 "|     |     |        |           |        |",
 "+-----+-----+--------+-----------+--------+",
 "|empty|cells|are     |best       |there is|",
 "+-----+-----+--------+-----------+--------+"]
coords = [[3,0], [3,4]]
print(cellsJoining(table, coords))

table = ["+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+-1",
 "|1|1|  |  |  |3|     |4|   |    |5|ggg                                        |",
 "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+0",
 "| | |11|23|44| |55555| |abc|defg| |                                           |",
 "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+1",
 "| | |  |  |  | |     | |   |    | |#$%#                                       |",
 "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+2",
 "| | |  |  |  | |     | |   |    | |!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|",
 "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+3",
 "|*|*|42|  |  | |     |0|=) |    | |                                           |",
 "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+4"]
coords = [[4,0], [0,11]]
print(cellsJoining(table, coords))
table = ["+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+-",
 "|1|1|  |  |  |3|     |4|   |    |5|ggg                                        |",
 "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+0",
 "| | |11|23|44| |55555| |abc|defg| |                                           |",
 "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+1",
 "| | |  |  |  | |     | |   |    | |#$%#                                       |",
 "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+2",
 "| | |  |  |  | |     | |   |    | |!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|",
 "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+3",
 "|*|*|42|  |  | |     |0|=) |    | |                                           |",
 "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+4",
 "| | |  |  |  | |     | |   |    | |#$%#                                       |",
 "| | |  |  |  | |  *  | |   | dd | |#$%#                                       |",
 "| | |  |  |  | |     | |   |    | |#$%#                                       |",
 "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+5",
 "|1|1|  |  |  |3|     |4|   |    |5|ggg                                        |",
 "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+6",
 "| | |11|23|44| |55555| |abc|defg| |                                           |",
 "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+7",
 "| | |  |  |  | |     | |   |    | |#$%#                                       |",
 "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+8",
 "| | |  |  |  | |     | |   |    | |!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|",
 "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+9",
 "|*|*|42|  |  | |     |0|=) |    | |                                           |",
 "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+10"]
coords = [[5,6],
 [4,9]]
print(cellsJoining(table, coords))
"""
You are writing a spreadsheet application for an ancient operating system. The system runs on a computer so old that it can only display ASCII graphics. Currently you are stuck with implementing the cells joining algorithm.

You are given a table in ASCII graphics, where the following characters are used for borders: +, -, |. The rows can have different heights and the columns can have different widths. Each cell has an area greater than 1 (excluding the borders) and can contain any ASCII characters excluding +, - and |.

The algorithm you want to implement should merge the cells within a given rectangular part of the table into a single cell by removing the borders between them (i.e. replace them with space characters (' ') and replace redundant +s with correct border symbols). The cells to join are represented by the coordinates of the cells at the extreme bottom-left and top-right of the area.

Example
For

table =                         ["+----+--+-----+----+",
                                 "|abcd|56|!@#$%|qwer|",
                                 "|1234|78|^&=()|tyui|",
                                 "+----+--+-----+----+",
                                 "|zxcv|90|77777|stop|",
                                 "+----+--+-----+----+",
                                 "|asdf|~~|ghjkl|100$|",
                                 "+----+--+-----+----+"]

and coords = [[2, 0], [1, 1]], the output should be

cellsJoining(table, coords) = ["+----+--+-----+----+",
                               "|abcd|56|!@#$%|qwer|",
                               "|1234|78|^&=()|tyui|",
                               "+----+--+-----+----+",
                               "|zxcv 90|77777|stop|",
                               "|       +-----+----+",
                               "|asdf ~~|ghjkl|100$|",
                               "+-------+-----+----+"]

"""
