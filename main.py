numbers = []
numbers_quantity = int(input("how manny phone numbers do you want to add? "))

count = 1
while count <= numbers_quantity:
    numbers.append(int(input(f"enter number {count}: ")))
    count +=1  
    
country_code = int(input("enter the country code: "))
for number in numbers:
    print(f"sending messages to +{country_code}\t{number}")
    
price = 0.10
total_price = numbers_quantity * price
print(f"Total cost of sending messages: ${total_price}")

discount = 0.2
if numbers_quantity > 5:
    total_discount = numbers_quantity * price * discount
    print(f"Discount: ${total_discount}")
    print(f"Total cost after discount: ${total_price - total_discount}")
