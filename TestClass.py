#Play with strings class
class Practice:

    def __init__(self, name, num1, num2):
        self.name = name
        self.num1 = num1
        self.num2 = num2

# this function demonstrates string slicing
    def reverse(self):
        reverse = self.name[len(self.name)::-1]
        return reverse

    def sum(self):
        return self.num1 + self.num2

    def getName(self):
        return self.name

    def getNum(self):
        return self.someNum


