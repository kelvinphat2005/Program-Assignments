cities = ["Oakland","Atlanta","New York City","Seattle","Memphis","Miami","Boston","Los Angeles","Denver","New Orleans"]
desserts = ["Cake","Ice Cream","Cupcakes","Pie","Brownies","Cookies"]

print(cities[0])
print(cities[2])
print(cities[6])

#slicing
three_cities = cities[0:3]
print(three_cities)
four_desserts = desserts[0:4]
print(four_desserts)

#changing lists
cities[0] = "San Francisco"
cities[2] = "Brooklyn"
cities[7] = "Hollywood"
cities[5] = "Tampa"
print(cities)

#adding to lists
cities.append("New Jersey")
cities.extend(["Santa Cruz","Selma","Chicago"])
cities.insert(7,"Washington, D.C")
print(cities)

cities.append("Oakland")
cities.extend(["New York City","Los Angeles"])
cities.insert(0,"Miami")
print(cities)

#deleting in lists
del cities[7]
cities.pop(0)
cities.remove("Chicago")
print(cities)