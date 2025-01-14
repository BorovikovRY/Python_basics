import pprint
workers = {
    "John": {"position": "Manager", "salary": 7500},
    "Brad": {"position": "Engineer", "salary": 8000},
    "Anna": {"position": "Designer", "salary": 500}
}
workers["Brad"]["salary"] = 8500
pprint.pprint(workers)