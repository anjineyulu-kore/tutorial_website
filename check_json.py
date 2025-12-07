import json
try:
    with open('data/concepts.json', 'r') as f:
        data = json.load(f)
        print("JSON is valid!")
except json.JSONDecodeError as e:
    print(f"Error at line {e.lineno}, column {e.colno}: {e.msg}")
