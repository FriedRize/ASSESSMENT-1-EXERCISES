print("Welcome to the movie theater! Type 'Finish' to exit.")

total_cost = 0

while True:
    age = input("Please enter your age: ")
    
    if age == 'Finish':
        print(f"Thank you! Your total cost is ${total_cost}. Have a great day!")
        break
    
    try:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif 3 <= age <= 12:
            print("Your ticket costs $10.")
            total_cost += 10
        else:
            print("Your ticket costs $15.")
            total_cost += 15
    except:
        print("Please enter a valid age or type 'Finish' to exit.")