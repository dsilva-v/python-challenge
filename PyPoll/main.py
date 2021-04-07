import csv

# voterId array
voterIds = []
# dictionary to hold voterid, county and candidate name
electionData = {}

# open csv file
with open('Resources/election_data.csv', newline='') as electionDataCSVFile:
    csvReader = csv.reader(
        electionDataCSVFile, delimiter=',')
    row = next(csvReader)

    for row in csvReader:
        voterIds.append(row[0])

        if not row[2] in electionData:
            electionData[row[2]] = 1
        else:
            electionData[row[2]] += 1

# Calculate the winner
Winner = max(electionData, key=electionData.get)
# Assign a var with total number of votes
TotalVotes = len(voterIds)

# Print Analysis to Terminal
print(f'Election Results\n')
print(f'----------------------------\n')
# Total number of votes cast
print(f'Total Votes: {TotalVotes} \n')
print(f'----------------------------\n')
for key, value in electionData.items():
    print(f'{key}: ({value})\n')
print(f'----------------------------\n')
print(f'Winner: {Winner} \n')
print(f'----------------------------\n')


# Write the outputs to an analysis file
with open('analysis/analysis.txt', 'w') as analysisFile:
    analysisFile.write(f'Election Results\n')
    analysisFile.write(f'----------------------------\n')
    analysisFile.write(f'Total Votes: {TotalVotes} \n')
    analysisFile.write(f'----------------------------\n')
    for key, value in electionData.items():
        analysisFile.write(f'{key}: ({value})\n')
    analysisFile.write(f'----------------------------\n')
    analysisFile.write(f'Winner: {Winner} \n')
    analysisFile.write(f'----------------------------\n')
