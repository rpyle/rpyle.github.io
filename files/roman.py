from __future__ import print_function

romans = [('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]
romans_str = ''.join([letter for letter, _ in romans])

def int_to_roman(conversion):
    ''' Converts an integer to a Roman numeral '''
    if conversion >= 5000 or conversion <= 0:
        raise ValueError("4range error")

    # Decrement value as numeral is assembled
    parts = []
    for letter, value in romans:
        while value <= conversion:
            conversion -= value
            parts.append(letter)
    return ''.join(parts)

def roman_to_int(conversion):
    ''' Converts a Roman numeral to an integer '''
    result = 0
    conversion = conversion.upper()

    # Step through string and add together Roman numerals and sum
    for letter, value in romans:
        while conversion.startswith(letter):
            result += value
            conversion = conversion[len(letter):]
  
    if len(conversion) != 0:
        raise Exception("invalid Roman numeral")
    if result >= 5000 or result <= 0:
        raise ValueError("range error")
    return result

if __name__ == "__main__":
    print('Enter a Roman numeral or Arabic number (European digits) for conversion:')
    convert = raw_input('>>> ')

    # Attempt to cast input to int and convert, else convert string to int
    try:
        print(int_to_roman(int(convert)))
    except ValueError as err:
        try:
            print(roman_to_int(convert))
        except ValueError as err:
            print(err)
        except Exception as err:
            print(err)