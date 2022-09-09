import csv

infile = open('customers.csv','r')

csvfile = csv.reader(infile, delimiter = ',')

next(csvfile) #this will skip the first row

for record in csvfile: 
    #print(record[0:6])#prints list (square brackets)#first element is 0
    print('ID:',record[0])
    print('Fname:',record[1])
    print('Lname:',record[2])
    print('City:',record[3])
    print('Country:',record[4])
    print('Phone:',record[5])
    
    input()