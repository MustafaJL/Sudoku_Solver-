#!C:\Users\Hp\AppData\Local\Programs\Python\Python310\python.exe
print("Content-type: text/html\n\n")

import cgi
from page_creator import * 
from algo import *

form = cgi.FieldStorage()
list = []
# to get valur from form
for i in range(81):
    val = i+1
    name = "inp"+ str(val)
    a = form.getvalue(name)
    if a == None:
        list.append(-1)
    else:
        a = int(a)
        list.append(a)
alg = sudoko()
list = alg.sub_list(list)

solved = alg.solve_sudoku(list)
doc_creator()
html_open_tag()

head_open_tag()

link("stylesheet","./css/style1.css") 
title("solution")


head_close_tag()

body_open_tag()

div_open_tag("container")
div_open_tag("sudoko_matrix")

form_open_tag()
table_open_tag("1")

# list = [-1,-1,-1,2,6,-1,7,-1,1,6,8,-1,-1,7,-1,-1,9,-1,1,9,-1,-1,-1,4,5,-1,-1,8,2,-1,1,-1,-1,-1,4,-1,-1,-1,4,6,-1,2,9,-1,-1,-1,5,-1,-1,-1,3,-1,2,8,-1,-1,9,3,-1,-1,-1,7,4,-1,4,-1,-1,5,-1,-1,3,6,7,-1,3,-1,1,8,-1,-1,-1]


if solved == True:
    for i in range(0,9):
        tr_open_tag()
        for j in range(0,9):
            td_open_tag()
            value = list[i][j]
            input_tag("text","inp1",value=value)
            td_close_tag()
            
        tr_close_tag()
else:
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    for i in range(0,9):
        tr_open_tag()
        for j in range(0,9):
            td_open_tag()
            value = 0
            input_tag("text","inp1",value=value)
            td_close_tag()
        tr_close_tag()
    print("Can't be solved")



table_close_tag()
form_close_tag()

div_close_tag()
a_href_opne("./html/index.html","Go Back","btn return")

div_close_tag()


body_close_tag()

script_open_tag()
script_close_tag()


html_close_tag()

