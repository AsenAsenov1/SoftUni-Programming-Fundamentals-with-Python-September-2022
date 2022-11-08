def loading_bar(number):
    result = number // 10
    dots = 10 - result
    if number == 100:
        return ("100% Complete!" '\n'
                f"[{result * '%'}{dots * '.'}]")
    else:
        return (f"{number}% [{result * '%'}{dots * '.'}]" '\n'
                "Still loading...")


percent_num = int(input())
print(loading_bar(percent_num))
