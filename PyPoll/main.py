import os
import csv

#set path for file
csvpath = os.path.join("Resources", "election_data.csv")
# print(csvpath)

# Creating Variables

total_number_vote = 0
candidates_list = []
candidates_vote = {}
Percent_votes_candidate = 0
total_number_candidate_won = 0
total_percentage_vote_per_candidate = []
winner_candidate = ""


# # Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # set up for loop
    header = next(csvreader)
    for current_row_value in csvreader:
        # print(current_row_value)
        # print(total_number_vote)
    
        # print(type (current_row_value))
        # lets store the Ballot ID, County, and Candidates as three seprate values
        # print(current_row_value[0])
        # print(current_row_value[1])
        # print(current_row_value[2])
        
        # Count the totla number cotes cast
        total_number_vote = total_number_vote + 1
        # print("Total Number of Votes: ", str(total_number_vote))

        # Create a complete list of candidates who received votes
        candidate = current_row_value[2]
        # print(candidate)

        # Adding each candidate in the candidates list
        if candidate not in candidates_list:
            candidates_list.append(candidate)

            #Initializing candidates vote 
            candidates_vote[candidate] = 0

        # Calculating total number of votes each candidate won
        candidates_vote[candidate] = candidates_vote[candidate] + 1
        candidates_vote.keys()

#calculating the total number of votes for each candidates
total_num_vote_Charles = candidates_vote["Charles Casper Stockham"] 
total_num_vote_Diana= candidates_vote["Diana DeGette"] 
total_num_vote_Raymon = candidates_vote["Raymon Anthony Doane"] 
#Printing to confirm total number of votes for each candidates
# print(total_num_vote_Charles)
# print(total_num_vote_Diana)
# print(total_num_vote_Raymon)

# print("Total Number of Votes: ", str(total_number_vote))

# see if all total number of votes for each candidates printed
# print(candidates_vote)
# print(candidates_vote["Charles Casper Stockham"])
# print(candidates_vote["Diana DeGette"])
# print(candidates_vote["Raymon Anthony Doane"])
# Calculateing the percentage of votes each candidate won
total_Perc_vote_Charles = (candidates_vote["Charles Casper Stockham"] / total_number_vote) * 100
total_Perc_vote_Diana= (candidates_vote["Diana DeGette"] / total_number_vote) * 100
total_Perc_vote_Raymon= (candidates_vote["Raymon Anthony Doane"] / total_number_vote) * 100

# print(total_Perc_vote_Charles)
# print(total_Perc_vote_Diana)
# print(total_Perc_vote_Raymon)

# Find the winner of the election based on popular vote
winner_candidate = max(candidates_vote, key=candidates_vote.get)
# print(winner_candidate)

# Printing the Election Results
with open("analysis/Election Results.txt", "w") as file:
    message = f"""Election Results

{"-"*28}

Total Votes: {total_number_vote}

{"-"*28}

Charles Casper Stockham: {round(total_Perc_vote_Charles, 3)}% ({total_num_vote_Charles})

Diana DeGette: {round(total_Perc_vote_Diana, 3)}% ({total_num_vote_Diana})

Raymon Anthony Doane: {round(total_Perc_vote_Raymon, 3)}% ({total_num_vote_Raymon})

{"-"*28}

Winner: {winner_candidate}

{"-"*28}"""
    print(message)
    file.write(message)