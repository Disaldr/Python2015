# func = lambda x, y: x + y
# print(func(1,2))
# print(func('a', 'b'))
# print((lambda x, y: x * y)(2,5))

def adder(*nums):
    sum = 0

    for n in nums:
        sum += n
    print(type(nums))
    print("Sum:", sum)

adder(2, 3, 4, 6, 7 ,8)
adder(3,4,5,6,7)
