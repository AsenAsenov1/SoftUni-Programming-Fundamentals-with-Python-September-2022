word = list(input())
indices = []
for i in range(len(word)):
    if word[i].isupper():
        indices.append(i)
print(indices)
