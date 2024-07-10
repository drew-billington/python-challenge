#!/usr/bin/env python
# coding: utf-8

# In[35]:


#dependencies
import os
import csv


# In[37]:


#file load
csvpath = os.path.join('.','Resources','election_data.csv')

#dependencies / baselines
total_votes = 0
ccs_total = 0
dd_total = 0
rad_total = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # print(csvreader)
    for row in csvreader:
        # print(row)

        #total votes
        total_votes += 1    

        #totals by candidate
        if row[2] == "Charles Casper Stockham":
            ccs_total += 1
        elif row[2] == "Diana DeGette":
            dd_total += 1
        else:
            rad_total += 1

        #percent of total votes by candidate
        ccs_percent = round( ccs_total / total_votes * 100 , 1)
        dd_percent = round( dd_total / total_votes * 100 , 1)
        rad_percent = round( rad_total / total_votes * 100 , 1)

#winner
if ccs_percent > (dd_percent or rad_percent):
    winner = "Charles Casper Stockham"
elif dd_percent > (ccs_percent or rad_percent):
    winner = "Diana DeGette"
else:
    winner = "Raymon Anthony Doane"

#output = use variable 'output' with f strings; use '\n' suffix within quotes to delineate next line...
output = (
f"Election Results\n"
f"-----------------------------\n"
f"Total Votes: {total_votes}\n"
f"-----------------------------\n"
f"Charles Casper Stockham:  {ccs_percent}%  ({ccs_total})\n"
f"Diana DeGette:  {dd_percent}%  ({dd_total})\n"
f"Raymon Anthony Doane:  {rad_percent}%  ({rad_total})\n"
f"-----------------------------\n"
f"Winner: {winner}\n"
f"-----------------------------\n"
)

print(output)


# In[39]:


#export to file
file_output = os.path.join(".","analysis","election_results.txt")
with open(file_output, "w") as txt_file:
    txt_file.write(output)


# In[ ]:




