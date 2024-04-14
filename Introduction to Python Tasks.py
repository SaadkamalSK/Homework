
### Hi Lucy jupyter kept craching so I dediced to use this instead. to check if the code is working simply select the code and press CTRL+/ to test it. Thanks in advance

# ### Task 1a - Variables
# # 1. Create a variable that stores a whole number.
# WholeNumber = int(input("Please enter a number : "))
# print(WholeNumber)
# # 2. Create a variable that stores a decimal number.
# DecimalNumber = float(input("Please enter a number : "))
# print(DecimalNumber)
# # 3. Create a variable that stores a word.
# WordInput = str(input("Please enter a Word : "))
# print(WordInput)
# # Based on input type
# Entry = input("Please insert an entry")
# EntryType = type(Entry)
# if EntryType = str
# print(str(Entry))
# elif 
# EntryType = int
# print(int(Entry))
# else
# print(float(Entry))
# # Based on input type
# Entry = input("Please insert an entry ")
# EntryType = type(Entry)
# if EntryType == str :
#     print(str(Entry))
# elif EntryType == int :
#     print(int(Entry))
# else:
#     print(float(Entry))

    ### Task 1b - Input/Output (I/O)
#1. Ask for the user’s first name and display the output message Hello [First Name].
# FirstName = input("What is your first Name? : ")
# print("Hello", FirstName)
    
#2. Ask for the user’s first name and then ask for their surname and display the output message Hello [First Name] [Surname].

# FirstName = input("What is your first Name? : ")
# SurName = input("What is your  SurName? : ")
# print("Hello", FirstName, SurName)

#3. Write code that will display the joke “What do you call a bear with no teeth?” and on the next line display the answer “A gummy bear!” Try to create it using only one line of code.
# print("""What do you call a bear with no teeth?
#  A gummy bear!""")

### Task 1c - Math Operators
#1. Ask the user to enter two numbers. Add them together and display the answer as The total is [answer].

# x=float(input("Please enter the first number : "))
# y=float(input("Please enter the second number : "))
# print("The total is : ",x+y)

#2. Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third. Display the answer as The answer is [answer].
# x=float(input("Please enter the first number : "))
# y=float(input("Please enter the second number : "))
# z=float(input("Please enter the third number : "))
# print("The answer is : ", (x+y)*z)

#3. Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices they have left and display the answer in a user- friendly format.
# StartedSlices = int(input("How many slices of pizza you started with? : "))
# EatenSlices = int(input("How many slices of pizza you ate? : "))
# print("The number of slices you have let with is : ", StartedSlices-EatenSlices)

#4. Ask the user for their name and their age. Add 1 to their age and display the output [Name] next birthday you will be [new age].
# UserName=str(input("What is your name? : "))
# UserAge=int(input("What is your age? : "))
# print(UserName,", you will be",UserAge+1,"years old in your next birthday")
    
#5. Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay.

# TotalBill = float(input("What is the total price of the bill? : "))
# DinersTotal = int(input("How many diners are there? : "))
# BillPerDinner = TotalBill/DinersTotal
# print(f"Bill's split per diner is : {BillPerDinner:.2f}")


#6. Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days.
# NumberOfDays = int(input("Please insert a number of days : "))
# print("The number of Hours in",NumberOfDays,"days are: ",NumberOfDays*24)
# print("The number of Minutes in",NumberOfDays,"days are: ",NumberOfDays*24*60)
# print("The number of Seconds in",NumberOfDays,"days are: ",NumberOfDays*24*60*60)

#7. There are 2,204 pounds in a kilogram. Ask the user to enter a weight in kilograms and convert it to pounds.
# KgsToPounds=float(input("Please enter the weight in Kgs "))
# print(f"{KgsToPounds:.2f} Kgs is equal to : {KgsToPounds*2204:.2f} Pounds")

#8. Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format.
# Over100=float(input("Please enter a number over 100 : "))
# while Over100<=100:
#         print("Number entered is not over 100, please try again")
#         Over100=float(input("Please enter a number over 100 : "))

# Under100=float(input("Please enter a number under 100 : "))

# while Under100<=0:
#          print("Number entered cannot be 0, please try again")
#          Under100=float(input("Please enter a number under 100 : "))
# while Under100>=100:
#          print("Number entered is over 100, please try again")
#          Under100=float(input("Please enter a number under 100 : "))

