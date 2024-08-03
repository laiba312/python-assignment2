# Prompt the user for a temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert the temperature to Celsius using the formula
celsius = (fahrenheit - 32) * 5.0 / 9.0

# Output the result
print(f"Temperature: {fahrenheit}F = {celsius}C")
