# #!C:\Users\Hp\AppData\Local\Programs\Python\Python310\python.exe
# print("Content-type: text/html\n\n")



example_board = [
        [4, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 6, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]


    


        
def remove_duplication_from_row(ls):
    nw = []
    for a in ls:
        if a == -1:
            nw.append(-1)
        if a not in nw:
            nw.append(a)
    return nw

# for i in example_board:
#     if remove_duplication(i) == i:
        
#         print(True)
#     else:
#         print(False)

def remove_duplication_from_column(ls,col):
    col_val = [ls[i][col] for i in range(9)]
    nw = []
    for a in col_val:
        if a == -1:
            nw.append(-1)
        if a not in nw:
            nw.append(a)
    
        
    

# for i in range(9):
#     if remove_duplication_from_column(example_board,i) == [example_board[col][i] for col in range(9)]:
#         print(True)
#     else:
#         print(False)


row_col = []
for i in range(9):
    for j in range(9):
        row_start = (i // 3) * 3 # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
        col_start = (j // 3) * 3
        if (row_start,col_start) not in row_col:
            row_col.append((row_start,col_start))

nw = []
count = 0
for r in range(row_col[count][0], row_col[count][0]+3):
    for c in range(row_col[count][1],row_col[count][1]+3):
        nw.append(example_board)
    #     nw.append(example_board[r][c])
    #     count += 1
    # if remove_duplication_from_row(nw)== nw:
    #     print(True)
    # else:
    #     print(False)
    