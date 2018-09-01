'''
	Assignment name: HW1.py

    A python program to encrypt or deccrypt a text file.

    Commands:
    d = decrypt
    e = encrypt
    1 = caesar cipher
    2 = simple substitution cipher
    3 = poly alphabetic cipher
    4 = transposition cipher
    5 =


    Usage: choose mode, choose cipher types, choose input file, choose output file



    @author Qingchen meng
'''


"""
    Caesar cipher: each letter of the text is replaced
    by the letter which stands a certain number of places
    before or after it in the alphabet.
    Reference:
        "Manual of Cryptography", 1911, page 28
        https://learncryptography.com/classical-encryption/caesar-cipher
        https://www.xarg.org/tools/caesar-cipher/
"""

def caesar_Encrypt(infile, outfile) :
    plain_file = open(infile, 'r')
    cipher_file = open(outfile, 'w')
    for line in plain_file:
        for letter in line:
                    # Only convert alphabetic characters
            if letter.isalpha():
                cipher_file.write(caesar_Encrypt_shift(letter))
            else:
                cipher_file.write(letter)

def caesar_Encrypt_shift(letter) :
    if (letter.isupper()):
        letter = chr((ord(letter) + 3 - 65) % 26 + 65)

        # Encrypt lowercase characters
    else:
        letter = chr((ord(letter) + 3 - 97) % 26 + 97)

    return letter


def caesar_Decrypt(infile, outfile) :
    plain_file = open(infile, 'r')
    cipher_file = open(outfile, 'w')
    for line in plain_file:
        for letter in line:
                    # Only convert alphabetic characters
            if letter.isalpha():
                cipher_file.write(caesar_Decrypt_shift(letter))
            else:
                cipher_file.write(letter)

def caesar_Decrypt_shift(letter) :
    if (letter.isupper()):
        letter = chr((ord(letter) - 3 - 65) % 26 + 65)

        # Encrypt lowercase characters
    else:
        letter = chr((ord(letter) - 3 - 97) % 26 + 97)

    return letter


"""
	Simple substitution cipher each letter of the message is replaced by
	a fixed substitute, usually also a letter.where the function f(m) is
	function with an inverse. The key is a permutation of the alphabet
	when the substitutes are letters.

	Reference:
		"The Mathamatical Theory of Cryptography", 1945, pages 31-32
		http://practicalcryptography.com/ciphers/simple-substitution-cipher/
		http://rumkin.com/tools/cipher/substitution.php

"""
key = 4

def substitution_Encrypt(infile, outfile) :
    plain_file = open(infile, 'r')
    cipher_file = open(outfile, 'w')
    for line in plain_file:
        for letter in line:
            if letter.isalpha():
                cipher_file.write(sub_Encrypt_shift(letter))
            else:
                cipher_file.write(letter)

def substitution_Decrypt(infile, outfile) :
    plain_file = open(infile, 'r')
    cipher_file = open(outfile, 'w')
    for line in plain_file:
        for letter in line:
            if letter.isalpha():
                cipher_file.write(sub_Decrypt_shift(letter))
            else:
                cipher_file.write(letter)

def sub_Encrypt_shift(letter) :
    if (letter.isupper()):
        letter = chr((ord(letter) + key - 65) % 26 + 65)

        # Encrypt lowercase characters
    else:
        letter = chr((ord(letter) + key - 97) % 26 + 97)

    return letter

def sub_Decrypt_shift(letter) :
    if (letter.isupper()):
        letter = chr((ord(letter) - key - 65) % 26 + 65)

        # Encrypt lowercase characters
    else:
        letter = chr((ord(letter) - key - 97) % 26 + 97)

    return letter


