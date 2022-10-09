# About project:
This project is a sudoko solver application that solve a sudoko puzzle using backtracking algorithm and brute force approach.

## FrontEnd:
we implement frontend using simple web tools as html / css / js

## BackEnd:
we use python programming language to solve the puzzle 

### 1- directories
    1.1-html: contain the structure of design of 9x9 grid
    1.2-css: contain the style of structure       
    1.3-Js: contain the functionallity that disallow user to enter more than one number in each input and use a regex to let user enter just numbers
    1.4-python_project_sudoko_solver: contain the enviroment of the project that has all the modules 
### 2- files
    2.1-algo.py: files that contain the algorithm to solve sudoko using backtracking
    2.2-connection.php: contain the connection between mysql and server
    2.3-login.php: contain the login page that the user enter his account using it when he wants to play
    2.4-env.txt: contain the modules names the user of this project should install 
    2.5-page_creator.py: contain functions that control the creation of html structure
    2.6-python.py:contains method to check if there is duplication in row or column or 3x3 grid
    2.7-test.py: first of all we import cgi module and then call data from html form then 
                fill it in a list then import algo.py and use sub_list() function 
                to divide the list into 2D list of length 9

## How to run the application ?

    first we run the xampp or wampp server and start appache and mysql.
    second we open any search enginee and run localhost and port number and name of directory 
    such as: localhost:80/myproject/login.php
    then we enter a valid username and password: 
    Email-> mij004@usal.edu.lb
    Password-> M@m123456
    then the index.html page will loaded on screen
    after that we enter a valid sudoko and click submit button
    finally the game will retrieve a solution for the sudoko puzzle.



#### Note: connection.php file need to be connected to valid database.














