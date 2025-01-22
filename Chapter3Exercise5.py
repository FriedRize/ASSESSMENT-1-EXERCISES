Names = ["Mc", "Jan", "Will", "Aaron", "Tan"]

print("\nSending out the invitations:")
for person in Names:
    print(f"Dear {person}, I would be honored to have you join me for dinner!")

print("\nUnfortunately, Mc and Aaron can't make it to dinner.")

Names[0] = "Lee" 
Names[3] = "Kyle"

print("\nSending out the new invitations:")
for person in Names:
    print(f"Dear {person}, I would be honored to have you join me for dinner!")
