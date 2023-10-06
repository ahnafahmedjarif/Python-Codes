# realine method

f = open('myfile2.txt' , 'r')
i = 0
while True:
    i += 1
    line =  f.readline()    
    if not line: 
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student {i} in math is : {m1*2} ")
    print(f"Marks of student {i} in english is : {m2*2} ")
    print(f"Marks of student {i} in bangla is : {m3 *2} ")

# writeline method
w = open('myfile3.txt' , 'w')
lines = ['line 1\n' , 'line 2\n' , 'line 3\n']
w.writelines(lines)
w.close

     