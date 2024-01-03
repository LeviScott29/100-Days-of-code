

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
play_again = "yes"
print("welcome to ceaser cipher!")
while play_again=="yes":
    text = input("type your message to be encoded: \n").lower()
    shift = int(input("type your shift number \n "))
    direction = input(" type encode or decode: ")


    def ceaser( word, shift, direction):
        cipher_text=""
        if direction == "encode":
    # this iterates over the input and uses the list alphabet to reference letter positions using the index position
    # it then adds the shift value to the index and replaces the letter with the new index element for the output
    # if the input is not a letter it just appends it to the new phrase
        
            for char in word:
                if char in alphabet:
                   position = alphabet.index(char)
                   new_position = (position + shift)%26
                   new_letter = alphabet[new_position]
                   cipher_text +=new_letter
                else: cipher_text += char
            print("your encrypted message is: ", cipher_text)

        if direction == "decode":
    # this iterates over the input and uses the list alphabet to reference letter positions using the index position
    # it then subtracts the shift value to the index and replaces the letter with the new index element for the output
    # if the input is not a letter it just appends it to the new phrase
            for char in word:
                if char in alphabet:
                   position = alphabet.index(char)
                   new_position = position - shift
                   new_letter = alphabet[new_position]
                   cipher_text +=new_letter
                else: cipher_text += char
            print("your encrypted message is: ", cipher_text)

    ceaser(text, shift, direction)
    play_again =input("do you want to play again? yes or no?: ")

            
            
    
