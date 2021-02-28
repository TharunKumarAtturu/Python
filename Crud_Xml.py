import os
import xml.etree.ElementTree as xml
DATAFILE = "data.xml"
MENU_FILE = "menu.cfg"

def getRoot():
	if os.stat(DATAFILE).st_size == 0:
		root = xml.Element('bank')
		tree = xml.ElementTree(root)
		with open(DATAFILE,"wb") as f:
			tree.write(f)
	else:
		tree = xml.parse(DATAFILE)
		root = tree.getroot()
		return root
	
root = getRoot()


def create():
	child = xml.Element("customer")
	root.append(child)
	Id = xml.SubElement(child, "Id")
	Id.text = input("Enter Account Number: ")
	Name = xml.SubElement(child, 'Name')
	Name.text = input("Enter Name: ")
	Balance = xml.SubElement(child, 'Balance')
	Balance.text = input("Enter Balance: ")
	Status = xml.SubElement(child, 'Status')
	Status.text = input("Enter Status: ")
	tree = xml.ElementTree(root)
	with open(DATAFILE,"wb") as f:
		tree.write(f)

def read():
	mytree = xml.parse(DATAFILE)
	root = mytree.getroot()
	for x in root.findall('customer'):
		Id = x.find('Id').text
		Name = x.find('Name').text
		Balance = x.find('Balance').text
		Status = x.find('Status').text
		if Status == "1":
			print(Id, Name, Balance, Status)	

def update():
	found = 0
	givenId = input("Enter id to update: ")
	mytree = xml.parse(DATAFILE)
	root = mytree.getroot()
	for x in root.findall('customer'):
		Id = x.find('Id').text
		if Id == givenId:
			print("Match found")
			print("Choose one option from below to update.")
			print("1.Name\n2.Balance")
			option = int(input("Enter option: "))
			if option == 1:
				Name = x.find('Name')
				Name.text = input("Enter new name: ")
				found = 1
			if option == 2:
				Balance = x.find('Balance')
				Balance.text = input("Enter new balance: ")
				found = 1

			tree = xml.ElementTree(root)
			with open(DATAFILE, "wb") as fileObject:
				tree.write(fileObject)
			print("Updated successfully!")
			break
	if found == 0:
		print("ID not found!")

def delete():
	found = 0
	givenId = input("Enter id to delete: ")
	mytree = xml.parse(DATAFILE)
	root = mytree.getroot()
	for x in root.findall('customer'):
		Id = x.find('Id').text
		if Id == givenId:
			print("Match found")
			Status = x.find('Status')
			Status.text = str(0)
			found = 1
			tree = xml.ElementTree(root)
			with open(DATAFILE, "wb") as fileObject:
				tree.write(fileObject)
			print("Deleted successfully!")
			break
	if found == 0:
		print("ID not found!")
			

def exitFromMenu():
	print("Thank you.")
	exit()


def showMenu():
	while True:
		print("\n")
		print(open("menu.cfg").read())
		[create, read, update, delete, exitFromMenu][int(input("Enter your choice: ")) - 1]()


showMenu()	

