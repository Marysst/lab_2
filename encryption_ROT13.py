from sys import stdin, stderr, stdout, exit

def encoder(text: str) -> str:
    encoded = ''
    for char in text:
        if char.isascii():
            if char.islower():
                encoded += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            elif char.isupper():
                encoded += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                encoded += char
        else:
            stderr.write('String must contain only Latin alphabet, digits and special characters\n')
            exit(1)
    stdout.write(f'Encoded text is: {encoded}\n')
    exit(0)

if __name__ == '__main__':
    stdout.write(f'Encoded text is: {encoder(stdin.readline())}\n')
