#You are given two lists of numbers and you need to find the total of each of these list
#tom_exp_list =[2100,3400,3500]
#joe_exp_list =[200,500,700]

#Without using a funtioon
#total = 0
#for item in tom_exp_list:
#    total = total + item
#print("Tom's total is:", total)
#
#total = 0
#for item in joe_exp_list:
 #   total=total + item
#print("Joe's total is:", total)

#Using a Funtion
def calculate_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total

tom_exp_list =[2100,3400,3500]
joe_exp_list =[200,500,700]
toms_total = calculate_total(tom_exp_list)
joe_total = calculate_total(joe_exp_list)

print("Tom's total expenses:", toms_total)
print("Joe's total expenses:", joe_total)

