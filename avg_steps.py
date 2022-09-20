import csv
from statistics import mean

infile = open('steps.csv','r')

csvfile = csv.reader(infile,delimiter = ',')

outfile = open('avg_steps.csv','w')

next(csvfile)


days = [31,28,31,30,31,30,31,31,30,31,30,31]
#n = 11
steps_list = []

outfile.write("Month,Steps\n")
monthNames = ['','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Decemebr']


totalSteps = 0
month = 1
dayCount = 0

next(csvfile)

for rec in csvfile: 
    if int(rec[0]) == month: 
        totalSteps += int(rec[1])
        dayCount += 1
    else: 
        avgSteps = round(totalSteps/dayCount,2)
        outfile.write(monthNames[month]+','+str(avgSteps)+'\n')
        totalSteps = int(rec[1])
        dayCount = 1
        month += 1

avgSteps = round(totalSteps/dayCount,2)   #these two steps are for december 
outfile.write(monthNames[month]+','+str(avgSteps)+'\n')


outfile.close()