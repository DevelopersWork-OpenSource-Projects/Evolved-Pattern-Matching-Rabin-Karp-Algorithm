import sys
from algorithm import search
import datetime

if __name__=="__main__":
	argv = sys.argv
	if len(argv) < 3:
		print("Usage: '$","python",argv[0],"SEQUENCES_FILENAME","WORD_FILENAME'")
		exit(0)

	print()

	otus_fasta = None
	query = None
	try:
		otus_fasta = open(argv[1])
		query = open(argv[2])
	except:
		exit("ERROR WITH READING INPUT FILES")

	query = query.readline().split("\n")[0]
	# otus_fasta = open('./pattern')

	print("Key Pattern looking for",query)
	print()
	line_no = 1
	found = 0

	t1 = datetime.datetime.now()

	key = otus_fasta.readline().split("\n")[0]
	while(key):
		value = otus_fasta.readline().split("\n")[0]
		# print(key+" : "+value)
		result = search(value,query)
		# print(result)
		if result != None:
			print("key was found (Line, column):",str(line_no),result)
			found += 1
		key = otus_fasta.readline().split("\n")[0]
		line_no += 2

	t2 = datetime.datetime.now()

	print()

	print("Total Number of read:",line_no//2)

	tm = (t2 - t1)
  
	print("Total Execution Time: ",tm)