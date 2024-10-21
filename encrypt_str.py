def encrypt(input_string, stride):
    word = ""
    for i in range(stride):
       word += input_string[i::stride]

    new_string = word
    encrypted_string = ''
    print(encrypted_string)
    for i in range(len(new_string)):
        char = new_string[i]
        ordinal_value = ord(char)
        new_ordinal_value = ordinal_value + i
        encrypted_char = chr(new_ordinal_value)
        encrypted_string += encrypted_char

    return encrypted_string
def decrypt(input_string, stride):
    dencrypted_string = ''
    for i in range(len(input_string)):
        char = input_string[i]
        ordinal_value = ord(char)
        new_ordinal_value = ordinal_value - i
        encrypted_char = chr(new_ordinal_value)
        dencrypted_string += encrypted_char
    chunk_size = len(dencrypted_string) // stride
    remainder = len(dencrypted_string) % stride

    og_string= ''
    for i in range(chunk_size):
        chunk_number = 0
        current_index = i
        while current_index < len(dencrypted_string):
            og_string += dencrypted_string[current_index]
            current_index += chunk_size
            if chunk_number < remainder:
                current_index += 1
            chunk_number += 1

    current_index = chunk_size
    for character in range(remainder):
        og_string += encrypted_string[current_index]
        current_index += chunk_size + 1

    return og_string




input_string = input("Enter a word:")
stride = int(input("Stride: "))


print(f'Encrypted: {encrypt(input_string, stride)}')
print(f'Decrypt: {decrypt(encrypt(input_string, stride), stride)}')
