import csv
import json


def main():
    csvfile = 'data.csv'
    outputfile = 'output.json'
    get_json_from_csv(csvfile, outputfile)
    print("Conversion complete.")


def get_json_from_csv(csvfile, outputfile):
    """Converts a csv file to a json formatted data."""
    with open(csvfile) as cf:
        reader = csv.reader(cf)
        csvRows = list(reader)
    with open(outputfile, 'w') as jsonfile:
        for row in csvRows[1:]:
            line = {
                "title": "Floor Access Event",
                "type": "object",
                "properties": {
                    "person_id": row[0],
                    "datetime": row[1].replace(' ', '-'),
                    "floor_level": int(row[2]),
                    "building": row[3]
                },
                "required": ["person_id", "datetime", "floor_level", "building"]
            }
            json.dump(line, jsonfile)
            jsonfile.write('\n')


if __name__ == '__main__':
    main()