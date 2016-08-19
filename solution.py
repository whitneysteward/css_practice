# def answer(x):
#     if x == 7:
#         return (8)
#     else:
#         return (x ** 7 + answer(x-1))

def answer(x):
    nums = list(range(2, x + 1))[::-1]
    print (nums)
    total = 8
    for num in nums:
        total += 7 ** num
    return total
print (answer(2))
