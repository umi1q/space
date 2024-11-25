import math
from collections import Counter
def count_variations(word):
    letter_counts = Counter(word)
    n = len(word)
    numerator = math.factorial(n)
    denominator = 1
    for count in letter_counts.values():
        denominator *= math.factorial(count)
    return numerator // denominator
word = "голова"
variations_count = count_variations(word)
print(f"Количество вариаций слова '{word}': {variations_count}")
