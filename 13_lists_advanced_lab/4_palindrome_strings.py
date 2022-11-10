words_list = input().split()
palindrome = input()

palindrome_list = [word for word in words_list if word == word[::-1]]
times = palindrome_list.count(palindrome)
print(palindrome_list)
print(f"Found palindrome {times} times")
