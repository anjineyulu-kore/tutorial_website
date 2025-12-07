#!/usr/bin/env python3
import json

# Load current concepts
with open("data/concepts.json", "r") as f:
    concepts = json.load(f)

# ============= SELENIUM COMPREHENSIVE GUIDE =============
selenium_content = """<h1>🌐 Selenium WebDriver - Complete & Comprehensive Guide</h1>
<p><strong>Master web automation and browser testing with detailed explanations, practical examples, step-by-step instructions, and advanced techniques.</strong></p>

<hr>

<h2>📖 1. Introduction to Selenium</h2>
<h3>What is Selenium?</h3>
<p>Selenium is a powerful open-source tool for automating web browsers. It allows you to write scripts that interact with web applications, perform automated testing, and validate functionality across different browsers and platforms.</p>

<h3>Why Use Selenium?</h3>
<ul>
<li><strong>Cross-Browser Testing:</strong> Works with Chrome, Firefox, Safari, Edge, IE</li>
<li><strong>Multiple Languages:</strong> Python, Java, C#, Ruby, JavaScript support</li>
<li><strong>Flexible Testing:</strong> Unit tests, integration tests, end-to-end tests</li>
<li><strong>Large Community:</strong> Extensive documentation and libraries</li>
<li><strong>CI/CD Integration:</strong> Works with Jenkins, Travis, GitHub Actions</li>
</ul>

<h3>Selenium Architecture</h3>
<p><strong>Client Library:</strong> Your test code (Python, Java, etc.)</p>
<p><strong>Selenium API:</strong> Commands and methods</p>
<p><strong>JSON Wire Protocol:</strong> Communication layer</p>
<p><strong>WebDriver:</strong> Browser automation interface</p>
<p><strong>Browser:</strong> Chrome, Firefox, Safari, Edge</p>

<h3>Installation</h3>
<pre><code># Install Selenium via pip
pip install selenium

# Download WebDriver
# Chrome: chromedriver from https://chromedriver.chromium.org/
# Firefox: geckodriver from https://github.com/mozilla/geckodriver
# Safari: Built-in, no download needed
# Edge: msedgedriver from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/</code></pre>

<h3>Your First Selenium Script</h3>
<pre><code>from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome driver
driver = webdriver.Chrome()

try:
    # Navigate to website
    driver.get("https://www.google.com")
    
    # Find search box
    search_box = driver.find_element(By.NAME, "q")
    
    # Type search query
    search_box.send_keys("Selenium Python")
    
    # Submit search
    search_box.submit()
    
    # Print page title
    print(driver.title)
    
finally:
    # Close browser
    driver.quit()</code></pre>

<hr>

<h2>🔧 2. Installation &amp; Setup</h2>
<h3>Step-by-Step Installation</h3>
<p><strong>Step 1:</strong> Install Python 3.6+</p>
<p><strong>Step 2:</strong> Install Selenium: <code>pip install selenium</code></p>
<p><strong>Step 3:</strong> Download WebDriver for your browser</p>
<p><strong>Step 4:</strong> Add WebDriver to PATH or specify path in code</p>

<h3>Using WebDriver Manager (Recommended)</h3>
<pre><code># Install webdriver-manager
pip install webdriver-manager

# Automatic driver management
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# No need to download manually!
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)</code></pre>

<h3>Initialize Different Browsers</h3>
<pre><code>from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

# Chrome
chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Firefox
firefox_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Safari (no service needed)
safari_driver = webdriver.Safari()

# Chrome with options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--headless")
chrome_driver = webdriver.Chrome(options=options)</code></pre>

<hr>

<h2>🖱️ 3. Basic Browser Operations</h2>
<h3>Navigation</h3>
<pre><code>driver = webdriver.Chrome()

# Navigate to URL
driver.get("https://www.example.com")

# Navigate back (browser back button)
driver.back()

# Navigate forward (browser forward button)
driver.forward()

# Refresh page
driver.refresh()

# Get current URL
current_url = driver.current_url
print(current_url)

# Get page title
title = driver.title
print(title)</code></pre>

<h3>Window Management</h3>
<pre><code># Maximize window
driver.maximize_window()

# Minimize window
driver.minimize_window()

# Set window size
driver.set_window_size(1920, 1080)

# Get window size
width = driver.get_window_size()['width']
height = driver.get_window_size()['height']

# Get window position
position = driver.get_window_position()

# Close current tab
driver.close()

# Close all tabs/windows (quit driver)
driver.quit()</code></pre>

<h3>Page Source &amp; Cookies</h3>
<pre><code># Get page source
page_source = driver.page_source

# Get page source length
source_length = len(page_source)

# Add cookie
driver.add_cookie({'name': 'my_cookie', 'value': 'cookie_value'})

# Get all cookies
all_cookies = driver.get_cookies()

# Get specific cookie
cookie = driver.get_cookie('my_cookie')

# Delete cookie
driver.delete_cookie('my_cookie')

# Delete all cookies
driver.delete_all_cookies()</code></pre>

<hr>

<h2>🔍 4. Finding Elements</h2>
<h3>Locator Strategies</h3>
<pre><code>from selenium.webdriver.common.by import By

# By ID
element = driver.find_element(By.ID, "element_id")

# By Name
element = driver.find_element(By.NAME, "element_name")

# By Class Name
element = driver.find_element(By.CLASS_NAME, "class_name")

# By CSS Selector
element = driver.find_element(By.CSS_SELECTOR, ".class > div")

# By XPath
element = driver.find_element(By.XPATH, "//div[@id='main']")

# By Link Text
element = driver.find_element(By.LINK_TEXT, "Click Here")

# By Partial Link Text
element = driver.find_element(By.PARTIAL_LINK_TEXT, "Click")

# By Tag Name
elements = driver.find_elements(By.TAG_NAME, "button")</code></pre>

<h3>Advanced XPath Examples</h3>
<pre><code>from selenium.webdriver.common.by import By

# Absolute path
xpath = "/html/body/div[1]/div/span"

# Relative path (recommended)
xpath = "//button[@id='submit']"

# By text content
xpath = "//button[text()='Submit']"

# By partial text
xpath = "//button[contains(text(), 'Submit')]"

# By attribute
xpath = "//input[@type='email']"

# Multiple conditions (AND)
xpath = "//input[@type='email' and @name='user_email']"

# Multiple conditions (OR)
xpath = "//button[text()='Submit' or text()='OK']"

# Parent element
xpath = "//button/parent::div"

# Child elements
xpath = "//div[@id='parent']/child::span"

# Following sibling
xpath = "//h1/following-sibling::p[1]"

# Preceding sibling
xpath = "//input/preceding-sibling::label"

element = driver.find_element(By.XPATH, xpath)</code></pre>

<h3>Finding Multiple Elements</h3>
<pre><code>from selenium.webdriver.common.by import By

# Find all buttons
buttons = driver.find_elements(By.TAG_NAME, "button")

# Count elements
count = len(buttons)

# Iterate through elements
for button in buttons:
    print(button.text)

# Find all inputs with specific type
email_inputs = driver.find_elements(By.XPATH, "//input[@type='email']")

# First element
first_element = driver.find_elements(By.TAG_NAME, "button")[0]

# Last element
last_element = driver.find_elements(By.TAG_NAME, "button")[-1]</code></pre>

<hr>

<h2>⌨️ 5. Interacting with Elements</h2>
<h3>Clicking Elements</h3>
<pre><code>from selenium.webdriver.common.by import By

# Simple click
button = driver.find_element(By.ID, "submit")
button.click()

# Right-click (context menu)
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
actions.context_click(button).perform()

# Double-click
actions.double_click(button).perform()</code></pre>

<h3>Typing Text</h3>
<pre><code># Send text to input field
input_field = driver.find_element(By.ID, "username")
input_field.send_keys("John Doe")

# Clear field first
input_field.clear()
input_field.send_keys("New Value")

# Typing with delays
from selenium.webdriver.common.keys import Keys
input_field.send_keys("Hello")
input_field.send_keys(Keys.TAB)  # Tab key

# Special keys
input_field.send_keys(Keys.ENTER)     # Enter
input_field.send_keys(Keys.ESCAPE)    # Escape
input_field.send_keys(Keys.BACKSPACE) # Backspace
input_field.send_keys(Keys.CONTROL + 'a')  # Ctrl+A
input_field.send_keys(Keys.CONTROL + 'c')  # Ctrl+C</code></pre>

<h3>Working with Dropdowns</h3>
<pre><code>from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

# Find dropdown element
dropdown = driver.find_element(By.ID, "country")

# Create Select object
select = Select(dropdown)

# Select by visible text
select.select_by_visible_text("United States")

# Select by value
select.select_by_value("USA")

# Select by index
select.select_by_index(0)

# Get all options
all_options = select.options
for option in all_options:
    print(option.text)

# Get selected option
selected_option = select.first_selected_option
print(selected_option.text)

# Deselect (for multi-select)
select.deselect_all()</code></pre>

<h3>Form Operations</h3>
<pre><code># Get element text
text = element.text
print(text)

# Get attribute value
href = link.get_attribute("href")
src = image.get_attribute("src")
value = input_field.get_attribute("value")

# Check if element is displayed
is_displayed = element.is_displayed()

# Check if element is enabled
is_enabled = element.is_enabled()

# Check if element is selected
is_selected = checkbox.is_selected()

# Submit form
form = driver.find_element(By.ID, "myForm")
form.submit()</code></pre>

<hr>

<h2>⏱️ 6. Waits &amp; Synchronization</h2>
<h3>Implicit Wait</h3>
<pre><code># Wait up to 10 seconds for elements to appear
driver.implicitly_wait(10)

# Any find_element call will wait up to 10 seconds
element = driver.find_element(By.ID, "dynamic_element")

# Applied globally to all find operations</code></pre>

<h3>Explicit Wait (Recommended)</h3>
<pre><code>from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Wait for element to be visible (max 10 seconds)
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "myElement"))
)

# Wait for element to be clickable
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "button"))
)

# Wait for element to be present in DOM
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "element"))
)

# Wait for specific text to appear
element = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "status"), "Done")
)</code></pre>

<h3>Common Wait Conditions</h3>
<pre><code">from selenium.webdriver.support import expected_conditions as EC

# Element is visible
EC.visibility_of_element_located((By.ID, "element"))

# Element is present in DOM
EC.presence_of_element_located((By.ID, "element"))

# Element is clickable
EC.element_to_be_clickable((By.ID, "button"))

# Element is selected
EC.element_to_be_selected((By.ID, "checkbox"))

# Text in element
EC.text_to_be_present_in_element((By.ID, "msg"), "Success")

# All elements visible
EC.visibility_of_all_elements_located((By.TAG_NAME, "button"))

# URL contains text
EC.url_contains("dashboard")

# URL matches exactly
EC.url_to_be("https://example.com")

# Number of windows
EC.number_of_windows_to_be(2)</code></pre>

<h3>Fluent Wait</h3>
<pre><code>from selenium.webdriver.support.ui import FluentWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Check every 0.5 seconds, timeout after 10 seconds
wait = FluentWait(driver)\
    .with_timeout(10)\
    .polling_every(0.5)\
    .ignoring(NoSuchElementException)

element = wait.until(
    EC.presence_of_element_located((By.ID, "element"))
)</code></pre>

<hr>

<h2>🪟 7. Windows &amp; Alerts</h2>
<h3>Handling Multiple Windows</h3>
<pre><code"># Get current window handle
current_window = driver.current_window_handle

# Get all window handles
all_windows = driver.window_handles

# Switch to new window
driver.switch_to.window(all_windows[1])

# Switch back to first window
driver.switch_to.window(all_windows[0])

# Close current window
driver.close()

# Quit all windows
driver.quit()</code></pre>

<h3>Handling Alerts</h3>
<pre><code"># Accept alert (click OK)
alert = driver.switch_to.alert
alert.accept()

# Dismiss alert (click Cancel)
alert.dismiss()

# Get alert text
alert_text = alert.text
print(alert_text)

# Type in alert (for prompt)
alert.send_keys("Input text")
alert.accept()

# Complete example
from selenium.webdriver.common.alert import Alert
try:
    # Trigger alert
    driver.find_element(By.ID, "alert_button").click()
    
    # Wait for alert
    time.sleep(1)
    
    # Handle alert
    alert = Alert(driver)
    alert.accept()
except NoAlertPresentException:
    print("No alert present")</code></pre>

<hr>

<h2>📊 8. JavaScript Execution</h2>
<h3>Execute JavaScript</h3>
<pre><code"># Execute JavaScript and return result
result = driver.execute_script("return 2 + 2;")
print(result)  # 4

# Execute JavaScript on element
element = driver.find_element(By.ID, "myElement")
driver.execute_script("arguments[0].scrollIntoView();", element)

# Set value (bypass UI)
driver.execute_script("arguments[0].value = 'new_value';", element)

# Get element property
text = driver.execute_script("return arguments[0].textContent;", element)

# Click element (JavaScript click)
driver.execute_script("arguments[0].click();", element)

# Scroll page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Get page height
height = driver.execute_script("return document.body.parentNode.scrollHeight")

<h3>Asynchronous JavaScript</h3>
<pre><code># Execute async JavaScript
# driver.execute_async_script with proper handling
time.sleep(2)  # Instead of async script</code></pre>

<hr>

<h2>📸 9. Screenshots</h2>
<h3>Taking Screenshots</h3>
<pre><code># Full page screenshot
driver.save_screenshot("page.png")

# Get screenshot as bytes
screenshot = driver.get_screenshot_as_png()

# Element screenshot
element = driver.find_element(By.ID, "myElement")
element.screenshot("element.png")</code></pre>

<hr>

<h2>🎯 10. Advanced Actions</h2>
<h3>Action Chains</h3>
<pre><code># Hover over element
element = driver.find_element(By.ID, "menu")
actions = ActionChains(driver)
actions.move_to_element(element).perform()

# Click and hold
actions.click_and_hold(element).perform()

# Release
actions.release().perform()

# Drag and drop
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
actions.drag_and_drop(source, target).perform()</code></pre>

<hr>

<h2>🧪 11. Writing Test Cases</h2>
<h3>Using unittest</h3>
<pre><code>import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):
    def setUp(self):
        # Run before each test
        self.driver = webdriver.Chrome()
    
    def tearDown(self):
        # Run after each test
        self.driver.quit()
    
    def test_valid_login(self):
        driver = self.driver
        driver.get("https://example.com/login")
        
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        
        username.send_keys("user@example.com")
        password.send_keys("password123")
        
        login_button = driver.find_element(By.ID, "login")
        login_button.click()
        
        # Assert
        self.assertIn("Dashboard", driver.title)
    
    def test_invalid_login(self):
        driver = self.driver
        driver.get("https://example.com/login")
        
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        
        username.send_keys("wrong@example.com")
        password.send_keys("wrong")
        
        login_button = driver.find_element(By.ID, "login")
        login_button.click()
        
        error = driver.find_element(By.CLASS_NAME, "error")
        self.assertTrue(error.is_displayed())

if __name__ == "__main__":
    unittest.main()</code></pre>

<hr>

<h2>✅ 12. Best Practices</h2>
<ul>
<li><strong>Use Explicit Waits:</strong> Prefer WebDriverWait over implicit waits</li>
<li><strong>Use Relative XPaths:</strong> More maintainable than absolute</li>
<li><strong>Page Object Model:</strong> Organize code into page classes</li>
<li><strong>Headless Mode:</strong> Faster test execution: <code>options.add_argument("--headless")</code></li>
<li><strong>Take Screenshots:</strong> On failures for debugging</li>
<li><strong>Handle Exceptions:</strong> Proper error handling in tests</li>
<li><strong>Clean up:</strong> Always call driver.quit()</li>
<li><strong>Use waits:</strong> Never use sleep() for synchronization</li>
</ul>

<hr>

<h2>⚠️ 13. Common Challenges &amp; Solutions</h2>
<p><strong>Challenge 1: StaleElementReferenceException</strong></p>
<p>Element is no longer attached to DOM. Solution: Re-find element after page changes</p>

<p><strong>Challenge 2: TimeoutException</strong></p>
<p>Element not found within wait time. Solution: Check locator, increase wait time, or wait for right condition</p>

<p><strong>Challenge 3: NoSuchElementException</strong></p>
<p>Element doesn't exist. Solution: Verify locator is correct, use waits</p>

<p><strong>Challenge 4: ElementNotInteractableException</strong></p>
<p>Element exists but not clickable. Solution: Scroll to element, use JavaScript click</p>

<hr>

<p style="text-align: center; margin-top: 30px;">
<strong>🎉 Selenium WebDriver Mastery Achieved!</strong><br>
You're ready to automate web browsers like a pro!
</p>
"""

