import csv
MENU_FILE = "menu.cfg"
DATAFILE = "names.csv"
FIELD_FILE = 'field.cfg'
fields = eval(open(FIELD_FILE).read())
libraryList = []

def create():
	library = []
	[library.append(input("Enter the " + field + ": "))for field in fields]
	libraryList.append(library)
	with open(DATAFILE, 'w', newline = '') as csv_file:
		writer = csv.writer(csv_file)
		for line in libraryList:
			writer.writerow(line)

def read():
	with open(DATAFILE, 'r') as csv_file:
		reader = csv.reader(csv_file)
		for line in reader:
			print(line)

def update():
	tempId = input("Enter the ID to update: ")
	found = 0
	counter = -1
	with open(DATAFILE, 'r') as csv_file:
		reader = csv.reader(csv_file)
		for line in reader:
			counter += 1
			if line[0] == tempId:
				print("Select one option from the below mentioned to update.\n")
				option = int(input("1. Name\n2. Book\nEnter your option: "))
				if option == 1:
					libraryList[counter][option] = input("Enter new Name: ")
				elif option == 2:
					libraryList[counter][option] = input("Enter new book: ")
				else: 
					print("No such option available.")
				print("Match is found")
				with open(DATAFILE, 'w', newline = '') as csv_file:
					writer = csv.writer(csv_file)
					for line in libraryList:
						writer.writerow(line)

					found = 1
					print("Updated successfully")
					break
				

		if found == 0:
			print("No such Id")

def delete():
	tempId = input("Enter the ID to delete: ")
	found = 0
	counter = -1
	with open(DATAFILE, 'r') as csv_file:
		reader = csv.reader(csv_file)
		for line in reader:
			counter += 1
			if line[0] == tempId:
				libraryList[counter][-1] = 0
				print("Match is found")
				with open(DATAFILE, 'w', newline = '') as csv_file:
					writer = csv.writer(csv_file)
					for line in libraryList:
						writer.writerow(line)

					found = 1
					print("Deleted successfully")
					break
				

		if found == 0:
			print("No such Id")

def exitFromMenu():
	print("Thank you.")
	exit()

def storeTemporaryList():
	with open(DATAFILE, 'r') as csv_file:
		reader = csv.reader(csv_file)
		for line in reader:
			libraryList.append(line)



def showMenu():
	while True:
		print("\n")
		print(open("menu.cfg").read())
		[create, read, update, delete, exitFromMenu][int(input("Enter your choice: ")) - 1]()

storeTemporaryList()
showMenu()		

