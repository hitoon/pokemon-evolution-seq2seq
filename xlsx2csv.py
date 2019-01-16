import xlrd
import csv

def csv_from_excel():
    wb = xlrd.open_workbook('pokemon.xlsx')
    sh = wb.sheet_by_name('Evolution')
    csv_file = open('Evolution_en.csv', 'w')
    wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    csv_file.close()

csv_from_excel()
