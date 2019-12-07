# import the os module, create file paths across operating systems, module for reading the csv file
import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("..", "homework03", "budget_data.csv")

#define variables
total_months = 0
total_net = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 55555555]
net_change_list = []

# Read in the CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas    
    csvreader = csv.reader(csvfile, delimiter=',')

    #Store the header row and read the header row first
    header = next(csvreader)
    first_row = next(csvreader)
    
    #define variables in for loop
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    previous_net = int(first_row[1])

    #for loop to find total monts, total net, total change, previous net, and net change list
    for row in csvreader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list = net_change_list + [net_change]
    
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
   
    # calculate average (note used len and not months, because it is a comparision between 2 months)
    average = sum(net_change_list)/len(net_change_list)

    # print results
    print(f"Financial Analysis")
    print(f"-------------------")
    print(f"Total Months: {str(total_months)}")
    print(f"Total: ${str(total_net)}")
    print(f"Average Change: ${str(average)}")
    print(f"Greatest Increase in Profits: {str(greatest_increase)}")
    print(f"Greatest Decrease in Profits: {str(greatest_decrease)}")

#write to a text file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join("pybank_output.txt")
with open(output_path, "w", newline="") as txt_file:
    txt_file.write("Financial Analysis \n")
    txt_file.write("------------------- \n")
    txt_file.write(f"Total Months: {(total_months)} \n")
    txt_file.write(f"Total: ${(total_net)} \n")
    txt_file.write(f"Average Change: ${(average)} \n")
    txt_file.write(f"Greatest Increase in Profits: {(greatest_increase)} \n")
    txt_file.write(f"Greatest Decrease in Profits: {str(greatest_decrease)} \n")