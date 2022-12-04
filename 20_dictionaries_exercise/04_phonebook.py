phone_numbers_dict = {}
number_of_contacts = 0

while True:
    person_info = input()
    if person_info.isdigit():
        number_of_contacts = int(person_info)
        break
    person_info = person_info.split("-")
    person = person_info[0]
    phone_number = person_info[1]
    phone_numbers_dict[person] = phone_number

for i in range(number_of_contacts):
    name = input()
    if name in phone_numbers_dict.keys():

        print(f"{name} -> {phone_numbers_dict[name]}")
    else:
        print(f"Contact {name} does not exist.")
