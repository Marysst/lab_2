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
        stdout.write(f'Encoded text is: {encoder(stdin.readline())}\n')
    except:
        function_incorrect()
    else:
        function_correct()
