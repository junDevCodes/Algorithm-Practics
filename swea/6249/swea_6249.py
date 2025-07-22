from collections import Counter

def count_digits_flexible(number):
    digit_counts = Counter(str(number))
    counts_list = [digit_counts.get(str(i), 0) for i in range(10)]
    return counts_list

input_num = int(input())
result_counts = count_digits_flexible(input_num)
print("0 1 2 3 4 5 6 7 8 9")
print(" ".join(map(str, result_counts)))
