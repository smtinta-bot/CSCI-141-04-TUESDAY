currencies = ["EUR", "GBP", "CNY", "INR"]
rates = [1.08, 1.21, 0.15, 0.012]

choice = int(input("Choose to convert to 1. EUR 2. GBP 3. CNY 4. INR: ")) - 1

amount_str = input("Enter dollar amount to exchange: ")
amount = float(amount_str[1:])

after_fee = amount * 0.95

converted = round (after_fee / rates[choice])

print("After fees you will receive", currencies[choice], converted)