numbers = range(1, 1000001)
divisible_by_7 = [num for num in numbers if num % 7 == 0]
print(f"Количество чисел, делящихся на 7: {len(divisible_by_7)}")
