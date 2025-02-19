
amount1 = int(input("Enter amount1 (in cent): ").strip())
amount2 = int(input("Enter amount2 (in cent): ").strip())

total_cents = amount1 + amount2

euros = total_cents // 100  
cents = total_cents % 100    

print(f"The sum of these is €{euros}.{cents:02d}")

#I had to do a bit of research to understand how to print it with 2 decimal places.
#I found the :02d format specifier, which means that the number will be printed with at least 2 digits,
#and if it has less than 2 digits, it will be padded with zeros.

#I also had to use // to get the integer division, and % to get the remainder.
#I then used f-strings to format the output.
