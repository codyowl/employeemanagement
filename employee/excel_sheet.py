import xlrd

loc = ("Assesment Data Model.xlsx")       

wb = xlrd.open_workbook(loc)  

sheet = wb.sheet_by_index(1)

columns = sheet.ncols

for c in range(len(columns)):
	for i in range(sheet.nrows): 
		print(sheet.cell_value(i, c))  