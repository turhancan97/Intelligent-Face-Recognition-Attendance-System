# Generate a password hash
from werkzeug.security import generate_password_hash

your_password = input("Enter your password: ")
print(
    "Please copy the generated hash for your password:",
    generate_password_hash(your_password),
)
