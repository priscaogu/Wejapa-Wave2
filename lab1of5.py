elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}



#To insert the "is_noble_gas" I had to add a representation for it
elements["hydrogen"]["is_noble_gas"]="False"
elements["helium"]["is_noble_gas"]="True"
print(elements)

print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])