# OrangeHRM_automation_assessment
Coding assessment for automatted testing of the OrangeHRM website



How to run locally: 
1. Download the full project folder
2. pip install requirements.txt
3. Download and install the latest Chrome testing version and make sure it's in your PATH. 
	Download from https://googlechromelabs.github.io/chrome-for-testing/
	Tested with Version 131.0.6778.204 but any recent version should work.
4. From the OrangeHRM_automation_assessment folder run:
	> pytest
	
	
Code workflow overview:

This project is split across several files: 

test_orangehrm.py: Contains the test case to be run
connections.py: Contains functions for communicating with the (faked) backend API and SQL dbs
conftest.py: Defines the chrome_browser fixture
pages.login_page.py: A class for handeling interactions with the initial login page of OrangeHRM
pages.admin_page.py: A class for handeling interactions with the main admin page
pages.add_user_page.py: A class for handeling interactions with the add user page


Basic code execution overview: 
From the initial assessment prompt I created a single test case test_add_and_delete_user that is paramaterized to run twice with two different users. test_admin_1 as an Enabled, Admin user and test_user_1 as a Disabled ESS user. 

The test case starts by loging in with the default admin credentials. 
It then navigates to the add user screen, enters all the required information and adds the user to the website. 
The test waits for the admin page to fully load before checking that the user was added via the search UI, an API get call (faked with a local JSON file), and a query to an SQL db (faked with hard coded responses). 

Once the user has been confirmed to be added, the test case will reset the search field and verify that it's reset. (requirement from the prompt)

Once the search results have been reset the test will delete the user via the UI and confirm it's been deleted via the search UI, an API get call (faked with a local JSON file), and a query to an SQL db 

Notes on implementation choices: 
I hardcoded all the usernames and passcodes in the project for the sake of simplicity. This is generally bad practice and they should probably be stored in a seperate file. 
The test can potentially fail with a timeout error when creating the user if the username is already in use. In production I would add some better error handleing here, but it's beyond the scope of this project. 
The project makes extensive use of CSS_SELECTORS to find elements on the site. While they are more reliable than XPATH, the test is still fairly fragile to changes in layout. In a production setting I would be requesting the Dev team take some time and add identifiers to most of these elements to improve reliablility and readablility. 
The OrangeHRM site uses a few non-standard dynamic elements in the add user page. My handling of them works for now, but is very fragile to site changes. A better solution would probably be checking the text of the elements rather than blindly clicking via CSS_SELECTORS, but while I was implemeting this someone kept changing various parts of the site to Mandarin rendering a text based method unreliable. 
Verifying the search reset button works should probably be a seperate test case, but I interpreted the prompt as requireing it to be done after verifing the user was created. 
