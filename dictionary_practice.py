grocery_list = {
    "chicken":1.59,
    "beef":1.99,
    "cheese":1.00,
    "milk":2.50
}
game_prices = {
    "cyberpunk 2077":59.99,
    "witcher 3":39.99,
    "gta 5":29.99,
    "undertale":9.99
}

#assigning food prices
chicken_price = grocery_list["chicken"]
beef_price = grocery_list["beef"]
cheese_price = grocery_list["cheese"]
milk_price = grocery_list["milk"]

#assigning game prices
cyberpunk_price = game_prices["cyberpunk 2077"]
witcher_price = game_prices["witcher 3"]
gta_price = game_prices["gta 5"]
undertale_price = game_prices["undertale"]

#chaning game prices
game_prices["cyberpunk 2077"] -= -10.00
game_prices["witcher 3"] += 15.00
game_prices["gta 5"] -= 15.00
game_prices["undertale"] -= 10.00

#shoe inventory
shoe_inv = {
    "Jordan 13":1,
    "Yeezy":8,
    "Foamposite":10,
    "Air Max":5,
    "SB Dunk":20
}
#shoe inventory changes
shoe_inv["SB Dunk"] -= 2
shoe_inv["Yeezy"] += 1
shoe_inv["Jordan 13"] +=7
shoe_inv["Yeezy"] +=7
shoe_inv["Foamposite"] +=7
shoe_inv["Air Max"] +=7
shoe_inv["SB Dunk"] +=7
shoe_inv["Jordan 13"] -= 2
shoe_inv["Yeezy"] -= 2
shoe_inv["Foamposite"] -= 2
shoe_inv["Air Max"] -= 2
shoe_inv["SB Dunk"] -= 2

shoe_inv["Pegasus"] = 6
game_prices["Minecraft"] = 27.99

print(shoe_inv)

#deleting
del shoe_inv["SB Dunk"]
del shoe_inv["Air Max"]

#functions
def total_price(food1,food2):
    return "The total price of beef and cheese is " + str(grocery_list[food1] + grocery_list[food2])
print(total_price("beef","cheese"))
def price_difference(item1,item2):
    price = grocery_list[item1] - grocery_list[item2]
    return price
print(price_difference("beef","cheese"))

def restock(shoe,value):
    shoe_inv[shoe] += value
    return shoe_inv[shoe]
print(shoe_inv["Yeezy"])
restock("Yeezy",5)
print(shoe_inv["Yeezy"])

def clearance_sale(shoe,value):
    shoe_inv[shoe] = shoe_inv[shoe]//value
    return shoe_inv
print(shoe_inv["Jordan 13"])
clearance_sale("Jordan 13",5)
print(shoe_inv["Jordan 13"])