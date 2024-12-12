def count_programs(n):
    if n == 1:
        return 1
    if n == 26:
        return 0
    if n < 1:
        return 0
    total_ways = count_programs(n - 1)  
    if (n - 1) % 2 == 0:
        total_ways += count_programs((n - 1) // 2)
    return total_ways
result = count_programs(27)
print(result)
