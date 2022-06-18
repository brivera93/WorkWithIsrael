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
            index = index - 1

        else:
            index = index + 1
            if (strLen % 2 != 0) and (index == int(strLen / 2)):
            # and (index + 1 == int(strLen / 2) + 1)
                continue
            else:
                stack.append(char)
                # index = index + 1

    if not stack:
        print("palindrome")
    else:
        print("not a palindrome")


str1 = "racecar"
str2 = "bojangles"
str3 = "bennynneb"
# isPalindrome(str1)
# isPalindrome(str2)
isPalindrome(str3)
str3 = "racecar"
odd = len("racecar")
print(int(odd/2) + 1)