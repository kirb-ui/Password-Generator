import random

def password_lean():
    password_length = int(input("Enter password length: "))
    
    if password_length < 8:
        print("Password has to be at least 8 characters long!")
        return None
    return password_length

def password_generator(length):


    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    specialcharacter = '!@#$%&*'
    numbercharacter = '1234567890'

    all_characters = uppercase + lowercase + specialcharacter + numbercharacter

  
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(specialcharacter),
        random.choice(numbercharacter)
    ]

    password += random.choices(all_characters, k=length-4)

    random.shuffle(password)

    return ''.join(password)

def main():
    password_length = password_lean()
    if password_length:
        print("Generated password: ", password_generator(password_length))

if __name__ == "__main__":
    main()
