UNITIES = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

TEN_BASED = {
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen'
}

DOZENS = {
    '2': 'twenty',
    '3': 'thirty',
    '4': 'fourty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety'
}

def write_number(number: (str, int)):
    number = str(number) if isinstance(number, int) else number
    number = strip_number(number)

    if len(number) > 3 or not number.isdecimal():
        raise TypeError(f'{number} is not supported')
    
    match len(number):
        case 1:
            return write_unity(number)
        case 2:
            return write_dozen(number)
        case 3:
            return write_hundred(number)
            

def write_unity(number):
    return UNITIES.get(number)


def write_dozen(number):
    if number[-2] == '1':
        return TEN_BASED.get(number)
    
    if number[-1] == '0':
        return DOZENS.get(number[-2])
    
    return f'{DOZENS.get(number[-2])}-{UNITIES.get(number[-1])}'


def write_hundred(number):
    coef = 'a' if number[-3] == '1' else UNITIES.get(number[-3])
    return f'{coef} hundred {write_number(number[-2:])}'


def strip_number(number):
    while number[0] == '0' and len(number) > 1:
        number = number[1:]
    
    return number   


print(write_number(input('Insert a number: ').strip()))