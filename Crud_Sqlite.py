import sqlite3
MENU_FILE = "sqlMenu.cfg"
DATABASENAME = "studentdata.db"

connection = sqlite3.connect(DATABASENAME)
cursor = connection.cursor()

def createTable():
		sql = ''' CREATE TABLE STUDENT(
		STUDENT_ID TEXT PRIMARY KEY NOT NULL,
		NAME TEXT NOT NULL,
		EMAIL TEXT,
		PHONE TEXT NOT NULL
		);
		'''
		cursor.execute(sql)
		connection.commit()
		print("Table created successfully.")

def addRecord():
	studentId = int(input("Enter student Id: "))
	name = input("Enter student Name: ")
	email = input("Enter Mail Id: ")
	mobile = input("Enter mobile number: ")
	cursor.execute("INSERT INTO STUDENT VALUES(?,?,?,?)", (studentId, name, email, mobile))
	connection.commit()
	print("Record added successfully.")

def readRecords():
	query = connection.execute("SELECT * FROM STUDENT")
	[print(record[0], record[1], record[2], record[3])for record in query]

def updateRecord():
	tempId = input("Enter Id number to update the record: ")
	query = cursor.execute("SELECT * FROM STUDENT")
	for data in query:
		if data[0] == tempId:
			print("1. NAME\n2. EMAIL ID\n3. MOBILE NUMBER\n")
			option = int(input("Select one option to update:  "))
			if option == 1:
				name =  input("Enter new Name: ")
				cursor.execute(" UPDATE STUDENT  SET NAME = ? WHERE STUDENT_ID = ?", (name, tempId))

			if option == 2:
				email = input("Enter new Mail Id: ")
				cursor.execute(" UPDATE STUDENT  SET EMAIL = ? WHERE STUDENT_ID = ?", (email, tempId))

			if option == 3:
				mobile = input("Enter new Mobile number: ")
				cursor.execute(" UPDATE STUDENT  SET PHONE = ? WHERE STUDENT_ID = ?", (mobile, tempId))

		connection.commit()


def deleteRecord():
	tempId = input("Enter Id number to delete the record: ")
	query = cursor.execute("SELECT * FROM STUDENT")
	for data in query:
		if data[0] == tempId:
			cursor.execute("DELETE FROM STUDENT WHERE STUDENT_ID =" + tempId)

		connection.commit()


def exitFromMenu():
	print("Thank you.")
	exit()


def showMenu():
	while True:
		print("\nChoose one option: ")
		print(open(MENU_FILE).read())
		[createTable, addRecord, readRecords, updateRecord, deleteRecord, exitFromMenu][int(input("Enter your choice: ")) - 1]()


showMenu()	



		