# Smallerby=float((-1+(Over100/Under100))*100)
# print(f"{Under100:.2f}, is smaller by {Smallerby:.3}% compared to {Over100:.2f}")


#9. Ask the user for two numbers, sum the two numbers and save in a variable. Finally, print out the result using the variable name.
# FirstNumber=float(input("Please enter the first number "))
# SecondNumber=float(input("Please enter the second number "))
# Sum=FirstNumber+SecondNumber
# print("The sum is :",Sum)


# Task 2 - Selection of, elif, else
#1. Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number, otherwise show the first number first and then the second.
# FirstNumber=int(input("Please Enter The First Number "))
# SecondNumber=int(input("Please Enter The Second Number "))
# if FirstNumber>SecondNumber:
#     print(SecondNumber
#           ,FirstNumber)
    
# else:
#     print(FirstNumber, SecondNumber)

#2. Ask the user to enter a number that is under 20. If they enter a number that is 20 or more, display the message “Too high”, otherwise display “Thank you”.
# Under20=float(input("Please enter a number that is under 20 "))
# while Under20>=20:
#     print("Too High")
#     Under20=float(input("Please enter a number that is under 20 "))

# print("Thank you.")

#3. Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range, display the message “Thank you”, otherwise display the message “Incorrect answer”.

# NumberBetween10and20=int(input("Please Enter A Number "))
# if NumberBetween10and20>=10 and NumberBetween10and20<=20:
#     print("Thank you")
# else:
#     print("Incorrect answer")


#4. Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”, otherwise display the message “I don’t like [colour], I prefer red”.

# Color=input("What is your favourite colour ? ")
# if (Color=="red" or Color=="RED" or Color=="Red"):
#     print("I Like red too")
# else:
#     print("I do not like", Color,", I perefer red")


#5. Ask the user to enter a number. If it is under 10, display the message “Too low”, if their number is between 10 and 20, display “Correct”, otherwise display “Too high”.

# Entry=float(input("Please enter a number "))
# if Entry<10:
#         print("Too Low")
# elif Entry<=20:
#     print("Correct")
# else:
#       print("Too high")

#6. Ask the user to enter 1, 2 or 3. If they enter a 1, display the message “Thank you”, if they enter a 2, display “Well done”, if they enter a 3, display “Correct”. If they enter anything else, display “Error message”.

# Entry=int(input("Please enter a number "))
# match Entry:
#     case 1:
#         print("Thank you")
#     case 2:
#         print("Well Done")
#     case 3:
#         print("Correct")
#     case _:
#         print("Error message")


# Task 3 - Data Structures
#1. Create a list of the first 10 positive integers and print the list to the console.
# First10PositiveIntegers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(First10PositiveIntegers)


#2. Create a list of 5 names, then print each name on a separate line.

# NamesList=["Edward", "Alex", "Imran", "Antony", "Natalie"]
# for Name in NamesList:
#     print(Name)


#3. Create a list of 5 names, reverse the list and print each name on a separate line.

# NamesList=["Edward", "Alex", "Imran", "Antony", "Natalie"]
# NamesList.reverse()
# for Name in NamesList:
#     print(Name)

#4. Create a dictionary with all the days of the week, each weekday should have an incremental day number. The week should start from day 1, which is a Monday.

# AllDaysOfTheWeek= {"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}

#5. Remove the day "Saturday" and its key from the dictionary in question 4.

# AllDaysOfTheWeek= {"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
# del AllDaysOfTheWeek["Saturday"]

#6. Print out only Tuesday and Thursday elements from the dictionary  question 4.

# AllDaysOfTheWeek= {"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
# print(AllDaysOfTheWeek["Tuesday"], AllDaysOfTheWeek["Thursday"])

# Task 4 - Loops
# 1. Set the total to 0 to start with. While the total is 50 or less, ask the user to input a number. Add that number to the total and print the message “The total is… [total]”. Stop the loop when the total is over 50.

# Total = 0
# while Total<=50:
#     x=int(input("Please enter a number "))
#     if x>50:
#         x=int(input("""Number entered more than 50
# Please enter a number less than 50 """))
#         Total=x+Total
#     else:
#         Total=x+Total
#     if Total==50:
#         break
# print("The total is :",Total)

# 2. Ask the user to enter a number. Keep asking until they enter a value over 5 and then display the message “The last number you entered was a [number]” and stop the program.

# X=float(input("Please enter a number "))
# while X<5:
#     X=float(input("Please enter a number "))
#     Y=X
# print("The last number you entered was a ",Y)

