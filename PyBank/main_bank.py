import os
import csv

# Path to collect data
bank_csv_path = os.path.join('..','PyBank','Resources_bank','budget_data.csv')

# Define variables
months = []
profit_losses = []
profit_change = []
count_months = 0

# open and read CSV
with open(bank_csv_path, 'r') as file:

    reader = csv.reader(file, delimiter=",")

    csv_header = next(file)

    # for row in reader:
        #print(row) *to view data in CSV
             
    # Read through each row of data after the header
    for row in reader:

        months.append(row[0])
        profit_losses.append(int(row[1]))


    # Count of months
        count_months += 1
    

    # Net total amount of "Profit/Losses" over the entire period

    n = 1
    for n in range(1,len(profit_losses)-1):
        profit_change.append(int(profit_losses[n+1])-int(profit_losses[n]))

    
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes

    average_change = sum(profit_change) / len(profit_change)
    

    # The greatest increase in profits (date and amount) over the entire period

    max_increase = max(profit_change)
    max_increase_date = profit_change.index(max(profit_change)) + 1
    max_month = months[max_increase_date]

    # The greatest decrease in profits (date and amount) over the entire period

    min_increase = min(profit_change)
    min_increase_date = profit_change.index(min(profit_change)) + 1
    min_month = months[min_increase_date]

    # print all statements to terminal

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {count_months}")
    print(f"Total: ${sum(profit_losses)}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {max_month} (${str(max(profit_change))})")
    print(f"Greatest Decrease in Profits: {min_month} (${str(min(profit_change))})")

    # write to ouput file 

    output_file = os.path.join('..','PyBank','Analysis_bank','budget_analysis.txt')
    
    with open(output_file, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("----------------------------\n")
        file.write(f"Total Months: {count_months}\n")
        file.write(f"Total: ${sum(profit_losses)}\n")
        file.write(f"Average Change: ${average_change}\n")
        file.write(f"Greatest Increase in Profits: {max_month} (${str(max(profit_change))})\n")
        file.write(f"Greatest Decrease in Profits: {min_month} (${str(min(profit_change))})\n")
