"""Problem: Check password strength."""

# Problem:
# Decide whether a password is strong.

password = "Strong@123"

# Solution:
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Strong password")
else:
    print("Weak password")

# Logic:
# 1. Check length.
# 2. Check uppercase, lowercase, digits, and special characters.
# 3. All conditions must be true for a strong password.

# Explanation:
# Validation problems often use multiple boolean checks.
