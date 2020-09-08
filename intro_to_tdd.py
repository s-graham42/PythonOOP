import unittest

def reverseList(list):
    for i in range(int(len(list)/2)):
        list[i], list[len(list)-i-1] = list[len(list)-i-1], list[i]
    return list

class ReverseArrayTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([1,3,5]), [5,3,1])
    def testTwo(self):
        self.assertEqual(reverseList([5,1,2,3,4,9]), [9,4,3,2,1,5])
    def testThree(self):
        self.assertEqual(reverseList([52,31,56,40,77,15,40]), [40,15,77,40,56,31,52])
    # def setUp(self):
    #     print("Running Setup.")
    # def tearDown(self):
    #     print("Running TearDown tasks.")

def isPalindrome(word):
    newWord = ""
    for i in range(len(word)-1, -1, -1):
        newWord += word[i]
    if word == newWord:
        return True
    else:
        return False

class IsPalindromeTests(unittest.TestCase):
    def testOne(self):
        self.assertTrue(isPalindrome('racecar'))
    def testTwo(self):
        self.assertEqual(isPalindrome('kayak'), True)
    def testThree(self):
        self.assertTrue(isPalindrome('step on no pets'))
    def testFour(self):
        self.assertFalse(isPalindrome('step on on pets'))
    def testFive(self):
        self.assertNotEqual(isPalindrome('racecar'), False)

# def coins(amount):
#     pass

# class IsPalindromeTests(unittest.TestCase):
#     def testOne(self):
#         self.assertEqual(coins(87), [3, 1, 0, 2])
    # def testTwo(self):
    #     self.assertEqual(isPalindrome('kayak'), True)
    # def testThree(self):
    #     self.assertTrue(isPalindrome('step on no pets'))
    # def testFour(self):
    #     self.assertFalse(isPalindrome('step on on pets'))
    # def testFive(self):
    #     self.assertNotEqual(isPalindrome('racecar'), False)


if __name__ == '__main__':
    unittest.main()