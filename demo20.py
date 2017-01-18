# coding=utf-8
"""
    蛇形矩阵,蛇形填数
"""
while True:  # 蛇形矩阵
    try:
        a = input()
        l = [[0]*a for i in range(a)]
        s = 1
        for i in range(a):
            col = i
            while col >= 0:
                row = i - col
                l[row][col] = s
                col -= 1
                s += 1
        for i in l:
            for j in i:
                if j !=0:
                   print j,
            print
    except:
        break

while True:  # 蛇形矩阵
    try:
        row = 0
        col = 0
        s = 1
        a = input()
        bool = True
        l = [[0]*a for i in range(a)]
        for i in range(a):
            row = i
            while row >= 0:
                col = i -row
                if bool:
                    l[row][col] = s
                else:
                    l[col][row] = s
                s += 1
                row -= 1
            bool = not bool
        for i in l:
            for j in i:
                if j != 0:
                    print j,
            print
    except:
        break

while True:
    try:
        s = 1
        a = input()
        l = [[0]*a for i in range(a)]
        bool = True
        for i in range(2*a-1):
            col = i
            while col >= (0 if i < a else i-a+1):
                if col > a - 1:
                    col = a - 1
                row = i - col
                if bool:
                    l[row][col] = s
                else:
                    l[col][row] = s
                s += 1
                col -= 1
            bool = not bool
        for i in l:
            for j in i:
                    print j,
            print
    except:
        break

while True: # 蛇形填数
    try:
        cols, rows=input()
        matrix = [[0 for col in range(cols)] for row in range(rows)]
        i = j = 0
        n = 1
        matrix[i][j] = 1
        while n < rows*cols:
             while j+1 < cols and matrix[i][j+1] == 0:
                 j += 1
                 n += 1
                 matrix[i][j] = n
             while i+1 < rows and matrix[i+1][j] == 0:
                 i += 1
                 n += 1
                 matrix[i][j] = n
             while j > 0 and matrix[i][j-1] == 0:
                 j -= 1
                 n += 1
                 matrix[i][j] = n
             while i > 0 and matrix[i-1][j] == 0:
                 i -= 1
                 n += 1
                 matrix[i][j] = n
        for i in matrix:
            for j in i:
                print j,
            print
    except:
        break