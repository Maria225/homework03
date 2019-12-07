# import the os module, create file paths across operating systems, module for reading the csv file
import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("..", "homework03", "election_data.csv")

#define variables
total_votes = 0
total_votes_Khan = 0
total_votes_Correy = 0
total_votes_Li = 0
total_votes_OTooley = 0

# Read in the CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas    
    csvreader = csv.reader(csvfile, delimiter=',')

    #Store the header row and read the header row first
    header = next(csvreader)

    #for loop to find total votes, total votes for Khan, Correy, Li, and O'Tooley
    for row in csvreader:
        total_votes = total_votes + 1
        
        if str(row[2]) == "Khan":
            total_votes_Khan = total_votes_Khan + 1
        
        if str(row[2]) == "Correy":
            total_votes_Correy = total_votes_Correy + 1

        if str(row[2]) == "Li":
            total_votes_Li = total_votes_Li + 1

        if str(row[2]) == "O'Tooley":
            total_votes_OTooley = total_votes_OTooley + 1
    
    #calcualte percent of votes for each candidiate
    percent_of_votes_for_Khan = float(total_votes_Khan)/float(total_votes)*100
    percent_of_votes_for_Correy = float(total_votes_Correy)/float(total_votes)*100
    percent_of_votes_for_Li = float(total_votes_Li)/float(total_votes)*100
    percent_of_votes_for_OTooley = float(total_votes_OTooley)/float(total_votes)*100

    #identify winner
    if percent_of_votes_for_Khan > percent_of_votes_for_Correy and percent_of_votes_for_Khan > percent_of_votes_for_Li and percent_of_votes_for_Khan > percent_of_votes_for_OTooley:
        winner = "Khan"
    elif percent_of_votes_for_Correy > percent_of_votes_for_Khan and percent_of_votes_for_Correy > percent_of_votes_for_Li and percent_of_votes_for_Correy > percent_of_votes_for_OTooley:
        winner = "Correy"   
    elif percent_of_votes_for_Li > percent_of_votes_for_Khan and percent_of_votes_for_Li > percent_of_votes_for_Correy and percent_of_votes_for_Li > percent_of_votes_for_OTooley:
        winner = "Li"
    elif percent_of_votes_for_OTooley > percent_of_votes_for_Khan and percent_of_votes_for_OTooley > percent_of_votes_for_Correy and percent_of_votes_for_OTooley > percent_of_votes_for_Li:
        winner = "O'Tooley"

    # print results
    print(f"Election Results")
    print(f"-------------------")
    print(f"Total Votes: {str(total_votes)}")
    print(f"-------------------")
    print(f"Khan: {str(percent_of_votes_for_Khan)}% ({str(total_votes_Khan)})")
    print(f"Correy: {str(percent_of_votes_for_Correy)}% ({str(total_votes_Correy)})")
    print(f"Li: {str(percent_of_votes_for_Li)}% ({str(total_votes_Li)})")
    print(f"O'Tooley: {str(percent_of_votes_for_OTooley)}% ({str(total_votes_OTooley)})")
    print(f"-------------------")
    print(f"Winner: {str(winner)}") 
    print(f"-------------------")

#write to a text file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join("pyvotes_output.txt")
with open(output_path, "w", newline="") as txt_file:
    txt_file.write("Election Results \n")
    txt_file.write("------------------- \n")
    txt_file.write("Total Votes: {(total_votes)} \n")
    txt_file.write("------------------- \n")
    txt_file.write(f"Khan: {(percent_of_votes_for_Khan)}% ({(total_votes_Khan)}) \n")
    txt_file.write(f"Correy: {(percent_of_votes_for_Correy)}% ({(total_votes_Correy)}) \n")
    txt_file.write(f"Li: {(percent_of_votes_for_Li)}% ({(total_votes_Li)}) \n")
    txt_file.write(f"O'Tooley: {(percent_of_votes_for_OTooley)}% ({(total_votes_OTooley)}) \n")
    txt_file.write("------------------- \n")
    txt_file.write(f"Winner: {(winner)} \n")
    txt_file.write("------------------- \n")