company_info = {}

while True:
    command = input().split("->")
    if "End" in command:
        break
    company = command[0].strip()
    identity = command[1].strip()
    if company not in company_info.keys():
        company_info[company] = []
    if identity not in company_info[company]:
        company_info[company].append(identity)

for company_key, id_value in company_info.items():
    print(company_key)
    for current_id in id_value:
        print(f'-- {current_id}')
