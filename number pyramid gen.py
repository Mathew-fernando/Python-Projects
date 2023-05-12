import keyboard as kb
from  time import sleep

x = int(input("insert a number: "))

if x >= 60:
    print("\n" + "woah there buddy! chill with the numbers.. 💀")
    quit()
    
z = int(input("input the multiplier for indents - default is 2: "))

if z >= 30:
    print("\n" + "woah there buddy! chill with the numbers.. 💀")
    quit()
    
print("\n" + "press any key to generate the results.." + "\n")
    
def program():
    def main(min_n, max_n, y):
        list = []
        for i in range(min_n, max_n):
            square = i * i
            list.append(square)
            if len(str(x*x)) != len(str(list[i-1])):
                rem = len(str(x*x)) - len(str(list[i-1]))
                list[i-1] = "0"*rem + str(square)
        print(y*z*" " + str(list))

    for j in range(2, x):
        main(1, j, x - j)

    list1 = []
    for i in range(1, x+1):
        square = i * i
        list1.append(square)
        if len(str(x*x)) != len(str(list1[i-1])):
                rem = len(str(x*x)) - len(str(list1[i-1]))
                list1[i-1] = "0"*rem + str(square)
    print(list1)
    
    for j in reversed(range(2, x)):
        main(1, j, x - j)
    
    print("\n"+"zoom out if its too big.. ")

if kb.read_key() != "a":
    program()
else:
    program()

sleep(60)