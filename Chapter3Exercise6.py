Names = ["Kyle", "Jan", "Will", "Lee", "Tan"]

for person in Names:
    print(f"Dear {person}, I would be honored to have you join me for dinner!")

print("\nUnfortunately, my new dinner table won't arrive in time, so I can only invite two people.")

while len(Names) > 2:
    removed_guest = Names.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

print("\nFinal list of invitees:")
for person in Names:
    print(f"Dear {person}, you are still invited to dinner!")