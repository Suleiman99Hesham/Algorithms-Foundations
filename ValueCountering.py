# items = ["apple", "pear", "orange", "banana", "apple",
#          "orange", "apple", "pear", "banana", "orange",
#          "apple", "kiwi", "pear", "apple", "orange"]
# counter = dict()
# for item in items:
#     if ( item in counter.keys()):
#         counter[item]+=1
#     else:
#         counter[item]=1
#
# print(counter)
def combine_two_numbers(how_to,numbers):
    return how_to(numbers)

def add_two_numbers(numbers):
    a,b=numbers
    return a+b

def multiply_two_numbers(numbers):
    a,b=numbers
    return a*b

result=combine_two_numbers(multiply_two_numbers,(2,3))
print(result)