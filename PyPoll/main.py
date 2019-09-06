# Modules
import os
import csv
import sys

# Set path for file
csvpath = os.path.join('election_data.csv')

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvreader)

    # Define variables
    votes_dict = {}
    total_number_of_votes = 0

    # Iterate on each row
    for vote_row in csvreader:
        # increase the total number of votes by 1
        total_number_of_votes = total_number_of_votes + 1

        # get the candidate's name from the 3rd column
        candidate_name = vote_row[2]

        # get the candidate's total vote number (get zero if no votes were added to votes_dict yet)
        candidate_total_vote = votes_dict.get(candidate_name, 0)

        # increase the number of votes for the candidate in the dict
        votes_dict[candidate_name] = candidate_total_vote + 1

# print everything to the terminal
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(total_number_of_votes))
print('-------------------------')
winner = ''
winner_percentage = 0
for candidate_name in votes_dict:
    vote_percentage = votes_dict[candidate_name] / total_number_of_votes * 100
    print(candidate_name + ': ' + str(round(vote_percentage, 3)) + '% (' + str(votes_dict[candidate_name]) + ')')
    if winner_percentage < vote_percentage:
        winner = candidate_name
        winner_percentage = vote_percentage
print('-------------------------')
print('Winner: ' + winner)
print('-------------------------')

# print everything to the results file
results_file = open('PyPoll_Results.txt', 'w')
sys.stdout = results_file

print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(total_number_of_votes))
print('-------------------------')
winner = ''
winner_percentage = 0
for candidate_name in votes_dict:
    vote_percentage = votes_dict[candidate_name] / total_number_of_votes * 100
    print(candidate_name + ': ' + str(round(vote_percentage, 3)) + '% (' + str(votes_dict[candidate_name]) + ')')
    if winner_percentage < vote_percentage:
        winner = candidate_name
        winner_percentage = vote_percentage
print('-------------------------')
print('Winner: ' + winner)
print('-------------------------')
