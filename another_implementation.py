import string
from sys import stdin, stderr, stdout, exit

def create_translation_table():
    return str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[13:] + string.ascii_lowercase[:13] + 
        string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
    )

def encoder(text: str, translation_table) -> str:
    if all(char.isascii() for char in text):
        return text.translate(translation_table)
    else:
        stderr.write('String must contain only Latin alphabet characters\n')
        raise ValueError('String must contain only Latin alphabet, digits and special characters')

def function_incorrect():
    exit(1)

def function_correct():
    exit(0)

if __name__ == '__main__':
    try:
        translation_table = create_translation_table()

        text = stdin.readline()
        
        encoder(text, translation_table)
        
        function_correct()

    except:
        function_incorrect()
