import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LinkedInBot:
    """
    A bot to automate LinkedIn connection requests via the 'My Network' page.
    """
    def __init__(self, email, password):
        self.email = email
        self.password = password
        # Initialize Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)

    def login(self):
        """Logs into LinkedIn using provided credentials."""
        print("Logging in...")
        self.driver.get("https://www.linkedin.com/login")
        try:
            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
            username_field.send_keys(self.email)
            
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys(self.password)
            
            # Submit the form
            password_field.submit()
            
            # Wait for the feed to load to confirm login
            self.wait.until(EC.url_contains("feed"))
            print("Login successful!")
        except Exception as e:
            print(f"Login failed: {str(e)}")
            raise

    def connect_from_network(self, n_requests):
        """
        Navigates to 'My Network' and sends connection requests.
        
        Args:
            n_requests (int): The number of connection requests to send.
        """
        print(f"Starting connection process. Target: {n_requests} requests.")
        self.driver.get("https://www.linkedin.com/mynetwork/grow/")
        
        # Allow initial page load
        time.sleep(5)

        requests_sent = 0
        
        while requests_sent < n_requests:
            # Scroll to bottom to trigger infinite scroll and load more suggestions
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            try:
                # Find all potential "Connect" buttons
                # We prioritize buttons with the specific text "Connect" inside a span, 
                # which is the common structure on the 'My Network' page.
                buttons = self.driver.find_elements(By.XPATH, "//span[text()='Connect']/ancestor::button")
                
                if not buttons:
                    print("No 'Connect' buttons visible. Scrolling...")
                    continue

                for button in buttons:
                    if requests_sent >= n_requests:
                        break
                    
                    try:
                        if not button.is_displayed() or not button.is_enabled():
                            continue

                        # Scroll element into view to ensure it's clickable
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                        time.sleep(random.uniform(0.5, 1.5))
                        
                        # Click the button
                        button.click()
                        requests_sent += 1
                        print(f"Connection request sent: {requests_sent}/{n_requests}")
                        
                        # Human-like delay to avoid flagging
                        time.sleep(random.uniform(2, 5))
                        
                    except Exception as e:
                        # Sometimes elements move or become stale, just skip them
                        continue
                        
            except Exception as e:
                print(f"Error finding buttons: {e}")
                time.sleep(2)
        
        print("Finished sending requests.")

    def close(self):
        """Closes the browser instance."""
        self.driver.quit()
