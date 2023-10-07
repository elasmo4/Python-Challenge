import csv

#export as text file
python_challenge_2 = open('Analysis/Election_Report.txt','w')

#read file as dictionary
file = csv.DictReader(open('Resources/election_data.csv'))

#initialize votes
votes = 0
candidate_dict = {}
winner = 0
winner_name = ""

#iterate through each row in file
for row in file:
    #counting votes
    votes += 1

    #store candidates to variable "candidate"
    candidate = row['Candidate']

    #candidate's name appears once in dictionary
    if candidate not in candidate_dict.keys():
        #initialize count for each candidate
        candidate_dict[candidate] = 0

    #add up counts for each candidate
    candidate_dict[candidate] += 1


output = f'''
Election Results
-------------------------
Total Votes: {votes:,}
-------------------------
'''
#iterate through the value pairs for each key
for candidate in candidate_dict.keys():
    #string together candidate's name, percentage of votes, and total votes in parentheses
    output += f"{candidate}: {candidate_dict[candidate]/votes * 100:.2f}% ({candidate_dict[candidate]})\n"

    #find the greatest candidate vote
    if candidate_dict[candidate] > winner:
        #store the greatest vote in winner
        winner = candidate_dict[candidate]
        #store winner's name
        winner_name = candidate

output += f'''
-------------------------
Winner: {winner_name}
'''

print(output)

python_challenge_2.write(output)