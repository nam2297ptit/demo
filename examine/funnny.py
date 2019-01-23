import array as arr 
numbers = arr.array('i', [3, 5, 7]) 
numbers.append(4) 
print(numbers) 
# Output: array('i', [3, 5, 7, 4]) 
# extend() nối vào cuối mảng 
numbers.extend([5, 6, 7]) 
print(numbers) 
# Output: array('i', [3, 5, 7, 4, 5, 6, 7])
