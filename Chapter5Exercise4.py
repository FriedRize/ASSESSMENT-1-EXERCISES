rivers = {
    "Pasig": "Philippines",
    "Shinano": "Japan",
    "Dubai creek": "UAE"
}

for river, country in rivers.items():
    print(f"\nThe {river.title()} runs through {country.title()}.")

print("\n")

print("Rivers included in the dictionary:")
for river in rivers.keys():
    print(river.title())

print("\n")

print("Countries included in the dictionary:")
for country in rivers.values():
    print(country.title())
