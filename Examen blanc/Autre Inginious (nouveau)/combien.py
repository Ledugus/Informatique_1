def is_valid_serie(i, n):
    sum = 0
    while sum < n:
        sum += i
        i += 1
        if sum == n:
            return True
    return False


def combien(n):
    count = 1
    for i in range(1, n):
        if is_valid_serie(i, n):
            count += 1
    return count


print(combien(100))
print(combien(6))
print(combien(1))
