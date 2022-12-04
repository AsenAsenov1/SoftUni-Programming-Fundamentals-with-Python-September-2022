countries = input().split(", ")
capitals = input().split(", ")

cities_countries_dict = dict(zip(countries, capitals))

for country, capital in cities_countries_dict.items():
    print(f"{country} -> {capital}")
