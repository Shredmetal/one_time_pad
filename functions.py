# alphabet list (duh)

import random

from encryptor_class import EncryptorObject

from decryptor_class import DecryptorObject

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# encryption function

def encrypt_new_cipher(t):

    # Generate text as a list of numbers, get rid of anything that's not a letter

    textlist = []
    for letter in t:
        if letter in alphabet:
            wordindex = alphabet.index(letter)
            textlist.append(wordindex)
        else:
            pass

    # Create lists for the text represented as numbers and the shift to be applied to the items, i.e. the cipher.

    shifted_list = []
    cipher_list = []

    # Randomly apply shift to each and every letter

    for shifted_number in textlist:
        s = random.randint(0, 25)
        if (shifted_number + s) > 25:
            over_number = (shifted_number + s) % 26
            shifted_list.append(over_number)
            cipher_list.append(s)
        else:
            normal_add_number = shifted_number + s
            shifted_list.append(normal_add_number)
            cipher_list.append(s)

    # Create the list of randomly shifted numbers which represent letters, converting them back to letters as we
    # go along.

    encrypted_text_unspaced = []
    for encrypted_letter in shifted_list:
        encrypted_text_unspaced.append(alphabet[encrypted_letter])

    # Scramble the shifted text

    encrypted_position = 0
    encrypted_objects_list = []

    for n in encrypted_text_unspaced:
        encrypted_objects_list.append(EncryptorObject(n, encrypted_position))
        encrypted_position += 1

    random.shuffle(encrypted_objects_list)

    encrypted_shuffled_text = []
    order_cipher = []

    for obj in encrypted_objects_list:
        encrypted_shuffled_text.append(obj.char)
        order_cipher.append(int(obj.position))

    # Introduce random spaces into the encrypted text - make sure that spaces DO NOT appear twice at a time, and the
    # text ALWAYS starts with a letter. Print the encrypted text.

    final_encrypted_text = []
    random_space = 1
    for encrypted_char in encrypted_shuffled_text:
        if random_space == 0:
            final_encrypted_text.append(encrypted_char)
            final_encrypted_text.append(" ")
        else:
            final_encrypted_text.append(encrypted_char)
        random_space = random.randint(0, 4)
    print(f"\nThe encoded text is: \n\n{''.join(final_encrypted_text)}\n")
    print(f"The cipher is: {cipher_list}")
    print(f"The order cipher is: {order_cipher}")

def encrypt_preset_cipher(t):

    # Generate text as a list of numbers, get rid of anything that's not a letter

    textlist = []
    for letter in t:
        if letter in alphabet:
            wordindex = alphabet.index(letter)
            textlist.append(wordindex)
        else:
            pass

    # Create a list for the text and a list for the cipher which is to be received as an input.
    # Use % to run through the cipher list again once it has been exhausted.

    shifted_list = []
    cipher = input("\nType the cipher:\n")
    cipher_list = cipher.split(", ")
    cipher_index = 0
    for shifted_number in textlist:
        s = cipher_index % len(cipher_list)
        if (shifted_number + int(cipher_list[s])) > 25:
            over_number = (shifted_number + int(cipher_list[s])) % 26
            shifted_list.append(over_number)
            cipher_index += 1
        else:
            normal_add_number = shifted_number + int(cipher_list[s])
            shifted_list.append(normal_add_number)
            cipher_index += 1

    # Create the list of randomly shifted numbers which represent letters, converting them back to letters as we
    # go along.

    encrypted_text_unspaced = []

    for encrypted_letter in shifted_list:
        encrypted_text_unspaced.append(alphabet[encrypted_letter])

    # Scramble the shifted text up, produce an order_cipher

    encrypted_position = 0
    encrypted_objects_list = []

    for n in encrypted_text_unspaced:
        encrypted_objects_list.append(EncryptorObject(n, encrypted_position))
        encrypted_position += 1

    random.shuffle(encrypted_objects_list)

    encrypted_shuffled_text = []
    order_cipher = []

    for obj in encrypted_objects_list:
        encrypted_shuffled_text.append(obj.char)
        order_cipher.append(int(obj.position))

    # Introduce random spaces into the encrypted text - make sure that spaces DO NOT appear twice at a time, and the
    # text ALWAYS starts with a letter. Print the encrypted text.

    final_encrypted_text = []

    random_space = 1
    for encrypted_char in encrypted_shuffled_text:
        if random_space == 0:
            final_encrypted_text.append(" ")
            final_encrypted_text.append(encrypted_char)
        else:
            final_encrypted_text.append(encrypted_char)
        random_space = random.randint(0, 4)

    print(f"\nThe encoded text is: \n\n{''.join(final_encrypted_text)}\n")
    print(f"The order cipher is: {order_cipher}")



# decryption function

def decrypt_known(t, s):

    # Generate text as a list of numbers, ditch anything that is not a letter.

    scrambled_text_list = []
    for letter in t:
        if letter in alphabet:
            word_index = alphabet.index(letter)
            scrambled_text_list.append(word_index)
        else:
            pass

    # Unscramble the text

    order_cipher_input = input("\nPlease enter the order cipher: \n")
    order_cipher_strings = order_cipher_input.split(", ")
    order_cipher = []

    for order_cipher_int in order_cipher_strings:
        order_cipher_item = int(order_cipher_int)
        order_cipher.append(order_cipher_item)

    scrambled_object_list = []

    for n in range(0, len(scrambled_text_list)):
        scrambled_object_list.append(DecryptorObject(scrambled_text_list[n], order_cipher[n]))

    unscrambled_object_list = sorted(scrambled_object_list, key=lambda x: x.position)

    textlist = []

    for obj in unscrambled_object_list:
        textlist.append(obj.char)


    ## don't forget to call whatever unscrambled text appears "textlist"

    # Convert the cipher into a list of ints.

    cipher_list_strings = s.split(", ")
    cipher_list = []
    for cipher_ints in cipher_list_strings:
        cipher_list_item = int(cipher_ints)
        cipher_list.append(cipher_list_item)

    # Start the cipher index off at 0. Increase by one for every pass. There should only be letters at this point.
    # In cases where the text is longer than the cipher list, use % to restart the list.
    # Note - the 'test value' code can be fucked around with if you want cipher values that are like 125.
    # Use % to get the remainder to determine how much to shift the characters by. This functionality has not
    # been implemented yet.

    shifted_list = []
    cipher_index = 0
    for shifted_number in textlist:
        corrected_cipher_index = cipher_index % len(cipher_list)
        cipher_value = cipher_list[corrected_cipher_index]
        test_value = shifted_number - cipher_value
        if test_value < 0:
            under_number = test_value
            absolute_under_number = abs(under_number)
            corrected_under_number = 26 - absolute_under_number
            shifted_list.append(corrected_under_number)
            cipher_index += 1
        else:
            normal_subtract_number = shifted_number - cipher_value
            shifted_list.append(normal_subtract_number)
            cipher_index += 1

    # Convert the numbers back to letters and print.

    decrypted_text = []
    for decrypted_letter in shifted_list:
        decrypted_text.append(alphabet[decrypted_letter])
    print(f"The decrypted text is: \n\n{''.join(decrypted_text)}\n")

def generate_cipher():

    cipher_list = []

    cipher_length = input("How long do you want the cipher to be? Type a number: ")

    try:

        for n in range(0, int(cipher_length)):
            cipher_number = random.randint(0, 25)
            cipher_list.append(cipher_number)

    except TypeError or ValueError:

        return

    print(cipher_list)

