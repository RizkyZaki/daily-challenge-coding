# Zch Coding Challenge 2024
# 3/366
# https://www.codewars.com/kata/576bb71bbbcf0951d5000044

def count_positives_sum_negatives(arr):
  if not arr:
    return []
  
  positive_count = sum_negativ = 0
  
  for num in arr:
    if num > 0:
      positive_count += 1
    elif num < 0:
      sum_negativ += num


  return [positive_count, sum_negativ]


print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))