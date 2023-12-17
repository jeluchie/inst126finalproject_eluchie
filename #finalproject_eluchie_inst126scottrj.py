#Comment
#Final Project INST126



#This is code for a One-Time Password (OTP) Generator. 

# Importing required modules
import random
import string

# Function to generate a one-time password
def generate_otp(length=9):
    # Using string.ascii_letters and string.digits to include both letters and numbers
    characters = string.ascii_letters + string.digits
    otp = ''.join(random.choice(characters) for i in range(length))
    return otp

# User input for OTP length
otp_length = int(float(input("Enter the length of the OTP: ")))

# Generate OTP
generated_otp = generate_otp(otp_length)

# Display the generated OTP
print(f"Generated OTP: {generated_otp}")

# Save OTP to a file
file_path = "./data/otp.txt"
with open(file_path, "w") as file:
    file.write(f"Generated OTP: {generated_otp}")

# Conditionals and Error Handling
try:
    # Converting the OTP to an integer to check its validity
    int(generated_otp)
    print("OTP is valid.")
except ValueError:
    print("Error: OTP contains non-numeric characters.")

# Iteration: Loops
# Code to generate and display multiple OTPs
num_otps = 3
for _ in range(num_otps):
    print(f"Generated OTP: {generate_otp(otp_length)}")

# Iteration: Lists, Dictionaries, and Tuples
# Store generated OTPs in a list
otp_list = [generate_otp(otp_length) for _ in range(num_otps)]
print("Generated OTPs:", otp_list)

# Documentation
"""
This script generates a one-time password (OTP) based on user input for the OTP length.
The generated OTP is displayed, saved to a file, and checked for validity.
Multiple OTPs are generated in a loop, and the generated OTPs are stored in a list.
"""