#3. Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they want to add another number. If they enter “y", ask them to enter another number and keep adding numbers until they do not answer “y”.  Once the loop has stopped, display the total.

# X=float(input("Enter the first number "))
# Y=float(input("Enter the second number "))
# Sum=X+Y
# Additional = str(input("""Would you like to add another number? 
# Please enter Y or N? """))
# while Additional == "Y" or Additional == "y":
#     AdditionalNumber=float(input("Enter the additional number "))
#     z=AdditionalNumber+X+Y
#     Additional = str(input("""Would you like to add another number? 
# Please enter Y or N? """))
#     Total=z+AdditionalNumber
# print(Total)

#4. Create a list with at least 8 elements. Use a for loop to print out each element in the list.
# list = [1,2,3,4,5,6,7,8,9,10,11,12]
# for x in list[:8]:
#     print(x)

#5. Complete question 4 using a while loop instead of a for loop.
# list = [1,2,3,4,5,6,7,8,9,10,11,12]
# NumberOfReturnedItems=0
# while NumberOfReturnedItems<8:
#     print(list[NumberOfReturnedItems])
#     NumberOfReturnedItems=1+NumberOfReturnedItems

#6. Print out all of the content within the multi-dimensional list using nested for loops

# january = [['Week1', 'Monday1', 'Tuesday2', 'Wednesday3', 'Thursday4', 'Friday5', 'Saturday6', 'Sunday7'],
# ['Week2', 'Monday8', 'Tuesday9', 'Wednesday10', 'Thursday11', 'Friday12', 'Saturday13', 'Sunday14'],
# ['Week3', 'Monday15', 'Tuesday16', 'Wednesday17', 'Thursday18', 'Friday19', 'Saturday20', 'Sunday21'],
# ['Week4', 'Monday22', 'Tuesday23', 'Wednesday24', 'Thursday25', 'Friday26', 'Saturday27', 'Sunday28'],
# ['Week5', 'Monday29', 'Tuesday30', 'Wednesday31']]
# for x in january:
#     for y in x:
#         print(y)

# Task 5 - Subroutines (Homework)
#1. Define a procedure that will ask the user to enter a number and save it as the variable “num”. Print this number to the screen inside the procedure.

# def variable():
#     x=input("Please enter a number ")
#     return int(x)

# num=variable()
# print(num)

#2. Define a function that will add two number together and return the result. Ask the user for 2 numbers, you must utilise a loop inside a main() function to do this. Pass the two numbers to the function. Print th result to the screen at the end of the main() function.


# def addingtwonumbersloop():
#     while True:
#        x=input("Please enter the first number ")
#        try:
#         x = float(x)
#         break
#        except ValueError:
#         x=print("""Entry is not a valid number!
# Please enter first number """)
    
    
#     while True:
#          y=input("Please enter the second number ")
#          try:
#             y = float(y)
#             break
#          except ValueError:
#             y=print("""Entry is not a valid number!
# Please enter second number """)
   
#     return float(x)+float(y)

        
# print(addingtwonumbersloop())
            

#3. Display the following menu to the user: ``` 1. Addition 2. Subtraction Enter 1 or 2: ``` If they enter a 1, it should run a function that will generate two random numbers between 5 and 20, and ask the user to add them together. Work out the correct answer and return both the user’s answer and the correct answer. If they entered 2 as their selection on the menu, it should run a function that will generate one number between 25 and 50 and another number between 1 and 25 and ask them to work out num1 minus num2. This way they will not have to worry about negative answers. Return both the user’s answer and the correct answer. If they do not select a relevant option on the first menu you should display a suitable message to alert the user and show the menu again.

