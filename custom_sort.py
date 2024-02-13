string_list = []

again = True
while again:
    string = input("Enter as many strings as you like. Enter 'x' to quit. ") 

    if string == 'x' or string == 'X':
        break

    string_list.append(string)

sorted_string_list = sorted(string_list, key=lambda x: (len(x), x)) # sorts the string list by length but can sort alphabetically if a tie happens

print(f"Your sorted string list would be: {sorted_string_list}")