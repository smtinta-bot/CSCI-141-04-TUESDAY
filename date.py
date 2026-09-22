user_date = input("Enter the date in US format (MM/DD/YY): ")

month = user_date[0:2]
day = user_date[3:5]
year = user_date[6:8]

iso_date = "20" + year + "-" + month + "-" + day

print("The date in ISO 8601 extended format is:", iso_date)