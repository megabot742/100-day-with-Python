import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# function
def caesar(star_text, shift_amount, cipher_direction):
    after_text = ""         # Get each letter for string
    if cipher_direction == "decode":       # Check between encode and decode
        shift_amount *= -1
    for letter in star_text:
        # Get position on alphabet
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount     # Get new position whit shift
            after_text += alphabet[new_position]        # Change new_position to new_letter + combine letter to string
        else:
            after_text += letter
    print(f"The {cipher_direction} text is {after_text}")
print(f"{art.logo}")

# Type 'yes' if you want to go again. Otherwise, type 'no'.
# they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
end_of_game = False
while not end_of_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    while shift > 26:
        shift %= 26
    caesar(star_text=text, shift_amount=shift, cipher_direction=direction)
    play_or_not = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if play_or_not == "no":
        end_of_game = True
        print("Goodbye")

