import csv

infile = open('EmployeePay.csv','r')

csvfile = csv.reader(infile,delimiter = ',')

next(csvfile)

print('ID,', 'Full Name,', 'Salary,', 'Bonus,', 'Total Pay')

#salary = int(record[3])
#bonus_percentage = float(record[4])
#bonus = (salary * bonus_percentage)
#total_pay = (salary + bonus)


for record in csvfile:
    salary = float(record[3])
    bonus_percentage = float(record[4])
    bonus = (salary * bonus_percentage)
    total_pay = (salary + bonus)

    print(str(record[0])+',' + ' ' + str(record[1]) + ' ' + str(record[2])+',' + ' ' + '$'+str(salary)+',' + ' ' + '$'+str(bonus)+',' + ' ' + '$'+str(total_pay))
    #print(record[1] + record[2])
    #print(salary)
    #print(bonus)
    #print(total_pay)


    #bonus * salary + salary = total pay 