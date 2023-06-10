from functions import encrypt_new_cipher, encrypt_preset_cipher, decrypt_known, generate_cipher

endloop = False

while endloop == False:

    direction = input("\nType 'encrypt' to encrypt, type 'decrypt' to decrypt. Type 'generate' to generate a new "
                      "cipher: ").lower()

    if direction == "encrypt":
        new_cipher = input("\nDo you wish to generate a new cipher? Type 'yes' or 'no': ").lower()
        if new_cipher == "yes" or new_cipher == "y":
            text = input("\nType your message:\n").lower()
            encrypt_new_cipher(t=text)
        elif new_cipher == "no" or new_cipher == "n":
            text = input("\nType your message:\n").lower()
            encrypt_preset_cipher(t=text)
        else:
            pass
    elif direction == "decrypt":
        text = input("\nType your message:\n").lower()
        cipher = input("\nType the cipher:\n")
        decrypt_known(t=text, s=cipher)
    elif direction == "generate":
        generate_cipher()
    else:
        print("Unrecognised input.")

    ending_instruction_loop = True

    while ending_instruction_loop == True:

        ending_instruction = input("Do you want to run the program again? (Yes or No)\n").lower()

        if ending_instruction == "yes":
            endloop = False
            ending_instruction_loop = False
        elif ending_instruction == "no":
            endloop = True
            ending_instruction_loop = False
            print("\nProgram terminated.")
        else:
            print("\nInvalid input. Please type 'yes' or 'no'.\n")

