print("Enter pizza toppings one by one. Type 'Finish' to complete your order.")
while True:
    topping = input("Enter a topping: ")
    
    if topping == "Finish":
        print("Thank you! Your pizza order is being prepared.")
        break
    else:
        print(f"I'll add {topping} to your pizza!")