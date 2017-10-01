import csv
import json


def main():
    csvfile = 'data.csv'
    outputfile = 'output.json'
    convert_to_json(csvfile, outputfile)
    print("Conversion complete.")


def convert_to_json(csvfile, outputjson):
    with open(csvfile) as f:
        reader = csv.DictReader(f)
        
        with open(outputjson, 'w') as jsonfile:
            for row in reader:
                line = {}
                line['building'] = row['Building']
                line['datetime'] = row['Floor Access DateTime'].replace(' ', '-')
                try:
                    line['floor_level'] = int(row['Floor Level'])
                except ValueError:
                    line['floor_level'] = row['Floor Level']
                line['person_id'] = row['Person Id']
                
                json.dump(line, jsonfile)
                jsonfile.write('\n')


if __name__ == '__main__':
    main()