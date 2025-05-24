from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure Edge
options = Options()
options.add_argument("--start-maximized")

# Initialize Edge
driver = webdriver.Edge(
    service=Service("msedgedriver.exe"),
    options=options
)

try:
    # Test parameters
    search_term = "Python"
    expected_url_fragment = "search"
    
    print("STEP 1: Loading Python.org...")
    driver.get("https://www.python.org")
    
    print("\nSTEP 2: Executing search...")
    search_box = driver.find_element(By.ID, "id-search-field")
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    
    print("\nSTEP 3: Automation Validation...")
    # Wait for URL to change
    WebDriverWait(driver, 10).until(
        lambda d: d.current_url != "https://www.python.org/"
    )
    
    # Validation 1: URL contains search term
    current_url = driver.current_url.lower()
    assert search_term.lower() in current_url, \
        f"Search term not in URL: {current_url}"
    print(f"✓ URL contains search term: {current_url}")
    
    # Validation 2: Search term in page
    assert search_term.lower() in driver.page_source.lower(), \
        "Search term not in page source"
    print("✓ Search term found in page HTML")
    
    # Validation 3: URL indicates search was processed
    assert expected_url_fragment in current_url, \
        f"URL doesn't contain '{expected_url_fragment}': {current_url}"
    print(f"✓ URL contains '{expected_url_fragment}'")
    
    print("\nTEST PASSED: All validations completed successfully")

except AssertionError as e:
    print(f"\nVALIDATION FAILED: {str(e)}")
    print("Current URL:", driver.current_url)
    print("Page title:", driver.title)
    driver.save_screenshot("validation_failed.png")
    print("Saved screenshot: validation_failed.png")

except Exception as e:
    print(f"\nTEST FAILED: {str(e)}")
    driver.save_screenshot("error.png")
    print("Saved screenshot: error.png")

finally:
    print("\nTest completed. Browser will close in 10 seconds...")
    time.sleep(10)
    driver.quit()