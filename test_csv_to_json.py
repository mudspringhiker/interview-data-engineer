import unittest
from csv_to_json import convert_to_json


class JsonTestCase(unittest.TestCase):
	"""Tests for csv_to_json.py."""

	def test_json_format(self):
		"""Is the json formatting correct and that 
		the values are filled as required in schema?"""
		json_list = convert_to_json('data_test1.csv')
		expected_list = [
				{
				  	"building": "B", 
					 "datetime": "10/01/15-08:02", 
					 "floor_level": 6, 
					 "person_id": "1"
				},
				{
				  	"building": "B", 
					 "datetime": "10/01/15-08:02", 
					 "floor_level": 6, 
					 "person_id": "99999"
				},
				{
				  	"building": "99999", 
					 "datetime": "10/01/15-08:02", 
					 "floor_level": 6, 
					 "person_id": "3"
				}
			]
		self.assertEqual(json_list, expected_list)


	def test_floor_level(self):
		"""Is floor level properly converted and 
		have a value if missing in original file?"""
		json_list = convert_to_json('data_test2.csv')
		expected_list = [
				{
					"building": "B",
					"datetime": "10/01/15-08:02",
					"floor_level": 0,
					"person_id": "1"
				}
			]
		self.assertEqual(json_list, expected_list)


	def test_datetime_format(self):
		"""Is datetime format properly converted and
		have a value if missing in original file?"""
		json_list = convert_to_json('data_test3.csv')
		expected_list = [
				{
					"building": "B",
					"datetime": "99999",
					"floor_level": 6,
					"person_id": "1"	
				},
				{
					"building": "B",
					"datetime": "99999",
					"floor_level": 6,
					"person_id": "2"	
				}
			]
		self.assertEqual(json_list, expected_list)


unittest.main()