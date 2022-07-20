import requests
import unittest
from pathlib import Path
import json
import os
BASE_DIR = Path(__file__).resolve().parent.parent
CONTEXT_DIR = os.path.join(os.path.join(BASE_DIR, "model"), "context")


class TestRequests(unittest.TestCase):
    URL_JSONLD = "http://localhost:3004/json-context.jsonld"
    URL_NGSILD = "http://localhost:3004/ngsi-context.jsonld"
    PATH_JSONLD = os.path.join(CONTEXT_DIR, "json-context.jsonld")
    PATH_NGSILD = os.path.join(CONTEXT_DIR, "ngsi-context.jsonld")

    def test_context_content(self):
        response_jsonld = requests.get(url=self.URL_JSONLD)
        response_ngsild = requests.get(url=self.URL_NGSILD)
        with open(self.PATH_JSONLD) as file:
            data = json.load(file)
            self.assertEqual(data, response_jsonld.json())
        with open(self.PATH_NGSILD) as file:
            data = json.load(file)
            self.assertEqual(data, response_ngsild.json())

    def test_context_status_code(self):
        response_jsonld = requests.get(url=self.URL_JSONLD)
        response_ngsild = requests.get(url=self.URL_NGSILD)
        self.assertEqual(response_jsonld.status_code, 200)
        self.assertEqual(response_ngsild.status_code, 200)


if __name__ == "__main__":
   unittest.main()
