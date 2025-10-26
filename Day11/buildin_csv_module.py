import csv

file_name='sample.csv.csv'

with open(file_name,mode='r',newline='') as file:
    csv_reader=csv.reader(file)
    with open("output.csv",mode='w',newline='') as file:
        csv_writer=csv.writer(file)
        for row in csv_reader:
            csv_writer.writerow([row[0],row[8]])

    

sample_data=[
    ['Name','Age','City'],
    ['Alice',30,'New York'],
    ['Bob',25,'Los Angeles'],
    ['Charlie',35,'Chicago']
]

with open('sample_output.csv',mode='w',newline='') as file:
    csv_writer=csv.writer(file)
    for row in sample_data:
        csv_writer.writerow(row)    


csv.        