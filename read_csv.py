import csv

with open('file1.csv','r') as csv_file:
   reader = csv.reader(csv_file)
   #next(reader)
   for line in reader:
      print(line)