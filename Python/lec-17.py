s = {2, 2, 4 ,5}    
print(s)    # set doesn't take repeated values

# createing empty set
jarif = set()
print(type(jarif))

# Accessing set items
# Using  a for loop
info = {"Arham" , 19 , True , 5.4 }
for value in info:
    print(value) 

# Methods of Sets
# Union in sets
s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))

# Update in sets
s1.update(s2)
print(s1, s2)

# Intersection in sets
cities = {"Dhaka" , "Tokyo" , "Madrid", "Berlin"}
cities2 = {"Tokyo" , "Seoul", "Kabul" , "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

cities4 =  cities.intersection_update(cities2)  # Intersection update in sets
print(cities4)

cities5 = cities.symmetric_difference(cities2)   # symmetric_defference in sets
print(cities5)

