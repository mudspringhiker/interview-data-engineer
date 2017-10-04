from jsonschema import validate
from schema import schema
import json

def main():
	file = "output.json"
	validate_file(file)
	print("Done validation")


def validate_file(file):
	with open(file) as f:
		data = f.read()
		data = data.split('\n')
	# 	print(len(data))
	# print(data[-2:])
	counter = 0
	for line in data:
		counter += 1
		if line:
			try:
				line_json = json.loads(line)
			except Exception as e:
				print(counter)
				print(e)
			try:
				validate(line_json, schema)
			except Exception as e:
				print(counter)
				print(e)


if __name__ == '__main__':
	main()
