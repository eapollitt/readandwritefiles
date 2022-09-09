import csv

infile = open('customers.csv','r')
outfile = open('customer_country.csv','w')

csvfile = csv.reader(infile,delimiter = ',')

#next(csvfile) #this will skip the first row
next(csvfile)

outfile.write("Full Name, Country\n")
#count = 0

#print("Full name, Country")
for record in csvfile: 
    full_name = record[1] + " " + record[2]
    country = record[4]

    outfile.write(full_name + ',' + country+ '\n')

outfile.close()
    #print(record[0:6])#prints list (square brackets)#first element is 0
    
    #print('Name:',record[1],record[2])
    #print('Country:',record[4])
    #print("Full name, Country")
    #print(record[1],record[2]+',',record[4])
    #count = count + 1
    
   # input()

#print(count)

#infile.close()