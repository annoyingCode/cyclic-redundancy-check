def generate_crc(input_data, key):

    original_data = ''.join(format(ord(x), '08b') for x in input_data)

    binary_key = key

    # To keep track of the previous iteration XOR result
    old_xor = ""

    # Get the length of the zeros to be appended
    zeros_to_append = len(binary_key) - 1

    # Modified data where we append zeros at the end of the original data
    appended_data = original_data + ("0" * zeros_to_append)

    # This pointer will keep track of the bit position (last bit) that
    # will be appened from the appended_data to the XOR result at the end
    # of each iteration
    pointer = 0

    for i in range(len(original_data)):

        # XOR to calculate for current iteration
        new_xor = ""

        # This will run for the rest of the first iteration
        if i > 0:

            # Ignore the firt bit (start from 1st index)
            if old_xor[1] == "1":
                for j in range(0, len(binary_key)):
                    new_xor += str(int(binary_key[j]) ^ int(old_xor[j + 1]))

                new_xor += appended_data[pointer]
                old_xor = new_xor

            elif old_xor[1] == "0":
                tmp_binary_key = "0" * len(binary_key)
                for j in range(0, len(binary_key)):
                    new_xor += str(int(tmp_binary_key[j])
                                   ^ int(old_xor[j + 1]))

                new_xor += appended_data[pointer]
                old_xor = new_xor

            # Because there will be no bit left in the last iteration which will cause exception
            # list index out of range
            if pointer != len(appended_data) - 1:
                pointer += 1

        # This will run for the first iteration
        else:
            if appended_data[pointer] == "1":
                for j in range(len(binary_key)):
                    old_xor += str(int(binary_key[j]) ^ int(appended_data[j]))
                    pointer += 1

                old_xor += appended_data[pointer]

            elif appended_data[pointer] == "0":
                tmp_binary_key = "0" * len(binary_key)
                for j in range(len(binary_key)):
                    old_xor += str(int(tmp_binary_key[j])
                                   ^ int(appended_data[j]))
                    pointer += 1

                old_xor += appended_data[pointer]

            if pointer != len(appended_data) - 1:
                pointer += 1

    # Remove the last extra appended bit and return the tuple
    return (original_data, old_xor[1:-1])
