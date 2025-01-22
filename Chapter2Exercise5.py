budget = 50
usb_price = 6

usb_count = budget // usb_price 
money_left = budget % usb_price 

print(f"She can buy {usb_count} USB sticks.")
print(f"She will have £{money_left} left.")