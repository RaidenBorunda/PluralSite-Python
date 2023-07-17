total = 0
expenses = []#<-LIST
num_expenses = int(input("Enter # of expenses:"))
#Part 2
for i in range(num_expenses):
# for i in range(7):
    expenses.append(float(input("Enter an expense:")))
total = sum(expenses)

#Part 1
#expenses = [10.50, 8, 5, 15, 20, 5, 3]
#total = sum(expenses)

#sum = 0

#for x in expenses:
#    sum = sum + x

print("You spent $", total, " on lunch this week.", sep='')
#sep='' is used to remove the whitespace
