from Algorithms import Algorithms


def strStr(needle, haystack):
    ptrH = 0  # Used to parse through haystack string
    startIndex = 0
    ptrN = -1
    strN = ""
    if needle == " ":
        return -1
    while ptrH < len(haystack):
        if haystack[ptrH] == needle[0] and startIndex == 0:
            ptrN = ptrH
            ptrH += 1
            startIndex += 1
            strN += needle[0]
            # str += f'{needle[0]}'
        elif haystack[ptrH] == needle[startIndex]:
            ptrH += 1
            strN += needle[startIndex]
            # str += f'{needle[startIndex]}'
            startIndex += 1
            if needle == strN:
                break
        else:
            ptrH += 1
            ptrN = -1
    return ptrN


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
    # accounts for last element to be added
    if ptr1 < ptr2:
        newList.append(list1[ptr1])
    else:
        newList.append(list2[ptr2])
    return newList

#
# str1 = "racecar"
# str2 = "bojangles"
# str3 = "bennynneb"
# isPalindrome(str1)
# isPalindrome(str2)
# isPalindrome(str3)
# l1 = [1, 3, 5, 7, 9]
# l2 = [2, 4, 6, 8, 10]
# l3 = [11, 33, 55, 77, 99]
# l4 = [22, 32, 33, 58, 1010]
# l5 = [13, 69, 127, 349, 1001]
# l6 = [11, 34, 128, 312, 900]
# sortedList1 = mergeSortedLists(l1, l2)
# print(sortedList1)
# sortedList2 = mergeSortedLists(l3, l4)
# print(sortedList2)
# sortedList3 = mergeSortedLists(l5, l6)
# print(sortedList3)
# print("this is a break")
# isPalindromePtr(str1)
# isPalindromePtr(str2)
# isPalindromePtr(str3)


# needles = "hell", "nia", "kep", "nav", "llowe"
# haystacks = "hello", "california", "keeper", "banana", "halloween"
# for index in range(5):
#     print("Index of needle in haystack " + str(index)
#           + " is = " + str(strStr(needles[index], haystacks[index])))

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 9]
list3 = [9, 9, 9, 9, 9, 9, 9]
list4 = [9, 9, 9, 9]
list5 = [9, 8, 4, 7]
list6 = [6, 8, 1, 2, 9, 5, 4]
newList1 = Algorithms.addTwoLists(list1, list2)
newList2 = Algorithms.addTwoLists(list3, list4)
newList3 = Algorithms.addTwoLists(list5, list6)

print(newList1)
print(newList2)
print(newList3)
# print(list1[-1])

