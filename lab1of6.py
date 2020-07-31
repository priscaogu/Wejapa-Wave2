#COUNT UNIQUE

verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# To split a string into a list of words, the str.split() method is used and the delimeter " "
verse_list =verse.split(" ")
print(verse_list, '\n')

# To convert list to a data structure that stores unique values  set() is used.
verse_set = set(verse_list)
print(verse_set, '\n')

# To get the number of elements in a list, the len() function is used
num_unique = len(verse_set)
print(num_unique, '\n')