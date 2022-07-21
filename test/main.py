import requests
import unittest
from pathlib import Path
import json
import os

BASE_DIR = Path(__file__).resolve().parent.parent
CONTEXT_DIR = os.path.join(os.path.join(BASE_DIR, "model"), "context")
TEST_DIR = Path(__file__).resolve().parent


def create_entity(path: str, url: str) -> requests.models.Response:
    headers = {'Content-Type': 'application/ld+json', 'Fiware-Service': 'woodwork40'}
    with open(path) as file:
        data = json.load(file)
        payload = json.dumps(data)
        response = requests.post(url=url, headers=headers, data=payload)
    return response


class TestRequests(unittest.TestCase):
    URL_JSONLD = "http://localhost:3004/json-context.jsonld"
    URL_NGSILD = "http://localhost:3004/ngsi-context.jsonld"
    URL_NGSILD_ORION = "http://localhost:1026/ngsi-ld/v1/"
    URL_NGSILD_ORION_ENTITIES = URL_NGSILD_ORION + "entities/"
    PATH_JSONLD = os.path.join(CONTEXT_DIR, "json-context.jsonld")
    PATH_NGSILD = os.path.join(CONTEXT_DIR, "ngsi-context.jsonld")

    def assert_status_code(self, response: requests.models.Response, *codes):
        result = False
        for code in codes:
            if response.status_code == code:
                result = True or result
            else:
                result = False or result
        return self.assertTrue(result)

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

    def test_orion_version(self):
        response = requests.get(url="http://localhost:1026/version")
        self.longMessage = True
        self.assertEqual(response.json().get("orionld version"),
                         "1.0.0", "orion version did not match!")

    def test_create_client(self):
        self.assert_status_code(create_entity(path=os.path.join(TEST_DIR, "client_payload.json"),
                                              url=self.URL_NGSILD_ORION_ENTITIES), 201, 409)

    def test_create_project(self):
        self.assert_status_code(create_entity(path=os.path.join(TEST_DIR, "project_payload.json"),
                                              url=self.URL_NGSILD_ORION_ENTITIES), 201, 409)

    def test_create_part(self):
        self.assert_status_code(create_entity(path=os.path.join(TEST_DIR, "part_payload.json"),
                                              url=self.URL_NGSILD_ORION_ENTITIES), 201, 409)

if __name__ == "__main__":
    unittest.main()
