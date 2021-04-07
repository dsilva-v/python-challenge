import csv

# Dates array
dates = []
# Profit/Loss array
profit_loss = []
# Initialize netProfitLoss variable to 0
netProfitLoss = 0
# Change in monthly revenue dictionary
monthlyRevenueChange = {}
greatestProfitIncreaseKeysArr = []


# open csv file
with open('Resources/budget_data.csv', newline='') as budgetDataCSVFile:
    csvReader = csv.reader(
        budgetDataCSVFile, delimiter=',')

    # skip the headers
    csvHeaders = next(csvReader)

    # This is only for getting hold of initial row values for calcualtion of averages later
    firstRow = next(csvReader)

    # assign the first row's profit/loss,date data to a variable to help start calculating the change of profit/loss over entire period
    prevRowProfitLoss = int(firstRow[1])
    prevRowDate = firstRow[0]

    # These will make sure we didn't skip saving the first row's data
    dates.append(prevRowDate)
    profit_loss.append(prevRowProfitLoss)
    netProfitLoss = netProfitLoss + prevRowProfitLoss

    for row in csvReader:
        dates.append(row[0])
        profit_loss.append(int(row[1]))
        # calculation of the change of profit or loss over a period
        profitLossChangeFromPrevRow = int(row[1]) - prevRowProfitLoss
        # Preserve the prev row's value for next iteration
        prevRowProfitLoss = int(row[1])
        # Helps calcualte the average of profit loss changes over a period
        monthlyRevenueChange[row[0]] = profitLossChangeFromPrevRow
        # monthlyRevenueChange['Date'].append(row[0])
        netProfitLoss = netProfitLoss + int(row[1])

Avg_ProfitLossChange = sum(monthlyRevenueChange.values())/(len(dates) - 1)
sortedMonthlyRevenueArray = sorted(monthlyRevenueChange.values())
greatestProfitIncreaseKeysArr = monthlyRevenueChange.keys()
greatestProfitIncreaseDate = list(greatestProfitIncreaseKeysArr)[0]
greatestProfitIncrease = monthlyRevenueChange[greatestProfitIncreaseDate]

# The length of the dates array --> no.of months
print(len(dates))
# array of profit and loss values
print(sortedMonthlyRevenueArray)
# The net total amount of profit/losses over a period
print(netProfitLoss)
# The average of profit loss changes over a period
print(Avg_ProfitLossChange)


# Write the outputs to an analysis file
with open('analysis/analysis.txt', 'w') as analysisFile:
    analysisFile.write(f'Financial Analysis\n')
    analysisFile.write(f'----------------------------\n')
    analysisFile.write(f'Total Months: {len(dates)}\n')
    analysisFile.write(f'Total: {netProfitLoss}\n')
    analysisFile.write(f'Average Change: {Avg_ProfitLossChange:.2f}\n')
    analysisFile.write(
        f'GPI: {greatestProfitIncrease} on {greatestProfitIncreaseDate}\n')
    analysisFile.write('')
