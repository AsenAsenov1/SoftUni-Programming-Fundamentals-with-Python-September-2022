def sum_ascii(the_string: str, start_num: int, stop_num: int):
    total_sum = 0
    for char in the_string:
        if ord(char) in range(start_num + 1, stop_num - 1):
            total_sum += ord(char)
    print(total_sum)


start = ord(input())
stop = ord(input())
random_string = input()
sum_ascii(random_string, start, stop)
