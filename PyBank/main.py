import csv

# Dates array
dates = []
# Profit/Loss array
profit_loss = []
# Initialize netProfitLoss variable to 0
netProfitLoss = 0
# Change in monthly revenue dictionary
monthlyRevenueChangeArr = []
monthlyRevenueChange = 0
# greatestProfitIncreaseKeysArr = []


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
        monthlyRevenueChangeArr.append(
            {"date": row[0], "value": profitLossChangeFromPrevRow})
        monthlyRevenueChange = monthlyRevenueChange + profitLossChangeFromPrevRow

        netProfitLoss = netProfitLoss + int(row[1])

Avg_ProfitLossChange = monthlyRevenueChange/(len(dates) - 1)
sortedMonthlyRevenueArray = sorted(
    monthlyRevenueChangeArr, key=lambda item: item["value"])
length_sortedMonthlyRevenueArray = len(sortedMonthlyRevenueArray)
greatestProfitDecreaseDate = (sortedMonthlyRevenueArray[0])["date"]
greatestProfitDecrease = (sortedMonthlyRevenueArray[0])["value"]
greatestProfitIncreaseDate = (
    sortedMonthlyRevenueArray[length_sortedMonthlyRevenueArray - 1])["date"]
greatestProfitIncrease = (
    sortedMonthlyRevenueArray[length_sortedMonthlyRevenueArray - 1])["value"]

# Print Analysis to Terminal
print(f'Financial Analysis\n')
print(f'----------------------------\n')
# The length of the dates array --> no.of months
print(f'Total Months: {len(dates)}\n')
# The net total amount of profit/losses over a period
print(f'Total: {netProfitLoss}\n')
# The average of profit loss changes over a period
print(f'Average Change: ${Avg_ProfitLossChange:.2f}\n')
print(
    f'Greatest Increase in Profits: {greatestProfitIncreaseDate} (${greatestProfitIncrease})\n')
print(
    f'Greatest Decrease in Profits: {greatestProfitDecreaseDate} (${greatestProfitDecrease})\n')


# Write the outputs to an analysis file
with open('analysis/analysis.txt', 'w') as analysisFile:
    analysisFile.write(f'Financial Analysis\n')
    analysisFile.write(f'----------------------------\n')
    analysisFile.write(f'Total Months: {len(dates)}\n')
    analysisFile.write(f'Total: {netProfitLoss}\n')
    analysisFile.write(f'Average Change: ${Avg_ProfitLossChange:.2f}\n')
    analysisFile.write(
        f'Greatest Increase in Profits: {greatestProfitIncreaseDate} (${greatestProfitIncrease})\n')
    analysisFile.write(
        f'Greatest Decrease in Profits: {greatestProfitDecreaseDate} (${greatestProfitDecrease})\n')
