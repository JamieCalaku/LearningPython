# Exercise 1 from lesson 14
# Task was to hide the complete credit card number except the last 4 digits

credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")