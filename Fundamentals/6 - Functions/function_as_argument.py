# Sorting a dictionary by values.
# Defining a function to return the "value" from the (key, value) tuple,
# and passing it as an argument to the key in sorted() function.

dict1 = {'a': 3, 'b': 1, 'c': 2}

def get_values(item):
    return item[1]

sorted_dict1 = dict(sorted(dict1.items(), key=get_values))
print(sorted_dict1)  # Output = {'b': 1, 'c': 2, 'a': 3}