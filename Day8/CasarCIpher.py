alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    ' '
    ]

direction = input("write 'encode' to encrypt and 'decode' to decrypt\n").lower()
text = input("Write your massage:\n").lower()
shift = int(input("Type your Shift Number: "))


def encrypt(massage,shift_number):
    ciphere_text = ""
    for letter in massage:
        shifted_position = alphabet.index(letter) + shift_number
        shifted_position%=len(alphabet)
        ciphere_text+=alphabet[shifted_position]

    print(f"Here is the encoded massage:\n{ciphere_text}")


def decrypt(massage,shift_number):
    output_text = ""
    for letter in massage:
        shifted_position = alphabet.index(letter)- shift_number
        shifted_position%=len(alphabet)
        output_text+=alphabet[shifted_position]

    print(f"Here is the decoded massage:\n{output_text}")


if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)
else:
    print("you made an error")