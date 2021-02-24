import os
MENU_FILE = "menu.cfg"
DATAFILE = "data2.txt"
FIELD_FILE = 'field.cfg'
fields = eval(open(FIELD_FILE).read())
libraryList = []

def create():
	
	libraryData = []
	[libraryData.append(input("Enter the " + field + ": "))for field in fields]	
	libraryList.append(libraryData)
	with open(DATAFILE, "w") as fileObject:
		fileObject.write(str(libraryList))

def read():
	for field in fields:
		print(field, end = " ")
	tempList = eval(open(DATAFILE, "r").read())
	for lines in tempList:
		print("\n")
		for line in lines:
			print(line, end = " ")

def storeTemporaryList():
	if os.stat(DATAFILE).st_size == 0:
		emptyList = []
		with open(DATAFILE, "w") as fileObject:
			fileObject.write(str(emptyList))
	else:
		[libraryList.append(line) for line in eval(open(DATAFILE).read())]
		

def update():
	tempId = input("Enter Id number to update: ")
	status = True
	idFound = 0
	counter = 0
	while status:
		if counter < len(libraryList):
			userId = libraryList[counter][0]
			if tempId == userId:
				print("Select one option from the below mentioned to update.\n")
				option = int(input("1. Name\n2. Book\n3. Mobile\nEnter your option: "))
				if option == 1:
					libraryList[counter][option] = input("Enter new Name: ")
				elif option == 2:
					libraryList[counter][option] = input("Enter new book: ")
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
				for field in fields:
					print(field, end = " ")
				print("\n")
				for line in libraryList[counter]:
					print(line, end = " ")
				print("\nSearch is successful.")

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
		print(open("menu.cfg").read())
		[create, read, update, delete, search, exitFromMenu][int(input("Enter your choice: ")) - 1]()

storeTemporaryList()
showMenu()
