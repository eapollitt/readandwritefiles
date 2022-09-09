import csv
from statistics import mean

infile = open('steps.csv','r')

csvfile = csv.reader(infile,delimiter = ',')

outfile = open('avg_steps.csv','w')

next(csvfile)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Decemebr']
days = [31,28,31,30,31,30,31,31,30,31,30,31]
#n = 11
steps_list = []

outfile.write("Month, Average Steps\n")
for record in csvfile: 
    month = float(record[0])
    steps = float(record[1])
    #if month ==1:
        #steps_list.append(steps)
    

outfile.write(months[0] + ','+' ' + str(steps)+ '\n')
outfile.write(months[1] + ','+' ' + str(steps)+ '\n')
outfile.write(months[2] + ','+' ' + str(steps)+ '\n')
outfile.write(months[3] + ','+' ' + str(steps)+ '\n')
outfile.write(months[4] + ','+' ' + str(steps)+ '\n')
outfile.write(months[5] + ','+' ' + str(steps)+ '\n')
outfile.write(months[6] + ','+' ' + str(steps)+ '\n')
outfile.write(months[7] + ','+' ' + str(steps)+ '\n')
outfile.write(months[8] + ','+' ' + str(steps)+ '\n')
outfile.write(months[9] + ','+' ' + str(steps)+ '\n')
outfile.write(months[10] + ','+' ' + str(steps)+ '\n')
outfile.write(months[11] + ','+' ' + str(steps)+ '\n')
   # if month == 1: 
      # average = mean(steps)
      # print(average)


   # print(month)
   # print(steps)

   # print(record[0:1])
   # steps = [record[0]]
    #steps.append(record[1:2])
    #print(steps)
   # print(steps)


#January_steps = 0

#for record in csvfile:
    #month = int(record[[0],[0:30]])
    #if record[0] == 1:
        #month = 'January'
        #for record[1] in month:
           # print(record[0:])

#for record in csvfile:
    #print(record[0:0])
    #print(record[0:1])
   # print(record[0:2])
   # print(record[1:0])
   # print(record[1:1])
   # print(record[1:2])

    #January = [(record[0:30])#record[30:1]]
    #print(record[0:30])
    #print(record[0:2])
    #print([record[1:2], record[2:2]])
    #print(January)
   # while record[0] == 1: 
      # January_steps = float(record[1])
    
#print(January_steps)


#print(January_steps)        #print(record[0,1])
    #elif record [0] == 2: 
        #month = 'February'
    #print(record[1])
    #print(month)
    #January = float(record[0:0, 0:31])
    #print(January)
   # steps = float(record[1])
    #avg = (month,steps)
    #if month == 1:
        #print(sum(steps))
       # print(month,steps)
       
    
   # print(record)
   # print(record[1])

#if record[0] = 1:
   # print(record[1])
#for loop and if statement, can also use list 

outfile.close()