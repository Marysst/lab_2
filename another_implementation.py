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

def function_correct():
    exit(0)

def function_incorrect():
    exit(1)

if __name__ == '__main__':
    try:
        translation_table = create_translation_table()
        text = stdin.readline().strip()

        encoded_text = encoder(text, translation_table) 
        stdout.write(f'Encoded text is: {encoded_text}\n')
    except ValueError as e:
        stderr.write(str(e) + '\n')
        function_incorrect()
    else:
        function_correct() 
