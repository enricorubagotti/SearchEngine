my_dict = {"apple": 5, "banana": 3, "cherry": 8, "date": 1}

# Sort the dictionary items by their values in descending order
sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

# Iterate over the sorted keys
for key, value in sorted_items:
    print(str(key)+"="+str(value))
