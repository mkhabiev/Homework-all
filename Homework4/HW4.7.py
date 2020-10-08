#array123
nums = []
for i in range(3):
    nums.append(int(input()))

for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
        print(True)
    else:
        print(False)
