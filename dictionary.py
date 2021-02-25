import requests
import json

app_id = '5b1a043f'
app_key = '8e784c217d979f4fe09052d2c6bcb71f'
word_id = input("Enter the word: ")

url ="https://od-api.oxforddictionaries.com/api/v2/entries/en-gb/" + word_id + "?strictMatch=false"
response = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
meaning = response.json();
results = meaning['results']
temp1 = results[0]
lexicalEntries = temp1['lexicalEntries']
temp2 = lexicalEntries[0]
entries = temp2['entries']
temp3 = entries[0]
senses = temp3['senses']
temp4 = senses[0]
definition = temp4['definitions']
temp4 = entries[0]['pronunciations']
audioFile = temp4[0]['audioFile']

print("Meaning of " + word_id + " : " + str(definition[0]))
print("Pronounciation link for a given word is: " + audioFile)
