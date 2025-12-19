def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

text = input("Please enter the text you wanna encrypt/decrypt: ")
enc_or_dec = input("Please enter 0 if you wanna encrypt the text and 1 otherwise: ")
shift = int(input("Please specify the required shift: "))

if enc_or_dec == 0 :
    print(encrypt(text, shift))
else:
    print(decrypt(text, shift))

