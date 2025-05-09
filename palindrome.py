'''
You are give an integer x, return true if x is a palindrome, and false otherwise.

Hint: An integer is a palindrome when it reads the same forwards and backwards.
For example: 121 is a palindrome while 123 is not.

'''

class is_Palindrome:

    def __init__(self, num: int):
        self.num  = num

    def palindrome(self):
        reversed_num = int(str(self.num)[::-1])
        if self.num == reversed_num:
            return True
        return False
    
if __name__ == "__main__":
    obj = is_Palindrome(1001)
    result = obj.palindrome()
    print(result)

        