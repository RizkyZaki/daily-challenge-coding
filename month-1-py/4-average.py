# Zch Coding Challenge 2024
# 4/366
# https://www.codewars.com/kata/57a2013acf1fa5bfc4000921

def find_average(numbers):
     return sum(numbers) / len(numbers) if numbers else 0

print(find_average([1, 2, 3]))