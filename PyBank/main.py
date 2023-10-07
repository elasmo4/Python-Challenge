import csv

# open csv file
python_challenge_1 = open("Analysis/budget_report.txt", "w")

with open("C:/Users/Al/OneDrive/Desktop/Data-Analyst/Projects/Python_Analysis/Python-Challenge/PyBank/Resources/budget_data.csv", "r") as csvfile:
#   read csv file
#   csvreader = csvfile.read()
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
#   print(f'CSV Header: {csv_header}')

    date = []
    day = []
    month = []
    statement = []
    pre_rev = 0
    total_ch = 0
    inc = ["", 0]
    dec = ["", 0]


    for row in csvreader:
        date.append(row[0])
        split_date = row[0].split("-")
        #print(split_date)
        day.append(split_date[0])
        month.append(split_date[1])
        rev = int(row[1])
        statement.append(rev)

        ch = rev-pre_rev
        if pre_rev == 0:
            ch = 0
        total_ch += ch

        if ch > inc[1]:
            inc[0] = row[0]
            inc[1] = ch

        if ch < dec[1]:
            dec[0] = row[0]
            dec[1] = ch

        pre_rev = rev

    output = f"""
Financial Analysis
----------------------------
Total Months: {len(month)}
Total: ${sum(statement):,}
Average Change: ${total_ch/(len(month) - 1):,.2f}
Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})
"""
    
print(output)

python_challenge_1.write(output)

        
        