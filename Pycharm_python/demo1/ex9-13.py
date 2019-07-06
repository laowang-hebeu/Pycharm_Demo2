import openpyxl

wb = openpyxl.load_workbook('data.xlsx', data_only=True)

ws = wb.worksheets[0]

for row in ws.rows:
    print(row[0].value)

