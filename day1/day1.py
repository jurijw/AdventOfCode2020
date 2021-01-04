nums = []
with open('input1.txt') as f:
    for line in f.readlines():
        nums.append(int(line))
    assert len(set(nums)) == len(nums), "Inputs are not unique"
    f.close()

for num in nums:
    pass