# ============= ROBOT FRAMEWORK COMPREHENSIVE GUIDE =============
robot_content = """<h1>🤖 Robot Framework - Complete & Comprehensive Guide</h1>
<p><strong>Master keyword-driven test automation with detailed explanations, practical examples, and advanced techniques.</strong></p>

<hr>

<h2>📖 1. Introduction to Robot Framework</h2>
<h3>What is Robot Framework?</h3>
<p>Robot Framework is an open-source keyword-driven test automation framework for acceptance testing and acceptance test-driven development (ATDD). It's written in Python and uses a tabular syntax that's easy to read and write.</p>

<h3>Key Features</h3>
<ul>
<li><strong>Keyword-Driven:</strong> Write tests using keywords, not code</li>
<li><strong>Data-Driven:</strong> Run same test with different data</li>
<li><strong>Tabular Syntax:</strong> Easy to understand format</li>
<li><strong>Multiple Libraries:</strong> SeleniumLibrary, RequestsLibrary, Database, etc.</li>
<li><strong>Detailed Reports:</strong> HTML reports with logs</li>
<li><strong>Cross-Platform:</strong> Windows, Mac, Linux support</li>
</ul>

<h3>Installation</h3>
<pre><code"># Install Robot Framework
pip install robotframework

# Install SeleniumLibrary for web testing
pip install robotframework-seleniumlibrary

# Install RequestsLibrary for API testing
pip install robotframework-requests

# Verify installation
robot --version</code></pre>

<h3>Your First Robot Test</h3>
<pre><code">*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open Google And Search
    [Documentation]    This test opens Google and performs a search
    Open Browser    https://www.google.com    Chrome
    Input Text    name:q    Selenium Python
    Press Keys    name:q    RETURN
    Title Should Contain    Selenium Python
    Close Browser

*** Keywords ***
Open Google And Search
    [Documentation]    Custom keyword
    Open Browser    https://www.google.com    Chrome
    Close Browser</code></pre>

<hr>

<h2>🔧 2. Installation &amp; Setup</h2>
<h3>Complete Setup Guide</h3>
<pre><code"># 1. Install Python 3.6+
# 2. Install Robot Framework
pip install robotframework

# 3. Install libraries
pip install robotframework-seleniumlibrary
pip install robotframework-requests
pip install robotframework-databaselibrary

# 4. Install Selenium WebDriver (for web tests)
pip install selenium
pip install webdriver-manager

# 5. Verify installation
robot --version
rebot --version</code></pre>

<hr>

<h2>📋 3. Test Suite Structure</h2>
<h3>File Organization</h3>
<pre><code">project/
├── tests/
│   ├── login_tests.robot
│   ├── search_tests.robot
│   └── checkout_tests.robot
├── keywords/
│   ├── common.robot
│   └── ui_keywords.robot
├── resources/
│   └── variables.robot
└── results/</code></pre>

<h3>Basic Test File Structure</h3>
<pre><code">*** Settings ***
Library    SeleniumLibrary
Library    Collections
Resource   resources/variables.robot

Suite Setup       Open Browser To Login Page
Suite Teardown    Close All Browsers

*** Variables ***
${BROWSER}        Chrome
${LOGIN_URL}      https://example.com/login

*** Test Cases ***
Valid Login Test
    [Documentation]    Test valid login functionality
    [Tags]    login    smoke
    Input Username    user@example.com
    Input Password    password123
    Submit Login Form
    Welcome Page Should Be Open

Invalid Login Test
    [Documentation]    Test invalid credentials
    [Tags]    login    negative
    Input Username    wrong@example.com
    Input Password    wrong
    Submit Login Form
    Error Message Should Be Visible

*** Keywords ***
Input Username
    [Arguments]    ${username}
    Input Text    id:username    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    id:password    ${password}

Submit Login Form
    Click Button    id:login_button

Welcome Page Should Be Open
    Title Should Be    Welcome to Dashboard

Error Message Should Be Visible
    Element Should Be Visible    id:error_msg</code></pre>

<hr>

<h2>📦 4. Variables</h2>
<h3>Variable Types</h3>
<pre><code>*** Variables ***
# Scalar variables
${BROWSER}                Chrome
${LOGIN_URL}             https://example.com/login
${TIMEOUT}               5 seconds
${USERNAME}              user@example.com

# List variables
@{BROWSERS}              Chrome    Firefox    Edge
@{COLORS}                Red    Green    Blue

# Dictionary variables
&{USER_DATA}             name=John    email=john@example.com    age=30

# Variable substitution
${GREETING}              Hello ${USERNAME}!</code></pre>

<h3>Using Variables</h3>
<pre><code>*** Test Cases ***
Use Variables
    Log    ${BROWSER}
    Log Many    ${TIMEOUT}</code></pre>

<h3>Variable Scope</h3>
<pre><code">*** Test Cases ***
Global vs Local Variables
    Log    ${BROWSER}</code></pre>

<hr>

<h2>🎯 5. Keywords</h2>
<h3>Built-in Keywords</h3>
<pre><code">*** Keywords ***
Common Logging Keywords
    Log    Message to log
    Log Many    arg1    arg2    arg3
    Log List    ${list}
    Log Dictionary    ${dict}

Conditional Keywords
    Run Keyword If    ${condition}    Keyword Name    argument
    Run Keyword Unless    ${condition}    Other Keyword
    Run Keyword And Continue On Failure    Risky Keyword

Looping Keywords
    Repeat Keyword    5 times    Log    Hello
    FOR    ${item}    IN    @{ITEMS}
        Log    ${item}
    END

Wait Keywords
    Wait Until Keyword Succeeds    3x    2 seconds    Flaky Keyword
    Sleep    5 seconds</code></pre>

<h3>SeleniumLibrary Keywords</h3>
<pre><code">*** Keywords ***
Web Testing Keywords
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Close Browser
    Close All Browsers
    
    # Finding elements
    Find Element    id:element_id
    Get Element Count    xpath://button
    
    # Interacting
    Click Element    id:button
    Input Text    id:username    ${USERNAME}
    Click Button    xpath://button[@type='submit']
    
    # Assertions
    Title Should Be    Expected Title
    Page Should Contain    Expected Text
    Element Should Be Visible    id:element</code></pre>

<hr>

<h2>🌐 6. SeleniumLibrary</h2>
<h3>Web Testing with Robot + Selenium</h3>
<pre><code">*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Test Web Application
    [Setup]    Open Browser    https://example.com    Chrome
    [Teardown]    Close All Browsers
    
    # Navigation
    Get Current Url
    Reload Page
    Go Back
    
    # Finding elements
    Find Element    id:search_box
    Get WebElements    xpath://div[@class='item']
    
    # Interactions
    Type Text    id:search_box    ${SEARCH_TERM}
    Press Key    id:search_box    RETURN
    
    # Waits
    Wait Until Element Is Visible    id:results    timeout=10 seconds
    Wait Until Page Contains    ${EXPECTED_TEXT}
    
    # Assertions
    Title Should Be    Search Results
    Page Should Contain Element    xpath://div[@class='result']</code></pre>

<hr>

<h2>📡 7. RequestsLibrary (API Testing)</h2>
<h3>API Testing with Robot</h3>
<pre><code">*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    https://api.example.com
${API_KEY}     your-api-key-here

*** Test Cases ***
Get Users API Test
    Create Session    my_session    ${BASE_URL}
    ${response}=    GET On Session    my_session    /users
    Should Be Equal As Integers    ${response.status_code}    200
    
Create User Test
    Create Session    my_session    ${BASE_URL}
    &{body}=    Create Dictionary    name=John    email=john@example.com
    ${response}=    POST On Session    my_session    /users    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201

Test API With Headers
    Create Session    my_session    ${BASE_URL}
    &{headers}=    Create Dictionary    Authorization=Bearer ${API_KEY}
    ${response}=    GET On Session    my_session    /protected    headers=${headers}
    Should Be Equal As Integers    ${response.status_code}    200</code></pre>

<hr>

<h2>🔀 8. Control Structures</h2>
<h3>FOR Loops</h3>
<pre><code">*** Test Cases ***
FOR Loop Examples
    # Simple loop
    FOR    ${item}    IN    item1    item2    item3
        Log    ${item}
    END
    
    # Loop over list
    FOR    ${browser}    IN    @{BROWSERS}
        Open Browser    https://example.com    ${browser}
        Close Browser
    END
    
    # Loop with range
    FOR    ${index}    IN RANGE    10
        Log    Index: ${index}
    END
    
    # Loop with enumeration
    FOR    ${index}    ${item}    IN ENUMERATE    @{ITEMS}
        Log    ${index}: ${item}
    END</code></pre>

<h3>IF Conditions</h3>
<pre><code">*** Test Cases ***
IF Examples
    IF    ${condition}
        Log    Condition is true
    ELSE IF    ${other_condition}
        Log    Other condition is true
    ELSE
        Log    No conditions met
    END</code></pre>

<hr>

<h2>🛠️ 9. Setup &amp; Teardown</h2>
<h3>Test Fixtures</h3>
<pre><code">*** Settings ***
Library    SeleniumLibrary

Suite Setup       Setup Database Connection
Suite Teardown    Close Database Connection

Test Setup        Open Browser To Login Page
Test Teardown     Close Browser And Cleanup

*** Test Cases ***
Test 1
    [Documentation]    Runs with Test Setup/Teardown
    Log    Test content

Test 2
    [Setup]    Custom Setup For This Test
    [Teardown]    Custom Teardown For This Test
    Log    Test content

*** Keywords ***
Setup Database Connection
    Log    Opening database

Close Database Connection
    Log    Closing database

Open Browser To Login Page
    Open Browser    https://example.com/login    Chrome

Custom Setup For This Test
    Log    Custom setup</code></pre>

<hr>

<h2>▶️ 10. Test Execution</h2>
<h3>Running Tests</h3>
<pre><code"># Run all tests
robot tests/

# Run specific file
robot tests/login_tests.robot

# Run with tag
robot --include smoke tests/

# Run excluding tag
robot --exclude slow tests/

# Run with custom variable
robot --variable BROWSER:Firefox tests/

# Run with output directory
robot --outputdir results/ tests/

# Run with custom name
robot --name "Login Tests" tests/login_tests.robot

# Run in headless mode
robot --variable HEADLESS:True tests/</code></pre>

<h3>Output Files</h3>
<pre><code"># Generated files
output.xml      # Machine readable results
report.html     # HTML report with pass/fail
log.html        # Detailed logs

# View report
open report.html  # Open in browser</code></pre>

<hr>

<h2>✅ 11. Best Practices</h2>
<ul>
<li><strong>Keyword-Driven:</strong> Focus on readability, not code</li>
<li><strong>Organize Keywords:</strong> Create reusable keyword libraries</li>
<li><strong>Use Variables:</strong> Avoid hardcoding values</li>
<li><strong>Meaningful Names:</strong> Clear test and keyword names</li>
<li><strong>Detailed Logs:</strong> Use Log keywords for debugging</li>
<li><strong>Tag Tests:</strong> For selective execution (smoke, sanity, regression)</li>
<li><strong>Error Handling:</strong> Use Run Keyword And Continue On Failure</li>
<li><strong>Maintainability:</strong> Keep keywords focused and reusable</li>
</ul>

<hr>

<p style="text-align: center; margin-top: 30px;">
<strong>🎉 Robot Framework Mastery Achieved!</strong><br>
Ready to build keyword-driven test automation!
</p>
"""

# Update concepts in memory
for i, concept in enumerate(concepts):
    if concept["id"] == "selenium-webdriver":
        concepts[i]["content"] = selenium_content
        concepts[i]["updated_at"] = "2025-12-07T00:00:00Z"
    elif concept["id"] == "robot-framework":
        concepts[i]["content"] = robot_content
        concepts[i]["updated_at"] = "2025-12-07T00:00:00Z"

# Save to file
with open("data/concepts.json", "w") as f:
    json.dump(concepts, f, indent=2)

print("✅ Selenium & Robot Framework comprehensive guides created!")
print("Selenium content:", len(selenium_content), "characters")
print("Robot Framework content:", len(robot_content), "characters")
