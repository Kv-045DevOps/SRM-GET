import unittest
from app import *
import json
import requests
import responses

class parse_json_success(unittest.TestCase):
    
    def test_received_url(self):
        self.assertEqual(self.s, parse_json(self.arg1, self.arg2, self.arg3))

    @classmethod
    def setUpClass(cls):
        cls.arg1 = {'DEP': ['IT', 'Man']}
        cls.arg2 = {'Manager': 'Goose1'}
        cls.arg3 = {'Personal': 33} 
        cls.s = json.dumps({'DEP': ['IT', 'Man'], 'Manager': 'Goose1', 'Personal': 33})
    def setUp(self):
        print("\nTest for func success 'parse_json()'")
    def tearDown(self):
        print ("Finish tests for success result func 'parse_json()'")

class parse_json_failed(unittest.TestCase):
    
    def test_failed_res(self):
        self.assertNotEqual(self.s, parse_json(self.arg1, self.arg2, self.arg3))
    def test_exception_res(self):
        with self.assertRaises(Exception):
            parse_json(self.arg4) 

    @classmethod
    def setUpClass(cls):
        cls.arg1 = {'DEP': ['IT', 'Man']}
        cls.arg2 = {'Manager': 'Goose1'}
        cls.arg3 = {'Personal': 33}
        cls.arg4 = [1, "String"]
        cls.s = {'DEP': ['IT', 'Man'], 'Manager': 'Goose1', 'Personal': 33}
    def setUp(self):
        print("\nTest for func 'parse_json()'")
    def tearDown(self):
        print ("Finish tests for result func 'parse_json()'")
    
    

if __name__ == '__main__':
    unittest.main()
