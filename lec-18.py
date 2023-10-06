dic = {
    643: "Jarif",
    673: "Siyam",
    142: "Adi",
    354: "Mubeen"
}

print(dic[643])

info = {
    "Name" : "Jarif",
    "Age" : 15,
    "Eligible": True 
}

print(info)
# print(info['Name'])
print(info.get('Name'))
print(info.keys())   # Accessing all keys

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}      ")
