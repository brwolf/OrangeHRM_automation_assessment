from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class AddUserPage:
    # Add user page class 
    
    # Most elements have no id or name so I'm using CSS_SELECTORs for almost everything. This is non-ideal as the script is fragile to changes on the website. I would be asking my dev team to spend some time to add identifiers to most of these interactable elements. 
    
    def __init__(self, driver):
        self.driver = driver
        
    def select_user_role(self, role):
        # selects the user role from the dropdown.
        
        # user_role dropdown is a non-standard dynamic element, normal webdriver Select functionality doesn't work on it. 
        # I would perfer to select by the text of the elements rather than the CSS_SELECTOR of the position, but while I was testing the site someone kept changing the display language making that unreliable. 
        if role == "Admin":
            dropdown_item = "div.oxd-select-option:nth-child(2) > span:nth-child(1)"
        elif role == "ESS":
            dropdown_item = "div.oxd-select-option:nth-child(3) > span:nth-child(1)"
        else:
            # fail the test with a helpful error if given an invalid role
            assert False, f'Script Error! Invalid User Role selection! Given "{role}", accept "Admin" or "ESS".'
        
        # Click the dropdown to open it    
        self.driver.find_element(By.CSS_SELECTOR,"form > div:nth-child(1) > div > div:nth-child(1) > div > div:nth-child(2) > div").click()
        
        # Click the element of the dropdown that we want
        self.driver.find_element(By.CSS_SELECTOR,dropdown_item).click()

    def enter_employee_name(self, employee_name):
        # enters the employee name
        
        # The Employee Name input only allows names already in the DB and does not accept just typing into the field. The name MUST be selected from the dropdown after it searches the DB for it.
        
        self.driver.find_element(By.CSS_SELECTOR,"form > div:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(2) > div > div > input").send_keys(employee_name)
        
        # wait a bit for it to finish searching. 
        time.sleep(2)
        
        # click the first element of the dropdown
        self.driver.find_element(By.CSS_SELECTOR,".oxd-autocomplete-option").click()
    
    def select_status(self, status):
        # selects the status
        
        # status dropdown is a non-standard dynamic element, normal webdriver Select functionality doesn't work on it. 
        # I would perfer to select by the text of the elements rather than the CSS_SELECTOR of the position, but while I was testing the site someone kept changing the display language making that unreliable. 
        
        if status == "Enabled":
            dropdown_item = "div.oxd-select-option:nth-child(2) > span:nth-child(1)"
        elif status == "Disabled":
            dropdown_item = "div.oxd-select-option:nth-child(3) > span:nth-child(1)"
        else:
            # fail the test with a helpful error if given an invalid status
            assert False, f'Script Error! Invalid Status selection! Given "{status}", accept "Enabled" or "Disabled".'
        
        # Click the dropdown to open it   
        self.driver.find_element(By.CSS_SELECTOR,"div.oxd-grid-item:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)").click()
        
        # Click the element of the dropdown that we want
        self.driver.find_element(By.CSS_SELECTOR,dropdown_item).click()
        
        
    def enter_username(self, username):
        # enters the username
        
        username_input = self.driver.find_element(By.CSS_SELECTOR,"div:nth-child(1) > div > div:nth-child(4) > div > div:nth-child(2) > input")
        username_input.send_keys(username)
        
    def enter_password(self, password):
        # enters the password into both input boxes
        
        password_input = self.driver.find_element(By.CSS_SELECTOR,"div.oxd-form-row.user-password-row > div > div.oxd-grid-item.oxd-grid-item--gutters.user-password-cell > div > div:nth-child(2) > input")
        password_input.send_keys(password)
        
        password_verify_input = self.driver.find_element(By.CSS_SELECTOR,"div.oxd-form-row.user-password-row > div > div:nth-child(2) > div > div:nth-child(2) > input")
        password_verify_input.send_keys(password)
    
    def click_save_button(self):
        # clicks the save button on the add user form
        self.driver.find_element(By.CSS_SELECTOR,"button.oxd-button:nth-child(3)").click()
    
    def add_test_user(self, username, role, status):    
        # fills all the fields to add a new employee
        # dummy data we don't care about for the test
        employee_name = "FName Mname LName"
        password = "testpassword1"
        
        self.select_user_role(role)
        self.enter_employee_name(employee_name)        
        self.enter_username(username)
        self.select_status(status)
        self.enter_password(password)        
        
    def verify_add_user_panel(self):
        # Verify that the page is in the add user panel
        
        if self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser":
            return True
        else:
            assert False, "Navigation Failed! Not on the add user page." 