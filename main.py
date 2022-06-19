def isPalindrome(string):
    stack = []
    index = 0
    strLen = len(string)
    for char in string:
        length = len(stack)
        if length == 0:
            stack.append(char)
            # index = index + 1
        elif stack[length-1] == char and index >= int(strLen / 2):
            stack.pop(length-1)
            # index = index - 1
        else:
            index = index + 1
            if (strLen % 2 != 0) and (index == int(strLen / 2)):
                continue
            else:
                stack.append(char)
                # index = index + 1
    if not stack:
        print("the string " + string + " is a palindrome")
    else:
        print("the string " + string + " is not a palindrome")

# dood
def isPalindromePtr(string):
    ptr1 = 0
    ptr2 = len(string) - 1
    flag = False

    while ptr1 <= ptr2:
        if string[ptr1] == string[ptr2]:
            ptr1 += 1
            ptr2 -= 1
        else:
            print("the string " + string + " is not a palindrome")
            flag = True
            break
    if not flag:
        print("the string " + string + " is a palindrome")


def mergeSortedLists(list1, list2):
    ptr1 = 0
    ptr2 = 0
    newList = []
    while ptr1 < len(list1) and ptr2 < len(list2):
        if list1[ptr1] <= list2[ptr2]:
            newList.append(list1[ptr1])
            ptr1 += 1
        else:
            newList.append(list2[ptr2])
            ptr2 += 1
    if ptr1 < ptr2:
        newList.append(list1[ptr1])
    else:
        newList.append(list2[ptr2])
    return newList


str1 = "racecar"
str2 = "bojangles"
str3 = "bennynneb"
isPalindrome(str1)
isPalindrome(str2)
isPalindrome(str3)
l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]
sortedList = mergeSortedLists(l1, l2)
print(sortedList)
# print("this is a break")
# isPalindromePtr(str1)
# isPalindromePtr(str2)
# isPalindromePtr(str3)

