#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import os

# Files to load and output
file_to_load = os.path.join(".", "Resources", "election_data.csv")
file_output = os.path.join(".", "election_analysis.txt")

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_votes = {}
candidate_options = []

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    # Read the header
    header = next(reader)
    print(header)
    
    for row in reader:
        # Add to the total vote count
        total_votes = total_votes + 1
        # print(row)
        
        # Get the candidate name from each row
        candidate_name = row[2]
        
        # If candidate does not match any existing candidate...
        # in a way our loop is discovering candidates as it goes
        if candidate_name not in candidate_options:
            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)
            
            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0
        
        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

with open(file_output, "w") as txt_file:
    election_results += (
        f"Total Votes {total_votes}\n"
        "-------------------------\n"
    )
    print(election_results, end="")
    
    txt_file.write(election_results)
    
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        voter_output = f"{candidate}: {vote_percentage:.1f}% ({votes})\n"
        print(voter_output, end="")
        
        txt_file.write(voter_output)
    
    winning_candidate_summary = (
        "-------------------------\n"
        f"Winner: {winning_candidate}\n"
        "-------------------------\n"
    )
    print(winning_candidate_summary)
    
    txt_file.write(winning_candidate_summary)




# In[ ]:




