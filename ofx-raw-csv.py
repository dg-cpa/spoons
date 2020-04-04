import csv

# establishing the input file
filein = 'bankimport.csv'
data = []
date = []
description = []
amount = []

# opening the source file - filein - and reading contents
with open(filein) as f:
	reader = csv.reader(f)
	for row in reader:
		reader = data.append(row)

# dates
for i in range(1,len(data),5):
	date.append(data[i])
	
# descriptions
for i in range(2,len(data),5):
	description.append(data[i])

# amounts
for i in range(3,len(data),5):
	amount.append(data[i])

# opening and creating and output file to do some basic manipulation
with open('output.csv', 'w', newline='') as f:

	# establishing headers into the new output
	writer = csv.writer(f)
	writer.writerow(('Date','Description','Amount'))
	for i in range(len(date)):
		writer.writerow((date[i],description[i],amount[i]))


# pushed lists to CSV output
# CSV outputs start and end with [' '] by column

# establishing the input file
filein = 'output.csv'

with open(filein) as f:
	reader = csv.reader(f)

	with open('outputfinal.csv', 'w', newline='') as f:

		# establishing headers into the new output
		writer = csv.writer(f)
		writer.writerow(('Date','Description','Amount'))

		try:
			for row in reader:
				# removing the ['D and '] from the 1st value
				cleandate = row[0].replace("['D",'')
				date = cleandate.replace("']",'')
				# removing the ['P and '] from the 2nd value
				cleandescription = row[1].replace("['P",'')
				description = cleandescription.replace("']",'')
				# removing the ['T and '] from the 3rd value
				cleanamount = row[2].replace("['T",'')
				amount = cleanamount.replace("']",'')
				writer.writerow((date,description,amount))

		# simple error and exception handling  for CSV error
		except csv.Error as e:
			sys.exit('file {}, line {}: {}'.format(filein, reader.line_num, e))

