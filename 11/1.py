text = open('input.txt')
lines = text.readlines()
target = int(lines[0])
nums = list(map(int, lines[1].split()))
new = [target - i for i in nums]
flag = False
for i in range(len(nums)):
    if nums[i] in new:
        flag = True
text.close()
result = open('output.txt', 'w')
result.write(str(1*flag))
result.close()
text.close()