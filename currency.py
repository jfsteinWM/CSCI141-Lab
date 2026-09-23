US = float(1.00)
EUR = float(US/1.08)
GBP = float(US/1.21)
CNY = float(US/0.15)
INR = float(US/0.012)

transaction_fee = 0.95

convert = input("Choose to convert (1. EUR, 2. GBP, 3. CNY, 4. INR): ")

dollar_amount = float(input("Enter dollar amount to exchange: ").replace("$", ""))

rates = {
    "1": EUR,
    "2": GBP,
    "3": CNY,
    "4": INR
}

currencies = {
    "1": "EUR",
    "2": "GBP",
    "3": "CNY",
    "4": "INR"
}

amount_after_fee = dollar_amount * transaction_fee
converted_amount = amount_after_fee * rates[convert]

print("After fees you will receive", currencies[convert], converted_amount)