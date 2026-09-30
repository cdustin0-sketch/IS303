#create list
expenses = []

#ask for their expenses
while True:
    expense = float(input("Enter an expense or 0 to finish: "))

    if expense == 0:
        break
    elif expense < 0:
        print("Expenses cannot be negative.")
    else:
        expenses.append(expense)

print(expenses)

#add and average their total expenses
if len(expenses) > 0:
    total = sum(expenses)
    average = total / len(expenses)

    print(f"Total: ${total:,.2f}")
    print(f"Average: ${average:,.2f}") 
else:
    print("No expenses were entered.")
#give the answers to their responses

#classify size of expenses
smallest = min(expenses)
largest = max(expenses)

print(f"Smallest expense: ${smallest:,.2f}")
print(f"Largest expense: ${largest:,.2f}")

#describe amount of each purchase
#Less than $25: Small expense
#$25 through $100: Moderate expense
#Greater than $100: Large expense

small_count = 0
moderate_count = 0
large_count = 0

for expense in expenses:
    if expense < 25:
        small_count += 1
    elif expense <= 100:
        moderate_count += 1
    else:
        large_count += 1

print("Small expenses:", small_count)
print("Moderate expenses:", moderate_count)
print("Large expenses:", large_count)