"""
	Polyaphabeical cipher consists of a set of twenty-six alphabets successively displaced
	one letter per row, with the plaintext letters at the top of the square,
	the key letters at the side, and the cipher letter inside.
	Reference:
	        "Friedman Lectures on Cryptography", 1965, page 29
	        https://www.geeksforgeeks.org/vigenere-cipher/
	        http://www.codingalpha.com/polyalphabetic-cipher-c-program/
"""


def alpha_Encrypt(infile, key):
    key = key.upper().replace(' ', '')
    plaintext = infile.upper().replace(' ', '')
    ciphertext = ''
    j = 0
    for i in range(len(plaintext)):
        ciphertext += chr((((ord(key[j]) - 65) + (ord(plaintext[i])) - 65) % 26) + 65)
        i += 1
        j += 1
        if j >= len(key):
            j = 0
    return ciphertext


def alpha_Decrypt(infile, key):
    key = key.upper().replace(' ', '')
    plaintext = ''
    j = 0
    for i in range(len(infile)):
        plaintext += chr((((ord(infile[i]) - 65) - (ord(key[j]) - 65)) % 26) + 65)
        i += 1
        j += 1
        if j >= len(key):
            j = 0
    return plaintext



"""
	Transposition cipher lines containing a certain number of letters
	are agreed upon, and the message is then wrriten out in lines
	of this lines;
	Reference:
        "Manual of Cryptography", 1911, page 21.
        https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_transposition_cipher.htm
        https://inventwithpython.com/hacking/chapter8.html
"""
def trans_Encrypt(key, infile, outfile):
    plain_file = open(infile, 'r')
    cipher_file = open(outfile, 'w')
    for line in plain_file:
        for letter in line:
            cipher_file = [''] * key
            for col in range(key):
                pointer = col
                while pointer < len(letter):
                    cipher_file[col] += letter[pointer]


def trans_Decrypt(key, infile, outfile):
    plain_file = open(infile, 'r')
    cipher_file = open(outfile, 'w')
    for line in plain_file:
        for letter in line:
            cipher_file = [''] * key
            for col in range(key):
                pointer = col
                while pointer < len(letter):
                    cipher_file[col] += letter[pointer]

"""
	The Affine cipher is a type of monoalphabetic substitution cipher,
	 wherein each letter in an alphabet is mapped to its numeric equivalent,
	 encrypted using a simple mathematical function, and converted back to a letter.
	Reference:
    https://www.geeksforgeeks.org/implementation-affine-cipher/
"""

ALPHABET_SIZE = 36

def affine_Encrypt(a, b, m, x):
    return (a*x+b)%m

def affine_Decrypt(a, b, m, y):

    return;



def main() :

    key1 = "zxcvbnmasdfghjklqwertyuiop"
    key2 = 8
    mode = input("Do you want to encrypt or decrypt?(encrypt = e, decrypt = d")
    type = input("Please choose the cipher type: 1 = Caesar cipher, 2 = simple substitution cipher, 3 = polyalphabetic cipher,"
                 "4 = transposition cipher, 5 = affine cipher")
    infile = input("Enter the name of your file: ")
    outfile = input("Enter the name of output file")
    if mode == 'e' and type == '1':
        caesar_Encrypt(infile, outfile)
    elif mode == 'd' and type == '1':
        caesar_Decrypt(infile, outfile)
    elif mode == 'e' and type == '2':
        substitution_Encrypt(infile,outfile)
    elif mode == 'd' and type == '2':
        substitution_Decrypt(infile, outfile)
    elif mode == 'e' and type == '3':
        alpha_Encrypt(infile, key1)
    elif mode == 'd' and type == '3':
        alpha_Decrypt(infile, key1)
    elif mode == 'e' and type == '4':
        trans_Encrypt(infile, key2, outfile)
    elif mode == 'd' and type == '4':
        trans_Decrypt(infile, key2, outfile)
    elif mode == 'e' and type == '5':
        trans_Encrypt(infile, key2, outfile)
    elif mode == 'd' and type == '5':
        trans_Decrypt(infile, key2, outfile)

main()




