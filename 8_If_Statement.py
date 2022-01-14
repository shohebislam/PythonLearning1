indian = ["samosa", "daal", "naan"]
chinese =["egg role", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]

dish = input("Enter a dish name:")

if dish in indian:
    print("Indian")
elif dish in chinese:
    print("Chinese")
elif dish in italian:
    print ("Italian")
else:
    print("Based on the little knowledge I have, I don't know where this cuisine is from")



