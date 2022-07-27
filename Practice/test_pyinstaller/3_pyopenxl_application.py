import openpyxl
import time

excelFile = openpyxl.load_workbook('3_some_excel_data.xlsx')
sheet = excelFile.active
data = []
for i in range(10):
    for j in range(10):
        data.append(sheet.cell(row=i+1, column=j+1).value)

print(data)
time.sleep(10)