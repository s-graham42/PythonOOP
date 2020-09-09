class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for number in nums:
            self.result += number
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for number in nums:
            self.result -= number
        return self

md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)

addSubTest = MathDojo()
print(format(addSubTest.add(2,4,6,8,10,10,12,14,16,18).add(0.1, 1.1, 2.1, 3.1, 4.1, 5.1).add(0.003, 0.011, 0.021, 0.031).result, '.3f'))
print(format(addSubTest.subtract(10.6).subtract(19, 17, 15, 13, 11, 9).subtract(2.2, 4.4, 5.5, 0.66, 0.88, 0.99).result, '.3f'))

anotherAddSubTest = MathDojo()
print(format(anotherAddSubTest.add(2,4,6,8,10,10,12,14,16,18).add(0.1, 1.1, 2.1, 3.1, 4.1, 5.1).add(0.003, 0.011, 0.021, 0.031).subtract(10.6).subtract(19, 17, 15, 13, 11, 9).subtract(2.2, 4.4, 5.5, 0.66, 0.88, 0.99).result, '.3f'))