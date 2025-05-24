# Selenium Python Test Automation

Automates browser testing for Python.org's search functionality using Selenium with Microsoft Edge.

## 📦 Project Structure
selenium-python-tutorial/
├── test_edge.py # Main test script
└── .gitignore # Ignores virtual env, screenshots, etc.


## 🛠️ Setup
1. **Install Python** (3.8+ recommended)
2. **Install dependencies**:
   ```bash
   pip install selenium

   Download Edge WebDriver

Place msedgedriver.exe in the project root
🚀 How to Run
python test_edge.py

✅ What It Tests
Submits a search query to Python.org

Verifies the search term appears in the URL

Validates the page content updates (when applicable)

📸 Screenshots
Test results are saved as:

success.png (on pass)

error.png (on failure)

🌟 Next Steps
Add more test cases

Integrate with pytest

Set up GitHub Actions for CI/CD

Created with Selenium + Edge WebDriver.
