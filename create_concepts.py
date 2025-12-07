import json

concepts = [
  {
    "id": "python-basics",
    "title": "Python Programming - Complete Guide",
    "slug": "python-complete-guide",
    "created_at": "2025-01-01T00:00:00Z",
    "updated_at": "2025-01-01T00:00:00Z",
    "content": "<h1>Python - Complete Guide</h1><p>Master Python programming with comprehensive coverage of all major concepts.</p><h2>Topics Covered</h2><p>Introduction, Variables and Data Types, Operators, String Operations, Lists and Collections, Control Flow, Loops, Functions, OOP, File Handling, Exception Handling, List Comprehension, Modules, Decorators, Generators, Best Practices, Quick Reference</p><p>Each topic includes detailed explanations, code examples, and practical demonstrations.</p>"
  },
  {
    "id": "selenium-webdriver",
    "title": "Selenium WebDriver - Complete Guide",
    "slug": "selenium-webdriver-guide",
    "created_at": "2025-01-01T00:00:00Z",
    "updated_at": "2025-01-01T00:00:00Z",
    "content": "<h1>Selenium WebDriver - Complete Guide</h1><p>Master web automation and browser testing with Selenium WebDriver.</p><h2>Topics Covered</h2><p>Introduction, Installation, Basic Browser Operations, Finding Elements, Interacting with Elements, Waits and Synchronization, Windows and Alerts, JavaScript Execution, Screenshots, Advanced Actions, Test Cases, Best Practices, Common Challenges, Page Object Model, Parallel Execution</p><p>Learn to automate web applications across Chrome, Firefox, Safari, and Edge browsers.</p>"
  },
  {
    "id": "robot-framework",
    "title": "Robot Framework - Complete Guide",
    "slug": "robot-framework-guide",
    "created_at": "2025-01-01T00:00:00Z",
    "updated_at": "2025-01-01T00:00:00Z",
    "content": "<h1>Robot Framework - Complete Guide</h1><p>Master keyword-driven test automation with Robot Framework.</p><h2>Topics Covered</h2><p>Introduction, Installation, Test Suite Structure, Variables, Keywords, SeleniumLibrary, RequestsLibrary, Control Structures, Setup and Teardown, Test Execution, Best Practices, Advanced Features</p><p>Write readable tests using keyword-driven approach without extensive programming knowledge.</p>"
  },
  {
    "id": "api-testing",
    "title": "API Testing - Complete Guide",
    "slug": "api-testing-guide",
    "created_at": "2025-01-01T00:00:00Z",
    "updated_at": "2025-01-01T00:00:00Z",
    "content": "<h1>API Testing - Complete Guide</h1><p>Master REST API testing with Python and automated testing frameworks.</p><h2>Topics Covered</h2><p>Introduction, HTTP Fundamentals, Requests Library, GET/POST/PUT/PATCH/DELETE Methods, Response Validation, Authentication, Test Cases, Pytest Integration, Advanced Scenarios, API Mocking, Best Practices</p><p>Learn to test APIs efficiently with comprehensive validation and error handling techniques.</p>"
  },
  {
    "id": "playwright",
    "title": "Playwright - Complete Guide",
    "slug": "playwright-guide",
    "created_at": "2025-01-01T00:00:00Z",
    "updated_at": "2025-01-01T00:00:00Z",
    "content": "<h1>Playwright - Complete Guide</h1><p>Master modern browser automation with Playwright framework.</p><h2>Topics Covered</h2><p>Introduction, Installation, Basic Operations, Finding Elements, Interactions, Waiting and Assertions, Screenshots and Video, Network Interception, Test Framework Integration, Best Practices, Playwright vs Selenium Comparison</p><p>Build fast and reliable cross-browser tests with Chromium, Firefox, and WebKit support.</p>"
  }
]

with open('data/concepts.json', 'w') as f:
    json.dump(concepts, f, indent=2, ensure_ascii=False)
    print("✓ concepts.json created successfully")
