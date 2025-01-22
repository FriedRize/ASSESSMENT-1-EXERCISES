pet_1 = {
    "Animal": "Dog",
    "Owner": "Kyle"
}

pet_2 = {
    "Animal": "Cat",
    "Owner": "Ash"
}

pet_3 = {
    "Animal": "Parrot",
    "Owner": "Lee"
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Pet: {pet['Animal'].title()}")
    print(f"Owner: {pet['Owner']}\n")
