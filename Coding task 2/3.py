import random

def int_to_binary_check_bit(num):
    # Convert integer to binary string
    binary_str = bin(num)[2:]
    print(f"Binary representation of {num}: {binary_str}")
    # Choose a random position within the binary string
    pos = random.randint(0, len(binary_str) - 1)
    print(f"Random position chosen: {pos}")

    # Check if the bit at that position is 1 or 0
    if binary_str[pos] == '1':
        print(True)
    else:
        print(False)


int_to_binary_check_bit(79)
