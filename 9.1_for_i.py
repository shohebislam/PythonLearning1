

exp = [2340, 2500, 2100, 3100, 2980] 
for i in range (len(exp)):
    print('Month:', (i+1), 'Expense:', exp[i])

total = 0
for item in exp:
    total= total + item
print ("My total expense is: ", total)