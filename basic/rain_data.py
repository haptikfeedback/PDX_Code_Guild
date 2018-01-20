import csv
import datetime

f = open('astor.rain')
f = f.replace("  ", '')
csv_f = csv.reader(f)

attendee_emails = []

for row in csv_f:
    attendee_emails.append(row[0])

print(attendee_emails)