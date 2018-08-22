#read a csv file
import csv
exampleFile = open('example.csv') 

exampleReader = csv.reader(exampleFile)


outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile, delimiter='\t', lineterminator='\n\n')

#outputWriter = csv.writer(outputFile)

for row in exampleReader:
	print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
	#print(str(row))
	outputWriter.writerow(row) #writes the row in a CSV file

print(f'\n\nProcessed {(exampleReader.line_num)} lines.')

# example.csv
# 4/5/2015 13:34,Apples,73
# 4/5/2015 3:41,Cherries,85
# 4/6/2015 12:46,Pears,14
# 4/8/2015 8:59,Oranges,52
# 4/10/2015 2:07,Apples,152
# 4/10/2015 18:10,Bananas,23
# 4/10/2015 2:40,Strawberries,98


# outputFile = open('output.csv', 'w', newline='')
# outputWriter = csv.writer(outputFile)
# outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
# outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
# outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()


# with open('employee_birthday.txt') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
#         line_count += 1
#     print(f'Processed {line_count} lines.')