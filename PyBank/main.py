import csv

#export as text file
python_challenge_1 = open("Analysis/budget_report.txt", "w")

#where to read csv file
with open("C:/Users/Al/OneDrive/Desktop/Data-Analyst/Projects/Python_Analysis/Python-Challenge/PyBank/Resources/budget_data.csv", "r") as csvfile:

    #read csv file and separate values by commas
    csvreader = csv.reader(csvfile, delimiter=",")

    #separate headers
    csv_header = next(csvreader)


    date = []
    day = []
    month = []
    statement = []
    pre_revenue = 0
    total_change = 0
    increase = ["", 0]
    decrease = ["", 0]

    #iterate through each row in file
    for row in csvreader:
        #store values in column A to empty list called date
        date.append(row[0])
        #split values in date by dash
        split_date = row[0].split("-")
        #store values to left of dash into empty list day
        day.append(split_date[0])
        #store values to right of dash into empty list month
        month.append(split_date[1])

        #store values in column B as intergers into variable called revenue
        revenue = int(row[1])
        #store revenue values in empty list called statement
        statement.append(revenue)

        #difference between the previous value and the current value in column B
        change = revenue-pre_revenue
        #initializing change
        if pre_revenue == 0:
            change = 0
        total_change += change

        #finding the greatest increase in profits
        if change > increase[1]:
            increase[0] = row[0]
            increase[1] = change

        #finding the greatest decrease in profits
        if change < decrease[1]:
            decrease[0] = row[0]
            decrease[1] = change

        pre_revenue = revenue

    output = f"""
Financial Analysis
----------------------------
Total Months: {len(month)}
Total: ${sum(statement):,}
Average Change: ${total_change/(len(month) - 1):,.2f}
Greatest Increase in Profits: {increase[0]} (${increase[1]:,})
Greatest Decrease in Profits: {decrease[0]} (${decrease[1]:,})
"""
    
print(output)

python_challenge_1.write(output)

        
        