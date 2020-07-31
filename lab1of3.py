# Use this playground to experiment with list methods, using Test Run

#list.append(item). This is used to add an item or a list to a list.

colours = ["red", "red", "blue", "yellow"]
append_item = colours.append("pink")
print(colours)
colour_1 = ["green", "white", "lemon"]
append_list = colours.append(colour_1)
print(colours)

#list.count() is used to count the number of times an element appear in a list
count_list = colours.count("red")
print(count_list)

#list.copy() is used to make a copy of tge list
copied_list = colours.copy()
print(copied_list)

#list.extend() adds elements of another list to the list directly.
colours.extend(colour_1)
print(colours)

#list.index tells the index of an element of a list
index_list = colours.index("blue")
print(index_list)

#list.insert() puts an element in a particular index in a list
colours.insert(5,"purple")
print(colours)

#list.pop removes an item in a given index and returns the item
list_pop = colours.pop(5)
print(list_pop)

#list.remove removes a given element and if there's a duplicate, the first matching one will be removed
colours.remove("red")
print(colours)

#list.reverse updates a list
colour_1.reverse()
print(colour_1)

#list.sort is used to order a list either in ascending order
colour_1.sort()
print(colour_1)

# or descending order
colour_1.sort(reverse=True)
print(colour_1)


#list.clear() is used to clear the elements of a list
colours.clear()
print(colours)

#values cannot be assigned when adding, reversing, removing, sorting or clearing elements from a list

