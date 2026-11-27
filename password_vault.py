import random
import string

# This is the file where we will save the passwords
VAULT_FILE = "my_vault.txt"

def generate_password(length):
    # Get all letters, numbers, and symbols
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    
    # Pick random characters and join them together
    password = ""
    for i in range(length):
        password = password + random.choice(characters)
        
    return password

print("================================")
print("       🔒 PASSWORD VAULT 🔒     ")
print("================================")

# 1. Ask for the website
website = input("Which website is this for? (e.g., GitHub): ")

# 2. Ask for the length
length_input = input("How long should the password be? (e.g., 12): ")
length = int(length_input)

# 3. Generate the password
new_password = generate_password(length)
print("\nGenerated Password: " + new_password)

# 4. Save it to the file
# The 'a' means 'append' (add to the end of the file, don't delete old ones)
with open(VAULT_FILE, "a") as file:
    file.write("Website: " + website + " | Password: " + new_password + "\n")

print("✅ Success! Password saved to " + VAULT_FILE)
print("================================\n")