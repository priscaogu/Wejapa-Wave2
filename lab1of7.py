verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# To get the unique keys in a dictionary, the set() function is used, then to get the length the len() function is used.
num_keys =len(set(verse_dict))
print(num_keys)

# to check if a particular key is in a dictionary we use the get("name of key") function
contains_breathe = verse_dict.get('breathe')
print(contains_breathe)

#first convert the dictionary to a list
verse_list= list(verse_dict.items())

#then sort
sorted_keys = verse_list.sort()
print(verse_list)


# Using index 0 , we get the first value 
print(verse_list[0])

# to get the element with the highest value
list3 = max(list(verse_dict.values()))
print(list3) 

# to get the first key in the  dictionary
list2 = list(verse_dict.keys())[0]
print(list2)