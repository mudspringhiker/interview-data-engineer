import csv
import json
import datetime


def main():
    csvfile = 'data.csv'
    outputfile = 'output.json'
    save_json(convert_to_json(csvfile), outputfile)
    print("Conversion complete.")


def convert_to_json(csvfile):
    """Convert data from a csv file to a list of dictionaries according to schema.json."""
    with open(csvfile) as f:
        reader = csv.DictReader(f)
        json_list = []
        for row in reader:

            # json formatting making sure that keys have values if missing in csv file
            line = {}
            if row['Building']:
                line['building'] = row['Building']
            else:
                line['building'] = '99999'
            if row['Person Id']: 
                line['person_id'] = row['Person Id']
            else:
                line['person_id'] = '99999'
            
            # converting the format of datetime to "date-time" and making sure the type is string
            try:
                line['datetime'] = str((datetime.datetime.strptime(row['Floor Access DateTime'], \
                         "%m/%d/%y %H:%M")).strftime("%m/%d/%y-%H:%M"))
            except ValueError:
                line['datetime'] = '99999'
            
            # converting the value of 'floor_level' key to int
            try:
                line['floor_level'] = int(row['Floor Level'])
            except ValueError:
                line['floor_level'] = 0

            json_list.append(line)
    return json_list


def save_json(json_list, outputfile):
    with open(outputfile, 'w') as jsonfile:
        for line in json_list:
            json.dump(line, jsonfile)
            jsonfile.write('\n')


if __name__ == '__main__':
    main()