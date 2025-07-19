'''
1. rectangle
2. square
3. x
4. triangle bottom left
5. triangle bottom right
6. triangle top left
7. triangle top right
8. |x|
'''


def rectangle(x,y):
    for i in range(x):
        for j in range(y):
            if i == 0 or i == x-1 or j == 0 or j == y-1:
                print("* ",end="")
            else:
                print("  ",end="")
        print()

def square(x):
    for i in range(x):
        for j in range(x):
            if i == 0 or i == x-1 or j == 0 or j == x-1:
                print("* ",end="")
            else:
                print("  ",end="")
        print()

def letterX(x,y):
    for i in range(x):
        for j in range(y):
            if i == j or j == x-i-1:
                print("* ",end="")
            else:
                print("  ",end="")
        print()


def triangleBottomLeft(x,y):
    for i in range(x):
        for j in range(x):
            if j == i or i == x-1 or j == 0 :
                print("* ",end="")
            else:
                print("  ",end="")
        print()

def triangleBottomRight(x,y):
    for i in range(x):
        for j in range(x):
            if j == x-i-1 or i == x-1 or j == y-1 :
                print("* ",end="")
            else:
                print("  ",end="")
        print()



def triangleTopLeft(x,y):
    for i in range(x):
        for j in range(x):
            if j == x-i-1 or i == 0 or j == 0 :
                print("* ",end="")
            else:
                print("  ",end="")
        print()

def triangleTopRight(x,y):
    for i in range(x):
        for j in range(x):
            if j == i or i == 0 or j == y-1 :
                print("* ",end="")
            else:
                print("  ",end="")
        print()



def BorderedletterX(x,y):
    for i in range(x):
        for j in range(y):
            if i == j or i == 0 or i == x-1 or j == x-i-1 or j == 0 or j == y-1:
                print("* ",end="")
            else:
                print("  ",end="")
        print()




def Call_shapes():
    choise = input("Pick your shape from the list by number.\n\t1. rectangle\n\t2. square\n\t3. x\n\t4. triangle bottom left\n\t5. triangle bottom right\n\t6. triangle top left\n\t7. triangle top right\n\t8.|x|\n--( CHOISE )--$  ")
    x = y = 0
    input_string = ""
    if choise[0]   == "1":
        print(f"--( {choise} )--[ width: x  height: y ]$  ",end="")
        input_string = input().split()
        x,y = input_string[0],input_string[1]
        print(f"[ width: {x} height: {y} ]\n")
        rectangle(int(x),int(y))
    elif choise[0] == "2":
        print(f"--( {choise} )--[ side: x ]$  ",end="")
        input_string = input().split()
        x= input_string[0]
        print(f"[ side: {x} ]\n")
        square(int(x))
    elif choise[0] == "3":
        print(f"--( {choise} )--[ width: x  height: y ]$  ",end="")
        input_string = input().split()
        x,y = input_string[0],input_string[1]
        print(f"[ width: {x} height: {y} ]\n")
        letterX(int(x),int(y))
    elif choise[0] == "4":
        print(f"--( {choise} )--[ width: x  height: y ]$  ",end="")
        input_string = input().split()
        x,y = input_string[0],input_string[1]
        print(f"[ width: {x} height: {y} ]\n")
        triangleBottomLeft(int(x),int(y))
    elif choise[0] == "5":
        print(f"--( {choise} )--[ width: x  height: y ]$  ",end="")
        input_string = input().split()
        x,y = input_string[0],input_string[1]
        print(f"[ width: {x} height: {y} ]\n")
        triangleBottomRight(int(x),int(y))
    elif choise[0] == "6":
        print(f"--( {choise} )--[ width: x  height: y ]$  ",end="")
        input_string = input().split()
        x,y = input_string[0],input_string[1]
        print(f"[ width: {x} height: {y} ]\n")
        triangleTopLeft(int(x),int(y))
    elif choise[0] == "7":
        print(f"--( {choise} )--[ width: x  height: y ]$  ",end="")
        input_string = input().split()
        x,y = input_string[0],input_string[1]
        print(f"[ width: {x} height: {y} ]\n")
        triangleTopRight(int(x),int(y))
    elif choise[0] == "8":
        print(f"--( {choise} )--[ width: x  height: y ]$  ",end="")
        input_string = input().split()
        x,y = input_string[0],input_string[1]
        print(f"[ width: {x} height: {y} ]\n")
        BorderedletterX(int(x),int(y))
  