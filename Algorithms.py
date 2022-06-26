class Algorithms:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName(self):
        print(self.name)

    def factorial(self, num):
        if num < 2:
            return 1
        else:
            return num * self.factorial(num-1)

    @staticmethod
    def addTwoLists(list1, list2):
        ptr1 = len(list1) - 1  # point to last element in list1
        endList1 = False
        ptr2 = len(list2) - 1  # point to last element in list2
        endList2 = False
        sumList = []  # list containing some of list1, list2
        carry = False
        # currentSum = 0
        while not endList1 or not endList2:
            if endList1 and not endList2:
                if carry:
                    currentSum = list2[ptr2] + 1
                    if currentSum < 10:
                        carry = False
                        sumList.append(currentSum)
                    else:
                        sumList.append(0)
                else:
                    sumList.append(list2[ptr2])
                ptr2 -= 1
            elif not endList1 and endList2:
                if carry:
                    currentSum = list1[ptr1] + 1
                    if currentSum < 10:
                        carry = False
                        sumList.append(currentSum)
                    else:
                        sumList.append(0)
                else:
                    sumList.append(list1[ptr1])
                ptr1 -= 1
            else:  # not at the end of list1 or list 2 (i.e. there items to be processed in both lists)
                currentSum = list1[ptr1] + list2[ptr2] + 1 if carry else list1[ptr1] + list2[ptr2]
                carry = True if currentSum >= 10 else False
                if carry:
                    numStr = str(currentSum)
                    sumList.append(int(numStr[1]))
                else:
                    sumList.append(currentSum)
                ptr1 -= 1
                ptr2 -= 1
            endList1 = True if ptr1 < 0 else False
            endList2 = True if ptr2 < 0 else False
        if carry:
            sumList.append(1)
        return sumList



