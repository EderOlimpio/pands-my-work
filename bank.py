# Step 1: Read inputs as integers
amount1 = int(input("Enter amount1 (in cent): ").strip())
amount2 = int(input("Enter amount2 (in cent): ").strip())

# Step 2: Calculate total amount in cents
total_cents = amount1 + amount2

# Step 3: Convert to euros and cents
euros = total_cents // 100  # Integer division to get euro part
cents = total_cents % 100    # Modulus to get remaining cents

# Step 4: Print the result in human-readable format
print(f"The sum of these is €{euros}.{cents:02d}")  # Format cents with 2 digits