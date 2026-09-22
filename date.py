date = input("Enter the date in US format (MM/DD/YY): ")
month, day, year = date.split("/")
iso_date = ("20" + year + "-" + month + "-" + day,)

print("the date in ISO 8601 extended format is:", iso_date)



