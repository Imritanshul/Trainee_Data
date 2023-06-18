import openpyxl

workbook = openpyxl.load_workbook('Orders-With Nulls.xlsx')

# Print the tuples
sheet = workbook['Orders']  # Replace 'Sheet1' with the actual sheet name

data_tuples = []

for row in sheet.iter_rows(values_only=True):
    data_tuples.append(tuple(row))

for data_tuple in data_tuples:
    print(data_tuple)
