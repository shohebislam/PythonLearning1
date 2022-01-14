item1= "Bread"
item2 = "Pasta"
item3 = "Fruits"
item4 = "Vegetables"

items=["Bread","Pasta","Fruits","Vegetables"]
print(items)

print(items[2])
items[0]="Chips"
print(items[0])

print(items[0:2])
print(items[-1])

#What to do when you want to add an item to the list:

items.append("Butter")
print(items)

items=["Bread","Pasta","Fruits","Vegetables"]
print(items)
#What to do when we want the item to be in a specific location within the list?
items.insert(1,'butter')
print(items)

#How to combine 2 different lists?
food =["bread", "pasta", "fruits"]
bathroom = ["shampoo","soap"]
items= food+bathroom
print(items)

#How many items within the list?
print(len(items))
#Is x item within the list? e.g bread (USE in Funtion)
print("bread" in items)