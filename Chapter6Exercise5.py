sandwich_orders = ["Tuna", "Chicken", "Pastrami", "Pastrami", "Pastrami", "Ham"]

finished_sandwiches = []

print("Sorry, we have run out of pastrami sandwiches.")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")
