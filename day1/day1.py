nums = []
with open('input1.txt') as f:
    for line in f.readlines():
        nums.append(int(line))
    assert len(set(nums)) == len(nums), "Inputs are not unique"
    f.close()


def sol1():
    for num1 in nums:
        for num2 in nums:
            if num1 + num2 == 2020:
                return num1 * num2


print(sol1())
