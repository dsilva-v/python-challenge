import csv

# Dates array
dates = []
# Profit/Loss array
profit_loss = []
# Initialize netProfitLoss variable to 0
netProfitLoss = 0

# open csv file
with open('Resources/budget_data.csv', newline='') as budgetDataCSVFile:
    csvReader = csv.reader(
        budgetDataCSVFile, delimiter=',')
    row = next(csvReader)
    for row in csvReader:
        dates.append(row[0])
        profit_loss.append(int(row[1]))
        netProfitLoss = netProfitLoss + int(row[1])

# The length of the dates array - 1(excluding header)--> no.of months
print(len(dates))
# The length of the dates array - 1(excluding header)--> no.of months
print(profit_loss)
# The net total amount of profit/losses over a period
print(netProfitLoss)
