'''
Using a lambda function and sorted() to sort a list by length of strings, but also alphabetically if there's a tie between string lengths
'''

test_cases = {
    "Test Case 1": ['Jonathan', 'Apple', 'Computer', 'Discrete Math', 'Dog'],
    "Test Case 2": ['Dog', 'Cat', 'And', 'Are', 'Bat', 'Fog', 'Zed'],
    "Test Case 3": ['CS3: Intro to Software', 'Ethics', 'Jazz Band', 'Discrete Math']
}

for case, string_list in test_cases.items():
    sorted_string_list = sorted(string_list, key=lambda x: (len(x), x)) # sorts the string list by length but can sort alphabetically if a tie happens
    print(f"{case}\n-----------")
    print(f"Sorting {string_list} would be: {sorted_string_list}\n")