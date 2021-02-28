import csv
import json
import xmltodict
import xml.etree.ElementTree as xml
XML_DATAFILE = "data.xml"
CSV_DATAFILE = "data.csv"
JSON_DATAFILE = "data.json"
MENU_FILE = "exportMenu.cfg"

fields = ["Id", "Name", "Balance", "Status"]
records = [] 

def convertXmlToCsv():
	mytree = xml.parse(DATAFILE)
	root = mytree.getroot()
	for x in root.findall('customer'):
		Id = x.find('Id').text
		Name = x.find('Name').text
		Balance = x.find('Balance').text
		Status = x.find('Status').text
		records.append([Id, Name, Balance,Status])

	with open(CSV_DATAFILE, 'w', newline = '') as csv_file:
		writer = csv.writer(csv_file)
		[writer.writerow(record)for record in records]
	print("Successfully exported from XML to CSV")




def convertXmlToJson():
	
	with open(XML_DATAFILE) as xmlFile:
		data_dict = xmltodict.parse(xmlFile.read())
	json_data = json.dumps(data_dict)
	with open (JSON_DATAFILE, "w") as f:
		f.write(json_data)
	print("Successfully exported from XML to JSON.")


def exitFromMenu():
	print("Thank you.")
	exit()


def showMenu():
	while True:
		print("\nChoose export option: ")
		print(open(MENU_FILE).read())
		[convertXmlToCsv,convertXmlToJson, exitFromMenu][int(input("Enter your choice: ")) - 1]()


showMenu()	

