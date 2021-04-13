phonebook = {
    "Abe": 4893024839,
    "Bill": 2189375932,
    "Barry": 4190853213
}

print(phonebook)

# get specific value mapped to key
print(phonebook["Bill"])

# add to dictionary
phonebook["Herb"] = 8291235398

# change dict value
phonebook["Abe"] = 1111111

# delete / remove from dictionary
del phonebook["Barry"]

# Does Herb exist in the dict phonebook
if "Herb" in phonebook:
    print("yes")
else:
    print("no")

if "Herb" not in phonebook:
    print("yes")
else:
    print("no")


# print keys
for k in phonebook.keys():
    print(k)

# print values
print(phonebook.values())
print(phonebook.items())

# bundle key and value together
for (keys, values) in phonebook.items():
    print(keys, values)