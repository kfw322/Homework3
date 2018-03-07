import os
import csv

files = []
name = ""
votes = 0
totalvotes = 0
candidate = []
i = 0
data = []
highnumber = 0
winner = ""

print("Files found in Resources directory:")
for file in os.listdir("Resources"):
    if file.endswith(".csv"):
        files.append(file)
        print("(", files.index(file), ") ", os.path.join(file))

userchoice = int(input("Which file do you want to run? Pick the number of your selection: "))
filepath = os.path.join("Resources", files[userchoice])

with open(filepath,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    for row in csvreader:
        name = str(row[2])
        data.append(name)
        if name not in candidate:
            candidate.append(name)

totalvotes = len(data)
print("Results:")
for c in candidate:
    votes = data.count(c)
    if votes > highnumber:
        winner = c
        highnumber = votes
    elif votes == highnumber:
        winner = "Tie"
    else:
        winner = winner
    print(str(c), ": ", round(votes/totalvotes*100, 2), "% (", str(votes), ")")
print("Winner: ", winner)
print("Total Votes: ", totalvotes)