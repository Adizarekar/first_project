indian = ["samosa", "vadapav", "pavbhaji"]
chinese = ["manchurian", "friedrice", "egg role"]
italian = ["pizza", "pasta"]

dish = input("Enter a cuisin: ")

if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print(dish , "is unknown")