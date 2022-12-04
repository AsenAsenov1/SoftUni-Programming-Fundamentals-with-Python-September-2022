some_text = " ".join(input())

some_text = some_text.split()

counter_dictionary = {x: some_text.count(x) for x in some_text}

for key, value in counter_dictionary.items():
    print(f"{key} -> {value}")
