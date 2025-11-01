import random
OTP_LENGTH = 4
MAX_ATTEMPTS = 5
def generate_otp():
    return f"{random.randint(0, 10**OTP_LENGTH - 1):0{OTP_LENGTH}d}"

def main():
    otp = generate_otp()
    print("OTP (for demo only):", otp)  
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        guess = input(f"Enter the {OTP_LENGTH}-digit OTP (attempt {attempts+1}/{MAX_ATTEMPTS}): ").strip()
        if guess == otp:
            print("Correct OTP. Verified.")
            return
        else:
            attempts += 1
            print("Incorrect OTP.")
    
    print("Too many failed attempts. Try again later.")

if __name__ == "__main__":
    main()
