def sorting():
    integer_list = list(map(int, simple_list))
    return sorted(integer_list)


simple_list = input().split()
print(sorting())
