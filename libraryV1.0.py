import os
DATAFILE = 'data.dat'
fields = ["Id", "Name", "Book", "Mobile", "Status"]
menu = ["______Library Management______", "1. Create", "2. Read", "3. Update", "4. Delete", "5. Search", "6. Exit"]
libraryList = []

def create():
	with open(DATAFILE, "w") as fileObject:
		libraryData = []
		for field in fields:
			libraryData.append(input("Enter the " + field + ": "))
		libraryList.append(libraryData)
		fileObject.write(str(libraryList))

def read():
	for field in fields:
		print(field, end = " ")
	with open(DATAFILE, "r") as fileObject:
		record = fileObject.read()
		temporaryList = eval(record)
		for lines in temporaryList:
			print("\n")
			for line in lines:
				print(line, end = " ")	

def storeTemporaryList():
	if os.stat(DATAFILE).st_size == 0:
		with open(DATAFILE, "w") as fileObject:
			emptyList = []
			fileObject.write(str(emptyList))

	else:
		with open(DATAFILE, "r") as fileObject:
			records = fileObject.read()
			if records == None:
				print("nothing")
			listFromFile = eval(records)
			for line in listFromFile:
				libraryList.append(line)


def update():
	tempId = input("Enter Id number to update: ")
	status = True
	idFound = 0
	counter = 0
	while status:
		if counter < len(libraryList):
			userId = libraryList[counter][0]
			if tempId == userId:
				print("matching successful")
				print("Select one option from the below mentioned to update.\n")
				option = int(input("1. Name\n2. Book\n3. Mobile\nEnter your option: "))
				if option == 1:
					libraryList[counter][option] = input("Enter new Name: ")
				elif option == 2:
					libraryList[counter][option] = input("Enter new Book: ")
				elif option == 3:
					libraryList[counter][option] = input("Enter new Mobile number: ")
				else: 
					print("No such option available.")
				with open(DATAFILE, "w") as fileObject:
					fileObject.write(str(libraryList))
					print("updated successfully.")
				
				idFound = 1
				break
		counter += 1
		if counter == len(libraryList):
			status = False
	if idFound == 0:
		print("Id is not found.")

def delete():
	userId = input("Enter Id number to delete: ")
	status = True
	idFound = 0
	counter = 0
	while status:
		if counter < len(libraryList):
			tempId = libraryList[counter][0]
			if tempId == userId:
				print("matching successful")
				libraryList[counter][4] = "Deleted"
				with open(DATAFILE, "w") as fileObject:
					fileObject.write(str(libraryList))
					print("Deleted successfully.")

				idFound = 1
				break
		counter += 1
		if counter == len(libraryList):
			status = False
	if idFound == 0:
		print("Id is not found.")


def search():
	tempId = input("Enter Id number to search: ")
	status = True
	idFound = 0
	counter = 0
	while status:
		if counter < len(libraryList):
			userId = libraryList[counter][0]
			if tempId == userId:
				print("matching successful")
				for line in libraryList[counter]:
					print(line, end = " ")
				print("\nsearch is successful.")

				idFound = 1
				break
		counter += 1
		if counter == len(libraryList):
			status = False
	if idFound == 0:
		print("Id is not found.")

def exitFromMenu():
	print("Thank you.")
	exit()

def showMenu():
	while True:
		print("\n")
		for menuLine in menu:
			print(menuLine)

		[create, read, update, delete, search, exitFromMenu][int(input("Enter your choice: ")) - 1]()

storeTemporaryList()
showMenu()
