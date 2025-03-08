import datetime

def is_weekday():
    # Get the current day of the week (0=Monday, 6=Sunday)
    today = datetime.datetime.today().weekday()
    
    if today < 5:
        print("Yes, unfortunately today is a weekday.")
    else:
        print("It is the weekend, yay!")

if __name__ == "__main__":
    is_weekday()

# References - Python Software Foundation. (2024). 
# datetime — Basic date and time types. Python 3.12 Documentation. Retrieved from: https://docs.python.org/3/library/datetime.html
# datetime.date.weekday() Method. Python 3.12 Documentation. Retrieved from: https://docs.python.org/3/library/datetime.html#datetime.date.weekday
# What does if name == 'main' do?. Python FAQ. Retrieved from: https://docs.python.org/3/library/main.html