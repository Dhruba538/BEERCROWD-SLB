# Read an integer input between 1 and 12
month_number = int(input())

# List of months with the first letter capitalized
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

# Print the corresponding month if the input is valid
if 1 <= month_number <= 12:
    print(months[month_number - 1])
else:
    print("Invalid input. Please enter a number between 1 and 12.")
