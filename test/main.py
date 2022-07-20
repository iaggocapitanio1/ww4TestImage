import requests
import unittest
from pathlib import Path
import json
import os

BASE_DIR = Path(__file__).resolve().parent.parent
CONTEXT_DIR = os.path.join(os.path.join(BASE_DIR, "model"), "context")
TEST_DIR = Path(__file__).resolve().parent


# class TestRequests(unittest.TestCase):
#     URL_JSONLD = "http://localhost:3004/json-context.jsonld"
#     URL_NGSILD = "http://localhost:3004/ngsi-context.jsonld"
#     URL_NGSILD_ORION = "http://localhost:1026/ngsi-ld/v1/"
#     PATH_JSONLD = os.path.join(CONTEXT_DIR, "json-context.jsonld")
#     PATH_NGSILD = os.path.join(CONTEXT_DIR, "ngsi-context.jsonld")
#
#     def test_context_content(self):
#         response_jsonld = requests.get(url=self.URL_JSONLD)
#         response_ngsild = requests.get(url=self.URL_NGSILD)
#         with open(self.PATH_JSONLD) as file:
#             data = json.load(file)
#             self.assertEqual(data, response_jsonld.json())
#         with open(self.PATH_NGSILD) as file:
#             data = json.load(file)
#             self.assertEqual(data, response_ngsild.json())
#
#     def test_context_status_code(self):
#         response_jsonld = requests.get(url=self.URL_JSONLD)
#         response_ngsild = requests.get(url=self.URL_NGSILD)
#         self.assertEqual(response_jsonld.status_code, 200)
#         self.assertEqual(response_ngsild.status_code, 200)
#
#     def test_orion_version(self):
#         response = requests.get(url="http://localhost:1026/version")
#         self.longMessage = True
#         self.assertEqual(response.json().get("orionld version"),
#                          "1.0.0", "orion version did not match!")
#
#     def test_create_client(self):
#         url = self.URL_NGSILD_ORION + "entities/"
#         headers = {
#             'Content-Type': 'application/ld+json',
#             'Fiware-Service': 'woodwork40',
#             'Cookie': 'connect.sid=s%3ArRPMJqXnaF0Qi9E9eHrgQSIDMSy9gdPl.sx%2F8wrUpZt%2FQHmrIvapRyAILqTy7Xc6OfqT%2FMdP'
#                       '%2BrUA '
#         }
#
#         with open(os.path.join(TEST_DIR, "client_payload.json")) as file:
#             data = json.load(file)
#             response = requests.post(url=url, headers=headers, data=data)
#             print(response)
#         print(data)


if __name__ == "__main__":
   # unittest.main()
   import requests
   import json

   url = "http://localhost:1026/ngsi-ld/v1/entities"

   payload = json.dumps({
       "id": "urn:ngsi-ld:Owner:001",
       "type": "Owner",
       "clientTypeInstitution": {
           "type": "Property",
           "value": "Institucional"
       },
       "legalName": {
           "type": "Property",
           "value": "Mayer Interiors"
       },
       "address": {
           "type": "Property",
           "value": "171 Rue St Sauveur, 06110 Le Cannet"
       },
       "email": {
           "type": "Property",
           "value": "contact@mayerinteriors.com"
       },
       "telephone": {
           "type": "Property",
           "value": "+33 (0) 4 92 92 92 96"
       },
       "hasOrganization": {
           "type": "Relationship",
           "object": "urn:ngsi-ld:Mofreita"
       },
       "@context": [
           "https://raw.githubusercontent.com/More-Collaborative-Laboratory/ww4zero/main/ww4zero.context.normalized.jsonld"
       ]
   })
   headers = {
       'Content-Type': 'application/ld+json',
       'Fiware-Service': 'woodwork40',

   }
   print(type(payload))
   response = requests.request("POST", url, headers=headers, data=payload)

   print(response.text)
   print(response)
   with open(os.path.join(TEST_DIR, "client_payload.json")) as file:
       data = json.load(file)
       response = requests.post(url=url, headers=headers, data=json.dumps(data))
       print(response)
       print(response.text)
