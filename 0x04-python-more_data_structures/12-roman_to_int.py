#!/usr/bin/python3
def roman_to_int(roman_string):
    output = 0
    roman_dics = {'I': 1,
                  'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom_digit = roman_string
    if not roman_string or not isinstance(roman_string, str):
        return 0
    for i in range(len(rom_digit)):
        if i < len(rom_digit) - 1 and \
              roman_dics[rom_digit[i]] < roman_dics[rom_digit[i + 1]]:
            output -= roman_dics[rom_digit[i]]
        else:
            output += roman_dics[rom_digit[i]]
    return output
