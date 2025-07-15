"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
direction = input ("Do you want to convert (1:THB to USD, 2: USD to THB):")
amout = input ("Amout to convert:")

if direction == "1":
   result = amout / 35.5
   print(f"USD{result:.2f}")
if direction == "2":
   result = amout *35.5
   print(f"THB{result:.2f}")
