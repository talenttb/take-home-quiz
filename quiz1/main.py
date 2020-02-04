import re


def count_digit_v1(n):
    if n <= 0:
        return 0

    res = 0
    for i in range(n):
        res += len(re.findall("7", str(i)))
    return res


# print(count_digit_v1(120))
# print(count_digit_v1(10))
# print(count_digit_v1(50))
# print(count_digit_v1(70))
# print(count_digit_v1(80))
print(count_digit_v1(1000))
