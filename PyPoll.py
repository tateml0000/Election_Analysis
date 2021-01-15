# The data we need to retrieve
# 1. The total number of cotes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each canddiate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a vaiable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a vaiable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the elevtion results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and rpint the header row
    headers = next(file_reader)
    print(headers)
    
    









