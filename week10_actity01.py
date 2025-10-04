'''
This function used for string and list analysing
'''
from typing import List, Union

InputDataType = Union[str, List[str]]

class DataAnalyzer:
    '''
    This class is the main class
    '''
    def __init__(self, data):
        '''
        Initial function
        '''
        if not isinstance(data, (str, list)):
            raise TypeError("Input must be a string or a list of strings.")
        self.data = data

    def get_total_length(self):
        '''
        Get total length function
        '''
        return len(self.data)

    def count_uppercase(self):
        '''
        Count function
        '''
        text_to_check = "".join(self.data) if isinstance(self.data, list) else self.data
        return sum(1 for char in text_to_check if char.isupper())

    def analyze(self):
        '''
        Analyzer function
        '''
        return {
            "input_data": self.data,
            "total_length": self.get_total_length(),
            "uppercase_characters": self.count_uppercase()
        }

    def calculate_digits_special_chars(self):
        '''
        Calculate digits and special cahrs
        '''
        digit_count = 0
        special_char_count = 0

        text_to_check = "".join(self.data) if isinstance(self.data, list) else self.data

        for char in text_to_check:
            if char.isdigit():
                digit_count += 1
            elif not char.isalnum() and not char.isspace():
                special_char_count += 1
        return digit_count, special_char_count


if __name__ == "__main__":
    STRING_INPUT = "Hello World From Python"
    LIST_INPUT = ["This", "Is", "A", "LIST"]

    analyzer1 = DataAnalyzer(STRING_INPUT)
    results1 = analyzer1.analyze()
    results1_digit, result1_sepcial = analyzer1.calculate_digits_special_chars()
    print(results1)
    print(f"This char's digits are {results1_digit}, and special chars are {result1_sepcial}")

    analyzer2 = DataAnalyzer(LIST_INPUT)
    results2 = analyzer2.analyze()
    results2_digit, result2_sepcial = analyzer1.calculate_digits_special_chars()
    print(results2)
    print(f"This char's digits are {results2_digit}, and special chars are {result2_sepcial}")
