import json
#import requests # would be used to get data from the API that doesn't actually exist
#from mysql.connector import connect, Error # would be used to get data from SQL db that doesn't actually exist
import os, sys # used to get data from a local json to fake the API response


def get_user_data_api():
    # get a JSON from the (non-existant) API with userdata
    # I'm assuming the API just gives me a full list of the user_data in a JSON and not individual entries. 

    '''
    # Make a GET request to the API endpoint
    url = https://fakeendpoint.com
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
   
    # Check the response status code
    assert response.status_code == 200, f"Error: {response.status_code} trying to access API"
        
    return response.json()
    '''
    # Get values from JSON
	
    # Faked API with a local json file
    fake_api_fp = os.path.join(sys.path[0], 'fake_api.json')
    with open(fake_api_fp, 'r') as fake_api_file:
        user_data = json.load(fake_api_file)
    return user_data

def verify_user_in_api(username, role, status):
    # pulls userdata from the API and verifies that the test user is present
    
    user_data = get_user_data_api()
    
    if username in user_data:
        assert user_data[username]['role'] == role, f"Test Fail! Expected user {username} role: '{role}' got '{user_data[username]['role']}'"
        assert user_data[username]['status'] == status, f"Test Fail! Expected user {username} status: '{status}' got '{user_data[username]['status']}'"
    else:
        assert False, f"Test Fail! Expected user '{username}' not in API response"
        
 
def verify_user_not_in_api(username):
    # pulls userdata from the API and verifies that the test user is NOT present
    
    # this should probably be combined with verify_user_in_api by having it return False with the user is not present and calling it with "assert not verify_user_in_api" 
    # but this method is easier to fake
    
    # Modified to fake expected response
    '''
    user_data = get_user_data_api() 
	'''
    user_data = [] 
    
    assert username not in user_data, f"Test Fail! Expected user '{username}' present in API response after deletion"
    
def verify_user_in_sql_db(username, role, status):
    # this is entirely untested
    
    # Modified to fake expected response
    '''
    response = None:
    try:
        with connect(host="fakeMySQLdb",user="username",password="password",database="fakeOrangeHRM") as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT username, role, status WHERE username = {username}")
                response = cursor.fetchone()
    except Error as e:
        assert False, f"Failed to connect to SQL DB with error: {e}"
    '''
    
    # Fake the response with the expected data and in the same format that the DB would present
    response  = (username, role, status)
    if response == None:
        assert False, f"Test Fail! SQL db does not contain username: {username}"
    else:
        assert response[1] == role, f"Test Fail! Expected user {username} role: '{role}' got '{response[1]}'"
        assert response[2] == status, f"Test Fail! Expected user {username} status: '{status}' got '{response[2]}'"
        
def verify_user_not_in_sql_db(username):
    # this is entirely untested
    
    # this should probably be combined with verify_user_in_sql_db by having it return False with the user is not present and calling it with "assert not verify_user_in_sql_db" 
    # but this method is easier to fake
    
    
    # Modified to fake expected response
    '''
    response = None:
    try:
        with connect(host="fakeMySQLdb",user="username",password="password",database="fakeOrangeHRM") as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT username, role, status WHERE username = {username}")
                response = cursor.fetchone()
    except Error as e:
        assert False, f"Failed to connect to SQL DB with error: {e}"
    '''
    
    # Fake the response with the expected data and in the same format that the DB would present
    response  = None
    
    assert response == None, f"Test Fail! SQL db unexpectedly contains username: {username}"