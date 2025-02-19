def mask_account_number(account_number):
    length = len(account_number)
    if length <= 4:
        return account_number 
    else:
        masked_part = "X" * (length - 4)
        return masked_part + account_number[-4:]

account_number = input("Please enter a 10-digit account number: ").strip()
print(mask_account_number(account_number))


#deal with account number of any length
def mask_account_number(account_number):
    length = len(account_number)
    if length <= 1:
        return account_number 
    else:
        masked_part = "X" * (length - 1)
        return masked_part + account_number[-1:]

account_number = input("Please enter an account number: ").strip()
print(mask_account_number(account_number))
