def generate_divisor(key):

    key = key.split("+")
    binary_key = ""

    # Remove the last term which is just a coefficient ("x" with a power of zero)
    last_coefficient = key.pop() if key[-1].isdigit() else False

    # Get the powers from the terms
    key_powers = [term[1:] if len(term) > 1 else "1" for term in key]

    # Get the range to generate binary numbers equal to the length of the maximum power
    powers = range(int(key[0][1:] if len(key[0]) > 1 else "1"), 0, -1)

    for power in powers:
        if str(power) in key_powers:
            binary_key += "1"
        else:
            binary_key += "0"

    binary_key += "1" if last_coefficient else "0"

    return binary_key

# for i, term in enumerate(key):

#     if term.isalpha() and len(term) == 1:
#         term += "1"

#     is_digit = term[1:].isdigit()

#     # For first term
#     if i == 0 and len(term) > 1 and is_digit:
#         power = int(term[1:])
#         binary_key += "1"

#     elif i > 0 and is_digit:
#         pow_diff = power - 1
#         if pow_diff == term[1:]:
#             binary_key += "1"
#         else:
#             binary_key += "01"

#         power = term[1:]

#     else:
#         binary_key += "1"

# print(binary_key)
