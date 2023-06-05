import gspread
import csv
import sys

gs = gspread.service_account()
sheet_name = sys.argv[1]

sheet = gs.open("YGO Deck DB")
worksheet = sheet.worksheet(sheet_name)

with open(f'decks/{sheet_name.lower().replace(" ", "_")}.csv', 'w') as csv_f:
    csv.writer(csv_f).writerows(worksheet.get_all_values())
