nums = list(map(str, input().split(", ")))

nums_without_zeros = [x for x in nums if int(x) != 0]
zeros = ["0"] * nums.count("0")
reordered_nums = list(map(int, (nums_without_zeros + zeros)))

print(reordered_nums)
