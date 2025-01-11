from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:
    # Admin page class 
    
    # Most elements have no id or name so I'm using CSS_SELECTORs for almost everything. This is non-ideal as the script is fragile to changes on the website. I would be asking my dev team to spend some time to add identifiers to most of these interactable elements. 
    
    def __init__(self, driver):
        self.driver = driver
    
    def open_page(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    
    def click_admin_page(self):
        # clicks the Admin button on the side panel 
        self.driver.find_element(By.CSS_SELECTOR,"div.oxd-sidepanel-body > ul > li:nth-child(1)").click()
        
    def click_add_user(self):
        # clicks the Add button to add a new user
        #self.driver.find_element(By.CSS_SELECTOR,"div.orangehrm-paper-container > div.orangehrm-header-container > button").click()
        self.driver.find_element(By.CSS_SELECTOR,"button.oxd-button--secondary:nth-child(1)").click()
           
    def enter_search_username(self, username):
        # enter the username into the search box on the main admin page        
        self.driver.find_element(By.CSS_SELECTOR,"input.oxd-input:nth-child(1)").send_keys(username)
        
    def click_search_button(self):
        # click the search button on the search form
        self.driver.find_element(By.CSS_SELECTOR,"button.oxd-button:nth-child(2)").click()
        
    def click_search_reset_button(self):
        # click on the reset button on the search form
        self.driver.find_element(By.CSS_SELECTOR,".oxd-button--ghost").click()
        
    def click_top_search_result_delete_button(self):
        # clicks the delete button on the first search result
        self.driver.find_element(By.CSS_SELECTOR,"button.oxd-table-cell-action-space:nth-child(1)").click()
        
    def click_confirm_delete_button(self):
        # clicks the "Yes, Delete" button on the delete user confirmation screen
        self.driver.find_element(By.CSS_SELECTOR,".oxd-button--label-danger").click()
    
    def search_and_wait(self, username):
        # enter the username into the search field, click search, and wait for the result
        self.enter_search_username(username)
        self.click_search_button()
        self.wait_for_search_result()
        
    def delete_top_search_result(self):
        # deletes the top search result
        # MAKE SURE TO VERIFY THE TOP SEARCH RESULT BEFORE DELETING!!
        
        self.click_top_search_result_delete_button()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".oxd-button--label-danger")))
        except TimeoutException:
            assert False, "Timed out waiting for delete confirmation button"
        
        self.click_confirm_delete_button()
        
    
    def verify_top_search_result(self, username, role, status):
        # verify that the top search result has the expected user data
        
        # find the text boxes
        search_username = self.driver.find_element(By.CSS_SELECTOR,"div.oxd-table-card:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)")
        search_role = self.driver.find_element(By.CSS_SELECTOR,"div.oxd-table-card:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)")
        search_status = self.driver.find_element(By.CSS_SELECTOR,"div.oxd-table-card:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1)")
        
        assert username == search_username.text, f"Test Fail, Wrong username found in search result! Expected '{username}' got '{search_username.text}'"
        assert role == search_role.text, f"Test Fail, Wrong role found in search result! Expected '{role}' got '{search_role.text}'"
        assert status == search_status.text, f"Test Fail, Wrong status found in search result! Expected '{status}' got '{search_status.text}'"

    def verify_reset_search_field(self):
        # verifies the search fields are properly reset
        
        # get all the search field elements
        search_username_input = self.driver.find_element(By.CSS_SELECTOR,"input.oxd-input:nth-child(1)")
        search_user_roll_dropdown = self.driver.find_element(By.CSS_SELECTOR,"div.oxd-grid-item:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
        search_employee_name_input = self.driver.find_element(By.CSS_SELECTOR,".oxd-autocomplete-text-input > input:nth-child(2)")
        search_status_dropdown = self.driver.find_element(By.CSS_SELECTOR,"div.oxd-grid-item:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
        
        # verify all elements are the default values
        assert "" == search_username_input.text, f"Test Fail, Wrong username found in search result! Expected '' got '{search_username_input.text}'"
        assert "-- Select --" == search_user_roll_dropdown.text, f"Test Fail, Wrong username found in search result! Expected '-- Select --' got '{search_user_roll_dropdown.text}'"
        assert "" == search_employee_name_input.text, f"Test Fail, Wrong username found in search result! Expected '' got '{search_employee_name_input.text}'"
        assert "-- Select --" == search_status_dropdown.text, f"Test Fail, Wrong username found in search result! Expected '-- Select --' got '{search_status_dropdown.text}'"
        
    def verify_no_search_result(self):
        # verifies there are no search results by reading the records found label 
        
        search_records_label = self.driver.find_element(By.CSS_SELECTOR,"span.oxd-text:nth-child(1)")        
        assert search_records_label.text == "No Records Found", f"Test Fail, found unexpected search records! Expected 'No Records Found' got '{search_records_label.text}'"

    def verify_admin_page(self):
        # Verify that current page is the Admin page
        if self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers":
            return True
        else:
            assert False, "Navigation Failed! Not on the Admin / User Management page." 
    
    def wait_for_search_result(self):
        # waits up to 10 seconds for the presense of the record found label
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"span.oxd-text:nth-child(1)")))
        except TimeoutException:
            assert False, "Timed out waiting for search result."
        
