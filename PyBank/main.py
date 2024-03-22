import os
import csv

#set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
# print(csvpath)

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # Creating Varibales
    total_months = 0
    total_net = 0
    previous_row_values = []
    monthly_changes = []
    greatest_increase_date = ""
    greatest_increase_amount = 0
    greatest_decrease_date = ""
    greatest_decrease_amount = 0


    # For loop
    header = next(csvreader)
    for current_row_values in csvreader:
        # print(previous_row_values)
        # print(current_row_values)
        
        # Count the totla number months included in the csv file
        total_months = total_months + 1
        # print("Total Months: ", str(total_months))
         
        # print(type (csv_row_value))
        # lets store the month and the profit loss as two seprate values
        # print(csv_row_value[0])
        # print(current_row_values[1])

        current_row_month = current_row_values[0]
        current_row_profit_losses = current_row_values[1]

        # The net total amount of "Profit/Losses" over the entire period
        total_net = total_net + int(current_row_profit_losses)
        # print(total_net)


        if len(previous_row_values) > 0:
            difference_between_current_and_previous_month = int(current_row_profit_losses) - int(previous_row_values[1])
            # print(difference_between_current_and_previous_month)
            monthly_changes.append(difference_between_current_and_previous_month)
            # print(monthly_changes)

            # Calculating the greatest increased amount
            if difference_between_current_and_previous_month > greatest_increase_amount:
                greatest_increase_amount = difference_between_current_and_previous_month
                greatest_increase_date = current_row_month

            if difference_between_current_and_previous_month < greatest_decrease_amount:
                greatest_decrease_amount = difference_between_current_and_previous_month
                greatest_decrease_date = current_row_month



        #updating previours row values to a current row values to be used by the next month(row)
        previous_row_values = current_row_values
        # print(previous_row_values)
        # print("-----")

# Calculate total montly changes
total_entire_period_change = sum(monthly_changes)
# print(total_entire_period_change)

# Calculate average entire period changes
average_entire_period_change = total_entire_period_change / len(monthly_changes)
# print(average_entire_period_change)

with open("analysis/Financial Analysis.txt", "w") as file:
    message = f"""Financial Analysis
{"-"*28}
Total Months: {total_months}
Total: ${total_net}
Average Change: ${round(average_entire_period_change, 2)}
Greatest Increase in Profits: {greatest_increase_date} ({greatest_increase_amount})
Greatest Decrease in Profits: {greatest_decrease_date} ({greatest_decrease_amount})"""
    print(message)
    file.write(message)










