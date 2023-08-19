UNITIES = {
    '0': 'zero',
    '1': 'um',
    '2': 'dois',
    '3': 'três',
    '4': 'quatro',
    '5': 'cinco',
    '6': 'seis',
    '7': 'sete',
    '8': 'oito',
    '9': 'nove'
}

TEN_BASED = {
    '10': 'dez',
    '11': 'onze',
    '12': 'doze',
    '13': 'treze',
    '14': 'catorze',
    '15': 'quinze',
    '16': 'dezesseis',
    '17': 'dezessete',
    '18': 'dezoito',
    '19': 'dezenove'
}

DOZENS = {
    '2': 'vinte',
    '3': 'trinta',
    '4': 'quarenta',
    '5': 'cinquenta',
    '6': 'sessenta',
    '7': 'setenta',
    '8': 'oitenta',
    '9': 'noventa'
}

HUNDREDS = {
    '1': 'cento',
    '2': 'duzentos',
    '3': 'trezentos',
    '4': 'quatrocentos',
    '5': 'quinhentos',
    '6': 'seiscentos',
    '7': 'setecentos',
    '8': 'oitocentos',
    '9': 'novecentos'
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
    
    return f'{DOZENS.get(number[-2])} e {UNITIES.get(number[-1])}'


def write_hundred(number):
    if number == '100':
        return 'cem'
    
    return f'{HUNDREDS.get(number[-3])} e {write_number(number[-2:])}'


def strip_number(number):

    while number[0] == '0' and len(number) > 1:
        number = number[1:]
    
    return number   


print(write_number(input('Insira um número: ').strip()))