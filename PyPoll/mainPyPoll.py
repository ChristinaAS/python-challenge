import os
import csv


totalvotes = 0
can_list = []
candidatevotes = {}
winning_candidate = ""
winning_count = 0


#Import and export paths
election_csv = os.path.join('Resources', 'election_data.csv')
OutPutPath = os.path.join("Analysis", "Pollanalysis.txt")

#open and read csv
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        
        #Count the votes
        totalvotes += 1

        # Pick out the candidates
        candidatename = row[2]
        if candidatename in can_list:
            candidatevotes[candidatename] = candidatevotes[candidatename] + 1
            # Add new candidate to the list
        else:
            can_list.append(candidatename)
            candidatevotes[candidatename]= 1
    
    #create a loop to count percentages for each candidate
    for candidate in candidatevotes:
        votes = candidatevotes[candidate]
        votepercentage = float(votes)/float(totalvotes)
        votepercentage = "{:.2%}".format(votepercentage)
        
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
         

#print evertyhing
print("Election Results")
print("--------------------------------------------------") 
print(f"Total Votes: {totalvotes}")
print("--------------------------------------------------")
for candidate in candidatevotes:
    votes = candidatevotes[candidate]
    votepercentage = float(votes)/float(totalvotes)
    votepercentage = "{:.2%}".format(votepercentage)
    print(candidate + ": " + str(candidatevotes[candidate]) + " (" + str(votepercentage) + ")")
print("---------------------------------------------------")
print("Winner " + (winning_candidate))

with open(OutPutPath, "w") as file:
    file.write("Election Results \n")
    file.write("----------------------------------------------------\n") 
    file.write(f"Total Votes: {totalvotes} \n")
    file.write("----------------------------------------------------\n")
    for candidate in candidatevotes:
        votes = candidatevotes[candidate]
        votepercentage = float(votes)/float(totalvotes)
        votepercentage = "{:.2%}".format(votepercentage)
        file.write(candidate + ": " + str(candidatevotes[candidate]) + " (" + str(votepercentage) + ") \n")
    file.write("-----------------------------------------------------\n")
    file.write("Winner " + (winning_candidate))
    file.close
