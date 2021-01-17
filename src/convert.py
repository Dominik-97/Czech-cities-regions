import csv
import json

def make_json(csvFilePath, jsonFilePath):
    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf, delimiter=';')
        for rows in csvReader:
            key = rows['PSČ']
            data[key] = rows

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4, ensure_ascii=False))

csvFilePath = r'psc-list.csv'
jsonFilePath = r'psc-list.json'

make_json(csvFilePath, jsonFilePath)
