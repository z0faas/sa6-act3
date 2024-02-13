'''
Raising each number in a list to the power of n using a lambda function and map()
'''

test_cases = {
    "Test Case 1": ([1, 2, 3, 4, 5], 3),
    "Test Case 2": ([2, 4, 6, 8, 10], 2),
    "Test Case 3": ([1000, 213, 422, 111, 589], 0),
}

for case, (numbers, n) in test_cases.items():
    result = list(map(lambda x: x ** n, numbers))
    print(f"{case}\n-----------")
    print(f"Raising all the numbers in {numbers} to the power of {n} = {result}\n")