import string

def checkPasswordStrength(password, popularPasswords):
    score = 0

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
    print("\nPassword strength : ", result)

if __name__ == "__main__":
    main()