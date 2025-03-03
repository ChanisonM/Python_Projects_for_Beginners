import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet_title = sheet.title
print("active sheet title "  + sheet_title)