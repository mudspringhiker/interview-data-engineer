"""
Main program for the project assignment from 
https://github.com/haystax-technology/interview-data-engineer.
"""


import csv
import json
import datetime


def main():
    csvfile = input("Name of file: ")
    try:
        data = convert_to_json(csvfile)
    except FileNotFoundError:
        print("File not found. Try again.")
    else:
        save_json(data, "output.json")
        print("Conversion complete. Output saved in 'output.json'.")


def convert_to_json(csvfile):
    """Convert data from a csv file to a list of dictionaries according to schema.json."""
    with open(csvfile) as f:
            reader = csv.DictReader(f)
            data = list(reader)

    key_map = {
                'building': 'Building',
                'person_id': 'Person Id',
                'datetime': 'Floor Access DateTime',
                'floor_level': 'Floor Level' 
    }

    json_list = []
    counter = 0
    for row in data:
        counter += 1
        line = {}
        for key in key_map:
            try:
                if key == "floor_level":
                    line[key] = int(row[key_map[key]])
                elif key == "datetime":
                    line[key] = str((datetime.datetime.strptime(row[key_map[key]], \
                        "%m/%d/%y %H:%M")).strftime("%m/%d/%y-%H:%M"))
                else:
                    line[key] = row[key_map[key]]
            except KeyError:
                print("Column does not exist.")
                
            except ValueError:
                print("Missing value at row {}.".format(counter))
                
        json_list.append(line)

    return json_list


def save_json(json_list, outputfile):
    with open(outputfile, 'w') as jsonfile:
        for line in json_list:
            json.dump(line, jsonfile)
            jsonfile.write('\n')


if __name__ == '__main__':
    main()