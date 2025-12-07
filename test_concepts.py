import json

try:
    with open('data/concepts.json', 'r') as f:
        concepts = json.load(f)
    
    print("✓ All {} concepts loaded successfully:".format(len(concepts)))
    for concept in concepts:
        print("  - {} (slug: {})".format(concept['title'], concept['slug']))
    
except Exception as e:
    print("✗ Error loading concepts: {}".format(e))
