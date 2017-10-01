import csv
import json
from schema import schema


def main():
    csvfile = 'data.csv'
    outputfile = 'output.json'
    convert_to_json(csvfile, outputfile)
    print("Conversion complete.")


def convert_to_json(csvfile, outputjson, schema=schema):
    with open(csvfile) as f:
        reader = csv.DictReader(f)
        
        with open(outputjson, 'w') as jsonfile:
            for row in reader:
                schema['properties'] = {
                    'building': row['Building'],
                    'datetime': row['Floor Access DateTime'].replace(' ', '-'),
                    'floor_level': int(row['Floor Level']),
                    'person_id': row['Person Id']}
                json.dump(schema, jsonfile)
                jsonfile.write('\n')


if __name__ == '__main__':
    main()