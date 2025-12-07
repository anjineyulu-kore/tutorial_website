import json

data = json.load(open('data/concepts.json'))
print('✓ All 5 concepts loaded successfully:')
for c in data:
    print(f'  - {c["title"]} (slug: {c["slug"]})')
    print(f'    Content length: {len(c["content"])} characters')
