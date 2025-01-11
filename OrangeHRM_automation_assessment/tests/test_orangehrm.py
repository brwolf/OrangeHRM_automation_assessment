import pytest
from selenium.webdriver.common.by import By
from tests.pages.login_page import LoginPage
from tests.pages.admin_page import AdminPage
from tests.pages.add_user_page import AddUserPage
from tests.connections import verify_user_in_api, verify_user_not_in_api, verify_user_in_sql_db, verify_user_not_in_sql_db



"""  
    1. Add a test user(ex: testUser1) with Admin role and status as enabled.

    2. Add a test user(ex: testUser2)  with ESS role and status as disabled.

    Validate if the users got added as expected and are being displayed using the “Search” button.
    Validate if the users info gets cleared when using the “Reset” button
    Delete the test user(ex: testUser2) with the ESS role and validate if the user got deleted in the front end as well as backend using SQL (please use any sample table data for this part of the exercise).
    Retrieve the user records using an API GET request and validate that the records received match with what is displayed on the user management screen. (You may assume what the API will look like, and include your assumption in the readme).
    Add a readme to explain the code execution workflow process and how to run the code locally.
    Please create the above code in the github repository and share the repository information. 
    """  

           


@pytest.mark.parametrize("username, role, status",[("test_admin_1","Admin", "Enabled"),("test_user_1","ESS","Disabled")])
def test_add_and_delete_user(chrome_browser, username, role, status):
    # paramatized to run the test twice, first with enabled admin user, second with disabled ess user
    # In a real test environment these would probably be populated from a config file

    # Add a user with the given data
    # Validate that it was added using the search function
    # Verfiy the user was added via API get (faked due to not actually having an API to test)
    # Verfiy the user was added to a SQL db (faked due to not actually having an SQL db to test)
    
    # Clear user info via the reset button
    # Validate that the info was cleared using in the UI
    
    # Delete the user
    # Validate that it was removed using the search function
    # Verfiy the user was deleted via API get (faked out due to not actually having an API to test)
    # Verfiy the user was deleted from a SQL db (faked out due to not actually having an SQL db to test)
    
    login_page = LoginPage(chrome_browser)
    admin_page = AdminPage(chrome_browser)
    add_user_page = AddUserPage(chrome_browser)
    
    # Login to the website
    login_page.login_flow("Admin","admin123")
    
    # Click on the Admin tab on the side panel and verify navigation
    admin_page.click_admin_page()
    admin_page.verify_admin_page()
    
    # Click the Add user button and verify navigation
    admin_page.click_add_user()    
    add_user_page.verify_add_user_panel()
    
    # Fill all the fields to add a user
    add_user_page.add_test_user(username, role, status)
    
    # Click the Save button
    add_user_page.click_save_button()
        
    # Wait for the user to finish being added
    # This takes a few seconds for the user to be added and the main admin page to fully load, the search results are the last thing to load so are a good proxy for the page finishing to load
    admin_page.wait_for_search_result()
    admin_page.verify_admin_page()
    
    # check the user was correctly added on the API backend
    verify_user_in_api(username, role, status)
    
    # check the user was correctly added to the SQL db
    verify_user_in_sql_db(username, role, status)
    
    # search for the user
    admin_page.search_and_wait(username)
    
    # verify the top search result
    admin_page.verify_top_search_result(username, role, status)
    
    # clear the search field with the reset button
    admin_page.click_search_reset_button()
    admin_page.wait_for_search_result()
    
    # verify the search fields are reset
    admin_page.verify_reset_search_field()
    
    # Delete the user
    admin_page.search_and_wait(username)
    admin_page.verify_top_search_result(username, role, status)
    admin_page.delete_top_search_result()
    
    # check the API backend to verify the user was correctly deleted
    verify_user_not_in_api(username)
    
    # check the SQL db to verify the user was correctly deleted
    verify_user_not_in_sql_db(username)
    
    # Verify the user is deleted with search
    admin_page.click_search_reset_button()
    admin_page.wait_for_search_result()
    admin_page.search_and_wait(username)
    admin_page.verify_no_search_result()
    
    
    
    
    