input_words = input().split()

filtered_lst = [word for word in input_words if len(word) % 2 == 0]

print("\n".join(filtered_lst))
