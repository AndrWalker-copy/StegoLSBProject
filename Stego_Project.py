from PIL import Image 
import numpy as np

def encode_LSB(image_path,message_bytes,bit_layers,component,output_path,step):
    message_bits = ''.join(format(byte, '08b') for byte in message_bytes)
    message_len_bits = format(len(message_bits), '032b') 
    print(len(message_bits))
    full_message_bits = message_len_bits + message_bits
    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = np.array(image)
    idx = 0
    message_len = len(full_message_bits)
    for b in range(0,bit_layers):
        for i in range(0, pixels.shape[0],step):
            for j in range(0, pixels.shape[1],step):
                    if idx != message_len:
                        if (full_message_bits[idx]=='1'): pixels[i,j,component] |= (1 << b)
                        if (full_message_bits[idx]=='0'): pixels[i,j,component] &= ~(1 << b)
                        idx += 1
                    else:
                        break
    new_image = Image.fromarray(pixels)
    new_image.save(output_path)

def decode_LSB(image_path, bit_layers, component,step):
    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = np.array(image)
    message_len_bits = []
    idx = 0
    for b in range(0,bit_layers):
        for i in range(0,pixels.shape[0],step):
            for j in range(0,pixels.shape[1],step):
                if idx < 32:
                    bit = (pixels[i, j, component] >> b) & 1
                    message_len_bits.append(bit)
                    idx += 1
                else:
                    break
    message_len = int(''.join(map(str, message_len_bits)), 2)
    message_bits = []
    idx = 0
    for b in range(0,bit_layers):
        for i in range(0,pixels.shape[0],step):
            for j in range(0,pixels.shape[1],step):
                    if idx < message_len+32:
                        bit = (pixels[i, j, component] >> b) & 1
                        message_bits.append(bit)
                        idx += 1
                    else:
                        break
    message_bits = message_bits[32:]
    message_bytes = bytearray(
        int(''.join(map(str, message_bits[i:i + 8])), 2)
        for i in range(0, len(message_bits), 8)
    )
    return bytes(message_bytes)

# output_path = "C:\\Users\\MyHonorPro\\Pictures\\result1.bmp"
# output_path2 = "C:\\Users\\MyHonorPro\\Pictures\\result3.bmp"
# component = 0
# message = "Hi world!!!!!world!!!!!" 
# bit_layers = 1
# step = 2
# input_path = "C:\\Users\\MyHonorPro\\Pictures\\test3.bmp"
# hidden_image_path = "C:\\Users\\MyHonorPro\\Pictures\\test2.bmp"

def encrypt_LSB_file(input_path, output_path, hidden_image_path, component, bit_layers, step):
    with open(hidden_image_path, "rb") as hidden_image_file:
            hidden_image_bytes = hidden_image_file.read()
    encode_LSB(input_path , hidden_image_bytes, bit_layers, component, output_path,step)

def decrypt_LSB_file(input_path, output_path, component, bit_layers, step):
    hidden_image_bytes = decode_LSB(input_path, bit_layers, component,step)
    with open(output_path, "wb") as hidden_image_file:
            hidden_image_file.write(hidden_image_bytes)
