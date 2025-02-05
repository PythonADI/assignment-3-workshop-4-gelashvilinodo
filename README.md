[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cHZXPzk6)
## Assignment Messaging (lists, loops, conditionals)


You are building a messaging program that will send messages to your customers. You have a list of customers and you want to send them messages.

1. Create an empty list of phone numbers.
2. Ask user how many phone numbers they want to add to the list.
3. Use a loop to get the phone numbers from the user and add them to the list.
4. Send a message to each phone number in the list. (print `Sending message to: ` followed by the phone number)

**Expected Output:**
```
How many phone numbers do you want to add to the list? 3
Enter phone number: 123-456-7890
Enter phone number: 234-567-8901
Enter phone number: 345-678-9012

Sending Messages!
Sending message to: 123-456-7890
Sending message to: 234-567-8901
Sending message to: 345-678-9012
```


**Our application is going global!** We need to send messages to customers in different countries. We need to update our program to include country codes.
- ask user for country code and add this country code for each phone number in the list.

**Expected Output:**
```
How many phone numbers do you want to add to the list? 3
Enter phone number: 123-456-7890
Enter phone number: 234-567-8901
Enter phone number: 345-678-9012
Enter country code: 1

Sending Messages!
Sending message to: +1 123-456-7890
Sending message to: +1 234-567-8901
Sending message to: +1 345-678-9012
```

We need to keep track of sent messages to calculate the total cost of sending messages. Each message costs $0.10. Update the program to calculate the total cost of sending messages.

**Expected Output:**
```
How many phone numbers do you want to add to the list? 3
Enter phone number: 123-456-7890
Enter phone number: 234-567-8901
Enter phone number: 345-678-9012
Enter country code: 1

Sending Messages!
Sending message to: +1 123-456-7890
Sending message to: +1 234-567-8901
Sending message to: +1 345-678-9012

Total cost of sending messages: $0.30
```


We need to add discount for our premium customers. If the customer is a premium customer, we will give them a 20% discount on the total cost of sending messages if they send more than 5 messages. Update the program to include premium customers.

**Expected Output:**
```
Premium Customer? (yes/no): yes
How many phone numbers do you want to add to the list? 3
Enter phone number: 123-456-7890
Enter phone number: 234-567-8901
Enter phone number: 345-678-9012
Enter country code: 1

Sending Messages!
Sending message to: +1 123-456-7890
Sending message to: +1 234-567-8901
Sending message to: +1 345-678-9012

Total cost of sending messages: $0.30
Discount: $0.06
Total cost after discount: $0.24
```