# import random
# FisrtRandomNumber=random.randint(5,20)
# SecondRandomNumber=random.randint(5,20)
# ThirdRandomNumber=random.randint(25,50)
# FourthRandomNumber=random.randint(1,25)
# Addition=FisrtRandomNumber+SecondRandomNumber
# Subtraction=ThirdRandomNumber-FourthRandomNumber
# TypeOfOperation=input("Please choose either 1 for addition or 2 for subtraction ")
# while True:
#     try:
#         TypeOfOperation=int(TypeOfOperation)
#         break
#     except:
#         TypeOfOperation=input("Invalid entry! Please either enter 1 for addition or 2 for subtraction ")
# if int(TypeOfOperation)==1:
#     UserAnswer=input(f"what is {FisrtRandomNumber} + {SecondRandomNumber} ? ")
#     if int(Addition)==int(UserAnswer):
#         print(f"Your Answer is correct. It is indeed : {Addition}")
#     else:
#         print(f"Unfortunately your answer is incorrect. The correct answer is: {Addition} whereas your answer was {UserAnswer}")
# else:
#     UserAnswer=int(input(f"what is {ThirdRandomNumber} - {FourthRandomNumber} ? "))
#     if int(Subtraction)==int(UserAnswer):
#          print(f"Your Answer is correct. It is indeed : {Subtraction}")
#     else:
#         print(f"Unfortunately your answer is incorrect. The correct answer is: {Subtraction} whereas your answer was {UserAnswer}")

#3.a) Create another function that will check if the user’s answer matches the actual answer. If it does, display “Correct”, otherwise display a message that will say “Incorrect, the answer is” and display the real answer.

#see above

#4. OPTIONAL TASK: Create the following menu: ``` 1) Add to file 2) View all records 3) Quit program Enter the number of your selection: ``` If the user selects 1, allow them to add to a file called Salaries.csv which will store their name and salary. You will need to create this in Excel, store as a table with correct data types. If they select 2 it should display all records in the Salaries.csv file. If they select 3 it should stop the program. If they select an incorrect option they should see an error message. They should keep returning to the menu until they select option 3.


# selection_options={1: "Add to file", 2: "View all records", 3: "Quit program"}
# print("Available oprion are: ")
# for x, y in selection_options.items():
#     print(x, ":", y)

# selected_number=input("Please enter the number of your selection: ")

# while True:
#     try:
#         selected_number==int(selected_number)
#         break
#     except:
#         selected_number=input("Entry Invalid! Please either choose option 1, 2 or 3 : ")
# if int(selected_number)==1:
#     import csv
#     with open("salaries.csv", mode="a") as salaries:
#         csvheaders=["employee_name", "employee_salary"]
#         writer=csv.DictWriter(salaries, fieldnames=csvheaders)
#         employeename=input("What is the employee's name? ")
#         while True:
#             try:
#                 employeename==str(employeename)
#                 break
#             except:
#                 employeename=input("Please enter a valid name ")
#         employeesalary=input(f"What is {employeename}'s salary? ")
#         while True:
#             try:
#                 employeesalary=float(employeesalary)
#                 break
#             except:
#                 employeesalary=input("Please enter a valid salary ")
#         writer.writerow({"employee_name": employeename, "employee_salary": employeesalary})
# elif int(selected_number)==2:
#     import csv
#     with open("salaries.csv") as salaries_display:
#         csvreader=csv.reader(salaries_display, delimiter=",")
#         next(csvreader)
#         output=[]
#         for details in csvreader:
#             output.append(details)
#     print(output)

# else:
#     exit

# Task 6 - Random (Homework) - Self Learning

#1. Display a random integer between 1 and 100 inclusive.

# import random
# print(random.randint(1,100))

#2. Display a random fruit from a list of five fruits.
# fruits=("Apple", "Banana", "Cherry", "Mango", "Grape")
# import random
# print(random.choice(fruits))

#3. Randomly choose either heads or tails (“h” or “t”). Ask the user to make their choice. If their choice is the same as the randomly selected value, display the message “You win”, otherwise display Bad luck”. At the end, tell the user if the computer selected heads or tails.
# choice_list=("heads","trails")
# user_choice_list=("heads","trails","Heads","Trails","HEADS","TRAILS")
# user_choice=input("What is your choice : Heads or Trails? ")
# while (user_choice in user_choice_list)==False:
#     user_choice=input("Plase select either Heads or Trails ")
# import random
# random_choice=random.choice(choice_list)
# if user_choice==random_choice:
#     print("You won!")
# else:
#     print(f"Bad luck. The correct answer is {random_choice}")


