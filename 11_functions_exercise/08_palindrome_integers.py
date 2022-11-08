def palindrome(number):
    filtered_list = []
    for num in number:
        if num == num[::-1]:
            filtered_list.append("True")
        else:
            filtered_list.append("False")
    return "\n".join(filtered_list)


input_list = input().split(", ")
print(palindrome(input_list))
