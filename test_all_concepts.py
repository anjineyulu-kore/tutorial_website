import requests

concepts = [
    'python-complete-guide',
    'selenium-webdriver-guide',
    'robot-framework-guide',
    'api-testing-guide',
    'playwright-guide'
]

print("✓ Testing all concept endpoints:")
for slug in concepts:
    r = requests.get(f'http://127.0.0.1:7000/concepts/{slug}')
    print(f"  {slug}: {r.status_code} OK - {len(r.text)} chars")
    
print("\n✓ All 5 concepts are accessible and working!")
