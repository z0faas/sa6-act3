'''
Finding the sum of all the digits in an inputted number while also using lambda
'''

test_cases = {
    "Test Case 1": 123,
    "Test Case 2": 200,
    "Test Case 3": 1110
}

for case, num in test_cases.items():
    digits_sum = sum(map(lambda x: int(x), str(num)))  # using lambda inside map to convert each digit to int, then adding them
    print(f"{case}\n-----------")
    print(f"The sum of the digits in {num} is {digits_sum}\n")