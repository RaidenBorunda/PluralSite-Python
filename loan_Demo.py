
# Get the loan details
money_owed = float(input("How much money do you owe, in dollars?\n")) # $50,000
new_money_owed = money_owed
apr = float(input("What is the annual percentage rate?\n")) # 3%
payment = float(input("What will your monthly payment be, in dollars?\n")) # $1,000
months = int(input("How many months do you want to see results for?\n")) # 24

# Divide apr by 100 to make it a percent, then divide by 12 to make monthly
monthly_rate = apr/100/12


for i in range(months):
    # Add in interest
    interest_paid = round(money_owed) * monthly_rate
    money_owed = round(money_owed) + round(interest_paid)
        

    if (money_owed - payment <0):
        print("The last payment is $"+ str(money_owed))
        print("You paid off the loan in", i+1, "months")
        total_interest = new_money_owed * monthly_rate * i
        print('You paid a total of $' + str(round(total_interest)), 'in interest!')
        break

    # Make Payment
    money_owed = money_owed - payment
    total_interest = new_money_owed * monthly_rate * i
    # Print the results after this month
    print("Paid $" + str(payment), "of which $" + str(round(interest_paid)), "was interest.", end=' ')
    print("Now I owe $" + str(money_owed))
    print("You have paid $" + str(round(total_interest)), "in interest so far!")
    