"""Morse Code Translator"""

LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}

MORSE_TO_LETTER = {
    morse: letter
    for letter, morse in LETTER_TO_MORSE.items()
}


def encode(message: str) -> str:
    r"""
    Кодирует строку в соответсвие с таблицей азбуки Морзе

    >>> encode('SOS')
    '... --- ...'
    >>> encode("Not caps")
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/doctest.py", line 1346, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest morse.encode[1]>", line 1, in <module>
        encode("Hahaha\n")
      File "/Users/buchkovv/PycharmProjects/avito_analytics_academy/python_hw/hw_3_testing/MORSE.py", line 43, in encode
        encoded_signs = [
      File "/Users/buchkovv/PycharmProjects/avito_analytics_academy/python_hw/hw_3_testing/MORSE.py", line 44, in <listcomp>
        LETTER_TO_MORSE[letter] for letter in message
    KeyError: 'o'
    >>> encode("SPECIALSYMBOL\n")
    Traceback (most recent call last):
    KeyError
    >>> encode('') #doctest: +SKIP
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """
    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]

    return ''.join(decoded_letters)


if __name__ == '__main__':
    morse_msg = '-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.'
    decoded_msg = decode(morse_msg)
    print(decoded_msg)

    assert morse_msg == encode(decoded_msg)
