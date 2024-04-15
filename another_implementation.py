import string
from sys import stdin, stderr, stdout, exit

def create_translation_table():
    return str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[13:] + string.ascii_lowercase[:13] + 
        string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
    )

def encoder(text: str, translation_table) -> str:
    return text.translate(translation_table)

def function_incorrect():
    exit(1)

def function_correct():
    exit(0)

if __name__ == '__main__':
    try:
        translation_table = create_translation_table()

        text = stdin.readline()
        
        if all(char.isascii() for char in text):
            stdout.write(f'Encoded text is: {encoder(text, translation_table)}\n')
            function_correct()
        else:
            stderr.write('String must contain only Latin alphabet characters\n')
            function_incorrect()

    except:
        function_incorrect()
