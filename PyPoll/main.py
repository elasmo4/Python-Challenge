import csv

python_challenge_2 = open('Analysis/Election_Report.txt','w')

file = csv.DictReader(open('Resources/election_data.csv'))

votes = 0
candidate_dict = {}

for row in file:
    votes += 1

    candidate = row['Candidate']

    if candidate not in candidate_dict.keys():
        candidate_dict[candidate] = 0

    candidate_dict[candidate] += 1

winner = 0
winner_name = ""

output = f'''
Election Results
-------------------------
Total Votes: {votes:,}
-------------------------
'''
for candidate in candidate_dict.keys():
    output += f"{candidate}: {candidate_dict[candidate]/votes * 100:.2f}% ({candidate_dict[candidate]})\n"
    if candidate_dict[candidate] > winner:
        winner = candidate_dict[candidate]
        winner_name = candidate

output += f'''
-------------------------
Winner: {winner_name}
'''

print(output)

python_challenge_2.write(output)