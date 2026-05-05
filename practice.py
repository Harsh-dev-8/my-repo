data = {"name": "harsh",
    "age":20,
    "grade": "f",
    "passed": "yes barely"
}
#print(data.get("name"))
#data.update({"grade": "d"})
#data.update({"school": "kvs"})

#keys = data.keys()
#value = data.values()
#for new_data in data.keys():
#    print(keys)

#keys = data.keys()
#values = data.values()

#all_values = keys , values

#for new_data in data.keys , data.values:
#    print(f"{keys} : {values}")
#    print(new_data)

for x,y in data.items():
    print(f"{x}: {y}")