import csv

# establishing the input file
filein = 'ccofxreformat.csv'

# opening the source file - filein - and reading contents
with open(filein) as f:
	reader = csv.reader(f)

	# opening and creating and output file to do some basic manipulation
	with open('output.csv', 'w', newline='') as f:

		# establishing headers into the new output
		writer = csv.writer(f)
		writer.writerow(('Date','Description','Amount'))

		try:
			for row in reader:
				# removing the leading D from the 1st value
				date = row[0].replace('D','')
				# removing the leading P from the 3rd value
				description = row[2].replace('P','')
				# removing the leading T from the 5th value
				amount = row[4].replace('T','')
				# leaving the original dataset intact and writing clean data to output row
				writer.writerow((date,description,amount))

		# simple error and exception handling  for CSV error
		except csv.Error as e:
			sys.exit('file {}, line {}: {}'.format(filein, reader.line_num, e))
