import re


def htmlTable(table, row, column):
    ans = "No such cell"
    pattern = r"<tr>(.+?)</tr>"
    try:
        t_row = re.findall(pattern, table)[row]
        pattern = r"<td>(.+?)</td>"
        t_cells = re.findall(pattern, t_row)
        if column < len(t_cells):
            ans = t_cells[column]
        else: return ans
    except:
        return ans  # превышение лимита рядов
    return ans




table = "<table><tr><td>1</td><td>TWO</td></tr><tr><td>three</td><td>FoUr4</td></tr></table>"
row = 0
column = 1
print(htmlTable(table, row, column))
table = "<table><tr><td>1</td><td>040S713</td><td>2974b</td><td>Pp4Y9</td><td>UWvp2Sq6Sd</td><td>997r6De</td><td>Bh</td><td>TBy</td><td>Ss6C</td><td>8c</td></tr><tr><td>2</td><td>R81hX704</td><td>89b6a6</td><td>jwk0b</td><td>JC80xBvW</td><td>Ka</td><td>7</td><td>E3Lx</td><td>0wg1</td><td>4HCs</td></tr><tr><td>C6d2</td><td>o2N9Twup6</td><td>Pa42t</td><td>88T0itrA</td><td>DtAmM23</td><td>09Fseat</td><td>Qd5j8Cg</td><td>N20GvC8sk2</td><td>Eqq</td><td>Dq2XnGa0</td></tr><tr><td>Kd</td><td>SO4cZHM</td><td>x</td><td>ie3lbmsvx</td><td>23jWU</td><td>3UjEeT9h</td><td>Es9K7q5</td><td>ij58GnGEuk</td><td>5</td><td>bx0</td></tr><tr><td>aNXo91iG78</td><td>6M</td><td>6J9Lf8b5</td><td>MbQ1HRGtDH</td><td>5skjIH</td><td>P7z2SQnlX2</td><td>6ng</td><td>gAvz4dtCH</td><td>78NN98d</td><td>F8zy4SHXA1</td></tr><tr><td>khAM1</td><td>TIJ</td><td>gA034V</td><td>Cg95</td><td>62</td><td>6N371</td><td>1IN1I</td><td>b</td><td>PafB8Bnf</td><td>6jah</td></tr><tr><td>A4q</td><td>KWvhoy76Z</td><td>WLRK</td><td>0u</td><td>AC6H</td><td>JXM8WxO</td><td>0riDU6</td><td>1</td><td>BX327aD0</td><td>j2WDGTiIL</td></tr><tr><td>eCfoZ7</td><td>h96JOr3</td><td>93gC</td><td>jZT1ZShL3</td><td>NP3</td><td>T6a3KG</td><td>pN</td><td>3jVF</td><td>PZ4P</td><td>3bQk4TKe</td></tr><tr><td>6</td><td>z</td><td>VN</td><td>1PlI5T5</td><td>m5P</td><td>N</td><td>6Rz4CAC31r</td><td>7A732yr74</td><td>60</td><td>669N5t</td></tr><tr><td>ugT9</td><td>BM9</td><td>x6wi</td><td>NLMrzA9</td><td>Y61Dd8MF</td><td>45G9Nq15uS</td><td>VcDP</td><td>A</td><td>z</td><td>08HL8EXL5S</td></tr></table>0"
row = 9
column = 9
print(htmlTable(table, row, column))
table = "<table><tr><th>CIRCUMFERENCE</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th></tr><tr><th>BITS</th><td>3</td><td>4</td><td>8</td><td>10</td><td>12</td><td>15</td></tr></table>"
row = 1
column = 0
print(htmlTable(table, row, column))
'''
HTML tables allow web developers to arrange data into rows and columns of cells. 
They are created using the <table> tag. Its content consists of one or more rows denoted by the <tr> tag. 
Further, the content of each row comprises one or more cells denoted by the <td> tag, 
and content within the <td> tags is what site visitors see in the table. 
For this task assume that tags have no attributes in contrast to real world HTML.

Some tables contain the <th> tag. This tag defines header cells, which shouldn't be counted as regular cells.

You are given a rectangular HTML table. Extract the content of the cell with coordinates (row, column).

If you are not familiar with HTML, check out this note.

Example

    For table = "<table><tr><td>1</td><td>TWO</td></tr><tr><td>three</td><td>FoUr4</td></tr></table>", 
row = 0, and column = 1, the output should be
    htmlTable(table, row, column) = "TWO".

    <table>
     <tr>
      <td>1</td>
      <td>TWO</td>
     </tr>
     <tr>
      <td>three</td>
      <td>FoUr4</td>
     </tr>
    </table>

    corresponds to:
    1	TWO
    three	FoUr4

    For table = "<table><tr><td>1</td><td>TWO</td></tr></table>", row = 1, and column = 0, the output should be
    htmlTable(table, row, column) = "No such cell".

    <table>
     <tr>
      <td>1</td>
      <td>TWO</td>
     </tr>
    </table>

    corresponds to:
    1	TWO'''
