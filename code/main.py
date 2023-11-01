import divisor_generator as gdiv
import crc_generator as gcrc

key = input("Enter the equation: ")
data = input("Enter your data: ")

binary_key = gdiv.generate_divisor(key)
crc = gcrc.generate_crc(data, binary_key)

print(f"Original data (binary): {crc[0]} | CRC: {crc[1]}")
