#!/usr/bin/env python
# coding: utf-8

# In[1]:


#NEED:



# In[193]:


#dependencies
import os
import csv


# In[195]:


#file load
csvpath = os.path.join('.','Resources','budget_data.csv')

total_months = 0
total = 0

net_change_list = []

greatest = ["", 0]
least = ["", 999999999]
# print(greatest)
# print(least)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    header = next(csvreader)
    # print(f"Header: {header}")
    first_row = next(csvreader)
    total =+ int(first_row[1])
    previous_net = int(first_row[1])

    total_months += 1
    
    for row in csvreader:
        # print(row)
        total_months += 1
        total += int(row[1])

        #avg change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
        avg_change = round( sum(net_change_list) / len(net_change_list) , 2)
#print(net_change_list)

        #greatest increase
        if(net_change)> greatest[1]:
            greatest[0] = row[0]
            greatest[1] = net_change
            great_inc_profit = greatest[1]
            great_inc_date = greatest[0]

        #greatest decrease
        if(net_change)< least[1]:
            least[0] = row[0]
            least[1] = net_change
            great_dec_date = least[0]
            great_dec_profit = least[1]

#output = use variable 'output' with f strings; use '\n' suffix within quotes to delineate next line...
output = (
f"Financial Analysis\n"
f"-------------------------------------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${total}\n"
f"Average Change: ${avg_change}\n"
f"Greatest Increase in Profits:  {great_inc_date}  ${great_inc_profit}\n"
f"Greatest Decrease in Profits:  {great_dec_date}  ${great_dec_profit}\n" )

print(output)


# In[197]:


#export to file
file_output = os.path.join(".","analysis","budget_analysis.txt")
with open(file_output, "w") as txt_file:
    txt_file.write(output)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




