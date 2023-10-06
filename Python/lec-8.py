# Break and Continue in Python

# Break Statement with for loop

for i in range(12):
    print('5 X' , i , '=' , 5 * i)
    if i == 10 :    #condition for break
        break

print('ran away ---')

# Break statement with while loop

num = 4
num2 = 0
while num2 < 12: 
    print(num , "X" , num2 +1  , "=" , num*(num2+1))
    num2 += 1
    if num2 == 10: #condition for break
        break
print("Ran away --")


# continue statement with for loop

for k in range(1,13):
    print('4 + ' , k , '=' , 4+i)
    if k == 10:
        continue
print('skip the iteration')

# continue statement with while loop

num3 = 4
num4 = 0
while num4 <= 13:
    print(num3 , "+" , num4 , "=" , num3+num4)
    num4 += 1
    if num4 == 10:
        continue
print("Skip the iteration")
