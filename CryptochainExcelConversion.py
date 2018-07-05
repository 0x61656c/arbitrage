import xlsxwriter

def writetoExcel(filename, data, row = 1, col = 1):
    
    workbook = xlsxwriter.Workbook('%s.xlsx' %filename)
    worksheet = workbook.add_worksheet()
    
    #writes data to spreadsheet
    for item in data:
        worksheet.write(row, col, item)
        row += 1
        
    #closes spreadsheet session
    workbook.close()
    