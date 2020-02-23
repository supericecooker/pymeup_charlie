#doing imports
import os
import csv
#pulling file
csv_file = os.path.join('budget_data.csv')
#open file with read mode 
with open(csv_file,'r') as budget_data:
    csv_reader = csv.reader(budget_data, delimiter=',')
    #read header of data table
    header = next(csv_reader)
    print(f'the headers are:{header}')
#Track month values 
month_total = 0 
#track total profit/losses to

net_profit_total = 0
#store old profit
before_profit = 0
profit = []
change_over_month = []
change_profit = []
average_profit = 0

#track greatest loss
greatest_loss = ["",999999999]
#track greatest profit
greatest_profit = ["",0]
#loop through all data 
for row in csv_reader:
    #calculate month total
    month_total = month_total += 1
    #calculate profit total
    net_profit_total = net_profit_total + int(row["Profit/Losses"])
    #calculate change in profit
    before_profit = float(row["Profit/Losses"])
    change_profit = float(row["Profit/Losses"])- before_profit
    change_over_month = [change_over_month] + [row["Date"]]

    #The greatest increase in profit
        if change_profit>greatest_profit[1]:
            greatest_profit[1]= change_profit
            greatest_profit[0] = row['Date']

        #The greatest decrease in revenue (date and amount) over the entire period
        if change_profit<greatest_loss[1]:
            greatest_loss[1]= change_profit
            greatest_loss[0] = row['Date']
    average_profit = sum(change_profit)/len(change_profit)
    
#print what i have
print(f'Financial Analysis')
print(f'------------------')
print(f'Total number Months: {month_total}')
print(f'Net Total of profit/losses: {net_profit_total}')
print(f'average of change in profit/losses:{average_profit}')
print(f'greatest increase in profit:{change_profit},+ {greatest_profit}')
print(f'greatest decrease in profit:{change_profit},+ {greatest_loss}')

        




