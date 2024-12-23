import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.LoginPage import Login

class LoginTest(unittest.TestCase):
    def setUp(self):
        """Setup before each test."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Optional, for headless execution
        self.driver = webdriver.Chrome(options=chrome_options)
        self.url = "https://dma-dev.naxa.com.np/login"
        self.login_page = Login(self.driver, self.url)

    def test_valid_login(self):
        """Test login with valid credentials."""
        self.login_page.open()
        self.login_page.enter_email("dma-dev@naxa.com")
        self.login_page.enter_password("admin@naxa##")
        self.login_page.submit()
        time.sleep(3)  # Add a wait if necessary to inspect post-login behavior

    def test_empty_login(self):
        """Test login with empty email and password fields."""
        self.login_page.open()
        self.login_page.submit()  # Submit the empty form
        time.sleep(3)  # Wait for the result

    def test_whitespace_login(self):
        """Test login with whitespace email."""
        self.login_page.open()
        self.login_page.enter_email("  ")
        self.login_page.enter_password("  ")
        self.login_page.submit()
        print("Whitespace email test executed.")
        time.sleep(3)

    def test_invalid_email(self):
        """Test login with an invalid email address."""
        random_email = self.login_page.generate_random_email()
        self.login_page.open()
        self.login_page.enter_email(random_email)
        self.login_page.enter_password("dma-admin-naxa")
        self.login_page.submit()
        time.sleep(3)

    def test_invalid_password(self):
        """Test login with invalid password."""
        random_password = self.login_page.generate_random_password()
        self.login_page.open()
        self.login_page.enter_email("dma-dev@naxa.com")
        self.login_page.enter_password(random_password)
        self.login_page.submit()
        time.sleep(3)

    def tearDown(self):
        """Teardown after each test."""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
