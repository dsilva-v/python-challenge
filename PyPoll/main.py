import csv

# voterId array
voterId = []
# votes count array
count = []
# candidates arrray
candidates = []

# open csv file
with open('Resources/election_data.csv', newline='') as electionDataCSVFile:
    csvReader = csv.reader(
        electionDataCSVFile, delimiter=',')
    row = next(csvReader)
    for row in csvReader:
        voterId.append(row[0])
        count.append(row[1])
        candidates.append(row[2])
# Total number of votes cast
print(len(count))
