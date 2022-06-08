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


def factorial(num):
    if num < 2:
        return 1
    return num * factorial(num-1)
#
# 3 * factorial(3-1)
# 3 * factorial(2)
# 3 * 2 * factorial(2-1)
# 3 * 2 * factorial(1)
# 3 * 2 * 1



def romanToInt(romanNum):
    sum = 0
    index = 0
    while index < len(romanNum):
        # get value of current symbol
        currentVal = value(romanNum[index])
        if (index + 1) < len(romanNum):
            nextVal = value(romanNum[index+1])
            if currentVal >= nextVal:
                sum = sum + currentVal
                index = index + 1
            else:
                sum = sum + nextVal - currentVal
                index = index + 2

    return sum


def value(val):
    if val == 'I':
        return 1
    if val == 'V':
        return 5
    if val == 'X':
        return 10
    if val == 'L':
        return 50
    if val == 'C':
        return 100
    if val == 'D':
        return 500
    if val == 'M':
        return 1000
    return -1

#
# {1,2,3,4,5,6,8}
# 1,2,3,4,5,6,8


def missingNum(array = []):
    # length = len(array)
    missingValue = set(range(array[0], array[-1] + 1)) - set(array)
    return missingValue


def reverseString(str):
    length = len(str)
    if length <= 1:
        return str
    low = 0
    high = length - 1
    while low < high:
        str[low], str[high] = str[high], str[low]
        low += 1
        high -= 1
    return str


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()


class Palindrome:
    def __init__(self, string, stack_object):
        self.string = string
        self.obj = stack_object

    def check(self):
        length = len(self.string)

        for ch in self.string:
            self.obj.push(ch)

        rev_string = ""
        for i in range(length):
            rev_string += self.obj.pop()

        if rev_string == self.string:
            return True
        else:
            return False

#
# obj1 = Practice("Bryan", 42, 99)
# print("tbis is name in reverse " + obj1.reverse())
# print("this is the sum of " + str(obj1.num1) + " and " + str(obj1.num2) + " is " + str(obj1.sum()))
#
#
# num1 = 300
# num2 = 200

# numArray = 20, 30, 10, 5, 15, 70


print(romanToInt("MCMIV"))



list1 = [1,2,3,5]
list2 = [0,2,3,4,5]
list3 = [0,1,2,3,4,5,6,7,9]

print(missingNum(list1))
print(missingNum(list2))
print(missingNum(list3))
random = ['h', 'e', 'l', 'l', 'o']
# olleh
# oellh

print(random)
print(reverseString(random))

# string = input("Enter a string: ")
# stack_obj = Stack()
# obj = Palindrome(string, stack_obj)
# if obj.check():
#     print("The given string is a palindrome!")
# else:
#     print("The given string is not a palindrome!")

#
# val = input("Enter input 0-6\n")
# value = int(val)
# print(factorial(value))




