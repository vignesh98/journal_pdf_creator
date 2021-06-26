#!/usr/bin/python3

import datetime
import sys
import getpass

from fpdf import FPDF


try:
    year = sys.argv[1]
except:
    print("Year as an arg not received , Please try './journal_creator.py <yearname>'\nFor Example: ./journal_creator.py 2050")
    sys.exit("\n-E-:Error ==> Argument not recieved, Exiting.....")

try:
    start = datetime.datetime.strptime("01-01-"+str(int(sys.argv[1])), "%d-%m-%Y")
    end = datetime.datetime.strptime("01-01-"+str(int(sys.argv[1])+1), "%d-%m-%Y")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
except Exception as e:
    print("Encountered error ==> "+e+"\n")
    sys.exit("Exiting....")


count=0
lt = []
for date in date_generated:
    count +=1
    lt.append(date.strftime("%d %B %Y , %A %d-%m-%Y "))

print("Creating Journal with "+str(count)+" days.....\n")

pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
pdf.add_page()
pdf.set_font("Times", size = 16)
pdf.set_text_color(0,0,255)
pdf.cell(0,100,txt="Journal for "+sys.argv[1],align = "C")
pdf.set_text_color(0,0,0)

for x in lt:
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    pdf.cell(200, 10, txt = x, 
            ln = 1)
    pdf.cell(200, 10, txt = "------------------------------------------------------------------------------------------------------------",
            ln = 2, align = 'L')

try:
    pdf.output(sys.argv[1]+"_Journal_"+getpass.getuser()+".pdf")
except Exception as e:
    print("Cannot get System Username, ignoring ....")
    pdf.output(sys.argv[1]+"_Journal_.pdf")
print("Journal PDF generated..... :)")