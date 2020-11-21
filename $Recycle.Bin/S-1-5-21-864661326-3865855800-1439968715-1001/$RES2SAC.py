from faker import Faker
fake = Faker()



dict_1 = {"Number": {
    1: {4,5,6},
    
    3: {7,8,9},
    2: {10,11,12}
    
    }}

a = max(dict_1["Number"])
c = dict_1["Number"].values().count()
b = sorted(dict_1["Number"],reverse=True)
print(c)



