import random


def get_grid():                      #表格生成函数(creat a grid)
    lst = []
    y = 0
    x = 0
    while y < wide[level - 1]:
        lst.append([])
        x = 0
        while x < wide[level - 1]:
            lst[y].append(" ")
            x = x + 1
        y = y + 1
    return lst


def print_grid(lst):                  #表格呈现函数(print a grid)
    print("Mines:", Mines, end="   ")
    print("Flags:", Flags, end="   ")
    print("Num_visible_squares:",Num_visible_squares)
    print(lines[level-1][0])
    print(lines[level-1][1])
    x = 0
    y = 0
    while y < wide[level - 1]:
        x = 0
        while x < wide[level - 1]:
            if x == 0:
                if y < 10:
                    print(str(y), " |", lst[y][x], "|", end="")
                else:
                    print(str(y), "|", lst[y][x], "|", end="")
            elif x == wide[level - 1] - 1:
                print("", lst[y][x], "|")
                if y != wide[level - 1] - 1:
                    print(lines[level - 1][2])
            else:
                print("",lst[y][x],"|",end="")
            x = x + 1
        y = y + 1
    print(lines[level - 1][3])


def fillzero(lst):                                     #表里填满0(fill the grid with 0)
    for y in range(0, wide[level - 1]):
        for x in range(0, wide[level - 1]):
            lst[y][x] = 0
    return lst


def produce_mine(lst):                                  #2表随机放雷函数(put the mines randomly)    
    t=0
    while t < nummine[level - 1]:
        x = random.randint(0, wide[level - 1] - 1)
        y = random.randint(0, wide[level - 1] - 1)
        if lst[y][x] != "X":
            lst[y][x] = "X"
            t = t + 1
        else:
            t = t + 0
    return lst


def fillnum(lst):                                       #填完雷之后填满数字(fill the grid with numbers after put the mines)
    y = 0
    around = [[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1],[1,0],[-1,0]]    
    while y < wide[level - 1]:
        x = 0
        while x < wide[level - 1]:
            if lst[y][x] == "X":
                for i in around:
                    row = y + i[1]
                    column = x + i[0]
                    if row >= 0 and column >= 0 and row < wide[level - 1] and column < wide[level - 1] and lst[row][column] != 'X':
                        lst[row][column] += 1
            x = x + 1
        y = y + 1
    return lst


def flag(string):                               #插旗F(put a flag)
    global Mines
    global Flags
    lstf = string.split(" ")
    x = int(lstf[1])
    y = int(lstf[2])
    if lst1[y][x] == "F":
        lst1[y][x] = " "
        Mines += 1
        Flags -= 1
        print_grid(lst1)
    elif lst1[y][x] == " ":
        lst1[y][x] = "F"
        Mines -= 1
        Flags += 1
        print_grid(lst1)
    else:
        move()


def clear(string):                             #左键(to clear the grid square )
    global access
    global boom
    lstf = string.split(" ")
    x = int(lstf[0])
    y = int(lstf[1])
    if lst1[y][x] != "F":
        if lst2[y][x] == "X":
            for y in range(0, wide[level - 1]):
                for x in range(0, wide[level - 1]):
                    if lst2[y][x] == "X":
                        lst1[y][x] = "X"
            print_grid(lst1)
            print('GAME OVER')
            boom = 1
            access = 1
        elif lst2[y][x] != "X" and lst2[y][x] != 0:
            lst1[y][x] = lst2[y][x]
        elif lst2[y][x] == 0:
            clear0(x, y)            
    else:
        move()


def clear0(x, y):
    lst1[y][x]=lst2[y][x]
    ignore.append((x, y))
    around = [[0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0]]
    for i in around:
        row = y + i[1]
        column = x + i[0]
        if row >= 0 and column >= 0 and row < wide[level - 1] and column < wide[level - 1]:
            if lst2[row][column] != 0:
                lst1[row][column] = lst2[row][column]
            else:
                lst1[row][column] = lst2[row][column]
                if (column,row) not in ignore:
                    clear0(column,row)   


def move():                              #对格子进行操作，左键或插旗(operate to the grid square)
    go = str(input("go go go!: "))
    if go[0] == "F":
        flag(go)
    else:
        clear(go)     


#1级制表(str部分变量定义)
r1_1 = "     0   1   2   3   4   5   6   7"
r1_2 = "   +---+---+---+---+---+---+---+---+"
r1_3 = "   |---+---+---+---+---+---+---+---+"
r1_4 = "   +-------------------------------+"
#2级制表(str部分变量定义)
r2_1 = "     0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15"
r2_2 = "   +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+"
r2_3 = "   |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+"
r2_4 = "   +---------------------------------------------------------------+"
#3级制表(str部分变量定义)
r3_1 = "     0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23"
r3_2 = "   +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+"
r3_3 = "   |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+"
r3_4 = "   +-----------------------------------------------------------------------------------------------+"
#1,2,3级制表素材库＆边长库
lines = [[r1_1, r1_2, r1_3, r1_4],[r2_1, r2_2, r2_3, r2_4],[r3_1, r3_2, r3_3, r3_4]]
wide = [8, 16, 24]
nummine = [10, 40, 99]

print("Welcome to Minesweeper")
print("Please choose your difficulty:\n  1: Beginner 8 x 8 grid with 10 mines\n  2: Intermediate 16 x 16 grid with 40 mines\n  3: Expert 24 x 24 grid with 99 mines ")
level = int(input("Choose a level(Enter a number from 1 to 3): "))

#表头的提示数
Mines = nummine[level - 1]  
Flags = 0                   
Num_visible_squares = 0     

lst1 = get_grid()
print_grid(lst1)
lst2 = get_grid()
lst2 = fillzero(lst2)                      #填0
lst2 = produce_mine(lst2)                  #填雷
lst2 = fillnum(lst2)                       #填数
print_grid(lst2)                           # (for test) 

ignore = []
access = 0
boom = 0
while access != 1:
    count = []
    move()
    for y in range(0, wide[level - 1]):
        for x in range(0, wide[level - 1]):
            if lst2[y][x] != "X" and lst2[y][x] != "F" and lst1[y][x] == lst2[y][x]:
                count.append(1)
    Num_visible_squares = len(count)
    if boom != 1:
        print_grid(lst1)   
    if len(count) == (wide[level - 1])** 2 - nummine[level - 1]:
        print("YOU WIN!!")
        access = 1