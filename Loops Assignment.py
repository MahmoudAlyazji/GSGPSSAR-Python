# Q1
# n = int(input("Enter a number to print its multiplication table: "))
# for counter in range(1,11):
#     print(n,"x",counter,"=", n*counter)

####################################################################

# Q2
# counter = 0
# for i in range(1,31):
#     if i % 2 == 0:
#         print(i)
#         counter += 1
# print("\nTotal even numbers: ",counter)

#####################################################################

#Q3
# correctPASS = "python123"
# attempts = 0
# max_attempts = 3
# while attempts < max_attempts:
#         enteredPASS = input("Enter your password: ")
#         if enteredPASS == correctPASS:
#             print("Access granted")
#             break
#         else:
#               print("Wrong password!")
#               attempts += 1
# if enteredPASS != correctPASS and attempts == max_attempts:
#       print("Account locked!")
          
#####################################################################

#Q4
# marks = int(input("How many marks do you want to enter? "))
# counter = 1
# sum = 0
# for counter in range(1,marks + 1):
#     mark = int(input("Enter mark: "))
#     sum += mark
#     counter += 1
# print("Average: ",round(sum/marks,2))

#####################################################################

#Q5
# secret_number = 7
# while True:
#     gussed_number = float(input("Guess a number :) "))
#     if gussed_number > secret_number:
#         print("Too high")
#     elif gussed_number == secret_number:
#         print("Correct!")
#         break
#     else:
#         print("Too low") 

####################################################################

#Q6
# balance = 1000
# while True:
#     print("\n1. Check balance \n2. Deposit money \n3. Withdraw money \n4. Exit")   
#     chosen_option = int(input("Choose an option: "))
#     if chosen_option == 1:
#         print("Your balance is: ",balance)
#     elif chosen_option == 2:
#         added_amount = int(input("Enter the amount you need to add: "))
#         balance += added_amount
#         print("Your new balance is:", balance)
#     elif chosen_option == 3:
#         withdraw_amount = int(input("Enter the amount you need to withdraw: "))
#         if withdraw_amount > balance:
#             print("Insufficient balance")
#         else: 
#             balance -= withdraw_amount
#             print("Your new balance is:", balance)
#     elif chosen_option == 4:
#         print("Thank you!")
#         break
        
#####################################################################

# count = 0         
# total = 0          
# most_expensive = 0 
# cheapest = 0    
# price = float(input("Enter item price or 0 to finish: "))
# while price != 0:
#     count += 1
#     total += price

#     if price > most_expensive:
#         most_expensive = price

#     if cheapest == 0 or price < cheapest:
#         cheapest = price

#     price = float(input("Enter item price or 0 to finish: "))

# if count == 0:
#     print("No items were added.")
# else:
#     average = total / count
#     print("\nNumber of items:", count)
#     print("Total price:", total)
#     print("Average item price:", round(average,2)
#     print("Most expensive item:", most_expensive)
#     print("Cheapest item:", cheapest)   

###################################################################
   


# total_students = 0
# passed_students = 0
# failed_students = 0
# highest_average = 0
# top_student = ""
# num_students = int(input("How many students do you want to enter? "))

# for i in range(num_students):
#     name = input("Enter student name: ")
#     marks_count = int(input(f"How many marks {name} has? "))
#     total_marks = 0
#     for i in range(1, marks_count + 1):
#         mark = float(input(f"Enter mark {i}: "))
#         total_marks += mark
#     average = total_marks / marks_count
#     print(f"\n{name}'s average is: {average:.1f}")
#     if average >= 50:
#         print("Result: Passed\n")
#         passed_students += 1
#     else:
#         print("Result: Failed")
#         failed_students += 1
#     total_students += 1
#     if highest_average == 0 or average > highest_average:
#         highest_average = average
#         top_student = name

# print("\nSummary:")
# print(f"Total students: {total_students}")
# print(f"Passed students: {passed_students}")
# print(f"Failed students: {failed_students}")
# print(f"Highest average: {highest_average:.1f}")
# print(f"Top student: {top_student}")