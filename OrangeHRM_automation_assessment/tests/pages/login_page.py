from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 


class LoginPage:
    # login page class to manage basic login functionality
    
    def __init__(self, driver):
        self.driver = driver
        
    def open_page(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
    def enter_username(self, username):
        self.driver.find_element(By.NAME,"username").send_keys(username)
        
    def enter_password(self, password): 
        self.driver.find_element(By.NAME,"password").send_keys(password)
    
    def click_submit(self):
        # Find and click on Submit Button (uses CSS_SELECTOR since the element is not named)
        self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
        
    def verify_login(self):
        # Verify the site has successfully logged in by checking for the user dropdown menu 
        try:
            user_dropdown = self.driver.find_element(By.CLASS_NAME,"oxd-userdropdown-tab")
            return user_dropdown.is_displayed()
        except NoSuchElementException:
            assert False, "Could not find user dropdown, likely failed to login."
    
    def login_flow(self, username, password):
        # Navigate to the website, login, and verify successful login
        
        # goto the login page
        self.open_page()
        
        # enter the username and password
        self.enter_username(username)
        self.enter_password(password)
    
        # click the Submit Button
        self.click_submit()
        
        # verify login
        self.verify_login()