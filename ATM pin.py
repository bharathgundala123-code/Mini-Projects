CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3

def atm_pin_verification():
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        pin = input("Enter your ATM PIN: ")

        if pin == CORRECT_PIN:
            print("✅ PIN verified successfully. Access granted.")
            return
        else:
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            print(f"❌ Incorrect PIN. Attempts left: {remaining}")

    print("🔒 Card blocked due to too many incorrect attempts.")


# Run the program
atm_pin_verification()

