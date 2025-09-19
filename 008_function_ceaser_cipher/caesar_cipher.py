from os import system

alphabet = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z"
]


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Result: {output_text}")


should_continue = True

while should_continue:
    system("cls || clear")
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = int(input("1 para rodar novamente, 2 para sair: "))
    if restart == 2:
        should_continue = False
        print("Farow")


# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     if encode_or_decode == "decode":
#         shift_amount = -shift_amount   # inverter fora do loop

#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]
#     print(f"Result: {output_text}")



# def encrypt(original_text: str, shift_amount: int) -> str:
#     cript_text = ""
#     for letter in original_text:
#         if letter == " ":
#             cript_text += " "
#         else:
#             shifted_position = alphabet.index(letter) + shift_amount
#             shifted_position %= len(alphabet)
#             new_letter = alphabet[shifted_position]
#             cript_text += new_letter
       
#     print(f"Text: {original_text} | Cifra: {cript_text}")


# def decrypt(cipher_text, shift_amount):
#     output_text = ""
#     for letter in cipher_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {output_text}")

# def decrypt(cipher_text, shift_amount):
#     alphabet.reverse()
#     decript_text = ""
#     for letter in cipher_text:
#         if letter == " ":
#             decript_text += " "
#         else:
#             shifted_position = alphabet.index(letter) + shift_amount
#             shifted_position %= len(alphabet)
#             new_letter = alphabet[shifted_position]
#             decript_text += new_letter
#     print(f"Text: {decript_text} | Cifra: {cipher_text}")