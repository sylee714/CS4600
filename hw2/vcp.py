import sys, getopt

keys_dict = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
    'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
    'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
    'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
    'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
    'z': 25,
}

keys_list = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y',
            'z']

# e = m + k mod 26
# d = 26 + c - k mod 26
# Method to perfrom the Vigenere cipher.
# Takes in a key and a plain text to encrypt
def vig_cipher(key, plain_text):
    cipher_text = ""
    # key_val = keys_dict.get(key)
    j = 0 # index for key
    for i in range(len(plain_text)):
        if plain_text[i] in keys_list:
            # print("{} : {}".format(plain_text[i], key[j % len(key)]))
            # print((keys_dict.get(plain_text[i]) + keys_dict.get(key[j % len(key)])) % 26)
            cipher_text += keys_list[(keys_dict.get(plain_text[i]) + keys_dict.get(key[j % len(key)])) % 26]
            j += 1
        else:
            cipher_text += plain_text[i]

    return cipher_text

# Checks the key input.
# Only English letters are allowed
def checkInputKey(key):
    for letter in key:
        if not letter in keys_list:
            return True
    return False

# Treating only lower cases.
# Converts everything to lower cases
def main():
    invalid = True
    while invalid:
        print("Enter the key: ")
        key = input()
        invalid = checkInputKey(key.lower())

    print("Enter the string to encrypt: ")
    string = input()

    print("Encrpyted result: ")
    print(vig_cipher(key.lower(), string.lower()))

if __name__ == "__main__":
    main()