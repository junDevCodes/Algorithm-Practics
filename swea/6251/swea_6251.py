num_rows = 5
for i in range(1, num_rows + 1):
    num_spaces = num_rows - i
    num_stars = i
    print(f"{' ' * num_spaces}{'*' * num_stars}")