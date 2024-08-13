# Encoder
# GOALS:
# BASE64 ENCODER/DECODER
# BINARY ENCODER/DECODER


# Base64 encoding scheme character set consists of 64 characters
BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encode_binary_8(data):
    binary_list = []

    for char in data:
        ascii_val = ord(char)
        ascii_val_binary = format(ascii_val, '08b')
        binary_list.append(ascii_val_binary)

    binary_representation = ''.join(binary_list)
    binary_representation_spaces = ' '.join(binary_list)

    return binary_representation

def encode_base64(data):

    binary_string = encode_binary_8(data)

    # Calculate the padding length needed to make the binary string a multiple of 6
    padding_length = (6 - len(binary_string) % 6) % 6

    # Add the necessary padding to the binary string
    binary_string += '0' * padding_length

    # Initialize the encoded string
    encoded_string = ''

    # Iterate over the binary string in chunks of 6 bits
    for i in range(0, len(binary_string), 6):
        # Extract each 6-bit chunk
        six_bit_chunk = binary_string[i:i+6]
        # Convert the 6-bit chunk to an integer
        index = int(six_bit_chunk, 2)
        # Get the corresponding Base64 character and append to the encoded string
        encoded_string += BASE64_CHARS[index]

    # Calculate the number of padding characters needed
    padding_chars = '=' * (padding_length // 2)

    # Return the final encoded string with padding
    return encoded_string + padding_chars


    

# Example usage
data = input("\nEnter your input: ")
encoded_data_base64 = encode_base64(data)
encoded_data_binary8 = encode_binary_8(data)
print("\n8-bit binary representation of \"" + data + "\": " + encoded_data_binary8)
print("\nBase64 representation of \"" + data + "\": " + encoded_data_base64)


