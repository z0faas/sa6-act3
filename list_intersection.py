'''
Finding the intersection between two lists using a lambda function and filter()
'''

test_cases = {
    "Test Case 1": ([1, 2, 3, 4, 5], [6, 7, 8, 1, 9]),
    "Test Case 2": ([2, 4, 6, 8, 10, 12, 14], [100, 12, 2, 14, 4, 71]),
    "Test Case 3": ([1, 2, 3], [4, 5, 6])
}

for case, (list1, list2) in test_cases.items(): # key -> case, value -> (list1, list2)
    intersection = list(filter(lambda x: x if x in list1 and list2 else None, list1 and list2)) # returns the numbers that are in list1 AND list2, if there is any
    print(f"{case}\n-----------")
    print(f"The intersection between {list1} and {list2} is {intersection}\n")