#!/usr/bin/python
# coding: utf-8

import email
import smtplib
import sys
import csv

# Capture stdin message via pipe
msg = email.message_from_file(sys.stdin)

# list with sellers or emails for distribution
sellers = [('Seller 01', 'seller01@domain.com'),
           ('Seller 02', 'seller02@domain.com')]

# Check the size of the vendor list
totalSellers = len(sellers)

# Get the last seller that received email
lastSeller = open('lastseller.txt', 'r').read()  # use the full path of file

# Determines the next seller who will receive email
nextSeller = 0 if int(lastSeller) == totalSellers - 1 else int(lastSeller) + 1
currentSeller = str(nextSeller)

with open('lastseller.txt', 'w') as fvend:
    fvend.write(currentSeller)
# Check if you have an email for reply
emailContact = msg['reply-to'] or msg['from']
# writes log to csv
with open('emails.csv', 'a') as fcsv:  # use the full path of file
    mailwriter = csv.writer(fcsv, delimiter=';')
    mailwriter.writerow(
        [msg['date'], msg['subject'], emailContact,
         sellers[nextSeller][0]])

# Forward the email to the seller of the time.
s = smtplib.SMTP('localhost')
s.sendmail("sellers@domain.com", sellers[nextSeller][1],
           msg.as_string())
s.quit()
