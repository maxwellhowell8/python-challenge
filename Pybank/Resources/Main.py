import os 
import csv
from pathlib import Path

csvpath = os.path.join("budget_data.csv")

total_months = []
total_profit = []
monthly_profit_change = []
 
with open('./Resources/budget_data.csv','r') as budget_data:

     # Store the contents of budget_data.csv in the variable budget_data
    budget_data = csv.reader(budget_data,delimiter=",") 

    # Skip the header labels to iterate with the values
    header = next(budget_data)  

    # Iterate through the rows in the stored file contents
    for row in budget_data: 

        # Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Obtain the max and min of the the montly profit change list
Greatest_increase_value = max(monthly_profit_change)
Greatest_decrease_value = min(monthly_profit_change)

# Correlate max and min to the proper month
Greatest_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
Greatest_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 
       
        #print
        
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[Greatest_increase_month]} (${(str(Greatest_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[Greatest_decrease_month]} (${(str(Greatest_decrease_value))})") 
        


# Output files
output_path = './Analysis/Financial_Analysis_Summary.txt' 

with open(output_path,"w") as file:
    #write
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[Greatest_increase_month]} (${(str(Greatest_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[Greatest_decrease_month]} (${(str(Greatest_decrease_value))})")




