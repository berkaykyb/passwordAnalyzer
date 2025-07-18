import string
import random

def checkPasswordStrength(password, popularPasswords):
    score = 0
    print("\n--- Password Check Report ---")
    if len(password) >= 8:
        score+=3
        print("\nPassword length is sufficient (✓)")
    else:
        print("\nPassword length is less than 8 (✗)")
    if any(char.isupper() for char in password):
        score+=1
        print("Contains an uppercase letter (✓)")
    else:
        print("Missing an uppercase letter (✗)")
    if any(char.islower() for char in password):
        score+=1
        print("Contains a lowercase letter (✓)")
    else:
        print("Missing a lowercase letter (✗)")
    if any(char.isdigit() for char in password):
        score+=1
        print("Contains a digit (✓)")
    else:
        print("Missing a digit (✗)")
    if any(char in string.punctuation for char in password): #special characters check
        score+=1
        print("Contains a special character (✓)")
    else:
        print("Missing a special character (✗)")
    if password in popularPasswords:
        return "This password is 'Very Weak' - found in the '10k Popular Passwords List'."

    
    if score <= 4:
        return "Weak Security"
    elif score in [5,6]:
        return "Medium Security"
    else:
        return "Strong Security"
    
def fixPassword(password):
    specialChar = string.punctuation
    password_chars = list(password)
    if not any(c.isupper() for c in password):
        index = random.randint(0, len(password_chars))
        password_chars.insert(index, random.choice(string.ascii_uppercase))
    if not any(c.islower() for c in password):
        index = random.randint(0, len(password_chars))
        password_chars.insert(index, random.choice(string.ascii_lowercase))
    if not any(c.isdigit() for c in password):
        index = random.randint(0, len(password_chars))
        password_chars.insert(index, random.choice(string.digits))
    if not any(c in specialChar for c in password):
        index = random.randint(0, len(password_chars))
        password_chars.insert(index, random.choice(specialChar))

    while len(password_chars) < 8:
        index = random.randint(0, len(password_chars))
        password_chars.insert(index, random.choice(string.ascii_letters + string.digits + specialChar))

    return ''.join(password_chars)

    
def loadPopularPasswords(filename):
    popularPasswords = set()
    try:
        with open(filename, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                popularPasswords.add(line.strip())
    except FileNotFoundError:
        print(f"Warning: '{filename}' not found.")
    return popularPasswords

def main():
    popularPasswords = loadPopularPasswords("10k-most-common.txt")
    password = input("Enter a password to check: ")
    result = checkPasswordStrength(password, popularPasswords)
    print("\nPassword Strength:", result)

    if result != "Strong Security":
        print("\n--- Auto-fixed Suggestions ---")
        fixed1 = fixPassword(password)
        fixed2 = fixPassword(password)
        fixed3 = fixPassword(password)
        print("Fixed Password 1:", fixed1)
        print("Fixed Password 2:", fixed2)
        print("Fixed Password 3:", fixed3)
        print("\nRechecking Fixed Passwords...")
        result = checkPasswordStrength(fixed1, popularPasswords)
        print("\nNew Passwords Strength:", result)

if __name__ == "__main__":
    main()