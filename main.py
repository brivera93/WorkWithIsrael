from TestClass import Practice


def bubbleSort(myList=[]):
    length = len(myList)
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]


def addNumber(num1, num2):
    # sum = 0
    sum = num1 + num2
    return sum


test = Practice("Bryan", 100, 250)
print(test.sum())

num1 = 300
num2 = 200

# if num1 > num2:
#     print('num1 is greater')
# elif num1 == num2:
#     print('num1 is equal to num2')
# else:
#     print("num1 is less than")
# list = 1, 3, 5, 7, 9
#
# for var in list:
#     print(var)

list = 20, 30, 10, 25, 5, 15, 70
sum = 0

while sum < 100:
    sum += 23
    if sum < 100:
        print(sum)

sum = 0
i = 0
print("while looping using list")
while sum < 100:
    sum += list[i]
    i += 1
    if sum < 100:
        print(sum)

print(test.getName())
print(test.reverse())









# lingo = "bingo"
# dubNum = 42.10293
# listy = [1, 3, 5, 7, 9]
# listy2 = [4, 1, 3, 9, 8, 6, 2, 7, 5]
# listy3 = [9, 3, 2, 5]
#
# for var in listy2:
#     print("element " + str(var))
#
# for var in range(4,9):
#     print(var)
#
# test2 = "we are going to reverse a really long string, easily"
# test1 = StringPlayer("BryanRivers", 28)
# print(test1.getString() + " " + str(test1.getNum()) + "how long does it go")
# print("Will this be on a new line")
# print(type(lingo))
# print(f"my name is {lingo} before reassignment")
# print(lingo[len(lingo)::-1])
# lingo = "zingo"
# print(f"my name is {lingo} after reassignment")
# print(type(listy))
# print(listy2)
# print(type(listy2))
# bubbleSort(listy2)
# print(listy2)
# print(lingo[len(lingo)::-1])
# print(test2)
# print(test2[len(test2)::-1])  # this worked perfectly
#
# # lets try making a dictionary
# dict1 = ([('A', 1), ('B', 2), ('C', 3)])
# print(dict1)
#
# number1 = 100
# number2 = 250
# print(addNumber(number1, number2))

# number = 0
# listy.insert(0, number)

# for number in range(len(listy)):
# print(listy[number])
# print(number)
# print("")
