'''
Finding the sum of all the digits in an inputted number while also using lambda
'''

num = int(input("Enter a number. I'll tell you the sum of its digits. "))

digits_sum = sum(map(lambda x: int(x), str(num)))  # using lambda inside map to convert each digit to int, then adding them

print(f"The sum of the digits in your number is {digits_sum}")