#4. Randomly choose a number between 1 and 5. Ask the user to pick a number. If they guess correctly, display the message “Well done”, otherwise tell them if they are too high or too low and ask them to pick a second number. If they guess correctly on their second guess, display “Correct”, otherwise display “You lose”.
# def checking(x):
#     while True:
#         try:
#             x=float(x)
#             if x<=5 and x>=1:
#                 break
#             else:
#                 x=input("Invalid entry! Please enter a number between 1 and 5: ")
#         except:
#             x=input("Invalid entry! Please enter a valid number between 1 and 5: ")
#     return x
# user_first_entry=input("Enter a number between 1 and 5: ")
# checking(user_first_entry)
# import random
# random_number=random.randint(1,5)
# if user_first_entry==random_number:
#     print("Well done")
# else:
#     if random_number>float(user_first_entry):
#         second_user_entry=input(f"Second chance! {user_first_entry} is lower than the random number. Pick another number between 1 and 5: ")
#         checking(second_user_entry)
#     elif random_number<user_first_entry:
#         second_user_entry=input(f"Second chance! {user_first_entry} is higher than the random number. Pick another number between 1 and 5: ")
#         checking(second_user_entry)
#     else:
#         next
# if second_user_entry==random_number:
#     print("Correct")
# else:
#     print(f"You lost! correct number was {random_number}")

    

    

#5. Randomly pick a whole number between 1 and 10. Ask the user to enter a number and keep entering numbers until they enter the number that was randomly picked.

# import random
# random_number=random.randrange(1,10,1)
# user_number=input("Pick a whole number between 1 and 10 ")
# while True:
#     try:
#         user_number=int(user_number)
#         if user_number!=random_number:
#             user_number=input("Try again ")
#         else:
#             print(f"Correct! randon number was: {random_number}")
#             break
#     except:
#         user_number=input("Inavlid entry! enter a whole number between 1 and 10 ")




#5.a Update the program so that it tells the user if they are too high or too low before they pick again.

# import random
# random_number=random.randrange(1,10,1)
# user_number=input("Pick a whole number between 1 and 10 ")
# while True:
#     try:
#         user_number=int(user_number)
#         if user_number!=random_number and user_number>random_number:
#             user_number=input(f"Try again {user_number} is higher than the random number ")
#         elif user_number!=random_number and user_number<random_number:
#             user_number=input(f"Try again {user_number} is lower than the random number ")
#         else:
#             print(f"Correct! randon number was: {random_number}")
#             break
#     except:
#         user_number=input("Inavlid entry! enter a whole number between 1 and 10 ")

#6. Make a maths quiz that asks five questions by randomly generating two whole numbers to make the question (e.g. [num1] + [num2]). Ask the user to enter the answer. If they get it right add a point to their score. At the end of the quiz, tell them how many they got correct out of five.

# import random

# number_of_tries = 0
# score = 0

# while True:
#     first_random_number = random.randrange(1, 100000)
#     second_random_number = random.randrange(1, 100000)
#     correct_sum = first_random_number + second_random_number

#     user_entry = input(f"What is {first_random_number} + {second_random_number}? ")

#     try:
#         user_entry = int(user_entry)
#         if user_entry == correct_sum:
#             if number_of_tries >= 5:
#                 break
#             else:
#                 print("You are correct! +1 point")
#                 first_random_number = random.randrange(1, 100000)
#                 second_random_number = random.randrange(1, 100000)
#                 correct_sum = first_random_number + second_random_number
#                 score += 1
#                 number_of_tries += 1
#         else:
#             print("Incorrect! Try again.")
#             number_of_tries += 1
#     except ValueError:
#         print("Invalid entry! Please enter an integer.")

# print(f"Your score is: {score} out of {number_of_tries}")


#7. Display five colours and ask the user to pick one. If they pick the same as the program has chosen, say “Well done”, otherwise display a witty answer which involves the correct colour, e.g. “I bet you are GREEN with envy” or “You are probably feeling BLUE right now”. Ask them to guess again; if they have still not got it right, keep giving them the same clue and ask the user to enter a colour until they guess it correctly.
        

# colors_dic={"blue": "You are probably feeling BLUE right now", "green": "I bet you are GREEN with envy"}
# import random
# random_key=random.choice(list(colors_dic.keys()))
# random_value=colors_dic[random_key]
# def list_choices():
#     for x in colors_dic.keys():
#         print(x)
# list_choices()
# user_color=input("Guess form the above list what color I am thinking of: ")
# while True:
#     try:
#         user_color=str(user_color)
#         if user_color in colors_dic:
#             if user_color==random_key:
#                 print("Well done!")
#                 break
#             else:
#                 user_color=input(f"Oops try again! Here is a hint: {random_value}. What is the color? ")
#         else:
#             list_choices()
#             user_color=input("Please enter a valid color from the above list: ")
#     except:
#         user_color=input("Invalid entry! Please try again ")

    









   
   




 


