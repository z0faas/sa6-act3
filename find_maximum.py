'''
Finding the maximum in a list of numbers using lambda inside another function
'''

def get_maximum(num_list, greater_num):
    i = 0
    result = num_list[i] # initializing the max as the first number in the list

    for num in range(len(num_list)-1): # using the length of the list, so there won't be an index error
        if greater_num(num_list[i], num_list[i+1]) > result: # updating the overall max if the next pair of numbers has a higher max
            result = greater_num(num_list[i], num_list[i+1])

        i += 1  
  
    return result

test_cases = {
    "Test Case 1": [1, 2, 8, 4, 5],
    "Test Case 2": [1, 2, 3, 4, 5],
    "Test Case 3": [100, 12, 22, 1, 3, 101, 2]
}

for case, num_list in test_cases.items():
    greater_num = lambda x, y: x if x > y else y # lambda function to compare 2 numbers and return the greater number
    print(f"{case}\n-----------")
    print(f"The maximum number in {num_list} is {get_maximum(num_list, greater_num)}\n")