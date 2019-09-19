

# """Calculate the price of dinner and tip percentage\n"""

# September 17, 2019\n

# CTI-110-P2HW1 - Meal Tip Calculator\n

# Doreen Strickland

###The total cost for food.###

food = float( input ("Please enter the charge for food"))

###The tip percentage is .15%###

tip = float ( input ("Please enter the tip for server"))

###The tax rate is 0.06%####

tax = float ( input ("Please enter tax amount"))

###The value for the food times the tip###

tipValue = food * tip

print ("The tip is $", format(tipValue, ".2f"))

###The value for the food times tax###

taxValue = food * tax

print ("The tax is $", format(taxValue, ".2f"))

###The total cost for food, tip, and tax.###

totalCost = food + tipValue + taxValue

print ("The total cost is $", format(totalCost, ".2f"))
                              

    





