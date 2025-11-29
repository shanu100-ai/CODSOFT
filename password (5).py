import random
import string

print("=== PASSWORD GENERATOR ===")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:", password)

input("\nPress Enter to exit...")