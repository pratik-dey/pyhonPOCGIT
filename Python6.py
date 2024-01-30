import json
import csv 
with open('2000_TMNAKAFKA_Dataout.json') as json_file:
    data = json.load(json_file)
# Extract the fields you want to include in the CSV file
fields = ['content', '_ts']

# Open a new CSV file and write the header row
with open('data1.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(fields)
    # Write each data row to the CSV file
    for row in data:
        writer.writerow([row[field] for field in fields])
        