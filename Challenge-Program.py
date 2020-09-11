# Calvin Comstock-Fisher, Kynan McCabe-Wild
# 9/11/2020
# Challenge Program Chapter 1
# 1. Get the user's input for the college they want to attend
# 2. Ask for the tuition of said college
# 3. Ask for the room/board cost of said college
# 4. Ask for the financial aid of the said college
# 5. Find the total cost to attend and print it to the user
# 6. Repeat steps 1-5 for a second college
# 7. Compare the two colleges in cost
# 8. Print out which college is cheaper

# This code will give us the variables to determine how to format
import os
rows, cols = os.popen('stty size', 'r').read().split()
formatCenter = "{:^"+cols+"}"

# The code below asks the user for the input of their college's name, cost, room/board cost, and financial aid
college1_name = str(input("What is the name of the college you want to attend? "))
college1_tuition_cost = int(input("How much is the tuition at " + college1_name + "? "))
college1_rab_cost = int(input("How much is the Room and board at " + college1_name + "? "))
college1_fa = int(input("How much financial aid and scholarships will you get at " + college1_name + "? "))

# The code below will find the total cost to attend said college
college1_total_cost = (college1_tuition_cost + college1_rab_cost) - college1_fa

# The code below is going to put all the variables together and print them out in a centered format
print(formatCenter.format("The total cost to attend " + college1_name + " is " + "${:,.2f}".format(college1_total_cost) + ".\n"))


# The code below is a copy of the code above and will find all the same variables for a second college
college2_name = str(input("What is the name of the other college you want to attend? "))
college2_tuition_cost = int(input("How much is the tuition at " + college2_name + "? "))
college2_rab_cost = int(input("How much is the Room and board at " + college2_name + "? "))
college2_fa = int(input("How much financial aid and scholarships will you get at " + college2_name + "? "))

# The code below will find the total cost of the second college the user plans to attend
college2_total_cost = (college2_tuition_cost + college2_rab_cost) - college2_fa

# The code below will print out the variables and total cost of the second college the user plans to attend
print(formatCenter.format("The total cost to attend " + college2_name + " is " + "${:,.2f}".format(college2_total_cost) + ".\n"))


if college1_total_cost > college2_total_cost:
  print(college2_name + " is a better value than " + college1_name + ".")
elif college1_total_cost == college2_total_cost:
  print("Both are good choices!")
else:
  print(college1_name + " is a better value than " + college2_name + ".")

input("\n\nPress the enter key to exit.")