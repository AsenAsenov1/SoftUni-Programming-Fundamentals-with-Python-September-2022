tail = input()
body = input()
head = input()

the_list = [tail, body, head]
the_list[0], the_list[2] = the_list[2], the_list[0]

print(the_list)
