def range_difference(num):   
    max_value = max(num)
    min_value = min(num)
    return max_value - min_value

numbers1 = [3, 7, 2, 9, 5]
numbers2 = [10, 10, 10]
numbers3 = [-5, 0, 15, 20]

print(f"{numbers1}=The differance between the maximum and minimum values is {range_difference(numbers1)}") 
print(f"{numbers2}=The differance between the maximum and minimum values is {range_difference(numbers2)}")  
print(f"{numbers3}=The differance between the maximum and minimum values is {range_difference(numbers3)}")  