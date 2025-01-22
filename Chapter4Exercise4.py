Age=int(input("Enter your age:"))

if Age < 2:
    print("The person is a baby.")
elif Age >= 2 and Age < 4:
    print("The person is a toddler.")
elif Age >= 4 and Age < 13:
    print("The person is a kid.")
elif Age >= 13 and Age < 20:
    print("The person is a teenager.")
elif Age >= 20 and Age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
