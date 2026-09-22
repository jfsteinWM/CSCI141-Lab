US = float(1.00)
EUR = float(1.08 * US)
GBP = float(1.21 * US)
CNY = float(0.15 * US)
INR = float(0.012 * US)

transaction_fee = US * 0.95

convert = input("Choose to convert (1. EUR, 2. GBP, 3. CNY, 4. INR): ")

dollar_amount = input("Enter dollar amount to exchange: ")

print("After fees you will receive", (dollar_amount * transaction_fee * convert, "in your chosen currency."))