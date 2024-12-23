from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

class Login:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """Open the login page."""
        self.driver.get(self.url)

    def _wait_for_element(self, by, value, timeout=10):
        """Wait for an element to be present."""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def enter_email(self, email):
        """Enter email into the email input field."""
        email_field = self._wait_for_element(By.CSS_SELECTOR, "input#email")
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        """Enter password into the password input field."""
        password_field = self._wait_for_element(By.CSS_SELECTOR, "input#password")
        password_field.clear()
        password_field.send_keys(password)

    def submit(self):
        """Submit the login form."""
        submit_button = self._wait_for_element(By.CSS_SELECTOR, "[type='submit']")
        submit_button.click()

    def get_error_message(self):
        """Get error message after login attempt (if exists)."""
        return self._wait_for_element(By.CSS_SELECTOR, "div.error-message").text

    def generate_random_email(self):
        """Generate a random email address."""
        local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        domain = "example.com"
        return f"{local_part}@{domain}"

    def generate_random_password(self, length=8):
        """Generate a random password of specified length."""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))
