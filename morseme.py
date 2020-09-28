CHAR_MORSE_DICT = {'A': '.-',
                   'B': '-...',
                   'C': '-.-.',
                   'D': '-..',
                   'E': '.',
                   'F': '..-.',
                   'G': '--.',
                   'H': '....',
                   'I': '..',
                   'J': '.---',
                   'K': '-.-',
                   'L': '.-..',
                   'M': '--',
                   'N': '-.',
                   'O': '---',
                   'P': '.--.',
                   'Q': '--.-',
                   'R': '.-.',
                   'S': '...',
                   'T': '-',
                   'U': '..-',
                   'V': '...-',
                   'W': '.--',
                   'X': '-..-',
                   'Y': '-.--',
                   'Z': '--..',
                   '0': '-----',
                   '1': '.----',
                   '2': '..---',
                   '3': '...--',
                   '4': '....-',
                   '5': '.....',
                   '6': '-....',
                   '7': '--...',
                   '8': '---..',
                   '9': '----.',
                   ':': '---...',
                   ';': '-.-.-.',
                   '=': '-...-',
                   '?': '..--..',
                   '@': '.--.-.',
                   '_': '..--.-',
                   '!': '-.-.--',
                   "'": '.----.',
                   '"': '.-..-.',
                   '$': '...-..-',
                   '&': '.-...',
                   '(': '-.--.',
                   ')': '-.--.-',
                   '+': '.-.-.',
                   ',': '--..--',
                   '-': '-....-',
                   '.': '.-.-.-',
                   '/': '-..-.', }


def encrypt(input_text):
    cipher = ''
    for letter in input_text:
        if letter != ' ':
            cipher += CHAR_MORSE_DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher


def decrypt(input_text):
    input_text += ' '
    decipher = ''
    citext = ''
    for letter in input_text:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(CHAR_MORSE_DICT.keys())[list(CHAR_MORSE_DICT.values()).index(citext)]
                citext = ''
    return decipher
