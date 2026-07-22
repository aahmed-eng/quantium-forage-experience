import csv


with open(f'data/daily_sales_data.csv', 'r') as file:
    with open('data/final_sales_data.csv', 'w') as file2:
        file2.write('sales,date,region\n')
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[0] == 'pink morsel':
                file2.write(f'${(float(row[1][1:]) * float(row[2])) :.2f},{row[3]},{row[4]}\n')

