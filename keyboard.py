print("Enter 1 for average 5 squared numbers ")
print("Enter 2 for average of 5 cube numbers")
print("Enter your choice: ")
choice = int(input(""))
if choice == 1:
    total_sum = 0
    for n in range(5):
        numbers = float(input('Enter number : '))
        total_sum = total_sum + (numbers * numbers)
    avg = total_sum / 5
    print('Average of 5 numbers is: ', avg)
elif choice == 2:
    total_sum = 0
    for n in range(5):
        numbers = float(input('Enter number : '))
        total_sum = total_sum + (numbers * numbers * numbers)
    avg = total_sum / 10
    print('Average of 5 numbers is:', avg)
else:
    print("Invalid Choice")
