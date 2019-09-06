# Modules
import os
import csv
import sys

# Set path for file
csvpath = os.path.join('budget_data.csv')

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvreader)

    # Define variables
    current_month = 0
    total_amount = 0
    previous_month_amount = 0
    total_change = 0
    greatest_increase_amount = 0
    greatest_increase_month = ''
    greatest_decrease_amount = 0
    greatest_decrease_month = ''

    # Iterate on each row
    for month_row in csvreader:
        # get the current month's amount
        current_month_amount = int(month_row[1])

        # calculate the change between previous and current month
        change = current_month_amount - previous_month_amount

        # increase the total change
        if current_month != 0:
            total_change = total_change + change

        # set the previous month's amount to use in the next iteration
        previous_month_amount = current_month_amount

        # increase the current month number
        current_month = current_month + 1

        # increase the total amount
        total_amount = total_amount + current_month_amount
        
        # check if it is the greatest increase
        if greatest_increase_amount < change:
            greatest_increase_amount = change
            greatest_increase_month = month_row[0] 

        # check if it is the greatest decrease
        if greatest_decrease_amount > change:
            greatest_decrease_amount = change
            greatest_decrease_month = month_row[0] 

# set total months to print
total_months = current_month

# print everything to the terminal
print('Financial Analysis')
print('----------------------------')
print('Total Months: ', total_months)
print('Total: $' + str(total_amount))
print('Average  Change: $' + str(round(total_change / (total_months - 1), 2)))
print('Greatest Increase in Profits: ' + greatest_increase_month + ' ($' + str(greatest_increase_amount) + ')')
print('Greatest Decrease in Profits: ' + greatest_decrease_month + ' ($' + str(greatest_decrease_amount) + ')')

# print everything to the results file
results_file = open('PyBank_Results.txt', 'w')
sys.stdout = results_file

print('Financial Analysis')
print('----------------------------')
print('Total Months: ', total_months)
print('Total: $' + str(total_amount))
print('Average  Change: $' + str(round(total_change / (total_months - 1), 2)))
print('Greatest Increase in Profits: ' + greatest_increase_month + ' ($' + str(greatest_increase_amount) + ')')
print('Greatest Decrease in Profits: ' + greatest_decrease_month + ' ($' + str(greatest_decrease_amount) + ')')
