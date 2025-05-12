'''
Implementation of roman to integer problem
'''

class RomanToInteger:
    """
    This class maps each roman numeral character to its integer value.
    """

    def __init__(self, roman_numeral: str):
        self.roman_numeral = roman_numeral
        self.__roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                              'C': 100, 'D': 500, 'M': 1000}
        self.total = 0

    def roman_to_int(self) -> int:
        prev_value = 0
        for char in reversed(self.roman_numeral.upper()):
            if self.__roman_map[char] < prev_value:
                self.total -= self.__roman_map[char]
            else:
                self.total += self.__roman_map[char]
            prev_value = self.__roman_map[char]
        return self.total


if __name__ == '__main__':
    obj = RomanToInteger('MCMXCIV')
    result = obj.roman_to_int()
    print(result)
