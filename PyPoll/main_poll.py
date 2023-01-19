import os
import csv

# Path to collect data
poll_csv_path = os.path.join('..','PyPoll','Resources_poll','election_data.csv')

# Define variables

total_votes = 0
Stockham_votes = 0
DeGette_votes = 0
Doane_votes = 0

# open and read CSV
with open(poll_csv_path, 'r') as file:

    reader = csv.reader(file, delimiter=",")

    csv_header = next(file)
             
    # Read through each row of data after the header
    for row in reader:
            

    # The total number of votes cast
        total_votes += 1
       

    # A complete list of candidates who received votes

        if (row[2]) == "Charles Casper Stockham":
            Stockham_votes += 1
        elif (row[2]) == "Diana DeGette":
            DeGette_votes += 1
        elif (row[2]) == "Raymon Anthony Doane":
            Doane_votes += 1

    # The percentage of votes each candidate won
        percent_Stockham = (Stockham_votes/total_votes)
        percent_DeGette = (DeGette_votes/total_votes)
        percent_Doane = (Doane_votes/total_votes)

    # The total number of votes each candidate won

    names = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
    votes = [Stockham_votes, DeGette_votes, Doane_votes]

    dict_names_votes = dict(zip(names, votes))

    # The winner of the election based on popular vote.
    key = max(dict_names_votes, key=dict_names_votes.get)


    # print all statements to terminal

    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")
    print(f"Charles Casper Stockham: {percent_Stockham:.3%} ({Stockham_votes})")
    print(f"Diana DeGette: {percent_DeGette:.3%} ({DeGette_votes})")
    print(f"Raymon Anthony Doane: {percent_Doane:.3%} ({Doane_votes})")
    print("----------------------------")
    print(f"Winner: {key}")
  
    # write to ouput file 
    
output_file = os.path.join('..','PyPoll','Analysis_poll','election_analysis.txt')
    
with open(output_file, 'w') as file:
        file.write("Election Results\n")
        file.write("----------------------------\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write("----------------------------\n")
        file.write(f"Charles Casper Stockham: {percent_Stockham:.3%} ({Stockham_votes})\n")
        file.write(f"Diana DeGette: {percent_DeGette:.3%} ({DeGette_votes})\n")
        file.write(f"Raymon Anthony Doane: {percent_Doane:.3%} ({Doane_votes})\n")
        file.write("----------------------------\n")
        file.write(f"Winner: {key}\n")