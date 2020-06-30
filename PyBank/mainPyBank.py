import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")
OutPutPath = os.path.join("Analysis", "Budgetanalysis.txt")
totalPL = 0
totalmonths = 0
aveRevChange = []
lastMonthPL = 0
greatestinc = 0
greatestincMonth = None
changes = []
greatestdec = 0
revChange = 0
diff = 0
# Open and read csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    firstrow = next(csvreader)
    totalmonths = totalmonths + 1
    totalPL += int(firstrow[1])
    lastMonthPL = int(firstrow[1])
    
    for row in csvreader:
        
        #count number of months
        totalmonths = totalmonths + 1

        #add the total amount of "Profit/Losses"
        totalPL += int(row[1])

        #find the difference in values between months
        diff = int(row[1]) - lastMonthPL
                  
        #find the month with the greatest increase in profits
        if diff > greatestinc:
            greatestinc = diff
            greatestincMonth = row[0]
        
        #find the month with the greatest decrease in profits
        if diff < greatestdec:
            greatestdec = diff
            greatestdecMonth = row[0]
        
        aveRevChange.append(diff)
        lastMonthPL = int(row[1])
   
        

#print evertyhing
print("Financial Analysis")
print("--------------------------------------------------") 
print(f"Total Months: {totalmonths}")
print(f"Total Profit/Loss: ${totalPL}")
print(f"Avg. Change: ${round(sum(aveRevChange)/len(aveRevChange),2)}")
print(f"Month with Greatest Increase: {greatestincMonth} ${greatestinc} ")
print(f"Greatest Decrease in Profit/Loss: {greatestdecMonth} ${greatestdec}")

with open(OutPutPath, "w") as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------------------------------\n") 
    file.write(f"Total Months: {totalmonths} \n")
    file.write(f"Total Profit/Loss: ${totalPL} \n")
    file.write(f"Avg. Change: ${round(sum(aveRevChange)/len(aveRevChange),2)} \n")
    file.write(f"Month with Greatest Increase: {greatestincMonth} ${greatestinc} \n")
    file.write(f"Greatest Decrease in Profit/Loss: {greatestdecMonth} ${greatestdec}")
    file.close
