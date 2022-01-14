key_location = "sofa"
locations = ["garage", "living room", "chair", "sofa", "kitchen", "basement"]
for i in locations:
    if i == key_location:
        print("The key was found in:", i)
        break
    else:
        print("The key could not be located in ",i)