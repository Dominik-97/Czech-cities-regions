import csv
import json
import pandas as pd

# Path definition
CSV_path = r'../psc-list.csv'
XML_path = r'../psc-list.xml'
XLSX_path = r'../psc-list.xlsx'
JSON_path = r'../psc-list.json'

# Functions definitions
def convert_row(row):
    """
    Function to turn each row to XML

    Arguments:
        A DataFrame row
    Returns:
        XML tag
    """
    return """<psc num="%s">
    <kodcobce>%s</kodcobce>
    <nazcobce>%s</nazcobce>
    <kodobce>%s</kodobce>
    <nazobce>%s</nazobce>
    <kodokresu>%s</kodokresu>
    <nazokresu>%s</nazokresu>
    <kodkraj>%s</kodkraj>
    <nazevkraj>%s</nazevkraj>
    </psc>""" % (
    row.psc, row.kodcobce, row.nazcobce, row.kodobce, row.nazobce, row.kodokresu, row.nazokresu, row.kodkraj, row.nazevkraj)


def convert_to_xml(CSV_path, XML_path):
    """
    Function to convert the whole csv into an XML.

    Arguments:
        CSV path, XML path
    Returns:
        XML file
    """
    DF_XML = pd.read_csv(CSV_path, encoding='UTF-8', sep=',')
    XML_output = '\n'.join(DF_XML.apply(convert_row, axis=1))

    with open(XML_path, 'w', encoding='utf-8') as xmlf:
        xmlf.write(r'<?xml version="1.0" encoding="UTF-8" ?>' + 
                '\n' + 
                r'<!-- Poznámka: Seznam veškerých PSČ v České republice.. -->' +
                '\n' +
                r'<list>' +
                '\n' +
                XML_output + 
                '\n' +
                r'</list>')
        xmlf.close()


def make_json(CSV_path, JSON_path):
    """
    Function to convert the whole csv into JSON.

    Arguments:
        CSV path, JSON path
    Returns:
        JSON file
    """
    data = {}

    with open(CSV_path, encoding='UTF-8') as csvf:
        csvReader = csv.DictReader(csvf, delimiter=',')
        for rows in csvReader:
            key = rows['psc']
            data[key] = rows

    with open(JSON_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4, ensure_ascii=False))


def make_xlsx(CSV_path, XLSX_path):
    """
    Function to convert the whole csv into an Excel file.

    Arguments:
        CSV path, Excel file path
    Returns:
        Excel file
    """
    DF_XLSX = pd.read_csv(CSV_path, encoding='UTF-8', sep=',')
    DF_XLSX.to_excel(XLSX_path, index = None, header=True)


if __name__ == '__main__':
    convert_to_xml(CSV_path, XML_path)
    make_json(CSV_path, JSON_path)
    make_xlsx(CSV_path, XLSX_path)