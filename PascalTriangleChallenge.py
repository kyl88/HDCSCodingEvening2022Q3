import row as row
from Tools.demo.beer import n


def PascalTriangle(n):
    row = [1]
    y = [0]


for x in range(n):
    print(row)

row =[left + right for left,right in zip(row + y,y +row)]

return n>=1

PascalTriangle(30);

