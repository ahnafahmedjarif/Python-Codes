# operation on Tuple in Python

countries = ("Spain" , "Italy"  , "Bangladesh" , "England" , "Germany")
temp = list(countries)
temp.append("Russia")  # add item
temp.pop(3)  #remove item
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

# count() Method
tuple1  = (0, 2, 2 ,1 , 3, 4 ,3 ,5)
res = tuple1.count(3) # counting 3 in the tuple
print(res)

# index() Method
tuple2 = (3, 4, 5, 6, 7 ,4, 3 , 5)
res2 = tuple2.index(5)
res3 = tuple2.index(3, 4 , 7)
print(res2)
print(res3)

